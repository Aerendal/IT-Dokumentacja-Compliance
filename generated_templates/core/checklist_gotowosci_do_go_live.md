---
title: Checklist gotowości do go-live
status: needs_content
aligned: true
aligned_rev: 6
aligned_at: 2026-02-09
aligned_by: codex
---
# Checklist gotowości do go-live


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Sprawdzić, czy produkt/usługa jest gotowa do uruchomienia produkcyjnego: funkcja, bezpieczeństwo, wydajność, operacje, wsparcie, compliance.


## Zakres i granice

- Obejmuje: kompletność funkcjonalną, testy (unit/integration/e2e/perf/security/UAT), bezpieczeństwo (sekrety/TLS/access review), observability (logi/metryki/trace/alerty), operacje (backup/DR/capacity/on-call/runbook), release/change (plan deploy/rollback/komunikacja/CAB), wsparcie (KB/FAQ/support readiness), compliance/privacy/licencje.  
- Poza zakresem: szczegółowy plan wdrożenia na środowisko (osobny dokument runbook deploy).


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia

- Wejścia: backlog i AC, raporty testów, lista zależności, polityki bezpieczeństwa i compliance, SLO/SLA, runbooki, plan komunikacji.  
- Wyjścia: wypełniona checklist go-live, decyzja go/conditional/no-go, lista blokujących i action items, linki w linkage_index.


## Założenia

- [Założenie 1 — co przyjmujemy za prawdziwe bez weryfikacji]
- [Założenie 2 — warunki brzegowe, które muszą być spełnione]

## Otwarte pytania

- [Pytanie 1 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]
- [Pytanie 2 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]

## Powiązania (meta)

- Key Documents: incident_response_playbook, testowanie_wydajnosci_api, testowanie_bezpieczenstwa_api, logging_strategy, audit_logging, backup_and_disaster_recovery, change_management_policy.  
- Key Document Structures: funkcja/testy, bezpieczeństwo, observability, operacje, release/change, wsparcie, compliance.  
- Document Dependencies: CI/CD pipeline, monitoring stack, ticketing/CAB, status page, KB/FAQ repo.



## Zależności dokumentu
- Upstream: systemy źródłowe, dane referencyjne, decyzje architektoniczne nadrzędne.
- Downstream: konsumpcja rezultatów (zespoły, usługi, dokumenty pokrewne).
- Zewnętrzne: dostawcy, standardy branżowe, umowy/regulacje wpływające na zakres.
## Fazy cyklu życia
- Discovery/Analiza: doprecyzowanie problemu, interesariusze, ograniczenia.
- Projektowanie/Planowanie: decyzje, warianty, kryteria akceptacji, plan wdrożenia.
- Implementacja/Testy: realizacja, walidacja, kryteria go/no-go.
- Wdrożenie/Operacje: rollout, monitoring, eskalacje, ciągłe doskonalenie.
## Struktura sekcji (szkielet)
- Cel i zakres
- Definicje i role/RACI
- Standardy/zasady i narzędzia
- Kroki procesu / checklisty
- Kryteria jakości/DoD i wyjątki
- Komunikacja i eskalacje
- Rejestr zmian i utrzymanie
## Szybkie powiązania

- linkage_index.jsonl (release/go_live_checklist)  
- incident_response_playbook, testowanie_wydajnosci_api, testowanie_bezpieczenstwa_api, backup_and_disaster_recovery


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

1. Zbierz dowody i wypełnij sekcje; oznacz N/A tam, gdzie nie dotyczy.  
2. Oceń kryteria go/conditional/no-go; przypisz action items i właścicieli.  
3. Podpisz checklistę, zaktualizuj linkage_index, przygotuj komunikację.


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

- [Termin 1] — [definicja robocza i źródło]
- [Termin 2] — [definicja robocza i źródło]

## Przykłady użycia

- [Przykład 1 — krótki opis sytuacji i zastosowania tego dokumentu]
- [Przykład 2 — krótki opis sytuacji i zastosowania tego dokumentu]

## Ryzyka i ograniczenia

- [Ryzyko 1 — prawdopodobieństwo, wpływ, sposób ograniczenia]
- [Ryzyko 2 — prawdopodobieństwo, wpływ, sposób ograniczenia]

## Decyzje i uzasadnienia

- [Decyzja 1 — uzasadnienie, alternatywy odrzucone, data]
- [Decyzja 2 — uzasadnienie, alternatywy odrzucone, data]

## Powiązania z innymi dokumentami

- [Dokument A] — [typ relacji: wymaga/uzupełnia/zastępuje/jest-częścią] — [uzasadnienie]
- [Dokument B] — [typ relacji] — [uzasadnienie]

## Powiązania z sekcjami innych dokumentów

- [Dokument X → Sekcja Y] — [powód powiązania i kierunek przepływu informacji]
- [Dokument Z → Sekcja W] — [powód powiązania i kierunek przepływu informacji]

## Słownik pojęć w dokumencie

- [Pojęcie 1] — [definicja i źródło normalizacyjne lub wewnętrzne]
- [Pojęcie 2] — [definicja i źródło normalizacyjne lub wewnętrzne]

## Wymagane odwołania do standardów

- [Standard 1, np. ISO 27001 §A.5] — [sekcja lub wymaganie, którego dotyczy to odwołanie]
- [Standard 2] — [sekcja lub wymaganie]

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

- [ ] AC/UAT spełnione; krytyczne bugi=0; dowody testów są.  
- [ ] Observability/alerty i on-call aktywne; plan deploy/rollback gotowy.  
- [ ] Compliance/privacy/OSS licencje potwierdzone; linkage_index uzupełniony.


## Lista kontrolna spójności relacji

- [ ] Czy każda sekcja z relacją ma wskazaną sekcję źródłową?
- [ ] Czy relacje nie tworzą sprzecznych wymagań?
- [ ] Czy wszystkie wymagane standardy mają odwołania?
- [ ] Czy RACI jest kompletne dla kluczowych działań?

## Artefakty powiązane

- Raporty testów, skany SAST/DAST, raport perf, access review, backup/DR test, plan deploy/rollback, release notes, KB/FAQ, ADR/waiver log.


## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji

- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status: oczekuje/zatwierdzone/odrzucone]
- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status]

## Metryki jakości

- Liczba go-live bez rollbacku, % checklist kompletnych, liczba braków dowodów odkrytych w CAB, czas przygotowania release, liczba incydentów po release.

## Kryteria ukończenia

- [ ] Go-live może się odbyć: kompletna checklist, dowody testów, bezpieczeństwo/observability/operacje/spójność compliance zapewnione.


## Struktura sekcji

1) Funkcjonalność i jakość (AC spełnione, krytyczne bugi=0, UAT podpisane)  
2) Testy i dowody (unit/integration/e2e, performance, security SAST/DAST, pen test jeśli wymagany)  
3) Bezpieczeństwo (sekrety/TLS, access review, hardening, privacy/PII, dane testowe ≠ prod)  
4) Observability (logi/metryki/trace, alerty, SLO/SLA, dashboardy, runbooki)  
5) Operacje i ciągłość (capacity, backup/DR, on-call, runbook incident, rehearsal)  
6) Release/Change (plan deploy, feature flags, rollback, komunikacja, CAB/approvals)  
7) Wsparcie i UX (KB/FAQ, support readiness, monitoring UX, kanały eskalacji)  
8) Compliance i licencje (RODO/PCI/ISO, ToS/Privacy, OSS/licencje)  
9) Decyzja go/conditional/no-go i action items  
10) Załączniki (dowody testów, checklisty bezpieczeństwa, plan deploy/rollback, ADR/waiver log)


## Wymagane rozwinięcia

- Minimalny zestaw dowodów: raporty testów, skany SAST/DAST, wyniki perf, access review, backup/DR test, dry-run deploy/rollback.  
- Kryteria go/conditional/no-go oraz właściciele action items.  
- Szablon komunikacji (release note/status page) i lista odbiorców.  
- Lista zależności z potwierdzonym stanem (wersje usług, feature flags).


## Wymagane streszczenia

- Executive: status go-live, kluczowe ryzyka/blokery, plan rollback i on-call.


## Guidance (skrót)

- Nie ma go-live bez dowodów testów i podpisów UAT; bezpieczeństwo i observability muszą być aktywne.  
- Plan rollback tak samo ważny jak deploy; utrzymuj feature flags.  
- Utrzymuj pojedyncze źródło prawdy checklisty; brak dowodu = N/A/No-go.  
- Aktualizuj linkage_index i checklisty po każdej zmianie.


## Checklisty Definition of Ready (DoR)

- [ ] Backlog/AC zamknięte; środowisko prod gotowe; runbook deploy/rollback dostępny.  
- [ ] Raporty testów i skany bezpieczeństwa dostępne; monitoring/alerty skonfigurowane.


## Checklisty Definition of Done (DoD)

- [ ] Checklist wypełniona, kryteria go/no-go ocenione; linkage_index zaktualizowany; status/metadane aktualne.  
- [ ] Action items przypisane; komunikacja release przygotowana; on-call wyznaczony.  
- [ ] Dowody (testy, bezpieczeństwo, backup/DR) dołączone lub podlinkowane.

