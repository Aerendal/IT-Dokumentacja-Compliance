"""tests/test_cli.py — testy CLI/TUI itdoc/__main__.py.

Test Scope Matrix (TESTING_METHODOLOGY):
  Module:   cli.py
  RT:       1.70  (C=2 R=3 K=3 P=2 D=0 S=0 F=0)
  Class:    medium
  UT_min:   20   (2·B=2·10, PF=4)
  IT_min:   6    (DEP=2 → 3·ceil(1.7)=6)
  CT_min:   4    (EP=4 · 1)
  Coverage: ≥47%

Zasada UI: workspace powitalny = pusty (brak bannerów, brak ASCII art).
Złożoność w CLI — testy sprawdzają zwięzłość wyjścia.
"""

import subprocess
import sys
from pathlib import Path

import pytest

from itdoc.cli import build_parser, cmd_find, cmd_validate, cmd_db_check, main

_REPO_ROOT = Path(__file__).parent.parent
_DB_PATH = _REPO_ROOT / "reports" / "it_doc_matrix.db"


def _skip_if_no_db():
    if not _DB_PATH.exists():
        pytest.skip(f"Real DB not found: {_DB_PATH}")


# ─── Czyste powitanie (empty workspace) ──────────────────────────────────


class TestWelcomeWorkspace:
    """Zasada: workspace powitalny jest czytelny = minimalny."""

    def test_no_args_returns_zero(self):
        code = main([])
        assert code == 0

    def test_no_args_no_crash(self, capsys):
        main([])
        out = capsys.readouterr()
        combined = out.out + out.err
        # Nie powinno być stack trace
        assert "Traceback" not in combined
        assert "Error" not in combined

    def test_no_args_output_is_short(self, capsys):
        """Powitanie ≤ 3 linie — czyste UI."""
        main([])
        out = capsys.readouterr()
        lines = [l for l in (out.out + out.err).splitlines() if l.strip()]
        assert len(lines) <= 3, f"Zbyt wiele linii powitania: {lines}"

    def test_no_args_no_banner(self, capsys):
        """Brak ASCII bannerów, brak emoji."""
        main([])
        out = capsys.readouterr()
        combined = out.out + out.err
        assert "██" not in combined
        assert "╔" not in combined
        assert "═" not in combined

    def test_help_exits_with_zero(self):
        with pytest.raises(SystemExit) as exc:
            main(["--help"])
        assert exc.value.code == 0


# ─── build_parser ────────────────────────────────────────────────────────


class TestBuildParser:
    def test_returns_parser(self):
        p = build_parser()
        assert p is not None

    def test_parser_has_subcommands(self):
        p = build_parser()
        args = p.parse_args(["find", "--standard", "X"])
        assert args.command == "find"

    def test_parser_find_requires_standard_or_regulation(self):
        p = build_parser()
        with pytest.raises(SystemExit):
            p.parse_args(["find"])  # brak --standard i --regulation

    def test_parser_db_path_optional(self):
        p = build_parser()
        args = p.parse_args(["db-check"])
        assert args.db is None  # domyślnie None

    def test_parser_rhythm_depth_default(self):
        p = build_parser()
        args = p.parse_args(["rhythm", "UID001"])
        assert args.depth == 2

    def test_parser_find_limit_default(self):
        p = build_parser()
        args = p.parse_args(["find", "--standard", "ISO"])
        assert args.limit == 20

    def test_parser_contract_json_flag(self):
        p = build_parser()
        args = p.parse_args(["contract", "UID001", "--json"])
        assert args.json is True

    def test_parser_contract_no_json_default(self):
        p = build_parser()
        args = p.parse_args(["contract", "UID001"])
        assert args.json is False


# ─── cmd_validate ────────────────────────────────────────────────────────


class TestCmdValidate:
    def _make_args(self, path: str, db: str = None):
        class Args:
            pass
        a = Args()
        a.path = path
        a.db = db
        return a

    def test_valid_template_returns_0(self, tmp_path):
        p = tmp_path / "t.md"
        p.write_text(
            "---\ntitle: T\nstatus: draft\naligned: true\n---\n"
            "## Cel dokumentu\nT\n## Zakres i granice\nT\n## Wejścia i wyjścia\nT\n",
            encoding="utf-8",
        )
        code = cmd_validate(self._make_args(str(p)))
        assert code == 0

    def test_missing_file_returns_1(self, tmp_path):
        code = cmd_validate(self._make_args(str(tmp_path / "missing.md")))
        assert code == 1

    def test_invalid_template_returns_1(self, tmp_path, capsys):
        p = tmp_path / "bad.md"
        p.write_text("# No frontmatter\nbody", encoding="utf-8")
        code = cmd_validate(self._make_args(str(p)))
        assert code == 1

    def test_validate_output_clean(self, tmp_path, capsys):
        """Wyjście OK powinno zawierać 'OK' — czytelne dla CI."""
        p = tmp_path / "t.md"
        p.write_text(
            "---\ntitle: T\nstatus: draft\naligned: true\n---\n"
            "## Cel dokumentu\nT\n## Zakres i granice\nT\n## Wejścia i wyjścia\nT\n",
            encoding="utf-8",
        )
        cmd_validate(self._make_args(str(p)))
        out = capsys.readouterr()
        assert "OK" in out.out or "OK" in out.err


# ─── cmd_db_check ────────────────────────────────────────────────────────


class TestCmdDbCheck:
    def _make_args(self, db_path=None):
        class Args:
            pass
        a = Args()
        a.db = str(db_path) if db_path else None
        return a

    def test_missing_db_exits_1(self, tmp_path):
        """Gdy DB nie istnieje, cmd_db_check powinno zwrócić kod 1 (przez main)."""
        from itdoc.cli import main as cli_main
        code = cli_main(["--db", str(tmp_path / "missing.db"), "db-check"])
        assert code == 1

    @pytest.mark.integration
    def test_real_db_returns_0(self):
        _skip_if_no_db()
        args = type("A", (), {"db": None})()
        code = cmd_db_check(args)
        assert code == 0


# ─── cmd_find (integration) ──────────────────────────────────────────────


class TestCmdFind:
    @pytest.mark.integration
    def test_find_standard_prints_results(self, capsys):
        _skip_if_no_db()
        args = type("A", (), {
            "db": None, "standard": "ISO/IEC 27001", "regulation": None, "limit": 5,
        })()
        code = cmd_find(args)
        out = capsys.readouterr()
        assert code == 0
        # Powinny być jakieś wyniki
        assert len(out.out.strip().splitlines()) >= 1

    @pytest.mark.integration
    def test_find_unknown_standard_clean_output(self, capsys):
        _skip_if_no_db()
        args = type("A", (), {
            "db": None, "standard": "NIEZNANY_XYZ_99999", "regulation": None, "limit": 5,
        })()
        code = cmd_find(args)
        out = capsys.readouterr()
        assert code == 0
        # Informacja o braku wyników, nie crash
        assert "brak" in out.out.lower() or out.out.strip() == "" or len(out.out.strip()) < 100


# ─── Subprocess tests (end-to-end CLI) ────────────────────────────────────


class TestCliSubprocess:
    def test_module_runnable(self):
        result = subprocess.run(
            [sys.executable, "-m", "itdoc"],
            capture_output=True, text=True, timeout=10,
            cwd=str(_REPO_ROOT),
        )
        assert result.returncode == 0

    def test_help_flag_runnable(self):
        result = subprocess.run(
            [sys.executable, "-m", "itdoc", "--help"],
            capture_output=True, text=True, timeout=10,
            cwd=str(_REPO_ROOT),
        )
        assert result.returncode == 0
        assert "itdoc" in result.stdout.lower()

    @pytest.mark.integration
    def test_db_check_subprocess(self):
        _skip_if_no_db()
        result = subprocess.run(
            [sys.executable, "-m", "itdoc", "db-check"],
            capture_output=True, text=True, timeout=30,
            cwd=str(_REPO_ROOT),
        )
        assert result.returncode == 0
        assert "OK" in result.stdout
