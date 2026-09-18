# Kopiemottagande enhet - Logical Models from Visual Paradigm XMI v0.1.0

## Logical Model: Kopiemottagande enhet 

 
Supporting logical model generated from gloo4.xmi (source class: Kopiemottagande enhet). 

**Usages:**

* Use this Logical Model: [Organisatorisk enhet : Organisation (inom hälso- och sjukvård)](StructureDefinition-Organisatorisk-enhet-Organisation-inom-halso--och-sjukv.md) and [Remissvar : Dokument (inom hälso- och sjukvård)](StructureDefinition-Remissvar-Dokument-inom-halso--och-sjukvard.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/xmi.to.fsh|current/StructureDefinition/StructureDefinition-Kopiemottagande-enhet.json)

### Formal Views of Profile Content

 [Description Differentials, Snapshots, and other representations](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](../StructureDefinition-Kopiemottagande-enhet.csv), [Excel](../StructureDefinition-Kopiemottagande-enhet.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "Kopiemottagande-enhet",
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-type-characteristics",
    "valueCode" : "can-be-target"
  }],
  "url" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Kopiemottagande-enhet",
  "version" : "0.1.0",
  "name" : "Kopiemottagandeenhet",
  "title" : "Kopiemottagande enhet",
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
  "description" : "Supporting logical model generated from gloo4.xmi (source class: Kopiemottagande enhet).",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Kopiemottagande-enhet",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "Kopiemottagande-enhet",
      "path" : "Kopiemottagande-enhet",
      "short" : "Kopiemottagande enhet",
      "definition" : "Supporting logical model generated from gloo4.xmi (source class: Kopiemottagande enhet)."
    },
    {
      "id" : "Kopiemottagande-enhet.tarEmotKopiaAv",
      "path" : "Kopiemottagande-enhet.tarEmotKopiaAv",
      "short" : "Source attribute: tar emot kopia av",
      "definition" : "Source attribute: tar emot kopia av",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Remissvar-Dokument-inom-halso--och-sjukvard"
      }]
    },
    {
      "id" : "Kopiemottagande-enhet.arEn",
      "path" : "Kopiemottagande-enhet.arEn",
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
