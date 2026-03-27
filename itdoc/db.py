"""itdoc.db — zarzadzanie polaczeniem z DB i walidacja schematu.

Funkcje:
  get_connection(db_path=None) -> context manager / sqlite3.Connection
  validate_schema(conn, on_error=None, expected_profile="legacy-runtime") -> list[str]
  validate_current_snapshot_schema(conn, on_error=None) -> list[str]
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
from contextlib import contextmanager
from pathlib import Path
from typing import Callable, Generator, List, Optional

from itdoc.exceptions import SchemaError
from itdoc.schema_profile import (
    CURRENT_REQUIRED,
    LEGACY_REQUIRED,
    detect_schema_profile,
)

_DEFAULT_DB = Path(__file__).parent.parent / "reports" / "it_doc_matrix.db"

# Zachowane dla kompatybilności wstecznej — używaj LEGACY_REQUIRED z schema_profile
_REQUIRED_TABLES = sorted(LEGACY_REQUIRED)


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
    expected_profile: str = "legacy-runtime",
) -> list:
    """Sprawdza profil schematu i niepustosc kluczowych tabel.

    Najpierw weryfikuje profil DB (legacy-runtime lub current-snapshot),
    potem sprawdza niepustosc tabel wymaganego profilu.

    Args:
        conn: Polaczenie z DB.
        on_error: Opcjonalny callback (error_msg: str) -> None wywolywany
            dla kazdego znalezionego bledu.
        expected_profile: Oczekiwany profil schematu (domyslnie "legacy-runtime").

    Returns:
        Lista bledow (stringow). Pusta lista = schema OK.
    """
    errors: List[str] = []

    detected = detect_schema_profile(conn)
    if detected.profile != expected_profile:
        msg = (
            f"Schema profile mismatch: expected={expected_profile}, "
            f"got={detected.profile}, "
            f"missing_required={sorted(detected.missing_required)}"
        )
        errors.append(msg)
        if on_error:
            on_error(msg)
        return errors

    for table in sorted(LEGACY_REQUIRED):
        count = conn.execute(f"SELECT COUNT(*) FROM [{table}]").fetchone()[0]
        if count == 0:
            msg = f"Pusta tabela: {table}"
            errors.append(msg)
            if on_error:
                on_error(msg)

    return errors


def validate_current_snapshot_schema(
    conn: sqlite3.Connection,
    on_error: Optional[Callable[[str], None]] = None,
) -> list:
    """Sprawdza profil current-snapshot i niepustosc jego tabel.

    Args:
        conn: Polaczenie z DB.
        on_error: Opcjonalny callback (error_msg: str) -> None.

    Returns:
        Lista bledow. Pusta lista = schema OK.
    """
    errors: List[str] = []

    detected = detect_schema_profile(conn)
    if detected.profile != "current-snapshot":
        msg = (
            "Schema profile mismatch: expected=current-snapshot, "
            f"got={detected.profile}, "
            f"missing_required={sorted(detected.missing_required)}"
        )
        errors.append(msg)
        if on_error:
            on_error(msg)
        return errors

    for table in sorted(CURRENT_REQUIRED):
        count = conn.execute(f"SELECT COUNT(*) FROM [{table}]").fetchone()[0]
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
