---
title: "ControlSchema (D02-COG-009)"
type: entity
project: namencora
division: "Division 02: Cognitive & Ontological Systems"
subsystem: "Machine Ontologies & Taxonomic Hierarchies"
category: "Formal Schemas & Validation"
namespace: ControlSchema
term_code: D02-COG-009
status: candidate
canonical_uri: "urn:namencora:d02:controlschema"
tags:
  - entity
  - namespace
  - cognitive-systems
  - cohort-b
schema_org:
  "@type": DefinedTerm
  name: ControlSchema
  termCode: D02-COG-009
---

> **System Anchor**: `controlschema.com`  
> **Classification ID**: `D02-COG-009`  
> **Subsystem**: Machine Ontologies & Taxonomic Hierarchies / Formal Schemas & Validation
---

## 1. Technical Definition (Human Layer)

Ontological and cognitive semantic primitive for the Machine Ontologies & Taxonomic Hierarchies subsystem (category: Formal Schemas & Validation). Enforces deterministic knowledge normalization, graph relational structures, and conceptual topologies.

---

## 2. Machine Contract (Schema.org / JSON-LD)

```json
{
  "@context": "https://schema.org",
  "@type": "DefinedTerm",
  "name": "ControlSchema",
  "inDefinedTermSet": {
    "@type": "DefinedTermSet",
    "name": "Division 02: Cognitive & Ontological Systems"
  },
  "termCode": "D02-COG-009",
  "description": "Formal architectural primitive for formal schemas & validation.",
  "additionalProperty": [
    {
      "name": "subsystem",
      "value": "Machine Ontologies & Taxonomic Hierarchies"
    },
    {
      "name": "category",
      "value": "Formal Schemas & Validation"
    },
    {
      "name": "canonicalUri",
      "value": "urn:namencora:d02:controlschema"
    }
  ]
}
```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "DefinedTerm",
  "name": "ControlSchema",
  "inDefinedTermSet": {
    "@type": "DefinedTermSet",
    "name": "Division 02: Cognitive & Ontological Systems"
  },
  "termCode": "D02-COG-009",
  "description": "Formal architectural primitive for formal schemas & validation.",
  "additionalProperty": [
    {
      "name": "subsystem",
      "value": "Machine Ontologies & Taxonomic Hierarchies"
    },
    {
      "name": "category",
      "value": "Formal Schemas & Validation"
    },
    {
      "name": "canonicalUri",
      "value": "urn:namencora:d02:controlschema"
    }
  ]
}
</script>

---

## 3. Architectural Properties

| Invariant / Property | Specification |
| :--- | :--- |
| **Subsystem Tier** | `Machine Ontologies & Taxonomic Hierarchies` |
| **Category Target** | `Formal Schemas & Validation` |
| **Canonical URI** | `urn:namencora:d02:controlschema` |
| Specification Status | Candidate Specification (Active Review) |
| **Ontology Model** | `Directed Acyclic Graph (DAG) / Lattice Hierarchy` |

---
*Part of the Namencora Systems & Nomenclature Registry (Cohort B).*
