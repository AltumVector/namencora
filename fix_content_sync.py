import os
import re

base_dir = os.path.expanduser("~/DataHub/02_Knowledge/Namencora")
entities_dir = os.path.join(base_dir, "02_Entities")

# Специфічні корекції назв файлів, якщо десь залишився неточний регістр
FILENAME_FIXES = {
    "Entity — MlopsCore.md": "Entity — MlOpsCore.md",
    "Entity — Aidronesops.md": "Entity — AidronesOps.md",
    "Entity — Aidronops.md": "Entity — AidronOps.md",
    "Entity — Aidronsops.md": "Entity — AidronsOps.md"
}

# 1. Виправляємо імена файлів на диску (безпечно через tmp для macOS APFS)
for root, dirs, files in os.walk(entities_dir):
    for f in files:
        if f in FILENAME_FIXES:
            target_fname = FILENAME_FIXES[f]
            src = os.path.join(root, f)
            tmp = os.path.join(root, f"tmp_{target_fname}")
            dst = os.path.join(root, target_fname)
            os.rename(src, tmp)
            os.rename(tmp, dst)
            print(f"• Файл перейменовано: {f} -> {target_fname}")

# 2. Синхронізуємо вміст усіх 341 карток із назвою файлу
fixed_content_count = 0

for root, dirs, files in os.walk(entities_dir):
    for f in sorted(files):
        if f.startswith("Entity — ") and f.endswith(".md"):
            canonical_name = f.replace("Entity — ", "").replace(".md", "")
            file_path = os.path.join(root, f)
            
            with open(file_path, "r", encoding="utf-8") as fp:
                content = fp.read()
            
            old_content = content
            
            # Оновлюємо namespace, name та заголовок H1
            content = re.sub(r'(\bnamespace:\s*)([^\r\n]+)', rf'\g<1>{canonical_name}', content)
            content = re.sub(r'(\bname:\s*)([^\r\n]+)', rf'\g<1>{canonical_name}', content)
            content = re.sub(r'(^\s*#\s+)([^\r\n]+)', rf'\g<1>{canonical_name}', content, flags=re.MULTILINE)
            content = re.sub(r'("@type":\s*"DefinedTerm",\s*"name":\s*")[^"]+(")', rf'\g<1>{canonical_name}\g<2>', content)
            content = re.sub(r'("name":\s*")[^"]+("(?=,\s*"inDefinedTermSet"))', rf'\g<1>{canonical_name}\g<2>', content)
            
            if content != old_content:
                with open(file_path, "w", encoding="utf-8") as fp:
                    fp.write(content)
                print(f"  ✓ Синхронізовано метадані всередині: {canonical_name}")
                fixed_content_count += 1

print(f"\n[Готово] Оновлено вміст карток: {fixed_content_count}")
