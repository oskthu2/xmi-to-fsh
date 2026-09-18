# Referenser - Logical Models from Visual Paradigm XMI v0.1.0

## Logical Model: Referenser 

 
Supporting logical model generated from gloo4.xmi (source class: Referenser). 

**Usages:**

* This Logical Model is not used by any profiles in this Specification

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/xmi.to.fsh|current/StructureDefinition/StructureDefinition-Referenser.json)

### Formal Views of Profile Content

 [Description Differentials, Snapshots, and other representations](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](../StructureDefinition-Referenser.csv), [Excel](../StructureDefinition-Referenser.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "Referenser",
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-type-characteristics",
    "valueCode" : "can-be-target"
  }],
  "url" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Referenser",
  "version" : "0.1.0",
  "name" : "Referenser",
  "title" : "Referenser",
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
  "description" : "Supporting logical model generated from gloo4.xmi (source class: Referenser).",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Referenser",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "Referenser",
      "path" : "Referenser",
      "short" : "Referenser",
      "definition" : "Supporting logical model generated from gloo4.xmi (source class: Referenser)."
    },
    {
      "id" : "Referenser.R1",
      "path" : "Referenser.R1",
      "short" : "Source attribute: R1; type could not be resolved from source model",
      "definition" : "Source attribute: R1; type could not be resolved from source model",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "Referenser.R2",
      "path" : "Referenser.R2",
      "short" : "Source attribute: R2; type could not be resolved from source model",
      "definition" : "Source attribute: R2; type could not be resolved from source model",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    }]
  }
}

```
