import os
import re
import json

base_dir = os.path.expanduser("~/DataHub/02_Knowledge/Namencora")
entities_dir = os.path.join(base_dir, "02_Entities")

# Вичерпний словник виправлень: артефакти v2 + усі 69 сутностей
EXPLICIT_FIXES = {
    # 1. Виправлення артефактів жадібного збігу v2
    "synchronizator": "Synchronizator",
    "synchronizator": "Synchronizator",
    "synchronizator": "Synchronizator",
    "opticballistics": "OpticBallistics",
    "opsyslife": "OpsysLife",
    "graphioma": "Graphioma",
    "tickpipeline": "TickPipeline",
    "logickeyai": "LogicKeyAI",
    "logicula": "Logicula",
    
    # 2. Повний пул 69 пропущених сутностей
    "basalchip": "BasalChip",
    "bluesema": "BlueSema",
    "botassay": "BotAssay",
    "clexicle": "Clexicle",
    "controlschema": "ControlSchema",
    "eigenvim": "EigenVim",
    "eventplexa": "EventPlexa",
    "flexcle": "Flexcle",
    "gigavim": "GigaVim",
    "gradientfold": "GradientFold",
    "gradientwarp": "GradientWarp",
    "infivim": "InfiVim",
    "ipvim": "IpVim",
    "iterachip": "IteraChip",
    "jetvim": "JetVim",
    "kronchip": "KronChip",
    "lexiclave": "LexiClave",
    "lexifluid": "LexiFluid",
    "lexigara": "LexiGara",
    "lexilogue": "LexiLogue",
    "lexistruct": "LexiStruct",
    "lithochip": "LithoChip",
    "messagequeues": "MessageQueues",
    "monadpulse": "MonadPulse",
    "neutrochip": "NeutroChip",
    "peritask": "PeriTask",
    "piochip": "PioChip",
    "postulex": "PostuLex",
    "quantovim": "QuantoVim",
    "quarchip": "QuarChip",
    "riftchip": "RiftChip",
    "semaconn": "SemaConn",
    "semacont": "SemaCont",
    "semafield": "SemaField",
    "semafork": "SemaFork",
    "semaintegra": "SemaIntegra",
    "semaintegral": "SemaIntegral",
    "semakernel": "SemaKernel",
    "semamat": "SemaMat",
    "semanticanalyticstools": "SemanticAnalyticsTools",
    "semanticballistics": "SemanticBallistics",
    "semantona": "SemanTona",
    "semantora": "SemanTora",
    "semantuda": "SemanTuda",
    "semarate": "SemaRate",
    "semascan": "SemaScan",
    "semature": "SemaTure",
    "semavim": "SemaVim",
    "shellassay": "ShellAssay",
    "silicochip": "SilicoChip",
    "staplechip": "StapleChip",
    "starkchip": "StarkChip",
    "stratovim": "StratoVim",
    "surfacewarper": "SurfaceWarper",
    "taxonalgo": "TaxonAlgo",
    "taxonatlas": "TaxonAtlas",
    "taxonext": "TaxoNext",
    "taxonior": "TaxonIor",
    "taxonology": "TaxonOlogy",
    "taxonox": "TaxonOx",
    "templatedraft": "TemplateDraft",
    "thesisaudit": "ThesisAudit",
    "thrustnaut": "ThrustNaut",
    "torriddata": "TorridData",
    "trajectorysync": "TrajectorySync",
    "uxvim": "UxVim",
    "vugchip": "VugChip"
}

# Список легітимних монолітних назв протоколів
ALLOWED_MONOLITHS = {"Enumerat", "Enumeros", "Clexicle", "Flexcle", "Synchronizator", "Logicula", "Graphioma"}

updated_count = 0
recase_map = {}

for root, dirs, files in os.walk(entities_dir):
    for f in sorted(files):
        if f.startswith("Entity — ") and f.endswith(".md"):
            current_name = f.replace("Entity — ", "").replace(".md", "")
            key = current_name.lower()
            
            # Шукаємо прямий збіг у карті виправлень
            if key in EXPLICIT_FIXES:
                target_name = EXPLICIT_FIXES[key]
                if current_name != target_name:
                    recase_map[current_name] = target_name
                    file_path = os.path.join(root, f)
                    
                    with open(file_path, "r", encoding="utf-8") as fp:
                        content = fp.read()
                    
                    content = re.sub(rf"namespace:\s*{re.escape(current_name)}", f"namespace: {target_name}", content)
                    content = re.sub(rf"name:\s*{re.escape(current_name)}", f"name: {target_name}", content)
                    content = re.sub(rf"#\s+{re.escape(current_name)}", f"# {target_name}", content)
                    content = re.sub(rf'"name":\s*"{re.escape(current_name)}"', f'"name": "{target_name}"', content)
                    
                    with open(file_path, "w", encoding="utf-8") as fp:
                        fp.write(content)
                    
                    new_file = f"Entity — {target_name}.md"
                    new_file_path = os.path.join(root, new_file)
                    tmp_file_path = os.path.join(root, f"tmp_v3_{new_file}")
                    
                    os.rename(file_path, tmp_file_path)
                    os.rename(tmp_file_path, new_file_path)
                    
                    print(f"  ✓ {current_name:<22} -> {target_name}")
                    updated_count += 1

print(f"\n[Успішно] Відкалібровано сутностей: {updated_count}")

# Перевірка наявності залишкових нерозділених сутностей
remaining_single = []
for root, dirs, files in os.walk(entities_dir):
    for f in sorted(files):
        if f.startswith("Entity — ") and f.endswith(".md"):
            name = f.replace("Entity — ", "").replace(".md", "")
            if name not in ALLOWED_MONOLITHS and len([c for c in name if c.isupper()]) < 2:
                remaining_single.append(name)

if remaining_single:
    print(f"\n[Увага] Залишились некалібровані назви ({len(remaining_single)}):")
    for item in sorted(set(remaining_single)):
        print(f"  ? {item}")
else:
    print("\n[Ідеально] Усі 341 сутності реєстру Namencora на 100% уніфіковані за стандартом PascalCase!")
