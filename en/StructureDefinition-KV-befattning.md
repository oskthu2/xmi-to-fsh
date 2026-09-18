# KV befattning - Logical Models from Visual Paradigm XMI v0.1.0

## Logical Model: KV befattning 

 
Innehåller ingormation om en vård- och sjukvårdspersonals befattning. 
OID: 1.2.752.129.2.2.1.4 

**Usages:**

* This Logical Model is not used by any profiles in this Specification

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/xmi.to.fsh|current/StructureDefinition/StructureDefinition-KV-befattning.json)

### Formal Views of Profile Content

 [Description Differentials, Snapshots, and other representations](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](../StructureDefinition-KV-befattning.csv), [Excel](../StructureDefinition-KV-befattning.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "KV-befattning",
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-type-characteristics",
    "valueCode" : "can-be-target"
  }],
  "url" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/KV-befattning",
  "version" : "0.1.0",
  "name" : "KVbefattning",
  "title" : "KV befattning",
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
  "description" : "Innehåller ingormation om en vård- och sjukvårdspersonals befattning.\n\nOID: 1.2.752.129.2.2.1.4",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/KV-befattning",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "KV-befattning",
      "path" : "KV-befattning",
      "short" : "KV befattning",
      "definition" : "Innehåller ingormation om en vård- och sjukvårdspersonals befattning.\n\nOID: 1.2.752.129.2.2.1.4"
    }]
  }
}

```
