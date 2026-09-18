# Ansvarig enhet : Organisation (inom hälso- och sjukvård) - gloo4 v0.1.0

## Logical Model: Ansvarig enhet : Organisation (inom hälso- och sjukvård) 

 
Den enhet som ansvarar för innehållet i laboratoriesvaret. 

**Usages:**

* Use this Logical Model: [Laboratoriesvar : Dokument (inom hälso- och sjukvård)](StructureDefinition-Laboratoriesvar-Dokument-inom-halso--och-sjukvard.md), [Organisatorisk enhet : Organisation (inom hälso- och sjukvård)](StructureDefinition-Organisatorisk-enhet-Organisation-inom-halso--och-sjukv.md) and [Remissvar : Dokument (inom hälso- och sjukvård)](StructureDefinition-Remissvar-Dokument-inom-halso--och-sjukvard.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/gloo4|current/StructureDefinition/StructureDefinition-Ansvarig-enhet-Organisation-inom-halso--och-sjukvard.json)

### Formal Views of Profile Content

 [Description Differentials, Snapshots, and other representations](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](../StructureDefinition-Ansvarig-enhet-Organisation-inom-halso--och-sjukvard.csv), [Excel](../StructureDefinition-Ansvarig-enhet-Organisation-inom-halso--och-sjukvard.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "Ansvarig-enhet-Organisation-inom-halso--och-sjukvard",
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-type-characteristics",
    "valueCode" : "can-be-target"
  }],
  "url" : "http://example.org/fhir/gloo4/StructureDefinition/Ansvarig-enhet-Organisation-inom-halso--och-sjukvard",
  "version" : "0.1.0",
  "name" : "AnsvarigenhetOrganisationinomhalsoochsjukvard",
  "title" : "Ansvarig enhet : Organisation (inom hälso- och sjukvård)",
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
  "description" : "Den enhet som ansvarar för innehållet i laboratoriesvaret.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://example.org/fhir/gloo4/StructureDefinition/Ansvarig-enhet-Organisation-inom-halso--och-sjukvard",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "Ansvarig-enhet-Organisation-inom-halso--och-sjukvard",
      "path" : "Ansvarig-enhet-Organisation-inom-halso--och-sjukvard",
      "short" : "Ansvarig enhet : Organisation (inom hälso- och sjukvård)",
      "definition" : "Den enhet som ansvarar för innehållet i laboratoriesvaret."
    },
    {
      "id" : "Ansvarig-enhet-Organisation-inom-halso--och-sjukvard.ansvararFor",
      "path" : "Ansvarig-enhet-Organisation-inom-halso--och-sjukvard.ansvararFor",
      "short" : "Source attribute: ansvarar för",
      "definition" : "Source attribute: ansvarar för",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/gloo4/StructureDefinition/Remissvar-Dokument-inom-halso--och-sjukvard"
      }]
    },
    {
      "id" : "Ansvarig-enhet-Organisation-inom-halso--och-sjukvard.arEn",
      "path" : "Ansvarig-enhet-Organisation-inom-halso--och-sjukvard.arEn",
      "short" : "Source attribute: är en",
      "definition" : "Source attribute: är en",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/gloo4/StructureDefinition/Organisatorisk-enhet-Organisation-inom-halso--och-sjukv"
      }]
    },
    {
      "id" : "Ansvarig-enhet-Organisation-inom-halso--och-sjukvard.ansvararFor2",
      "path" : "Ansvarig-enhet-Organisation-inom-halso--och-sjukvard.ansvararFor2",
      "short" : "Source attribute: ansvarar för",
      "definition" : "Source attribute: ansvarar för",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/gloo4/StructureDefinition/Laboratoriesvar-Dokument-inom-halso--och-sjukvard"
      }]
    }]
  }
}

```
