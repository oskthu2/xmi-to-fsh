# RevisionshistorikTA - gloo4 v0.1.0

## Logical Model: RevisionshistorikTA 

 
Supporting logical model generated from gloo4.xmi (source class: RevisionshistorikTA). 

**Usages:**

* This Logical Model is not used by any profiles in this Specification

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/gloo4|current/StructureDefinition/StructureDefinition-RevisionshistorikTA.json)

### Formal Views of Profile Content

 [Description Differentials, Snapshots, and other representations](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](../StructureDefinition-RevisionshistorikTA.csv), [Excel](../StructureDefinition-RevisionshistorikTA.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "RevisionshistorikTA",
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-type-characteristics",
    "valueCode" : "can-be-target"
  }],
  "url" : "http://example.org/fhir/gloo4/StructureDefinition/RevisionshistorikTA",
  "version" : "0.1.0",
  "name" : "RevisionshistorikTA",
  "title" : "RevisionshistorikTA",
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
  "description" : "Supporting logical model generated from gloo4.xmi (source class: RevisionshistorikTA).",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://example.org/fhir/gloo4/StructureDefinition/RevisionshistorikTA",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "RevisionshistorikTA",
      "path" : "RevisionshistorikTA",
      "short" : "RevisionshistorikTA",
      "definition" : "Supporting logical model generated from gloo4.xmi (source class: RevisionshistorikTA)."
    },
    {
      "id" : "RevisionshistorikTA.Version40",
      "path" : "RevisionshistorikTA.Version40",
      "short" : "Source attribute: Version 4.0; type could not be resolved from source model",
      "definition" : "Ny informationsspecifikation för laboratoriesvar fastställd.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "RevisionshistorikTA.Version401",
      "path" : "RevisionshistorikTA.Version401",
      "short" : "Source attribute: Version 4.0.1; type could not be resolved from source model",
      "definition" : "Uppdaterat samtliga urval.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "RevisionshistorikTA.Version402",
      "path" : "RevisionshistorikTA.Version402",
      "short" : "Source attribute: Version 4.0.2; type could not be resolved from source model",
      "definition" : "Uppdaterad med exempel för resistensbestämning.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    }]
  }
}

```
