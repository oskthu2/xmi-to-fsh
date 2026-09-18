# Laboratorieanalys : Aktivitet - Logical Models from Visual Paradigm XMI v0.1.0

## Logical Model: Laboratorieanalys : Aktivitet 

 
Klassen Laboratorieanalys håller information om en analys 

**Usages:**

* Use this Logical Model: [Analysgrupp](StructureDefinition-Analysgrupp.md), [Analysutrustning : Resurs](StructureDefinition-Analysutrustning-Resurs.md), [Laboratorieanalysresultat : Observation](StructureDefinition-Laboratorieanalysresultat-Observation.md), [Organisatorisk enhet : Organisatorisk enhet](StructureDefinition-Organisatorisk-enhet-Organisatorisk-enhet.md) and [Prov : Resurs](StructureDefinition-Prov-Resurs.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/xmi.to.fsh|current/StructureDefinition/StructureDefinition-Laboratorieanalys-Aktivitet.json)

### Formal Views of Profile Content

 [Description Differentials, Snapshots, and other representations](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](../StructureDefinition-Laboratorieanalys-Aktivitet.csv), [Excel](../StructureDefinition-Laboratorieanalys-Aktivitet.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "Laboratorieanalys-Aktivitet",
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-type-characteristics",
    "valueCode" : "can-be-target"
  }],
  "url" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Laboratorieanalys-Aktivitet",
  "version" : "0.1.0",
  "name" : "LaboratorieanalysAktivitet",
  "title" : "Laboratorieanalys : Aktivitet",
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
  "description" : "Klassen Laboratorieanalys håller information om en analys",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Laboratorieanalys-Aktivitet",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "Laboratorieanalys-Aktivitet",
      "path" : "Laboratorieanalys-Aktivitet",
      "short" : "Laboratorieanalys : Aktivitet",
      "definition" : "Klassen Laboratorieanalys håller information om en analys"
    },
    {
      "id" : "Laboratorieanalys-Aktivitet.-id",
      "path" : "Laboratorieanalys-Aktivitet._id",
      "short" : "Source attribute: id; renamed from reserved FSH name 'id'",
      "definition" : "Angivelse av identitetsbeteckning för en laboratorieanalys.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/II"
      }]
    },
    {
      "id" : "Laboratorieanalys-Aktivitet.status",
      "path" : "Laboratorieanalys-Aktivitet.status",
      "short" : "Source attribute: status",
      "definition" : "Kod för analysens status.",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/CV"
      }]
    },
    {
      "id" : "Laboratorieanalys-Aktivitet.kod",
      "path" : "Laboratorieanalys-Aktivitet.kod",
      "short" : "Source attribute: kod",
      "definition" : "Kod för den typ av analys som utförts.\n\nOm kod inte kan anges från nationellt urval kan originalText användas för textalternativ.",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/CV-CWE"
      }]
    },
    {
      "id" : "Laboratorieanalys-Aktivitet.tid",
      "path" : "Laboratorieanalys-Aktivitet.tid",
      "short" : "Source attribute: tid",
      "definition" : "Angivelse av tidpunkt då analysen utfördes.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/TS"
      }]
    },
    {
      "id" : "Laboratorieanalys-Aktivitet.metod",
      "path" : "Laboratorieanalys-Aktivitet.metod",
      "short" : "Source attribute: metod",
      "definition" : "Kod för den typ av tillvägagångssätt för utförandet av analysen som avses.\n\nOm kod inte kan anges från nationellt urval kan originalText användas för textalternativ.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/CV-CWE"
      }]
    },
    {
      "id" : "Laboratorieanalys-Aktivitet.kommentar",
      "path" : "Laboratorieanalys-Aktivitet.kommentar",
      "short" : "Source attribute: kommentar",
      "definition" : "Angivelse av kommentar för en enskild analys.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/ST"
      }]
    },
    {
      "id" : "Laboratorieanalys-Aktivitet.ackrediteradMetod",
      "path" : "Laboratorieanalys-Aktivitet.ackrediteradMetod",
      "short" : "Source attribute: ackrediterad metod",
      "definition" : "Angivelse av om analysmetoden är ackrediterad eller inte.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/BL"
      }]
    },
    {
      "id" : "Laboratorieanalys-Aktivitet.bestarAv",
      "path" : "Laboratorieanalys-Aktivitet.bestarAv",
      "short" : "Source attribute: består av",
      "definition" : "Source attribute: består av",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Analysgrupp"
      }]
    },
    {
      "id" : "Laboratorieanalys-Aktivitet.harAnvant",
      "path" : "Laboratorieanalys-Aktivitet.harAnvant",
      "short" : "Source attribute: har använt",
      "definition" : "Source attribute: har använt",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Analysutrustning-Resurs"
      }]
    },
    {
      "id" : "Laboratorieanalys-Aktivitet.harUtforande",
      "path" : "Laboratorieanalys-Aktivitet.harUtforande",
      "short" : "Source attribute: har utförande",
      "definition" : "Source attribute: har utförande",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Organisatorisk-enhet-Organisatorisk-enhet"
      }]
    },
    {
      "id" : "Laboratorieanalys-Aktivitet.harResultat",
      "path" : "Laboratorieanalys-Aktivitet.harResultat",
      "short" : "Source attribute: har resultat",
      "definition" : "Source attribute: har resultat",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Laboratorieanalysresultat-Observation"
      }]
    },
    {
      "id" : "Laboratorieanalys-Aktivitet.avser",
      "path" : "Laboratorieanalys-Aktivitet.avser",
      "short" : "Source attribute: avser",
      "definition" : "Source attribute: avser",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Prov-Resurs"
      }]
    },
    {
      "id" : "Laboratorieanalys-Aktivitet.foranlederFordjupad",
      "path" : "Laboratorieanalys-Aktivitet.foranlederFordjupad",
      "short" : "Source attribute: föranleder fördjupad",
      "definition" : "Source attribute: föranleder fördjupad",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Laboratorieanalysresultat-Observation"
      }]
    }]
  }
}

```
