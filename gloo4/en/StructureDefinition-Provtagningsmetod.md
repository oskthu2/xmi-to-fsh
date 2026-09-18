# Provtagningsmetod - gloo4 v0.1.0

## Logical Model: Provtagningsmetod 

 
Tillvägagångssätt för utförande av provtagning. 
En vanlig synonym är provtagningsteknik. 

**Usages:**

* Use this Logical Model: [Prov : Resurs (inom hälso- och sjukvård)](StructureDefinition-Prov-Resurs-inom-halso--och-sjukvard.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/gloo4|current/StructureDefinition/StructureDefinition-Provtagningsmetod.json)

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
  "url" : "http://example.org/fhir/gloo4/StructureDefinition/Provtagningsmetod",
  "version" : "0.1.0",
  "name" : "Provtagningsmetod",
  "title" : "Provtagningsmetod",
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
  "description" : "Tillvägagångssätt för utförande av provtagning.\n\nEn vanlig synonym är provtagningsteknik.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://example.org/fhir/gloo4/StructureDefinition/Provtagningsmetod",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "Provtagningsmetod",
      "path" : "Provtagningsmetod",
      "short" : "Provtagningsmetod",
      "definition" : "Tillvägagångssätt för utförande av provtagning.\n\nEn vanlig synonym är provtagningsteknik."
    },
    {
      "id" : "Provtagningsmetod.tasMedViss",
      "path" : "Provtagningsmetod.tasMedViss",
      "short" : "Source attribute: tas med viss",
      "definition" : "Source attribute: tas med viss",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/gloo4/StructureDefinition/Prov-Resurs-inom-halso--och-sjukvard"
      }]
    }]
  }
}

```
