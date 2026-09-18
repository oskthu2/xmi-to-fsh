# : Hälso- och sjukvårdspersonal - Logical Models from Visual Paradigm XMI v0.1.0

## Logical Model: : Hälso- och sjukvårdspersonal 

 
Supporting logical model generated from gloo4.xmi (source class: : Hälso- och sjukvårdspersonal). 

**Usages:**

* Use this Logical Model: [Remittent : Hälso- och sjukvårdspersonal](StructureDefinition-Remittent-Halso--och-sjukvardspersonal.md) and [Signering : Deltagande](StructureDefinition-Signering-Deltagande-2.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/xmi.to.fsh|current/StructureDefinition/StructureDefinition-Halso--och-sjukvardspersonal.json)

### Formal Views of Profile Content

 [Description Differentials, Snapshots, and other representations](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](../StructureDefinition-Halso--och-sjukvardspersonal.csv), [Excel](../StructureDefinition-Halso--och-sjukvardspersonal.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "Halso--och-sjukvardspersonal",
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-type-characteristics",
    "valueCode" : "can-be-target"
  }],
  "url" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Halso--och-sjukvardspersonal",
  "version" : "0.1.0",
  "name" : "Halsoochsjukvardspersonal",
  "title" : ": Hälso- och sjukvårdspersonal",
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
  "description" : "Supporting logical model generated from gloo4.xmi (source class: : Hälso- och sjukvårdspersonal).",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Halso--och-sjukvardspersonal",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "Halso--och-sjukvardspersonal",
      "path" : "Halso--och-sjukvardspersonal",
      "short" : ": Hälso- och sjukvårdspersonal",
      "definition" : "Supporting logical model generated from gloo4.xmi (source class: : Hälso- och sjukvårdspersonal)."
    },
    {
      "id" : "Halso--och-sjukvardspersonal.gorsAv",
      "path" : "Halso--och-sjukvardspersonal.gorsAv",
      "short" : "Source attribute: görs av",
      "definition" : "Source attribute: görs av",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Signering-Deltagande-2"
      }]
    },
    {
      "id" : "Halso--och-sjukvardspersonal.arEn",
      "path" : "Halso--och-sjukvardspersonal.arEn",
      "short" : "Source attribute: är en",
      "definition" : "Source attribute: är en",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Remittent-Halso--och-sjukvardspersonal"
      }]
    }]
  }
}

```
