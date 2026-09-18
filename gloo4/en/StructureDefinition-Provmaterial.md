# Provmaterial - gloo4 v0.1.0

## Logical Model: Provmaterial 

 
Det material som ett prov består av. 
Kan t.ex. vara kroppsvätska, vävnad … (vad är viktigt att få med i exemplen?) 

**Usages:**

* Use this Logical Model: [Prov : Resurs (inom hälso- och sjukvård)](StructureDefinition-Prov-Resurs-inom-halso--och-sjukvard.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/gloo4|current/StructureDefinition/StructureDefinition-Provmaterial.json)

### Formal Views of Profile Content

 [Description Differentials, Snapshots, and other representations](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](../StructureDefinition-Provmaterial.csv), [Excel](../StructureDefinition-Provmaterial.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "Provmaterial",
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-type-characteristics",
    "valueCode" : "can-be-target"
  }],
  "url" : "http://example.org/fhir/gloo4/StructureDefinition/Provmaterial",
  "version" : "0.1.0",
  "name" : "Provmaterial",
  "title" : "Provmaterial",
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
  "description" : "Det material som ett prov består av.\n\nKan t.ex. vara kroppsvätska, vävnad … (vad är viktigt att få med i exemplen?)",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://example.org/fhir/gloo4/StructureDefinition/Provmaterial",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "Provmaterial",
      "path" : "Provmaterial",
      "short" : "Provmaterial",
      "definition" : "Det material som ett prov består av.\n\nKan t.ex. vara kroppsvätska, vävnad … (vad är viktigt att få med i exemplen?)"
    },
    {
      "id" : "Provmaterial.bestarAvVisst",
      "path" : "Provmaterial.bestarAvVisst",
      "short" : "Source attribute: består av visst",
      "definition" : "Source attribute: består av visst",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/gloo4/StructureDefinition/Prov-Resurs-inom-halso--och-sjukvard"
      }]
    }]
  }
}

```
