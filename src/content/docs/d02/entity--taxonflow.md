---
title: "TaxonFlow (D02-COG-005)"
type: entity
project: namencora
division: "Division 02: Cognitive & Ontological Systems"
subsystem: "Machine Ontologies & Taxonomic Hierarchies"
category: "Core Taxonomic Engines"
namespace: TaxonFlow
term_code: D02-COG-005
status: candidate
canonical_uri: "urn:namencora:d02:taxonflow"
tags:
  - entity
  - namespace
  - cognitive-systems
  - cohort-b
schema_org:
  "@type": DefinedTerm
  name: TaxonFlow
  termCode: D02-COG-005
---> **System Anchor**: `taxonflow.com`  
> **Classification ID**: `D02-COG-005`  
> **Subsystem**: Machine Ontologies & Taxonomic Hierarchies / Core Taxonomic Engines
---

## 1. Technical Definition (Human Layer)

Ontological and cognitive semantic primitive for the Machine Ontologies & Taxonomic Hierarchies subsystem (category: Core Taxonomic Engines). Enforces deterministic knowledge normalization, graph relational structures, and conceptual topologies.

---

## 2. Machine Contract (Schema.org / JSON-LD)

```json
{
  "@context": "https://schema.org",
  "@type": "DefinedTerm",
  "name": "TaxonFlow",
  "inDefinedTermSet": {
    "@type": "DefinedTermSet",
    "name": "Division 02: Cognitive & Ontological Systems"
  },
  "termCode": "D02-COG-005",
  "description": "Formal architectural primitive for core taxonomic engines.",
  "additionalProperty": [
    {
      "name": "subsystem",
      "value": "Machine Ontologies & Taxonomic Hierarchies"
    },
    {
      "name": "category",
      "value": "Core Taxonomic Engines"
    },
    {
      "name": "canonicalUri",
      "value": "urn:namencora:d02:taxonflow"
    }
  ]
}
```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "DefinedTerm",
  "name": "TaxonFlow",
  "inDefinedTermSet": {
    "@type": "DefinedTermSet",
    "name": "Division 02: Cognitive & Ontological Systems"
  },
  "termCode": "D02-COG-005",
  "description": "Formal architectural primitive for core taxonomic engines.",
  "additionalProperty": [
    {
      "name": "subsystem",
      "value": "Machine Ontologies & Taxonomic Hierarchies"
    },
    {
      "name": "category",
      "value": "Core Taxonomic Engines"
    },
    {
      "name": "canonicalUri",
      "value": "urn:namencora:d02:taxonflow"
    }
  ]
}
</script>

---

## 3. Architectural Properties

| Invariant / Property | Specification |
| :--- | :--- |
| **Subsystem Tier** | `Machine Ontologies & Taxonomic Hierarchies` |
| **Category Target** | `Core Taxonomic Engines` |
| **Canonical URI** | `urn:namencora:d02:taxonflow` |
| Specification Status | Candidate Specification (Active Review) |
| **Ontology Model** | `Directed Acyclic Graph (DAG) / Lattice Hierarchy` |

---
*Part of the Namencora Systems & Nomenclature Registry (Cohort B).*
