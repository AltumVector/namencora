import os
import re

dirs = [
    os.path.expanduser("~/DataHub/02_Knowledge/Namencora/02_Entities"),
    os.path.abspath("02_Entities"),
    os.path.abspath(".")
]

target_dir = next((d for d in dirs if os.path.isdir(d)), ".")
print(f"• Опрацювання карток у: {target_dir}")

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

        if re.search(r'\|\s*Execution Model\s*\|', content):
            new_content = re.sub(
                r'(\|\s*Execution Model\s*\|[^\n]+)',
                rf'\1\n| Specification Status | {status_val} |',
                content
            )
            if new_content != content:
                with open(p, "w", encoding="utf-8") as file:
                    file.write(new_content)
                updated += 1

print(f"• Всього перевірено карток: {total}")
print(f"• Додано Specification Status: {updated}")
