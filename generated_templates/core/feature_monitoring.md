---
title: Feature Monitoring
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Feature Monitoring


## Metadane

- Właściciel: DevOps Engineer
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Monitorować nowe i istniejące funkcje produktu: metryki adopcji, zdrowia technicznego, jakości danych i doświadczenia użytkownika, aby szybko wykrywać regresje i potwierdzać wartość biznesową.


## Zakres i granice

- Obejmuje: definicje metryk feature (adopcja, aktywność, konwersja, retention), zdrowie techniczne (error rate, latency, resource), data quality, eksperymenty A/B, alerty i progi, dashboardy, rollout i post-launch review, logowanie i sampling, standardy taggingu eventów.  
- Poza zakresem: pełna strategia analityczna produktu (oddzielny dokument), testy QA (opisane w ui_test_strategy).


## Użytkownicy i interesariusze
- **DevOps / Platform Engineer** — zarządza infrastrukturą i pipeline'ami wdrożeniowymi
- **SRE (Site Reliability Engineer)** — definiuje SLO/SLI i zarządza niezawodnością
- **Development Team** — dostarcza artefakty do wdrożenia
- **Security Officer** — weryfikuje zgodność wdrożeń z polityką bezpieczeństwa

## Wejścia i wyjścia

- Wejścia: hipoteza i cele funkcji, event schema, baseline metryk, SLA/SLO, dane telemetryczne, feedback użytkowników, rollout plan.  
- Wyjścia: dashboard i alerty feature, metryki adopcji i zdrowia, raport post-launch, checklisty DoR/DoD, decyzje rollout/rollback, aktualizacja taggingu i dokumentacji.


## Założenia

- Platforma analytics/monitoring dostępna.  
- Feature flagi zaimplementowane.  
- Zespół gotowy reagować na alerty.


## Otwarte pytania

- Jak długo monitorować po rollout?  
- Jak łączyć metryki jakości z doświadczeniem użytkownika (NPS/CSAT)?  
- Jak zarządzać wersjonowaniem eventów przy iteracjach?

## Powiązania (meta)

- Key Documents: product_metrics_definition, ui_test_strategy, monitoring_strategy_document, zero_results_monitoring (dla search), experimentation_playbook, rollback_runbook.  
- Key Document Structures: metryki, eventy, alerty, rollout, raport.  
- Document Dependencies: analytics platform, logging, feature flags, monitoring/observability, A/B framework, data catalog.


## Zależności dokumentu

Wymaga: zdefiniowanych celów/metryk feature, event schema z taggingiem, dostępnych dashboardów/alertów, integracji z monitoringiem i A/B, planu rollout/rollback. Brak = brak DoR.


## Fazy cyklu życia

- Definicja metryk i eventów.  
- Konfiguracja dashboardów/alertów.  
- Rollout i monitoring post-launch.  
- Analiza i decyzje; iteracje.  
- Utrzymanie i regresja.



## Struktura sekcji (szkielet)
- Cel i zakres
- Definicje i role/RACI
- Standardy/zasady i narzędzia
- Kroki procesu / checklisty
- Kryteria jakości/DoD i wyjątki
- Komunikacja i eskalacje
- Rejestr zmian i utrzymanie
## Szybkie powiązania

- linkage_index.jsonl (feature/monitoring)  
- product_metrics_definition, experimentation_playbook, rollback_runbook


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

1. Zdefiniuj metryki i eventy; skonfiguruj dashboard/alerty.  
2. Wdrażaj z flagą; monitoruj i reaguj.  
3. Sporządź raport post-launch; zdecyduj o rollout/iteracjach.  
4. Aktualizuj dokumentację, progi i linkage_index.


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

- Adopcja: % użytkowników korzystających z funkcji.  
- Data completeness: odsetek oczekiwanych eventów.  
- Feature flag: przełącznik pozwalający sterować rolloutem.


## Przykłady użycia

- Monitoring nowego checkout flow.  
- Weryfikacja skuteczności rekomendacji.  
- Ocena nowej funkcji wyszukiwania.


## Ryzyka i ograniczenia

- Brak eventów → brak obserwowalności.  
- Złe progi → szum alertów.  
- Brak data quality → błędne wnioski.  
- Rollout bez flag → trudny rollback.


## Decyzje i uzasadnienia

- Progi KPI i alertów.  
- Strategia rollout/rollback i A/B.  
- Zakres data quality testów.  
- Kadencja raportów post-launch.


## Powiązania z innymi dokumentami

- [Dokument A] — [typ relacji: wymaga/uzupełnia/zastępuje/jest-częścią] — [uzasadnienie]
- [Dokument B] — [typ relacji] — [uzasadnienie]

## Powiązania z sekcjami innych dokumentów

- [Dokument X → Sekcja Y] — [powód powiązania i kierunek przepływu informacji]
- [Dokument Z → Sekcja W] — [powód powiązania i kierunek przepływu informacji]

## Słownik pojęć w dokumencie

- [Pojęcie 1] — [definicja i źródło normalizacyjne lub wewnętrzne]
- [Pojęcie 2] — [definicja i źródło normalizacyjne lub wewnętrzne]

## Wymagane odwołania do standardów

- [Standard 1, np. ISO 27001 §A.5] — [sekcja lub wymaganie, którego dotyczy to odwołanie]
- [Standard 2] — [sekcja lub wymaganie]

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

- Metryki ↔ Alerty ↔ Decyzje rollout/rollback.  
- Eventy ↔ Data quality ↔ Raport post-launch.  
- A/B ↔ Adopcja/konwersja ↔ Rollout.


## Struktura sekcji

1) Cele i metryki feature (biznes + techniczne)  
2) Event schema i tagging (naming, props)  
3) Dashboardy/alerty i progi  
4) Rollout/rollback i A/B (jeśli dotyczy)  
5) Raport post-launch i lekcje  
6) DoR/DoD, ryzyka, pytania


## Wymagane rozwinięcia

- Lista metryk z definicjami i targetami.  
- Event schema (nazwa, props, typy, wersjonowanie).  
- Alerty: adopcja, error rate, latency, data completeness.  
- Szablon raportu post-launch i checklist.  
- Plan rollout/rollback z feature flags.  
- Data quality testy dla eventów.


## Wymagane streszczenia

- Executive summary: status feature, metryki vs target, rekomendacja.  
- Skrót alertów i incydentów po wdrożeniu.


## Guidance (skrót)

- Definiuj metryki i eventy przed rolloutem; weryfikuj w staging.  
- Taguj konsekwentnie (naming, version); waliduj eventy w CI.  
- Monitoruj adopcję razem z error/latency i data quality.  
- Używaj feature flags i A/B; rollback przy spadku KPI lub wzroście błędów.  
- Raportuj post-launch w ciągu kilku dni; aktualizuj linkage_index.  
- Automatyzuj alerty; unikaj szumu (progi, agregacje).


## Checklisty Definition of Ready (DoR)

- [ ] Cele i metryki feature zdefiniowane; event schema gotowa.  
- [ ] Dashboardy/alerty przygotowane; progi ustalone.  
- [ ] Feature flag i plan rollout/rollback gotowe.  
- [ ] Data quality testy dla eventów w CI.  
- [ ] Odbiorcy raportu post-launch ustaleni.


## Checklisty Definition of Done (DoD)

- [ ] Metryki po rollout spełniają lub mają plan naprawy.  
- [ ] Alerty działają; brak nieadresowanych incydentów.  
- [ ] Raport post-launch opublikowany; linkage_index zaktualizowany.  
- [ ] Event schema stabilna i udokumentowana.  
- [ ] Wnioski i kolejne kroki zapisane.

