---
title: Technology Stack Training
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Technology Stack Training


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Program szkolenia z firmowego stacku technologicznego (frontend/backend/data/cloud). Ma skrócić ramp‑up, ujednolicić praktyki i zwiększyć jakość delivery.


## Zakres i granice

- Obejmuje: przegląd architektury, języki/frameworki, standardy kodu/testów/CI-CD, observability, bezpieczeństwo (IAM/secret/PII), dane (DB, cache, messaging), IaC/deploy, narzędzia deweloperskie, A11y/UX (frontend), procedury on-call.  
- Poza zakresem: ogólne kursy CS (algorytmy itp.).


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia

- Wejścia: opis architektury, standardy kodu, runbooki, narzędzia, przykładowe projekty, wymagania bezpieczeństwa, syllabus L&D.  
- Wyjścia: sylabus i materiały (slajdy, laby), checklisty DoR/DoD, lab repos, oceny (quiz/praktyka), harmonogram i lista uczestników, wyniki ewaluacji.


## Założenia

- Dostępne środowiska i narzędzia.  
- Budżet na trenerów/czas.  
- Zespoły mają czas na udział.


## Otwarte pytania

- Jak mierzyć wpływ na velocity/quality?  
- Jakie moduły obowiązkowe vs opcjonalne?  
- Jak często aktualizować sylabus?


## Powiązania (meta)

- Key Documents: coding_guidelines, observability_plan, security_requirements, ci_cd_standards, architecture_vision, onboarding_engineer, on_call_training.  
- Key Document Structures: architektura, kod/testy, deploy/IaC, security, data, tools, ewaluacja.  
- Document Dependencies: repos, CI/CD, cloud accounts/sandboxes, monitoring, LMS.


## Zależności dokumentu

Wymaga: aktualnych standardów kodu/CI-CD/security, dostępu do repo i sandboxes, materiałów architektonicznych, listy trenerów i uczestników, LMS. Braki = DoR otwarte.


## Fazy cyklu życia

- Przygotowanie materiałów i labów.  
- Szkolenia i oceny.  
- Ewaluacja i iteracje.  
- Odświeżenia cykliczne przy zmianie stacku.



## Struktura sekcji (szkielet)
- Cele szkolenia i oczekiwane rezultaty
- Grupa docelowa/persony i wymagania wstępne
- Moduły/agenda z czasem i formą (teoria/lab)
- Materiały i środowisko (lab/demo)
- Ćwiczenia/prace domowe i kryteria zaliczenia
- Ocena postępów (quiz/lab/egzamin) i feedback
- Plan komunikacji/mentoringu i utrzymania materiałów
## Szybkie powiązania

- linkage_index.jsonl (technology/stack/training)  
- coding_guidelines, observability_plan, security_requirements, ci_cd_standards


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **ISO/IEC 23053** — Framework dla Systemów AI z Uczeniem Maszynowym
- **ISO/IEC 42001** — System Zarządzania Sztuczną Inteligencją (AIMS)
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

1. Przygotuj sylabus/laby i dostęp do środowisk.  
2. Przeprowadź szkolenia; oceń wiedzę; zbierz feedback.  
3. Aktualizuj materiały i linkage_index; odnotuj DoR/DoD.


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

- IaC: Infrastructure as Code.  
- NPS: Net Promoter Score.  
- Sandboxes: izolowane środowiska treningowe.


## Przykłady użycia

- Onboarding nowych inżynierów.  
- Migracja stacku (np. monolit → microservices).  
- Program upskilling dla zespołów legacy.


## Ryzyka i ograniczenia

- Brak dostępu do narzędzi → słaba efektywność.  
- Nieaktualne materiały → złe praktyki.  
- Niska frekwencja → niewielki efekt.


## Decyzje i uzasadnienia

- Format (self‑paced vs live).  
- Zakres labów vs czas.  
- Kryteria zaliczenia i certyfikacji.


## Powiązania z innymi dokumentami

- onboarding_engineer — plan startowy.  
- on_call_training — operacje.  
- security_requirements — bezpieczeństwo.


## Powiązania z sekcjami innych dokumentów

- [Dokument X → Sekcja Y] — [powód powiązania i kierunek przepływu informacji]
- [Dokument Z → Sekcja W] — [powód powiązania i kierunek przepływu informacji]

## Słownik pojęć w dokumencie

- [Pojęcie 1] — [definicja i źródło normalizacyjne lub wewnętrzne]
- [Pojęcie 2] — [definicja i źródło normalizacyjne lub wewnętrzne]

## Wymagane odwołania do standardów

- Wewnętrzne standardy kodu/CI/CD/security/observability.  
- Polityki PII/RODO jeśli obejmuje dane.

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

- Architektura → Kod/standardy → Deploy/IaC → Observability/on-call.  
- Security → CI/CD → Deploy/ops.  
- Laby → Oceny → Ewaluacja/udoskonalenia.


## Struktura sekcji

1) Cele szkolenia i grupa docelowa  
2) Architektura i przegląd systemu  
3) Języki/frameworki i standardy kodu/testów  
4) CI/CD i IaC (pipelines, deployments, feature flags)  
5) Observability i on-call (metryki/logi/traces, alerty, runbooki)  
6) Bezpieczeństwo (IAM, secrets, PII, dependency scanning)  
7) Dane (DB, cache, queues, schema migration)  
8) Narzędzia dev (IDE, linters, formatters, local env)  
9) Laby, oceny i certyfikacja  
10) Ryzyka, decyzje, otwarte pytania


## Wymagane rozwinięcia

- Sylabus modułów i czas; laby per domena.  
- Checklista środowiska lokalnego i dostępów.  
- Quiz/praktyka i rubryka ocen.  
- Plan aktualizacji materiałów (release train).


## Wymagane streszczenia

- One‑pager: cele, moduły, terminy, prerekwizyty.  
- Snapshot wyników: frekwencja, zdawalność, NPS.


## Guidance (skrót)

- Ucz na realnych repo i case’ach; automatyzuj laby.  
- Wbuduj security/observability w każdy moduł.  
- Sprawdzaj prerekwizyty i dostęp do narzędzi przed startem.  
- Zbieraj feedback po każdej sesji; iteruj materiały.  
- Odświeżaj przy zmianie stacku (releases).


## Checklisty Definition of Ready (DoR)

- [ ] Standardy kodu/CI-CD/security aktualne.  
- [ ] Repo/laby i sandboxes gotowe.  
- [ ] Trenerzy i terminy potwierdzeni; LMS skonfigurowany.  
- [ ] Prerekwizyty/instalacje zakomunikowane.  
- [ ] Rubryka ocen przygotowana.


## Checklisty Definition of Done (DoD)

- [ ] Sesje przeprowadzone; frekwencja/wyniki zapisane; status/wersja/data uzupełnione.  
- [ ] Materiały/laby zaktualizowane wg feedbacku.  
- [ ] Certyfikacje/badges wydane (jeśli dotyczy); linkage_index uzupełniony.  
- [ ] Plan kolejnego odświeżenia ustalony.  
- [ ] Ryzyka/lessons learned zapisane.

