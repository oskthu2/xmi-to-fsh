# Referens - gloo4 v0.1.0

## Logical Model: Referens 

 
Klassen Referens håller information om vilket referensintervall eller referensvärde som gäller för ett resultat. 

**Usages:**

* Use this Logical Model: [Laboratorieanalysresultat : Observation](StructureDefinition-Laboratorieanalysresultat-Observation.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/gloo4|current/StructureDefinition/StructureDefinition-Referens.json)

### Formal Views of Profile Content

 [Description Differentials, Snapshots, and other representations](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](../StructureDefinition-Referens.csv), [Excel](../StructureDefinition-Referens.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "Referens",
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-type-characteristics",
    "valueCode" : "can-be-target"
  }],
  "url" : "http://example.org/fhir/gloo4/StructureDefinition/Referens",
  "version" : "0.1.0",
  "name" : "Referens",
  "title" : "Referens",
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
  "description" : "Klassen Referens håller information om vilket referensintervall eller referensvärde som gäller för ett resultat.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://example.org/fhir/gloo4/StructureDefinition/Referens",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "Referens",
      "path" : "Referens",
      "short" : "Referens",
      "definition" : "Klassen Referens håller information om vilket referensintervall eller referensvärde som gäller för ett resultat."
    },
    {
      "id" : "Referens.intervall",
      "path" : "Referens.intervall",
      "short" : "Source attribute: intervall",
      "definition" : "Angivelse av referensintervall som numeriskt värde av mätvärden. Ett referensvärde anges genom att antingen ange ett intervall från det lägre värdet 0 till det högre värdet som sätts till referensvärdet, alternativt från referensvärde som start på intervallet utan angivelse av intervallets slut för att ange att normalvärde ligger över referensvärdet.\n\nEtt och endast ett av attributen intervall eller text ska anges.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "Referens.text",
      "path" : "Referens.text",
      "short" : "Source attribute: text",
      "definition" : "Textuell beskrivning av referensintervall.\n\nEtt och endast ett av attributen intervall eller text ska anges.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/gloo4/StructureDefinition/ST"
      }]
    },
    {
      "id" : "Referens.population",
      "path" : "Referens.population",
      "short" : "Source attribute: population",
      "definition" : "Angivelse av den referenspopulation som ligger till grund för angivet referensintervall.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/gloo4/StructureDefinition/ST"
      }]
    },
    {
      "id" : "Referens.kommentar",
      "path" : "Referens.kommentar",
      "short" : "Source attribute: kommentar",
      "definition" : "Angivelse av kommentar för det angivna referensintervallet.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/gloo4/StructureDefinition/ST"
      }]
    },
    {
      "id" : "Referens.jamforsMed",
      "path" : "Referens.jamforsMed",
      "short" : "Source attribute: jämförs med",
      "definition" : "Source attribute: jämförs med",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "http://example.org/fhir/gloo4/StructureDefinition/Laboratorieanalysresultat-Observation"
      }]
    }]
  }
}

```
