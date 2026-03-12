"""itdoc.db — zarzadzanie polaczeniem z DB i walidacja schematu.

Funkcje:
  get_connection(db_path=None) -> context manager / sqlite3.Connection
  validate_schema(conn, on_error=None) -> list[str]
  check_link_resolution_coverage(conn) -> float

Uzycie (zalecane):
    with get_connection() as conn:
        rows = conn.execute("SELECT * FROM docs").fetchall()

Uzycie (klasyczne — wymaga recznego .close()):
    conn = get_connection()
    try: ...
    finally: conn.close()
"""

import sqlite3
from collections.abc import Generator
from contextlib import contextmanager
from pathlib import Path
from typing import Callable, Optional

from itdoc.exceptions import SchemaError

_DEFAULT_DB = Path(__file__).parent.parent / "reports" / "it_doc_matrix.db"

_REQUIRED_TABLES = [
    "docs",
    "sections",
    "standards",
    "compliance_regulations",
    "content_links",
    "content_links_resolved",
    "rhythm_edges",
    "contracts",
    "flags",
    "_schema_version",
]


def _open_connection(db_path: Optional[Path] = None) -> sqlite3.Connection:
    """Otwiera i konfiguruje polaczenie (wewnetrzna)."""
    path = Path(db_path) if db_path else _DEFAULT_DB
    if not path.exists():
        raise FileNotFoundError(f"DB not found: {path}")
    conn = sqlite3.connect(str(path), timeout=30)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    return conn


@contextmanager
def get_connection(db_path: Optional[Path] = None) -> Generator[sqlite3.Connection, None, None]:
    """Context manager — otwiera polaczenie z DB i zamyka je automatycznie.

    Args:
        db_path: Sciezka do pliku .db. Jesli None, uzywa domyslnej DB.

    Raises:
        FileNotFoundError: Gdy plik DB nie istnieje.
    """
    conn = _open_connection(db_path)
    try:
        yield conn
    finally:
        conn.close()


def validate_schema(
    conn: sqlite3.Connection,
    on_error: Optional[Callable[[str], None]] = None,
) -> list:
    """Sprawdza obecnosc i niepustosc kluczowych tabel.

    Args:
        conn: Polaczenie z DB.
        on_error: Opcjonalny callback (error_msg: str) -> None wywolywany
            dla kazdego znalezionego bledu (np. do logowania lub alertow).
            None = tylko zbierz bledy w liscie.

    Returns:
        Lista bledow (stringow). Pusta lista = schema OK.
    """
    errors: list[str] = []
    cur = conn.execute("SELECT name FROM sqlite_master WHERE type='table'")
    existing = {row[0] for row in cur.fetchall()}

    for table in _REQUIRED_TABLES:
        if table not in existing:
            msg = f"Brakujaca tabela: {table}"
            errors.append(msg)
            if on_error:
                on_error(msg)
            continue
        count = conn.execute(
            f"SELECT COUNT(*) FROM [{table}]"  # nosec B608 -- table from hardcoded _REQUIRED_TABLES whitelist, not user input
        ).fetchone()[0]
        if count == 0:
            msg = f"Pusta tabela: {table}"
            errors.append(msg)
            if on_error:
                on_error(msg)

    return errors


def check_link_resolution_coverage(conn: sqlite3.Connection) -> float:
    """Zwraca pokrycie resolucji linkow: resolved / total.

    Returns:
        Float 0.0-1.0. Zwraca 0.0 gdy nie ma zadnych linkow.

    Raises:
        SchemaError: Gdy tabele content_links lub content_links_resolved nie istnieja.
    """
    cur = conn.execute("SELECT name FROM sqlite_master WHERE type='table'")
    existing = {row[0] for row in cur.fetchall()}

    for t in ("content_links", "content_links_resolved"):
        if t not in existing:
            raise SchemaError(f"Brakujaca tabela: {t}")

    total = conn.execute("SELECT COUNT(*) FROM content_links").fetchone()[0]
    if total == 0:
        return 0.0

    resolved = conn.execute("SELECT COUNT(*) FROM content_links_resolved").fetchone()[0]
    return resolved / total


# Backward-compatible alias — zwraca polaczenie bezposrednio (wymaga recznego .close())
# Uzyj get_connection() (context manager) dla nowego kodu.
open_connection = _open_connection
