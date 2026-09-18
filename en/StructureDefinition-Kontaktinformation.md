# Kontaktinformation - Logical Models from Visual Paradigm XMI v0.1.0

## Logical Model: Kontaktinformation 

 
Supporting logical model generated from gloo4.xmi (source class: Kontaktinformation). 

**Usages:**

* Use this Logical Model: [Laboratoriesvar : Dokument](StructureDefinition-Laboratoriesvar-Dokument.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/xmi.to.fsh|current/StructureDefinition/StructureDefinition-Kontaktinformation.json)

### Formal Views of Profile Content

 [Description Differentials, Snapshots, and other representations](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](../StructureDefinition-Kontaktinformation.csv), [Excel](../StructureDefinition-Kontaktinformation.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "Kontaktinformation",
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-type-characteristics",
    "valueCode" : "can-be-target"
  }],
  "url" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Kontaktinformation",
  "version" : "0.1.0",
  "name" : "Kontaktinformation",
  "title" : "Kontaktinformation",
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
  "description" : "Supporting logical model generated from gloo4.xmi (source class: Kontaktinformation).",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Kontaktinformation",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "Kontaktinformation",
      "path" : "Kontaktinformation",
      "short" : "Kontaktinformation",
      "definition" : "Supporting logical model generated from gloo4.xmi (source class: Kontaktinformation)."
    },
    {
      "id" : "Kontaktinformation.text",
      "path" : "Kontaktinformation.text",
      "short" : "Source attribute: text",
      "definition" : "Source attribute: text",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/ST"
      }]
    },
    {
      "id" : "Kontaktinformation.innehaller",
      "path" : "Kontaktinformation.innehaller",
      "short" : "Source attribute: innehåller",
      "definition" : "Source attribute: innehåller",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Laboratoriesvar-Dokument"
      }]
    }]
  }
}

```
