---
title: Embedded Engineer Onboarding
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Embedded Engineer Onboarding


## Metadane

- Właściciel: Document Owner
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved

> Powiązania: linkage_index.jsonl


## Cel dokumentu

Przyspieszyć wdrożenie inżynierów embedded, zapewniając dostęp do narzędzi, środowisk, standardów kodu/hardware, procesów build/flash/test oraz kluczowych artefaktów projektu.


## Zakres i granice

- Obejmuje: setup środowiska (toolchain, IDE, debugger/JTAG, build system), dostęp do repo i dokumentacji hardware, standardy kodu/bezpieczeństwa, proces review/testów (unit/HIL/SIL), flash/bootloader, konfiguracje CI, logowanie i trace, procedury debug, checklisty bezpieczeństwa (memory, interrupt, concurrency), SLA wsparcia.
- Poza zakresem: onboarding produktowy poza zespołem embedded (osobne dokumenty).


## Użytkownicy i interesariusze

- [Rola] — [potrzeby/odpowiedzialności]
- [Rola] — [potrzeby/odpowiedzialności]


## Wejścia i wyjścia

- Wejścia: lista projektów/MCU/SoC, instrukcje hardware, toolchainy wspierane, standardy kodu, dostęp do labu i sprzętu, polityki bezpieczeństwa, dane do certyfikatów/kluczy.
- Wyjścia: checklisty setup, linki do repo/CI, pakiet startowy (sample build/flash), instrukcja debug/logowania, kontakty do wsparcia, harmonogram pierwszych zadań.


## Założenia

- [Założenie 1]
- [Założenie 2]


## Otwarte pytania

- [Pytanie 1]
- [Pytanie 2]


## Powiązania (meta)

- Wymaga odniesienia do: Key Documents
- Wymaga odniesienia do: Key Document Structures
- Wymaga odniesienia do: Document Dependencies
- Wymaga odniesienia do: RACI i role
- Wymaga odniesienia do: Standardy i compliance


## Zależności dokumentu

Wskaż: repo firmware/hardware, instrukcje płyt, licencje narzędzi, polityki bezpieczeństwa kluczy, CI/CD, system zgłoszeń; brak – odnotuj.


## Fazy cyklu życia

Plan → Przygotowanie pakietu → Onboarding (tydzień 1–2) → Zadania startowe → Retrospektywa i aktualizacja materiałów.



## Struktura sekcji (szkielet)

- Profil sprzętu/projektów i wymagane toolchainy.
- Setup środowiska (OS, pakiety, IDE, debug, JTAG, sterowniki).
- Build/flash (komendy, config, bootloader, recovery).
- Standardy kodu/bezpieczeństwa (MISRA/CERT jeśli dotyczy, review, style).
- Testy (unit, SIL, HIL, regresja, coverage).
- Debug/log/trace (UART/SWD/ETM), typowe problemy.
- CI/CD i artefakty (pipelines, artefakty binarne, signing).
- Wsparcie i kontakty (lab, sprzęt, dostęp, ticketing).
- Checklista onboarding.


## Szybkie powiązania

- Meta: Key Documents
- Meta: Key Document Structures
- Meta: Document Dependencies


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

- Skonfiguruj środowisko wg checklisty; zbuduj/flashnij sample; skonfiguruj debug/log; poznaj standardy/testy; wykonaj pierwsze zadania; uzupełnij feedback.


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

- [Termin 1]
- [Termin 2]
- [Termin 3]


## Przykłady użycia

- [Przykład 1]
- [Przykład 2]


## Ryzyka i ograniczenia

- [Ryzyko 1]
- [Ryzyko 2]


## Decyzje i uzasadnienia

- [Decyzja 1]
- [Decyzja 2]


## Powiązania z innymi dokumentami

- [Dokument A] — [typ relacji] — [uzasadnienie]
- [Dokument B] — [typ relacji] — [uzasadnienie]


## Powiązania z sekcjami innych dokumentów

- [Dokument X → Sekcja Y] — [powód]
- [Dokument Z → Sekcja W] — [powód]


## Słownik pojęć w dokumencie

- [Pojęcie 1] — [definicja i źródło normalizacyjne lub wewnętrzne]
- [Pojęcie 2] — [definicja i źródło normalizacyjne lub wewnętrzne]

## Wymagane odwołania do standardów

- [Standard 1]
- [Standard 2]


## Mapa relacji sekcja→sekcja

- [Sekcja A] -> [Sekcja B] : [typ]
- [Sekcja C] -> [Sekcja D] : [typ]


## Mapa relacji dokument→dokument

- [Dokument A] -> [Dokument B] : [typ]
- [Dokument C] -> [Dokument D] : [typ]


## Ścieżki informacji

- [Wejście] → [Źródło] → [Rozwinięcie] → [Wyjście]
- [Wejście] → [Źródło] → [Streszczenie] → [Wyjście]


## Weryfikacja spójności

- [ ] Ścieżki informacji zamknięte
- [ ] Brak sprzecznych relacji
- [ ] Sekcje krytyczne mają źródła


## Lista kontrolna spójności relacji

- [ ] Relacje mają sekcje źródłowe
- [ ] Relacje nie są sprzeczne
- [ ] Cross-doc uzasadnione
- [ ] Rozwinięcia/streszczenia odnotowane


## Artefakty powiązane

- [Artefakt 1]
- [Artefakt 2]


## Ścieżka decyzji

- [Decyzja] → [Uzasadnienie] → [Konsekwencje]
- [Decyzja] → [Uzasadnienie] → [Konsekwencje]


## Ścieżka akceptacji

1. Autor przygotowuje wersję roboczą i przeprowadza samorecenzję.
2. Recenzent techniczny (Tech Lead / BA) weryfikuje merytorycznie.
3. Właściciel procesu zatwierdza treść i zakres.
4. PM / Scrum Master aktualizuje metadata (wersja, data, status).
5. Dokument trafia do repozytorium i jest linkowany w Szybkie powiązania.

## Metryki jakości

- [Metryka 1, np. pokrycie testami] — [cel / próg minimalny]
- [Metryka 2, np. czas przeglądu] — [cel / próg minimalny]

## Kryteria ukończenia

- [ ] Kryterium 1 — [opis stanu ukończenia tej sekcji lub dokumentu]
- [ ] Kryterium 2 — [opis stanu ukończenia tej sekcji lub dokumentu]

## Powiązania sekcja↔sekcja

Setup → build/flash; standardy → review/testy; debug/log → HIL/SIL; bezpieczeństwo → dostęp do kluczy.


## Wymagane rozwinięcia

- Testy → konkretne narzędzia/ramy; build → configi dla MCU/boards.
- Bezpieczeństwo → polityka kluczy/signing.


## Wymagane streszczenia

- One-pager: setup + build/flash + kontakty.


## Guidance

Cel: szybki start na sprzęcie. DoR: sprzęt/toolchainy/standardy/CI gotowe. DoD: checklisty setup/build/test/log/wsparcie wypełnione; sekcje N/A uzasadnione; metadane aktualne.


## Checklisty jakości (DoR/DoD skrót)

- DoR: [ ] Sprzęt i toolchainy dostępne; [ ] Repo i CI dostępne; [ ] Polityki bezpieczeństwa znane.
- DoD: [ ] Setup/build/flash/test/debug opisane i sprawdzone; [ ] Kontakty i wsparcie dodane; [ ] Sekcje N/A uzasadnione; metadane aktualne.

