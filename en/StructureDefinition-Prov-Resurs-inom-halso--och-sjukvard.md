# Prov : Resurs (inom hälso- och sjukvård) - Logical Models from Visual Paradigm XMI v0.1.0

## Logical Model: Prov : Resurs (inom hälso- och sjukvård) 

 
Supporting logical model generated from gloo4.xmi (source class: Prov : Resurs (inom hälso- och sjukvård)). 

**Usages:**

* Use this Logical Model: [Analysgrupp (svarsgrupp)](StructureDefinition-Analysgrupp-svarsgrupp.md), [Laboratorieanalys : Aktivitet (inom hälso- och sjukvård)](StructureDefinition-Laboratorieanalys-Aktivitet-inom-halso--och-sjukvard.md), [Prov-id](StructureDefinition-Prov-id.md), [Provgivare](StructureDefinition-Provgivare.md)... Show 2 more, [Provmaterial](StructureDefinition-Provmaterial.md) and [Provtagningsmetod](StructureDefinition-Provtagningsmetod.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/xmi.to.fsh|current/StructureDefinition/StructureDefinition-Prov-Resurs-inom-halso--och-sjukvard.json)

### Formal Views of Profile Content

 [Description Differentials, Snapshots, and other representations](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](../StructureDefinition-Prov-Resurs-inom-halso--och-sjukvard.csv), [Excel](../StructureDefinition-Prov-Resurs-inom-halso--och-sjukvard.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "Prov-Resurs-inom-halso--och-sjukvard",
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-type-characteristics",
    "valueCode" : "can-be-target"
  }],
  "url" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Prov-Resurs-inom-halso--och-sjukvard",
  "version" : "0.1.0",
  "name" : "ProvResursinomhalsoochsjukvard",
  "title" : "Prov : Resurs (inom hälso- och sjukvård)",
  "status" : "draft",
  "date" : "2026-09-18T08:41:45+00:00",
  "publisher" : "xmi-to-fsh",
  "contact" : [{
    "name" : "xmi-to-fsh",
    "telecom" : [{
      "system" : "url",
      "value" : "https://github.com/oskthu2/xmi-to-fsh"
    }]
  }],
  "description" : "Supporting logical model generated from gloo4.xmi (source class: Prov : Resurs (inom hälso- och sjukvård)).",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Prov-Resurs-inom-halso--och-sjukvard",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "Prov-Resurs-inom-halso--och-sjukvard",
      "path" : "Prov-Resurs-inom-halso--och-sjukvard",
      "short" : "Prov : Resurs (inom hälso- och sjukvård)",
      "definition" : "Supporting logical model generated from gloo4.xmi (source class: Prov : Resurs (inom hälso- och sjukvård))."
    },
    {
      "id" : "Prov-Resurs-inom-halso--och-sjukvard.grupperarAnalyserSomUtfortsPaSamma",
      "path" : "Prov-Resurs-inom-halso--och-sjukvard.grupperarAnalyserSomUtfortsPaSamma",
      "short" : "Source attribute: grupperar analyser som utförts på samma",
      "definition" : "Source attribute: grupperar analyser som utförts på samma",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Analysgrupp-svarsgrupp"
      }]
    },
    {
      "id" : "Prov-Resurs-inom-halso--och-sjukvard.Identifierar",
      "path" : "Prov-Resurs-inom-halso--och-sjukvard.Identifierar",
      "short" : "Source attribute: Identifierar",
      "definition" : "Source attribute: Identifierar",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Prov-id"
      }]
    },
    {
      "id" : "Prov-Resurs-inom-halso--och-sjukvard.bestarAvVisst",
      "path" : "Prov-Resurs-inom-halso--och-sjukvard.bestarAvVisst",
      "short" : "Source attribute: består av visst",
      "definition" : "Source attribute: består av visst",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Provmaterial"
      }]
    },
    {
      "id" : "Prov-Resurs-inom-halso--och-sjukvard.utforsPa",
      "path" : "Prov-Resurs-inom-halso--och-sjukvard.utforsPa",
      "short" : "Source attribute: utförs på",
      "definition" : "Source attribute: utförs på",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Laboratorieanalys-Aktivitet-inom-halso--och-sjukvard"
      }]
    },
    {
      "id" : "Prov-Resurs-inom-halso--och-sjukvard.tasMedViss",
      "path" : "Prov-Resurs-inom-halso--och-sjukvard.tasMedViss",
      "short" : "Source attribute: tas med viss",
      "definition" : "Source attribute: tas med viss",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Provtagningsmetod"
      }]
    },
    {
      "id" : "Prov-Resurs-inom-halso--och-sjukvard.lamnar",
      "path" : "Prov-Resurs-inom-halso--och-sjukvard.lamnar",
      "short" : "Source attribute: lämnar",
      "definition" : "Source attribute: lämnar",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Provgivare"
      }]
    }]
  }
}

```
