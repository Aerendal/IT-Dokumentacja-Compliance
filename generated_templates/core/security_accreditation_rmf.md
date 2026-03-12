---
title: Security Accreditation (RMF)
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Security Accreditation (RMF)


## Metadane

- Właściciel: Security Officer
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved
- Repo / moduł: [link]


## Cel dokumentu

Przeprowadzić akredytację bezpieczeństwa wg NIST RMF: opis kroków, kontrolek, dowodów, ról i decyzji autoryzacyjnej (ATO/ATO with POA&M).


## Zakres i granice

- Obejmuje: kroki RMF (Categorize → Select → Implement → Assess → Authorize → Monitor), kontrolki i dowody, role/RACI, harmonogram, status ATO i plan monitoringu ciągłego.
- Poza zakresem: szczegółowe konfiguracje usług (opisane w dokumentach technicznych/runbookach).


## Użytkownicy i interesariusze
- **CISO / Security Officer** — odpowiada za strategię bezpieczeństwa i akceptuje dokument
- **Security Engineer** — implementuje mechanizmy ochronne i przeprowadza testy
- **Compliance Officer** — weryfikuje zgodność z regulacjami (ISO 27001, RODO, NIS2)
- **DevOps / Platform Team** — wdraża zmiany infrastrukturalne wynikające z zaleceń

## Wejścia i wyjścia
- Wejścia: cele biznesowe, backlog/epiki, wymagania niefunkcjonalne, ograniczenia prawne/techniczne, istniejące systemy/dane.
- Wyjścia: zaakceptowana wersja dokumentu, decyzje architektoniczne/procesowe, action items z właścicielami i terminami.
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
- Discovery/Analiza: doprecyzowanie problemu, interesariusze, ograniczenia.
- Projektowanie/Planowanie: decyzje, warianty, kryteria akceptacji, plan wdrożenia.
- Implementacja/Testy: realizacja, walidacja, kryteria go/no-go.
- Wdrożenie/Operacje: rollout, monitoring, eskalacje, ciągłe doskonalenie.
## Struktura sekcji (szkielet)

- Kontekst i zakres systemu (mission, impact levels)
- Categorize: dane/impact, boundary, interfejsy
- Select: baseline, tailoryzacja, wyjątki
- Implement: kontrolki, właściciele, dowody
- Assess: SAP/SAR, wyniki, rekomendacje
- Authorize: decyzja ATO, warunki, daty ważności
- Monitor: plan ciągłego monitoringu, przeglądy, raportowanie


## Szybkie powiązania
- vm-security-hardening
- security-training
- security-testing-st-e
- security-testing
- security-strategy

## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **CIS Controls v8** — Krytyczne Mechanizmy Bezpieczeństwa (CIS)
- **ISO/IEC 27001** — System Zarządzania Bezpieczeństwem Informacji (ISMS)
- **ISO/IEC 27002** — Wytyczne Praktyk Bezpieczeństwa Informacji
- **ISO/IEC 27005** — Zarządzanie Ryzykiem Bezpieczeństwa Informacji
- **NIST CSF** — Framework Cyberbezpieczeństwa NIST

### Polskie normy i regulacje
- **CERT-PL-WYTYCZNE** — Wytyczne CERT Polska (CSIRT NASK) dot. cyberbezpieczeństwa
- **KNF-REKOM-IT** — Rekomendacje KNF dot. systemów IT w sektorze finansowym
- **KSC-PL** — Ustawa o Krajowym Systemie Cyberbezpieczeństwa
- **MIFID2-PL** — MiFID II — Dyrektywa dot. Rynku Finansowego (implementacja PL)
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

- Wypełnij kroki RMF, dołącz dowody i status; sekcje N/A uzasadnij.
- Dodaj quick-links i checklisty DoR/DoD w `reports/checklist_atomic.jsonl`.
- Podlinkuj artefakty (SSP/SAP/SAR/POA&M) i harmonogram monitoringu.


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

- Opis systemu/architektura i dane (impact levels), DFD.
- Katalog kontrolek/baseline (np. 800-53), polityki/regulacje.
- Dowody/testy (scan/pentest/config), rejestr ryzyk, wcześniejsze ATO/POA&M.
- Role (ISO, AO, ISSO, właściciele systemu) i harmonogram.


## Wyjścia

- Artefakty RMF: SSP, SAP/SAR, POA&M, ATO/ATO with conditions.
- Lista kontrolek z dowodami i statusem.
- Plan monitoringu ciągłego i przeglądów.



## Szybkie powiązania (uzupełnij)

- security_compliance_matrix.md
- security_controls_documentation.md
- security_controls_evaluation.md
- security_status_report.md
- logging_and_audit_trail.md
- risk_management_framework.md


## Wymagane rozwinięcia / streszczenia

- Tabela kontrolek: kontrolka → implementacja → dowód → status → owner.
- Streszczenie SAR: główne wyniki, rekomendacje, ryzyka resztkowe.


## Wymagane powiązania

- Polityki/standardy, compliance matrix, rejestr ryzyk, audyty/testy.
- Artefakty RMF (SSP, SAP, SAR, POA&M), ATO decyzja.


## Kryteria DoR

- [ ] Boundary/impact i architektura opisane.
- [ ] Baseline kontrolek i role zdefiniowane.
- [ ] Dane/dowody dostępne.


## Kryteria DoD

- [ ] Wszystkie kroki RMF wypełnione; status ATO podany.
- [ ] Kontrolki i dowody udokumentowane; luki w POA&M wpisane.
- [ ] Plan monitoringu ciągłego opisany; quick-links/checklisty zaktualizowane.


## Artefakty do załączenia

- SSP, SAP, SAR, POA&M.
- Rejestr ryzyk i wyjątki.
- Decyzja ATO/warunki, harmonogram przeglądów.


## Walidacja / testy

- Peer review artefaktów RMF.
- Sprawdzenie spójności między SSP↔SAP↔SAR↔POA&M.


## Metryki monitorowane

- % kontrolek compliant; liczba luk w POA&M i ich wiek.
- Czas do wydania ATO; status monitoringu ciągłego.


## Utrzymanie i aktualizacje

- Monitorowanie ciągłe wg planu; przeglądy okresowe (np. kwartalne/roczne).
- Aktualizuj artefakty po zmianach architektury/incydentach/audytach.


## Zakończenie

Po spełnieniu DoD opublikuj dokument, podlinkuj artefakty, odhacz checklisty w `reports/checklist_atomic.jsonl` i poinformuj właścicieli systemu/AO.
