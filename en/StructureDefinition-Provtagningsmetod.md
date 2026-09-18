# Provtagningsmetod - Logical Models from Visual Paradigm XMI v0.1.0

## Logical Model: Provtagningsmetod 

 
Supporting logical model generated from gloo4.xmi (source class: Provtagningsmetod). 

**Usages:**

* Use this Logical Model: [Prov : Resurs (inom hälso- och sjukvård)](StructureDefinition-Prov-Resurs-inom-halso--och-sjukvard.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/xmi.to.fsh|current/StructureDefinition/StructureDefinition-Provtagningsmetod.json)

### Formal Views of Profile Content

 [Description Differentials, Snapshots, and other representations](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](../StructureDefinition-Provtagningsmetod.csv), [Excel](../StructureDefinition-Provtagningsmetod.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "Provtagningsmetod",
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-type-characteristics",
    "valueCode" : "can-be-target"
  }],
  "url" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Provtagningsmetod",
  "version" : "0.1.0",
  "name" : "Provtagningsmetod",
  "title" : "Provtagningsmetod",
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
  "description" : "Supporting logical model generated from gloo4.xmi (source class: Provtagningsmetod).",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Provtagningsmetod",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "Provtagningsmetod",
      "path" : "Provtagningsmetod",
      "short" : "Provtagningsmetod",
      "definition" : "Supporting logical model generated from gloo4.xmi (source class: Provtagningsmetod)."
    },
    {
      "id" : "Provtagningsmetod.tasMedViss",
      "path" : "Provtagningsmetod.tasMedViss",
      "short" : "Source attribute: tas med viss",
      "definition" : "Source attribute: tas med viss",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Prov-Resurs-inom-halso--och-sjukvard"
      }]
    }]
  }
}

```
