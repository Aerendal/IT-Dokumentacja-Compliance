---
title: User Data Privacy Assessment
status: needs_content
aligned: true
aligned_rev: 7
aligned_at: 2026-02-09
aligned_by: codex
---
# User Data Privacy Assessment


## Metadane

- Właściciel: Document Owner
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved

> Powiązania: linkage_index.jsonl


## Cel dokumentu

Ocena prywatności danych użytkowników (lekka PIA) dla funkcji/systemu: identyfikacja danych/transferów, podstaw prawnych, ryzyk i środków, przed releasem lub zmianą.


## Zakres i granice

- Obejmuje: kategorie danych użytkownika, cele i podstawy prawne, notice/zgody, prawa osób (DSAR), transfery/podmioty trzecie, retencję/usuwanie, bezpieczeństwo (IAM, szyfrowanie, DLP, audyt), logi/monitoring, ryzyka i plan środków, decyzję go/conditional/no-go.
- Poza zakresem: pełne DPIA dla wysokiego ryzyka (oddzielny dokument), polityka prywatności publiczna.


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
1) Kontekst i zakres DPIA/PIA  
2) Dane i cele (kategorie, źródła, odbiorcy, minimalizacja, retencja)  
3) Podstawy prawne i notice/zgody  
4) Diagramy przepływu i transfery (kraje, podmioty, SCC/BCR, lokalizacja)  
5) Ryzyka dla osób (impact/likelihood, profilowanie/automatyzacja)  
6) Środki techniczne/organizacyjne (minimizacja, retencja, IAM, szyfrowanie, DLP, logi, DSAR, privacy by design)  
7) Plan działań i akceptacje (owner, termin, status; warunki)  
8) Decyzja go/conditional/no-go i warunki/waivery (z sunset)  
9) Raportowanie i rejestry (ROP, DPIA log, kontrakty)  
10) Ryzyka, decyzje, otwarte pytania
## Szybkie powiązania

- user-privacy-assessment
- user-data-privacy
- data-privacy-assessment
- data-privacy-impact-assessment
- data-privacy-architecture-assessment

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

## Powiązania sekcja↔sekcja

- Dane/cele/podstawa → ryzyka → środki → decyzja → rejestry/klauzule.


## Struktura sekcji

1) Zakres i opis funkcji/systemu  
2) Dane, cele i podstawy prawne, notice/zgody  
3) Transfery/podmioty trzecie i umowy (DPA/SCC/BCR)  
4) Retencja/usuwanie/deidentyfikacja  
5) Bezpieczeństwo danych (IAM, szyfrowanie, DLP, audyt, backup/DR)  
6) Prawa osób/DSAR (SLA, narzędzia, dowody)  
7) Ryzyka i środki (impact/likelihood, owner, termin)  
8) Decyzja go/conditional/no-go, warunki, waivery (sunset)  
9) Rejestry/klauzule do aktualizacji (ROP/DPIA log, notice)  
10) Ryzyka, decyzje (ADR), otwarte pytania  


## Wymagane rozwinięcia

- Tabela ryzyk i środków (owner, termin, dowód); lista transferów/umów; retencja; DSAR/notice; bezpieczeństwo.
- Plan działań i warunki decyzji; log waivers z sunset.


## Wymagane streszczenia

- Executive summary: dane/cele, top ryzyka, środki, decyzja/warunki.
- One-pager: dane/transfery, środki kluczowe, decyzja.


## Guidance (skrót)

- DoR: opis danych/DFD/transferów, podstawy prawne, umowy, polityki retencji/bezpieczeństwa, DSAR/consent narzędzia; ownerzy domen.
- DoD: ryzyka/środki opisane; decyzja go/conditional/no-go; rejestry/klauzule zaktualizowane; waivery z sunset; metadane aktualne; dokument w linkage_index.
- Spójność: każda kategoria danych ma cel/podstawę/retencję/środek; transfery i umowy są pokryte; DSAR/notice/retencja mają SLA/logi; warunki decyzji są mierzalne.

