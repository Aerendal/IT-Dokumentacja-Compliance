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
# pre-commit hook — uruchamia testy przed commitem
# Wygenerowany przez scripts/install_hooks.sh

# Znajdź katalog dokumentacja/ (hook uruchamia się z root repo)
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
DOC_DIR="$REPO_ROOT"

# Sprawdź czy pytest dostępny
if ! command -v python3 >/dev/null 2>&1; then
    echo "pre-commit: python3 niedostępny — pomijam testy"
    exit 0
fi

echo "▶ pre-commit: pytest -m 'not slow' -q ..."
cd "$DOC_DIR"
if python3 -m pytest -m "not slow" -q --tb=short 2>&1; then
    echo "✓ Testy OK"
    exit 0
else
    echo ""
    echo "✗ Testy FAIL — commit zablokowany."
    echo "  Uruchom: cd dokumentacja && make test"
    exit 1
fi
HOOK

chmod +x "$HOOK_FILE"
echo "✓ pre-commit hook zainstalowany: $HOOK_FILE"
echo "  Przy każdym 'git commit' uruchomi się pytest (not slow)."
echo "  Aby pominąć jednorazowo: git commit --no-verify"
