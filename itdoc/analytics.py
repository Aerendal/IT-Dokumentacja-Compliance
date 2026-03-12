"""
itdoc/analytics.py

Moduł analityczny — statystyki pokrycia biblioteki, raporty zdrowia,
identyfikacja luk w mapowaniach.

Użycie:
    from itdoc.analytics import library_health_report, coverage_by_standard
    python3 -m itdoc.analytics --format markdown > reports/health.md
"""

from __future__ import annotations

import argparse
import sqlite3
from collections import defaultdict
from pathlib import Path


# ---------------------------------------------------------------------------
# Publiczne API
# ---------------------------------------------------------------------------


def coverage_by_standard(conn: sqlite3.Connection) -> dict:
    """
    Zwraca liczbę zmapowanych szablonów dla każdego standardu.

    Returns:
        {standard_code: count, ...} posortowane malejąco po count.
    """
    rows = conn.execute("""
        SELECT standard_code, COUNT(DISTINCT doc_path) AS cnt
        FROM doc_standard_mapping
        WHERE doc_path IS NOT NULL AND doc_path != ''
        GROUP BY standard_code
        ORDER BY cnt DESC
    """).fetchall()
    return {r["standard_code"]: r["cnt"] for r in rows}


def unmapped_by_category(conn: sqlite3.Connection) -> dict:
    """
    Zwraca niezmapowane szablony pogrupowane wg kategorii ścieżki.
    Kategoria = pierwsza część ścieżki po 'core/' lub 'satellite/' (podkatalog) lub 'root'.

    Returns:
        {category: [path, ...], ...}
    """
    mapped = {
        r[0]
        for r in conn.execute(
            "SELECT DISTINCT doc_path FROM doc_standard_mapping WHERE doc_path IS NOT NULL AND doc_path != ''"
        )
    }

    all_docs = conn.execute(
        "SELECT path FROM docs WHERE path IS NOT NULL AND path != '' AND path != 'ORPHAN'"
    ).fetchall()

    groups: dict = defaultdict(list)
    for row in all_docs:
        path = row["path"]
        if path in mapped:
            continue
        # Wyciągnij kategorię: core/subcategory/file.md → subcategory
        parts = Path(path).parts
        if len(parts) >= 3:
            category = parts[-2]
        elif len(parts) >= 2:
            category = parts[-2]
        else:
            category = "root"
        groups[category].append(path)

    return dict(sorted(groups.items(), key=lambda x: len(x[1]), reverse=True))


def standard_gaps(conn: sqlite3.Connection, min_coverage: int = 5) -> list:
    """
    Zwraca listę standardów poniżej minimalnego progu pokrycia.

    Args:
        min_coverage: minimalna liczba szablonów na standard

    Returns:
        [(standard_code, count), ...] dla standardów poniżej progu
    """
    coverage = coverage_by_standard(conn)
    return sorted(
        [(code, cnt) for code, cnt in coverage.items() if cnt < min_coverage],
        key=lambda x: x[1],
    )


def match_reason_distribution(conn: sqlite3.Connection) -> dict:
    """
    Zwraca rozkład typów mapowań (keyword_match, explicit_audit, candidate_match...).

    Returns:
        {match_reason: count, ...}
    """
    rows = conn.execute("""
        SELECT match_reason, COUNT(*) AS cnt
        FROM doc_standard_mapping
        GROUP BY match_reason
        ORDER BY cnt DESC
    """).fetchall()
    return {r["match_reason"]: r["cnt"] for r in rows}


def library_health_report(conn: sqlite3.Connection) -> str:
    """
    Generuje pełny raport zdrowia biblioteki w formacie Markdown.

    Returns:
        str — raport w formacie Markdown
    """
    # --- zbierz dane ---
    total_docs = conn.execute(
        "SELECT COUNT(*) FROM docs WHERE path IS NOT NULL AND path != '' AND path != 'ORPHAN'"
    ).fetchone()[0]

    mapped_docs = conn.execute(
        "SELECT COUNT(DISTINCT doc_path) FROM doc_standard_mapping WHERE doc_path IS NOT NULL AND doc_path != ''"
    ).fetchone()[0]

    total_mappings = conn.execute("SELECT COUNT(*) FROM doc_standard_mapping").fetchone()[0]
    unmapped = total_docs - mapped_docs
    coverage_pct = (mapped_docs / total_docs * 100) if total_docs else 0

    cov = coverage_by_standard(conn)
    reason_dist = match_reason_distribution(conn)
    gaps = standard_gaps(conn, min_coverage=5)
    unmapped_cats = unmapped_by_category(conn)

    # --- buduj raport ---
    lines = [
        "# Raport zdrowia biblioteki szablonów IT",
        "",
        f"_Wygenerowano automatycznie przez `itdoc.analytics`_",
        "",
        "---",
        "",
        "## Podsumowanie",
        "",
        f"| Metryka | Wartość |",
        f"|---------|---------|",
        f"| Łączna liczba szablonów | **{total_docs:,}** |",
        f"| Zmapowane szablony | **{mapped_docs:,}** ({coverage_pct:.1f}%) |",
        f"| Niezmapowane szablony | **{unmapped:,}** |",
        f"| Łączna liczba mapowań | **{total_mappings:,}** |",
        f"| Standardy w katalogu | **{len(cov)}** |",
        "",
        "---",
        "",
        "## Top 10 standardów (liczba szablonów)",
        "",
        "| Standard | Szablony |",
        "|----------|----------|",
    ]

    for code, cnt in list(cov.items())[:10]:
        lines.append(f"| {code} | {cnt:,} |")

    lines += [
        "",
        "---",
        "",
        "## Rozkład typów mapowań",
        "",
        "| Typ mapowania | Liczba |",
        "|---------------|--------|",
    ]
    for reason, cnt in reason_dist.items():
        lines.append(f"| {reason or '(brak)'} | {cnt:,} |")

    if gaps:
        lines += [
            "",
            "---",
            "",
            f"## Standardy poniżej progu (< 5 szablonów)",
            "",
            "| Standard | Szablony |",
            "|----------|----------|",
        ]
        for code, cnt in gaps:
            lines.append(f"| {code} | {cnt} |")

    if unmapped_cats:
        lines += [
            "",
            "---",
            "",
            "## Top 10 kategorii niezmapowanych szablonów",
            "",
            "| Kategoria | Niezmapowane |",
            "|-----------|--------------|",
        ]
        for cat, paths in list(unmapped_cats.items())[:10]:
            lines.append(f"| {cat} | {len(paths)} |")

    lines += ["", "---", ""]
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="python3 -m itdoc.analytics",
        description="Raporty zdrowia biblioteki szablonów IT",
    )
    p.add_argument(
        "--db",
        default="reports/it_doc_matrix.db",
        help="Ścieżka do bazy danych SQLite (domyślnie: reports/it_doc_matrix.db)",
    )
    p.add_argument(
        "--format",
        choices=["markdown", "text"],
        default="markdown",
        help="Format raportu (domyślnie: markdown)",
    )
    p.add_argument(
        "--coverage",
        action="store_true",
        help="Pokaż tylko tabelę pokrycia per standard",
    )
    p.add_argument(
        "--gaps",
        action="store_true",
        help="Pokaż standardy poniżej progu pokrycia",
    )
    p.add_argument(
        "--min-coverage",
        type=int,
        default=5,
        help="Minimalny próg pokrycia dla --gaps (domyślnie: 5)",
    )
    return p


def main(argv=None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)

    db_path = Path(args.db)
    if not db_path.exists():
        print(f"[BŁĄD] Baza danych nie istnieje: {db_path}", flush=True)
        import sys
        sys.stderr.write(f"Brak pliku: {db_path}\n")
        return 1

    conn = sqlite3.connect(str(db_path))
    conn.row_factory = sqlite3.Row

    try:
        if args.coverage:
            cov = coverage_by_standard(conn)
            for code, cnt in cov.items():
                print(f"{code:40s} {cnt:5d}")
            return 0

        if args.gaps:
            gaps = standard_gaps(conn, min_coverage=args.min_coverage)
            if not gaps:
                print(f"Brak standardów poniżej progu {args.min_coverage}.")
            else:
                for code, cnt in gaps:
                    print(f"{code:40s} {cnt:3d} szablonów")
            return 0

        report = library_health_report(conn)
        print(report)
        return 0
    finally:
        conn.close()


if __name__ == "__main__":
    import sys
    sys.exit(main())
