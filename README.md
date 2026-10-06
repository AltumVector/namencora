# Namencora: Canonical Systems Registry

![Registry Status](https://img.shields.io/badge/status-active-success) 
![Entities](https://img.shields.io/badge/canonical--entities-355-blue) 
![Governance](https://img.shields.io/badge/governance-hybrid--rfc-orange) 
![Schema](https://img.shields.io/badge/schema.org-DefinedTerm-informational)

**Namencora** — детермінований інженерний реєстр канонічних просторів імен, архітектурних примітивів та системних топологій. Проєкт встановлює машинно-верифіковану онтологію для високопродуктивних розподілених систем, фазової динаміки та потокових середовищ виконання.

---

## 1. Топологія дивізіонів

| Дивізіон | Найменування | Активи | Спрямування |
| :--- | :--- | :---: | :--- |
| **`Division 00`** | Core & Protocol Primitives | **2** | Фундаментальні протокольні примітиви нульового рівня |
| **`Division 01`** | Storage Engines & Memory Topologies | **42** | Двигуни зберігання, векторні простори та структури індексації |
| **`Division 02`** | Cognitive & Ontological Systems | **91** | Онтологічні матриці, класифікатори та семантичні простори |
| **`Division 03`** | Systems Governance & Consensus | **64** | Запобіжники (circuit breakers), вето-кворуми та арбітраж компромісів |
| **`Division 04`** | Computational Physics & Dynamics | **45** | Фазові простори, нелінійні динамічні оператори та дисипація |
| **`Division 05`** | Execution Pipelines & Streaming Runtimes | **83** | Потокові рантайми, конвеєри нульового копіювання та черги подій |
| **Division 06** | Computational Dynamics & Metrology | 28 | Нелінійна динаміка, тензорні оператори, метрологія NDT та обчислювальні ядра |
| **Разом** | | **355** | |

---

## 2. Стандарти кодифікації та машинні контракти

Кожна сутність реєстру закріплюється двома взаємопов'язаними рівнями:
1. **Human Layer (Markdown-специфікація):** Семантичне та інженерне визначення меж, властивостей і моделі поведінки примітива.
2. **Machine Contract (`Schema.org/DefinedTerm` JSON-LD):** Детермінований машинозчитуваний блок для автоматичної індексації ШІ-краулерами, RAG-контурами та графами знань.

Ідентифікатори сутностей формуються за схемою:
```text
D[Дивізіон]-[Категорія]-[Порядковий_номер]
Приклади: D01-STG-001 (BTreeIndex), D03-GOV-067 (BallisticTradeoffs)
```

---

## 3. Машинний доступ (LLM / Agent Grounding)

- **`llm.txt`**: Спеціалізований структурований індекс для контекстного заземлення агентів і LLM.
- **`registry.json`**: Повний машиночитаний JSON-маніфест реєстру для інтеграцій та пайплайнів перевірки сумісності.

---

## 4. Регламент участі (Governance & Contributing)

Реєстр функціонує за гібридною моделлю управління (Open RFC / Architectural Veto):
- Подання нових сутностей здійснюється через стандартизовані Pull Requests.
- Усі заявки проходять лінтинг валідності JSON-LD та перевірку на колізії імен.
- Фінальне затвердження статусу (`Adopted`) закріплене за архітектурним ядром Namencora.

Детальний опис процедури зафіксовано в документорі: `00_Meta/Registry_Governance.md`.

---
© 2026 Namencora Systems Architecture. Distributed under deterministic consensus protocols.