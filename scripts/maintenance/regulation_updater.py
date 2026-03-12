#!/usr/bin/env python3
"""
scripts/maintenance/regulation_updater.py

Narzędzie CLI do zarządzania przypisaniami dokumentów do regulacji i standardów.

Użycie:
    python3 regulation_updater.py add --doc core/X.md --standard "NIS2" --reason explicit_audit
    python3 regulation_updater.py remove --doc core/X.md --standard "NIS2"
    python3 regulation_updater.py list --standard "GDPR / RODO" --format csv
    python3 regulation_updater.py list --format table
    python3 regulation_updater.py add-regulation --doc core/X.md --regulation "AML/KYC"
    python3 regulation_updater.py stats
"""

import argparse
import csv
import io
import sqlite3
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional

# ---------------------------------------------------------------------------
# Stałe
# ---------------------------------------------------------------------------

VERSION = "1.0.0"

VALID_CONFIDENCE = ("exact", "high", "medium", "low")

VALID_MATCH_REASONS = (
    "explicit_audit",
    "keyword_match",
    "manual",
    "auto",
    "inferred",
)

DEFAULT_DB = Path(__file__).parent.parent.parent / "reports" / "it_doc_matrix.db"


# ---------------------------------------------------------------------------
# Funkcje pomocnicze top-level (na potrzeby testów)
# ---------------------------------------------------------------------------


def validate_match_reason(reason: str) -> bool:
    """Zwraca True jeśli reason jest jedną ze znanych wartości."""
    return reason in VALID_MATCH_REASONS


def validate_confidence(confidence: str) -> bool:
    """Zwraca True jeśli confidence należy do VALID_CONFIDENCE."""
    return confidence in VALID_CONFIDENCE


def build_list_query(
    standard: Optional[str] = None,
    regulation: Optional[str] = None,
    reason: Optional[str] = None,
) -> tuple:
    """Buduje zapytanie SQL do listowania mappingów z opcjonalnymi filtrami.

    Returns:
        (sql: str, params: list)

    Uwaga: join z gap_analysis używa kolumny matched_doc_path (nie doc_path).
    """
    sql = """
        SELECT
            m.doc_path,
            m.standard_code,
            m.match_reason,
            g.confidence,
            g.status
        FROM doc_standard_mapping m
        LEFT JOIN gap_analysis g
            ON m.doc_path = g.matched_doc_path
            AND m.standard_code = g.standard_code
    """
    conditions: list = []
    params: list = []

    if standard is not None:
        conditions.append("m.standard_code = ?")
        params.append(standard)

    if regulation is not None:
        conditions.append(
            "EXISTS ("
            "SELECT 1 FROM doc_regulation_mapping r "
            "WHERE r.doc_path = m.doc_path AND r.regulation_code = ?"
            ")"
        )
        params.append(regulation)

    if reason is not None:
        conditions.append("m.match_reason = ?")
        params.append(reason)

    if conditions:
        sql += " WHERE " + " AND ".join(conditions)

    sql += " ORDER BY m.doc_path"
    return sql, params


def format_row_csv(row: dict) -> str:
    """Formatuje wiersz mappingu jako linię CSV (bez nagłówka)."""
    buf = io.StringIO()
    writer = csv.writer(buf)
    writer.writerow(
        [
            row.get("doc_path") or "",
            row.get("standard_code") or "",
            row.get("match_reason") or "",
            row.get("confidence") or "",
            row.get("status") or "",
        ]
    )
    return buf.getvalue().rstrip("\r\n")


def format_row_table(row: dict, widths: dict) -> str:
    """Formatuje wiersz mappingu jako linię tabeli z podanymi szerokościami kolumn.

    widths: dict z kluczami "doc_path", "standard_code", "match_reason",
            "confidence", "status" i wartościami int.
    """
    w_doc = widths.get("doc_path", 50)
    w_std = widths.get("standard_code", 22)
    w_reason = widths.get("match_reason", 20)
    w_conf = widths.get("confidence", 10)
    w_status = widths.get("status", 10)

    doc = (row.get("doc_path") or "")[:w_doc]
    std = (row.get("standard_code") or "")[:w_std]
    reason = (row.get("match_reason") or "")[:w_reason]
    conf = (row.get("confidence") or "-")[:w_conf]
    status = (row.get("status") or "-")[:w_status]

    return (
        f"{doc:<{w_doc}} {std:<{w_std}} {reason:<{w_reason}} {conf:<{w_conf}} {status:<{w_status}}"
    )


# ---------------------------------------------------------------------------
# Klasa RegulationUpdater
# ---------------------------------------------------------------------------


class RegulationUpdater:
    """Zarządza przypisaniami dokumentów do regulacji i standardów w SQLite."""

    def __init__(self, db_path: Optional[str] = None) -> None:
        path = Path(db_path) if db_path else DEFAULT_DB
        if not path.exists():
            print(f"[BŁĄD] Brak bazy danych: {path}", file=sys.stderr)
            sys.exit(1)
        self.conn = sqlite3.connect(str(path))
        self.conn.row_factory = sqlite3.Row

    # ------------------------------------------------------------------
    # Wewnętrzne
    # ------------------------------------------------------------------

    def _log_changelog(
        self,
        doc_path: str,
        change_type: str,
        change_reason: str,
    ) -> None:
        """Zapisuje wpis do template_changelog."""
        self.conn.execute(
            """
            INSERT INTO template_changelog
                (template_path, changed_at, change_type, change_reason)
            VALUES (?, ?, ?, ?)
            """,
            (doc_path, datetime.now().isoformat(), change_type, change_reason),
        )

    # ------------------------------------------------------------------
    # Operacje
    # ------------------------------------------------------------------

    def add_standard_mapping(
        self,
        doc_path: str,
        standard_code: str,
        match_reason: str = "explicit_audit",
    ) -> None:
        """Dodaje (lub aktualizuje) przypisanie dokumentu do standardu."""
        self.conn.execute(
            """
            INSERT INTO doc_standard_mapping (doc_path, standard_code, match_reason)
            VALUES (?, ?, ?)
            ON CONFLICT(doc_path, standard_code) DO UPDATE
                SET match_reason = excluded.match_reason
            """,
            (doc_path, standard_code, match_reason),
        )
        self._log_changelog(
            doc_path,
            "mapping_add",
            f"standard={standard_code} reason={match_reason}",
        )
        self.conn.commit()
        print(f"[OK]   Przypisano '{doc_path}' do standardu '{standard_code}'")

    def remove_standard_mapping(
        self,
        doc_path: str,
        standard_code: str,
    ) -> None:
        """Usuwa przypisanie dokumentu od standardu."""
        cur = self.conn.execute(
            "DELETE FROM doc_standard_mapping WHERE doc_path = ? AND standard_code = ?",
            (doc_path, standard_code),
        )
        self._log_changelog(
            doc_path,
            "mapping_remove",
            f"standard={standard_code}",
        )
        self.conn.commit()
        if cur.rowcount:
            print(f"[OK]   Odpieto '{doc_path}' od standardu '{standard_code}'")
        else:
            print(f"[WARN] Nie znaleziono powiązania: '{doc_path}' / '{standard_code}'")

    def list_mappings(
        self,
        standard: Optional[str] = None,
        regulation: Optional[str] = None,
        reason: Optional[str] = None,
        fmt: str = "table",
    ) -> list:
        """Zwraca listę mappingów jako list[dict].

        Opcjonalne filtry: standard, regulation, reason.
        Parametr fmt jest przyjmowany dla spójności interfejsu,
        ale samo formatowanie leży po stronie wywołującego.
        """
        sql, params = build_list_query(standard, regulation, reason)
        rows = self.conn.execute(sql, params).fetchall()
        return [dict(r) for r in rows]

    def add_regulation_mapping(
        self,
        doc_path: str,
        regulation_code: str,
        match_reason: str = "explicit_audit",
    ) -> None:
        """Dodaje (lub aktualizuje) przypisanie dokumentu do regulacji."""
        self.conn.execute(
            """
            INSERT INTO doc_regulation_mapping (doc_path, regulation_code, match_reason)
            VALUES (?, ?, ?)
            ON CONFLICT(doc_path, regulation_code) DO UPDATE
                SET match_reason = excluded.match_reason
            """,
            (doc_path, regulation_code, match_reason),
        )
        self._log_changelog(
            doc_path,
            "mapping_add",
            f"regulation={regulation_code} reason={match_reason}",
        )
        self.conn.commit()
        print(f"[OK]   Przypisano '{doc_path}' do regulacji '{regulation_code}'")

    def show_stats(self) -> None:
        """Wyświetla statystyki mappingów w bazie."""
        std_count = self.conn.execute("SELECT COUNT(*) FROM doc_standard_mapping").fetchone()[0]
        reg_count = self.conn.execute("SELECT COUNT(*) FROM doc_regulation_mapping").fetchone()[0]
        gap_count = self.conn.execute("SELECT COUNT(*) FROM gap_analysis").fetchone()[0]

        sep = "=" * 55
        print(f"\n{sep}")
        print("STATYSTYKI MAPPINGÓW")
        print(sep)
        print(f"  Przypisania do standardów:  {std_count:>6}")
        print(f"  Przypisania do regulacji:   {reg_count:>6}")
        print(f"  Wpisów gap_analysis:        {gap_count:>6}")

        std_rows = self.conn.execute(
            """
            SELECT standard_code, COUNT(*) AS cnt
            FROM doc_standard_mapping
            GROUP BY standard_code
            ORDER BY cnt DESC
            """
        ).fetchall()
        if std_rows:
            print(f"\n  Standardy ({len(std_rows)}):")
            for r in std_rows:
                print(f"    {r['standard_code']:<35} {r['cnt']:>4} dok.")

        reg_rows = self.conn.execute(
            """
            SELECT regulation_code, COUNT(*) AS cnt
            FROM doc_regulation_mapping
            GROUP BY regulation_code
            ORDER BY cnt DESC
            """
        ).fetchall()
        if reg_rows:
            print(f"\n  Regulacje ({len(reg_rows)}):")
            for r in reg_rows:
                print(f"    {r['regulation_code']:<35} {r['cnt']:>4} dok.")

        conf_rows = self.conn.execute(
            """
            SELECT confidence, COUNT(*) AS cnt
            FROM gap_analysis
            GROUP BY confidence
            ORDER BY cnt DESC
            """
        ).fetchall()
        if conf_rows:
            print("\n  Confidence (gap_analysis):")
            for r in conf_rows:
                label = r["confidence"] or "brak"
                print(f"    {label:<12} {r['cnt']:>5}")

        print(f"{sep}\n")

    def close(self) -> None:
        self.conn.close()


# ---------------------------------------------------------------------------
# Wyświetlanie wyników (CLI helpers)
# ---------------------------------------------------------------------------

_DEFAULT_WIDTHS = {
    "doc_path": 50,
    "standard_code": 22,
    "match_reason": 20,
    "confidence": 10,
    "status": 10,
}


def _print_table(rows: list) -> None:
    if not rows:
        print("  (brak wyników)")
        return
    header = format_row_table(
        {
            "doc_path": "DOKUMENT",
            "standard_code": "STANDARD",
            "match_reason": "POWÓD",
            "confidence": "CONF",
            "status": "STATUS",
        },
        _DEFAULT_WIDTHS,
    )
    sep = "-" * len(header)
    print(sep)
    print(header)
    print(sep)
    for row in rows:
        print(format_row_table(row, _DEFAULT_WIDTHS))
    print(sep)
    print(f"  Łącznie: {len(rows)}")


def _print_csv(rows: list) -> None:
    print("doc_path,standard_code,match_reason,confidence,status")
    for row in rows:
        print(format_row_csv(row))


# ---------------------------------------------------------------------------
# Parser CLI
# ---------------------------------------------------------------------------


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Zarządzanie przypisaniami dokumentów do regulacji i standardów.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "--db",
        default=str(DEFAULT_DB),
        help="Ścieżka do bazy danych SQLite",
    )

    sub = parser.add_subparsers(dest="command", metavar="KOMENDA")

    # --- add ---
    p_add = sub.add_parser("add", help="Dodaj przypisanie dokumentu do standardu")
    p_add.add_argument("--doc", required=True, help="Ścieżka dokumentu (np. core/X.md)")
    p_add.add_argument("--standard", required=True, help="Kod standardu (np. NIS2, ISO27001)")
    p_add.add_argument(
        "--reason",
        default="explicit_audit",
        help=f"Powód przypisania. Znane: {', '.join(VALID_MATCH_REASONS)}",
    )

    # --- remove ---
    p_rem = sub.add_parser("remove", help="Usuń przypisanie dokumentu od standardu")
    p_rem.add_argument("--doc", required=True, help="Ścieżka dokumentu")
    p_rem.add_argument("--standard", required=True, help="Kod standardu")

    # --- list ---
    p_list = sub.add_parser("list", help="Listuj przypisania do standardów")
    p_list.add_argument("--standard", default=None, help="Filtruj po kodzie standardu")
    p_list.add_argument("--regulation", default=None, help="Filtruj po kodzie regulacji")
    p_list.add_argument("--reason", default=None, help="Filtruj po powodzie przypisania")
    p_list.add_argument(
        "--format",
        choices=["table", "csv"],
        default="table",
        dest="fmt",
        help="Format wyjścia",
    )

    # --- add-regulation ---
    p_reg = sub.add_parser("add-regulation", help="Dodaj przypisanie dokumentu do regulacji")
    p_reg.add_argument("--doc", required=True, help="Ścieżka dokumentu")
    p_reg.add_argument(
        "--regulation", required=True, help="Kod regulacji (np. GDPR / RODO, AML/KYC)"
    )
    p_reg.add_argument(
        "--reason",
        default="explicit_audit",
        help=f"Powód przypisania. Znane: {', '.join(VALID_MATCH_REASONS)}",
    )

    # --- stats ---
    sub.add_parser("stats", help="Wyświetl statystyki mappingów")

    return parser


# ---------------------------------------------------------------------------
# Punkt wejścia
# ---------------------------------------------------------------------------


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    updater = RegulationUpdater(args.db)
    try:
        if args.command == "add":
            if not validate_match_reason(args.reason):
                print(f"[WARN] Nieznany powód '{args.reason}' — kontynuuję mimo to.")
            updater.add_standard_mapping(args.doc, args.standard, args.reason)

        elif args.command == "remove":
            updater.remove_standard_mapping(args.doc, args.standard)

        elif args.command == "list":
            rows = updater.list_mappings(
                standard=args.standard,
                regulation=args.regulation,
                reason=args.reason,
                fmt=args.fmt,
            )
            if args.fmt == "csv":
                _print_csv(rows)
            else:
                _print_table(rows)

        elif args.command == "add-regulation":
            if not validate_match_reason(args.reason):
                print(f"[WARN] Nieznany powód '{args.reason}' — kontynuuję mimo to.")
            updater.add_regulation_mapping(args.doc, args.regulation, args.reason)

        elif args.command == "stats":
            updater.show_stats()

    finally:
        updater.close()


if __name__ == "__main__":
    main()
