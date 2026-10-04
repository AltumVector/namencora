import os
import re
import json

base_dir = os.path.expanduser("~/DataHub/02_Knowledge/Namencora")
entities_dir = os.path.join(base_dir, "02_Entities")

# Словник усіх семантичних блоків у реєстрі (сортуємо від найдовших до найкоротших)
TOKENS = sorted([
    # Префікси та корені
    "Aegis", "Essence", "Gnosis", "Grid", "Morse", "Agent", "Arka", "Caph", 
    "Cerber", "Cryo", "Distill", "Edge", "Bastion", "Ballistic", "Altum", 
    "Context", "Drift", "Ingest", "Index", "Eta", "Know", "Memory", "Monada", 
    "Pheno", "Phire", "Prax", "Tur", "Vector", "BTree", "Vim", "Xray", "Axio", 
    "Ax", "Nano", "Micro", "Hyper", "Cyber", "Zero", "One", "Bit", "Byte", 
    "Data", "Quantum", "Chrono", "Agi", "Aidron", "Aidrons", "Mute", "Ops", 
    "Gs", "Llm", "Ml", "Ai",
    # Суфікси та компоненти систем
    "Synchrony", "Syncos", "Mechanism", "Tradeoffs", "Tradeoff", "Embedding", 
    "Signal", "Optic", "Audit", "Proof", "Chain", "Cloud", "Veto", "Brain", 
    "Cipher", "Code", "Logic", "Matrix", "Neural", "Schema", "Stack", "Tensor", 
    "Torch", "Trace", "Vault", "Volt", "Wall", "Pipe", "Naut", "Phore", "Vect", 
    "Visor", "Vizer", "Spark", "Unit", "Tick", "Sona", "Safe", "Trax", "Node", 
    "Core", "Mesh", "Flow", "Grid", "Gate", "Tree", "Pool", "Queue", "Stream", 
    "State", "Model", "Bench", "Scale", "Scope", "Pulse", "Space", "Plane", 
    "Field", "Frame", "Graph", "Chart", "Draft", "Spec", "Sync", "Chip", "Hub", 
    "Sor", "Xor", "Vex", "Trx", "Zor", "Pix", "Que", "Apix", "Io"
], key=lambda x: len(x), reverse=True)

# Точні заміни для складних/трискладових випадків
EXACT_OVERRIDES = {
    "agisyncos": "AgiSyncOs",
    "aidronops": "AidronOps",
    "aidronsops": "AidronsOps",
    "arkaops": "ArkaOps",
    "caphops": "CaphOps",
    "distillops": "DistillOps",
    "essenceaudit": "EssenceAudit",
    "gnosisaudit": "GnosisAudit",
    "gridsynchrony": "GridSynchrony",
    "gschainsync": "GsChainSync",
    "llmopscloud": "LlmOpsCloud",
    "llmopshub": "LlmOpsHub",
    "mlopscore": "MlopsCore",
    "monadaops": "MonadaOps",
    "morsesync": "MorseSync",
    "muteops": "MuteOps",
    "opsapix": "OpsApix",
    "opschip": "OpsChip",
    "opsmechanism": "OpsMechanism",
    "opsque": "OpsQue",
    "cryopsy": "CryoPsy",
    "aegisoptic": "AegisOptic",
}

def decompose(name):
    lower = name.lower()
    if lower in EXACT_OVERRIDES:
        return EXACT_OVERRIDES[lower]
        
    # Якщо вже містить 2+ великі літери
    caps = [c for c in name if c.isupper()]
    if len(caps) >= 2:
        return name

    # Жадібний пошук токенів
    rem = lower
    matched = []
    while rem:
        found = False
        for tok in TOKENS:
            if rem.startswith(tok.lower()):
                matched.append(tok)
                rem = rem[len(tok):]
                found = True
                break
        if not found:
            # Залишок, який не розпізнано
            matched.append(rem.capitalize())
            break
            
    res = "".join(matched)
    return res if len([c for c in res if c.isupper()]) >= 2 else name

updated_count = 0
recase_map = {}
single_cap_remains = []

for root, dirs, files in os.walk(entities_dir):
    for f in sorted(files):
        if f.startswith("Entity — ") and f.endswith(".md"):
            old_name = f.replace("Entity — ", "").replace(".md", "")
            new_name = decompose(old_name)
            
            # Якщо все ще має лише 1 велику літеру
            if len([c for c in new_name if c.isupper()]) < 2:
                single_cap_remains.append(new_name)

            if old_name != new_name:
                recase_map[old_name] = new_name
                file_path = os.path.join(root, f)
                
                with open(file_path, "r", encoding="utf-8") as fp:
                    content = fp.read()
                
                # Оновлюємо внутрішні поля
                content = re.sub(rf"namespace:\s*{re.escape(old_name)}", f"namespace: {new_name}", content)
                content = re.sub(rf"name:\s*{re.escape(old_name)}", f"name: {new_name}", content)
                content = re.sub(rf"#\s+{re.escape(old_name)}", f"# {new_name}", content)
                content = re.sub(rf'"name":\s*"{re.escape(old_name)}"', f'"name": "{new_name}"', content)
                
                with open(file_path, "w", encoding="utf-8") as fp:
                    fp.write(content)
                
                # Перейменування файлу через тимчасове ім'я (APFS Safe)
                new_file = f"Entity — {new_name}.md"
                new_file_path = os.path.join(root, new_file)
                tmp_file_path = os.path.join(root, f"tmp_rec_{new_file}")
                
                os.rename(file_path, tmp_file_path)
                os.rename(tmp_file_path, new_file_path)
                
                print(f"  • {old_name:<18} -> {new_name}")
                updated_count += 1

print(f"\n[Успішно] Додатково переведено в PascalCase: {updated_count}")

if single_cap_remains:
    print(f"\n[Контроль] Залишились сутності з одним словом ({len(single_cap_remains)}):")
    for item in sorted(set(single_cap_remains)):
        print(f"  ? {item}")
else:
    print("\n[Ідеально] Усі 341 сутність тепер мають детермінований PascalCase!")
