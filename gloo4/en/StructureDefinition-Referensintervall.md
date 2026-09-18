# Referensintervall - gloo4 v0.1.0

## Logical Model: Referensintervall 

 
Det intervall som värden för ett fysiologiskt mätvärde hos en referenspopulation med e n given sannolikhet ligger inom för den givna typen av analys med den givna metoden. 
Referensintervallet utgör en bas för jämförelse (en referensram) för att tolka ett analysresultat för en viss patient. 

**Usages:**

* Use this Logical Model: [Laboratorieanalysresultat : Observerat hälsotillstånd](StructureDefinition-Laboratorieanalysresultat-Observerat-halsotillstand.md) and [Referenspopulation](StructureDefinition-Referenspopulation.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/gloo4|current/StructureDefinition/StructureDefinition-Referensintervall.json)

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
  "url" : "http://example.org/fhir/gloo4/StructureDefinition/Referensintervall",
  "version" : "0.1.0",
  "name" : "Referensintervall",
  "title" : "Referensintervall",
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
  "description" : "Det intervall som värden för ett fysiologiskt mätvärde hos  en referenspopulation   med e  n   given sannolikhet  ligger inom för den givna typen av analys med den givna metoden.\n\nReferensintervallet utgör en bas för jämförelse (en referensram) för att tolka ett analysresultat för en viss patient.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://example.org/fhir/gloo4/StructureDefinition/Referensintervall",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "Referensintervall",
      "path" : "Referensintervall",
      "short" : "Referensintervall",
      "definition" : "Det intervall som värden för ett fysiologiskt mätvärde hos  en referenspopulation   med e  n   given sannolikhet  ligger inom för den givna typen av analys med den givna metoden.\n\nReferensintervallet utgör en bas för jämförelse (en referensram) för att tolka ett analysresultat för en viss patient."
    },
    {
      "id" : "Referensintervall.liggerTillGrundFor",
      "path" : "Referensintervall.liggerTillGrundFor",
      "short" : "Source attribute: ligger till grund för",
      "definition" : "Source attribute: ligger till grund för",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/gloo4/StructureDefinition/Referenspopulation"
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
        "code" : "http://example.org/fhir/gloo4/StructureDefinition/Laboratorieanalysresultat-Observerat-halsotillstand"
      }]
    }]
  }
}

```
