---
title: Monitoring Crash Rate
status: needs_content
aligned: true
aligned_rev: 3
aligned_at: 2026-02-09
aligned_by: codex
---
# Monitoring Crash Rate


## Metadane

- Właściciel: DevOps Engineer
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved



## Cel dokumentu

Monitorować i redukować wskaźnik crashy aplikacji (mobile/desktop/webview), zapewniając szybkie wykrycie i reakcję.



## Zakres i granice
- Obejmuje: źródła danych (SDK crash, RUM, logs), metryki (crash-free users/sessions, fatal/non-fatal, ANR), progi alertów, segmentację (device/OS/app version/region), triage i klasyfikację, priorytety, komunikację, rollout/rollback, raporty trendów, integrację z issue trackerem, zgodność (PII).
- Poza zakresem: testy przedrelease (link do QA/perf), architektura app (referencja).
## Użytkownicy i interesariusze
- SRE, QA, Mobile/Web Eng, Product, Support, Privacy/Security.
## Wejścia i wyjścia
- Wejścia: dane crash (SDK/RUM), release notes, feature flags, wersje app, dane device/OS, polityki PII, definiowane progi SLA, issue tracker.
- Wyjścia: dashboardy/metyki, alerty, raporty trendów, lista incydentów i defektów, decyzje rollback/hold, plan naprawczy.
## Założenia
- SDK/RUM z PII masking, monitoring i issue tracker dostępne; feature flags działają.
## Otwarte pytania
- Jakie progi dla platform (iOS/Android/Web)? 
- Jakie SLA triage i fix dla P0/P1 crashy?
## Powiązania (meta)
- Key Documents: observability_rum, release_plan, incident_response_plan, privacy_policy, mobile_web_qastrategy, feature_flag_policy.
- Key Document Structures: metryki, alerty, triage, działania, raporty.
- Document Dependencies: crash SDK/RUM, logging, issue tracker, feature flags, release data.
## Zależności dokumentu
Wymaga: SDK crash/RUM z danymi (bez PII lub z maskowaniem), konfiguracji alertów, progi SLA, mapy wersji/feature flags, issue tracker. Bez tego DoR otwarte.
## Fazy cyklu życia
- Ustalenie metryk/progów i alertów.
- Monitoring ciągły; triage incydentów crash.
- Działania: hotfix/rollback/feature flag; testy/regresja.
- Raportowanie trendów; retrospektywa i poprawa progów/instrumentacji.
## Struktura sekcji (szkielet)

1. Definicje: crash rate per session/user/release/platform; ANR/oom osobno.
2. Instrumentacja: SDK crashlytics, symbolication, build IDs, proguard/mapping.
3. Dashboardy i alerty: progi na release/region/urządzenie, error budgets, alerting.
4. Triaging: kategoryzacja (top offenders), grouping, priorytety, właściciele.
5. Release management: gates przed rolloutem, staged rollout, hotfix policy.
6. Raportowanie: trend, time-to-resolve, regresje, wpływ na retention/CSAT.


## Szybkie powiązania

- Dodaj ręcznie 2–3 kluczowe powiązania doc↔doc lub sekcja↔sekcja, korzystając z linkage_index.jsonl / content_links*.json (decyzje, ryzyka, zależności).


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

- Przeczytaj sekcje "Cel dokumentu" i "Zakres i granice" i upewnij się, że opisują Twój przypadek.
- Wypełniaj kolejne sekcje zgodnie z guidance i powiązaniami; korzystaj z kryteriów DoR/DoD w `reports/checklist_atomic.jsonl`.
- Aktualizuj statusy w checklistach (structure/clarity/links, DoR/DoD), gdy sekcje są gotowe lub oznaczone jako N/A.



## Checklisty jakości

- [ ] Crash rate zdefiniowany i mierzony per release/platforma.
- [ ] Symbolication i grouping skonfigurowane; alerty z progami ustawione.
- [ ] Proces triage i hotfix/staged rollout opisany.
- [ ] Raporty trendów i wpływu na retention/CSAT generowane.

## Definicje robocze
- Crash-free users/sessions, ANR, Fatal/Non-fatal, Regression, Rollback, Feature flag.
## Przykłady użycia
- Release mobile: crash-free spada <98% → alert → rollback/flag → hotfix.
- Web: spike JS errors po deploy → triage stack, feature flag off, postmortem.
## Ryzyka i ograniczenia
- Brak segmentacji → błędne priorytety; brak privacy → ryzyko danych; brak alertów → długi MTTR.
## Decyzje i uzasadnienia

- [Decyzja 1 — uzasadnienie, alternatywy odrzucone, data]
- [Decyzja 2 — uzasadnienie, alternatywy odrzucone, data]

## Powiązania z innymi dokumentami
- Observability RUM, Release Plan, Incident Response, Privacy Policy, QA Strategy, Feature Flag Policy.
## Powiązania z sekcjami innych dokumentów
- Privacy → PII maskowanie; Release → progi i rollback; Incident Response → eskalacje.
## Słownik pojęć w dokumencie
- Crash-free, ANR, Fatal/Non-fatal, Regression, Rollback, Feature flag.
## Wymagane odwołania do standardów
- Polityki privacy/PII, SLA organizacyjne.
## Mapa relacji sekcja→sekcja
- Metryki → Alerty → Triage → Działania → Raporty → Udoskonalenia.
## Mapa relacji dokument→dokument
- Crash Monitoring → Release/Incident/Privacy → QA/Feature Flags.
## Ścieżki informacji
- Metryki → Alert → Triage → Działania → Raport → Korekta progów.
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
- Dashboardy crash, alert config, issue tracker tickets, raporty, release notes.
## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji
- SRE/QA → Eng/Product → Privacy/Security (dla PII) → Owner sign‑off.
## Metryki jakości
- Crash-free %, ANR %, MTTR crash, liczba rollbacków/hotfixów, liczba regresji crash per release, czas reakcji na P0 crash.
## Kryteria ukończenia
- [ ] Monitoring/alerty/triage gotowe; działania i raporty opisane; dokument w linkage_index.
- [ ] Wersja/data/właściciel aktualne.
