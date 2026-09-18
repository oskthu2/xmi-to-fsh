# Provmaterial - Logical Models from Visual Paradigm XMI v0.1.0

## Logical Model: Provmaterial 

 
Supporting logical model generated from gloo4.xmi (source class: Provmaterial). 

**Usages:**

* Use this Logical Model: [Prov : Resurs (inom hälso- och sjukvård)](StructureDefinition-Prov-Resurs-inom-halso--och-sjukvard.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/xmi.to.fsh|current/StructureDefinition/StructureDefinition-Provmaterial.json)

### Formal Views of Profile Content

 [Description Differentials, Snapshots, and other representations](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](../StructureDefinition-Provmaterial.csv), [Excel](../StructureDefinition-Provmaterial.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "Provmaterial",
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-type-characteristics",
    "valueCode" : "can-be-target"
  }],
  "url" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Provmaterial",
  "version" : "0.1.0",
  "name" : "Provmaterial",
  "title" : "Provmaterial",
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
  "description" : "Supporting logical model generated from gloo4.xmi (source class: Provmaterial).",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Provmaterial",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "Provmaterial",
      "path" : "Provmaterial",
      "short" : "Provmaterial",
      "definition" : "Supporting logical model generated from gloo4.xmi (source class: Provmaterial)."
    },
    {
      "id" : "Provmaterial.bestarAvVisst",
      "path" : "Provmaterial.bestarAvVisst",
      "short" : "Source attribute: består av visst",
      "definition" : "Source attribute: består av visst",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Prov-Resurs-inom-halso--och-sjukvard"
      }]
    }]
  }
}

```
