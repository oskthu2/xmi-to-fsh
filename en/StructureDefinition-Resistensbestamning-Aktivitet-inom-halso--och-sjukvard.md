# Resistensbestämning : Aktivitet (inom hälso- och sjukvård) - Logical Models from Visual Paradigm XMI v0.1.0

## Logical Model: Resistensbestämning : Aktivitet (inom hälso- och sjukvård) 

 
Supporting logical model generated from gloo4.xmi (source class: Resistensbestämning : Aktivitet (inom hälso- och sjukvård)). 

**Usages:**

* Use this Logical Model: [Mikroorganism](StructureDefinition-Mikroorganism.md) and [Resistens](StructureDefinition-Resistens.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/xmi.to.fsh|current/StructureDefinition/StructureDefinition-Resistensbestamning-Aktivitet-inom-halso--och-sjukvard.json)

### Formal Views of Profile Content

 [Description Differentials, Snapshots, and other representations](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](../StructureDefinition-Resistensbestamning-Aktivitet-inom-halso--och-sjukvard.csv), [Excel](../StructureDefinition-Resistensbestamning-Aktivitet-inom-halso--och-sjukvard.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "Resistensbestamning-Aktivitet-inom-halso--och-sjukvard",
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-type-characteristics",
    "valueCode" : "can-be-target"
  }],
  "url" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Resistensbestamning-Aktivitet-inom-halso--och-sjukvard",
  "version" : "0.1.0",
  "name" : "ResistensbestamningAktivitetinomhalsoochsjukvard",
  "title" : "Resistensbestämning : Aktivitet (inom hälso- och sjukvård)",
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
  "description" : "Supporting logical model generated from gloo4.xmi (source class: Resistensbestämning : Aktivitet (inom hälso- och sjukvård)).",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Resistensbestamning-Aktivitet-inom-halso--och-sjukvard",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "Resistensbestamning-Aktivitet-inom-halso--och-sjukvard",
      "path" : "Resistensbestamning-Aktivitet-inom-halso--och-sjukvard",
      "short" : "Resistensbestämning : Aktivitet (inom hälso- och sjukvård)",
      "definition" : "Supporting logical model generated from gloo4.xmi (source class: Resistensbestämning : Aktivitet (inom hälso- och sjukvård))."
    },
    {
      "id" : "Resistensbestamning-Aktivitet-inom-halso--och-sjukvard.faststaller",
      "path" : "Resistensbestamning-Aktivitet-inom-halso--och-sjukvard.faststaller",
      "short" : "Source attribute: fastställer",
      "definition" : "Source attribute: fastställer",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Resistens"
      }]
    },
    {
      "id" : "Resistensbestamning-Aktivitet-inom-halso--och-sjukvard.kanUtforasPa",
      "path" : "Resistensbestamning-Aktivitet-inom-halso--och-sjukvard.kanUtforasPa",
      "short" : "Source attribute: kan utföras på",
      "definition" : "Source attribute: kan utföras på",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Mikroorganism"
      }]
    }]
  }
}

```
