# Analysutrustning : Resurs - Logical Models from Visual Paradigm XMI v0.1.0

## Logical Model: Analysutrustning : Resurs 

 
Supporting logical model generated from gloo4.xmi (source class: Analysutrustning : Resurs). 

**Usages:**

* Use this Logical Model: [Laboratorieanalys : Aktivitet](StructureDefinition-Laboratorieanalys-Aktivitet.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/xmi.to.fsh|current/StructureDefinition/StructureDefinition-Analysutrustning-Resurs.json)

### Formal Views of Profile Content

 [Description Differentials, Snapshots, and other representations](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](../StructureDefinition-Analysutrustning-Resurs.csv), [Excel](../StructureDefinition-Analysutrustning-Resurs.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "Analysutrustning-Resurs",
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-type-characteristics",
    "valueCode" : "can-be-target"
  }],
  "url" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Analysutrustning-Resurs",
  "version" : "0.1.0",
  "name" : "AnalysutrustningResurs",
  "title" : "Analysutrustning : Resurs",
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
  "description" : "Supporting logical model generated from gloo4.xmi (source class: Analysutrustning : Resurs).",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Analysutrustning-Resurs",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "Analysutrustning-Resurs",
      "path" : "Analysutrustning-Resurs",
      "short" : "Analysutrustning : Resurs",
      "definition" : "Supporting logical model generated from gloo4.xmi (source class: Analysutrustning : Resurs)."
    },
    {
      "id" : "Analysutrustning-Resurs.-id",
      "path" : "Analysutrustning-Resurs._id",
      "short" : "Source attribute: id; renamed from reserved FSH name 'id'",
      "definition" : "Source attribute: id; renamed from reserved FSH name 'id'",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/II"
      }]
    },
    {
      "id" : "Analysutrustning-Resurs.typ",
      "path" : "Analysutrustning-Resurs.typ",
      "short" : "Source attribute: typ",
      "definition" : "Source attribute: typ",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/CV-CWE"
      }]
    },
    {
      "id" : "Analysutrustning-Resurs.beskrivning",
      "path" : "Analysutrustning-Resurs.beskrivning",
      "short" : "Source attribute: beskrivning",
      "definition" : "Source attribute: beskrivning",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/ST"
      }]
    },
    {
      "id" : "Analysutrustning-Resurs.harAnvant",
      "path" : "Analysutrustning-Resurs.harAnvant",
      "short" : "Source attribute: har använt",
      "definition" : "Source attribute: har använt",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Laboratorieanalys-Aktivitet"
      }]
    }]
  }
}

```
