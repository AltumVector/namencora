import os
import re

dirs = [
    os.path.expanduser("~/DataHub/02_Knowledge/Namencora/02_Entities"),
    os.path.abspath("02_Entities"),
    os.path.abspath(".")
]

target_dir = next((d for d in dirs if os.path.isdir(d)), ".")
print(f"• Обработка каталога: {target_dir}")

total = 0
updated = 0

pattern = re.compile(r'"inDefinedTermSet":\s*"([^"]+)"')

for root, _, files in os.walk(target_dir):
    for f in files:
        if not f.endswith(".md"):
            continue
        total += 1
        filepath = os.path.join(root, f)
        with open(filepath, "r", encoding="utf-8") as file:
            content = file.read()

        if pattern.search(content):
            new_content = pattern.sub(
                r'"inDefinedTermSet": {\n    "@type": "DefinedTermSet",\n    "name": "\1"\n  }',
                content
            )
            if new_content != content:
                with open(filepath, "w", encoding="utf-8") as file:
                    file.write(new_content)
                updated += 1

print(f"• Всего проверено файлов: {total}")
print(f"• Обновлено контрактов Schema.org: {updated}")
