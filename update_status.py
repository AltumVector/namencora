import os
import re

dirs = [
    os.path.expanduser("~/DataHub/02_Knowledge/Namencora/02_Entities"),
    os.path.abspath("02_Entities"),
    os.path.abspath(".")
]

target_dir = next((d for d in dirs if os.path.isdir(d)), ".")
print(f"• Опрацювання каталогу: {target_dir}")

total = 0
updated = 0

for root, _, files in os.walk(target_dir):
    for f in files:
        if not f.endswith(".md"):
            continue
        total += 1
        p = os.path.join(root, f)
        with open(p, "r", encoding="utf-8") as file:
            content = file.read()

        if "Specification Status" in content:
            continue

        is_alias = bool(re.search(r'^[ \t]*type:\s*["\']?alias["\']?', content, re.MULTILINE | re.IGNORECASE))
        status_val = "Defensive Alias / Routing Mirror" if is_alias else "Canonical Specification (Active)"
        status_row = f"| Specification Status | {status_val} |"

        new_content = None

        # 1. Спроба вставити після Execution Model (для канонічних)
        if re.search(r'\|\s*\*?\*?Execution Model\*?\*?', content):
            new_content = re.sub(
                r'(\|\s*\*?\*?Execution Model\*?\*?[^\n]+)',
                rf'\1\n{status_row}',
                content,
                count=1
            )
        # 2. Спроба вставити після Canonical URI (для аліасів або скорочених специфікацій)
        elif re.search(r'\|\s*\*?\*?Canonical URI\*?\*?', content):
            new_content = re.sub(
                r'(\|\s*\*?\*?Canonical URI\*?\*?[^\n]+)',
                rf'\1\n{status_row}',
                content,
                count=1
            )
        # 3. Універсальна вставка останнім рядком таблиці Розділу 3
        elif "## 3. Architectural Properties" in content:
            parts = content.split("## 3. Architectural Properties", 1)
            rows = list(re.finditer(r'\n[ \t]*\|[^\n]+\|', parts[1]))
            if rows:
                last_match = rows[-1]
                idx = last_match.end()
                sec3 = parts[1][:idx] + f"\n{status_row}" + parts[1][idx:]
                new_content = parts[0] + "## 3. Architectural Properties" + sec3

        if new_content and new_content != content:
            with open(p, "w", encoding="utf-8") as file:
                file.write(new_content)
            updated += 1

print(f"• Всього карток перевірено: {total}")
print(f"• Оновлено (додано рядок): {updated}")
