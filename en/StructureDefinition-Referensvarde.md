# Referensvärde - Logical Models from Visual Paradigm XMI v0.1.0

## Logical Model: Referensvärde 

 
Ö verenskommet värde hos egenskap mot vilket kan jämföras uppmätta eller observerade värden . 

**Usages:**

* Use this Logical Model: [Laboratorieanalysresultat : Observerat hälsotillstånd](StructureDefinition-Laboratorieanalysresultat-Observerat-halsotillstand.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/xmi.to.fsh|current/StructureDefinition/StructureDefinition-Referensvarde.json)

### Formal Views of Profile Content

 [Description Differentials, Snapshots, and other representations](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](../StructureDefinition-Referensvarde.csv), [Excel](../StructureDefinition-Referensvarde.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "Referensvarde",
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-type-characteristics",
    "valueCode" : "can-be-target"
  }],
  "url" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Referensvarde",
  "version" : "0.1.0",
  "name" : "Referensvarde",
  "title" : "Referensvärde",
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
  "description" : "Ö  verenskommet värde   hos egenskap   mot vilket kan jämföras uppmätta eller observerade värden  .",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Referensvarde",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "Referensvarde",
      "path" : "Referensvarde",
      "short" : "Referensvärde",
      "definition" : "Ö  verenskommet värde   hos egenskap   mot vilket kan jämföras uppmätta eller observerade värden  ."
    },
    {
      "id" : "Referensvarde.gallerFor",
      "path" : "Referensvarde.gallerFor",
      "short" : "Source attribute: gäller för",
      "definition" : "Source attribute: gäller för",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Laboratorieanalysresultat-Observerat-halsotillstand"
      }]
    }]
  }
}

```
