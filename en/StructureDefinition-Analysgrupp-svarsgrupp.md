# Analysgrupp (svarsgrupp) - Logical Models from Visual Paradigm XMI v0.1.0

## Logical Model: Analysgrupp (svarsgrupp) 

 
Supporting logical model generated from gloo4.xmi (source class: Analysgrupp (svarsgrupp)). 

**Usages:**

* Use this Logical Model: [Prov : Resurs (inom hälso- och sjukvård)](StructureDefinition-Prov-Resurs-inom-halso--och-sjukvard.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/xmi.to.fsh|current/StructureDefinition/StructureDefinition-Analysgrupp-svarsgrupp.json)

### Formal Views of Profile Content

 [Description Differentials, Snapshots, and other representations](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](../StructureDefinition-Analysgrupp-svarsgrupp.csv), [Excel](../StructureDefinition-Analysgrupp-svarsgrupp.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "Analysgrupp-svarsgrupp",
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-type-characteristics",
    "valueCode" : "can-be-target"
  }],
  "url" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Analysgrupp-svarsgrupp",
  "version" : "0.1.0",
  "name" : "Analysgruppsvarsgrupp",
  "title" : "Analysgrupp (svarsgrupp)",
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
  "description" : "Supporting logical model generated from gloo4.xmi (source class: Analysgrupp (svarsgrupp)).",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Analysgrupp-svarsgrupp",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "Analysgrupp-svarsgrupp",
      "path" : "Analysgrupp-svarsgrupp",
      "short" : "Analysgrupp (svarsgrupp)",
      "definition" : "Supporting logical model generated from gloo4.xmi (source class: Analysgrupp (svarsgrupp))."
    },
    {
      "id" : "Analysgrupp-svarsgrupp.grupperarAnalyserSomUtfortsPaSamma",
      "path" : "Analysgrupp-svarsgrupp.grupperarAnalyserSomUtfortsPaSamma",
      "short" : "Source attribute: grupperar analyser som utförts på samma",
      "definition" : "Source attribute: grupperar analyser som utförts på samma",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Prov-Resurs-inom-halso--och-sjukvard"
      }]
    }]
  }
}

```
