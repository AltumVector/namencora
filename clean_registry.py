import os
import re

base_dir = os.path.expanduser("~/DataHub/02_Knowledge/Namencora/02_Entities")
if not os.path.isdir(base_dir):
    base_dir = os.path.abspath("02_Entities")

print(f"• Опрацювання каталогу: {base_dir}")

total = 0
updated = 0

for root, _, files in os.walk(base_dir):
    for file in files:
        if not file.endswith(".md"):
            continue
        filepath = os.path.join(root, file)
        total += 1

        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        orig_content = content

        fm_match = re.search(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
        if not fm_match:
            continue
        fm_text = fm_match.group(1)

        sub_m = re.search(r'^[ \t]*subsystem:\s*["\']?(.*?)["\']?\s*$', fm_text, re.MULTILINE)
        cat_m = re.search(r'^[ \t]*category:\s*["\']?(.*?)["\']?\s*$', fm_text, re.MULTILINE)
        div_m = re.search(r'^[ \t]*division:\s*["\']?(.*?)["\']?\s*$', fm_text, re.MULTILINE)
        type_m = re.search(r'^[ \t]*type:\s*["\']?(.*?)["\']?\s*$', fm_text, re.MULTILINE)
        name_m = re.search(r'^[ \t]*namespace:\s*["\']?(.*?)["\']?\s*$', fm_text, re.MULTILINE)

        raw_sub = sub_m.group(1).strip() if sub_m else ""
        raw_cat = cat_m.group(1).strip() if cat_m else ""
        division = div_m.group(1).strip() if div_m else ""
        ent_type = type_m.group(1).strip() if type_m else "entity"
        name = name_m.group(1).strip() if name_m else file.replace("Entity — ", "").replace(".md", "")

        # 1. Очищення префіксів і постфіксів
        clean_sub = re.sub(r'^\s*\d+[\.\)]\s*', '', raw_sub).strip(' \t\n\r":\'')
        clean_cat = re.sub(r'[:\.\s]+$', '', raw_cat).strip(' \t\n\r":\'')
        clean_cat = re.sub(r'^\s*\d+[\.\)]\s*', '', clean_cat)

        # 2. Пакетна заміна артефактів по всьому тексту (JSON, таблиці, цитати)
        if raw_sub and raw_sub != clean_sub:
            content = content.replace(raw_sub, clean_sub)
        if raw_cat and raw_cat != clean_cat:
            content = content.replace(raw_cat, clean_cat)

        if clean_sub:
            content = re.sub(r'^[ \t]*subsystem:\s*.*$', f'subsystem: "{clean_sub}"', content, flags=re.MULTILINE)
        if clean_cat:
            content = re.sub(r'^[ \t]*category:\s*.*$', f'category: "{clean_cat}"', content, flags=re.MULTILINE)

        # Прибираємо кінцеву двокрапку в блоці Subsystem
        content = re.sub(r'^([ \t]*>?\s*\*{0,2}Subsystem\*{0,2}:?\s*.*?)[:\s]+$', r'\1', content, flags=re.MULTILINE)

        # 3. Англомовний опис за замовчуванням (Human Layer)
        if ent_type == "alias":
            if "aidronops" in name.lower() and "aidronsops" not in name.lower():
                eng_desc = "Deterministic defensive namespace mirror (singular form) for the canonical AiDronesOps specification. Acts as a tier-1 defensive alias to resolve phonetic collisions and routing ambiguities during operational dispatch."
            elif "aidronsops" in name.lower():
                eng_desc = "Deterministic defensive namespace mirror (plural form) for the canonical AiDronesOps specification. Preserves namespace integrity and provides fault-tolerant request resolution across autonomous agent fleet operations."
            else:
                eng_desc = f"Deterministic defensive namespace mirror for canonical target entity. Guarantees fault-tolerant request resolution and prevents naming collisions across {clean_sub}."
        else:
            div_num = ""
            m = re.search(r'Division\s*(\d+)', division, re.IGNORECASE)
            if m:
                div_num = m.group(1)

            if div_num in ["00", "0"]:
                eng_desc = f"Foundational protocol primitive for the {clean_sub} subsystem (category: {clean_cat}). Enforces core consensus invariants, state execution models, and deterministic coordination boundaries."
            elif div_num in ["01", "1"]:
                eng_desc = f"Distributed persistence and storage tier primitive for the {clean_sub} subsystem (category: {clean_cat}). Enforces deterministic state retention, cache coherency, and transactional replication topologies."
            elif div_num in ["02", "2"]:
                eng_desc = f"Ontological and cognitive semantic primitive for the {clean_sub} subsystem (category: {clean_cat}). Enforces deterministic knowledge normalization, graph relational structures, and conceptual topologies."
            elif div_num in ["03", "3"]:
                eng_desc = f"Architectural governance and control primitive for the {clean_sub} subsystem (category: {clean_cat}). Implements deterministic transaction arbitration, circuit breaking mechanisms, and consensus policy balancing."
            elif div_num in ["04", "4"]:
                eng_desc = f"Execution runtime and interface boundary primitive for the {clean_sub} subsystem (category: {clean_cat}). Governs secure ingress validation, schema transformation, and low-latency interaction protocols."
            elif div_num in ["05", "5"]:
                eng_desc = f"Distributed systems and infrastructure primitive for the {clean_sub} subsystem (category: {clean_cat}). Coordinates high-throughput asynchronous pipelines, node synchronization, and fault-tolerant telemetry."
            else:
                eng_desc = f"Formal architectural primitive for the {clean_sub} subsystem (category: {clean_cat}). Provides standardized nomenclature, machine-verifiable contracts, and deterministic namespace routing within Namencora."

        # Заміна тіла Розділу 1
        s1_pattern = r'(## 1\. Technical Definition \(Human Layer\)\s*\n\n)(.*?)(\n\s*---\s*\n\s*## 2\. Machine Contract)'
        if re.search(s1_pattern, content, re.DOTALL):
            content = re.sub(s1_pattern, f'\\g<1>{eng_desc}\\g<3>', content, flags=re.DOTALL)
        else:
            s1_alt = r'(## 1\. Technical Definition \(Human Layer\)\s*\n+)(.*?)(\n+## 2\. Machine Contract)'
            if re.search(s1_alt, content, re.DOTALL):
                content = re.sub(s1_alt, f'\\g<1>{eng_desc}\n\n---\n\n\\g<3>', content, flags=re.DOTALL)

        # 4. Нормалізація рядка опису в Schema.org JSON
        if clean_cat:
            content = re.sub(
                r'("description":\s*")[^"]*(")',
                f'\\g<1>Formal architectural primitive for {clean_cat.lower()}.\\g<2>',
                content
            )

        if content != orig_content:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            updated += 1

print(f"• Оброблено карток: {total}")
print(f"• Оновлено та переведено на англійську: {updated}")
