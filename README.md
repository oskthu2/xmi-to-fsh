# xmi-to-fsh

Turns Visual Paradigm XMI exports into a FHIR Implementation Guide of
logical models, built and published automatically by GitHub Actions.

## How it works

1. Drop `.xmi` files exported from Visual Paradigm into [`xmi-input/`](xmi-input).
2. [`scripts/xmi_to_fsh.py`](scripts/xmi_to_fsh.py) converts every file into
   one FSH file under `input/fsh/models/` (generated, not committed):
   - Every `uml:Class` in the file becomes a FSH `Logical:` model.
   - The class marked **Root** in Visual Paradigm (exported as
     `<isRoot xmi:value="true"/>`) becomes the profile that represents the
     file; every other class it depends on is emitted alongside it so the
     FSH is self-contained.
   - Attribute data types and cardinalities (`lowerValue`/`upperValue`) are
     carried over as FSH cardinality/type rules.
   - Attribute names that collide with FSH keywords or with elements every
     logical model already inherits (e.g. `id`, `extension`) are renamed
     with a leading underscore (`id` -> `_id`); the original name is kept
     in the element's short description.
   - Relationships modeled as UML associations (rather than as attributes)
     are converted on a best-effort basis, since Visual Paradigm often
     exports these without role names — check the build log for
     `synthesized attribute` warnings and consider adding explicit role
     names in Visual Paradigm if the generated names aren't right.
3. GitHub Actions ([`.github/workflows/ig-build.yml`](.github/workflows/ig-build.yml))
   runs this in two gated steps on every push/PR to `main`:
   - **`extract-and-validate`** — runs the conversion script, then
     `sushi build .` to compile and validate the generated FSH. This step
     fails the whole workflow if the FSH doesn't compile.
   - **`build-ig`** — only runs if validation passed. Downloads the
     validated FSH, then runs the official HL7 FHIR IG Publisher to build
     the complete IG website (profiles, narrative pages from
     `input/pagecontent/`, artifact index, etc.).
4. On every push to `main` (not on pull requests), the built site is
   published to the `gh-pages` branch via `peaceiris/actions-gh-pages`.
   Turn on **Settings -> Pages -> Deploy from a branch -> `gh-pages`** once
   to serve it.

## Repository layout

```
xmi-input/              Source XMI files exported from Visual Paradigm
scripts/xmi_to_fsh.py   The XMI -> FSH converter
sushi-config.yaml       SUSHI / IG Publisher configuration
ig.ini                  IG Publisher entry point (points at the SUSHI-generated IG resource)
input/pagecontent/      Hand-written narrative pages (index.md, etc.)
input/fsh/models/       Generated FSH logical models (gitignored, built by CI)
.github/workflows/      The two-step CI pipeline
```

`input/` is the HL7 IG Publisher's own reserved project folder (FSH
sources, page content, etc.), which is why the raw XMI files live in the
separate `xmi-input/` folder instead.

## Running locally

```sh
npm install
python3 scripts/xmi_to_fsh.py --input xmi-input --output input/fsh/models
npx sushi build .           # validate FSH
# optional, requires Java 17+ and downloads the IG Publisher jar:
curl -fL -o publisher.jar https://github.com/HL7/fhir-ig-publisher/releases/latest/download/publisher.jar
java -jar publisher.jar -ig sushi-config.yaml
```

## Before publishing for real

`sushi-config.yaml` uses placeholder values (`id`, `canonical`,
`publisher`) — update these to your organization's own before treating the
published site as anything but a CI preview.
