---
title: Security Testing (ST&E)
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Security Testing (ST&E)


## Metadane

- Właściciel: Security Officer
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved
- Repo / moduł: [link]


## Cel dokumentu

Plan Security Test & Evaluation (ST&E): definiuje zakres, metody, środowiska, kryteria akceptacji i plan raportowania dla testów bezpieczeństwa.


## Zakres i granice

- Obejmuje: klasy testów (vuln scan, config review, code review, pentest), macierz pokrycia, dane testowe, środowiska, kryteria akceptacji/go‑no‑go, raportowanie i cykliczność.
- Poza zakresem: implementacja poprawek oraz utrzymanie narzędzi poza wymaganiami testu.


## Użytkownicy i interesariusze
- **CISO / Security Officer** — odpowiada za strategię bezpieczeństwa i akceptuje dokument
- **Security Engineer** — implementuje mechanizmy ochronne i przeprowadza testy
- **Compliance Officer** — weryfikuje zgodność z regulacjami (ISO 27001, RODO, NIS2)
- **DevOps / Platform Team** — wdraża zmiany infrastrukturalne wynikające z zaleceń

## Wejścia i wyjścia
- Wejścia: wymagania/AC, architektura, dane testowe, środowiska, narzędzia, ryzyka.
- Wyjścia: plan testów, scenariusze, wyniki, defekty, wnioski i rekomendacje.
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
- Strategia/plan.
- Przygotowanie danych/środowisk.
- Wykonanie testów i raportowanie defektów.
- Raport końcowy i decyzja go/no-go.
## Struktura sekcji (szkielet)

- Kontekst i zakres systemu
- Typy testów i macierz pokrycia (komponent × metoda)
- Środowisko, dane testowe i kontrola prywatności
- Role/RACI, dostępy i narzędzia
- Kryteria akceptacji i go/no‑go
- Plan wykonania i harmonogram
- Raportowanie, ścieżka audytu i retencja artefaktów


## Szybkie powiązania
- security-testing-st-e
- security-testing
- security-testing-report
- security-testing-plan
- security-penetration-testing

## Mające zastosowanie standardy i normy

### Standardy międzynarodowe
- **ISO/IEC 27001** — System Zarządzania Bezpieczeństwem Informacji (ISMS)
- **ISO/IEC 27002** — Wytyczne Praktyk Bezpieczeństwa Informacji
- **ISO/IEC 27005** — Zarządzanie Ryzykiem Bezpieczeństwa Informacji
- **CIS Controls v8** — Krytyczne Mechanizmy Bezpieczeństwa (CIS)
- **NIST CSF** — Framework Cyberbezpieczeństwa NIST
- **ISO/IEC 25010** — Model Jakości Systemu i Oprogramowania (SQuaRE)
- **ISO 9001** — System Zarządzania Jakością (QMS)
- **IEEE 829** — Dokumentacja Testowania Oprogramowania i Systemów

## Standardy i compliance
### Standardy międzynarodowe
- **ISO/IEC 27001** — System Zarządzania Bezpieczeństwem Informacji (ISMS)
- **ISO/IEC 27002** — Wytyczne Praktyk Bezpieczeństwa Informacji
- **ISO/IEC 27005** — Zarządzanie Ryzykiem Bezpieczeństwa Informacji
- **CIS Controls v8** — Krytyczne Mechanizmy Bezpieczeństwa (CIS)
- **NIST CSF** — Framework Cyberbezpieczeństwa NIST
- **ISO/IEC 25010** — Model Jakości Systemu i Oprogramowania (SQuaRE)
- **ISO 9001** — System Zarządzania Jakością (QMS)
- **IEEE 829** — Dokumentacja Testowania Oprogramowania i Systemów

## RACI i role

| Działanie | Responsible | Accountable | Consulted | Informed |
|-----------|-------------|-------------|-----------|----------|
| Tworzenie dokumentu | DEV / BA | PM | BA / ARCH | OPS / SM |
| Przegląd i zatwierdzenie | PM / BA | PM | Tech Lead | OPS |
| Aktualizacja | DEV / BA | PM | BA | OPS |
| Archiwizacja | OPS | PM | BA | SM |

## Jak używać dokumentu

- Ustal zakres i macierz pokrycia; wypełnij dane o środowisku, dostępy i kryteria akceptacji.
- Dodaj quick-links oraz checklisty DoR/DoD w `reports/checklist_atomic.jsonl`; sekcje N/A uzasadnij.
- Uzgodnij harmonogram z zespołami i podlinkuj w kalendarzu/PM.


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

- Wymagania bezpieczeństwa i architektura systemu.
- Rejestr ryzyk, poprzednie wyniki testów/audytów.
- Listy komponentów/assetów, dostępów, kont testowych.
- Narzędzia i ich wersje, okna serwisowe/zmian.


## Wyjścia

- Plan ST&E z zakresem i harmonogramem.
- Macierz pokrycia testów i kryteria akceptacji.
- Plan danych/środowisk i kontrole prywatności.
- Plan raportowania (format, SLA, właściciele).


## Szybkie powiązania (uzupełnij)

- security_testing_plan.md
- security_testing.md
- penetration_testing.md
- security_audit.md
- security_requirements_specification.md
- data_privacy_compliance.md


## Wymagane rozwinięcia / streszczenia

- Szczegóły narzędzi (wersje, parametry, progi) i dane testowe.
- Procedura obsługi false‑positive i kolizji z change windows.
- Streszczenie dla decydentów: zakres, kryteria go/no‑go, kluczowe ryzyka.


## Wymagane powiązania

- Rejestr ryzyk, architektura, polityki prywatności i dane wrażliwe.
- Runbook incydentowy na wypadek zakłóceń testów.
- Backlog defektów i kanały raportowania.


## Kryteria DoR

- [ ] Zakres i lista komponentów uzgodnione.
- [ ] Macierz pokrycia i typy testów zdefiniowane.
- [ ] Środowiska/dane i dostępy przygotowane.
- [ ] Kryteria akceptacji i harmonogram zatwierdzone.


## Kryteria DoD

- [ ] Plan ST&E wypełniony, quick-links dodane.
- [ ] Macierz pokrycia i kryteria go/no‑go opisane.
- [ ] Procedura raportowania/retencji artefaktów doprecyzowana.
- [ ] Artefakty podlinkowane, metadane zaktualizowane.


## Artefakty do załączenia

- Plan ST&E (ten dokument), macierz pokrycia.
- Lista narzędzi i konfiguracji.
- Harmonogram testów, lista dostępu/kont.
- Szablon raportu i kanały komunikacji.


## Walidacja / testy

- Przegląd planu przez właściciela systemu i zespół bezpieczeństwa.
- Dry‑run wybranych skryptów w bezpiecznym zakresie.


## Metryki monitorowane

- Pokrycie komponentów (procent i krytyczność).
- Liczba blokujących zależności/dostępów przed startem.
- SLA raportowania wyników i zamykania defektów.


## Utrzymanie i aktualizacje

- Aktualizuj plan co release/kwartał lub po większych zmianach architektury.
- Rewiduj listę narzędzi i wersji oraz kont dostępowych.


## Zakończenie

Po spełnieniu DoD opublikuj plan, zsynchronizuj terminy z zespołami, odhacz checklisty w `reports/checklist_atomic.jsonl` i rozpocznij egzekucję ST&E.
