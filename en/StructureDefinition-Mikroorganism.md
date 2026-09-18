# Mikroorganism - Logical Models from Visual Paradigm XMI v0.1.0

## Logical Model: Mikroorganism 

 
Levande, nästan alltid encellig varelse som är så liten att den inte kan ses med blotta ögat. 
Det finns fyra huvudgrupper: bakterier, svampar, virus och parasiter. 

**Usages:**

* Use this Logical Model: [Laboratorieanalysresultat : Observerat hälsotillstånd](StructureDefinition-Laboratorieanalysresultat-Observerat-halsotillstand.md) and [Resistensbestämning : Aktivitet (inom hälso- och sjukvård)](StructureDefinition-Resistensbestamning-Aktivitet-inom-halso--och-sjukvard.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/xmi.to.fsh|current/StructureDefinition/StructureDefinition-Mikroorganism.json)

### Formal Views of Profile Content

 [Description Differentials, Snapshots, and other representations](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](../StructureDefinition-Mikroorganism.csv), [Excel](../StructureDefinition-Mikroorganism.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "Mikroorganism",
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-type-characteristics",
    "valueCode" : "can-be-target"
  }],
  "url" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Mikroorganism",
  "version" : "0.1.0",
  "name" : "Mikroorganism",
  "title" : "Mikroorganism",
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
  "description" : "Levande, nästan alltid encellig varelse som är så liten att den inte kan ses med blotta ögat.\n\nDet finns fyra huvudgrupper: bakterier, svampar, virus och parasiter.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Mikroorganism",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "Mikroorganism",
      "path" : "Mikroorganism",
      "short" : "Mikroorganism",
      "definition" : "Levande, nästan alltid encellig varelse som är så liten att den inte kan ses med blotta ögat.\n\nDet finns fyra huvudgrupper: bakterier, svampar, virus och parasiter."
    },
    {
      "id" : "Mikroorganism.kanUtforasPa",
      "path" : "Mikroorganism.kanUtforasPa",
      "short" : "Source attribute: kan utföras på",
      "definition" : "Source attribute: kan utföras på",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Resistensbestamning-Aktivitet-inom-halso--och-sjukvard"
      }]
    },
    {
      "id" : "Mikroorganism.kanVaraFyndAv",
      "path" : "Mikroorganism.kanVaraFyndAv",
      "short" : "Source attribute: kan vara fynd av",
      "definition" : "Source attribute: kan vara fynd av",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Laboratorieanalysresultat-Observerat-halsotillstand"
      }]
    }]
  }
}

```
