# Remissvarsmottagande enhet : Organisation (inom hälso- och sjukvård) - gloo4 v0.1.0

## Logical Model: Remissvarsmottagande enhet : Organisation (inom hälso- och sjukvård) 

 
Den organisatoriska enhet som ett remissvar skickas till. 
Är vanligtvis samma organisatoriska enhet som den remitterande enheten. 

**Usages:**

* Use this Logical Model: [Organisatorisk enhet : Organisation (inom hälso- och sjukvård)](StructureDefinition-Organisatorisk-enhet-Organisation-inom-halso--och-sjukv.md) and [Remissvar : Dokument (inom hälso- och sjukvård)](StructureDefinition-Remissvar-Dokument-inom-halso--och-sjukvard.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/gloo4|current/StructureDefinition/StructureDefinition-Remissvarsmottagande-enhet-Organisation-inom-halso--och.json)

### Formal Views of Profile Content

 [Description Differentials, Snapshots, and other representations](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](../StructureDefinition-Remissvarsmottagande-enhet-Organisation-inom-halso--och.csv), [Excel](../StructureDefinition-Remissvarsmottagande-enhet-Organisation-inom-halso--och.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "Remissvarsmottagande-enhet-Organisation-inom-halso--och",
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-type-characteristics",
    "valueCode" : "can-be-target"
  }],
  "url" : "http://example.org/fhir/gloo4/StructureDefinition/Remissvarsmottagande-enhet-Organisation-inom-halso--och",
  "version" : "0.1.0",
  "name" : "RemissvarsmottagandeenhetOrganisationinomhalsoochsjukvard",
  "title" : "Remissvarsmottagande enhet : Organisation (inom hälso- och sjukvård)",
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
  "description" : "Den organisatoriska enhet som ett remissvar skickas till.\n\nÄr vanligtvis samma organisatoriska enhet som den remitterande enheten.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://example.org/fhir/gloo4/StructureDefinition/Remissvarsmottagande-enhet-Organisation-inom-halso--och",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "Remissvarsmottagande-enhet-Organisation-inom-halso--och",
      "path" : "Remissvarsmottagande-enhet-Organisation-inom-halso--och",
      "short" : "Remissvarsmottagande enhet : Organisation (inom hälso- och sjukvård)",
      "definition" : "Den organisatoriska enhet som ett remissvar skickas till.\n\nÄr vanligtvis samma organisatoriska enhet som den remitterande enheten."
    },
    {
      "id" : "Remissvarsmottagande-enhet-Organisation-inom-halso--och.arMottagareAv",
      "path" : "Remissvarsmottagande-enhet-Organisation-inom-halso--och.arMottagareAv",
      "short" : "Source attribute: är mottagare av",
      "definition" : "Source attribute: är mottagare av",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/gloo4/StructureDefinition/Remissvar-Dokument-inom-halso--och-sjukvard"
      }]
    },
    {
      "id" : "Remissvarsmottagande-enhet-Organisation-inom-halso--och.arEn",
      "path" : "Remissvarsmottagande-enhet-Organisation-inom-halso--och.arEn",
      "short" : "Source attribute: är en",
      "definition" : "Source attribute: är en",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/gloo4/StructureDefinition/Organisatorisk-enhet-Organisation-inom-halso--och-sjukv"
      }]
    }]
  }
}

```
