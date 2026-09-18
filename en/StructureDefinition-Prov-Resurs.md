# Prov : Resurs - Logical Models from Visual Paradigm XMI v0.1.0

## Logical Model: Prov : Resurs 

 
Supporting logical model generated from gloo4.xmi (source class: Prov : Resurs). 

**Usages:**

* Use this Logical Model: [Laboratorieanalys : Aktivitet](StructureDefinition-Laboratorieanalys-Aktivitet.md), [Provbehållare : Resurs](StructureDefinition-Provbehallare-Resurs.md) and [Provrelaterad aktivitet: Aktivitet](StructureDefinition-Provrelaterad-aktivitet-Aktivitet.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/xmi.to.fsh|current/StructureDefinition/StructureDefinition-Prov-Resurs.json)

### Formal Views of Profile Content

 [Description Differentials, Snapshots, and other representations](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](../StructureDefinition-Prov-Resurs.csv), [Excel](../StructureDefinition-Prov-Resurs.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "Prov-Resurs",
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-type-characteristics",
    "valueCode" : "can-be-target"
  }],
  "url" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Prov-Resurs",
  "version" : "0.1.0",
  "name" : "ProvResurs",
  "title" : "Prov : Resurs",
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
  "description" : "Supporting logical model generated from gloo4.xmi (source class: Prov : Resurs).",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Prov-Resurs",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "Prov-Resurs",
      "path" : "Prov-Resurs",
      "short" : "Prov : Resurs",
      "definition" : "Supporting logical model generated from gloo4.xmi (source class: Prov : Resurs)."
    },
    {
      "id" : "Prov-Resurs.-id",
      "path" : "Prov-Resurs._id",
      "short" : "Source attribute: id; renamed from reserved FSH name 'id'",
      "definition" : "Source attribute: id; renamed from reserved FSH name 'id'",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/II"
      }]
    },
    {
      "id" : "Prov-Resurs.material",
      "path" : "Prov-Resurs.material",
      "short" : "Source attribute: material",
      "definition" : "Source attribute: material",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/CV-CWE"
      }]
    },
    {
      "id" : "Prov-Resurs.provtagningstidpunkt",
      "path" : "Prov-Resurs.provtagningstidpunkt",
      "short" : "Source attribute: provtagningstidpunkt",
      "definition" : "Source attribute: provtagningstidpunkt",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/TS"
      }]
    },
    {
      "id" : "Prov-Resurs.anatomiskLokalisation",
      "path" : "Prov-Resurs.anatomiskLokalisation",
      "short" : "Source attribute: anatomisk lokalisation",
      "definition" : "Source attribute: anatomisk lokalisation",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/CV-CWE"
      }]
    },
    {
      "id" : "Prov-Resurs.kommentar",
      "path" : "Prov-Resurs.kommentar",
      "short" : "Source attribute: kommentar",
      "definition" : "Source attribute: kommentar",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/ST"
      }]
    },
    {
      "id" : "Prov-Resurs.forvarasI",
      "path" : "Prov-Resurs.forvarasI",
      "short" : "Source attribute: förvaras i",
      "definition" : "Source attribute: förvaras i",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Provbehallare-Resurs"
      }]
    },
    {
      "id" : "Prov-Resurs.avser",
      "path" : "Prov-Resurs.avser",
      "short" : "Source attribute: avser",
      "definition" : "Source attribute: avser",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Provrelaterad-aktivitet-Aktivitet"
      }]
    },
    {
      "id" : "Prov-Resurs.avser2",
      "path" : "Prov-Resurs.avser2",
      "short" : "Source attribute: avser",
      "definition" : "Source attribute: avser",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Laboratorieanalys-Aktivitet"
      }]
    }]
  }
}

```
