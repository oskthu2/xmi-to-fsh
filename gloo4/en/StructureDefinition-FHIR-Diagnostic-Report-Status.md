# FHIR Diagnostic Report Status - gloo4 v0.1.0

## Logical Model: FHIR Diagnostic Report Status 

 
Value set från FHIR som specificerar typen av provsvar OID: 2.16.840.1.113883.4.642.3.235 http://hl7.org/fhir/ValueSet/diagnostic-report-status 

**Usages:**

* This Logical Model is not used by any profiles in this Specification

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/gloo4|current/StructureDefinition/StructureDefinition-FHIR-Diagnostic-Report-Status.json)

### Formal Views of Profile Content

 [Description Differentials, Snapshots, and other representations](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](../StructureDefinition-FHIR-Diagnostic-Report-Status.csv), [Excel](../StructureDefinition-FHIR-Diagnostic-Report-Status.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "FHIR-Diagnostic-Report-Status",
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-type-characteristics",
    "valueCode" : "can-be-target"
  }],
  "url" : "http://example.org/fhir/gloo4/StructureDefinition/FHIR-Diagnostic-Report-Status",
  "version" : "0.1.0",
  "name" : "FHIRDiagnosticReportStatus",
  "title" : "FHIR Diagnostic Report Status ",
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
  "description" : "Value set från FHIR som specificerar typen av provsvar\nOID: 2.16.840.1.113883.4.642.3.235\nhttp://hl7.org/fhir/ValueSet/diagnostic-report-status",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://example.org/fhir/gloo4/StructureDefinition/FHIR-Diagnostic-Report-Status",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "FHIR-Diagnostic-Report-Status",
      "path" : "FHIR-Diagnostic-Report-Status",
      "short" : "FHIR Diagnostic Report Status ",
      "definition" : "Value set från FHIR som specificerar typen av provsvar\nOID: 2.16.840.1.113883.4.642.3.235\nhttp://hl7.org/fhir/ValueSet/diagnostic-report-status"
    }]
  }
}

```
