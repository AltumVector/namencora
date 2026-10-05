---
type: entity
project: namencora
division: "Division 02: Cognitive & Ontological Systems"
subsystem: "Semantic Runtime & Knowledge Representation"
category: "Analysis, Scanning & Metrics"
namespace: SemaScan
term_code: D02-COG-029
status: candidate
canonical_uri: "urn:namencora:d02:semascan"
tags:
  - entity
  - namespace
  - cognitive-systems
  - cohort-b
schema_org:
  "@type": DefinedTerm
  name: SemaScan
  termCode: D02-COG-029
---

# SemaScan

> **System Anchor**: `semascan.com`  
> **Classification ID**: `D02-COG-029`  
> **Subsystem**: Semantic Runtime & Knowledge Representation / Analysis, Scanning & Metrics
---

## 1. Technical Definition (Human Layer)

Ontological and cognitive semantic primitive for the Semantic Runtime & Knowledge Representation subsystem (category: Analysis, Scanning & Metrics). Enforces deterministic knowledge normalization, graph relational structures, and conceptual topologies.

---

## 2. Machine Contract (Schema.org / JSON-LD)

```json
{
  "@context": "https://schema.org",
  "@type": "DefinedTerm",
  "name": "SemaScan",
  "inDefinedTermSet": "Division 02: Cognitive & Ontological Systems",
  "termCode": "D02-COG-029",
  "description": "Formal architectural primitive for analysis, scanning & metrics.",
  "additionalProperty": [
    {
      "name": "subsystem",
      "value": "Semantic Runtime & Knowledge Representation"
    },
    {
      "name": "category",
      "value": "Analysis, Scanning & Metrics"
    },
    {
      "name": "canonicalUri",
      "value": "urn:namencora:d02:semascan"
    }
  ]
}
```

---

## 3. Architectural Properties

| Invariant / Property | Specification |
| :--- | :--- |
| **Subsystem Tier** | `Semantic Runtime & Knowledge Representation` |
| **Category Target** | `Analysis, Scanning & Metrics` |
| **Canonical URI** | `urn:namencora:d02:semascan` |
| Specification Status | Canonical Specification (Active) |
| **Ontology Model** | `Directed Acyclic Graph (DAG) / Lattice Hierarchy` |

---
*Part of the Namencora Systems & Nomenclature Registry (Cohort B).*
