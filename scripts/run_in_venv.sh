#!/usr/bin/env bash
# scripts/run_in_venv.sh — uruchamia komendę przez .venv/bin/python
#
# Użycie:
#   scripts/run_in_venv.sh scripts/doctor.py --strict
#   scripts/run_in_venv.sh -m pytest -q -m "not slow and not integration"
#
# Jeśli .venv nie istnieje, wypisuje instrukcję naprawczą i kończy z błędem.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
VENV_PYTHON="$REPO_ROOT/.venv/bin/python"

if [ ! -x "$VENV_PYTHON" ]; then
    echo "ERROR: .venv not found at $REPO_ROOT/.venv" >&2
    echo "  Run bootstrap:" >&2
    echo "    python3 -m venv .venv" >&2
    echo "    source .venv/bin/activate" >&2
    echo "    pip install -e '.[dev]'" >&2
    exit 1
fi

exec "$VENV_PYTHON" "$@"
