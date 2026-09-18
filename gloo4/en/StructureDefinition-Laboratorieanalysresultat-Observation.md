# Laboratorieanalysresultat : Observation - gloo4 v0.1.0

## Logical Model: Laboratorieanalysresultat : Observation 

 
Klassen Laboratorieanalysresultat håller information om resultat av en utförd analys. 
Detta resultat kan exempelvis bestå av ett mätvärde inom laboratoriedisciplinen kemi, ett fynd av en viss bakterieart eller en textuell beskrivning av analysresultatet. Utöver detta kan en kommentar avseende analysresultatet anges separat. 

**Usages:**

* Use this Logical Model: [Laboratorieanalys : Aktivitet](StructureDefinition-Laboratorieanalys-Aktivitet.md), [Referens](StructureDefinition-Referens.md) and [Signering : Deltagande](StructureDefinition-Signering-Deltagande.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/gloo4|current/StructureDefinition/StructureDefinition-Laboratorieanalysresultat-Observation.json)

### Formal Views of Profile Content

 [Description Differentials, Snapshots, and other representations](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](../StructureDefinition-Laboratorieanalysresultat-Observation.csv), [Excel](../StructureDefinition-Laboratorieanalysresultat-Observation.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "Laboratorieanalysresultat-Observation",
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-type-characteristics",
    "valueCode" : "can-be-target"
  }],
  "url" : "http://example.org/fhir/gloo4/StructureDefinition/Laboratorieanalysresultat-Observation",
  "version" : "0.1.0",
  "name" : "LaboratorieanalysresultatObservation",
  "title" : "Laboratorieanalysresultat : Observation",
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
  "description" : "Klassen Laboratorieanalysresultat håller information om resultat av en utförd analys.\n\nDetta resultat kan exempelvis bestå av ett mätvärde inom laboratoriedisciplinen kemi, ett fynd av en viss bakterieart eller en textuell beskrivning av analysresultatet. Utöver detta kan en kommentar avseende analysresultatet anges separat.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://example.org/fhir/gloo4/StructureDefinition/Laboratorieanalysresultat-Observation",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "Laboratorieanalysresultat-Observation",
      "path" : "Laboratorieanalysresultat-Observation",
      "short" : "Laboratorieanalysresultat : Observation",
      "definition" : "Klassen Laboratorieanalysresultat håller information om resultat av en utförd analys.\n\nDetta resultat kan exempelvis bestå av ett mätvärde inom laboratoriedisciplinen kemi, ett fynd av en viss bakterieart eller en textuell beskrivning av analysresultatet. Utöver detta kan en kommentar avseende analysresultatet anges separat."
    },
    {
      "id" : "Laboratorieanalysresultat-Observation.typ",
      "path" : "Laboratorieanalysresultat-Observation.typ",
      "short" : "Source attribute: typ",
      "definition" : "Kod för typ av laboratorieanalysresultat.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/gloo4/StructureDefinition/CV"
      }]
    },
    {
      "id" : "Laboratorieanalysresultat-Observation.varde",
      "path" : "Laboratorieanalysresultat-Observation.varde",
      "short" : "Source attribute: värde",
      "definition" : "Angivelse av utfall av en utförd analys.\n\nPQ|IVL<PQ>|ST|CV",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "Laboratorieanalysresultat-Observation.kommentar",
      "path" : "Laboratorieanalysresultat-Observation.kommentar",
      "short" : "Source attribute: kommentar",
      "definition" : "Angivelse av kommentar som rör laboratorieanalysresultatet.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/gloo4/StructureDefinition/ST"
      }]
    },
    {
      "id" : "Laboratorieanalysresultat-Observation.tolkning",
      "path" : "Laboratorieanalysresultat-Observation.tolkning",
      "short" : "Source attribute: tolkning",
      "definition" : "Kod för en tolkning av laboratorieanalysresultatet.  \n\nEn sådan tolkning kan vara att analysresultatet ligger utanför aktuellt referensintervall, vilket även benämns som patologisk markör.",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "http://example.org/fhir/gloo4/StructureDefinition/CV"
      }]
    },
    {
      "id" : "Laboratorieanalysresultat-Observation.negation",
      "path" : "Laboratorieanalysresultat-Observation.negation",
      "short" : "Source attribute: negation",
      "definition" : "Source attribute: negation",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/gloo4/StructureDefinition/BL"
      }]
    },
    {
      "id" : "Laboratorieanalysresultat-Observation.harResultat",
      "path" : "Laboratorieanalysresultat-Observation.harResultat",
      "short" : "Source attribute: har resultat",
      "definition" : "Source attribute: har resultat",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/gloo4/StructureDefinition/Laboratorieanalys-Aktivitet"
      }]
    },
    {
      "id" : "Laboratorieanalysresultat-Observation.foranlederFordjupad",
      "path" : "Laboratorieanalysresultat-Observation.foranlederFordjupad",
      "short" : "Source attribute: föranleder fördjupad",
      "definition" : "Source attribute: föranleder fördjupad",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "http://example.org/fhir/gloo4/StructureDefinition/Laboratorieanalys-Aktivitet"
      }]
    },
    {
      "id" : "Laboratorieanalysresultat-Observation.jamforsMed",
      "path" : "Laboratorieanalysresultat-Observation.jamforsMed",
      "short" : "Source attribute: jämförs med",
      "definition" : "Source attribute: jämförs med",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/gloo4/StructureDefinition/Referens"
      }]
    },
    {
      "id" : "Laboratorieanalysresultat-Observation.harMottagares",
      "path" : "Laboratorieanalysresultat-Observation.harMottagares",
      "short" : "Source attribute: har mottagares",
      "definition" : "Source attribute: har mottagares",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/gloo4/StructureDefinition/Signering-Deltagande"
      }]
    },
    {
      "id" : "Laboratorieanalysresultat-Observation.harUtforares",
      "path" : "Laboratorieanalysresultat-Observation.harUtforares",
      "short" : "Source attribute: har utförares",
      "definition" : "Source attribute: har utförares",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/gloo4/StructureDefinition/Signering-Deltagande"
      }]
    }]
  }
}

```
