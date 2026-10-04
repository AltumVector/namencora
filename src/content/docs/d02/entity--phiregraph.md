---
title: "PhireGraph (D02-COG-018)"
type: entity
project: namencora
division: "Division 02: Cognitive & Ontological Systems"
subsystem: "Machine Ontologies & Taxonomic Hierarchies"
category: "Knowledge & Lock Graphs"
namespace: PhireGraph
term_code: D02-COG-018
status: candidate
canonical_uri: "urn:namencora:d02:phiregraph"
tags:
  - entity
  - namespace
  - cognitive-systems
  - cohort-b
schema_org:
  "@type": DefinedTerm
  name: PhireGraph
  termCode: D02-COG-018
---> **System Anchor**: `phiregraph.com`  
> **Classification ID**: `D02-COG-018`  
> **Subsystem**: Machine Ontologies & Taxonomic Hierarchies / Knowledge & Lock Graphs
---

## 1. Technical Definition (Human Layer)

Ontological and cognitive semantic primitive for the Machine Ontologies & Taxonomic Hierarchies subsystem (category: Knowledge & Lock Graphs). Enforces deterministic knowledge normalization, graph relational structures, and conceptual topologies.

---

## 2. Machine Contract (Schema.org / JSON-LD)

```json
{
  "@context": "https://schema.org",
  "@type": "DefinedTerm",
  "name": "PhireGraph",
  "inDefinedTermSet": "Division 02: Cognitive & Ontological Systems",
  "termCode": "D02-COG-018",
  "description": "Formal architectural primitive for knowledge & lock graphs.",
  "additionalProperty": [
    {
      "name": "subsystem",
      "value": "Machine Ontologies & Taxonomic Hierarchies"
    },
    {
      "name": "category",
      "value": "Knowledge & Lock Graphs"
    },
    {
      "name": "canonicalUri",
      "value": "urn:namencora:d02:phiregraph"
    }
  ]
}
```

---

## 3. Architectural Properties

| Invariant / Property | Specification |
| :--- | :--- |
| **Subsystem Tier** | `Machine Ontologies & Taxonomic Hierarchies` |
| **Category Target** | `Knowledge & Lock Graphs` |
| **Canonical URI** | `urn:namencora:d02:phiregraph` |
| **Ontology Model** | `Directed Acyclic Graph (DAG) / Lattice Hierarchy` |

---
*Part of the Namencora Systems & Nomenclature Registry (Cohort B).*
