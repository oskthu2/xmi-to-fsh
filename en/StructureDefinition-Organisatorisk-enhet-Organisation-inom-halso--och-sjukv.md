# Organisatorisk enhet : Organisation (inom hälso- och sjukvård) - Logical Models from Visual Paradigm XMI v0.1.0

## Logical Model: Organisatorisk enhet : Organisation (inom hälso- och sjukvård) 

 
Supporting logical model generated from gloo4.xmi (source class: Organisatorisk enhet : Organisation (inom hälso- och sjukvård)). 

**Usages:**

* Use this Logical Model: [Ansvarig enhet : Organisation (inom hälso- och sjukvård)](StructureDefinition-Ansvarig-enhet-Organisation-inom-halso--och-sjukvard.md), [Kopiemottagande enhet](StructureDefinition-Kopiemottagande-enhet.md), [Remissmottagande enhet : Organisation (inom hälso- och sjukvård)](StructureDefinition-Remissmottagande-enhet-Organisation-inom-halso--och-sju.md), [Remissvarsmottagande enhet : Organisation (inom hälso- och sjukvård)](StructureDefinition-Remissvarsmottagande-enhet-Organisation-inom-halso--och.md)... Show 2 more, [Remitterande enhet : Organisation (inom hälso- och sjukvård)](StructureDefinition-Remitterande-enhet-Organisation-inom-halso--och-sjukvar.md) and [Utförande enhet : Organisation (inom hälso- och sjukvård)](StructureDefinition-Utforande-enhet-Organisation-inom-halso--och-sjukvard.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/xmi.to.fsh|current/StructureDefinition/StructureDefinition-Organisatorisk-enhet-Organisation-inom-halso--och-sjukv.json)

### Formal Views of Profile Content

 [Description Differentials, Snapshots, and other representations](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](../StructureDefinition-Organisatorisk-enhet-Organisation-inom-halso--och-sjukv.csv), [Excel](../StructureDefinition-Organisatorisk-enhet-Organisation-inom-halso--och-sjukv.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "Organisatorisk-enhet-Organisation-inom-halso--och-sjukv",
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-type-characteristics",
    "valueCode" : "can-be-target"
  }],
  "url" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Organisatorisk-enhet-Organisation-inom-halso--och-sjukv",
  "version" : "0.1.0",
  "name" : "OrganisatoriskenhetOrganisationinomhalsoochsjukvard",
  "title" : "Organisatorisk enhet : Organisation (inom hälso- och sjukvård)",
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
  "description" : "Supporting logical model generated from gloo4.xmi (source class: Organisatorisk enhet : Organisation (inom hälso- och sjukvård)).",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Organisatorisk-enhet-Organisation-inom-halso--och-sjukv",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "Organisatorisk-enhet-Organisation-inom-halso--och-sjukv",
      "path" : "Organisatorisk-enhet-Organisation-inom-halso--och-sjukv",
      "short" : "Organisatorisk enhet : Organisation (inom hälso- och sjukvård)",
      "definition" : "Supporting logical model generated from gloo4.xmi (source class: Organisatorisk enhet : Organisation (inom hälso- och sjukvård))."
    },
    {
      "id" : "Organisatorisk-enhet-Organisation-inom-halso--och-sjukv.arEn",
      "path" : "Organisatorisk-enhet-Organisation-inom-halso--och-sjukv.arEn",
      "short" : "Source attribute: är en",
      "definition" : "Source attribute: är en",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Remissvarsmottagande-enhet-Organisation-inom-halso--och"
      }]
    },
    {
      "id" : "Organisatorisk-enhet-Organisation-inom-halso--och-sjukv.arEn2",
      "path" : "Organisatorisk-enhet-Organisation-inom-halso--och-sjukv.arEn2",
      "short" : "Source attribute: är en",
      "definition" : "Source attribute: är en",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Kopiemottagande-enhet"
      }]
    },
    {
      "id" : "Organisatorisk-enhet-Organisation-inom-halso--och-sjukv.arEn3",
      "path" : "Organisatorisk-enhet-Organisation-inom-halso--och-sjukv.arEn3",
      "short" : "Source attribute: är en",
      "definition" : "Source attribute: är en",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Ansvarig-enhet-Organisation-inom-halso--och-sjukvard"
      }]
    },
    {
      "id" : "Organisatorisk-enhet-Organisation-inom-halso--och-sjukv.arEn4",
      "path" : "Organisatorisk-enhet-Organisation-inom-halso--och-sjukv.arEn4",
      "short" : "Source attribute: är en",
      "definition" : "Source attribute: är en",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Utforande-enhet-Organisation-inom-halso--och-sjukvard"
      }]
    },
    {
      "id" : "Organisatorisk-enhet-Organisation-inom-halso--och-sjukv.arEn5",
      "path" : "Organisatorisk-enhet-Organisation-inom-halso--och-sjukv.arEn5",
      "short" : "Source attribute: är en",
      "definition" : "Source attribute: är en",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Remissmottagande-enhet-Organisation-inom-halso--och-sju"
      }]
    },
    {
      "id" : "Organisatorisk-enhet-Organisation-inom-halso--och-sjukv.arEn6",
      "path" : "Organisatorisk-enhet-Organisation-inom-halso--och-sjukv.arEn6",
      "short" : "Source attribute: är en",
      "definition" : "Source attribute: är en",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Remitterande-enhet-Organisation-inom-halso--och-sjukvar"
      }]
    }]
  }
}

```
