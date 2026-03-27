#!/usr/bin/env bash
# scripts/install_hooks.sh — instaluje pre-commit hook dla IT Dokumentacja
#
# Uruchamiaj z katalogu dokumentacja/:
#   bash scripts/install_hooks.sh

set -e

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
HOOK_DIR="$REPO_ROOT/.git/hooks"
HOOK_FILE="$HOOK_DIR/pre-commit"

if [ ! -d "$HOOK_DIR" ]; then
    echo "UWAGA: $HOOK_DIR nie istnieje — nie jesteś w repo git."
    echo "Utwórz repo: cd \"$REPO_ROOT\" && git init"
    exit 1
fi

cat > "$HOOK_FILE" << 'HOOK'
#!/usr/bin/env bash
# pre-commit hook — uruchamia testy przez .venv zamiast systemowego Pythona
# Wygenerowany przez scripts/install_hooks.sh

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
DOC_DIR="$REPO_ROOT"
VENV_PYTHON="$REPO_ROOT/.venv/bin/python"

# Jeśli .venv nie istnieje, użyj systemowego Pythona z ostrzeżeniem
if [ ! -x "$VENV_PYTHON" ]; then
    echo "pre-commit: .venv not found — falling back to system python3" >&2
    echo "  Run: python3 -m venv .venv && source .venv/bin/activate && pip install -e '.[dev]'" >&2
    VENV_PYTHON="python3"
fi

echo "▶ pre-commit: pytest -m 'not slow and not integration' -q ..."
cd "$DOC_DIR"
if "$VENV_PYTHON" -m pytest -m "not slow and not integration" -q --tb=short 2>&1; then
    echo "✓ Testy OK"
    exit 0
else
    echo ""
    echo "✗ Testy FAIL — commit zablokowany."
    echo "  Uruchom: python3 -m pytest -m 'not slow and not integration'"
    exit 1
fi
HOOK

chmod +x "$HOOK_FILE"
echo "✓ pre-commit hook zainstalowany: $HOOK_FILE"
echo "  Hook używa .venv/bin/python (z fallback na python3 gdy brak .venv)."
echo "  Aby pominąć jednorazowo: git commit --no-verify"
