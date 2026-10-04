---
title: "SubstrateNode (D01-STG-008)"
type: entity
project: namencora
division: "Division 01: Storage Engines & Memory Topologies"
subsystem: "1. Deep Storage & Hardware Substrates"
category: "Zero-Copy & Hardware Substrates:"
namespace: SubstrateNode
term_code: D01-STG-008
status: candidate
canonical_uri: "urn:namencora:d01:substratenode"
tags:
  - entity
  - namespace
  - storage-engines
  - cohort-b
schema_org:
  "@type": DefinedTerm
  name: SubstrateNode
  termCode: D01-STG-008
---> **System Anchor**: `substratenode.com`  
> **Classification ID**: `D01-STG-008`  
> **Subsystem**: 1. Deep Storage & Hardware Substrates / Zero-Copy & Hardware Substrates:

---

## 1. Technical Definition (Human Layer)

Архітектурний примітив підсистеми **1. Deep Storage & Hardware Substrates** (категорія: *Zero-Copy & Hardware Substrates:*). Забезпечує детерміновану роботу контуру зберігання та обробки станів.

---

## 2. Machine Contract (Schema.org / JSON-LD)

```json
{
  "@context": "https://schema.org",
  "@type": "DefinedTerm",
  "name": "SubstrateNode",
  "inDefinedTermSet": "Division 01: Storage Engines & Memory Topologies",
  "termCode": "D01-STG-008",
  "description": "Formal architectural primitive for zero-copy & hardware substrates: within 1. deep storage & hardware substrates.",
  "additionalProperty": [
    {
      "name": "subsystem",
      "value": "1. Deep Storage & Hardware Substrates"
    },
    {
      "name": "category",
      "value": "Zero-Copy & Hardware Substrates:"
    },
    {
      "name": "canonicalUri",
      "value": "urn:namencora:d01:substratenode"
    }
  ]
}
```

---

## 3. Architectural Properties

| Invariant / Property | Specification |
| :--- | :--- |
| **Subsystem Tier** | `1. Deep Storage & Hardware Substrates` |
| **Category Target** | `Zero-Copy & Hardware Substrates:` |
| **Canonical URI** | `urn:namencora:d01:substratenode` |
| **Isolation Model** | `Process-bounded memory / Direct NVMe-aligned` |

---
*Part of the Namencora Systems & Nomenclature Registry (Cohort B).*
