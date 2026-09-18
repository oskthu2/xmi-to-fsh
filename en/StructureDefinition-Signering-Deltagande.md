# Signering : Deltagande - Logical Models from Visual Paradigm XMI v0.1.0

## Logical Model: Signering : Deltagande 

 
Supporting logical model generated from gloo4.xmi (source class: Signering : Deltagande). 

**Usages:**

* Use this Logical Model: [Hälso- och sjukvårdspersonal : Hälso- och sjukvårdspersonal](StructureDefinition-Halso--och-sjukvardspersonal-Halso--och-sjukvardsperson.md), [Laboratorieanalysresultat : Observation](StructureDefinition-Laboratorieanalysresultat-Observation.md) and [Laboratoriesvar : Dokument](StructureDefinition-Laboratoriesvar-Dokument.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/xmi.to.fsh|current/StructureDefinition/StructureDefinition-Signering-Deltagande.json)

### Formal Views of Profile Content

 [Description Differentials, Snapshots, and other representations](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](../StructureDefinition-Signering-Deltagande.csv), [Excel](../StructureDefinition-Signering-Deltagande.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "Signering-Deltagande",
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-type-characteristics",
    "valueCode" : "can-be-target"
  }],
  "url" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Signering-Deltagande",
  "version" : "0.1.0",
  "name" : "SigneringDeltagande",
  "title" : "Signering : Deltagande",
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
  "description" : "Supporting logical model generated from gloo4.xmi (source class: Signering : Deltagande).",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Signering-Deltagande",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "Signering-Deltagande",
      "path" : "Signering-Deltagande",
      "short" : "Signering : Deltagande",
      "definition" : "Supporting logical model generated from gloo4.xmi (source class: Signering : Deltagande)."
    },
    {
      "id" : "Signering-Deltagande.tidpunkt",
      "path" : "Signering-Deltagande.tidpunkt",
      "short" : "Source attribute: tidpunkt",
      "definition" : "Source attribute: tidpunkt",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/TS"
      }]
    },
    {
      "id" : "Signering-Deltagande.harMottgares",
      "path" : "Signering-Deltagande.harMottgares",
      "short" : "Source attribute: har mottgares",
      "definition" : "Source attribute: har mottgares",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Laboratoriesvar-Dokument"
      }]
    },
    {
      "id" : "Signering-Deltagande.harAnsvarigs",
      "path" : "Signering-Deltagande.harAnsvarigs",
      "short" : "Source attribute: har ansvarigs",
      "definition" : "Source attribute: har ansvarigs",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Laboratoriesvar-Dokument"
      }]
    },
    {
      "id" : "Signering-Deltagande.harMottagares",
      "path" : "Signering-Deltagande.harMottagares",
      "short" : "Source attribute: har mottagares",
      "definition" : "Source attribute: har mottagares",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Laboratorieanalysresultat-Observation"
      }]
    },
    {
      "id" : "Signering-Deltagande.harUtforares",
      "path" : "Signering-Deltagande.harUtforares",
      "short" : "Source attribute: har utförares",
      "definition" : "Source attribute: har utförares",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Laboratorieanalysresultat-Observation"
      }]
    },
    {
      "id" : "Signering-Deltagande.utforsAv",
      "path" : "Signering-Deltagande.utforsAv",
      "short" : "Source attribute: utförs av",
      "definition" : "Source attribute: utförs av",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Halso--och-sjukvardspersonal-Halso--och-sjukvardsperson"
      }]
    }]
  }
}

```
