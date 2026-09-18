# Laboratoriedisciplin - gloo4 v0.1.0

## Logical Model: Laboratoriedisciplin 

 
Disciplin som en laboratorieverksamhet kan utföra laboratorieundersökningar inom. 
Fråga till referensgruppen: ser indelningen olika ut? Funkar det i praktiken? 
 Klinisk kemi; Mikrobiologi … 
2018-03-09: Jonas Svanberg:
 Laboratoriedisciplin
 Ursprungligen är det en indelning av medicinsk kunskap, t.ex. klinisk kemi och klinisk immunologi. Traditionellt var det också både organisatorisk indelning och utförande laboratorium. Så behöver det inte vara nu, men i beställarnas (och labbens) tankevärld finns denna indelning kvar.
 Här behövs det (om det finns i svaret) som en tagg att sortera eller filtrera på. 
2018-03-20: 20/3: Kan strykas i begreppsmodellen, i infomodellen nytt attribut i klassen Organisatorisk enhet. 
Laboratoriemedicinska specialiteter 
 Klinisk immunologi och 
 transfusionsmedicin 
 Klinisk kemi 
 Klinisk mikrobiologi 
 Klinisk patologi 
 http://www.socialstyrelsen.se/sosfs/2015-8 
Referensgruppsmötet 2018-03-27: Slutsats 1: Vi använder HSA-koder så länge (i HSA finns klinisk genetik som verksamhetskod, men den är där inte klassificerad som laboratorieverksamhet, vilket den borde vara enligt gruppen). 
 Kategorisera det enskilda provet med hjälp av HSA-koderna. 
 Kategoriseringen varierar från land till land. 
 Listkoderna. De är nödvändiga för mikrobiologi idag. 
 Slutsats 2: En liten arbetsgrupp (kodverksgrupp) jobbar vidare med detta. 

**Usages:**

* Use this Logical Model: [Laboratorieanalys : Aktivitet (inom hälso- och sjukvård)](StructureDefinition-Laboratorieanalys-Aktivitet-inom-halso--och-sjukvard.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/gloo4|current/StructureDefinition/StructureDefinition-Laboratoriedisciplin.json)

### Formal Views of Profile Content

 [Description Differentials, Snapshots, and other representations](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](../StructureDefinition-Laboratoriedisciplin.csv), [Excel](../StructureDefinition-Laboratoriedisciplin.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "Laboratoriedisciplin",
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-type-characteristics",
    "valueCode" : "can-be-target"
  }],
  "url" : "http://example.org/fhir/gloo4/StructureDefinition/Laboratoriedisciplin",
  "version" : "0.1.0",
  "name" : "Laboratoriedisciplin",
  "title" : "Laboratoriedisciplin",
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
  "description" : "Disciplin som en laboratorieverksamhet kan utföra laboratorieundersökningar inom.\n\nFråga till referensgruppen: ser indelningen olika ut? Funkar det i praktiken?   \nKlinisk kemi; Mikrobiologi   ...\n\n2018-03-09: Jonas Svanberg:  \nLaboratoriedisciplin  \nUrsprungligen är det en indelning av medicinsk kunskap, t.ex. klinisk kemi och klinisk immunologi. Traditionellt var det också både organisatorisk indelning och utförande laboratorium. Så behöver det inte vara nu, men i beställarnas (och labbens) tankevärld finns denna indelning kvar.  \nHär behövs det (om det finns i svaret) som en tagg att sortera eller filtrera på. \n\n2018-03-20: 20/3: Kan strykas i begreppsmodellen, i infomodellen nytt attribut i klassen Organisatorisk enhet. \n\n\n Laboratoriemedicinska specialiteter   \n Klinisk immunologi och   \n transfusionsmedicin   \n Klinisk kemi   \n Klinisk mikrobiologi   \n Klinisk patologi   \n http://www.socialstyrelsen.se/sosfs/2015-8  \n\nReferensgruppsmötet 2018-03-27: \nSlutsats 1: Vi använder HSA-koder så länge (i HSA finns klinisk genetik som verksamhetskod, men den är där inte klassificerad som laboratorieverksamhet, vilket den borde vara enligt gruppen).    \nKategorisera det enskilda provet med hjälp av HSA-koderna.    \nKategoriseringen varierar från land till land.    \nListkoderna. De är nödvändiga för mikrobiologi idag.    \nSlutsats 2: En liten arbetsgrupp (kodverksgrupp) jobbar vidare med detta.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://example.org/fhir/gloo4/StructureDefinition/Laboratoriedisciplin",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "Laboratoriedisciplin",
      "path" : "Laboratoriedisciplin",
      "short" : "Laboratoriedisciplin",
      "definition" : "Disciplin som en laboratorieverksamhet kan utföra laboratorieundersökningar inom.\n\nFråga till referensgruppen: ser indelningen olika ut? Funkar det i praktiken?   \nKlinisk kemi; Mikrobiologi   ...\n\n2018-03-09: Jonas Svanberg:  \nLaboratoriedisciplin  \nUrsprungligen är det en indelning av medicinsk kunskap, t.ex. klinisk kemi och klinisk immunologi. Traditionellt var det också både organisatorisk indelning och utförande laboratorium. Så behöver det inte vara nu, men i beställarnas (och labbens) tankevärld finns denna indelning kvar.  \nHär behövs det (om det finns i svaret) som en tagg att sortera eller filtrera på. \n\n2018-03-20: 20/3: Kan strykas i begreppsmodellen, i infomodellen nytt attribut i klassen Organisatorisk enhet. \n\n\n Laboratoriemedicinska specialiteter   \n Klinisk immunologi och   \n transfusionsmedicin   \n Klinisk kemi   \n Klinisk mikrobiologi   \n Klinisk patologi   \n http://www.socialstyrelsen.se/sosfs/2015-8  \n\nReferensgruppsmötet 2018-03-27: \nSlutsats 1: Vi använder HSA-koder så länge (i HSA finns klinisk genetik som verksamhetskod, men den är där inte klassificerad som laboratorieverksamhet, vilket den borde vara enligt gruppen).    \nKategorisera det enskilda provet med hjälp av HSA-koderna.    \nKategoriseringen varierar från land till land.    \nListkoderna. De är nödvändiga för mikrobiologi idag.    \nSlutsats 2: En liten arbetsgrupp (kodverksgrupp) jobbar vidare med detta."
    },
    {
      "id" : "Laboratoriedisciplin.utforsInomEn",
      "path" : "Laboratoriedisciplin.utforsInomEn",
      "short" : "Source attribute: utförs inom en",
      "definition" : "Source attribute: utförs inom en",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/gloo4/StructureDefinition/Laboratorieanalys-Aktivitet-inom-halso--och-sjukvard"
      }]
    }]
  }
}

```
