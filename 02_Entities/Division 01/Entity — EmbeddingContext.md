---
type: entity
project: namencora
division: "Division 01: Storage Engines & Memory Topologies"
subsystem: "2. High-Dimensional Vector Runtime"
category: "Context Spaces:"
namespace: EmbeddingContext
term_code: D01-STG-013
status: candidate
canonical_uri: "urn:namencora:d01:embeddingcontext"
tags:
  - entity
  - namespace
  - storage-engines
  - cohort-b
schema_org:
  "@type": DefinedTerm
  name: EmbeddingContext
  termCode: D01-STG-013
---

# EmbeddingContext

> **System Anchor**: `embeddingcontext.com`  
> **Classification ID**: `D01-STG-013`  
> **Subsystem**: 2. High-Dimensional Vector Runtime / Context Spaces:

---

## 1. Technical Definition (Human Layer)

Архітектурний примітив підсистеми **2. High-Dimensional Vector Runtime** (категорія: *Context Spaces:*). Забезпечує детерміновану роботу контуру зберігання та обробки станів.

---

## 2. Machine Contract (Schema.org / JSON-LD)

```json
{
  "@context": "https://schema.org",
  "@type": "DefinedTerm",
  "name": "EmbeddingContext",
  "inDefinedTermSet": "Division 01: Storage Engines & Memory Topologies",
  "termCode": "D01-STG-013",
  "description": "Formal architectural primitive for context spaces: within 2. high-dimensional vector runtime.",
  "additionalProperty": [
    {
      "name": "subsystem",
      "value": "2. High-Dimensional Vector Runtime"
    },
    {
      "name": "category",
      "value": "Context Spaces:"
    },
    {
      "name": "canonicalUri",
      "value": "urn:namencora:d01:embeddingcontext"
    }
  ]
}
```

---

## 3. Architectural Properties

| Invariant / Property | Specification |
| :--- | :--- |
| **Subsystem Tier** | `2. High-Dimensional Vector Runtime` |
| **Category Target** | `Context Spaces:` |
| **Canonical URI** | `urn:namencora:d01:embeddingcontext` |
| **Isolation Model** | `Process-bounded memory / Direct NVMe-aligned` |

---
*Part of the Namencora Systems & Nomenclature Registry (Cohort B).*
