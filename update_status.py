import os

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

        if "Canonical Specification (Active)" in content:
            new_content = content.replace(
                "Canonical Specification (Active)",
                "Candidate Specification (Active Review)"
            )
            with open(p, "w", encoding="utf-8") as file:
                file.write(new_content)
            updated += 1

print(f"• Перевірено карток: {total}")
print(f"• Переведено в Candidate Specification: {updated}")
