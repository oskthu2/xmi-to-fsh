# Fördjupad analys - Logical Models from Visual Paradigm XMI v0.1.0

## Logical Model: Fördjupad analys 

 
Supporting logical model generated from gloo4.xmi (source class: Fördjupad analys). 

**Usages:**

* Use this Logical Model: [Laboratorieanalys : Aktivitet (inom hälso- och sjukvård)](StructureDefinition-Laboratorieanalys-Aktivitet-inom-halso--och-sjukvard.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/xmi.to.fsh|current/StructureDefinition/StructureDefinition-Fordjupad-analys.json)

### Formal Views of Profile Content

 [Description Differentials, Snapshots, and other representations](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](../StructureDefinition-Fordjupad-analys.csv), [Excel](../StructureDefinition-Fordjupad-analys.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "Fordjupad-analys",
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-type-characteristics",
    "valueCode" : "can-be-target"
  }],
  "url" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Fordjupad-analys",
  "version" : "0.1.0",
  "name" : "Fordjupadanalys",
  "title" : "Fördjupad analys",
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
  "description" : "Supporting logical model generated from gloo4.xmi (source class: Fördjupad analys).",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Fordjupad-analys",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "Fordjupad-analys",
      "path" : "Fordjupad-analys",
      "short" : "Fördjupad analys",
      "definition" : "Supporting logical model generated from gloo4.xmi (source class: Fördjupad analys)."
    },
    {
      "id" : "Fordjupad-analys.arEn",
      "path" : "Fordjupad-analys.arEn",
      "short" : "Source attribute: är en",
      "definition" : "Source attribute: är en",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Laboratorieanalys-Aktivitet-inom-halso--och-sjukvard"
      }]
    }]
  }
}

```
