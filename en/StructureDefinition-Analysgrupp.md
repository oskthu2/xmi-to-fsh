# Analysgrupp - Logical Models from Visual Paradigm XMI v0.1.0

## Logical Model: Analysgrupp 

 
Supporting logical model generated from gloo4.xmi (source class: Analysgrupp). 

**Usages:**

* Use this Logical Model: [Laboratorieanalys : Aktivitet](StructureDefinition-Laboratorieanalys-Aktivitet.md) and [Laboratoriesvar : Dokument](StructureDefinition-Laboratoriesvar-Dokument.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/xmi.to.fsh|current/StructureDefinition/StructureDefinition-Analysgrupp.json)

### Formal Views of Profile Content

 [Description Differentials, Snapshots, and other representations](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](../StructureDefinition-Analysgrupp.csv), [Excel](../StructureDefinition-Analysgrupp.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "Analysgrupp",
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-type-characteristics",
    "valueCode" : "can-be-target"
  }],
  "url" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Analysgrupp",
  "version" : "0.1.0",
  "name" : "Analysgrupp",
  "title" : "Analysgrupp",
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
  "description" : "Supporting logical model generated from gloo4.xmi (source class: Analysgrupp).",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Analysgrupp",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "Analysgrupp",
      "path" : "Analysgrupp",
      "short" : "Analysgrupp",
      "definition" : "Supporting logical model generated from gloo4.xmi (source class: Analysgrupp)."
    },
    {
      "id" : "Analysgrupp.namn",
      "path" : "Analysgrupp.namn",
      "short" : "Source attribute: namn",
      "definition" : "Source attribute: namn",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/ST"
      }]
    },
    {
      "id" : "Analysgrupp.listkod",
      "path" : "Analysgrupp.listkod",
      "short" : "Source attribute: listkod",
      "definition" : "Source attribute: listkod",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/CV"
      }]
    },
    {
      "id" : "Analysgrupp.gruppkommentar",
      "path" : "Analysgrupp.gruppkommentar",
      "short" : "Source attribute: gruppkommentar",
      "definition" : "Source attribute: gruppkommentar",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/ST"
      }]
    },
    {
      "id" : "Analysgrupp.bestarAv",
      "path" : "Analysgrupp.bestarAv",
      "short" : "Source attribute: består av",
      "definition" : "Source attribute: består av",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Laboratoriesvar-Dokument"
      }]
    },
    {
      "id" : "Analysgrupp.bestarAv2",
      "path" : "Analysgrupp.bestarAv2",
      "short" : "Source attribute: består av",
      "definition" : "Source attribute: består av",
      "min" : 1,
      "max" : "*",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Laboratorieanalys-Aktivitet"
      }]
    }]
  }
}

```
