# Origin - Logical Models from Visual Paradigm XMI v0.1.0

## Logical Model: Origin 

 
Supporting logical model generated from gloo4.xmi (source class: Origin). 

**Usages:**

* This Logical Model is not used by any profiles in this Specification

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/xmi.to.fsh|current/StructureDefinition/StructureDefinition-Origin.json)

### Formal Views of Profile Content

 [Description Differentials, Snapshots, and other representations](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](../StructureDefinition-Origin.csv), [Excel](../StructureDefinition-Origin.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "Origin",
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-type-characteristics",
    "valueCode" : "can-be-target"
  }],
  "url" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Origin",
  "version" : "0.1.0",
  "name" : "Origin",
  "title" : "Origin",
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
  "description" : "Supporting logical model generated from gloo4.xmi (source class: Origin).",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Origin",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "Origin",
      "path" : "Origin",
      "short" : "Origin",
      "definition" : "Supporting logical model generated from gloo4.xmi (source class: Origin)."
    },
    {
      "id" : "Origin.timeStamp",
      "path" : "Origin.timeStamp",
      "short" : "Source attribute: timeStamp",
      "definition" : "Source attribute: timeStamp",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "Origin.byRole",
      "path" : "Origin.byRole",
      "short" : "Source attribute: byRole",
      "definition" : "Source attribute: byRole",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    }]
  }
}

```
