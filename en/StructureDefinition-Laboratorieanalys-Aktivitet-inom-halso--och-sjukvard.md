# Laboratorieanalys : Aktivitet (inom hälso- och sjukvård) - Logical Models from Visual Paradigm XMI v0.1.0

## Logical Model: Laboratorieanalys : Aktivitet (inom hälso- och sjukvård) 

 
Bestämning av egenskaper hos prov, t.ex. artbestämning, fysikaliska och kemiska egenskaper. 

**Usages:**

* Use this Logical Model: [Analysgrupp](StructureDefinition-Analysgrupp-2.md), [Fördjupad analys](StructureDefinition-Fordjupad-analys.md), [Laboratorieanalysresultat : Observerat hälsotillstånd](StructureDefinition-Laboratorieanalysresultat-Observerat-halsotillstand.md), [Laboratoriedisciplin](StructureDefinition-Laboratoriedisciplin.md)... Show 3 more, [Prov : Resurs (inom hälso- och sjukvård)](StructureDefinition-Prov-Resurs-inom-halso--och-sjukvard.md), [Remiss : Dokument (inom hälso- och sjukvård)](StructureDefinition-Remiss-Dokument-inom-halso--och-sjukvard.md) and [Utförande enhet : Organisation (inom hälso- och sjukvård)](StructureDefinition-Utforande-enhet-Organisation-inom-halso--och-sjukvard.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/xmi.to.fsh|current/StructureDefinition/StructureDefinition-Laboratorieanalys-Aktivitet-inom-halso--och-sjukvard.json)

### Formal Views of Profile Content

 [Description Differentials, Snapshots, and other representations](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](../StructureDefinition-Laboratorieanalys-Aktivitet-inom-halso--och-sjukvard.csv), [Excel](../StructureDefinition-Laboratorieanalys-Aktivitet-inom-halso--och-sjukvard.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "Laboratorieanalys-Aktivitet-inom-halso--och-sjukvard",
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-type-characteristics",
    "valueCode" : "can-be-target"
  }],
  "url" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Laboratorieanalys-Aktivitet-inom-halso--och-sjukvard",
  "version" : "0.1.0",
  "name" : "LaboratorieanalysAktivitetinomhalsoochsjukvard",
  "title" : "Laboratorieanalys : Aktivitet (inom hälso- och sjukvård)",
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
  "description" : "Bestämning av egenskaper hos prov, t.ex. artbestämning, fysikaliska och kemiska egenskaper.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Laboratorieanalys-Aktivitet-inom-halso--och-sjukvard",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "Laboratorieanalys-Aktivitet-inom-halso--och-sjukvard",
      "path" : "Laboratorieanalys-Aktivitet-inom-halso--och-sjukvard",
      "short" : "Laboratorieanalys : Aktivitet (inom hälso- och sjukvård)",
      "definition" : "Bestämning av egenskaper hos prov, t.ex. artbestämning, fysikaliska och kemiska egenskaper."
    },
    {
      "id" : "Laboratorieanalys-Aktivitet-inom-halso--och-sjukvard.arEn",
      "path" : "Laboratorieanalys-Aktivitet-inom-halso--och-sjukvard.arEn",
      "short" : "Source attribute: är en",
      "definition" : "Source attribute: är en",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Fordjupad-analys"
      }]
    },
    {
      "id" : "Laboratorieanalys-Aktivitet-inom-halso--och-sjukvard.arResultatAv",
      "path" : "Laboratorieanalys-Aktivitet-inom-halso--och-sjukvard.arResultatAv",
      "short" : "Source attribute: är resultat av",
      "definition" : "Source attribute: är resultat av",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Laboratorieanalysresultat-Observerat-halsotillstand"
      }]
    },
    {
      "id" : "Laboratorieanalys-Aktivitet-inom-halso--och-sjukvard.utforsPa",
      "path" : "Laboratorieanalys-Aktivitet-inom-halso--och-sjukvard.utforsPa",
      "short" : "Source attribute: utförs på",
      "definition" : "Source attribute: utförs på",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Prov-Resurs-inom-halso--och-sjukvard"
      }]
    },
    {
      "id" : "Laboratorieanalys-Aktivitet-inom-halso--och-sjukvard.utforsInomEn",
      "path" : "Laboratorieanalys-Aktivitet-inom-halso--och-sjukvard.utforsInomEn",
      "short" : "Source attribute: utförs inom en",
      "definition" : "Source attribute: utförs inom en",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Laboratoriedisciplin"
      }]
    },
    {
      "id" : "Laboratorieanalys-Aktivitet-inom-halso--och-sjukvard.utfor",
      "path" : "Laboratorieanalys-Aktivitet-inom-halso--och-sjukvard.utfor",
      "short" : "Source attribute: utför",
      "definition" : "Source attribute: utför",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Utforande-enhet-Organisation-inom-halso--och-sjukvard"
      }]
    },
    {
      "id" : "Laboratorieanalys-Aktivitet-inom-halso--och-sjukvard.avserBegaranOmUtforandeAvEnEllerFlera",
      "path" : "Laboratorieanalys-Aktivitet-inom-halso--och-sjukvard.avserBegaranOmUtforandeAvEnEllerFlera",
      "short" : "Source attribute: avser begäran om utförande av en eller flera",
      "definition" : "Source attribute: avser begäran om utförande av en eller flera",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Remiss-Dokument-inom-halso--och-sjukvard"
      }]
    },
    {
      "id" : "Laboratorieanalys-Aktivitet-inom-halso--och-sjukvard.grupperar",
      "path" : "Laboratorieanalys-Aktivitet-inom-halso--och-sjukvard.grupperar",
      "short" : "Source attribute: grupperar",
      "definition" : "Source attribute: grupperar",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Analysgrupp-2"
      }]
    }]
  }
}

```
