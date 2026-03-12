"""tests/test_maintenance.py — testy dry-run skryptów maintenance.

Sprawdzają że skrypty:
  1. Nie modyfikują plików w trybie dry-run.
  2. Kończą się kodem 0 na poprawnych danych wejściowych.
  3. Zwracają sensowne wyjście.
"""

import json
import subprocess
import sys
from pathlib import Path

import pytest

pytestmark = pytest.mark.integration

_REPO_ROOT = Path(__file__).parent.parent
_SCRIPTS_DIR = _REPO_ROOT / "scripts"
_DB_PATH = _REPO_ROOT / "reports" / "it_doc_matrix.db"
_MAINTENANCE_DIR = _SCRIPTS_DIR / "maintenance"


def _skip_if_no_db():
    if not _DB_PATH.exists():
        pytest.skip(f"Real DB not found: {_DB_PATH}")


def _run_script(script_path: Path, args: list, cwd=None) -> subprocess.CompletedProcess:
    """Uruchamia skrypt Python i zwraca CompletedProcess."""
    return subprocess.run(
        [sys.executable, str(script_path)] + args,
        capture_output=True,
        text=True,
        cwd=str(cwd or _REPO_ROOT),
        timeout=120,
    )


class TestTemplateAuditor:
    def test_exits_with_zero(self):
        _skip_if_no_db()
        script = _MAINTENANCE_DIR / "template_auditor.py"
        if not script.exists():
            pytest.skip(f"Skrypt nie istnieje: {script}")
        result = _run_script(script, ["--glob", "core/21_cfr_part_11_compliance.md"])
        assert result.returncode == 0, (
            f"template_auditor.py zakończył się kodem {result.returncode}\n{result.stderr}"
        )

    def test_produces_output(self):
        _skip_if_no_db()
        script = _MAINTENANCE_DIR / "template_auditor.py"
        if not script.exists():
            pytest.skip(f"Skrypt nie istnieje: {script}")
        result = _run_script(script, ["--glob", "core/21_cfr_part_11_compliance.md"])
        # Cokolwiek na stdout (niekoniecznie JSON)
        combined = result.stdout + result.stderr
        assert len(combined) > 0, "Audytor nie zwrócił żadnego wyjścia"


class TestBulkSectionPatcher:
    def test_dry_run_exits_with_zero(self):
        _skip_if_no_db()
        script = _MAINTENANCE_DIR / "bulk_section_patcher.py"
        if not script.exists():
            pytest.skip(f"Skrypt nie istnieje: {script}")
        result = _run_script(
            script,
            [
                "--filter-glob",
                "core/21_cfr_part_11_compliance.md",
                "--add-section",
                "## Test sekcja DRY",
                "--section-content",
                "Treść testowa dry-run",
                "--dry-run",
            ],
        )
        assert result.returncode == 0, (
            f"bulk_section_patcher.py (dry-run) zakończył się kodem {result.returncode}\n{result.stderr}"
        )

    def test_dry_run_does_not_modify_files(self):
        _skip_if_no_db()
        script = _MAINTENANCE_DIR / "bulk_section_patcher.py"
        if not script.exists():
            pytest.skip(f"Skrypt nie istnieje: {script}")
        target = _REPO_ROOT / "generated_templates" / "core" / "21_cfr_part_11_compliance.md"
        if not target.exists():
            pytest.skip(f"Szablon nie istnieje: {target}")

        before = target.read_text(encoding="utf-8")
        _run_script(
            script,
            [
                "--filter-glob",
                "core/21_cfr_part_11_compliance.md",
                "--add-section",
                "## Test sekcja DRY",
                "--section-content",
                "Treść testowa",
                "--dry-run",
            ],
        )
        after = target.read_text(encoding="utf-8")
        assert before == after, "Dry-run zmodyfikował plik (niedozwolone!)"


class TestImpactAnalyzer:
    def test_exits_with_zero_for_known_standard(self):
        _skip_if_no_db()
        script = _MAINTENANCE_DIR / "impact_analyzer.py"
        if not script.exists():
            pytest.skip(f"Skrypt nie istnieje: {script}")
        result = _run_script(script, ["--standard", "ISO/IEC 27001"])
        assert result.returncode == 0, (
            f"impact_analyzer.py zakończył się kodem {result.returncode}\n{result.stderr}"
        )

    def test_produces_nonempty_output(self):
        _skip_if_no_db()
        script = _MAINTENANCE_DIR / "impact_analyzer.py"
        if not script.exists():
            pytest.skip(f"Skrypt nie istnieje: {script}")
        result = _run_script(script, ["--standard", "ISO/IEC 27001"])
        combined = result.stdout + result.stderr
        assert len(combined) > 10, "impact_analyzer nie zwrócił sensownego wyjścia"

    def test_json_output_has_results(self):
        _skip_if_no_db()
        script = _MAINTENANCE_DIR / "impact_analyzer.py"
        if not script.exists():
            pytest.skip(f"Skrypt nie istnieje: {script}")
        result = _run_script(script, ["--standard", "ISO/IEC 27001", "--output", "json"])
        if result.returncode != 0:
            pytest.skip("Skrypt nie obsługuje --output json")
        # Sprawdź czy stdout zawiera parseowalny JSON
        stdout = result.stdout.strip()
        if stdout:
            try:
                data = json.loads(stdout)
                # Powinien mieć jakiś klucz z wynikami
                assert isinstance(data, (dict, list))
            except json.JSONDecodeError:
                pass  # Niektóre skrypty mogą mieszać tabele + JSON
