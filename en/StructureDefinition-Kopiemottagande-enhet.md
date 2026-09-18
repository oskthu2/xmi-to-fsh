# Kopiemottagande enhet - Logical Models from Visual Paradigm XMI v0.1.0

## Logical Model: Kopiemottagande enhet 

 
Den organisatoriska enhet som tar emot en kopia av laboratoriesvaret. 
Eller ”… av remissvaret”, om detta ska vara generellt. I projektet e-remiss finns ingen kopiemottagare, är det något speciellt för laboratorieremisser? 
2018-03-14: Vi stryker denna ur begreppsmodellen, svarskopia är inget unikt för labbremisser. 
2018-03-09: Jonas Svanberg:
 Kopiemottagande enhet
 Nej, svarskopia är inget unikt för labbremisser. Det är en kvarleva från papperstiden, då det var lätt att ta en kopia (på vad som helst) och skicka till någon annan.
 Det förekommer säkert hos vissa landsting, men vanligast är nog att det bara finns ett svar. 

**Usages:**

* Use this Logical Model: [Organisatorisk enhet : Organisation (inom hälso- och sjukvård)](StructureDefinition-Organisatorisk-enhet-Organisation-inom-halso--och-sjukv.md) and [Remissvar : Dokument (inom hälso- och sjukvård)](StructureDefinition-Remissvar-Dokument-inom-halso--och-sjukvard.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/xmi.to.fsh|current/StructureDefinition/StructureDefinition-Kopiemottagande-enhet.json)

### Formal Views of Profile Content

 [Description Differentials, Snapshots, and other representations](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](../StructureDefinition-Kopiemottagande-enhet.csv), [Excel](../StructureDefinition-Kopiemottagande-enhet.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "Kopiemottagande-enhet",
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-type-characteristics",
    "valueCode" : "can-be-target"
  }],
  "url" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Kopiemottagande-enhet",
  "version" : "0.1.0",
  "name" : "Kopiemottagandeenhet",
  "title" : "Kopiemottagande enhet",
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
  "description" : "Den organisatoriska enhet som tar emot en kopia av laboratoriesvaret.  \n   \nEller ”… av remissvaret”, om detta ska vara generellt. I projektet e-remiss finns ingen kopiemottagare, är det något speciellt för laboratorieremisser? \n\n2018-03-14: Vi stryker denna ur begreppsmodellen, svarskopia är inget unikt för labbremisser.\n\n2018-03-09: Jonas Svanberg:  \nKopiemottagande enhet  \nNej, svarskopia är inget unikt för labbremisser. Det är en kvarleva från papperstiden, då det var lätt att ta en kopia (på vad som helst) och skicka till någon annan.  \nDet förekommer säkert hos vissa landsting, men vanligast är nog att det bara finns ett svar.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Kopiemottagande-enhet",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "Kopiemottagande-enhet",
      "path" : "Kopiemottagande-enhet",
      "short" : "Kopiemottagande enhet",
      "definition" : "Den organisatoriska enhet som tar emot en kopia av laboratoriesvaret.  \n   \nEller ”… av remissvaret”, om detta ska vara generellt. I projektet e-remiss finns ingen kopiemottagare, är det något speciellt för laboratorieremisser? \n\n2018-03-14: Vi stryker denna ur begreppsmodellen, svarskopia är inget unikt för labbremisser.\n\n2018-03-09: Jonas Svanberg:  \nKopiemottagande enhet  \nNej, svarskopia är inget unikt för labbremisser. Det är en kvarleva från papperstiden, då det var lätt att ta en kopia (på vad som helst) och skicka till någon annan.  \nDet förekommer säkert hos vissa landsting, men vanligast är nog att det bara finns ett svar."
    },
    {
      "id" : "Kopiemottagande-enhet.tarEmotKopiaAv",
      "path" : "Kopiemottagande-enhet.tarEmotKopiaAv",
      "short" : "Source attribute: tar emot kopia av",
      "definition" : "Source attribute: tar emot kopia av",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Remissvar-Dokument-inom-halso--och-sjukvard"
      }]
    },
    {
      "id" : "Kopiemottagande-enhet.arEn",
      "path" : "Kopiemottagande-enhet.arEn",
      "short" : "Source attribute: är en",
      "definition" : "Source attribute: är en",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/xmi-to-fsh/StructureDefinition/Organisatorisk-enhet-Organisation-inom-halso--och-sjukv"
      }]
    }]
  }
}

```
