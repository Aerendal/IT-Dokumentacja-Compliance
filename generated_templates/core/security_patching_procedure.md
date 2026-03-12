---
title: Security Patching Procedure
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Security Patching Procedure


## Metadane

- Właściciel: Security Officer
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved
- Repo / moduł: [link]


## Cel dokumentu

Zdefiniować procedurę łat bezpieczeństwa: zakres, klasyfikacja, okna serwisowe, testy, rollback, komunikacja i raportowanie.


## Zakres i granice

- Obejmuje: inwentarz i klasyfikację assetów, okna zmian, kanały komunikacji, proces testów/regresji, kryteria go/no‑go, rollback, raportowanie i wskaźniki.
- Poza zakresem: szczegółowa konfiguracja per usługa (osobne dokumenty techniczne).


## Użytkownicy i interesariusze
- **CISO / Security Officer** — odpowiada za strategię bezpieczeństwa i akceptuje dokument
- **Security Engineer** — implementuje mechanizmy ochronne i przeprowadza testy
- **Compliance Officer** — weryfikuje zgodność z regulacjami (ISO 27001, RODO, NIS2)
- **DevOps / Platform Team** — wdraża zmiany infrastrukturalne wynikające z zaleceń

## Wejścia i wyjścia
- Wejścia: definicja triggera/scenariusza, wymagane uprawnienia/narzędzia, dane wejściowe, RACI i kontakty.
- Wyjścia: wykonane kroki z timestamp, dowody/artefakty, status (sukces/niepowodzenie), decyzje i eskalacje.
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
- Upstream: systemy źródłowe, dane referencyjne, decyzje architektoniczne nadrzędne.
- Downstream: konsumpcja rezultatów (zespoły, usługi, dokumenty pokrewne).
- Zewnętrzne: dostawcy, standardy branżowe, umowy/regulacje wpływające na zakres.
## Fazy cyklu życia
- Przygotowanie runbooka: wersja, właściciel, testowane ścieżki.
- Egzekucja: krokowo z dowodami.
- Postmortem: usprawnienia runbooka i monitoringu.
## Struktura sekcji (szkielet)

- Zakres assetów i klasyfikacja krytyczności
- Okna serwisowe i zależności
- Pozyskiwanie i priorytetyzacja patchy (CVE/CSAF)
- Testy, regresja i kryteria go/no‑go
- Rollback i plan awaryjny
- Komunikacja (biznes/IT/klienci) i change management
- Raportowanie, SLA i wyjątki


## Szybkie powiązania
- system-patching-procedure
- database-patching-procedure
- patching-and-update-procedure
- vm-security-hardening
- vm-provisioning-procedure

## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **CIS Controls v8** — Krytyczne Mechanizmy Bezpieczeństwa (CIS)
- **ISO/IEC 27001** — System Zarządzania Bezpieczeństwem Informacji (ISMS)
- **ISO/IEC 27002** — Wytyczne Praktyk Bezpieczeństwa Informacji
- **ISO/IEC 27005** — Zarządzanie Ryzykiem Bezpieczeństwa Informacji
- **NIST CSF** — Framework Cyberbezpieczeństwa NIST

### Polskie normy i regulacje
- **CERT-PL-WYTYCZNE** — Wytyczne CERT Polska (CSIRT NASK) dot. cyberbezpieczeństwa
- **KSC-PL** — Ustawa o Krajowym Systemie Cyberbezpieczeństwa

> Sekcja generowana automatycznie. Zweryfikuj trafność i uzupełnij o dodatkowe normy/regulacje specyficzne dla kontekstu projektu.

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

- Zmapuj assety i okna zmian, priorytetyzuj patche wg CVSS/eksploatacji, zaplanuj testy i komunikację.
- Dodaj quick-links i checklisty DoR/DoD w `reports/checklist_atomic.jsonl`; sekcje N/A uzasadnij.
- Raportuj wykonanie, wyjątki i rollbacki; aktualizuj metryki po każdym cyklu.


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

## Wejścia

- Polityki/standardy/regulacje, SLA i apetyt na ryzyko.
- Architektura, inwentarz assetów i zależności, mapa okien serwisowych.
- Wyniki skanów, bulletiny vendorów, CVE/CSAF, rejestr wyjątków.


## Wyjścia

- Plan patchingu (harmonogram, właściciele, okna).
- Lista paczek/aktualizacji z priorytetami i stanem.
- Raport z testów/regresji i komunikacji.
- Raport zgodności (coverage, SLA, wyjątki).



## Szybkie powiązania (uzupełnij)

- security_hardening_checklist.md
- security_operations_runbook.md
- logging_and_audit_trail.md
- security_incident_response.md
- api_outage_response.md
- security_status_report.md
- devsecops_pipeline.md


## Wymagane rozwinięcia / streszczenia

- Tabela patchy (asset → patch → priorytet → okno → status → właściciel).
- Streszczenie ryzyk/wyjątków i decyzji go/no‑go.


## Wymagane powiązania

- Rejestr wyjątków i ryzyk, polityki change management, monitoring/logging.
- Pipeline CI/CD (jeśli patchowanie przez build) i runbook IR.


## Kryteria DoR

- [ ] Inwentarz assetów i klasyfikacja krytyczności gotowe.
- [ ] Okna serwisowe i kanały komunikacji uzgodnione.
- [ ] Lista patchy/bulletinów zebrana; priorytety wstępne nadane.
- [ ] Środowiska testowe i plan regresji dostępne.


## Kryteria DoD

- [ ] Patche wykonane/testowane lub wyjątki zatwierdzone.
- [ ] Raport z testów/regresji i komunikacji uzupełniony.
- [ ] KPI/SLA zaktualizowane; quick-links/checklisty odhaczone.


## Artefakty do załączenia

- Lista patchy i statusów.
- Logi z testów/regresji i rollout/rollback.
- Komunikaty do interesariuszy.
- Raport SLA/coverage i wyjątki.


## Walidacja / testy

- Sanity na środowisku testowym; rollback drill dla krytycznych systemów.
- Sprawdzenie spójności wersji/konfiguracji po rollout.


## Metryki monitorowane

- Patch compliance (% załatanych assetów) per krytyczność.
- Czas od wydania patcha do wdrożenia; liczba rollbacków.
- Liczba wyjątków i ich wiek; MTTR dla luk wykrytych w scanach.


## Utrzymanie i aktualizacje

- Cykl patchowania zgodny z polityką (np. tyg./msc); aktualizuj okna i listy assetów.
- Rewiduj priorytety wg exploitów w dziczy; aktualizuj procedury komunikacji.


## Zakończenie

Po spełnieniu DoD podlinkuj artefakty, zaktualizuj checklisty w `reports/checklist_atomic.jsonl`, zamknij wyjątki lub zaplanuj ich przegląd.
