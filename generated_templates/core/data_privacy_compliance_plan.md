---
title: Data Privacy Compliance Plan
status: needs_content
aligned: true
aligned_rev: 6
aligned_at: 2026-02-09
aligned_by: codex
---
# Data Privacy Compliance Plan


## Metadane

- Właściciel: Project Manager
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved

> Powiązania: linkage_index.jsonl


## Cel dokumentu

Plan dostosowania produktu/usługi/organizacji do wymogów prywatności (GDPR/CCPA/HIPAA itp.): zakres danych, obowiązki, środki techniczne/organizacyjne, harmonogram działań i odpowiedzialności.


## Zakres i granice

- Obejmuje: kategorie danych i systemy w scope, obowiązki (informacja, zgoda, prawa osób, ROP/DPIA), podstawy prawne, transfery transgraniczne, retencję, bezpieczeństwo (IAM, szyfrowanie, DLP, audyt), procesy DSAR, rejestrowanie i dowody zgodności, harmonogram działań, ryzyka i waivery.
- Poza zakresem: pełna polityka prywatności (osobny dokument), szczegółowe DPIA (osobne dla systemów/feature).


## Użytkownicy i interesariusze
- **Project Manager** — prowadzi projekt, raportuje status i zarządza ryzykami
- **Project Sponsor** — akceptuje kluczowe decyzje i zapewnia zasoby
- **Development Team** — realizuje zadania zgodnie z planem
- **Stakeholders / Interesariusze** — odbierają raportowanie i zgłaszają zmiany zakresu

## Wejścia i wyjścia

- Wejścia: inventory danych/systemów, ROP/DPIA wyniki, polityki retencji/bezpieczeństwa, procesy DSAR/consent, listy podmiotów trzecich i umów (DPA/SCC/BCR), wymagania regulatora/klienta, gap analysis.
- Wyjścia: plan działań z ownerami/terminami, lista środków techn./org., mapa systemów w scope, aktualizacje rejestrów i klauzul, plan testów/audytów, wskaźniki postępu zgodności.


## Założenia

- [Założenie 1 — co przyjmujemy za prawdziwe bez weryfikacji]
- [Założenie 2 — warunki brzegowe, które muszą być spełnione]

## Otwarte pytania

- [Pytanie 1 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]
- [Pytanie 2 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]

## Powiązania (meta)

- Key Documents: records_of_processing, privacy_policy, data_retention_policy, data_privacy_assessment (DPIA), security_requirements, vendor_risk_assessment, incident_response_runbook, access_control_policy.
- Dependencies: CMDB/system inventory, data classification, consent/DSAR tooling, legal bases, SCC/BCR/DPA, DLP/logging/audit.


## Zależności dokumentu

- Upstream: inventory danych/systemów, ROP/DPIA, polityki retencji/bezpieczeństwa, umowy z procesorami, wymagania prawne/regulator.
- Downstream: wdrożenia środków, aktualizacje ROP/DPIA/polityk, audyty i testy, szkolenia i komunikacja.
- Zewnętrzne: procesorzy/dostawcy, organy nadzorcze, klienci z wymaganiami kontraktowymi.


## Fazy cyklu życia

- Inwentaryzacja i gap analysis.
- Planowanie działań i priorytety.
- Wdrożenia i testy/audyty.
- Utrzymanie i przeglądy (okresowe/po zmianach).



## Struktura sekcji (szkielet)

1) Streszczenie (cel, regulacje, scope, top ryzyka, plan)  
2) Scope danych/systemów i regulacji (kraje, kategorie danych, podmioty trzecie)  
3) Gap analysis (obowiązki vs stan: informacja/zgoda/prawa osób/retencja/transfery/bezpieczeństwo)  
4) Plan działań (środki techn./org., owner, termin, status, dowody)  
5) Transfery i umowy (SCC/BCR/DPA, lokalizacja, escrow/keys)  
6) DSAR/consent/procesy praw osób (SLA, narzędzia, dowody)  
7) Bezpieczeństwo i retencja (IAM, szyfrowanie, DLP, audyt, backup/DR, retencja/depers.)  
8) Testy i audyty (privacy testing, tabletop, re-assessment)  
9) Ryzyka, waivery (sunset, kompensacje), decyzje (ADR)  
10) KPI postępu i raportowanie (dashboard, cadence)  


## Szybkie powiązania

- data-privacy-compliance
- user-data-privacy
- student-data-privacy
- simulation-data-privacy
- privacy-compliance-reporting

## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **COBIT 2019** — Kontrola nad Informacją i Technologiami (ISACA)
- **GDPR / RODO** — Ogólne Rozporządzenie o Ochronie Danych Osobowych (UE)
- **ISO/IEC 27018** — Ochrona Danych Osobowych w Chmurze (PII)
- **ISO/IEC 27701** — Zarządzanie Informacjami o Prywatności (PIMS)
- **ISO/IEC 38500** — Ład Informatyczny Organizacji
- **TOGAF ADM** — Framework Architektury Korporacyjnej (The Open Group)

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
- Wypełnij sekcje według szkieletu; jeśli sekcja N/A, uzasadnij.
- Dodaj quick-links i uzupełnij checklisty DoR/DoD w reports/checklist_atomic.jsonl.
- Po review zaktualizuj metadane, artefakty i status.
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

- Gap analysis → środki/plan → owner/termin → status/postęp → audyt/dowody.


## Wymagane rozwinięcia

- Tabela gap→środek→owner→termin→dowód; priorytety wg ryzyka/regulacji.
- Lista systemów/podmiotów w scope, transferów i umów (SCC/BCR/DPA).
- Plan testów/audytów i przeglądów okresowych; plan szkoleń/komunikacji.


## Wymagane streszczenia

- Executive summary: regulacje w scope, top ryzyka/luki, plan i daty krytyczne.
- One-pager: scope, najważniejsze środki i terminy, KPI postępu.


## Guidance (skrót)

- DoR: inventory danych/systemów, regulacje w scope, gap analysis wstępna, ROP/DPIA dostępne, ownerzy domen.
- DoD: plan działań z ownerami/terminami/dowodami; umowy/transfery pokryte; KPI i raportowanie; ryzyka/waivery; metadane aktualne; dokument w linkage_index.
- Spójność: każda luka ma środek, owner, termin i dowód; transfery mają SCC/BCR/DPA; DSAR/consent mają SLA i logi; KPI postępu są mierzone.

