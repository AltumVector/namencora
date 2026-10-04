---
title: "VetoEdge (D03-GOV-002)"
type: entity
project: namencora
division: "Division 03: Systems Governance & Consensus"
subsystem: "1. Deterministic Circuit Breakers & Veto Quorums"
category: "Core Veto Primitives:"
namespace: VetoEdge
term_code: D03-GOV-002
status: candidate
canonical_uri: "urn:namencora:d03:vetoedge"
tags:
  - entity
  - namespace
  - systems-governance
  - cohort-b
schema_org:
  "@type": DefinedTerm
  name: VetoEdge
  termCode: D03-GOV-002
---> **System Anchor**: `vetoedge.com`  
> **Classification ID**: `D03-GOV-002`  
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
  "name": "VetoEdge",
  "inDefinedTermSet": "Division 03: Systems Governance & Consensus",
  "termCode": "D03-GOV-002",
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
      "value": "urn:namencora:d03:vetoedge"
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
| **Canonical URI** | `urn:namencora:d03:vetoedge` |
| **Governance Model** | `Byzantine Fault Tolerant / Deterministic Abort Envelope` |

---
*Part of the Namencora Systems & Nomenclature Registry (Cohort B).*
