# Makefile — IT Dokumentacja dev tasks
# Uruchamiaj z katalogu dokumentacja/

PYTEST    = python3 -m pytest
PYTEST_Q  = $(PYTEST) -m "not slow" -q
DB_PATH   = reports/it_doc_matrix.db

.PHONY: test test-all lint check install hooks clean help

help:
	@echo "Dostępne cele:"
	@echo "  make install   - pip install -e .[dev]"
	@echo "  make test      - pytest (bez slow), wymaga DB"
	@echo "  make test-all  - pytest (z slow)"
	@echo "  make lint      - sprawdź styl kodu (flake8 jeśli dostępny)"
	@echo "  make check     - install + test (pełna walidacja)"
	@echo "  make hooks     - zainstaluj pre-commit hook"
	@echo "  make clean     - usuń __pycache__, .pytest_cache"

install:
	pip install -e ".[dev]" -q

test:
	@echo "▶ pytest (unit + integration, bez slow)..."
	$(PYTEST_Q)

test-all:
	@echo "▶ pytest (pełny zestaw)..."
	$(PYTEST)

lint:
	@if command -v flake8 >/dev/null 2>&1; then \
		flake8 itdoc/ --max-line-length=100 --ignore=E501,W503; \
	else \
		echo "flake8 niedostępny — pomiń lint lub: pip install flake8"; \
	fi

check: install test

hooks:
	@bash scripts/install_hooks.sh

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -name "*.pyc" -delete 2>/dev/null || true
	@echo "✓ Wyczyszczone"
