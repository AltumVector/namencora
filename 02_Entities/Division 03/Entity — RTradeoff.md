---
type: entity
project: namencora
division: "Division 03: Systems Governance & Consensus"
subsystem: "Multi-Objective Trade-off Engines"
category: "Systems Trade-off Analysis & Arbitration"
namespace: RTradeoff
term_code: D03-GOV-020
status: candidate
canonical_uri: "urn:namencora:d03:rtradeoff"
tags:
  - entity
  - namespace
  - systems-governance
  - cohort-b
schema_org:
  "@type": DefinedTerm
  name: RTradeoff
  termCode: D03-GOV-020
---

# RTradeoff

> **System Anchor**: `rtradeoff.com`  
> **Classification ID**: `D03-GOV-020`  
> **Subsystem**: Multi-Objective Trade-off Engines / Systems Trade-off Analysis & Arbitration
---

## 1. Technical Definition (Human Layer)

Architectural governance and control primitive for the Multi-Objective Trade-off Engines subsystem (category: Systems Trade-off Analysis & Arbitration). Implements deterministic transaction arbitration, circuit breaking mechanisms, and consensus policy balancing.

---

## 2. Machine Contract (Schema.org / JSON-LD)

```json
{
  "@context": "https://schema.org",
  "@type": "DefinedTerm",
  "name": "RTradeoff",
  "inDefinedTermSet": "Division 03: Systems Governance & Consensus",
  "termCode": "D03-GOV-020",
  "description": "Formal architectural primitive for systems trade-off analysis & arbitration.",
  "additionalProperty": [
    {
      "name": "subsystem",
      "value": "Multi-Objective Trade-off Engines"
    },
    {
      "name": "category",
      "value": "Systems Trade-off Analysis & Arbitration"
    },
    {
      "name": "canonicalUri",
      "value": "urn:namencora:d03:rtradeoff"
    }
  ]
}
```

---

## 3. Architectural Properties

| Invariant / Property | Specification |
| :--- | :--- |
| **Subsystem Tier** | `Multi-Objective Trade-off Engines` |
| **Category Target** | `Systems Trade-off Analysis & Arbitration` |
| **Canonical URI** | `urn:namencora:d03:rtradeoff` |
| **Governance Model** | `Byzantine Fault Tolerant / Deterministic Abort Envelope` |

---
*Part of the Namencora Systems & Nomenclature Registry (Cohort B).*
