# Slutsvar : Dokument (inom hälso- och sjukvård) - Logical Models from Visual Paradigm XMI v0.1.0

## Logical Model: Slutsvar : Dokument (inom hälso- och sjukvård) 

 
Svar där samtliga i remissen beställda analyser i och med detta svar är besvarade slutligt, och inga fortsatta analyser pågår. 
Den remissvarsmottagande enheten ska i och med detta inte förvänta sig ytterligare svar. Även efter ett slutsvar finns det möjlighet för utförande enhet att skicka ytterligare svar relaterat till samma remiss. 

**Usages:**

* Use this Logical Model: [Remissvar : Dokument (inom hälso- och sjukvård)](StructureDefinition-Remissvar-Dokument-inom-halso--och-sjukvard.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/xmi.to.fsh|current/StructureDefinition/StructureDefinition-Slutsvar-Dokument-inom-halso--och-sjukvard.json)

### Formal Views of Profile Content

 [Description Differentials, Snapshots, and other representations](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](../StructureDefinition-Slutsvar-Dokument-inom-halso--och-sjukvard.csv), [Excel](../StructureDefinition-Slutsvar-Dokument-inom-halso--och-sjukvard.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "Slutsvar-Dokument-inom-halso--och-sjukvard",
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-type-characteristics",
    "valueCode" : "can-be-target"
  }],
  "url" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Slutsvar-Dokument-inom-halso--och-sjukvard",
  "version" : "0.1.0",
  "name" : "SlutsvarDokumentinomhalsoochsjukvard",
  "title" : "Slutsvar : Dokument (inom hälso- och sjukvård)",
  "status" : "draft",
  "date" : "2026-09-18T10:29:51+00:00",
  "publisher" : "xmi-to-fsh",
  "contact" : [{
    "name" : "xmi-to-fsh",
    "telecom" : [{
      "system" : "url",
      "value" : "https://github.com/oskthu2/xmi-to-fsh"
    }]
  }],
  "description" : "Svar där samtliga i remissen beställda analyser i och med detta svar är besvarade slutligt, och inga fortsatta analyser pågår.\n\nDen remissvarsmottagande enheten ska i och med detta inte förvänta sig ytterligare svar. Även efter ett slutsvar finns det möjlighet för utförande enhet att skicka ytterligare svar relaterat till samma remiss.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Slutsvar-Dokument-inom-halso--och-sjukvard",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "Slutsvar-Dokument-inom-halso--och-sjukvard",
      "path" : "Slutsvar-Dokument-inom-halso--och-sjukvard",
      "short" : "Slutsvar : Dokument (inom hälso- och sjukvård)",
      "definition" : "Svar där samtliga i remissen beställda analyser i och med detta svar är besvarade slutligt, och inga fortsatta analyser pågår.\n\nDen remissvarsmottagande enheten ska i och med detta inte förvänta sig ytterligare svar. Även efter ett slutsvar finns det möjlighet för utförande enhet att skicka ytterligare svar relaterat till samma remiss."
    },
    {
      "id" : "Slutsvar-Dokument-inom-halso--och-sjukvard.arEtt",
      "path" : "Slutsvar-Dokument-inom-halso--och-sjukvard.arEtt",
      "short" : "Source attribute: är ett",
      "definition" : "Source attribute: är ett",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Remissvar-Dokument-inom-halso--och-sjukvard"
      }]
    }]
  }
}

```
