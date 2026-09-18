# xmi-to-fsh

Turns Visual Paradigm XMI exports into FHIR Implementation Guides of
logical models, built and published automatically by GitHub Actions.
**Every XMI file becomes its own, independent IG, named after the file.**

## Using it day to day

1. **Add or update XMI files.** Export your model(s) from Visual Paradigm
   as `.xmi` and drop them into [`xmi-input/`](xmi-input) (any filename,
   any number of files — one IG comes out per file). Commit and push —
   either directly to `main` or via a pull request.
   - In each file, mark exactly one class as **Root** in Visual Paradigm
     (this exports as `<isRoot xmi:value="true"/>`). That class becomes
     the logical model the file's IG represents; every other class it
     depends on comes along as a supporting type in the same IG.
   - If you open a PR, GitHub Actions extracts and validates every IG's
     FSH automatically — check the PR's checks before merging.
2. **Merge to `main`.** This triggers the full pipeline: extraction,
   validation, and an IG Publisher build for every IG, ending with all of
   them pushed to the `gh-pages` branch.
3. **Get the built IGs.** Once GitHub Pages is turned on for this repo
   (**Settings → Pages → Source: Deploy from a branch → `gh-pages` → `/`
   (root)** — a one-time setup), a landing page listing every IG is
   published at `https://<owner>.github.io/<repo>/`, and each IG itself
   at `https://<owner>.github.io/<repo>/<slug>/` (`<slug>` is the XMI
   filename, lowercased — `Test1.xmi` → `test1/`). Both update
   automatically on every push to `main`. You can also download all the
   sites, or the FHIR packages, as a build artifact from the `build-ig`
   job of any workflow run, without waiting for Pages.
4. **If something fails**, read the failing job's log first — it names
   which IG failed, and the converter prints a warning for every
   attribute, association, or instance it couldn't confidently convert
   (see below), which is usually enough to tell whether it's a real bug
   or something to adjust in the source model (e.g. adding an explicit
   association role name).

## How the conversion works

Everything happens in [`scripts/xmi_to_fsh.py`](scripts/xmi_to_fsh.py),
which parses each XMI file directly (no Visual Paradigm needed) and
writes a complete, self-contained IG project per file under
`igs/<slug>/` — its own `sushi-config.yaml`, `ig.ini`, generated FSH, and
a starter `input/pagecontent/index.md`. Nothing is shared between IGs:
each file's classes, ids, and names live in their own namespace, so two
files can reuse the same class name without colliding.

- **Classes → Logical models.** Every `uml:Class` becomes a FSH
  `Logical:` definition (`Parent: Base`) inside that file's IG. The class
  flagged **Root** becomes the profile representing the IG; the rest are
  emitted alongside it as supporting types, since FSH needs every
  referenced type defined somewhere. If no class is flagged root, the
  converter guesses (prefers a class nothing else points to) and logs a
  warning — mark a root explicitly in Visual Paradigm to control this.
- **Attributes → cardinality + type rules.** `lowerValue`/`upperValue`
  become the FSH cardinality (`0..1`, `1..*`, etc.), defaulting to `0..1`
  when absent, matching UML's own default. The attribute's UML type is
  mapped to a FHIR primitive (`string`, `integer`, `dateTime`, …) when
  recognized, or to another Logical model when it points at a class in
  the same file; an unresolvable type falls back to `string` with a
  warning.
- **Reserved names.** An attribute named `id`, `extension`, or any real
  FSH keyword (`from`, `and`, `obeys`, …) would collide with FSH syntax
  or with elements every Logical model already inherits, so it's renamed
  with a leading underscore (`id` → `_id`). The original name is kept in
  the element's short description.
- **Associations (best-effort).** A relationship modeled as a UML
  association rather than a plain attribute is converted into an
  attribute on each navigable side. Visual Paradigm often exports these
  without role names, so the generated field name falls back to the
  association's own name or the target class's name — check the build
  log for `synthesized attribute` warnings and add explicit role names
  in Visual Paradigm if the generated names read oddly.
- **Object diagrams → example instances.** A `uml:InstanceSpecification`
  (an object in one of the model's object diagrams) becomes a FSH
  `Instance:` of the class it's an instance of, with its slots copied
  over as `* field = value` rules. Object diagrams are usually partial
  sketches that don't set every required attribute of their class, and
  FHIR/SUSHI rejects an incomplete instance — so only instances that
  *do* set every required attribute become real, validated, browsable
  `Usage: #example` instances; the rest are written out as FSH comments
  instead (visible in the source, harmless to validation, not published
  as their own example page).
- **Documentation → descriptions/definitions.** When a class or
  attribute has free-text documentation in Visual Paradigm (an
  `ownedComment`), it becomes the Logical model's `Description:` (for a
  class) or a `* field ^definition = "..."` rule (for an attribute).
  Without documentation, a generic auto-generated description is used
  instead.

Every warning the script prints is informational, not fatal — a file
only fails (and blocks CI for its IG) if it has no classes at all or
genuinely can't be parsed as XML; other files still succeed.

## Repository layout

```
xmi-input/              Source XMI files exported from Visual Paradigm — edit these
scripts/xmi_to_fsh.py   The XMI -> FSH converter (one IG project per file)
scripts/validate_all_igs.sh   Runs `sushi build .` in every igs/<slug>/ (used by CI)
scripts/build_all_igs.sh      Runs SUSHI + the IG Publisher in every igs/<slug>/,
                               collecting output into site/<slug>/ (used by CI)
igs/<slug>/             One full IG project per XMI file (gitignored, rebuilt by CI):
  sushi-config.yaml       SUSHI / IG Publisher configuration for this IG
  ig.ini                  IG Publisher entry point for this IG
  input/fsh/models/       Generated FSH
  input/pagecontent/      Generated starter narrative page
.github/workflows/      The two-step CI pipeline
```

`igs/<slug>/input/` is the HL7 IG Publisher's own reserved project folder
per IG (FSH sources, page content, etc.), which is why the raw XMI files
live in the separate top-level `xmi-input/` folder instead.

## CI pipeline

[`.github/workflows/ig-build.yml`](.github/workflows/ig-build.yml) runs
two gated jobs on every push and pull request to `main`:

1. **`extract-and-validate`** — runs the conversion script (producing
   `igs/<slug>/` for every XMI file), then `scripts/validate_all_igs.sh`
   to `sushi build .` each one and compile+validate its FSH. Fails the
   whole workflow if any IG's FSH doesn't compile, so `build-ig` never
   runs on broken output.
2. **`build-ig`** — only runs if validation passed. Downloads the
   validated IGs, then `scripts/build_all_igs.sh` runs SUSHI again to
   produce each IG's FHIR resources, then the official HL7 FHIR IG
   Publisher to build its complete site, collecting every IG's site into
   `site/<slug>/` plus a `site/index.html` landing page linking to all of
   them. On a push to `main` (not on pull requests), `site/` is pushed to
   the `gh-pages` branch via `peaceiris/actions-gh-pages` — this needs
   the `contents: write` permission the workflow already grants itself
   for that job.

## Running locally

```sh
npm install
python3 scripts/xmi_to_fsh.py --input xmi-input --output-root igs
SUSHI_CMD="npx sushi" bash scripts/validate_all_igs.sh   # validate every IG's FSH

# optional, requires Java 17+ and Ruby+Jekyll, and downloads the IG Publisher jar:
curl -fL -o publisher.jar https://github.com/HL7/fhir-ig-publisher/releases/latest/download/publisher.jar
npm install -g fsh-sushi@$(node -p "require('./package.json').devDependencies['fsh-sushi']")
SUSHI_CMD=sushi PUBLISHER_JAR="$PWD/publisher.jar" bash scripts/build_all_igs.sh
# built sites land in site/<slug>/, with site/index.html linking to all of them
```

## Before publishing for real

Each generated `igs/<slug>/sushi-config.yaml` uses a placeholder
canonical URL (`http://example.org/fhir/<slug>` by default) and a
placeholder publisher — pass `--canonical-base`, `--publisher-name`, and
`--publisher-url` to `scripts/xmi_to_fsh.py` (or edit the CI workflow's
invocation of it) to point these at your organization's own before
treating the published sites as anything but a CI preview.
