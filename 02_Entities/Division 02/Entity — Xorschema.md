---
type: entity
project: namencora
division: "Division 02: Cognitive & Ontological Systems"
subsystem: "1. Machine Ontologies & Taxonomic Hierarchies"
category: "Formal Schemas & Validation:"
namespace: XorSchema
term_code: D02-COG-013
status: candidate
canonical_uri: "urn:namencora:d02:xorschema"
tags:
  - entity
  - namespace
  - cognitive-systems
  - cohort-b
schema_org:
  "@type": DefinedTerm
  name: XorSchema
  termCode: D02-COG-013
---

# XorSchema

> **System Anchor**: `xorschema.com`  
> **Classification ID**: `D02-COG-013`  
> **Subsystem**: 1. Machine Ontologies & Taxonomic Hierarchies / Formal Schemas & Validation:

---

## 1. Technical Definition (Human Layer)

Онтологічний та семантичний примітив підсистеми **1. Machine Ontologies & Taxonomic Hierarchies** (категорія: *Formal Schemas & Validation:*). Забезпечує детерміновану нормалізацію структур знань, графових зв'язків та концептуальних топологій.

---

## 2. Machine Contract (Schema.org / JSON-LD)

```json
{
  "@context": "https://schema.org",
  "@type": "DefinedTerm",
  "name": "XorSchema",
  "inDefinedTermSet": "Division 02: Cognitive & Ontological Systems",
  "termCode": "D02-COG-013",
  "description": "Formal architectural primitive for formal schemas & validation: within 1. machine ontologies & taxonomic hierarchies.",
  "additionalProperty": [
    {
      "name": "subsystem",
      "value": "1. Machine Ontologies & Taxonomic Hierarchies"
    },
    {
      "name": "category",
      "value": "Formal Schemas & Validation:"
    },
    {
      "name": "canonicalUri",
      "value": "urn:namencora:d02:xorschema"
    }
  ]
}
```

---

## 3. Architectural Properties

| Invariant / Property | Specification |
| :--- | :--- |
| **Subsystem Tier** | `1. Machine Ontologies & Taxonomic Hierarchies` |
| **Category Target** | `Formal Schemas & Validation:` |
| **Canonical URI** | `urn:namencora:d02:xorschema` |
| **Ontology Model** | `Directed Acyclic Graph (DAG) / Lattice Hierarchy` |

---
*Part of the Namencora Systems & Nomenclature Registry (Cohort B).*
