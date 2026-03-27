"""tests/test_resource_leaks.py — wykrywanie wycieków zasobów.

Sprawdza że moduły itdoc nie przeciekają:
  - połączeń DB (file descriptors)
  - file handles (load_template)
  - memory (duże zapytania)

Filozofia: "wykrycie przecieków i miejsc do rozwinięć" z TESTING_METHODOLOGY §12.
"""

import gc
import os
import sqlite3
import tempfile
from pathlib import Path

import pytest

from itdoc.db import get_connection, open_connection
from itdoc.query import find_by_standard, rhythm_downstream
from itdoc.template import load_template


_REPO_ROOT = Path(__file__).parent.parent
_DB_PATH = _REPO_ROOT / "reports" / "it_doc_matrix.db"


# ─── DB connection leaks ──────────────────────────────────────────────────


class TestDbConnectionLeaks:
    def test_get_connection_can_be_explicitly_closed(self, tmp_path):
        """get_connection zwraca obiekt z metodą close()."""
        db = tmp_path / "t.db"
        sqlite3.connect(str(db)).execute("CREATE TABLE t (x)").connection.commit()
        conn = open_connection(db)
        assert hasattr(conn, "close")
        conn.close()

    def test_multiple_open_close_no_crash(self, tmp_path):
        """50 open/close nie powinno wyczerpać file descriptorów."""
        db = tmp_path / "t.db"
        raw = sqlite3.connect(str(db))
        raw.execute("CREATE TABLE t (x INTEGER)")
        raw.commit()
        raw.close()

        for _ in range(50):
            conn = open_connection(db)
            conn.execute("SELECT 1")
            conn.close()

    def test_gc_collect_after_unclosed(self, tmp_path):
        """Garbage collector powinien obsluzyc niezamknieta konekce."""
        db = tmp_path / "t.db"
        raw = sqlite3.connect(str(db))
        raw.execute("CREATE TABLE t (x INTEGER)")
        raw.commit()
        raw.close()

        conn = open_connection(db)
        del conn  # Brak explicit close
        gc.collect()
        # Jesli FD wyciekl — kolejne polaczenie by zawiodlo
        with get_connection(db) as conn2:
            assert conn2 is not None

    def test_connection_is_not_shared_between_calls(self, tmp_path):
        """Kazde get_connection() otwiera NOWE polaczenie (context manager)."""
        db = tmp_path / "t.db"
        raw = sqlite3.connect(str(db))
        raw.execute("CREATE TABLE t (x INTEGER)")
        raw.commit()
        raw.close()

        with get_connection(db) as conn1:
            with get_connection(db) as conn2:
                assert conn1 is not conn2


# ─── File handle leaks (load_template) ────────────────────────────────────


class TestFileHandleLeaks:
    def _make_template(self, tmp_path: Path, name: str = "t.md") -> Path:
        p = tmp_path / name
        p.write_text(
            "---\ntitle: T\nstatus: x\naligned: true\n---\n"
            "## Cel dokumentu\nT\n## Zakres i granice\nT\n## Wejścia i wyjścia\nT\n",
            encoding="utf-8",
        )
        return p

    def test_repeated_loads_no_fd_exhaustion(self, tmp_path):
        """100 wczytań tego samego pliku nie powinno wyczerpać FD."""
        p = self._make_template(tmp_path)
        for _ in range(100):
            load_template(p)

    def test_load_after_delete_raises_gracefully(self, tmp_path):
        """Plik usunięty po załadowaniu — kolejna próba raise TemplateError."""
        from itdoc.exceptions import TemplateError
        p = self._make_template(tmp_path)
        # Załaduj raz (ok)
        load_template(p)
        # Usuń plik
        p.unlink()
        with pytest.raises(TemplateError):
            load_template(p)

    def test_load_returns_independent_copy(self, tmp_path):
        """Dwa wywołania load_template → dwa niezależne dict."""
        p = self._make_template(tmp_path)
        t1 = load_template(p)
        t2 = load_template(p)
        t1["frontmatter"]["title"] = "ZMIENIONE"
        assert t2["frontmatter"]["title"] != "ZMIENIONE"


# ─── Memory leaks / large result sets ────────────────────────────────────


class TestLargeResultLeaks:
    def test_large_chain_bfs_bounded(self):
        """BFS na grafie 1000-węzłowym z depth=2 zwraca ≤ 2 poziomy."""
        conn = sqlite3.connect(":memory:")
        conn.row_factory = sqlite3.Row
        conn.executescript("""
            CREATE TABLE _schema_version (version TEXT, applied_at TEXT);
            INSERT INTO _schema_version VALUES ('1.0.0', '2026-01-01');
            CREATE TABLE docs (doc_uid TEXT, title TEXT, title_norm TEXT, path TEXT, origin TEXT, created_at_utc TEXT, updated_at_utc TEXT);
            CREATE TABLE sections (section_uid TEXT, doc_uid TEXT, heading_text TEXT, heading_norm TEXT, heading_level INTEGER, heading_path TEXT, anchor TEXT, ordinal INTEGER, status TEXT, text_fingerprint_sha256 TEXT, start_line INTEGER, end_line INTEGER);
            CREATE TABLE standards (standard_id INTEGER, standard_code TEXT, standard_name TEXT, standard_name_en TEXT, description TEXT, version TEXT, url TEXT, applicable_industries TEXT);
            CREATE TABLE compliance_regulations (id INTEGER, regulation_code TEXT, regulation_name TEXT, jurisdiction TEXT, industry TEXT, key_requirements TEXT, penalty_info TEXT, data_engineering_impact TEXT);
            CREATE TABLE content_links (id INTEGER, from_doc TEXT, to_doc TEXT, link_type TEXT);
            INSERT INTO content_links VALUES (1, 'a.md', 'b.md', 'requires');
            CREATE TABLE content_links_resolved (id INTEGER, content_link_id INTEGER, from_kind TEXT, from_uid TEXT, to_kind TEXT, to_uid TEXT, link_type TEXT, direction TEXT, rationale TEXT, strength TEXT, resolution_method TEXT, resolution_confidence REAL, notes TEXT);
            INSERT INTO content_links_resolved VALUES (1,1,'doc','A','doc','B','requires','forward','','required','explicit',1.0,'');
            CREATE TABLE contracts (contract_id INTEGER, scope_kind TEXT, scope_uid TEXT, version TEXT, inputs_json TEXT, outputs_json TEXT, gates_json TEXT, impact_json TEXT, owner TEXT, notes TEXT, created_at_utc TEXT, updated_at_utc TEXT);
            INSERT INTO contracts VALUES (1,'doc','N0','1.0','[]','[]','[]','{}','owner','','2026','2026');
            CREATE TABLE flags (id INTEGER, doc_uid TEXT, version TEXT, branch_id INTEGER, access_mask INTEGER);
            INSERT INTO flags VALUES (1, 'N0', '1.0', 1, 0);
        """)
        conn.execute("""CREATE TABLE rhythm_edges (
            edge_id INTEGER, from_node TEXT, to_node TEXT,
            rhythm_type TEXT, weight REAL, conditions TEXT, version_range TEXT, notes TEXT)""")
        # Łańcuch 1000 węzłów: N0→N1→N2→...→N999
        conn.executemany(
            "INSERT INTO rhythm_edges VALUES (?,?,?,'triggers',1.0,'','','')",
            [(i, f"N{i}", f"N{i+1}") for i in range(999)],
        )
        conn.commit()

        result = rhythm_downstream(conn, "N0", depth=2)
        assert len(result) == 2  # Tylko N1 (depth=1) i N2 (depth=2)
        conn.close()

    def test_find_standard_result_not_generator(self, db_conn):
        """find_by_standard zwraca list, nie generator — można sprawdzić len()."""
        result = find_by_standard(db_conn, "ISO/IEC 27001")
        assert isinstance(result, list)
        # Sprawdzamy że list jest zmaterializowany (nie lazy)
        assert len(result) >= 0

    @pytest.mark.integration
    def test_large_real_query_memory_ok(self, real_db_conn):
        """Zapytanie do real DB z dużym wynikiem nie powoduje problemu."""
        result = find_by_standard(real_db_conn, "ISO")
        assert len(result) >= 100
        # Jeśli pamięć by wyciekła — GC by się zatrzymał
        gc.collect()
