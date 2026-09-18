# Referenspopulation - Logical Models from Visual Paradigm XMI v0.1.0

## Logical Model: Referenspopulation 

 
Den grupp man jämför med målpopulationen. 
Referenspopulationen måste stämma överens med målpopulationen i fråga om ålder, kön och sådana saker som spelar roll i sammanhanget. 

**Usages:**

* Use this Logical Model: [Målpopulation](StructureDefinition-Malpopulation.md) and [Referensintervall](StructureDefinition-Referensintervall.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/xmi.to.fsh|current/StructureDefinition/StructureDefinition-Referenspopulation.json)

### Formal Views of Profile Content

 [Description Differentials, Snapshots, and other representations](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](../StructureDefinition-Referenspopulation.csv), [Excel](../StructureDefinition-Referenspopulation.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "Referenspopulation",
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-type-characteristics",
    "valueCode" : "can-be-target"
  }],
  "url" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Referenspopulation",
  "version" : "0.1.0",
  "name" : "Referenspopulation",
  "title" : "Referenspopulation",
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
  "description" : "Den grupp man jämför med målpopulationen.\n\nReferenspopulationen måste stämma överens med målpopulationen i fråga om ålder, kön och sådana saker som spelar roll i sammanhanget.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Referenspopulation",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "Referenspopulation",
      "path" : "Referenspopulation",
      "short" : "Referenspopulation",
      "definition" : "Den grupp man jämför med målpopulationen.\n\nReferenspopulationen måste stämma överens med målpopulationen i fråga om ålder, kön och sådana saker som spelar roll i sammanhanget."
    },
    {
      "id" : "Referenspopulation.liggerTillGrundFor",
      "path" : "Referenspopulation.liggerTillGrundFor",
      "short" : "Source attribute: ligger till grund för",
      "definition" : "Source attribute: ligger till grund för",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Referensintervall"
      }]
    },
    {
      "id" : "Referenspopulation.jamforsMed",
      "path" : "Referenspopulation.jamforsMed",
      "short" : "Source attribute: jämförs med",
      "definition" : "Source attribute: jämförs med",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Malpopulation"
      }]
    }]
  }
}

```
