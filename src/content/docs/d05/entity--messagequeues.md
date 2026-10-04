---
title: "MessageQueues (D05-RUN-001)"
type: entity
project: namencora
division: "Division 05: Execution Pipelines & Streaming Runtimes"
subsystem: "1. Core Streaming Fabrics & Message Queues"
category: "Category Standard Queues & Streams:"
namespace: MessageQueues
term_code: D05-RUN-001
status: candidate
canonical_uri: "urn:namencora:d05:messagequeues"
tags:
  - entity
  - namespace
  - execution-pipelines
  - cohort-b
schema_org:
  "@type": DefinedTerm
  name: MessageQueues
  termCode: D05-RUN-001
---> **System Anchor**: `messagequeues.com`  
> **Classification ID**: `D05-RUN-001`  
> **Subsystem**: 1. Core Streaming Fabrics & Message Queues / Category Standard Queues & Streams:

---

## 1. Technical Definition (Human Layer)

Виконавчий та потоковий примітив підсистеми **1. Core Streaming Fabrics & Message Queues** (категорія: *Category Standard Queues & Streams:*). Забезпечує конвеєрну маршрутизацію транзакцій, нульове копіювання при передачі подій (zero-allocation messaging) та диспетчеризацію задач реального часу.

---

## 2. Machine Contract (Schema.org / JSON-LD)

```json
{
  "@context": "https://schema.org",
  "@type": "DefinedTerm",
  "name": "MessageQueues",
  "inDefinedTermSet": "Division 05: Execution Pipelines & Streaming Runtimes",
  "termCode": "D05-RUN-001",
  "description": "Formal architectural primitive for category standard queues & streams: within 1. core streaming fabrics & message queues.",
  "additionalProperty": [
    {
      "name": "subsystem",
      "value": "1. Core Streaming Fabrics & Message Queues"
    },
    {
      "name": "category",
      "value": "Category Standard Queues & Streams:"
    },
    {
      "name": "canonicalUri",
      "value": "urn:namencora:d05:messagequeues"
    }
  ]
}
```

---

## 3. Architectural Properties

| Invariant / Property | Specification |
| :--- | :--- |
| **Subsystem Tier** | `1. Core Streaming Fabrics & Message Queues` |
| **Category Target** | `Category Standard Queues & Streams:` |
| **Canonical URI** | `urn:namencora:d05:messagequeues` |
| **Execution Model** | `Event-Driven Streaming DAG / Zero-Allocation Ring Pipeline` |

---
*Part of the Namencora Systems & Nomenclature Registry (Cohort B).*
