---
type: entity
project: namencora
division: "Division 03: Systems Governance & Consensus"
subsystem: "Deterministic Circuit Breakers & Veto Quorums"
category: "Core Veto Primitives"
namespace: VetoIQ
term_code: D03-GOV-010
status: candidate
canonical_uri: "urn:namencora:d03:vetoiq"
tags:
  - entity
  - namespace
  - systems-governance
  - cohort-b
schema_org:
  "@type": DefinedTerm
  name: VetoIQ
  termCode: D03-GOV-010
---

# VetoIQ

> **System Anchor**: `vetoiq.com`  
> **Classification ID**: `D03-GOV-010`  
> **Subsystem**: Deterministic Circuit Breakers & Veto Quorums / Core Veto Primitives
---

## 1. Technical Definition (Human Layer)

Architectural governance and control primitive for the Deterministic Circuit Breakers & Veto Quorums subsystem (category: Core Veto Primitives). Implements deterministic transaction arbitration, circuit breaking mechanisms, and consensus policy balancing.

---

## 2. Machine Contract (Schema.org / JSON-LD)

```json
{
  "@context": "https://schema.org",
  "@type": "DefinedTerm",
  "name": "VetoIQ",
  "inDefinedTermSet": "Division 03: Systems Governance & Consensus",
  "termCode": "D03-GOV-010",
  "description": "Formal architectural primitive for core veto primitives.",
  "additionalProperty": [
    {
      "name": "subsystem",
      "value": "Deterministic Circuit Breakers & Veto Quorums"
    },
    {
      "name": "category",
      "value": "Core Veto Primitives"
    },
    {
      "name": "canonicalUri",
      "value": "urn:namencora:d03:vetoiq"
    }
  ]
}
```

---

## 3. Architectural Properties

| Invariant / Property | Specification |
| :--- | :--- |
| **Subsystem Tier** | `Deterministic Circuit Breakers & Veto Quorums` |
| **Category Target** | `Core Veto Primitives` |
| **Canonical URI** | `urn:namencora:d03:vetoiq` |
| Specification Status | Candidate Specification (Active Review) |
| **Governance Model** | `Byzantine Fault Tolerant / Deterministic Abort Envelope` |

---
*Part of the Namencora Systems & Nomenclature Registry (Cohort B).*
