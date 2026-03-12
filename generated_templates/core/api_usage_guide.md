---
title: API Usage Guide
status: needs_content
aligned: true
aligned_rev: 6
aligned_at: 2026-02-09
aligned_by: codex
---
# API Usage Guide


## Metadane

- Właściciel: Backend Developer
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved
- Repo / moduł: [link]


## Cel dokumentu

Przewodnik dla deweloperów korzystających z API (onboarding, auth, przykłady, limity).


## Zakres i granice

- Obejmuje: jak zacząć, auth, pierwsze wywołania, przykłady, limity/rate limiting, debug/observability, wsparcie.
- Poza zakresem: implementacja backendu.


## Użytkownicy i interesariusze
- **Backend Developer / API Owner** — projektuje i implementuje interfejs API
- **Frontend Developer / Consumer** — integruje się z API i zgłasza wymagania
- **Integration Architect** — definiuje standardy integracji i kontrakt API
- **QA Engineer** — weryfikuje kontrakty i scenariusze błędów

## Wejścia i wyjścia
- Wejścia: cele biznesowe, backlog/epiki, wymagania niefunkcjonalne, ograniczenia prawne/techniczne, istniejące systemy/dane.
- Wyjścia: zaakceptowana wersja dokumentu, decyzje architektoniczne/procesowe, action items z właścicielami i terminami.
## Założenia
- Dostępny design system i komponenty A11y.  
- CI/CD pozwala na skany i raporty.  
- Zespół ma kompetencje do testów manualnych AT.
## Otwarte pytania
- Jakie jurysdykcje/klienci wymagają formalnego VPAT/ACR?  
- Jak mierzyć i raportować trend defektów A11y?  
- Jak obsługiwać wyjątki/waivery?
## Powiązania (meta)
- Wymaga odniesienia do: Key Documents
- Wymaga odniesienia do: Key Document Structures
- Wymaga odniesienia do: Document Dependencies
- Wymaga odniesienia do: RACI i role
- Wymaga odniesienia do: Standardy i compliance
## Zależności dokumentu
- Upstream: systemy źródłowe, dane referencyjne, decyzje architektoniczne nadrzędne.
- Downstream: konsumpcja rezultatów (zespoły, usługi, dokumenty pokrewne).
- Zewnętrzne: dostawcy, standardy branżowe, umowy/regulacje wpływające na zakres.
## Fazy cyklu życia
- Discovery/Analiza: doprecyzowanie problemu, interesariusze, ograniczenia.
- Projektowanie/Planowanie: decyzje, warianty, kryteria akceptacji, plan wdrożenia.
- Implementacja/Testy: realizacja, walidacja, kryteria go/no-go.
- Wdrożenie/Operacje: rollout, monitoring, eskalacje, ciągłe doskonalenie.
## Struktura sekcji (szkielet)

- Wprowadzenie/onboarding
- Auth i klucze
- Pierwsze wywołania/quickstart
- Limity i good practices
- Debug/observability
- Wsparcie


## Szybkie powiązania
- dashboard-usage-guide
- component-usage-guide
- api-usage-report
- api-usage-monitoring
- api-usage-analytics

## Mające zastosowanie standardy i normy

### Standardy międzynarodowe
- **IEEE 830** — Zalecana Praktyka dla Specyfikacji Wymagań Oprogramowania (SRS)
- **OWASP ASVS** — Standard Weryfikacji Bezpieczeństwa Aplikacji (OWASP)
- **ISO/IEC 25010** — Model Jakości Systemu i Oprogramowania (SQuaRE)
- **ITIL 4** — Biblioteka Infrastruktury IT (Zarządzanie Usługami)
- **ISO 20000-1** — System Zarządzania Usługami IT (SMS)
- **ISO/IEC 12207** — Procesy Cyklu Życia Oprogramowania

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

- API reference
- Przykłady SDK
- Polityki auth/rate limiting
- Kanały wsparcia


## Wyjścia

- Przewodnik published
- Przykłady quickstart
- Linki do SDK/sandbox
- Checklisty DoR/DoD



## Szybkie powiązania (uzupełnij)

- [ ] api_reference.md
- [ ] api_documentation.md
- [ ] api_best_practices_guide.md
- [ ] api_rate_limiting_requirements.md
- [ ] api_monitoring_strategy.md
- [ ] api_support_procedure.md


## Wymagane rozwinięcia / streszczenia

- Streszczenie kluczowych decyzji/ryzyk; rozwinięcia zasad/wzorców.


## Wymagane powiązania

- Dokumenty design/docs/security/monitoring/rate limiting; runbooki wsparcia.


## Kryteria DoR

- [ ] API reference dostępna
- [ ] Przykłady/SDK przygotowane
- [ ] Polityki auth/limity zebrane
- [ ] Kanały wsparcia znane


## Kryteria DoD

- [ ] Przewodnik opublikowany
- [ ] Przykłady dodane
- [ ] Linki do SDK/sandbox uzupełnione
- [ ] Checklisty/quick-links zaktualizowane


## Artefakty do załączenia

- Przewodnik (MD/PDF)
- Przykłady quickstart
- Linki SDK/sandbox
- FAQ


## Walidacja / testy

- Sprawdź spójność z reference, limity i przykłady; sanity kontraktów jeśli dotyczy.


## Metryki monitorowane

- Czas onboardingu dewelopera
- Liczba błędów auth/limity
- Zgłoszenia wsparcia na start
- Adopcja SDK


## Utrzymanie i aktualizacje

- Przegląd co release lub przy zmianach API/polityk.


## Zakończenie

Po spełnieniu DoD zaktualizuj status, podlinkuj artefakty/quick-links i odhacz checklistę w reports/checklist_atomic.jsonl.
