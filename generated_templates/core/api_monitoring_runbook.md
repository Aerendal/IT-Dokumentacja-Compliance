---
title: API Monitoring Runbook
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# API Monitoring Runbook


## Metadane

- Właściciel: Backend Developer
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved
- Repo / moduł: [link]


## Cel dokumentu

Zapewnić procedury reagowania na alerty monitoringu API (latencja, błędy, throttling, auth).


## Zakres i granice

- Obejmuje: triage alertów (latency/error/429/auth), checklista szybkiej diagnostyki, eskalacje, komunikację, rollback jeśli dotyczy.
- Poza zakresem: naprawy backendów usług.


## Użytkownicy i interesariusze
- **Backend Developer / API Owner** — projektuje i implementuje interfejs API
- **Frontend Developer / Consumer** — integruje się z API i zgłasza wymagania
- **Integration Architect** — definiuje standardy integracji i kontrakt API
- **QA Engineer** — weryfikuje kontrakty i scenariusze błędów

## Wejścia i wyjścia
- Wejścia: lista krytycznych flow/stron, standardy A11y (WCAG 2.1 AA), konfiguracje narzędzi, budżet czasowy testów manualnych, release plan, backlog defektów, polityka VPAT/ACR.  
- Wyjścia: dashboard/metyki A11y, alerty, raporty cykliczne, backlog defektów z priorytetem/SLA, plan retestów, status VPAT/ACR.
## Założenia
- Dostępny design system i komponenty A11y.  
- CI/CD pozwala na skany i raporty.  
- Zespół ma kompetencje do testów manualnych AT.
## Otwarte pytania
- Jakie jurysdykcje/klienci wymagają formalnego VPAT/ACR?  
- Jak mierzyć i raportować trend defektów A11y?  
- Jak obsługiwać wyjątki/waivery?
## Powiązania (meta)
- Key Documents: accessibility_compliance, design_system_guidelines, release_plan, qa_strategy_document, incident_response_runbook, communication_plan.  
- Key Document Structures: scope, narzędzia, metryki, alerty, triage, raportowanie, SLA.  
- Document Dependencies: CI/CD, monitoring, bug tracker, design system, status page/comm channels.
## Zależności dokumentu
Wymaga: listy krytycznych flow, standardów A11y, narzędzi skanowania, kanałów komunikacji, SLAs dla napraw. Braki = DoR otwarte.
## Fazy cyklu życia
- Konfiguracja monitoringu i scope.  
- Ciągłe skanowanie i testy manualne w rytmie release.  
- Triage, naprawa, retest i raportowanie.  
- Przeglądy okresowe i aktualizacja narzędzi/scope.
## Struktura sekcji (szkielet)

- Kontekst i SLO
- Typy alertów i triage
- Checklista diagnostyczna
- Eskalacje/komunikacja
- Rollforward/rollback
- Raportowanie/postmortem


## Szybkie powiązania
- runbook-monitorowania-api
- performance-monitoring-runbook
- model-monitoring-runbook
- integration-monitoring-runbook
- database-monitoring-runbook

## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **CIS Controls v8** — Krytyczne Mechanizmy Bezpieczeństwa (CIS)
- **ISO/IEC 12207** — Procesy Cyklu Życia Oprogramowania
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

- Wypełnij sekcje według szkieletu; jeśli sekcja N/A, uzasadnij.
- Dodaj quick-links i uzupełnij checklisty DoR/DoD w reports/checklist_atomic.jsonl.
- Po review zaktualizuj metadane, artefakty i status.


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
- VPAT/ACR: raport dostępności dla klientów/regulatorów.  
- P1/P2/P3: priorytety napraw A11y (blokujące/krytyczne/ważne).  
- Focus management: poprawne prowadzenie focusu klawiatury.
## Przykłady użycia
- Regresja kontrastu w checkout → alert, triage P1, hotfix, retest.  
- Nowy release: skan CI + manual AT na krytycznych flow.  
- Przygotowanie VPAT dla klienta public sector.
## Ryzyka i ograniczenia
- Tylko automatyczne skany → brak pokrycia AT/UX.  
- Brak SLA → defekty A11y zalegają.  
- Niewystarczająca komunikacja → klienci nie znają ograniczeń/waiverów.
## Decyzje i uzasadnienia
- Częstotliwość skanów i zestaw narzędzi.  
- Priorytety P1/P2/P3 i SLA.  
- Zakres publikacji VPAT/ACR.
## Powiązania z innymi dokumentami
- accessibility_compliance — wymagania i checklisty.  
- design_system_guidelines — komponenty A11y.  
- communication_plan — komunikaty o statusie A11y.
## Powiązania z sekcjami innych dokumentów

- [Dokument X → Sekcja Y] — [powód powiązania i kierunek przepływu informacji]
- [Dokument Z → Sekcja W] — [powód powiązania i kierunek przepływu informacji]

## Słownik pojęć w dokumencie

- [Pojęcie 1] — [definicja i źródło normalizacyjne lub wewnętrzne]
- [Pojęcie 2] — [definicja i źródło normalizacyjne lub wewnętrzne]

## Wymagane odwołania do standardów
- WCAG 2.1 AA (lub nowsze), EN 301 549, ADA (jeśli dotyczy).  
- Wewnętrzne standardy A11y i bezpieczeństwa danych.
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

- Alerty i dashboardy
- SLO/SLA i progi
- Runbooki incydentów/gateway
- Lista ownerów i kanałów komunikacji


## Wyjścia

- Procedura triage per typ alertu
- Checklista diagnostyczna
- Ścieżki eskalacji i komunikacji
- Powiązania do postmortem



## Szybkie powiązania (uzupełnij)

- [ ] api_outage_response.md
- [ ] api_gateway_operations_runbook.md
- [ ] api_error_rate_monitoring.md
- [ ] api_response_time_monitoring.md
- [ ] security_incident_response.md
- [ ] api_incident_postmortem.md


## Wymagane rozwinięcia / streszczenia

- Streszczenie kluczowych decyzji/ryzyk; rozwinięcia polityk/limitów/testów.


## Wymagane powiązania

- Dokumenty gateway/security/rate limiting/monitoring/testy; runbooki incydentów.


## Kryteria DoR

- [ ] SLO/progi znane
- [ ] Alerty i dashboardy zmapowane
- [ ] Ownerzy/eskalacje ustalone
- [ ] Kanały komunikacji gotowe


## Kryteria DoD

- [ ] Procedury triage spisane
- [ ] Checklisty dodane
- [ ] Powiązania/quick-links uzupełnione
- [ ] Metadane zaktualizowane


## Artefakty do załączenia

- Runbook alertów
- Checklista diagnostyczna
- Mapa eskalacji
- Linki do postmortem


## Walidacja / testy

- Sanity/regresje na krytycznych endpointach; weryfikacja alertów/limitów/logów.


## Metryki monitorowane

- MTTA/MTTR alertów
- Alert FP rate
- Liczba eskalacji
- Czas komunikatu status


## Utrzymanie i aktualizacje

- Przegląd co release lub przy zmianie polityk/konfiguracji.


## Zakończenie

Po spełnieniu DoD zaktualizuj status, podlinkuj artefaty/quick-links i odhacz checklistę w reports/checklist_atomic.jsonl.
