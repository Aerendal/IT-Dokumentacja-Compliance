---
title: Restaurant Onboarding Plan
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Restaurant Onboarding Plan


## Metadane

- Właściciel: Project Manager
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Zaplanować i przeprowadzić wdrożenie restauracji do platformy (marketplace/POS/delivery), zapewniając komplet danych, konfigurację systemów, szkolenia i testy, tak aby uruchomienie było szybkie i bez błędów operacyjnych.


## Zakres i granice

- Obejmuje: zbieranie danych restauracji (menu, ceny, godziny, lokalizacje), konfigurację POS/integracji, katalog produktów/variantów, zdjęcia i podatki, SLA dostaw, szkolenia personelu, testy zamówień, płatności i wydruków, checklisty jakości.  
- Poza zakresem: negocjacje handlowe/umowy (oddzielnie), marketing launch (osobny plan).


## Użytkownicy i interesariusze
- **Project Manager** — prowadzi projekt, raportuje status i zarządza ryzykami
- **Project Sponsor** — akceptuje kluczowe decyzje i zapewnia zasoby
- **Development Team** — realizuje zadania zgodnie z planem
- **Stakeholders / Interesariusze** — odbierają raportowanie i zgłaszają zmiany zakresu

## Wejścia i wyjścia

- Wejścia: dane podstawowe restauracji, menu/ingrediencje, strefy dostaw, konta bankowe, ustawienia podatków, sprzęt POS/kuchnia, SLA i zasady obsługi.  
- Wyjścia: skonfigurowany sklep/venue, integracja POS/delivery, przetestowane zamówienia (dine‑in/takeaway/delivery), szkolenia zakończone, checklisty DoR/DoD, linki do runbooków wsparcia.


## Założenia

- Restauracja dostarczy pełne dane na czas.  
- POS/vendor wspiera wymagane API.  
- Zespół ma zasoby do szkoleń i hypercare.


## Otwarte pytania

- Jak zarządzać zmianami menu po starcie (SLA na aktualizacje)?  
- Czy wymagane są lokalne języki/formaty fiskalne?  
- Jakie KPI oceniamy w pierwszych 30 dniach?

## Powiązania (meta)

- Key Documents: partner_onboarding_policy, menu_management_guidelines, payment_processing_standards, sla_catalog, support_runbook, branding_assets_guidelines.  
- Key Document Structures: dane restauracji, menu, integracje, płatności, szkolenia, testy, launch.  
- Document Dependencies: POS/integration API, payment gateway, catalog system, logistics/delivery system, ticketing/support, content studio (zdjęcia).


## Zależności dokumentu

Wymaga: podpisanej umowy, danych restauracji, dostępu do POS/integracji, zdjęć/brandingu, ustawień podatków i płatności, dostępności sprzętu (drukarki/KDS). Braki = brak DoR.


## Fazy cyklu życia

- Zbieranie danych i przygotowanie.  
- Konfiguracja systemów i treści.  
- Testy end‑to‑end i akceptacja.  
- Launch i hypercare.  
- Przekazanie do wsparcia ciągłego.



## Struktura sekcji (szkielet)
- Profil zespołu/projektów i narzędzia.
- Setup środowiska (IDE, CUDA, CLI, VPN, secrets).
- Dostępy: repo, dane, feature store, registry modeli.
- Eksperyment tracking i standardy repo (naming, review, testy).
- CI/CD modeli i deployment (batch/online).
- Bezpieczeństwo i PII (maskowanie, sandbox, licencje datasetów).
- Monitoring i observability (drift, latency, koszt, alerty).
- Runbooki i wsparcie (mentoring, slack, FAQ).
- Checklista onboarding.
## Szybkie powiązania

- linkage_index.jsonl (restaurant/onboarding/plan)  
- menu_management_guidelines, payment_processing_standards, support_runbook


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **COBIT 2019** — Kontrola nad Informacją i Technologiami (ISACA)
- **ISO/IEC 38500** — Ład Informatyczny Organizacji
- **TOGAF ADM** — Framework Architektury Korporacyjnej (The Open Group)

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

1. Zbierz dane i artefakty (menu, zdjęcia, podatki).  
2. Skonfiguruj systemy i integracje; uruchom testy e2e.  
3. Przeprowadź szkolenia; przygotuj hypercare.  
4. Launch; monitoruj i zamknij DoD, aktualizuj dokumentację.


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

- KDS: Kitchen Display System.  
- Hypercare: wzmocnione wsparcie tuż po starcie.  
- POS integration: dwukierunkowa synchronizacja zamówień i stanów.


## Przykłady użycia

- Onboarding pojedynczej restauracji franczyzowej.  
- Migracja sieci 50 lokali na wspólny POS + platformę delivery.  
- Wznowienie restauracji po rebrandingu z nowym menu.


## Ryzyka i ograniczenia

- Błędy podatków lub menu → reklamacje i straty.  
- Brak zgodności POS → utrata zamówień/druków.  
- Nieprzeszkolony personel → słaba obsługa i opinie.  
- Niewydolny hypercare → eskalacje w pierwszym tygodniu.


## Decyzje i uzasadnienia

- Wybór trybu integracji POS (pull/push/webhook).  
- Zakres hypercare i SLO.  
- Model cen/podatków dla różnych stref.  
- Priorytetyzacja publikacji (regiony/segmenty).


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

- Menu ↔ Podatki/ceny ↔ Testy zamówień.  
- Integracja POS ↔ Płatności ↔ Druk/KDS.  
- Szkolenia ↔ SLA/operacje ↔ Wsparcie.


## Struktura sekcji

1) Dane i wymagania restauracji  
2) Konfiguracja menu/cen/podatków/stref dostaw  
3) Integracja POS/płatności/drukarki/KDS  
4) Testy e2e (zamówienia, płatności, refundy, wydruki)  
5) Szkolenia personelu i materiały  
6) Launch plan i hypercare  
7) DoR/DoD, ryzyka, pytania


## Wymagane rozwinięcia

- Szablon zbierania danych (menu, alergeny, VAT, godziny).  
- Macierz integracji POS (vendor, wersja, funkcje).  
- Scenariusze testów: single item, combo, modyfikatory, refund, druk.  
- Plan hypercare: kanały wsparcia, SLO reakcji, raporty pierwszego tygodnia.  
- Materiały szkoleniowe (POS/KDS, SLA dostawy, obsługa reklamacji).  
- Checklisty jakości zdjęć i opisów.


## Wymagane streszczenia

- Executive summary: status onboarding, brakujące dane, ETA launch.  
- Skrót testów e2e i wyników.


## Guidance (skrót)

- Waliduj menu i podatki przed publikacją; testuj na środowisku stage.  
- Sprawdź wydruki i routing do kuchni dla każdej strefy/usługi.  
- Zapewnij fallback offline POS i procedurę awarii płatności.  
- Szkol personel z refundów/reklamacji; przygotuj skrypty.  
- Monitoruj pierwsze 7 dni: SLA dostawy, błędy POS, opinie klientów.  
- Aktualizuj linkage_index po każdej restauracji.


## Checklisty Definition of Ready (DoR)

- [ ] Umowa i dane restauracji kompletne.  
- [ ] Dostęp do POS/integracji i kont płatności.  
- [ ] Menu, podatki, strefy dostaw dostarczone.  
- [ ] Sprzęt (drukarki/KDS) gotowy.  
- [ ] Materiały szkoleniowe przygotowane.


## Checklisty Definition of Done (DoD)

- [ ] Testy e2e zamówień/płatności/druków zaliczone.  
- [ ] Menu i ceny opublikowane; podatki poprawne.  
- [ ] Personel przeszkolony; kontakty wsparcia przekazane.  
- [ ] Hypercare aktywne; brak krytycznych incydentów w okresie startu.  
- [ ] linkage_index i ticketingi uzupełnione.

