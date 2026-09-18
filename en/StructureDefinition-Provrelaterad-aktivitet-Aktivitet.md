# Provrelaterad aktivitet: Aktivitet - Logical Models from Visual Paradigm XMI v0.1.0

## Logical Model: Provrelaterad aktivitet: Aktivitet 

 
Klassen Provrelaterad aktivitet håller information om aktiviteter relaterade till hantering av prov. Inkluderar även t.ex. aktiviteter i samband med transport, frysning, förvaring, bearbetning och delning i sekundärprov. 

**Usages:**

* Use this Logical Model: [Prov : Resurs](StructureDefinition-Prov-Resurs.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/xmi.to.fsh|current/StructureDefinition/StructureDefinition-Provrelaterad-aktivitet-Aktivitet.json)

### Formal Views of Profile Content

 [Description Differentials, Snapshots, and other representations](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](../StructureDefinition-Provrelaterad-aktivitet-Aktivitet.csv), [Excel](../StructureDefinition-Provrelaterad-aktivitet-Aktivitet.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "Provrelaterad-aktivitet-Aktivitet",
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-type-characteristics",
    "valueCode" : "can-be-target"
  }],
  "url" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Provrelaterad-aktivitet-Aktivitet",
  "version" : "0.1.0",
  "name" : "ProvrelateradaktivitetAktivitet",
  "title" : "Provrelaterad aktivitet: Aktivitet",
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
  "description" : "Klassen Provrelaterad aktivitet håller information om aktiviteter relaterade till hantering av prov.\nInkluderar även t.ex. aktiviteter i samband med transport, frysning, förvaring, bearbetning och delning i sekundärprov.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Provrelaterad-aktivitet-Aktivitet",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "Provrelaterad-aktivitet-Aktivitet",
      "path" : "Provrelaterad-aktivitet-Aktivitet",
      "short" : "Provrelaterad aktivitet: Aktivitet",
      "definition" : "Klassen Provrelaterad aktivitet håller information om aktiviteter relaterade till hantering av prov.\nInkluderar även t.ex. aktiviteter i samband med transport, frysning, förvaring, bearbetning och delning i sekundärprov."
    },
    {
      "id" : "Provrelaterad-aktivitet-Aktivitet.kod",
      "path" : "Provrelaterad-aktivitet-Aktivitet.kod",
      "short" : "Source attribute: kod",
      "definition" : "Kod för provrelaterad aktivitet.\n\nOm kod inte kan anges från nationellt urval kan originalText användas för textalternativ.",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/CV-CWE"
      }]
    },
    {
      "id" : "Provrelaterad-aktivitet-Aktivitet.tid",
      "path" : "Provrelaterad-aktivitet-Aktivitet.tid",
      "short" : "Source attribute: tid",
      "definition" : "Angivelse av tid eller tidsintervall då den provrelaterade aktiviteten utfördes.",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "Provrelaterad-aktivitet-Aktivitet.metod",
      "path" : "Provrelaterad-aktivitet-Aktivitet.metod",
      "short" : "Source attribute: metod",
      "definition" : "Kod för metod för provrelaterad aktivitet.\n\nOm kod inte kan anges från nationellt urval kan originalText användas för textalternativ.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/CV-CWE"
      }]
    },
    {
      "id" : "Provrelaterad-aktivitet-Aktivitet.avser",
      "path" : "Provrelaterad-aktivitet-Aktivitet.avser",
      "short" : "Source attribute: avser",
      "definition" : "Source attribute: avser",
      "min" : 1,
      "max" : "*",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Prov-Resurs"
      }]
    }]
  }
}

```
