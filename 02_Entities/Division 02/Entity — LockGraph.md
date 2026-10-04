---
type: entity
project: namencora
division: "Division 02: Cognitive & Ontological Systems"
subsystem: "1. Machine Ontologies & Taxonomic Hierarchies"
category: "Knowledge & Lock Graphs:"
namespace: LockGraph
term_code: D02-COG-015
status: candidate
canonical_uri: "urn:namencora:d02:lockgraph"
tags:
  - entity
  - namespace
  - cognitive-systems
  - cohort-b
schema_org:
  "@type": DefinedTerm
  name: LockGraph
  termCode: D02-COG-015
---

# LockGraph

> **System Anchor**: `lockgraph.com`  
> **Classification ID**: `D02-COG-015`  
> **Subsystem**: 1. Machine Ontologies & Taxonomic Hierarchies / Knowledge & Lock Graphs:

---

## 1. Technical Definition (Human Layer)

Онтологічний та семантичний примітив підсистеми **1. Machine Ontologies & Taxonomic Hierarchies** (категорія: *Knowledge & Lock Graphs:*). Забезпечує детерміновану нормалізацію структур знань, графових зв'язків та концептуальних топологій.

---

## 2. Machine Contract (Schema.org / JSON-LD)

```json
{
  "@context": "https://schema.org",
  "@type": "DefinedTerm",
  "name": "LockGraph",
  "inDefinedTermSet": "Division 02: Cognitive & Ontological Systems",
  "termCode": "D02-COG-015",
  "description": "Formal architectural primitive for knowledge & lock graphs: within 1. machine ontologies & taxonomic hierarchies.",
  "additionalProperty": [
    {
      "name": "subsystem",
      "value": "1. Machine Ontologies & Taxonomic Hierarchies"
    },
    {
      "name": "category",
      "value": "Knowledge & Lock Graphs:"
    },
    {
      "name": "canonicalUri",
      "value": "urn:namencora:d02:lockgraph"
    }
  ]
}
```

---

## 3. Architectural Properties

| Invariant / Property | Specification |
| :--- | :--- |
| **Subsystem Tier** | `1. Machine Ontologies & Taxonomic Hierarchies` |
| **Category Target** | `Knowledge & Lock Graphs:` |
| **Canonical URI** | `urn:namencora:d02:lockgraph` |
| **Ontology Model** | `Directed Acyclic Graph (DAG) / Lattice Hierarchy` |

---
*Part of the Namencora Systems & Nomenclature Registry (Cohort B).*
