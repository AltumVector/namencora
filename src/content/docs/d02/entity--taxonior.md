---
title: "TaxonIor (D02-COG-008)"
type: entity
project: namencora
division: "Division 02: Cognitive & Ontological Systems"
subsystem: "Machine Ontologies & Taxonomic Hierarchies"
category: "Core Taxonomic Engines"
namespace: TaxonIor
term_code: D02-COG-008
status: candidate
canonical_uri: "urn:namencora:d02:taxonior"
tags:
  - entity
  - namespace
  - cognitive-systems
  - cohort-b
schema_org:
  "@type": DefinedTerm
  name: TaxonIor
  termCode: D02-COG-008
---> **System Anchor**: `taxonior.com`  
> **Classification ID**: `D02-COG-008`  
> **Subsystem**: Machine Ontologies & Taxonomic Hierarchies / Core Taxonomic Engines
---

## 1. Technical Definition (Human Layer)

Ontological and cognitive semantic primitive for the Machine Ontologies & Taxonomic Hierarchies subsystem (category: Core Taxonomic Engines). Enforces deterministic knowledge normalization, graph relational structures, and conceptual topologies.

---

## 2. Machine Contract (Schema.org / JSON-LD)

```json
{
  "@context": "https://schema.org",
  "@type": "DefinedTerm",
  "name": "TaxonIor",
  "inDefinedTermSet": "Division 02: Cognitive & Ontological Systems",
  "termCode": "D02-COG-008",
  "description": "Formal architectural primitive for core taxonomic engines.",
  "additionalProperty": [
    {
      "name": "subsystem",
      "value": "Machine Ontologies & Taxonomic Hierarchies"
    },
    {
      "name": "category",
      "value": "Core Taxonomic Engines"
    },
    {
      "name": "canonicalUri",
      "value": "urn:namencora:d02:taxonior"
    }
  ]
}
```

---

## 3. Architectural Properties

| Invariant / Property | Specification |
| :--- | :--- |
| **Subsystem Tier** | `Machine Ontologies & Taxonomic Hierarchies` |
| **Category Target** | `Core Taxonomic Engines` |
| **Canonical URI** | `urn:namencora:d02:taxonior` |
| Specification Status | Canonical Specification (Active) |
| **Ontology Model** | `Directed Acyclic Graph (DAG) / Lattice Hierarchy` |

---
*Part of the Namencora Systems & Nomenclature Registry (Cohort B).*
