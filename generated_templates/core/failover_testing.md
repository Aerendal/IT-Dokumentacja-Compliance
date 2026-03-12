---
title: Failover Testing
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Failover Testing


## Metadane

- Właściciel: QA Lead
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved

> Powiązania: linkage_index.jsonl


## Cel dokumentu

Zaplanować i opisać testy failover (infrastruktura/aplikacja/dane), aby potwierdzić zdolność systemu do przełączenia na zapasowe zasoby bez naruszenia SLO/DR i zgodności.


## Zakres i granice

- Obejmuje: scenariusze awarii (AZ/region/serwer/baza/kolejka), tryby przełączeń (active-active/active-passive), RTO/RPO, dane i replikacja, runbooki, automatyka/manual, walidacja integralności i konsystencji, pomiar SLO, raportowanie.
- Poza zakresem: projekt architektury HA/DR (opisany w innych dokumentach), ciągłość biznesowa poza IT (w BCP).


## Użytkownicy i interesariusze
- QA, PM/Release, Dev, Security/Perf, Product/Business.
## Wejścia i wyjścia

- Wejścia: architektura HA/DR, RTO/RPO, inwentaryzacja zależności, dane testowe, harmonogram okien serwisowych, polityki change/komunikacji.
- Wyjścia: plan i protokoły testów, wyniki (czas przełączenia, utrata danych, błędy), lista defektów i działań naprawczych, aktualizacje runbooków, decyzje go/conditional/no-go.


## Założenia
- Dostępne są środowiska, dane i narzędzia testowe; zespoły mają czas na runy.
## Otwarte pytania
- Jakie dodatkowe testy wymagane przez regulatorów/klientów?  
- Czy potrzebne testy prod-shadow / canary?
## Powiązania (meta)

- Wymaga odniesienia do: Key Documents
- Wymaga odniesienia do: Key Document Structures
- Wymaga odniesienia do: Document Dependencies
- Wymaga odniesienia do: RACI i role
- Wymaga odniesienia do: Standardy i compliance


## Zależności dokumentu

Wskaż: architekturę HA/DR, CMDB/dependencies, backup/replika, monitoring/alerty, change management, komunikację; brak – odnotuj.


## Fazy cyklu życia

- Planowanie: wybór scenariuszy, okien, danych, ról.
- Przygotowanie: środowiska, dane, narzędzia, monitoring.
- Wykonanie: testy failover, pomiary, logi.
- Walidacja: integralność danych, SLO, funkcjonalność.
- Raportowanie: wyniki, CAPA, aktualizacje runbooków.
- Retrospektywa: lekcje i plan kolejnych testów.



## Struktura sekcji (szkielet)

- RTO/RPO i SLO testu.
- Scenariusze awarii i macierz priorytetów.
- Środowisko i dane testowe.
- Kroki testowe (per scenariusz), narzędzia/komendy.
- Metryki i weryfikacja (czas przełączenia, utrata danych, błędy aplikacji).
- Walidacja integralności i konsystencji danych.
- Komunikacja i eskalacja (przed/w trakcie/po).
- Wyniki, defekty, CAPA.


## Szybkie powiązania

- Meta: Key Documents
- Meta: Key Document Structures
- Meta: Document Dependencies


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **IEEE 829** — Dokumentacja Testowania Oprogramowania i Systemów
- **ISO 22301** — System Zarządzania Ciągłością Działania (BCMS)
- **ISO 9001** — System Zarządzania Jakością (QMS)
- **ISO/IEC 25010** — Model Jakości Systemu i Oprogramowania (SQuaRE)
- **ISO/IEC 27001** — System Zarządzania Bezpieczeństwem Informacji (ISMS)
- **ITIL 4** — Biblioteka Infrastruktury IT (Zarządzanie Usługami)

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

- Zdefiniuj scenariusze i dane; wykonaj testy wg kroków; zmierz metryki; waliduj dane; zapisz wyniki i CAPA; aktualizuj runbooki.


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
- Go/Conditional/No‑go, Defect leakage, Flakiness, Entry/Exit criteria.
## Przykłady użycia
- Release: smoke → regression → perf → security smoke → UAT; decyzja go/conditional/no‑go na podstawie kryteriów.  
- Hotfix: skrócony plan (smoke + targeted regression) z klarownym go/conditional/no‑go.
## Ryzyka i ograniczenia
- Brak gotowości środowisk/danych → poślizgi; niejasne kryteria go/conditional/no‑go → spory; flakiness maskuje defekty.
## Decyzje i uzasadnienia

- [Decyzja 1]
- [Decyzja 2]


## Powiązania z innymi dokumentami
- QA Strategy, Test Data Preparation, Release Plan, Risk Mgmt Plan, Change Mgmt, Security/Perf Testing Plans.
## Powiązania z sekcjami innych dokumentów
- Test Data → dane/środowiska; Release Plan → harmonogram/go-no-go; Risk → priorytety.
## Słownik pojęć w dokumencie
- Go/Conditional/No‑go, Defect leakage, Flakiness, Entry/Exit criteria, Regression, Smoke.
## Wymagane odwołania do standardów
- Polityki QA, bezpieczeństwa i wydajności; wymagania klienta/regulatora jeśli dotyczy.
## Mapa relacji sekcja→sekcja
- Zakres/Ryzyka → Typy testów → Harmonogram → Runy → Raporty → Decyzje → Retro.
## Mapa relacji dokument→dokument
- Testing Plan → QA/Release/Risk → Change/Incident → Lessons Learned.
## Ścieżki informacji
- Wymagania/ryzyka → Plan → Runy → Raporty → Decyzje → Retro → Aktualizacja planu.
## Weryfikacja spójności

- [ ] Ścieżki informacji zamknięte
- [ ] Brak sprzecznych relacji
- [ ] Sekcje krytyczne mają źródła


## Lista kontrolna spójności relacji

- [ ] Relacje mają sekcje źródłowe
- [ ] Relacje nie są sprzeczne
- [ ] Cross-doc uzasadnione
- [ ] Rozwinięcia/streszczenia odnotowane


## Artefakty powiązane
- Harmonogram runów, raporty runów, metryki, defekt log, decyzje go/conditional/no‑go, retrospektywa.
## Ścieżka decyzji

- [Decyzja] → [Uzasadnienie] → [Konsekwencje]
- [Decyzja] → [Uzasadnienie] → [Konsekwencje]


## Ścieżka akceptacji
- QA/PM → Security/Perf (jeśli dotyczy) → Product/Business → Release/CAB.
## Metryki jakości
- Pass rate, Defect leakage, Flake rate, Czas cyklu testów, MTTR defektów w cyklu, dotrzymanie harmonogramu.
## Kryteria ukończenia
- [ ] Plan wykonany; decyzje i raporty zapisane; retrospektywa z lekcjami.  
- [ ] Dokument w linkage_index/checklistach; wersja/data/właściciel aktualne.
## Powiązania sekcja↔sekcja

Scenariusze → kroki testu → metryki → decyzje; dane/replika → walidacja integralności; komunikacja → harmonogram.


## Wymagane rozwinięcia

- Kroki/komendy → runbooki usług.
- Dane → zestawy walidacyjne i checksumy.


## Wymagane streszczenia

- Tabela scenariusz → wynik → RTO/RPO → status go/conditional/no-go.


## Guidance

Cel: dowód, że failover spełnia RTO/RPO i SLO. DoR: architektura, RTO/RPO, scenariusze, dane i okna gotowe. DoD: testy wykonane, wyniki/walidacja zapisane, CAPA nadane, sekcje N/A uzasadnione, metadane aktualne.


## Checklisty jakości (DoR/DoD skrót)

- DoR: [ ] RTO/RPO/SLO znane; [ ] Scenariusze i środowiska przygotowane; [ ] Dane testowe i monitoring gotowe.
- DoD: [ ] Testy przeprowadzone; [ ] Walidacja danych/SLO; [ ] Wyniki/CAPA udokumentowane; [ ] Sekcje N/A uzasadnione; metadane aktualne.

