# Referens - Logical Models from Visual Paradigm XMI v0.1.0

## Logical Model: Referens 

 
Supporting logical model generated from gloo4.xmi (source class: Referens). 

**Usages:**

* Use this Logical Model: [Laboratorieanalysresultat : Observation](StructureDefinition-Laboratorieanalysresultat-Observation.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/xmi.to.fsh|current/StructureDefinition/StructureDefinition-Referens.json)

### Formal Views of Profile Content

 [Description Differentials, Snapshots, and other representations](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](../StructureDefinition-Referens.csv), [Excel](../StructureDefinition-Referens.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "Referens",
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-type-characteristics",
    "valueCode" : "can-be-target"
  }],
  "url" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Referens",
  "version" : "0.1.0",
  "name" : "Referens",
  "title" : "Referens",
  "status" : "draft",
  "date" : "2026-09-18T09:59:15+00:00",
  "publisher" : "xmi-to-fsh",
  "contact" : [{
    "name" : "xmi-to-fsh",
    "telecom" : [{
      "system" : "url",
      "value" : "https://github.com/oskthu2/xmi-to-fsh"
    }]
  }],
  "description" : "Supporting logical model generated from gloo4.xmi (source class: Referens).",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Referens",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "Referens",
      "path" : "Referens",
      "short" : "Referens",
      "definition" : "Supporting logical model generated from gloo4.xmi (source class: Referens)."
    },
    {
      "id" : "Referens.intervall",
      "path" : "Referens.intervall",
      "short" : "Source attribute: intervall",
      "definition" : "Source attribute: intervall",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "Referens.text",
      "path" : "Referens.text",
      "short" : "Source attribute: text",
      "definition" : "Source attribute: text",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/ST"
      }]
    },
    {
      "id" : "Referens.population",
      "path" : "Referens.population",
      "short" : "Source attribute: population",
      "definition" : "Source attribute: population",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/ST"
      }]
    },
    {
      "id" : "Referens.kommentar",
      "path" : "Referens.kommentar",
      "short" : "Source attribute: kommentar",
      "definition" : "Source attribute: kommentar",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/ST"
      }]
    },
    {
      "id" : "Referens.jamforsMed",
      "path" : "Referens.jamforsMed",
      "short" : "Source attribute: jämförs med",
      "definition" : "Source attribute: jämförs med",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Laboratorieanalysresultat-Observation"
      }]
    }]
  }
}

```
