---
title: Access Control Goals
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Access Control Goals


## Metadane

- Właściciel: Document Owner
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved

> Powiązania: linkage_index.jsonl


## Cel dokumentu

Definiuje cele i zasady kontroli dostępu dla organizacji/produktu: least privilege, SoD, spójność ról/atrybutów, audytowalność, user experience i zgodność regulacyjna. Służy jako fundament dla projektów macierzy, polityk i implementacji.


## Zakres i granice

- Obejmuje: cele biznesowe i bezpieczeństwa, zasady (least privilege, SoD, need-to-know), zakres systemów/danych, priorytety (UX vs bezpieczeństwo), metryki sukcesu, minimalne wymagania (IdP/SSO, MFA, recertyfikacje), wyjątki i governance.
- Poza zakresem: szczegółowe macierze i workflow nadawania (w Access Control Matrix Design / IAM docs).


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia

- Wejścia: strategia bezpieczeństwa, regulacje (SOX/PCI/RODO), klasyfikacja danych, wymagania produktowe/operacyjne, risk register.
- Wyjścia: zdefiniowane cele/zasady AC, priorytety UX vs bezpieczeństwo, metryki, minimalne kontrolki, wytyczne dla projektów macierzy i polityk.


## Założenia

- [Założenie 1 — co przyjmujemy za prawdziwe bez weryfikacji]
- [Założenie 2 — warunki brzegowe, które muszą być spełnione]

## Otwarte pytania

- [Pytanie 1 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]
- [Pytanie 2 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]

## Powiązania (meta)

- Key Documents: access_control_policy, identity_and_access_architecture, access_control_matrix_design, multi_factor_authentication_design, data_classification, security_controls_reference, risk_register.
- Dependencies: data classification, IdP/IAM capabilities, regulatory requirements, risk appetite.


## Zależności dokumentu

- Upstream: strategia bezpieczeństwa, regulacje, klasyfikacja danych, risk appetite.
- Downstream: macierze ról/uprawnień, polityki i workflow, recertyfikacje, audyt/logi, projekty aplikacji/API/baz.
- Zewnętrzne: wymagania audytorów/regulatorów, dostawcy IdP/IAM.


## Fazy cyklu życia

- Definicja celów i zasad.
- Walidacja z interesariuszami (biznes/bezpieczeństwo/produkt/ops).
- Publikacja i aktualizacje po zmianie ryzyka/regulacji.



## Struktura sekcji (szkielet)

1) Streszczenie i cele (biznes, bezpieczeństwo, zgodność)  
2) Zakres (systemy/dane, klasyfikacja, użytkownicy/kanały)  
3) Zasady AC (least privilege, SoD, need-to-know, just-in-time)  
4) Metryki sukcesu (recert compliance, SoD violations, time-to-provision, UX frictions)  
5) Minimalne kontrolki (IdP/SSO, MFA, logging, recertyfikacje, waivery z sunset)  
6) Priorytety i kompromisy (UX vs bezpieczeństwo)  
7) Wyjątki/waivery i governance (approval, sunset, kompensacje)  
8) Guidance dla projektów macierzy/polityk i recertyfikacji  
9) Ryzyka i założenia; decyzje (ADR) i otwarte pytania  


## Szybkie powiązania

- access_control_policy, identity_and_access_architecture, access_control_matrix_design, multi_factor_authentication_design, data_classification, security_controls_reference, risk_register


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

- [ ] Każdy cel ma powiązane zasady i metryki; minimalne kontrolki wspierają cele.
- [ ] Wyjątki mają uzasadnienie i sunset; guidance spójne z macierzami i politykami.


## Lista kontrolna spójności relacji

- [ ] Czy każda sekcja z relacją ma wskazaną sekcję źródłową?
- [ ] Czy relacje nie tworzą sprzecznych wymagań?
- [ ] Czy wszystkie wymagane standardy mają odwołania?
- [ ] Czy RACI jest kompletne dla kluczowych działań?

## Artefakty powiązane

- Lista zasad i metryk, minimalne kontrolki, waiver log (jeśli istnieje), ADR log.


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

- Cele biznes/bezpieczeństwo → zasady → metryki → kontrolki minimalne → guidance dla macierzy/polityk.


## Wymagane rozwinięcia

- Lista zasad i ich uzasadnień; metryki z definicją i targetem.
- Minimalne kontrolki i warunki wyjątków; proces sunset/waiver.
- Guidance dla nowych systemów (jak stosować zasady przy projektach AC).


## Wymagane streszczenia

- Executive summary: top cele, zasady, metryki, minimalne kontrolki, wyjątki.
- One-pager: zasady AC i metryki, minimalne kontrolki, kontakt/owner.


## Guidance (skrót)

- DoR: strategia bezpieczeństwa i risk appetite znane; klasyfikacja danych; wymagania regulatorów.
- DoD: cele/zasady/metryki/minimalne kontrolki zdefiniowane; wyjątki/waivery z sunset; guidance dla projektów; metadane aktualne; dokument w linkage_index.
- Spójność: metryki mierzą cele; kontrolki odpowiadają zasadom; wyjątki mają sunset/kompensacje.


## Checklisty Definition of Ready (DoR)

- [ ] Risk appetite, regulacje i klasyfikacja danych znane; główni interesariusze AC wskazani.


## Checklisty Definition of Done (DoD)

- [ ] Cele/zasady/metryki/minimalne kontrolki opisane; wyjątki/waivery z sunset; guidance dla projektów; dokument w linkage_index.

