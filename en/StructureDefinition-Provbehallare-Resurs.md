# Provbehållare : Resurs - Logical Models from Visual Paradigm XMI v0.1.0

## Logical Model: Provbehållare : Resurs 

 
Supporting logical model generated from gloo4.xmi (source class: Provbehållare : Resurs). 

**Usages:**

* Use this Logical Model: [Prov : Resurs](StructureDefinition-Prov-Resurs.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/xmi.to.fsh|current/StructureDefinition/StructureDefinition-Provbehallare-Resurs.json)

### Formal Views of Profile Content

 [Description Differentials, Snapshots, and other representations](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](../StructureDefinition-Provbehallare-Resurs.csv), [Excel](../StructureDefinition-Provbehallare-Resurs.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "Provbehallare-Resurs",
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-type-characteristics",
    "valueCode" : "can-be-target"
  }],
  "url" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Provbehallare-Resurs",
  "version" : "0.1.0",
  "name" : "ProvbehallareResurs",
  "title" : "Provbehållare : Resurs",
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
  "description" : "Supporting logical model generated from gloo4.xmi (source class: Provbehållare : Resurs).",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Provbehallare-Resurs",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "Provbehallare-Resurs",
      "path" : "Provbehallare-Resurs",
      "short" : "Provbehållare : Resurs",
      "definition" : "Supporting logical model generated from gloo4.xmi (source class: Provbehållare : Resurs)."
    },
    {
      "id" : "Provbehallare-Resurs.-id",
      "path" : "Provbehallare-Resurs._id",
      "short" : "Source attribute: id; renamed from reserved FSH name 'id'",
      "definition" : "Source attribute: id; renamed from reserved FSH name 'id'",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/II"
      }]
    },
    {
      "id" : "Provbehallare-Resurs.typ",
      "path" : "Provbehallare-Resurs.typ",
      "short" : "Source attribute: typ",
      "definition" : "Source attribute: typ",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/CV"
      }]
    },
    {
      "id" : "Provbehallare-Resurs.forvarasI",
      "path" : "Provbehallare-Resurs.forvarasI",
      "short" : "Source attribute: förvaras i",
      "definition" : "Source attribute: förvaras i",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Prov-Resurs"
      }]
    }]
  }
}

```
