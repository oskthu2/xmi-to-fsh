# Person : Person - Logical Models from Visual Paradigm XMI v0.1.0

## Logical Model: Person : Person 

 
Supporting logical model generated from gloo4.xmi (source class: Person : Person). 

**Usages:**

* Use this Logical Model: [Patient : Patient](StructureDefinition-Patient-Patient.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/xmi.to.fsh|current/StructureDefinition/StructureDefinition-Person-Person.json)

### Formal Views of Profile Content

 [Description Differentials, Snapshots, and other representations](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](../StructureDefinition-Person-Person.csv), [Excel](../StructureDefinition-Person-Person.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "Person-Person",
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-type-characteristics",
    "valueCode" : "can-be-target"
  }],
  "url" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Person-Person",
  "version" : "0.1.0",
  "name" : "PersonPerson",
  "title" : "Person : Person",
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
  "description" : "Supporting logical model generated from gloo4.xmi (source class: Person : Person).",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Person-Person",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "Person-Person",
      "path" : "Person-Person",
      "short" : "Person : Person",
      "definition" : "Supporting logical model generated from gloo4.xmi (source class: Person : Person)."
    },
    {
      "id" : "Person-Person.-id",
      "path" : "Person-Person._id",
      "short" : "Source attribute: id; renamed from reserved FSH name 'id'",
      "definition" : "Source attribute: id; renamed from reserved FSH name 'id'",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/II"
      }]
    },
    {
      "id" : "Person-Person.namn",
      "path" : "Person-Person.namn",
      "short" : "Source attribute: namn",
      "definition" : "Source attribute: namn",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/ST"
      }]
    },
    {
      "id" : "Person-Person.fodelsetidpunkt",
      "path" : "Person-Person.fodelsetidpunkt",
      "short" : "Source attribute: födelsetidpunkt",
      "definition" : "Source attribute: födelsetidpunkt",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/TS"
      }]
    },
    {
      "id" : "Person-Person.kon",
      "path" : "Person-Person.kon",
      "short" : "Source attribute: kön",
      "definition" : "Source attribute: kön",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/CV"
      }]
    },
    {
      "id" : "Person-Person.antarRollen",
      "path" : "Person-Person.antarRollen",
      "short" : "Source attribute: antar rollen",
      "definition" : "Source attribute: antar rollen",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Patient-Patient"
      }]
    }]
  }
}

```
