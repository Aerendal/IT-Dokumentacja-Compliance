---
title: Privacy Compliance Reporting
status: needs_content
aligned: true
aligned_rev: 6
aligned_at: 2026-02-09
aligned_by: codex
---
# Privacy Compliance Reporting


## Metadane

- Właściciel: Document Owner
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved
- Repo / moduł: [link]


## Cel dokumentu

Zapewnić spójny proces raportowania zgodności z przepisami o ochronie danych (RODO/GDPR, CCPA, krajowe regulacje), w tym zakres raportów, źródła danych, harmonogramy oraz odpowiedzialności.


## Zakres i granice

- Obejmuje: typy raportów (np. DPIA, rejestr czynności, incydenty, żądania podmiotów danych), częstotliwości, odbiorców, formaty, kontrolę jakości, ścieżkę audytu i archiwizację.
- Poza zakresem: szczegółowe polityki bezpieczeństwa danych, procedury reagowania na incydenty (opisane w innych dokumentach), treść polityk prywatności.


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia
- Wejścia: definicje metryk, źródła danych, okres raportowania, limity/targety, wcześniejsze raporty.
- Wyjścia: sekcja wyników z wizualizacjami, wnioski, rekomendacje i przypisane zadania.
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
- Zbieranie danych i walidacja.
- Analiza i interpretacja.
- Rekomendacje i plan działań.
- Follow-up i przegląd wyników.
## Struktura sekcji (szkielet)

- Wymogi regulacyjne i kontraktowe
- Katalog raportów (typ, cel, odbiorcy, częstotliwość)
- Źródła danych i mapowanie pól
- Procedura przygotowania i walidacji
- Ścieżka audytu, retencja, bezpieczeństwo
- SLA/terminy i eskalacje
- Ryzyka i działania korygujące
- KPI/KRI raportowania zgodności


## Szybkie powiązania

- Polityka prywatności, Incident Response (privacy), Data Retention, DPIA/DPIA register, DSAR workflow.


## Mające zastosowanie standardy i normy

### Standardy międzynarodowe
- **GDPR / RODO** — Ogólne Rozporządzenie o Ochronie Danych Osobowych (UE)
- **ISO/IEC 27701** — Zarządzanie Informacjami o Prywatności (PIMS)
- **ISO/IEC 27018** — Ochrona Danych Osobowych w Chmurze (PII)
- **COBIT 2019** — Kontrola nad Informacją i Technologiami (ISACA)
- **ISO/IEC 38500** — Ład Informatyczny Organizacji
- **ISO/IEC 27001** — System Zarządzania Bezpieczeństwem Informacji (ISMS)
- **ITIL 4** — Biblioteka Infrastruktury IT (Zarządzanie Usługami)

## Standardy i compliance
### Standardy międzynarodowe
- **GDPR / RODO** — Ogólne Rozporządzenie o Ochronie Danych Osobowych (UE)
- **ISO/IEC 27701** — Zarządzanie Informacjami o Prywatności (PIMS)
- **ISO/IEC 27018** — Ochrona Danych Osobowych w Chmurze (PII)
- **COBIT 2019** — Kontrola nad Informacją i Technologiami (ISACA)
- **ISO/IEC 38500** — Ład Informatyczny Organizacji
- **ISO/IEC 27001** — System Zarządzania Bezpieczeństwem Informacji (ISMS)
- **ITIL 4** — Biblioteka Infrastruktury IT (Zarządzanie Usługami)

## RACI i role

| Działanie | Responsible | Accountable | Consulted | Informed |
|-----------|-------------|-------------|-----------|----------|
| Tworzenie dokumentu | DEV / BA | PM | BA / ARCH | OPS / SM |
| Przegląd i zatwierdzenie | PM / BA | PM | Tech Lead | OPS |
| Aktualizacja | DEV / BA | PM | BA | OPS |
| Archiwizacja | OPS | PM | BA | SM |

## Jak używać dokumentu
- Przeczytaj sekcje "Cel dokumentu" i "Zakres i granice" i upewnij się, że opisują Twój przypadek.
- Wypełniaj kolejne sekcje zgodnie z guidance i powiązaniami; korzystaj z kryteriów DoR/DoD w `reports/checklist_atomic.jsonl`.
- Aktualizuj statusy w checklistach (structure/clarity/links, DoR/DoD), gdy sekcje są gotowe lub oznaczone jako N/A.
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

- Polityki prywatności i bezpieczeństwa, rejestr czynności przetwarzania, DPIA.
- Logi bezpieczeństwa i incydentów, DSR/DSAR, zgody/withdrawals, systemy CRM/HR/produktowe.
- Wymagania regulatorów i klauzule umów z klientami/partnerami.


## Wyjścia

- Raporty zgodności (cykliczne i ad-hoc) z metrykami i wnioskami.
- Rejestr działań naprawczych, plan usprawnień i status zgodności.
- Artefakty audytowe: ścieżka dowodowa, protokoły przeglądów, potwierdzenia wysyłki raportów.


## Jak używać (checklista)

- Zweryfikuj aktualny katalog raportów i wymagania regulatorów/klientów.
- Dla każdego raportu: uzupełnij źródła, właściciela, częstotliwość, SLA, format.
- Skonfiguruj walidacje jakości danych i podpisy aprobujące.
- Ustal retencję i kontrolę dostępu do artefaktów.
- Oznacz brakujące dane lub luki procesowe w sekcji DoR.


## Wymagane rozwinięcia / powiązania

- Linki do wzorów raportów, słownika pól, definicji metryk, polityk retencji.


## Kryteria DoR (Definition of Ready)

- Zidentyfikowane wszystkie wymagane raporty i odbiorcy.
- Mapowanie źródeł danych i właściciele zatwierdzeni.
- Ustalona częstotliwość, SLA oraz kanał publikacji.


## Kryteria DoD (Definition of Done)

- Raport wygenerowany, zweryfikowany, zatwierdzony i zarchiwizowany z pełną ścieżką audytu.
- Metryki i wnioski przekazane interesariuszom, zadania naprawcze zarejestrowane.


## Artefakty

- Szablony raportów, pliki CSV/Parquet, dashboardy BI, rejestr audytu, protokoły przeglądów.


## Walidacja

- Spójność pól z rejestrem czynności i polityką retencji.
- Kontrola kompletności (wszystkie wymagane okresy/zakresy) i poprawności danych wrażliwych.
- Podpisy: właściciel danych, DPO, security/privacy officer.


## Metryki

- % raportów dostarczonych w SLA.
- Liczba braków danych / korekt na raport.
- Czas cyklu przygotowania i weryfikacji.
- Liczba niezgodności wykrytych przez audyt.


## Utrzymanie

- Przegląd kwartalny katalogu raportów i wymogów regulacyjnych.
- Aktualizacja mapowania źródeł po zmianach systemów.
- Test procesu (tabletop) co 6 miesięcy.


## Zakończenie

Po wypełnieniu sekcji powyżej dokument stanowi referencję operacyjną do raportowania zgodności prywatności; utrzymuj go wraz ze zmianami regulacji i architektur.
