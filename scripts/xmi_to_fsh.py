#!/usr/bin/env python3
"""Convert Visual Paradigm XMI exports into FSH logical model definitions.

Each *.xmi file in the input directory becomes one *.fsh file. Every
uml:Class found in the file becomes a `Logical:` definition. The class
flagged as the root (Visual Paradigm's "Root" checkbox, exported as
<isRoot xmi:value="true"/>) is treated as the logical-model profile for
that file; any other classes it depends on are emitted alongside it as
supporting logical types so the FSH is self-contained.
"""
from __future__ import annotations

import argparse
import re
import sys
import unicodedata
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from pathlib import Path

UML_NS = "http://schema.omg.org/spec/UML/2.0"
XMI_NS = "http://schema.omg.org/spec/XMI/2.1"


def xmi_attr(el: ET.Element, name: str) -> str | None:
    return el.get(f"{{{XMI_NS}}}{name}")


# Words that must not be used verbatim as FSH/logical-model element names:
# real FSH grammar keywords, plus the attributes every Logical model already
# inherits from the "Base"/"Element" type. Attributes with one of these
# names are prefixed with "_" (e.g. "id" -> "_id").
RESERVED_NAMES = {
    "alias", "codesystem", "extension", "instance", "instanceof",
    "invariant", "logical", "mapping", "profile", "resource", "ruleset",
    "valueset", "and", "or", "contains", "from", "only", "obeys", "insert",
    "named", "exclude", "include", "codes", "true", "false", "description",
    "expression", "xpath", "severity", "id", "title", "usage", "source",
    "target", "context", "characteristics", "parent",
    "modifierextension",
}

# Visual Paradigm / generic UML type name -> FHIR type.
PRIMITIVE_TYPE_MAP = {
    "string": "string", "str": "string", "text": "string",
    "boolean": "boolean", "bool": "boolean",
    "integer": "integer", "int": "integer",
    "decimal": "decimal", "float": "decimal", "double": "decimal", "number": "decimal",
    "date": "date", "datetime": "dateTime", "timestamp": "dateTime",
    "time": "time", "instant": "instant",
    "uri": "uri", "url": "url", "canonical": "canonical",
    "oid": "oid", "uuid": "uuid", "id": "id", "code": "code",
    "markdown": "markdown", "base64binary": "base64Binary", "base64": "base64Binary",
    "unsignedint": "unsignedInt", "positiveint": "positiveInt",
    "xhtml": "xhtml", "any": "string",
}

# FHIR types that are already spelled correctly and should pass through as-is.
KNOWN_FHIR_TYPES = {
    "string", "boolean", "integer", "decimal", "date", "dateTime", "time",
    "instant", "uri", "url", "canonical", "oid", "uuid", "id", "code",
    "markdown", "base64Binary", "unsignedInt", "positiveInt", "xhtml",
    "Coding", "CodeableConcept", "Quantity", "Range", "Ratio", "Period",
    "Identifier", "HumanName", "Address", "ContactPoint", "Attachment",
    "Annotation", "Money", "Reference",
}


def strip_diacritics(text: str) -> str:
    normalized = unicodedata.normalize("NFKD", text)
    return "".join(ch for ch in normalized if not unicodedata.combining(ch))


def slug_id(name: str, used: set[str], fallback: str = "unnamed") -> str:
    """Sanitize into a valid, unique FHIR id: [A-Za-z0-9\\-.]{1,64}"""
    ascii_name = strip_diacritics(name or "")
    ascii_name = re.sub(r"[^A-Za-z0-9.\-]+", "-", ascii_name).strip("-.")
    ascii_name = ascii_name or fallback
    ascii_name = ascii_name[:55]  # leave room for a dedup suffix
    candidate = ascii_name
    n = 2
    while candidate.lower() in used:
        candidate = f"{ascii_name}-{n}"
        n += 1
    used.add(candidate.lower())
    return candidate


def sanitize_field_name(name: str) -> str:
    """FHIR element names must be simple alphanumerics (invariant eld-20) —
    no underscores, hyphens, spaces, etc. Multi-word names (e.g. from a
    Swedish attribute/role name with spaces) are joined into camelCase
    instead of being underscore-separated, so `är ansvarig för` becomes
    `arAnsvarigFor` rather than the invalid `ar_ansvarig_for`. A name
    that's already a single alphanumeric token is left untouched."""
    ascii_name = strip_diacritics(name or "")
    words = re.findall(r"[A-Za-z0-9]+", ascii_name)
    if not words:
        return "field"
    result = words[0]
    for word in words[1:]:
        result += word[0].upper() + word[1:]
    if result[0].isdigit():
        result = f"f{result}"
    return result


def escape_fsh_string(text: str) -> str:
    return text.replace("\\", "\\\\").replace('"', '\\"')


def normalize_cardinality_bound(value: str | None, default: str) -> str:
    if value is None or value == "":
        return default
    if value in ("*", "-1"):
        return "*"
    return value


@dataclass
class Attribute:
    original_name: str
    field_name: str
    renamed_reserved: bool
    lower: str
    upper: str
    type_name: str
    is_complex: bool
    unresolved_type: bool = False
    source_id: str | None = None


@dataclass
class LogicalClass:
    xmi_id: str
    name: str
    is_root: bool
    attributes: list[Attribute] = field(default_factory=list)
    fsh_id: str | None = None
    fsh_name: str | None = None


@dataclass
class InstanceSpec:
    xmi_id: str
    name: str
    classifier_id: str | None
    slots: list[tuple[str, str]]  # (definingFeature xmi:id, value text)


class ConversionWarning(Exception):
    pass


def find_isroot(class_el: ET.Element) -> bool:
    for ext in class_el.findall("xmi:Extension", {"xmi": XMI_NS}):
        is_root_el = ext.find("isRoot")
        if is_root_el is not None and is_root_el.get(f"{{{XMI_NS}}}value") == "true":
            return True
    return False


def is_element_type(el: ET.Element, *type_names: str) -> bool:
    return xmi_attr(el, "type") in type_names


def parse_instance_spec(el: ET.Element) -> InstanceSpec:
    xid = xmi_attr(el, "id") or ""
    classifier_el = el.find("classifier")
    classifier_id = xmi_attr(classifier_el, "idref") if classifier_el is not None else None
    slots: list[tuple[str, str]] = []
    for slot_el in el.findall("slot"):
        defining_feature = slot_el.get("definingFeature")
        value_el = slot_el.find("value")
        if not defining_feature or value_el is None:
            continue
        value_text = value_el.get("body")
        if value_text is None:
            continue
        slots.append((defining_feature, value_text))
    return InstanceSpec(
        xmi_id=xid,
        name=el.get("name") or xid,
        classifier_id=classifier_id,
        slots=slots,
    )


def build_registry(root: ET.Element):
    """Walk the whole document once, indexing classes/datatypes/enumerations,
    associations and instance specifications (object-diagram instances) by
    xmi:id, regardless of how deeply they're nested (Visual Paradigm nests
    classes inside packages and inside each other)."""
    classes: dict[str, LogicalClass] = {}
    type_name: dict[str, str] = {}  # xmi:id -> raw UML type/enumeration name
    associations: list[ET.Element] = []
    instance_specs: list[InstanceSpec] = []

    for el in root.iter():
        if is_element_type(el, "uml:Class"):
            xid = xmi_attr(el, "id")
            if not xid:
                continue
            classes[xid] = LogicalClass(
                xmi_id=xid,
                name=el.get("name") or xid,
                is_root=find_isroot(el),
            )
        elif is_element_type(el, "uml:DataType", "uml:PrimitiveType", "uml:Enumeration"):
            xid = xmi_attr(el, "id")
            if xid:
                type_name[xid] = el.get("name") or xid
        elif is_element_type(el, "uml:Association"):
            associations.append(el)
        elif is_element_type(el, "uml:InstanceSpecification"):
            instance_specs.append(parse_instance_spec(el))

    return classes, type_name, associations, instance_specs


def assign_fsh_names(classes: dict[str, LogicalClass], name_registry: set[str]) -> None:
    """Compute a unique, FSH-safe identifier for every class up front, so
    both the `Logical:` declaration and any `* attr card TypeName` rules
    that reference it agree on the same name. `name_registry` is shared
    across all files processed in this run, since Logical model names must
    be unique across the whole IG."""
    for cls in classes.values():
        name = re.sub(r"[^A-Za-z0-9]", "", strip_diacritics(cls.name)) or "Model"
        if name[0].isdigit():
            name = f"M{name}"
        candidate = name
        n = 2
        while candidate.lower() in name_registry:
            candidate = f"{name}{n}"
            n += 1
        name_registry.add(candidate.lower())
        cls.fsh_name = candidate


def resolve_type(type_id: str | None, classes: dict[str, LogicalClass],
                  type_name: dict[str, str], warnings: list[str],
                  context: str) -> tuple[str, bool, bool]:
    """Returns (fsh_type_name, is_complex_class_reference, unresolved)."""
    if type_id and type_id in classes:
        return classes[type_id].fsh_name, True, False
    if type_id and type_id in type_name:
        raw = type_name[type_id]
        mapped = PRIMITIVE_TYPE_MAP.get(raw.lower())
        if mapped:
            return mapped, False, False
        if raw in KNOWN_FHIR_TYPES:
            return raw, False, False
        warnings.append(
            f"{context}: unrecognized data type '{raw}', defaulting to 'string'"
        )
        return "string", False, False
    warnings.append(
        f"{context}: attribute type could not be resolved (dangling/missing "
        f"reference '{type_id}'), defaulting to 'string'"
    )
    return "string", False, True


def make_attribute(raw_name: str | None, type_id: str | None, lower_el, upper_el,
                    classes, type_name, warnings, context,
                    default_lower="0", default_upper="1",
                    source_id: str | None = None) -> Attribute:
    original_name = raw_name or "field"
    field_name = sanitize_field_name(original_name)
    renamed = False
    if field_name.lower() in RESERVED_NAMES:
        field_name = f"_{field_name}"
        renamed = True

    lower = normalize_cardinality_bound(
        lower_el.get("value") if lower_el is not None else None, default_lower)
    upper = normalize_cardinality_bound(
        upper_el.get("value") if upper_el is not None else None, default_upper)

    type_fsh, is_complex, unresolved = resolve_type(
        type_id, classes, type_name, warnings,
        f"{context}.{original_name}")

    return Attribute(
        original_name=original_name,
        field_name=field_name,
        renamed_reserved=renamed,
        lower=lower,
        upper=upper,
        type_name=type_fsh,
        is_complex=is_complex,
        unresolved_type=unresolved,
        source_id=source_id,
    )


def collect_class_attributes(class_el: ET.Element, cls: LogicalClass, classes,
                              type_name, warnings):
    for attr_el in class_el.findall("ownedAttribute"):
        if not is_element_type(attr_el, "uml:Property"):
            continue
        attr = make_attribute(
            attr_el.get("name"),
            attr_el.get("type"),
            attr_el.find("lowerValue"),
            attr_el.find("upperValue"),
            classes, type_name, warnings,
            context=cls.name,
            source_id=xmi_attr(attr_el, "id"),
        )
        cls.attributes.append(attr)


def existing_field_names(cls: LogicalClass) -> set[str]:
    return {a.field_name.lower() for a in cls.attributes}


def apply_associations(associations: list[ET.Element], classes: dict[str, LogicalClass],
                        warnings):
    """Best-effort: Visual Paradigm associations are frequently exported
    without role names on either end. We synthesize an attribute on each
    navigable side, named after the role (if present) or the association's
    own name/target class as a fallback. This is a heuristic — if the
    source model has explicit association role names, those are always
    preferred and this produces exact results."""
    for assoc in associations:
        ends = [e for e in assoc.findall("ownedEnd") if is_element_type(e, "uml:Property")]
        if len(ends) != 2:
            continue
        assoc_name = assoc.get("name") or ""
        end_a, end_b = ends

        for owner_end, target_end in ((end_a, end_b), (end_b, end_a)):
            if target_end.get("isNavigable") != "true":
                continue
            owner_type_id = owner_end.get("type")
            owner_cls = classes.get(owner_type_id)
            if owner_cls is None:
                continue
            target_type_id = target_end.get("type")
            target_cls = classes.get(target_type_id)
            if target_cls is None:
                continue

            raw_name = (target_end.get("name") or assoc_name
                        or target_cls.name).strip()
            base_field = sanitize_field_name(raw_name)
            candidate = base_field
            existing = existing_field_names(owner_cls)
            n = 2
            while candidate.lower() in existing:
                candidate = f"{base_field}{n}"
                n += 1

            renamed = False
            if candidate.lower() in RESERVED_NAMES:
                candidate = f"_{candidate}"
                renamed = True

            lower = normalize_cardinality_bound(
                (target_end.find("lowerValue").get("value")
                 if target_end.find("lowerValue") is not None else None), "0")
            upper = normalize_cardinality_bound(
                (target_end.find("upperValue").get("value")
                 if target_end.find("upperValue") is not None else None), "1")

            owner_cls.attributes.append(Attribute(
                original_name=raw_name,
                field_name=candidate,
                renamed_reserved=renamed,
                lower=lower,
                upper=upper,
                type_name=target_cls.fsh_name,
                is_complex=True,
                source_id=xmi_attr(target_end, "id"),
            ))
            warnings.append(
                f"{owner_cls.name}: synthesized attribute '{candidate}' -> "
                f"{target_cls.name} from association "
                f"'{assoc_name or '(unnamed)'}' (best-effort, no explicit "
                f"role name in source model)"
            )


def render_class_fsh(cls: LogicalClass, is_root: bool, source_file: str,
                      id_registry: set[str]) -> str:
    fsh_id = slug_id(cls.name, id_registry)
    cls.fsh_id = fsh_id
    role = "Root logical model" if is_root else "Supporting logical model"
    lines = [f"Logical: {cls.fsh_name}"]
    lines.append(f"Id: {fsh_id}")
    lines.append(f'Title: "{escape_fsh_string(cls.name)}"')
    lines.append(
        f'Description: "{role} generated from {escape_fsh_string(source_file)} '
        f'(source class: {escape_fsh_string(cls.name)})."'
    )
    lines.append("Parent: Base")
    lines.append("Characteristics: #can-be-target")
    if not cls.attributes:
        lines.append("// (no attributes found on this class in the source XMI)")
    for attr in cls.attributes:
        short_bits = [f"Source attribute: {attr.original_name}"]
        if attr.renamed_reserved:
            short_bits.append(
                f"renamed from reserved FSH name '{attr.original_name}'")
        if attr.unresolved_type:
            short_bits.append("type could not be resolved from source model")
        short = escape_fsh_string("; ".join(short_bits))
        lines.append(
            f'* {attr.field_name} {attr.lower}..{attr.upper} '
            f'{attr.type_name} "{short}"'
        )
    return "\n".join(lines) + "\n"


def build_attribute_index(classes: dict[str, LogicalClass]
                           ) -> dict[str, tuple[LogicalClass, Attribute]]:
    """Maps a source ownedAttribute/association-end xmi:id to the class that
    owns it and the Attribute we generated for it, so InstanceSpecification
    slots (which reference that same xmi:id via `definingFeature`) can be
    matched back to a FSH element name."""
    index: dict[str, tuple[LogicalClass, Attribute]] = {}
    for cls in classes.values():
        for attr in cls.attributes:
            if attr.source_id:
                index[attr.source_id] = (cls, attr)
    return index


def format_instance_value(value_text: str, type_name: str) -> str:
    text = value_text.strip()
    if type_name == "boolean" and text.lower() in ("true", "false"):
        return text.lower()
    if type_name in ("integer", "unsignedInt", "positiveInt") and re.fullmatch(r"-?\d+", text):
        return text
    if type_name == "decimal":
        try:
            float(text)
            return text
        except ValueError:
            pass
    return f'"{escape_fsh_string(value_text)}"'


def render_instances(instance_specs: list[InstanceSpec], classes: dict[str, LogicalClass],
                      attr_index: dict[str, tuple[LogicalClass, Attribute]],
                      instance_name_registry: set[str],
                      warnings: list[str], source_file: str) -> list[str]:
    """Best-effort: converts each uml:InstanceSpecification (an object in one
    of the source model's object diagrams) into a FSH Instance of the
    corresponding Logical model. Slot values are copied through as-is —
    some object diagrams use real example data, others use descriptive
    placeholder text (e.g. "{comment} [0..1]"), and this does not try to
    tell them apart.

    Object diagrams are inherently partial sketches: they rarely set every
    required (min cardinality >= 1) attribute of the class they instantiate,
    which SUSHI rejects for `Usage: #example` instances. So an instance is
    only marked #example (a standalone, browsable example in the built IG)
    when every one of its class's required attributes got a value from a
    slot; otherwise it's marked #inline (still compiled and included in the
    FHIR package, just not validated or published as its own example page)."""
    out: list[str] = []
    for spec in instance_specs:
        cls = classes.get(spec.classifier_id) if spec.classifier_id else None
        if cls is None:
            warnings.append(
                f"{spec.name}: skipped example instance — classifier "
                f"'{spec.classifier_id}' not found among converted classes"
            )
            continue

        inst_name = re.sub(r"[^A-Za-z0-9]", "", strip_diacritics(spec.name)) or "Example"
        if inst_name[0].isdigit():
            inst_name = f"Example{inst_name}"
        candidate = inst_name
        n = 2
        while candidate.lower() in instance_name_registry:
            candidate = f"{inst_name}{n}"
            n += 1
        instance_name_registry.add(candidate.lower())

        rules: list[str] = []
        covered_source_ids: set[str] = set()
        for defining_feature, value_text in spec.slots:
            found = attr_index.get(defining_feature)
            if found is None:
                warnings.append(
                    f"{spec.name}: skipped a slot — its attribute could not "
                    f"be matched back to '{cls.name}'"
                )
                continue
            _, attr = found
            if attr.is_complex:
                warnings.append(
                    f"{spec.name}.{attr.field_name}: skipped — value is a "
                    f"complex/reference type, only primitive slot values are "
                    f"converted automatically"
                )
                continue
            rules.append(
                f"* {attr.field_name} = {format_instance_value(value_text, attr.type_name)}"
            )
            covered_source_ids.add(attr.source_id)

        is_complete = all(
            attr.lower == "0" or attr.source_id in covered_source_ids
            for attr in cls.attributes
        )
        usage = "#example" if is_complete else "#inline"
        if not is_complete:
            warnings.append(
                f"{spec.name}: marked Usage: #inline instead of #example — "
                f"this object diagram doesn't set every required attribute "
                f"of '{cls.name}', so SUSHI would reject it as an example"
            )

        lines = [f"Instance: {candidate}"]
        lines.append(f"InstanceOf: {cls.fsh_name}")
        lines.append(f'Title: "{escape_fsh_string(spec.name)}"')
        lines.append(f"Usage: {usage}")
        role = "Example" if is_complete else "Partial example (illustrative only)"
        lines.append(
            f'Description: "{role} instance generated from an object diagram '
            f'in {escape_fsh_string(source_file)}."'
        )
        lines.extend(rules)
        if not rules:
            lines.append("// (no slot values could be mapped to attributes)")
        out.append("\n".join(lines) + "\n")
    return out


def convert_file(xmi_path: Path, out_dir: Path, id_registry: set[str],
                  name_registry: set[str], instance_name_registry: set[str]) -> list[str]:
    warnings: list[str] = []
    try:
        tree = ET.parse(xmi_path)
    except ET.ParseError as exc:
        raise ConversionWarning(f"{xmi_path.name}: could not parse XML ({exc})")

    root = tree.getroot()
    classes, type_name, associations, instance_specs = build_registry(root)

    if not classes:
        raise ConversionWarning(f"{xmi_path.name}: no uml:Class elements found")

    assign_fsh_names(classes, name_registry)

    for el in root.iter():
        if is_element_type(el, "uml:Class"):
            xid = xmi_attr(el, "id")
            if xid in classes:
                collect_class_attributes(el, classes[xid], classes, type_name,
                                          warnings)

    apply_associations(associations, classes, warnings)

    roots = [c for c in classes.values() if c.is_root]
    if len(roots) == 0:
        # Best-effort fallback: prefer a class that nothing else points to.
        referenced = {a.type_name for c in classes.values() for a in c.attributes
                      if a.is_complex}
        candidates = [c for c in classes.values() if c.fsh_name not in referenced]
        root_cls = candidates[0] if len(candidates) == 1 else next(iter(classes.values()))
        warnings.append(
            f"{xmi_path.name}: no class flagged as root (isRoot=true); "
            f"defaulting to '{root_cls.name}'. Mark a class as Root in "
            f"Visual Paradigm to control this."
        )
        roots = [root_cls]
    elif len(roots) > 1:
        names = ", ".join(c.name for c in roots)
        warnings.append(
            f"{xmi_path.name}: multiple classes flagged as root ({names}); "
            f"using '{roots[0].name}'."
        )
        roots = [roots[0]]

    root_cls = roots[0]
    ordered = [root_cls] + [c for c in classes.values() if c is not root_cls]

    out_parts = [
        f"// Generated automatically from {xmi_path.name} — do not edit by hand.\n"
        f"// Re-run scripts/xmi_to_fsh.py to regenerate.\n"
    ]
    for cls in ordered:
        out_parts.append(render_class_fsh(cls, cls is root_cls, xmi_path.name,
                                           id_registry))

    instance_count = 0
    if instance_specs:
        attr_index = build_attribute_index(classes)
        instance_blocks = render_instances(
            instance_specs, classes, attr_index,
            instance_name_registry, warnings,
            xmi_path.name,
        )
        out_parts.extend(instance_blocks)
        instance_count = len(instance_blocks)

    out_dir.mkdir(parents=True, exist_ok=True)
    out_name = re.sub(r"[^A-Za-z0-9.\-]+", "_", xmi_path.stem) + ".fsh"
    out_path = out_dir / out_name
    out_path.write_text("\n".join(out_parts), encoding="utf-8")

    print(f"[ok] {xmi_path.name} -> {out_path} "
          f"({len(classes)} class(es), {instance_count} example instance(s), "
          f"root: {root_cls.name})")
    for w in warnings:
        print(f"  [warn] {w}")
    return warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", default="xmi-input",
                         help="Directory containing *.xmi files")
    parser.add_argument("--output", default="input/fsh/models",
                         help="Directory to write generated *.fsh files into")
    args = parser.parse_args()

    in_dir = Path(args.input)
    out_dir = Path(args.output)

    if not in_dir.is_dir():
        print(f"error: input directory '{in_dir}' does not exist", file=sys.stderr)
        return 1

    xmi_files = sorted(in_dir.glob("*.xmi"))
    if not xmi_files:
        print(f"error: no .xmi files found in '{in_dir}'", file=sys.stderr)
        return 1

    if out_dir.is_dir():
        for old in out_dir.glob("*.fsh"):
            old.unlink()

    id_registry: set[str] = set()
    name_registry: set[str] = set()
    instance_name_registry: set[str] = set()
    total_warnings = 0
    failed = False
    for xmi_path in xmi_files:
        try:
            warnings = convert_file(xmi_path, out_dir, id_registry, name_registry,
                                     instance_name_registry)
            total_warnings += len(warnings)
        except ConversionWarning as exc:
            print(f"[error] {exc}", file=sys.stderr)
            failed = True

    print(f"\nDone: {len(xmi_files)} file(s) processed, "
          f"{total_warnings} warning(s).")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
