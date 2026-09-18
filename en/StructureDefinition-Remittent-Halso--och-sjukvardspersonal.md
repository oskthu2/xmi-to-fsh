# Remittent : Hälso- och sjukvårdspersonal - Logical Models from Visual Paradigm XMI v0.1.0

## Logical Model: Remittent : Hälso- och sjukvårdspersonal 

 
Supporting logical model generated from gloo4.xmi (source class: Remittent : Hälso- och sjukvårdspersonal). 

**Usages:**

* Use this Logical Model: [: Hälso- och sjukvårdspersonal](StructureDefinition-Halso--och-sjukvardspersonal.md), [Remiss : Dokument (inom hälso- och sjukvård)](StructureDefinition-Remiss-Dokument-inom-halso--och-sjukvard.md) and [Remitterande enhet : Organisation (inom hälso- och sjukvård)](StructureDefinition-Remitterande-enhet-Organisation-inom-halso--och-sjukvar.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/xmi.to.fsh|current/StructureDefinition/StructureDefinition-Remittent-Halso--och-sjukvardspersonal.json)

### Formal Views of Profile Content

 [Description Differentials, Snapshots, and other representations](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](../StructureDefinition-Remittent-Halso--och-sjukvardspersonal.csv), [Excel](../StructureDefinition-Remittent-Halso--och-sjukvardspersonal.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "Remittent-Halso--och-sjukvardspersonal",
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-type-characteristics",
    "valueCode" : "can-be-target"
  }],
  "url" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Remittent-Halso--och-sjukvardspersonal",
  "version" : "0.1.0",
  "name" : "RemittentHalsoochsjukvardspersonal",
  "title" : "Remittent : Hälso- och sjukvårdspersonal",
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
  "description" : "Supporting logical model generated from gloo4.xmi (source class: Remittent : Hälso- och sjukvårdspersonal).",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Remittent-Halso--och-sjukvardspersonal",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "Remittent-Halso--och-sjukvardspersonal",
      "path" : "Remittent-Halso--och-sjukvardspersonal",
      "short" : "Remittent : Hälso- och sjukvårdspersonal",
      "definition" : "Supporting logical model generated from gloo4.xmi (source class: Remittent : Hälso- och sjukvårdspersonal)."
    },
    {
      "id" : "Remittent-Halso--och-sjukvardspersonal.skapar",
      "path" : "Remittent-Halso--och-sjukvardspersonal.skapar",
      "short" : "Source attribute: skapar",
      "definition" : "Source attribute: skapar",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Remiss-Dokument-inom-halso--och-sjukvard"
      }]
    },
    {
      "id" : "Remittent-Halso--och-sjukvardspersonal.tillhor",
      "path" : "Remittent-Halso--och-sjukvardspersonal.tillhor",
      "short" : "Source attribute: tillhör",
      "definition" : "Source attribute: tillhör",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Remitterande-enhet-Organisation-inom-halso--och-sjukvar"
      }]
    },
    {
      "id" : "Remittent-Halso--och-sjukvardspersonal.arEn",
      "path" : "Remittent-Halso--och-sjukvardspersonal.arEn",
      "short" : "Source attribute: är en",
      "definition" : "Source attribute: är en",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Halso--och-sjukvardspersonal"
      }]
    }]
  }
}

```
