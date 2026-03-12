"""
tests/test_qol_infrastructure.py

Testy weryfikujące infrastrukturę QoL:
- obecność i poprawność plików konfiguracyjnych
- działanie ITDOC_STRICT env var
- poprawność pyproject.toml
- brak utcnow() deprecation warnings
- brak pustych exceptów bez logowania
"""

from __future__ import annotations

import ast
import os
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).parent.parent


# ---------------------------------------------------------------------------
# Pliki konfiguracyjne — obecność
# ---------------------------------------------------------------------------


class TestConfigFiles:
    """Weryfikuje że pliki konfiguracyjne QoL istnieją i mają wymagane sekcje."""

    def test_pre_commit_config_exists(self):
        assert (PROJECT_ROOT / ".pre-commit-config.yaml").exists(), (
            ".pre-commit-config.yaml nie istnieje — uruchom: cp .pre-commit-config.yaml.example ..."
        )

    def test_env_example_exists(self):
        assert (PROJECT_ROOT / ".env.example").exists(), (
            ".env.example nie istnieje — dokumentuje zmienne środowiskowe"
        )

    def test_env_example_documents_itdoc_strict(self):
        content = (PROJECT_ROOT / ".env.example").read_text()
        assert "ITDOC_STRICT" in content, ".env.example powinno dokumentować zmienną ITDOC_STRICT"

    def test_pre_commit_config_has_ruff(self):
        content = (PROJECT_ROOT / ".pre-commit-config.yaml").read_text()
        assert "ruff" in content, ".pre-commit-config.yaml powinien zawierać hook ruff"

    def test_pre_commit_config_has_autoflake(self):
        content = (PROJECT_ROOT / ".pre-commit-config.yaml").read_text()
        assert "autoflake" in content, ".pre-commit-config.yaml powinien zawierać hook autoflake"

    def test_pyproject_has_ruff_section(self):
        content = (PROJECT_ROOT / "pyproject.toml").read_text()
        assert "[tool.ruff]" in content, "pyproject.toml powinien zawierać sekcję [tool.ruff]"

    def test_pyproject_has_mypy_section(self):
        content = (PROJECT_ROOT / "pyproject.toml").read_text()
        assert "[tool.mypy]" in content, "pyproject.toml powinien zawierać sekcję [tool.mypy]"

    def test_pyproject_dev_deps_include_ruff(self):
        content = (PROJECT_ROOT / "pyproject.toml").read_text()
        assert "ruff" in content, "pyproject.toml dev deps powinny zawierać ruff"

    def test_pyproject_dev_deps_include_pre_commit(self):
        content = (PROJECT_ROOT / "pyproject.toml").read_text()
        assert "pre-commit" in content, "pyproject.toml dev deps powinny zawierać pre-commit"

    def test_pyproject_dev_deps_include_pytest_xdist(self):
        content = (PROJECT_ROOT / "pyproject.toml").read_text()
        assert "pytest-xdist" in content, (
            "pyproject.toml dev deps powinny zawierać pytest-xdist (równoległe testy)"
        )


# ---------------------------------------------------------------------------
# CI Workflows — obecność i poprawność
# ---------------------------------------------------------------------------


class TestCIWorkflows:
    """Weryfikuje że workflows GitHub Actions zawierają wymagane etapy."""

    def _read_workflow(self, name: str) -> str:
        path = PROJECT_ROOT / ".github" / "workflows" / name
        assert path.exists(), f"Workflow {name} nie istnieje"
        return path.read_text()

    def test_ci_has_lint_job(self):
        content = self._read_workflow("ci.yml")
        assert "ruff" in content.lower(), "ci.yml powinien zawierać krok ruff (linting)"

    def test_ci_has_strict_test_job(self):
        content = self._read_workflow("ci.yml")
        assert "ITDOC_STRICT" in content, (
            "ci.yml powinien zawierać job strict-test z ITDOC_STRICT=1"
        )

    def test_ci_has_pytest_xdist(self):
        content = self._read_workflow("ci.yml")
        assert "-n auto" in content or "xdist" in content, (
            "ci.yml powinien uruchamiać pytest z -n auto (pytest-xdist)"
        )

    def test_ci_has_coverage_xml(self):
        content = self._read_workflow("ci.yml")
        assert "coverage.xml" in content, "ci.yml powinien generować coverage.xml dla Codecov"

    def test_ci_has_type_check_job(self):
        content = self._read_workflow("ci.yml")
        assert "mypy" in content, "ci.yml powinien zawierać job type-check z mypy"

    def test_precommit_workflow_exists(self):
        content = self._read_workflow("pre-commit.yml")
        assert "pre-commit" in content

    def test_dependabot_covers_pip(self):
        self._read_workflow("../../.github/dependabot.yml")  # special path
        # Try direct path
        dep_path = PROJECT_ROOT / ".github" / "dependabot.yml"
        assert dep_path.exists(), "dependabot.yml nie istnieje"
        dep_content = dep_path.read_text()
        assert "pip" in dep_content, "dependabot.yml powinien monitorować ekosystem pip"


# ---------------------------------------------------------------------------
# Makefile — nowe cele
# ---------------------------------------------------------------------------


class TestMakefile:
    """Weryfikuje że Makefile zawiera wymagane cele QoL."""

    def _makefile_content(self) -> str:
        return (PROJECT_ROOT / "Makefile").read_text()

    def test_makefile_has_strict_test(self):
        assert "strict-test" in self._makefile_content(), (
            "Makefile powinien zawierać cel strict-test"
        )

    def test_makefile_has_lint_ruff(self):
        content = self._makefile_content()
        assert "ruff" in content, "Makefile powinien używać ruff do lintowania"

    def test_makefile_has_format(self):
        assert "format" in self._makefile_content(), "Makefile powinien zawierać cel format"

    def test_makefile_has_type_check(self):
        assert "type-check" in self._makefile_content(), (
            "Makefile powinien zawierać cel type-check (mypy)"
        )

    def test_makefile_has_test_par(self):
        assert "test-par" in self._makefile_content(), (
            "Makefile powinien zawierać cel test-par (równoległe testy)"
        )

    def test_makefile_strict_test_uses_itdoc_strict(self):
        content = self._makefile_content()
        assert "ITDOC_STRICT=1" in content, "Makefile strict-test powinien ustawiać ITDOC_STRICT=1"

    def test_makefile_has_mutate(self):
        assert "mutate" in self._makefile_content(), (
            "Makefile powinien zawierać cel mutate (mutation testing)"
        )


# ---------------------------------------------------------------------------
# Kod źródłowy — brak utcnow() deprecation
# ---------------------------------------------------------------------------


class TestDeprecationFixes:
    """Weryfikuje że kod nie używa zdeprecjonowanych API."""

    def _find_python_files(self) -> list[Path]:
        files = []
        for pattern in ["itdoc/**/*.py", "scripts/**/*.py"]:
            files.extend(PROJECT_ROOT.glob(pattern))
        return files

    def test_no_datetime_utcnow(self):
        """datetime.utcnow() jest zdeprecjonowane w Python 3.12+."""
        violations = []
        for f in self._find_python_files():
            try:
                content = f.read_text(encoding="utf-8", errors="replace")
                if "utcnow()" in content:
                    violations.append(str(f.relative_to(PROJECT_ROOT)))
            except OSError:
                pass
        assert not violations, (
            f"Znaleziono datetime.utcnow() (zdeprecjonowane) w: {violations}\n"
            "Użyj: datetime.now(timezone.utc)"
        )

    def test_no_bare_except_without_variable(self):
        """Weryfikuje że nie ma 'except SomeType: pass' bez przypisania do zmiennej."""
        violations = []
        for f in self._find_python_files():
            try:
                source = f.read_text(encoding="utf-8", errors="replace")
                tree = ast.parse(source)
            except (OSError, SyntaxError):
                continue

            for node in ast.walk(tree):
                if not isinstance(node, ast.ExceptHandler):
                    continue
                # Puste ciało (tylko pass lub ...) bez `as exc`
                if node.name is None:
                    body = node.body
                    if len(body) == 1 and isinstance(body[0], (ast.Pass, ast.Expr)):
                        if isinstance(body[0], ast.Expr) and isinstance(
                            body[0].value, ast.Constant
                        ):
                            violations.append(f"{f.relative_to(PROJECT_ROOT)}:{node.lineno}")
                        elif isinstance(body[0], ast.Pass):
                            violations.append(f"{f.relative_to(PROJECT_ROOT)}:{node.lineno}")

        assert not violations, (
            "Znaleziono puste excepts bez `as exc` (py/empty-except):\n"
            + "\n".join(f"  {v}" for v in violations[:20])
            + "\nUżyj: except SomeError as exc: _log.debug(..., exc)"
        )


# ---------------------------------------------------------------------------
# ITDOC_STRICT — zachowanie batch_continue()
# ---------------------------------------------------------------------------


class TestStrictModeIntegration:
    """Weryfikuje że ITDOC_STRICT=1 działa end-to-end przez zmienną środowiskową."""

    def test_strict_mode_env_var_respected(self):
        """batch_continue() w STRICT=1 powinien re-rzucać wyjątek jako RuntimeError."""
        from itdoc._batch import batch_continue

        old = os.environ.get("ITDOC_STRICT")
        try:
            os.environ["ITDOC_STRICT"] = "1"
            with pytest.raises(RuntimeError, match="batch_continue"):
                with batch_continue("test context"):
                    raise ValueError("intentional error")
        finally:
            if old is None:
                os.environ.pop("ITDOC_STRICT", None)
            else:
                os.environ["ITDOC_STRICT"] = old

    def test_non_strict_mode_swallows_exception(self):
        """batch_continue() bez STRICT=1 powinien połknąć wyjątek."""
        from itdoc._batch import batch_continue

        old = os.environ.get("ITDOC_STRICT")
        try:
            os.environ.pop("ITDOC_STRICT", None)
            # Nie powinno rzucić wyjątku
            with batch_continue("test context"):
                raise ValueError("swallowed error")
        finally:
            if old is not None:
                os.environ["ITDOC_STRICT"] = old

    def test_strict_mode_zero_string_not_strict(self):
        """ITDOC_STRICT=0 (string) powinien być traktowany jako wyłączony."""
        from itdoc._batch import batch_continue

        old = os.environ.get("ITDOC_STRICT")
        try:
            os.environ["ITDOC_STRICT"] = "0"
            # Nie powinno rzucić
            with batch_continue("test context"):
                raise ValueError("should be swallowed")
        finally:
            if old is None:
                os.environ.pop("ITDOC_STRICT", None)
            else:
                os.environ["ITDOC_STRICT"] = old
