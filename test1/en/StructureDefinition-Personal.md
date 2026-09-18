# Personal - Test1 v0.1.0

## Logical Model: Personal 

 
Supporting logical model generated from Test1.xmi (source class: Personal). 

**Usages:**

* Use this Logical Model: [Patient](StructureDefinition-Patient.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/test1|current/StructureDefinition/StructureDefinition-Personal.json)

### Formal Views of Profile Content

 [Description Differentials, Snapshots, and other representations](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](../StructureDefinition-Personal.csv), [Excel](../StructureDefinition-Personal.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "Personal",
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-type-characteristics",
    "valueCode" : "can-be-target"
  }],
  "url" : "http://example.org/fhir/test1/StructureDefinition/Personal",
  "version" : "0.1.0",
  "name" : "Personal",
  "title" : "Personal",
  "status" : "draft",
  "date" : "2026-09-18T11:15:37+00:00",
  "publisher" : "xmi-to-fsh",
  "contact" : [{
    "name" : "xmi-to-fsh",
    "telecom" : [{
      "system" : "url",
      "value" : "https://github.com/oskthu2/xmi-to-fsh"
    }]
  }],
  "description" : "Supporting logical model generated from Test1.xmi (source class: Personal).",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://example.org/fhir/test1/StructureDefinition/Personal",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "Personal",
      "path" : "Personal",
      "short" : "Personal",
      "definition" : "Supporting logical model generated from Test1.xmi (source class: Personal)."
    },
    {
      "id" : "Personal.HSAId",
      "path" : "Personal.HSAId",
      "short" : "Source attribute: HSAId",
      "definition" : "Source attribute: HSAId",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "id"
      }]
    },
    {
      "id" : "Personal.namn",
      "path" : "Personal.namn",
      "short" : "Source attribute: namn",
      "definition" : "Source attribute: namn",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "Personal.ansvarig",
      "path" : "Personal.ansvarig",
      "short" : "Source attribute: ansvarig",
      "definition" : "Source attribute: ansvarig",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "http://example.org/fhir/test1/StructureDefinition/Patient"
      }]
    }]
  }
}

```
