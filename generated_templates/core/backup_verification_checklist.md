---
title: Backup Verification Checklist
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Backup Verification Checklist


## Metadane

- Właściciel: Document Owner
- Wersja: v0.3
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved
- Zakres systemów/danych: [lista]


## Cel dokumentu

Operacyjna checklista weryfikacji backupów: potwierdza RPO/RTO, integralność i odtwarzalność danych oraz kompletność dowodów dla audytu/regulatora.


## Zakres i granice

- Zakres: istnienie/świeżość backupów, testy restore (full/partial/PITR, ransomware/tampering), integralność danych, dostęp/klucze KMS/HSM, monitorowanie/alerty, dowody i action items.
- Poza zakresem: projekt architektury backup/DR (oddzielne dokumenty).


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia
- Wejścia: plan audytu, standardy (ISO/SOC/PCI/GxP), polityki i procedury, listy systemów, wcześniejsze wyniki audytów, ryzyka, zakres procesów.  
- Wyjścia: wypełniona checklista, zebrane dowody, lista wyjątków i obserwacji, działania korygujące, raport audytu, checklisty DoR/DoD.
## Założenia

- [Założenie 1 — co przyjmujemy za prawdziwe bez weryfikacji]
- [Założenie 2 — warunki brzegowe, które muszą być spełnione]

## Otwarte pytania

- [Pytanie 1 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]
- [Pytanie 2 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]

## Powiązania (meta)
- Key Documents: compliance_architecture_review, security_controls_reference, data_protection_compliance, incident_response_playbook, change_management.  
- Key Document Structures: przygotowanie, dowody, pytania, próbki, wyjątki, raport.  
- Document Dependencies: CMDB/system inventory, ticketing, logi/audyt, policy repo.
## Zależności dokumentu
Wymaga: zdefiniowanego zakresu i standardów, listy systemów/procesów, dostępnych logów i dowodów, narzędzi do zbierania próbek, harmonogramu audytu. Brak = brak DoR.
## Fazy cyklu życia
- Przygotowanie (zakres, kryteria, dokumenty).  
- Zbieranie dowodów i sampling.  
- Testy kontroli i pytania.  
- Raport i działania korygujące.  
- Follow-up i zamknięcie.
## Struktura sekcji (szkielet)
1. Zakres systemów/danych i typy backupów.
2. Scenariusze weryfikacji restore (pełne, częściowe, PITR, detekcja manipulacji).
3. Kryteria akceptacji (RPO/RTO, integralność, spójność, zgodność regulacyjna).
4. Procedura testu i środowisko (dostępy, klucze, separacja danych testowych).
5. Raportowanie wyników i remediacja (action items, właściciele, terminy).
6. Harmonogram weryfikacji (częstotliwość per klasa danych/usługi, wymagania audytu).
7. Dowody i audyt (logi, checksumy, raporty, ticketing).
## Szybkie powiązania
- backup-verification
- security-checklist
- reproducibility-checklist
- procurement-checklist
- mtls-verification

## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **IEEE 829** — Dokumentacja Testowania Oprogramowania i Systemów
- **ISO 22301** — System Zarządzania Ciągłością Działania (BCMS)
- **ISO 9001** — System Zarządzania Jakością (QMS)
- **ISO/IEC 25010** — Model Jakości Systemu i Oprogramowania (SQuaRE)
- **ISO/IEC 27001** — System Zarządzania Bezpieczeństwem Informacji (ISMS)
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

1. Przygotuj plan backup/RPO/RTO, scenariusze i środowisko testowe.  
2. Wykonaj testy restore, zaznacz punkty kontrolne, zapisz dowody.  
3. Utwórz action items/waivery, zaplanuj retest i follow‑up; zaktualizuj quick links i checklisty w `reports/checklist_atomic.jsonl`.


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

- Harmonogram/plan backupów, cele RPO/RTO, lista systemów/danych krytycznych, procedury restore, klucze KMS/HSM, logi backup/monitoring, wymagania audytu/regulatora.


## Wyjścia

- Wypełniona checklista, dowody z testów, lista braków/action items z owner/ETA, decyzja go/conditional/no‑go dla wzorca backupu, quick links w `linkage_index.jsonl`.


## Punkty kontroli

- [ ] Backupy istnieją dla wszystkich systemów/krytycznych danych; retencja/lokalizacje zgodne z planem.
- [ ] Świeżość zgodna z harmonogramem; RPO spełnione.
- [ ] Test restore wykonany (full/partial/PITR); scenariusz ransomware/tampering uwzględniony.
- [ ] Integralność danych po restore (checksums, spójność aplikacyjna/DB).
- [ ] Czas odtwarzania zmierzony i ≤ RTO; RPO potwierdzone.
- [ ] Dokumentacja restore aktualna; ścieżka do kluczy KMS/HSM sprawdzona.
- [ ] Dostępy do backupów/kluczy zabezpieczone (IAM/least privilege); audyt logów.
- [ ] Monitorowanie/alerty backupu działają; brakujące alerty zapisane.
- [ ] Dowody z testu zapisane (logi, checksumy, zrzuty, ticket); lokalizacja wskazana.
- [ ] Braki/action items mają ownera i termin; waiver (jeśli RPO/RTO niespełnione) z sunset/kompensacją; follow‑up zaplanowany.


## Szybkie powiązania (uzupełnij po zlinkowaniu)

- [ ] `linkage_index.jsonl` → `backup_verification.md`, `checklista_weryfikacji_backupow.md`
- [ ] `linkage_index.jsonl` → `backup_and_recovery_testing.md`, `backup_and_recovery_reference.md`
- [ ] `linkage_index.jsonl` → `backup_and_disaster_recovery.md`, `security_controls_reference.md`


## Wymagane rozwinięcia / streszczenia

- Progi RPO/RTO per system, format dowodów, scenariusze testów i częstotliwość retestów.
- Streszczenie: spełnienie RPO/RTO, główne braki, action items i terminy.


## Wymagane powiązania

- System backup/restore, KMS/HSM, monitoring/alerty, ticketing/audyt, DRP/BCP.


## Kryteria DoR (Definition of Ready)

- [ ] Plan backup/retencji i cele RPO/RTO dostępne; lista systemów/danych krytycznych gotowa.
- [ ] Procedury restore i scenariusze testowe opisane; klucze KMS/HSM dostępne.
- [ ] Miejsce na dowody i ticket audytowy ustalone.


## Kryteria DoD (Definition of Done)

- [ ] Checklist wypełniona; RPO/RTO zmierzone; integralność potwierdzona.
- [ ] Dowody zapisane i podlinkowane; action items/waivery z owner/ETA; follow‑up ustawiony.
- [ ] Quick links i status w repo/DB zaktualizowane; checklisty DoR/DoD odhaczone.


## Artefakty do załączenia

- Logi/raporty restore, checksums, screenshoty, ticket audytowy, lista action items, waiver log, ADR log.


## Walidacja / testy

- Testy restore (full/partial/PITR/ransomware), weryfikacja integralności i czasu RPO/RTO.
- Audyt dostępu do backupów/kluczy; sprawdzenie alertów i logów backupu.


## Metryki monitorowane

- Spełnienie RPO/RTO, czas odtwarzania, % testów z dowodami, liczba waiverów i czas ich zamknięcia, liczba krytycznych action items otwartych.


## Utrzymanie i aktualizacje

- Przegląd po każdym cyklu testów lub kwartalnie; rejestr zmian w `reports/change_log.jsonl`.
- Aktualizacja quick links po każdej iteracji testów.


## Zakończenie

Po spełnieniu DoD zaktualizuj status w Metadane, odhacz checklisty, dodaj powiązania w `linkage_index.jsonl` oraz wpis w `reports/checklist_atomic.jsonl`.

