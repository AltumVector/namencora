import os
import shutil
import re
from datetime import datetime

src_root = "02_Entities"
dest_root = "src/content/docs"

div_mapping = {
    "Division 00": "d00",
    "Division 01": "d01",
    "Division 02": "d02",
    "Division 03": "d03",
    "Division 04": "d04",
    "Division 05": "d05",
    "Division 06": "d06",
}

os.makedirs(dest_root, exist_ok=True)

# 1. Головна сторінка порталу
index_content = """---
title: Namencora Systems & Nomenclature Registry
description: Deterministic architecture registry and canonical namespace ontology.
template: splash
hero:
  tagline: Deterministic specification registry for high-throughput distributed architectures, state primitives, and consensus topographies.
  actions:
    - text: Explore Division 00
      link: /d00/entity--enumeros/
      icon: right-arrow
      variant: primary
    - text: View GitHub Source
      link: https://github.com/AltumVector/namencora
      icon: external
      variant: minimal
---

## Canonical Topology

| Division | Domain Focus | Primitives |
| :--- | :--- | :---: |
| **Division 00** | Core Protocols & Zero-Copy Primitives | 2 |
| **Division 01** | Storage Engines & Memory Topologies | 42 |
| **Division 02** | Cognitive & Ontological Systems | 91 |
| **Division 03** | Systems Governance & Consensus | 67 |
| **Division 04** | Computational Physics & Dynamics | 45 |
| **Division 05** | Execution Pipelines & Streaming Runtimes | 94 |
| **Total Canonical Entities** | **Deterministic Architectural Standard** | **341** |
"""
with open(os.path.join(dest_root, "index.md"), "w", encoding="utf-8") as f:
    f.write(index_content.strip() + "\n")

# 2. Сторінка Governance
gov_src = "00_Meta/Registry_Governance.md"
if os.path.exists(gov_src):
    with open(gov_src, "r", encoding="utf-8") as f:
        gov_txt = f.read()
    if not gov_txt.startswith("---"):
        gov_txt = "---\ntitle: \"Registry Governance\"\n---\n\n" + gov_txt
    with open(os.path.join(dest_root, "governance.md"), "w", encoding="utf-8") as f:
        f.write(gov_txt)

# 3. Синхронізація 341 сутності
synced_total = 0
for div_folder, slug in div_mapping.items():
    div_path = os.path.join(src_root, div_folder)
    target_div = os.path.join(dest_root, slug)
    
    if os.path.exists(target_div):
        shutil.rmtree(target_div)
    os.makedirs(target_div, exist_ok=True)
    
    if not os.path.exists(div_path):
        continue
        
    for fname in sorted(os.listdir(div_path)):
        if fname.startswith("Entity — ") and fname.endswith(".md"):
            in_file = os.path.join(div_path, fname)
            with open(in_file, "r", encoding="utf-8") as f:
                content = f.read()
                
            ns_m = re.search(r"namespace:\s*([^\r\n]+)", content)
            code_m = re.search(r"term_code:\s*([^\r\n]+)", content)
            
            ns = ns_m.group(1).strip() if ns_m else fname.replace("Entity — ", "").replace(".md", "")
            code = code_m.group(1).strip() if code_m else ""
            
            clean_title = f"{ns} ({code})" if code else ns
            
            if content.startswith("---"):
                parts = content.split("---", 2)
                fm = parts[1]
                body = parts[2] if len(parts) > 2 else ""
                if "title:" not in fm:
                    fm = f"\ntitle: \"{clean_title}\"\n" + fm.lstrip()
                
                # ВИДАЛЯЄМО ДУБЛЬОВАНИЙ ЗАГОЛОВОК # З ТІЛА
                body = re.sub(r'^\s*#\s+[^\r\n]+\r?\n+', '', body)
                
                new_content = f"---{fm}---{body}"
            else:
                body = re.sub(r'^\s*#\s+[^\r\n]+\r?\n+', '', content)
                new_content = f"---\ntitle: \"{clean_title}\"\n---\n\n" + body
                
            safe_fname = fname.replace("Entity — ", "entity--").replace(" ", "-").lower()
            out_file = os.path.join(target_div, safe_fname)
            with open(out_file, "w", encoding="utf-8") as f:
                f.write(new_content)
            synced_total += 1

print(f"• Синхронізовано {synced_total} карток у каталог Starlight (дублювання H1 прибрано)")

def generate_sitemap():
    dist_dir = "dist"
    if not os.path.exists(dist_dir):
        return
    today = datetime.now().strftime("%Y-%m-%d")
    urls = [
        ("https://namencora.com/", "1.0"),
        ("https://namencora.com/governance/", "0.8")
    ]
    for div_folder, slug in div_mapping.items():
        target_div = os.path.join(dest_root, slug)
        if os.path.exists(target_div):
            for f in sorted(os.listdir(target_div)):
                if f.endswith(".md"):
                    page_slug = f.replace(".md", "")
                    urls.append((f"https://namencora.com/{slug}/{page_slug}/", "0.7"))
    
    xml_lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
    ]
    for url, prio in urls:
        xml_lines.append("  <url>")
        xml_lines.append(f"    <loc>{url}</loc>")
        xml_lines.append(f"    <lastmod>{today}</lastmod>")
        xml_lines.append(f"    <priority>{prio}</priority>")
        xml_lines.append("  </url>")
    xml_lines.append("</urlset>")
    
    out_path = os.path.join(dist_dir, "sitemap.xml")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(xml_lines))
    print(f"• [SEO] Успішно згенеровано {out_path} ({len(urls)} канонічних URL)")

if __name__ == "__main__":
    pass
