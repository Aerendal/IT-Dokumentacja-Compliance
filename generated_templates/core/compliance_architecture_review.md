---
title: Compliance Architecture Review
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Compliance Architecture Review


## Metadane

- Właściciel: Solution Architect
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Zapewnić, że architektura systemu spełnia wymagania regulacyjne (RODO/PII, PCI DSS, HIPAA/GxP, lokalne przepisy) oraz standardy bezpieczeństwa i audytu. Dokument identyfikuje luki, proponuje środki zaradcze i definiuje ścieżkę zgodności dla nowych i istniejących rozwiązań.


## Zakres i granice

- Obejmuje: architekturę aplikacji i danych, IAM/SSO/MFA, szyfrowanie w spoczynku i tranzycie, logging/audyt, segregację obowiązków, retencję/usuwanie danych, ciągłość działania, zarządzanie zmianą, ścieżki audytu.  
- Poza zakresem: szczegółowe procedury operacyjne SOC i IR (oddzielne runbooki), polityki HR, negocjacje umów z dostawcami.


## Użytkownicy i interesariusze
- **Solution / Enterprise Architect** — projektuje i zatwierdza architekturę
- **Tech Lead** — odpowiada za spójność techniczną implementacji
- **Product Owner** — definiuje wymagania biznesowe wchodzące na wejście
- **Development Team** — implementuje na podstawie projektu

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
- Cel i zakres polityki
- Zakres obowiązywania i wyjątki
- Role i odpowiedzialności
- Wymagania/kontrole (techniczne/procesowe)
- Proces zarządzania zmianą i wyjątkami
- Dowody/audyt, metryki zgodności
- Komunikacja/szkolenia i utrzymanie
## Szybkie powiązania

- linkage_index.jsonl (compliance/architecture/review)  
- security_controls_reference, data_protection_compliance, retention_policy, logging_and_audit_trail


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **COBIT 2019** — Kontrola nad Informacją i Technologiami (ISACA)
- **IEEE 1016** — Standard dla Opisów Projektowania Oprogramowania (SDD)
- **IEEE 42010** — Opis Architektoniczny Systemów i Oprogramowania
- **IEEE 829** — Dokumentacja Testowania Oprogramowania i Systemów
- **ISO 9001** — System Zarządzania Jakością (QMS)
- **ISO/IEC 15288** — Procesy Cyklu Życia Systemów
- **ISO/IEC 25010** — Model Jakości Systemu i Oprogramowania (SQuaRE)
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

1. Zbierz dane wejściowe (DFD, klasyfikacja, IAM, dostawcy).  
2. Oceń kontrole vs wymagania regulacyjne; spisz luki i ryzyko.  
3. Zdefiniuj działania naprawcze i właścicieli; wprowadź do backlogu.  
4. Waliduj wdrożenie i zarchiwizuj dowody audytowe; odhacz DoD.


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

- Dane i klasyfikacja ↔ Szyfrowanie ↔ Retencja/usuwanie.  
- IAM/SoD ↔ Dostawcy ↔ Audyt/monitoring.  
- Ciągłość/DR ↔ Backup ↔ Recovery objectives (RPO/RTO).


## Struktura sekcji

1) Kontekst systemu i regulacji  
2) Klasyfikacja danych i przepływy  
3) Kontrola dostępu (IAM/SoD/SSO/MFA)  
4) Szyfrowanie i ochrona danych  
5) Logging, audyt, monitorowanie  
6) Retencja i usuwanie danych  
7) Dostawcy i transfery transgraniczne  
8) Ciągłość działania i DR  
9) Luka → plan działania → dowody  
10) Ryzyka, decyzje, pytania


## Wymagane rozwinięcia

- Data flow diagram (DFD) z klasami danych.  
- Macierz SoD i dostępów uprzywilejowanych.  
- Plan retencji/usuwania i mechanizmy egzekucji.  
- Lista kontrolna szyfrowania (at-rest/in-transit, klucze/KMS).  
- Plan działań naprawczych z terminami i właścicielami.  
- Dowody audytowe: logi, konfiguracje, raporty testów.


## Wymagane streszczenia

- Executive summary: status zgodności, top 5 luk i ich ryzyko.  
- Snapshot dostawców z oceną ryzyka i miejscem przetwarzania danych.


## Guidance (skrót)

- Zacznij od przepływów danych i klasyfikacji; bez nich kontrola nie jest kompletna.  
- Preferuj SSO/MFA, least privilege, rotację kluczy, centralne KMS/HSM.  
- Logi: pełne, niezmienialne, z korelacją w SIEM; testuj alerty.  
- Retencja/usuwanie musi być egzekwowana automatycznie; dokumentuj wyjątki.  
- Każdą kontrolę wiąż z konkretną regulacją i dowodem audytowym.  
- Ustal cykl przeglądów (np. kwartalny) i własność luk.


## Checklisty Definition of Ready (DoR)

- [ ] Aktualne DFD i klasy danych.  
- [ ] Lista systemów, dostawców i lokalizacji danych.  
- [ ] Polityki: IAM, retencja, szyfrowanie, logging.  
- [ ] Wyniki ostatnich testów bezpieczeństwa dostępne.  
- [ ] Zidentyfikowane regulacje (RODO/PCI/HIPAA/GxP itp.).


## Checklisty Definition of Done (DoD)

- [ ] Luki zmapowane na regulacje; ryzyka ocenione.  
- [ ] Plan działań naprawczych z właścicielami i terminami.  
- [ ] Dowody wdrożenia kontroli zarchiwizowane.  
- [ ] Linkage_index/CMDB zaktualizowane; decyzje zapisane w ADR.  
- [ ] Harmonogram kolejnego przeglądu ustalony.

