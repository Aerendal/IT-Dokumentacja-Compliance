---
title: Access Change Notification
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Access Change Notification


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Ustalić procedurę informowania o zmianach dostępu (nadanie, odebranie, zmiana roli) dla użytkowników i systemów, aby zachować zgodność, audytowalność i minimalizować ryzyko nieautoryzowanego dostępu.


## Zakres i granice

- Obejmuje: kanały notyfikacji (email/ticket/webhook), typy zmian (joiner/mover/leaver, uprzywilejowane), SLA powiadomień, integracje z IAM/HRIS, logowanie i audyt, szablony komunikatów, zatwierdzenia, wyjątki, monitoring i raporty.  
- Poza zakresem: pełny proces JML (osobny dokument), konfiguracja narzędzi IAM.


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia

- Wejścia: zgłoszenia JML, zmiany ról w HRIS/IAM, polityki SoD, lista odbiorców (manager, data owner, security), wymagania audytu.  
- Wyjścia: potwierdzone notyfikacje, logi/audyt, checklisty DoR/DoD, raporty zmian dostępu, wzory komunikatów, SLA spełnione.


## Założenia

- IAM/HRIS ma eventy zmian.  
- SIEM/monitoring dostępny.  
- Zespół ma właścicieli danych/systemów.


## Otwarte pytania

- Jak obsłużyć systemy offline/legacy bez eventów?  
- Jak długo przechowywać logi notyfikacji?  
- Czy potrzebne są powiadomienia do klientów/partnerów?

## Powiązania (meta)

- Key Documents: access_control_policy, access_review_procedure, incident_response_playbook, security_controls_reference, change_management.  
- Key Document Structures: typy zmian, kanały, SLA, logi/audyt, wyjątki.  
- Document Dependencies: IAM/IDP, HRIS, ticketing, SIEM, email/webhook service.


## Zależności dokumentu

Wymaga: zintegrowanego IAM/HRIS, listy właścicieli danych/systemów, polityk SoD, szablonów komunikatów, kanałów notyfikacji i SIEM/logów. Brak = brak DoR.


## Fazy cyklu życia

- Detekcja zmiany (HRIS/IAM/ticket).  
- Generacja i wysyłka notyfikacji.  
- Logowanie/audyt i eskalacje.  
- Raportowanie i przeglądy SLA.  
- Ulepszenia procesu.



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

- linkage_index.jsonl (access/change/notification)  
- access_review_procedure, access_control_policy, security_controls_reference


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

1. Zmapuj typy zmian i odbiorców; ustaw SLA i kanały.  
2. Skonfiguruj szablony i automaty z IAM/HRIS/ticketing.  
3. Monitoruj i raportuj SLA; obsługuj wyjątki.  
4. Aktualizuj dokument i linkage_index po audytach/lekcjach learned.


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

- SLA notyfikacji: maksymalny czas od zmiany do powiadomienia.  
- SoD: Separation of Duties.  
- SIEM: system zbierania i korelacji logów.


## Przykłady użycia

- Nadanie roli admina w systemie finansowym → powiadomienie data owner + security.  
- Offboarding pracownika → notyfikacje o revokacji kont w krytycznych systemach.  
- Zmiana zespołu (mover) → update dostępu i powiadomienie nowych właścicieli.


## Ryzyka i ograniczenia

- Opóźnione notyfikacje → ryzyko nadużyć.  
- Brak logów → niepowodzenie audytu.  
- Niedokładne odbiorniki → brak świadomości właścicieli.  
- Błędy integracji → brak powiadomień.


## Decyzje i uzasadnienia

- SLA i kanały (email/webhook/ticket).  
- Zakres logowania i retencji.  
- Kto akceptuje wyjątki i eskalacje.  
- Priorytety powiadomień uprzywilejowanych.


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

- Typy zmian ↔ SLA ↔ Odbiorcy.  
- Notyfikacje ↔ Logi/audyt ↔ Raporty.  
- Wyjątki ↔ Zatwierdzenia ↔ Incydenty.


## Struktura sekcji

1) Typy zmian dostępu i odbiorcy  
2) SLA i kanały notyfikacji  
3) Szablony komunikatów i wymagane dane  
4) Logowanie, audyt i SIEM  
5) Wyjątki i eskalacje  
6) Raporty i przeglądy okresowe  
7) DoR/DoD, ryzyka, pytania


## Wymagane rozwinięcia

- Matryca: typ zmiany → odbiorcy → kanał → SLA.  
- Szablony komunikatów (grant/revoke/role change).  
- Integracja z SIEM/logami i retention.  
- Procedura wyjątków i ręcznych notyfikacji.  
- Raport miesięczny (liczba zmian, SLA, wyjątki).  
- Kontrole SoD i powiadomienia o uprzywilejowanych.


## Wymagane streszczenia

- Executive summary: SLA i główne kanały.  
- Skrót raportu ostatniego okresu (SLA, wyjątki).


## Guidance (skrót)

- Automatyzuj notyfikacje z IAM/HRIS; minimalizuj ręczne kroki.  
- Utrzymuj czytelne szablony z kontekstem (kto, co, kiedy, system).  
- Loguj każdą zmianę i notyfikację; integruj z SIEM.  
- Monitoruj SLA; eskaluj spóźnienia.  
- Sprawdzaj SoD dla zmian uprzywilejowanych.  
- Aktualizuj linkage_index po zmianach procesu.


## Checklisty Definition of Ready (DoR)

- [ ] Kanały notyfikacji i SIEM dostępne.  
- [ ] Matryca typów zmian/odbiorców gotowa.  
- [ ] Szablony komunikatów zatwierdzone.  
- [ ] Polityki SoD i wyjątki zdefiniowane.  
- [ ] Integracje IAM/HRIS działają.


## Checklisty Definition of Done (DoD)

- [ ] Notyfikacje działają wg SLA; logi kompletne.  
- [ ] Raport okresowy opublikowany; wyjątki obsłużone.  
- [ ] linkage_index zaktualizowany; audyt zgodny.  
- [ ] Brak krytycznych opóźnień/eskalacji otwartych.  
- [ ] Szablony/odbiorcy aktualni po zmianach organizacyjnych.

