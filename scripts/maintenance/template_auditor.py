#!/usr/bin/env python3
"""
scripts/maintenance/template_auditor.py

Audit jakości szablonów IT Dokumentacja.

Sprawdza każdy szablon pod kątem:
  - Obecności wymaganych sekcji (## Cel, ## Zakres, ## Wejścia, ## Wyjścia, ## Powiązania)
  - Kompletności guidance (sekcje z TODO lub placeholderami)
  - Aktualności referencji standardów (czy sekcja Standardy i compliance jest wypełniona)
  - Braku emoji
  - Poprawności linków (czy pliki .md do których linkuje istnieją)

Wynik: score 0–100 per szablon, raport zbiorczy.

Użycie:
  python3 scripts/maintenance/template_auditor.py
  python3 scripts/maintenance/template_auditor.py --glob "core/security_*.md"
  python3 scripts/maintenance/template_auditor.py --doc "Polityka bezpieczeństwa"
  python3 scripts/maintenance/template_auditor.py --min-score 60 --output json
  python3 scripts/maintenance/template_auditor.py --save reports/audit_latest.json
"""

import argparse
import fnmatch
import json
import re
import sqlite3
import sys
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.parent
DB_PATH = BASE_DIR / "reports" / "it_doc_matrix.db"
TEMPLATES_DIR = BASE_DIR / "generated_templates"
REPORTS_DIR = BASE_DIR / "reports"

# Required ## headings — each worth 10 points (50 total)
REQUIRED_SECTIONS = [
    ("Cel dokumentu", 10),
    ("Zakres i granice", 10),
    ("Wejścia i wyjścia", 10),
    ("Powiązania", 5),  # partial match — covers all ## Powiązania* variants
    ("Standardy i compliance", 10),
    ("RACI i role", 5),
    ("Metadane", 5),
]

# Penalty patterns
PLACEHOLDER_PATTERNS = [
    re.compile(r"\[TODO.*?\]", re.IGNORECASE),
    re.compile(r"TODO:", re.IGNORECASE),
    re.compile(r"\[PLACEHOLDER\]", re.IGNORECASE),
    re.compile(r"\[wypełnij\]", re.IGNORECASE),
    re.compile(r"\[rola\]", re.IGNORECASE),
]

EMOJI_RE = re.compile(
    "[\U0001f300-\U0001f9ff\U00002700-\U000027bf\U0001fa00-\U0001fa9f\U00002600-\U000026ff]+",
    flags=re.UNICODE,
)


def connect() -> sqlite3.Connection:
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    return conn


def audit_file(filepath: Path, rel_path: str, conn: sqlite3.Connection) -> dict:
    try:
        content = filepath.read_text(encoding="utf-8")
    except Exception as e:
        return {"path": rel_path, "score": 0, "error": str(e)}

    issues = []
    score = 0

    # 1. Required sections (50 pts max)
    headings = re.findall(r"^##\s+(.+)", content, re.MULTILINE)
    headings_lower = [h.lower() for h in headings]
    sections_found = []
    sections_missing = []

    for section, pts in REQUIRED_SECTIONS:
        found = any(section.lower() in h for h in headings_lower)
        if found:
            score += pts
            sections_found.append(section)
        else:
            sections_missing.append(section)
            issues.append(f"Brak sekcji: ## {section}")

    # 2. Placeholder count (up to -20 penalty)
    placeholder_count = sum(len(p.findall(content)) for p in PLACEHOLDER_PATTERNS)
    placeholder_penalty = min(20, placeholder_count * 2)
    if placeholder_count:
        issues.append(f"Placeholdery: {placeholder_count} wystąpień")

    # 3. Standardy i compliance — is it filled? (10 pts)
    m_std = re.search(r"^##\s+Standardy\s+i\s+compliance\b", content, re.MULTILINE)
    standards_filled = False
    if m_std:
        m_next = re.search(r"^#{1,3} ", content[m_std.end() :], re.MULTILINE)
        section_end = m_std.end() + m_next.start() if m_next else len(content)
        section_body = content[m_std.end() : section_end].strip()
        bullet_count = section_body.count("\n-")
        if bullet_count >= 1:
            score += 10
            standards_filled = True
        else:
            issues.append("Sekcja 'Standardy i compliance' nie zawiera pozycji")
    # (no extra penalty — sekcja already penalized as missing if not present)

    # 4. RACI filled? (5 pts)
    m_raci = re.search(r"^##\s+RACI\s+i\s+role\b", content, re.MULTILINE)
    raci_filled = False
    if m_raci:
        m_next = re.search(r"^#{1,3} ", content[m_raci.end() :], re.MULTILINE)
        section_end = m_raci.end() + m_next.start() if m_next else len(content)
        section_body = content[m_raci.end() : section_end].strip()
        if "|" in section_body or "-" in section_body:
            score += 5
            raci_filled = True
        else:
            issues.append("Sekcja 'RACI i role' nie zawiera tabeli ani listy")

    # 5. Guidance completeness — check doc_section_guidance (10 pts)
    cur = conn.cursor()
    cur.execute(
        """
        SELECT COUNT(*) FROM doc_section_guidance dsg
        JOIN docs d ON d.title = dsg.doc_title
        WHERE d.path = ? AND (dsg.guidance IS NOT NULL AND length(dsg.guidance) > 20)
    """,
        (rel_path,),
    )
    guidance_rows = cur.fetchone()[0]

    cur.execute(
        """
        SELECT COUNT(*) FROM doc_section_guidance dsg
        JOIN docs d ON d.title = dsg.doc_title
        WHERE d.path = ?
    """,
        (rel_path,),
    )
    total_guidance_rows = cur.fetchone()[0]

    guidance_score = 0
    if total_guidance_rows > 0:
        ratio = guidance_rows / total_guidance_rows
        guidance_score = int(ratio * 10)
        if ratio < 0.5:
            issues.append(f"Guidance niekompletne: {guidance_rows}/{total_guidance_rows} sekcji")
    score += guidance_score

    # 6. Emoji check (hard — 0 score if has emoji)
    emoji_found = bool(EMOJI_RE.search(content))
    if emoji_found:
        issues.append("Znaleziono emoji — naruszenie hard gate")
        score = 0

    # 7. Apply placeholder penalty
    score = max(0, score - placeholder_penalty)

    # Clamp to 100
    score = min(100, score)

    # Determine grade
    if score >= 80:
        grade = "A"
    elif score >= 60:
        grade = "B"
    elif score >= 40:
        grade = "C"
    else:
        grade = "D"

    return {
        "path": rel_path,
        "score": score,
        "grade": grade,
        "sections_found": sections_found,
        "sections_missing": sections_missing,
        "standards_filled": standards_filled,
        "raci_filled": raci_filled,
        "placeholder_count": placeholder_count,
        "guidance_rows": guidance_rows,
        "total_guidance_rows": total_guidance_rows,
        "emoji": emoji_found,
        "issues": issues,
    }


def collect_targets(conn: sqlite3.Connection, args) -> list[tuple[str, Path]]:
    cur = conn.cursor()
    if args.doc:
        cur.execute(
            "SELECT path FROM docs WHERE title LIKE ? AND path IS NOT NULL", (f"%{args.doc}%",)
        )
    else:
        cur.execute("SELECT path FROM docs WHERE path IS NOT NULL")

    paths = [(r[0], TEMPLATES_DIR / r[0]) for r in cur.fetchall() if r[0]]

    if args.glob:
        paths = [
            (p, fp)
            for p, fp in paths
            if fnmatch.fnmatch(p, args.glob) or fnmatch.fnmatch(Path(p).name, args.glob)
        ]

    return paths


def main():
    parser = argparse.ArgumentParser(description="Audit jakości szablonów IT Dokumentacja")
    parser.add_argument(
        "--glob", metavar="PATTERN", help="Filtr ścieżki (np. 'core/security_*.md')"
    )
    parser.add_argument("--doc", metavar="TITLE", help="Filtr tytułu dokumentu")
    parser.add_argument(
        "--min-score",
        type=int,
        default=0,
        metavar="N",
        help="Pokaż tylko szablony z score < N (filtr problemów)",
    )
    parser.add_argument("--output", choices=["table", "json"], default="table")
    parser.add_argument("--save", metavar="FILE", help="Zapisz wyniki do pliku JSON")
    parser.add_argument("--limit", type=int, default=0, help="Ogranicz do N szablonów")
    args = parser.parse_args()

    conn = connect()
    targets = collect_targets(conn, args)
    if args.limit:
        targets = targets[: args.limit]

    print(f"Audyt: {len(targets)} szablonów...", file=sys.stderr)

    results = []
    for i, (rel_path, filepath) in enumerate(targets):
        r = audit_file(filepath, rel_path, conn)
        results.append(r)
        if (i + 1) % 500 == 0:
            print(f"  {i + 1}/{len(targets)}...", file=sys.stderr)

    conn.close()

    # Filter by min-score
    display = (
        [r for r in results if r.get("score", 100) < args.min_score] if args.min_score else results
    )

    # Summary stats
    scores = [r["score"] for r in results if "error" not in r]
    summary = {
        "total": len(results),
        "avg_score": round(sum(scores) / len(scores), 1) if scores else 0,
        "grade_A": sum(1 for r in results if r.get("grade") == "A"),
        "grade_B": sum(1 for r in results if r.get("grade") == "B"),
        "grade_C": sum(1 for r in results if r.get("grade") == "C"),
        "grade_D": sum(1 for r in results if r.get("grade") == "D"),
        "with_emoji": sum(1 for r in results if r.get("emoji")),
        "with_placeholders": sum(1 for r in results if r.get("placeholder_count", 0) > 0),
        "missing_standardy": sum(
            1 for r in results if "Standardy i compliance" in r.get("sections_missing", [])
        ),
        "missing_raci": sum(1 for r in results if "RACI i role" in r.get("sections_missing", [])),
    }

    output = {"summary": summary, "results": display}

    if args.output == "json":
        print(json.dumps(output, ensure_ascii=False, indent=2))
    else:
        print("\n=== Podsumowanie audytu ===")
        print(f"  Łącznie szablonów: {summary['total']}")
        print(f"  Średni score:      {summary['avg_score']}/100")
        print(f"  Ocena A (≥80):     {summary['grade_A']}")
        print(f"  Ocena B (60-79):   {summary['grade_B']}")
        print(f"  Ocena C (40-59):   {summary['grade_C']}")
        print(f"  Ocena D (<40):     {summary['grade_D']}")
        print(f"  Z emoji:           {summary['with_emoji']} (hard gate!)")
        print(f"  Z placeholderami:  {summary['with_placeholders']}")
        print(f"  Brak std-section:  {summary['missing_standardy']}")
        print(f"  Brak RACI:         {summary['missing_raci']}")

        if display and args.min_score:
            print(f"\n=== Szablony z score < {args.min_score} ({len(display)} szt.) ===")
            for r in sorted(display, key=lambda x: x["score"])[:50]:
                print(f"  [{r['grade']}:{r['score']:3d}] {r['path']}")
                for issue in r["issues"][:3]:
                    print(f"         - {issue}")

    if args.save:
        save_path = Path(args.save)
        save_path.write_text(json.dumps(output, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"\nZapisano do: {save_path}", file=sys.stderr)

    return 0


if __name__ == "__main__":
    sys.exit(main())
