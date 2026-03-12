---
title: Tenant Portal User Guide
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Tenant Portal User Guide


## Metadane

- Właściciel: Technical Writer
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved
- Repo / moduł: [link]


## Cel dokumentu

Przewodnik użytkownika portalu/apki najemcy: funkcje, nawigacja, zgłoszenia, płatności i bezpieczeństwo konta.


## Zakres i granice

- Obejmuje: rejestracja/logowanie/SSO, przegląd umów/płatności, zgłoszenia serwisowe, rezerwacje (udogodnienia), komunikacja/ogłoszenia, dokumenty, bezpieczeństwo (MFA, reset hasła), preferencje, dostęp mobilny/web, wsparcie.
- Poza zakresem: procesy backoffice zarządcy (osobne dokumenty), marketing ofert.


## Użytkownicy i interesariusze
- **Technical Writer / Documentation Owner** — tworzy i utrzymuje dokumentację
- **Subject Matter Expert (SME)** — dostarcza merytoryczne treści i weryfikuje poprawność
- **Development Team** — recenzuje dokumentację techniczną
- **End Users** — korzystają z dokumentacji i zgłaszają nieścisłości

## Wejścia i wyjścia
- Wejścia: procesy najmu/rozliczeń, integracje ERP/CMMS/payments, wymagania prawne (RODO, lokalne), design system, analityka, wymagania A11y, listy funkcji i priorytetów.  
- Wyjścia: specyfikacja funkcjonalna i NFR, kontrakty API, wymagania bezpieczeństwa/PII, mapy przepływów UX, checklisty DoR/DoD, kryteria akceptacji, raport braków.
## Założenia
- Dostępny design system i integracje płatności/CMMS/ERP.  
- Zespół ma zasoby UX/BE/QA.  
- Wymagania prawne/A11y zidentyfikowane.
## Otwarte pytania
- Czy portal musi działać offline (np. mobile app)?  
- Jakie języki/lokalizacje na start?  
- Jakie KPI sukcesu (płatności online %, czas zamknięcia zgłoszeń)?
## Powiązania (meta)
- Key Documents: property_management_architecture, payments_integration, cmms_integration, privacy_policy, accessibility_compliance, communication_plan, service_level_agreement.  
- Key Document Structures: auth/profil, płatności, zgłoszenia, komunikacja, dokumenty, rezerwacje, A11y/UX, bezpieczeństwo.  
- Document Dependencies: IAM/SSO, payment gateway, CMMS, document store, notification service, analytics, CRM/ERP.
## Zależności dokumentu
Wymaga: listy integracji (payments/CMMS/ERP), wymagań prawnych/A11y, design systemu, planu komunikacji, decyzji o kanałach powiadomień, danych o SLA wsparcia. Braki = DoR otwarte.
## Fazy cyklu życia
- Zbieranie wymagań i priorytetyzacja.  
- Projektowanie UX i kontraktów API.  
- Implementacja i integracje.  
- Testy (funkcje, A11y, bezpieczeństwo) i rollout.  
- Operacje i doskonalenie.
## Struktura sekcji (szkielet)

- Start (rejestracja/logowanie/MFA/reset)
- Dashboard i główne funkcje
- Zgłoszenia serwisowe i status
- Płatności/faktury i historia
- Rezerwacje udogodnień
- Ogłoszenia/komunikacja
- Ustawienia i bezpieczeństwo konta
- FAQ i wsparcie


## Szybkie powiązania

- Real Estate Digital Transformation Strategy, Security/Privacy, Support Strategy, Payment Integration.


## Mające zastosowanie standardy i normy


### Polskie normy i regulacje
- **UODO-PL** — Ustawa o Ochronie Danych Osobowych (implementacja RODO)
- **UŚUDE-PL** — Ustawa o Świadczeniu Usług Drogą Elektroniczną

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
1. Ustal persony/scenariusze i priorytety funkcji.  
2. Zaprojektuj flow i kontrakty API; uwzględnij bezpieczeństwo/PII/A11y.  
3. Zaplanuj testy i rollout; monitoruj metryki; aktualizuj DoR/DoD i linkage_index.
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
- CMMS: system zarządzania zgłoszeniami/utrzymaniem.  
- SLA: czas reakcji/naprawy dla zgłoszeń.  
- NFR: wymagania niefunkcjonalne (wydajność, dostępność, bezpieczeństwo).
## Przykłady użycia
- Portal mieszkaniowy: płatności czynszu, zgłoszenia usterek, ogłoszenia.  
- Portal biurowy: rezerwacje sal, dostęp do dokumentów, komunikacja B2B.  
- Portal mixed‑use: media/zużycie, parking, powiadomienia kryzysowe.
## Ryzyka i ograniczenia
- Brak A11y → ryzyko prawne i wykluczenie.  
- Niewydolne powiadomienia → SLA niewidoczne dla najemcy.  
- Luki PII/prywatności → incydenty danych.
## Decyzje i uzasadnienia
- Kanały płatności i providerzy.  
- Zakres self‑service vs wsparcie manualne.  
- Zakres danych przechowywanych o najemcach.
## Powiązania z innymi dokumentami
- payments_integration — płatności.  
- cmms_integration — zgłoszenia.  
- accessibility_compliance — A11y.
## Powiązania z sekcjami innych dokumentów

- [Dokument X → Sekcja Y] — [powód powiązania i kierunek przepływu informacji]
- [Dokument Z → Sekcja W] — [powód powiązania i kierunek przepływu informacji]

## Słownik pojęć w dokumencie

- [Pojęcie 1] — [definicja i źródło normalizacyjne lub wewnętrzne]
- [Pojęcie 2] — [definicja i źródło normalizacyjne lub wewnętrzne]

## Wymagane odwołania do standardów
- RODO/PII, lokalne przepisy najmu/danych.  
- Wewnętrzne standardy bezpieczeństwa i A11y.
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

- Konfiguracja portalu, polityki bezpieczeństwa/prywatności, SLA wsparcia, ceny/usługi, kanały kontaktu.


## Wyjścia

- Instrukcje krok‑po‑kroku, FAQ, linki do wsparcia, checklisty bezpieczeństwa konta.



## Jak używać (checklista)

- Dodaj screeny i kroki dla logowania/MFA; opisz kluczowe flow (płatność, zgłoszenie, rezerwacja).
- Dodaj FAQ i kontakty wsparcia; wskaż zasady bezpieczeństwa konta.


## Wymagane rozwinięcia / powiązania

- Zrzuty ekranu, FAQ, polityka prywatności, instrukcje płatności, SLA wsparcia.


## Kryteria DoR

- Portal skonfigurowany; funkcje potwierdzone; polityki bezpieczeństwa dostępne.


## Kryteria DoD

- Kluczowe flow opisane, FAQ dodane, linki wsparcia/prywatności zamieszczone.


## Artefakty

- Guide (MD/PDF), screeny, FAQ, linki wsparcia.


## Walidacja

- Przegląd UX; test ścieżek na sandbox; sprawdzenie linków i bezpieczeństwa (MFA/reset).


## Metryki

- CSAT portalu, liczba zgłoszeń wsparcia na użytkownika, powodzenie logowania/MFA, adoption.


## Utrzymanie

- Aktualizacja przy zmianach funkcji; przegląd FAQ kwartalnie; weryfikacja screenów.


## Zakończenie

Przewodnik portalu najemcy ułatwia korzystanie i redukuje zgłoszenia; utrzymuj go z aktualnymi funkcjami i bezpieczeństwem.

