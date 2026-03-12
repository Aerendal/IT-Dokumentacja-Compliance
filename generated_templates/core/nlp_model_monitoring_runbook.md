---
title: NLP Model Monitoring Runbook
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# NLP Model Monitoring Runbook


## Metadane

- Właściciel: ML Engineer
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Zapewnić operacyjne monitorowanie modeli NLP (klasyfikacja, NER, QA, generacja): metryki, alerty, diagnostyka, reakcje na degradację/drift, aby utrzymać jakość i zgodność SLA.


## Zakres i granice

- Obejmuje: metryki online/offline (accuracy/F1, BLEU/ROUGE, toksyczność, latency), stabilność wejść (lang detection, długość), drift danych/cech, zdrowie pipeline (tokenizer, embeddings), błędy (timeout, OOM), rate limiting, bezpieczeństwo (PII/leak), logowanie i sampling, playbooki reakcji (rollback/retrain/throttle), raporty.  
- Poza zakresem: projekt nowych modeli NLP (osobne dokumenty), labeling pipeline (osobne playbooki).


## Użytkownicy i interesariusze
- **ML Engineer / Data Scientist** — buduje, trenuje i ewaluuje modele
- **Data Engineer** — przygotowuje dane i zarządza pipeline'ami
- **Product Owner** — definiuje metryki sukcesu i priorytety eksperymentów
- **MLOps Engineer** — zarządza wdrożeniem i monitoringiem modeli na produkcji

## Wejścia i wyjścia

- Wejścia: definicja SLA/KPI, baseline metryk, schemat logów, sampling plan, listy słów wrażliwych/PII, limity latency i kosztów, registry modeli, kontrakty API.  
- Wyjścia: dashboard/alerty, runbook reakcji (drift/degradacja/incydent bezpieczeństwa), lista metryk i progów, procedura rollback/retrain, checklisty DoR/DoD, raporty cykliczne.


## Założenia

- Dostępne narzędzia monitoring/logging i PII/toksyczność.  
- Model registry/feature store działają.  
- Zespół ma proces releasu i rollbacku.


## Otwarte pytania

- Jak szybko musimy reagować na alert toksyczności/PII?  
- Jak etykietować próbki w trybie ciągłym?  
- Czy wymagane są raporty zgodności dla regulatorów/klientów?  
- Jak zarządzać wielojęzycznością w metrykach?

## Powiązania (meta)

- Key Documents: predictive_model_degradation, data_quality_playbook, security_controls_reference, rollback_runbook, bias_fairness_policy, logging_and_audit_trail.  
- Key Document Structures: metryki, alerty, diagnostyka, reakcje, raporty.  
- Document Dependencies: model registry, feature store, monitoring/logging, PII detector, throttling/rate limiter, CI/CD ML.


## Zależności dokumentu

Wymaga: baseline metryk, definicji SLA, dostępnych logów i sampling, narzędzi do detekcji PII/toksyczności, możliwości rollback/retrain, dostępu do model registry i feature store. Brak = brak DoR.


## Fazy cyklu życia

- Ustalenie SLA i baseline.  
- Konfiguracja logów/samplingu/metryk.  
- Detekcja i alerty.  
- Reakcja (rollback/retrain/throttle).  
- Raporty i retrospektywa.



## Struktura sekcji (szkielet)
- Cel, zakres i definicje sukcesu
- Trigger/scenariusze i preconditions
- Role, uprawnienia i narzędzia
- Kroki operacyjne (checklista) z walidacją
- Monitoring i dowody wykonania
- Rollback/contingency oraz komunikacja/escalacja
- Rejestr zmian runbooka
## Szybkie powiązania

- linkage_index.jsonl (nlp/model/monitoring/runbook)  
- predictive_model_degradation, bias_fairness_policy, rollback_runbook


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **CIS Controls v8** — Krytyczne Mechanizmy Bezpieczeństwa (CIS)
- **ISO/IEC 12207** — Procesy Cyklu Życia Oprogramowania
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

1. Zdefiniuj SLA i baseline; ustaw metryki i progi.  
2. Skonfiguruj logowanie i sampling; uruchom alerty.  
3. Reaguj według runbooków na alerty; waliduj po akcji.  
4. Raportuj cyklicznie; dostrajaj progi i monitoring; aktualizuj linkage_index.


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

- Toxicity score: miara treści obraźliwych lub szkodliwych.  
- Drift: zmiana dystrybucji danych wejściowych/wyjściowych vs referencja.  
- Sampling: wybór podzbioru żądań do oceny jakości.


## Przykłady użycia

- Monitorowanie klasyfikatora tematów w wielu językach.  
- Runbook dla wzrostu toksyczności w modelu czatowym.  
- Reakcja na degradację BLEU w tłumaczeniu maszynowym.


## Ryzyka i ograniczenia

- Fałszywe alerty przy małych próbkach.  
- Brak etykiet online → opóźniona detekcja degradacji.  
- PII leak → incydent bezpieczeństwa/regulacyjny.  
- Zbyt agresywne progi → nadmierne eskalacje.


## Decyzje i uzasadnienia

- Wybór metryk i progów.  
- Strategia sampling i etykietowania.  
- Kryteria rollback vs retrain.  
- Polityka obsługi incydentów PII/toksyczności.


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

- Metryki ↔ Progi ↔ Alerty ↔ Reakcje.  
- Drift danych ↔ Degradacja jakości ↔ Retraining/rollback.  
- Bezpieczeństwo (PII/toksyczność) ↔ Alerty ↔ Eskalacje.


## Struktura sekcji

1) SLA/KPI i baseline  
2) Metryki i progi (quality, latency, koszt, bezpieczeństwo)  
3) Logowanie/sampling i dane referencyjne  
4) Alerty i eskalacje  
5) Diagnostyka i runbook reakcji (drift, degradacja, incydent PII)  
6) Rollback/retrain i walidacja  
7) Raporty cykliczne i ciągłe doskonalenie  
8) Ryzyka, decyzje, pytania


## Wymagane rozwinięcia

- Lista metryk i progów (F1, BLEU/ROUGE, toxicity, latency, koszt/token).  
- Plan sampling (procent, stratified po językach/tematach).  
- Procedury detekcji driftu (PSI/JS divergence) i bezpieczeństwa (PII).  
- Runbook: co robić przy spadku metryk, wzroście toksyczności, latencji.  
- Checklisty rollback/retrain i walidacji offline/online.  
- Szablon raportu tygodniowego z trendami.


## Wymagane streszczenia

- Executive summary: status metryk, alerty, działania.  
- Skrót bezpieczeństwa: wykryte PII/toksyczność, reakcje.


## Guidance (skrót)

- Mierz zarówno jakość jak i koszt/latencję; balansuj budżet.  
- Używaj reprezentatywnych próbek i taguj język/kontekst.  
- Alertuj na zmiany dystrybucji wejść i wyjść.  
- Trzymaj ścieżkę szybkiego rollbacku; dokumentuj decyzje.  
- Monitoruj PII/toksyczność; eskaluj incydenty bezpieczeństwa.  
- Automatyzuj raporty i aktualizuj linkage_index.


## Checklisty Definition of Ready (DoR)

- [ ] SLA/KPI i baseline metryk zdefiniowane.  
- [ ] Logi/sampling skonfigurowane; dane referencyjne zebrane.  
- [ ] Narzędzia PII/toksyczność i drift gotowe.  
- [ ] Ścieżka rollback/retrain dostępna.  
- [ ] Dashboard/alerty przygotowane.


## Checklisty Definition of Done (DoD)

- [ ] Monitoring działa; alerty trafiają do właściwych kanałów.  
- [ ] Runbooki reakcji przetestowane; rollback/retrain wykonalne.  
- [ ] Raporty cykliczne publikowane; linkage_index zaktualizowany.  
- [ ] Brak otwartych krytycznych alertów lub plan działań zapisany.  
- [ ] Dostrojenie progów po retrospektywie wykonane.

