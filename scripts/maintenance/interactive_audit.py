#!/usr/bin/env python3
"""
interactive_audit.py

Interaktywny audytor wpisow doc_standard_mapping.
Pozwala przejrzec mapowania dokumentow do standardow i zatwierdzic (explicit_audit)
lub usunac podejrzane wpisy.

Uzycie:
    python interactive_audit.py [opcje]

Przyklady:
    python interactive_audit.py --standard ISO27001 --limit 20
    python interactive_audit.py --reason keyword_match
    python interactive_audit.py --stats
"""

import sqlite3
import os
import subprocess
import platform
import argparse
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional, List, Dict, Tuple


# ---------------------------------------------------------------------------
# Stale
# ---------------------------------------------------------------------------

VERSION = "1.0.0"

VALID_CONFIDENCE = ("exact", "high", "medium", "low")

VALID_REASONS = ("keyword_match", "explicit_audit", "extracted_from_section", "primary_standard")

ANSI_RESET  = "\033[0m"
ANSI_RED    = "\033[91m"
ANSI_YELLOW = "\033[93m"
ANSI_GREEN  = "\033[92m"
ANSI_CYAN   = "\033[96m"
ANSI_BOLD   = "\033[1m"
ANSI_DIM    = "\033[2m"

_DEFAULT_DB = (
    Path(__file__).parent.parent.parent / "reports" / "it_doc_matrix.db"
)

COMMANDS = (
    "y  - zatwierdz (ustaw match_reason='explicit_audit')",
    "n  - usun powiazanie z doc_standard_mapping",
    "s  - pomin (przejdz dalej)",
    "o  - otworz plik w edytorze",
    "q  - zapisz i wyjdz",
    "?  - pokaz te pomoc",
)


# ---------------------------------------------------------------------------
# Funkcje pomocnicze (publiczne, na potrzeby testow jednostkowych)
# ---------------------------------------------------------------------------

def format_preview(
    doc_path: str,
    standard_code: str,
    match_reason: str,
    title: Optional[str],
) -> str:
    """Zwraca czytelny podglad jednego wpisu doc_standard_mapping."""
    reason_color = {
        "keyword_match": ANSI_YELLOW,
        "explicit_audit": ANSI_GREEN,
        "extracted_from_section": ANSI_CYAN,
        "primary_standard": ANSI_GREEN,
    }.get(match_reason, ANSI_RESET)

    lines = [
        f"  Dokument: {_colored(doc_path, ANSI_CYAN)}",
        f"  Standard: {_colored(standard_code, ANSI_BOLD)}",
        f"  Powod:    {_colored(match_reason, reason_color)}",
    ]
    if title:
        lines.append(f"  Tytul:    {title}")
    return "\n".join(lines)


def build_filter_query(
    standard: Optional[str],
    reason: Optional[str],
    limit: int,
) -> Tuple[str, list]:
    """
    Buduje sparametryzowane zapytanie SELECT na doc_standard_mapping.

    Zwraca (sql, params).
    """
    conditions: List[str] = []
    params: list = []

    if standard:
        conditions.append("m.standard_code LIKE ?")
        params.append(f"%{standard}%")

    if reason:
        conditions.append("m.match_reason = ?")
        params.append(reason)

    where = ("WHERE " + " AND ".join(conditions)) if conditions else ""

    sql = f"""
        SELECT
            m.id,
            m.doc_path,
            m.standard_code,
            m.match_reason,
            g.matched_doc_title AS title
        FROM doc_standard_mapping m
        LEFT JOIN gap_analysis g
            ON g.matched_doc_path = m.doc_path
            AND g.standard_code = m.standard_code
        {where}
        ORDER BY m.id ASC
        LIMIT ?
    """
    params.append(limit)
    return sql, params


def parse_keypress(key: str) -> str:
    """
    Parsuje nacisniety klawisz.

    Zwraca jeden z: "confirm", "delete", "skip", "open", "quit", "invalid".
    """
    mapping = {
        "y": "confirm",
        "n": "delete",
        "s": "skip",
        "o": "open",
        "q": "quit",
    }
    return mapping.get(key.strip().lower(), "invalid")


# ---------------------------------------------------------------------------
# Wewnetrzne narzedzia UI
# ---------------------------------------------------------------------------

def _colored(text: str, color: str) -> str:
    if not sys.stdout.isatty():
        return text
    return f"{color}{text}{ANSI_RESET}"


def _print_separator(char: str = "-", width: int = 60) -> None:
    print(_colored(char * width, ANSI_DIM))


def _print_help() -> None:
    print(_colored("\nDostepne komendy:", ANSI_BOLD))
    for cmd in COMMANDS:
        print(f"  {cmd}")
    print()


def _progress_bar(current: int, total: int, width: int = 30) -> str:
    if total == 0:
        return "[brak wpisow]"
    filled = int(width * current / total)
    if filled < width:
        bar = "=" * filled + ">" + " " * (width - filled - 1)
    else:
        bar = "=" * width
    pct = int(100 * current / total)
    return f"[{bar}] {current}/{total} ({pct}%)"


def _open_file_in_editor(filepath: str, base_dir: str) -> None:
    full_path = os.path.join(base_dir, filepath)
    if not os.path.exists(full_path):
        print(_colored(f"  [BLAD] Plik nie istnieje: {full_path}", ANSI_RED))
        return
    try:
        if platform.system() == "Darwin":
            subprocess.call(("open", full_path))
        elif platform.system() == "Windows":
            os.startfile(full_path)  # type: ignore[attr-defined]
        else:
            subprocess.call(("xdg-open", full_path))
    except Exception as exc:
        print(_colored(f"  [BLAD] Nie mozna otworzyc pliku: {exc}", ANSI_RED))


# ---------------------------------------------------------------------------
# Klasa glowna
# ---------------------------------------------------------------------------

class InteractiveAuditor:
    """Interaktywny audytor wpisow doc_standard_mapping."""

    def __init__(
        self,
        db_path: str,
        base_dir: str,
        username: Optional[str],
        standard: Optional[str],
        reason: Optional[str],
        limit: int,
    ) -> None:
        self.db_path = db_path
        self.base_dir = base_dir
        self.username = username
        self.standard = standard
        self.reason = reason
        self.limit = limit

        if not os.path.exists(db_path):
            print(_colored(f"[BLAD] Brak pliku bazy danych: {db_path}", ANSI_RED))
            sys.exit(1)

        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row
        self._init_tables()

    # ------------------------------------------------------------------
    # Inicjalizacja tabel
    # ------------------------------------------------------------------

    def _init_tables(self) -> None:
        self.conn.executescript("""
            CREATE TABLE IF NOT EXISTS audit_log (
                id            INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp     TEXT NOT NULL,
                username      TEXT,
                mapping_id    INTEGER NOT NULL,
                doc_path      TEXT NOT NULL,
                standard_code TEXT NOT NULL,
                action        TEXT NOT NULL,
                old_reason    TEXT,
                new_reason    TEXT
            );
        """)
        self.conn.commit()

    # ------------------------------------------------------------------
    # Publiczne metody
    # ------------------------------------------------------------------

    def run(self) -> None:
        """Glowna petla interaktywna."""
        sql, params = build_filter_query(self.standard, self.reason, self.limit)
        rows = self.conn.execute(sql, params).fetchall()

        if not rows:
            print(_colored("[OK] Brak wpisow do weryfikacji.", ANSI_GREEN))
            self.conn.close()
            return

        total = len(rows)
        print(f"[INFO] Uzytkownik: {self.username or 'anonim'}")
        print(f"[INFO] Znaleziono {total} wpisow do weryfikacji.")
        _print_separator()
        print("Wpisz '?' aby zobaczyc dostepne komendy.\n")

        stats: Dict[str, int] = {"processed": 0, "confirmed": 0, "deleted": 0, "skipped": 0}

        index = 0
        while index < len(rows):
            row = rows[index]
            position = index + 1

            print(f"\n{_progress_bar(position - 1, total)}")
            _print_separator()
            print(format_preview(
                doc_path=row["doc_path"],
                standard_code=row["standard_code"],
                match_reason=row["match_reason"],
                title=row["title"],
            ))

            full_path = os.path.join(self.base_dir, row["doc_path"])
            if not os.path.exists(full_path):
                print(_colored("  [!] Plik nie istnieje na dysku!", ANSI_RED))

            result = self.process_item(row, stats)
            if result == "quit":
                break

            index += 1

        self.show_stats(stats)
        self.conn.close()

    def process_item(self, row: sqlite3.Row, stats: Dict[str, int]) -> str:
        """
        Interaktywnie przetwarza jeden wpis.

        Zwraca "quit" jesli uzytkownik wybrał [q], w przeciwnym razie "next".
        """
        while True:
            try:
                raw = input(_colored("  Akcja [y/n/s/o/q/?]: ", ANSI_BOLD)).strip()
            except (EOFError, KeyboardInterrupt):
                print(_colored("\n[INFO] Przerwano (Ctrl+C).", ANSI_YELLOW))
                return "quit"

            action = parse_keypress(raw)

            if raw == "?":
                _print_help()
                continue

            if action == "quit":
                print(_colored("\n[INFO] Wyjscie...", ANSI_DIM))
                return "quit"

            if action == "confirm":
                self.conn.execute(
                    "UPDATE doc_standard_mapping SET match_reason = ? WHERE id = ?",
                    ("explicit_audit", row["id"]),
                )
                self._log(row, "confirm", row["match_reason"], "explicit_audit")
                self.conn.commit()
                stats["confirmed"] += 1
                stats["processed"] += 1
                print(_colored("  [OK] Zatwierdzono (match_reason='explicit_audit').", ANSI_GREEN))
                return "next"

            if action == "delete":
                confirm = input("  Usunac powiazanie? [tak/nie]: ").strip().lower()
                if confirm in ("tak", "t", "yes", "y"):
                    self.conn.execute(
                        "DELETE FROM doc_standard_mapping WHERE id = ?",
                        (row["id"],),
                    )
                    self._log(row, "delete", row["match_reason"], None)
                    self.conn.commit()
                    stats["deleted"] += 1
                    stats["processed"] += 1
                    print(_colored("  [OK] Usunieto powiazanie.", ANSI_RED))
                    return "next"
                print("  Anulowano.")
                continue

            if action == "skip":
                stats["skipped"] += 1
                print(_colored("  [INFO] Pominieto.", ANSI_DIM))
                return "next"

            if action == "open":
                _open_file_in_editor(row["doc_path"], self.base_dir)
                continue

            print(_colored("  Nieznana komenda. Wpisz '?' po pomoc.", ANSI_YELLOW))

    def show_stats(self, stats: Dict[str, int]) -> None:
        """Wyswietla statystyki po zakonczeniu sesji."""
        _print_separator("=")
        print(_colored("PODSUMOWANIE SESJI", ANSI_BOLD))
        _print_separator("=")
        print(f"  Przejrzano:    {stats['processed']}")
        print(f"  Zatwierdzono:  {_colored(str(stats['confirmed']), ANSI_GREEN)}")
        print(f"  Usunieto:      {_colored(str(stats['deleted']), ANSI_RED)}")
        print(f"  Pominieto:     {stats['skipped']}")
        _print_separator()

    # ------------------------------------------------------------------
    # Wewnetrzne
    # ------------------------------------------------------------------

    def _log(
        self,
        row: sqlite3.Row,
        action: str,
        old_reason: Optional[str],
        new_reason: Optional[str],
    ) -> None:
        self.conn.execute(
            """
            INSERT INTO audit_log
                (timestamp, username, mapping_id, doc_path, standard_code,
                 action, old_reason, new_reason)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                datetime.now().isoformat(),
                self.username,
                row["id"],
                row["doc_path"],
                row["standard_code"],
                action,
                old_reason,
                new_reason,
            ),
        )


# ---------------------------------------------------------------------------
# Statystyki bez sesji interaktywnej
# ---------------------------------------------------------------------------

def _print_stats_only(conn: sqlite3.Connection) -> None:
    _print_separator("=")
    print(_colored("STATYSTYKI DOC_STANDARD_MAPPING", ANSI_BOLD))
    _print_separator("=")

    total = conn.execute("SELECT COUNT(*) FROM doc_standard_mapping").fetchone()[0]
    print(f"  Lacznie wpisow: {total}")

    print(_colored("\n  Wedlug match_reason:", ANSI_BOLD))
    for row in conn.execute(
        "SELECT match_reason, COUNT(*) FROM doc_standard_mapping GROUP BY match_reason ORDER BY 2 DESC"
    ).fetchall():
        print(f"    {(row[0] or 'NULL'):<35} {row[1]}")

    top_standards = conn.execute("""
        SELECT standard_code, COUNT(*) AS cnt
        FROM doc_standard_mapping
        GROUP BY standard_code
        ORDER BY cnt DESC
        LIMIT 10
    """).fetchall()
    if top_standards:
        print(_colored("\n  Top 10 standardow:", ANSI_BOLD))
        for row in top_standards:
            print(f"    {row[0]:<30} {row[1]}")

    pending = conn.execute(
        "SELECT COUNT(*) FROM audit_log"
    ).fetchone()[0]
    print(f"\n  Wpisow w audit_log: {pending}")

    last_sessions = conn.execute(
        "SELECT timestamp, username, action, doc_path FROM audit_log ORDER BY id DESC LIMIT 5"
    ).fetchall()
    if last_sessions:
        print(_colored("\n  Ostatnie akcje audytu:", ANSI_BOLD))
        for r in last_sessions:
            print(f"    {r[0][:16]}  {(r[1] or 'anonim'):<12}  {r[2]:<10}  {r[3][:40]}")

    _print_separator()


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Interaktywny audytor wpisow doc_standard_mapping.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "--db",
        default=str(_DEFAULT_DB),
        help="Sciezka do pliku bazy SQLite",
    )
    parser.add_argument(
        "--dir",
        default=".",
        help="Katalog bazowy z dokumentami (do otwierania plikow)",
    )
    parser.add_argument(
        "--user",
        default=None,
        help="Nazwa uzytkownika zapisywana w audit_log",
    )
    parser.add_argument(
        "--standard",
        default=None,
        metavar="CODE",
        help="Filtruj po kodzie standardu (substring)",
    )
    parser.add_argument(
        "--reason",
        default=None,
        choices=list(VALID_REASONS),
        metavar="REASON",
        help=f"Filtruj po match_reason: {', '.join(VALID_REASONS)}",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=500,
        help="Maksymalna liczba wpisow do przejrzenia",
    )
    parser.add_argument(
        "--stats",
        action="store_true",
        help="Wyswietl tylko statystyki bazy i wyjdz",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {VERSION}",
    )

    args = parser.parse_args()

    if args.stats:
        if not os.path.exists(args.db):
            print(_colored(f"[BLAD] Brak pliku bazy danych: {args.db}", ANSI_RED))
            sys.exit(1)
        conn = sqlite3.connect(args.db)
        conn.row_factory = sqlite3.Row
        _print_stats_only(conn)
        conn.close()
        sys.exit(0)

    InteractiveAuditor(
        db_path=args.db,
        base_dir=args.dir,
        username=args.user,
        standard=args.standard,
        reason=args.reason,
        limit=args.limit,
    ).run()
