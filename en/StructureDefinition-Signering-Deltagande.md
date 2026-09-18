# Signering : Deltagande - Logical Models from Visual Paradigm XMI v0.1.0

## Logical Model: Signering : Deltagande 

 
Klassen Signering håller information om tidsangivelse då ett relaterat objekt är signerat. Inom laboratoriedomänen finns det fyra olika typer av signering. Signeringen avser hela laboratoriesvaret eller enskilda analyser. 
1. Laboratoriesvaret signeras av en medicinskt ansvarig hälso- och sjukvårdspersonal på den ansvariga enheten. Den ansvariga enheten kan vara den remissvarsmottagande enheten eller den utförande enheten (exempelvis vid patientnära analyser).
1. En enskild analys signeras av den hälso- och sjukvårdspersonal som utför analysen.
1. Laboratoriesvaret signeras av hälso- och sjukvårdspersonal på den remissvarsmottagande enheten när det förs in i patientjournalen.
1. En enskild analys signeras av hälso- och sjukvårdspersonal på den remissvarsmottagande enheten när den förs in i patientjournalen.
 

**Usages:**

* Use this Logical Model: [Hälso- och sjukvårdspersonal : Hälso- och sjukvårdspersonal](StructureDefinition-Halso--och-sjukvardspersonal-Halso--och-sjukvardsperson.md), [Laboratorieanalysresultat : Observation](StructureDefinition-Laboratorieanalysresultat-Observation.md) and [Laboratoriesvar : Dokument](StructureDefinition-Laboratoriesvar-Dokument.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/xmi.to.fsh|current/StructureDefinition/StructureDefinition-Signering-Deltagande.json)

### Formal Views of Profile Content

 [Description Differentials, Snapshots, and other representations](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](../StructureDefinition-Signering-Deltagande.csv), [Excel](../StructureDefinition-Signering-Deltagande.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "Signering-Deltagande",
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-type-characteristics",
    "valueCode" : "can-be-target"
  }],
  "url" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Signering-Deltagande",
  "version" : "0.1.0",
  "name" : "SigneringDeltagande",
  "title" : "Signering : Deltagande",
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
  "description" : "Klassen Signering håller information om tidsangivelse då ett relaterat objekt är signerat.\nInom laboratoriedomänen finns det fyra olika typer av signering. Signeringen avser hela laboratoriesvaret eller enskilda analyser.\n1. Laboratoriesvaret signeras av en medicinskt ansvarig hälso- och sjukvårdspersonal på den ansvariga enheten.\nDen ansvariga enheten kan vara den remissvarsmottagande enheten eller den utförande enheten (exempelvis vid patientnära analyser).\n2. En enskild analys signeras av den hälso- och sjukvårdspersonal som utför analysen.\n3. Laboratoriesvaret signeras av hälso- och sjukvårdspersonal på den remissvarsmottagande enheten när det förs in i patientjournalen.\n4. En enskild analys signeras av hälso- och sjukvårdspersonal på den remissvarsmottagande enheten när den förs in i patientjournalen.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Signering-Deltagande",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "Signering-Deltagande",
      "path" : "Signering-Deltagande",
      "short" : "Signering : Deltagande",
      "definition" : "Klassen Signering håller information om tidsangivelse då ett relaterat objekt är signerat.\nInom laboratoriedomänen finns det fyra olika typer av signering. Signeringen avser hela laboratoriesvaret eller enskilda analyser.\n1. Laboratoriesvaret signeras av en medicinskt ansvarig hälso- och sjukvårdspersonal på den ansvariga enheten.\nDen ansvariga enheten kan vara den remissvarsmottagande enheten eller den utförande enheten (exempelvis vid patientnära analyser).\n2. En enskild analys signeras av den hälso- och sjukvårdspersonal som utför analysen.\n3. Laboratoriesvaret signeras av hälso- och sjukvårdspersonal på den remissvarsmottagande enheten när det förs in i patientjournalen.\n4. En enskild analys signeras av hälso- och sjukvårdspersonal på den remissvarsmottagande enheten när den förs in i patientjournalen."
    },
    {
      "id" : "Signering-Deltagande.tidpunkt",
      "path" : "Signering-Deltagande.tidpunkt",
      "short" : "Source attribute: tidpunkt",
      "definition" : "Angivelse av tidpunkt då signering genomfördes.",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/TS"
      }]
    },
    {
      "id" : "Signering-Deltagande.harMottgares",
      "path" : "Signering-Deltagande.harMottgares",
      "short" : "Source attribute: har mottgares",
      "definition" : "Source attribute: har mottgares",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Laboratoriesvar-Dokument"
      }]
    },
    {
      "id" : "Signering-Deltagande.harAnsvarigs",
      "path" : "Signering-Deltagande.harAnsvarigs",
      "short" : "Source attribute: har ansvarigs",
      "definition" : "Source attribute: har ansvarigs",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Laboratoriesvar-Dokument"
      }]
    },
    {
      "id" : "Signering-Deltagande.harMottagares",
      "path" : "Signering-Deltagande.harMottagares",
      "short" : "Source attribute: har mottagares",
      "definition" : "Source attribute: har mottagares",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Laboratorieanalysresultat-Observation"
      }]
    },
    {
      "id" : "Signering-Deltagande.harUtforares",
      "path" : "Signering-Deltagande.harUtforares",
      "short" : "Source attribute: har utförares",
      "definition" : "Source attribute: har utförares",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Laboratorieanalysresultat-Observation"
      }]
    },
    {
      "id" : "Signering-Deltagande.utforsAv",
      "path" : "Signering-Deltagande.utforsAv",
      "short" : "Source attribute: utförs av",
      "definition" : "Source attribute: utförs av",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Halso--och-sjukvardspersonal-Halso--och-sjukvardsperson"
      }]
    }]
  }
}

```
