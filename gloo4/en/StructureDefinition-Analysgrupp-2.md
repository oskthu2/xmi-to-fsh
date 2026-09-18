# Analysgrupp - gloo4 v0.1.0

## Logical Model: Analysgrupp 

 
Grupp av analyser utförda på ett eller flera prov från samma provgivare och som man väljer att betrakta som en enhet. 

**Usages:**

* Use this Logical Model: [Laboratorieanalys : Aktivitet (inom hälso- och sjukvård)](StructureDefinition-Laboratorieanalys-Aktivitet-inom-halso--och-sjukvard.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/gloo4|current/StructureDefinition/StructureDefinition-Analysgrupp-2.json)

### Formal Views of Profile Content

 [Description Differentials, Snapshots, and other representations](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](../StructureDefinition-Analysgrupp-2.csv), [Excel](../StructureDefinition-Analysgrupp-2.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "Analysgrupp-2",
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-type-characteristics",
    "valueCode" : "can-be-target"
  }],
  "url" : "http://example.org/fhir/gloo4/StructureDefinition/Analysgrupp-2",
  "version" : "0.1.0",
  "name" : "Analysgrupp2",
  "title" : "Analysgrupp",
  "status" : "draft",
  "date" : "2026-09-18T11:14:11+00:00",
  "publisher" : "xmi-to-fsh",
  "contact" : [{
    "name" : "xmi-to-fsh",
    "telecom" : [{
      "system" : "url",
      "value" : "https://github.com/oskthu2/xmi-to-fsh"
    }]
  }],
  "description" : "Grupp av analyser utförda på ett eller flera prov från samma provgivare och som man väljer att betrakta som en enhet.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://example.org/fhir/gloo4/StructureDefinition/Analysgrupp-2",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "Analysgrupp-2",
      "path" : "Analysgrupp-2",
      "short" : "Analysgrupp",
      "definition" : "Grupp av analyser utförda på ett eller flera prov från samma provgivare och som man väljer att betrakta som en enhet."
    },
    {
      "id" : "Analysgrupp-2.grupperar",
      "path" : "Analysgrupp-2.grupperar",
      "short" : "Source attribute: grupperar",
      "definition" : "Source attribute: grupperar",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/gloo4/StructureDefinition/Laboratorieanalys-Aktivitet-inom-halso--och-sjukvard"
      }]
    }]
  }
}

```
