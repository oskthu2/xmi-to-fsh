# Remitterande enhet : Organisation (inom hälso- och sjukvård) - Logical Models from Visual Paradigm XMI v0.1.0

## Logical Model: Remitterande enhet : Organisation (inom hälso- och sjukvård) 

 
Supporting logical model generated from gloo4.xmi (source class: Remitterande enhet : Organisation (inom hälso- och sjukvård)). 

**Usages:**

* Use this Logical Model: [Organisatorisk enhet : Organisation (inom hälso- och sjukvård)](StructureDefinition-Organisatorisk-enhet-Organisation-inom-halso--och-sjukv.md) and [Remittent : Hälso- och sjukvårdspersonal](StructureDefinition-Remittent-Halso--och-sjukvardspersonal.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/xmi.to.fsh|current/StructureDefinition/StructureDefinition-Remitterande-enhet-Organisation-inom-halso--och-sjukvar.json)

### Formal Views of Profile Content

 [Description Differentials, Snapshots, and other representations](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](../StructureDefinition-Remitterande-enhet-Organisation-inom-halso--och-sjukvar.csv), [Excel](../StructureDefinition-Remitterande-enhet-Organisation-inom-halso--och-sjukvar.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "Remitterande-enhet-Organisation-inom-halso--och-sjukvar",
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-type-characteristics",
    "valueCode" : "can-be-target"
  }],
  "url" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Remitterande-enhet-Organisation-inom-halso--och-sjukvar",
  "version" : "0.1.0",
  "name" : "RemitterandeenhetOrganisationinomhalsoochsjukvard",
  "title" : "Remitterande enhet : Organisation (inom hälso- och sjukvård)",
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
  "description" : "Supporting logical model generated from gloo4.xmi (source class: Remitterande enhet : Organisation (inom hälso- och sjukvård)).",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Remitterande-enhet-Organisation-inom-halso--och-sjukvar",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "Remitterande-enhet-Organisation-inom-halso--och-sjukvar",
      "path" : "Remitterande-enhet-Organisation-inom-halso--och-sjukvar",
      "short" : "Remitterande enhet : Organisation (inom hälso- och sjukvård)",
      "definition" : "Supporting logical model generated from gloo4.xmi (source class: Remitterande enhet : Organisation (inom hälso- och sjukvård))."
    },
    {
      "id" : "Remitterande-enhet-Organisation-inom-halso--och-sjukvar.tillhor",
      "path" : "Remitterande-enhet-Organisation-inom-halso--och-sjukvar.tillhor",
      "short" : "Source attribute: tillhör",
      "definition" : "Source attribute: tillhör",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Remittent-Halso--och-sjukvardspersonal"
      }]
    },
    {
      "id" : "Remitterande-enhet-Organisation-inom-halso--och-sjukvar.arEn",
      "path" : "Remitterande-enhet-Organisation-inom-halso--och-sjukvar.arEn",
      "short" : "Source attribute: är en",
      "definition" : "Source attribute: är en",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Organisatorisk-enhet-Organisation-inom-halso--och-sjukv"
      }]
    }]
  }
}

```
