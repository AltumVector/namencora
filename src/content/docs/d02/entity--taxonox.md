---
title: "TaxonOx (D02-COG-007)"
type: entity
project: namencora
division: "Division 02: Cognitive & Ontological Systems"
subsystem: "Machine Ontologies & Taxonomic Hierarchies"
category: "Core Taxonomic Engines"
namespace: TaxonOx
term_code: D02-COG-007
status: candidate
canonical_uri: "urn:namencora:d02:taxonox"
tags:
  - entity
  - namespace
  - cognitive-systems
  - cohort-b
schema_org:
  "@type": DefinedTerm
  name: TaxonOx
  termCode: D02-COG-007
---

> **System Anchor**: `taxonox.com`  
> **Classification ID**: `D02-COG-007`  
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
  "name": "TaxonOx",
  "inDefinedTermSet": {
    "@type": "DefinedTermSet",
    "name": "Division 02: Cognitive & Ontological Systems"
  },
  "termCode": "D02-COG-007",
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
      "value": "urn:namencora:d02:taxonox"
    }
  ]
}
```

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "DefinedTerm",
  "name": "TaxonOx",
  "inDefinedTermSet": {
    "@type": "DefinedTermSet",
    "name": "Division 02: Cognitive & Ontological Systems"
  },
  "termCode": "D02-COG-007",
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
      "value": "urn:namencora:d02:taxonox"
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
| **Canonical URI** | `urn:namencora:d02:taxonox` |
| Specification Status | Candidate Specification (Active Review) |
| **Ontology Model** | `Directed Acyclic Graph (DAG) / Lattice Hierarchy` |

---
*Part of the Namencora Systems & Nomenclature Registry (Cohort B).*
