# Referensintervall - Logical Models from Visual Paradigm XMI v0.1.0

## Logical Model: Referensintervall 

 
Supporting logical model generated from gloo4.xmi (source class: Referensintervall). 

**Usages:**

* Use this Logical Model: [Laboratorieanalysresultat : Observerat hälsotillstånd](StructureDefinition-Laboratorieanalysresultat-Observerat-halsotillstand.md) and [Referenspopulation](StructureDefinition-Referenspopulation.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/xmi.to.fsh|current/StructureDefinition/StructureDefinition-Referensintervall.json)

### Formal Views of Profile Content

 [Description Differentials, Snapshots, and other representations](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](../StructureDefinition-Referensintervall.csv), [Excel](../StructureDefinition-Referensintervall.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "Referensintervall",
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-type-characteristics",
    "valueCode" : "can-be-target"
  }],
  "url" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Referensintervall",
  "version" : "0.1.0",
  "name" : "Referensintervall",
  "title" : "Referensintervall",
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
  "description" : "Supporting logical model generated from gloo4.xmi (source class: Referensintervall).",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Referensintervall",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "Referensintervall",
      "path" : "Referensintervall",
      "short" : "Referensintervall",
      "definition" : "Supporting logical model generated from gloo4.xmi (source class: Referensintervall)."
    },
    {
      "id" : "Referensintervall.liggerTillGrundFor",
      "path" : "Referensintervall.liggerTillGrundFor",
      "short" : "Source attribute: ligger till grund för",
      "definition" : "Source attribute: ligger till grund för",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Referenspopulation"
      }]
    },
    {
      "id" : "Referensintervall.gallerFor",
      "path" : "Referensintervall.gallerFor",
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
