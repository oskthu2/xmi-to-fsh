# Delsvar : Dokument (inom hälso- och sjukvård) - Logical Models from Visual Paradigm XMI v0.1.0

## Logical Model: Delsvar : Dokument (inom hälso- och sjukvård) 

 
Supporting logical model generated from gloo4.xmi (source class: Delsvar : Dokument (inom hälso- och sjukvård)). 

**Usages:**

* Use this Logical Model: [Preliminärsvar : Dokument (inom hälso- och sjukvård)](StructureDefinition-Preliminarsvar-Dokument-inom-halso--och-sjukvard.md) and [Remissvar : Dokument (inom hälso- och sjukvård)](StructureDefinition-Remissvar-Dokument-inom-halso--och-sjukvard.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/xmi.to.fsh|current/StructureDefinition/StructureDefinition-Delsvar-Dokument-inom-halso--och-sjukvard.json)

### Formal Views of Profile Content

 [Description Differentials, Snapshots, and other representations](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](../StructureDefinition-Delsvar-Dokument-inom-halso--och-sjukvard.csv), [Excel](../StructureDefinition-Delsvar-Dokument-inom-halso--och-sjukvard.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "Delsvar-Dokument-inom-halso--och-sjukvard",
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-type-characteristics",
    "valueCode" : "can-be-target"
  }],
  "url" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Delsvar-Dokument-inom-halso--och-sjukvard",
  "version" : "0.1.0",
  "name" : "DelsvarDokumentinomhalsoochsjukvard",
  "title" : "Delsvar : Dokument (inom hälso- och sjukvård)",
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
  "description" : "Supporting logical model generated from gloo4.xmi (source class: Delsvar : Dokument (inom hälso- och sjukvård)).",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Delsvar-Dokument-inom-halso--och-sjukvard",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "Delsvar-Dokument-inom-halso--och-sjukvard",
      "path" : "Delsvar-Dokument-inom-halso--och-sjukvard",
      "short" : "Delsvar : Dokument (inom hälso- och sjukvård)",
      "definition" : "Supporting logical model generated from gloo4.xmi (source class: Delsvar : Dokument (inom hälso- och sjukvård))."
    },
    {
      "id" : "Delsvar-Dokument-inom-halso--och-sjukvard.arEtt",
      "path" : "Delsvar-Dokument-inom-halso--och-sjukvard.arEtt",
      "short" : "Source attribute: är ett",
      "definition" : "Source attribute: är ett",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Preliminarsvar-Dokument-inom-halso--och-sjukvard"
      }]
    },
    {
      "id" : "Delsvar-Dokument-inom-halso--och-sjukvard.arEtt2",
      "path" : "Delsvar-Dokument-inom-halso--och-sjukvard.arEtt2",
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
