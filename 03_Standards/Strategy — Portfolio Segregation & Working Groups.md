---
type: strategy
project: namencora
created: 2026-10-02
status: ratified
tags:
  - strategy
  - portfolio-segregation
  - working-groups
  - anti-alchemy
  - air-gap-architecture
---

# Strategy: Portfolio Segregation & Research Divisions

## 1. Проблема семантичної ентропії (Anti-Trash Principle)
Спроба об'єднати різнорідні активи портфеля (~700+ преміумів) в один загальний список знищує технічний авторитет платформи. Поєднання вузькопрофільних інженерних понять із побутовими або комерційними брендами класифікується пошуковими системами та інженерами як семантичний шум і лістинг реселлера.

## 2. Жорстка сегрегація портфеля на когорти
- **Когорта A: Комерційні та брендові активи (~550–600 доменів)**
  - Приклади: `Vetlona.com`, `Pilovex.com`, `PureDiox.com`, `Fluxwolf.com`.
  - Статус: **Повна ізоляція від Namencora**. 
  - Позиціонування: Прямий лістинг на Atom/Afternic як готові брендові імена для відповідних комерційних індустрій (клініки, рітейл, сервіси). Жодної штучної «алхімії» чи вигаданих протоколів.
- **Когорта B: Системні, обчислювальні та наукові активи (~100–150 доменів)**
  - Приклади: `Taxonology.com`, `BTreeIndex.com`, `ContextEmbedding.com`, `TradeoffCore.com`, `SubstrateFlow.com`.
  - Статус: **Фундамент лабораторії Namencora**.
  - Позиціонування: Канонічні кореневі ідентифікатори (Namespace Anchors) для архітектурних специфікацій, верифікованих патернів та інтерфейсних контрактів.

## 3. Дослідницькі треки (Working Groups / Divisions)
Активи Когорти B публікуються виключно в межах спеціалізованих інженерних напрямів (модель W3C / Apache):

### Division 01: Storage Engines & Memory Topologies
- **Фокус:** Архітектури баз даних, індексація, сторінкове читання, zero-copy буфери.
- **Активи:** `BTreeIndex.com`, `ContextEmbedding.com`, `SubstrateFlow.com`, `Enumeros.com` / `Enumerat.com`.

### Division 02: Cognitive & Ontological Systems
- **Фокус:** Машинні онтології, класифікація знань, векторні простори та семантичні графи.
- **Активи:** `Taxonology.com`, `TaxonMatrix.com`, `SemanticAnalysisTools.com`, `SemaIntegral.com`.

### Division 03: Systems Governance & Consensus
- **Фокус:** Розподілений консенсус, кворуми, контури вето та архітектурні компроміси.
- **Активи:** `TradeoffCore.com`, `EdgeVeto.com`, `VetoLoop.com`, `VetoPilot.com`, `SyncroOps.com`.

### Division 04: Applied Dynamics & Hardware Interfaces
- **Фокус:** Сигнальні процесори, фазовий аналіз, шини введення-виведення, обчислювальна геометрія.
- **Активи:** `IOArm.com`, `PhaseGradient.com`, `SurfaceWarper.com`, `Dioptrex.com`, `XrayChip.com`.

### Division 05: Execution Pipelines & Streaming Runtimes
- **Фокус:** Мікрорушії виконання та високошвидкісні конвеєри передачі даних.
- **Активи:** Серія `Vim*` (`VimIndex`, `VimUnit`, `VimNeural`), серія `Flow*` (`PistonFlow`, `TorridFlow`).

## 4. Інженерний фільтр валідації (Anti-Alchemy RFC)
Кожна специфікація повинна:
1. Вирішувати фізичну проблему системи (I/O bottleneck, memory contention, write amplification).
2. Містити синтаксично валідний контракт (gRPC, Protobuf, struct).
3. Фіксувати архітектурні обмеження та компроміси (Trade-offs & Constraints).

## 5. Дворівнева ізоляція середовищ (Air-Gapped Architecture)
Контури R&D та Production функціонують як паралельні, фізично розімкнені структури:
- **Внутрішній контур (Local Obsidian Vault):**
  - Призначення: Глибинний синтез, семантичний бекенд, повний обсяг портфеля, скорингові оцінки (TAS), чорнові зв'язки графа знань та стратегічні нотатки.
  - Режим доступу: Суворо локальний, автономний, закритий від публічної мережі.
- **Зовнішній контур (Public Git / Cloudflare Edge):**
  - Призначення: Тільки затверджені, дистильовані та фінально валідовані інженерні артефакти (чисті HTML, RFC-документи, Schema.org).
  - Режим доступу: Публічне джерело істини для інженерів, агентів та краулерів.
- **Заборона автоматичної наскрізної синхронізації:**
  - Будь-який перенос знань із Obsidian у публічний репозиторій є дискретною операцією ручної інженерної вибірки. Спроби побудови авто-паблішингу або прямого дзеркалювання заборонені для запобігання витоку внутрішнього контексту.
