# Presentationsformat - Logical Models from Visual Paradigm XMI v0.1.0

## Logical Model: Presentationsformat 

 
Typ av filformat för svaret. [Så står det nu i informationsmodellen, klassen Svar, attributet "presentationsformat". Detta behöver knappast finnas med i begreppsmodellen.] 
Dokument som innehåller den visuella presentationen av laboratoriesvaret. 
Men jfr projektet e-remiss, där finns bilaga:
 Dokument som kompletterar ett annat dokument och är avsett att användas tillsammans med detta. 
Exempelvis utdrag ur patientjournal, en bild eller liknande som biläggs remissen, eller remissvaret. 
Är presentation något annat än bilaga? 

**Usages:**

* Use this Logical Model: [Remissvar : Dokument (inom hälso- och sjukvård)](StructureDefinition-Remissvar-Dokument-inom-halso--och-sjukvard.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/xmi.to.fsh|current/StructureDefinition/StructureDefinition-Presentationsformat.json)

### Formal Views of Profile Content

 [Description Differentials, Snapshots, and other representations](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](../StructureDefinition-Presentationsformat.csv), [Excel](../StructureDefinition-Presentationsformat.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "Presentationsformat",
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-type-characteristics",
    "valueCode" : "can-be-target"
  }],
  "url" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Presentationsformat",
  "version" : "0.1.0",
  "name" : "Presentationsformat",
  "title" : "Presentationsformat",
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
  "description" : "Typ av filformat för svaret. \n[Så står det nu i informationsmodellen, klassen Svar, attributet \"presentationsformat\". Detta behöver knappast finnas med i begreppsmodellen.]\n\n\n\nDokument som innehåller den visuella presentationen av laboratoriesvaret.  \n   \nMen jfr projektet e-remiss, där finns bilaga:  \nDokument som kompletterar ett annat dokument och är avsett att användas tillsammans med detta.   \n   \nExempelvis utdrag ur patientjournal, en bild eller liknande som biläggs remissen, eller remissvaret.  \n   \nÄr presentation något annat än bilaga?",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Presentationsformat",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "Presentationsformat",
      "path" : "Presentationsformat",
      "short" : "Presentationsformat",
      "definition" : "Typ av filformat för svaret. \n[Så står det nu i informationsmodellen, klassen Svar, attributet \"presentationsformat\". Detta behöver knappast finnas med i begreppsmodellen.]\n\n\n\nDokument som innehåller den visuella presentationen av laboratoriesvaret.  \n   \nMen jfr projektet e-remiss, där finns bilaga:  \nDokument som kompletterar ett annat dokument och är avsett att användas tillsammans med detta.   \n   \nExempelvis utdrag ur patientjournal, en bild eller liknande som biläggs remissen, eller remissvaret.  \n   \nÄr presentation något annat än bilaga?"
    },
    {
      "id" : "Presentationsformat.harVisst",
      "path" : "Presentationsformat.harVisst",
      "short" : "Source attribute: har visst",
      "definition" : "Source attribute: har visst",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Remissvar-Dokument-inom-halso--och-sjukvard"
      }]
    }]
  }
}

```
