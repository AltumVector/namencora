import os
import re
import json

base_dir = os.path.expanduser("~/DataHub/02_Knowledge/Namencora")
entities_dir = os.path.join(base_dir, "02_Entities")

# Словник відомих коренів та афіксів для детермінованого розбиття
KNOWN_PREFIXES = [
    "Assay", "Bastion", "Vim", "Xray", "Axio", "Ax", "Altum", "Cerber", 
    "Eta", "Drift", "Ingest", "Index", "Ballistic", "Ailab", "Nano", 
    "Micro", "Hyper", "Cyber", "Zero", "One", "Bit", "Byte", "Data"
]

KNOWN_SUFFIXES = [
    "Brain", "Cipher", "Code", "Io", "Ml", "Neural", "Node", "Safe", 
    "Schema", "Stack", "Trax", "Trx", "Logic", "Matrix", "Sona", "Sor", 
    "Spark", "Tensor", "Tick", "Torch", "Trace", "Unit", "Vault", 
    "Vector", "Vex", "Volt", "Wall", "Xor", "Pipe", "Index", "Cache", 
    "Embed", "Point", "Mesh", "Flow", "Grid", "Core", "Layer", "Base", 
    "Gate", "Route", "Sync", "Tree", "Pool", "Queue", "Stream", "State", 
    "Model", "Agent", "Proof", "Chain", "Link", "Bench", "Craft", "Forge", 
    "Shift", "Scale", "Drift", "Sweep", "Scope", "Pulse", "Space", "Plane", 
    "Field", "Frame", "Graph", "Chart", "Spec", "Draft", "Trade", "Tradeoff", 
    "Tradeoffs", "Naut", "Phore", "Vect", "Ora", "Rift", "Visor", "Vizer", 
    "Axio", "Ax", "Assay"
]

# Специфічні абревіатури
ACRONYMS = {
    "Io": "IO",
    "Ml": "ML",
    "Ai": "AI"
}

def split_to_pascal(name):
    # Якщо вже містить більше однієї великої літери (наприклад AltumVector, BTreeIndex)
    caps = [c for c in name if c.isupper()]
    if len(caps) > 1:
        # Перевірка на специфічні кінцівки (наприклад AssayIO)
        for old, new in ACRONYMS.items():
            if name.endswith(old) and not name.endswith(new):
                return name[:-len(old)] + new
        return name

    # Шукаємо збіг за префіксом
    for pref in sorted(KNOWN_PREFIXES, key=len, reverse=True):
        if name.lower().startswith(pref.lower()) and len(name) > len(pref):
            rest = name[len(pref):]
            for suff in sorted(KNOWN_SUFFIXES, key=len, reverse=True):
                if rest.lower() == suff.lower():
                    final_suff = ACRONYMS.get(suff, suff)
                    return pref + final_suff
            # Якщо точного суфіксу немає в списку, капіталізуємо залишок
            rest_cap = rest.capitalize()
            rest_cap = ACRONYMS.get(rest_cap, rest_cap)
            return pref + rest_cap

    return name

updated_count = 0
recase_map = {}

for root, dirs, files in os.walk(entities_dir):
    for f in sorted(files):
        if f.startswith("Entity — ") and f.endswith(".md"):
            old_name = f.replace("Entity — ", "").replace(".md", "")
            new_name = split_to_pascal(old_name)
            
            if old_name != new_name:
                recase_map[old_name] = new_name
                file_path = os.path.join(root, f)
                
                with open(file_path, "r", encoding="utf-8") as fp:
                    content = fp.read()
                
                # 1. Оновлюємо вміст картки
                content = re.sub(rf"namespace:\s*{re.escape(old_name)}", f"namespace: {new_name}", content)
                content = re.sub(rf"name:\s*{re.escape(old_name)}", f"name: {new_name}", content)
                content = re.sub(rf"#\s+{re.escape(old_name)}", f"# {new_name}", content)
                content = re.sub(rf'"name":\s*"{re.escape(old_name)}"', f'"name": "{new_name}"', content)
                
                with open(file_path, "w", encoding="utf-8") as fp:
                    fp.write(content)
                
                # 2. Безпечне перейменування файлу для macOS APFS
                new_file = f"Entity — {new_name}.md"
                new_file_path = os.path.join(root, new_file)
                tmp_file_path = os.path.join(root, f"tmp_{new_file}")
                
                os.rename(file_path, tmp_file_path)
                os.rename(tmp_file_path, new_file_path)
                
                print(f"  • {old_name:<18} -> {new_name}")
                updated_count += 1

print(f"\n[Успішно] Оновлено сутностей до PascalCase: {updated_count}")

# 3. Оновлення registry.json та llm.txt, якщо вони існують
reg_json_path = os.path.join(base_dir, "реестр.json")
if not os.path.exists(reg_json_path):
    reg_json_path = os.path.join(base_dir, "registry.json")

if os.path.exists(reg_json_path):
    with open(reg_json_path, "r", encoding="utf-8") as fp:
        reg_data = json.load(fp)
    
    for item in reg_data.get("entities", []):
        old_ns = item.get("namespace", "")
        if old_ns in recase_map:
            item["namespace"] = recase_map[old_ns]
            if "schema_org" in item and "name" in item["schema_org"]:
                item["schema_org"]["name"] = recase_map[old_ns]
                
    with open(reg_json_path, "w", encoding="utf-8") as fp:
        json.dump(reg_data, fp, indent=2, ensure_ascii=False)
    print("• Синхронізовано registry.json")

llm_txt_path = os.path.join(base_dir, "llm.txt")
if os.path.exists(llm_txt_path):
    with open(llm_txt_path, "r", encoding="utf-8") as fp:
        llm_content = fp.read()
    for old_ns, new_ns in recase_map.items():
        llm_content = re.sub(rf"\b{re.escape(old_ns)}\b", new_ns, llm_content)
    with open(llm_txt_path, "w", encoding="utf-8") as fp:
        fp.write(llm_content)
    print("• Синхронізовано llm.txt")
