---
type: entity
project: namencora
division: "Division 03: Systems Governance & Consensus"
subsystem: "1. Deterministic Circuit Breakers & Veto Quorums"
category: "Core Veto Primitives:"
namespace: VetoNode
term_code: D03-GOV-004
status: candidate
canonical_uri: "urn:namencora:d03:vetonode"
tags:
  - entity
  - namespace
  - systems-governance
  - cohort-b
schema_org:
  "@type": DefinedTerm
  name: VetoNode
  termCode: D03-GOV-004
---

# VetoNode

> **System Anchor**: `vetonode.com`  
> **Classification ID**: `D03-GOV-004`  
> **Subsystem**: 1. Deterministic Circuit Breakers & Veto Quorums / Core Veto Primitives:

---

## 1. Technical Definition (Human Layer)

Керуючий примітив та контур безпеки підсистеми **1. Deterministic Circuit Breakers & Veto Quorums** (категорія: *Core Veto Primitives:*). Реалізує детермінований арбітраж транзакцій, механізми переривання (circuit breakers) або балансування компромісних критеріїв.

---

## 2. Machine Contract (Schema.org / JSON-LD)

```json
{
  "@context": "https://schema.org",
  "@type": "DefinedTerm",
  "name": "VetoNode",
  "inDefinedTermSet": "Division 03: Systems Governance & Consensus",
  "termCode": "D03-GOV-004",
  "description": "Formal architectural primitive for core veto primitives: within 1. deterministic circuit breakers & veto quorums.",
  "additionalProperty": [
    {
      "name": "subsystem",
      "value": "1. Deterministic Circuit Breakers & Veto Quorums"
    },
    {
      "name": "category",
      "value": "Core Veto Primitives:"
    },
    {
      "name": "canonicalUri",
      "value": "urn:namencora:d03:vetonode"
    }
  ]
}
```

---

## 3. Architectural Properties

| Invariant / Property | Specification |
| :--- | :--- |
| **Subsystem Tier** | `1. Deterministic Circuit Breakers & Veto Quorums` |
| **Category Target** | `Core Veto Primitives:` |
| **Canonical URI** | `urn:namencora:d03:vetonode` |
| **Governance Model** | `Byzantine Fault Tolerant / Deterministic Abort Envelope` |

---
*Part of the Namencora Systems & Nomenclature Registry (Cohort B).*
