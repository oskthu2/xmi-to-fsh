# Revisionshistorik - Logical Models from Visual Paradigm XMI v0.1.0

## Logical Model: Revisionshistorik 

 
Supporting logical model generated from gloo4.xmi (source class: Revisionshistorik). 

**Usages:**

* This Logical Model is not used by any profiles in this Specification

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/xmi.to.fsh|current/StructureDefinition/StructureDefinition-Revisionshistorik.json)

### Formal Views of Profile Content

 [Description Differentials, Snapshots, and other representations](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](../StructureDefinition-Revisionshistorik.csv), [Excel](../StructureDefinition-Revisionshistorik.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "Revisionshistorik",
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-type-characteristics",
    "valueCode" : "can-be-target"
  }],
  "url" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Revisionshistorik",
  "version" : "0.1.0",
  "name" : "Revisionshistorik",
  "title" : "Revisionshistorik",
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
  "description" : "Supporting logical model generated from gloo4.xmi (source class: Revisionshistorik).",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Revisionshistorik",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "Revisionshistorik",
      "path" : "Revisionshistorik",
      "short" : "Revisionshistorik",
      "definition" : "Supporting logical model generated from gloo4.xmi (source class: Revisionshistorik)."
    },
    {
      "id" : "Revisionshistorik.Version40RC2",
      "path" : "Revisionshistorik.Version40RC2",
      "short" : "Source attribute: Version 4.0 RC2; type could not be resolved from source model",
      "definition" : "Ny version 4.0 av laboratoriesvarskontrakt som stödjer mikrobiologiska svar. Förarbete av Fredrik Ström och Helena Antonsson.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "Revisionshistorik.Version40RC5",
      "path" : "Revisionshistorik.Version40RC5",
      "short" : "Source attribute: Version 4.0 RC5; type could not be resolved from source model",
      "definition" : "Fortsatt arbete där koppling till kodverk har förtydligats. Vissa specifika klasser har bytts ut till generiska kombinationer av analys/analysresultat. Begreppsmodellering och terminologi i enlighet med Socialstyrelsens termbank och Nationella Informationsstruktur.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "Revisionshistorik.Version40RC6",
      "path" : "Revisionshistorik.Version40RC6",
      "short" : "Source attribute: Version 4.0 RC6; type could not be resolved from source model",
      "definition" : "Utökade attribut för analysutrustning.\nMöjlighet för mottagare att signera enskilda resultat förutom hela svaret\nÄndrad kardinalitet på signatur från ansvarig för svar.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "Revisionshistorik.Version40RC9",
      "path" : "Revisionshistorik.Version40RC9",
      "short" : "Source attribute: Version 4.0 RC9; type could not be resolved from source model",
      "definition" : "Lagt till coding strength på CV-datatyp (CNE - Coded with No Exceptions och CWE - Coded With Exceptions)",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "Revisionshistorik.Version40",
      "path" : "Revisionshistorik.Version40",
      "short" : "Source attribute: Version 4.0; type could not be resolved from source model",
      "definition" : "Ny informationsspecifikation för laboratoriesvar fastställd.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "Revisionshistorik.Version401",
      "path" : "Revisionshistorik.Version401",
      "short" : "Source attribute: Version 4.0.1; type could not be resolved from source model",
      "definition" : "Uppdaterat samtliga urval.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "Revisionshistorik.f402",
      "path" : "Revisionshistorik.f402",
      "short" : "Source attribute: 4.0.2; type could not be resolved from source model",
      "definition" : "Uppdaterade tomma fält i beskrivningen av informationsmodellen.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "Revisionshistorik.Version41",
      "path" : "Revisionshistorik.Version41",
      "short" : "Source attribute: Version 4.1; type could not be resolved from source model",
      "definition" : "Uppdaterat beskrivningen för olika typer av signeringar.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    }]
  }
}

```
