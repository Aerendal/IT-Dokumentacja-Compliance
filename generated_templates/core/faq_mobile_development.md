---
title: FAQ Mobile Development
status: needs_content
aligned: true
aligned_rev: 7
aligned_at: 2026-02-09
aligned_by: codex
---
# FAQ Mobile Development


## Metadane

- Właściciel: Mobile Developer
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Zebrać najczęstsze pytania i krótkie odpowiedzi dla zespołów iOS/Android, z linkami do playbooków i runbooków (setup, build, test, release, security, perf).


## Zakres i granice

- Obejmuje: setup środowiska, build/CI/CD, signing/certyfikaty, store assets, sieć/SSL pinning/offline/cache, feature flags, testy (unit/UI/E2E/device farm), crash/ANR monitoring, rozmiar bundla, wydajność (start/jank/battery), A11y, polityki prywatności/zgody.
- Poza zakresem: pełne guideline UX i design system (linkowane).


## Użytkownicy i interesariusze
- **Mobile Developer (iOS/Android)** — projektuje i implementuje funkcje aplikacji mobilnej
- **UX/UI Designer** — dostarcza projekty interfejsu dopasowane do platform
- **QA Engineer** — testuje na urządzeniach docelowych
- **Product Owner** — definiuje wymagania funkcjonalne aplikacji

## Wejścia i wyjścia

- Wejścia: pytania z supportu dev, playbooki, runbooki, konfiguracje CI/CD, polityki security/privacy, store checklists.
- Wyjścia: lista Q&A z linkami do źródeł, status weryfikacji, plan przeglądów.



## Założenia
- Backend booking/schedule dostępny.  
- Payment provider zgodny z PCI.  
- Zespół ma proces release mobilnych.
## Otwarte pytania
- Jak obsłużyć zwroty i zmiany rezerwacji w offline?  
- Jak długo przechowywać dane biletów i telemetry?  
- Jak wspierać multi-tenant/regionalne różnice treści?
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
- Streszczenie celu i KPI
- Kontekst, założenia i ograniczenia
- Zakres oraz role/RACI
- Główne decyzje i warianty
- Proces/architektura/etapy
- Ryzyka, zależności i mitigacje
- Plan wdrożenia i kryteria akceptacji
- Monitoring i raportowanie
- Załączniki i źródła
## Szybkie powiązania

- linkage_index.jsonl (mobile/faq)
- mobile_setup_guide, mobile_ci_cd_playbook, signing_and_certificates, app_store_checklist, ssl_pinning_guide, offline_and_cache, feature_flags_policy, device_farm_playbook, crash_anr_monitoring, performance_budget_mobile, privacy_and_consent_mobile


## Mające zastosowanie standardy i normy

### Standardy międzynarodowe
- **OWASP MASVS** — Standard Weryfikacji Bezpieczeństwa Aplikacji Mobilnych (OWASP)
- **ISO/IEC 27001** — System Zarządzania Bezpieczeństwem Informacji (ISMS)
- **IEEE 829** — Dokumentacja Testowania Oprogramowania i Systemów

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

1. Dodaj Q&A w odpowiednich kategoriach, z tagami i linkami.  
2. Oznacz status/owner/datę weryfikacji; archiwizuj przestarzałe wpisy.  
3. Utrzymuj linkage_index/checklisty; planuj cykliczne przeglądy.


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
- Boarding pass: elektroniczny dokument wejścia na pokład.  
- Staged rollout: stopniowe udostępnianie wersji użytkownikom.  
- Offline-first: kluczowe dane dostępne bez połączenia.
## Przykłady użycia
- Aplikacja linii lotniczej z boarding pass i status flight.  
- Aplikacja kolejowa z biletami i mapą stacji offline.  
- Aplikacja komunikacji miejskiej z opóźnieniami i płatnościami.
## Ryzyka i ograniczenia
- Brak offline → utrata dostępu do biletów.  
- Opóźnione notyfikacje → frustracja użytkowników.  
- Błędy płatności → utrata przychodu.  
- Luka bezpieczeństwa → wycieki PII/płatności.
## Decyzje i uzasadnienia
- Model offline/cache i TTL.  
- Metody płatności i provider.  
- Priorytety notyfikacji i częstotliwość.  
- Strategie rollout i monitoring KPI.
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

- [ ] Każde Q&A ma link do źródła; status/owner/data weryfikacji podane.  
- [ ] Kategorie/tagi spójne; przestarzałe wpisy oznaczone/archiwizowane.  
- [ ] Relacje cross‑doc opisane; dokument w linkage_index.


## Lista kontrolna spójności relacji

- [ ] Czy każda sekcja z relacją ma wskazaną sekcję źródłową?
- [ ] Czy relacje nie tworzą sprzecznych wymagań?
- [ ] Czy wszystkie wymagane standardy mają odwołania?
- [ ] Czy RACI jest kompletne dla kluczowych działań?

## Artefakty powiązane

- Lista Q&A (CSV/MD/DB), log zmian, snapshot statystyk, linki do playbooków/runbooków, waiver log (jeśli wpis tymczasowo bez pełnego źródła).


## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji

- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status: oczekuje/zatwierdzone/odrzucone]
- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status]

## Metryki jakości

- Czas znalezienia odpowiedzi, liczba przestarzałych wpisów, % Q&A z linkiem, użycie FAQ w ticketach, liczba aktualizacji po release/SDK zmianie.

## Kryteria ukończenia

- [ ] FAQ aktualne i podlinkowane; wersja/data/właściciel aktualne; dokument w linkage_index.


## Struktura sekcji

1) Jak korzystać (IA, tagi, aktualizacje)  
2) Kategorie: Setup, Build/CI/CD, Signing/Store, Network/Security, Offline/Cache, Testy/Device Farm, Monitoring/Crash/ANR, Performance/Bundle, A11y/Privacy.  
3) Q&A w kategoriach (pytanie, krótka odpowiedź, linki, owner, data weryfikacji, tagi, status)  
4) Polityka aktualizacji (cadence, kto weryfikuje, kryteria archiwizacji)  
5) Załączniki: szablon wpisu, log zmian


## Wymagane rozwinięcia

- Lista kategorii/tagów i zasady nazewnictwa.  
- Szablon Q&A (≤2–3 zdania + linki).  
- Linki do: setup (Xcode/Android Studio, SDK), fastlane/gradle configs, signing/profiles, store checklists, SSL pinning/offline/cache guide, feature flags policy, test matrix/device farm, crash/ANR monitoring, perf budget (startup/jank/battery/size), A11y/privacy.


## Wymagane streszczenia

- Snapshot: top P0 pytania, ostatnie aktualizacje, coverage kategorii.


## Guidance (skrót)

- Odpowiadaj krótko, zawsze linkuj do playbooków; utrzymuj datę weryfikacji.  
- Dodawaj przykłady komend/skryptów (fastlane/gradle) w linkach, nie w treści Q&A.  
- Aktualizuj po zmianach SDK/CI/store policies; oznacz przestarzałe wpisy.


## Checklisty Definition of Ready (DoR)

- [ ] Kategorie/tagi i szablon Q&A zdefiniowane; źródła playbooków zebrane.  
- [ ] Ownerzy wpisów wskazani; polityka aktualizacji ustalona.


## Checklisty Definition of Done (DoD)

- [ ] Q&A dodane z linkami, tagami, statusem i datą weryfikacji.  
- [ ] Snapshot/statystyki zaktualizowane; log zmian zapisany.  
- [ ] Dokument w linkage_index; metadane aktualne.

