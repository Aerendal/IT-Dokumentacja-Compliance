#!/bin/bash
# start_server.sh — uruchamia IT Dokumentacja Compliance API
# Użycie: ./scripts/api/start_server.sh [--port 8000] [--reload]

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"

# Default values
PORT=${IT_DOC_PORT:-8000}
HOST=${IT_DOC_HOST:-"127.0.0.1"}
DB_PATH=${IT_DOC_DB:-"$PROJECT_ROOT/reports/it_doc_matrix.db"}
API_TOKEN=${IT_DOC_API_TOKEN:-"change-me-before-production"}
RELOAD=""

# Parse args
while [[ "$#" -gt 0 ]]; do
  case $1 in
    --port) PORT="$2"; shift ;;
    --host) HOST="$2"; shift ;;
    --reload) RELOAD="--reload" ;;
    --help) echo "Usage: $0 [--port PORT] [--host HOST] [--reload]"; exit 0 ;;
  esac
  shift
done

# Warn if using default token
if [[ "$API_TOKEN" == "change-me-before-production" ]]; then
  echo "WARNING: Using default API token. Set IT_DOC_API_TOKEN env var for production." >&2
fi

# Check DB exists
if [[ ! -f "$DB_PATH" ]]; then
  echo "ERROR: DB not found at $DB_PATH" >&2
  exit 1
fi

export IT_DOC_DB="$DB_PATH"
export IT_DOC_API_TOKEN="$API_TOKEN"

echo "Starting IT Dokumentacja Compliance API"
echo "  Host:  $HOST:$PORT"
echo "  DB:    $DB_PATH"
echo "  Docs:  http://$HOST:$PORT/docs"

cd "$PROJECT_ROOT"
exec uvicorn scripts.api.main:app --host "$HOST" --port "$PORT" $RELOAD
