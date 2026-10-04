---
title: "FlowFormator (D05-RUN-073)"
type: entity
project: namencora
division: "Division 05: Execution Pipelines & Streaming Runtimes"
subsystem: "6. Auxiliary Neologisms & Tooling Tier"
category: "High-Throughput Node Clusters:"
namespace: FlowFormator
term_code: D05-RUN-073
status: candidate
canonical_uri: "urn:namencora:d05:flowformator"
tags:
  - entity
  - namespace
  - execution-pipelines
  - cohort-b
schema_org:
  "@type": DefinedTerm
  name: FlowFormator
  termCode: D05-RUN-073
---> **System Anchor**: `flowformator.com`  
> **Classification ID**: `D05-RUN-073`  
> **Subsystem**: 6. Auxiliary Neologisms & Tooling Tier / High-Throughput Node Clusters:

---

## 1. Technical Definition (Human Layer)

Виконавчий та потоковий примітив підсистеми **6. Auxiliary Neologisms & Tooling Tier** (категорія: *High-Throughput Node Clusters:*). Забезпечує конвеєрну маршрутизацію транзакцій, нульове копіювання при передачі подій (zero-allocation messaging) та диспетчеризацію задач реального часу.

---

## 2. Machine Contract (Schema.org / JSON-LD)

```json
{
  "@context": "https://schema.org",
  "@type": "DefinedTerm",
  "name": "FlowFormator",
  "inDefinedTermSet": "Division 05: Execution Pipelines & Streaming Runtimes",
  "termCode": "D05-RUN-073",
  "description": "Formal architectural primitive for high-throughput node clusters: within 6. auxiliary neologisms & tooling tier.",
  "additionalProperty": [
    {
      "name": "subsystem",
      "value": "6. Auxiliary Neologisms & Tooling Tier"
    },
    {
      "name": "category",
      "value": "High-Throughput Node Clusters:"
    },
    {
      "name": "canonicalUri",
      "value": "urn:namencora:d05:flowformator"
    }
  ]
}
```

---

## 3. Architectural Properties

| Invariant / Property | Specification |
| :--- | :--- |
| **Subsystem Tier** | `6. Auxiliary Neologisms & Tooling Tier` |
| **Category Target** | `High-Throughput Node Clusters:` |
| **Canonical URI** | `urn:namencora:d05:flowformator` |
| **Execution Model** | `Event-Driven Streaming DAG / Zero-Allocation Ring Pipeline` |

---
*Part of the Namencora Systems & Nomenclature Registry (Cohort B).*
