---
title: Regulatory Document Management
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Regulatory Document Management


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Ustalić zasady zarządzania dokumentacją regulacyjną (submission, approvals, korespondencja z regulatorami, raporty okresowe), zapewniając zgodność, audytowalność, wersjonowanie i kontrolę dostępu.


## Zakres i granice

- Obejmuje: kategorie dokumentów (submission, variation, safety, GMP/GxP, SOP), wersjonowanie i ślad audytu, kontrolę dostępu i klasyfikację, taksonomię/metadane, harmonogramy raportów, korespondencję z regulatorami, podpisy elektroniczne, retencję/legal hold, integracje z DMS/quality systems, checklisty i log zmian.  
- Poza zakresem: treść merytoryczna dossier (oddzielne dokumenty branżowe), systemy laboratoryjne (osobne procedury).


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia

- Wejścia: wymagania regulatorów (FDA/EMA/MDR itp.), polityki jakości, listy produktów/rynków, taksonomia klas dokumentów, harmonogramy raportów, role/uprawnienia.  
- Wyjścia: model metadanych i klas, matryca dostępu, workflow publikacji/approval, kalendarz regulacyjny, procedury audytu, checklisty DoR/DoD, raporty statusu.


## Założenia

- Dane master produktów/rynków są aktualne.  
- DMS wspiera e‑signature i audyt zgodny z regulacjami.  
- Zespół compliance nadzoruje proces.


## Otwarte pytania

- Czy regulator wymaga dostępu on‑line czy tylko submission?  
- Jak długo przechowywać wersje robocze?  
- Jak obsłużyć lokalne wymagania (język, format) dla wielu rynków?  
- Jak audytować komunikację e‑mail/portale regulatorów?

## Powiązania (meta)

- Key Documents: compliance_architecture_review, retention_policy, document_management_system, data_protection_compliance, quality_assurance_plan, audit_trail_monitoring.  
- Key Document Structures: klasy dokumentów, metadane, wersjonowanie/audyt, uprawnienia, workflow, harmonogramy.  
- Document Dependencies: DMS/ECM, e-signature, CMDB produktów/rynków, calendar/alerting, legal hold.


## Zależności dokumentu

Wymaga: listy produktów/rynków i wymagań regulatorów, zatwierdzonej taksonomii/metadanych, polityk retencji i dostępu, narzędzi e-signature i DMS, kalendarza raportów. Braki = brak DoR.


## Fazy cyklu życia

- Analiza wymagań regulacyjnych i klas dokumentów.  
- Projekt metadanych/uprawnień i workflow.  
- Implementacja w DMS/ECM i migracja.  
- Operacje, raportowanie, audyty.  
- Przeglądy i aktualizacje zgodności.



## Struktura sekcji (szkielet)
- Źródła i monitoring zmian regulacyjnych
- Ocena wpływu (procesy, systemy, dane, dostawcy)
- RACI i governance zmian regulacyjnych
- Plan wdrożenia (działania, terminy, zależności)
- Komunikacja (wew./zew., regulator jeśli wymagane)
- Dowody zgodności, audyt i utrzymanie rejestru
## Szybkie powiązania

- linkage_index.jsonl (regulatory/document/management)  
- document_management_system, compliance_architecture_review, audit_trail_monitoring


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

1. Zbierz wymagania regulatorów i zdefiniuj klasy/metadane.  
2. Skonfiguruj uprawnienia, workflow i e‑signature w DMS.  
3. Wprowadź kalendarz raportów i alertów; migruj dokumenty.  
4. Prowadź operacje i audyty; aktualizuj dokument i linkage_index.


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

- Submission: zgłoszenie/dossier do regulatora.  
- Variation: zmiana zatwierdzonego dossier.  
- PSUR/CSR/DSUR: przykłady raportów okresowych w farmacji.


## Przykłady użycia

- Zarządzanie dossier medycznym na wielu rynkach UE/US.  
- Obsługa variation po zmianie produkcji.  
- Przygotowanie raportów okresowych bezpieczeństwa.


## Ryzyka i ograniczenia

- Brak legal hold → ryzyko prawne.  
- Niespójne metadane → trudne audyty i wyszukiwanie.  
- Niepełny audyt → niezgodność regulacyjna.  
- Brak kalendarza → spóźnione raporty.


## Decyzje i uzasadnienia

- Wybór taksonomii i narzędzi DMS/ECM.  
- Poziom dostępu regulatora (viewer?).  
- Zakres audytu i retencji.  
- Automatyzacja alertów i integracji.


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

- Klasy dokumentów ↔ Metadane ↔ Wyszukiwanie/audyt.  
- Uprawnienia ↔ Workflow approvals ↔ E‑signature.  
- Harmonogramy ↔ Raporty ↔ Legal hold/retencja.


## Struktura sekcji

1) Zakres i wymagania regulacyjne  
2) Klasy dokumentów i metadane/taksonomia  
3) Uprawnienia i workflow (submission/approval/changes)  
4) Wersjonowanie, audyt, e‑signature  
5) Harmonogramy raportów i kalendarz regulacyjny  
6) Retencja/legal hold i polityki dostępu  
7) Integracje (DMS/quality/ECM)  
8) Ryzyka, decyzje, pytania


## Wymagane rozwinięcia

- Słownik metadanych (produkt, rynek, regulacja, status).  
- Matryca ról/uprawnień (author, reviewer, approver, regulator view).  
- Workflow submission/variation i log komunikacji z regulatorem.  
- Kalendarz raportów (PSUR/CSR/DSUR itd.) z przypomnieniami.  
- Polityka retencji/legal hold i audytowania zmian.  
- Szablony checklist dla submission i variation.


## Wymagane streszczenia

- Executive summary: zakres, rynki, harmonogramy kluczowe.  
- Skrót ról/uprawnień i klas dokumentów.


## Guidance (skrót)

- Używaj spójnej taksonomii/metadanych; każda zmiana dokumentu = nowa wersja + audyt.  
- Egzekwuj least privilege; e‑signature i pełny audit trail.  
- Zarządzaj kalendarzem raportów z alertami i właścicielami.  
- Legal hold ma najwyższy priorytet; blokuje kasowanie.  
- Synchronizuj dane produktu/rynku z master data.  
- Aktualizuj linkage_index po każdej publikacji/approval.


## Checklisty Definition of Ready (DoR)

- [ ] Taksonomia i metadane uzgodnione; lista produktów/rynków dostępna.  
- [ ] Role/uprawnienia i e‑signature skonfigurowane.  
- [ ] Kalendarz raportów/regulacji zdefiniowany.  
- [ ] Polityki retencji/legal hold zatwierdzone.  
- [ ] DMS/ECM i integracje gotowe.


## Checklisty Definition of Done (DoD)

- [ ] DMS/ECM działa z metadanymi, wersjonowaniem i e‑signature.  
- [ ] Dokumenty mają przypisane klasy i właścicieli; audyt aktywny.  
- [ ] Kalendarz raportów i alerty działają; legal hold skonfigurowane.  
- [ ] Raport statusu i linkage_index zaktualizowane.  
- [ ] Procedury audytu i przeglądów okresowych opisane.

