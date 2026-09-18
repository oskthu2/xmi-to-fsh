# Signatur - Logical Models from Visual Paradigm XMI v0.1.0

## Logical Model: Signatur 

 
Supporting logical model generated from gloo4.xmi (source class: Signatur). 

**Usages:**

* Use this Logical Model: [Signering : Deltagande](StructureDefinition-Signering-Deltagande-2.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/xmi.to.fsh|current/StructureDefinition/StructureDefinition-Signatur.json)

### Formal Views of Profile Content

 [Description Differentials, Snapshots, and other representations](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](../StructureDefinition-Signatur.csv), [Excel](../StructureDefinition-Signatur.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "Signatur",
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-type-characteristics",
    "valueCode" : "can-be-target"
  }],
  "url" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Signatur",
  "version" : "0.1.0",
  "name" : "Signatur",
  "title" : "Signatur",
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
  "description" : "Supporting logical model generated from gloo4.xmi (source class: Signatur).",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Signatur",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "Signatur",
      "path" : "Signatur",
      "short" : "Signatur",
      "definition" : "Supporting logical model generated from gloo4.xmi (source class: Signatur)."
    },
    {
      "id" : "Signatur.arResultatAv",
      "path" : "Signatur.arResultatAv",
      "short" : "Source attribute: är resultat av",
      "definition" : "Source attribute: är resultat av",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Signering-Deltagande-2"
      }]
    }]
  }
}

```
