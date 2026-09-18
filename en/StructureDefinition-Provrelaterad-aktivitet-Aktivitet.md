# Provrelaterad aktivitet: Aktivitet - Logical Models from Visual Paradigm XMI v0.1.0

## Logical Model: Provrelaterad aktivitet: Aktivitet 

 
Supporting logical model generated from gloo4.xmi (source class: Provrelaterad aktivitet: Aktivitet). 

**Usages:**

* Use this Logical Model: [Prov : Resurs](StructureDefinition-Prov-Resurs.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/xmi.to.fsh|current/StructureDefinition/StructureDefinition-Provrelaterad-aktivitet-Aktivitet.json)

### Formal Views of Profile Content

 [Description Differentials, Snapshots, and other representations](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](../StructureDefinition-Provrelaterad-aktivitet-Aktivitet.csv), [Excel](../StructureDefinition-Provrelaterad-aktivitet-Aktivitet.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "Provrelaterad-aktivitet-Aktivitet",
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-type-characteristics",
    "valueCode" : "can-be-target"
  }],
  "url" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Provrelaterad-aktivitet-Aktivitet",
  "version" : "0.1.0",
  "name" : "ProvrelateradaktivitetAktivitet",
  "title" : "Provrelaterad aktivitet: Aktivitet",
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
  "description" : "Supporting logical model generated from gloo4.xmi (source class: Provrelaterad aktivitet: Aktivitet).",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Provrelaterad-aktivitet-Aktivitet",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "Provrelaterad-aktivitet-Aktivitet",
      "path" : "Provrelaterad-aktivitet-Aktivitet",
      "short" : "Provrelaterad aktivitet: Aktivitet",
      "definition" : "Supporting logical model generated from gloo4.xmi (source class: Provrelaterad aktivitet: Aktivitet)."
    },
    {
      "id" : "Provrelaterad-aktivitet-Aktivitet.kod",
      "path" : "Provrelaterad-aktivitet-Aktivitet.kod",
      "short" : "Source attribute: kod",
      "definition" : "Source attribute: kod",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/CV-CWE"
      }]
    },
    {
      "id" : "Provrelaterad-aktivitet-Aktivitet.tid",
      "path" : "Provrelaterad-aktivitet-Aktivitet.tid",
      "short" : "Source attribute: tid",
      "definition" : "Source attribute: tid",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "Provrelaterad-aktivitet-Aktivitet.metod",
      "path" : "Provrelaterad-aktivitet-Aktivitet.metod",
      "short" : "Source attribute: metod",
      "definition" : "Source attribute: metod",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/CV-CWE"
      }]
    },
    {
      "id" : "Provrelaterad-aktivitet-Aktivitet.avser",
      "path" : "Provrelaterad-aktivitet-Aktivitet.avser",
      "short" : "Source attribute: avser",
      "definition" : "Source attribute: avser",
      "min" : 1,
      "max" : "*",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Prov-Resurs"
      }]
    }]
  }
}

```
