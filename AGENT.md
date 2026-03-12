# AGENT.md — IT Dokumentacja (Status i Ustalenia)

## Kontekst
- Praca nad standaryzacją paczek dokumentacji IT i ujednoliceniem struktur.
- Źródła: pliki `.md` (Część 1–9), bazy `.db`, pliki `.csv`, rozpakowane zipy `unpacked/files(13..22)/`.
- Nie usuwamy „nadmiarowych” tytułów — traktujemy je jako satelitarne.

## Ustalenia kluczowe
- Lista referencyjna tytułów (`documents_expected`): 6 054 (część 1–9 + brakujące 153).
- Pełna baza tytułów (`documents_final`): 11 810 wierszy, 7 934 unikalnych tytułów (core + satellite + import z baz w `unpacked/`).
- Wszystkie tytuły pozostają (core + satellite); **brak braków** – `missing_template` wyzerowane (wszystkie szablony wygenerowane w PL).
- Powiązania sekcja↔sekcja / dokument↔dokument / podsekcja↔podsekcja są trzymane w DB.
- Treści właściwe (mięso) będą uzupełniane ręcznie; skryptowo tworzymy tylko szkielet i „tory przepływu informacji”.
- Filozofia pracy: **optymalizuj przez rozwój, nie ucinanie** — preferujemy pełny zakres i rozbudowę zamiast redukcji.

- Docelowa baza: `reports/it_doc_matrix.db` (WAL włączony; kopie: `/tmp/it_doc_matrix_clean.db`, `reports/it_doc_matrix_frozen.db`).
- Szablony: `generated_templates/`
  - `generated_templates/core/` — 7 203 szablony `.md`
  - `generated_templates/satellite/` — 741 szablonów `.md`
  - `generated_templates/linkage_index.jsonl`, `generated_templates/guidance_index.jsonl` — indeksy pomocnicze
  - Łącznie szablony `.md`: 7 944; brakujące: 0.
- Raporty: `reports/*.json`, checklisty: `reports/quality_checklist.jsonl`, braki z części 1–9: `reports/missing_from_parts.md`, braki z baz pobocznych: `reports/missing_from_other_dbs.json`, bieżący status: `reports/template_status_latest.json`.
- Lokalizacje źródeł: kopia paczek w `sources_raw/` (rsync z `unpacked/`), oryginalne `unpacked/` można usunąć po backupie.

## Najważniejsze tabele w DB
- `documents_expected` — lista referencyjna (5,901 tytułów)
- `documents_final` — pełna lista tytułów (core + satellite)
- `content_links` — powiązania sekcja/dokument/podsekcja
- `link_types` — słownik typów powiązań
- `doc_section_links` — relacje dokument → faza / meta‑sekcje
- `doc_doc_links` — zależności dokument ↔ dokument (z DB)

## Wygenerowane szkielety
- `generated_templates/core/*.md`
- `generated_templates/satellite/*.md`

Każdy szablon zawiera:
- Cel dokumentu
- Zakres i granice
- Wejścia/wyjścia
- Powiązania meta
- Zależności
- Fazy cyklu życia
- Struktura sekcji (szkielet)
- Wymagane rozwinięcia / streszczenia

## Ustalenia robocze
- Zależności doc↔doc pobierane z tabel dependency/relation/link w DB, gdy dostępne.
- Definicje i opisy sekcji są wstępnie minimalne — mają tylko wyjaśniać przepływ i zależności.
- W razie braków w danych lokalnych, dopuszcza się neutralne definicje pomocnicze.

## Status
- Rozpakowane wszystkie zipy.
- Zbudowana wspólna baza `it_doc_matrix.db` (schemat + staging + final). Statystyki: `documents_final` 11 810 wiersze (7 934 unikat), `content_links` 484 289 wierszy, `from_ref` unikat 209 946, `to_ref` unikat 196 504.
- Wygenerowane szkielety szablonów (PL) — brak braków.
- Powiązania i `link_types` zasiane.
- ISIC: pełne pokrycie 11 810 rekordów (assigned_total), **unassigned = 0**. PropTech/real‑estate pakiet (ID 2697–2790) wymuszony na ISIC 68. Reszta braków domyślnie przypisana do ISIC 62 (software/IT), zgodnie z zasadą „optymalizuj przez rozwój, nie ucinanie”.
- ISIC refinements v3: dodatkowe reguły słów kluczowych przeniosły 604 dokumenty z domyślnego 62 do sektorów m.in. finansowych (64/65), zdrowia (86), edukacji (85), administracji (84), transportu (49/50/51/52), retail (47), hospitality (55), energy (35), telco (61), media (59/60), adtech (73), travel (79). Kod 62 pozostaje dla 5 485 dokumentów czysto IT/ogólnych.
- ISIC refinements v4: granularne słowa kluczowe (fintech/AML/telemed/edtech/retail/e‑commerce/media/telco/transport/energy/public) przeniosły dodatkowe ~1,5k dokumentów z kodu 62. Nowy rozkład (wybrane): 35=206, 47=211, 51=56 (drony przypięte do 51), 52=802 (floty → 52), 59=190, 61=147, 64=112 (billing → 64), 84=210 (privacy → 84), 85=537, 86=331, 62=4 849 (tylko IT/ogólne). Dodatkowo: “agri” tytuły -> 01. Unassigned = 0. Raport: reports/isic_assignment_report.json.

## Następne kroki (ogólnie)
- Uzupełnianie powiązań sekcja↔sekcja na poziomie konkretnych dokumentów.
- Dodanie reguł streszczeń/rozwinięć per dokument.
- Ręczne doprecyzowanie treści przez użytkowników.


## Ostatnie rozszerzenia (automatyczne)
- content_links: relacje sekcja↔sekcja (core + satellite), relacje fazowe, cross‑phase, doc↔doc
- doc_section_guidance: guidance 2–3 zdania dla sekcji bazowych, meta‑sekcji, faz i cross‑relacji
- link_type_guidance: opis typów relacji
- Szablony: wstrzyknięto sekcję Guidance do 6,491 plików

- Checklisty: `reports/checklist_atomic.jsonl` posiadają teraz pola DoR/DoD (atomowe kryteria gotowości i ukończenia) dla każdego z 7 934 tytułów; statusy domyślnie `pending`.

- Szablony core/satellite wzbogacone o sekcję "Jak używać dokumentu" (3 kroki: przeczytaj cel/zakres, wypełniaj wg guidance + DoR/DoD, aktualizuj statusy checklist).

- Guidance light (skrót) dostępny w reports/guidance_light.md (PL).

- W 6 504 szablonach dodano sekcję "Szybkie powiązania" (z linkage_index.jsonl, z dekodowaniem tytułów z mojibake).

- Raport braków "Szybkie powiązania": reports/templates_missing_quick_links.txt (1440 plików bez sekcji quick-links).

- Wszystkie szablony mają sekcję "Szybkie powiązania" (dla 1440 braków dodano fallback z instrukcją ręcznego uzupełnienia).

- Guidance w szablonach zastąpione wersją light (skrót z reports/guidance_light.md) w 6 638 plikach.

- Sekcja "Metadane" (właściciel, wersja, data, status) dodana do wszystkich 7 944 szablonów.

- Raport porównania DB vs szablony: reports/templates_db_diff.json (DB 7 934 tytuły, szablony 7 926; brakujących: w DB 36, tylko w szablonach 28).

- Dodano 15 brakujących szablonów (z listy only_in_db); nowy diff: DB 7 934, szablony 7 941; only_in_db 21, only_in_templates 28 (raport: reports/templates_db_diff.json).

- Próba dodania pozostałych 21 szablonów: brak nowych (te 21 tytułów nadal only_in_db wg najnowszego diff).

- Uzgodnienie tytułów DB↔szablony: nowy diff shows only_in_db=0; only_in_templates=7 (sat). Raport: reports/templates_db_diff.json; szczegóły normalizacji: reports/templates_db_diff_norm2.json.

- Dodano 7 tytułów satelitarnych do DB; diff DB↔szablony = only_in_db 0 / only_in_templates 0 (reports/templates_db_diff.json).

- DB i szablony zrównane (7941); only_in_db=0/only_in_templates=0. Checklisty rozszerzone o 7 nowych tytułów (total 7941). Raporty: templates_db_diff.json, checklist_progress.json.

- Szablony DRP i BCP doprecyzowane (zakres, struktura, powiązania, wejścia/wyjścia); status w template_status_latest.json zaktualizowany.

- Doprecyzowane: Business Continuity Plan (BCP) wariant szablonowy, Disaster Recovery Testing, Business Continuity Requirements (zakres, wejścia/wyjścia, struktura, powiązania, rozwinięcia/streszczenia).

- Doprecyzowano Backup and Disaster Recovery (cel/zakres, wejścia/wyjścia, powiązania, struktura, rozwinięcia/streszczenia); status zaktualizowany.

- Doprecyzowano Backup and Recovery Testing (cel/zakres, wejścia/wyjścia, struktura, powiązania, rozwinięcia/streszczenia); status zaktualizowany.

- Doprecyzowano Backup Verification (cel/zakres, wejścia/wyjścia, struktura, zależności) oraz Backup and Recovery Testing; status zaktualizowany w template_status_latest.json.

- Doprecyzowano Backup Verification Checklist (operacyjna checklista RPO/RTO/integralność/dowody); status zaktualizowany.

- Dodano szablony komunikacji kryzysowej: crisis_communication_template.md (klienci/partnerzy/wewnętrzni) oraz crisis_communication_regulator.md (regulatorzy).

- Doprecyzowano Backup and Recovery Design (architektura, RPO/RTO, topologie, testy, ryzyka); status zaktualizowany.

- Doprecyzowano Backup and Recovery Reference (karta referencyjna: RPO/RTO, harmonogramy, lokalizacje, szyfrowanie/klucze, kontakty, audyt).

- Usunięto wszystkie placeholdery z backup_and_recovery_guide/procedure/testing i vm_*; szablony gotowe strukturalnie.

- Usunięto placeholdery w observability_architecture.md (doprecyzowane guidance/relacje/ścieżki info).

- ISIC Rev.4 (2-cyfrowe) wprowadzone: kolumna industry_code_isic + industry_code_isic_tag; automapowanie pokryło 4 401 dokumentów, 7 409 nieprzypisanych. Raport: reports/isic_assignment_report.json.

- ISIC automap v2: TF-IDF + rozszerzony słownik; auto-przypisane +476, pozostaje 6 933 unassigned. Raport: reports/isic_assignment_report.json; kandydaci: reports/isic_candidates.csv.

- Automatyczne przypisanie ISIC na liberalnym progu nadal 0 (kandydaci w reports/isic_candidates_remaining.csv = 6 933); obecne przypisania ISIC: 4 877.

- ISIC mapowanie + rozszerzony słownik branżowy: przypisane 5 401 dokumentów, nieprzypisane 5 933; raport: reports/isic_assignment_report.json; pozostali kandydaci: reports/isic_candidates_remaining.csv.

- Observability: doprecyzowano requirements, setup guide, service mesh observability, MLOps observability (sekcje, metryki, sampling, bezpieczeństwo, rozwinięcia/streszczenia).

- ISIC mapowanie: dodano rozszerzone reguły branżowe (+129); przypisane 5 530 dokumentów, nieprzypisane 5 804 (raport: reports/isic_assignment_report.json).

- Doprecyzowano szablony postmortem: service_incident_postmortem i postmortem_analysis (cel, struktura, powiązania, checklisty).

- Doprecyzowano Incident Response Playbook i Incident Notifications (klasyfikacja, scenariusze, komunikacja, powiązania z DRP/BCP i postmortem, checklisty).

- ISIC: dodano reguły niszowe (aviation, port/maritime, gaming, GIS, stream processing, privacy); przypisane 6 248, nieprzypisane 5 086 (raport: reports/isic_assignment_report.json).
- ISIC finalizacja: PropTech/real‑estate blok przypięty do 68; domyślny fallback na 62 dla pozostałych braków. Raport: reports/isic_assignment_report.json (unassigned=0).

- Doprecyzowano pakiet API security (assessment, best practices, design, testing): cele, zakres, wejścia/wyjścia, struktura, wymagane rozwinięcia/streszczenia.

## Sesja 2026-03-09 — Uzupełnienie biblioteki (standardy, regulacje, linki, guidance)

### Faza 1 — Naprawa mojibake (DONE)
- Naprawiono kodowanie cp1252→utf-8 w kolumnach: `doc_section_guidance.doc_title` (59 520 wierszy),
  `documents_final.title` (1 488), `docs.title` (337), `content_links.from_ref` (49 253),
  `content_links.to_ref` (47 616). Skrypt: `scripts/fix_mojibake_guidance.py`.

### Faza 2 & 3 — Zasilenie standardów i regulacji (DONE)
- Tabela `standards`: 44 normy (ISO/IEC 27001/02/05/17/18/35/701, ISO 9001/20000/22301/12207/15288/25010,
  IEEE 829/830/1016/42010, ITIL 4, TOGAF ADM, PMBOK 7, PRINCE2 7, COBIT 2019, SAFe 6.0, SCRUM Guide,
  DORA, NIS2, SOC 2, CIS Controls v8, OWASP ASVS/MASVS, PCI DSS, HL7 FHIR, GDPR/RODO,
  NIST CSF/SP 800-53, OpenAPI 3.x, AsyncAPI 3.x, ISO 38500/20546/23053/42001/29110/25040).
- Tabela `compliance_regulations`: 21 polskich regulacji (KSC-PL, UODO-PL, PZP-PL, UŚUDE-PL, PT-PL,
  UoR-PL, KSH-IT-PL, KEP-PL, MIFID2-PL, SOLVENCY2-PL, 6 norm PN, CERT-PL-WYTYCZNE, KNF-REKOM-IT,
  UKE-WYTYCZNE, MC-INTEROP-PL, CYBERSEC-STRATEGIA-PL). Skrypt: `scripts/seed_standards.py`.

### Faza 4 — Mapowanie standardów do dokumentów (DONE)
- Tabela `doc_standard_mapping`: 19 116 wierszy (keyword matching na path+title).
- Tabela `doc_regulation_mapping`: 2 026 wierszy.
- Wstrzyknięto sekcję "Mające zastosowanie standardy i normy" do 4 867 plików `.md`.
  Skrypt: `scripts/map_standards_to_docs.py`.

### Faza 4b — Rozwiązanie content_links (DONE, częściowe)
- Naprawiono skrypt `scripts/resolve_content_links_extended.py` (bug: błędny anchor strip, mojibake).
- Tabela `content_links_resolved`: 78 310 wierszy (z 53 poprzednio; 16.2% z 484 289).
- Naprawiono bug "database is locked" w `pipeline_run.py` (brak `conn.commit()` przed
  `diagnostics_report`). Linia ~1162.

### Korekty po sesji — głęboka naprawa (DONE)

#### Krok 1 — Kompleksowa naprawa mojibake (3 rundy)
- Runda 1: `Ã³→ó` pattern (czyste Ã) — naprawiono 7 950 from_ref + 8 480 to_ref.
- Runda 2: partial fix (split ref na `::section::`, napraw tylko część TITLE) — 14 370 + 15 328.
- Runda 3: mapa znakowa (iteracja U+0080–U+05FF, generuj pary mojibake→poprawny) — 3 585 + 3 824.
- Wynik: **0 wierszy z mojibake** w from_ref, to_ref, docs.title (weryfikacja GLOB potwierdza).

#### Krok 2 — Reindeksacja sekcji
- Skrypt: `scripts/reindex_sections.py` — skanuje `.md` pliki pod kątem `##` i `###` nagłówków.
- Schemat: `heading_level` (2/3) + `heading_path` (breadcrumb) uzupełniane przy INSERT (NOT NULL).
- Wynik: `sections` wzrosła z 392 851 → 403 387 (+10 536 nowych wierszy).
- Dwie sekcje aspiracyjne (`standardy-i-compliance`, `raci-i-role`) nadal brakuje jako prawdziwych
  nagłówków `##` — są tylko jako bullet-pointy w `## Powiązania (meta)`. Znana luka, osobna faza.

#### Krok 3 — Ponowne uruchomienie resolvera
- Po wszystkich poprawkach resolver uruchomiony ponownie (usunięto stare resolved, restart).
- Tabela `content_links_resolved`: **92 351 wierszy** (19.1% z 484 289).
- **"Brak dokumentu: 0"** — wszystkie doc_title znalezione (z 41k poprzednio).
- Pozostałe 390 029 "brak sekcji": sekcje naprawdę nieistniejące w szablonach.

### Pipeline po korektach
- Ostatni run: **PASS**, snapshot NOOP (2026-03-09T06-50-03Z__run).

### Faza 5 — Wzbogacenie guidance o standardy (DONE)
- Dodano kolumny `standards_refs` i `regulations_refs` do `doc_section_guidance`.
- Skrypt `scripts/enrich_guidance_standards.py` wypełnił:
  - `standards_refs`:    347 867 / 415 843 wierszy
  - `regulations_refs`:   88 904 / 415 843 wierszy
- Źródło: doc-level z `doc_standard_mapping` + section-level z reguł keyword per `section_title`.

### Faza 6 — Wizard nowych szablonów (DONE)
- Skrypt: `scripts/new_template_wizard.py` — interaktywny CLI, tworzy `.md` + wstawia do DB.
- Dokumentacja: `TEMPLATE_HOWTO.md` — kompletny przewodnik PL (kiedy, jak, zasady, błędy).

### Pipeline po sesji
- Ostatni run: PASS, snapshot CREATED (2026-03-09T06-27-48Z__run).
- Po korektach: PASS, snapshot NOOP (2026-03-09T06-50-03Z__run).

---

## Sesja 2026-03-09 — Faza 8: Aspiracyjne sekcje + Narzędzia utrzymania

### Faza 8A — Aspiracyjne sekcje jako prawdziwe nagłówki (DONE)
- Skrypt: `scripts/inject_aspirational_sections.py`
- Wstrzyknięto `## Standardy i compliance` i `## RACI i role` do **7 017 szablonów**.
- Po reindeksacji `sections`: `standardy-i-compliance` i `raci-i-role` po **7 885** wierszy.
- Po re-run resolvera: `content_links_resolved` = **131 749** (27.2% z 484 289, poprzednio 19.1%).
- Pipeline: **PASS**, snapshot CREATED (2026-03-09T07-11-41Z__run).

### Faza 8B — Narzędzia ciągłego utrzymania (DONE)
Nowe skrypty w `scripts/maintenance/`:

| Skrypt | Opis |
|--------|------|
| `impact_analyzer.py` | Analiza wpływu: `--standard`, `--regulation`, `--section`, `--doc` → lista szablonów |
| `bulk_section_patcher.py` | Masowa aktualizacja sekcji z dry-run, backupem, logiem do changelog |
| `regulation_updater.py` | Wizard: dodaj/aktualizuj regulację lub standard + auto-propagacja do DB + szablonów |
| `template_auditor.py` | Audit jakości szablonu (score 0-100, ocena A-D), bulk raport |
| `changelog_tracker.py` | Historia zmian (`list`, `stats`, `export`); tabela `template_changelog` w DB |

Nowy plik: `MAINTENANCE_HOWTO.md` — pełny przewodnik PL dla administratora biblioteki.

## Kontrola emoji (hard gate)
- Skrypt: `scripts/check_no_emoji.py` — skanuje pliki tekstowe (md/markdown/txt/json/jsonl/yaml/yml/csv/tsv/sql); zwraca kod 1 przy wykryciu emoji.
- Pipeline: `scripts/pipeline_run.py` uruchamia `emoji_check` na starcie; raport w `reports/runs/<run_id>/emoji_report.json`. Pipeline przerywa się (`FAIL: emoji check failed`) jeśli znajdzie emoji.

---

## Sesja 2026-03-09 — Faza 9: Zasilenie pustych tabel metadanych DB

### Faza 9A — Slowniki bazowe (DONE)
- Skrypt: `scripts/seed_base_dicts.py`

| Tabela | Wiersze |
|--------|---------|
| `roles` | 40 |
| `phases` | 23 |
| `industries` | 30 |
| `document_categories` | 15 |
| `relationship_types` | 10 |
| `quality_dimensions` | 8 |

### Faza 9B — Typy dokumentow (DONE)
- Skrypt: `scripts/seed_document_types.py`
- Wstawiono **20** typow dokumentow (POLICY, STANDARD, PROCEDURE, RUNBOOK, PLAYBOOK, CHECKLIST, SPEC, ADR, DESIGN, REPORT, PLAN, GUIDE, MATRIX, REGISTER, CONTRACT, ASSESSMENT, POSTMORTEM, RFC, ONBOARDING, ARCHITECTURE).

### Faza 9C — Mapowania faza + lifecycle (DONE)
- Skrypt: `scripts/derive_document_phase_mapping.py`
- `document_phase_mapping`: **2 323** wierszy (szablony powiazan z fazami cyklu zycia).
- `document_lifecycle`: **2 500** wierszy (probka 500 dok., stany: draft/review/approved/active/archived).

### Faza 9D — RACI per dokument (DONE)
- Skrypt: `scripts/derive_document_raci.py`
- `document_raci`: **7 941** wierszy (1 wpis RACI per dokument, na podstawie slowa kluczowego tytulu).

### Faza 9E — Zaleznosci miedzy dokumentami (DONE)
- Skrypt: `scripts/derive_document_dependencies.py`
- Zrodlo: `content_links WHERE to_type='document'` (1 855 linkow) -> dopasowanie po tytule -> deduplikacja.
- `document_dependencies`: **897** unikalnych relacji dok-dok (dep_type: requires / relates_to).

### Faza 9F — Pipeline (DONE)
- Pipeline: **PASS**, snapshot NOOP (2026-03-09T08-01-39Z__run).

---

## Stan finalny po Fazie 9

| Tabela | Wiersze |
|--------|---------|
| `docs` | 7 941 |
| `sections` | 419 154 |
| `standards` | 44 |
| `compliance_regulations` | 21 |
| `doc_standard_mapping` | 19 013 |
| `doc_regulation_mapping` | 2 026 |
| `content_links_resolved` | 131 749 |
| `roles` | 40 |
| `phases` | 23 |
| `industries` | 30 |
| `document_categories` | 15 |
| `relationship_types` | 10 |
| `quality_dimensions` | 8 |
| `document_types` | 20 |
| `document_phase_mapping` | 2 323 |
| `document_lifecycle` | 2 500 |
| `document_raci` | 7 941 |
| `document_dependencies` | 897 |
| Pipeline | PASS (2026-03-09T08-01-39Z) |

---

## Sesja 2026-03-09 — Faza 10+11: Uzupełnienie małych szablonów

### Analiza przed Fazą 10
Wykryto 914 szablonów <3KB z tylko 6-8 sekcjami (stary format szkieletu).
Duże szablony (6622 plików >15 sekcji) mają ~20-30 sekcji z pełnym guidance.
Brakujące sekcje: Zakres i granice, Użytkownicy i interesariusze, Wejścia i wyjścia,
Założenia, Otwarte pytania, Powiązania (meta), Zależności dokumentu, Fazy cyklu życia,
Mapa relacji sekcja/dokument, Weryfikacja spójności, i inne.

### Faza 10 — Uzupełnienie struktury (DONE)
- Skrypt: `scripts/enrich_small_templates.py`
- Wstrzyknięto brakujące sekcje z generycznym guidance do **1066 plików** (<3.2KB).
- Każdy plik urósł z ~1.6-3KB do ~7-9KB z pełnymi 20+ sekcjami.
- Pipeline: PASS, snapshot CREATED (2026-03-09T08-15-25Z__run).

### Faza 11 — Wypełnienie guidance z podobnych szablonów (DONE)
- Skrypt: `scripts/fill_guidance_from_similar.py`
- Metoda: keyword matching tytułów → klonowanie guidance z najlepiej pasującego dużego szablonu.
- Kluczowe sekcje wypełnione specyficznym guidance (zamiast generycznych placeholderów):
  - `## Cel dokumentu`, `## Zakres i granice`, `## Wejścia i wyjścia`,
    `## Założenia`, `## Otwarte pytania`, `## Powiązania (meta)`,
    `## Zależności dokumentu`, `## Fazy cyklu życia`
- Naprawiono bug: samopasowanie (self-match) wykluczone z indeksu donorów.

### Stan finalny po Fazie 10+11

| Kategoria | Pliki |
|-----------|-------|
| Duże szablony z pełnym, specyficznym guidance | ~6 622 |
| Małe szablony uzupełnione guidance z podobnych dok. | ~988 |
| Małe szablony z guidance domyślnym (brak dobrego wzorca) | ~78 |
| Sekcje end-user (Słownik, Metryki) — prawidłowe placeholdery | wszystkie |
| Generyczne `Dla każdej fazy określ` — wyeliminowane | 0 |

- Pipeline: **PASS**, snapshot CREATED (2026-03-09T08-29-09Z__run).

## Sesja 2026-03-09 — Faza 10+11 Rundy 2-4: Rozszerzenie wzbogacania szablonów

### Runda 2 (próg 9KB) — DONE
- `enrich_small_templates.py` (MAX_SIZE_BYTES=9000) → 1073 nowych plików wzbogaconych strukturalnie.
- `fill_guidance_from_similar.py` → 1484 pliki zaktualizowane guidance z donorów.
- Fix: 103 placeholdery "Dla każdej fazy określ" naprawione.
- Pipeline: **PASS**, snapshot CREATED (2026-03-09T08-36-25Z__run).

### Runda 3 (próg 11KB) — DONE
- `enrich_small_templates.py` (MAX_SIZE_BYTES=11000) → 2061 nowych plików wzbogaconych strukturalnie.
- `fill_guidance_from_similar.py` → 882 pliki zaktualizowane.
- Fazy fix: 0 (wszystkie naprawione w rundzie 2).
- Pipeline: **PASS**, snapshot CREATED (2026-03-09T08-39-44Z__run).

### Runda 4 (niższy próg podobieństwa 0.01) — DONE
- `fill_guidance_from_similar.py` (min_score=0.01) → 320 pliki zaktualizowane.
- Targeted per-section fill → 17 pliki zaktualizowane (section-specific donor matching).
- Fallback fill: 18 plików z Wejścia section standardowym tekstem fallback.
- Pipeline: **PASS**, snapshot CREATED (2026-03-09T08-50-35Z__run).

### Stan końcowy po rundach 2-4
| Metryka | Wartość |
|---------|---------|
| kompletne_z_guidance | **7965** / 7966 |
| brak_guidance | **0** |
| brak_struktury | 1 (security_analyst_onboarding.md — używa oddzielnych ## Wejścia i ## Wyjścia) |
| Pipeline | **PASS** (2026-03-09T08-50-35Z) |
