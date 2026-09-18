# Resistens - Logical Models from Visual Paradigm XMI v0.1.0

## Logical Model: Resistens 

 
Supporting logical model generated from gloo4.xmi (source class: Resistens). 

**Usages:**

* Use this Logical Model: [Resistensbestämning : Aktivitet (inom hälso- och sjukvård)](StructureDefinition-Resistensbestamning-Aktivitet-inom-halso--och-sjukvard.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/xmi.to.fsh|current/StructureDefinition/StructureDefinition-Resistens.json)

### Formal Views of Profile Content

 [Description Differentials, Snapshots, and other representations](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](../StructureDefinition-Resistens.csv), [Excel](../StructureDefinition-Resistens.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "Resistens",
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-type-characteristics",
    "valueCode" : "can-be-target"
  }],
  "url" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Resistens",
  "version" : "0.1.0",
  "name" : "Resistens",
  "title" : "Resistens",
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
  "description" : "Supporting logical model generated from gloo4.xmi (source class: Resistens).",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Resistens",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "Resistens",
      "path" : "Resistens",
      "short" : "Resistens",
      "definition" : "Supporting logical model generated from gloo4.xmi (source class: Resistens)."
    },
    {
      "id" : "Resistens.faststaller",
      "path" : "Resistens.faststaller",
      "short" : "Source attribute: fastställer",
      "definition" : "Source attribute: fastställer",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Resistensbestamning-Aktivitet-inom-halso--och-sjukvard"
      }]
    }]
  }
}

```
