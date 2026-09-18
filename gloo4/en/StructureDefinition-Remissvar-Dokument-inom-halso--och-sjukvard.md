# Remissvar : Dokument (inom hälso- och sjukvård) - gloo4 v0.1.0

## Logical Model: Remissvar : Dokument (inom hälso- och sjukvård) 

 
Det som kommuniceras till remittenten efter att en remiss har bedömts och den remissmottagande enheten har accepterat att hantera det som frågeställningen avser. 
Det kan röra sig om ett svar på frågeställning i remissen men också vara en redogörelse för att en eller flera önskade åtgärder har utförts. 
 [Projektet e-remiss, "Remissvar"] 

**Usages:**

* Use this Logical Model: [Ansvarig enhet : Organisation (inom hälso- och sjukvård)](StructureDefinition-Ansvarig-enhet-Organisation-inom-halso--och-sjukvard.md), [Delsvar : Dokument (inom hälso- och sjukvård)](StructureDefinition-Delsvar-Dokument-inom-halso--och-sjukvard.md), [Kopiemottagande enhet](StructureDefinition-Kopiemottagande-enhet.md), [Laboratoriesvar : Dokument (inom hälso- och sjukvård)](StructureDefinition-Laboratoriesvar-Dokument-inom-halso--och-sjukvard.md)... Show 5 more, [Presentationsformat](StructureDefinition-Presentationsformat.md), [Remiss : Dokument (inom hälso- och sjukvård)](StructureDefinition-Remiss-Dokument-inom-halso--och-sjukvard.md), [Remissvarsmottagande enhet : Organisation (inom hälso- och sjukvård)](StructureDefinition-Remissvarsmottagande-enhet-Organisation-inom-halso--och.md), [Signering : Deltagande](StructureDefinition-Signering-Deltagande-2.md) and [Slutsvar : Dokument (inom hälso- och sjukvård)](StructureDefinition-Slutsvar-Dokument-inom-halso--och-sjukvard.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/gloo4|current/StructureDefinition/StructureDefinition-Remissvar-Dokument-inom-halso--och-sjukvard.json)

### Formal Views of Profile Content

 [Description Differentials, Snapshots, and other representations](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](../StructureDefinition-Remissvar-Dokument-inom-halso--och-sjukvard.csv), [Excel](../StructureDefinition-Remissvar-Dokument-inom-halso--och-sjukvard.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "Remissvar-Dokument-inom-halso--och-sjukvard",
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-type-characteristics",
    "valueCode" : "can-be-target"
  }],
  "url" : "http://example.org/fhir/gloo4/StructureDefinition/Remissvar-Dokument-inom-halso--och-sjukvard",
  "version" : "0.1.0",
  "name" : "RemissvarDokumentinomhalsoochsjukvard",
  "title" : "Remissvar : Dokument (inom hälso- och sjukvård)",
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
  "description" : "Det som kommuniceras till remittenten efter att en remiss har bedömts och den remissmottagande enheten har accepterat att hantera det som frågeställningen avser.\n\nDet kan röra sig om ett svar på frågeställning i remissen men också vara en redogörelse för att en eller flera önskade åtgärder har utförts.   \n[Projektet e-remiss, \"Remissvar\"]",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://example.org/fhir/gloo4/StructureDefinition/Remissvar-Dokument-inom-halso--och-sjukvard",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "Remissvar-Dokument-inom-halso--och-sjukvard",
      "path" : "Remissvar-Dokument-inom-halso--och-sjukvard",
      "short" : "Remissvar : Dokument (inom hälso- och sjukvård)",
      "definition" : "Det som kommuniceras till remittenten efter att en remiss har bedömts och den remissmottagande enheten har accepterat att hantera det som frågeställningen avser.\n\nDet kan röra sig om ett svar på frågeställning i remissen men också vara en redogörelse för att en eller flera önskade åtgärder har utförts.   \n[Projektet e-remiss, \"Remissvar\"]"
    },
    {
      "id" : "Remissvar-Dokument-inom-halso--och-sjukvard.gorsAv",
      "path" : "Remissvar-Dokument-inom-halso--och-sjukvard.gorsAv",
      "short" : "Source attribute: görs av",
      "definition" : "Source attribute: görs av",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/gloo4/StructureDefinition/Signering-Deltagande-2"
      }]
    },
    {
      "id" : "Remissvar-Dokument-inom-halso--och-sjukvard.harVisst",
      "path" : "Remissvar-Dokument-inom-halso--och-sjukvard.harVisst",
      "short" : "Source attribute: har visst",
      "definition" : "Source attribute: har visst",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/gloo4/StructureDefinition/Presentationsformat"
      }]
    },
    {
      "id" : "Remissvar-Dokument-inom-halso--och-sjukvard.arMottagareAv",
      "path" : "Remissvar-Dokument-inom-halso--och-sjukvard.arMottagareAv",
      "short" : "Source attribute: är mottagare av",
      "definition" : "Source attribute: är mottagare av",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/gloo4/StructureDefinition/Remissvarsmottagande-enhet-Organisation-inom-halso--och"
      }]
    },
    {
      "id" : "Remissvar-Dokument-inom-halso--och-sjukvard.tarEmotKopiaAv",
      "path" : "Remissvar-Dokument-inom-halso--och-sjukvard.tarEmotKopiaAv",
      "short" : "Source attribute: tar emot kopia av",
      "definition" : "Source attribute: tar emot kopia av",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/gloo4/StructureDefinition/Kopiemottagande-enhet"
      }]
    },
    {
      "id" : "Remissvar-Dokument-inom-halso--och-sjukvard.ansvararFor",
      "path" : "Remissvar-Dokument-inom-halso--och-sjukvard.ansvararFor",
      "short" : "Source attribute: ansvarar för",
      "definition" : "Source attribute: ansvarar för",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/gloo4/StructureDefinition/Ansvarig-enhet-Organisation-inom-halso--och-sjukvard"
      }]
    },
    {
      "id" : "Remissvar-Dokument-inom-halso--och-sjukvard.kanHa",
      "path" : "Remissvar-Dokument-inom-halso--och-sjukvard.kanHa",
      "short" : "Source attribute: kan ha",
      "definition" : "Source attribute: kan ha",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/gloo4/StructureDefinition/Remiss-Dokument-inom-halso--och-sjukvard"
      }]
    },
    {
      "id" : "Remissvar-Dokument-inom-halso--och-sjukvard.arEtt",
      "path" : "Remissvar-Dokument-inom-halso--och-sjukvard.arEtt",
      "short" : "Source attribute: är ett",
      "definition" : "Source attribute: är ett",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/gloo4/StructureDefinition/Delsvar-Dokument-inom-halso--och-sjukvard"
      }]
    },
    {
      "id" : "Remissvar-Dokument-inom-halso--och-sjukvard.arEtt2",
      "path" : "Remissvar-Dokument-inom-halso--och-sjukvard.arEtt2",
      "short" : "Source attribute: är ett",
      "definition" : "Source attribute: är ett",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/gloo4/StructureDefinition/Slutsvar-Dokument-inom-halso--och-sjukvard"
      }]
    },
    {
      "id" : "Remissvar-Dokument-inom-halso--och-sjukvard.arEtt3",
      "path" : "Remissvar-Dokument-inom-halso--och-sjukvard.arEtt3",
      "short" : "Source attribute: är ett",
      "definition" : "Source attribute: är ett",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/gloo4/StructureDefinition/Laboratoriesvar-Dokument-inom-halso--och-sjukvard"
      }]
    }]
  }
}

```
