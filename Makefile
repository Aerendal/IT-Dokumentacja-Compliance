# Makefile — IT Dokumentacja dev tasks
# Uruchamiaj z katalogu projektu (dokumentacja/)

PYTEST       = python3 -m pytest
PYTEST_Q     = $(PYTEST) -m "not slow and not integration" -q
PYTEST_PAR   = $(PYTEST_Q) -n auto           # równoległe (pytest-xdist)
DB_PATH      = reports/it_doc_matrix.db
RUFF         = python3 -m ruff
SRC          = itdoc/ scripts/ tests/

.PHONY: test test-all test-par strict-test lint lint-ruff format type-check \
        mutate check install hooks hooks-run clean help \
        new-template validate-templates audit-templates \
        bulk-patch bulk-enrich enrich-standards enrich-placeholders

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
	@echo "║  SZABLONY — tworzenie i zarządzanie                          ║"
	@echo "║    make new-template          wizard CLI (args lub interakt.) ║"
	@echo "║    make validate-templates    sprawdź schemat wszystkich      ║"
	@echo "║    make audit-templates       raport pokrycia norm            ║"
	@echo "║    make bulk-patch            masowa aktualizacja sekcji      ║"
	@echo "║    make bulk-enrich           uzupełnij małe szablony         ║"
	@echo "║    make enrich-standards      dodaj referencje do norm        ║"
	@echo "║    make enrich-placeholders   wypełnij placeholdery treścią   ║"
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
	@echo "  Przykłady szablonów:"
	@echo "    make new-template TITLE='Zarządzanie Incydentami' TYPE=core \\"
	@echo "                      STANDARD='ISO/IEC 27001' GOAL='Opis celu'"
	@echo "    make bulk-patch   SECTION='Zakres' OP=append CONTENT='- nowy punkt' DRY=1"
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

# ── Szablony ─────────────────────────────────────────────────────────────────
# Zmienne z wartościami domyślnymi (nadpisz przez make new-template TITLE=... itd.)
TITLE    ?=
TYPE     ?= core
STANDARD ?=
REGULATION ?=
GOAL     ?=
DRY      ?= 1
SECTION  ?=
OP       ?= append
CONTENT  ?=
FILTER_STD ?=
FILTER_GLOB ?=

new-template:
	@python3 scripts/new_template_wizard.py \
		$(if $(TITLE),--title "$(TITLE)") \
		$(if $(TYPE),--type "$(TYPE)") \
		$(if $(STANDARD),--standard "$(STANDARD)") \
		$(if $(REGULATION),--regulation "$(REGULATION)") \
		$(if $(GOAL),--goal "$(GOAL)") \
		$(if $(filter 1,$(DRY)),--dry-run)

validate-templates:
	@echo "▶ Walidacja schematów szablonów..."
	python3 scripts/validate_template_schema.py --report --strict

audit-templates:
	@echo "▶ Generowanie raportu pokrycia norm..."
	python3 scripts/generate_audit_report.py
	@echo "✓ Raport: reports/standards_audit_report.md"

# Masowa aktualizacja sekcji w szablonach.
# Przykład: make bulk-patch SECTION='Zakres' OP=append CONTENT='- nowy punkt' DRY=0
bulk-patch:
	@if [ -z "$(SECTION)" ]; then \
		echo "BŁĄD: podaj SECTION='nazwa sekcji'"; exit 1; \
	fi
	@python3 scripts/maintenance/bulk_section_patcher.py \
		$(if $(FILTER_STD),--filter-standard "$(FILTER_STD)") \
		$(if $(FILTER_GLOB),--filter-glob "$(FILTER_GLOB)") \
		$(if $(filter append,$(OP)),--append-to-section "$(SECTION)" --section-content "$(CONTENT)") \
		$(if $(filter replace,$(OP)),--replace-in-section "$(SECTION)" --section-content "$(CONTENT)") \
		$(if $(filter add,$(OP)),--add-section "## $(SECTION)" --section-content "$(CONTENT)") \
		$(if $(filter 1,$(DRY)),--dry-run)

# Wzbogacanie małych szablonów — faza 10 potoku
bulk-enrich:
	@echo "▶ Uzupełnianie małych szablonów brakującymi sekcjami..."
	python3 scripts/enrich_small_templates.py $(if $(filter 1,$(DRY)),--dry-run)

# Dodawanie referencji do norm i regulacji w guidance
enrich-standards:
	@echo "▶ Mapowanie sekcji na normy i regulacje..."
	python3 scripts/enrich_guidance_standards.py

# Wypełnianie placeholderów archetypową treścią
enrich-placeholders:
	@echo "▶ Wypełnianie placeholderów w szablonach..."
	python3 scripts/maintenance/enrich_placeholders.py $(if $(filter 1,$(DRY)),--dry-run)

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
