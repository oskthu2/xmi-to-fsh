# Analysutrustning : Resurs - gloo4 v0.1.0

## Logical Model: Analysutrustning : Resurs 

 
Klassen Analysutrustning håller information om den utrustning som använts för att utföra en analys. 

**Usages:**

* Use this Logical Model: [Laboratorieanalys : Aktivitet](StructureDefinition-Laboratorieanalys-Aktivitet.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/gloo4|current/StructureDefinition/StructureDefinition-Analysutrustning-Resurs.json)

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
  "url" : "http://example.org/fhir/gloo4/StructureDefinition/Analysutrustning-Resurs",
  "version" : "0.1.0",
  "name" : "AnalysutrustningResurs",
  "title" : "Analysutrustning : Resurs",
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
  "description" : "Klassen Analysutrustning håller information om den utrustning som använts för att utföra en analys.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://example.org/fhir/gloo4/StructureDefinition/Analysutrustning-Resurs",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "Analysutrustning-Resurs",
      "path" : "Analysutrustning-Resurs",
      "short" : "Analysutrustning : Resurs",
      "definition" : "Klassen Analysutrustning håller information om den utrustning som använts för att utföra en analys."
    },
    {
      "id" : "Analysutrustning-Resurs.-id",
      "path" : "Analysutrustning-Resurs._id",
      "short" : "Source attribute: id; renamed from reserved FSH name 'id'",
      "definition" : "Identitetsbeteckning för en analysutrustning.Id identifierar unikt en viss instans av utrustning,till skillnad från attributet typ som identifierar en typ eller modellbeteckning.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/gloo4/StructureDefinition/II"
      }]
    },
    {
      "id" : "Analysutrustning-Resurs.typ",
      "path" : "Analysutrustning-Resurs.typ",
      "short" : "Source attribute: typ",
      "definition" : "Typ eller modellbeteckning\n\nOm kod inte kan anges från nationellt urval kan originalText användas för textalternativ.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/gloo4/StructureDefinition/CV-CWE"
      }]
    },
    {
      "id" : "Analysutrustning-Resurs.beskrivning",
      "path" : "Analysutrustning-Resurs.beskrivning",
      "short" : "Source attribute: beskrivning",
      "definition" : "-",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/gloo4/StructureDefinition/ST"
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
        "code" : "http://example.org/fhir/gloo4/StructureDefinition/Laboratorieanalys-Aktivitet"
      }]
    }]
  }
}

```
