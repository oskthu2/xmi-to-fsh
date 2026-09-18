# Provgivare - Logical Models from Visual Paradigm XMI v0.1.0

## Logical Model: Provgivare 

 
Person som lämnar prov. (Biobank Sverige, under revidering) 

**Usages:**

* Use this Logical Model: [Prov : Resurs (inom hälso- och sjukvård)](StructureDefinition-Prov-Resurs-inom-halso--och-sjukvard.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/xmi.to.fsh|current/StructureDefinition/StructureDefinition-Provgivare.json)

### Formal Views of Profile Content

 [Description Differentials, Snapshots, and other representations](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](../StructureDefinition-Provgivare.csv), [Excel](../StructureDefinition-Provgivare.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "Provgivare",
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-type-characteristics",
    "valueCode" : "can-be-target"
  }],
  "url" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Provgivare",
  "version" : "0.1.0",
  "name" : "Provgivare",
  "title" : "Provgivare",
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
  "description" : "Person som lämnar prov.\n(Biobank Sverige, under revidering)",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Provgivare",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "Provgivare",
      "path" : "Provgivare",
      "short" : "Provgivare",
      "definition" : "Person som lämnar prov.\n(Biobank Sverige, under revidering)"
    },
    {
      "id" : "Provgivare.lamnar",
      "path" : "Provgivare.lamnar",
      "short" : "Source attribute: lämnar",
      "definition" : "Source attribute: lämnar",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Prov-Resurs-inom-halso--och-sjukvard"
      }]
    }]
  }
}

```
