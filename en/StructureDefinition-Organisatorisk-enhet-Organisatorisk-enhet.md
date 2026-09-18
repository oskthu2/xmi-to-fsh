# Organisatorisk enhet : Organisatorisk enhet - Logical Models from Visual Paradigm XMI v0.1.0

## Logical Model: Organisatorisk enhet : Organisatorisk enhet 

 
Supporting logical model generated from gloo4.xmi (source class: Organisatorisk enhet : Organisatorisk enhet). 

**Usages:**

* Use this Logical Model: [Hälso- och sjukvårdspersonal : Hälso- och sjukvårdspersonal](StructureDefinition-Halso--och-sjukvardspersonal-Halso--och-sjukvardsperson.md), [Laboratorieanalys : Aktivitet](StructureDefinition-Laboratorieanalys-Aktivitet.md) and [Laboratoriesvar : Dokument](StructureDefinition-Laboratoriesvar-Dokument.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/xmi.to.fsh|current/StructureDefinition/StructureDefinition-Organisatorisk-enhet-Organisatorisk-enhet.json)

### Formal Views of Profile Content

 [Description Differentials, Snapshots, and other representations](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](../StructureDefinition-Organisatorisk-enhet-Organisatorisk-enhet.csv), [Excel](../StructureDefinition-Organisatorisk-enhet-Organisatorisk-enhet.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "Organisatorisk-enhet-Organisatorisk-enhet",
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-type-characteristics",
    "valueCode" : "can-be-target"
  }],
  "url" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Organisatorisk-enhet-Organisatorisk-enhet",
  "version" : "0.1.0",
  "name" : "OrganisatoriskenhetOrganisatoriskenhet",
  "title" : "Organisatorisk enhet : Organisatorisk enhet",
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
  "description" : "Supporting logical model generated from gloo4.xmi (source class: Organisatorisk enhet : Organisatorisk enhet).",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Organisatorisk-enhet-Organisatorisk-enhet",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "Organisatorisk-enhet-Organisatorisk-enhet",
      "path" : "Organisatorisk-enhet-Organisatorisk-enhet",
      "short" : "Organisatorisk enhet : Organisatorisk enhet",
      "definition" : "Supporting logical model generated from gloo4.xmi (source class: Organisatorisk enhet : Organisatorisk enhet)."
    },
    {
      "id" : "Organisatorisk-enhet-Organisatorisk-enhet.-id",
      "path" : "Organisatorisk-enhet-Organisatorisk-enhet._id",
      "short" : "Source attribute: id; renamed from reserved FSH name 'id'",
      "definition" : "Source attribute: id; renamed from reserved FSH name 'id'",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/II"
      }]
    },
    {
      "id" : "Organisatorisk-enhet-Organisatorisk-enhet.namn",
      "path" : "Organisatorisk-enhet-Organisatorisk-enhet.namn",
      "short" : "Source attribute: namn",
      "definition" : "Source attribute: namn",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/ST"
      }]
    },
    {
      "id" : "Organisatorisk-enhet-Organisatorisk-enhet.typAvVerksamhet",
      "path" : "Organisatorisk-enhet-Organisatorisk-enhet.typAvVerksamhet",
      "short" : "Source attribute: typ av verksamhet",
      "definition" : "Source attribute: typ av verksamhet",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/CV"
      }]
    },
    {
      "id" : "Organisatorisk-enhet-Organisatorisk-enhet.arAnsvarigForInnehalletI",
      "path" : "Organisatorisk-enhet-Organisatorisk-enhet.arAnsvarigForInnehalletI",
      "short" : "Source attribute: är ansvarig för innehållet i",
      "definition" : "Source attribute: är ansvarig för innehållet i",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Laboratoriesvar-Dokument"
      }]
    },
    {
      "id" : "Organisatorisk-enhet-Organisatorisk-enhet.harSvarsmottagande",
      "path" : "Organisatorisk-enhet-Organisatorisk-enhet.harSvarsmottagande",
      "short" : "Source attribute: har svarsmottagande",
      "definition" : "Source attribute: har svarsmottagande",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Laboratoriesvar-Dokument"
      }]
    },
    {
      "id" : "Organisatorisk-enhet-Organisatorisk-enhet.harUtforande",
      "path" : "Organisatorisk-enhet-Organisatorisk-enhet.harUtforande",
      "short" : "Source attribute: har utförande",
      "definition" : "Source attribute: har utförande",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Laboratorieanalys-Aktivitet"
      }]
    },
    {
      "id" : "Organisatorisk-enhet-Organisatorisk-enhet.harUppdragFor",
      "path" : "Organisatorisk-enhet-Organisatorisk-enhet.harUppdragFor",
      "short" : "Source attribute: har uppdrag för",
      "definition" : "Source attribute: har uppdrag för",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Halso--och-sjukvardspersonal-Halso--och-sjukvardsperson"
      }]
    }]
  }
}

```
