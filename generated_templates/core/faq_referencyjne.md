---
title: FAQ (referencyjne)
status: needs_content
aligned: true
aligned_rev: 6
aligned_at: 2026-02-09
aligned_by: codex
---
# FAQ (referencyjne)


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Zebrać najczęstsze pytania i krótkie odpowiedzi z linkami do źródeł, aby przyspieszyć wsparcie i samopomoc zespołów/użytkowników.


## Zakres i granice

- Obejmuje: kategorie/IA, pytanie→odpowiedź→linki, datę/owner odpowiedzi, tagi i wyszukiwalność, status (aktualne/zweryfikowane), politykę aktualizacji.
- Poza zakresem: pełna dokumentacja techniczna (linkowana), polityki firmowe (linkowane).


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia

- Wejścia: logi pytań z supportu/fora/chat, dokumentacja referencyjna, decyzje/ADR, runbooki.
- Wyjścia: skategoryzowana lista Q&A, tagi i linki, status weryfikacji, plan przeglądu.


## Założenia

- Dostęp do repo dokumentacji i logów supportu; dedykowany owner FAQ.


## Otwarte pytania

- Jakie SLA aktualizacji po release?  
- Czy potrzebne są wersje językowe FAQ?


## Powiązania (meta)

- Key Documents: knowledge_base, support_runbook, product_docs, troubleshooting_guides, release_notes.
- Key Document Structures: pytanie, odpowiedź, linki, tagi, status.
- Document Dependencies: repo dokumentacji, ticketing/support, search/IA narzędzia.



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

- linkage_index.jsonl (knowledge/faq)
- knowledge_base, support_runbook, product_docs, troubleshooting_guides, release_notes


## Mające zastosowanie standardy i normy

### Standardy międzynarodowe
- **ISO/IEC 12207** — Procesy Cyklu Życia Oprogramowania
- **PMBOK 7** — Przewodnik po Zarządzaniu Projektami (PMI)
- **ITIL 4** — Biblioteka Infrastruktury IT (Zarządzanie Usługami)

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

1. Ustal kategorie/tagi; dodaj Q&A w szablonie.  
2. Linkuj do dokumentów źródłowych/runbooków; oznacz status i datę weryfikacji.  
3. Planuj cykliczne przeglądy; aktualizuj linkage_index/checklisty.


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

- Przestarzałe odpowiedzi wprowadzają w błąd; brak linków → długa diagnoza; brak właściciela → brak aktualizacji.


## Decyzje i uzasadnienia

- [Decyzja] Struktura kategorii/tagów; [Decyzja] Cadence przeglądów; [Decyzja] Kryteria archiwizacji.


## Powiązania z innymi dokumentami

- Knowledge Base, Support Runbook, Product Docs, Troubleshooting Guides, Release Notes.


## Powiązania z sekcjami innych dokumentów

- Release Notes → nowe Q&A; Runbooki → szczegóły procedur; KB → treści referencyjne.


## Słownik pojęć w dokumencie

- FAQ, IA, Tag, Owner, Review cadence, Archived.


## Wymagane odwołania do standardów

- Wewnętrzne standardy dokumentacji/knowledge management.


## Mapa relacji sekcja→sekcja

- Kategorie/tagi → Q&A → Snapshot → Aktualizacje.


## Mapa relacji dokument→dokument

- FAQ → Knowledge Base/Runbooki/Docs → Release Notes → Support.


## Ścieżki informacji

- Support/logi pytań → Q&A → Linki do źródeł → Aktualizacje/archiwizacja.


## Weryfikacja spójności

- [ ] Każde Q&A ma link do źródła/runbooka; status/owner/data weryfikacji podane.  
- [ ] Kategorie/tagi spójne; przestarzałe wpisy oznaczone/archiwizowane.  
- [ ] Relacje cross‑doc opisane; dokument w linkage_index.


## Lista kontrolna spójności relacji

- [ ] Czy każda sekcja z relacją ma wskazaną sekcję źródłową?
- [ ] Czy relacje nie tworzą sprzecznych wymagań?
- [ ] Czy wszystkie wymagane standardy mają odwołania?
- [ ] Czy RACI jest kompletne dla kluczowych działań?

## Artefakty powiązane

- Lista Q&A (CSV/MD/DB), log zmian, snapshot statystyk, linki do źródeł, szablon wpisu, waiver log (jeśli info zostaje tymczasowo bez źródła).


## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji

- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status: oczekuje/zatwierdzone/odrzucone]
- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status]

## Metryki jakości

- Średni czas znalezienia odpowiedzi, liczba przestarzałych wpisów, liczba Q&A bez linku źródłowego, częstotliwość aktualizacji, wykorzystanie FAQ w ticketach.

## Kryteria ukończenia

- [ ] Q&A aktualne, otagowane, z linkami i statusami; dokument w linkage_index.  
- [ ] Wersja/data/właściciel aktualne.


## Struktura sekcji

1) Jak korzystać z FAQ (zakres, aktualizacja, kontakt)  
2) Kategorie i tagi (mapa IA)  
3) Lista Q&A (pytanie, krótka odpowiedź, linki, właściciel, data weryfikacji, tagi, status)  
4) Polityka aktualizacji i przeglądów (cadence, kto weryfikuje, kryteria usunięcia/archiwizacji)  
5) Załączniki: szablon wpisu, log zmian


## Wymagane rozwinięcia

- Definicja kategorii/tagów i zasad nazewnictwa.  
- Szablon rekordu Q&A (pytanie, odpowiedź ≤ N zdań, linki, owner, data, status).  
- Harmonogram przeglądów i kryteria archiwizacji/aktualizacji.


## Wymagane streszczenia

- Snapshot: liczba Q&A per kategoria, ostatnie aktualizacje, top 5 najczęstszych pytań.


## Guidance (skrót)

- Odpowiadaj zwięźle, maks 2–3 zdania; resztę linkuj.  
- Utrzymuj datę weryfikacji i ownera; oznacz przestarzałe i zaplanuj update.  
- Łącz z runbookami i dokumentacją źródłową; dodawaj tagi dla wyszukiwania.


## Checklisty Definition of Ready (DoR)

- [ ] Źródła pytań zebrane; kategorie/tagi zdefiniowane.  
- [ ] Szablon Q&A uzgodniony; ownerzy wyznaczeni.  
- [ ] Reguły weryfikacji/archiwizacji określone.


## Checklisty Definition of Done (DoD)

- [ ] Q&A dodane z linkami/tagami; status i data weryfikacji uzupełnione.  
- [ ] Snapshot/statystyki zaktualizowane; log zmian uzupełniony.  
- [ ] Dokument w linkage_index/checklistach; metadane aktualne.

