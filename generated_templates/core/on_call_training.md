---
title: On-Call Training
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# On-Call Training


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Program szkolenia dyżurujących (on-call): procedury, narzędzia, komunikacja, bezpieczeństwo i wellbeing. Celem jest skrócenie MTTR, poprawa jakości reakcji i zmniejszenie stresu.


## Zakres i granice

- Obejmuje: rolę on-call, kryteria eskalacji, runbooki, monitoring/alerty, narzędzia (pager/chat/ticketing), bezpieczeństwo (dostępy, PII), komunikację (status, klient), ćwiczenia (game day), raportowanie i retro, wellbeing (rotacje, zmiany, handover).  
- Poza zakresem: pełne procedury IR (linkowane), polityki HR.


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia

- Wejścia: matryca on-call, runbooki, SLO/SLA, narzędzia monitoringu, polityki bezpieczeństwa, harmonogramy, przykładowe incydenty, komunikacja klientów.  
- Wyjścia: sylabus szkoleń, checklisty DoR/DoD, playbooki, plan ćwiczeń, raporty z ewaluacji, poprawki runbooków.


## Założenia

- Narzędzia i logi dostępne.  
- Zespół akceptuje zasady wellbeing.  
- SLO/SLA są zdefiniowane.


## Otwarte pytania

- Jak obsłużyć różne strefy czasowe?  
- Jak mierzyć sukces (MTTR, customer impact)?  
- Czy potrzebny pageduty/inna platforma?


## Powiązania (meta)

- Key Documents: incident_response_runbook, escalation_procedure_design, communication_plan, access_control_policy, observability_plan, game_day_plan.  
- Key Document Structures: rola, narzędzia, alerty, eskalacje, komunikacja, ćwiczenia, wellbeing.  
- Document Dependencies: monitoring/alerting, pager/chat, ticketing, CMDB, runbook repo.


## Zależności dokumentu

Wymaga: aktualnej matrycy on-call, runbooków i SLO, narzędzi monitoringu/pagera, polityk dostępu i komunikacji, harmonogramów rotacji. Braki = DoR otwarte.


## Fazy cyklu życia

- Przygotowanie materiałów i narzędzi.  
- Szkolenia i ćwiczenia (dry-run, game day).  
- Dyżury i operacje.  
- Retro/ewaluacja i iteracje.



## Struktura sekcji (szkielet)
- Cele szkolenia i oczekiwane rezultaty
- Grupa docelowa/persony i wymagania wstępne
- Moduły/agenda z czasem i formą (teoria/lab)
- Materiały i środowisko (lab/demo)
- Ćwiczenia/prace domowe i kryteria zaliczenia
- Ocena postępów (quiz/lab/egzamin) i feedback
- Plan komunikacji/mentoringu i utrzymania materiałów
## Szybkie powiązania

- linkage_index.jsonl (on_call/training)  
- incident_response_runbook, escalation_procedure_design, communication_plan, observability_plan


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **ISO 20000-1** — System Zarządzania Usługami IT (SMS)
- **ISO/IEC 23053** — Framework dla Systemów AI z Uczeniem Maszynowym
- **ISO/IEC 42001** — System Zarządzania Sztuczną Inteligencją (AIMS)
- **ITIL 4** — Biblioteka Infrastruktury IT (Zarządzanie Usługami)
- **NIST CSF** — Framework Cyberbezpieczeństwa NIST

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

1. Przygotuj szkolenie, dostępy i runbooki.  
2. Przeprowadź ćwiczenia; oceń i popraw.  
3. Monitoruj metryki on-call; iteruj proces i linkage_index.


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
- Alert fatigue: przeciążenie liczbą alertów.  
- Game day: ćwiczenie symulujące awarie.


## Przykłady użycia

- Szkolenie nowych SRE przed dołączeniem do rotacji.  
- Game day dla usługi krytycznej.  
- Retro po serii nocnych alertów.


## Ryzyka i ograniczenia

- Brak ćwiczeń → słaba reakcja.  
- Za dużo alertów → burnout/fatigue.  
- Nieaktualne runbooki → dłuższy MTTR.


## Decyzje i uzasadnienia

- Częstotliwość game day.  
- Limity alertów/osoba i rotacje.  
- Zakres uprawnień na dyżurach.


## Powiązania z innymi dokumentami

- escalation_procedure_design — ścieżki eskalacji.  
- communication_plan — komunikaty.  
- observability_plan — alerty.


## Powiązania z sekcjami innych dokumentów

- [Dokument X → Sekcja Y] — [powód powiązania i kierunek przepływu informacji]
- [Dokument Z → Sekcja W] — [powód powiązania i kierunek przepływu informacji]

## Słownik pojęć w dokumencie

- [Pojęcie 1] — [definicja i źródło normalizacyjne lub wewnętrzne]
- [Pojęcie 2] — [definicja i źródło normalizacyjne lub wewnętrzne]

## Wymagane odwołania do standardów

- Wewnętrzne polityki bezpieczeństwa i dostępu, PII.  
- Standardy SRE/ITIL jeśli przyjęte.

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

- Alerty → Eskalacja → Komunikacja → Postmortem.  
- Handover → Jakość reakcji → Wellbeing.  
- Ćwiczenia → Poprawa runbooków → Skrócenie MTTR.


## Struktura sekcji

1) Cel i zakres on-call  
2) Rola i odpowiedzialności, RACI  
3) Narzędzia i dostępy (pager, chat, ticketing, CMDB, logi)  
4) Alerty/SLO/SLA i kryteria eskalacji  
5) Komunikacja (wewnętrzna/zewnętrzna, status page, klient)  
6) Runbooki i playbooki (linki, aktualizacje)  
7) Ćwiczenia i game days (plan, częstotliwość)  
8) Wellbeing i rotacje (handover, zmiany, limit alertów)  
9) Raportowanie i retro (postmortem, poprawki)  
10) Ryzyka, decyzje, otwarte pytania


## Wymagane rozwinięcia

- Plan szkolenia (agenda, laby), lista runbooków krytycznych.  
- Szablon handover i komunikatów status.  
- Harmonogram game day i checklisty.  
- Metryki (MTTA/MTTR, alert fatigue) i progi.


## Wymagane streszczenia

- One‑pager: „jak reagować na alert” + kontakty.  
- Snapshot metryk on-call (MTTR, alerty/osoba, fatigue).


## Guidance (skrót)

- Ucz na realnych narzędziach i danych.  
- Ustal jasne progi eskalacji i komunikacji.  
- Dbaj o wellbeing: rotacje, quiet hours, load balancing.  
- Aktualizuj runbooki po każdym incydencie i ćwiczeniu.  
- Mierz MTTR/MTTA i redukuj alert noise.


## Checklisty Definition of Ready (DoR)

- [ ] Matryca on-call i runbooki dostępne.  
- [ ] Narzędzia (pager/chat/ticketing/logi) skonfigurowane.  
- [ ] SLO/SLA i kryteria eskalacji znane.  
- [ ] Plan szkolenia/ćwiczeń ustalony.  
- [ ] Polityki dostępu/PII potwierdzone.


## Checklisty Definition of Done (DoD)

- [ ] Szkolenia/ćwiczenia wykonane; wyniki/feedback zapisane; status/wersja/data uzupełnione.  
- [ ] Runbooki zaktualizowane; wnioski z retro wdrożone.  
- [ ] Metryki on-call monitorowane; plany poprawy opisane.  
- [ ] Linkage_index uzupełniony; ryzyka/dec. udokumentowane.  
- [ ] Wellbeing (rotacje/limity) potwierdzone z zespołem.

