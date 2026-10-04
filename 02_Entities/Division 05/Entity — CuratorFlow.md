---
type: entity
project: namencora
division: "Division 05: Execution Pipelines & Streaming Runtimes"
subsystem: "3. Event Runtimes & Execution Schedulers"
category: "Schedulers, Task Loops & Pipelines:"
namespace: CuratorFlow
term_code: D05-RUN-023
status: candidate
canonical_uri: "urn:namencora:d05:curatorflow"
tags:
  - entity
  - namespace
  - execution-pipelines
  - cohort-b
schema_org:
  "@type": DefinedTerm
  name: CuratorFlow
  termCode: D05-RUN-023
---

# CuratorFlow

> **System Anchor**: `curatorflow.com`  
> **Classification ID**: `D05-RUN-023`  
> **Subsystem**: 3. Event Runtimes & Execution Schedulers / Schedulers, Task Loops & Pipelines:

---

## 1. Technical Definition (Human Layer)

Виконавчий та потоковий примітив підсистеми **3. Event Runtimes & Execution Schedulers** (категорія: *Schedulers, Task Loops & Pipelines:*). Забезпечує конвеєрну маршрутизацію транзакцій, нульове копіювання при передачі подій (zero-allocation messaging) та диспетчеризацію задач реального часу.

---

## 2. Machine Contract (Schema.org / JSON-LD)

```json
{
  "@context": "https://schema.org",
  "@type": "DefinedTerm",
  "name": "CuratorFlow",
  "inDefinedTermSet": "Division 05: Execution Pipelines & Streaming Runtimes",
  "termCode": "D05-RUN-023",
  "description": "Formal architectural primitive for schedulers, task loops & pipelines: within 3. event runtimes & execution schedulers.",
  "additionalProperty": [
    {
      "name": "subsystem",
      "value": "3. Event Runtimes & Execution Schedulers"
    },
    {
      "name": "category",
      "value": "Schedulers, Task Loops & Pipelines:"
    },
    {
      "name": "canonicalUri",
      "value": "urn:namencora:d05:curatorflow"
    }
  ]
}
```

---

## 3. Architectural Properties

| Invariant / Property | Specification |
| :--- | :--- |
| **Subsystem Tier** | `3. Event Runtimes & Execution Schedulers` |
| **Category Target** | `Schedulers, Task Loops & Pipelines:` |
| **Canonical URI** | `urn:namencora:d05:curatorflow` |
| **Execution Model** | `Event-Driven Streaming DAG / Zero-Allocation Ring Pipeline` |

---
*Part of the Namencora Systems & Nomenclature Registry (Cohort B).*
