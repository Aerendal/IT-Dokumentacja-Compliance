---
title: System Patching Procedure
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# System Patching Procedure


## Metadane

- Właściciel: Technical Writer
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved

> Powiązania: linkage_index.jsonl


## Cel dokumentu

Opisać procedurę patchowania systemów (OS/app/middleware), aby redukować ryzyko bezpieczeństwa przy minimalnym wpływie na dostępność.


## Zakres i granice

- Obejmuje: cykle patch (security/feature), źródła patchy, kwalifikację (severity/CVE), okna serwisowe, testy pre/post, backup/rollback, narzędzia (WSUS/Ansible/K8s/RPM), wyjątki/waivery, raportowanie i audyt, SLA.
- Poza zakresem: upgrade sprzętu (osobne), refaktoryzacja aplikacji.


## Użytkownicy i interesariusze
- **Technical Writer / Documentation Owner** — tworzy i utrzymuje dokumentację
- **Subject Matter Expert (SME)** — dostarcza merytoryczne treści i weryfikuje poprawność
- **Development Team** — recenzuje dokumentację techniczną
- **End Users** — korzystają z dokumentacji i zgłaszają nieścisłości

## Wejścia i wyjścia

- Wejścia: polityka patchowania, CVE/advisories, inwentarz i krytyczność, okna serwisowe, narzędzia, testy/regresja, backupy.
- Wyjścia: harmonogram patch, checklisty pre/post, raport z wykonania, lista wyjątków, dowody (logi/skany), metryki (compliance, MTTP).


## Założenia
- Synchronizacja czasu (NTP) w całym środowisku.  
- Możliwość szybkiego odcięcia ruchu (LB/feature flag).  
- Monitoring i logi dostępne w czasie rzeczywistym.
## Otwarte pytania
- Czy wszystkie batch/cron muszą być zatrzymane, czy wystarczy drenaż kolejek?  
- Jakie są limity PSP/partnerów na przerwy w dostępności?  
- Czy potrzebny jest tymczasowy read‑only fallback dla raportów?
## Powiązania (meta)

- Wymaga odniesienia do: Key Documents
- Wymaga odniesienia do: Key Document Structures
- Wymaga odniesienia do: Document Dependencies
- Wymaga odniesienia do: RACI i role
- Wymaga odniesienia do: Standardy i compliance


## Zależności dokumentu

Wskaż: CMDB, polityki patch, narzędzia automatyzacji, testy/regresja, backup/DR, okna serwisowe; brak – odnotuj.


## Fazy cyklu życia

Planowanie → Przygotowanie → Testy → Wykonanie → Walidacja → Raport → Przegląd.



## Struktura sekcji (szkielet)

- Zakres i krytyczność systemów.
- Kwalifikacja patchy i priorytety.
- Harmonogram i okna serwisowe.
- Testy pre/post i walidacja.
- Backup/rollback.
- Narzędzia i automatyzacja.
- Raportowanie i audyt (dane dowodowe, compliance).
- Wyjątki/waivery i przeglądy.
- Ryzyka i mitigacje.


## Szybkie powiązania

- Meta: Key Documents
- Meta: Key Document Structures
- Meta: Document Dependencies


## Mające zastosowanie standardy i normy

### Standardy międzynarodowe
- **ISO/IEC 12207** — Procesy Cyklu Życia Oprogramowania
- **PMBOK 7** — Przewodnik po Zarządzaniu Projektami (PMI)
- **ITIL 4** — Biblioteka Infrastruktury IT (Zarządzanie Usługami)

## Standardy i compliance


Lista standardów i wymagań regulacyjnych mających zastosowanie do tego dokumentu.
Uzupełnij na podstawie sekcji "Mające zastosowanie standardy i normy" oraz tabeli `doc_standard_mapping`.

- Standard / norma: [kod i nazwa]
- Wymaganie regulacyjne: [kod i treść]
- Polityka wewnętrzna: [nazwa polityki]


## RACI i role


Macierz RACI (Responsible / Accountable / Consulted / Informed) dla działań związanych z tym dokumentem.

| Działanie | Responsible | Accountable | Consulted | Informed |
|-----------|-------------|-------------|-----------|----------|
| Tworzenie | [rola]      | [rola]      | [rola]    | [rola]   |
| Przegląd  | [rola]      | [rola]      | [rola]    | [rola]   |
| Aktualizacja | [rola]   | [rola]      | [rola]    | [rola]   |
| Archiwizacja | [rola]   | [rola]      | [rola]    | [rola]   |

## Jak używać dokumentu

- Oceń severity; zaplanuj okno; przygotuj testy i backup; wykonaj patch; zweryfikuj; raportuj i audytuj.


## Checklisty jakości

### Kompletność
- **Kryterium:** Wszystkie wymagane sekcje i pola są wypełnione
- **Metryka:** Odsetek wypełnionych sekcji do wymaganych
- **Próg OK:** 90%
- **Narzędzie:** template_auditor.py, checklist_atomic.jsonl

### Dokładność
- **Kryterium:** Informacje są poprawne merytorycznie i aktualne
- **Metryka:** Przegląd ekspercki; data ostatniej aktualizacji
- **Próg OK:** Przegląd co 3 mies.
- **Narzędzie:** regulation_updater.py

### Spójność
- **Kryterium:** Terminologia i struktura są spójne w całej bibliotece
- **Metryka:** Liczba niespójności terminologicznych i strukturalnych
- **Próg OK:** 0 niespójności
- **Narzędzie:** bulk_section_patcher.py

### Śledzalność
- **Kryterium:** Każda sekcja ma źródło (standard, regulacja, decyzja)
- **Metryka:** Odsetek sekcji z wypełnionymi standards_refs
- **Próg OK:** 80%
- **Narzędzie:** impact_analyzer.py

### Aktualność
- **Kryterium:** Dokument jest aktualny względem obowiązujących regulacji
- **Metryka:** Czas od ostatniej aktualizacji vs. częstotliwość przeglądów
- **Próg OK:** < 6 mies.
- **Narzędzie:** changelog_tracker.py

### Użyteczność
- **Kryterium:** Użytkownik końcowy może efektywnie wypełnić dokument na podstawie guidance
- **Metryka:** Ocena guidance (score z template_auditor); feedback użytkowników
- **Próg OK:** Score >= 70
- **Narzędzie:** template_auditor.py

## Definicje robocze
- Cutover: moment przełączenia ruchu na nowy primary/cluster.  
- Freeze: blokada zmian schematu/deployów na czas okna.  
- Go/No‑Go: formalna decyzja na podstawie checklist i walidacji.
## Przykłady użycia
- Migracja z single‑primary do HA cluster.  
- Przeniesienie na nową wersję bazy lub inny engine (np. MySQL→PostgreSQL) z dual‑write.  
- Cutover regionu w architekturze active‑active (wyłączenie ruchu z jednego regionu).
## Ryzyka i ograniczenia
- Brak spójności danych przy dual‑write bez idempotentnych operacji.  
- Zbyt długie okno read‑only powoduje straty biznesowe.  
- Niedoszacowanie TTL/timeoutów klientów skutkuje falą retry i przeciążeniem.
## Decyzje i uzasadnienia
- Strategia cutover (blue/green vs dual‑write) — zależnie od zgodności schematu i RTO/RPO.  
- Długość okna serwisowego — kompromis między bezpieczeństwem a biznesem.  
- Zakres walidacji — minimalny zestaw blokujący go/no‑go.
## Powiązania z innymi dokumentami
- change_management_request — formalna akceptacja okna.  
- incident_response_runbook — ścieżka eskalacji, gdy cutover się nie powiedzie.  
- performance_baseline_report — porównanie p99/p999 przed vs po.
## Powiązania z sekcjami innych dokumentów

- [Dokument X → Sekcja Y] — [powód powiązania i kierunek przepływu informacji]
- [Dokument Z → Sekcja W] — [powód powiązania i kierunek przepływu informacji]

## Słownik pojęć w dokumencie

- [Pojęcie 1] — [definicja i źródło normalizacyjne lub wewnętrzne]
- [Pojęcie 2] — [definicja i źródło normalizacyjne lub wewnętrzne]

## Wymagane odwołania do standardów
- Wewnętrzne standardy ciągłości działania (RPO/RTO).  
- Standardy bezpieczeństwa kopii zapasowych i szyfrowania.
## Mapa relacji sekcja→sekcja

- [Sekcja A] -> [Sekcja B] : [typ relacji: rozszerza/streszcza/wymaga/wyklucza]
- [Sekcja C] -> [Sekcja D] : [typ relacji]

## Mapa relacji dokument→dokument

- [Dokument A] -> [Dokument B] : [typ relacji]
- [Dokument C] -> [Dokument D] : [typ relacji]

## Ścieżki informacji

- [Wejście] -> [Sekcja źródłowa] -> [Sekcja rozwinięcia] -> [Wyjście]
- [Wejście] -> [Sekcja źródłowa] -> [Sekcja streszczenia] -> [Wyjście]

## Weryfikacja spójności

- [ ] Czy wszystkie ścieżki informacji są zamknięte (każde wejście ma wyjście)?
- [ ] Czy istnieją pętle lub sprzeczne relacje między sekcjami?
- [ ] Czy sekcje kluczowe mają wskazane źródła i odbiorców?
- [ ] Czy terminologia jest spójna z sekcją "Słownik pojęć"?

## Lista kontrolna spójności relacji

- [ ] Czy każda sekcja z relacją ma wskazaną sekcję źródłową?
- [ ] Czy relacje nie tworzą sprzecznych wymagań?
- [ ] Czy wszystkie wymagane standardy mają odwołania?
- [ ] Czy RACI jest kompletne dla kluczowych działań?

## Artefakty powiązane

- [Artefakt 1, np. diagram architektury] — [opis i relacja do tego dokumentu]
- [Artefakt 2, np. schemat bazy danych] — [opis i relacja do tego dokumentu]

## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji

- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status: oczekuje/zatwierdzone/odrzucone]
- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status]

## Metryki jakości

- [Metryka 1, np. pokrycie testami] — [cel / próg minimalny]
- [Metryka 2, np. czas przeglądu] — [cel / próg minimalny]

## Kryteria ukończenia

- [ ] Kryterium 1 — [opis stanu ukończenia tej sekcji lub dokumentu]
- [ ] Kryterium 2 — [opis stanu ukończenia tej sekcji lub dokumentu]

## Powiązania sekcja↔sekcja

Severity → harmonogram; testy → go/no-go; backup → rollback; wyjątki → audyt.


## Wymagane rozwinięcia

- Matryca severity→SLA; checklisty test/rollback.


## Wymagane streszczenia

- Tabela system → patch → termin → status → dowód.


## Guidance

Cel: bezpieczne i przewidywalne patchowanie. DoR: polityka, CVE, CMDB, okna, narzędzia. DoD: harmonogram/testy/backup/raport/wyjątki; sekcje N/A uzasadnione; metadane aktualne.


## Checklisty jakości (DoR/DoD skrót)

- DoR: [ ] Polityka patch; [ ] CMDB/krytyczność; [ ] CVE/severity; [ ] Okna/narzędzia/testy/backup.
- DoD: [ ] Harmonogram/testy/backup/raport/wyjątki; [ ] Sekcje N/A uzasadnione; metadane aktualne.
