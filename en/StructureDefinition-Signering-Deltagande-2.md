# Signering : Deltagande - Logical Models from Visual Paradigm XMI v0.1.0

## Logical Model: Signering : Deltagande 

 
Supporting logical model generated from gloo4.xmi (source class: Signering : Deltagande). 

**Usages:**

* Use this Logical Model: [: Hälso- och sjukvårdspersonal](StructureDefinition-Halso--och-sjukvardspersonal.md), [Laboratorieanalysresultat : Observerat hälsotillstånd](StructureDefinition-Laboratorieanalysresultat-Observerat-halsotillstand.md), [Remissvar : Dokument (inom hälso- och sjukvård)](StructureDefinition-Remissvar-Dokument-inom-halso--och-sjukvard.md) and [Signatur](StructureDefinition-Signatur.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/xmi.to.fsh|current/StructureDefinition/StructureDefinition-Signering-Deltagande-2.json)

### Formal Views of Profile Content

 [Description Differentials, Snapshots, and other representations](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](../StructureDefinition-Signering-Deltagande-2.csv), [Excel](../StructureDefinition-Signering-Deltagande-2.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "Signering-Deltagande-2",
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-type-characteristics",
    "valueCode" : "can-be-target"
  }],
  "url" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Signering-Deltagande-2",
  "version" : "0.1.0",
  "name" : "SigneringDeltagande2",
  "title" : "Signering : Deltagande",
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
  "description" : "Supporting logical model generated from gloo4.xmi (source class: Signering : Deltagande).",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Signering-Deltagande-2",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "Signering-Deltagande-2",
      "path" : "Signering-Deltagande-2",
      "short" : "Signering : Deltagande",
      "definition" : "Supporting logical model generated from gloo4.xmi (source class: Signering : Deltagande)."
    },
    {
      "id" : "Signering-Deltagande-2.gorsAv",
      "path" : "Signering-Deltagande-2.gorsAv",
      "short" : "Source attribute: görs av",
      "definition" : "Source attribute: görs av",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Laboratorieanalysresultat-Observerat-halsotillstand"
      }]
    },
    {
      "id" : "Signering-Deltagande-2.gorsAv2",
      "path" : "Signering-Deltagande-2.gorsAv2",
      "short" : "Source attribute: görs av",
      "definition" : "Source attribute: görs av",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Halso--och-sjukvardspersonal"
      }]
    },
    {
      "id" : "Signering-Deltagande-2.gorsAv3",
      "path" : "Signering-Deltagande-2.gorsAv3",
      "short" : "Source attribute: görs av",
      "definition" : "Source attribute: görs av",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Remissvar-Dokument-inom-halso--och-sjukvard"
      }]
    },
    {
      "id" : "Signering-Deltagande-2.arResultatAv",
      "path" : "Signering-Deltagande-2.arResultatAv",
      "short" : "Source attribute: är resultat av",
      "definition" : "Source attribute: är resultat av",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Signatur"
      }]
    }]
  }
}

```
