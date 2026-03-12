#!/usr/bin/env python3
"""Export document titles per industry_code_isic into 10 markdown files.
Outputs to ../exports/branże_md/IT_Dokumentacja_Branze_Pakiet_{i}.md
Format inspired by existing IT_Dokumentacja_Czesc_* files.
"""
import math
import sqlite3
from pathlib import Path
from datetime import date

ISIC_NAMES = {
    "01": "Crop and animal production, hunting and related services",
    "02": "Forestry and logging",
    "05": "Mining of coal and lignite",
    "06": "Extraction of crude petroleum and natural gas",
    "07": "Mining of metal ores",
    "09": "Mining support service activities",
    "10": "Manufacture of food products",
    "14": "Manufacture of wearing apparel",
    "16": "Manufacture of wood products",
    "18": "Printing and reproduction of recorded media",
    "21": "Manufacture of pharmaceuticals",
    "23": "Manufacture of non-metallic mineral products",
    "25": "Manufacture of fabricated metal products",
    "26": "Manufacture of computer, electronic and optical products",
    "28": "Manufacture of machinery and equipment",
    "33": "Repair and installation of machinery and equipment",
    "35": "Electricity, gas, steam and air conditioning supply",
    "36": "Water collection, treatment and supply",
    "38": "Waste collection, treatment and disposal; materials recovery",
    "39": "Remediation and other waste management services",
    "41": "Construction of buildings",
    "42": "Civil engineering",
    "45": "Motor vehicles trade and repair",
    "47": "Retail trade",
    "49": "Land transport and transport via pipelines",
    "50": "Water transport",
    "51": "Air transport",
    "52": "Warehousing and support for transportation",
    "55": "Accommodation",
    "56": "Food and beverage service activities",
    "58": "Publishing activities",
    "59": "Film, video, TV production; music publishing",
    "60": "Programming and broadcasting activities",
    "61": "Telecommunications",
    "62": "Computer programming, consultancy and related activities",
    "63": "Information service activities",
    "64": "Financial service activities (except insurance/pensions)",
    "65": "Insurance and pension funding",
    "66": "Auxiliary finance and insurance activities",
    "68": "Real estate activities",
    "69": "Legal and accounting activities",
    "70": "Head offices; management consultancy",
    "71": "Architectural/engineering; technical testing/analysis",
    "72": "Scientific research and development",
    "73": "Advertising and market research",
    "78": "Employment activities",
    "79": "Travel agency, tour operator services",
    "80": "Security and investigation activities",
    "82": "Office/admin and other business support",
    "84": "Public administration and defence; social security",
    "85": "Education",
    "86": "Human health activities",
    "88": "Social work activities",
    "91": "Libraries, archives, museums, cultural activities",
    "93": "Sports, amusement and recreation activities",
    "94": "Activities of membership organisations",
    "95": "Repair of computers and personal/household goods",
    "98": "Undifferentiated household production for own use",
}

ROOT = Path(__file__).resolve().parents[1]
DB = ROOT / "reports" / "it_doc_matrix.db"
OUT_DIR = ROOT / "exports" / "branże_md"
OUT_DIR.mkdir(parents=True, exist_ok=True)

TODAY = date.today().isoformat()

conn = sqlite3.connect(f"file:{DB}?mode=ro", uri=True)
cur = conn.cursor()

cur.execute(
    "SELECT industry_code_isic, industry_code_isic_tag, COUNT(*) "
    "FROM documents_final GROUP BY industry_code_isic, industry_code_isic_tag "
    "ORDER BY industry_code_isic"
)
rows = cur.fetchall()

# choose best tag per code (longest cleaned tag), sum counts per code
best_by_code = {}
for code, tag, count in rows:
    tag_clean = (tag or "").replace("_", " ").strip()
    # prefer canonical ISIC name if available
    tag_clean = ISIC_NAMES.get(code, tag_clean)
    if len(tag_clean) < 3:
        tag_clean = ISIC_NAMES.get(code, "")
    current = best_by_code.get(code)
    if current is None or len(tag_clean) > len(current["tag"]):
        best_by_code[code] = {"code": code, "tag": tag_clean, "count": count}
    else:
        best_by_code[code]["count"] += count

industries = sorted(best_by_code.values(), key=lambda x: x["code"])

total_docs = sum(i["count"] for i in industries)
target_files = 10
max_per_file = math.ceil(total_docs / target_files)

buckets = []
current = []
cum = 0
for ind in industries:
    if current and cum + ind["count"] > max_per_file and len(buckets) < target_files - 1:
        buckets.append(current)
        current = []
        cum = 0
    current.append(ind)
    cum += ind["count"]
if current:
    buckets.append(current)

# if fewer buckets than target, split the last bucket until we reach target_files
while len(buckets) < target_files and buckets:
    last = buckets.pop()
    if len(last) <= 1:
        buckets.append(last)
        break
    mid = len(last) // 2
    buckets.append(last[:mid])
    buckets.append(last[mid:])

total_files = len(buckets)

# helper to fetch titles for a code
cur_titles = conn.cursor()


def fetch_titles(code):
    cur_titles.execute(
        "SELECT DISTINCT title FROM documents_final WHERE industry_code_isic=? ORDER BY title COLLATE NOCASE",
        (code,),
    )
    return [t[0] for t in cur_titles.fetchall()]

for idx, bucket in enumerate(buckets, start=1):
    codes = [b["code"] for b in bucket]
    total_bucket = sum(b["count"] for b in bucket)
    branze_desc = "; ".join([f"{b['code']} {b['tag']}".strip() for b in bucket])
    filename = OUT_DIR / f"IT_Dokumentacja_Branze_Pakiet_{idx}.md"

    # Build TOC
    toc_lines = []
    for b in bucket:
        anchor = f"isic-{b['code']}"
        label = f"ISIC {b['code']} — {b['tag']}" if b["tag"] else f"ISIC {b['code']}"
        toc_lines.append(f"- [{label}](#{anchor})")

    body_lines = []
    for b in bucket:
        anchor = f"isic-{b['code']}"
        titles = fetch_titles(b["code"])
        label = f"ISIC {b['code']} — {b['tag']}" if b["tag"] else f"ISIC {b['code']}"
        body_lines.append(f"## {label}\n")
        body_lines.append(f"Liczba dokumentów: {len(titles)}\n")
        for t in titles:
            body_lines.append(f"- {t}")
        body_lines.append("")

    content = "\n".join([
        "---",
        f"title: IT Documentation Matrix - Branże (Pakiet {idx}/{total_files})",
        f"subtitle: Branże ISIC — Pakiet {idx}/{total_files}",
        "version: 1.0",
        f"generated: {TODAY}",
        f"branze: {branze_desc}",
        "status: Generated",
        "description: >",
        f"  Pakiet branż ISIC: {branze_desc}. Łącznie dokumentów: {total_bucket}.",
        "---",
        "",
        "# IT Documentation Matrix - Branże",
        f"## Pakiet {idx}/{total_files}",
        "",
        "### Spis treści",
        *toc_lines,
        "",
        *body_lines,
    ])

    filename.write_text(content, encoding="utf-8")

conn.close()
print(f"Generated {total_files} files in {OUT_DIR}")
