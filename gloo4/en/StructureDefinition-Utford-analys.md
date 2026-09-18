# Utförd analys - gloo4 v0.1.0

## Logical Model: Utförd analys 

 
Detta är väl mer en statusmarkering? Planerad, pågående, utförd; kanske inte behövs i en begreppsmodell? 

**Usages:**

* This Logical Model is not used by any profiles in this Specification

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/gloo4|current/StructureDefinition/StructureDefinition-Utford-analys.json)

### Formal Views of Profile Content

 [Description Differentials, Snapshots, and other representations](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](../StructureDefinition-Utford-analys.csv), [Excel](../StructureDefinition-Utford-analys.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "Utford-analys",
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-type-characteristics",
    "valueCode" : "can-be-target"
  }],
  "url" : "http://example.org/fhir/gloo4/StructureDefinition/Utford-analys",
  "version" : "0.1.0",
  "name" : "Utfordanalys",
  "title" : "Utförd analys",
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
  "description" : "Detta är väl mer en statusmarkering? Planerad, pågående, utförd; kanske inte behövs i en begreppsmodell?",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://example.org/fhir/gloo4/StructureDefinition/Utford-analys",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "Utford-analys",
      "path" : "Utford-analys",
      "short" : "Utförd analys",
      "definition" : "Detta är väl mer en statusmarkering? Planerad, pågående, utförd; kanske inte behövs i en begreppsmodell?"
    }]
  }
}

```
