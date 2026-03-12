---
title: Security Tools Training
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Security Tools Training


## Metadane

- Właściciel: Security Officer
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved
- Repo / moduł: [link]


## Cel dokumentu

Szkolenie praktyczne z narzędzi bezpieczeństwa (SIEM, EDR, skanery, secret/IaC/SAST/DAST, SOAR) z labami i oceną.


## Zakres i granice

- Obejmuje: grupy docelowe, cele i moduły, środowiska/laby, dane testowe, uprawnienia, ćwiczenia i kryteria zaliczenia, metryki skuteczności.
- Poza zakresem: pełna konfiguracja produkcyjna narzędzi (oddzielne runbooki/implementation guides).


## Użytkownicy i interesariusze
- **CISO / Security Officer** — odpowiada za strategię bezpieczeństwa i akceptuje dokument
- **Security Engineer** — implementuje mechanizmy ochronne i przeprowadza testy
- **Compliance Officer** — weryfikuje zgodność z regulacjami (ISO 27001, RODO, NIS2)
- **DevOps / Platform Team** — wdraża zmiany infrastrukturalne wynikające z zaleceń

## Wejścia i wyjścia
- Wejścia: katalog usług/stacków, standardy performance, narzędzia dostępne w org, przykładowe incydenty, polityki dostępu do prod, budżet czasowy szkolenia.  
- Wyjścia: sylabus i laboratoria, instrukcje „how-to”, scenariusze ćwiczeń, checklisty DoR/DoD, wyniki ewaluacji (quiz/praktyka), lista usprawnień narzędzi.
## Założenia
- Środowiska lab/stage dostępne i zbliżone do prod.  
- Organizacja ma polityki prod-safe/PII.  
- Zespoły mają czas na udział w szkoleniu.
## Otwarte pytania
- Czy potrzebna certyfikacja formalna?  
- Jak często odświeżać szkolenie?  
- Jak mierzyć wpływ szkolenia na MTTR/performance?
## Powiązania (meta)
- Key Documents: performance_engineering_guidelines, observability_plan, incident_response_runbook, security_requirements, onboarding_engineer.  
- Key Document Structures: narzędzia, scenariusze, ćwiczenia, bezpieczeństwo, ewaluacja.  
- Document Dependencies: dostęp do środowisk, uprawnienia, próbki aplikacji, monitoring/logi.
## Zależności dokumentu
Wymaga: listy narzędzi dostępnych w org, polityk dostępu do prod, przykładów incydentów performance, mentorów/trenerów, środowisk lab/stage. Braki = DoR otwarte.
## Fazy cyklu życia
- Przygotowanie sylabusa i labów.  
- Przeprowadzenie szkoleń/cykli.  
- Ewaluacja i doskonalenie materiałów.  
- Odświeżenie przy zmianie stacku/narzędzi.
## Struktura sekcji (szkielet)

- Cele i grupy docelowe
- Narzędzia i wymagania dostępu
- Moduły i scenariusze (detect/respond/scan)
- Środowisko i dane testowe (bezpieczeństwo danych!)
- Ćwiczenia/laby i kryteria zaliczenia
- Metryki, raportowanie i refresh


## Szybkie powiązania
- security-training
- security-policy-training
- security-awareness-training
- profiling-tools-training
- mlops-tools-training

## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **CIS Controls v8** — Krytyczne Mechanizmy Bezpieczeństwa (CIS)
- **ISO/IEC 23053** — Framework dla Systemów AI z Uczeniem Maszynowym
- **ISO/IEC 27001** — System Zarządzania Bezpieczeństwem Informacji (ISMS)
- **ISO/IEC 27002** — Wytyczne Praktyk Bezpieczeństwa Informacji
- **ISO/IEC 27005** — Zarządzanie Ryzykiem Bezpieczeństwa Informacji
- **ISO/IEC 42001** — System Zarządzania Sztuczną Inteligencją (AIMS)
- **NIST CSF** — Framework Cyberbezpieczeństwa NIST

### Polskie normy i regulacje
- **CERT-PL-WYTYCZNE** — Wytyczne CERT Polska (CSIRT NASK) dot. cyberbezpieczeństwa
- **KSC-PL** — Ustawa o Krajowym Systemie Cyberbezpieczeństwa

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

- Wybierz narzędzia i scenariusze, przygotuj konta/laby i dane testowe.
- Dodaj quick-links i checklisty DoR/DoD w `reports/checklist_atomic.jsonl`; sekcje N/A uzasadnij.
- Po szkoleniu uzupełnij wyniki/feedback, zaktualizuj materiały i metryki.


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
- Flamegraph: wizualizacja stosu CPU/Wall/Memory.  
- Prod-safe: zasady minimalizujące wpływ na produkcję.  
- Profiling sampling vs tracing: kompromis obciążenie vs szczegół.
## Przykłady użycia
- Warsztat „GC pause” dla JVM.  
- Profiling API latency (pprof) w Go.  
- Chrome DevTools dla front-end TTI/LCP.
## Ryzyka i ograniczenia
- Profiling na prod może degradować usługę.  
- Brak kompetencji → błędne wnioski z profili.  
- PII w zrzutach/profilach.
## Decyzje i uzasadnienia
- Które narzędzia standardowe w org na dany stack.  
- Poziom dostępu do prod dla uczestników.  
- Kryteria certyfikacji/zaliczenia.
## Powiązania z innymi dokumentami
- incident_response_runbook — profilowanie w incydentach.  
- performance_engineering_guidelines — zasady optymalizacji.  
- onboarding_engineer — plan dla nowych osób.
## Powiązania z sekcjami innych dokumentów

- [Dokument X → Sekcja Y] — [powód powiązania i kierunek przepływu informacji]
- [Dokument Z → Sekcja W] — [powód powiązania i kierunek przepływu informacji]

## Słownik pojęć w dokumencie

- [Pojęcie 1] — [definicja i źródło normalizacyjne lub wewnętrzne]
- [Pojęcie 2] — [definicja i źródło normalizacyjne lub wewnętrzne]

## Wymagane odwołania do standardów
- Wewnętrzne polityki prod access/PII.  
- Standardy językowe/stackowe dla narzędzi profilujących.
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

- Lista narzędzi i wersji, konta testowe/dostępy.
- Use-case’y (detect/respond/scan), playbooki, dane testowe.
- Wymagania compliance/danych (PII, logi produkcyjne – redakcja/anonymizacja).


## Wyjścia

- Sylabus i instrukcje labowe per narzędzie.
- Checklisty dostępu i bezpieczeństwa danych w labach.
- Quiz/ocena praktyczna, metryki ukończeń i skuteczności.



## Szybkie powiązania (uzupełnij)

- security_awareness_training.md
- security_tools_runbook.md
- security_operations_runbook.md
- security_incident_response.md
- devsecops_pipeline.md
- security_policy_training.md


## Wymagane rozwinięcia / streszczenia

- Scenariusze labów (kroki, expected results, dane testowe) per narzędzie.
- Rubryka oceny praktycznej.
- One-pager dla managerów: cele, czas, wymagania dostępu.


## Wymagane powiązania

- Runbooki operacyjne, polityki dostępu/logowania, zasady anonimizacji danych.
- Playbooki SOC/IR, pipeline CI/CD dla skanerów.


## Kryteria DoR

- [ ] Narzędzia i wersje wybrane, konta testowe dostępne.
- [ ] Dane testowe przygotowane, zasady PII/anonimizacji potwierdzone.
- [ ] Środowiska/laby i ownerzy zdefiniowani.


## Kryteria DoD

- [ ] Moduły i instrukcje labowe uzupełnione.
- [ ] Ćwiczenia/quiz/ocena skonfigurowane, wyniki zbierane.
- [ ] Metryki i feedback zebrane; quick-links/checklisty zaktualizowane.


## Artefakty do załączenia

- Sylabus i instrukcje labowe.
- Lista kont/dostępów, dane testowe.
- Quiz/ocena praktyczna i raport wyników.


## Walidacja / testy

- Pilotaż labów; sprawdzenie bezpieczeństwa danych i powtarzalności.
- Peer review scenariuszy pod kątem zgodności z runbookami/politykami.


## Metryki monitorowane

- % ukończenia i wyniki praktyczne/quiz.
- Czas wykonania ćwiczeń; liczba błędów/pytań podczas labów.
- Adoption narzędzi (np. liczba faktycznych użyć w SOC/DevSecOps po szkoleniu).


## Utrzymanie i aktualizacje

- Refresh po zmianach wersji narzędzi lub co 6–12 mies.
- Aktualizuj screeny, kroki i dane testowe; utrzymuj listę dostępów.


## Zakończenie

Po spełnieniu DoD opublikuj materiały, podlinkuj artefakty, odhacz checklisty w `reports/checklist_atomic.jsonl` i zaplanuj kolejny cykl szkoleń.
