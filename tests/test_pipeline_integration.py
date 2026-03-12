"""tests/test_pipeline_integration.py — testy integracyjne pipeline.

Sprawdzają że pipeline_run.py zwraca status PASS.
Oznaczone @pytest.mark.slow — pomijane w szybkim CI (pytest -m "not slow").
"""

import subprocess
import sys
from pathlib import Path

import pytest

pytestmark = pytest.mark.slow

_REPO_ROOT = Path(__file__).parent.parent
_PIPELINE_SCRIPT = _REPO_ROOT / "scripts" / "pipeline_run.py"
_DB_PATH = _REPO_ROOT / "reports" / "it_doc_matrix.db"


@pytest.fixture(scope="module", autouse=True)
def require_db():
    if not _DB_PATH.exists():
        pytest.skip(f"Real DB not found: {_DB_PATH}")
    if not _PIPELINE_SCRIPT.exists():
        pytest.skip(f"Pipeline script not found: {_PIPELINE_SCRIPT}")


class TestPipelinePass:
    def test_pipeline_exits_with_zero(self):
        """Pipeline musi kończyć się kodem 0."""
        result = subprocess.run(
            [sys.executable, str(_PIPELINE_SCRIPT)],
            capture_output=True,
            text=True,
            cwd=str(_REPO_ROOT),
            timeout=300,
        )
        assert result.returncode == 0, (
            f"Pipeline zakończył się kodem {result.returncode}\n"
            f"STDOUT:\n{result.stdout[-3000:]}\n"
            f"STDERR:\n{result.stderr[-1000:]}"
        )

    def test_pipeline_reports_pass(self):
        """Pipeline musi wypisać 'PASS' w wyjściu."""
        result = subprocess.run(
            [sys.executable, str(_PIPELINE_SCRIPT)],
            capture_output=True,
            text=True,
            cwd=str(_REPO_ROOT),
            timeout=300,
        )
        combined = result.stdout + result.stderr
        assert (
            "PASS" in combined
        ), f"Brak 'PASS' w wyjściu pipeline\nOutput (ostatnie 2000 znaków):\n{combined[-2000:]}"
