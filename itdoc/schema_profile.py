"""itdoc.schema_profile — jawna detekcja i weryfikacja profilu schematu bazy danych.

Dwa obsługiwane profile:
  legacy-runtime   — używany przez itdoc/*, scripts/new_template_wizard.py,
                     scripts/compliance_*.py, scripts/api/main.py
  current-snapshot — używany przez scripts/pipeline_run.py, config/pipeline_policy.yaml

Użycie:
    from itdoc.schema_profile import detect_schema_profile, assert_schema_profile

    check = detect_schema_profile(conn)
    # check.profile -> "legacy-runtime" | "current-snapshot" | "unknown"

    assert_schema_profile(conn, "legacy-runtime")
    # rzuca RuntimeError gdy profil nie pasuje
"""
from __future__ import annotations

import sqlite3
from dataclasses import dataclass
from typing import Literal

SchemaProfile = Literal["legacy-runtime", "current-snapshot", "unknown"]

LEGACY_REQUIRED: frozenset[str] = frozenset({
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
})

CURRENT_REQUIRED: frozenset[str] = frozenset({
    "documents_current",
    "documents_snapshot",
    "anomalies_current",
    "document_tags_current",
    "snapshots",
    "current_build",
    "runs",
})

OPTIONAL_LEGACY: frozenset[str] = frozenset({
    "doc_standard_mapping",
    "doc_regulation_mapping",
    "gap_analysis",
    "doc_section_guidance",
})


@dataclass(frozen=True)
class ProfileCheck:
    profile: SchemaProfile
    existing_tables: frozenset[str]
    missing_required: frozenset[str]


def list_tables(conn: sqlite3.Connection) -> frozenset[str]:
    """Zwraca zbiór nazw tabel w bazie."""
    cur = conn.execute("SELECT name FROM sqlite_master WHERE type='table'")
    return frozenset(row[0] for row in cur.fetchall())


def detect_schema_profile(conn: sqlite3.Connection) -> ProfileCheck:
    """Wykrywa profil schematu na podstawie obecności wymaganych tabel.

    Returns:
        ProfileCheck z profile="legacy-runtime" gdy wszystkie tabele LEGACY_REQUIRED istnieją,
        profile="current-snapshot" gdy wszystkie CURRENT_REQUIRED istnieją,
        profile="unknown" w przeciwnym razie (missing_required = krótszy brakujący zbiór).
    """
    existing = list_tables(conn)
    missing_legacy = LEGACY_REQUIRED - existing
    missing_current = CURRENT_REQUIRED - existing

    if not missing_legacy:
        return ProfileCheck(
            profile="legacy-runtime",
            existing_tables=existing,
            missing_required=frozenset(),
        )
    if not missing_current:
        return ProfileCheck(
            profile="current-snapshot",
            existing_tables=existing,
            missing_required=frozenset(),
        )

    # Zwróć profil bliższy (mniej brakujących tabel)
    closer_missing = missing_legacy if len(missing_legacy) <= len(missing_current) else missing_current
    return ProfileCheck(
        profile="unknown",
        existing_tables=existing,
        missing_required=closer_missing,
    )


def assert_schema_profile(
    conn: sqlite3.Connection,
    expected: SchemaProfile,
) -> None:
    """Wymusza profil schematu. Rzuca RuntimeError gdy profil nie zgadza się z oczekiwanym.

    Args:
        conn: Połączenie z SQLite.
        expected: Oczekiwany profil ("legacy-runtime" lub "current-snapshot").

    Raises:
        RuntimeError: Gdy wykryty profil różni się od oczekiwanego.
    """
    if expected == "unknown":
        return
    detected = detect_schema_profile(conn)
    if detected.profile != expected:
        raise RuntimeError(
            f"Schema profile mismatch: expected={expected}, got={detected.profile}, "
            f"missing_required={sorted(detected.missing_required)}"
        )


def list_missing_tables(conn: sqlite3.Connection, profile: SchemaProfile) -> list[str]:
    """Zwraca listę brakujących tabel dla danego profilu.

    Args:
        conn: Połączenie z SQLite.
        profile: Profil do sprawdzenia ("legacy-runtime" lub "current-snapshot").

    Returns:
        Posortowana lista brakujących tabel. Pusta lista = schemat kompletny.
    """
    existing = list_tables(conn)
    if profile == "legacy-runtime":
        return sorted(LEGACY_REQUIRED - existing)
    if profile == "current-snapshot":
        return sorted(CURRENT_REQUIRED - existing)
    return []


def has_tables(conn: sqlite3.Connection, tables: set[str]) -> bool:
    """Sprawdza czy wszystkie podane tabele istnieją w bazie."""
    existing = list_tables(conn)
    return tables.issubset(existing)
