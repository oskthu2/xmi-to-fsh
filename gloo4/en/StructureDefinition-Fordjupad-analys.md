# Fördjupad analys - gloo4 v0.1.0

## Logical Model: Fördjupad analys 

 
Ytterligare analys föranledd av specifikt analysresultat. 
2018-03-14: Vi stryker denna i begreppsmodellen, det löser sig i informationsmodellen. 
Vad är skillnad mellan fördjupad analys och konfirmationsanalys som de pratade om på mötet? Är det samma? 
2018-03-09: Jonas Svanberg: 
 För mig oklart begrepp. Möjligen kan man mena ”analys/undersökning som normalt inte utförs i aktuell situation”. För mig är det bara en ytterligare Fyndegenskap (8.4).
 Eller avses ”analys som utförs pga. resultatet i beställd analys, och som inte är beställd från början”? Och behövs för att hantera den situationen? 

**Usages:**

* Use this Logical Model: [Laboratorieanalys : Aktivitet (inom hälso- och sjukvård)](StructureDefinition-Laboratorieanalys-Aktivitet-inom-halso--och-sjukvard.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/gloo4|current/StructureDefinition/StructureDefinition-Fordjupad-analys.json)

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
  "url" : "http://example.org/fhir/gloo4/StructureDefinition/Fordjupad-analys",
  "version" : "0.1.0",
  "name" : "Fordjupadanalys",
  "title" : "Fördjupad analys",
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
  "description" : "Ytterligare analys föranledd av specifikt analysresultat. \n\n2018-03-14: Vi stryker denna i begreppsmodellen, det löser sig i informationsmodellen. \n\nVad är skillnad mellan fördjupad analys och konfirmationsanalys som de pratade om på mötet? Är det samma? \n\n2018-03-09: Jonas Svanberg:   \nFör mig oklart begrepp. Möjligen kan man mena ”analys/undersökning som normalt inte utförs i aktuell situation”. För mig är det bara en ytterligare Fyndegenskap (8.4).  \nEller avses ”analys som utförs pga. resultatet i beställd analys, och som inte är beställd från början”? Och behövs för att hantera den situationen?",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://example.org/fhir/gloo4/StructureDefinition/Fordjupad-analys",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "Fordjupad-analys",
      "path" : "Fordjupad-analys",
      "short" : "Fördjupad analys",
      "definition" : "Ytterligare analys föranledd av specifikt analysresultat. \n\n2018-03-14: Vi stryker denna i begreppsmodellen, det löser sig i informationsmodellen. \n\nVad är skillnad mellan fördjupad analys och konfirmationsanalys som de pratade om på mötet? Är det samma? \n\n2018-03-09: Jonas Svanberg:   \nFör mig oklart begrepp. Möjligen kan man mena ”analys/undersökning som normalt inte utförs i aktuell situation”. För mig är det bara en ytterligare Fyndegenskap (8.4).  \nEller avses ”analys som utförs pga. resultatet i beställd analys, och som inte är beställd från början”? Och behövs för att hantera den situationen?"
    },
    {
      "id" : "Fordjupad-analys.arEn",
      "path" : "Fordjupad-analys.arEn",
      "short" : "Source attribute: är en",
      "definition" : "Source attribute: är en",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/gloo4/StructureDefinition/Laboratorieanalys-Aktivitet-inom-halso--och-sjukvard"
      }]
    }]
  }
}

```
