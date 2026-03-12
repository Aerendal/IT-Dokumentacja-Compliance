---
title: Escalation Procedure Design
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Escalation Procedure Design


## Metadane

- Właściciel: Technical Writer
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Definiuje procedurę eskalacji dla incydentów/problemów/zapytań: kiedy eskalować, do kogo, jakimi kanałami i z jakimi wymaganymi informacjami. Ma skrócić czas reakcji i zwiększyć skuteczność rozwiązywania.


## Zakres i granice

- Obejmuje: kryteria eskalacji (severity/impact/urgency), ścieżki (techniczne, produktowe, biznesowe, klient), kanały (pager/chat/phone/email/ticket), RACI, SLA/OLA, szablony komunikacji, hand‑off między zespołami, wymagane dane (summary, timeline, logs), monitoring i audyt eskalacji, ciągłe doskonalenie.  
- Poza zakresem: szczegółowe runbooki techniczne (są w innych dokumentach), polityki personalne.


## Użytkownicy i interesariusze
- **Technical Writer / Documentation Owner** — tworzy i utrzymuje dokumentację
- **Subject Matter Expert (SME)** — dostarcza merytoryczne treści i weryfikuje poprawność
- **Development Team** — recenzuje dokumentację techniczną
- **End Users** — korzystają z dokumentacji i zgłaszają nieścisłości

## Wejścia i wyjścia

- Wejścia: katalog usług i właścicieli, klasyfikacja incydentów, SLA/OLA, polityki komunikacji, narzędzia on‑call/ticketing, logi/monitoring, lessons learned.  
- Wyjścia: matryca eskalacji, playbook krok‑po‑kroku, szablony komunikacji, listy kontrolne DoR/DoD, metryki (MTTA/MTTR/escape), raporty eskalacji i poprawki procesu.


## Założenia

- Monitoring/alerting istnieje i jest zintegrowany z pagerem.  
- Kanały komunikacji są dostępne i ćwiczone.  
- Organizacja akceptuje audyt eskalacji.


## Otwarte pytania

- Czy potrzebne są różne ścieżki dla regionów/produktów?  
- Jakie SLA/OLA wymagają klienci?  
- Jak mierzyć skuteczność eskalacji (escape rate, satisfaction)?


## Powiązania (meta)

- Key Documents: incident_response_runbook, communication_plan, service_catalog, risk_register, customer_support_playbook, change_management_policy.  
- Key Document Structures: kryteria, ścieżki, kanały, RACI, komunikacja, SLA, audyt.  
- Document Dependencies: on‑call rota, ticketing, paging/chat tools, CMDB/service catalog, monitoring/alerting.


## Zależności dokumentu

Wymaga: aktualnej matrycy właścicieli/on‑call, SLA/OLA, narzędzi komunikacji i ticketingu, klasyfikacji incydentów, polityk komunikacji i risk register. Braki = DoR otwarte.


## Fazy cyklu życia

- Definicja i publikacja procedury.  
- Szkolenia i dry‑runy.  
- Operacje i audyt eskalacji.  
- Przeglądy i doskonalenie.



## Struktura sekcji (szkielet)
- Cel, zakres i definicje sukcesu
- Trigger/scenariusze i preconditions
- Role, uprawnienia i narzędzia
- Kroki operacyjne (checklista) z walidacją
- Monitoring i dowody wykonania
- Rollback/contingency oraz komunikacja/escalacja
- Rejestr zmian runbooka
## Szybkie powiązania

- linkage_index.jsonl (escalation/procedure/design)  
- incident_response_runbook, communication_plan, service_catalog, risk_register


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **IEEE 1016** — Standard dla Opisów Projektowania Oprogramowania (SDD)
- **IEEE 42010** — Opis Architektoniczny Systemów i Oprogramowania
- **ISO 20000-1** — System Zarządzania Usługami IT (SMS)
- **ISO/IEC 15288** — Procesy Cyklu Życia Systemów
- **ITIL 4** — Biblioteka Infrastruktury IT (Zarządzanie Usługami)
- **TOGAF ADM** — Framework Architektury Korporacyjnej (The Open Group)

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

1. Ustal kryteria i matrycę; opublikuj cheat‑sheet.  
2. W incydencie stosuj playbook i szablony; loguj dane i decyzje.  
3. Po incydencie audytuj eskalacje, aktualizuj DoR/DoD i linkage_index.


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

- MTTA/MTTR: Mean Time To Acknowledge/Resolve.  
- Escape: incydent wykryty przez klienta zamiast monitoringu.  
- Duty manager: rola koordynatora eskalacji.


## Przykłady użycia

- Eskalacja krytycznego incydentu produkcyjnego.  
- Eskalacja problemu klienta enterprise do warstwy produktowej/exec.  
- Dry‑run procedury przed sezonem szczytu.


## Ryzyka i ograniczenia

- Niejasne kryteria → over/under‑escalation.  
- Brak danych przy eskalacji → wolne decyzje.  
- Nieaktualne on‑call → „dead pager”.


## Decyzje i uzasadnienia

- Progi severity i kanały (pager/chat/voice).  
- Kto wysyła komunikaty zewnętrzne i kiedy.  
- Jakie dane są wymagane minimalnie przy eskalacji.


## Powiązania z innymi dokumentami

- incident_response_runbook — działania techniczne.  
- communication_plan — komunikaty.  
- risk_register — ryzyka z eskalacji.


## Powiązania z sekcjami innych dokumentów

- [Dokument X → Sekcja Y] — [powód powiązania i kierunek przepływu informacji]
- [Dokument Z → Sekcja W] — [powód powiązania i kierunek przepływu informacji]

## Słownik pojęć w dokumencie

- [Pojęcie 1] — [definicja i źródło normalizacyjne lub wewnętrzne]
- [Pojęcie 2] — [definicja i źródło normalizacyjne lub wewnętrzne]

## Wymagane odwołania do standardów

- Wewnętrzne polityki incident/change i komunikacji.  
- Wymogi klientów/regulatorów jeśli dotyczy.

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

## Powiązania sekcja↔sekcja

- Kryteria severity → Ścieżki eskalacji → Komunikacja → Decyzje.  
- Wymagane dane → Skuteczność eskalacji → MTTR.  
- Lessons learned → Ulepszenie kryteriów/ścieżek.


## Struktura sekcji

1) Zakres i cele procedury  
2) Kryteria eskalacji (severity/impact/urgency)  
3) Ścieżki i kanały (techniczne/produktowe/biznesowe/klient)  
4) RACI i właściciele (on‑call, duty manager, exec)  
5) Wymagane dane przy eskalacji (summary, timeline, logi, decyzje)  
6) Komunikacja i szablony (internal/external, status page)  
7) SLA/OLA i metryki (MTTA/MTTR/escape)  
8) Audyt i ciągłe doskonalenie (postmortem, KPI procesu)  
9) Ryzyka, decyzje, otwarte pytania


## Wymagane rozwinięcia

- Matryca eskalacji (severity × ścieżka × owner × kanał).  
- Szablony komunikacji (alert, update, closure) i checklista danych.  
- Procedura hand‑off (co przekazać, kiedy, komu).  
- Metryki procesu i dashboard.


## Wymagane streszczenia

- Jednostronicowy cheat‑sheet eskalacji.  
- Executive snapshot: liczba eskalacji, MTTA/MTTR, top przyczyny, escape rate.


## Guidance (skrót)

- Jasne kryteria i minimalne dane przy eskalacji; inaczej hałas.  
- Używaj jednego kanału głównego + backup; unikaj chaosu komunikacyjnego.  
- Eskalacje audytuj i włączaj do postmortem.  
- Aktualizuj matrycę on‑call i kanały; przetestuj dry‑runami.  
- Miej ścieżkę klient/PR, jeśli incydent wpływa na użytkowników.


## Checklisty Definition of Ready (DoR)

- [ ] Matryca on‑call/ownerów aktualna.  
- [ ] Kryteria severity/impact/urgency zdefiniowane.  
- [ ] Kanały i szablony komunikacji przygotowane.  
- [ ] SLA/OLA i metryki procesu ustalone.  
- [ ] Narzędzia ticketing/pager działają.


## Checklisty Definition of Done (DoD)

- [ ] Eskalacje wykonane zgodnie z matrycą; dane/logi zapisane.  
- [ ] Komunikaty wysłane; status/wersja/data uzupełnione.  
- [ ] Metryki (MTTA/MTTR/escape) zebrane; raport procesu.  
- [ ] Lessons learned i poprawki procedury zapisane; linkage_index zaktualizowany.  
- [ ] RACI i on‑call zrewidowane po incydencie jeśli potrzebne.

