# Patient : Patient - gloo4 v0.1.0

## Logical Model: Patient : Patient 

 
Klassen Patient håller information om en person som erhåller eller är registrerad för att erhålla hälso- och sjukvård. 

**Usages:**

* Use this Logical Model: [Laboratoriesvar : Dokument](StructureDefinition-Laboratoriesvar-Dokument.md) and [Person : Person](StructureDefinition-Person-Person.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/gloo4|current/StructureDefinition/StructureDefinition-Patient-Patient.json)

### Formal Views of Profile Content

 [Description Differentials, Snapshots, and other representations](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](../StructureDefinition-Patient-Patient.csv), [Excel](../StructureDefinition-Patient-Patient.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "Patient-Patient",
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-type-characteristics",
    "valueCode" : "can-be-target"
  }],
  "url" : "http://example.org/fhir/gloo4/StructureDefinition/Patient-Patient",
  "version" : "0.1.0",
  "name" : "PatientPatient",
  "title" : "Patient : Patient",
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
  "description" : "Klassen Patient håller information om en person som erhåller eller är registrerad för att erhålla hälso- och sjukvård.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://example.org/fhir/gloo4/StructureDefinition/Patient-Patient",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "Patient-Patient",
      "path" : "Patient-Patient",
      "short" : "Patient : Patient",
      "definition" : "Klassen Patient håller information om en person som erhåller eller är registrerad för att erhålla hälso- och sjukvård."
    },
    {
      "id" : "Patient-Patient.-id",
      "path" : "Patient-Patient._id",
      "short" : "Source attribute: id; renamed from reserved FSH name 'id'",
      "definition" : "Angivelse av identitetsbeteckning för patient.\n\nDetta kan vara av typen personnummer, samordningsnummer eller reservnummer.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/gloo4/StructureDefinition/II"
      }]
    },
    {
      "id" : "Patient-Patient.avser",
      "path" : "Patient-Patient.avser",
      "short" : "Source attribute: avser",
      "definition" : "Source attribute: avser",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "http://example.org/fhir/gloo4/StructureDefinition/Laboratoriesvar-Dokument"
      }]
    },
    {
      "id" : "Patient-Patient.antarRollen",
      "path" : "Patient-Patient.antarRollen",
      "short" : "Source attribute: antar rollen",
      "definition" : "Source attribute: antar rollen",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/gloo4/StructureDefinition/Person-Person"
      }]
    }]
  }
}

```
