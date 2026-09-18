# Prov : Resurs - gloo4 v0.1.0

## Logical Model: Prov : Resurs 

 
Klassen Prov håller information om ett prov. 

**Usages:**

* Use this Logical Model: [Laboratorieanalys : Aktivitet](StructureDefinition-Laboratorieanalys-Aktivitet.md), [Provbehållare : Resurs](StructureDefinition-Provbehallare-Resurs.md) and [Provrelaterad aktivitet: Aktivitet](StructureDefinition-Provrelaterad-aktivitet-Aktivitet.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/gloo4|current/StructureDefinition/StructureDefinition-Prov-Resurs.json)

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
  "url" : "http://example.org/fhir/gloo4/StructureDefinition/Prov-Resurs",
  "version" : "0.1.0",
  "name" : "ProvResurs",
  "title" : "Prov : Resurs",
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
  "description" : "Klassen Prov håller information om ett prov.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://example.org/fhir/gloo4/StructureDefinition/Prov-Resurs",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "Prov-Resurs",
      "path" : "Prov-Resurs",
      "short" : "Prov : Resurs",
      "definition" : "Klassen Prov håller information om ett prov."
    },
    {
      "id" : "Prov-Resurs.-id",
      "path" : "Prov-Resurs._id",
      "short" : "Source attribute: id; renamed from reserved FSH name 'id'",
      "definition" : "Angivelse av identitetsbeteckning för ett prov.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/gloo4/StructureDefinition/II"
      }]
    },
    {
      "id" : "Prov-Resurs.material",
      "path" : "Prov-Resurs.material",
      "short" : "Source attribute: material",
      "definition" : "Kod för typ av provmaterial.\n\nKoden för provmaterial kan även innefatta information om provtagningsmetod.\nOm kod inte kan anges från nationellt urval kan originalText användas för textalternativ.",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/gloo4/StructureDefinition/CV-CWE"
      }]
    },
    {
      "id" : "Prov-Resurs.provtagningstidpunkt",
      "path" : "Prov-Resurs.provtagningstidpunkt",
      "short" : "Source attribute: provtagningstidpunkt",
      "definition" : "Angivelse av den tidpunkt då ett prov är taget.",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/gloo4/StructureDefinition/TS"
      }]
    },
    {
      "id" : "Prov-Resurs.anatomiskLokalisation",
      "path" : "Prov-Resurs.anatomiskLokalisation",
      "short" : "Source attribute: anatomisk lokalisation",
      "definition" : "Kod som anger var provet är taget.\n\nExempel: höger arm, vänster njure.\nOm kod inte kan anges från nationellt urval kan originalText användas för textalternativ.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/gloo4/StructureDefinition/CV-CWE"
      }]
    },
    {
      "id" : "Prov-Resurs.kommentar",
      "path" : "Prov-Resurs.kommentar",
      "short" : "Source attribute: kommentar",
      "definition" : "Angivelse av kommentar om enskilt prov.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/gloo4/StructureDefinition/ST"
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
        "code" : "http://example.org/fhir/gloo4/StructureDefinition/Provbehallare-Resurs"
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
        "code" : "http://example.org/fhir/gloo4/StructureDefinition/Provrelaterad-aktivitet-Aktivitet"
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
        "code" : "http://example.org/fhir/gloo4/StructureDefinition/Laboratorieanalys-Aktivitet"
      }]
    }]
  }
}

```
