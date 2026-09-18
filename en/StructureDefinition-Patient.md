# Patient - Logical Models from Visual Paradigm XMI v0.1.0

## Logical Model: Patient 

 
Root logical model generated from Test1.xmi (source class: Patient). 

**Usages:**

* Use this Logical Model: [Personal](StructureDefinition-Personal.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/xmi.to.fsh|current/StructureDefinition/StructureDefinition-Patient.json)

### Formal Views of Profile Content

 [Description Differentials, Snapshots, and other representations](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](../StructureDefinition-Patient.csv), [Excel](../StructureDefinition-Patient.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "Patient",
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-type-characteristics",
    "valueCode" : "can-be-target"
  }],
  "url" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Patient",
  "version" : "0.1.0",
  "name" : "Patient",
  "title" : "Patient",
  "status" : "draft",
  "date" : "2026-09-18T10:29:51+00:00",
  "publisher" : "xmi-to-fsh",
  "contact" : [{
    "name" : "xmi-to-fsh",
    "telecom" : [{
      "system" : "url",
      "value" : "https://github.com/oskthu2/xmi-to-fsh"
    }]
  }],
  "description" : "Root logical model generated from Test1.xmi (source class: Patient).",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Patient",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "Patient",
      "path" : "Patient",
      "short" : "Patient",
      "definition" : "Root logical model generated from Test1.xmi (source class: Patient)."
    },
    {
      "id" : "Patient.-id",
      "path" : "Patient._id",
      "short" : "Source attribute: id; renamed from reserved FSH name 'id'",
      "definition" : "Source attribute: id; renamed from reserved FSH name 'id'",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "id"
      }]
    },
    {
      "id" : "Patient.namn",
      "path" : "Patient.namn",
      "short" : "Source attribute: namn",
      "definition" : "Source attribute: namn",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "Patient.ansvarig",
      "path" : "Patient.ansvarig",
      "short" : "Source attribute: ansvarig",
      "definition" : "Source attribute: ansvarig",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Personal"
      }]
    }]
  }
}

```
