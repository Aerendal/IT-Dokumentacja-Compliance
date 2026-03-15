---
title: "NLP Engine — Integracja z Istniejącym Projektem"
document_class: ARCH
gold_standard: "ISO/IEC 42010:2022"
validation_mode: PRE_PRODUCTION
version: "0.1"
tags:
  - nlp-engine
  - integration
  - database-schema
  - api
  - cli
audit_rules:
  - ARCH-01
  - ARCH-06
  - API-01
related_docs:
  - "ARCHITECTURE.md"
  - "IMPLEMENTATION_PLAN.md"
  - "DOC_AUDIT_MODULE.md"
---

# NLP Engine — Integracja z Istniejącym Projektem

## Stan bieżący — istniejące punkty integracji (✅ Zaimplementowane)

Przed uruchomieniem Faz 1–5 powstał **Moduł Audytu Dokumentacji**, który już jest
zintegrowany z projektem w następujący sposób:

### `scripts/compliance_check.py` — subkomenda `doc-audit`

```bash
python scripts/compliance_check.py doc-audit --dir dokumentacja/docs/
```

Wywołuje `DocAuditor.scan()` z modułu `scripts.nlp.doc_auditor`. Wyniki trafiają
do `reports/it_doc_audit.db` (osobna baza — nie `it_doc_matrix.db`).

### `reports/it_doc_audit.db` — baza wyników audytu docs

5 tabel (schemat w `scripts/nlp/ddl_audit.sql`):
- `doc_audit_runs` — przebiegi
- `doc_completeness` — score per dokument
- `doc_audit_findings` — luki (ERROR/WARNING/INFO)
- `doc_duplicates` — pary duplikatów
- `doc_relations` — graf powiązań

**Dlaczego osobna baza?** Audyt dokumentacji to oddzielna domena od matrycy zgodności (`it_doc_matrix.db`). Wyniki doc-audit są wejściem diagnostycznym, nie częścią pipeline compliance.

---

## Zasada integracji (dla Faz 1–5)

NLP Engine **nie zastępuje** żadnego istniejącego kodu. Działa jako **addytywna warstwa**:
- dodaje nowe tabele do SQLite
- dodaje kolumny do istniejących tabel (niedestrukcyjnie — `ALTER TABLE ADD COLUMN`)
- dodaje nowy router do istniejącego FastAPI
- dodaje nową komendę do istniejącego CLI
- istniejące testy **muszą nadal przechodzić** po integracji

---

## Zmiany w schemacie SQLite

### Nowe tabele

```sql
-- Wyniki ewaluacji pluginów compliance
CREATE TABLE IF NOT EXISTS nlp_findings (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    doc_path      TEXT    NOT NULL,
    sentence_id   INTEGER,
    finding_id    TEXT    NOT NULL,          -- np. "ACC-001"
    plugin        TEXT    NOT NULL,          -- "AccessControlPlugin"
    standard_code TEXT,                      -- "ISO/IEC 27001"
    control_id    TEXT,                      -- "A.9.2.1"
    severity      TEXT    NOT NULL,          -- OK/INFO/WARNING/ERROR
    raw_text      TEXT,                      -- zdanie które wyzwoliło finding
    message       TEXT,
    evidence      TEXT,
    remediation   TEXT,
    locked        INTEGER DEFAULT 0,         -- 1 = ConclusionFreezer zablokował
    created_at    TEXT    DEFAULT CURRENT_TIMESTAMP
);

-- Macierz pokrycia (traceability)
CREATE TABLE IF NOT EXISTS nlp_traceability (
    id               INTEGER PRIMARY KEY AUTOINCREMENT,
    doc_path         TEXT,
    section          TEXT,                   -- np. "3.2"
    requirement_text TEXT,
    semantic_role    TEXT,                   -- JSON: {agent, action, patient, instrument}
    standard_code    TEXT,
    control_id       TEXT,
    validation_mode  TEXT,                   -- PRE_PRODUCTION/POST_EXECUTION
    status           TEXT,                   -- PLAN_OK/MISSING_EVIDENCE/EVIDENCE_OK
    created_at       TEXT    DEFAULT CURRENT_TIMESTAMP
);
```

### Rozszerzenie istniejących tabel

```sql
-- Istniejąca tabela doc_standard_mapping
ALTER TABLE doc_standard_mapping ADD COLUMN nlp_confidence  REAL;
ALTER TABLE doc_standard_mapping ADD COLUMN nlp_evidence    TEXT;  -- zdanie-dowód wyekstrahowane przez SRL
ALTER TABLE doc_standard_mapping ADD COLUMN validation_mode TEXT;  -- PRE_PRODUCTION/POST_EXECUTION

-- Istniejąca tabela template_violations
ALTER TABLE template_violations ADD COLUMN nlp_finding_id TEXT;    -- powiązanie z nlp_findings
ALTER TABLE template_violations ADD COLUMN sentence_id    INTEGER;
ALTER TABLE template_violations ADD COLUMN raw_text       TEXT;
```

**Uwaga:** Wszystkie `ALTER TABLE ADD COLUMN` są bezpieczne (nowe kolumny mają DEFAULT NULL — nie naruszają istniejących danych ani zapytań).

---

## Rozszerzenie FastAPI (`scripts/api/main.py`)

### Nowy router

```python
# scripts/api/nlp_router.py
from fastapi import APIRouter, Depends, HTTPException
from scripts.nlp.nlp_engine import run_nlp_audit
from scripts.api.main import get_db, verify_token

nlp_router = APIRouter(prefix="/nlp", tags=["NLP Audit"])

@nlp_router.post("/audit")
def nlp_audit(
    path: str,
    mode: str = "PRE_PRODUCTION",
    token: str = Depends(verify_token),
    conn = Depends(get_db),
):
    """Uruchamia pełny NLP audit dokumentu."""
    findings = run_nlp_audit(path, mode=mode, conn=conn)
    return {"findings": findings, "total": len(findings)}

@nlp_router.get("/findings/{doc_path:path}")
def get_findings(doc_path: str, conn = Depends(get_db)):
    """Zwraca zapisane findings dla dokumentu."""
    rows = conn.execute(
        "SELECT * FROM nlp_findings WHERE doc_path = ? ORDER BY severity DESC",
        [doc_path]
    ).fetchall()
    return [dict(r) for r in rows]
```

### Rejestracja routera w `main.py`

```python
# Dodać do scripts/api/main.py:
from scripts.api.nlp_router import nlp_router
app.include_router(nlp_router)
```

---

## Rozszerzenie CLI (`itdoc/cli.py`)

### Nowa komenda `nlp-audit`

```python
# Dodać do itdoc/cli.py:

def cmd_nlp_audit(args: argparse.Namespace) -> int:
    """Uruchamia NLP audit dokumentu."""
    from scripts.nlp.nlp_engine import run_nlp_audit
    try:
        findings = run_nlp_audit(
            args.doc,
            mode=args.mode,
            db_path=args.db or DB_DEFAULT
        )
        errors   = [f for f in findings if f["severity"] == "ERROR"]
        warnings = [f for f in findings if f["severity"] == "WARNING"]
        print(f"NLP Audit: {args.doc}")
        print(f"  ERRORs:   {len(errors)}")
        print(f"  WARNINGs: {len(warnings)}")
        for f in errors + warnings:
            print(f"  [{f['severity']}] {f['finding_id']} — {f['message']}")
        return 1 if errors else 0
    except Exception as e:
        print(f"Błąd NLP audit: {e}", file=sys.stderr)
        return 2

# W build_parser():
nlp_p = sub.add_parser("nlp-audit", help="Semantyczny audit dokumentu")
nlp_p.add_argument("doc", help="Ścieżka do dokumentu")
nlp_p.add_argument("--mode", choices=["PRE_PRODUCTION", "POST_EXECUTION"],
                   default="PRE_PRODUCTION")
nlp_p.add_argument("--db", help="Ścieżka do bazy SQLite")
nlp_p.set_defaults(func=cmd_nlp_audit)
```

---

## Makefile

```makefile
# Dodać do Makefile:
.PHONY: nlp-audit nlp-test nlp-install

nlp-install:
	pip install morfeusz2 ufal.udpipe spacy
	python -m spacy download pl_core_news_sm

nlp-audit:
	python scripts/nlp/nlp_engine.py --doc $(DOC) --mode $(MODE)

nlp-test:
	python -m pytest tests/test_nlp_*.py -v
```

---

## GitHub Actions

```yaml
# Dodać do .github/workflows/ci.yml (nowy job lub rozszerzenie istniejącego):
- name: Install NLP dependencies
  run: |
    pip install morfeusz2 ufal.udpipe spacy
    python -m spacy download pl_core_news_sm

- name: Run NLP tests
  run: python -m pytest tests/test_nlp_*.py -v --tb=short
```

---

## Mapowanie NLP → istniejące mechanizmy

| Istniejący mechanizm | Ograniczenie | Co dodaje NLP |
|---|---|---|
| Keyword matching w `map_standards_to_docs.py` | "TLS" pasuje też do "ATLAS" | SRL + kontekst → tylko prawdziwe użycia |
| `confidence` ustalany heurystycznie | Brak podstawy lingwistycznej | `nlp_confidence` = pewność semantyczna |
| Brak detekcji „obowiązku vs dowodu" | Spec i raport traktowane jednakowo | `TenseModeAnalysis` → `validation_mode` |
| `template_violations` tylko schema | Nie sprawdza treści zdań | `GapAnalysis` sprawdza treść i znaczenie |
| Brak wyciągania ról semantycznych | Wiadomo że dokument dotyczy ISO 27001, ale nie wiadomo CO mówi | SRL wyciąga: kto, co robi, czym, na co |

---

## Punkt wejścia — `nlp_engine.py`

```python
# scripts/nlp/nlp_engine.py
def run_nlp_audit(
    doc_path: str,
    mode: str = "PRE_PRODUCTION",
    db_path: Optional[str] = None,
    conn: Optional[sqlite3.Connection] = None,
) -> list[dict]:
    """
    Główna funkcja: tekst → StateMatrix → findings → zapis do SQLite.
    Zwraca listę AuditFinding jako dicts.
    """
    # 1. Klasyfikacja kontekstu
    ctx = classify_document(doc_path, mode)

    # 2. Budowa StateMatrix
    text = load_document(doc_path)
    matrix = build_state_matrix(text, ctx)

    # 3. Ewaluacja pluginów
    findings = []
    for plugin in get_active_plugins():
        for sentence in matrix.sentences:
            if plugin.should_activate(sentence):
                findings.extend(plugin.evaluate(sentence, matrix))

    # 4. Cross-reference
    findings = run_cross_reference(findings, matrix)

    # 5. Zapis do SQLite
    if conn or db_path:
        save_findings(findings, conn or sqlite3.connect(db_path))

    return [f.model_dump() for f in findings]
```
