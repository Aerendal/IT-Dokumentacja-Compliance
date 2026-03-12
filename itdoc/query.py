"""itdoc.query — zapytania do DB: szablony po standardach, regulacjach, kontraktach i rytmie.

Wszystkie funkcje przyjmują sqlite3.Connection (z row_factory=Row).
Wyniki są zwracane jako list[dict].

Funkcje:
  find_by_standard(conn, code) → list[dict]
  find_curated_by_standard(conn, code) → list[dict]
  find_by_regulation(conn, code) → list[dict]
  get_contract(conn, doc_uid) → dict
  rhythm_upstream(conn, doc_uid, depth=2) → list[dict]
  rhythm_downstream(conn, doc_uid, depth=2) → list[dict]
  coverage_stats(conn) → dict
  find_unmapped(conn, limit=50) → list[dict]
  find_by_category(conn, category) → list[dict]
  suggest_for_doc(conn, doc_path) → list[dict]
"""

import json
import sqlite3
from typing import Optional

from itdoc.exceptions import QueryError

# match_reason values considered "high quality" for curated queries
_CURATED_REASONS = frozenset({"primary_standard", "explicit_audit"})


def find_by_standard(conn: sqlite3.Connection, code: str) -> list:
    """Zwraca szablony powiązane z danym standardem (częściowe dopasowanie kodu lub nazwy).

    Args:
        conn: Połączenie z DB (row_factory=Row).
        code: Kod lub fragment nazwy standardu (np. "ISO/IEC 27001", "ITIL").

    Returns:
        list[dict] z kluczami: doc_path, standard_code, standard_name, match_reason, title.

    Raises:
        QueryError: Gdy kod jest pusty.
    """
    if not code or not code.strip():
        raise QueryError("Kod standardu nie może być pusty")

    like = f"%{code.strip()}%"
    cur = conn.execute("""
        SELECT m.doc_path,
               m.standard_code,
               s.standard_name,
               m.match_reason,
               d.title
        FROM doc_standard_mapping m
        LEFT JOIN standards s ON s.standard_code = m.standard_code
        LEFT JOIN docs d ON d.path = m.doc_path
        WHERE m.standard_code LIKE ?
           OR s.standard_name LIKE ?
           OR s.standard_code LIKE ?
        ORDER BY m.doc_path
    """, (like, like, like))
    return [dict(r) for r in cur.fetchall()]


def find_curated_by_standard(conn: sqlite3.Connection, code: str) -> list:
    """Zwraca wyselekcjonowane szablony dla danego standardu — tylko zweryfikowane dopasowania.

    Priorytet wyników:
    1. gap_analysis (exact/high confidence) — szablony z audytu kompletności
    2. doc_standard_mapping z match_reason w {primary_standard, explicit_audit}

    Wyniki nie zawierają duplikatów. Duplikaty gap_analysis są usuwane przez deduplikację po doc_path.

    Args:
        conn: Połączenie z DB (row_factory=Row).
        code: Kod lub fragment nazwy standardu.

    Returns:
        list[dict] z kluczami: doc_path, standard_code, confidence, match_reason, title, source.
        Klucz ``source`` przyjmuje wartość "gap_analysis" lub "mapping".

    Raises:
        QueryError: Gdy kod jest pusty.
    """
    if not code or not code.strip():
        raise QueryError("Kod standardu nie może być pusty")

    like = f"%{code.strip()}%"

    # 1. gap_analysis results (exact + high confidence)
    gap_rows = conn.execute("""
        SELECT g.matched_doc_path  AS doc_path,
               g.standard_code,
               g.confidence,
               g.doc_title         AS catalog_title,
               d.title
        FROM gap_analysis g
        LEFT JOIN docs d ON d.path = g.matched_doc_path
        WHERE (g.standard_code LIKE ? OR g.standard_code LIKE ?)
          AND g.status = 'present'
          AND g.confidence IN ('exact', 'high')
        ORDER BY
            CASE g.confidence WHEN 'exact' THEN 0 ELSE 1 END,
            g.matched_doc_path
    """, (like, like)).fetchall()

    seen: set[str] = set()
    results: list[dict] = []

    for r in gap_rows:
        path = r["doc_path"]
        if path and path not in seen:
            seen.add(path)
            entry = dict(r)
            entry["match_reason"] = "gap_analysis"
            entry["source"] = "gap_analysis"
            results.append(entry)

    # 2. doc_standard_mapping with primary_standard / explicit_audit
    map_rows = conn.execute("""
        SELECT m.doc_path,
               m.standard_code,
               m.match_reason,
               d.title
        FROM doc_standard_mapping m
        LEFT JOIN docs d ON d.path = m.doc_path
        WHERE (m.standard_code LIKE ?)
          AND m.match_reason IN ('primary_standard', 'explicit_audit')
        ORDER BY m.doc_path
    """, (like,)).fetchall()

    for r in map_rows:
        path = r["doc_path"]
        if path and path not in seen:
            seen.add(path)
            entry = dict(r)
            entry["confidence"] = None
            entry["source"] = "mapping"
            results.append(entry)

    return results
    """Zwraca szablony powiązane z danym standardem (częściowe dopasowanie kodu lub nazwy).

    Args:
        conn: Połączenie z DB (row_factory=Row).
        code: Kod lub fragment nazwy standardu (np. "ISO/IEC 27001", "ITIL").

    Returns:
        list[dict] z kluczami: doc_path, standard_code, standard_name, match_reason, title.

    Raises:
        QueryError: Gdy kod jest pusty.
    """
    if not code or not code.strip():
        raise QueryError("Kod standardu nie może być pusty")

    like = f"%{code.strip()}%"
    cur = conn.execute("""
        SELECT m.doc_path,
               m.standard_code,
               s.standard_name,
               m.match_reason,
               d.title
        FROM doc_standard_mapping m
        LEFT JOIN standards s ON s.standard_code = m.standard_code
        LEFT JOIN docs d ON d.path = m.doc_path
        WHERE m.standard_code LIKE ?
           OR s.standard_name LIKE ?
           OR s.standard_code LIKE ?
        ORDER BY m.doc_path
    """, (like, like, like))
    return [dict(r) for r in cur.fetchall()]


def find_by_regulation(conn: sqlite3.Connection, code: str) -> list:
    """Zwraca szablony powiązane z daną regulacją (częściowe dopasowanie kodu).

    Args:
        conn: Połączenie z DB (row_factory=Row).
        code: Kod lub fragment nazwy regulacji (np. "UODO-PL", "KSC", "RODO").

    Returns:
        list[dict] z kluczami: doc_path, regulation_code, match_reason, title.

    Raises:
        QueryError: Gdy kod jest pusty.
    """
    if not code or not code.strip():
        raise QueryError("Kod regulacji nie może być pusty")

    like = f"%{code.strip()}%"
    cur = conn.execute("""
        SELECT m.doc_path,
               m.regulation_code,
               r.regulation_name,
               m.match_reason,
               d.title
        FROM doc_regulation_mapping m
        LEFT JOIN compliance_regulations r ON r.regulation_code = m.regulation_code
        LEFT JOIN docs d ON d.path = m.doc_path
        WHERE m.regulation_code LIKE ?
           OR r.regulation_name LIKE ?
        ORDER BY m.doc_path
    """, (like, like))
    return [dict(r) for r in cur.fetchall()]


def get_contract(conn: sqlite3.Connection, doc_uid: str) -> dict:
    """Zwraca kontrakt dokumentu: wejścia, wyjścia, bramki i wpływ.

    Args:
        conn: Połączenie z DB.
        doc_uid: ULID dokumentu.

    Returns:
        dict z kluczami: doc_uid, inputs, outputs, gates, impact.
        inputs/outputs/gates/impact są listami lub słownikami (ze sparsowanego JSON).

    Raises:
        QueryError: Gdy dokument o podanym doc_uid nie istnieje.
    """
    if not doc_uid or not doc_uid.strip():
        raise QueryError("doc_uid nie może być pusty")

    row = conn.execute(
        "SELECT * FROM contracts WHERE scope_uid = ?", (doc_uid.strip(),)
    ).fetchone()

    if row is None:
        raise QueryError(f"Brak kontraktu dla doc_uid: {doc_uid}")

    result = dict(row)
    for old_key, new_key in (
        ("inputs_json", "inputs"),
        ("outputs_json", "outputs"),
        ("gates_json", "gates"),
        ("impact_json", "impact"),
    ):
        val = result.pop(old_key, None)
        if val:
            try:
                result[new_key] = json.loads(val)
            except (json.JSONDecodeError, TypeError):
                result[new_key] = val
        else:
            result[new_key] = []
    return result


def rhythm_upstream(
    conn: sqlite3.Connection,
    doc_uid: str,
    depth: int = 2,
    edge_type: Optional[str] = None,
) -> list:
    """Zwraca dokumenty które muszą powstać PRZED danym dokumentem (upstream w rytmie).

    Przechodzi `depth` poziomów wstecz po krawędziach rhythm_edges.

    Args:
        conn: Połączenie z DB.
        doc_uid: ULID dokumentu startowego.
        depth: Głębokość przeszukiwania (domyślnie 2).
        edge_type: Filtr po typie krawędzi rhythm_type (np. "requires", "informs").
            None = wszystkie typy.

    Returns:
        list[dict] z kluczami: from_uid, to_uid, edge_type, weight, distance.
    """
    if not doc_uid or not doc_uid.strip():
        raise QueryError("doc_uid nie może być pusty")

    visited = set()
    results = []
    frontier = [doc_uid.strip()]

    for dist in range(1, depth + 1):
        if not frontier:
            break
        placeholders = ",".join("?" * len(frontier))
        params: list = list(frontier)
        edge_filter = ""
        if edge_type:
            edge_filter = " AND re.rhythm_type = ?"
            params.append(edge_type)
        rows = conn.execute(f"""
            SELECT re.from_node AS from_uid, re.to_node AS to_uid,
                   re.rhythm_type AS edge_type, re.weight
            FROM rhythm_edges re
            WHERE re.to_node IN ({placeholders}){edge_filter}
        """, params).fetchall()

        next_frontier = []
        for row in rows:
            uid = row["from_uid"]
            if uid not in visited:
                visited.add(uid)
                entry = dict(row)
                entry["distance"] = dist
                results.append(entry)
                next_frontier.append(uid)
        frontier = next_frontier

    return results


def rhythm_downstream(
    conn: sqlite3.Connection,
    doc_uid: str,
    depth: int = 2,
    edge_type: Optional[str] = None,
) -> list:
    """Zwraca dokumenty które powstają PO danym dokumencie (downstream w rytmie).

    Args:
        conn: Połączenie z DB.
        doc_uid: ULID dokumentu startowego.
        depth: Głębokość przeszukiwania (domyślnie 2).
        edge_type: Filtr po typie krawędzi rhythm_type (np. "requires", "informs").
            None = wszystkie typy.

    Returns:
        list[dict] z kluczami: from_uid, to_uid, edge_type, weight, distance.
    """
    if not doc_uid or not doc_uid.strip():
        raise QueryError("doc_uid nie może być pusty")

    visited = set()
    results = []
    frontier = [doc_uid.strip()]

    for dist in range(1, depth + 1):
        if not frontier:
            break
        placeholders = ",".join("?" * len(frontier))
        params: list = list(frontier)
        edge_filter = ""
        if edge_type:
            edge_filter = " AND re.rhythm_type = ?"
            params.append(edge_type)
        rows = conn.execute(f"""
            SELECT re.from_node AS from_uid, re.to_node AS to_uid,
                   re.rhythm_type AS edge_type, re.weight
            FROM rhythm_edges re
            WHERE re.from_node IN ({placeholders}){edge_filter}
        """, params).fetchall()

        next_frontier = []
        for row in rows:
            uid = row["to_uid"]
            if uid not in visited:
                visited.add(uid)
                entry = dict(row)
                entry["distance"] = dist
                results.append(entry)
                next_frontier.append(uid)
        frontier = next_frontier

    return results


def coverage_stats(conn: sqlite3.Connection) -> dict:
    """Zwraca szybki przegląd statystyk pokrycia biblioteki.

    Returns:
        dict z kluczami:
          - total_docs: łączna liczba szablonów
          - mapped_docs: liczba szablonów z min. 1 mapowaniem
          - unmapped_docs: liczba szablonów bez mapowania
          - coverage_pct: % pokrycia (0.0–100.0)
          - total_mappings: łączna liczba wierszy doc_standard_mapping
          - unique_standards: liczba unikalnych standardów
    """
    total = conn.execute(
        "SELECT COUNT(*) FROM docs WHERE path IS NOT NULL AND path != '' AND path != 'ORPHAN'"
    ).fetchone()[0]

    mapped = conn.execute(
        "SELECT COUNT(DISTINCT doc_path) FROM doc_standard_mapping "
        "WHERE doc_path IS NOT NULL AND doc_path != ''"
    ).fetchone()[0]

    total_mappings = conn.execute("SELECT COUNT(*) FROM doc_standard_mapping").fetchone()[0]

    unique_standards = conn.execute(
        "SELECT COUNT(DISTINCT standard_code) FROM doc_standard_mapping"
    ).fetchone()[0]

    return {
        "total_docs": total,
        "mapped_docs": mapped,
        "unmapped_docs": total - mapped,
        "coverage_pct": round(mapped / total * 100, 1) if total else 0.0,
        "total_mappings": total_mappings,
        "unique_standards": unique_standards,
    }


def find_unmapped(conn: sqlite3.Connection, limit: int = 50) -> list:
    """Zwraca szablony bez żadnego mapowania do standardów.

    Args:
        conn: Połączenie z DB.
        limit: Maksymalna liczba wyników (domyślnie 50).

    Returns:
        list[dict] z kluczami: path, title, title_norm.
    """
    if limit <= 0:
        raise QueryError("limit musi być > 0")

    rows = conn.execute("""
        SELECT d.path, d.title, d.title_norm
        FROM docs d
        WHERE d.path IS NOT NULL
          AND d.path != ''
          AND d.path != 'ORPHAN'
          AND NOT EXISTS (
              SELECT 1 FROM doc_standard_mapping m
              WHERE m.doc_path = d.path
          )
        ORDER BY d.path
        LIMIT ?
    """, (limit,)).fetchall()

    return [dict(r) for r in rows]


def find_by_category(conn: sqlite3.Connection, category: str) -> list:
    """Zwraca szablony z danej kategorii (podkatalog ścieżki).

    Kategoria to fragment ścieżki, np. "security", "compliance", "architecture".
    Dopasowanie LIKE: ścieżka zawiera '/category/' lub zaczyna się od 'category/'.

    Args:
        conn: Połączenie z DB.
        category: Nazwa kategorii (podkatalog).

    Returns:
        list[dict] z kluczami: path, title, doc_uid.

    Raises:
        QueryError: Gdy kategoria jest pusta.
    """
    if not category or not category.strip():
        raise QueryError("Kategoria nie może być pusta")

    like = f"%/{category.strip()}/%"
    rows = conn.execute("""
        SELECT path, title, doc_uid
        FROM docs
        WHERE (path LIKE ? OR path LIKE ?)
          AND path IS NOT NULL
          AND path != 'ORPHAN'
        ORDER BY path
    """, (like, f"{category.strip()}/%")).fetchall()

    return [dict(r) for r in rows]


def suggest_for_doc(conn: sqlite3.Connection, doc_path: str) -> list:
    """Zwraca sugestie standardów dla danego szablonu na podstawie candidate_match.

    Szuka w doc_standard_mapping wpisów z match_reason='candidate_match'
    dla danej ścieżki, posortowanych malejąco po confidence.

    Args:
        conn: Połączenie z DB.
        doc_path: Ścieżka do szablonu (np. "core/api_gateway.md").

    Returns:
        list[dict] z kluczami: standard_code, confidence, match_reason.
        Pusta lista jeśli brak sugestii.

    Raises:
        QueryError: Gdy doc_path jest pusty.
    """
    if not doc_path or not doc_path.strip():
        raise QueryError("doc_path nie może być pusty")

    rows = conn.execute("""
        SELECT standard_code, confidence, match_reason
        FROM doc_standard_mapping
        WHERE doc_path = ?
          AND match_reason = 'candidate_match'
        ORDER BY confidence DESC
    """, (doc_path.strip(),)).fetchall()

    return [dict(r) for r in rows]
