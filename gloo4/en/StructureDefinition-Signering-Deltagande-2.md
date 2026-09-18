# Signering : Deltagande - gloo4 v0.1.0

## Logical Model: Signering : Deltagande 

 
Påförande av signatur. 
Inom laboratoriedomänen finns det fyra olika typer av signering. Signeringen avser hela laboratoriesvaret eller enskilda analyser. 
1. Laboratoriesvaret signeras av en medicinskt ansvarig hälso- och sjukvårdspersonal på den ansvariga enheten.
 
Den ansvariga enheten kan vara den remissvarsmottagande enheten eller den utförande enheten (exempelvis vid patientnära analyser). 
1. En enskild analys signeras av den hälso- och sjukvårdspersonal som utför analysen.
1. Laboratoriesvaret signeras av hälso- och sjukvårdspersonal på den remissvarsmottagande enheten när det förs in i patientjournalen.
1. En enskild analys signeras av hälso- och sjukvårdspersonal på den remissvarsmottagande enheten när den förs in i patientjournalen.
 

**Usages:**

* Use this Logical Model: [: Hälso- och sjukvårdspersonal](StructureDefinition-Halso--och-sjukvardspersonal.md), [Laboratorieanalysresultat : Observerat hälsotillstånd](StructureDefinition-Laboratorieanalysresultat-Observerat-halsotillstand.md), [Remissvar : Dokument (inom hälso- och sjukvård)](StructureDefinition-Remissvar-Dokument-inom-halso--och-sjukvard.md) and [Signatur](StructureDefinition-Signatur.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/gloo4|current/StructureDefinition/StructureDefinition-Signering-Deltagande-2.json)

### Formal Views of Profile Content

 [Description Differentials, Snapshots, and other representations](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](../StructureDefinition-Signering-Deltagande-2.csv), [Excel](../StructureDefinition-Signering-Deltagande-2.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "Signering-Deltagande-2",
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-type-characteristics",
    "valueCode" : "can-be-target"
  }],
  "url" : "http://example.org/fhir/gloo4/StructureDefinition/Signering-Deltagande-2",
  "version" : "0.1.0",
  "name" : "SigneringDeltagande2",
  "title" : "Signering : Deltagande",
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
  "description" : "Påförande av signatur.  \n   \nInom laboratoriedomänen finns det fyra olika typer av signering. Signeringen avser hela laboratoriesvaret eller enskilda analyser.\n\n1. Laboratoriesvaret signeras av en medicinskt ansvarig hälso- och sjukvårdspersonal på den ansvariga enheten.\n\nDen ansvariga enheten kan vara den remissvarsmottagande enheten eller den utförande enheten (exempelvis vid patientnära analyser).\n\n2. En enskild analys signeras av den hälso- och sjukvårdspersonal som utför analysen.\n\n3. Laboratoriesvaret signeras av hälso- och sjukvårdspersonal på den remissvarsmottagande enheten när det förs in i patientjournalen.\n\n4. En enskild analys signeras av hälso- och sjukvårdspersonal på den remissvarsmottagande enheten när den förs in i patientjournalen.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://example.org/fhir/gloo4/StructureDefinition/Signering-Deltagande-2",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "Signering-Deltagande-2",
      "path" : "Signering-Deltagande-2",
      "short" : "Signering : Deltagande",
      "definition" : "Påförande av signatur.  \n   \nInom laboratoriedomänen finns det fyra olika typer av signering. Signeringen avser hela laboratoriesvaret eller enskilda analyser.\n\n1. Laboratoriesvaret signeras av en medicinskt ansvarig hälso- och sjukvårdspersonal på den ansvariga enheten.\n\nDen ansvariga enheten kan vara den remissvarsmottagande enheten eller den utförande enheten (exempelvis vid patientnära analyser).\n\n2. En enskild analys signeras av den hälso- och sjukvårdspersonal som utför analysen.\n\n3. Laboratoriesvaret signeras av hälso- och sjukvårdspersonal på den remissvarsmottagande enheten när det förs in i patientjournalen.\n\n4. En enskild analys signeras av hälso- och sjukvårdspersonal på den remissvarsmottagande enheten när den förs in i patientjournalen."
    },
    {
      "id" : "Signering-Deltagande-2.gorsAv",
      "path" : "Signering-Deltagande-2.gorsAv",
      "short" : "Source attribute: görs av",
      "definition" : "Source attribute: görs av",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/gloo4/StructureDefinition/Laboratorieanalysresultat-Observerat-halsotillstand"
      }]
    },
    {
      "id" : "Signering-Deltagande-2.gorsAv2",
      "path" : "Signering-Deltagande-2.gorsAv2",
      "short" : "Source attribute: görs av",
      "definition" : "Source attribute: görs av",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/gloo4/StructureDefinition/Halso--och-sjukvardspersonal"
      }]
    },
    {
      "id" : "Signering-Deltagande-2.gorsAv3",
      "path" : "Signering-Deltagande-2.gorsAv3",
      "short" : "Source attribute: görs av",
      "definition" : "Source attribute: görs av",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/gloo4/StructureDefinition/Remissvar-Dokument-inom-halso--och-sjukvard"
      }]
    },
    {
      "id" : "Signering-Deltagande-2.arResultatAv",
      "path" : "Signering-Deltagande-2.arResultatAv",
      "short" : "Source attribute: är resultat av",
      "definition" : "Source attribute: är resultat av",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/gloo4/StructureDefinition/Signatur"
      }]
    }]
  }
}

```
