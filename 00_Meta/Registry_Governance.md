# Namencora: Architecture & Registry Governance Model

## 1. System Triad (Ontological Layers)
1. **Registry (State of Truth):** Primary authoritative namespace origin (`urn:namencora:dXX:name`). Anchors mathematical, logical, and physical invariants of entities independent of domain availability or external software.
2. **Catalog (Read Projection):** Public state projection (`namencora.com/registry`, `llm.txt`, API) for developers, search crawlers, and AI agents.
3. **Domain (Canonical Transport Resolver):** Direct network resolution address bridging the namespace to the global web.

## 2. Hybrid Intake Mechanics
* **Open RFC Submission:** External teams and researchers propose new primitives using a standardized RFC template (field schema, boundaries, Schema.org).
* **Automated Collision Linting:** Automated validation against collisions, semantic duplication, and JSON-LD compliance.
* **Architectural Veto:** Final adoption status (`Adopted`) remains reserved for the Namencora steering core to maintain division orthogonality.

## 3. Long-Term Institutionalization
* **Machine Grounding:** Semantic grounding of engineering primitives within latent spaces of LLMs.
* **Assay Conformance:** System certification confirming compliance with Namencora primitive specifications.
