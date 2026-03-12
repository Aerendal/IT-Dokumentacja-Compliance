---
title: Common API Issues and Solutions
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Common API Issues and Solutions


## Metadane

- Właściciel: Backend Developer
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Lista najczęstszych problemów z API i gotowe sposoby ich rozwiązania, aby skrócić czas diagnozy i poprawić doświadczenie konsumentów API.


## Zakres i granice

- Obejmuje: auth/401/403, rate limiting/429, timeouty/latencja, walidacja schematu, idempotencja, CORS, wersjonowanie/deprecjacje, obsługa błędów, typowe kwestie bezpieczeństwa (OWASP API).  
- Poza zakresem: pełna specyfikacja bezpieczeństwa (design_bezpieczenstwa_api) i testy bezpieczeństwa (testowanie_bezpieczenstwa_api).


## Użytkownicy i interesariusze
- **Backend Developer / API Owner** — projektuje i implementuje interfejs API
- **Frontend Developer / Consumer** — integruje się z API i zgłasza wymagania
- **Integration Architect** — definiuje standardy integracji i kontrakt API
- **QA Engineer** — weryfikuje kontrakty i scenariusze błędów

## Wejścia i wyjścia

- Wejścia: logi/gateway, request-id, telemetry 4xx/5xx, zgłoszenia klientów, kontrakt OpenAPI, zasady wersjonowania.  
- Wyjścia: tabela problem→diagnoza→remedium, zalecenia klient/serwer, linki do runbooków i dokumentacji, wpis w linkage_index.


## Założenia

- [Założenie 1 — co przyjmujemy za prawdziwe bez weryfikacji]
- [Założenie 2 — warunki brzegowe, które muszą być spełnione]

## Otwarte pytania

- [Pytanie 1 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]
- [Pytanie 2 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]

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

- Cel i zakres dokumentu
- Główne sekcje merytoryczne
- Powiązania z innymi dokumentami
- Wymagane zatwierdzenia i przeglądy
- Historia zmian

## Szybkie powiązania

- linkage_index.jsonl (api/common_issues)  
- design_bezpieczenstwa_api, strategia_wersjonowania_api, api_rate_limiting_requirements


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **IEEE 1016** — Standard dla Opisów Projektowania Oprogramowania (SDD)
- **IEEE 42010** — Opis Architektoniczny Systemów i Oprogramowania
- **ISO/IEC 15288** — Procesy Cyklu Życia Systemów
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

1. Zidentyfikuj objawy (kody 4xx/5xx, latency, klient).  
2. Znajdź odpowiadający wiersz problem→remedium; zastosuj zalecenia serwer/klient.  
3. Jeśli brak remedium, dodaj wpis, zaktualizuj linkage_index i checklisty.


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

- [Termin 1] — [definicja robocza i źródło]
- [Termin 2] — [definicja robocza i źródło]

## Przykłady użycia

- [Przykład 1 — krótki opis sytuacji i zastosowania tego dokumentu]
- [Przykład 2 — krótki opis sytuacji i zastosowania tego dokumentu]

## Ryzyka i ograniczenia

- [Ryzyko 1 — prawdopodobieństwo, wpływ, sposób ograniczenia]
- [Ryzyko 2 — prawdopodobieństwo, wpływ, sposób ograniczenia]

## Decyzje i uzasadnienia

- [Decyzja 1 — uzasadnienie, alternatywy odrzucone, data]
- [Decyzja 2 — uzasadnienie, alternatywy odrzucone, data]

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

- [ ] Każdy typowy problem ma diagnozę i remedium; kody błędów spójne.  
- [ ] Linki do polityk wersjonowania/rate limitów i bezpieczeństwa są dodane; linkage_index uzupełniony.


## Lista kontrolna spójności relacji

- [ ] Czy każda sekcja z relacją ma wskazaną sekcję źródłową?
- [ ] Czy relacje nie tworzą sprzecznych wymagań?
- [ ] Czy wszystkie wymagane standardy mają odwołania?
- [ ] Czy RACI jest kompletne dla kluczowych działań?

## Artefakty powiązane

- Logi/trace z przykładami, nagłówki RateLimit/Retry-After, wzór JSON error, linki do runbooków, ADR/waiver log.


## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji

- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status: oczekuje/zatwierdzone/odrzucone]
- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status]

## Metryki jakości

- Średni czas rozwiązania typowych zgłoszeń, liczba powtórzeń tego samego problemu, udział zgłoszeń z poprawnym request-id/logami, % przypadków rozwiązanych z tej listy bez eskalacji.


## Kryteria ukończenia

- [ ] Dokument pomaga skrócić MTTR dla typowych problemów API i jest powiązany w linkage_index.


## Typowe problemy / rozwiązania

- Auth/401/403: brak/expired token, zły scope → odśwież token, sprawdź scope/role, wymuś clock sync.  
- Rate limit/429: brak retry/backoff → exponential backoff + jitter, idempotency key, optymalizuj batch, sprawdź nagłówki RateLimit.  
- Timeouty/latencja: duże payloady/brak paginacji → paginacja, kompresja, cache, rozdziel read/write.  
- Schema/validation: breaking change, brak pola → sprawdź wersję, fallback/compat warstwa, kontrakty i tests.  
- Idempotencja: duplikaty przy retry → idempotency key, PUT dla tworzenia, once-only side effects.  
- CORS: brak nagłówków → popraw `Access-Control-*` zgodnie z polityką.  
- Version mismatch: stary klient → komunikacja deprecji, semver w ścieżce/nagłówku, feature flags.  
- Error handling: niespójne kody → ustandaryzuj JSON error (code/message/request-id).  
- Security/OWASP: brak input validation → waliduj schemat, limituj, loguj z request-id, SCA/DAST.


## Checklisty Definition of Ready (DoR)

- [ ] Dostęp do logów/gateway i request-id; kontrakt API znany.  
- [ ] Polityka wersjonowania i rate limitów dostępna.


## Checklisty Definition of Done (DoD)

- [ ] Tabela problemów uzupełniona, linki/runbooki dodane; linkage_index zaktualizowany.  
- [ ] Status/metadane aktualne; checklisty DoR/DoD odhaczone.

