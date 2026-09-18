# Laboratoriesvar : Dokument (inom hälso- och sjukvård) - Logical Models from Visual Paradigm XMI v0.1.0

## Logical Model: Laboratoriesvar : Dokument (inom hälso- och sjukvård) 

 
Supporting logical model generated from gloo4.xmi (source class: Laboratoriesvar : Dokument (inom hälso- och sjukvård)). 

**Usages:**

* Use this Logical Model: [Ansvarig enhet : Organisation (inom hälso- och sjukvård)](StructureDefinition-Ansvarig-enhet-Organisation-inom-halso--och-sjukvard.md), [Laboratorieanalysresultat : Observerat hälsotillstånd](StructureDefinition-Laboratorieanalysresultat-Observerat-halsotillstand.md), [Remissvar : Dokument (inom hälso- och sjukvård)](StructureDefinition-Remissvar-Dokument-inom-halso--och-sjukvard.md) and [Utförande enhet : Organisation (inom hälso- och sjukvård)](StructureDefinition-Utforande-enhet-Organisation-inom-halso--och-sjukvard.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/xmi.to.fsh|current/StructureDefinition/StructureDefinition-Laboratoriesvar-Dokument-inom-halso--och-sjukvard.json)

### Formal Views of Profile Content

 [Description Differentials, Snapshots, and other representations](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](../StructureDefinition-Laboratoriesvar-Dokument-inom-halso--och-sjukvard.csv), [Excel](../StructureDefinition-Laboratoriesvar-Dokument-inom-halso--och-sjukvard.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "Laboratoriesvar-Dokument-inom-halso--och-sjukvard",
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-type-characteristics",
    "valueCode" : "can-be-target"
  }],
  "url" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Laboratoriesvar-Dokument-inom-halso--och-sjukvard",
  "version" : "0.1.0",
  "name" : "LaboratoriesvarDokumentinomhalsoochsjukvard",
  "title" : "Laboratoriesvar : Dokument (inom hälso- och sjukvård)",
  "status" : "draft",
  "date" : "2026-09-18T09:59:15+00:00",
  "publisher" : "xmi-to-fsh",
  "contact" : [{
    "name" : "xmi-to-fsh",
    "telecom" : [{
      "system" : "url",
      "value" : "https://github.com/oskthu2/xmi-to-fsh"
    }]
  }],
  "description" : "Supporting logical model generated from gloo4.xmi (source class: Laboratoriesvar : Dokument (inom hälso- och sjukvård)).",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Laboratoriesvar-Dokument-inom-halso--och-sjukvard",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "Laboratoriesvar-Dokument-inom-halso--och-sjukvard",
      "path" : "Laboratoriesvar-Dokument-inom-halso--och-sjukvard",
      "short" : "Laboratoriesvar : Dokument (inom hälso- och sjukvård)",
      "definition" : "Supporting logical model generated from gloo4.xmi (source class: Laboratoriesvar : Dokument (inom hälso- och sjukvård))."
    },
    {
      "id" : "Laboratoriesvar-Dokument-inom-halso--och-sjukvard.ansvararFor",
      "path" : "Laboratoriesvar-Dokument-inom-halso--och-sjukvard.ansvararFor",
      "short" : "Source attribute: ansvarar för",
      "definition" : "Source attribute: ansvarar för",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Ansvarig-enhet-Organisation-inom-halso--och-sjukvard"
      }]
    },
    {
      "id" : "Laboratoriesvar-Dokument-inom-halso--och-sjukvard.skriver",
      "path" : "Laboratoriesvar-Dokument-inom-halso--och-sjukvard.skriver",
      "short" : "Source attribute: skriver",
      "definition" : "Source attribute: skriver",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Utforande-enhet-Organisation-inom-halso--och-sjukvard"
      }]
    },
    {
      "id" : "Laboratoriesvar-Dokument-inom-halso--och-sjukvard.arEtt",
      "path" : "Laboratoriesvar-Dokument-inom-halso--och-sjukvard.arEtt",
      "short" : "Source attribute: är ett",
      "definition" : "Source attribute: är ett",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Remissvar-Dokument-inom-halso--och-sjukvard"
      }]
    },
    {
      "id" : "Laboratoriesvar-Dokument-inom-halso--och-sjukvard.innehaller",
      "path" : "Laboratoriesvar-Dokument-inom-halso--och-sjukvard.innehaller",
      "short" : "Source attribute: innehåller",
      "definition" : "Source attribute: innehåller",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Laboratorieanalysresultat-Observerat-halsotillstand"
      }]
    }]
  }
}

```
