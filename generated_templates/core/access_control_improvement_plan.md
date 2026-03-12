---
title: Access Control Improvement Plan
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Access Control Improvement Plan


## Metadane

- Właściciel: Project Manager
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved

> Powiązania: linkage_index.jsonl


## Cel dokumentu

Plan podniesienia dojrzałości kontroli dostępu: roadmapa zmian w rolach/atrybutach, macierzach, procesach JML, SoD, narzędziach IAM/IdP, audycie i recertyfikacjach, z KPI postępu i odpowiedzialnościami.


## Zakres i granice

- Obejmuje: backlog usprawnień AC (role/atrybuty, macierze, SoD, workflow JML, recertyfikacje, automatyzacje, audyt/logi), priorytety i harmonogram, KPI/KRI, ryzyka i wyjątki, budżet/narzędzia.
- Poza zakresem: bieżąca operacja przydzielania uprawnień (opis w procedurach operacyjnych), zmiany produktowe niezwiązane z AC.


## Użytkownicy i interesariusze
- **Project Manager** — prowadzi projekt, raportuje status i zarządza ryzykami
- **Project Sponsor** — akceptuje kluczowe decyzje i zapewnia zasoby
- **Development Team** — realizuje zadania zgodnie z planem
- **Stakeholders / Interesariusze** — odbierają raportowanie i zgłaszają zmiany zakresu

## Wejścia i wyjścia

- Wejścia: ocena dojrzałości AC, wyniki audytów/SoD recerts, gap analysis, ryzyka z risk register, wymagania regulatorów (SOX/PCI/RODO), incydenty, backlog techniczny IAM.
- Wyjścia: plan działań (owner, termin, KPI), harmonogram fal, lista zależności i ryzyk, plan testów i audytów, raport postępu.


## Założenia

- [Założenie 1 — co przyjmujemy za prawdziwe bez weryfikacji]
- [Założenie 2 — warunki brzegowe, które muszą być spełnione]

## Otwarte pytania

- [Pytanie 1 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]
- [Pytanie 2 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]

## Powiązania (meta)

- Key Documents: access_control_goals, access_control_matrix_design, multi_factor_authentication_design, access_control_review, access_control_testing, security_controls_reference, risk_register.
- Dependencies: IdP/IAM, CMDB/asset, HR/JML, ticketing/workflow, SIEM/logi, SoD rules, audyt harmonogram.


## Zależności dokumentu

- Upstream: oceny/audyty/recerts/SoD, risk register, wymagania regulacyjne.
- Downstream: wdrożenia w aplikacjach/IAM, recertyfikacje, audyty, komunikacja do użytkowników.
- Zewnętrzne: audytorzy/regulatorzy, dostawcy IAM/IdP.


## Fazy cyklu życia

- Ocena i priorytetyzacja.
- Planowanie i harmonogram.
- Wdrożenia falami, testy i audyty.
- Monitoring postępu, rewizje, utrzymanie.



## Struktura sekcji (szkielet)

1) Streszczenie (cele, KPI, top ryzyka, główne działania)  
2) Zakres i cele poprawy (domeny AC, SoD, automatyzacje)  
3) Gap analysis i priorytety (wysokie/średnie/niskie)  
4) Plan działań i harmonogram fal (owner, termin, zależności)  
5) KPI/KRI i mierzenie postępu (recert compliance, SoD violations, time-to-provision, UX frictions)  
6) Ryzyka i wyjątki/waivery (sunset, kompensacje)  
7) Budżet/narzędzia i zależności (IAM/IdP, workflow, SIEM)  
8) Testy i audyty (SoD, least privilege, regressje), kryteria akceptacji  
9) Komunikacja i szkolenia (kogo, kiedy, materiały)  
10) Decyzje (ADR) i otwarte pytania  


## Szybkie powiązania

- access_control_goals, access_control_matrix_design, multi_factor_authentication_design, access_control_review, access_control_testing, security_controls_reference, risk_register


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **CIS Controls v8** — Krytyczne Mechanizmy Bezpieczeństwa (CIS)
- **ISO/IEC 27001** — System Zarządzania Bezpieczeństwem Informacji (ISMS)
- **ISO/IEC 27002** — Wytyczne Praktyk Bezpieczeństwa Informacji
- **ISO/IEC 27005** — Zarządzanie Ryzykiem Bezpieczeństwa Informacji
- **NIST CSF** — Framework Cyberbezpieczeństwa NIST

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

- [ ] Czy wszystkie ścieżki informacji są zamknięte?
- [ ] Czy istnieją pętle lub sprzeczne relacje?
- [ ] Czy sekcje krytyczne mają wskazane źródła i rozwinięcia?

## Lista kontrolna spójności relacji

- [ ] Czy każda sekcja z relacją ma wskazaną sekcję źródłową?
- [ ] Czy relacje nie tworzą sprzecznych wymagań?
- [ ] Czy wszystkie wymagane standardy mają odwołania?
- [ ] Czy RACI jest kompletne dla kluczowych działań?

## Artefakty powiązane

- Backlog działań, harmonogram, KPI dashboard, waiver log, plan testów/audytów, plan komunikacji/szkoleń, ADR log.


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

- Gap/prio → działania → owner/termin → KPI → raport postępu.


## Wymagane rozwinięcia

- Backlog działań (gap → action → owner → termin → KPI/dowód); harmonogram fal.
- KPI/KRI z targetami; raport postępu; log waivers/wyjątków z sunset.
- Plan testów/audytów i recertyfikacji; plan komunikacji/szkoleń.


## Wymagane streszczenia

- Executive summary: cele, top działania, KPI, ryzyka, terminy krytyczne.
- One-pager: plan fal, KPI, właściciele, daty, ryzyka top.


## Guidance (skrót)

- DoR: ocena/gap i priorytety gotowe; wymagania regulacyjne/SoD znane; ownerzy domen; zasoby/narzędzia IAM dostępne.
- DoD: backlog z owner/termin/KPI; harmonogram; KPI/KRI i raportowanie; waivery z sunset; plan testów/audytów; metadane aktualne; dokument w linkage_index.
- Spójność: każda luka ma działanie/owner/termin; KPI mierzą postęp; waivery mają sunset; testy/audyty pokrywają SoD/least privilege.


## Checklisty Definition of Ready (DoR)

- [ ] Ocena/gap i priorytety zebrane; wymagania regulacyjne/SoD znane; ownerzy domen i narzędzia IAM dostępne.


## Checklisty Definition of Done (DoD)

- [ ] Backlog działań z owner/termin/KPI; harmonogram fal; KPI/KRI raportowane; waivery z sunset; dokument w linkage_index.

