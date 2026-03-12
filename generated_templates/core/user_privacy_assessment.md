---
title: User Privacy Assessment
status: needs_content
aligned: true
aligned_rev: 6
aligned_at: 2026-02-09
aligned_by: codex
---
# User Privacy Assessment


## Metadane

- Właściciel: Document Owner
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved
- Repo / moduł: [link]


## Cel dokumentu

Przeprowadzić ocenę prywatności użytkownika (PIA/DPIA): zidentyfikować dane osobowe, ryzyka, środki ochrony i zgodność regulacyjną.


## Zakres i granice

- Obejmuje: inwentaryzację danych (PII/PIA), cel przetwarzania, podstawę prawną, minimalizację, retencję, prawa podmiotów danych, udostępnianie/transfery (w tym cross‑border), techniczne i organizacyjne środki ochrony, ocena ryzyk i plan mitigacji, konsultacje z DPO.
- Poza zakresem: szczegółowa polityka bezpieczeństwa (linkowana), pełna implementacja kontroli (osobne runbooki).


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia
- Wejścia: opis funkcji/systemu, dane/źródła, cele/podstawy prawne, DPA/SCC/BCR, polityki retencji/bezpieczeństwa, mechanizmy DSAR/consent, architektura/DFD, rejestry incydentów.
- Wyjścia: raport oceny (ryzyka/środki), plan działań z ownerami/terminami, decyzja go/conditional/no-go i warunki, aktualizacje rejestrów (ROP/DPIA log), lista umów/klauzul do uzupełnienia.
## Założenia

- [Założenie 1 — co przyjmujemy za prawdziwe bez weryfikacji]
- [Założenie 2 — warunki brzegowe, które muszą być spełnione]

## Otwarte pytania

- [Pytanie 1 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]
- [Pytanie 2 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]

## Powiązania (meta)
- Key Documents: user_data_privacy, data_privacy_assessment, data_privacy_compliance_plan, data_retention_policy, security_requirements, vendor_risk_assessment, incident_response_runbook, breach_notification_procedure, access_control_policy.
- Dependencies: data classification, DPA/SCC/BCR, DSAR/consent tools, logging/audit, architektura/DFD.
## Zależności dokumentu
- Upstream: opis funkcji/danych/DFD/transferów, podstawy prawne, umowy, polityki, narzędzia DSAR/consent.
- Downstream: wdrożenie środków, aktualizacja rejestrów/klauzul, audyty/testy, komunikacja.
- Zewnętrzne: procesorzy/dostawcy, regulator/klienci (wymogi kontraktowe).
## Fazy cyklu życia
- Identyfikacja i opis (dane/cele/podstawa).
- Ocena ryzyk/środków.
- Decyzja i plan działań.
- Aktualizacje po zmianach/incydentach.
## Struktura sekcji (szkielet)

- Zakres i cel przetwarzania
- Dane i przepływy (źródła, odbiorcy, transfery)
- Podstawa prawna i prawa użytkowników
- Minimalizacja, retencja, anonimizacja
- Środki techniczne/organizacyjne (TOC)
- Ocena ryzyk i plan mitigacji
- Konsultacje (DPO/regulator jeśli wymagane)
- Decyzje i działania


## Szybkie powiązania

- Privacy Compliance Reporting, Data Retention Policy, Security Controls, Incident/Breach Response, Vendor/Data Processing Agreements.


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **GDPR / RODO** — Ogólne Rozporządzenie o Ochronie Danych Osobowych (UE)
- **ISO/IEC 27018** — Ochrona Danych Osobowych w Chmurze (PII)
- **ISO/IEC 27701** — Zarządzanie Informacjami o Prywatności (PIMS)

### Polskie normy i regulacje
- **UODO-PL** — Ustawa o Ochronie Danych Osobowych (implementacja RODO)

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

Wypełniaj każdą sekcję zgodnie z rzeczywistym stanem dokumentowanego systemu lub projektu.
- Sekcje obowiązkowe: Cel dokumentu, Zakres i granice, Wejścia i wyjścia.
- Sekcje oznaczone [opcjonalnie] wypełnij gdy masz dane; wpisz 'Nie dotyczy' jeśli sekcja nie ma zastosowania.
- Po wypełnieniu przekaż do przeglądu zgodnie z macierzą RACI; zaktualizuj metadata (wersja, data, autor).
- Śledź zmiany przez system kontroli wersji; podlinkuj powiązane dokumenty w sekcji 'Szybkie powiązania'.

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
- Formularz DPIA/PIA, DFD/transfer maps, tabela ryzyk/środków, decyzja/akceptacje, rejestr DPIA/ROP, umowy SCC/BCR/DPA, log waivers, plan wdrożenia środków.
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

- Opis procesu/systemu, katalog danych, przepływy danych, umowy/transfery, wymagania regulacyjne (RODO/CCPA itp.), wytyczne DPO, ocena ryzyk.


## Wyjścia

- Raport PIA/DPIA: opis przetwarzania, ryzyka, środki ochrony, decyzje (go/mitigate), plan działań, rejestr konsultacji.



## Jak używać (checklista)

- Zbierz opis procesu i dane; wypełnij sekcje danych/przepływów.
- Określ podstawę prawną i prawa użytkowników; zaplanuj retencję/minimalizację.
- Oceń ryzyka; dobierz środki TOC; skonsultuj z DPO.
- Zapisz plan działań i decyzję; zarejestruj w PIA/DPIA log.


## Wymagane rozwinięcia / powiązania

- Szablon PIA/DPIA, katalog danych, mapy przepływów, matryca ryzyk, lista środków TOC, log konsultacji.


## Kryteria DoR

- Opis procesu i dane dostępne; wymagania regulacyjne zidentyfikowane; DPO zaangażowany.


## Kryteria DoD

- Raport PIA/DPIA ukończony, ryzyka i środki opisane, decyzja go/mitigate, działania zaplanowane.


## Artefakty

- Raport PIA/DPIA, mapy danych, matryca ryzyk, log konsultacji, plan działań.


## Walidacja

- Przegląd DPO; zgodność z wytycznymi regulatora; weryfikacja wdrożenia działań mitigacyjnych.


## Metryki

- Liczba PIA/DPIA w terminie, czas realizacji, liczba otwartych ryzyk, incydenty/breach w obszarze objętym PIA.


## Utrzymanie

- Przegląd przy każdej zmianie procesu/danych; roczny review; aktualizacja po incydentach/regulacjach.


## Zakończenie

Ocena prywatności zapewnia zgodność i ochronę danych użytkowników; utrzymuj ją w cyklu zmian systemu i regulacji.

