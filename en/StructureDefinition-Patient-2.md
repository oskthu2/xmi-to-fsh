# : Patient - Logical Models from Visual Paradigm XMI v0.1.0

## Logical Model: : Patient 

 
Supporting logical model generated from gloo4.xmi (source class: : Patient). 

**Usages:**

* Use this Logical Model: [Målpopulation](StructureDefinition-Malpopulation.md) and [Remiss : Dokument (inom hälso- och sjukvård)](StructureDefinition-Remiss-Dokument-inom-halso--och-sjukvard.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/xmi.to.fsh|current/StructureDefinition/StructureDefinition-Patient-2.json)

### Formal Views of Profile Content

 [Description Differentials, Snapshots, and other representations](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](../StructureDefinition-Patient-2.csv), [Excel](../StructureDefinition-Patient-2.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "Patient-2",
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-type-characteristics",
    "valueCode" : "can-be-target"
  }],
  "url" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Patient-2",
  "version" : "0.1.0",
  "name" : "Patient2",
  "title" : ": Patient",
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
  "description" : "Supporting logical model generated from gloo4.xmi (source class: : Patient).",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Patient-2",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "Patient-2",
      "path" : "Patient-2",
      "short" : ": Patient",
      "definition" : "Supporting logical model generated from gloo4.xmi (source class: : Patient)."
    },
    {
      "id" : "Patient-2.tillhor",
      "path" : "Patient-2.tillhor",
      "short" : "Source attribute: tillhör",
      "definition" : "Source attribute: tillhör",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Malpopulation"
      }]
    },
    {
      "id" : "Patient-2.avser",
      "path" : "Patient-2.avser",
      "short" : "Source attribute: avser",
      "definition" : "Source attribute: avser",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Remiss-Dokument-inom-halso--och-sjukvard"
      }]
    }]
  }
}

```
