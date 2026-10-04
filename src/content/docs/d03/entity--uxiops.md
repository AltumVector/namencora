---
title: "UxiOps (D03-GOV-079)"
type: entity
project: namencora
division: "Division 03: Systems Governance & Consensus"
subsystem: "Systems Governance"
category: "Consensus Primitive"
namespace: UxiOps
term_code: D03-GOV-079
status: candidate
canonical_uri: "urn:namencora:d03:uxiops"
tags:
  - entity
  - namespace
  - systems-governance
  - cohort-b
schema_org:
  "@type": DefinedTerm
  name: UxiOps
  termCode: D03-GOV-079
---> **System Anchor**: `uxiops.com`  
> **Classification ID**: `D03-GOV-079`  
> **Subsystem**: Systems Governance / Consensus Primitive

---

## 1. Technical Definition (Human Layer)

Керуючий примітив та контур безпеки підсистеми **Systems Governance**. Реалізує детермінований арбітраж транзакцій та механізми переривання (circuit breakers).

---

## 2. Machine Contract (Schema.org / JSON-LD)

```json
{
  "@context": "https://schema.org",
  "@type": "DefinedTerm",
  "name": "UxiOps",
  "inDefinedTermSet": "Division 03: Systems Governance & Consensus",
  "termCode": "D03-GOV-079",
  "description": "Formal architectural primitive for governance and arbitration within Systems Governance.",
  "additionalProperty": [
    {
      "name": "subsystem",
      "value": "Systems Governance"
    },
    {
      "name": "category",
      "value": "Consensus Primitive"
    },
    {
      "name": "canonicalUri",
      "value": "urn:namencora:d03:uxiops"
    }
  ]
}
```

---

## 3. Architectural Properties

| Invariant / Property | Specification |
| :--- | :--- |
| **Subsystem Tier** | `Systems Governance` |
| **Category Target** | `Consensus Primitive` |
| **Canonical URI** | `urn:namencora:d03:uxiops` |
| **Governance Model** | `Byzantine Fault Tolerant / Deterministic Abort Envelope` |

---
*Part of the Namencora Systems & Nomenclature Registry (Cohort B).*
