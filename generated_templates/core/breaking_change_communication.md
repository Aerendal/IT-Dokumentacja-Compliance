---
title: Breaking Change Communication
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Breaking Change Communication


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Zapewnić spójną komunikację zmian niezgodnych wstecz (breaking changes) do klientów/partnerów/użytkowników: kto, kiedy, jak, z jakim wsparciem i ścieżką migracji.


## Zakres i granice

- Obejmuje: identyfikację breaking change, segmentację odbiorców, timeline komunikacji (pre‑notice, notice, cutoff), kanały (email, status page, release notes, deprecation headers), materiały migracyjne (guide, sample code), wersjonowanie i fallback, wsparcie (SLA, office hours), monitoring adopcji, decyzje rollback.  
- Poza zakresem: zmiany kompatybilne wstecz (regularne release notes).


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

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

- linkage_index.jsonl (breaking/change/communication)  
- api_versioning_maintenance, documentation_publishing_plan


## Mające zastosowanie standardy i normy

### Standardy międzynarodowe
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

1. Określ wpływ i odbiorców; przygotuj timeline.  
2. Przygotuj komunikaty i materiały; opublikuj pre‑notice.  
3. Prowadź wsparcie i monitoring; przeprowadź cutoff.  
4. Raportuj wyniki/adopcję; zaktualizuj dokument i linkage_index.


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

## Powiązania sekcja↔sekcja

- Timeline ↔ Kanały ↔ Materiały migracji.  
- Wersjonowanie ↔ Fallback ↔ Rollback.  
- Monitoring adopcji ↔ SLA wsparcia ↔ Decyzje.


## Struktura sekcji

1) Opis breaking change i wpływ  
2) Timeline (pre‑notice, notice, cutoff) i kanały  
3) Wersjonowanie, fallback, polityka deprecacji  
4) Materiały migracji i wsparcie (FAQ, code, office hours)  
5) Monitoring adopcji i metryki  
6) Decyzje rollback i kryteria  
7) DoR/DoD, ryzyka, pytania


## Wymagane rozwinięcia

- Harmonogram komunikacji z datami i kanałami.  
- Szablony komunikatów (pre‑notice/notice/cutoff).  
- Przewodnik migracyjny i sample code/SDK.  
- Wersjonowanie (semver, header/path) i fallback plan.  
- Metryki adopcji (vers uptake, error rate) i progi rollback.  
- Raport końcowy i lessons learned.


## Wymagane streszczenia

- Executive summary: co się zmienia, dla kogo, do kiedy.  
- Skrót timeline i kanałów.


## Guidance (skrót)

- Komunikuj wcześnie i wieloma kanałami; jasne daty.  
- Zapewnij migracja guide + sample + FAQ; promuj ścieżkę testową.  
- Monitoruj adopcję i błędy; rozważ wydłużenie terminu przy problemach.  
- Miej fallback/rollback; dokumentuj decyzje.  
- Aktualizuj linkage_index po publikacjach.


## Checklisty Definition of Ready (DoR)

- [ ] Breaking change potwierdzony; wersjonowanie ustalone.  
- [ ] Lista odbiorców i kanałów dostępna.  
- [ ] Materiały migracyjne zaplanowane; właściciele.  
- [ ] Daty pre‑notice/notice/cutoff uzgodnione.  
- [ ] Monitoring adopcji/metryk skonfigurowany.


## Checklisty Definition of Done (DoD)

- [ ] Komunikaty wysłane; materiały opublikowane.  
- [ ] Adopcja monitorowana; błędy w normie lub plan działań.  
- [ ] Cutoff wykonany; fallback/rollback zgodnie z decyzją.  
- [ ] Raport końcowy i linkage_index zaktualizowane.  
- [ ] Lessons learned zapisane.

