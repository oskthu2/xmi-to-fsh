# Målpopulation - Logical Models from Visual Paradigm XMI v0.1.0

## Logical Model: Målpopulation 

 
Supporting logical model generated from gloo4.xmi (source class: Målpopulation). 

**Usages:**

* Use this Logical Model: [: Patient](StructureDefinition-Patient-2.md) and [Referenspopulation](StructureDefinition-Referenspopulation.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/xmi.to.fsh|current/StructureDefinition/StructureDefinition-Malpopulation.json)

### Formal Views of Profile Content

 [Description Differentials, Snapshots, and other representations](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](../StructureDefinition-Malpopulation.csv), [Excel](../StructureDefinition-Malpopulation.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "Malpopulation",
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-type-characteristics",
    "valueCode" : "can-be-target"
  }],
  "url" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Malpopulation",
  "version" : "0.1.0",
  "name" : "Malpopulation",
  "title" : "Målpopulation",
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
  "description" : "Supporting logical model generated from gloo4.xmi (source class: Målpopulation).",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Malpopulation",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "Malpopulation",
      "path" : "Malpopulation",
      "short" : "Målpopulation",
      "definition" : "Supporting logical model generated from gloo4.xmi (source class: Målpopulation)."
    },
    {
      "id" : "Malpopulation.jamforsMed",
      "path" : "Malpopulation.jamforsMed",
      "short" : "Source attribute: jämförs med",
      "definition" : "Source attribute: jämförs med",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Referenspopulation"
      }]
    },
    {
      "id" : "Malpopulation.tillhor",
      "path" : "Malpopulation.tillhor",
      "short" : "Source attribute: tillhör",
      "definition" : "Source attribute: tillhör",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Patient-2"
      }]
    }]
  }
}

```
