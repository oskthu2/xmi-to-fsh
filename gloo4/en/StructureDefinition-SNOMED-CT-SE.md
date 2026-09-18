# SNOMED-CT SE - gloo4 v0.1.0

## Logical Model: SNOMED-CT SE 

 
SNOMED CT innehåller en stor mängd kliniska termer. 
OID: 1.2.752.116.2.1.1 

**Usages:**

* This Logical Model is not used by any profiles in this Specification

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/gloo4|current/StructureDefinition/StructureDefinition-SNOMED-CT-SE.json)

### Formal Views of Profile Content

 [Description Differentials, Snapshots, and other representations](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](../StructureDefinition-SNOMED-CT-SE.csv), [Excel](../StructureDefinition-SNOMED-CT-SE.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "SNOMED-CT-SE",
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-type-characteristics",
    "valueCode" : "can-be-target"
  }],
  "url" : "http://example.org/fhir/gloo4/StructureDefinition/SNOMED-CT-SE",
  "version" : "0.1.0",
  "name" : "SNOMEDCTSE",
  "title" : "SNOMED-CT SE",
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
  "description" : "SNOMED CT innehåller en stor mängd kliniska termer.\n\nOID: 1.2.752.116.2.1.1",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://example.org/fhir/gloo4/StructureDefinition/SNOMED-CT-SE",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "SNOMED-CT-SE",
      "path" : "SNOMED-CT-SE",
      "short" : "SNOMED-CT SE",
      "definition" : "SNOMED CT innehåller en stor mängd kliniska termer.\n\nOID: 1.2.752.116.2.1.1"
    }]
  }
}

```
