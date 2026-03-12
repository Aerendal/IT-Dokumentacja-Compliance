---
title: Accessibility Improvement Plan
status: needs_content
aligned: true
aligned_rev: 6
aligned_at: 2026-02-09
aligned_by: codex
---
# Accessibility Improvement Plan


## Metadane

- Właściciel: Project Manager
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Określić plan poprawy dostępności produktu zgodnie z WCAG (docelowo AA), eliminować bariery, planować audyty i wdrożenia, by zapewnić dostępność dla wszystkich użytkowników i zgodność prawną.


## Zakres i granice

- Obejmuje: audyty a11y (automatyczne i manualne), backlog problemów, priorytety i roadmapę, standardy komponentów (design system), treści i lokalizacja, testy z czytnikami ekranu/klawiaturą, dokumentację i szkolenia, monitoring regresji.  
- Poza zakresem: pełne wytyczne WCAG (odniesienie do wcag_level_requirements), decyzje produktowe niezwiązane z a11y.


## Użytkownicy i interesariusze
- Streaming/Video Eng, SRE/Observability, Product, Ads/Monetization, FinOps, Security/DRM.
## Wejścia i wyjścia

- Wejścia: aktualne wyniki audytów, lista komponentów/widoków, poziom docelowy WCAG, dane o użytkownikach z niepełnosprawnościami, standardy treści, dostępne narzędzia testowe.  
- Wyjścia: roadmapa z priorytetami, backlog ticketów, standardy a11y dla komponentów, plan testów/regresji, checklisty DoR/DoD, raporty statusu.


## Założenia

- Dostępny design system i CI.  
- Zespół ma dostęp do SR i narzędzi.  
- Interesariusze akceptują roadmapę.


## Otwarte pytania

- Jak mierzyć poprawę a11y (np. % luk zamkniętych, score)?  
- Jak obsłużyć dostępność w aplikacjach mobilnych?  
- Czy potrzebne są testy z realnymi użytkownikami?

## Powiązania (meta)

- Key Documents: wcag_level_requirements, aria_implementation_design, ui_test_strategy, semantic_html_implementation, documentation_roadmap, accessibility_vision.  
- Key Document Structures: audyt, backlog, standardy, testy, szkolenia, monitoring.  
- Document Dependencies: design system, repo komponentów, CI/CD z testami a11y, analytics/feedback, training materials.


## Zależności dokumentu

Wymaga: poziomu docelowego WCAG, aktualnych audytów i listy komponentów, narzędzi testowych (axe/lint/SR), zespołu do poprawek, planu szkoleniowego, kanału do feedbacku użytkowników. Brak = brak DoR.


## Fazy cyklu życia

- Audyt i analiza luk.  
- Priorytetyzacja i roadmapa.  
- Implementacja i testy.  
- Monitoring/regresja i raporty.  
- Szkolenia i ciągłe doskonalenie.



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

- linkage_index.jsonl (accessibility/improvement/plan)  
- wcag_level_requirements, aria_implementation_design


## Mające zastosowanie standardy i normy

### Standardy międzynarodowe
- **PMBOK 7** — Przewodnik po Zarządzaniu Projektami (PMI)
- **PRINCE2 7** — Projekty w Kontrolowanych Środowiskach
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

1. Zbierz wyniki audytu i ustal cele WCAG.  
2. Utwórz backlog i roadmapę; przypisz właścicieli.  
3. Implementuj standardy w design systemie; testuj w CI.  
4. Raportuj postęp, aktualizuj dokument i linkage_index.


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

- WCAG: Web Content Accessibility Guidelines.  
- SR: screen reader.  
- Impact scoring: priorytetyzacja wg wpływu na dostępność.


## Przykłady użycia

- Plan naprawy dostępności panelu admin po audycie.  
- Włączenie standardów a11y do design systemu.  
- Przygotowanie do przeglądu zgodności WCAG AA.


## Ryzyka i ograniczenia

- Brak zasobów → opóźnienia.  
- Tylko automaty → niewykryte problemy SR.  
- Brak standardów → regresje w nowych feature’ach.  
- Słaba komunikacja → brak wsparcia zespołów.


## Decyzje i uzasadnienia

- Poziom WCAG docelowy i termin.  
- Kadencja audytów/regresji.  
- Progi impact/RAG.  
- Zakres szkoleń obowiązkowych.


## Powiązania z innymi dokumentami
- Streaming Platform, Live Streaming Implementation, Observability QoE, DRM/Ads/CDN policies, Cost Optimization.
## Powiązania z sekcjami innych dokumentów
- Observability QoE → metryki; CDN Strategy → routing; Cost → optymalizacje.
## Słownik pojęć w dokumencie
- QoE, Rebuffer, Startup, ABR, CDN, Canary, FinOps.
## Wymagane odwołania do standardów
- HLS/DASH/CMAF, DRM/ads standardy, polityki QoE/SLA firmy.
## Mapa relacji sekcja→sekcja
- Problemy → Backlog → Testy/Rollout → Monitoring → Raport → Korekta.
## Mapa relacji dokument→dokument
- Improvement Plan → Platform/Live/Observability/CDN/DRM/Ads → Cost Optimization.
## Ścieżki informacji
- Metryki → Problemy → Backlog → Rollout → Monitoring → Raport → Iteracja.
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
- Dashboardy QoE/koszt, backlog działań, plan testów, raporty postępu, decyzje rollout/rollback.
## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji
- Streaming/SRE → Product/Ads → FinOps/Security → Owner sign‑off.
## Metryki jakości
- Zmiana QoE (rebuffer/startup/error), koszt CDN/transcode, liczba rollbacków, czas reakcji na regresje, tempo realizacji backlogu.
## Kryteria ukończenia
- [ ] Backlog i plan wdrożenia gotowe; raport postępu przygotowany; dokument w linkage_index.
- [ ] Wersja/data/właściciel aktualne.
## Powiązania sekcja↔sekcja

- Audyty ↔ Backlog ↔ Roadmapa ↔ Monitoring regresji.  
- Standardy komponentów ↔ Szkolenia ↔ Testy.  
- Treści ↔ Lokalizacja ↔ WCAG.


## Struktura sekcji

1) Cele i poziom WCAG  
2) Audyty i luki (raport)  
3) Backlog i priorytety (RAG/impact)  
4) Standardy komponentów i treści  
5) Plan testów/regresji (SR/klawiatura/automaty)  
6) Szkolenia i komunikacja  
7) Raportowanie, DoR/DoD  
8) Ryzyka, decyzje, pytania


## Wymagane rozwinięcia

- Lista luk z audytu + priorytety.  
- Standardy design systemu (kolory/kontrast, focus, ARIA).  
- Plan testów z SR (NVDA/JAWS/VoiceOver) i urządzeniami.  
- Szablon raportu statusowego.  
- Roadmapa z datami i właścicielami.  
- Plan szkoleń i materiałów.


## Wymagane streszczenia

- Executive summary: poziom docelowy, top luki i plan.  
- Skrót postępu (RAG) i najbliższe releasy.


## Guidance (skrót)

- Naprawiaj najpierw blokery dla użytkowników klawiatury/SR.  
- Wprowadzaj standardy do design systemu; audytuj PR.  
- Automaty + manual (SR/klawiatura) w CI; regresja po każdej zmianie UI.  
- Utrzymuj backlog z impact/empathy scoringiem.  
- Komunikuj postępy interesariuszom; aktualizuj linkage_index.


## Checklisty Definition of Ready (DoR)

- [ ] Poziom WCAG i zakres widoków określony.  
- [ ] Raport audytu i lista komponentów dostępne.  
- [ ] Narzędzia testowe i SR przygotowane.  
- [ ] Zespół/właściciele zidentyfikowani.  
- [ ] Kanał feedbacku użytkowników aktywny.


## Checklisty Definition of Done (DoD)

- [ ] Luki usunięte zgodnie z roadmapą; testy a11y zielone.  
- [ ] Standardy design systemu zaktualizowane; PR review a11y działa.  
- [ ] Raport postępu i linkage_index zaktualizowane.  
- [ ] Szkolenia przeprowadzone; materiały dostępne.  
- [ ] Brak otwartych krytycznych braków a11y.

