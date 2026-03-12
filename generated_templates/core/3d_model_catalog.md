---
title: 3D Model Catalog
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# 3D Model Catalog

## Metadane
- Właściciel: ML Engineer
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


> Powiązania: linkage_index.jsonl

## Cel dokumentu
Utworzyć i utrzymać katalog modeli 3D z kluczowymi metadanymi (typ, styl, formaty, LOD, kolizje, licencje, właścicielstwo, status QA), aby ułatwić wyszukiwanie, ponowne użycie, zgodność techniczną i zarządzanie licencjami.

## Zakres i granice
- Obejmuje: strukturę katalogu, wymagane pola metadanych, standardy techniczne (formaty, skala, PBR/UV/LOD), statusy QA, licencje/prawa, wersjonowanie, powiązania z asset store/DCC/silnikiem, proces dodawania/aktualizacji/deprecjacji.
- Poza zakresem: szczegółowe specyfikacje pojedynczych assetów (w ich spec), pipeline budowy modeli (oddzielne dokumenty).

## Wejścia i wyjścia
- Wejścia: lista istniejących modeli, wymagania techniczne (formaty, skala, PBR, LOD, kolizje), prawa/licencje (OSS/stock/własne), źródła DCC, repozytoria, QA statusy.
- Wyjścia: katalog (DB/arkusz/asset manager) z metadanymi, raport luk/duplikatów, checklisty QA/akceptacji, wytyczne dla nowych wpisów.

## Powiązania (meta)
- Wymaga odniesienia do: Key Documents
- Wymaga odniesienia do: Key Document Structures
- Wymaga odniesienia do: Document Dependencies
- Wymaga odniesienia do: RACI i role
- Wymaga odniesienia do: Standardy i compliance

## Zależności dokumentu
Jeżeli brak danych w bazie: wypisz znane zależności (dokumenty, kontrakty, usługi), wskaż właścicieli i wpływ na kolejność prac; gdy brak zależności – zapisz to wprost.

## Powiązania sekcja↔sekcja
Określ, które sekcje wymagają rozwinięcia lub streszczenia (np. gdy są kluczowe dla decyzji, ryzyka lub zgodności) i podaj uzasadnienie.

## Fazy cyklu życia
- Faza 1: Koncepcja i Wizja: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 2: Analiza Wymagań: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 3: Projekt / Design: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 4: Planowanie: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 5: Implementacja: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 6: Testowanie / QA: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 7: Bezpieczeństwo / Compliance: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 8: Wdrożenie / Deployment: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 9: Operacje / Maintenance: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 10: Incident Management: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 11: Monitoring / Observability: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 12: Dokumentacja referencyjna: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 13: Szkolenie / Onboarding: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 14: Komunikacja stakeholders: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 15: Knowledge Management: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 16: Postmortem / Retrospektywa: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 17: Budżetowanie / Cost Management: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 18: Vendor Management: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 19: Governance / Compliance: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 20: Decommission / Sunset: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 21: DR / BCP: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 22: Change Management: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 23: Capacity Planning: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.


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
- Struktura katalogu: kategorie, tagi, słowniki (typ, styl, platforma).
- Metadane obowiązkowe: nazwa, ID, kategoria/tags, styl, platforma, skala/jednostki, formaty (fbx/gltf), LOD (liczba, progi), kolizje, UV/texel density, mapy PBR, materiały, wersja, właściciel, status QA, data, linki (repo/engine/preview), licencja/prawa.
- Standardy techniczne: wymagane formaty, naming, pivot/origin, orientacja osi, skala, mapy, texel density, PBR, LOD, kolizje.
- Proces katalogowania: dodanie nowego modelu, review, QA, oznaczanie deprecated, aktualizacje wersji.
- Licencje i prawa: rodzaj licencji, źródło (stock/OSS/custom), atrybucje, ograniczenia użycia, dowody.
- Integracje: asset manager/DB, DCC → engine pipeline, generowanie miniaturek/podglądów.
- Raporty i audyt: duplikaty, braki metadanych, statusy QA, raport licencji.

## Wymagane rozwinięcia
- Standardy techniczne → 3D Asset Design Specification, Graphics Architecture.
- Licencje → Asset Copyright Compliance.
- QA → 3D Model QA/Testing guidelines.
- Integracje → pipeline DCC/engine, asset manager.

## Wymagane streszczenia
- Streszczenie braków metadanych/licencji i planu uzupełnień.
- Streszczenie stanu QA (np. % modeli „approved” vs „pending”).

## Guidance
Cel: skrócone wskazówki do wypełniania szablonów dokumentów (core/satellite).

- Cel dokumentu: 2–3 zdania o decyzjach, ryzykach i wartości dokumentu.
- Zakres i granice: co obejmuje (systemy/procesy/zespoły) i czego nie obejmuje; zaznacz granice odpowiedzialności.
- Wejścia: dane, wymagania, standardy, zależności potrzebne przed startem.
- Wyjścia: artefakty/rezultaty, kto je konsumuje, format (link/plik).
- Zależności dokumentu: wymagane dokumenty lub decyzje; właściciel; wpływ na kolejność prac.
- Powiązania sekcja↔sekcja: które sekcje się rozwijają/streszczają; podaj uzasadnienie.
- Struktura sekcji: utrzymuj układ logiczny; sekcje bez treści oznacz jako N/A z krótkim uzasadnieniem.
- Fazy cyklu życia: zaznacz, w których fazach dokument powstaje/aktualizuje się/archiwizuje; kto odpowiada.
- DoR (Definition of Ready): zakres, wejścia, role, zależności, kryteria akceptacji gotowe.
- DoD (Definition of Done): sekcje uzupełnione lub N/A, powiązania wpisane, checklisty jakości sprawdzone, wersja/data/właściciel, linki/artefakty działają.
- Język: polski; nazwy własne pozostają bez zmian; liczby w nazwach plików usunięte już w szablonach.
- Filozofia: optymalizuj przez rozwój, nie ucinanie — dodawaj, nie kasuj; elementy „satelitarne” zostają.

odwołania.

## Szybkie powiązania
- Meta: Key Documents
- Meta: Key Document Structures
- Meta: Document Dependencies

## Mające zastosowanie standardy i normy

### Standardy międzynarodowe
- **ISO/IEC 23053** — Framework dla Systemów AI z Uczeniem Maszynowym
- **ISO/IEC 42001** — System Zarządzania Sztuczną Inteligencją (AIMS)
- **NIST CSF** — Framework Cyberbezpieczeństwa NIST

> Sekcja generowana automatycznie. Zweryfikuj trafność i uzupełnij o dodatkowe normy/regulacje specyficzne dla kontekstu projektu.
## Jak używać dokumentu
- Przeczytaj sekcje "Cel dokumentu" i "Zakres i granice" i upewnij się, że opisują Twój przypadek.
- Wypełniaj kolejne sekcje zgodnie z guidance i powiązaniami; korzystaj z kryteriów DoR/DoD w `reports/checklist_atomic.jsonl`.
- Aktualizuj statusy w checklistach (structure/clarity/links, DoR/DoD), gdy sekcje są gotowe lub oznaczone jako N/A.


## Checklisty jakości (DoR/DoD skrót)
- DoR:
  - [ ] Zebrana lista modeli i źródeł; znane wymagania techniczne.
  - [ ] Ustalony właściciel katalogu i narzędzie/DB do przechowywania.
- DoD:
  - [ ] Katalog zawiera obowiązkowe metadane, linki, licencje i statusy QA.
  - [ ] Standardy techniczne i proces dodawania/aktualizacji opisane; raporty braków działają.
  - [ ] Sekcje N/A uzasadnione; metadane aktualne.

## Definicje robocze
- [Termin 1] — [definicja robocza]
- [Termin 2] — [definicja robocza]
- [Termin 3] — [definicja robocza]

## Przykłady użycia
- [Przykład 1 — krótki opis sytuacji i zastosowania]
- [Przykład 2 — krótki opis sytuacji i zastosowania]

## Ryzyka i ograniczenia
- [Ryzyko 1 — wpływ i sposób ograniczenia]
- [Ryzyko 2 — wpływ i sposób ograniczenia]

## Decyzje i uzasadnienia
- [Decyzja 1 — uzasadnienie]
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
- **ML Engineer / Data Scientist** — buduje, trenuje i ewaluuje modele
- **Data Engineer** — przygotowuje dane i zarządza pipeline'ami
- **Product Owner** — definiuje metryki sukcesu i priorytety eksperymentów
- **MLOps Engineer** — zarządza wdrożeniem i monitoringiem modeli na produkcji

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
