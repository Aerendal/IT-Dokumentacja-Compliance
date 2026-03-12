---
title: Common Edge AI Issues
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Common Edge AI Issues


## Metadane

- Właściciel: ML Engineer
- Wersja: v0.3
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Katalog typowych problemów w systemach Edge AI (urządzenia, brzeg sieci, małe inferencje) oraz sposoby diagnozy i mitigacji, aby skrócić czas reakcji na regresje jakości, wydajności i stabilności.


## Zakres i granice

- Obejmuje: dane/kalibrację (drift, szum), model (kwantyzacja/pruning/kompresja), runtime/zasoby (latencja, OOM, throttling), łączność (offline/jitter), OTA/wersje/compat, bezpieczeństwo (klucze/model theft), monitoring/logi, testy regresyjne edge.  
- Poza zakresem: trening modeli (osobne dokumenty), projekt hardware od podstaw.


## Użytkownicy i interesariusze
- **ML Engineer / Data Scientist** — buduje, trenuje i ewaluuje modele
- **Data Engineer** — przygotowuje dane i zarządza pipeline'ami
- **Product Owner** — definiuje metryki sukcesu i priorytety eksperymentów
- **MLOps Engineer** — zarządza wdrożeniem i monitoringiem modeli na produkcji

## Wejścia i wyjścia

- Wejścia: telemetria urządzeń (CPU/GPU/TPU, RAM, temperatura), dane kalibracyjne, wersje modeli/runtime/driverów/firmware, profile ruchu, SLO (latencja/accuracy), polityki OTA/rollback, polityki bezpieczeństwa.  
- Wyjścia: tabela issue→diagnoza→mitigacja, checklisty debug, wymagania monitoringu/logów, plan testów regresyjnych edge, linki do playbooków, wpis w linkage_index.


## Założenia

- [Założenie 1 — co przyjmujemy za prawdziwe bez weryfikacji]
- [Założenie 2 — warunki brzegowe, które muszą być spełnione]

## Otwarte pytania

- [Pytanie 1 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]
- [Pytanie 2 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]

## Powiązania (meta)

- Key Documents: iot_sensor_integration_design, ota_update_policy, observability_edge, security_edge_ai, model_serving_architecture.  
- Key Document Structures: dane/kalibracja, model, runtime/zasoby, łączność, OTA/compat, bezpieczeństwo, monitoring, testy.  
- Document Dependencies: device fleet mgmt, monitoring/telemetry, OTA/feature flags, model registry, driver/firmware mgmt.



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
- Streszczenie celu i KPI
- Kontekst, założenia i ograniczenia
- Zakres oraz role/RACI
- Główne decyzje i warianty
- Proces/architektura/etapy
- Ryzyka, zależności i mitigacje
- Plan wdrożenia i kryteria akceptacji
- Monitoring i raportowanie
- Załączniki i źródła
## Szybkie powiązania

- linkage_index.jsonl (edge_ai/common_issues)  
- observability_edge, ota_update_policy, security_edge_ai


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **ISO/IEC 23053** — Framework dla Systemów AI z Uczeniem Maszynowym
- **ISO/IEC 42001** — System Zarządzania Sztuczną Inteligencją (AIMS)
- **NIST CSF** — Framework Cyberbezpieczeństwa NIST

### Polskie normy i regulacje
- **UODO-PL** — Ustawa o Ochronie Danych Osobowych (implementacja RODO)

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

1. Zidentyfikuj objaw (accuracy drop, latency, offline, OTA fail); przejdź odpowiednią sekcję.  
2. Użyj checklisty debug i logów; zastosuj mitigację.  
3. Dodaj nowe wzorce, zaktualizuj linkage_index i checklisty.


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

- [ ] Każdy typowy problem ma diagnozę i mitigację; alerty dla SLO działają.  
- [ ] OTA/rollback i bezpieczeństwo (klucze/model) opisane; drift/temperatura monitorowane.  
- [ ] Linkage_index i checklisty aktualne.


## Lista kontrolna spójności relacji

- [ ] Czy każda sekcja z relacją ma wskazaną sekcję źródłową?
- [ ] Czy relacje nie tworzą sprzecznych wymagań?
- [ ] Czy wszystkie wymagane standardy mają odwołania?
- [ ] Czy RACI jest kompletne dla kluczowych działań?

## Artefakty powiązane

- Telemetria/logi, wersje model/runtime/driver/firmware, polityka OTA, benchmarki/QA wyniki, SLO dashboardy, ADR/waiver log.


## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji

- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status: oczekuje/zatwierdzone/odrzucone]
- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status]

## Metryki jakości

- MTTR edge AI, accuracy/latency vs SLO, sukces OTA/rollback, liczba powtórzeń tych samych wzorców, % urządzeń z aktualnym modelem/runtime.

## Kryteria ukończenia

- [ ] Dokument skraca MTTR dla incydentów Edge AI i jest powiązany w linkage_index.


## Struktura sekcji

1) Dane i kalibracja (drift, bias, brakujące dane, szum)  
2) Model (kwantyzacja/pruning/kompresja; accuracy vs latencja)  
3) Runtime/zasoby (CPU/GPU/TPU, OOM, temperatura, throttling, scheduler)  
4) Łączność i QoS (offline, jitter, retry, cache, store-and-forward)  
5) OTA/wersje/compat (model/runtime/driver/firmware, rollback, staged rollout)  
6) Bezpieczeństwo (klucze, model theft, integrity, TEE/secure element)  
7) Monitoring/logi (metryki, sampling, privacy, storage)  
8) Testy regresyjne edge (lab/in‑field, canary/A-B, benchmarki)  
9) Załączniki (checklisty, wzorce logów, ADR/waiver log)


## Wymagane rozwinięcia

- Najczęstsze wzorce issue per sekcja (np. drift po wymianie sensora, OOM po kwantyzacji, throttling GPU, OTA brick) z krokami diagnozy/mitigacji.  
- Progi alertów dla SLO (latencja p95, accuracy drop) i routing on-call.  
- Checklisty debug: jakie logi/metryki zebrać, jak odtworzyć w labie.  
- Plan testów regresyjnych edge przed rolloutem (devices/regions) i kryteria pass/fail.


## Wymagane streszczenia

- Executive: top 5 edge AI issue patterns, stan SLO (latencja/accuracy), główne ryzyka (OTA/driver/drift).


## Guidance (skrót)

- Najpierw sprawdź wersje model/runtime/driver i kalibrację sensora; wersje często psują QoS.  
- Przy braku łączności stosuj store-and-forward i retry z backoff; waliduj cache spójność.  
- Kwantyzacja/pruning: mierz accuracy i latencję; miej rollback.  
- OTA zawsze staged + rollback + health check; loguj i podpisuj paczki.  
- Monitoruj drift i temperatury; throttling to częsty winowajca.


## Checklisty Definition of Ready (DoR)

- [ ] Telemetria urządzeń i wersje model/runtime/driver dostępne; polityka OTA/rollback znana.  
- [ ] SLO (latencja/accuracy) i progi wstępne zdefiniowane.


## Checklisty Definition of Done (DoD)

- [ ] Wzorce issue i mitigacje opisane; progi/alerty uzupełnione; linkage_index zaktualizowany.  
- [ ] Checklisty debug/testów regresyjnych dołączone; status/metadane aktualne; checklisty DoR/DoD odhaczone.  
- [ ] Plan retest/rollback dla OTA/wersji opisany.

