---
title: Recruitment Funnel Metrics
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Recruitment Funnel Metrics


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Zdefiniować i monitorować metryki lejka rekrutacyjnego, aby mierzyć skuteczność pozyskiwania talentów, optymalizować proces i raportować interesariuszom.


## Zakres i granice

- Obejmuje: metryki źródeł kandydatów, konwersje etapów (aplikacja→screening→interview→offer→hire), time-to-hire, time-in-stage, cost-per-hire, quality-of-hire, diversity, drop-off, SLA dla rekruterów/managerów, raportowanie i alerty.  
- Poza zakresem: polityka wynagrodzeń, oceny performance po onboardingu (oddzielne dokumenty).


## Użytkownicy i interesariusze
- Automation CoE, Ops/SRE, Business Owners, Security/Compliance, Finance/FinOps.
## Wejścia i wyjścia

- Wejścia: dane ATS, kalendarze, źródła kandydatów, koszty kampanii, SLA, role/poziomy, dane DEI.  
- Wyjścia: słownik metryk, dashboard/raporty, progi alertów, checklisty DoR/DoD, harmonogram raportowania, mapowanie danych do warehouse.


## Założenia

- ATS zapewnia spójne dane.  
- Zespół ma dostęp do BI.  
- Polityki DEI i prywatności są zatwierdzone.


## Otwarte pytania

- Jak mierzyć quality-of-hire (proxy, czas)?  
- Jak długo przechowywać dane kandydatów w raportach?  
- Jak obsłużyć rynki z różnymi wymogami DEI?

## Powiązania (meta)

- Key Documents: performance_metrics_dashboard, data_quality_playbook, access_control_policy, bias_fairness_policy, documentation_roadmap.  
- Key Document Structures: metryki, źródła, konwersje, SLA, raporty.  
- Document Dependencies: ATS, BI/warehouse, identity/roles, calendar, cost tracking.


## Zależności dokumentu

Wymaga: spójnych danych ATS, słownika etapów, mapy źródeł, kosztów kampanii, polityk DEI, dostępu do BI/warehouse. Brak = brak DoR.


## Fazy cyklu życia

- Definicja metryk i źródeł.  
- Implementacja zbierania danych i dashboardów.  
- Monitoring i alerty.  
- Przeglądy i iteracje.



## Struktura sekcji (szkielet)

- Podsumowanie wykonawcze
- Kluczowe metryki i KPI
- Trendy i analiza
- Problemy i rekomendacje
- Kolejne kroki

## Szybkie powiązania

- linkage_index.jsonl (recruitment/funnel/metrics)  
- performance_metrics_dashboard, bias_fairness_policy


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

1. Ustal metryki i mapowanie danych.  
2. Zbuduj dashboard i alerty; włącz QA danych.  
3. Raportuj cyklicznie; aktualizuj progi i definicje.  
4. Dokumentuj zmiany w linkage_index.


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

- Time-to-hire: czas od otwarcia do akceptacji oferty.  
- Drop-off: odsetek kandydatów opuszczających etap.  
- Quality-of-hire: wskaźnik po onboardingu (np. performance/retention proxy).


## Przykłady użycia

- Porównanie źródeł kandydatów pod kątem konwersji i kosztu.  
- Alert na wydłużenie time-to-hire dla ról krytycznych.  
- Raport DEI dla etapu shortlist i offer.


## Ryzyka i ograniczenia

- Złe dane ATS → błędne KPI.  
- Brak anonimizacji DEI → ryzyko prawne.  
- Zbyt wiele metryk → brak fokusu.  
- Brak actionability → metryki nie prowadzą do zmian.


## Decyzje i uzasadnienia

- Wybór minimalnego zestawu KPI.  
- Zakres segmentacji (region, rola, poziom).  
- Progi alertów.  
- Częstotliwość raportów.


## Powiązania z innymi dokumentami
- Automation Strategy, RPA Governance, ML Ops Runbook, Security Baseline, Change Mgmt.
## Powiązania z sekcjami innych dokumentów
- ML Ops → accuracy/drift; Security/SoD → access metrics; FinOps → cost/value.
## Słownik pojęć w dokumencie
- KPI/KRI, SLA/SLO, Drift, Retry, MTTR, SoD, Audit trail.
## Wymagane odwołania do standardów
- Polityki SoD, audyt (np. SOC2/ISO), wymagania prywatności danych procesów.
## Mapa relacji sekcja→sekcja
- Procesy → Metryki → Progi/alerty → Dashboardy → Decyzje → Action plan.
## Mapa relacji dokument→dokument
- Hyperautomation Metrics → Automation Strategy → Change/Release → Audit/Compliance.
## Ścieżki informacji
- Logi/monitoring → Agregacja → Dashboardy/alerty → Decyzje → Retrospektywa.
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
- Dashboardy (BI/observability), raporty cykliczne, definicje metryk, konfiguracje alertów.
## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji
- Automation CoE → Security/Compliance → Business Owners → Exec sign‑off.
## Metryki jakości
- Coverage procesów (% z metrykami), alert fidelity (false positive/negative), aktualność danych, czas reakcji na alert, wartość biznesowa (czas/koszt saved), MTTR botów, drift ML.
## Kryteria ukończenia
- [ ] Metryki/progi/alerty działają i są raportowane.
- [ ] Dashboardy dostępne dla interesariuszy; instrukcje widoków opisane.
- [ ] Dokument powiązany w linkage_index i checklistach.
## Powiązania sekcja↔sekcja

- Etapy → Konwersje → Time-to-hire.  
- Źródła → Jakość/dostępność → Cost-per-hire.  
- DEI → Quality-of-hire → Raporty.


## Struktura sekcji

1) Słownik metryk i definicji  
2) Dane i mapowanie z ATS/BI  
3) SLA i progi alertów  
4) Dashboardy/raporty i kadencja  
5) DEI i bias monitorowanie  
6) DoR/DoD, ryzyka, pytania


## Wymagane rozwinięcia

- Tabela metryk (definicja, wzór, źródło, segmenty, właściciel).  
- Progi SLA/alertów (time-to-hire, time-in-stage, drop-off).  
- Widoki DEI (płeć, region, seniority) zgodne z polityką prywatności.  
- Raporty tyg./mies. i odbiorcy.  
- Kontrola jakości danych ATS (duplikaty, brak etapów).


## Wymagane streszczenia

- Executive summary: top KPI i trendy.  
- Skrót źródeł o najwyższej konwersji/koszcie.


## Guidance (skrót)

- Standaryzuj etapy i kody źródeł w ATS.  
- Waliduj dane wejściowe; brak etapów = brak raportu.  
- Alertuj na wydłużony time-to-hire i drop-off w krytycznych rolach.  
- Monitoruj DEI, ale respektuj prywatność i prawo pracy.  
- Aktualizuj linkage_index po zmianach metryk.


## Checklisty Definition of Ready (DoR)

- [ ] Etapy i źródła w ATS ustandaryzowane.  
- [ ] Dane dostępne w warehouse/BI.  
- [ ] Definicje metryk i SLA zatwierdzone.  
- [ ] Polityka DEI i prywatności uwzględniona.  
- [ ] Odbiorcy raportów określeni.


## Checklisty Definition of Done (DoD)

- [ ] Dashboard i alerty działają; dane poprawne.  
- [ ] Raporty w kadencji publikowane; brak krytycznych braków danych.  
- [ ] Definicje/metadane w słowniku; linkage_index zaktualizowany.  
- [ ] Progi/SLA zweryfikowane po pierwszym cyklu.  
- [ ] Feedback wdrożony; plan kolejnych iteracji.

