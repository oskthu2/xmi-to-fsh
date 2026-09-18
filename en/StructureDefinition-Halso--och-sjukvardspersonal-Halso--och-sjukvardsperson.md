# Hälso- och sjukvårdspersonal : Hälso- och sjukvårdspersonal - Logical Models from Visual Paradigm XMI v0.1.0

## Logical Model: Hälso- och sjukvårdspersonal : Hälso- och sjukvårdspersonal 

 
Klassen hälso- och sjukvårdspersonal håller information om person som i sitt yrke utför hälso- och sjukvård. Hälso- och sjukvårdspersonal är oftast anställd av en vårdgivare. En vårdgivare kan ha anställd hälso- och sjukvårdspersonal, och ibland, som till exempel för enskild näringsidkare, kan rollerna sammanfalla. 

**Usages:**

* Use this Logical Model: [Laboratoriesvar : Dokument](StructureDefinition-Laboratoriesvar-Dokument.md), [Organisatorisk enhet : Organisatorisk enhet](StructureDefinition-Organisatorisk-enhet-Organisatorisk-enhet.md), [Remiss : Dokument](StructureDefinition-Remiss-Dokument.md) and [Signering : Deltagande](StructureDefinition-Signering-Deltagande.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/xmi.to.fsh|current/StructureDefinition/StructureDefinition-Halso--och-sjukvardspersonal-Halso--och-sjukvardsperson.json)

### Formal Views of Profile Content

 [Description Differentials, Snapshots, and other representations](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](../StructureDefinition-Halso--och-sjukvardspersonal-Halso--och-sjukvardsperson.csv), [Excel](../StructureDefinition-Halso--och-sjukvardspersonal-Halso--och-sjukvardsperson.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "Halso--och-sjukvardspersonal-Halso--och-sjukvardsperson",
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-type-characteristics",
    "valueCode" : "can-be-target"
  }],
  "url" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Halso--och-sjukvardspersonal-Halso--och-sjukvardsperson",
  "version" : "0.1.0",
  "name" : "HalsoochsjukvardspersonalHalsoochsjukvardspersonal",
  "title" : "Hälso- och sjukvårdspersonal : Hälso- och sjukvårdspersonal",
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
  "description" : "Klassen hälso- och sjukvårdspersonal håller information om person som i sitt yrke utför hälso- och sjukvård.\nHälso- och sjukvårdspersonal är oftast anställd av en vårdgivare. En vårdgivare kan ha anställd hälso- och sjukvårdspersonal, och ibland, som till exempel för enskild näringsidkare, kan rollerna sammanfalla.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Halso--och-sjukvardspersonal-Halso--och-sjukvardsperson",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "Halso--och-sjukvardspersonal-Halso--och-sjukvardsperson",
      "path" : "Halso--och-sjukvardspersonal-Halso--och-sjukvardsperson",
      "short" : "Hälso- och sjukvårdspersonal : Hälso- och sjukvårdspersonal",
      "definition" : "Klassen hälso- och sjukvårdspersonal håller information om person som i sitt yrke utför hälso- och sjukvård.\nHälso- och sjukvårdspersonal är oftast anställd av en vårdgivare. En vårdgivare kan ha anställd hälso- och sjukvårdspersonal, och ibland, som till exempel för enskild näringsidkare, kan rollerna sammanfalla."
    },
    {
      "id" : "Halso--och-sjukvardspersonal-Halso--och-sjukvardsperson.-id",
      "path" : "Halso--och-sjukvardspersonal-Halso--och-sjukvardsperson._id",
      "short" : "Source attribute: id; renamed from reserved FSH name 'id'",
      "definition" : "Angivelse av identitetsbeteckning för hälso- och sjukvårdspersonal.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/II"
      }]
    },
    {
      "id" : "Halso--och-sjukvardspersonal-Halso--och-sjukvardsperson.namn",
      "path" : "Halso--och-sjukvardspersonal-Halso--och-sjukvardsperson.namn",
      "short" : "Source attribute: namn",
      "definition" : "Angivelse av personnamn sammanslaget enligt formatet \"Mellannamn Efternamn, Förnamn\".\n\nOm flera namn av samma typ förekommer ska dessa separeras med mellanslag.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/ST"
      }]
    },
    {
      "id" : "Halso--och-sjukvardspersonal-Halso--och-sjukvardsperson.befattning",
      "path" : "Halso--och-sjukvardspersonal-Halso--och-sjukvardsperson.befattning",
      "short" : "Source attribute: befattning",
      "definition" : "Kod för hälso- och sjukvårdspersonalens befattning.\nOm möjligt ska KV Befattning användas (notera dock att befattning INTE alltid kan jämställas med roll i detta avseende).\n\nOm kod inte kan anges från nationellt urval kan originalText användas för textalternativ.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/CV-CWE"
      }]
    },
    {
      "id" : "Halso--och-sjukvardspersonal-Halso--och-sjukvardsperson.harMedicinsktAnsvarig",
      "path" : "Halso--och-sjukvardspersonal-Halso--och-sjukvardsperson.harMedicinsktAnsvarig",
      "short" : "Source attribute: har medicinskt ansvarig",
      "definition" : "Source attribute: har medicinskt ansvarig",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Laboratoriesvar-Dokument"
      }]
    },
    {
      "id" : "Halso--och-sjukvardspersonal-Halso--och-sjukvardsperson.utforsAv",
      "path" : "Halso--och-sjukvardspersonal-Halso--och-sjukvardsperson.utforsAv",
      "short" : "Source attribute: utförs av",
      "definition" : "Source attribute: utförs av",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Signering-Deltagande"
      }]
    },
    {
      "id" : "Halso--och-sjukvardspersonal-Halso--och-sjukvardsperson.harRemittent",
      "path" : "Halso--och-sjukvardspersonal-Halso--och-sjukvardsperson.harRemittent",
      "short" : "Source attribute: har remittent",
      "definition" : "Source attribute: har remittent",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Remiss-Dokument"
      }]
    },
    {
      "id" : "Halso--och-sjukvardspersonal-Halso--och-sjukvardsperson.harUppdragFor",
      "path" : "Halso--och-sjukvardspersonal-Halso--och-sjukvardsperson.harUppdragFor",
      "short" : "Source attribute: har uppdrag för",
      "definition" : "Source attribute: har uppdrag för",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Organisatorisk-enhet-Organisatorisk-enhet"
      }]
    }]
  }
}

```
