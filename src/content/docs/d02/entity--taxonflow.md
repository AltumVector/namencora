---
title: "TaxonFlow (D02-COG-005)"
type: entity
project: namencora
division: "Division 02: Cognitive & Ontological Systems"
subsystem: "1. Machine Ontologies & Taxonomic Hierarchies"
category: "Core Taxonomic Engines:"
namespace: TaxonFlow
term_code: D02-COG-005
status: candidate
canonical_uri: "urn:namencora:d02:taxonflow"
tags:
  - entity
  - namespace
  - cognitive-systems
  - cohort-b
schema_org:
  "@type": DefinedTerm
  name: TaxonFlow
  termCode: D02-COG-005
---> **System Anchor**: `taxonflow.com`  
> **Classification ID**: `D02-COG-005`  
> **Subsystem**: 1. Machine Ontologies & Taxonomic Hierarchies / Core Taxonomic Engines:

---

## 1. Technical Definition (Human Layer)

Онтологічний та семантичний примітив підсистеми **1. Machine Ontologies & Taxonomic Hierarchies** (категорія: *Core Taxonomic Engines:*). Забезпечує детерміновану нормалізацію структур знань, графових зв'язків та концептуальних топологій.

---

## 2. Machine Contract (Schema.org / JSON-LD)

```json
{
  "@context": "https://schema.org",
  "@type": "DefinedTerm",
  "name": "TaxonFlow",
  "inDefinedTermSet": "Division 02: Cognitive & Ontological Systems",
  "termCode": "D02-COG-005",
  "description": "Formal architectural primitive for core taxonomic engines: within 1. machine ontologies & taxonomic hierarchies.",
  "additionalProperty": [
    {
      "name": "subsystem",
      "value": "1. Machine Ontologies & Taxonomic Hierarchies"
    },
    {
      "name": "category",
      "value": "Core Taxonomic Engines:"
    },
    {
      "name": "canonicalUri",
      "value": "urn:namencora:d02:taxonflow"
    }
  ]
}
```

---

## 3. Architectural Properties

| Invariant / Property | Specification |
| :--- | :--- |
| **Subsystem Tier** | `1. Machine Ontologies & Taxonomic Hierarchies` |
| **Category Target** | `Core Taxonomic Engines:` |
| **Canonical URI** | `urn:namencora:d02:taxonflow` |
| **Ontology Model** | `Directed Acyclic Graph (DAG) / Lattice Hierarchy` |

---
*Part of the Namencora Systems & Nomenclature Registry (Cohort B).*
