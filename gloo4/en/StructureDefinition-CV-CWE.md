# CV CWE - gloo4 v0.1.0

## Logical Model: CV CWE 

 
Kodade värden som tillåter text som alternativ. 

**Usages:**

* Use this Logical Model: [Analysutrustning : Resurs](StructureDefinition-Analysutrustning-Resurs.md), [Hälso- och sjukvårdspersonal : Hälso- och sjukvårdspersonal](StructureDefinition-Halso--och-sjukvardspersonal-Halso--och-sjukvardsperson.md), [Laboratorieanalys : Aktivitet](StructureDefinition-Laboratorieanalys-Aktivitet.md), [Prov : Resurs](StructureDefinition-Prov-Resurs.md)... Show 2 more, [Provrelaterad aktivitet: Aktivitet](StructureDefinition-Provrelaterad-aktivitet-Aktivitet.md) and [Remiss : Dokument](StructureDefinition-Remiss-Dokument.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/gloo4|current/StructureDefinition/StructureDefinition-CV-CWE.json)

### Formal Views of Profile Content

 [Description Differentials, Snapshots, and other representations](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](../StructureDefinition-CV-CWE.csv), [Excel](../StructureDefinition-CV-CWE.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "CV-CWE",
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-type-characteristics",
    "valueCode" : "can-be-target"
  }],
  "url" : "http://example.org/fhir/gloo4/StructureDefinition/CV-CWE",
  "version" : "0.1.0",
  "name" : "CVCWE",
  "title" : "CV CWE",
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
  "description" : "Kodade värden som tillåter text som alternativ.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://example.org/fhir/gloo4/StructureDefinition/CV-CWE",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "CV-CWE",
      "path" : "CV-CWE",
      "short" : "CV CWE",
      "definition" : "Kodade värden som tillåter text som alternativ."
    }]
  }
}

```
