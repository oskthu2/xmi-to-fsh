# Prov-id - Logical Models from Visual Paradigm XMI v0.1.0

## Logical Model: Prov-id 

 
Supporting logical model generated from gloo4.xmi (source class: Prov-id). 

**Usages:**

* Use this Logical Model: [Prov : Resurs (inom hälso- och sjukvård)](StructureDefinition-Prov-Resurs-inom-halso--och-sjukvard.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/xmi.to.fsh|current/StructureDefinition/StructureDefinition-Prov-id.json)

### Formal Views of Profile Content

 [Description Differentials, Snapshots, and other representations](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](../StructureDefinition-Prov-id.csv), [Excel](../StructureDefinition-Prov-id.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "Prov-id",
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-type-characteristics",
    "valueCode" : "can-be-target"
  }],
  "url" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Prov-id",
  "version" : "0.1.0",
  "name" : "Provid",
  "title" : "Prov-id",
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
  "description" : "Supporting logical model generated from gloo4.xmi (source class: Prov-id).",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Prov-id",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "Prov-id",
      "path" : "Prov-id",
      "short" : "Prov-id",
      "definition" : "Supporting logical model generated from gloo4.xmi (source class: Prov-id)."
    },
    {
      "id" : "Prov-id.Identifierar",
      "path" : "Prov-id.Identifierar",
      "short" : "Source attribute: Identifierar",
      "definition" : "Source attribute: Identifierar",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Prov-Resurs-inom-halso--och-sjukvard"
      }]
    }]
  }
}

```
