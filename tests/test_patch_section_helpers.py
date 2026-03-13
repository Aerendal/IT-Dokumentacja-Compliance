"""
test_patch_section_helpers.py — Unit testy dla helperów wydzielonych w refaktorze
Fazy 2B/C/D patch_section.py.

Cel: weryfikacja każdego helpera w izolacji.
Hierarchia wg "Jak pisać testy.md": Krok 1 — Unit tests.
"""

from __future__ import annotations

import argparse
import json
import textwrap
from pathlib import Path

import pytest
import yaml


# ---------------------------------------------------------------------------
# _parse_template_vars
# ---------------------------------------------------------------------------

class TestParseTemplateVars:
    """Unit testy dla _parse_template_vars()."""

    def _make_args(self, template_vars=None):
        ns = argparse.Namespace()
        ns.template_vars = template_vars
        return ns

    def test_none_returns_none(self):
        from scripts.maintenance.patch_section import _parse_template_vars
        result = _parse_template_vars(self._make_args(None))
        assert result is None

    def test_empty_list_returns_empty_dict(self):
        from scripts.maintenance.patch_section import _parse_template_vars
        result = _parse_template_vars(self._make_args([]))
        assert result == {} or result is None  # pustą listę możemy traktować jak None

    def test_single_key_value(self):
        from scripts.maintenance.patch_section import _parse_template_vars
        result = _parse_template_vars(self._make_args(["key=value"]))
        assert result is not None
        assert result["key"] == "value"

    def test_multiple_key_values(self):
        from scripts.maintenance.patch_section import _parse_template_vars
        result = _parse_template_vars(self._make_args(["k1=v1", "k2=v2"]))
        assert result["k1"] == "v1"
        assert result["k2"] == "v2"

    def test_value_with_equals_sign(self):
        """Wartość zawierająca '=' — split tylko na pierwszym '='."""
        from scripts.maintenance.patch_section import _parse_template_vars
        result = _parse_template_vars(self._make_args(["url=http://a.com/x=1"]))
        assert result is not None
        assert result["url"] == "http://a.com/x=1"

    def test_strips_whitespace_from_key_and_value(self):
        from scripts.maintenance.patch_section import _parse_template_vars
        result = _parse_template_vars(self._make_args([" key = value "]))
        assert result is not None
        assert "key" in result
        assert result["key"] == "value"


# ---------------------------------------------------------------------------
# _validate_patch_args
# ---------------------------------------------------------------------------

class TestValidatePatchArgs:
    """Unit testy dla _validate_patch_args()."""

    def _make_args(self, **kwargs):
        """Tworzy args z sensownymi domyślnymi + override z kwargs."""
        defaults = {
            "section": "## Cel",
            "section_regex": None,
            "old": None,
            "new_text": None,
            "operation": "replace",
            "content": "nowa treść",
            "content_file": None,
            "new_name": None,
            "extract_dir": None,
        }
        defaults.update(kwargs)
        return argparse.Namespace(**defaults)

    def _make_parser(self):
        """Parser argparse — jego error() rzuca SystemExit."""
        return argparse.ArgumentParser()

    def test_valid_replace_no_exception(self):
        from scripts.maintenance.patch_section import _validate_patch_args
        args = self._make_args()
        # Nie powinno rzucić wyjątku
        _validate_patch_args(args, self._make_parser())

    def test_missing_section_and_section_regex_raises(self):
        from scripts.maintenance.patch_section import _validate_patch_args
        args = self._make_args(section=None, section_regex=None)
        with pytest.raises(SystemExit):
            _validate_patch_args(args, self._make_parser())

    def test_old_with_non_replace_operation_raises(self):
        from scripts.maintenance.patch_section import _validate_patch_args
        args = self._make_args(operation="append", old="stara treść")
        with pytest.raises(SystemExit):
            _validate_patch_args(args, self._make_parser())

    def test_replace_without_content_raises(self):
        from scripts.maintenance.patch_section import _validate_patch_args
        args = self._make_args(content=None, content_file=None, old=None)
        with pytest.raises(SystemExit):
            _validate_patch_args(args, self._make_parser())

    def test_rename_without_new_name_raises(self):
        from scripts.maintenance.patch_section import _validate_patch_args
        args = self._make_args(operation="rename", new_name=None)
        with pytest.raises(SystemExit):
            _validate_patch_args(args, self._make_parser())

    def test_rename_with_new_name_no_exception(self):
        from scripts.maintenance.patch_section import _validate_patch_args
        args = self._make_args(operation="rename", new_name="## Nowy tytuł", content=None)
        _validate_patch_args(args, self._make_parser())

    def test_extract_without_extract_dir_raises(self):
        from scripts.maintenance.patch_section import _validate_patch_args
        args = self._make_args(operation="extract", extract_dir=None, content=None)
        with pytest.raises(SystemExit):
            _validate_patch_args(args, self._make_parser())

    def test_section_regex_instead_of_section_is_valid(self):
        from scripts.maintenance.patch_section import _validate_patch_args
        args = self._make_args(section=None, section_regex=r"^## Cel.*")
        _validate_patch_args(args, self._make_parser())


# ---------------------------------------------------------------------------
# _load_batch_file
# ---------------------------------------------------------------------------

class TestLoadBatchFile:
    """Unit testy dla _load_batch_file()."""

    def test_nonexistent_file_returns_empty(self, tmp_path):
        """Nieistniejący plik → ([], {}) bez wyjątku."""
        from scripts.maintenance.patch_section import _load_batch_file
        ops, gvars = _load_batch_file(str(tmp_path / "nie_istnieje.yaml"))
        assert ops == []
        assert isinstance(gvars, dict)

    def test_valid_batch_file_returns_operations(self, tmp_path):
        """Poprawny plik YAML z operations → lista operacji."""
        batch = {
            "variables": {"version": "2.0"},
            "operations": [
                {"action": "replace", "section": "## Cel", "content": "Treść"},
                {"action": "append",  "section": "## Zakres", "content": "Nowe"},
            ],
        }
        batch_file = tmp_path / "batch.yaml"
        batch_file.write_text(yaml.dump(batch), encoding="utf-8")

        from scripts.maintenance.patch_section import _load_batch_file
        ops, gvars = _load_batch_file(str(batch_file))
        assert len(ops) == 2
        assert ops[0]["action"] == "replace"
        assert gvars["version"] == "2.0"

    def test_batch_file_injects_default_variables(self, tmp_path):
        """Brak date/version → wstrzykuje domyślne wartości."""
        batch = {"operations": [{"action": "replace", "section": "## X", "content": "Y"}]}
        batch_file = tmp_path / "batch.yaml"
        batch_file.write_text(yaml.dump(batch), encoding="utf-8")

        from scripts.maintenance.patch_section import _load_batch_file
        ops, gvars = _load_batch_file(str(batch_file))
        assert "date" in gvars
        assert "version" in gvars

    def test_empty_operations_returns_empty_list(self, tmp_path):
        """Brak operacji → pusta lista (nie crash)."""
        batch = {"variables": {"foo": "bar"}, "operations": []}
        batch_file = tmp_path / "empty.yaml"
        batch_file.write_text(yaml.dump(batch), encoding="utf-8")

        from scripts.maintenance.patch_section import _load_batch_file
        ops, gvars = _load_batch_file(str(batch_file))
        assert ops == []

    def test_custom_variable_overrides_default(self, tmp_path):
        """Własna zmienna 'version' nie jest nadpisywana przez domyślną."""
        batch = {"variables": {"version": "99.0"}, "operations": []}
        batch_file = tmp_path / "custom.yaml"
        batch_file.write_text(yaml.dump(batch), encoding="utf-8")

        from scripts.maintenance.patch_section import _load_batch_file
        _, gvars = _load_batch_file(str(batch_file))
        assert gvars["version"] == "99.0"


# ---------------------------------------------------------------------------
# build_parser — argumenty parsera
# ---------------------------------------------------------------------------

class TestBuildParser:
    """Smoke testy dla build_parser() — czy parser w ogóle działa."""

    @pytest.fixture(scope="class")
    def parser(self):
        from scripts.maintenance.patch_section import build_parser
        return build_parser()

    def test_parser_created(self, parser):
        assert parser is not None

    def test_help_does_not_raise(self, parser):
        """--help uruchamia się bez nieoczekiwanego wyjątku (poza SystemExit 0)."""
        with pytest.raises(SystemExit) as exc_info:
            parser.parse_args(["--help"])
        assert exc_info.value.code == 0

    def test_section_argument_accepted(self, parser):
        args = parser.parse_args(["--section", "## Cel", "--content", "x", "--apply"])
        assert args.section == "## Cel"

    def test_dry_run_is_default(self, parser):
        """Bez --apply domyślnie dry_run=True."""
        args = parser.parse_args(["--section", "## X", "--content", "x"])
        # dry_run jest odwrotnością apply
        assert not args.apply

    def test_batch_argument_accepted(self, parser):
        args = parser.parse_args(["--batch", "ops.yaml"])
        assert args.batch == "ops.yaml"
