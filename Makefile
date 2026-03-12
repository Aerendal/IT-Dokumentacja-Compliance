# Makefile — IT Dokumentacja dev tasks
# Uruchamiaj z katalogu projektu (dokumentacja/)

PYTEST       = python3 -m pytest
PYTEST_Q     = $(PYTEST) -m "not slow and not integration" -q
PYTEST_PAR   = $(PYTEST_Q) -n auto           # równoległe (pytest-xdist)
DB_PATH      = reports/it_doc_matrix.db
RUFF         = python3 -m ruff
SRC          = itdoc/ scripts/ tests/

.PHONY: test test-all test-par strict-test lint lint-ruff format type-check \
        mutate check install hooks hooks-run clean help

help:
	@echo ""
	@echo "╔══════════════════════════════════════════════════════════════╗"
	@echo "║           IT Dokumentacja — dostępne cele make               ║"
	@echo "╠══════════════════════════════════════════════════════════════╣"
	@echo "║  INSTALACJA                                                  ║"
	@echo "║    make install      pip install -e .[dev]                   ║"
	@echo "║    make hooks        zainstaluj pre-commit hooks             ║"
	@echo "║    make hooks-run    uruchom pre-commit na wszystkich plikach ║"
	@echo "╠══════════════════════════════════════════════════════════════╣"
	@echo "║  TESTY                                                       ║"
	@echo "║    make test         pytest (bez slow/integration), szybki   ║"
	@echo "║    make test-par     pytest równoległy -n auto (szybszy CI)  ║"
	@echo "║    make test-all     pytest pełny zestaw (wymaga DB)         ║"
	@echo "║    make strict-test  ITDOC_STRICT=1 — ujawnia ukryte błędy  ║"
	@echo "╠══════════════════════════════════════════════════════════════╣"
	@echo "║  JAKOŚĆ KODU                                                 ║"
	@echo "║    make lint         ruff check (linter)                     ║"
	@echo "║    make format       ruff format (formatter)                 ║"
	@echo "║    make type-check   mypy itdoc/ (statyczne typy)            ║"
	@echo "║    make mutate       mutmut (mutation testing, wolny)        ║"
	@echo "╠══════════════════════════════════════════════════════════════╣"
	@echo "║  PEŁNA WALIDACJA                                             ║"
	@echo "║    make check        install + lint + test (lokalne CI)      ║"
	@echo "║    make clean        usuń __pycache__, .pytest_cache         ║"
	@echo "╚══════════════════════════════════════════════════════════════╝"
	@echo ""

# ── Instalacja ──────────────────────────────────────────────────────────────

install:
	pip install -e ".[dev]" -q

hooks:
	@if command -v pre-commit >/dev/null 2>&1; then \
		pre-commit install; \
		echo "✓ pre-commit hooks zainstalowane"; \
	else \
		echo "pre-commit niedostępny — uruchom: pip install pre-commit"; \
		exit 1; \
	fi

hooks-run:
	pre-commit run --all-files

# ── Testy ───────────────────────────────────────────────────────────────────

test:
	@echo "▶ pytest (unit + fast, bez slow/integration)..."
	$(PYTEST_Q)

test-par:
	@echo "▶ pytest równoległy (n=auto)..."
	$(PYTEST_PAR)

test-all:
	@echo "▶ pytest pełny zestaw (wymaga DB)..."
	$(PYTEST)

strict-test:
	@echo "▶ pytest w trybie STRICT — batch_continue() re-rzuca wyjątki..."
	@echo "   Użyj do debugowania ukrytych błędów w skryptach batch."
	ITDOC_STRICT=1 $(PYTEST_Q) -x

# ── Jakość kodu ─────────────────────────────────────────────────────────────

lint:
	@echo "▶ ruff check (linter)..."
	$(RUFF) check $(SRC)

lint-fix:
	@echo "▶ ruff check --fix (auto-naprawa)..."
	$(RUFF) check --fix $(SRC)

format:
	@echo "▶ ruff format..."
	$(RUFF) format $(SRC)

format-check:
	@echo "▶ ruff format --check (weryfikacja formatowania)..."
	$(RUFF) format --check $(SRC)

type-check:
	@echo "▶ mypy itdoc/ (statyczne sprawdzanie typów)..."
	@if command -v mypy >/dev/null 2>&1; then \
		mypy itdoc/ --ignore-missing-imports --no-error-summary; \
	else \
		echo "mypy niedostępny — uruchom: pip install mypy"; \
	fi

mutate:
	@echo "▶ mutmut run (mutation testing — może trwać kilka minut)..."
	@if command -v mutmut >/dev/null 2>&1; then \
		mutmut run; \
		mutmut results; \
	else \
		echo "mutmut niedostępny — uruchom: pip install mutmut"; \
	fi

# ── Pełna walidacja (odpowiednik lokalnego CI) ───────────────────────────────

check: install lint test
	@echo ""
	@echo "✓ Lokalne CI zakończone (install + lint + test)"

# ── Czyszczenie ──────────────────────────────────────────────────────────────

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -name "*.pyc" -delete 2>/dev/null || true
	find . -name ".ruff_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -name ".mypy_cache" -exec rm -rf {} + 2>/dev/null || true
	@echo "✓ Wyczyszczone"

