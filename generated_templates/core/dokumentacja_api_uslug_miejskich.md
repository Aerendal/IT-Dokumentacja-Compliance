---
title: Dokumentacja API usług miejskich
status: needs_content
aligned: true
aligned_rev: 6
aligned_at: 2026-02-09
aligned_by: codex
---
# Dokumentacja API usług miejskich


## Metadane

- Właściciel: Backend Developer
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Opisać API dla usług miejskich (transport, energia/utility, środowisko, zgłoszenia mieszkańców): kontrakty, bezpieczeństwo, limity, open data vs restricted, prywatność (lokacja/PII), SLA i integracje.


## Zakres i granice

- Obejmuje: domeny i endpointy (transport rozkłady/RT, energia/utility, środowisko/sensory, zgłoszenia mieszkańców), auth/roles, throttling/rate limits, open data vs restricted, schematy i przykłady (OpenAPI), kody błędów/paginacja/filtry/wersjonowanie, SLA/SLO/dostępność/cache, webhooki/eventy, sandbox/test cases, prywatność (lokacja/PII) i zgodność (RODO).  
- Poza zakresem: szczegółowe UI/portal mieszkańca (osobny dokument).


## Użytkownicy i interesariusze
- **Backend Developer / API Owner** — projektuje i implementuje interfejs API
- **Frontend Developer / Consumer** — integruje się z API i zgłasza wymagania
- **Integration Architect** — definiuje standardy integracji i kontrakt API
- **QA Engineer** — weryfikuje kontrakty i scenariusze błędów

## Wejścia i wyjścia

- Wejścia: wymagania domen miejskich, dane źródłowe (GTFS/GBFS/utility IoT), polityki open data/restricted, wymogi prywatności/RODO, limity infrastruktury, wzorce błędów, wymagania partnerów.  
- Wyjścia: spec OpenAPI, przykłady request/response, kody błędów, polityki auth/limity, SLA/SLO, plan cache, webhook/event spec, sandbox, sekcja privacy/RODO.


## Założenia

- [Założenie 1 — co przyjmujemy za prawdziwe bez weryfikacji]
- [Założenie 2 — warunki brzegowe, które muszą być spełnione]

## Otwarte pytania

- [Pytanie 1 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]
- [Pytanie 2 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]

## Powiązania (meta)

- Key Documents: api_gateway_policy, open_data_policy, privacy_policy, security_requirements, monitoring_strategy_document, incident_response_runbook, data_classification, access_control_policy.
- Key Document Structures: domeny/endpointy, auth/limits, kontrakty, SLA, privacy.
- Document Dependencies: API gateway, auth (OAuth2/JWT/eID), rate limiting/cache, logging/monitoring, sandbox, open data portal.



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
- Streszczenie celu i KPI
- Kontekst, założenia i ograniczenia
- Zakres oraz role/RACI
- Główne decyzje i warianty
- Proces/architektura/etapy
- Ryzyka, zależności i mitigacje
- Plan wdrożenia i kryteria akceptacji
- Monitoring i raportowanie
- Załączniki i źródła
## Szybkie powiązania

- linkage_index.jsonl (smart_city/api_docs)
- api_gateway_policy, open_data_policy, privacy_policy, security_requirements, monitoring_strategy_document, incident_response_runbook, data_classification, access_control_policy


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

1. Opisz domeny/endpointy i auth/limity; dodaj OpenAPI/kody błędów.  
2. Ustal SLA/cache/CDN, webhooki i sandbox; dodaj sekcję privacy/RODO.  
3. Linkuj do gateway/monitoring/runbooków; zamknij DoR/DoD i linkage_index.


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

- [ ] Kontrakty zgodne z danymi i auth/limity; SLA/alerty opisane.  
- [ ] Privacy (PII/lokacja) opisana; retencja i anonimizacja zgodne z polityką.  
- [ ] Dokument w linkage_index; relacje cross‑doc opisane.


## Lista kontrolna spójności relacji

- [ ] Czy każda sekcja z relacją ma wskazaną sekcję źródłową?
- [ ] Czy relacje nie tworzą sprzecznych wymagań?
- [ ] Czy wszystkie wymagane standardy mają odwołania?
- [ ] Czy RACI jest kompletne dla kluczowych działań?

## Artefakty powiązane

- OpenAPI spec, przykłady, test cases, rate limit/config, cache/CDN policy, webhook spec, sandbox instrukcje, privacy/RODO sekcja, runbook incident, waiver log, ADR log.


## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji

- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status: oczekuje/zatwierdzone/odrzucone]
- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status]

## Metryki jakości

- % endpointów z przykładami i testami, liczba błędów 4xx/5xx/limitów, SLA uptime/latency, liczba incydentów privacy, liczba waiverów i czas sunset.

## Kryteria ukończenia

- [ ] Dokumentacja API kompletna (kontrakty, auth/limity, SLA, privacy, sandbox); dokument w linkage_index; wersja/data/właściciel aktualne.


## Struktura sekcji

1) Domeny i endpointy (transport, energia/utility, środowisko, zgłoszenia) z opisem danych  
2) Auth/roles i rate limits (open vs restricted, PII, klucze, eID)  
3) Kontrakty i przykłady (OpenAPI, schematy, paginacja/filtry, kody błędów, wersjonowanie)  
4) SLA/SLO, dostępność, cache/CDN, retry/backoff  
5) Webhooki/eventy i sandbox/test cases  
6) Prywatność i zgodność (lokacja/PII, anonimizacja, RODO, retention)  
7) Monitoring/observability i incident response  
8) Ryzyka i ograniczenia; waivery (sunset)  
9) Załączniki (OpenAPI, przykłady, polityki, runbooki)


## Wymagane rozwinięcia

- Spec OpenAPI per domena; przykłady request/response; kody błędów.  
- Polityki auth/limitów dla open vs restricted; zasady cache/CDN.  
- Sekcja privacy: jakie dane lokacyjne/PII, retencja, anonimizacja.  
- Sandbox/test cases i kryteria akceptacji integratorów.


## Wymagane streszczenia

- Executive: domeny w scope, SLA/limity, open vs restricted, kluczowe ryzyka prywatności.


## Guidance (skrót)

- Oddziel open data od restricted; jasno określ auth/roles/limity.  
- Utrzymuj OpenAPI i przykłady w repo; wersjonuj kontrakty.  
- Dane lokacyjne traktuj jako wrażliwe; stosuj anonimizację i retencję.  
- Zapewnij webhooki/testy/sandbox dla integratorów; monitoruj błędy i SLA.


## Checklisty Definition of Ready (DoR)

- [ ] Wymagania domen i źródła danych znane; polityka open vs restricted dostępna.  
- [ ] Narzędzia OpenAPI i gateway auth/limity gotowe; ownerzy domen wskazani.


## Checklisty Definition of Done (DoD)

- [ ] OpenAPI/przykłady/kody błędów gotowe; auth/limity i SLA opisane; sandbox działa.  
- [ ] Sekcja privacy/RODO i retencja opisana; monitoring/IR link; dokument w linkage_index; metadane aktualne.

