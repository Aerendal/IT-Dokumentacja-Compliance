---
title: Post-mortem POC
status: needs_content
aligned: true
aligned_rev: 7
aligned_at: 2026-02-09
aligned_by: codex
---
# Post-mortem POC


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Podsumować wyniki POC po jego zakończeniu: ocenić cele i kryteria sukcesu, przedstawić wyniki/metyki/feedback, wskazać problemy i root cause, podjąć decyzję (Go/Iterate/No-Go) i zaplanować dalsze kroki lub zamknięcie z lessons learned.


## Zakres i granice

- Obejmuje: cele/kryteria sukcesu POC, wyniki/metyki/demo, feedback użytkowników/stakeholderów, problemy i root cause (tech/organizacyjne), decyzję Go/Iterate/No-Go z uzasadnieniem, plan dalszy (backlog, zasoby, harmonogram) lub zamknięcie, lekcje i rekomendacje.  
- Poza zakresem: pełny plan rollout produkcyjny (osobny dokument).


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia

- Wejścia: cele/kryteria POC, metryki/testy, logi/demo, feedback, ryzyka i założenia, koszty/czas.  
- Wyjścia: decyzja Go/Iterate/No-Go, lista action items/backlog, rekomendacje, lessons learned, plany zasobów/harmonogram jeśli Go/Iterate.


## Założenia
- Zasoby DC dostępne; łączność stabilna.  
- Dostęp do licencji vendorów.  
- Zespół ma kompetencje w NFV/SDN.
## Otwarte pytania
- Jak obsłużyć compliance (np. 3GPP/ETSI) w audytach?  
- Jakie są limity licencyjne i CAPEX/OPEX na skalowanie?  
- Czy wymagane są profile k8s dla CNF (CPU pinning/hugepages)?  
- Jak testować SFC/latencję end-to-end?
## Powiązania (meta)

- Key Documents: harmonogram_poc_pilota, experimentation_plan, risk_register, change_management_plan, monitoring_strategy_document, communication_plan, postmortem_analysis.
- Key Document Structures: cele/kryteria, wyniki, problemy/root cause, decyzja, plan dalszy, lessons.
- Document Dependencies: dane/metyki/testy, demo/artefakty, feedback, koszt/czas.



## Zależności dokumentu
- Upstream: systemy źródłowe, dane referencyjne, decyzje architektoniczne nadrzędne.
- Downstream: konsumpcja rezultatów (zespoły, usługi, dokumenty pokrewne).
- Zewnętrzne: dostawcy, standardy branżowe, umowy/regulacje wpływające na zakres.
## Fazy cyklu życia
- Przygotowanie/migracja danych.
- Rollout (pilot → fala → pełne wdrożenie).
- Walidacja i smoke testy.
- Stabilizacja/monitoring i przekazanie do operacji.
## Struktura sekcji (szkielet)
- Cel i zakres wdrożenia
- Środowiska i okna wdrożeniowe
- Architektura docelowa i przepływy danych
- Kroki/migracja (pilot → produkcja)
- Plan testów i kryteria go/no-go
- Monitoring/observability i runbooki
- Rollback/contingency i komunikacja
- Ryzyka, zależności, RACI
## Szybkie powiązania

- linkage_index.jsonl (project/poc_postmortem)
- harmonogram_poc_pilota, experimentation_plan, risk_register, change_management_plan, monitoring_strategy_document, communication_plan, postmortem_analysis


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

1. Wprowadź cele/metryki i wyniki; opisz problemy/root cause.  
2. Podejmij decyzję i uzasadnij; dodaj plan dalszy lub zamknięcie.  
3. Dodaj lessons/action items; zaktualizuj linkage_index/checklisty.


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
- NFVI: infrastruktura uruchamiająca funkcje sieciowe.  
- MANO: orkiestracja i zarządzanie VNF/CNF.  
- SR-IOV/DPDK: techniki przyspieszania I/O sieciowego.
## Przykłady użycia
- Wdrożenie core 5G jako CNF na klastrze Kubernetes + SDN.  
- Wirtualizacja firewall/load balancer z akceleracją DPDK.  
- Skalowanie VNF EPC na nowe regiony z MANO.
## Ryzyka i ograniczenia
- Brak akceleracji → niespełnienie SLA latency.  
- Złożoność MANO/SDN → ryzyko błędów.  
- Brak testów HA → dłuższe outage.  
- Licencje vendorów ograniczające skalowanie.
## Decyzje i uzasadnienia
- Wybór platformy NFVI/SDN i MANO.  
- Które VNF/CNF akcelerować i jak.  
- Model segmentacji i bezpieczeństwa.  
- Parametry scale-out i alarmów.
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

- [ ] Kryteria sukcesu ocenione; decyzja oparta na danych; plan dalszy lub zamknięcie opisane.  
- [ ] Action items mają owner/ETA; dokument w linkage_index.


## Lista kontrolna spójności relacji

- [ ] Czy każda sekcja z relacją ma wskazaną sekcję źródłową?
- [ ] Czy relacje nie tworzą sprzecznych wymagań?
- [ ] Czy wszystkie wymagane standardy mają odwołania?
- [ ] Czy RACI jest kompletne dla kluczowych działań?

## Artefakty powiązane

- Raport metryk, demo, feedback, logi, ADR, action plan, waiver log (jeśli wyjątki), lessons repository.


## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji

- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status: oczekuje/zatwierdzone/odrzucone]
- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status]

## Metryki jakości

- Czas od końca POC do decyzji, % kryteriów osiągniętych, liczba action items otwartych/zamkniętych, czas do rollout/iteracji (jeśli Go), jakość lessons (feedback).

## Kryteria ukończenia

- [ ] Post-mortem POC kompletne; decyzja i plan zapisane; wersja/data/właściciel aktualne.


## Struktura sekcji

1) Cele POC i kryteria sukcesu (osiągnięte/nie; metryki)  
2) Wyniki i feedback (dane/metyki, demo, użytkownicy/stakeholderzy)  
3) Problemy i root cause (tech/organizacyjne; ograniczenia)  
4) Decyzja: Go/Iterate/No-Go (uzasadnienie, koszty/zasoby)  
5) Plan na dalej (backlog ulepszeń, zasoby, harmonogram) lub zamknięcie  
6) Lekcje i rekomendacje (dla przyszłych POC/projektów)  
7) Załączniki (metryki, demo linki, feedback, logi, ADR)


## Wymagane rozwinięcia

- Ocena kryteriów sukcesu z danymi; tabela metryk vs target.  
- Root cause i ograniczenia; wpływ na decyzję.  
- Plan po decyzji: backlog, zasoby, harmonogram, koszty; jeśli No-Go — co archiwizujemy/utrzymujemy.


## Wymagane streszczenia

- Executive: cele i status, decyzja Go/Iterate/No-Go, top 3 powody, główne rekomendacje i koszty/zasoby.


## Guidance (skrót)

- Decyzja musi być oparta na danych/feedbacku; dokumentuj uzasadnienie.  
- Lessons i rekomendacje wpisz do repo wiedzy; action items z owner/ETA.  
- Jeśli Iterate/Go – zaplanuj koszty/zasoby/harmonogram; jeśli No-Go – zamknij i zabezpiecz artefakty.


## Checklisty Definition of Ready (DoR)

- [ ] Cele/kryteria i metryki POC zebrane; wyniki/testy/demo dostępne; feedback zebrany.  
- [ ] Owner decyzji i interesariusze zidentyfikowani.


## Checklisty Definition of Done (DoD)

- [ ] Decyzja Go/Iterate/No-Go z uzasadnieniem; action items/backlog z owner/ETA; lessons i rekomendacje zapisane; dokument w linkage_index; metadane aktualne.

