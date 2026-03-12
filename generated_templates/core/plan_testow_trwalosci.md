---
title: Plan testów trwałości
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Plan testów trwałości


## Metadane

- Właściciel: Project Manager
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Przeprowadzić testy trwałości (soak/endurance) systemu/urządzeń, aby wykryć degradacje w długim okresie (drift metryk, leaki, stabilność UX).


## Zakres i granice

- Obejmuje: komponenty/urządzenia, środowisko, czas trwania i profil obciążenia, metryki (błędy/leaki, latency drift, CPU/RAM/IO, temperatura/baterie), scenariusze (stałe/zmienne obciążenie, cykle sleep/wake, niestabilna sieć), narzędzia i monitoring, kryteria akceptacji, raport i RCA/retest.  
- Poza zakresem: testy stress/spike (osobny plan), security.


## Użytkownicy i interesariusze
- **Project Manager** — prowadzi projekt, raportuje status i zarządza ryzykami
- **Project Sponsor** — akceptuje kluczowe decyzje i zapewnia zasoby
- **Development Team** — realizuje zadania zgodnie z planem
- **Stakeholders / Interesariusze** — odbierają raportowanie i zgłaszają zmiany zakresu

## Wejścia i wyjścia

- Wejścia: SLA/SLO, profile użytkowania, dane testowe, środowisko lab/prod-like, narzędzia load/monitoring, limity termiczne/battery (jeśli mobile/edge).  
- Wyjścia: scenariusze i konfiguracje testu, metryki i progi, raport wyników, lista defektów i rekomendacji z owner/ETA, plan retestu.


## Założenia

- [Założenie 1 — co przyjmujemy za prawdziwe bez weryfikacji]
- [Założenie 2 — warunki brzegowe, które muszą być spełnione]

## Otwarte pytania

- [Pytanie 1 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]
- [Pytanie 2 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]

## Powiązania (meta)

- Key Documents: endurance_testing_plan (jeśli rozdzielasz), performance_testing_plan, monitoring_strategy_document, capacity_planning, incident_response_playbook, change_management_plan, risk_register.
- Key Document Structures: zakres, scenariusze, metryki, narzędzia/monitoring, kryteria, raport.
- Document Dependencies: CI/CD, środowisko long-run, dane testowe, APM/logs/metrics, hardware telemetry (temp/battery), feature flags.



## Zależności dokumentu

- Konsumuje: [dokumenty wejściowe — co musi istnieć zanim ten dokument powstanie]
- Dostarcza do: [dokumenty wyjściowe — co korzysta z tego dokumentu]

## Fazy cyklu życia
- Faza 1: Koncepcja i Wizja: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 2: Analiza Wymagań: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 3: Projekt / Design: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 4: Planowanie: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 5: Implementacja: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 6: Testowanie / QA: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 7: Bezpieczeństwo / Compliance: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 8: Wdrożenie / Deployment: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 9: Operacje / Maintenance: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
## Struktura sekcji (szkielet)
1. Zakres: komponenty/ścieżki krytyczne, SLA/SLO, środowisko testowe.
2. Scenariusze: load/stress/soak/spike, profile ruchu, dane testowe.
3. Metryki: latency p95/p99, throughput, error rate, zasoby, koszt.
4. Narzędzia i konfiguracja: generator ruchu, monitoring, korelacja trace/logs.
5. Kryteria akceptacji: progi, tolerancje, budżet błędów; Go/No-Go.
6. Plan wykonania i raport: harmonogram, role, ryzyka, format wyników.
## Szybkie powiązania

- linkage_index.jsonl (qa/durability_testing)
- endurance_testing_plan, performance_testing_plan, monitoring_strategy_document, capacity_planning, incident_response_playbook, change_management_plan, risk_register


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **IEEE 829** — Dokumentacja Testowania Oprogramowania i Systemów
- **ISO 9001** — System Zarządzania Jakością (QMS)
- **ISO/IEC 25010** — Model Jakości Systemu i Oprogramowania (SQuaRE)

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

1. Zdefiniuj czas/profil/metyki/progi; przygotuj środowisko i monitoring.  
2. Uruchom test, zbierz logi/metryki, obserwuj drift; stosuj progi stop.  
3. Sporządź raport i action items; zaplanuj retest; zaktualizuj linkage_index.


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

- [ ] Scenariusze i progi spójne z SLO; monitoring/alerty aktywne; logi kompletne.  
- [ ] Action items przypisane; retest zaplanowany; dokument w linkage_index.


## Lista kontrolna spójności relacji

- [ ] Czy każda sekcja z relacją ma wskazaną sekcję źródłową?
- [ ] Czy relacje nie tworzą sprzecznych wymagań?
- [ ] Czy wszystkie wymagane standardy mają odwołania?
- [ ] Czy RACI jest kompletne dla kluczowych działań?

## Artefakty powiązane

- Skrypty/config, logi/dash, raport, defekt log, action plan, waiver log, ADR log.


## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji

- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status: oczekuje/zatwierdzone/odrzucone]
- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status]

## Metryki jakości

- Drift latency/error, liczba/leak rate, czas do degradacji, sukces retestu, liczba krytycznych defektów, czas analizy, liczba waiverów i czas sunset.

## Kryteria ukończenia

- [ ] Raport testów trwałości z decyzjami i planem retestu; wersja/data/właściciel aktualne.


## Struktura sekcji

1) Zakres i cele (komponenty, czas testu, obciążenie, SLO)  
2) Metryki i progi (errors, latency drift, CPU/RAM/IO, FD/threads, temp/battery)  
3) Scenariusze (stałe/zmienne obciążenie, sleep/wake, niestabilna sieć, long-run)  
4) Narzędzia i monitoring (generator ruchu, długoterminowe logi, alerty, log rotation)  
5) Kryteria akceptacji/stopu (brak wzrostu błędów/leak, drift w granicach, UX stabilny)  
6) Raport i RCA/retest (wyniki, anomalie, action items, ETA)  
7) Załączniki (skrypty, config, dashboardy, logi, test data)


## Wymagane rozwinięcia

- Czas trwania i profil obciążenia; progi drift/leak; plan log rotation/retencji.  
- Scenariusze sieci/sleep/wake i hardware (temp/battery) jeśli dotyczy.  
- Plan retestu po fixach; ochrona środowiska (bezpieczeństwo danych).


## Wymagane streszczenia

- Executive: SLO vs wyniki, wykryte leaki/drift, defekty krytyczne, rekomendacje/ETA, plan retestu.


## Guidance (skrót)

- Long‑run = mierz trendy; włącz GC/FD/threads i temp/battery.  
- Kontroluj dane/seed; loguj i rotuj logi; ustaw progi stop.  
- Raportuj z rekomendacjami i planem retestu; zabezpiecz rollback/stop.


## Checklisty Definition of Ready (DoR)

- [ ] SLO/profil/czas testu ustalone; środowisko i dane gotowe; monitoring długoterminowy skonfigurowany.  
- [ ] Progi drift/leak/stop wstępnie ustalone.


## Checklisty Definition of Done (DoD)

- [ ] Test wykonany; metryki zebrane; raport i action items z owner/ETA; plan retestu ustawiony; dokument w linkage_index; metadane aktualne.

