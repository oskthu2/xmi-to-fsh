# Remissmottagande enhet : Organisation (inom hälso- och sjukvård) - Logical Models from Visual Paradigm XMI v0.1.0

## Logical Model: Remissmottagande enhet : Organisation (inom hälso- och sjukvård) 

 
Supporting logical model generated from gloo4.xmi (source class: Remissmottagande enhet : Organisation (inom hälso- och sjukvård)). 

**Usages:**

* Use this Logical Model: [Organisatorisk enhet : Organisation (inom hälso- och sjukvård)](StructureDefinition-Organisatorisk-enhet-Organisation-inom-halso--och-sjukv.md) and [Remiss : Dokument (inom hälso- och sjukvård)](StructureDefinition-Remiss-Dokument-inom-halso--och-sjukvard.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/xmi.to.fsh|current/StructureDefinition/StructureDefinition-Remissmottagande-enhet-Organisation-inom-halso--och-sju.json)

### Formal Views of Profile Content

 [Description Differentials, Snapshots, and other representations](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](../StructureDefinition-Remissmottagande-enhet-Organisation-inom-halso--och-sju.csv), [Excel](../StructureDefinition-Remissmottagande-enhet-Organisation-inom-halso--och-sju.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "Remissmottagande-enhet-Organisation-inom-halso--och-sju",
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-type-characteristics",
    "valueCode" : "can-be-target"
  }],
  "url" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Remissmottagande-enhet-Organisation-inom-halso--och-sju",
  "version" : "0.1.0",
  "name" : "RemissmottagandeenhetOrganisationinomhalsoochsjukvard",
  "title" : "Remissmottagande enhet : Organisation (inom hälso- och sjukvård)",
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
  "description" : "Supporting logical model generated from gloo4.xmi (source class: Remissmottagande enhet : Organisation (inom hälso- och sjukvård)).",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Remissmottagande-enhet-Organisation-inom-halso--och-sju",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "Remissmottagande-enhet-Organisation-inom-halso--och-sju",
      "path" : "Remissmottagande-enhet-Organisation-inom-halso--och-sju",
      "short" : "Remissmottagande enhet : Organisation (inom hälso- och sjukvård)",
      "definition" : "Supporting logical model generated from gloo4.xmi (source class: Remissmottagande enhet : Organisation (inom hälso- och sjukvård))."
    },
    {
      "id" : "Remissmottagande-enhet-Organisation-inom-halso--och-sju.arEn",
      "path" : "Remissmottagande-enhet-Organisation-inom-halso--och-sju.arEn",
      "short" : "Source attribute: är en",
      "definition" : "Source attribute: är en",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Organisatorisk-enhet-Organisation-inom-halso--och-sjukv"
      }]
    },
    {
      "id" : "Remissmottagande-enhet-Organisation-inom-halso--och-sju.hanterasAv",
      "path" : "Remissmottagande-enhet-Organisation-inom-halso--och-sju.hanterasAv",
      "short" : "Source attribute: hanteras av",
      "definition" : "Source attribute: hanteras av",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Remiss-Dokument-inom-halso--och-sjukvard"
      }]
    }]
  }
}

```
