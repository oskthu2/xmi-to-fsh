# Remiss : Dokument - Logical Models from Visual Paradigm XMI v0.1.0

## Logical Model: Remiss : Dokument 

 
Supporting logical model generated from gloo4.xmi (source class: Remiss : Dokument). 

**Usages:**

* Use this Logical Model: [Hälso- och sjukvårdspersonal : Hälso- och sjukvårdspersonal](StructureDefinition-Halso--och-sjukvardspersonal-Halso--och-sjukvardsperson.md) and [Laboratoriesvar : Dokument](StructureDefinition-Laboratoriesvar-Dokument.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/xmi.to.fsh|current/StructureDefinition/StructureDefinition-Remiss-Dokument.json)

### Formal Views of Profile Content

 [Description Differentials, Snapshots, and other representations](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](../StructureDefinition-Remiss-Dokument.csv), [Excel](../StructureDefinition-Remiss-Dokument.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "Remiss-Dokument",
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-type-characteristics",
    "valueCode" : "can-be-target"
  }],
  "url" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Remiss-Dokument",
  "version" : "0.1.0",
  "name" : "RemissDokument",
  "title" : "Remiss : Dokument",
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
  "description" : "Supporting logical model generated from gloo4.xmi (source class: Remiss : Dokument).",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Remiss-Dokument",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "Remiss-Dokument",
      "path" : "Remiss-Dokument",
      "short" : "Remiss : Dokument",
      "definition" : "Supporting logical model generated from gloo4.xmi (source class: Remiss : Dokument)."
    },
    {
      "id" : "Remiss-Dokument.remissId",
      "path" : "Remiss-Dokument.remissId",
      "short" : "Source attribute: remiss-id",
      "definition" : "Source attribute: remiss-id",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/II"
      }]
    },
    {
      "id" : "Remiss-Dokument.remisstidpunkt",
      "path" : "Remiss-Dokument.remisstidpunkt",
      "short" : "Source attribute: remisstidpunkt",
      "definition" : "Source attribute: remisstidpunkt",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/TS"
      }]
    },
    {
      "id" : "Remiss-Dokument.versionsnummer",
      "path" : "Remiss-Dokument.versionsnummer",
      "short" : "Source attribute: versionsnummer",
      "definition" : "Source attribute: versionsnummer",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/INT"
      }]
    },
    {
      "id" : "Remiss-Dokument.fragestallning",
      "path" : "Remiss-Dokument.fragestallning",
      "short" : "Source attribute: frågeställning",
      "definition" : "Source attribute: frågeställning",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/ST"
      }]
    },
    {
      "id" : "Remiss-Dokument.efterfragadTjanst",
      "path" : "Remiss-Dokument.efterfragadTjanst",
      "short" : "Source attribute: efterfrågad tjänst",
      "definition" : "Source attribute: efterfrågad tjänst",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/CV-CWE"
      }]
    },
    {
      "id" : "Remiss-Dokument.kommentarFranBestallare",
      "path" : "Remiss-Dokument.kommentarFranBestallare",
      "short" : "Source attribute: kommentar från beställare",
      "definition" : "Source attribute: kommentar från beställare",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/ST"
      }]
    },
    {
      "id" : "Remiss-Dokument.medicinskInformation",
      "path" : "Remiss-Dokument.medicinskInformation",
      "short" : "Source attribute: medicinsk information",
      "definition" : "Source attribute: medicinsk information",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/ST"
      }]
    },
    {
      "id" : "Remiss-Dokument.besvarar",
      "path" : "Remiss-Dokument.besvarar",
      "short" : "Source attribute: besvarar",
      "definition" : "Source attribute: besvarar",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Laboratoriesvar-Dokument"
      }]
    },
    {
      "id" : "Remiss-Dokument.harRemittent",
      "path" : "Remiss-Dokument.harRemittent",
      "short" : "Source attribute: har remittent",
      "definition" : "Source attribute: har remittent",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Halso--och-sjukvardspersonal-Halso--och-sjukvardsperson"
      }]
    }]
  }
}

```
