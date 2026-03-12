---
title: Functional Safety Analysis
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Functional Safety Analysis


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Opisuje analizę bezpieczeństwa funkcjonalnego systemu (np. automotive/industrial/robotyka) zgodnie z normami (np. ISO 26262, IEC 61508). Ma identyfikować zagrożenia, ocenić ryzyko, określić cele bezpieczeństwa i środki redukcji, zapewniając ślad audytowy.


## Zakres i granice

- Obejmuje: kontekst systemu, definicję elementów, HARA/HAZOP/FMEA, ASIL/SIL oceny, cele bezpieczeństwa, wymagania bezpieczeństwa, środki kontrolne (architektura, diagnosable faults, redundancja), analizy kwantytatywne (SPFM/LFM, probabilistic metrics), traceability do wymagań/testów, plany weryfikacji/validacji, zarządzanie zmianą, dokumentację audytową.
- Poza zakresem: pełna architektura produktu (link), testy szczegółowe (w planach V&V).


## Użytkownicy i interesariusze

- Safety, Engineering, QA/V&V, Compliance/Audit, Product/Project.


## Wejścia i wyjścia

- Wejścia: opis systemu i funkcji, diagramy/bloki, interfejsy, use case’y, scenariusze zagrożeń, dane środowiskowe, normy (ISO 26262/IEC 61508), wcześniejsze analizy, historyczne incydenty, profile misji, założenia bezpieczeństwa.
- Wyjścia: lista zagrożeń i scenariuszy, oceny ryzyka/ASIL/SIL, cele bezpieczeństwa, wymagania techniczne i architektoniczne, środki redukcji, plany V&V i dowody, mapa traceability, rejestr zmian i założeń.


## Założenia

- Dostępne normy i wykwalifikowany personel; dane środowiskowe i misji są znane.


## Otwarte pytania

- Czy wymagane są dodatkowe normy sektorowe (rail/medical/avionics)?
- Jakie są wymagania niezależności i audit trail dla tego projektu?


## Powiązania (meta)

- Key Documents: iso_26262_compliance, safety_concept, hazard_log, fmea_register, validation_plan, change_management, configuration_management.
- Key Document Structures: kontekst, analiza zagrożeń, cele, wymagania, środki, V&V, traceability.
- Document Dependencies: hazard log, architektura, normy, narzędzia safety (HARA/FMEA/FMEDA), repo traceability, testy/V&V.


## Zależności dokumentu

Wymaga pełnego opisu systemu, interfejsów, funkcji, hazard log, norm referencyjnych, danych środowiskowych, narzędzi HARA/FMEA/FMEDA i repozytorium traceability. Brak = DoR otwarte.


## Fazy cyklu życia

- Definicja systemu i kontekstu.
- Identyfikacja zagrożeń i ocena ryzyka (HARA/HAZOP/FMEA).
- Cele bezpieczeństwa i wymagania pochodne.
- Projekt środków kontrolnych (architektura, diagnostyka, redundancja).
- Weryfikacja/Validacja i ocena metryk (SPFM/LFM/PMHF).
- Utrzymanie i zmiany (impact analysis, re‑assessment).



## Struktura sekcji (szkielet)
1. Item definition i zakres: granice systemu, funkcje, interfejsy, warunki pracy; docelowe ASIL/e.
2. HARA: zagrożenia, S/E/C, klasyfikacja ASIL, scenariusze operacyjne.
3. Safety Goals i FSR: cele bezpieczeństwa z ASIL, funkcjonalne wymagania bezpieczeństwa.
4. Technical Safety Concept (TSC): architektura, mechanizmy bezpieczeństwa, redundancje, monitorowanie, interfejsy.
5. HW/SW Safety Requirements (HSR/SSR): timing, diagnostyka, freedom from interference, partitioning, watchdogi.
6. Analizy bezpieczeństwa: FMEA/FMEDA/FTA, DFA, SPFM/LFM/PMHF, dependent failures.
7. Walidacja i weryfikacja: strategia testów per ASIL, pokrycie, fault injection, traceability (req→test→wynik).
8. Zarządzanie konfiguracją/zmianą: baseline artefaktów bezpieczeństwa, kwalifikacja narzędzi, change control.
9. Produkcja i operacje: release for production, wytwarzanie/serwis, OTA/field updates, recall/incident handling.
10. Safety case i audyty: lista work products ISO 26262, dowody, safety case, oceny/assessments.
## Szybkie powiązania

- linkage_index.jsonl (safety/functional)
- iso_26262_compliance, safety_concept, hazard_log, fmea_register, validation_plan, change_management, configuration_management


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

1. Opisz system i interfejsy; wybierz metody (HARA/FMEA/FMEDA) i założenia.
2. Wykonaj analizę zagrożeń, ocenę ryzyka i wyznacz cele bezpieczeństwa.
3. Zdefiniuj wymagania i środki; zaplanuj V&V i metryki.
4. Utrzymuj traceability; aktualizuj po zmianach; zamknij DoR/DoD i linkage_index.


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

- HARA, FMEA, FMEDA, ASIL, SIL, SPFM, LFM, PMHF, Hazard log, Traceability.


## Przykłady użycia

- Analiza funkcji ADAS: HARA → ASIL → środki (redundant sensors, diagnostics) → V&V.
- System przemysłowy: HAZOP + FMEA, SIL określone, testy proof‑test, metrics PMHF.


## Ryzyka i ograniczenia

- Niepełna identyfikacja zagrożeń → niewystarczające środki; brak traceability → audyt niezaliczony.
- Brak weryfikacji założeń → błędne oceny ryzyka.


## Decyzje i uzasadnienia

- [Decyzja] Poziomy ASIL/SIL i środki kontrolne — uzasadnienie ryzyka i norm.
- [Decyzja] Metody i narzędzia analizy — uzasadnienie zgodności i powtarzalności.


## Powiązania z innymi dokumentami

- ISO 26262 Compliance, Safety Concept, Hazard Log, FMEA Register, Validation Plan, Change Mgmt, Configuration Mgmt.


## Powiązania z sekcjami innych dokumentów

- Hazard Log → scenariusze; Safety Concept → cele; Validation Plan → testy.


## Słownik pojęć w dokumencie

- HARA, FMEA, FMEDA, ASIL, SIL, SPFM, LFM, PMHF, Hazard log, Traceability.


## Wymagane odwołania do standardów

- ISO 26262, IEC 61508, normy sektorowe (rail/medical/avionics) jeśli dotyczy.


## Mapa relacji sekcja→sekcja

- HARA/FMEA → Cele → Wymagania → Środki → V&V → Traceability → Zmiany.


## Mapa relacji dokument→dokument

- Functional Safety Analysis → Safety Concept/Validation Plan → Change/Config Mgmt → Audit/Compliance.


## Ścieżki informacji

- System/Interfejsy → HARA/FMEA → Cele/Wymagania → Środki → V&V → Audit.


## Weryfikacja spójności

- [ ] Hazard log i cele spójne; traceability kompletne.
- [ ] Metryki SPFM/LFM/PMHF zgodne z normami lub zaplanowane.
- [ ] Relacje cross‑doc opisane; dokument w linkage_index.


## Lista kontrolna spójności relacji

- [ ] Każdy hazard ma ASIL/SIL, cel, wymagania i testy.
- [ ] Każda zmiana ma impact analysis i ewentualny re‑assessment.
- [ ] Relacje cross‑doc opisane z uzasadnieniem.


## Artefakty powiązane

- Hazard log, FMEA/FMEDA, Safety Concept, metryki SPFM/LFM/PMHF, plany V&V, traceability matryce, raporty review/audit.


## Ścieżka decyzji

- [Decyzja] → [Uzasadnienie] → [Konsekwencje] → [Właściciel] → [Data].


## Ścieżka akceptacji

- Safety/Engineering → QA/V&V → Compliance/Audit → Owner sign‑off.


## Metryki jakości

- Pokrycie hazardów, zgodność ASIL/SIL, spełnienie metryk SPFM/LFM/PMHF, kompletność traceability, liczba otwartych założeń/ryzyk.

## Kryteria ukończenia

- [ ] Analiza zakończona, cele/wymagania/środki określone, traceability kompletne.
- [ ] Dokument w linkage_index/checklistach; wersja/data/właściciel aktualne.


## Powiązania sekcja↔sekcja

- HARA/FMEA → Cele bezpieczeństwa → Wymagania → Środki kontrolne → V&V → Traceability.
- Założenia → Analiza → Ryzyka → Środki → Weryfikacja założeń.


## Struktura sekcji

1) Kontekst i definicja systemu (zakres, granice, interfejsy)  
2) Metody analizy (HARA/HAZOP/FMEA/FMEDA) i założenia  
3) Identyfikacja zagrożeń i scenariuszy, ocena ryzyka (ASIL/SIL)  
4) Cele bezpieczeństwa i wymagania bezpieczeństwa (funkcyjne/tech)  
5) Środki kontrolne (architektura, redundancja, diagnostyka, fail‑safe/degraded)  
6) Weryfikacja i walidacja (testy, analiza, pokrycie, metryki SPFM/LFM/PMHF)  
7) Traceability (hazard → cel → wymaganie → test → wynik)  
8) Zarządzanie zmianą i założeniami (impact, re‑analysis, re‑cert)  
9) Ryzyka, decyzje, open issues


## Wymagane rozwinięcia

- Tabele HARA/FMEA z rankingiem ryzyka, założenia i dowody.
- Cele bezpieczeństwa i ich alokacja do architektury/składowych.
- Metryki SPFM/LFM/PMHF i wyniki; kryteria akceptacji.


## Wymagane streszczenia

- Kluczowe zagrożenia i ASIL/SIL, cele bezpieczeństwa, główne środki kontrolne.
- Status V&V i główne metryki (SPFM/LFM/PMHF); otwarte ryzyka/założenia.


## Guidance (skrót)

- Prowadź hazard log i traceability end‑to‑end; aktualizuj po każdej zmianie.
- Jasno dokumentuj założenia i ich weryfikację; brak weryfikacji = ryzyko.
- Zgodność z normami: rolę niezależności, review, kwalifikacja narzędzi.
- Ustal degradację/fail‑safe i potwierdź w V&V; mierzalne metryki bezpieczeństwa.
- Przy zmianach wykonuj impact analysis i re‑assessment ASIL/SIL.


## Checklisty Definition of Ready (DoR)

- [ ] Opis systemu/interfejsów dostępny; normy i założenia zebrane.
- [ ] Narzędzia HARA/FMEA/FMEDA dostępne; hazard log aktualny.
- [ ] Struktura sekcji wypełniona/N/A.


## Checklisty Definition of Done (DoD)

- [ ] HARA/FMEA wykonane; cele i wymagania bezpieczeństwa opisane.
- [ ] Środki kontrolne zdefiniowane; metryki SPFM/LFM/PMHF obliczone lub zaplanowane.
- [ ] Traceability i plan V&V gotowe; dokument w linkage_index.
- [ ] Wersja/data/właściciel zaktualizowane.

