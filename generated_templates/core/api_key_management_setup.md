---
title: API Key Management Setup
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# API Key Management Setup


## Metadane

- Właściciel: Backend Developer
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved
- Środowiska: [dev/test/stage/prod]


## Cel dokumentu

Opisać wdrożenie i migrację zarządzania kluczami API (wydawanie, rotacja, odwołanie, audyt) wraz z konfiguracją gateway/portal, testami i rollbackiem, aby zapewnić bezpieczne i kontrolowane dostępy do API.


## Zakres i granice

- Zakres: issuance/rotacja/revokacja, format kluczy, uprawnienia/limity, przechowywanie (KMS/Vault), ekspozycja w portalach, obserwowalność i audyt, migracja legacy, BCP/DR dla kluczy.
- Poza zakresem: długoterminowa strategia auth (oddzielny dokument), kod usług korzystających z kluczy.


## Użytkownicy i interesariusze
- **Backend Developer / API Owner** — projektuje i implementuje interfejs API
- **Frontend Developer / Consumer** — integruje się z API i zgłasza wymagania
- **Integration Architect** — definiuje standardy integracji i kontrakt API
- **QA Engineer** — weryfikuje kontrakty i scenariusze błędów

## Wejścia i wyjścia
- Wejścia: cele biznesowe, brief produktowy, regulacje, istniejące procesy/systemy, dane referencyjne.
- Wyjścia: uporządkowana lista wymagań z priorytetami, kryteriami akceptacji i powiązaniem z testami/architekturą.
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
- Elicytacja i warsztaty.
- Konsolidacja i priorytetyzacja.
- Walidacja z interesariuszami (biznes/arch/security/legal).
- Traceability do backlogu/testów.
## Struktura sekcji (szkielet)

1. Cel i zakres wdrożenia; lista usług/klientów objętych.
2. Architektura i przepływy (wydanie, rotacja, revokacja, audyt; KMS/Vault; portal).
3. Plan migracji/rollout (pilot → fala → pełne; okna, freeze, feature flags).
4. Plan testów i kryteria go/no‑go (funkcjonalne, bezpieczeństwo, regresja).
5. Observability i audyt (logi, metryki, alerty, ścieżka audytu).
6. Rollback/contingency i komunikacja (status page, klienci, wewnętrzne).
7. Ryzyka, zależności i RACI.


## Szybkie powiązania
- setup-api-gateway
- fleet-management-setup
- api-management-requirements
- api-gateway-setup
- property-management-api-documentation

## Mające zastosowanie standardy i normy

### Standardy międzynarodowe
- **IEEE 830** — Zalecana Praktyka dla Specyfikacji Wymagań Oprogramowania (SRS)
- **OWASP ASVS** — Standard Weryfikacji Bezpieczeństwa Aplikacji (OWASP)
- **ISO/IEC 25010** — Model Jakości Systemu i Oprogramowania (SQuaRE)

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

- W sekcji 2 narysuj przepływy wydawania/rotacji/revokacji; podlinkuj configi KMS/Vault i gateway.
- W sekcji 3 zaplanuj migrację (shadow/canary), w sekcji 4 zdefiniuj testy i go/no‑go; w sekcji 6 opisz rollback i komunikację.
- Aktualizuj quick links i checklisty DoR/DoD w `reports/checklist_atomic.jsonl`.


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

- Wymagania bezpieczeństwa i rate limiting, modele uprawnień, lista konsumentów/planów, architektura gateway/portal, okna wdrożeniowe, narzędzia KMS/Vault.


## Wyjścia

- Plan wdrożenia/migracji (pilot → rollout), konfiguracje gateway/portal/KMS, procedury wydawania i rotacji, testy i kryteria go/no‑go, plan rollback i komunikacji.



## Szybkie powiązania (uzupełnij po zlinkowaniu)

- [ ] `linkage_index.jsonl` → `public_api_gateway.md`, `konfiguracja_rate_limiting.md`
- [ ] `linkage_index.jsonl` → `logging_and_audit_trail.md`, `audit_logging.md`
- [ ] `linkage_index.jsonl` → `security_requirements.md`, `api_change_communication.md`


## Wymagane rozwinięcia / streszczenia

- Matryca: klucz → uprawnienia/limity/plan → ważność/rotacja → właściciel.
- Szablony komunikatów dla klientów (wydanie, rotacja, revokacja, incident).
- Streszczenie ryzyk (wyciek klucza, brak rotacji, outage KMS) i planów mitigacji.


## Wymagane powiązania

- KMS/Vault, gateway/portal developerski, IdP/tenant registry, rate limiting/polityki SLA.
- Runbook incydentów kluczy (revocation, rotate‑all), testy bezpieczeństwa.


## Kryteria DoR (Definition of Ready)

- [ ] Lista konsumentów/planów i modeli uprawnień dostępna.
- [ ] Środowiska i KMS/Vault skonfigurowane do testów; okno wdrożenia uzgodnione.


## Kryteria DoD (Definition of Done)

- [ ] Przepływy wydawania/rotacji/revokacji opisane i przetestowane; configi podlinkowane.
- [ ] Rollout/migracja wykonane lub zaplanowane z datami; rollback opisany.
- [ ] Observability/audyt działa; quick links i status zaktualizowane.


## Artefakty do załączenia

- Diagramy przepływów, pliki config (gateway/portal/KMS), skrypty rotacji, checklisty wydania/odwołania, sample API responses.


## Walidacja / testy

- Testy funkcjonalne (wydanie, rotacja, revokacja), bezpieczeństwo (entropy/format, rate limit, abuse), regresja klientów (key injection), test DR KMS/Vault.
- Symulacja wycieku: revoke‑all + rotacja; walidacja logów/audytu.


## Metryki monitorowane

- Czas wydania i rotacji, odsetek kluczy po terminie, liczba revokacji/wyjątków, alerty wycieku/anomalii użycia.


## Utrzymanie i aktualizacje

- Przegląd kwartalny polityk kluczy i rotacji; test DR/BCP dla KMS/Vault.
- Rejestr zmian w `reports/change_log.jsonl`; aktualizuj quick links po każdej zmianie polityk.


## Zakończenie

Po spełnieniu DoD zaktualizuj status w Metadane, odhacz checklisty, wpisz powiązania w `linkage_index.jsonl` i `reports/checklist_atomic.jsonl`.
