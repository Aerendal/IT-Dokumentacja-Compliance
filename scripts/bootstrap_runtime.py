#!/usr/bin/env python3
"""scripts/bootstrap_runtime.py — przygotowuje środowisko runtime dla świeżego klonu.

Co robi
-------
1. Sprawdza, czy .venv istnieje i ma zainstalowane repo (pip show itdoc-style).
2. Tworzy brakujące katalogi: generated_templates/{core,satellite,imported}.
3. Inicjalizuje pusty reports/it_doc_matrix_clean.db z minimalnym schematem
   (current-snapshot profile), jeśli nie istnieje.
4. Generuje przykładowy reports/alignment_log.csv z nagłówkiem, jeśli nie istnieje.
5. Instaluje pre-commit hook (scripts/install_hooks.sh).
6. Uruchamia doctor --strict jako smoke check końcowy.

Użycie
------
  python3 scripts/bootstrap_runtime.py [--skip-hook] [--skip-doctor]

Exit codes
----------
  0  bootstrap OK (doctor zielony lub --skip-doctor)
  1  bootstrap zakończony częściowym sukcesem, doctor FAIL
  2  krytyczny błąd środowiska
"""
from __future__ import annotations

import argparse
import sqlite3
import subprocess
import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parent.parent
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

REPORTS = _REPO_ROOT / "reports"
GENERATED = _REPO_ROOT / "generated_templates"
ALIGNMENT_LOG = REPORTS / "alignment_log.csv"
CURRENT_DB = REPORTS / "it_doc_matrix_clean.db"
VENV = _REPO_ROOT / ".venv"

# ---------------------------------------------------------------------------
# Minimal current-snapshot schema  (tables checked by detect_schema_profile)
# ---------------------------------------------------------------------------
_CURRENT_SCHEMA = """
CREATE TABLE IF NOT EXISTS documents_current (
    id INTEGER PRIMARY KEY,
    path TEXT NOT NULL UNIQUE,
    title TEXT NOT NULL DEFAULT '',
    title_norm TEXT NOT NULL DEFAULT '',
    source TEXT NOT NULL DEFAULT 'unknown' CHECK(source IN ('core','imported','unknown')),
    status TEXT,
    aligned INTEGER NOT NULL DEFAULT 0 CHECK(aligned IN (0,1)),
    aligned_at_utc TEXT,
    aligned_by TEXT,
    hash_sha256 TEXT,
    hash_sha256_v2 TEXT,
    template_id TEXT,
    encoding_issue INTEGER NOT NULL DEFAULT 0 CHECK(encoding_issue IN (0,1)),
    created_at_utc TEXT NOT NULL DEFAULT (datetime('now','utc')),
    updated_at_utc TEXT NOT NULL DEFAULT (datetime('now','utc'))
);
CREATE TABLE IF NOT EXISTS anomalies_current (
    id INTEGER PRIMARY KEY,
    kind TEXT NOT NULL,
    path TEXT,
    detail TEXT,
    created_at_utc TEXT NOT NULL DEFAULT (datetime('now','utc'))
);
CREATE TABLE IF NOT EXISTS snapshots (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created_at_utc TEXT NOT NULL,
    note TEXT
);
CREATE TABLE IF NOT EXISTS documents_snapshot (
    id INTEGER PRIMARY KEY,
    snapshot_id INTEGER NOT NULL REFERENCES snapshots(id),
    path TEXT NOT NULL,
    title TEXT NOT NULL DEFAULT '',
    title_norm TEXT NOT NULL DEFAULT '',
    source TEXT NOT NULL DEFAULT 'unknown',
    hash_sha256_v2 TEXT
);
CREATE TABLE IF NOT EXISTS current_build (
    id INTEGER PRIMARY KEY,
    built_at_utc TEXT NOT NULL DEFAULT (datetime('now','utc')),
    note TEXT
);
CREATE TABLE IF NOT EXISTS runs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    run_id TEXT NOT NULL UNIQUE,
    started_at_utc TEXT,
    finished_at_utc TEXT,
    status TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS path_transitions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    from_path TEXT,
    to_path TEXT,
    transition_kind TEXT,
    snapshot_id INTEGER
);
"""


def _ok(msg: str) -> None:
    print(f"  [OK ] {msg}")


def _warn(msg: str) -> None:
    print(f"  [WARN] {msg}")


def _err(msg: str) -> None:
    print(f"  [ERR] {msg}", file=sys.stderr)


# ---------------------------------------------------------------------------
# Steps
# ---------------------------------------------------------------------------

def check_venv() -> bool:
    if not VENV.exists():
        _warn(f".venv not found at {VENV}")
        _warn("  Run:")
        _warn("    python3 -m venv .venv")
        _warn("    source .venv/bin/activate")
        _warn("    pip install -e '.[dev]'")
        return False
    _ok(f".venv exists: {VENV}")
    return True


def ensure_dirs() -> None:
    for subdir in ("core", "satellite", "imported"):
        d = GENERATED / subdir
        d.mkdir(parents=True, exist_ok=True)
        _ok(f"dir ready: generated_templates/{subdir}")
    REPORTS.mkdir(parents=True, exist_ok=True)
    _ok(f"dir ready: reports/")


def init_current_db() -> None:
    if CURRENT_DB.exists():
        _ok(f"current_db exists: {CURRENT_DB} ({CURRENT_DB.stat().st_size:,} bytes)")
        return
    conn = sqlite3.connect(str(CURRENT_DB))
    for stmt in _CURRENT_SCHEMA.strip().split(";"):
        s = stmt.strip()
        if s:
            conn.execute(s)
    conn.commit()
    conn.close()
    _ok(f"current_db created: {CURRENT_DB}")


def init_alignment_log() -> None:
    if ALIGNMENT_LOG.exists():
        lines = ALIGNMENT_LOG.read_text(encoding="utf-8").splitlines()
        _ok(f"alignment_log exists: {ALIGNMENT_LOG} ({len(lines):,} lines)")
        return
    ALIGNMENT_LOG.write_text("path,aligned_rev,aligned_at,aligned_by\n", encoding="utf-8")
    _ok(f"alignment_log created (empty): {ALIGNMENT_LOG}")
    _warn("  alignment_log.csv is empty — run build_current.py after populating generated_templates/")


def install_hook(skip: bool) -> None:
    if skip:
        _warn("skipping hook installation (--skip-hook)")
        return
    hook_script = _REPO_ROOT / "scripts" / "install_hooks.sh"
    if not hook_script.exists():
        _warn(f"install_hooks.sh not found: {hook_script}")
        return
    result = subprocess.run(
        ["bash", str(hook_script)],
        cwd=str(_REPO_ROOT),
        capture_output=True,
        text=True,
    )
    if result.returncode == 0:
        _ok("pre-commit hook installed")
    else:
        _warn(f"hook install failed:\n{result.stderr.strip()}")


def run_doctor(skip: bool) -> int:
    if skip:
        _warn("skipping doctor (--skip-doctor)")
        return 0
    print("\n--- doctor --strict ---")
    result = subprocess.run(
        [sys.executable, str(_REPO_ROOT / "scripts" / "doctor.py"), "--strict"],
        cwd=str(_REPO_ROOT),
    )
    return result.returncode


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(
        description="Bootstrap runtime assets for IT-Dokumentacja repo."
    )
    parser.add_argument("--skip-hook", action="store_true", help="Pomiń instalację pre-commit hook")
    parser.add_argument("--skip-doctor", action="store_true", help="Pomiń doctor --strict na końcu")
    args = parser.parse_args()

    print("=== bootstrap_runtime.py ===")
    print(f"repo: {_REPO_ROOT}\n")

    check_venv()      # only warns, doesn't abort
    ensure_dirs()
    init_current_db()
    init_alignment_log()
    install_hook(args.skip_hook)

    doctor_exit = run_doctor(args.skip_doctor)
    if doctor_exit != 0:
        print("\nbootstrap: doctor reported failures — check output above.")
        print("  Fix issues, then re-run: python3 scripts/bootstrap_runtime.py")
        return 1

    print("\nbootstrap: OK — repo ready.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
