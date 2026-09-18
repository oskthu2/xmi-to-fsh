# Patient : Patient - Logical Models from Visual Paradigm XMI v0.1.0

## Logical Model: Patient : Patient 

 
Supporting logical model generated from gloo4.xmi (source class: Patient : Patient). 

**Usages:**

* Use this Logical Model: [Laboratoriesvar : Dokument](StructureDefinition-Laboratoriesvar-Dokument.md) and [Person : Person](StructureDefinition-Person-Person.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/xmi.to.fsh|current/StructureDefinition/StructureDefinition-Patient-Patient.json)

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
  "url" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Patient-Patient",
  "version" : "0.1.0",
  "name" : "PatientPatient",
  "title" : "Patient : Patient",
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
  "description" : "Supporting logical model generated from gloo4.xmi (source class: Patient : Patient).",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Patient-Patient",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "Patient-Patient",
      "path" : "Patient-Patient",
      "short" : "Patient : Patient",
      "definition" : "Supporting logical model generated from gloo4.xmi (source class: Patient : Patient)."
    },
    {
      "id" : "Patient-Patient.-id",
      "path" : "Patient-Patient._id",
      "short" : "Source attribute: id; renamed from reserved FSH name 'id'",
      "definition" : "Source attribute: id; renamed from reserved FSH name 'id'",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/II"
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
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Laboratoriesvar-Dokument"
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
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Person-Person"
      }]
    }]
  }
}

```
