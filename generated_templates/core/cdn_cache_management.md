---
title: CDN Cache Management
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# CDN Cache Management


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Zdefiniować zasady zarządzania cache CDN/edge (TTL, wersjonowanie, purge, invalidacje) dla assetów i API, aby zoptymalizować wydajność i spójność przy minimalnym ryzyku starych treści.


## Zakres i granice

- Obejmuje: polityki TTL/ETag/If-None-Match, cache keys i vary headers, wersjonowanie assetów, purge/ban/soft purge, cache-busting, stale‑while‑revalidate, edge logic (redirects, compression), kontrolę API caching, metryki i alerty (hit ratio, latency), runbooki dla incydentów cache.  
- Poza zakresem: pełny design CDN (patrz content_delivery_network_cdn_design), bezpieczeństwo WAF (osobny dokument).


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia

- Wejścia: typy treści/assetów, SLA wydajności, wymagania spójności, ograniczenia bezpieczeństwa/licencji, konfiguracja CDN, modele wersjonowania, wzorce ruchu.  
- Wyjścia: polityki cache per typ treści, matryca TTL/headers, procedury purge/rollout, runbooki incydentów, checklisty DoR/DoD, dashboardy/metyki.


## Założenia

- CDN/edge wspiera potrzebne nagłówki/purge.  
- Origin posiada wersjonowane assety.  
- Monitoring jest dostępny.


## Otwarte pytania

- Jak obsłużyć multi‑region TTL/purge?  
- Czy potrzebne są dedykowane polityki dla partnerów/whitelabel?  
- Jak mierzyć koszt cache miss vs hit?

## Powiązania (meta)

- Key Documents: content_delivery_network_cdn_design, asset_delivery_strategy, asset_update_procedure, rollback_runbook, security_controls_reference, monitoring_strategy_document.  
- Key Document Structures: polityki cache, wersjonowanie, purge, monitoring, incydenty.  
- Document Dependencies: CDN/edge provider, origin, CI/CD, monitoring, logging.


## Zależności dokumentu

Wymaga: listy typów treści i ich SLA, konfiguracji CDN/headers, strategii wersjonowania assetów, dostępu do narzędzi purge i monitoringu. Brak = brak DoR.


## Fazy cyklu życia

- Definicja polityk i wersjonowania.  
- Konfiguracja CDN/edge.  
- Monitorowanie i kalibracja.  
- Incydenty i purge/rollback.  
- Przeglądy okresowe.



## Struktura sekcji (szkielet)
- Cele szkolenia i oczekiwane rezultaty
- Grupa docelowa/persony i wymagania wstępne
- Moduły/agenda z czasem i formą (teoria/lab)
- Materiały i środowisko (lab/demo)
- Ćwiczenia/prace domowe i kryteria zaliczenia
- Ocena postępów (quiz/lab/egzamin) i feedback
- Plan komunikacji/mentoringu i utrzymania materiałów
## Szybkie powiązania

- linkage_index.jsonl (cdn/cache/management)  
- asset_delivery_strategy, asset_update_procedure, rollback_runbook


## Mające zastosowanie standardy i normy

### Standardy międzynarodowe
- **ISO/IEC 12207** — Procesy Cyklu Życia Oprogramowania
- **PMBOK 7** — Przewodnik po Zarządzaniu Projektami (PMI)
- **ITIL 4** — Biblioteka Infrastruktury IT (Zarządzanie Usługami)

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

1. Skategoryzuj treści; przypisz polityki cache/TTL/headers.  
2. Skonfiguruj CDN/edge; ustaw wersjonowanie URL.  
3. Monitoruj metryki; reaguj wg runbooku na incydenty.  
4. Aktualizuj polityki po zmianach ruchu/produktów; odhacz DoD.


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

- TTL: czas życia cache.  
- Purge/Invalidate: wymuszenie usunięcia/starej treści.  
- Stale-while-revalidate: serwowanie starej treści w czasie odświeżania.


## Przykłady użycia

- Wersjonowane bundle JS/CSS z długim TTL.  
- Purge pojedynczej strony po release.  
- Wyłączenie cache dla API z PII/finansami.


## Ryzyka i ograniczenia

- Zbyt krótkie TTL → koszt i latencja.  
- Zbyt długie TTL bez wersji → stare treści u użytkowników.  
- Błędny purge globalny → wzrost ruchu na origin.  
- Cache API z danymi wrażliwymi → wycieki.


## Decyzje i uzasadnienia

- TTL per typ treści; kiedy wersjonowanie vs krótkie TTL.  
- Zakres cache dla API.  
- Polityka purge (soft vs hard).  
- Zakres monitoringu i alertów.


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

- TTL/Vary ↔ Wersjonowanie ↔ Purge.  
- Assety ↔ API ↔ Bezpieczeństwo (no‑store dla wrażliwych).  
- Monitoring ↔ Incydenty ↔ Rollback.


## Struktura sekcji

1) Typy treści i SLA/consistency  
2) Polityki cache (TTL, headers, keys, vary)  
3) Wersjonowanie assetów i cache-busting  
4) Procedury purge/invalidacji i rollout  
5) Monitoring (hit ratio, latency, stale) i alerty  
6) Runbook incydentów cache  
7) Ryzyka, decyzje, pytania


## Wymagane rozwinięcia

- Matryca TTL/headers per typ treści (HTML, JS/CSS, media, API).  
- Definicja cache keys i vary (lang/device/auth?).  
- Procedury purge: global/segment, soft/hard, kolejność.  
- Wzorce rollout (canary, versioned URLs).  
- Dashboard hit ratio/latency i progi alertów.  
- Checklista incydentu: stara treść, błędny purge, stale content.


## Wymagane streszczenia

- Executive summary: główne polityki TTL/wersjonowanie.  
- Skrót procedury purge i kontaktów on-call.


## Guidance (skrót)

- Preferuj wersjonowane URL (hashy) dla assetów; długie TTL.  
- API domyślnie no‑cache/no‑store, chyba że jawnie do cache.  
- Używaj ETag/If-None-Match zamiast krótkich TTL dla spójności.  
- Testuj purge na canary; utrzymuj runbooki.  
- Monitoruj hit ratio i stale; koryguj TTL na podstawie danych.  
- Dokumentuj i aktualizuj linkage_index po zmianach polityk.


## Checklisty Definition of Ready (DoR)

- [ ] Typy treści i SLA zdefiniowane.  
- [ ] Strategia wersjonowania assetów uzgodniona.  
- [ ] Narzędzia purge/monitoring dostępne.  
- [ ] Konfiguracja headers/keys przygotowana.  
- [ ] Plan runbooków incydentów spisany.


## Checklisty Definition of Done (DoD)

- [ ] Polityki wdrożone w CDN/edge; testy hit ratio OK.  
- [ ] Purge działa (test) i jest udokumentowany.  
- [ ] Monitoring/alerty aktywne; dashboardy dostępne.  
- [ ] Dokumentacja/linkage_index zaktualizowane.  
- [ ] Brak otwartych incydentów „stale content”.

