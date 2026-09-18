# Home - Logical Models from Visual Paradigm XMI v0.1.0

## Home

### Overview

This Implementation Guide is built automatically from Visual Paradigm XMI exports. Every `*.xmi` file in `xmi-input/` is converted into one or more FHIR [Logical Models](artifacts.md), one per UML class found in the file. The class marked as **Root** in Visual Paradigm becomes the logical model that represents that file; any other classes it uses are included as supporting logical models.

See the [Artifacts](artifacts.md) page for the full list of generated logical models.

### How this IG is built

1. **Extract & validate**—`scripts/xmi_to_fsh.py`reads every XMI file and generates FSH logical model definitions, then SUSHI compiles and validates the FSH.
1. **Build**— the HL7 FHIR IG Publisher builds the full IG website from the validated FSH.

Both steps run automatically in GitHub Actions on every push and pull request. See `README.md` in the repository for details.

