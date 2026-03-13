#!/usr/bin/env python3
"""
seed_base_dicts.py — Zasiewa słowniki bazowe do bazy danych IT Dokumentacja.
Dane słowników: config/base_dicts/*.yaml
"""

from __future__ import annotations

import sqlite3
from pathlib import Path

import yaml

DB_PATH = Path(__file__).parent.parent / "reports" / "it_doc_matrix.db"
_BASE_DICTS_DIR = Path(__file__).parent.parent / "config" / "base_dicts"


def _load_dict(name: str) -> list[dict]:
    """Wczytuje słownik z config/base_dicts/{name}.yaml, zwraca listę dict."""
    path = _BASE_DICTS_DIR / f"{name}.yaml"
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    # Każdy plik ma jeden klucz główny z listą wpisów
    return next(iter(data.values()))


def _load_as_tuples(name: str, fields: list[str]) -> list[tuple]:
    """Wczytuje słownik i konwertuje do listy krotek (backward compat)."""
    return [tuple(entry[f] for f in fields) for entry in _load_dict(name)]


ROLES = _load_as_tuples("roles", ["code", "name_pl", "name_en", "description"])
PHASES = _load_as_tuples("phases", ["number", "name_pl", "name_en", "category", "is_iterative", "description"])
INDUSTRIES = _load_as_tuples("industries", ["code", "name_pl", "name_en", "category"])
DOC_CATEGORIES = _load_as_tuples("document_categories", ["code", "name_pl", "name_en", "description", "color_hex"])
REL_TYPES = _load_as_tuples("rel_types", ["code", "name_pl", "name_en", "is_bidirectional", "description"])
QUALITY_DIMS = _load_as_tuples("quality_dims", ["dimension", "name_pl", "name_en", "description",
                                                 "measurement_method", "example_checks",
                                                 "good_threshold", "target_threshold", "tools"])

# ---------------------------------------------------------------------------

def main():
    conn = sqlite3.connect(str(DB_PATH))
    cur = conn.cursor()

    # Check columns for each table before inserting
    def get_cols(table):
        cur.execute(f'PRAGMA table_info("{table}")')
        return {r[1] for r in cur.fetchall()}

    results = {}

    # roles
    cols = get_cols("roles")
    if "role_name_pl" in cols:
        cur.executemany(
            "INSERT OR IGNORE INTO roles (role_code, role_name_pl, role_name_en, description) VALUES (?,?,?,?)",
            [(r[0], r[1], r[2], r[3]) for r in ROLES],
        )
    elif "role_name" in cols:
        cur.executemany(
            "INSERT OR IGNORE INTO roles (role_code, role_name, description) VALUES (?,?,?)",
            [(r[0], r[1], r[3]) for r in ROLES],
        )
    results["roles"] = len(ROLES)

    # phases
    cols = get_cols("phases")
    if "phase_number" in cols and "phase_name_pl" in cols:
        rows = [(p[0], p[1], p[2], p[3], 1 if p[4] else 0, p[5]) for p in PHASES]
        cur.executemany(
            """INSERT OR IGNORE INTO phases
            (phase_number, phase_name_pl, phase_name_en, phase_category, is_iterative, phase_description)
            VALUES (?,?,?,?,?,?)""",
            rows,
        )
    elif "phase_number" in cols and "name_pl" in cols:
        rows = [(p[0], p[1], p[2], p[3]) for p in PHASES]
        cur.executemany(
            "INSERT OR IGNORE INTO phases (phase_number, name_pl, name_en, phase_category) VALUES (?,?,?,?)",
            rows,
        )
    elif "phase_number" in cols:
        rows = [(p[0], p[1], p[3]) for p in PHASES]
        cur.executemany(
            "INSERT OR IGNORE INTO phases (phase_number, name, phase_category) VALUES (?,?,?)", rows
        )
    results["phases"] = len(PHASES)

    # industries
    cols = get_cols("industries")
    if "industry_code" in cols and "name_pl" in cols:
        rows = [(r[0], r[1], r[2], r[3]) for r in INDUSTRIES]
        cur.executemany(
            "INSERT OR IGNORE INTO industries (industry_code, name_pl, name_en, category) VALUES (?,?,?,?)",
            rows,
        )
    elif "industry_code" in cols and "industry_name_pl" in cols:
        rows = [(r[0], r[1], r[2], r[3]) for r in INDUSTRIES]
        cur.executemany(
            "INSERT OR IGNORE INTO industries (industry_code, industry_name_pl, industry_name_en, category) VALUES (?,?,?,?)",
            rows,
        )
    elif "industry_code" in cols:
        rows = [(r[0], r[1]) for r in INDUSTRIES]
        cur.executemany("INSERT OR IGNORE INTO industries (industry_code, name) VALUES (?,?)", rows)
    results["industries"] = len(INDUSTRIES)

    # document_categories
    cols = get_cols("document_categories")
    if "category_code" in cols and "category_name_pl" in cols:
        rows = [(r[0], r[1], r[2], r[3], r[4]) for r in DOC_CATEGORIES]
        cur.executemany(
            """INSERT OR IGNORE INTO document_categories
            (category_code, category_name_pl, category_name_en, description, color_hex)
            VALUES (?,?,?,?,?)""",
            rows,
        )
    elif "category_code" in cols and "category_name_en" in cols:
        rows = [(r[0], r[2], r[3]) for r in DOC_CATEGORIES]
        cur.executemany(
            "INSERT OR IGNORE INTO document_categories (category_code, category_name_en, description) VALUES (?,?,?)",
            rows,
        )
    elif "category_code" in cols:
        rows = [(r[0], r[1]) for r in DOC_CATEGORIES]
        cur.executemany(
            "INSERT OR IGNORE INTO document_categories (category_code, description) VALUES (?,?)",
            rows,
        )
    results["document_categories"] = len(DOC_CATEGORIES)

    # relationship_types
    cols = get_cols("relationship_types")
    if "rel_type_code" in cols and "rel_type_name_pl" in cols:
        rows = [(r[0], r[1], r[2], 1 if r[3] else 0, r[4]) for r in REL_TYPES]
        cur.executemany(
            """INSERT OR IGNORE INTO relationship_types
            (rel_type_code, rel_type_name_pl, rel_type_name_en, is_bidirectional, description)
            VALUES (?,?,?,?,?)""",
            rows,
        )
    elif "rel_type_code" in cols:
        rows = [(r[0], r[2], r[4]) for r in REL_TYPES]
        cur.executemany(
            "INSERT OR IGNORE INTO relationship_types (rel_type_code, rel_type_name_en, description) VALUES (?,?,?)",
            rows,
        )
    elif "rel_code" in cols:
        rows = [(r[0], r[2], r[1], r[4]) for r in REL_TYPES]
        cur.executemany(
            "INSERT OR IGNORE INTO relationship_types (rel_code, rel_name_en, rel_name_pl, description) VALUES (?,?,?,?)",
            rows,
        )
    results["relationship_types"] = len(REL_TYPES)

    # quality_dimensions
    cols = get_cols("quality_dimensions")
    if "dimension" in cols and "name" in cols:
        for r in QUALITY_DIMS:
            try:
                cur.execute(
                    """INSERT OR IGNORE INTO quality_dimensions
                    (dimension, name, description, measurement_method, example_checks, good_threshold, target_threshold, tools)
                    VALUES (?,?,?,?,?,?,?,?)""",
                    (r[0], r[1], r[3], r[4], r[5], r[6], r[7], r[8]),
                )
            except Exception:
                # fallback — fewer columns
                try:
                    cur.execute(
                        "INSERT OR IGNORE INTO quality_dimensions (dimension, name, description) VALUES (?,?,?)",
                        (r[0], r[1], r[3]),
                    )
                except Exception as exc:
                    _log.debug(
                        "quality_dimensions fallback insert failed: %s: %s", type(exc).__name__, exc
                    )
    results["quality_dimensions"] = len(QUALITY_DIMS)

    conn.commit()
    conn.close()

    print("Faza 9A — Zasilenie słowników bazowych:")
    for table, n in results.items():
        print(f"  {table:25s}: {n} wierszy")
    print("\nGotowe.")


if __name__ == "__main__":
    main()
