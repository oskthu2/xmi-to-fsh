# Utförande enhet : Organisation (inom hälso- och sjukvård) - Logical Models from Visual Paradigm XMI v0.1.0

## Logical Model: Utförande enhet : Organisation (inom hälso- och sjukvård) 

 
Den enhet som utför en enskild analys. 

**Usages:**

* Use this Logical Model: [Laboratorieanalys : Aktivitet (inom hälso- och sjukvård)](StructureDefinition-Laboratorieanalys-Aktivitet-inom-halso--och-sjukvard.md), [Laboratoriesvar : Dokument (inom hälso- och sjukvård)](StructureDefinition-Laboratoriesvar-Dokument-inom-halso--och-sjukvard.md) and [Organisatorisk enhet : Organisation (inom hälso- och sjukvård)](StructureDefinition-Organisatorisk-enhet-Organisation-inom-halso--och-sjukv.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/xmi.to.fsh|current/StructureDefinition/StructureDefinition-Utforande-enhet-Organisation-inom-halso--och-sjukvard.json)

### Formal Views of Profile Content

 [Description Differentials, Snapshots, and other representations](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](../StructureDefinition-Utforande-enhet-Organisation-inom-halso--och-sjukvard.csv), [Excel](../StructureDefinition-Utforande-enhet-Organisation-inom-halso--och-sjukvard.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "Utforande-enhet-Organisation-inom-halso--och-sjukvard",
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-type-characteristics",
    "valueCode" : "can-be-target"
  }],
  "url" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Utforande-enhet-Organisation-inom-halso--och-sjukvard",
  "version" : "0.1.0",
  "name" : "UtforandeenhetOrganisationinomhalsoochsjukvard",
  "title" : "Utförande enhet : Organisation (inom hälso- och sjukvård)",
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
  "description" : "Den enhet som utför en enskild analys.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Utforande-enhet-Organisation-inom-halso--och-sjukvard",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "Utforande-enhet-Organisation-inom-halso--och-sjukvard",
      "path" : "Utforande-enhet-Organisation-inom-halso--och-sjukvard",
      "short" : "Utförande enhet : Organisation (inom hälso- och sjukvård)",
      "definition" : "Den enhet som utför en enskild analys."
    },
    {
      "id" : "Utforande-enhet-Organisation-inom-halso--och-sjukvard.utfor",
      "path" : "Utforande-enhet-Organisation-inom-halso--och-sjukvard.utfor",
      "short" : "Source attribute: utför",
      "definition" : "Source attribute: utför",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Laboratorieanalys-Aktivitet-inom-halso--och-sjukvard"
      }]
    },
    {
      "id" : "Utforande-enhet-Organisation-inom-halso--och-sjukvard.arEn",
      "path" : "Utforande-enhet-Organisation-inom-halso--och-sjukvard.arEn",
      "short" : "Source attribute: är en",
      "definition" : "Source attribute: är en",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Organisatorisk-enhet-Organisation-inom-halso--och-sjukv"
      }]
    },
    {
      "id" : "Utforande-enhet-Organisation-inom-halso--och-sjukvard.skriver",
      "path" : "Utforande-enhet-Organisation-inom-halso--och-sjukvard.skriver",
      "short" : "Source attribute: skriver",
      "definition" : "Source attribute: skriver",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Laboratoriesvar-Dokument-inom-halso--och-sjukvard"
      }]
    }]
  }
}

```
