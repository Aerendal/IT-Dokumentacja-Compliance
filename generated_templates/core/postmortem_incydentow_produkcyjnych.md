---
title: Postmortem incydentów produkcyjnych
status: needs_content
aligned: true
aligned_rev: 8
aligned_at: 2026-02-09
aligned_by: codex
---
# Postmortem incydentów produkcyjnych


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Standard analizy incydentów w produkcji: timeline fact-based, wpływ/SLA, root cause, CAPA, usprawnienia systemowe, follow‑up i lessons learned, aby ograniczyć powtórki i skrócić MTTR.


## Zakres i granice

- Obejmuje: podsumowanie incydentu (wpływ, SLA, czasy detekcji/rezolucji), timeline (fakty/alerty/decyzje/komunikacja), root cause i czynniki współprzyczyniające, CAPA (akcje naprawcze/prewencyjne z owner/ETA), usprawnienia systemowe (monitoring/testy/runbooki/procesy/szkolenia), follow‑up (retest, walidacja CAPA, aktualizacja dokumentacji, lessons).  
- Poza zakresem: pełny raport bezpieczeństwa jeśli breach (link do IR/Breach).


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia

- Wejścia: ticket/alert/logi/metryki, SLA/SLO, change log, runbooki, komunikacja, wcześniejsze postmortemy.  
- Wyjścia: raport postmortem, CAPA z owner/ETA/status, usprawnienia systemowe, follow‑up/retest plan, lessons learned i decyzje.


## Założenia
- Dostępne są dane (logi/metryki), zespoły są dostępne do analizy, kultura blameless obowiązuje.
## Otwarte pytania
- Czy wymagane są powiadomienia regulatora/klientów?  
- Czy potrzebna jest dodatkowa analiza bezpieczeństwa (jeśli dotyczy)?
## Powiązania (meta)

- Key Documents: incident_response_playbook, incident_notifications, postmortem_analysis, disaster_recovery_plan, business_continuity_plan, monitoring_strategy_document, change_management_plan, risk_register.
- Key Document Structures: podsumowanie, timeline, root cause, CAPA, usprawnienia, follow‑up.
- Document Dependencies: logi/metryki/trace, change log, runbooki, monitoring/alerting, ticketing, CAB/Change.



## Zależności dokumentu
- Upstream: systemy źródłowe, dane referencyjne, decyzje architektoniczne nadrzędne.
- Downstream: konsumpcja rezultatów (zespoły, usługi, dokumenty pokrewne).
- Zewnętrzne: dostawcy, standardy branżowe, umowy/regulacje wpływające na zakres.
## Fazy cyklu życia
- Zbieranie faktów i timeline.
- Analiza wpływu i przyczyn.
- Definicja CAPA i usprawnień systemowych/procesowych.
- Walidacja CAPA, retesty, aktualizacja dokumentacji.
- Przegląd/akceptacja i zamknięcie.
## Struktura sekcji (szkielet)
- Cel i definicja sukcesu (KPI)
- Zakres, założenia i ograniczenia
- Interesariusze i role/RACI
- Kamienie milowe i daty
- Plan fal/sprintów z deliverables
- Zależności i ryzyka oraz plan mitigacji
- Budżet/zasoby i obłożenie
- Plan komunikacji i raportowania
- Kryteria akceptacji/go-live i plan rewizji
## Szybkie powiązania

- linkage_index.jsonl (incident/postmortem_prod)
- incident_response_playbook, incident_notifications, disaster_recovery_plan, business_continuity_plan, monitoring_strategy_document, change_management_plan, risk_register, postmortem_analysis


## Mające zastosowanie standardy i normy

### Standardy międzynarodowe
- **ITIL 4** — Biblioteka Infrastruktury IT (Zarządzanie Usługami)
- **ISO 22301** — System Zarządzania Ciągłością Działania (BCMS)
- **NIST CSF** — Framework Cyberbezpieczeństwa NIST
- **ISO/IEC 27001** — System Zarządzania Bezpieczeństwem Informacji (ISMS)

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

1. Zbierz fakty/timeline i wpływ; wypełnij sekcje 1–3.  
2. Dodaj CAPA/usprawnienia i follow‑up; linkuj dowody; zamknij DoR/DoD i linkage_index.


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
- Sanity check: proste testy wykrywające oczywiste błędy danych/wyników.  
- Backtest: testowanie modelu na danych historycznych z symulacją.  
- Conditional go: akceptacja z warunkami/mitigacjami.
## Przykłady użycia
- Walidacja analizy wpływu ceny na konwersję.  
- Backtest modelu scoringowego.  
- Re-run analizy po aktualizacji danych źródłowych.
## Ryzyka i ograniczenia
- Brak dowodów → wnioski słabe; brak follow‑up → powtórki; brak ownerów → CAPA niezamknięte; blame → kultura defensywna.
## Decyzje i uzasadnienia
- Progi istotności/efektu.  
- Zakres testów DQ/sanity vs czas.  
- Kiedy wymagany niezależny reviewer.
## Powiązania z innymi dokumentami
- Incident Response Playbook, Incident Notifications, DRP/BCP, Monitoring Strategy, Change Management Plan, Risk Register, SLO.
## Powiązania z sekcjami innych dokumentów
- Monitoring → alerty/timeline; DR/BCP → reakcja; Change → przyczyny; Risk Register → wpisy; Lessons Learned → baza wiedzy.
## Słownik pojęć w dokumencie
- MTTR, SLA/SLO, Root Cause, Contributing Factors, CAPA, Waiver, Sunset, Blameless.
## Wymagane odwołania do standardów
- Polityki IR/BCP/DR; ewentualne wymogi regulatora jeśli incydent dotyczył danych/usług krytycznych.
## Mapa relacji sekcja→sekcja
- Timeline → Wpływ → Root cause → CAPA → Usprawnienia → Follow‑up.
## Mapa relacji dokument→dokument
- Postmortem → Incident Response/DR/BCP/Monitoring/Change/Risk → Lessons Learned.
## Ścieżki informacji
- Alert/logi → Timeline → Analiza → CAPA → Retest → Aktualizacja dokumentacji.
## Weryfikacja spójności

- [ ] Root cause poparte faktami; CAPA ma dowód; usprawnienia z monitoring/test/runbook.  
- [ ] Follow‑up/retest ustawiony; dokument w linkage_index.


## Lista kontrolna spójności relacji

- [ ] Czy każda sekcja z relacją ma wskazaną sekcję źródłową?
- [ ] Czy relacje nie tworzą sprzecznych wymagań?
- [ ] Czy wszystkie wymagane standardy mają odwołania?
- [ ] Czy RACI jest kompletne dla kluczowych działań?

## Artefakty powiązane

- Logi/metryki/trace, change log, komunikacja, tickety CAPA, wykresy, lessons learned register, waiver log, ADR log.


## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji

- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status: oczekuje/zatwierdzone/odrzucone]
- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status]

## Metryki jakości

- MTTR/MTTA, % CAPA zamkniętych w terminie, recydywa podobnych incydentów, jakość danych w raporcie, liczba waiverów i czas sunset.

## Kryteria ukończenia

- [ ] Raport ukończony, CAPA/waivery i follow‑up zapisane; wersja/data/właściciel aktualne.


## Struktura sekcji

1) Podsumowanie (zdarzenie, wpływ, SLA/SLO, daty/czasy, status)  
2) Timeline (fakty, alerty, decyzje, komunikacja)  
3) Root cause i contributory factors (tech/proces/people)  
4) CAPA (akcje naprawcze/prewencyjne, owner, ETA, status, dowody)  
5) Usprawnienia systemowe (monitoring, testy, runbooki, procesy, szkolenia)  
6) Follow‑up i walidacja (retest, audyt CAPA, sunset waiverów, lessons learned)  
7) Załączniki (logi, wykresy, tickety, linki do runbooków)


## Wymagane rozwinięcia

- Pełna oś czasu z faktami; metryki wpływu; root cause + contributory.  
- CAPA z priorytetem i dowodem; usprawnienia w monitoring/testach/runbookach.  
- Plan follow‑up/retest; lekcje i wpis do lessons repository.


## Wymagane streszczenia

- Executive: co się stało, wpływ/SLA, root cause, top 3 CAPA/ETA, decyzje.


## Guidance (skrót)

- Blameless, oparte na faktach; oddziel symptomy od przyczyn.  
- Każda CAPA ma owner/ETA/dowód; waivery z sunset; follow‑up obowiązkowy.  
- Aktualizuj monitoring/runbooki/testy w tym samym cyklu; dokumentuj komunikację.


## Checklisty Definition of Ready (DoR)

- [ ] Logi/metryki/trace i timeline wstępny zebrane; owner postmortem wyznaczony; SLA/SLO znane.


## Checklisty Definition of Done (DoD)

- [ ] Timeline, wpływ, root cause opisane; CAPA/usprawnienia z owner/ETA; waivery z sunset; follow‑up/retest zaplanowany; dokument w linkage_index; metadane aktualne.

