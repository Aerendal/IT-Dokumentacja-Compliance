---
title: Product Operations Runbook
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Product Operations Runbook


## Metadane

- Właściciel: DevOps Engineer
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Runbook dla operacji produktowych: rytuały, raportowanie, zmiany, incydenty, komunikacja z klientami i zespołami. Ma zapewnić spójne działanie i szybkie reagowanie na problemy produktowe.


## Zakres i granice

- Obejmuje: governance backlogu, release cadence, feature flags, raporty (biz/dev/CS), monitorowanie KPI, obsługę incydentów produktowych, komunikację (changelog/status), feedback loop, eksperymenty/A-B, eskalacje do inżynierii/CS, zgodność (privacy/terms), narzędzia (ticketing/analytics).  
- Poza zakresem: szczegółowe runbooki techniczne SRE (oddzielne dokumenty).


## Użytkownicy i interesariusze
- IT Ops/SRE, Security/Compliance, Klinicyści/SME, Vendorzy, Service Desk.
## Wejścia i wyjścia

- Wejścia: roadmapa, backlog, metryki produktowe, status release, alerty/incidenty, feedback klientów, polityki komunikacji i privacy.  
- Wyjścia: plan operacyjny (tydzień/kwartał), statusy release, raporty KPI, decyzje go/no-go, komunikaty do klientów, retrospektywy, akcje z feedbacku, aktualizacje linkage_index i DoR/DoD.


## Założenia

- Dane KPI są mierzalne i dostępne.  
- Zespoły mają przypisane role w incydentach.  
- Narzędzia analytics/ticketing są zintegrowane.


## Otwarte pytania

- Czy potrzebne są osobne runbooki per produkt/region?  
- Jakie są wymagania prawne dot. komunikacji incydentów w danej branży?  
- Jak długo przechowywać dane w raportach (privacy)?


## Powiązania (meta)

- Key Documents: release_plan, incident_response_runbook, change_management_policy, communication_plan, experimentation_framework, privacy_and_terms_policy.  
- Key Document Structures: rytuały, monitoring, raporty, komunikacja, incydenty, eskalacje, eksperymenty.  
- Document Dependencies: ticketing/ALM, analytics/BI, feature flag system, status page, support/CS tools.


## Zależności dokumentu

Wymaga: ustalonego rytmu release, listy KPI, narzędzi analitycznych i ticketowych, polityk komunikacji/PR/privacy, procedur incident/CS. Braki = DoR otwarte.


## Fazy cyklu życia

- Planowanie operacji (tygodniowe/kwartalne).  
- Wykonanie: release, monitoring, komunikacja, obsługa incydentów.  
- Retrospektywy i doskonalenie procesów.



## Struktura sekcji (szkielet)

- Warunki wstępne i wymagania
- Kroki wykonania (krok po kroku)
- Weryfikacja poprawności
- Kroki rollback
- Typowe problemy i rozwiązania
- Log akcji

## Szybkie powiązania

- linkage_index.jsonl (product/operations/runbook)  
- release_plan, incident_response_runbook, communication_plan, experimentation_framework, privacy_and_terms_policy


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **PMBOK 7** — Przewodnik po Zarządzaniu Projektami (PMI)
- **SCRUM Guide** — Przewodnik Scrum

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

1. Ustal rytuały i odpowiedzialności; wypełnij szablony raportów.  
2. Prowadź release/monitoring/komunikację wg planu; loguj decyzje i incydenty.  
3. Aktualizuj DoR/DoD, linkage_index i backlog działań po retro.


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

- Product incident: zdarzenie pogarszające KPI/CSAT lub powodujące błędne działanie funkcji.  
- Go/No-Go: decyzja o wypuszczeniu releasu/feature.  
- Status page: publiczny lub prywatny kanał komunikacji o stanie usługi.


## Przykłady użycia

- Tygodniowy rytuał product ops z KPI i statusami release.  
- Obsługa incydentu „checkout failure spike” z komunikacją do klientów.  
- Retro po zakończonym kwartale i aktualizacja procesów.


## Ryzyka i ograniczenia

- Brak spójnej komunikacji → chaos u klientów/zespołów.  
- Niespinanie release z monitorowaniem → późne wykrycie regresji.  
- Brak follow‑up z retro → stagnacja procesu.


## Decyzje i uzasadnienia

- Kadencja raportów (tydzień/kwartał).  
- Kryteria go/no-go i required evidence.  
- Standard kanałów komunikacji (statuspage, e-mail, in-app).


## Powiązania z innymi dokumentami

- communication_plan — szczegóły komunikacji.  
- experimentation_framework — proces A/B.  
- incident_response_runbook — eskalacje techniczne.


## Powiązania z sekcjami innych dokumentów
- Privacy/Security → IAM/logi/szyfrowanie.
- HL7/FHIR Integration → Monitoring i testy interface’ów.
## Słownik pojęć w dokumencie
- EHR/EMR, PACS, LIS, RIS, HL7, FHIR, CAB, RTO/RPO.
## Wymagane odwołania do standardów

- Polityki privacy/terms, wewnętrzne standardy komunikacji i status page.  
- Regulacje branżowe, jeśli dotyczy (np. fintech/health).

## Mapa relacji sekcja→sekcja
- Inwentarz → Monitoring/Backup/DR → Incydenty/Downtime → Audyt.
## Mapa relacji dokument→dokument
- Healthcare IT Ops Runbook → Incident Response → Change Mgmt → Audit/Compliance.
## Ścieżki informacji
- Alert/Incydent → Triage/Eskalacja → Komunikacja → Mitigacja → Walidacja kliniczna → Postmortem.
- Zmiana/Patch → CAB → Wdrożenie → Walidacja → Dokumentacja/audyt.
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
- Dashboardy, harmonogramy patch/backup, szablony komunikatów, listy kontaktów, logi audytu.
## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji
- IT Ops → Security/Compliance → Klinika → CAB/Owner sign‑off.
## Metryki jakości
- Dostępność (SLA), liczba incydentów klinicznych, czas reakcji/naprawy, sukces testów DR, wskaźniki audytu (log completeness, access recertification), defekty po patchach.
## Kryteria ukończenia
- [ ] Harmonogramy, playbooki i kontakty kompletne.
- [ ] Dowody backup/DR/testów dostępne.
- [ ] Dokument powiązany w linkage_index.jsonl i checklistach.
## Powiązania sekcja↔sekcja

- Monitoring KPI → Raporty → Decyzje go/no-go → Komunikacja.  
- Incydenty → Eskalacja → Komunikaty → Retrospektywa.  
- Eksperymenty → Wyniki → Backlog/roadmapa.


## Struktura sekcji

1) Kontekst i cele operacji produktowych  
2) Rytuały i kalendarz (planning, review, release, retro)  
3) Monitoring i raportowanie KPI (biz/tech/CS)  
4) Release management i feature flags (go/no-go, checklists)  
5) Incydenty produktowe i eskalacje (role, kanały, SLA)  
6) Komunikacja z klientami i zespołami (changelog/status/CS)  
7) Feedback i eksperymenty (A/B, wynik, decyzje)  
8) Zgodność/privacy i ryzyka  
9) Narzędzia i dostęp (ticketing, analytics, status page)  
10) Ryzyka, decyzje, otwarte pytania


## Wymagane rozwinięcia

- Harmonogram rytuałów i właściciele.  
- Szablon raportu KPI i statusu release.  
- Playbook incydentu produktowego (SLA, kanały, message templates).  
- Szablon komunikatu klienta (statuspage/email/in-app).


## Wymagane streszczenia

- Tygodniowy/kwartalny snapshot: status release, KPI, incydenty, decyzje.  
- Krótka karta go/no-go dla releasu.


## Guidance (skrót)

- Synchronizuj product ops z SRE/CS; jedna prawda o statusie.  
- Standaryzuj komunikaty (co, kogo dotyczy, ETA, obejścia).  
- Mierz wpływ zmian i incydentów na KPI i CSAT.  
- Utrzymuj backlog akcji z retrospektyw i feedbacku z datami.  
- Dbaj o privacy/compliance w raportach i komunikacji.


## Checklisty Definition of Ready (DoR)

- [ ] Roadmapa i rytm release znane; KPI zdefiniowane.  
- [ ] Kanały komunikacji i szablony przygotowane.  
- [ ] Narzędzia (ticketing/analytics/status) dostępne.  
- [ ] Role/eskalacje i SLA incydentów ustalone.  
- [ ] Zasady privacy/compliance w komunikacji uzgodnione.


## Checklisty Definition of Done (DoD)

- [ ] Raporty/KPI i status release opublikowane; linki działają.  
- [ ] Incydenty obsłużone wg SLA; komunikaty wysłane; retro zapisane.  
- [ ] Decyzje go/no-go i flagi udokumentowane; status/wersja/data uzupełnione.  
- [ ] Backlog akcji z retro/feedbacku zaktualizowany; linkage_index uzupełniony.  
- [ ] Ryzyka/compliance w komunikacji zreviewowane.

