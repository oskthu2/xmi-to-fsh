# Remiss : Dokument (inom hälso- och sjukvård) - Logical Models from Visual Paradigm XMI v0.1.0

## Logical Model: Remiss : Dokument (inom hälso- och sjukvård) 

 
Supporting logical model generated from gloo4.xmi (source class: Remiss : Dokument (inom hälso- och sjukvård)). 

**Usages:**

* Use this Logical Model: [Laboratorieanalys : Aktivitet (inom hälso- och sjukvård)](StructureDefinition-Laboratorieanalys-Aktivitet-inom-halso--och-sjukvard.md), [: Patient](StructureDefinition-Patient-2.md), [Remissmottagande enhet : Organisation (inom hälso- och sjukvård)](StructureDefinition-Remissmottagande-enhet-Organisation-inom-halso--och-sju.md), [Remissvar : Dokument (inom hälso- och sjukvård)](StructureDefinition-Remissvar-Dokument-inom-halso--och-sjukvard.md) and [Remittent : Hälso- och sjukvårdspersonal](StructureDefinition-Remittent-Halso--och-sjukvardspersonal.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/xmi.to.fsh|current/StructureDefinition/StructureDefinition-Remiss-Dokument-inom-halso--och-sjukvard.json)

### Formal Views of Profile Content

 [Description Differentials, Snapshots, and other representations](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](../StructureDefinition-Remiss-Dokument-inom-halso--och-sjukvard.csv), [Excel](../StructureDefinition-Remiss-Dokument-inom-halso--och-sjukvard.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "Remiss-Dokument-inom-halso--och-sjukvard",
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-type-characteristics",
    "valueCode" : "can-be-target"
  }],
  "url" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Remiss-Dokument-inom-halso--och-sjukvard",
  "version" : "0.1.0",
  "name" : "RemissDokumentinomhalsoochsjukvard",
  "title" : "Remiss : Dokument (inom hälso- och sjukvård)",
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
  "description" : "Supporting logical model generated from gloo4.xmi (source class: Remiss : Dokument (inom hälso- och sjukvård)).",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Remiss-Dokument-inom-halso--och-sjukvard",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "Remiss-Dokument-inom-halso--och-sjukvard",
      "path" : "Remiss-Dokument-inom-halso--och-sjukvard",
      "short" : "Remiss : Dokument (inom hälso- och sjukvård)",
      "definition" : "Supporting logical model generated from gloo4.xmi (source class: Remiss : Dokument (inom hälso- och sjukvård))."
    },
    {
      "id" : "Remiss-Dokument-inom-halso--och-sjukvard.skapar",
      "path" : "Remiss-Dokument-inom-halso--och-sjukvard.skapar",
      "short" : "Source attribute: skapar",
      "definition" : "Source attribute: skapar",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Remittent-Halso--och-sjukvardspersonal"
      }]
    },
    {
      "id" : "Remiss-Dokument-inom-halso--och-sjukvard.hanterasAv",
      "path" : "Remiss-Dokument-inom-halso--och-sjukvard.hanterasAv",
      "short" : "Source attribute: hanteras av",
      "definition" : "Source attribute: hanteras av",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Remissmottagande-enhet-Organisation-inom-halso--och-sju"
      }]
    },
    {
      "id" : "Remiss-Dokument-inom-halso--och-sjukvard.avser",
      "path" : "Remiss-Dokument-inom-halso--och-sjukvard.avser",
      "short" : "Source attribute: avser",
      "definition" : "Source attribute: avser",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Patient-2"
      }]
    },
    {
      "id" : "Remiss-Dokument-inom-halso--och-sjukvard.avserBegaranOmUtforandeAvEnEllerFlera",
      "path" : "Remiss-Dokument-inom-halso--och-sjukvard.avserBegaranOmUtforandeAvEnEllerFlera",
      "short" : "Source attribute: avser begäran om utförande av en eller flera",
      "definition" : "Source attribute: avser begäran om utförande av en eller flera",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Laboratorieanalys-Aktivitet-inom-halso--och-sjukvard"
      }]
    },
    {
      "id" : "Remiss-Dokument-inom-halso--och-sjukvard.kanHa",
      "path" : "Remiss-Dokument-inom-halso--och-sjukvard.kanHa",
      "short" : "Source attribute: kan ha",
      "definition" : "Source attribute: kan ha",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Remissvar-Dokument-inom-halso--och-sjukvard"
      }]
    }]
  }
}

```
