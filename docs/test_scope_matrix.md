# Test Scope Matrix — IT Dokumentacja (`itdoc/`)

> Wygenerowana zgodnie z **TESTING_METHODOLOGY.md** (dockflow_it v10+).  
> Aktualizuj przy każdym PR z ≥3 zmienionymi plikami lub nowym defekcie.

---

## Parametry bazowe

Wagi RT: wC=0.20, wR=0.15, wK=0.15, wP=0.20, wD=0.10, wS=0.10, wF=0.10

---

## Macierz (stan: 2026-03-09)

| Moduł | C | R | K | P | D | S | F | **RT** | Klasa | UT_min | IT_min | CT_min | Coverage |
|-------|---|---|---|---|---|---|---|--------|-------|--------|--------|--------|----------|
| `anchor.py` | 1 | 1 | 0 | 2 | 0 | 0 | 0 | **0.75** | [niskie] niskie | 4 | 1 | 1 | ≥64% + FUZZ=1 |
| `db.py` | 2 | 2 | 2 | 4 | 2 | 1 | 0 | **2.10** | [srednie] średnie | 20 | 6 | 6 | ≥58% |
| `template.py` | 3 | 1 | 1 | 3 | 1 | 0 | 0 | **1.60** | [srednie] średnie | 30 | 2 | 1 | ≥70% + FUZZ=1 |
| `query.py` | 3 | 2 | 3 | 3 | 1 | 1 | 0 | **2.15** | [srednie] średnie | 48 | 6 | 10 | ≥59% |
| `cli.py` | 2 | 3 | 3 | 2 | 0 | 0 | 0 | **1.70** | [srednie] średnie | 20 | 6 | 4 | ≥47% |

---

## Aktualny stan pokrycia (testy)

| Plik testowy | Testy | Pokrywa |
|---|---|---|
| `test_anchor.py` | 23 | `anchor.py` unit (UT_min=4 OK) |
| `test_db_module.py` | 20 | `db.py` unit (UT_min=20 OK) |
| `test_template_parser.py` | 30 | `template.py` unit + fuzz (UT_min=30 OK) |
| `test_query.py` | 31 | `query.py` unit + integration |
| `test_query_extended.py` | 36 | `query.py` BFS + edge cases + contracts (UT_min=48 OK) |
| `test_cli.py` | 22 | `cli.py` unit + integration (UT_min=20 OK) |
| `test_db_integrity.py` | 22 | DB state (IT integracyjne) |
| `test_template_quality.py` | 19 | Template quality (IT integracyjne) |
| `test_maintenance.py` | 7 | Maintenance scripts dry-run |
| `test_resource_leaks.py` | 12 | Wycieki FD/file handles |
| `test_pipeline_integration.py` | 2 | Pipeline PASS (slow) |
| `test_graph_engine_sqlite.py` | 4 | Graph engine (istniejące) |
| **ŁĄCZNIE** | **228** | |

---

## Wymagane testy niefunkcjonalne

| Typ | Warunek | Status |
|-----|---------|--------|
| SAST (bandit) | Zawsze w CI | UWAGA Do dodania w `.github/workflows/` |
| Secrets scan | Zawsze w CI | UWAGA Do dodania |
| DAST | RT ≥ 3 (query.py) | [N/A] N/A — brak HTTP endpoint |
| Fuzz | parser_surface=True | OK Pokryte w `test_template_parser.py` |
| Performance | S ≥ 3 | [N/A] N/A — S=0/1 dla wszystkich modułów |
| Chaos/Resilience | RT ≥ 4 lub stateful=True | [N/A] N/A — RT_max=2.15, stateful=False |

---

## Quality Gates (fail build gdy)

```
coverage(itdoc/) < 70%          ← bramka coverage (najwyższy cel z matrycy)
UT_actual < UT_min               ← dla każdego modułu
new FAIL in pytest               ← zero regresji
```

---

## Wykryte miejsca rozszerzeń (pro-funkcjonalne mitygacje)

| Miejsce | Typ | Co można dodać |
|---------|-----|----------------|
| `find_by_standard()` | Extension Point | parametr `limit=`, `sort_by=` |
| `validate_schema()` | Extension Point | callback `on_error` dla custom checkerów |
| `get_required_sections()` | Extension Point | konfigurowalny zestaw sekcji (nie hardcoded) |
| `rhythm_upstream/downstream()` | Extension Point | filtr po `edge_type`, cache'owanie wyników |
| `validate_template()` | Extension Point | plugin validators: `validators=[check_raci, check_standards]` |
| `cli.py` commands | Extension Point | nowe komendy przez `sub.add_parser()` |
| DB connection | Leak Point | brak context manager (`with get_connection() as conn`) |
| `load_template` | OK | nie przecieka FD (potwierdzone testami) |

---

## Polityka aktualizacji RT

| Zdarzenie | Akcja |
|-----------|-------|
| PR z ≥3 plikami w `itdoc/` | Przelicz RT dla dotkniętych modułów |
| Nowy defekt (F) | Podnieś F o 1, zaktualizuj UT_min |
| Nowy moduł w `itdoc/` | Dodaj wiersz do macierzy |
| Co sprint Hardening | Pełny przegląd macierzy |
