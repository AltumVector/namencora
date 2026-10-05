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
        filepath = os.path.join(root, f)
        with open(filepath, "r", encoding="utf-8") as file:
            content = file.read()

        if '<script type="application/ld+json">' in content:
            continue

        # Шукаємо блок коду JSON у Розділі 2
        match = re.search(r'(```(?:json)?\s*\n)(\{[\s\S]*?"@context"[\s\S]*?\})(\n\s*```)', content)
        if match:
            raw_json = match.group(2).strip()
            # Виправляємо випадкові залишкові одинарні лапки на подвійні
            raw_json = re.sub(r"'\s*$", '"', raw_json, flags=re.MULTILINE)
            
            script_block = f"\n\n<script type=\"application/ld+json\">\n{raw_json}\n</script>"
            
            # Вставляємо тег одразу після блоку ```
            end_pos = match.end()
            new_content = content[:end_pos] + script_block + content[end_pos:]

            with open(filepath, "w", encoding="utf-8") as file:
                file.write(new_content)
            updated += 1

print(f"• Всього перевірено карток: {total}")
print(f"• Впроваджено машинний тег JSON-LD: {updated}")
