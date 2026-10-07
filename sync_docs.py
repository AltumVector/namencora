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

# Базові шляхи репозиторію
src_root = "02_Entities"
dest_root = "src/content/docs"
meta_root = "00_Meta"

# Канонічний мапінг дивізіонів та їхній архітектурний фокус
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
    """Знаходить фізичний каталог дивізіону в 02_Entities."""
    p1 = os.path.join(src_root, folder_name)
    if os.path.exists(p1) and os.path.isdir(p1):
        return p1
    p2 = os.path.join(src_root, slug)
    if os.path.exists(p2) and os.path.isdir(p2):
        return p2
    return None


def clean_duplicate_h1(markdown_text):
    """
    Прибирає дублювання першого H1 (# Title), оскільки Starlight
    автоматично генерує заголовок сторінки з frontmatter 'title'.
    """
    if markdown_text.startswith("---"):
        parts = markdown_text.split("---", 2)
        if len(parts) >= 3:
            fm = parts[1]
            body = parts[2]
            cleaned_body = re.sub(r'^\s*#[ \t]+[^\n]*\n+', '', body, count=1)
            return f"---{fm}---{cleaned_body}"
    return re.sub(r'^\s*#[ \t]+[^\n]*\n+', '', markdown_text, count=1)


def sync_all():
    os.makedirs(dest_root, exist_ok=True)

    # -------------------------------------------------------------
    # 1. Сканування файлової системи та динамічний підрахунок
    # -------------------------------------------------------------
    division_counts = {}
    total_entities = 0

    for div_title in sorted(DIV_MAPPING.keys()):
        slug = DIV_MAPPING[div_title]
        src_dir = resolve_div_source(div_title, slug)
        count = 0
        if src_dir:
            count = len([
                f for f in os.listdir(src_dir)
                if f.endswith(".md") and not f.startswith("index") and not f.startswith("README")
            ])
        division_counts[div_title] = count
        total_entities += count

    # -------------------------------------------------------------
    # 2. Динамічна генерація таблиці Canonical Topology
    # -------------------------------------------------------------
    table_lines = [
        "| Division | Domain Focus | Primitives |",
        "| :--- | :--- | :---: |"
    ]
    for div_title in sorted(DIV_MAPPING.keys()):
        focus = DIV_FOCUS.get(div_title, "Canonical Architecture Specification")
        count = division_counts[div_title]
        table_lines.append(f"| **{div_title}** | {focus} | {count} |")

    table_lines.append(
        f"| **Total Canonical Entities** | **Deterministic Architectural Standard** | **{total_entities}** |"
    )
    canonical_table_md = "\n".join(table_lines)

    # -------------------------------------------------------------
    # 3. Генерація Landing сторінки (src/content/docs/index.md)
    # -------------------------------------------------------------
    index_content = f"""---
title: Namencora Systems & Nomenclature Registry
description: Deterministic architecture registry and canonical namespace ontology.
template: splash
hero:
  tagline: Deterministic specification registry for high-throughput distributed architectures, state primitives, and consensus topographies.
  actions:
    - text: Explore Division 00
      link: /d00/entity-enumeros/
      icon: right-arrow
      variant: primary
    - text: View GitHub Source
      link: https://github.com/AltumVector/namencora
      icon: external
      variant: minimal
---

## Canonical Topology

{canonical_table_md}
"""

    with open(os.path.join(dest_root, "index.md"), "w", encoding="utf-8") as f:
        f.write(index_content.strip() + "\n")

    # -------------------------------------------------------------
    # 4. Синхронізація сторінки Governance
    # -------------------------------------------------------------
    gov_src = os.path.join(meta_root, "Registry_Governance.md")
    if os.path.exists(gov_src):
        with open(gov_src, "r", encoding="utf-8") as f:
            gov_txt = f.read()
        if not gov_txt.startswith("---"):
            gov_txt = '---\ntitle: "Registry Governance"\n---\n\n' + gov_txt
        with open(os.path.join(dest_root, "governance.md"), "w", encoding="utf-8") as f:
            f.write(gov_txt)

    # -------------------------------------------------------------
    # 5. Синхронізація карток сутностей у каталог Starlight
    # -------------------------------------------------------------
    synced_total = 0
    for div_title, slug in DIV_MAPPING.items():
        src_dir = resolve_div_source(div_title, slug)
        target_dir = os.path.join(dest_root, slug)
        os.makedirs(target_dir, exist_ok=True)

        if not src_dir:
            continue

        for fname in sorted(os.listdir(src_dir)):
            if fname.endswith(".md") and not fname.startswith("index"):
                src_path = os.path.join(src_dir, fname)
                dest_path = os.path.join(target_dir, fname)

                with open(src_path, "r", encoding="utf-8") as sf:
                    raw_content = sf.read()

                cleaned_content = clean_duplicate_h1(raw_content)

                with open(dest_path, "w", encoding="utf-8") as df:
                    df.write(cleaned_content)

                synced_total += 1

    print(f"• Синхронізовано {synced_total} карток у каталог Starlight (дублювання H1 прибрано)")

    # -------------------------------------------------------------
    # 6. Оновлення супутніх маніфестів (llms.txt та registry.json)
    # -------------------------------------------------------------
    llms_path = "public/llms.txt"
    if os.path.exists(llms_path):
        try:
            with open(llms_path, "r", encoding="utf-8") as f:
                llms_txt = f.read()
            llms_txt = re.sub(r'Entities:\s*\d+', f'Entities: {total_entities}', llms_txt)
            with open(llms_path, "w", encoding="utf-8") as f:
                f.write(llms_txt)
        except Exception:
            pass

    reg_path = "registry.json"
    if os.path.exists(reg_path):
        try:
            with open(reg_path, "r", encoding="utf-8") as f:
                reg_txt = f.read()
            reg_txt = re.sub(r'"total_entities":\s*\d+', f'"total_entities": {total_entities}', reg_txt)
            with open(reg_path, "w", encoding="utf-8") as f:
                f.write(reg_txt)
        except Exception:
            pass


def generate_sitemap():
    """
    Генератор sitemap.xml для виклику після компіляції Astro білду.
    Викликається ланцюжком у package.json: 'sync_docs.generate_sitemap()'.
    """
    dist_root = "dist"
    if not os.path.exists(dist_root):
        return

    base_url = "https://namencora.com"
    urls = []

    for root, _, files in os.walk(dist_root):
        for file in files:
            if file.endswith(".html"):
                rel_path = os.path.relpath(os.path.join(root, file), dist_root)
                if rel_path == "index.html":
                    loc = f"{base_url}/"
                elif rel_path.endswith("index.html"):
                    parent = os.path.dirname(rel_path).replace("\\", "/")
                    loc = f"{base_url}/{parent}/"
                else:
                    stem = rel_path[:-5].replace("\\", "/")
                    loc = f"{base_url}/{stem}/"
                urls.append(loc)

    urls = sorted(list(set(urls)))
    sitemap_lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for u in urls:
        sitemap_lines.append(f"  <url>\n    <loc>{u}</loc>\n  </url>")
    sitemap_lines.append('</urlset>')

    sitemap_path = os.path.join(dist_root, "sitemap.xml")
    with open(sitemap_path, "w", encoding="utf-8") as f:
        f.write("\n".join(sitemap_lines) + "\n")
    print(f"• Sitemap успішно оновлено: {len(urls)} URLs")


if __name__ == "__main__":
    sync_all()