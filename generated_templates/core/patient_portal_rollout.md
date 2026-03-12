---
title: Patient Portal Rollout
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Patient Portal Rollout


## Metadane

- Właściciel: Clinical Lead
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved

> Powiązania: linkage_index.jsonl


## Cel dokumentu

Zaplanować i przeprowadzić wdrożenie portalu pacjenta (web/mobile) z naciskiem na bezpieczeństwo, zgodność, onboarding i adopcję użytkowników.


## Zakres i granice

- Obejmuje: funkcje (wizyty, wyniki, płatności, messaging), integracje z EHR/EMR/LIS, bezpieczeństwo i prywatność (HIPAA/RODO), uwierzytelnianie (MFA, eID), zgody, dostępność (WCAG), migracja danych, komunikacja i szkolenia, monitoring/adopcja.
- Poza zakresem: projekt UI (opisany osobno), strategia marketingowa szeroka (osobne).


## Użytkownicy i interesariusze

- [Rola] — [potrzeby/odpowiedzialności]
- [Rola] — [potrzeby/odpowiedzialności]


## Wejścia i wyjścia

- Wejścia: wymagania kliniczne/pacjentów, systemy źródłowe, polityki zgód/prywatności, SLO, lista funkcji MVP, harmonogram klinik, kanały komunikacji.
- Wyjścia: plan rollout (fazy, kliniki, grupy użytkowników), konfiguracje integracji, plan bezpieczeństwa i testów, materiały onboarding, monitoring adopcji/KPI, playbook wsparcia.


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

Wskaż: integracje EHR/EMR, polityki zgód, mechanizmy MFA/eID, WCAG, plan komunikacji, support runbook; brak – odnotuj.


## Fazy cyklu życia

Planowanie → Przygotowanie → Pilotaż → Skalowanie → Utrzymanie/monitoring → Retrospektywa.



## Struktura sekcji (szkielet)

- Zakres funkcji i integracje (EHR/EMR/LIS/płatności).
- Bezpieczeństwo/prywatność: authn/z, MFA, consent, audyt, szyfrowanie, logi.
- Dostępność i języki (WCAG, lokalizacja).
- Dane i migracja (import, zgodność, testy).
- Plan rollout (fazy, kliniki, grupy użytkowników, daty, kryteria go/no-go).
- Komunikacja i onboarding (materiały, kanały, szkolenia personelu).
- Testy (funkcjonalne, bezpieczeństwo, wydajność, dostępność, UAT kliniczne).
- Monitoring i KPI adopcji (logowania, wizyty, drop-off, support tickets).
- Wsparcie i incidenty (runbook, eskalacje, SLA).


## Szybkie powiązania

- Meta: Key Documents
- Meta: Key Document Structures
- Meta: Document Dependencies


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **GDPR / RODO** — Ogólne Rozporządzenie o Ochronie Danych Osobowych (UE)
- **HL7 FHIR** — Standard Wymiany Danych w Ochronie Zdrowia
- **ISO/IEC 27001** — System Zarządzania Bezpieczeństwem Informacji (ISMS)

### Polskie normy i regulacje
- **UODO-PL** — Ustawa o Ochronie Danych Osobowych (implementacja RODO)
- **UŚUDE-PL** — Ustawa o Świadczeniu Usług Drogą Elektroniczną

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

- Zbierz wymagania i systemy; zaplanuj fazy; skonfiguruj bezpieczeństwo/integracje; przygotuj onboarding; przeprowadź pilotaż; monitoruj KPI i iteruj.


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

Integracje → bezpieczeństwo; zgody → funkcje; dostępność → UI; komunikacja → adopcja.


## Wymagane rozwinięcia

- Integracje → szczegóły interfejsów i danych.
- Bezpieczeństwo → polityki MFA, audyt, RODO/HIPAA.
- Onboarding → materiały i szkolenia.


## Wymagane streszczenia

- Jednostronicowy plan rollout (fazy, kryteria, KPI, ryzyka).


## Guidance

Cel: bezpieczne, zgodne i adoptowalne wdrożenie portalu pacjenta. DoR: wymagania kliniczne, integracje, polityki zgód, MFA/WCAG znane. DoD: plan rollout, bezpieczeństwo/dane/testy/monitoring opisane; sekcje N/A uzasadnione; metadane aktualne.


## Checklisty jakości (DoR/DoD skrót)

- DoR: [ ] Wymagania kliniczne/systemy i polityki zgód; [ ] MFA/WCAG zaadresowane; [ ] Harmonogram klinik i kanały komunikacji zebrane.
- DoD: [ ] Plan rollout/testy/bezpieczeństwo/monitoring gotowe; [ ] Onboarding i wsparcie opisane; [ ] Sekcje N/A uzasadnione; metadane aktualne.

