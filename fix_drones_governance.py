import os
import re
import json

base_dir = os.path.expanduser("~/DataHub/02_Knowledge/Namencora/02_Entities/Division 03")

# 1. Оновлення головного примітиву AiDronesOps
main_drone_path = os.path.join(base_dir, "Entity — AiDronesOps.md")
if os.path.exists(main_drone_path):
    with open(main_drone_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    content = re.sub(r'category:\s*"?[^"\r\n]+"?', 'category: "Autonomous Fleet Governance / Drone Operations Policy"', content)
    content = re.sub(r'(>\s*\*\*Subsystem\*\*:\s*)[^\r\n]+', r'\g<1>Systems Governance / Autonomous Fleet Governance', content)
    content = re.sub(
        r'## 1\. Technical Definition \(Human Layer\)[\s\S]*?---',
        '## 1. Technical Definition (Human Layer)\n\nКеруючий примітив та контур безпеки автономних польотних місій. Забезпечує детерміновану верифікацію польотних регламентів, авторизацію доступу дронів до повітряних коридорів та координацію операційних ролей.\n\n---',
        content
    )
    with open(main_drone_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("✓ Оновлено: AiDronesOps (встановлено категорію Autonomous Fleet Governance)")

# 2. Оновлення захисних активів AiDronOps та AiDronsOps
typo_specs = [
    {
        "old_file": "Entity — AidronOps.md",
        "new_name": "AiDronOps",
        "domain": "aidronops.com",
        "code": "D03-GOV-081",
        "raw": "aidronops",
        "desc_ua": "Фонетичний захисний примітив (Defensive Namespace Asset) та контур детермінованого перенаправлення трафіку для специфікації AiDronesOps. Мінімізує колізії маршрутизації та захищає простір імен автономного флоту."
    },
    {
        "old_file": "Entity — AidronsOps.md",
        "new_name": "AiDronsOps",
        "domain": "aidronsops.com",
        "code": "D03-GOV-082",
        "raw": "aidronsops",
        "desc_ua": "Фонетичний захисний примітив (Defensive Namespace Asset) множинної форми для специфікації AiDronesOps. Забезпечує цілісність семантичного простору імен та відмовостійку резолюцію адресації."
    }
]

for item in typo_specs:
    src_file = os.path.join(base_dir, item["old_file"])
    dst_file = os.path.join(base_dir, f"Entity — {item['new_name']}.md")
    tmp_file = os.path.join(base_dir, f"tmp_{item['new_name']}.md")
    
    if os.path.exists(src_file):
        with open(src_file, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Оновлюємо метадані
        content = re.sub(r'namespace:\s*[^\r\n]+', f'namespace: {item["new_name"]}', content)
        content = re.sub(r'name:\s*[^\r\n]+', f'name: {item["new_name"]}', content)
        content = re.sub(r'category:\s*"?[^"\r\n]+"?', 'category: "Defensive Namespace Resolution / Phonetic Collision Guard"', content)
        content = re.sub(r'#\s+[^\r\n]+', f'# {item["new_name"]}', content)
        content = re.sub(r'("name":\s*")[^"]+(")', rf'\g<1>{item["new_name"]}\g<2>', content)
        content = re.sub(r'(>\s*\*\*Subsystem\*\*:\s*)[^\r\n]+', r'\g<1>Systems Governance / Defensive Namespace Resolution', content)
        
        # Оновлюємо технічний опис
        content = re.sub(
            r'## 1\. Technical Definition \(Human Layer\)[\s\S]*?---',
            f'## 1. Technical Definition (Human Layer)\n\n{item["desc_ua"]}\n\n---',
            content
        )
        
        with open(src_file, "w", encoding="utf-8") as f:
            f.write(content)
            
        os.rename(src_file, tmp_file)
        os.rename(tmp_file, dst_file)
        print(f"✓ Оновлено та перейменовано: {item['old_file']} -> Entity — {item['new_name']}.md")
