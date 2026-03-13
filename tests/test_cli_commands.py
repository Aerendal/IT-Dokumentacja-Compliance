"""tests/test_cli_commands.py

Testy dla itdoc/cli.py — komendy CLI: find, contract, validate, db-check, rhythm, main().
Używa rzeczywistych plików SQLite (get_connection() wymaga istniejącego pliku).
Zasada: nie mockujemy tego co testujemy — prawdziwy SQL, prawdziwy parser.
"""

import json
import sqlite3
from pathlib import Path

import pytest

import itdoc.cli as cli


# ---------------------------------------------------------------------------
# Helpers — tworzenie minimalnego DB do testów CLI
# ---------------------------------------------------------------------------


def _create_minimal_db(path: Path) -> None:
    """Tworzy minimalne SQLite spełniające wymagania get_connection() + testowanych tabel."""
    conn = sqlite3.connect(str(path))
    conn.row_factory = sqlite3.Row

    # Tabele wymagane przez validate_schema (dla cmd_db_check)
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS docs (
            id INTEGER PRIMARY KEY,
            path TEXT,
            title TEXT,
            doc_uid TEXT
        );
        CREATE TABLE IF NOT EXISTS sections (
            id INTEGER PRIMARY KEY,
            doc_id INTEGER,
            heading TEXT,
            body TEXT
        );
        CREATE TABLE IF NOT EXISTS standards (
            standard_id INTEGER PRIMARY KEY,
            standard_code TEXT UNIQUE,
            standard_name TEXT
        );
        CREATE TABLE IF NOT EXISTS compliance_regulations (
            regulation_id INTEGER PRIMARY KEY,
            regulation_code TEXT UNIQUE,
            regulation_name TEXT
        );
        CREATE TABLE IF NOT EXISTS content_links (
            id INTEGER PRIMARY KEY,
            source_path TEXT,
            target_path TEXT
        );
        CREATE TABLE IF NOT EXISTS content_links_resolved (
            id INTEGER PRIMARY KEY,
            source_path TEXT,
            target_path TEXT
        );
        CREATE TABLE IF NOT EXISTS rhythm_edges (
            id INTEGER PRIMARY KEY,
            from_node TEXT,
            to_node TEXT,
            rhythm_type TEXT,
            weight REAL DEFAULT 1.0
        );
        CREATE TABLE IF NOT EXISTS contracts (
            id INTEGER PRIMARY KEY,
            scope_uid TEXT,
            version TEXT,
            inputs_json TEXT,
            outputs_json TEXT,
            gates_json TEXT,
            impact_json TEXT
        );
        CREATE TABLE IF NOT EXISTS flags (
            id INTEGER PRIMARY KEY,
            flag_name TEXT,
            flag_value TEXT
        );
        CREATE TABLE IF NOT EXISTS _schema_version (
            version INTEGER PRIMARY KEY
        );
        CREATE TABLE IF NOT EXISTS doc_standard_mapping (
            id INTEGER PRIMARY KEY,
            doc_path TEXT,
            standard_code TEXT,
            confidence REAL,
            match_reason TEXT,
            evidence TEXT
        );
        CREATE TABLE IF NOT EXISTS doc_regulation_mapping (
            id INTEGER PRIMARY KEY,
            doc_path TEXT,
            regulation_code TEXT,
            match_reason TEXT
        );
    """)

    # Minimalnie jeden wiersz w każdej wymaganej tabeli (dla validate_schema)
    conn.execute("INSERT INTO docs (path, title, doc_uid) VALUES ('core/test.md', 'Test', 'UID001')")
    conn.execute("INSERT INTO sections (doc_id, heading, body) VALUES (1, 'Cel', 'treść')")
    conn.execute("INSERT INTO standards (standard_code, standard_name) VALUES ('ISO27001', 'ISMS')")
    conn.execute("INSERT INTO compliance_regulations (regulation_code, regulation_name) VALUES ('UODO-PL', 'RODO')")
    conn.execute("INSERT INTO content_links (source_path, target_path) VALUES ('a.md', 'b.md')")
    conn.execute("INSERT INTO content_links_resolved (source_path, target_path) VALUES ('a.md', 'b.md')")
    conn.execute("INSERT INTO rhythm_edges (from_node, to_node, rhythm_type) VALUES ('UID001', 'UID002', 'requires')")
    conn.execute("INSERT INTO contracts (scope_uid, version, inputs_json, outputs_json, gates_json, impact_json) VALUES ('UID001', '1.0', '[\"input_a\"]', '[\"output_b\"]', '[]', '[]')")
    conn.execute("INSERT INTO flags (flag_name, flag_value) VALUES ('test', '1')")
    conn.execute("INSERT INTO _schema_version (version) VALUES (1)")

    # Dane dla cmd_find
    conn.execute("INSERT INTO doc_standard_mapping (doc_path, standard_code, confidence, match_reason) VALUES ('core/test.md', 'ISO27001', 0.9, 'keyword_match')")
    conn.execute("INSERT INTO doc_regulation_mapping (doc_path, regulation_code, match_reason) VALUES ('core/test.md', 'UODO-PL', 'keyword_match')")

    conn.commit()
    conn.close()


@pytest.fixture
def db_file(tmp_path) -> Path:
    """Tymczasowy plik DB z minimalną zawartością."""
    db = tmp_path / "test.db"
    _create_minimal_db(db)
    return db


@pytest.fixture
def valid_template(tmp_path) -> Path:
    """Poprawny szablon Markdown dla cmd_validate."""
    t = tmp_path / "template.md"
    t.write_text(
        "---\n"
        "title: Test Template\n"
        "status: needs_content\n"
        "aligned: true\n"
        "---\n"
        "\n"
        "# Test Template\n"
        "\n"
        "## Cel dokumentu\n"
        "Cel tego dokumentu.\n"
        "\n"
        "## Zakres i granice\n"
        "Zakres dokumentu.\n"
        "\n"
        "## Wejścia i wyjścia\n"
        "Lista wejść i wyjść.\n",
        encoding="utf-8",
    )
    return t


@pytest.fixture
def invalid_template(tmp_path) -> Path:
    """Niepoprawny szablon — brakuje wymaganych sekcji."""
    t = tmp_path / "bad_template.md"
    t.write_text(
        "---\n"
        "title: Zły szablon\n"
        "---\n"
        "\n"
        "# Zły szablon\n"
        "\n"
        "Brak wymaganych sekcji.\n",
        encoding="utf-8",
    )
    return t


# ---------------------------------------------------------------------------
# build_parser()
# ---------------------------------------------------------------------------


class TestBuildParser:
    def test_returns_parser(self):
        parser = cli.build_parser()
        assert parser is not None

    def test_has_db_argument(self):
        parser = cli.build_parser()
        args = parser.parse_args(["--db", "test.db", "find", "--standard", "ISO"])
        assert args.db == "test.db"

    def test_find_standard_arg(self):
        parser = cli.build_parser()
        args = parser.parse_args(["find", "--standard", "ISO/IEC 27001"])
        assert args.command == "find"
        assert args.standard == "ISO/IEC 27001"
        assert args.regulation is None

    def test_find_regulation_arg(self):
        parser = cli.build_parser()
        args = parser.parse_args(["find", "--regulation", "UODO-PL"])
        assert args.command == "find"
        assert args.regulation == "UODO-PL"

    def test_find_limit_default(self):
        parser = cli.build_parser()
        args = parser.parse_args(["find", "--standard", "ISO"])
        assert args.limit == 20

    def test_find_limit_custom(self):
        parser = cli.build_parser()
        args = parser.parse_args(["find", "--standard", "ISO", "--limit", "5"])
        assert args.limit == 5

    def test_contract_args(self):
        parser = cli.build_parser()
        args = parser.parse_args(["contract", "UID001"])
        assert args.command == "contract"
        assert args.uid == "UID001"
        assert not args.json

    def test_contract_json_flag(self):
        parser = cli.build_parser()
        args = parser.parse_args(["contract", "UID001", "--json"])
        assert args.json is True

    def test_rhythm_default_depth(self):
        parser = cli.build_parser()
        args = parser.parse_args(["rhythm", "UID001"])
        assert args.depth == 2

    def test_rhythm_custom_depth(self):
        parser = cli.build_parser()
        args = parser.parse_args(["rhythm", "UID001", "--depth", "4"])
        assert args.depth == 4

    def test_no_command_returns_none(self):
        parser = cli.build_parser()
        args = parser.parse_args([])
        assert args.command is None


# ---------------------------------------------------------------------------
# cmd_find() — --standard
# ---------------------------------------------------------------------------


class TestCmdFindStandard:
    def _make_args(self, db, standard="ISO27001", limit=20):
        parser = cli.build_parser()
        return parser.parse_args(["--db", str(db), "find", "--standard", standard, "--limit", str(limit)])

    def test_finds_mapped_standard(self, db_file, capsys):
        args = self._make_args(db_file)
        rc = cli.cmd_find(args)
        assert rc == 0
        out = capsys.readouterr().out
        assert "core/test.md" in out

    def test_no_results_returns_0(self, db_file, capsys):
        args = self._make_args(db_file, standard="NONEXISTENT_XYZ")
        rc = cli.cmd_find(args)
        assert rc == 0
        out = capsys.readouterr().out
        assert "brak wynikow" in out

    def test_empty_standard_returns_1(self, db_file, capsys):
        args = self._make_args(db_file, standard="  ")
        rc = cli.cmd_find(args)
        assert rc == 1

    def test_limit_applied(self, db_file, capsys):
        args = self._make_args(db_file, standard="ISO27001", limit=1)
        rc = cli.cmd_find(args)
        assert rc == 0

    def test_missing_db_returns_1(self, tmp_path, capsys):
        # ItDocError jest łapany w main(), nie w cmd_find() — testujemy przez main()
        rc = cli.main(["--db", str(tmp_path / "missing.db"), "find", "--standard", "ISO"])
        assert rc == 1


# ---------------------------------------------------------------------------
# cmd_find() — --regulation
# ---------------------------------------------------------------------------


class TestCmdFindRegulation:
    def _make_args(self, db, regulation="UODO-PL"):
        parser = cli.build_parser()
        return parser.parse_args(["--db", str(db), "find", "--regulation", regulation])

    def test_finds_mapped_regulation(self, db_file, capsys):
        args = self._make_args(db_file)
        rc = cli.cmd_find(args)
        assert rc == 0
        out = capsys.readouterr().out
        assert "core/test.md" in out

    def test_no_results_returns_0(self, db_file, capsys):
        args = self._make_args(db_file, regulation="NONEXISTENT")
        rc = cli.cmd_find(args)
        assert rc == 0


# ---------------------------------------------------------------------------
# cmd_contract()
# ---------------------------------------------------------------------------


class TestCmdContract:
    def _make_args(self, db, uid="UID001", as_json=False):
        argv = ["--db", str(db), "contract", uid]
        if as_json:
            argv.append("--json")
        return cli.build_parser().parse_args(argv)

    def test_prints_contract_text(self, db_file, capsys):
        args = self._make_args(db_file)
        rc = cli.cmd_contract(args)
        assert rc == 0
        out = capsys.readouterr().out
        assert "UID001" in out

    def test_json_output_is_valid_json(self, db_file, capsys):
        args = self._make_args(db_file, as_json=True)
        rc = cli.cmd_contract(args)
        assert rc == 0
        out = capsys.readouterr().out
        parsed = json.loads(out)
        assert isinstance(parsed, dict)

    def test_missing_uid_returns_1(self, db_file, capsys):
        args = self._make_args(db_file, uid="NONEXISTENT_UID")
        rc = cli.cmd_contract(args)
        assert rc == 1

    def test_empty_uid_returns_1(self, db_file, capsys):
        args = self._make_args(db_file, uid="  ")
        rc = cli.cmd_contract(args)
        assert rc == 1

    def test_inputs_in_output(self, db_file, capsys):
        args = self._make_args(db_file)
        cli.cmd_contract(args)
        out = capsys.readouterr().out
        assert "input_a" in out


# ---------------------------------------------------------------------------
# cmd_validate()
# ---------------------------------------------------------------------------


class TestCmdValidate:
    def _make_args(self, path):
        return cli.build_parser().parse_args(["validate", str(path)])

    def test_valid_template_returns_0(self, valid_template, capsys):
        args = self._make_args(valid_template)
        rc = cli.cmd_validate(args)
        assert rc == 0
        out = capsys.readouterr().out
        assert "OK" in out

    def test_invalid_template_returns_1(self, invalid_template, capsys):
        args = self._make_args(invalid_template)
        rc = cli.cmd_validate(args)
        assert rc == 1
        out = capsys.readouterr().out
        assert "FAIL" in out

    def test_missing_file_returns_1(self, tmp_path, capsys):
        args = self._make_args(tmp_path / "nonexistent.md")
        rc = cli.cmd_validate(args)
        assert rc == 1


# ---------------------------------------------------------------------------
# cmd_db_check()
# ---------------------------------------------------------------------------


class TestCmdDbCheck:
    def test_valid_schema_returns_0(self, db_file, capsys):
        args = cli.build_parser().parse_args(["--db", str(db_file), "db-check"])
        rc = cli.cmd_db_check(args)
        assert rc == 0
        out = capsys.readouterr().out
        assert "OK" in out

    def test_missing_table_returns_1(self, tmp_path, capsys):
        db = tmp_path / "partial.db"
        conn = sqlite3.connect(str(db))
        conn.execute("CREATE TABLE docs (id INTEGER PRIMARY KEY, path TEXT)")
        conn.execute("INSERT INTO docs (path) VALUES ('test.md')")
        conn.commit()
        conn.close()
        args = cli.build_parser().parse_args(["--db", str(db), "db-check"])
        rc = cli.cmd_db_check(args)
        assert rc == 1
        out = capsys.readouterr().out
        assert "FAIL" in out


# ---------------------------------------------------------------------------
# cmd_rhythm()
# ---------------------------------------------------------------------------


class TestCmdRhythm:
    def test_rhythm_with_edges(self, db_file, capsys):
        args = cli.build_parser().parse_args(["--db", str(db_file), "rhythm", "UID002"])
        rc = cli.cmd_rhythm(args)
        assert rc == 0

    def test_rhythm_no_edges_returns_0(self, db_file, capsys):
        args = cli.build_parser().parse_args(["--db", str(db_file), "rhythm", "UNKNOWN_UID"])
        rc = cli.cmd_rhythm(args)
        assert rc == 0
        out = capsys.readouterr().out
        assert "brak" in out

    def test_rhythm_upstream_shown(self, db_file, capsys):
        # UID002 jest to_node z UID001 — więc UID001 jest upstream dla UID002
        args = cli.build_parser().parse_args(["--db", str(db_file), "rhythm", "UID002"])
        cli.cmd_rhythm(args)
        out = capsys.readouterr().out
        assert "UID001" in out

    def test_rhythm_empty_uid_returns_1(self, db_file, capsys):
        args = cli.build_parser().parse_args(["--db", str(db_file), "rhythm", "  "])
        rc = cli.cmd_rhythm(args)
        assert rc == 1


# ---------------------------------------------------------------------------
# main() — dispatch
# ---------------------------------------------------------------------------


class TestMain:
    def test_no_command_returns_0(self):
        rc = cli.main([])
        assert rc == 0

    def test_find_dispatched(self, db_file, capsys):
        rc = cli.main(["--db", str(db_file), "find", "--standard", "ISO27001"])
        assert rc == 0

    def test_db_check_dispatched(self, db_file, capsys):
        rc = cli.main(["--db", str(db_file), "db-check"])
        assert rc == 0

    def test_validate_dispatched(self, valid_template):
        rc = cli.main(["validate", str(valid_template)])
        assert rc == 0

    def test_contract_dispatched(self, db_file):
        rc = cli.main(["--db", str(db_file), "contract", "UID001"])
        assert rc == 0

    def test_itdoc_error_propagates_to_exit_1(self, tmp_path):
        """ItDocError przechwycony w main() → exit code 1."""
        rc = cli.main(["--db", str(tmp_path / "missing.db"), "find", "--standard", "ISO"])
        assert rc == 1
