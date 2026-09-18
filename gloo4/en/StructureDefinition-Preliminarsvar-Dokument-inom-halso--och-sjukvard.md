# Preliminärsvar : Dokument (inom hälso- och sjukvård) - gloo4 v0.1.0

## Logical Model: Preliminärsvar : Dokument (inom hälso- och sjukvård) 

 
Delsvar som innehåller minst ett resultat från en analys som ännu inte är avslutad. 
Den remissvarsmottagande enheten ska förvänta sig ytterligare svar efter ett preliminärsvar och har fortfarande ett ansvar att bevaka detta till dess ett slutsvar har mottagits. 

**Usages:**

* Use this Logical Model: [Delsvar : Dokument (inom hälso- och sjukvård)](StructureDefinition-Delsvar-Dokument-inom-halso--och-sjukvard.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/gloo4|current/StructureDefinition/StructureDefinition-Preliminarsvar-Dokument-inom-halso--och-sjukvard.json)

### Formal Views of Profile Content

 [Description Differentials, Snapshots, and other representations](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](../StructureDefinition-Preliminarsvar-Dokument-inom-halso--och-sjukvard.csv), [Excel](../StructureDefinition-Preliminarsvar-Dokument-inom-halso--och-sjukvard.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "Preliminarsvar-Dokument-inom-halso--och-sjukvard",
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-type-characteristics",
    "valueCode" : "can-be-target"
  }],
  "url" : "http://example.org/fhir/gloo4/StructureDefinition/Preliminarsvar-Dokument-inom-halso--och-sjukvard",
  "version" : "0.1.0",
  "name" : "PreliminarsvarDokumentinomhalsoochsjukvard",
  "title" : "Preliminärsvar : Dokument (inom hälso- och sjukvård)",
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
  "description" : "Delsvar som innehåller minst ett resultat från en analys som ännu inte är avslutad.\n\nDen remissvarsmottagande enheten ska förvänta sig ytterligare svar efter ett preliminärsvar och har fortfarande ett ansvar att bevaka detta till dess ett slutsvar har mottagits.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://example.org/fhir/gloo4/StructureDefinition/Preliminarsvar-Dokument-inom-halso--och-sjukvard",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "Preliminarsvar-Dokument-inom-halso--och-sjukvard",
      "path" : "Preliminarsvar-Dokument-inom-halso--och-sjukvard",
      "short" : "Preliminärsvar : Dokument (inom hälso- och sjukvård)",
      "definition" : "Delsvar som innehåller minst ett resultat från en analys som ännu inte är avslutad.\n\nDen remissvarsmottagande enheten ska förvänta sig ytterligare svar efter ett preliminärsvar och har fortfarande ett ansvar att bevaka detta till dess ett slutsvar har mottagits."
    },
    {
      "id" : "Preliminarsvar-Dokument-inom-halso--och-sjukvard.arEtt",
      "path" : "Preliminarsvar-Dokument-inom-halso--och-sjukvard.arEtt",
      "short" : "Source attribute: är ett",
      "definition" : "Source attribute: är ett",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/gloo4/StructureDefinition/Delsvar-Dokument-inom-halso--och-sjukvard"
      }]
    }]
  }
}

```
