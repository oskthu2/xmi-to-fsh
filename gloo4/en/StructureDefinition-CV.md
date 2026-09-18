# CV - gloo4 v0.1.0

## Logical Model: CV 

 
Kodade värden 

**Usages:**

* Use this Logical Model: [Analysgrupp](StructureDefinition-Analysgrupp.md), [Laboratorieanalys : Aktivitet](StructureDefinition-Laboratorieanalys-Aktivitet.md), [Laboratorieanalysresultat : Observation](StructureDefinition-Laboratorieanalysresultat-Observation.md), [Laboratoriesvar : Dokument](StructureDefinition-Laboratoriesvar-Dokument.md)... Show 3 more, [Organisatorisk enhet : Organisatorisk enhet](StructureDefinition-Organisatorisk-enhet-Organisatorisk-enhet.md), [Person : Person](StructureDefinition-Person-Person.md) and [Provbehållare : Resurs](StructureDefinition-Provbehallare-Resurs.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/gloo4|current/StructureDefinition/StructureDefinition-CV.json)

### Formal Views of Profile Content

 [Description Differentials, Snapshots, and other representations](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](../StructureDefinition-CV.csv), [Excel](../StructureDefinition-CV.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "CV",
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-type-characteristics",
    "valueCode" : "can-be-target"
  }],
  "url" : "http://example.org/fhir/gloo4/StructureDefinition/CV",
  "version" : "0.1.0",
  "name" : "CV",
  "title" : "CV",
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
  "description" : "Kodade värden",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://example.org/fhir/gloo4/StructureDefinition/CV",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "CV",
      "path" : "CV",
      "short" : "CV",
      "definition" : "Kodade värden"
    }]
  }
}

```
