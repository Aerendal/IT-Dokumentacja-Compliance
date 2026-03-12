---
title: E-Waste Generation Monitoring
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# E-Waste Generation Monitoring


## Metadane

- Właściciel: DevOps Engineer
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Monitorować powstawanie elektroodpadów (sprzęt IT/OT) w organizacji, aby spełnić wymagania środowiskowe, optymalizować utylizację i raportować KPI zrównoważonego rozwoju.


## Zakres i granice

- Obejmuje: inwentaryzację sprzętu, cykl życia (zakup→użycie→wycofanie), klasyfikację e‑waste, proces zbiórki i magazynowania, przekazanie do recyklingu/odzysku, zgodność z przepisami (WEEE/RAEE), metryki (kg/rok, % recyklingu), raportowanie i audyt, integrację z CMDB/asset management.  
- Poza zakresem: zakupy sprzętu (osobna polityka), kontrakty z dostawcami recyklingu (oddzielne umowy).


## Użytkownicy i interesariusze
- **DevOps / Platform Engineer** — zarządza infrastrukturą i pipeline'ami wdrożeniowymi
- **SRE (Site Reliability Engineer)** — definiuje SLO/SLI i zarządza niezawodnością
- **Development Team** — dostarcza artefakty do wdrożenia
- **Security Officer** — weryfikuje zgodność wdrożeń z polityką bezpieczeństwa

## Wejścia i wyjścia

- Wejścia: CMDB/asset inventory, dane o wycofaniach, wagi/klasy sprzętu, wymagania prawne lokalne, harmonogramy odbiorów, certyfikaty recyklera.  
- Wyjścia: dashboard i raporty e‑waste, proces zbiórki i etykietowania, checklisty DoR/DoD, KPI i progi, audyt śladu, dowody recyklingu.


## Założenia

- CMDB/ITAM jest źródłem prawdy.  
- Vendorzy dostarczają certyfikaty.  
- Zespół ma zasoby do zbiórki i raportów.


## Otwarte pytania

- Jak raportować sprzęt przekazany do reuse?  
- Jak uwzględniać częściowe odzyski (baterie)?  
- Jak długo przechowywać certyfikaty?

## Powiązania (meta)

- Key Documents: e_waste_disposal_compliance, green_software_engineering, sustainability_reporting_standards, asset_update_procedure, asset_delivery_strategy.  
- Key Document Structures: inwentarz, cykl życia, zbiórka, raporty, zgodność.  
- Document Dependencies: CMDB/ITAM, recycling vendor systems, ticketing, monitoring kosztów/środowisk.


## Zależności dokumentu

Wymaga: aktualnego inwentarza sprzętu, procedury wycofań, dostawców recyklingu i ich certyfikatów, danych o wagach/klasach, wymogów prawnych lokalnych, narzędzi raportowania. Brak = brak DoR.


## Fazy cyklu życia

- Inwentaryzacja i klasyfikacja sprzętu.  
- Zbiórka/wycofanie i magazynowanie.  
- Przekazanie recyklerowi i dowody.  
- Raporty KPI i audyty.  
- Ulepszenia i prewencja (wydłużenie cyklu życia).



## Struktura sekcji (szkielet)
- SLO i device matrix.
- Sceny referencyjne i testy syntetyczne.
- Instrumentacja i eventy (FPS/frametime/stutter, HW metrics).
- Telemetria prod (sampling, priv), storage i koszty.
- Dashboardy i alerty (progi, kanały, runbook).
- Raporty wersja/build → FPS.
- Ryzyka i mitigacje.
## Szybkie powiązania

- linkage_index.jsonl (e_waste/generation/monitoring)  
- e_waste_disposal_compliance, sustainability_reporting_standards


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

1. Zbierz dane inwentarza; oznacz wycofania.  
2. Zorganizuj zbiórkę i przekazanie; zapisz wagi i certyfikaty.  
3. Raportuj KPI; koryguj procesy; aktualizuj linkage_index.  
4. Przy audycie pokaż dowody i raporty.


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

- E‑waste: zużyty sprzęt elektryczny/elektroniczny.  
- WEEE/RAEE: regulacje dot. e‑waste w UE.  
- Reuse vs recycle: ponowne użycie vs odzysk materiału.


## Przykłady użycia

- Wycofanie laptopów po wymianie floty.  
- Raport roczny e‑waste dla ESG.  
- Audyt certyfikatów recyklera.


## Ryzyka i ograniczenia

- Brak dowodów → ryzyko regulacyjne.  
- Zła klasyfikacja wag → błędne KPI.  
- Nieautoryzowany vendor → niezgodność.  
- Brak integracji z CMDB → podwójne liczenie.


## Decyzje i uzasadnienia

- Wybór vendorów i częstotliwości odbiorów.  
- Zakres KPI i progi.  
- Retencja logów/certyfikatów.  
- Polityka reuse/refurbish vs wymiana.


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

- Inwentarz ↔ Wycofanie ↔ Zbiórka → Raporty.  
- Przepisy ↔ Vendor certyfikaty ↔ Audyt.  
- KPI ↔ Budżet ↔ Cele ESG.


## Struktura sekcji

1) Inwentarz i klasyfikacja e‑waste  
2) Proces zbiórki/etykietowania i magazynowania  
3) Przekazanie do recyklingu/odzysku, certyfikaty  
4) KPI i raportowanie (kg, % reuse/recycle)  
5) Zgodność prawna i audyt  
6) Integracje (CMDB/ITAM, vendor)  
7) DoR/DoD, ryzyka, pytania


## Wymagane rozwinięcia

- Matryca kategorii e‑waste i wag.  
- Procedura etykietowania i tracking (tagi, kody).  
- Szablon raportu KPI i częstotliwość.  
- Lista wymaganych certyfikatów/dokumentów od vendorów.  
- Polityka przechowywania logów i dowodów.  
- Plan wydłużania cyklu życia (refurbish/reuse).


## Wymagane streszczenia

- Executive summary: wolumen e‑waste, % recyklingu, główne ryzyka.  
- Skrót zgodności (WEEE/RAEE) i vendorów.


## Guidance (skrót)

- Prowadź spójny inwentarz; każde wycofanie = ticket z wagą.  
- Wymagaj certyfikatów recyklera; audytuj losowo.  
- KPI: kg/rok, % reuse/recycle, koszt/ kg; monitoruj trend.  
- Integruj z CMDB/ITAM; automatyzuj oznaczanie wycofań.  
- Dokumentuj dowody i aktualizuj linkage_index.


## Checklisty Definition of Ready (DoR)

- [ ] Inwentarz aktualny; kategorie i wagi dostępne.  
- [ ] Dostawcy recyklingu i certyfikaty potwierdzone.  
- [ ] Narzędzia raportowe i ticketing gotowe.  
- [ ] Wymagania prawne zebrane.  
- [ ] Proces etykietowania uzgodniony.


## Checklisty Definition of Done (DoD)

- [ ] Wycofany sprzęt zarejestrowany; wagi i certyfikaty zebrane.  
- [ ] KPI zaktualizowane; raport opublikowany.  
- [ ] Dowody recyklingu przechowane; audyt trail kompletny.  
- [ ] linkage_index/CMDB zaktualizowane.  
- [ ] Plan usprawnień zapisany.

