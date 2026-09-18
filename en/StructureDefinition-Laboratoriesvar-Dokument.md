# Laboratoriesvar : Dokument - Logical Models from Visual Paradigm XMI v0.1.0

## Logical Model: Laboratoriesvar : Dokument 

 
Supporting logical model generated from gloo4.xmi (source class: Laboratoriesvar : Dokument). 

**Usages:**

* Use this Logical Model: [Analysgrupp](StructureDefinition-Analysgrupp.md), [Hälso- och sjukvårdspersonal : Hälso- och sjukvårdspersonal](StructureDefinition-Halso--och-sjukvardspersonal-Halso--och-sjukvardsperson.md), [Kontaktinformation](StructureDefinition-Kontaktinformation.md), [Organisatorisk enhet : Organisatorisk enhet](StructureDefinition-Organisatorisk-enhet-Organisatorisk-enhet.md)... Show 3 more, [Patient : Patient](StructureDefinition-Patient-Patient.md), [Remiss : Dokument](StructureDefinition-Remiss-Dokument.md) and [Signering : Deltagande](StructureDefinition-Signering-Deltagande.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/xmi.to.fsh|current/StructureDefinition/StructureDefinition-Laboratoriesvar-Dokument.json)

### Formal Views of Profile Content

 [Description Differentials, Snapshots, and other representations](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](../StructureDefinition-Laboratoriesvar-Dokument.csv), [Excel](../StructureDefinition-Laboratoriesvar-Dokument.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "Laboratoriesvar-Dokument",
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-type-characteristics",
    "valueCode" : "can-be-target"
  }],
  "url" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Laboratoriesvar-Dokument",
  "version" : "0.1.0",
  "name" : "LaboratoriesvarDokument",
  "title" : "Laboratoriesvar : Dokument",
  "status" : "draft",
  "date" : "2026-09-18T09:59:15+00:00",
  "publisher" : "xmi-to-fsh",
  "contact" : [{
    "name" : "xmi-to-fsh",
    "telecom" : [{
      "system" : "url",
      "value" : "https://github.com/oskthu2/xmi-to-fsh"
    }]
  }],
  "description" : "Supporting logical model generated from gloo4.xmi (source class: Laboratoriesvar : Dokument).",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Laboratoriesvar-Dokument",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "Laboratoriesvar-Dokument",
      "path" : "Laboratoriesvar-Dokument",
      "short" : "Laboratoriesvar : Dokument",
      "definition" : "Supporting logical model generated from gloo4.xmi (source class: Laboratoriesvar : Dokument)."
    },
    {
      "id" : "Laboratoriesvar-Dokument.-id",
      "path" : "Laboratoriesvar-Dokument._id",
      "short" : "Source attribute: id; renamed from reserved FSH name 'id'",
      "definition" : "Source attribute: id; renamed from reserved FSH name 'id'",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/II"
      }]
    },
    {
      "id" : "Laboratoriesvar-Dokument.laboratorieId",
      "path" : "Laboratoriesvar-Dokument.laboratorieId",
      "short" : "Source attribute: laboratorie-id",
      "definition" : "Source attribute: laboratorie-id",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/II"
      }]
    },
    {
      "id" : "Laboratoriesvar-Dokument.typ",
      "path" : "Laboratoriesvar-Dokument.typ",
      "short" : "Source attribute: typ",
      "definition" : "Source attribute: typ",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/CV"
      }]
    },
    {
      "id" : "Laboratoriesvar-Dokument.text",
      "path" : "Laboratoriesvar-Dokument.text",
      "short" : "Source attribute: text",
      "definition" : "Source attribute: text",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/ST"
      }]
    },
    {
      "id" : "Laboratoriesvar-Dokument.svarstidpunkt",
      "path" : "Laboratoriesvar-Dokument.svarstidpunkt",
      "short" : "Source attribute: svarstidpunkt",
      "definition" : "Source attribute: svarstidpunkt",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/TS"
      }]
    },
    {
      "id" : "Laboratoriesvar-Dokument.arAnsvarigForInnehalletI",
      "path" : "Laboratoriesvar-Dokument.arAnsvarigForInnehalletI",
      "short" : "Source attribute: är ansvarig för innehållet i",
      "definition" : "Source attribute: är ansvarig för innehållet i",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Organisatorisk-enhet-Organisatorisk-enhet"
      }]
    },
    {
      "id" : "Laboratoriesvar-Dokument.harSvarsmottagande",
      "path" : "Laboratoriesvar-Dokument.harSvarsmottagande",
      "short" : "Source attribute: har svarsmottagande",
      "definition" : "Source attribute: har svarsmottagande",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Organisatorisk-enhet-Organisatorisk-enhet"
      }]
    },
    {
      "id" : "Laboratoriesvar-Dokument.bestarAv",
      "path" : "Laboratoriesvar-Dokument.bestarAv",
      "short" : "Source attribute: består av",
      "definition" : "Source attribute: består av",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Analysgrupp"
      }]
    },
    {
      "id" : "Laboratoriesvar-Dokument.avser",
      "path" : "Laboratoriesvar-Dokument.avser",
      "short" : "Source attribute: avser",
      "definition" : "Source attribute: avser",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Patient-Patient"
      }]
    },
    {
      "id" : "Laboratoriesvar-Dokument.harMottgares",
      "path" : "Laboratoriesvar-Dokument.harMottgares",
      "short" : "Source attribute: har mottgares",
      "definition" : "Source attribute: har mottgares",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Signering-Deltagande"
      }]
    },
    {
      "id" : "Laboratoriesvar-Dokument.harAnsvarigs",
      "path" : "Laboratoriesvar-Dokument.harAnsvarigs",
      "short" : "Source attribute: har ansvarigs",
      "definition" : "Source attribute: har ansvarigs",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Signering-Deltagande"
      }]
    },
    {
      "id" : "Laboratoriesvar-Dokument.innehaller",
      "path" : "Laboratoriesvar-Dokument.innehaller",
      "short" : "Source attribute: innehåller",
      "definition" : "Source attribute: innehåller",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Kontaktinformation"
      }]
    },
    {
      "id" : "Laboratoriesvar-Dokument.harMedicinsktAnsvarig",
      "path" : "Laboratoriesvar-Dokument.harMedicinsktAnsvarig",
      "short" : "Source attribute: har medicinskt ansvarig",
      "definition" : "Source attribute: har medicinskt ansvarig",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Halso--och-sjukvardspersonal-Halso--och-sjukvardsperson"
      }]
    },
    {
      "id" : "Laboratoriesvar-Dokument.besvarar",
      "path" : "Laboratoriesvar-Dokument.besvarar",
      "short" : "Source attribute: besvarar",
      "definition" : "Source attribute: besvarar",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Remiss-Dokument"
      }]
    }]
  }
}

```
