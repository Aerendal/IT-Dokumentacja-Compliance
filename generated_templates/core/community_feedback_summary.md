---
title: Community Feedback Summary
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Community Feedback Summary


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Podsumowuje feedback społeczności (fora, NPS/CSAT, social, support) w danym okresie, identyfikuje tematy, priorytety i rekomendacje. Ma pomóc w podejmowaniu decyzji produktowych i operacyjnych.


## Zakres i granice

- Obejmuje: źródła feedbacku, kategoryzację/tematy, sentyment, priorytety (impact/frequency), rekomendacje i akcje, eskalacje, metryki (NPS/CSAT/volume), trend vs poprzedni okres, ryzyka reputacyjne.
- Poza zakresem: szczegółowe roadmap decyzje (link), indywidualne ticket handling.


## Użytkownicy i interesariusze

- Community/Support, Product, Analytics, Marketing, Leadership.


## Wejścia i wyjścia

- Wejścia: dane z forów/social/support/NPS/CSAT/ankiet, logi ticketów, kategorie/tematy, dane usage (kontekst), release/flags, incydenty.
- Wyjścia: raport tematów i priorytetów, rekomendacje działań (produkt/UX/support), eskalacje, metryki i trend, lista open issues, linki do backlogu.


## Założenia

- Dostęp do danych i kanałów; współpraca Product/Support/Analytics.


## Otwarte pytania

- Czy włączamy dane sprzedaż/utrata klientów? 
- Jaka częstotliwość raportu (mies./kw.)?


## Powiązania (meta)

- Key Documents: user_feedback_escalation, community_health_metrics, product_strategy, search_improvement_plan (jeśli dotyczy), incident_postmortems.
- Key Document Structures: źródła, tematy, metryki, rekomendacje, działania.
- Document Dependencies: narzędzia zbierające feedback, analytics, backlog/issue tracker, release data.


## Zależności dokumentu

Wymaga: danych feedback (źródła) i kategorii, metryk (NPS/CSAT/volume), narzędzi analitycznych, dostępu do backlogu. Bez tego DoR otwarte.


## Fazy cyklu życia

- Zbieranie i kategoryzacja danych.
- Analiza tematów i priorytetów; sentyment/trend.
- Rekomendacje i plan działań; eskalacje.
- Raport i follow‑up; ocena efektu w kolejnym cyklu.



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

- linkage_index.jsonl (community/feedback_summary)
- user_feedback_escalation, community_health_metrics, product_strategy, search_improvement_plan, incident_postmortems


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

1. Zbierz dane z kanałów; policz metryki; skategoryzuj tematy.
2. Ustal priorytety i rekomendacje; przypisz ownerów/ETA; dodaj do backlogu.
3. Raportuj eskalacje i ryzyka; śledź realizację i efekt w kolejnym cyklu.


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

- NPS, CSAT, Sentiment, Impact, Frequency, Eskalacja.


## Przykłady użycia

- Cykl miesięczny: spadek NPS, top temat: wyszukiwarka, rekomendacje backlog; eskalacja P0 incydentu.


## Ryzyka i ograniczenia

- Bias źródeł; brak taksonomii → chaos; brak follow‑up → brak poprawy.


## Decyzje i uzasadnienia

- [Decyzja] Taksonomia/priorytety — uzasadnienie wpływu; [Decyzja] Kanały w scope — uzasadnienie reprezentatywności.


## Powiązania z innymi dokumentami

- User Feedback Escalation, Community Health Metrics, Product Strategy, Search Improvement, Incident Postmortems.


## Powiązania z sekcjami innych dokumentów

- Feedback Escalation → eskalacje; Community Health → metryki; Product Strategy → priorytety.


## Słownik pojęć w dokumencie

- NPS, CSAT, Sentiment, Impact, Frequency, Eskalacja.


## Wymagane odwołania do standardów

- Polityki privacy/consent; zasady komunikacji klienta.


## Mapa relacji sekcja→sekcja

- Dane/Metryki → Tematy → Priorytety → Rekomendacje → Backlog → Follow‑up.


## Mapa relacji dokument→dokument

- Feedback Summary → Escalation/Health/Product → Backlog/Release.


## Ścieżki informacji

- Kanały → Analiza → Priorytety → Backlog → Raport → Kolejny cykl.


## Weryfikacja spójności

- [ ] Metryki i tematy spójne; rekomendacje mają owner/ETA; eskalacje opisane.
- [ ] Relacje cross‑doc opisane; dokument w linkage_index.


## Lista kontrolna spójności relacji

- [ ] Każdy temat ma dane/metryki, priorytet i rekomendacje.
- [ ] Każda rekomendacja ma owner/ETA i link do backlogu.
- [ ] Relacje cross‑doc opisane z uzasadnieniem.


## Artefakty powiązane

- Dashboardy NPS/CSAT, dane feedback, taksonomia, raport, backlog linki.


## Ścieżka decyzji

- [Decyzja] → [Uzasadnienie] → [Konsekwencje] → [Właściciel] → [Data].


## Ścieżka akceptacji

- Community/Support → Product/Analytics → Leadership → Owner sign‑off.


## Metryki jakości

- Zmiana NPS/CSAT, czas reakcji na feedback, odsetek zrealizowanych rekomendacji, liczba eskalacji.

## Kryteria ukończenia

- [ ] Raport/tematy/rekomendacje gotowe; dokument w linkage_index; wersja/data/właściciel aktualne.


## Powiązania sekcja↔sekcja

- Źródła/metryki → Tematy → Priorytety → Rekomendacje → Działania/backlog.
- Release/incydenty → Tematy → Priorytety.


## Struktura sekcji

1) Zakres okresu i źródeł (czas, kanały, wolumen)  
2) Metryki i trend (NPS/CSAT/volume/sentiment)  
3) Top tematy i priorytety (impact/frequency, segmenty)  
4) Rekomendacje i akcje (produkt/UX/support/policy) z owner/ETA  
5) Eskalacje i ryzyka reputacyjne  
6) Linki do backlogu/issue tracker, status działań  
7) Wnioski i plan na kolejny okres


## Wymagane rozwinięcia

- Metryki (NPS/CSAT, volume) i trend; metodologia kategoryzacji i priorytetyzacji.
- Lista top tematów z danymi; rekomendacje z owner/ETA; eskalacje.


## Wymagane streszczenia

- Najważniejsze metryki/trend, top 3 tematy, top 3 rekomendacje, eskalacje.


## Guidance (skrót)

- Używaj spójnej taksonomii tematów; łącz dane ilościowe i jakościowe.
- Priorytetyzuj według impact/frequency i ryzyka reputacji; loguj eskalacje.
- Linkuj rekomendacje do backlogu; śledź realizację i efekt w kolejnym cyklu.


## Checklisty Definition of Ready (DoR)

- [ ] Dane feedback z kanałów; metryki NPS/CSAT/volume dostępne.
- [ ] Taksonomia tematów uzgodniona; narzędzia analityczne dostępne.
- [ ] Struktura sekcji wypełniona/N/A.


## Checklisty Definition of Done (DoD)

- [ ] Metryki/trend policzone; top tematy/prior. opisane; rekomendacje z owner/ETA.
- [ ] Eskalacje/ryzyka opisane; linki do backlogu; dokument w linkage_index.
- [ ] Wersja/data/właściciel zaktualizowane.

