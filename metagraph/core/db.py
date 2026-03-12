import sqlite3
from pathlib import Path
from contextlib import contextmanager
from typing import Generator

DEFAULT_DB_PATH = Path(__file__).parent.parent / "metagraph.db"
MIGRATIONS_DIR = Path(__file__).parent.parent / "migrations"


def get_db_path() -> Path:
    """Zwraca ścieżkę do bazy danych (z config lub domyślna)."""
    import os
    return Path(os.environ.get("METAGRAPH_DB", str(DEFAULT_DB_PATH)))


def init_db(db_path: Path | None = None) -> sqlite3.Connection:
    """Inicjalizuje bazę danych i uruchamia migracje."""
    path = db_path or get_db_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(path))
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA foreign_keys=ON")
    _run_migrations(conn)
    return conn


def _run_migrations(conn: sqlite3.Connection) -> None:
    for sql_file in sorted(MIGRATIONS_DIR.glob("*.sql")):
        with open(sql_file) as f:
            conn.executescript(f.read())
    conn.commit()


@contextmanager
def get_conn(db_path: Path | None = None) -> Generator[sqlite3.Connection, None, None]:
    conn = init_db(db_path)
    try:
        yield conn
    finally:
        conn.close()
