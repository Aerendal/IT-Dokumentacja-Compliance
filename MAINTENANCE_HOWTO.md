# MAINTENANCE_HOWTO — IT Dokumentacja

Przewodnik utrzymania biblioteki szablonów IT dla administratora.
Biblioteka jest żywa: prawo się zmienia, nowe standardy wychodzą, nowe dokumenty są potrzebne.
Ten przewodnik opisuje wszystkie narzędzia do codziennego zarządzania.

---

## Spis treści

1. [Dodawanie nowego szablonu](#1-dodawanie-nowego-szablonu)
2. [Aktualizacja treści istniejącego szablonu](#2-aktualizacja-tresci-istniejacego-szablonu)
3. [Dodawanie nowej regulacji lub standardu](#3-dodawanie-nowej-regulacji-lub-standardu)
4. [Aktualizacja po zmianie prawa (propagacja)](#4-aktualizacja-po-zmianie-prawa-propagacja)
5. [Masowa aktualizacja sekcji](#5-masowa-aktualizacja-sekcji)
6. [Analiza wpływu przed zmianą](#6-analiza-wplywu-przed-zmiana)
7. [Audit jakości szablonów](#7-audit-jakosci-szablonow)
8. [Historia zmian](#8-historia-zmian)
9. [Reindeksacja i resolucja linków](#9-reindeksacja-i-resolucja-linkow)
10. [Uruchomienie pipeline](#10-uruchomienie-pipeline)

---

## 1. Dodawanie nowego szablonu

Użyj interaktywnego wizarda:

```bash
cd dokumentacja/
python3 scripts/new_template_wizard.py
```

Wizard zapyta o:
- Tytuł dokumentu (PL)
- Branżę ISIC
- Powiązane dokumenty
- Mające zastosowanie standardy

Wygeneruje plik `.md` w `generated_templates/core/` oraz
doda wpis do tabeli `docs`.

Zasady:
- Tytuł w języku polskim (bez emoji)
- Jeśli dokument dotyczy konkretnej branży (np. healthcare, fintech), dodaj to w tytule lub ścieżce
- Po wygenerowaniu sprawdź guidance w `doc_section_guidance` — dodaj je do sekcji szablonu

---

## 2. Aktualizacja treści istniejącego szablonu

### Ręcznie (jeden szablon)

Edytuj plik bezpośrednio:
```bash
nano generated_templates/core/nazwa_dokumentu.md
```

Zachowaj strukturę `##` nagłówków — nie usuwaj istniejących sekcji.
Po edycji uruchom reindeksację:

```bash
python3 scripts/reindex_sections.py
python3 scripts/pipeline_run.py
```

### Masowo (bulk)

Użyj `bulk_section_patcher.py` — patrz sekcja [5](#5-masowa-aktualizacja-sekcji).

---

## 3. Dodawanie nowej regulacji lub standardu

Gdy wychodzi nowe prawo (np. AI Act, NIS3) lub nowy standard (ISO 27001:2025):

```bash
cd dokumentacja/

# Dodaj nową regulację
python3 scripts/maintenance/regulation_updater.py add-regulation

# Dodaj nowy standard
python3 scripts/maintenance/regulation_updater.py add-standard

# Wyświetl listę wszystkich regulacji i standardów
python3 scripts/maintenance/regulation_updater.py list
```

Wizard zapyta o:
- Kod (np. `AI-ACT-EU`, `ISO/IEC 42001:2023`)
- Nazwę PL i EN
- Opis, branże, URL
- Słowa kluczowe do dopasowania szablonów (np. `ai`, `sztuczna inteligencja`, `machine learning`)

Następnie automatycznie:
- Wstawia do tabeli `standards` lub `compliance_regulations`
- Dopasowuje szablony (keyword matching) i aktualizuje `doc_standard_mapping` / `doc_regulation_mapping`
- Oferuje wstrzyknięcie referencji do sekcji `## Standardy i compliance` w szablonach

---

## 4. Aktualizacja po zmianie prawa (propagacja)

Gdy istniejąca regulacja zmienia treść (np. nowelizacja KSC):

```bash
# Krok 1: Sprawdź co się zmieni
python3 scripts/maintenance/impact_analyzer.py --regulation KSC-PL

# Krok 2: Zaktualizuj dane w DB
python3 scripts/maintenance/regulation_updater.py update-regulation KSC-PL

# Krok 3: Zaktualizuj treść w szablonach
python3 scripts/maintenance/bulk_section_patcher.py \
    --filter-regulation KSC-PL \
    --replace-in-section "## Standardy i compliance" \
    --old-text "- KSC-PL: Ustawa o KSC (stara treść)" \
    --new-text "- KSC-PL: Ustawa o KSC (zaktualizowana 2025)" \
    --reason "Nowelizacja KSC 2025"

# Krok 4: Zweryfikuj zmiany
python3 scripts/maintenance/changelog_tracker.py list --since 2025-01-01 --type bulk_patch
```

---

## 5. Masowa aktualizacja sekcji

Narzędzie: `scripts/maintenance/bulk_section_patcher.py`

### Przykłady użycia

**Dry-run — pokaż co by się zmieniło:**
```bash
python3 scripts/maintenance/bulk_section_patcher.py \
    --filter-standard "ISO/IEC 27001" \
    --add-section "## Przegląd zgodności" \
    --section-content "Wymagania ISO/IEC 27001 klauzula 9.2 — przegląd wewnętrzny." \
    --dry-run
```

**Dodaj sekcję do szablonów z danym standardem:**
```bash
python3 scripts/maintenance/bulk_section_patcher.py \
    --filter-standard "ISO/IEC 27001" \
    --add-section "## Przegląd zgodności" \
    --section-content "Wymagania ISO/IEC 27001 klauzula 9.2 — przegląd wewnętrzny." \
    --reason "Dodano sekcję przeglądu ISO 27001"
```

**Zamień tekst w sekcji:**
```bash
python3 scripts/maintenance/bulk_section_patcher.py \
    --filter-glob "core/security_*.md" \
    --replace-in-section "## Standardy i compliance" \
    --old-text "TODO: uzupełnić standardy" \
    --new-text "Patrz sekcja Mające zastosowanie standardy i normy" \
    --reason "Usunięto TODO w security templates"
```

**Dołącz tekst do sekcji:**
```bash
python3 scripts/maintenance/bulk_section_patcher.py \
    --filter-regulation KSC-PL \
    --append-to-section "## Standardy i compliance" \
    --append-text "- KSC-PL-2025: Ustawa o KSC (nowelizacja 2025) — klauzule dotyczące audytu" \
    --reason "Propagacja nowelizacji KSC 2025"
```

### Filtry

| Filtr | Opis |
|-------|------|
| `--filter-standard CODE` | Tylko szablony powiązane z danym standardem |
| `--filter-regulation CODE` | Tylko szablony powiązane z daną regulacją |
| `--filter-glob PATTERN` | Tylko szablony pasujące do wzorca ścieżki |
| `--filter-title TEXT` | Tylko szablony z tym słowem w tytule |

Filtry można łączyć — np. `--filter-standard ISO/IEC 27001 --filter-glob "core/access_*.md"`.

---

## 6. Analiza wpływu przed zmianą

Przed każdą zmianą standardu lub regulacji sprawdź skalę wpływu:

```bash
# Ile szablonów dotyczy ISO 27001?
python3 scripts/maintenance/impact_analyzer.py --standard "ISO/IEC 27001"

# Ile szablonów dotyczy KSC-PL?
python3 scripts/maintenance/impact_analyzer.py --regulation KSC-PL

# Które szablony mają sekcję "Standardy i compliance"?
python3 scripts/maintenance/impact_analyzer.py --section "Standardy i compliance"

# Co wiadomo o dokumencie "Polityka bezpieczeństwa"?
python3 scripts/maintenance/impact_analyzer.py --doc "Polityka bezpieczeństwa"

# Zapisz wynik do pliku
python3 scripts/maintenance/impact_analyzer.py --standard "NIS2-EU" --save reports/impact_NIS2.json
```

---

## 7. Audit jakości szablonów

```bash
# Pełny audit wszystkich szablonów
python3 scripts/maintenance/template_auditor.py --save reports/audit_latest.json

# Pokaż szablony z niskim score (problemy)
python3 scripts/maintenance/template_auditor.py --min-score 60

# Audit tylko szablonów security
python3 scripts/maintenance/template_auditor.py --glob "core/security_*.md"

# Sprawdź konkretny dokument
python3 scripts/maintenance/template_auditor.py --doc "Polityka bezpieczeństwa"
```

### Interpretacja score

| Score | Ocena | Znaczenie |
|-------|-------|-----------|
| 80-100 | A | Szablon kompletny |
| 60-79 | B | Dobry, drobne braki |
| 40-59 | C | Wymaga uzupełnienia |
| 0-39 | D | Krytyczne braki |

**Hard gate:** znalezienie emoji = score 0 (naruszenie zasad projektu).

### Kryteria oceny

- Obecność wymaganych sekcji (`## Cel dokumentu`, `## Zakres i granice`, `## Wejścia i wyjścia`,
  `## Powiązania`, `## Standardy i compliance`, `## RACI i role`, `## Metadane`)
- Wypełnienie sekcji `## Standardy i compliance` (co najmniej jedna pozycja `-`)
- Wypełnienie `## RACI i role` (tabela lub lista)
- Kompletność guidance w DB (`doc_section_guidance`)
- Brak placeholderów `[rola]`, `TODO:`, `[PLACEHOLDER]`

---

## 8. Historia zmian

```bash
# Lista ostatnich 50 zmian
python3 scripts/maintenance/changelog_tracker.py list

# Zmiany w konkretnym szablonie
python3 scripts/maintenance/changelog_tracker.py list --template "core/security_policy.md"

# Zmiany od danej daty
python3 scripts/maintenance/changelog_tracker.py list --since 2026-01-01

# Statystyki
python3 scripts/maintenance/changelog_tracker.py stats

# Eksport całego changelog
python3 scripts/maintenance/changelog_tracker.py export --save reports/changelog_export.json
```

Changelog rejestruje zmiany wykonane przez:
- `bulk_section_patcher.py`
- `regulation_updater.py` (propagate)
- Inne narzędzia maintenance

---

## 9. Reindeksacja i resolucja linków

Po masowych zmianach w szablonach uruchom:

```bash
cd dokumentacja/

# Krok 1: Zindeksuj nowe/zmienione nagłówki
python3 scripts/reindex_sections.py

# Krok 2: Wyczyść i ponownie rozwiąż content_links
python3 -c "
import sqlite3; conn = sqlite3.connect('reports/it_doc_matrix.db')
conn.execute('DELETE FROM content_links_resolved'); conn.commit(); conn.close()
print('Wyczyszczono content_links_resolved')
"
python3 scripts/resolve_content_links_extended.py
```

**Kiedy to uruchamiać:**
- Po dodaniu nowych `##` nagłówków do szablonów
- Po bulk_section_patcher z `--add-section`
- Po inject_aspirational_sections.py

---

## 10. Uruchomienie pipeline

Pipeline waliduje cały stan projektu i tworzy snapshot:

```bash
cd dokumentacja/
python3 scripts/pipeline_run.py
```

Wynik `PASS` = wszystko OK.
Wynik `FAIL: emoji check failed` = usuń emoji z wymienionych plików.

Pipeline sprawdza:
- Brak emoji (hard gate)
- Spójność DB (tabele, indeksy)
- Snapshot (porównanie z poprzednim stanem)

---

## Typowy workflow zmiany regulacyjnej

```
1. Dowiadujesz się o nowelizacji (np. KSC-PL 2025)
   └─ python3 scripts/maintenance/impact_analyzer.py --regulation KSC-PL

2. Widzisz: 312 szablonów dotkniętych

3. Aktualizujesz dane w DB
   └─ python3 scripts/maintenance/regulation_updater.py update-regulation KSC-PL

4. Propagacja do szablonów (dry-run najpierw)
   └─ python3 scripts/maintenance/bulk_section_patcher.py --filter-regulation KSC-PL \
       --replace-in-section "## Standardy i compliance" \
       --old-text "- KSC-PL: ..." --new-text "- KSC-PL: (zaktualizowano 2025) ..." \
       --dry-run

5. Faktyczny run
   └─ (to samo bez --dry-run)

6. Reindeks + pipeline
   └─ python3 scripts/reindex_sections.py && python3 scripts/pipeline_run.py

7. Audit kontrolny
   └─ python3 scripts/maintenance/template_auditor.py --filter-regulation KSC-PL --min-score 60
```

---

## 11. Health check i analytics

Szybki przegląd stanu biblioteki w jednym poleceniu:

```bash
cd dokumentacja/

# Pełny raport Markdown
python3 -m itdoc.analytics --format markdown > reports/health.md
cat reports/health.md

# Tylko pokrycie per standard (top-down)
python3 -m itdoc.analytics --coverage

# Standardy poniżej 5 szablonów
python3 -m itdoc.analytics --gaps --min-coverage 5
```

Z Pythona:

```python
from itdoc.db import get_connection
from itdoc.query import coverage_stats, find_unmapped

with get_connection() as conn:
    stats = coverage_stats(conn)
    print(f"Pokrycie: {stats['coverage_pct']}%  "
          f"Niezmapowane: {stats['unmapped_docs']}")

    # Pierwsze 10 niezmapowanych
    for doc in find_unmapped(conn, limit=10):
        print(f"  {doc['path']}")
```

**Interpretacja wskaźników:**

| Metryka | Dobry stan | Wymaga uwagi |
|---------|------------|--------------|
| Coverage % | ≥ 65% | < 50% |
| Unmapped docs | < 3 000 | > 4 000 |
| candidate_match % | < 20% | > 40% |

---

## 12. Automatyczne sugestie mapowań (suggest_mappings)

Skrypt `suggest_mappings.py` używa algorytmu TF-IDF żeby dopasować niezmapowane szablony
do właściwych standardów. Sugestie wymagają potwierdzenia — nigdy nie usuwają istniejących danych.

```bash
cd dokumentacja/

# Sprawdź sugestie bez zapisu (bezpieczne)
python3 scripts/maintenance/suggest_mappings.py --analyze --min-confidence 0.30

# Zatwierdź sugestie o pewności ≥ 0.75 (zapisuje jako candidate_match)
python3 scripts/maintenance/suggest_mappings.py --auto-approve --min-confidence 0.75

# Raport Markdown z pełną listą sugestii
python3 scripts/maintenance/suggest_mappings.py --report > reports/mapping_suggestions.md

# Sprawdź sugestie dla konkretnego szablonu
python3 -c "
from itdoc.db import get_connection
from itdoc.query import suggest_for_doc
with get_connection() as conn:
    for s in suggest_for_doc(conn, 'core/moj_szablon.md'):
        print(s['standard_code'], s['confidence'])
"
```

**Progi pewności:**
- `≥ 0.75` — wysokie zaufanie, można auto-zatwierdzić
- `0.30–0.75` — wymaga ręcznej weryfikacji
- `< 0.30` — zbyt niepewne, ignoruj

---

## 13. Uruchamianie testów

```bash
cd dokumentacja/

# Wszystkie testy (235+ testów)
python3 -m pytest tests/ -q

# Tylko szybkie testy jednostkowe (bez żywej DB)
python3 -m pytest tests/ -m unit -q

# Konkretne moduły
python3 -m pytest tests/test_analytics.py -v
python3 -m pytest tests/test_suggest_mappings.py -v
python3 -m pytest tests/test_maintenance_scripts.py -v

# Z coverage raportem
python3 -m pytest tests/ --cov=itdoc --cov-report=term-missing
```

Pre-commit hook uruchamia testy automatycznie przed każdym `git commit`. Instalacja:
```bash
bash scripts/install_hooks.sh
```

---

## Zasady niezmienne projektu

- Język opisów: **polski** (nazwy własne standardów w oryginale)
- Szablony = guidance + szkielet, **zero treści projektowych**
- Filozofia: **optymalizuj przez rozwój, nie ucinanie**
- Hard gate: **zero emoji** w plikach tekstowych
- Wszystkie zmiany masowe przez skrypty — nigdy ręcznie w setkach plików
