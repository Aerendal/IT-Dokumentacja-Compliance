from __future__ import annotations

import sqlite3
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
GRAPH_DIR = BASE_DIR / "scripts" / "graph_engine"
DDL_PATH = GRAPH_DIR / "ddl_nodes.sql"


def apply_ddl_tolerant(conn: sqlite3.Connection) -> None:
    cur = conn.cursor()
    sql = DDL_PATH.read_text(encoding="utf-8")
    buffer = []
    for line in sql.splitlines():
        buffer.append(line)
        chunk = "\n".join(buffer).strip()
        if not chunk or not sqlite3.complete_statement(chunk):
            continue
        try:
            cur.execute(chunk)
        except sqlite3.OperationalError as exc:
            if "duplicate column name" in str(exc).lower():
                buffer = []
                continue
            raise
        buffer = []
    conn.commit()


def create_base_schema(conn: sqlite3.Connection) -> None:
    conn.executescript(
        """
        CREATE TABLE sync_runs(
          sync_id TEXT PRIMARY KEY,
          ran_at_utc TEXT NOT NULL,
          kind TEXT NOT NULL,
          status TEXT NOT NULL,
          notes TEXT
        );

        CREATE TABLE docs(
          doc_uid TEXT PRIMARY KEY,
          title TEXT NOT NULL,
          title_norm TEXT NOT NULL,
          path TEXT,
          origin TEXT NOT NULL DEFAULT 'unknown',
          created_at_utc TEXT NOT NULL,
          updated_at_utc TEXT NOT NULL
        );

        CREATE TABLE sections(
          section_uid TEXT PRIMARY KEY,
          doc_uid TEXT NOT NULL,
          heading_text TEXT NOT NULL,
          heading_norm TEXT NOT NULL,
          heading_level INTEGER NOT NULL,
          heading_path TEXT NOT NULL,
          anchor TEXT NOT NULL,
          ordinal INTEGER NOT NULL,
          status TEXT NOT NULL DEFAULT 'unknown',
          text_fingerprint_sha256 TEXT,
          start_line INTEGER,
          end_line INTEGER
        );

        CREATE TABLE edges(
          edge_uid TEXT PRIMARY KEY,
          from_kind TEXT NOT NULL,
          from_uid TEXT NOT NULL,
          to_kind TEXT NOT NULL,
          to_uid TEXT NOT NULL,
          link_type TEXT NOT NULL,
          direction TEXT NOT NULL,
          rationale TEXT,
          strength TEXT NOT NULL DEFAULT 'navigational',
          impact_area TEXT,
          impact_level TEXT,
          source TEXT NOT NULL,
          source_row_id INTEGER
        );
        """
    )


def seed_minimal_data(conn: sqlite3.Connection) -> None:
    cur = conn.cursor()
    cur.executemany(
        """
        INSERT INTO docs(doc_uid,title,title_norm,path,origin,created_at_utc,updated_at_utc)
        VALUES(?,?,?,?,?,?,?)
        """,
        [
            ("doc-1", "Doc One", "doc one", "a.md", "core", "2026-01-01T00:00:00Z", "2026-01-01T00:00:00Z"),
            ("doc-2", "Doc Two", "doc two", "b.md", "core", "2026-01-01T00:00:00Z", "2026-01-01T00:00:00Z"),
        ],
    )
    cur.executemany(
        """
        INSERT INTO sections(
          section_uid,doc_uid,heading_text,heading_norm,heading_level,heading_path,anchor,ordinal,status,
          text_fingerprint_sha256,start_line,end_line
        ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)
        """,
        [
            ("sec-1", "doc-1", "S1", "s1", 2, "S1", "s1", 1, "ok", None, 1, 2),
            ("sec-2", "doc-2", "S2", "s2", 2, "S2", "s2", 1, "ok", None, 3, 4),
        ],
    )
    cur.executemany(
        """
        INSERT INTO edges(
          edge_uid,from_kind,from_uid,to_kind,to_uid,link_type,direction,rationale,strength,impact_area,impact_level,source,source_row_id
        ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)
        """,
        [
            ("e1", "doc", "doc-1", "section", "sec-1", "depends_on", "forward", "ok", "required", None, None, "doc_section_links", 1),
            ("e2", "doc", "doc-1", "section", "missing-node", "depends_on", "forward", "skip", "required", None, None, "doc_section_links", 2),
            ("e3", "section", "section::raw-ref", "doc", "doc-2", "references", "forward", "raw", "navigational", None, None, "content_links_resolved", 3),
        ],
    )
    conn.commit()


class GraphEngineSqliteTest(unittest.TestCase):
    def setUp(self) -> None:
        self.tmpdir = tempfile.TemporaryDirectory()
        self.db_path = Path(self.tmpdir.name) / "test_graph.db"

    def tearDown(self) -> None:
        self.tmpdir.cleanup()

    def run_script(self, script_name: str) -> None:
        script = GRAPH_DIR / script_name
        proc = subprocess.run(
            [sys.executable, str(script), "--db", str(self.db_path)],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(proc.returncode, 0, msg=f"{script_name}\nSTDOUT:\n{proc.stdout}\nSTDERR:\n{proc.stderr}")

    def test_ddl_applies(self) -> None:
        conn = sqlite3.connect(str(self.db_path))
        apply_ddl_tolerant(conn)

        cur = conn.cursor()
        cur.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name IN ('nodes','node_map_docs','node_map_sections','edges_manual','edges_inferred','influence')"
        )
        tables = {row[0] for row in cur.fetchall()}
        self.assertEqual(
            tables,
            {"nodes", "node_map_docs", "node_map_sections", "edges_manual", "edges_inferred", "influence"},
        )
        conn.close()

    def test_scripts_start_and_log_sync_runs(self) -> None:
        conn = sqlite3.connect(str(self.db_path))
        create_base_schema(conn)
        seed_minimal_data(conn)
        conn.close()

        self.run_script("build_nodes.py")
        self.run_script("migrate_edges_manual.py")
        self.run_script("infer_edges.py")
        self.run_script("compute_influence.py")

        conn = sqlite3.connect(str(self.db_path))
        cur = conn.cursor()

        cur.execute("SELECT COUNT(*) FROM nodes")
        self.assertEqual(cur.fetchone()[0], 4)

        cur.execute("SELECT COUNT(*) FROM edges_manual")
        self.assertEqual(cur.fetchone()[0], 1)

        cur.execute("SELECT kind, status FROM sync_runs")
        kinds = {(k, s) for k, s in cur.fetchall()}
        self.assertIn(("build_nodes", "OK"), kinds)
        self.assertIn(("migrate_edges_manual", "WARN"), kinds)

        cur.execute(
            """
            SELECT kind, status, notes
            FROM sync_runs
            WHERE kind='graph_edges_inferred'
            ORDER BY ran_at_utc DESC
            LIMIT 1
            """
        )
        infer_kind, infer_status, infer_notes = cur.fetchone()
        self.assertEqual(infer_kind, "graph_edges_inferred")
        self.assertEqual(infer_status, "OK")
        self.assertIn("gate=ok", infer_notes)
        self.assertIn("inserted_total=", infer_notes)
        self.assertIn("algorithm=infer_v1", infer_notes)

        cur.execute(
            """
            SELECT kind, status, notes
            FROM sync_runs
            WHERE kind='graph_influence'
            ORDER BY ran_at_utc DESC
            LIMIT 1
            """
        )
        influence_kind, influence_status, _influence_notes = cur.fetchone()
        self.assertEqual(influence_kind, "graph_influence")
        self.assertEqual(influence_status, "OK")
        conn.close()

    def test_build_nodes_hierarchy_from_sections_only(self) -> None:
        conn = sqlite3.connect(str(self.db_path))
        create_base_schema(conn)
        cur = conn.cursor()
        cur.execute(
            """
            INSERT INTO docs(doc_uid,title,title_norm,path,origin,created_at_utc,updated_at_utc)
            VALUES(?,?,?,?,?,?,?)
            """,
            ("doc-x", "Doc X", "doc x", "x.md", "core", "2026-01-01T00:00:00Z", "2026-01-01T00:00:00Z"),
        )
        cur.executemany(
            """
            INSERT INTO sections(
              section_uid,doc_uid,heading_text,heading_norm,heading_level,heading_path,anchor,ordinal,status,
              text_fingerprint_sha256,start_line,end_line
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)
            """,
            [
                ("s-1", "doc-x", "A", "a", 2, "A", "a", 1, "ok", None, 1, 10),
                ("s-2", "doc-x", "A.1", "a.1", 3, "A > A.1", "a-1", 2, "ok", None, 11, 20),
                ("s-3", "doc-x", "A.2", "a.2", 3, "A > A.2", "a-2", 3, "ok", None, 21, 30),
                ("s-4", "doc-x", "B", "b", 2, "B", "b", 4, "ok", None, 31, 40),
                ("s-5", "doc-x", "B.1.1", "b.1.1", 4, "B > B.1 > B.1.1", "b-1-1", 5, "ok", None, 41, 50),
            ],
        )
        conn.commit()
        conn.close()

        self.run_script("build_nodes.py")

        conn = sqlite3.connect(str(self.db_path))
        cur = conn.cursor()
        cur.execute("SELECT node_uid,kind,parent_node_uid FROM nodes WHERE kind IN ('sec','subsec') ORDER BY ordinal")
        rows = cur.fetchall()
        expected = [
            ("s-1", "sec", "doc-x"),
            ("s-2", "subsec", "s-1"),
            ("s-3", "subsec", "s-1"),
            ("s-4", "sec", "doc-x"),
            ("s-5", "subsec", "s-4"),
        ]
        self.assertEqual(rows, expected)
        conn.close()

    def test_infer_edges_warns_when_gate_missing_migrate_edges_manual(self) -> None:
        conn = sqlite3.connect(str(self.db_path))
        create_base_schema(conn)
        seed_minimal_data(conn)
        conn.close()

        self.run_script("build_nodes.py")
        self.run_script("migrate_edges_manual.py")

        conn = sqlite3.connect(str(self.db_path))
        cur = conn.cursor()
        cur.execute("DELETE FROM sync_runs WHERE kind='migrate_edges_manual'")
        conn.commit()
        conn.close()

        self.run_script("infer_edges.py")

        conn = sqlite3.connect(str(self.db_path))
        cur = conn.cursor()
        cur.execute(
            """
            SELECT status, notes
            FROM sync_runs
            WHERE kind='graph_edges_inferred'
            ORDER BY ran_at_utc DESC
            LIMIT 1
            """
        )
        status, notes = cur.fetchone()
        self.assertEqual(status, "WARN")
        self.assertIn("skip: gate:", notes)
        self.assertIn("missing sync_runs kind=migrate_edges_manual", notes)
        conn.close()


if __name__ == "__main__":
    unittest.main()
