---
title: Attack Patterns and Mitigation
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Attack Patterns and Mitigation


## Metadane

- Właściciel: Document Owner
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved

> Powiązania: linkage_index.jsonl


## Cel dokumentu

Zidentyfikować typowe wzorce ataków na system, przypisać kontrole i runbooki, aby zmniejszyć ryzyko i czas reakcji.


## Zakres i granice

- Obejmuje: wzorce (OWASP/CWE/MITRE ATT&CK), wektory (web/API/identity/data/supply chain), taktyki/techniki, mapowanie do kontrolek (prevent/detect/respond), IoCs, alerty, runbooki, testy (pentest/red/chaos), wymagania logowania.
- Poza zakresem: pełny program bezpieczeństwa (osobne), polityki org (linkowane).


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia

- Wejścia: model zagrożeń, architektura, logi/incydenty, standardy (OWASP/ATT&CK), polityki bezpieczeństwa, SLO bezpieczeństwa.
- Wyjścia: katalog wzorców i kontrolek, mapowanie TTP→kontrolka→alert→runbook, priorytety, luki i plan remediacji, checklisty testów.


## Założenia
- Dostępne są brokers/API gateway i registry.  
- Zespół zna standardy.  
- Monitoring działa end-to-end.
## Otwarte pytania
- Jak obsłużyć migracje wzorców (np. batch → async)?  
- Jakie SLO dla każdego wzorca?  
- Czy partnerzy akceptują podpisy/kontrakty?
## Powiązania (meta)

- Wymaga odniesienia do: Key Documents
- Wymaga odniesienia do: Key Document Structures
- Wymaga odniesienia do: Document Dependencies
- Wymaga odniesienia do: RACI i role
- Wymaga odniesienia do: Standardy i compliance


## Zależności dokumentu

Wskaż: model zagrożeń, logowanie/telemetria, SIEM/SOAR, polityki, architektura, runbooki, SLO; brak – odnotuj.


## Fazy cyklu życia

Discovery → Mapowanie TTP → Projekt kontrolek → Testy → Operacje → Przeglądy.



## Struktura sekcji (szkielet)

- Zakres systemu i priorytety (krytyczne dane/usługi).
- Katalog TTP (ATT&CK/OWASP) + ryzyko.
- Kontrolki prevent/detect/respond (IAM, WAF, RASP, rate limit, tokeny, DLP, EDR/SIEM).
- IoC i alerty (progi, kanały, KPI detekcji).
- Runbooki i eskalacje (linki).
- Testy i walidacja (pentest, red/chaos, purple teaming).
- Luki i plan remediacji.
- Ryzyka i mitigacje.


## Szybkie powiązania

- Meta: Key Documents
- Meta: Key Document Structures
- Meta: Document Dependencies


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

- Zmapuj TTP do kontrolek i alertów; uzupełnij runbooki; przetestuj; monitoruj luki i status.


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
- DLQ: Dead Letter Queue.  
- CDC: Change Data Capture.  
- Correlation ID: identyfikator śledzenia żądań.
## Przykłady użycia
- Webhook + podpisy do powiadomień partnerów.  
- Pub/sub do rozsyłania eventów biznesowych.  
- Batch/CDC do synchronizacji danych referencyjnych.
## Ryzyka i ograniczenia
- Brak idempotencji → duplikaty.  
- Zły wzorzec → wysokie koszty lub opóźnienia.  
- Brak versioning → breaking changes.  
- Słaba observability → trudna diagnostyka.
## Decyzje i uzasadnienia
- Wybór wzorca per domena.  
- Polityka retry/backoff.  
- Standardy kontraktów i wersjonowania.  
- Zakres logów/traces.
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

TTP → kontrole/alerty; logowanie → detekcja; luki → plan remediacji.


## Wymagane rozwinięcia

- Mapowanie TTP → kontrolki/alerty/runbooki.
- Testy → scenariusze ATT&CK/OWASP.


## Wymagane streszczenia

- Tabela TTP → kontrolka → alert → runbook → status.


## Guidance

Cel: jasna mapa zagrożeń i kontroli. DoR: model zagrożeń, logi/SIEM, architektura, polityki. DoD: katalog TTP, kontrole/alerty/runbooki, testy i luki; sekcje N/A uzasadnione; metadane aktualne.


## Checklisty jakości (DoR/DoD skrót)

- DoR: [ ] Model zagrożeń; [ ] SIEM/logi; [ ] Polityki; [ ] Architektura.
- DoD: [ ] Katalog TTP/kontrole/alerty/runbooki; [ ] Testy; [ ] Luki/plan; [ ] Sekcje N/A uzasadnione; metadane aktualne.
