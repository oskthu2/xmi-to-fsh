# Analysgrupp - gloo4 v0.1.0

## Logical Model: Analysgrupp 

 
Klassen Analysgrupp grupperar ett antal analyser som utförs på ett eller flera prov från samma patient och som man väljer att betrakta som en enhet. 

**Usages:**

* Use this Logical Model: [Laboratorieanalys : Aktivitet](StructureDefinition-Laboratorieanalys-Aktivitet.md) and [Laboratoriesvar : Dokument](StructureDefinition-Laboratoriesvar-Dokument.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/gloo4|current/StructureDefinition/StructureDefinition-Analysgrupp.json)

### Formal Views of Profile Content

 [Description Differentials, Snapshots, and other representations](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](../StructureDefinition-Analysgrupp.csv), [Excel](../StructureDefinition-Analysgrupp.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "Analysgrupp",
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-type-characteristics",
    "valueCode" : "can-be-target"
  }],
  "url" : "http://example.org/fhir/gloo4/StructureDefinition/Analysgrupp",
  "version" : "0.1.0",
  "name" : "Analysgrupp",
  "title" : "Analysgrupp",
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
  "description" : "Klassen Analysgrupp grupperar ett antal analyser som utförs på ett eller flera prov från samma patient och som man väljer att betrakta som en enhet.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://example.org/fhir/gloo4/StructureDefinition/Analysgrupp",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "Analysgrupp",
      "path" : "Analysgrupp",
      "short" : "Analysgrupp",
      "definition" : "Klassen Analysgrupp grupperar ett antal analyser som utförs på ett eller flera prov från samma patient och som man väljer att betrakta som en enhet."
    },
    {
      "id" : "Analysgrupp.namn",
      "path" : "Analysgrupp.namn",
      "short" : "Source attribute: namn",
      "definition" : "Angivelse av namn eller benämning på en analysgrupp",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/gloo4/StructureDefinition/ST"
      }]
    },
    {
      "id" : "Analysgrupp.listkod",
      "path" : "Analysgrupp.listkod",
      "short" : "Source attribute: listkod",
      "definition" : "Kod för en analysgrupp.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/gloo4/StructureDefinition/CV"
      }]
    },
    {
      "id" : "Analysgrupp.gruppkommentar",
      "path" : "Analysgrupp.gruppkommentar",
      "short" : "Source attribute: gruppkommentar",
      "definition" : "Angivelse av kommentar för hela analysgruppen.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/gloo4/StructureDefinition/ST"
      }]
    },
    {
      "id" : "Analysgrupp.bestarAv",
      "path" : "Analysgrupp.bestarAv",
      "short" : "Source attribute: består av",
      "definition" : "Source attribute: består av",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/gloo4/StructureDefinition/Laboratoriesvar-Dokument"
      }]
    },
    {
      "id" : "Analysgrupp.bestarAv2",
      "path" : "Analysgrupp.bestarAv2",
      "short" : "Source attribute: består av",
      "definition" : "Source attribute: består av",
      "min" : 1,
      "max" : "*",
      "type" : [{
        "code" : "http://example.org/fhir/gloo4/StructureDefinition/Laboratorieanalys-Aktivitet"
      }]
    }]
  }
}

```
