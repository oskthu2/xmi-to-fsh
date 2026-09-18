# Referensmodell - Logical Models from Visual Paradigm XMI v0.1.0

## Logical Model: Referensmodell 

 
Supporting logical model generated from gloo4.xmi (source class: Referensmodell). 

**Usages:**

* This Logical Model is not used by any profiles in this Specification

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/xmi.to.fsh|current/StructureDefinition/StructureDefinition-Referensmodell.json)

### Formal Views of Profile Content

 [Description Differentials, Snapshots, and other representations](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](../StructureDefinition-Referensmodell.csv), [Excel](../StructureDefinition-Referensmodell.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "Referensmodell",
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-type-characteristics",
    "valueCode" : "can-be-target"
  }],
  "url" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Referensmodell",
  "version" : "0.1.0",
  "name" : "Referensmodell",
  "title" : "Referensmodell",
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
  "description" : "Supporting logical model generated from gloo4.xmi (source class: Referensmodell).",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Referensmodell",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "Referensmodell",
      "path" : "Referensmodell",
      "short" : "Referensmodell",
      "definition" : "Supporting logical model generated from gloo4.xmi (source class: Referensmodell)."
    },
    {
      "id" : "Referensmodell.NINationellInformationsstruktur",
      "path" : "Referensmodell.NINationellInformationsstruktur",
      "short" : "Source attribute: NI (Nationell Informationsstruktur); type could not be resolved from source model",
      "definition" : "Source attribute: NI (Nationell Informationsstruktur); type could not be resolved from source model",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "Referensmodell.RIMSaknas",
      "path" : "Referensmodell.RIMSaknas",
      "short" : "Source attribute: RIM saknas; type could not be resolved from source model",
      "definition" : "Source attribute: RIM saknas; type could not be resolved from source model",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    }]
  }
}

```
