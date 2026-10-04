import os

folder = os.path.expanduser("~/DataHub/02_Knowledge/Namencora/02_Entities/Division 03")
B = chr(96) * 3

def generate(name, code, domain, uri, desc):
    return f"""---
type: alias
project: namencora
division: "Division 03: Systems Governance & Consensus"
subsystem: "Systems Governance"
category: "Defensive Namespace Resolution / Phonetic Collision Guard"
namespace: {name}
term_code: {code}
status: candidate
canonical_target: AiDronesOps
canonical_uri: {uri}
tags:
  - alias
  - defensive-namespace
  - systems-governance
  - cohort-b
schema_org:
  "@context": "https://schema.org"
  "@type": "DefinedTerm"
  name: "{name}"
  termCode: "{code}"
  inDefinedTermSet: "Division 03: Systems Governance & Consensus"
---

# {name}

> **System Anchor**: `{domain}`
> **Classification ID**: `{code}`
> **Canonical Target**: `AiDronesOps (D03-GOV-080)`
> **Subsystem**: Systems Governance / Defensive Namespace Resolution

---

## 1. Technical Definition (Human Layer)

{desc}

---

## 2. Machine Contract (Schema.org / JSON-LD)

{B}json
{{
  "@context": "https://schema.org",
  "@type": "DefinedTerm",
  "name": "{name}",
  "termCode": "{code}",
  "inDefinedTermSet": "Division 03: Systems Governance & Consensus",
  "sameAs": "https://namencora.com/d03/entity--aidronesops/"
}}
{B}

---

## 3. Architectural Properties

| Invariant / Property | Specification |
| :--- | :--- |
| **Subsystem Tier** | Systems Governance |
| **Category Target** | Defensive Namespace Resolution |
| **Canonical URI** | {uri} |
| **Canonical Target URI** | urn:namencora:d03:aidronesops |
| **Resolution Mode** | Deterministic Alias Forwarding |

---
*Part of the Namencora Systems & Nomenclature Registry (Defensive Namespace Layer).*
"""

c1 = generate(
    "AiDronOps",
    "D03-GOV-081",
    "aidronops.com",
    "urn:namencora:d03:aidronops",
    "Детермінований захисний примітив (Defensive Namespace Mirror) в однині для канонічної специфікації AiDronesOps. Виконує роль аліаса першого рівня для запобігання колізіям маршрутизації та усунення фонетичних розбіжностей під час виклику операційних контурів."
)

c2 = generate(
    "AiDronsOps",
    "D03-GOV-082",
    "aidronsops.com",
    "urn:namencora:d03:aidronsops",
    "Детермінований захисний примітив (Defensive Namespace Mirror) множинної форми для канонічної специфікації AiDronesOps. Забезпечує збереження цілісності простору імен та відмовостійку резолюцію запитів при адресації операцій агентного флоту."
)

with open(os.path.join(folder, "Entity — AiDronOps.md"), "w", encoding="utf-8") as f:
    f.write(c1.strip() + "\n")

with open(os.path.join(folder, "Entity — AiDronsOps.md"), "w", encoding="utf-8") as f:
    f.write(c2.strip() + "\n")

print("• [Успішно] Файли оновлено начисто.")
