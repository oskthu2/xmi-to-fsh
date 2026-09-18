# Resource Logical Models from Visual Paradigm XMI



## Resource Content

```json
{
  "resourceType" : "ImplementationGuide",
  "id" : "xmi.to.fsh",
  "language" : "en",
  "url" : "http://example.org/fhir/xmi-to-fsh/ImplementationGuide/xmi.to.fsh",
  "version" : "0.1.0",
  "name" : "XmiToFshIG",
  "title" : "Logical Models from Visual Paradigm XMI",
  "status" : "draft",
  "date" : "2026-09-18T08:41:45+00:00",
  "publisher" : "xmi-to-fsh",
  "contact" : [{
    "name" : "xmi-to-fsh",
    "telecom" : [{
      "system" : "url",
      "value" : "https://github.com/oskthu2/xmi-to-fsh"
    }]
  }],
  "description" : "Logical models generated automatically from Visual Paradigm XMI exports found in xmi-input/. Do not edit the generated FSH files under input/fsh/models/ by hand — re-run scripts/xmi_to_fsh.py instead.",
  "packageId" : "xmi.to.fsh",
  "license" : "CC0-1.0",
  "fhirVersion" : ["4.0.1"],
  "dependsOn" : [{
    "id" : "hl7tx",
    "extension" : [{
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/implementationguide-dependency-comment",
      "valueMarkdown" : "Automatically added as a dependency - all IGs depend on HL7 Terminology"
    }],
    "uri" : "http://terminology.hl7.org/ImplementationGuide/hl7.terminology",
    "packageId" : "hl7.terminology.r4",
    "version" : "7.3.0"
  },
  {
    "id" : "hl7ext",
    "extension" : [{
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/implementationguide-dependency-comment",
      "valueMarkdown" : "Automatically added as a dependency - all IGs depend on the HL7 Extension Pack"
    }],
    "uri" : "http://hl7.org/fhir/extensions/ImplementationGuide/hl7.fhir.uv.extensions",
    "packageId" : "hl7.fhir.uv.extensions.r4",
    "version" : "5.3.0"
  }],
  "definition" : {
    "extension" : [{
      "extension" : [{
        "url" : "code",
        "valueString" : "copyrightyear"
      },
      {
        "url" : "value",
        "valueString" : "2026+"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "releaselabel"
      },
      {
        "url" : "value",
        "valueString" : "ci-build"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "autoload-resources"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "path-liquid-template"
      },
      {
        "url" : "value",
        "valueString" : "template/liquid"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "path-liquid-template"
      },
      {
        "url" : "value",
        "valueString" : "input/liquid"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "path-qa"
      },
      {
        "url" : "value",
        "valueString" : "temp/qa"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "path-temp"
      },
      {
        "url" : "value",
        "valueString" : "temp/pages"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "path-output"
      },
      {
        "url" : "value",
        "valueString" : "output"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "path-suppressed-warnings"
      },
      {
        "url" : "value",
        "valueString" : "input/ignoreWarnings.txt"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "path-history"
      },
      {
        "url" : "value",
        "valueString" : "http://example.org/fhir/xmi-to-fsh/history.html"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "template-html"
      },
      {
        "url" : "value",
        "valueString" : "template-page.html"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "template-md"
      },
      {
        "url" : "value",
        "valueString" : "template-page-md.html"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "apply-contact"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "apply-context"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "apply-copyright"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "apply-jurisdiction"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "apply-license"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "apply-publisher"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "apply-version"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "apply-wg"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "active-tables"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "fmm-definition"
      },
      {
        "url" : "value",
        "valueString" : "http://hl7.org/fhir/versions.html#maturity"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "propagate-status"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "excludelogbinaryformat"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "tabbed-snapshots"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "i18n-default-lang"
      },
      {
        "url" : "value",
        "valueString" : "en"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-internal-dependency",
      "valueCode" : "hl7.fhir.uv.tools.r4#1.1.2"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "copyrightyear"
      },
      {
        "url" : "value",
        "valueString" : "2026+"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "releaselabel"
      },
      {
        "url" : "value",
        "valueString" : "ci-build"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "autoload-resources"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "path-liquid-template"
      },
      {
        "url" : "value",
        "valueString" : "template/liquid"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "path-liquid-template"
      },
      {
        "url" : "value",
        "valueString" : "input/liquid"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "path-qa"
      },
      {
        "url" : "value",
        "valueString" : "temp/qa"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "path-temp"
      },
      {
        "url" : "value",
        "valueString" : "temp/pages"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "path-output"
      },
      {
        "url" : "value",
        "valueString" : "output"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "path-suppressed-warnings"
      },
      {
        "url" : "value",
        "valueString" : "input/ignoreWarnings.txt"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "path-history"
      },
      {
        "url" : "value",
        "valueString" : "http://example.org/fhir/xmi-to-fsh/history.html"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "template-html"
      },
      {
        "url" : "value",
        "valueString" : "template-page.html"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "template-md"
      },
      {
        "url" : "value",
        "valueString" : "template-page-md.html"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "apply-contact"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "apply-context"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "apply-copyright"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "apply-jurisdiction"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "apply-license"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "apply-publisher"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "apply-version"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "apply-wg"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "active-tables"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "fmm-definition"
      },
      {
        "url" : "value",
        "valueString" : "http://hl7.org/fhir/versions.html#maturity"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "propagate-status"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "excludelogbinaryformat"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "tabbed-snapshots"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "i18n-default-lang"
      },
      {
        "url" : "value",
        "valueString" : "en"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    }],
    "resource" : [{
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-Halso--och-sjukvardspersonal.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/Halso--och-sjukvardspersonal"
      },
      "name" : ": Hälso- och sjukvårdspersonal",
      "description" : "Supporting logical model generated from gloo4.xmi (source class: : Hälso- och sjukvårdspersonal).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-Patient-2.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/Patient-2"
      },
      "name" : ": Patient",
      "description" : "Supporting logical model generated from gloo4.xmi (source class: : Patient).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-Analysgrupp.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/Analysgrupp"
      },
      "name" : "Analysgrupp",
      "description" : "Supporting logical model generated from gloo4.xmi (source class: Analysgrupp).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-Analysgrupp-2.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/Analysgrupp-2"
      },
      "name" : "Analysgrupp",
      "description" : "Supporting logical model generated from gloo4.xmi (source class: Analysgrupp).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-Analysgrupp-svarsgrupp.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/Analysgrupp-svarsgrupp"
      },
      "name" : "Analysgrupp (svarsgrupp)",
      "description" : "Supporting logical model generated from gloo4.xmi (source class: Analysgrupp (svarsgrupp)).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-Analysutrustning-Resurs.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/Analysutrustning-Resurs"
      },
      "name" : "Analysutrustning : Resurs",
      "description" : "Supporting logical model generated from gloo4.xmi (source class: Analysutrustning : Resurs).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-Ansvarig-enhet-Organisation-inom-halso--och-sjukvard.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/Ansvarig-enhet-Organisation-inom-halso--och-sjukvard"
      },
      "name" : "Ansvarig enhet : Organisation (inom hälso- och sjukvård)",
      "description" : "Supporting logical model generated from gloo4.xmi (source class: Ansvarig enhet : Organisation (inom hälso- och sjukvård)).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-BL.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/BL"
      },
      "name" : "BL",
      "description" : "Supporting logical model generated from gloo4.xmi (source class: BL).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-CV.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/CV"
      },
      "name" : "CV",
      "description" : "Supporting logical model generated from gloo4.xmi (source class: CV).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-CV-CWE.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/CV-CWE"
      },
      "name" : "CV CWE",
      "description" : "Supporting logical model generated from gloo4.xmi (source class: CV CWE).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-Delsvar-Dokument-inom-halso--och-sjukvard.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/Delsvar-Dokument-inom-halso--och-sjukvard"
      },
      "name" : "Delsvar : Dokument (inom hälso- och sjukvård)",
      "description" : "Supporting logical model generated from gloo4.xmi (source class: Delsvar : Dokument (inom hälso- och sjukvård)).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-FHIR-Diagnostic-Report-Status.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/FHIR-Diagnostic-Report-Status"
      },
      "name" : "FHIR Diagnostic Report Status ",
      "description" : "Supporting logical model generated from gloo4.xmi (source class: FHIR Diagnostic Report Status ).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-Fordjupad-analys.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/Fordjupad-analys"
      },
      "name" : "Fördjupad analys",
      "description" : "Supporting logical model generated from gloo4.xmi (source class: Fördjupad analys).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-Forekomst-av-antikropp-titer.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/Forekomst-av-antikropp-titer"
      },
      "name" : "Förekomst av antikropp (titer)",
      "description" : "Supporting logical model generated from gloo4.xmi (source class: Förekomst av antikropp (titer)).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-HSA-verksamhetskod.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/HSA-verksamhetskod"
      },
      "name" : "HSA verksamhetskod",
      "description" : "Supporting logical model generated from gloo4.xmi (source class: HSA verksamhetskod).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-Halso--och-sjukvardspersonal-Halso--och-sjukvardsperson.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/Halso--och-sjukvardspersonal-Halso--och-sjukvardsperson"
      },
      "name" : "Hälso- och sjukvårdspersonal : Hälso- och sjukvårdspersonal",
      "description" : "Supporting logical model generated from gloo4.xmi (source class: Hälso- och sjukvårdspersonal : Hälso- och sjukvårdspersonal).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-II.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/II"
      },
      "name" : "II",
      "description" : "Supporting logical model generated from gloo4.xmi (source class: II).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-Informationsmodell.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/Informationsmodell"
      },
      "name" : "Informationsmodell",
      "description" : "Root logical model generated from gloo4.xmi (source class: Informationsmodell).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-INT.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/INT"
      },
      "name" : "INT",
      "description" : "Supporting logical model generated from gloo4.xmi (source class: INT).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-IVL-PQ.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/IVL-PQ"
      },
      "name" : "IVL<PQ>",
      "description" : "Supporting logical model generated from gloo4.xmi (source class: IVL<PQ>).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-Kontaktinformation.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/Kontaktinformation"
      },
      "name" : "Kontaktinformation",
      "description" : "Supporting logical model generated from gloo4.xmi (source class: Kontaktinformation).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-Kopiemottagande-enhet.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/Kopiemottagande-enhet"
      },
      "name" : "Kopiemottagande enhet",
      "description" : "Supporting logical model generated from gloo4.xmi (source class: Kopiemottagande enhet).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-KV-befattning.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/KV-befattning"
      },
      "name" : "KV befattning",
      "description" : "Supporting logical model generated from gloo4.xmi (source class: KV befattning).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-KV-kon.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/KV-kon"
      },
      "name" : "KV kön",
      "description" : "Supporting logical model generated from gloo4.xmi (source class: KV kön).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-Laboratorieanalys-Aktivitet.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/Laboratorieanalys-Aktivitet"
      },
      "name" : "Laboratorieanalys : Aktivitet",
      "description" : "Supporting logical model generated from gloo4.xmi (source class: Laboratorieanalys : Aktivitet).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-Laboratorieanalys-Aktivitet-inom-halso--och-sjukvard.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/Laboratorieanalys-Aktivitet-inom-halso--och-sjukvard"
      },
      "name" : "Laboratorieanalys : Aktivitet (inom hälso- och sjukvård)",
      "description" : "Supporting logical model generated from gloo4.xmi (source class: Laboratorieanalys : Aktivitet (inom hälso- och sjukvård)).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-Laboratorieanalysresultat-Observation.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/Laboratorieanalysresultat-Observation"
      },
      "name" : "Laboratorieanalysresultat : Observation",
      "description" : "Supporting logical model generated from gloo4.xmi (source class: Laboratorieanalysresultat : Observation).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-Laboratorieanalysresultat-Observerat-halsotillstand.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/Laboratorieanalysresultat-Observerat-halsotillstand"
      },
      "name" : "Laboratorieanalysresultat : Observerat hälsotillstånd",
      "description" : "Supporting logical model generated from gloo4.xmi (source class: Laboratorieanalysresultat : Observerat hälsotillstånd).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-Laboratoriedisciplin.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/Laboratoriedisciplin"
      },
      "name" : "Laboratoriedisciplin",
      "description" : "Supporting logical model generated from gloo4.xmi (source class: Laboratoriedisciplin).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-Laboratoriesvar-Dokument.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/Laboratoriesvar-Dokument"
      },
      "name" : "Laboratoriesvar : Dokument",
      "description" : "Supporting logical model generated from gloo4.xmi (source class: Laboratoriesvar : Dokument).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-Laboratoriesvar-Dokument-inom-halso--och-sjukvard.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/Laboratoriesvar-Dokument-inom-halso--och-sjukvard"
      },
      "name" : "Laboratoriesvar : Dokument (inom hälso- och sjukvård)",
      "description" : "Supporting logical model generated from gloo4.xmi (source class: Laboratoriesvar : Dokument (inom hälso- och sjukvård)).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-Mikroorganism.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/Mikroorganism"
      },
      "name" : "Mikroorganism",
      "description" : "Supporting logical model generated from gloo4.xmi (source class: Mikroorganism).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-Malpopulation.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/Malpopulation"
      },
      "name" : "Målpopulation",
      "description" : "Supporting logical model generated from gloo4.xmi (source class: Målpopulation).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-NPU.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/NPU"
      },
      "name" : "NPU",
      "description" : "Supporting logical model generated from gloo4.xmi (source class: NPU).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-Organisatorisk-enhet-Organisation-inom-halso--och-sjukv.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/Organisatorisk-enhet-Organisation-inom-halso--och-sjukv"
      },
      "name" : "Organisatorisk enhet : Organisation (inom hälso- och sjukvård)",
      "description" : "Supporting logical model generated from gloo4.xmi (source class: Organisatorisk enhet : Organisation (inom hälso- och sjukvård)).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-Organisatorisk-enhet-Organisatorisk-enhet.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/Organisatorisk-enhet-Organisatorisk-enhet"
      },
      "name" : "Organisatorisk enhet : Organisatorisk enhet",
      "description" : "Supporting logical model generated from gloo4.xmi (source class: Organisatorisk enhet : Organisatorisk enhet).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-Origin.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/Origin"
      },
      "name" : "Origin",
      "description" : "Supporting logical model generated from gloo4.xmi (source class: Origin).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-Patient.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/Patient"
      },
      "name" : "Patient",
      "description" : "Root logical model generated from Test1.xmi (source class: Patient).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-Patient-Patient.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/Patient-Patient"
      },
      "name" : "Patient : Patient",
      "description" : "Supporting logical model generated from gloo4.xmi (source class: Patient : Patient).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-Person-Person.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/Person-Person"
      },
      "name" : "Person : Person",
      "description" : "Supporting logical model generated from gloo4.xmi (source class: Person : Person).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-Personal.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/Personal"
      },
      "name" : "Personal",
      "description" : "Supporting logical model generated from Test1.xmi (source class: Personal).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-PQ.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/PQ"
      },
      "name" : "PQ",
      "description" : "Supporting logical model generated from gloo4.xmi (source class: PQ).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-Preliminarsvar-Dokument-inom-halso--och-sjukvard.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/Preliminarsvar-Dokument-inom-halso--och-sjukvard"
      },
      "name" : "Preliminärsvar : Dokument (inom hälso- och sjukvård)",
      "description" : "Supporting logical model generated from gloo4.xmi (source class: Preliminärsvar : Dokument (inom hälso- och sjukvård)).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-Presentationsformat.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/Presentationsformat"
      },
      "name" : "Presentationsformat",
      "description" : "Supporting logical model generated from gloo4.xmi (source class: Presentationsformat).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-Prov-Resurs.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/Prov-Resurs"
      },
      "name" : "Prov : Resurs",
      "description" : "Supporting logical model generated from gloo4.xmi (source class: Prov : Resurs).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-Prov-Resurs-inom-halso--och-sjukvard.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/Prov-Resurs-inom-halso--och-sjukvard"
      },
      "name" : "Prov : Resurs (inom hälso- och sjukvård)",
      "description" : "Supporting logical model generated from gloo4.xmi (source class: Prov : Resurs (inom hälso- och sjukvård)).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-Prov-id.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/Prov-id"
      },
      "name" : "Prov-id",
      "description" : "Supporting logical model generated from gloo4.xmi (source class: Prov-id).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-Provbehallare-Resurs.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/Provbehallare-Resurs"
      },
      "name" : "Provbehållare : Resurs",
      "description" : "Supporting logical model generated from gloo4.xmi (source class: Provbehållare : Resurs).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-Provgivare.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/Provgivare"
      },
      "name" : "Provgivare",
      "description" : "Supporting logical model generated from gloo4.xmi (source class: Provgivare).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-Provmaterial.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/Provmaterial"
      },
      "name" : "Provmaterial",
      "description" : "Supporting logical model generated from gloo4.xmi (source class: Provmaterial).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-Provrelaterad-aktivitet-Aktivitet.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/Provrelaterad-aktivitet-Aktivitet"
      },
      "name" : "Provrelaterad aktivitet: Aktivitet",
      "description" : "Supporting logical model generated from gloo4.xmi (source class: Provrelaterad aktivitet: Aktivitet).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-Provtagningsmetod.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/Provtagningsmetod"
      },
      "name" : "Provtagningsmetod",
      "description" : "Supporting logical model generated from gloo4.xmi (source class: Provtagningsmetod).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-Referens.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/Referens"
      },
      "name" : "Referens",
      "description" : "Supporting logical model generated from gloo4.xmi (source class: Referens).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-Referenser.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/Referenser"
      },
      "name" : "Referenser",
      "description" : "Supporting logical model generated from gloo4.xmi (source class: Referenser).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-Referensintervall.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/Referensintervall"
      },
      "name" : "Referensintervall",
      "description" : "Supporting logical model generated from gloo4.xmi (source class: Referensintervall).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-Referensmodell.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/Referensmodell"
      },
      "name" : "Referensmodell",
      "description" : "Supporting logical model generated from gloo4.xmi (source class: Referensmodell).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-Referenspopulation.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/Referenspopulation"
      },
      "name" : "Referenspopulation",
      "description" : "Supporting logical model generated from gloo4.xmi (source class: Referenspopulation).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-Referensvarde.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/Referensvarde"
      },
      "name" : "Referensvärde",
      "description" : "Supporting logical model generated from gloo4.xmi (source class: Referensvärde).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-Remiss-Dokument.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/Remiss-Dokument"
      },
      "name" : "Remiss : Dokument",
      "description" : "Supporting logical model generated from gloo4.xmi (source class: Remiss : Dokument).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-Remiss-Dokument-inom-halso--och-sjukvard.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/Remiss-Dokument-inom-halso--och-sjukvard"
      },
      "name" : "Remiss : Dokument (inom hälso- och sjukvård)",
      "description" : "Supporting logical model generated from gloo4.xmi (source class: Remiss : Dokument (inom hälso- och sjukvård)).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-Remissmottagande-enhet-Organisation-inom-halso--och-sju.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/Remissmottagande-enhet-Organisation-inom-halso--och-sju"
      },
      "name" : "Remissmottagande enhet : Organisation (inom hälso- och sjukvård)",
      "description" : "Supporting logical model generated from gloo4.xmi (source class: Remissmottagande enhet : Organisation (inom hälso- och sjukvård)).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-Remissvar-Dokument-inom-halso--och-sjukvard.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/Remissvar-Dokument-inom-halso--och-sjukvard"
      },
      "name" : "Remissvar : Dokument (inom hälso- och sjukvård)",
      "description" : "Supporting logical model generated from gloo4.xmi (source class: Remissvar : Dokument (inom hälso- och sjukvård)).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-Remissvarsmottagande-enhet-Organisation-inom-halso--och.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/Remissvarsmottagande-enhet-Organisation-inom-halso--och"
      },
      "name" : "Remissvarsmottagande enhet : Organisation (inom hälso- och sjukvård)",
      "description" : "Supporting logical model generated from gloo4.xmi (source class: Remissvarsmottagande enhet : Organisation (inom hälso- och sjukvård)).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-Remittent-Halso--och-sjukvardspersonal.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/Remittent-Halso--och-sjukvardspersonal"
      },
      "name" : "Remittent : Hälso- och sjukvårdspersonal",
      "description" : "Supporting logical model generated from gloo4.xmi (source class: Remittent : Hälso- och sjukvårdspersonal).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-Remitterande-enhet-Organisation-inom-halso--och-sjukvar.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/Remitterande-enhet-Organisation-inom-halso--och-sjukvar"
      },
      "name" : "Remitterande enhet : Organisation (inom hälso- och sjukvård)",
      "description" : "Supporting logical model generated from gloo4.xmi (source class: Remitterande enhet : Organisation (inom hälso- och sjukvård)).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-Resistens.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/Resistens"
      },
      "name" : "Resistens",
      "description" : "Supporting logical model generated from gloo4.xmi (source class: Resistens).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-Resistensbestamning-Aktivitet-inom-halso--och-sjukvard.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/Resistensbestamning-Aktivitet-inom-halso--och-sjukvard"
      },
      "name" : "Resistensbestämning : Aktivitet (inom hälso- och sjukvård)",
      "description" : "Supporting logical model generated from gloo4.xmi (source class: Resistensbestämning : Aktivitet (inom hälso- och sjukvård)).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-Revisionshistorik.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/Revisionshistorik"
      },
      "name" : "Revisionshistorik",
      "description" : "Supporting logical model generated from gloo4.xmi (source class: Revisionshistorik).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-RevisionshistorikTA.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/RevisionshistorikTA"
      },
      "name" : "RevisionshistorikTA",
      "description" : "Supporting logical model generated from gloo4.xmi (source class: RevisionshistorikTA).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-Signatur.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/Signatur"
      },
      "name" : "Signatur",
      "description" : "Supporting logical model generated from gloo4.xmi (source class: Signatur).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-Signering-Deltagande.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/Signering-Deltagande"
      },
      "name" : "Signering : Deltagande",
      "description" : "Supporting logical model generated from gloo4.xmi (source class: Signering : Deltagande).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-Signering-Deltagande-2.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/Signering-Deltagande-2"
      },
      "name" : "Signering : Deltagande",
      "description" : "Supporting logical model generated from gloo4.xmi (source class: Signering : Deltagande).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-Slutsvar-Dokument-inom-halso--och-sjukvard.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/Slutsvar-Dokument-inom-halso--och-sjukvard"
      },
      "name" : "Slutsvar : Dokument (inom hälso- och sjukvård)",
      "description" : "Supporting logical model generated from gloo4.xmi (source class: Slutsvar : Dokument (inom hälso- och sjukvård)).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-SNOMED-CT-SE.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/SNOMED-CT-SE"
      },
      "name" : "SNOMED-CT SE",
      "description" : "Supporting logical model generated from gloo4.xmi (source class: SNOMED-CT SE).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-ST.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/ST"
      },
      "name" : "ST",
      "description" : "Supporting logical model generated from gloo4.xmi (source class: ST).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-TS.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/TS"
      },
      "name" : "TS",
      "description" : "Supporting logical model generated from gloo4.xmi (source class: TS).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-Urval-analyskoder-laboratoriemedicin.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/Urval-analyskoder-laboratoriemedicin"
      },
      "name" : "Urval analyskoder laboratoriemedicin",
      "description" : "Supporting logical model generated from gloo4.xmi (source class: Urval analyskoder laboratoriemedicin).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-Urval-analysmetod-laboratoriemedicin.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/Urval-analysmetod-laboratoriemedicin"
      },
      "name" : "Urval analysmetod laboratoriemedicin",
      "description" : "Supporting logical model generated from gloo4.xmi (source class: Urval analysmetod laboratoriemedicin).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-Urval-analysstatus-laboratoriemedicin.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/Urval-analysstatus-laboratoriemedicin"
      },
      "name" : "Urval analysstatus laboratoriemedicin  ",
      "description" : "Supporting logical model generated from gloo4.xmi (source class: Urval analysstatus laboratoriemedicin  ).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-Urval-anatomisk-lokalisation-laboratoriemedicin.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/Urval-anatomisk-lokalisation-laboratoriemedicin"
      },
      "name" : "Urval anatomisk lokalisation laboratoriemedicin",
      "description" : "Supporting logical model generated from gloo4.xmi (source class: Urval anatomisk lokalisation laboratoriemedicin).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-Urval-fynd-bakterieegenskaper-laboratoriemedicin.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/Urval-fynd-bakterieegenskaper-laboratoriemedicin"
      },
      "name" : "Urval fynd bakterieegenskaper laboratoriemedicin ",
      "description" : "Supporting logical model generated from gloo4.xmi (source class: Urval fynd bakterieegenskaper laboratoriemedicin ).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-Urval-fynd-mikroorganism-laboratoriemedicin.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/Urval-fynd-mikroorganism-laboratoriemedicin"
      },
      "name" : "Urval fynd mikroorganism laboratoriemedicin",
      "description" : "Supporting logical model generated from gloo4.xmi (source class: Urval fynd mikroorganism laboratoriemedicin).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-Urval-fynd-resistens-laboratoriemedicin.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/Urval-fynd-resistens-laboratoriemedicin"
      },
      "name" : "Urval fynd resistens laboratoriemedicin ",
      "description" : "Supporting logical model generated from gloo4.xmi (source class: Urval fynd resistens laboratoriemedicin ).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-Urval-fynd-ovrigt-laboratoriemedicin.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/Urval-fynd-ovrigt-laboratoriemedicin"
      },
      "name" : "Urval fynd övrigt laboratoriemedicin",
      "description" : "Supporting logical model generated from gloo4.xmi (source class: Urval fynd övrigt laboratoriemedicin).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-Urval-provbehallare-laboratoriemedicin.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/Urval-provbehallare-laboratoriemedicin"
      },
      "name" : "Urval provbehallare laboratoriemedicin",
      "description" : "Supporting logical model generated from gloo4.xmi (source class: Urval provbehallare laboratoriemedicin).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-Urval-provtyp-laboratoriemedicin.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/Urval-provtyp-laboratoriemedicin"
      },
      "name" : "Urval provtyp laboratoriemedicin",
      "description" : "Supporting logical model generated from gloo4.xmi (source class: Urval provtyp laboratoriemedicin).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-Urval-tolkning-resultat-laboratoriemedicin.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/Urval-tolkning-resultat-laboratoriemedicin"
      },
      "name" : "Urval tolkning resultat laboratoriemedicin",
      "description" : "Supporting logical model generated from gloo4.xmi (source class: Urval tolkning resultat laboratoriemedicin).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-Utforande-enhet-Organisation-inom-halso--och-sjukvard.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/Utforande-enhet-Organisation-inom-halso--och-sjukvard"
      },
      "name" : "Utförande enhet : Organisation (inom hälso- och sjukvård)",
      "description" : "Supporting logical model generated from gloo4.xmi (source class: Utförande enhet : Organisation (inom hälso- och sjukvård)).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-Utford-analys.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/Utford-analys"
      },
      "name" : "Utförd analys",
      "description" : "Supporting logical model generated from gloo4.xmi (source class: Utförd analys).",
      "exampleBoolean" : false
    }],
    "page" : {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-page-name",
        "valueUrl" : "toc.html"
      }],
      "nameUrl" : "toc.html",
      "title" : "Table of Contents",
      "generation" : "html",
      "page" : [{
        "extension" : [{
          "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-page-name",
          "valueUrl" : "index.html"
        }],
        "nameUrl" : "index.html",
        "title" : "Home",
        "generation" : "markdown"
      }]
    },
    "parameter" : [{
      "code" : "path-resource",
      "value" : "input/capabilities"
    },
    {
      "code" : "path-resource",
      "value" : "input/examples"
    },
    {
      "code" : "path-resource",
      "value" : "input/extensions"
    },
    {
      "code" : "path-resource",
      "value" : "input/models"
    },
    {
      "code" : "path-resource",
      "value" : "input/operations"
    },
    {
      "code" : "path-resource",
      "value" : "input/profiles"
    },
    {
      "code" : "path-resource",
      "value" : "input/resources"
    },
    {
      "code" : "path-resource",
      "value" : "input/vocabulary"
    },
    {
      "code" : "path-resource",
      "value" : "input/maps"
    },
    {
      "code" : "path-resource",
      "value" : "input/testing"
    },
    {
      "code" : "path-resource",
      "value" : "input/history"
    },
    {
      "code" : "path-resource",
      "value" : "fsh-generated/resources"
    },
    {
      "code" : "path-pages",
      "value" : "template/config"
    },
    {
      "code" : "path-pages",
      "value" : "input/assets"
    },
    {
      "code" : "path-pages",
      "value" : "input/images"
    },
    {
      "code" : "path-tx-cache",
      "value" : "input-cache/txcache"
    }]
  }
}

```
