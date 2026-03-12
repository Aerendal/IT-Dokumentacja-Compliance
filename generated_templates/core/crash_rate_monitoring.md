---
title: Crash Rate Monitoring
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Crash Rate Monitoring


## Metadane

- Właściciel: DevOps Engineer
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Opisuje monitoring i reakcję na crashe aplikacji (mobile/web/desktop), aby szybko redukować crash rate i wpływ na użytkowników. Definiuje metryki, progi, alerty, proces triage i raportowanie.


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
- Cel monitoringu i zakres (usługi/ścieżki)
- SLO/SLI i priorytety alertowania
- Metryki/logi/traces i źródła danych
- Alerty/reguły, progi i runbooki
- Dashboardy i testy syntetyczne
- Operacje: on-call, eskalacje, przeglądy
- Utrzymanie, budżety zdarzeń i ciągłe doskonalenie
## Szybkie powiązania

- linkage_index.jsonl (crash/monitoring)
- observability_rum, release_plan, incident_response_plan, privacy_policy, mobile_web_qastrategy, feature_flag_policy


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

1. Ustal metryki/progi i alerty; skonfiguruj SDK/logi.
2. Zdefiniuj triage/priorytety i właścicieli; powiąż z trackerem.
3. W trakcie incydentów stosuj działania (rollback/hotfix/flag); raportuj trend.
4. Aktualizuj progi po każdym release; zamknij DoR/DoD i linkage_index.


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

- Crash-free users/sessions, ANR, Fatal/Non-fatal, Regression, Rollback, Feature flag.


## Przykłady użycia

- Release mobile: crash-free spada <98% → alert → rollback/flag → hotfix.
- Web: spike JS errors po deploy → triage stack, feature flag off, postmortem.


## Ryzyka i ograniczenia

- Brak segmentacji → błędne priorytety; brak privacy → ryzyko danych; brak alertów → długi MTTR.


## Decyzje i uzasadnienia

- [Decyzja] Progi crash-free/ANR — uzasadnienie SLA/UX.
- [Decyzja] Polityka rollback vs. hotfix — uzasadnienie ryzyka/latency.


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

- [ ] Progi/metyki spójne z SLA; alerty działają; privacy spełnione.
- [ ] Relacje cross‑doc opisane; dokument w linkage_index.


## Lista kontrolna spójności relacji

- [ ] Każdy alert ma próg/owner; każdy crash regression ma ticket/owner.
- [ ] Każdy rollout ma warunki rollback/flag; relacje cross‑doc opisane.


## Artefakty powiązane

- Dashboardy crash, alert config, issue tracker tickets, raporty, release notes.


## Ścieżka decyzji

- [Decyzja] → [Uzasadnienie] → [Konsekwencje] → [Właściciel] → [Data].


## Ścieżka akceptacji

- SRE/QA → Eng/Product → Privacy/Security (dla PII) → Owner sign‑off.


## Metryki jakości

- Crash-free %, ANR %, MTTR crash, liczba rollbacków/hotfixów, liczba regresji crash per release, czas reakcji na P0 crash.

## Kryteria ukończenia

- [ ] Monitoring/alerty/triage gotowe; działania i raporty opisane; dokument w linkage_index.
- [ ] Wersja/data/właściciel aktualne.


## Powiązania sekcja↔sekcja

- Metryki/progi → Alerty → Triage → Decyzje (rollback/hotfix) → Raporty.
- Segmentacja (device/OS/version) → Priorytety → Backlog/rollout.


## Struktura sekcji

1) Metryki i progi (crash-free %, ANR, fatal/non-fatal, release/segment)  
2) Źródła danych i PII (SDK, RUM, maskowanie)  
3) Alerty i kanały (progi, who/when)  
4) Triage i priorytety (severity, impacted users, segmenty)  
5) Działania (rollback/hotfix/flag, testy, deploy)  
6) Raporty i dashboardy (trend, top crashes, regressions)  
7) Zgodność i prywatność (PII masking, retention)  
8) Ryzyka, decyzje, open issues


## Wymagane rozwinięcia

- Definicje progów per platforma/release; mapa do SLA.
- Workflow triage (SLO czas reakcji), klasyfikacja crashy, ownership.
- Szablony raportów (release, tygodniowy), top stack traces, regresje.


## Wymagane streszczenia

- Aktualne crash-free %, top 3 regresje, decyzje (hotfix/rollback) i status.


## Guidance (skrót)

- Monitoruj crash-free users/sessions i ANR; ustaw progi per release/platforma.
- Segmentuj po OS/device/region/version/flag; priorytetyzuj fatal/regresje.
- Automatyzuj alerty i linki do issue tracker; loguj decyzje rollback/hotfix.
- Respektuj privacy: maskuj PII, minimalna retencja crash logs.


## Checklisty Definition of Ready (DoR)

- [ ] Metryki/progi i SLA zdefiniowane; SDK/RUM wdrożone; PII maskowanie ustawione.
- [ ] Kanały alertów i triage/owners ustalone; issue tracker podłączony.
- [ ] Struktura sekcji wypełniona/N/A.


## Checklisty Definition of Done (DoD)

- [ ] Alerty działają; triage/ownership opisane; raporty dostępne.
- [ ] Działania (rollback/hotfix/flag) opisane; privacy/retencja spełnione.
- [ ] Dokument w linkage_index; wersja/data/właściciel aktualne.

