---
title: Security Analyst Onboarding
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# Security Analyst Onboarding

## Metadane
- Właściciel: Security Officer
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved
- Repo / moduł: [link]

## Cel dokumentu
Program onboardingowy dla Security Analyst z jasno opisanymi celami, modułami, praktykami hands‑on i sposobem oceny, żeby nowa osoba mogła produktywnie pracować w przewidywalnym czasie.

## Zakres i granice
- Obejmuje: grupę docelową/persony, cele uczenia, sylabus/moduły, środowiska labowe, materiały, ćwiczenia, ewaluację i feedback.
- Poza zakresem: ogólne polityki HR, szczegółowe procedury produktowe nieużywane w szkoleniu.

## Wejścia
- Profil uczestników i poziom wejściowy.
- Lista narzędzi/platform (SIEM, EDR, skanery, ticketing).
- Materiały referencyjne, runbooki, dane testowe/laby.
- Dostępność mentorów/trainerów i harmonogram.

## Wyjścia
- Sylabus i agenda z czasem trwania.
- Materiały i instrukcje labowe.
- Plan ewaluacji (quiz/lab/egzamin), kryteria zaliczenia.
- Action log z feedbacku i plan utrzymania materiałów.


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
## Struktura sekcji (szkielet)
- Streszczenie i cele szkolenia
- Grupa docelowa i wymagania wstępne
- Moduły/agenda (teoria + lab) z czasem
- Środowisko, dostęp i bezpieczeństwo danych w labach
- Ćwiczenia/prace domowe i rubryka oceny
- Ewaluacja (quiz/lab/egzamin), feedback i iteracje
- Plan komunikacji/mentoringu i utrzymania materiałów

## Szybkie powiązania (uzupełnij)
- security_training.md
- security_tools_training.md
- security_policy_training.md
- security_operations_runbook.md
- security_incident_response.md

## Mające zastosowanie standardy i normy

### Standardy międzynarodowe
- **CIS Controls v8** — Krytyczne Mechanizmy Bezpieczeństwa (CIS)
- **COBIT 2019** — Kontrola nad Informacją i Technologiami (ISACA)
- **ISO/IEC 27001** — System Zarządzania Bezpieczeństwem Informacji (ISMS)
- **ISO/IEC 27002** — Wytyczne Praktyk Bezpieczeństwa Informacji
- **ISO/IEC 27005** — Zarządzanie Ryzykiem Bezpieczeństwa Informacji
- **ISO/IEC 38500** — Ład Informatyczny Organizacji
- **NIST CSF** — Framework Cyberbezpieczeństwa NIST
- **TOGAF ADM** — Framework Architektury Korporacyjnej (The Open Group)

### Polskie normy i regulacje
- **CERT-PL-WYTYCZNE** — Wytyczne CERT Polska (CSIRT NASK) dot. cyberbezpieczeństwa
- **KSC-PL** — Ustawa o Krajowym Systemie Cyberbezpieczeństwa

> Sekcja generowana automatycznie. Zweryfikuj trafność i uzupełnij o dodatkowe normy/regulacje specyficzne dla kontekstu projektu.
## Jak używać dokumentu
- Uzupełnij sylabus i wymagania, następnie zaplanuj dostęp do środowisk labowych.
- Dodaj quick-links i checklisty DoR/DoD w `reports/checklist_atomic.jsonl`; sekcje N/A uzasadnij.
- Po pilotażu zaktualizuj materiały, metadane i status.

## Wymagane rozwinięcia / streszczenia
- Scenariusze labów z krokami i expected results.
- Rubryka oceny (quiz/lab) i kryteria zaliczenia.
- One-pager dla managerów: cele, czas ramp‑up, wymagania dostępu.

## Wymagane powiązania
- RACI dla trenerów/mentorów.
- Runbooki operacyjne, polityki bezpieczeństwa, procedury dostępu.
- Narzędzia: SIEM/EDR/skanery + konta testowe.

## Kryteria DoR
- [ ] Profil grupy docelowej i cele potwierdzone.
- [ ] Środowiska/laby i dostępności mentorów zapewnione.
- [ ] Materiały wyjściowe i narzędzia zebrane.
- [ ] Harmonogram i logistyka zatwierdzone.

## Kryteria DoD
- [ ] Sylabus i moduły opisane, materiały podlinkowane.
- [ ] Ćwiczenia/laby gotowe z danymi testowymi.
- [ ] Ewaluacja i rubryka oceny zdefiniowane, feedback loop ustawiony.
- [ ] Artefakty i quick-links zaktualizowane, metadane bieżące.

## Artefakty do załączenia
- Sylabus/agenda.
- Materiały i instrukcje labowe.
- Lista dostępu/akredytacji do narzędzi.
- Rubryka oceny i raport z pilotażu.

## Walidacja / testy
- Pilotaż na małej grupie; sprawdź czasy ćwiczeń, wskaźnik ukończenia i zrozumienie.
- Przegląd materiałów pod kątem zgodności z politykami bezpieczeństwa i minimalizacji danych w labach.

## Metryki monitorowane
- Time-to-productivity (dni/tyg.).
- % ukończenia szkolenia i zaliczeń labów.
- Pass rate quizów/egzaminów.
- NPS/CSAT uczestników; liczba zgłoszeń o brakach w materiałach.

## Utrzymanie i aktualizacje
- Przegląd co kwartał lub po większych zmianach w stacku/narzędziach.
- Aktualizacja dostępów i screenów po zmianach UI/wersji.
- Zbieraj feedback z każdej edycji i iteruj moduły.

## Zakończenie
Po spełnieniu DoD zaktualizuj status, podlinkuj artefakty, odhacz checklisty w `reports/checklist_atomic.jsonl` i przekaż zestaw startowy nowym uczestnikom.
- [Decyzja 2 — uzasadnienie]

## Założenia
- [Założenie 1]
- [Założenie 2]

## Otwarte pytania
- [Pytanie 1]
- [Pytanie 2]

## Powiązania z innymi dokumentami
- [Dokument A] — [typ relacji] — [uzasadnienie]
- [Dokument B] — [typ relacji] — [uzasadnienie]

## Powiązania z sekcjami innych dokumentów
- [Dokument X → Sekcja Y] — [powód powiązania]
- [Dokument Z → Sekcja W] — [powód powiązania]

## Słownik pojęć w dokumencie
- [Pojęcie 1] — [definicja i źródło]
- [Pojęcie 2] — [definicja i źródło]
- [Pojęcie 3] — [definicja i źródło]

## Wymagane odwołania do standardów
- [Standard 1] — [sekcja/fragment, którego dotyczy]
- [Standard 2] — [sekcja/fragment, którego dotyczy]

## Mapa relacji sekcja→sekcja
- [Sekcja A] -> [Sekcja B] : [typ relacji]
- [Sekcja C] -> [Sekcja D] : [typ relacji]

## Mapa relacji dokument→dokument
- [Dokument A] -> [Dokument B] : [typ relacji]
- [Dokument C] -> [Dokument D] : [typ relacji]

## Ścieżki informacji
- [Wejście] → [Sekcja źródłowa] → [Sekcja rozwinięcia] → [Wyjście]
- [Wejście] → [Sekcja źródłowa] → [Sekcja streszczenia] → [Wyjście]

## Weryfikacja spójności
- [ ] Czy wszystkie ścieżki informacji są zamknięte?
- [ ] Czy istnieją pętle lub sprzeczne relacje?
- [ ] Czy sekcje krytyczne mają wskazane źródła i rozwinięcia?

## Lista kontrolna spójności relacji
- [ ] Czy każda sekcja z relacją ma wskazaną sekcję źródłową?
- [ ] Czy relacje nie tworzą sprzecznych wymagań (np. wzajemne wykluczanie)?
- [ ] Czy relacje cross‑doc mają uzasadnienie i są zgodne z fazą?
- [ ] Czy relacje wymagają rozwinięć lub streszczeń są odnotowane?

## Artefakty powiązane
- [Artefakt 1] — [opis i relacja do dokumentu]
- [Artefakt 2] — [opis i relacja do dokumentu]

## Ścieżka decyzji
- [Decyzja] → [Uzasadnienie] → [Konsekwencje]
- [Decyzja] → [Uzasadnienie] → [Konsekwencje]

## Użytkownicy i interesariusze
- **CISO / Security Officer** — odpowiada za strategię bezpieczeństwa i akceptuje dokument
- **Security Engineer** — implementuje mechanizmy ochronne i przeprowadza testy
- **Compliance Officer** — weryfikuje zgodność z regulacjami (ISO 27001, RODO, NIS2)
- **DevOps / Platform Team** — wdraża zmiany infrastrukturalne wynikające z zaleceń

## Ścieżka akceptacji
- [Kto zatwierdza] → [kryteria akceptacji] → [status]
- [Kto zatwierdza] → [kryteria akceptacji] → [status]

## Kryteria ukończenia
- [ ] Kryterium 1 — [opis]
- [ ] Kryterium 2 — [opis]

## Metryki jakości
- [Metryka 1] — [cel / próg]
- [Metryka 2] — [cel / próg]

## Monitoring i utrzymanie
- [Co monitorujemy] — [narzędzie / częstotliwość]
- [Kto utrzymuje] — [rola]

## Kontrola zmian
- [Zmiana] — [powód] — [data] — [akceptacja]

## Wymogi prawne i regulacyjne
- [Wymóg 1] — [źródło / akt prawny / standard]
- [Wymóg 2] — [źródło / akt prawny / standard]

## Zasady bezpieczeństwa informacji
- [Zasada 1] — [opis i wpływ na dokument]
- [Zasada 2] — [opis i wpływ na dokument]

## Ochrona danych i prywatność
- [Wymaganie 1] — [opis i sekcja docelowa]
- [Wymaganie 2] — [opis i sekcja docelowa]

## Wersjonowanie treści
- [Wersja] — [zmiana] — [autor] — [data]
- [Wersja] — [zmiana] — [autor] — [data]

## Historia zmian sekcji
- [Sekcja] — [zmiana] — [data]
- [Sekcja] — [zmiana] — [data]

## Wymagane aktualizacje
- [Sekcja] — [powód aktualizacji] — [termin]
- [Sekcja] — [powód aktualizacji] — [termin]

## Integracje i interfejsy
- [System / API] — [zakres integracji] — [wymagania]
- [System / API] — [zakres integracji] — [wymagania]

## Wymagania danych
- [Dane wejściowe] — [format] — [walidacja]
- [Dane wyjściowe] — [format] — [walidacja]

## Logowanie i audyt
- [Zdarzenie] — [poziom] — [retencja]
- [Zdarzenie] — [poziom] — [retencja]

## Utrzymanie i operacje
- [Procedura] — [cel] — [częstotliwość]
- [Procedura] — [cel] — [częstotliwość]

## KPI i SLA
- [KPI] — [cel] — [pomiar]
- [SLA] — [cel] — [pomiar]

## Scenariusze awaryjne
- [Scenariusz] — [objawy] — [reakcja]
- [Scenariusz] — [objawy] — [reakcja]

## Wpływ na inne systemy
- [System] — [rodzaj wpływu] — [ryzyko]
- [System] — [rodzaj wpływu] — [ryzyko]

## Zależności danych między systemami
- [Źródło danych] → [Odbiorca] — [opis]
- [Źródło danych] → [Odbiorca] — [opis]

## Harmonogram przeglądów
- [Obszar] — [częstotliwość] — [właściciel]
- [Obszar] — [częstotliwość] — [właściciel]

## Wymagania wydajnościowe
- [Wymaganie] — [metryka] — [próg]
- [Wymaganie] — [metryka] — [próg]

## Wymagania dostępnościowe
- [Wymaganie] — [SLA] — [metoda pomiaru]
- [Wymaganie] — [SLA] — [metoda pomiaru]

## Wymagania skalowalności
- [Wymaganie] — [cel] — [warunki]
- [Wymaganie] — [cel] — [warunki]

## Wymagania dostępności danych
- [Dane] — [częstotliwość dostępu] — [SLA]
- [Dane] — [częstotliwość dostępu] — [SLA]

## Retencja i archiwizacja
- [Dane] — [retencja] — [archiwizacja]
- [Dane] — [retencja] — [archiwizacja]

## Dostępność w sytuacjach awaryjnych
- [Scenariusz] — [zachowanie] — [priorytet]
- [Scenariusz] — [zachowanie] — [priorytet]

## Testy i weryfikacja
- [Test] — [cel] — [wynik oczekiwany]
- [Test] — [cel] — [wynik oczekiwany]

## Walidacja zgodności
- [Wymóg] — [metoda weryfikacji]
- [Wymóg] — [metoda weryfikacji]

## Audyty i przeglądy
- [Audyty] — [częstotliwość] — [odpowiedzialny]
- [Audyty] — [częstotliwość] — [odpowiedzialny]
