# Resource gloo4



## Resource Content

```json
{
  "resourceType" : "ImplementationGuide",
  "id" : "gloo4",
  "language" : "en",
  "url" : "http://example.org/fhir/gloo4/ImplementationGuide/gloo4",
  "version" : "0.1.0",
  "name" : "gloo4IG",
  "title" : "gloo4",
  "status" : "draft",
  "date" : "2026-09-18T11:14:11+00:00",
  "publisher" : "xmi-to-fsh",
  "contact" : [{
    "name" : "xmi-to-fsh",
    "telecom" : [{
      "system" : "url",
      "value" : "https://github.com/oskthu2/xmi-to-fsh"
    }]
  }],
  "description" : "Logical model IG generated automatically from gloo4.xmi (Visual Paradigm XMI export). Do not edit the generated FSH under input/fsh/models/ by hand — re-run scripts/xmi_to_fsh.py instead.",
  "packageId" : "gloo4",
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
        "valueString" : "http://example.org/fhir/gloo4/history.html"
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
        "valueString" : "http://example.org/fhir/gloo4/history.html"
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
        "valueUri" : "StructureDefinition-Patient.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/Patient"
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
      "description" : "Klassen Analysgrupp grupperar ett antal analyser som utförs på ett eller flera prov från samma patient och som man väljer att betrakta som en enhet.",
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
      "description" : "Grupp av analyser utförda på ett eller flera prov från samma provgivare och som man väljer att betrakta som en enhet.",
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
      "description" : "Sökning på google visar att ”analysgrupp” verkar avse en grupp av personer som ska analysera något. Och ”svarsgrupp” tycks ha med telefoni att göra. Detta kanske är något informatiskt som inte behöver förklaras i en begreppsmodell? \n\nEller \"Grupp av analyser utförda på ett och samma prov\"? Stämmer det att det är ett och samma prov? I informationsmodellen står det att analysgrupp kan avse 0 till många prov, men i beskrivningen till klassen Analysgrupp står att denna grupperar ett antal analyser som utförs på ett prov. \n\n2018-03-14: Vi stryker denna i begreppsmodellen, det löser man i informationsmodellen (gruppkommentar e.d.). \n\nAnalysgrupp  \nDet kan vara ett eller flera prov. Exempel: påvisande av antikroppar mot Borrelia i både blod och cerebrospinalvätska.  \nObservera att olika landsting kan ha löst detta på olika sätt. Man kan av tekniska skäl tvingas ha en analysgrupp som en enda ”vanlig” analys. Och det kan vara tvärtom: labbet hanterar analyserna som en grupp, men av tekniska skäl måste de ingående analyserna svaras ut en och en.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/implementationguide-resource-format",
        "valueCode" : "application/fhir+json"
      },
      {
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Binary"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "Binary-Analysutrustning.html"
      }],
      "reference" : {
        "reference" : "Binary/Analysutrustning"
      },
      "name" : "Analysutrustning",
      "description" : "Example instance generated from an object diagram in gloo4.xmi.",
      "exampleCanonical" : "http://example.org/fhir/gloo4/StructureDefinition/Analysutrustning-Resurs"
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
      "description" : "Klassen Analysutrustning håller information om den utrustning som använts för att utföra en analys.",
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
      "description" : "Den enhet som ansvarar för innehållet i laboratoriesvaret.",
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
      "description" : "Booleskt värde",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/implementationguide-resource-format",
        "valueCode" : "application/fhir+json"
      },
      {
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Binary"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "Binary-BBasofilagranulocyterReferensintervall.html"
      }],
      "reference" : {
        "reference" : "Binary/BBasofilagranulocyterReferensintervall"
      },
      "name" : "B—Basofila granulocyter, Referensintervall",
      "description" : "Example instance generated from an object diagram in gloo4.xmi.",
      "exampleCanonical" : "http://example.org/fhir/gloo4/StructureDefinition/Referens"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/implementationguide-resource-format",
        "valueCode" : "application/fhir+json"
      },
      {
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Binary"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "Binary-BBasofilagranulocyterReferensintervall2.html"
      }],
      "reference" : {
        "reference" : "Binary/BBasofilagranulocyterReferensintervall2"
      },
      "name" : "B—Basofila granulocyter, Referensintervall",
      "description" : "Example instance generated from an object diagram in gloo4.xmi.",
      "exampleCanonical" : "http://example.org/fhir/gloo4/StructureDefinition/Referens"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/implementationguide-resource-format",
        "valueCode" : "application/fhir+json"
      },
      {
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Binary"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "Binary-BEosinofilagranulocyterReferensintervall.html"
      }],
      "reference" : {
        "reference" : "Binary/BEosinofilagranulocyterReferensintervall"
      },
      "name" : "B—Eosinofila granulocyter, Referensintervall",
      "description" : "Example instance generated from an object diagram in gloo4.xmi.",
      "exampleCanonical" : "http://example.org/fhir/gloo4/StructureDefinition/Referens"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/implementationguide-resource-format",
        "valueCode" : "application/fhir+json"
      },
      {
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Binary"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "Binary-BEosinofilagranulocyterReferensintervall2.html"
      }],
      "reference" : {
        "reference" : "Binary/BEosinofilagranulocyterReferensintervall2"
      },
      "name" : "B—Eosinofila granulocyter, Referensintervall",
      "description" : "Example instance generated from an object diagram in gloo4.xmi.",
      "exampleCanonical" : "http://example.org/fhir/gloo4/StructureDefinition/Referens"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/implementationguide-resource-format",
        "valueCode" : "application/fhir+json"
      },
      {
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Binary"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "Binary-BHbA1cIFCCReferensintervall.html"
      }],
      "reference" : {
        "reference" : "Binary/BHbA1cIFCCReferensintervall"
      },
      "name" : "B—HbA1c (IFCC), Referensintervall",
      "description" : "Example instance generated from an object diagram in gloo4.xmi.",
      "exampleCanonical" : "http://example.org/fhir/gloo4/StructureDefinition/Referens"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/implementationguide-resource-format",
        "valueCode" : "application/fhir+json"
      },
      {
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Binary"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "Binary-BHemoglobinHbReferensintervall.html"
      }],
      "reference" : {
        "reference" : "Binary/BHemoglobinHbReferensintervall"
      },
      "name" : "B—Hemoglobin (Hb), Referensintervall",
      "description" : "Example instance generated from an object diagram in gloo4.xmi.",
      "exampleCanonical" : "http://example.org/fhir/gloo4/StructureDefinition/Referens"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/implementationguide-resource-format",
        "valueCode" : "application/fhir+json"
      },
      {
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Binary"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "Binary-BHemoglobinHbReferensintervall2.html"
      }],
      "reference" : {
        "reference" : "Binary/BHemoglobinHbReferensintervall2"
      },
      "name" : "B—Hemoglobin (Hb), Referensintervall",
      "description" : "Example instance generated from an object diagram in gloo4.xmi.",
      "exampleCanonical" : "http://example.org/fhir/gloo4/StructureDefinition/Referens"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/implementationguide-resource-format",
        "valueCode" : "application/fhir+json"
      },
      {
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Binary"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "Binary-BHemoglobinHbReferensintervall3.html"
      }],
      "reference" : {
        "reference" : "Binary/BHemoglobinHbReferensintervall3"
      },
      "name" : "B—Hemoglobin (Hb), Referensintervall",
      "description" : "Example instance generated from an object diagram in gloo4.xmi.",
      "exampleCanonical" : "http://example.org/fhir/gloo4/StructureDefinition/Referens"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/implementationguide-resource-format",
        "valueCode" : "application/fhir+json"
      },
      {
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Binary"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "Binary-BLeukocyterReferensintervall.html"
      }],
      "reference" : {
        "reference" : "Binary/BLeukocyterReferensintervall"
      },
      "name" : "B—Leukocyter, Referensintervall",
      "description" : "Example instance generated from an object diagram in gloo4.xmi.",
      "exampleCanonical" : "http://example.org/fhir/gloo4/StructureDefinition/Referens"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/implementationguide-resource-format",
        "valueCode" : "application/fhir+json"
      },
      {
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Binary"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "Binary-BLeukocyterReferensintervall2.html"
      }],
      "reference" : {
        "reference" : "Binary/BLeukocyterReferensintervall2"
      },
      "name" : "B—Leukocyter, Referensintervall",
      "description" : "Example instance generated from an object diagram in gloo4.xmi.",
      "exampleCanonical" : "http://example.org/fhir/gloo4/StructureDefinition/Referens"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/implementationguide-resource-format",
        "valueCode" : "application/fhir+json"
      },
      {
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Binary"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "Binary-BLymfocyterReferensintervall.html"
      }],
      "reference" : {
        "reference" : "Binary/BLymfocyterReferensintervall"
      },
      "name" : "B—Lymfocyter, Referensintervall",
      "description" : "Example instance generated from an object diagram in gloo4.xmi.",
      "exampleCanonical" : "http://example.org/fhir/gloo4/StructureDefinition/Referens"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/implementationguide-resource-format",
        "valueCode" : "application/fhir+json"
      },
      {
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Binary"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "Binary-BLymfocyterReferensintervall2.html"
      }],
      "reference" : {
        "reference" : "Binary/BLymfocyterReferensintervall2"
      },
      "name" : "B—Lymfocyter, Referensintervall",
      "description" : "Example instance generated from an object diagram in gloo4.xmi.",
      "exampleCanonical" : "http://example.org/fhir/gloo4/StructureDefinition/Referens"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/implementationguide-resource-format",
        "valueCode" : "application/fhir+json"
      },
      {
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Binary"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "Binary-BMonocyterReferensintervall.html"
      }],
      "reference" : {
        "reference" : "Binary/BMonocyterReferensintervall"
      },
      "name" : "B—Monocyter, Referensintervall",
      "description" : "Example instance generated from an object diagram in gloo4.xmi.",
      "exampleCanonical" : "http://example.org/fhir/gloo4/StructureDefinition/Referens"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/implementationguide-resource-format",
        "valueCode" : "application/fhir+json"
      },
      {
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Binary"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "Binary-BMonocyterReferensintervall2.html"
      }],
      "reference" : {
        "reference" : "Binary/BMonocyterReferensintervall2"
      },
      "name" : "B—Monocyter, Referensintervall",
      "description" : "Example instance generated from an object diagram in gloo4.xmi.",
      "exampleCanonical" : "http://example.org/fhir/gloo4/StructureDefinition/Referens"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/implementationguide-resource-format",
        "valueCode" : "application/fhir+json"
      },
      {
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Binary"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "Binary-BNeutrofilagranulocyterReferensintervall.html"
      }],
      "reference" : {
        "reference" : "Binary/BNeutrofilagranulocyterReferensintervall"
      },
      "name" : "B—Neutrofila granulocyter, Referensintervall",
      "description" : "Example instance generated from an object diagram in gloo4.xmi.",
      "exampleCanonical" : "http://example.org/fhir/gloo4/StructureDefinition/Referens"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/implementationguide-resource-format",
        "valueCode" : "application/fhir+json"
      },
      {
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Binary"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "Binary-BNeutrofilagranulocyterReferensintervall2.html"
      }],
      "reference" : {
        "reference" : "Binary/BNeutrofilagranulocyterReferensintervall2"
      },
      "name" : "B—Neutrofila granulocyter, Referensintervall",
      "description" : "Example instance generated from an object diagram in gloo4.xmi.",
      "exampleCanonical" : "http://example.org/fhir/gloo4/StructureDefinition/Referens"
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
      "description" : "Kodade värden",
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
      "description" : "Kodade värden som tillåter text som alternativ.",
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
      "description" : "Svar som innehåller resultat från en eller flera analyser där alla beställda analyser ännu inte är slutligt besvarade.\n\nDen remissvarsmottagande enheten ska förvänta sig ytterligare svar tills samtliga beställda analyser är utförda och slutligt besvarade.\n\nEn typ av delsvar är preliminärsvar, som innehåller minst ett resultat från en analys som ännu inte är avslutad.",
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
      "description" : "Value set från FHIR som specificerar typen av provsvar\nOID: 2.16.840.1.113883.4.642.3.235\nhttp://hl7.org/fhir/ValueSet/diagnostic-report-status",
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
      "description" : "Ytterligare analys föranledd av specifikt analysresultat. \n\n2018-03-14: Vi stryker denna i begreppsmodellen, det löser sig i informationsmodellen. \n\nVad är skillnad mellan fördjupad analys och konfirmationsanalys som de pratade om på mötet? Är det samma? \n\n2018-03-09: Jonas Svanberg:   \nFör mig oklart begrepp. Möjligen kan man mena ”analys/undersökning som normalt inte utförs i aktuell situation”. För mig är det bara en ytterligare Fyndegenskap (8.4).  \nEller avses ”analys som utförs pga. resultatet i beställd analys, och som inte är beställd från början”? Och behövs för att hantera den situationen?",
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
      "description" : "Kod för typ av verksamhet som den organisatoriska enheten bedriver.\n\nOID: 1.2.752.129.2.2.1.3",
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
      "description" : "Klassen hälso- och sjukvårdspersonal håller information om person som i sitt yrke utför hälso- och sjukvård.\nHälso- och sjukvårdspersonal är oftast anställd av en vårdgivare. En vårdgivare kan ha anställd hälso- och sjukvårdspersonal, och ibland, som till exempel för enskild näringsidkare, kan rollerna sammanfalla.",
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
      "description" : "Unik Identifierare",
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
      "description" : "Ental",
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
      "description" : "Interval av PQ",
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
      "description" : "Klassen Kontaktinformation håller information om vart eller till vem vården kan vända sig vid frågor om laboratoriesvaret.",
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
      "description" : "Den organisatoriska enhet som tar emot en kopia av laboratoriesvaret.  \n   \nEller ”… av remissvaret”, om detta ska vara generellt. I projektet e-remiss finns ingen kopiemottagare, är det något speciellt för laboratorieremisser? \n\n2018-03-14: Vi stryker denna ur begreppsmodellen, svarskopia är inget unikt för labbremisser.\n\n2018-03-09: Jonas Svanberg:  \nKopiemottagande enhet  \nNej, svarskopia är inget unikt för labbremisser. Det är en kvarleva från papperstiden, då det var lätt att ta en kopia (på vad som helst) och skicka till någon annan.  \nDet förekommer säkert hos vissa landsting, men vanligast är nog att det bara finns ett svar.",
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
      "description" : "Innehåller ingormation om en vård- och sjukvårdspersonals befattning.\n\nOID: 1.2.752.129.2.2.1.4",
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
      "description" : "Anger administrativt kön\n\nOID: 1.2.752.129.2.2.1.1",
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
      "description" : "Klassen Laboratorieanalys håller information om en analys",
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
      "description" : "Bestämning av egenskaper hos prov, t.ex. artbestämning, fysikaliska och kemiska egenskaper.",
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
      "description" : "Klassen Laboratorieanalysresultat håller information om resultat av en utförd analys.\n\nDetta resultat kan exempelvis bestå av ett mätvärde inom laboratoriedisciplinen kemi, ett fynd av en viss bakterieart eller en textuell beskrivning av analysresultatet. Utöver detta kan en kommentar avseende analysresultatet anges separat.",
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
      "description" : "Resultat av en laboratorieanalys. \n \nEtt laboratorieanalysresultat kan utgöras av t.ex. ett fynd (som har sina egenskaper) eller ett mätvärde.  \nExempel på fynd är en viss bakterieart eller en viss typ av virus.   \nExempel på ett fynds egenskaper är serotyp, subserotyp och koncentration.",
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
      "description" : "Disciplin som en laboratorieverksamhet kan utföra laboratorieundersökningar inom.\n\nFråga till referensgruppen: ser indelningen olika ut? Funkar det i praktiken?   \nKlinisk kemi; Mikrobiologi   ...\n\n2018-03-09: Jonas Svanberg:  \nLaboratoriedisciplin  \nUrsprungligen är det en indelning av medicinsk kunskap, t.ex. klinisk kemi och klinisk immunologi. Traditionellt var det också både organisatorisk indelning och utförande laboratorium. Så behöver det inte vara nu, men i beställarnas (och labbens) tankevärld finns denna indelning kvar.  \nHär behövs det (om det finns i svaret) som en tagg att sortera eller filtrera på. \n\n2018-03-20: 20/3: Kan strykas i begreppsmodellen, i infomodellen nytt attribut i klassen Organisatorisk enhet. \n\n\n Laboratoriemedicinska specialiteter   \n Klinisk immunologi och   \n transfusionsmedicin   \n Klinisk kemi   \n Klinisk mikrobiologi   \n Klinisk patologi   \n http://www.socialstyrelsen.se/sosfs/2015-8  \n\nReferensgruppsmötet 2018-03-27: \nSlutsats 1: Vi använder HSA-koder så länge (i HSA finns klinisk genetik som verksamhetskod, men den är där inte klassificerad som laboratorieverksamhet, vilket den borde vara enligt gruppen).    \nKategorisera det enskilda provet med hjälp av HSA-koderna.    \nKategoriseringen varierar från land till land.    \nListkoderna. De är nödvändiga för mikrobiologi idag.    \nSlutsats 2: En liten arbetsgrupp (kodverksgrupp) jobbar vidare med detta.",
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
      "description" : "Klassen Laboratoriesvar håller information om laboratoriesvaret.",
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
      "description" : "Remissvar som avser laboratorieanalysresultat.",
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
      "description" : "Levande, nästan alltid encellig varelse som är så liten att den inte kan ses med blotta ögat.\n\nDet finns fyra huvudgrupper: bakterier, svampar, virus och parasiter.",
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
      "description" : "Den grupp man undersöker.",
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
      "description" : "NPU-systemet (Nomenclature of properties and units) är ett register med systematiska, unika benämningar och koder för laboratorieundersökningar.",
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
      "description" : "Formellt bildad enhet som tillhör en organisation.",
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
      "description" : "Klassen Organisatorisk enhet håller information om formellt bildade enheter som tillhör en organisation.",
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
        "valueUri" : "StructureDefinition-Patient-Patient.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/Patient-Patient"
      },
      "name" : "Patient : Patient",
      "description" : "Klassen Patient håller information om en person som erhåller eller är registrerad för att erhålla hälso- och sjukvård.",
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
        "valueUri" : "StructureDefinition-PQ.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/PQ"
      },
      "name" : "PQ",
      "description" : "Värde samt enhet enligt unified codes for units of measure (UCUM)",
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
      "description" : "Delsvar som innehåller minst ett resultat från en analys som ännu inte är avslutad.\n\nDen remissvarsmottagande enheten ska förvänta sig ytterligare svar efter ett preliminärsvar och har fortfarande ett ansvar att bevaka detta till dess ett slutsvar har mottagits.",
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
      "description" : "Typ av filformat för svaret. \n[Så står det nu i informationsmodellen, klassen Svar, attributet \"presentationsformat\". Detta behöver knappast finnas med i begreppsmodellen.]\n\n\n\nDokument som innehåller den visuella presentationen av laboratoriesvaret.  \n   \nMen jfr projektet e-remiss, där finns bilaga:  \nDokument som kompletterar ett annat dokument och är avsett att användas tillsammans med detta.   \n   \nExempelvis utdrag ur patientjournal, en bild eller liknande som biläggs remissen, eller remissvaret.  \n   \nÄr presentation något annat än bilaga?",
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
      "description" : "Klassen Prov håller information om ett prov.",
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
      "description" : "(inom hälso- och sjukvården:) humanbiologiskt material som tagits från en levande eller avliden person eller ett foster i syfte att erhålla information om den som provet härrör från (Biobanksordlistan, under rev.)\nExempel på humanbiologiskt material är vävnad och kroppsvätskor som blod, urin, sekret.",
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
      "description" : "Klassen Provbehållare håller information om den eller de provbehållare som provet förvaras i.",
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
      "description" : "Person som lämnar prov.\n(Biobank Sverige, under revidering)",
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
      "description" : "Det material som ett prov består av.\n\nKan t.ex. vara kroppsvätska, vävnad … (vad är viktigt att få med i exemplen?)",
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
      "description" : "Klassen Provrelaterad aktivitet håller information om aktiviteter relaterade till hantering av prov.\nInkluderar även t.ex. aktiviteter i samband med transport, frysning, förvaring, bearbetning och delning i sekundärprov.",
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
      "description" : "Tillvägagångssätt för utförande av provtagning.\n\nEn vanlig synonym är provtagningsteknik.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/implementationguide-resource-format",
        "valueCode" : "application/fhir+json"
      },
      {
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Binary"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "Binary-PCpeptidReferensintervall.html"
      }],
      "reference" : {
        "reference" : "Binary/PCpeptidReferensintervall"
      },
      "name" : "P—C-peptid, Referensintervall",
      "description" : "Example instance generated from an object diagram in gloo4.xmi.",
      "exampleCanonical" : "http://example.org/fhir/gloo4/StructureDefinition/Referens"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/implementationguide-resource-format",
        "valueCode" : "application/fhir+json"
      },
      {
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Binary"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "Binary-PCRPReferensintervall.html"
      }],
      "reference" : {
        "reference" : "Binary/PCRPReferensintervall"
      },
      "name" : "P—CRP, Referensintervall",
      "description" : "Example instance generated from an object diagram in gloo4.xmi.",
      "exampleCanonical" : "http://example.org/fhir/gloo4/StructureDefinition/Referens"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/implementationguide-resource-format",
        "valueCode" : "application/fhir+json"
      },
      {
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Binary"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "Binary-PGAD65akIgGELISAReferensintervall.html"
      }],
      "reference" : {
        "reference" : "Binary/PGAD65akIgGELISAReferensintervall"
      },
      "name" : "P—GAD65-ak (IgG, ELISA), Referensintervall",
      "description" : "Example instance generated from an object diagram in gloo4.xmi.",
      "exampleCanonical" : "http://example.org/fhir/gloo4/StructureDefinition/Referens"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/implementationguide-resource-format",
        "valueCode" : "application/fhir+json"
      },
      {
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Binary"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "Binary-PGlukosReferensintervall.html"
      }],
      "reference" : {
        "reference" : "Binary/PGlukosReferensintervall"
      },
      "name" : "P—Glukos, Referensintervall",
      "description" : "Example instance generated from an object diagram in gloo4.xmi.",
      "exampleCanonical" : "http://example.org/fhir/gloo4/StructureDefinition/Referens"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/implementationguide-resource-format",
        "valueCode" : "application/fhir+json"
      },
      {
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Binary"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "Binary-PHDLkolesterolReferensintervall.html"
      }],
      "reference" : {
        "reference" : "Binary/PHDLkolesterolReferensintervall"
      },
      "name" : "P—HDL-kolesterol, Referensintervall",
      "description" : "Example instance generated from an object diagram in gloo4.xmi.",
      "exampleCanonical" : "http://example.org/fhir/gloo4/StructureDefinition/Referens"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/implementationguide-resource-format",
        "valueCode" : "application/fhir+json"
      },
      {
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Binary"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "Binary-PKolesterolReferensintervall.html"
      }],
      "reference" : {
        "reference" : "Binary/PKolesterolReferensintervall"
      },
      "name" : "P—Kolesterol, Referensintervall",
      "description" : "Example instance generated from an object diagram in gloo4.xmi.",
      "exampleCanonical" : "http://example.org/fhir/gloo4/StructureDefinition/Referens"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/implementationguide-resource-format",
        "valueCode" : "application/fhir+json"
      },
      {
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Binary"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "Binary-PLDLkolesteroldirektReferensintervall.html"
      }],
      "reference" : {
        "reference" : "Binary/PLDLkolesteroldirektReferensintervall"
      },
      "name" : "P—LDL-kolesterol, direkt, Referensintervall",
      "description" : "Example instance generated from an object diagram in gloo4.xmi.",
      "exampleCanonical" : "http://example.org/fhir/gloo4/StructureDefinition/Referens"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/implementationguide-resource-format",
        "valueCode" : "application/fhir+json"
      },
      {
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Binary"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "Binary-PnonHDLkolesterolReferensintervall.html"
      }],
      "reference" : {
        "reference" : "Binary/PnonHDLkolesterolReferensintervall"
      },
      "name" : "P—non-HDL-kolesterol, Referensintervall",
      "description" : "Example instance generated from an object diagram in gloo4.xmi.",
      "exampleCanonical" : "http://example.org/fhir/gloo4/StructureDefinition/Referens"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/implementationguide-resource-format",
        "valueCode" : "application/fhir+json"
      },
      {
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Binary"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "Binary-PTriglyceriderReferensintervall.html"
      }],
      "reference" : {
        "reference" : "Binary/PTriglyceriderReferensintervall"
      },
      "name" : "P—Triglycerider, Referensintervall",
      "description" : "Example instance generated from an object diagram in gloo4.xmi.",
      "exampleCanonical" : "http://example.org/fhir/gloo4/StructureDefinition/Referens"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/implementationguide-resource-format",
        "valueCode" : "application/fhir+json"
      },
      {
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Binary"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "Binary-POcellIA2akReferensintervall.html"
      }],
      "reference" : {
        "reference" : "Binary/POcellIA2akReferensintervall"
      },
      "name" : "P—Ö-cell(IA-2)-ak, Referensintervall",
      "description" : "Example instance generated from an object diagram in gloo4.xmi.",
      "exampleCanonical" : "http://example.org/fhir/gloo4/StructureDefinition/Referens"
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
      "description" : "Klassen Referens håller information om vilket referensintervall eller referensvärde som gäller för ett resultat.",
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
      "description" : "Det intervall som värden för ett fysiologiskt mätvärde hos  en referenspopulation   med e  n   given sannolikhet  ligger inom för den givna typen av analys med den givna metoden.\n\nReferensintervallet utgör en bas för jämförelse (en referensram) för att tolka ett analysresultat för en viss patient.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/implementationguide-resource-format",
        "valueCode" : "application/fhir+json"
      },
      {
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Binary"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "Binary-Referensintervall.html"
      }],
      "reference" : {
        "reference" : "Binary/Referensintervall"
      },
      "name" : "Referensintervall",
      "description" : "Example instance generated from an object diagram in gloo4.xmi.",
      "exampleCanonical" : "http://example.org/fhir/gloo4/StructureDefinition/Referens"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/implementationguide-resource-format",
        "valueCode" : "application/fhir+json"
      },
      {
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Binary"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "Binary-Referensintervall2.html"
      }],
      "reference" : {
        "reference" : "Binary/Referensintervall2"
      },
      "name" : "Referensintervall",
      "description" : "Example instance generated from an object diagram in gloo4.xmi.",
      "exampleCanonical" : "http://example.org/fhir/gloo4/StructureDefinition/Referens"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/implementationguide-resource-format",
        "valueCode" : "application/fhir+json"
      },
      {
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Binary"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "Binary-Referensintervall3.html"
      }],
      "reference" : {
        "reference" : "Binary/Referensintervall3"
      },
      "name" : "Referensintervall",
      "description" : "Example instance generated from an object diagram in gloo4.xmi.",
      "exampleCanonical" : "http://example.org/fhir/gloo4/StructureDefinition/Referens"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/implementationguide-resource-format",
        "valueCode" : "application/fhir+json"
      },
      {
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Binary"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "Binary-Referensintervall4.html"
      }],
      "reference" : {
        "reference" : "Binary/Referensintervall4"
      },
      "name" : "Referensintervall",
      "description" : "Example instance generated from an object diagram in gloo4.xmi.",
      "exampleCanonical" : "http://example.org/fhir/gloo4/StructureDefinition/Referens"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/implementationguide-resource-format",
        "valueCode" : "application/fhir+json"
      },
      {
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Binary"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "Binary-Referensintervall5.html"
      }],
      "reference" : {
        "reference" : "Binary/Referensintervall5"
      },
      "name" : "Referensintervall",
      "description" : "Example instance generated from an object diagram in gloo4.xmi.",
      "exampleCanonical" : "http://example.org/fhir/gloo4/StructureDefinition/Referens"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/implementationguide-resource-format",
        "valueCode" : "application/fhir+json"
      },
      {
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Binary"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "Binary-Referensintervall6.html"
      }],
      "reference" : {
        "reference" : "Binary/Referensintervall6"
      },
      "name" : "Referensintervall",
      "description" : "Example instance generated from an object diagram in gloo4.xmi.",
      "exampleCanonical" : "http://example.org/fhir/gloo4/StructureDefinition/Referens"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/implementationguide-resource-format",
        "valueCode" : "application/fhir+json"
      },
      {
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Binary"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "Binary-Referensintervall7.html"
      }],
      "reference" : {
        "reference" : "Binary/Referensintervall7"
      },
      "name" : "Referensintervall",
      "description" : "Example instance generated from an object diagram in gloo4.xmi.",
      "exampleCanonical" : "http://example.org/fhir/gloo4/StructureDefinition/Referens"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/implementationguide-resource-format",
        "valueCode" : "application/fhir+json"
      },
      {
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Binary"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "Binary-Referensintervall8.html"
      }],
      "reference" : {
        "reference" : "Binary/Referensintervall8"
      },
      "name" : "Referensintervall",
      "description" : "Example instance generated from an object diagram in gloo4.xmi.",
      "exampleCanonical" : "http://example.org/fhir/gloo4/StructureDefinition/Referens"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/implementationguide-resource-format",
        "valueCode" : "application/fhir+json"
      },
      {
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Binary"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "Binary-Referensintervall9.html"
      }],
      "reference" : {
        "reference" : "Binary/Referensintervall9"
      },
      "name" : "Referensintervall",
      "description" : "Example instance generated from an object diagram in gloo4.xmi.",
      "exampleCanonical" : "http://example.org/fhir/gloo4/StructureDefinition/Referens"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/implementationguide-resource-format",
        "valueCode" : "application/fhir+json"
      },
      {
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Binary"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "Binary-Referensintervall10.html"
      }],
      "reference" : {
        "reference" : "Binary/Referensintervall10"
      },
      "name" : "Referensintervall",
      "description" : "Example instance generated from an object diagram in gloo4.xmi.",
      "exampleCanonical" : "http://example.org/fhir/gloo4/StructureDefinition/Referens"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/implementationguide-resource-format",
        "valueCode" : "application/fhir+json"
      },
      {
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Binary"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "Binary-Referensintervalltiter.html"
      }],
      "reference" : {
        "reference" : "Binary/Referensintervalltiter"
      },
      "name" : "Referensintervall (titer)",
      "description" : "Example instance generated from an object diagram in gloo4.xmi.",
      "exampleCanonical" : "http://example.org/fhir/gloo4/StructureDefinition/Referens"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/implementationguide-resource-format",
        "valueCode" : "application/fhir+json"
      },
      {
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Binary"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "Binary-Referensintervalltiter2.html"
      }],
      "reference" : {
        "reference" : "Binary/Referensintervalltiter2"
      },
      "name" : "Referensintervall (titer)",
      "description" : "Example instance generated from an object diagram in gloo4.xmi.",
      "exampleCanonical" : "http://example.org/fhir/gloo4/StructureDefinition/Referens"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/implementationguide-resource-format",
        "valueCode" : "application/fhir+json"
      },
      {
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Binary"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "Binary-Referensintervalltiter3.html"
      }],
      "reference" : {
        "reference" : "Binary/Referensintervalltiter3"
      },
      "name" : "Referensintervall (titer)",
      "description" : "Example instance generated from an object diagram in gloo4.xmi.",
      "exampleCanonical" : "http://example.org/fhir/gloo4/StructureDefinition/Referens"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/implementationguide-resource-format",
        "valueCode" : "application/fhir+json"
      },
      {
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Binary"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "Binary-Referensintervall1.html"
      }],
      "reference" : {
        "reference" : "Binary/Referensintervall1"
      },
      "name" : "Referensintervall 1",
      "description" : "Example instance generated from an object diagram in gloo4.xmi.",
      "exampleCanonical" : "http://example.org/fhir/gloo4/StructureDefinition/Referens"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/implementationguide-resource-format",
        "valueCode" : "application/fhir+json"
      },
      {
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Binary"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "Binary-Referensintervall22.html"
      }],
      "reference" : {
        "reference" : "Binary/Referensintervall22"
      },
      "name" : "Referensintervall 2",
      "description" : "Example instance generated from an object diagram in gloo4.xmi.",
      "exampleCanonical" : "http://example.org/fhir/gloo4/StructureDefinition/Referens"
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
      "description" : "Den grupp man jämför med målpopulationen.\n\nReferenspopulationen måste stämma överens med målpopulationen i fråga om ålder, kön och sådana saker som spelar roll i sammanhanget.",
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
      "description" : "Ö  verenskommet värde   hos egenskap   mot vilket kan jämföras uppmätta eller observerade värden  .",
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
      "description" : "Klassen Remiss håller information om den remiss som ligger till grund för svaret.",
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
      "description" : "Vårdbegäran som utgör beställning av tjänst eller begäran om övertagande av medicinskt ansvar för en patient.\n\nEn remiss kan vid utfärdandet ha en tilltänkt remissmottagande enhet eller så kan patienten få möjlighet att på egen hand välja remissmottagande/utförande enhet i efterhand.",
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
      "description" : "Den organisatoriska enhet som utför klinisk bedömning av inkommen remiss samt utför det remissen avser.\n[E-remiss]",
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
      "description" : "Det som kommuniceras till remittenten efter att en remiss har bedömts och den remissmottagande enheten har accepterat att hantera det som frågeställningen avser.\n\nDet kan röra sig om ett svar på frågeställning i remissen men också vara en redogörelse för att en eller flera önskade åtgärder har utförts.   \n[Projektet e-remiss, \"Remissvar\"]",
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
      "description" : "Den organisatoriska enhet som ett remissvar skickas till.\n\nÄr vanligtvis samma organisatoriska enhet som den remitterande enheten.",
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
      "description" : "Den hälso- och sjukvårdspersonal som i sitt uppdrag för en organisatorisk enhet har fattat beslut om att skicka remiss.\n\nVissa använder uttrycket \"beställare\" för detta begrepp.",
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
      "description" : "Den organisatoriska enhet som är uppdragsgivare åt remittenten.\n[Projekt e-remiss]\n\nVissa använder uttrycket \"beställande enhet\" för detta begrepp.",
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
      "description" : "I det aktuella provet påvisad mikroorganisms känslighet för relevanta antimikrobiella läkemedel.\n\nDet finns fyra huvudgrupper av mikroorganismer: bakterier, svampar, virus och parasiter.",
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
      "description" : "Bestämning av påvisad mikroorganisms känslighet för relevanta antimikrobiella läkemedel.",
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
      "description" : "Egenhändigt skriven namnteckning eller förkortad namnteckning.",
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
      "description" : "Klassen Signering håller information om tidsangivelse då ett relaterat objekt är signerat.\nInom laboratoriedomänen finns det fyra olika typer av signering. Signeringen avser hela laboratoriesvaret eller enskilda analyser.\n1. Laboratoriesvaret signeras av en medicinskt ansvarig hälso- och sjukvårdspersonal på den ansvariga enheten.\nDen ansvariga enheten kan vara den remissvarsmottagande enheten eller den utförande enheten (exempelvis vid patientnära analyser).\n2. En enskild analys signeras av den hälso- och sjukvårdspersonal som utför analysen.\n3. Laboratoriesvaret signeras av hälso- och sjukvårdspersonal på den remissvarsmottagande enheten när det förs in i patientjournalen.\n4. En enskild analys signeras av hälso- och sjukvårdspersonal på den remissvarsmottagande enheten när den förs in i patientjournalen.",
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
      "description" : "Påförande av signatur.  \n   \nInom laboratoriedomänen finns det fyra olika typer av signering. Signeringen avser hela laboratoriesvaret eller enskilda analyser.\n\n1. Laboratoriesvaret signeras av en medicinskt ansvarig hälso- och sjukvårdspersonal på den ansvariga enheten.\n\nDen ansvariga enheten kan vara den remissvarsmottagande enheten eller den utförande enheten (exempelvis vid patientnära analyser).\n\n2. En enskild analys signeras av den hälso- och sjukvårdspersonal som utför analysen.\n\n3. Laboratoriesvaret signeras av hälso- och sjukvårdspersonal på den remissvarsmottagande enheten när det förs in i patientjournalen.\n\n4. En enskild analys signeras av hälso- och sjukvårdspersonal på den remissvarsmottagande enheten när den förs in i patientjournalen.",
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
      "description" : "Svar där samtliga i remissen beställda analyser i och med detta svar är besvarade slutligt, och inga fortsatta analyser pågår.\n\nDen remissvarsmottagande enheten ska i och med detta inte förvänta sig ytterligare svar. Även efter ett slutsvar finns det möjlighet för utförande enhet att skicka ytterligare svar relaterat till samma remiss.",
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
      "description" : "SNOMED CT innehåller en stor mängd kliniska termer.\n\nOID: 1.2.752.116.2.1.1",
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
      "description" : "Textsträng",
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
      "description" : "Tidpunkt",
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
      "description" : "Kod för den typ av analys som utförts.   Urval från NPU.\n\nOID: 1.2.752.108.1.1",
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
      "description" : "Urval ur Snomed CT (OID: 1.2.752.116.2.1.1) för att beskriva metodprinciper inom laboratoriemedicin. Princip för analysmetod bör användas för laboratoriemedicinska undersökningar där resultaten kan skilja sig beroende på analysmetoden, även om man avser att mäta samma sak, eller när metodprincipen är viktig för tolkningen av resultatet.\n\nOID: 1.2.752.129.5.1.18\nRefset-ID: 63181000052104",
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
      "description" : "Urval ur Snomed CT (1.2.752.116.2.1.1) för att beskriva analysstatus inom laboratoriemedicin. Detta urval är baserat på urvalet aktivitetsstatus med Refset-ID 56421000052109.\n\nOID: 1.2.752.129.5.1.6\nRefset-ID: 500111000057108",
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
      "description" : "Urval ur Snomed CT (1.2.752.116.2.1.1) för att beskriva anatomisk lokalisation inom laboratoriemedicin.\n\nOID: 1.2.752.129.5.1.7\nRefset-ID: 500091000057101",
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
      "description" : "Urval ur Snomed CT (OID: 1.2.752.116.2.1.1) för att beskriva resultat av undersökning av egenskaper av bakterier som inte utgör släkte eller art inom laboratoriemedicin.\n\nOID: 1.2.752.129.5.1.8\nRefset-ID: 500101000057105",
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
      "description" : "Urval ur Snomed CT (OID: 1.2.752.116.2.1.1) för att beskriva fynd av mikroorganismer inom laboratoriemedicin.\n\nOID: 1.2.752.129.5.1.9\nRefset-ID: 500061000057107",
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
      "description" : "Urval ur Snomed CT (1.2.752.116.2.1.1) för att beskriva resultat av undersökning av resistens mot antibiotika inom laboratoriemedicin.\n\nOID: 1.2.752.129.5.1.10\nRefset-ID: 500041000057108",
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
      "description" : "Urval ur Snomed CT (OID: 1.2.752.116.2.1.1) för att beskriva resultat av laboratorieundersökning inom laboratoriemedicin.\n\nOID: 1.2.752.129.5.1.11\nRefset-ID: 500081000057104",
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
      "description" : "Urval ur Snomed CT (OID: 1.2.752.116.2.1.1) för att beskriva provbehållare inom laboratoriemedicin.\n\nOID: 1.2.752.129.5.1.12\nRefset-ID: 500071000057102",
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
      "description" : "Urval ur Snomed CT (OID: 1.2.752.116.2.1.1) för att beskriva provtyp inom laboratoriemedicin.\n\nOID: 1.2.752.129.5.1.13\nRefset-ID: 500121000057102",
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
      "description" : "Urval ur Snomed CT (OID: 1.2.752.116.2.1.1)för att beskriva tolkning av fynd inom laboratoriemedicin.\n\nOID: 1.2.752.129.5.1.14\nRefset-ID: 500051000057105",
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
      "description" : "Den enhet som utför en enskild analys.",
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
      "description" : "Detta är väl mer en statusmarkering? Planerad, pågående, utförd; kanske inte behövs i en begreppsmodell?",
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
