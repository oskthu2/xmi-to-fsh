# Laboratoriedisciplin - Logical Models from Visual Paradigm XMI v0.1.0

## Logical Model: Laboratoriedisciplin 

 
Supporting logical model generated from gloo4.xmi (source class: Laboratoriedisciplin). 

**Usages:**

* Use this Logical Model: [Laboratorieanalys : Aktivitet (inom hälso- och sjukvård)](StructureDefinition-Laboratorieanalys-Aktivitet-inom-halso--och-sjukvard.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/xmi.to.fsh|current/StructureDefinition/StructureDefinition-Laboratoriedisciplin.json)

### Formal Views of Profile Content

 [Description Differentials, Snapshots, and other representations](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](../StructureDefinition-Laboratoriedisciplin.csv), [Excel](../StructureDefinition-Laboratoriedisciplin.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "Laboratoriedisciplin",
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-type-characteristics",
    "valueCode" : "can-be-target"
  }],
  "url" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Laboratoriedisciplin",
  "version" : "0.1.0",
  "name" : "Laboratoriedisciplin",
  "title" : "Laboratoriedisciplin",
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
  "description" : "Supporting logical model generated from gloo4.xmi (source class: Laboratoriedisciplin).",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Laboratoriedisciplin",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "Laboratoriedisciplin",
      "path" : "Laboratoriedisciplin",
      "short" : "Laboratoriedisciplin",
      "definition" : "Supporting logical model generated from gloo4.xmi (source class: Laboratoriedisciplin)."
    },
    {
      "id" : "Laboratoriedisciplin.utforsInomEn",
      "path" : "Laboratoriedisciplin.utforsInomEn",
      "short" : "Source attribute: utförs inom en",
      "definition" : "Source attribute: utförs inom en",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Laboratorieanalys-Aktivitet-inom-halso--och-sjukvard"
      }]
    }]
  }
}

```
