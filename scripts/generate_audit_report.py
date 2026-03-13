#!/usr/bin/env python3
"""
generate_audit_report.py — Generuje Markdown raport audytu standardów.

Sekcje:
  1. Streszczenie wykonawcze
  2. Brakujące szablony (missing) per standard
  3. Szablony "extra" (50 bez mapowania do standardu)
  4. Dopasowania niskiej pewności (low/medium) — do weryfikacji ręcznej
  5. Tabela podsumowująca per standard
"""

from __future__ import annotations

import argparse
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

DB_DEFAULT = Path(__file__).parent.parent / "reports" / "it_doc_matrix.db"
REPORT_DIR = Path(__file__).parent.parent / "reports"


def run(conn: sqlite3.Connection) -> str:
    lines: list[str] = []
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    # ── Nagłówek ──────────────────────────────────────────────────────────
    lines += [
        "# Raport Audytu Standardów — IT_Dokumentacja",
        "",
        f"**Wygenerowano:** {ts}  ",
        "**Źródło:** `scripts/gap_analysis.py` + `scripts/build_standards_catalog.py`",
        "",
    ]

    # ── Statystyki ogólne ─────────────────────────────────────────────────
    total_docs = conn.execute("SELECT COUNT(*) FROM docs WHERE path != 'ORPHAN'").fetchone()[0]
    total_stds = conn.execute("SELECT COUNT(*) FROM standards").fetchone()[0]
    total_catalog = conn.execute("SELECT COUNT(*) FROM standards_catalog").fetchone()[0]
    present = conn.execute("SELECT COUNT(*) FROM gap_analysis WHERE status='present'").fetchone()[0]
    missing = conn.execute("SELECT COUNT(*) FROM gap_analysis WHERE status='missing'").fetchone()[0]
    req_missing = conn.execute(
        "SELECT COUNT(*) FROM gap_analysis WHERE status='missing' AND is_required=1"
    ).fetchone()[0]
    conf_exact = conn.execute(
        "SELECT COUNT(*) FROM gap_analysis WHERE confidence='exact'"
    ).fetchone()[0]
    conf_high = conn.execute(
        "SELECT COUNT(*) FROM gap_analysis WHERE confidence='high'"
    ).fetchone()[0]
    conf_medium = conn.execute(
        "SELECT COUNT(*) FROM gap_analysis WHERE confidence='medium'"
    ).fetchone()[0]
    conf_low = conn.execute("SELECT COUNT(*) FROM gap_analysis WHERE confidence='low'").fetchone()[
        0
    ]
    extra_docs = conn.execute("""
        SELECT COUNT(*) FROM docs d WHERE d.path != 'ORPHAN'
        AND NOT EXISTS (SELECT 1 FROM doc_standard_mapping m WHERE m.doc_path = d.path)
    """).fetchone()[0]

    coverage_pct = round(100.0 * present / total_catalog, 1) if total_catalog else 0

    lines += [
        "---",
        "",
        "## 1. Streszczenie wykonawcze",
        "",
        "| Metryka | Wartość |",
        "|---------|---------|",
        f"| Szablony w bazie (non-orphan) | **{total_docs:,}** |",
        f"| Standardów w DB | **{total_stds}** |",
        f"| Wpisów w katalogu standardów | **{total_catalog}** |",
        f"| Pokrycie katalogu przez szablony | **{coverage_pct}%** ({present}/{total_catalog}) |",
        f"| Brakujące szablony (wszystkie) | **{missing}** |",
        f"| Brakujące szablony (REQUIRED) | **{req_missing}** |",
        f"| Szablony bez przypisanego standardu (extra) | **{extra_docs}** |",
        "",
        "### Pewność dopasowań",
        "",
        "| Poziom | Liczba | Opis |",
        "|--------|--------|------|",
        f"| `exact`  | {conf_exact} | Dokładny match slug tytułu |",
        f"| `high`   | {conf_high} | Bigram Jaccard ≥ 0.50 |",
        f"| `medium` | {conf_medium} | Keyword overlap ≥ 0.40 — **wymaga weryfikacji** |",
        f"| `low`    | {conf_low} | Keyword overlap ≥ 0.25 — **wymaga weryfikacji** |",
        "",
        f"> **Uwaga:** Dopasowania `medium` i `low` (łącznie {conf_medium + conf_low}) oznaczają że algorytm",
        "> znalazł podobny szablon ale nie jest pewny dopasowania. Warto zweryfikować ręcznie",
        "> sekcje wymienione w tabeli per standard poniżej.",
        "",
    ]

    # ── 2. Brakujące szablony ─────────────────────────────────────────────
    lines += [
        "---",
        "",
        "## 2. Brakujące szablony (MISSING)",
        "",
        "Szablony wymagane przez standard których **nie znaleziono** w naszej bazie.",
        "",
    ]
    missing_rows = conn.execute("""
        SELECT standard_code, doc_title, is_required, catalog_category
        FROM gap_analysis WHERE status='missing'
        ORDER BY is_required DESC, standard_code, doc_title
    """).fetchall()

    if missing_rows:
        lines.append("| Standard | Dokument | Typ | Kategoria |")
        lines.append("|----------|----------|-----|-----------|")
        for code, title, req, cat in missing_rows:
            req_label = "**REQUIRED**" if req else "recommended"
            lines.append(f"| {code} | {title} | {req_label} | {cat} |")
    else:
        lines.append("✅ Brak brakujących szablonów!")
    lines.append("")

    # ── 3. Szablony extra ─────────────────────────────────────────────────
    lines += [
        "---",
        "",
        "## 3. Szablony bez przypisanego standardu (EXTRA)",
        "",
        "Te szablony istnieją w bazie ale **żaden standard** ich nie wymaga (brak w `doc_standard_mapping`).",
        "Mogą być: (a) specjalistyczne szablony branżowe bez formalnego standardu,",
        "(b) błędnie pominięte podczas mapowania, (c) kandydaci do usunięcia lub konsolidacji.",
        "",
    ]
    extra_rows = conn.execute("""
        SELECT d.title, d.path FROM docs d
        WHERE d.path != 'ORPHAN'
        AND NOT EXISTS (SELECT 1 FROM doc_standard_mapping m WHERE m.doc_path = d.path)
        ORDER BY d.title
    """).fetchall()

    lines.append(f"**Łącznie: {len(extra_rows)} szablonów**")
    lines.append("")
    lines.append("| Tytuł | Ścieżka |")
    lines.append("|-------|---------|")
    for title, path in extra_rows:
        lines.append(f"| {title} | `{path}` |")
    lines.append("")

    # ── 4. Dopasowania niskiej pewności ───────────────────────────────────
    lines += [
        "---",
        "",
        "## 4. Dopasowania niskiej pewności — do weryfikacji",
        "",
        "Dopasowania `low` (keyword overlap 0.25–0.40). Algorytm znalazł szablon ale pewność jest niska.",
        "Warto sprawdzić czy dopasowany szablon rzeczywiście spełnia wymagania standardu.",
        "",
        "| Standard | Oczekiwany dokument | Dopasowany szablon | Pewność |",
        "|----------|--------------------|--------------------|---------|",
    ]
    low_rows = conn.execute("""
        SELECT standard_code, doc_title, matched_doc_title, confidence
        FROM gap_analysis
        WHERE confidence = 'low'
        ORDER BY standard_code, doc_title
    """).fetchall()
    for code, expected, matched, conf in low_rows:
        matched_s = (matched or "—")[:60]
        expected_s = expected[:60]
        lines.append(f"| {code} | {expected_s} | {matched_s} | `{conf}` |")
    lines.append("")

    # ── 5. Tabela per standard ────────────────────────────────────────────
    lines += [
        "---",
        "",
        "## 5. Podsumowanie per standard",
        "",
        "| Standard | Present | Missing | Low/Med | Status |",
        "|----------|---------|---------|---------|--------|",
    ]
    summary_rows = conn.execute("""
        SELECT
            g.standard_code,
            SUM(CASE WHEN g.status='present' THEN 1 ELSE 0 END) AS present,
            SUM(CASE WHEN g.status='missing' THEN 1 ELSE 0 END) AS missing,
            SUM(CASE WHEN g.confidence IN ('low','medium') THEN 1 ELSE 0 END) AS low_med,
            COUNT(*) as total
        FROM gap_analysis g
        GROUP BY g.standard_code
        ORDER BY g.standard_code
    """).fetchall()
    for code, present, missing, low_med, total in summary_rows:
        pct = round(100.0 * present / total) if total else 0
        if missing > 0:
            status = "⚠️ LUKI"
        elif low_med > total * 0.5:
            status = "🔍 do weryfikacji"
        else:
            status = "✅ OK"
        lines.append(f"| {code} | {present}/{total} ({pct}%) | {missing} | {low_med} | {status} |")
    lines.append("")

    # ── 6. Rekomendacje ───────────────────────────────────────────────────
    lines += [
        "---",
        "",
        "## 6. Rekomendowane działania",
        "",
        "### Pilne (REQUIRED missing)",
        "",
    ]
    req_missing_rows = conn.execute("""
        SELECT standard_code, doc_title FROM gap_analysis
        WHERE status='missing' AND is_required=1
        ORDER BY standard_code
    """).fetchall()
    for code, title in req_missing_rows:
        lines.append(f"- **[{code}]** Dodać szablon: `{title}`")

    lines += [
        "",
        "### Szablony 'extra' — plan działania",
        "",
        "50 szablonów bez przypisanego standardu wymaga przeglądu:",
        "- Sprawdzić czy każdy szablon pasuje do któregoś z 44 standardów i dodać mapowanie",
        "- Szablony dziedzinowe (3D, Smart Grid, LMS) — rozważyć dodanie nowych standardów (np. branżowych)",
        "- Szablony z błędami w tytule (np. `Uwaga:`, `Architektura rozwiąania`) — poprawić",
        "",
        "### Dopasowania do ręcznej weryfikacji",
        "",
        "77 dopasowań z pewnością `low` + 150 z `medium` — priorytetyzuj standardy z ⚠️ przy Gap Analysis.",
        "",
    ]

    return "\n".join(lines)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--db",
        default=DB_DEFAULT,
        help="Ścieżka do pliku .db (domyślnie: reports/it_doc_matrix.db)",
    )
    ap.add_argument(
        "--output",
        default=None,
        help="Output .md file (default: reports/standards_audit_report.md)",
    )
    args = ap.parse_args()

    conn = sqlite3.connect(args.db)

    # Sprawdź czy tabele istnieją
    tables = [
        r[0] for r in conn.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
    ]
    if "gap_analysis" not in tables:
        print("ERROR: Tabela gap_analysis nie istnieje. Uruchom najpierw gap_analysis.py")
        return
    if "standards_catalog" not in tables:
        print(
            "ERROR: Tabela standards_catalog nie istnieje. Uruchom najpierw build_standards_catalog.py"
        )
        return

    report_md = run(conn)
    conn.close()

    out_path = Path(args.output) if args.output else (REPORT_DIR / "standards_audit_report.md")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(report_md, encoding="utf-8")
    print(f"Report written to: {out_path}")
    print(f"Lines: {len(report_md.splitlines())}")


if __name__ == "__main__":
    main()
