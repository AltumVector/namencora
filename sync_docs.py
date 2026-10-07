#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Namencora Documentation Sync & Dynamic Registry Generator
Deterministic pipeline: Entity scanning -> Dynamic topology -> Starlight sync -> Sitemap
"""

import os
import shutil
import re
from datetime import datetime

src_root = "02_Entities"
dest_root = "src/content/docs"

DIV_MAPPING = {
    "Division 00": "d00",
    "Division 01": "d01",
    "Division 02": "d02",
    "Division 03": "d03",
    "Division 04": "d04",
    "Division 05": "d05",
    "Division 06": "d06",
}

DIV_FOCUS = {
    "Division 00": "Core Protocols & Zero-Copy Primitives",
    "Division 01": "Storage Engines & Memory Topologies",
    "Division 02": "Cognitive & Ontological Systems",
    "Division 03": "Systems Governance & Consensus",
    "Division 04": "Computational Physics & Dynamics",
    "Division 05": "Execution Pipelines & Streaming Runtimes",
    "Division 06": "Computational Dynamics & Metrology",
}

def resolve_div_source(folder_name, slug):
    p1 = os.path.join(src_root, folder_name)
    if os.path.exists(p1) and os.path.isdir(p1):
        return p1
    p2 = os.path.join(src_root, slug)
    if os.path.exists(p2) and os.path.isdir(p2):
        return p2
    return None

def sync_all():
    os.makedirs(dest_root, exist_ok=True)

    # 1. Сканування та підрахунок карток
    counts = {}
    for folder_name, slug in DIV_MAPPING.items():
        src_dir = resolve_div_source(folder_name, slug)
        if src_dir:
            count = sum(
                1 for f in os.listdir(src_dir)
                if f.endswith(".md") and not f.startswith("index") and not f.startswith(".")
            )
            counts[folder_name] = count
        else:
            counts[folder_name] = 0

    total_entities = sum(counts.values())

    # 2. Динамічна генерація таблиці топології
    topology_rows = []
    for folder_name, slug in DIV_MAPPING.items():
        focus = DIV_FOCUS.get(folder_name, "Canonical Registry")
        count = counts.get(folder_name, 0)
        topology_rows.append(f"| **{folder_name}** | {focus} | {count} |")

    topology_table_str = "\n".join(topology_rows)

    # 3. Генерація landing page (index.md)
    index_content = f"""---
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
| :--- | :--- | :--- |
{topology_table_str}
| **Total Canonical Entities** | **Deterministic Architectural Standard** | **{total_entities}** |
"""

    with open(os.path.join(dest_root, "index.md"), "w", encoding="utf-8") as f:
        f.write(index_content.strip() + "\n")

    # 4. Сторінка Governance
    gov_src = "00_Meta/Registry_Governance.md"
    if os.path.exists(gov_src):
        with open(gov_src, "r", encoding="utf-8") as f:
            gov_txt = f.read()
        if not gov_txt.startswith("---"):
            gov_txt = "---\ntitle: \"Registry Governance\"\n---\n\n" + gov_txt
        with open(os.path.join(dest_root, "governance.md"), "w", encoding="utf-8") as f:
            f.write(gov_txt)

    # 5. Синхронізація та нормалізація карток у каталог Starlight
    synced_total = 0
    for folder_name, slug in DIV_MAPPING.items():
        src_dir = resolve_div_source(folder_name, slug)
        target_div = os.path.join(dest_root, slug)

        if os.path.exists(target_div):
            shutil.rmtree(target_div)
        os.makedirs(target_div, exist_ok=True)

        if not src_dir:
            continue

        for fname in sorted(os.listdir(src_dir)):
            if not fname.endswith(".md") or fname.startswith("index") or fname.startswith("."):
                continue

            in_file = os.path.join(src_dir, fname)
            with open(in_file, "r", encoding="utf-8") as f:
                content = f.read()

            # Отримуємо назву сутності без префікса Entity
            clean_base = re.sub(r'^[Ee]ntity\s*[-–—]\s*', '', fname[:-3]).strip()

            ns_m = re.search(r"^namespace:\s*([^\r\n]+)", content, re.MULTILINE)
            code_m = re.search(r"^term_code:\s*([^\r\n]+)", content, re.MULTILINE)

            ns = ns_m.group(1).strip() if ns_m else clean_base
            code = code_m.group(1).strip() if code_m else ""
            clean_title = f"{ns} ({code})" if code else ns

            # Нормалізуємо frontmatter для Astro
            if content.startswith("---"):
                parts = content.split("---", 2)
                fm = parts[1]
                body = parts[2] if len(parts) > 2 else ""
            else:
                # Обробка випадку, коли початковий '---' пропущено, але є закриваючий '---' або '--->'
                match = re.search(r'\n---(>)?\s*', content)
                if match:
                    idx = match.start()
                    fm = content[:idx]
                    body = content[match.end():]
                    if match.group(1):
                        body = "> " + body
                else:
                    fm = ""
                    body = content

            if "title:" not in fm:
                fm = f"\ntitle: \"{clean_title}\"\n" + fm.lstrip()

            # Прибираємо можливий дубль H1 з тіла документа
            body = re.sub(r'^\s*#\s+[^\r\n]+\r?\n+', '', body)
            new_content = f"---{fm}---\n\n{body.lstrip()}"

            # Формуємо безпечне веб-ім'я (entity--name.md)
            safe_slug = re.sub(r'[\s_–—]+', '-', clean_base).strip('-').lower()
            safe_fname = f"entity--{safe_slug}.md"

            out_file = os.path.join(target_div, safe_fname)
            with open(out_file, "w", encoding="utf-8") as f:
                f.write(new_content)
            synced_total += 1

    print(f"• Синхронізовано {synced_total} карток у каталог Starlight (дублювання H1 прибрано)")

def generate_sitemap():
    dist_dir = "dist"
    base_url = "https://namencora.com"
    if not os.path.exists(dist_dir):
        return

    pages = []
    for root, _, files in os.walk(dist_dir):
        for file in files:
            if file == "index.html":
                rel = os.path.relpath(root, dist_dir)
                url = f"{base_url}/" if rel == "." else f"{base_url}/{rel}/"
                pages.append(url)

    now = datetime.now().strftime("%Y-%m-%d")
    xml_lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
    ]
    for url in sorted(pages):
        xml_lines.append(f'  <url><loc>{url}</loc><lastmod>{now}</lastmod><changefreq>weekly</changefreq></url>')
    xml_lines.append('</urlset>')

    with open(os.path.join(dist_dir, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write("\n".join(xml_lines) + "\n")
    print(f"• sitemap.xml згенеровано ({len(pages)} URL)")

if __name__ == "__main__":
    sync_all()