---
title: Billing Metrics
status: needs_content
aligned: true
aligned_rev: 7
aligned_at: 2026-02-09
aligned_by: codex
---
# Billing Metrics


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Definiuje metryki rozliczeń i ich pomiar w systemie billingowym: poprawność naliczeń, kompletność danych, wydajność procesów, koszty i satysfakcję klientów. Ma zapobiegać błędom billingowym, stratom przychodu i sporom.


## Zakres i granice

- Obejmuje: metryki poprawności/kompletności (revenue leakage, error rate), wolumen i wydajność pipeline (ETL/rating/invoicing), SLA faktur, retry/queue, koszty (cloud/operacyjne), wskaźniki sporów/chargeback, satysfakcję (billing NPS), alerty i raporty, segmenty (plan/region).
- Poza zakresem: strategia cenowa i podatkowa (oddzielne dokumenty), szczegółowe modele produktowe.


## Użytkownicy i interesariusze
- Automation CoE, Ops/SRE, Business Owners, Security/Compliance, Finance/FinOps.
## Wejścia i wyjścia

- Wejścia: dane usage/entitlements/pricing, stawki podatkowe, kursy walut, harmonogramy faktur, SLA/reguły, logi błędów, dane chargeback/spory, koszty infra billing, dane NPS/CSAT.
- Wyjścia: zestaw metryk/KPI/KRI, definicje źródeł i wzorów, dashboardy i alerty, raporty cykliczne, lista defektów/odchyleń i działań korygujących.


## Założenia
- Orkiestrator/logi dostępne; dane kosztowe z FinOps/ERP.
- Polityka SoD i audytu jest zdefiniowana.
## Otwarte pytania
- Czy mierzymy efekty uboczne (shadow IT, manual overrides)?
- Jak często rewizja progów i dashboardów?
## Powiązania (meta)

- Key Documents: pricing_strategy, tax_compliance, revenue_management, finops, data_quality, incident_response_billing.
- Key Document Structures: metryki, progi, alerty, raporty, działania.
- Document Dependencies: billing data pipeline, pricing/tax services, DWH/BI, observability, customer support.


## Zależności dokumentu

Wymaga zmapowanych źródeł usage/entitlements/pricing/tax, SLA faktur, danych o błędach/sporach, dostępu do BI/alertingu. Brak = DoR otwarte.


## Fazy cyklu życia

- Planowanie: wybór KPI/KRI, progi, źródła, segmenty.
- Implementacja: instrumentacja, dashboardy, alerty.
- Operacje: monitoring, raporty, obsługa odchyleń/sporów.
- Retrospektywa: trend, wpływ działań, zmiana progów/metryk.



## Struktura sekcji (szkielet)

- Podsumowanie wykonawcze
- Kluczowe metryki i KPI
- Trendy i analiza
- Problemy i rekomendacje
- Kolejne kroki

## Szybkie powiązania
- transportation-metrics
- topic-metrics
- sustainability-metrics
- performance-metrics
- monetization-metrics

## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **GDPR / RODO** — Ogólne Rozporządzenie o Ochronie Danych Osobowych (UE)
- **IEEE 829** — Dokumentacja Testowania Oprogramowania i Systemów
- **ISO 9001** — System Zarządzania Jakością (QMS)
- **ISO/IEC 25010** — Model Jakości Systemu i Oprogramowania (SQuaRE)
- **ISO/IEC 27001** — System Zarządzania Bezpieczeństwem Informacji (ISMS)
- **PCI DSS** — Standard Bezpieczeństwa Danych Przemysłu Kart Płatniczych

### Polskie normy i regulacje
- **KNF-REKOM-IT** — Rekomendacje KNF dot. systemów IT w sektorze finansowym
- **MIFID2-PL** — MiFID II — Dyrektywa dot. Rynku Finansowego (implementacja PL)
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
1. Zbierz katalog procesów i dane źródłowe metryk.
2. Zdefiniuj KPI/KRI, progi i alerty; przypisz właścicieli.
3. Skonfiguruj dashboardy/widoki; opisz raportowanie cykliczne.
4. Wypełnij DoR/DoD; aktualizuj przy każdej większej zmianie automatyzacji.
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
- Throughput botów, Retry rate, Bot MTTR, Automation SLA, Drift ML, SoD hit.
## Przykłady użycia
- Raport miesięczny value i awaryjności dla zarządu.
- Alert: wzrost retraje > próg → analiza przyczyny i rollback wersji bota.
## Ryzyka i ograniczenia
- Metryki bez spójnych źródeł lub definicji → mylne decyzje.
- Brak SoD/audytu → ryzyko naruszeń compliance.
## Decyzje i uzasadnienia
- Wybór metryk/SLO na dashboardzie.  
- Progi i kanały eskalacji.  
- Layout (kolejność, grupowanie).  
- Retencja i wersjonowanie zmian.
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

- Poprawność/kompletność → Alerty → Działania korygujące → Raporty.
- Wydajność pipeline → SLA faktur → Backlog/incident response.
- Spory/chargeback → Customer support → Revenue impact.


## Struktura sekcji

1) Cele i segmenty (plany/regiony/typy usage)  
2) Poprawność i kompletność (revenue leakage, error rate, missing usage)  
3) Wydajność pipeline (ETL/rating/invoicing: latency, backlog, retry)  
4) SLA faktur i terminowość (on-time %, opóźnienia)  
5) Spory/chargeback i błędy klienta (count/rate, odzyskane)  
6) Koszty billing (cloud/ops per invoice/GB) i FinOps  
7) Satysfakcja (billing NPS/CSAT) i ticket volume  
8) Alerty/progi, raporty i właściciele reakcji

