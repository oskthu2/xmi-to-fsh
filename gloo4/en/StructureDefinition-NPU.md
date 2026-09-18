# NPU - gloo4 v0.1.0

## Logical Model: NPU 

 
NPU-systemet (Nomenclature of properties and units) är ett register med systematiska, unika benämningar och koder för laboratorieundersökningar. 

**Usages:**

* This Logical Model is not used by any profiles in this Specification

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/gloo4|current/StructureDefinition/StructureDefinition-NPU.json)

### Formal Views of Profile Content

 [Description Differentials, Snapshots, and other representations](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](../StructureDefinition-NPU.csv), [Excel](../StructureDefinition-NPU.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "NPU",
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-type-characteristics",
    "valueCode" : "can-be-target"
  }],
  "url" : "http://example.org/fhir/gloo4/StructureDefinition/NPU",
  "version" : "0.1.0",
  "name" : "NPU",
  "title" : "NPU",
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
  "description" : "NPU-systemet (Nomenclature of properties and units) är ett register med systematiska, unika benämningar och koder för laboratorieundersökningar.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://example.org/fhir/gloo4/StructureDefinition/NPU",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "NPU",
      "path" : "NPU",
      "short" : "NPU",
      "definition" : "NPU-systemet (Nomenclature of properties and units) är ett register med systematiska, unika benämningar och koder för laboratorieundersökningar."
    }]
  }
}

```
