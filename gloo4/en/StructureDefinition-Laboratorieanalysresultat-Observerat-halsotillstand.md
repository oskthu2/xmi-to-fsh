# Laboratorieanalysresultat : Observerat hälsotillstånd - gloo4 v0.1.0

## Logical Model: Laboratorieanalysresultat : Observerat hälsotillstånd 

 
Resultat av en laboratorieanalys. 
Ett laboratorieanalysresultat kan utgöras av t.ex. ett fynd (som har sina egenskaper) eller ett mätvärde.
 Exempel på fynd är en viss bakterieart eller en viss typ av virus. 
 Exempel på ett fynds egenskaper är serotyp, subserotyp och koncentration. 

**Usages:**

* Use this Logical Model: [Laboratorieanalys : Aktivitet (inom hälso- och sjukvård)](StructureDefinition-Laboratorieanalys-Aktivitet-inom-halso--och-sjukvard.md), [Laboratoriesvar : Dokument (inom hälso- och sjukvård)](StructureDefinition-Laboratoriesvar-Dokument-inom-halso--och-sjukvard.md), [Mikroorganism](StructureDefinition-Mikroorganism.md), [Referensintervall](StructureDefinition-Referensintervall.md)... Show 2 more, [Referensvärde](StructureDefinition-Referensvarde.md) and [Signering : Deltagande](StructureDefinition-Signering-Deltagande-2.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/gloo4|current/StructureDefinition/StructureDefinition-Laboratorieanalysresultat-Observerat-halsotillstand.json)

### Formal Views of Profile Content

 [Description Differentials, Snapshots, and other representations](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](../StructureDefinition-Laboratorieanalysresultat-Observerat-halsotillstand.csv), [Excel](../StructureDefinition-Laboratorieanalysresultat-Observerat-halsotillstand.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "Laboratorieanalysresultat-Observerat-halsotillstand",
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-type-characteristics",
    "valueCode" : "can-be-target"
  }],
  "url" : "http://example.org/fhir/gloo4/StructureDefinition/Laboratorieanalysresultat-Observerat-halsotillstand",
  "version" : "0.1.0",
  "name" : "LaboratorieanalysresultatObserverathalsotillstand",
  "title" : "Laboratorieanalysresultat : Observerat hälsotillstånd",
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
  "description" : "Resultat av en laboratorieanalys. \n \nEtt laboratorieanalysresultat kan utgöras av t.ex. ett fynd (som har sina egenskaper) eller ett mätvärde.  \nExempel på fynd är en viss bakterieart eller en viss typ av virus.   \nExempel på ett fynds egenskaper är serotyp, subserotyp och koncentration.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://example.org/fhir/gloo4/StructureDefinition/Laboratorieanalysresultat-Observerat-halsotillstand",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "Laboratorieanalysresultat-Observerat-halsotillstand",
      "path" : "Laboratorieanalysresultat-Observerat-halsotillstand",
      "short" : "Laboratorieanalysresultat : Observerat hälsotillstånd",
      "definition" : "Resultat av en laboratorieanalys. \n \nEtt laboratorieanalysresultat kan utgöras av t.ex. ett fynd (som har sina egenskaper) eller ett mätvärde.  \nExempel på fynd är en viss bakterieart eller en viss typ av virus.   \nExempel på ett fynds egenskaper är serotyp, subserotyp och koncentration."
    },
    {
      "id" : "Laboratorieanalysresultat-Observerat-halsotillstand.gallerFor",
      "path" : "Laboratorieanalysresultat-Observerat-halsotillstand.gallerFor",
      "short" : "Source attribute: gäller för",
      "definition" : "Source attribute: gäller för",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/gloo4/StructureDefinition/Referensintervall"
      }]
    },
    {
      "id" : "Laboratorieanalysresultat-Observerat-halsotillstand.gorsAv",
      "path" : "Laboratorieanalysresultat-Observerat-halsotillstand.gorsAv",
      "short" : "Source attribute: görs av",
      "definition" : "Source attribute: görs av",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/gloo4/StructureDefinition/Signering-Deltagande-2"
      }]
    },
    {
      "id" : "Laboratorieanalysresultat-Observerat-halsotillstand.arResultatAv",
      "path" : "Laboratorieanalysresultat-Observerat-halsotillstand.arResultatAv",
      "short" : "Source attribute: är resultat av",
      "definition" : "Source attribute: är resultat av",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/gloo4/StructureDefinition/Laboratorieanalys-Aktivitet-inom-halso--och-sjukvard"
      }]
    },
    {
      "id" : "Laboratorieanalysresultat-Observerat-halsotillstand.kanVaraFyndAv",
      "path" : "Laboratorieanalysresultat-Observerat-halsotillstand.kanVaraFyndAv",
      "short" : "Source attribute: kan vara fynd av",
      "definition" : "Source attribute: kan vara fynd av",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/gloo4/StructureDefinition/Mikroorganism"
      }]
    },
    {
      "id" : "Laboratorieanalysresultat-Observerat-halsotillstand.innehaller",
      "path" : "Laboratorieanalysresultat-Observerat-halsotillstand.innehaller",
      "short" : "Source attribute: innehåller",
      "definition" : "Source attribute: innehåller",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/gloo4/StructureDefinition/Laboratoriesvar-Dokument-inom-halso--och-sjukvard"
      }]
    },
    {
      "id" : "Laboratorieanalysresultat-Observerat-halsotillstand.gallerFor2",
      "path" : "Laboratorieanalysresultat-Observerat-halsotillstand.gallerFor2",
      "short" : "Source attribute: gäller för",
      "definition" : "Source attribute: gäller för",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/gloo4/StructureDefinition/Referensvarde"
      }]
    }]
  }
}

```
