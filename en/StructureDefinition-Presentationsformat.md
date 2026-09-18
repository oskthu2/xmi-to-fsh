# Presentationsformat - Logical Models from Visual Paradigm XMI v0.1.0

## Logical Model: Presentationsformat 

 
Supporting logical model generated from gloo4.xmi (source class: Presentationsformat). 

**Usages:**

* Use this Logical Model: [Remissvar : Dokument (inom hälso- och sjukvård)](StructureDefinition-Remissvar-Dokument-inom-halso--och-sjukvard.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/xmi.to.fsh|current/StructureDefinition/StructureDefinition-Presentationsformat.json)

### Formal Views of Profile Content

 [Description Differentials, Snapshots, and other representations](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](../StructureDefinition-Presentationsformat.csv), [Excel](../StructureDefinition-Presentationsformat.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "Presentationsformat",
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-type-characteristics",
    "valueCode" : "can-be-target"
  }],
  "url" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Presentationsformat",
  "version" : "0.1.0",
  "name" : "Presentationsformat",
  "title" : "Presentationsformat",
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
  "description" : "Supporting logical model generated from gloo4.xmi (source class: Presentationsformat).",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Presentationsformat",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "Presentationsformat",
      "path" : "Presentationsformat",
      "short" : "Presentationsformat",
      "definition" : "Supporting logical model generated from gloo4.xmi (source class: Presentationsformat)."
    },
    {
      "id" : "Presentationsformat.harVisst",
      "path" : "Presentationsformat.harVisst",
      "short" : "Source attribute: har visst",
      "definition" : "Source attribute: har visst",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Remissvar-Dokument-inom-halso--och-sjukvard"
      }]
    }]
  }
}

```
