# Analysgrupp (svarsgrupp) - gloo4 v0.1.0

## Logical Model: Analysgrupp (svarsgrupp) 

 
Sökning på google visar att ”analysgrupp” verkar avse en grupp av personer som ska analysera något. Och ”svarsgrupp” tycks ha med telefoni att göra. Detta kanske är något informatiskt som inte behöver förklaras i en begreppsmodell? 
Eller "Grupp av analyser utförda på ett och samma prov"? Stämmer det att det är ett och samma prov? I informationsmodellen står det att analysgrupp kan avse 0 till många prov, men i beskrivningen till klassen Analysgrupp står att denna grupperar ett antal analyser som utförs på ett prov. 
2018-03-14: Vi stryker denna i begreppsmodellen, det löser man i informationsmodellen (gruppkommentar e.d.). 
Analysgrupp
 Det kan vara ett eller flera prov. Exempel: påvisande av antikroppar mot Borrelia i både blod och cerebrospinalvätska.
 Observera att olika landsting kan ha löst detta på olika sätt. Man kan av tekniska skäl tvingas ha en analysgrupp som en enda ”vanlig” analys. Och det kan vara tvärtom: labbet hanterar analyserna som en grupp, men av tekniska skäl måste de ingående analyserna svaras ut en och en. 

**Usages:**

* Use this Logical Model: [Prov : Resurs (inom hälso- och sjukvård)](StructureDefinition-Prov-Resurs-inom-halso--och-sjukvard.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/gloo4|current/StructureDefinition/StructureDefinition-Analysgrupp-svarsgrupp.json)

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
  "url" : "http://example.org/fhir/gloo4/StructureDefinition/Analysgrupp-svarsgrupp",
  "version" : "0.1.0",
  "name" : "Analysgruppsvarsgrupp",
  "title" : "Analysgrupp (svarsgrupp)",
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
  "description" : "Sökning på google visar att ”analysgrupp” verkar avse en grupp av personer som ska analysera något. Och ”svarsgrupp” tycks ha med telefoni att göra. Detta kanske är något informatiskt som inte behöver förklaras i en begreppsmodell? \n\nEller \"Grupp av analyser utförda på ett och samma prov\"? Stämmer det att det är ett och samma prov? I informationsmodellen står det att analysgrupp kan avse 0 till många prov, men i beskrivningen till klassen Analysgrupp står att denna grupperar ett antal analyser som utförs på ett prov. \n\n2018-03-14: Vi stryker denna i begreppsmodellen, det löser man i informationsmodellen (gruppkommentar e.d.). \n\nAnalysgrupp  \nDet kan vara ett eller flera prov. Exempel: påvisande av antikroppar mot Borrelia i både blod och cerebrospinalvätska.  \nObservera att olika landsting kan ha löst detta på olika sätt. Man kan av tekniska skäl tvingas ha en analysgrupp som en enda ”vanlig” analys. Och det kan vara tvärtom: labbet hanterar analyserna som en grupp, men av tekniska skäl måste de ingående analyserna svaras ut en och en.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://example.org/fhir/gloo4/StructureDefinition/Analysgrupp-svarsgrupp",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "Analysgrupp-svarsgrupp",
      "path" : "Analysgrupp-svarsgrupp",
      "short" : "Analysgrupp (svarsgrupp)",
      "definition" : "Sökning på google visar att ”analysgrupp” verkar avse en grupp av personer som ska analysera något. Och ”svarsgrupp” tycks ha med telefoni att göra. Detta kanske är något informatiskt som inte behöver förklaras i en begreppsmodell? \n\nEller \"Grupp av analyser utförda på ett och samma prov\"? Stämmer det att det är ett och samma prov? I informationsmodellen står det att analysgrupp kan avse 0 till många prov, men i beskrivningen till klassen Analysgrupp står att denna grupperar ett antal analyser som utförs på ett prov. \n\n2018-03-14: Vi stryker denna i begreppsmodellen, det löser man i informationsmodellen (gruppkommentar e.d.). \n\nAnalysgrupp  \nDet kan vara ett eller flera prov. Exempel: påvisande av antikroppar mot Borrelia i både blod och cerebrospinalvätska.  \nObservera att olika landsting kan ha löst detta på olika sätt. Man kan av tekniska skäl tvingas ha en analysgrupp som en enda ”vanlig” analys. Och det kan vara tvärtom: labbet hanterar analyserna som en grupp, men av tekniska skäl måste de ingående analyserna svaras ut en och en."
    },
    {
      "id" : "Analysgrupp-svarsgrupp.grupperarAnalyserSomUtfortsPaSamma",
      "path" : "Analysgrupp-svarsgrupp.grupperarAnalyserSomUtfortsPaSamma",
      "short" : "Source attribute: grupperar analyser som utförts på samma",
      "definition" : "Source attribute: grupperar analyser som utförts på samma",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://example.org/fhir/gloo4/StructureDefinition/Prov-Resurs-inom-halso--och-sjukvard"
      }]
    }]
  }
}

```
