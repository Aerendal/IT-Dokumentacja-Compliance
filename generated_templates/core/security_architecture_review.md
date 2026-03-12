---
title: Security Architecture Review
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Security Architecture Review


## Metadane

- Właściciel: Security Officer
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved
- Repo / moduł: [link]


## Cel dokumentu

Przeprowadzić przegląd architektury pod kątem bezpieczeństwa: zakres, kryteria, znaleziska, decyzje i działania korygujące.


## Zakres i granice

- Obejmuje: opis systemu i zmian, kryteria oceny, scenariusze zagrożeń, przegląd kontrolek/trust boundaries, wyniki i rekomendacje.
- Poza zakresem: implementacja poprawek (oddzielne zadania) i pełny opis architektury (w dok. arch.).


## Użytkownicy i interesariusze
- **CISO / Security Officer** — odpowiada za strategię bezpieczeństwa i akceptuje dokument
- **Security Engineer** — implementuje mechanizmy ochronne i przeprowadza testy
- **Compliance Officer** — weryfikuje zgodność z regulacjami (ISO 27001, RODO, NIS2)
- **DevOps / Platform Team** — wdraża zmiany infrastrukturalne wynikające z zaleceń

## Wejścia i wyjścia
- Wejścia: katalog systemów i przepływów danych, klasyfikacja danych, mapa podmiotów przetwarzających, polityki bezpieczeństwa, wymagania branżowe (PCI/HIPAA/GxP), wyniki pen-testów, architektura referencyjna, matryca ról.  
- Wyjścia: raport luk zgodności, lista działań naprawczych z priorytetami, decyzje architektoniczne (ADR) dla kontroli, zaktualizowana mapa przepływów danych, checklisty DoR/DoD zgodności, linki do dowodów audytowych.
## Założenia
- Dane o przepływach i dostawcach są aktualne.  
- Dostępne są narzędzia SIEM/DLP/KMS i polityki bezpieczeństwa.  
- Zespoły produktowe dostarczą konfiguracje do audytu.
## Otwarte pytania
- Czy istnieją transfery transgraniczne wymagające SCC lub BCR?  
- Jakie minimalne wymagania SoD dla administratorów i developerów?  
- Jakie okresy retencji logów są wymagane przez regulatora/klientów?  
- Jak będzie weryfikowana skuteczność kontroli (testy okresowe)?
## Powiązania (meta)
- Key Documents: data_protection_compliance, security_controls_reference, logging_and_audit_trail, iam_strategy_document, retention_policy, business_continuity_plan.  
- Key Document Structures: przepływy danych, kontrola dostępu, szyfrowanie, monitoring/audyt, retencja, ciągłość, dostawcy.  
- Document Dependencies: SIEM/SOAR, secrets manager, DLP, backup/DR, CMDB, change management.  
- Standardy: ISO 27001/27701, SOC2, PCI DSS, HIPAA/GxP, lokalne akty prawne.
## Zależności dokumentu
Wymaga aktualnej mapy przepływów danych, klasyfikacji danych, inwentarza systemów i dostawców, matrycy ról/SoD, wyników testów bezpieczeństwa oraz polityk retencji. Brak któregokolwiek = blokery DoR.
## Fazy cyklu życia
- Scoping i identyfikacja regulacji.  
- Analiza architektury i przepływów danych.  
- Ocena kontroli i luk; plan działań.  
- Walidacja wdrożenia kontroli; dowody audytu.  
- Cykl przeglądów okresowych.
## Struktura sekcji (szkielet)

- Kontekst i zakres przeglądu
- Kryteria oceny i scenariusze zagrożeń
- Analiza kontrolek/trust boundaries
- Wyniki i znaleziska
- Rekomendacje i decyzje
- Plan działań i follow-up


## Szybkie powiązania
- security-architecture
- shader-security-review
- security-architecture-reference
- security-architecture-document
- network-security-architecture

## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **CIS Controls v8** — Krytyczne Mechanizmy Bezpieczeństwa (CIS)
- **IEEE 1016** — Standard dla Opisów Projektowania Oprogramowania (SDD)
- **IEEE 42010** — Opis Architektoniczny Systemów i Oprogramowania
- **IEEE 829** — Dokumentacja Testowania Oprogramowania i Systemów
- **ISO 9001** — System Zarządzania Jakością (QMS)
- **ISO/IEC 15288** — Procesy Cyklu Życia Systemów
- **ISO/IEC 25010** — Model Jakości Systemu i Oprogramowania (SQuaRE)
- **ISO/IEC 27001** — System Zarządzania Bezpieczeństwem Informacji (ISMS)
- **ISO/IEC 27002** — Wytyczne Praktyk Bezpieczeństwa Informacji
- **ISO/IEC 27005** — Zarządzanie Ryzykiem Bezpieczeństwa Informacji
- **NIST CSF** — Framework Cyberbezpieczeństwa NIST
- **TOGAF ADM** — Framework Architektury Korporacyjnej (The Open Group)

### Polskie normy i regulacje
- **CERT-PL-WYTYCZNE** — Wytyczne CERT Polska (CSIRT NASK) dot. cyberbezpieczeństwa
- **KSC-PL** — Ustawa o Krajowym Systemie Cyberbezpieczeństwa

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

- Wpisz zakres zmian/systemu, kryteria i scenariusze; podsumuj wyniki i decyzje.
- Dodaj quick-links i checklisty DoR/DoD w `reports/checklist_atomic.jsonl`; sekcje N/A uzasadnij.
- Po review podlinkuj artefakty i plan działań; zsynchronizuj z backlogiem/roadmapą.


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
- SoD (Segregation of Duties): rozdział uprawnień redukujący nadużycia.  
- DPIA: ocena skutków dla ochrony danych (RODO art. 35).  
- Evidence: materiał potwierdzający kontrolę (log, konfiguracja, ticket).
## Przykłady użycia
- Przegląd architektury e‑commerce pod kątem PCI DSS.  
- Walidacja systemu medycznego (PHI) wobec HIPAA/GxP.  
- Ocena SaaS z danymi UE i transferami poza EOG.
## Ryzyka i ograniczenia
- Niepełne DFD → ukryte przepływy danych.  
- Brak SoD → nadużycia i audytowe niezgodności.  
- Nieegzekwowana retencja → naruszenia RODO/PCI.  
- Dostawca bez SLA bezpieczeństwa → ryzyko transferu danych.
## Decyzje i uzasadnienia
- Przyjęte standardy i priorytety regulacyjne.  
- Model szyfrowania (KMS/HSM) i rotacja kluczy.  
- Zakres logowania i czas retencji logów.  
- Kryteria akceptacji ryzyka/wyjątków.
## Powiązania z innymi dokumentami
- privacy_and_consent_policy — zasady zgód i PII/PHI.  
- interoperability_plan — szczegóły integracji i testów.  
- dr_plan_clinical_it — ciągłość działania i testy DR.
## Powiązania z sekcjami innych dokumentów

- [Dokument X → Sekcja Y] — [powód powiązania i kierunek przepływu informacji]
- [Dokument Z → Sekcja W] — [powód powiązania i kierunek przepływu informacji]

## Słownik pojęć w dokumencie

- [Pojęcie 1] — [definicja i źródło normalizacyjne lub wewnętrzne]
- [Pojęcie 2] — [definicja i źródło normalizacyjne lub wewnętrzne]

## Wymagane odwołania do standardów
- HIPAA / RODO, normy lokalne (np. HL7 PL), FHIR/HL7/DICOM.  
- Wewnętrzne standardy bezpieczeństwa i segmentacji klinicznej.
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

- Dokumenty architektoniczne/DFD, backlog zmian, mapa danych.
- Polityki/standardy, wymagania niefunkcjonalne, ryzyka i incydenty.
- Wyniki wcześniejszych przeglądów/testów.


## Wyjścia

- Raport z przeglądu: znaleziska, ryzyka, rekomendacje.
- Decyzje (go/no‑go/warunkowe) i action plan z właścicielami/terminami.
- Aktualizacje do architektury/roadmapy.



## Szybkie powiązania (uzupełnij)

- security_architecture.md
- security_architecture_document.md
- security_architecture_for_cloud.md
- threat_model.md
- security_assessment_report.md
- security_compliance_matrix.md


## Wymagane rozwinięcia / streszczenia

- Tabela znalezisk/ryzyk i decyzji.
- Streszczenie dla decydentów: kluczowe ryzyka, warunki go/no‑go.


## Wymagane powiązania

- Dokumenty arch., threat model, compliance matrix, rejestr ryzyk, status reporty.
- Backlog techniczny/bezpieczeństwa.


## Kryteria DoR

- [ ] Dokumentacja architektury/DFD dostępna.
- [ ] Zakres zmian i scenariusze zagrożeń opisane.
- [ ] Kryteria oceny uzgodnione, właściciele/odbiorcy znani.


## Kryteria DoD

- [ ] Znaleziska i decyzje zapisane; plan działań z właścicielami.
- [ ] Powiązania do architektury/roadmapy zaktualizowane.
- [ ] Quick-links/checklisty zaktualizowane, metadane bieżące.


## Artefakty do załączenia

- Raport z przeglądu i tabela znalezisk.
- Diagramy/DFD użyte w ocenie.
- Plan działań i linki do backlogu.


## Walidacja / testy

- Peer review ustaleń; sanity scenariuszy zagrożeń.
- Weryfikacja spójności decyzji z apetytami na ryzyko/standardami.


## Metryki monitorowane

- Liczba krytycznych znalezisk/warunków go/no‑go.
- Czas zamknięcia działań po przeglądzie.
- Powtarzalność znalezisk między przeglądami.


## Utrzymanie i aktualizacje

- Przeglądy przy każdej istotnej zmianie architektury lub cyklicznie (np. kwartalnie).
- Aktualizuj kryteria w oparciu o nowe standardy/incydenty.


## Zakończenie

Po spełnieniu DoD opublikuj raport, podlinkuj artefakty, odhacz checklisty w `reports/checklist_atomic.jsonl` i zsynchronizuj z roadmapą techniczną.
