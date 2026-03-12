---
title: API Change Communication
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# API Change Communication


## Metadane

- Właściciel: Backend Developer
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved
- Zakres usług: [lista API]


## Cel dokumentu

Ustalić standard komunikacji zmian w API (breaking / non‑breaking / preview) tak, aby klienci i wewnętrzni konsumenci mogli bezpiecznie się dostosować, a wsparcie miało spójne instrukcje.


## Zakres i granice

- Zakres: klasyfikacja zmian, kanały (email/webhook/status page/changelog/SDK), notice periods, szablony komunikatów, harmonogram rollout/deprecation/EOL, migration guides/FAQ, monitoring adopcji, feedback i eskalacje.
- Poza zakresem: strategia wersjonowania (w `api_versioning_maintenance.md`), szczegóły bezpieczeństwa (w `design_bezpieczenstwa_api.md`).


## Użytkownicy i interesariusze
- **Backend Developer / API Owner** — projektuje i implementuje interfejs API
- **Frontend Developer / Consumer** — integruje się z API i zgłasza wymagania
- **Integration Architect** — definiuje standardy integracji i kontrakt API
- **QA Engineer** — weryfikuje kontrakty i scenariusze błędów

## Wejścia i wyjścia
- Wejścia: opis zmiany, wpływ na API/SDK/UI/dane, lista odbiorców i kontraktów, polityka wersjonowania, ryzyka, daty release/deprecation.  
- Wyjścia: plan komunikacji, harmonogram i kanały, materiały migracji, FAQ, checklisty DoR/DoD, metryki adopcji, decyzje rollback.
## Założenia
- Kanały komunikacji dostępne.  
- Zespół ma zasoby na wsparcie.  
- Monitoring adopcji jest możliwy.
## Otwarte pytania
- Jak obsłużyć klientów offline?  
- Jak długo przechowywać stare wersje?  
- Czy wymagane są podpisy/ack przy krytycznych zmianach?
## Powiązania (meta)
- Key Documents: api_versioning_maintenance, change_management, rollout_runbook, incident_response_for_customers, documentation_publishing_plan.  
- Key Document Structures: identyfikacja, timeline, kanały, materiały, wsparcie, monitoring.  
- Document Dependencies: mailing/status system, docs portal, SDK/API repo, analytics na adopcję.
## Zależności dokumentu
Wymaga: potwierdzenia breaking change i wpływu, listy odbiorców i kanałów, wersjonowania/deprecation policy, dat release/cutoff, zasobów do przygotowania materiałów i wsparcia. Brak = brak DoR.
## Fazy cyklu życia
- Identyfikacja i ocena wpływu.  
- Plan komunikacji i materiały.  
- Wysyłka pre‑notice/notice, wsparcie migracji.  
- Cutoff/rollout i monitoring adopcji.  
- Retrospektywa i aktualizacje policy.
## Struktura sekcji (szkielet)

1. Typy zmian i klasyfikacja (breaking / non‑breaking / preview) + kryteria.
2. Kanały i szablony (email, webhook payload, changelog, status page, release notes/SDK).
3. Harmonogram i notice periods (zapowiedź, deprecjacja, EOL, blackout/quiet period).
4. Wsparcie i materiały (FAQ, migration guides, sample code, contact/support runbook).
5. Monitoring adopcji i feedback (telemetria wersji, long‑tail, ankiety/tickets).
6. Załączniki (szablony komunikatów, webhook payloads, ADR/waiver log).


## Szybkie powiązania
- breaking-change-communication
- api-outage-communication
- user-communication
- sunset-communication
- release-communication

## Mające zastosowanie standardy i normy

### Standardy międzynarodowe
- **IEEE 830** — Zalecana Praktyka dla Specyfikacji Wymagań Oprogramowania (SRS)
- **OWASP ASVS** — Standard Weryfikacji Bezpieczeństwa Aplikacji (OWASP)
- **ISO/IEC 25010** — Model Jakości Systemu i Oprogramowania (SQuaRE)
- **ITIL 4** — Biblioteka Infrastruktury IT (Zarządzanie Usługami)
- **ISO 20000-1** — System Zarządzania Usługami IT (SMS)
- **COBIT 2019** — Kontrola nad Informacją i Technologiami (ISACA)

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

- Zaklasyfikuj zmianę (sekcja 1) i wybierz kanały/notice (sekcja 2–3).
- Przygotuj i opublikuj komunikaty + migration guide/FAQ (sekcja 4); ustaw monitoring adopcji (sekcja 5).
- Aktualizuj quick links i checklisty w `reports/checklist_atomic.jsonl` po każdym release.


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
- Breaking change: zmiana niekompatybilna wstecz.  
- Cutoff: data wyłączenia starej wersji.  
- Pre‑notice: wstępna informacja przed formalnym notice.
## Przykłady użycia
- Wyłączenie API v1 i przejście na v2.  
- Zmiana schematu eventów wymagająca migracji konsumentów.  
- Deprecacja SDK i zastąpienie nowym.
## Ryzyka i ograniczenia
- Niedostateczna komunikacja → przerwy u klientów.  
- Brak materiałów → niska adopcja.  
- Brak monitoringu → brak świadomości problemów.  
- Za krótki okres notice → niezadowolenie.
## Decyzje i uzasadnienia
- Długość okresu notice i cutoff.  
- Kanały obowiązkowe vs opcjonalne.  
- Progi rollback i wydłużenia notice.  
- Zakres wsparcia (office hours, SLA).
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

- Plan zmian i klasyfikacja, lista odbiorców/klientów/partnerów, telemetria użycia wersji, wymagania prawne/SLA, status page i system mailing/webhook, migration guides/SDK readiness.


## Wyjścia

- Harmonogram komunikacji i notice periods, szablony komunikatów (email/webhook/status page/changelog), migration guide/FAQ, plan wsparcia, monitor adopcji, uaktualnione quick links.



## Szybkie powiązania (uzupełnij po zlinkowaniu)

- [ ] `linkage_index.jsonl` → `api_versioning_maintenance.md`, `specyfikacja_wymagan_api.md`
- [ ] `linkage_index.jsonl` → `public_api_gateway.md`, `logging_and_audit_trail.md`
- [ ] `linkage_index.jsonl` → `api_rate_limiting_requirements.md`, `audit_logging.md`


## Wymagane rozwinięcia / streszczenia

- Definicje notice periods per change type (np. 90/180 dni dla breaking).
- Szablony komunikatów: zapowiedź, deprecjacja, EOL, rollback; webhook payload.
- Streszczenie ryzyk long‑tail i plan kontaktu (targeted outreach).


## Wymagane powiązania

- Status page, kanały mailing/webhook, registry klientów/kluczy, portal developerski/SDK.
- Telemetria wersji (dashboard), ticketing support, change management board.


## Kryteria DoR (Definition of Ready)

- [ ] Typ zmiany i odbiorcy zidentyfikowani; kanały dostępne.
- [ ] Telemetria wersji i status page gotowe; migration guide w przygotowaniu.


## Kryteria DoD (Definition of Done)

- [ ] Komunikaty wysłane/opublikowane; status page/changelog zaktualizowane; quick links uzupełnione.
- [ ] Monitoring adopcji aktywny; wsparcie/FAQ dostępne; status/metadane aktualne.
- [ ] Checklisty DoR/DoD odhaczone.


## Artefakty do załączenia

- Szablony email/webhook, status page entry, changelog, migration guide, FAQ, telemetry dashboards, ADR/waiver log.


## Walidacja / testy

- Dry‑run komunikacji i webhook payload; kontrola poprawności notice dat.
- Sprawdzenie telemetry i identyfikacji long‑tail; test ścieżki rollback komunikacji.


## Metryki monitorowane

- % klientów na docelowej wersji, czas migracji, liczba zgłoszeń na zmianę, open/click rate notice, liczba rollbacków spowodowanych komunikacją.


## Utrzymanie i aktualizacje

- Przegląd po każdym major/minor release lub kwartalnie.
- Rejestr zmian w `reports/change_log.jsonl`; aktualizacja quick links po każdej kampanii.


## Zakończenie

Po spełnieniu DoD zaktualizuj status w Metadane, odhacz checklisty, dodaj powiązania w `linkage_index.jsonl` i wpis w `reports/checklist_atomic.jsonl`.
