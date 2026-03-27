#!/usr/bin/env python3
"""scripts/doctor.py — diagnostyka kontraktu artefaktów repozytorium.

Sprawdza, czy wszystkie artefakty runtime są obecne i mają właściwy profil.
Uruchamiaj przed testami integracyjnymi i pipeline.

Użycie:
    python3 scripts/doctor.py            # raport, wyjście 0 nawet przy FAILach
    python3 scripts/doctor.py --strict   # wyjście 1 przy pierwszym FAILu
"""
from __future__ import annotations

import argparse
import sqlite3
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]

# Ensure repo root is on path so itdoc package can be imported
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))
REPORTS = REPO_ROOT / "reports"
GENERATED = REPO_ROOT / "generated_templates"
PIPELINE_CFG = REPO_ROOT / "config" / "pipeline_policy.yaml"
LEGACY_DB = REPORTS / "it_doc_matrix.db"
CURRENT_DB = REPORTS / "it_doc_matrix_clean.db"
ALIGNMENT_LOG = REPORTS / "alignment_log.csv"


def _open(db_path: Path) -> sqlite3.Connection:
    conn = sqlite3.connect(str(db_path))
    conn.row_factory = sqlite3.Row
    return conn


def check_db_profile(db_path: Path, expected: str) -> tuple[bool, str]:
    if not db_path.exists():
        return False, f"missing: {db_path}"
    conn = _open(db_path)
    try:
        from itdoc.schema_profile import detect_schema_profile
        detected = detect_schema_profile(conn)
        if detected.profile != expected:
            return (
                False,
                f"profile={detected.profile}, expected={expected}, "
                f"missing={sorted(detected.missing_required)}",
            )
        return True, f"profile={detected.profile}"
    finally:
        conn.close()


def check_path(path: Path, kind: str = "path") -> tuple[bool, str]:
    if not path.exists():
        return False, f"{kind} missing: {path}"
    return True, f"{kind} ok"


def check_pipeline_policy(cfg_path: Path) -> tuple[bool, str]:
    if not cfg_path.exists():
        return False, f"file missing: {cfg_path}"
    try:
        import yaml  # type: ignore
        data = yaml.safe_load(cfg_path.read_text(encoding="utf-8"))
        cmd = data.get("commands", {}).get("build_current_cmd", [])
        if cmd and cmd[0] not in ("true", "/bin/true", "python3"):
            script = next((c for c in cmd if c.endswith(".py")), None)
            if script:
                script_path = REPO_ROOT / script
                if not script_path.exists():
                    return (
                        False,
                        f"build_current_cmd points to missing script: {script}",
                    )
    except ImportError:
        pass  # yaml not installed — skip deep check
    except Exception as exc:
        return False, f"parse error: {exc}"
    return True, "config ok"


def main() -> int:
    parser = argparse.ArgumentParser(description="Diagnostyka artefaktów repozytorium")
    parser.add_argument(
        "--strict", action="store_true",
        help="Zakończ z kodem 1 przy pierwszym FAILu"
    )
    args = parser.parse_args()

    checks: list[tuple[str, bool, str]] = [
        ("generated_templates",          *check_path(GENERATED, "dir")),
        ("generated_templates/core",     *check_path(GENERATED / "core", "dir")),
        ("generated_templates/satellite",*check_path(GENERATED / "satellite", "dir")),
        ("legacy_db",                    *check_db_profile(LEGACY_DB, "legacy-runtime")),
        ("current_db",                   *check_db_profile(CURRENT_DB, "current-snapshot")),
        ("alignment_log",                *check_path(ALIGNMENT_LOG, "file")),
        ("pipeline_policy",              *check_pipeline_policy(PIPELINE_CFG)),
    ]

    failed: list[str] = []
    for name, ok, msg in checks:
        status = "OK  " if ok else "FAIL"
        print(f"[{status}] {name}: {msg}")
        if not ok:
            failed.append(name)

    if failed:
        print(f"\n{len(failed)} check(s) FAILED: {', '.join(failed)}")
        if args.strict:
            return 1
    else:
        print("\nAll checks passed.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
