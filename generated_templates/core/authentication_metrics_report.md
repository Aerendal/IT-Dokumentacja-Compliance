---
title: Authentication Metrics Report
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Authentication Metrics Report


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Raport metryk uwierzytelniania: skuteczność, bezpieczeństwo, UX i niezawodność. Ma służyć decyzjom o poprawkach, ryzykach i priorytetach backlogu.


## Zakres i granice

- Obejmuje: metryki sukcesu logowania/SSO/MFA, błędy i przyczyny (credential/OTP/device), fraud/suspicious logins, latency/availability, UX (drop-off, step-up), urządzenia/regiony, adopcję MFA, recovery/reset, alerty i SLA.  
- Poza zakresem: pełne runbooki incidentów bezpieczeństwa (linkowane).


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia

- Wejścia: logi auth/IdP, metryki API, eventy risk/fraud, dane urządzeń/regionów, konfiguracje polityk, release notes, zgłoszenia support.  
- Wyjścia: dashboard/raport (trend), główne przyczyny, rekomendacje, decyzje go/conditional/no-go na zmiany, status SLA/SLO, checklisty DoR/DoD.


## Założenia

- Stabilne logi i monitoring.  
- Dostęp do IdP danych.  
- Zespół ma czas na review.


## Otwarte pytania

- Jak raportować do klientów B2B?  
- Jak długo trzymać logi auth (privacy)?  
- Czy potrzebne metryki passkeys/WebAuthn osobno?


## Powiązania (meta)

- Key Documents: identity_architecture, mfa_adoption_plan, login_error_handling, fraud_detection_strategy, observability_plan, incident_response_runbook.  
- Key Document Structures: sukces/błędy, UX, bezpieczeństwo, wydajność, segmenty, rekomendacje.  
- Document Dependencies: IdP/IdaaS, logging/metrics, risk engine, ticketing/support, feature flags.


## Zależności dokumentu

Wymaga: spójnych logów auth, definicji metryk/SLO, segmentów (region/device/app), polityk MFA/risk, dostępu do dashboardów, danych support. Braki = DoR otwarte.


## Fazy cyklu życia

- Zbieranie danych i generacja raportu.  
- Review i decyzje.  
- Wdrożenie rekomendacji.  
- Retrospektywa i aktualizacja metryk.



## Struktura sekcji (szkielet)
- Zakres raportu i okres
- Definicje metryk/KPI i źródła danych
- Wyniki z trendami i wizualizacjami
- Insighty i obserwacje
- Ryzyka/odchylenia i ich wpływ
- Rekomendacje i plan działań z właścicielami
- Załączniki/metodologia
## Szybkie powiązania

- linkage_index.jsonl (authentication/metrics/report)  
- identity_architecture, mfa_adoption_plan, login_error_handling, observability_plan


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **CIS Controls v8** — Krytyczne Mechanizmy Bezpieczeństwa (CIS)
- **IEEE 829** — Dokumentacja Testowania Oprogramowania i Systemów
- **ISO 9001** — System Zarządzania Jakością (QMS)
- **ISO/IEC 25010** — Model Jakości Systemu i Oprogramowania (SQuaRE)
- **ISO/IEC 27001** — System Zarządzania Bezpieczeństwem Informacji (ISMS)
- **ISO/IEC 27002** — Wytyczne Praktyk Bezpieczeństwa Informacji
- **ISO/IEC 27005** — Zarządzanie Ryzykiem Bezpieczeństwa Informacji
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

1. Zbierz dane, wygeneruj metryki/segmenty.  
2. Wypełnij sekcje i rekomendacje; uzgodnij decyzje.  
3. Monitoruj wdrożenia, aktualizuj DoR/DoD i linkage_index.


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

- Success rate: % zakończonych flow auth.  
- MFA adoption: % użytkowników/flow z MFA.  
- SLO auth: cel dla latency/success.


## Przykłady użycia

- Raport tygodniowy auth dla zarządu.  
- Analiza spadku success po zmianie polityki.  
- Monitorowanie rollout MFA i impact na UX.


## Ryzyka i ograniczenia

- Brak spójnych logów → błędne metryki.  
- Zbyt wiele segmentów → szum.  
- Brak korelacji z release → trudne RCA.


## Decyzje i uzasadnienia

- Progi SLO/SLA.  
- Segmenty obowiązkowe.  
- Polityki retry/lockout.


## Powiązania z innymi dokumentami

- login_error_handling — kody błędów.  
- mfa_adoption_plan — MFA.  
- incident_response_runbook — incydenty auth.


## Powiązania z sekcjami innych dokumentów

- [Dokument X → Sekcja Y] — [powód powiązania i kierunek przepływu informacji]
- [Dokument Z → Sekcja W] — [powód powiązania i kierunek przepływu informacji]

## Słownik pojęć w dokumencie

- [Pojęcie 1] — [definicja i źródło normalizacyjne lub wewnętrzne]
- [Pojęcie 2] — [definicja i źródło normalizacyjne lub wewnętrzne]

## Wymagane odwołania do standardów

- Polityki bezpieczeństwa/PII, standardy logowania.  
- Wymogi regulatora (np. PSD2/SCA).

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

- Metryki → Rekomendacje → Backlog → Kolejne raporty.  
- Segmenty → UX/Fraud → Zmiany polityk.  
- Latency/availability → SLA/SLO → Incident response.


## Struktura sekcji

1) Podsumowanie executive (RAG, top problemy, decyzje)  
2) Metryki sukcesu/błędów (global + segmenty)  
3) MFA i recovery (adopcja, błędy, UX)  
4) Bezpieczeństwo/fraud (risk scores, suspicious, block/allow)  
5) Wydajność/availability (latency, error rate, SLO/SLA)  
6) UX/drop-off (funnel, device/region/app, A/B)  
7) Incydenty i support (ticket volume, top codes)  
8) Rekomendacje i plan działań  
9) Ryzyka, decyzje, otwarte pytania


## Wymagane rozwinięcia

- Definicje metryk i progi SLO; segmenty.  
- Tabele top błędów i przyczyn.  
- Rekomendacje i właściciele + ETA.


## Wymagane streszczenia

- Executive snapshot: RAG, top 3 problemy, rekomendacje.  
- Karta SLO/SLA auth.


## Guidance (skrót)

- Mierz zarówno sukces, jak i UX/fraud; segmentuj.  
- Koreluj błędy z release/politykami.  
- Monitoruj adopcję MFA i impact na UX.  
- Ustal progi SLO i alerty; eskaluj krytyczne spadki success rate.  
- Utrzymuj stałe definicje metryk.


## Checklisty Definition of Ready (DoR)

- [ ] Dane logów i segmentów dostępne.  
- [ ] Metryki/SLO zdefiniowane.  
- [ ] Polityki MFA/risk znane.  
- [ ] Dashboard/raport szablon gotowy.  
- [ ] Ownerzy review wyznaczeni.


## Checklisty Definition of Done (DoD)

- [ ] Raport wypełniony; status/wersja/data uzupełnione.  
- [ ] Rekomendacje z ownerami/ETA zapisane.  
- [ ] Metryki/SLO i alerty zaktualizowane.  
- [ ] Linkage_index i ticket/ALM zaktualizowane.  
- [ ] Ryzyka i decyzje udokumentowane.

