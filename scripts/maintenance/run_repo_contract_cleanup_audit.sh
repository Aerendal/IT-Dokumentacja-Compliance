#!/usr/bin/env bash
# run_repo_contract_cleanup_audit.sh
# Zbiera kompletny pakiet dowodowy stanu repo po wycofaniu satellite i imported.
# Uruchom: bash run_repo_contract_cleanup_audit.sh
# Wynik:   repo_contract_cleanup_FINAL.tar.gz

set -uo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$REPO_DIR"

REPORT="$REPO_DIR/reports/repo_cleanup_final"
rm -rf "$REPORT"
mkdir -p "$REPORT/meta" "$REPORT/logs" "$REPORT/grep"

echo "=== Repo cleanup final audit ==="
echo "Working directory: $REPO_DIR"
echo "Report directory:  $REPORT"
echo ""

# ---------------------------------------------------------------------------
# META
# ---------------------------------------------------------------------------
echo "[1/7] Meta informacje..."

git rev-parse --short HEAD > "$REPORT/meta/00_head.txt"
git status --short > "$REPORT/meta/01_git_status.txt"
git log --oneline -10 > "$REPORT/meta/02_git_log.txt"
find generated_templates -maxdepth 2 -type d | sort > "$REPORT/meta/03_templates_tree.txt"
git ls-files | awk -F/ '{print $1}' | sort | uniq -c | sort -rn > "$REPORT/meta/04_tracked_by_dir.txt"

# ---------------------------------------------------------------------------
# GIT GREP: satellite
# ---------------------------------------------------------------------------
echo "[2/7] grep satellite..."

git grep -n 'satellite' -- . ':!generated_templates' \
  > "$REPORT/grep/10_satellite_all.txt" 2>&1 || true

git grep -n 'satellite' \
  -- . ':!generated_templates' \
     ':!CHANGELOG.md' \
     ':!scripts/maintenance/satellite_linker.py' \
     ':!scripts/maintenance/enrich_placeholders.py' \
     ':!tests/test_maintenance_scripts.py' \
     ':!docs/OPEN_DECISIONS.md' \
     ':!docs/CLOSURE_CHECKLIST.md' \
  > "$REPORT/grep/11_satellite_unexpected.txt" 2>&1 || true

UNEXPECTED=$(wc -l < "$REPORT/grep/11_satellite_unexpected.txt")
echo "Nieoczekiwane odwołania satellite: $UNEXPECTED" >> "$REPORT/grep/11_satellite_unexpected.txt"

# ---------------------------------------------------------------------------
# GIT GREP: imported (katalog, nie Python import)
# ---------------------------------------------------------------------------
echo "[3/7] grep imported (templates dir)..."

git grep -n 'generated_templates/imported' -- . \
  > "$REPORT/grep/12_imported_templates_dir.txt" 2>&1 || true

IMPORTED_REFS=$(wc -l < "$REPORT/grep/12_imported_templates_dir.txt")
echo "Odwołania do generated_templates/imported: $IMPORTED_REFS" >> "$REPORT/grep/12_imported_templates_dir.txt"

# ---------------------------------------------------------------------------
# DOCTOR
# ---------------------------------------------------------------------------
echo "[4/7] doctor --strict..."

python3 scripts/doctor.py --strict > "$REPORT/logs/20_doctor.txt" 2>&1
echo $? > "$REPORT/logs/20_doctor.exit"

# ---------------------------------------------------------------------------
# BOOTSTRAP
# ---------------------------------------------------------------------------
echo "[5/7] bootstrap_runtime..."

python3 scripts/bootstrap_runtime.py > "$REPORT/logs/21_bootstrap.txt" 2>&1
echo $? > "$REPORT/logs/21_bootstrap.exit"

# ---------------------------------------------------------------------------
# BUILD CURRENT
# ---------------------------------------------------------------------------
echo "[6/7] build_current..."

python3 scripts/build_current.py \
  --db reports/it_doc_matrix_clean.db \
  --templates-root generated_templates \
  --alignment-log reports/alignment_log.csv \
  --mode rebuild \
  > "$REPORT/logs/22_build_current.txt" 2>&1
echo $? > "$REPORT/logs/22_build_current.exit"

# ---------------------------------------------------------------------------
# PIPELINE
# ---------------------------------------------------------------------------
python3 scripts/pipeline_run.py > "$REPORT/logs/23_pipeline.txt" 2>&1
echo $? > "$REPORT/logs/23_pipeline.exit"

# ---------------------------------------------------------------------------
# TESTY
# ---------------------------------------------------------------------------
python3 -m pytest -q -m "not integration and not slow" \
  > "$REPORT/logs/24_fast_suite.txt" 2>&1
echo $? > "$REPORT/logs/24_fast_suite.exit"

python3 -m pytest -q -m "integration and not slow" \
  > "$REPORT/logs/25_integration_suite.txt" 2>&1
echo $? > "$REPORT/logs/25_integration_suite.exit"

# ---------------------------------------------------------------------------
# RAPORT KOŃCOWY
# ---------------------------------------------------------------------------
echo "[7/7] Raport końcowy..."

DOCTOR_EXIT=$(cat "$REPORT/logs/20_doctor.exit")
BOOTSTRAP_EXIT=$(cat "$REPORT/logs/21_bootstrap.exit")
BUILD_EXIT=$(cat "$REPORT/logs/22_build_current.exit")
PIPELINE_EXIT=$(cat "$REPORT/logs/23_pipeline.exit")
FAST_EXIT=$(cat "$REPORT/logs/24_fast_suite.exit")
INTEGRATION_EXIT=$(cat "$REPORT/logs/25_integration_suite.exit")
SAT_UNEXPECTED=$(grep -v "Nieoczekiwane" "$REPORT/grep/11_satellite_unexpected.txt" | wc -l)
IMPORTED_DIR_REFS=$(grep -v "Odwołania do" "$REPORT/grep/12_imported_templates_dir.txt" | wc -l)

cat > "$REPORT/meta/99_final_assessment.txt" << EOF
=== REPO CONTRACT CLEANUP — FINAL ASSESSMENT ===
Data: $(date -u +%Y-%m-%dT%H:%M:%SZ)
HEAD: $(cat "$REPORT/meta/00_head.txt")

--- WYNIKI KOMEND ---
doctor --strict:       exit=$DOCTOR_EXIT  (expected: 0)
bootstrap_runtime:     exit=$BOOTSTRAP_EXIT  (expected: 0)
build_current (core):  exit=$BUILD_EXIT  (expected: 0)
pipeline_run:          exit=$PIPELINE_EXIT  (expected: 1 = pre-existing coverage preconditions)
fast suite:            exit=$FAST_EXIT  (expected: 0)
integration suite:     exit=$INTEGRATION_EXIT  (expected: 0)

--- GREP WYNIKI ---
Nieoczekiwane odwołania 'satellite' poza świadomymi plikami: $SAT_UNEXPECTED
Odwołania do 'generated_templates/imported': $IMPORTED_DIR_REFS

--- WERDYKT ---
$([ "$DOCTOR_EXIT" = "0" ] && echo "PASS: doctor" || echo "FAIL: doctor exit=$DOCTOR_EXIT")
$([ "$BOOTSTRAP_EXIT" = "0" ] && echo "PASS: bootstrap" || echo "FAIL: bootstrap exit=$BOOTSTRAP_EXIT")
$([ "$BUILD_EXIT" = "0" ] && echo "PASS: build_current" || echo "FAIL: build_current exit=$BUILD_EXIT")
$([ "$FAST_EXIT" = "0" ] && echo "PASS: fast suite" || echo "FAIL: fast suite exit=$FAST_EXIT")
$([ "$INTEGRATION_EXIT" = "0" ] && echo "PASS: integration suite" || echo "FAIL: integration suite exit=$INTEGRATION_EXIT")
$([ "$SAT_UNEXPECTED" = "0" ] && echo "PASS: satellite refs clean" || echo "WARN: $SAT_UNEXPECTED unexpected satellite refs")
$([ "$IMPORTED_DIR_REFS" = "0" ] && echo "PASS: no imported dir refs" || echo "WARN: $IMPORTED_DIR_REFS refs to generated_templates/imported")

--- ŚWIADOME WYJĄTKI (satellite_linker = DB concept, nie katalog) ---
CHANGELOG.md               — historyczny zapis zmian
docs/OPEN_DECISIONS.md     — OD-003 CLOSED
docs/CLOSURE_CHECKLIST.md  — historyczny checkpoint, OD-003 zaktualizowane
satellite_linker.py        — doc_satellites DB relacja parent-child
enrich_placeholders.py     — SQL JOIN na doc_satellites
test_maintenance_scripts.py — testy dla satellite_linker

--- ŚWIADOME WYJĄTKI (generated_templates/imported — opis historyczny) ---
CHANGELOG.md:13              — "przeniesiony do semantic lab" (past tense)
docs/DATA_LAYERS.md:55       — "zawierał surowe dane" (past tense, historyczny opis warstwy)
docs/EXTERNAL_REVIEW.md:155  — "został wycofany z kontraktu" (past tense, nota dla recenzenta)
docs/OPEN_DECISIONS.md:160   — OD-006 CLOSED, Opcja B (decyzja archiwalna)
EOF

# ---------------------------------------------------------------------------
# PAKOWANIE
# ---------------------------------------------------------------------------
PACK="$REPO_DIR/repo_contract_cleanup_FINAL.tar.gz"
tar -czf "$PACK" -C "$(dirname "$REPORT")" "$(basename "$REPORT")"

echo ""
echo "=== GOTOWE ==="
echo "Paczka: $PACK"
echo "Rozmiar: $(du -sh "$PACK" | cut -f1)"
echo ""
echo "Werdykt końcowy:"
grep -E "^(PASS|FAIL|WARN)" "$REPORT/meta/99_final_assessment.txt"
