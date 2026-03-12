---
title: Risk Management Plan
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# Risk Management Plan

## Metadane
- Właściciel: Project Manager
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


> Powiązania: linkage_index.jsonl

## Cel dokumentu
Zdefiniować podejście do identyfikacji, oceny, mitygacji i monitorowania ryzyk projektu/produktu. Zapewnia spójne zasady, role i cykl przeglądów, by minimalizować wpływ ryzyk na zakres, czas, koszt i jakość.

## Zakres i granice
Obejmuje: metodykę oceny (skala P/I, RAG), kategorie ryzyk, role i RACI, proces mitygacji, raportowanie, tolerancje ryzyka, integrację z harmonogramem, testami i zmianami. Nie obejmuje: szczegółowej listy pojedynczych ryzyk (ta jest w Risk Register).

## Ryzyko akceptowalne (risk appetite) i tolerancje
- Dostępność: tolerancja na przestoje ≤ RTO, utrata danych ≤ RPO; krytyczne systemy produkcyjne: brak akceptacji dla utraty transakcji.
- Bezpieczeństwo: brak akceptacji dla incydentów P1 dotyczących danych wrażliwych; incydenty P2/P3 do akceptacji, jeśli mitigacja ≤ X dni.
- Budżet: odchylenie ±5–10% w zależności od fazy; koszt mitygacji nie może przekraczać wartości zredukowanego ryzyka.
- Regulacje: zero‑tolerance dla niezgodności obowiązkowych (SOX/ISO 27001/PCI DSS/HIPAA); wyjątki dokumentowane w „Risk Acceptance Log” z datą wygaśnięcia.

## Wejścia i wyjścia
- Wejścia: cele projektu, WBS/harmonogram, architektura, wymagania (FRS/NFR), polityki korporacyjne, lekcje z postmortemów.
- Wyjścia: zasady oceny i akceptacji ryzyk, cykl przeglądów, szablon raportowania, powiązania z planem testów, zmian i releasów.

## Powiązania (meta)
- Wymaga odniesienia do: Key Documents
- Wymaga odniesienia do: Key Document Structures
- Wymaga odniesienia do: Document Dependencies
- Wymaga odniesienia do: RACI i role
- Wymaga odniesienia do: Standardy i compliance

## Zależności dokumentu
- Konsumuje: Project Charter, Risk Assessment, Postmortem learnings, Security/Compliance wymagania.
- Dostarcza do: Risk Register, Harmonogram (bufory), Test Strategy/Plans, Change/Release plans, Communication plan.

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
- Cel, zakres, risk appetite/tolerancje.
- Metodyka oceny: skala P (1–5) × I (1–5) = wynik; progi RAG (zielony ≤5, żółty 6–12, czerwony ≥15); opcjonalnie wykrywalność (D) dla FMEA.
- Kategorie ryzyk: biznes (przychody, KPI), techniczne (architektura, wydajność, skalowalność), bezpieczeństwo (CIA, IAM, kryptografia), operacyjne (procesy, zmiany), vendor/supply chain, regulacyjne/compliance, dane/AI, dostępność (RTO/RPO), reputacyjne.
- Role i RACI: Sponsor (A), Risk Owner (R), Risk Manager (R), Architekt/Tech Lead (C), Security/Compliance (C), PM (A/R), QA (C), Legal/Privacy (C), Ops/SRE (R/C), Steering Committee (I).
- Proces: identyfikacja → ocena (P/I/D, RAG) → wybór reakcji (avoid/mitigate/transfer/accept) → plan mitygacji z właścicielami i terminami → monitorowanie metryk → eskalacja.
- Powiązanie z harmonogramem: bufory na ryzyka czerwone, warunki „go/no‑go”, punkty kontroli na kamieniach milowych.
- Raportowanie i cykl przeglądów: tygodniowo dla czerwonych, dwutygodniowo dla żółtych, miesięcznie dla zielonych; format: dashboard + notatka ryzyka; eskalacja P1 do Steering Committee ≤24h.
- Integracja z testami/QA: ryzyka wpływają na priorytety testów, testy bezpieczeństwa/regresji dla mitygacji, kryteria wyjścia release zaktualizowane o ryzyka czerwone.
- Integracja z Change/Release/Incident/Problem: każde change request ma ocenę ryzyka; incydenty wysokie tworzą nowe ryzyka; postmortem aktualizuje rejestr.
- Narzędzia/artefakty: Risk Register (ID, opis, P/I/RAG, właściciel, akcje, daty), Risk Acceptance Log, Risk Heatmap, dashboard (BI/Observability), checklisty DoR/DoD, linkage_index.jsonl.
- Audyt i dowody: log decyzji, daty przeglądów, potwierdzenia wdrożeń mitygacji (ticket, commit, runbook), wyniki testów regresji bezpieczeństwa.

## Wymagane rozwinięcia
- Metodyka oceny: rozwinięcie ze standardów ISO 31000 / ISO 27005 / NIST SP 800‑30.
- Risk appetite: odwołanie do Polityki Ryzyka organizacji lub dokumentu „Risk Appetite Statement”.
- Kategoryzacja: powiązanie z katalogiem ryzyk bezpieczeństwa (CIS, OWASP, STRIDE) i ryzyk operacyjnych (ITIL/ISO 20000).
- Integracja z testami: rozwinięcie w „Test Strategy” i „Security Testing Plan”.
- Proces zmian: rozwinięcie w „Change Management Plan”.

## Wymagane streszczenia
- Streszczenie risk appetite i tolerancji na pierwszej stronie (executive summary).
- Streszczenie top 10 ryzyk (RAG, właściciel, ETA mitygacji) do komunikacji z C‑level.
- Streszczenie decyzji o akceptacji ryzyk z datą wygaśnięcia.

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
- **CIS Controls v8** — Krytyczne Mechanizmy Bezpieczeństwa (CIS)
- **ISO/IEC 27001** — System Zarządzania Bezpieczeństwem Informacji (ISMS)
- **ISO/IEC 27002** — Wytyczne Praktyk Bezpieczeństwa Informacji
- **ISO/IEC 27005** — Zarządzanie Ryzykiem Bezpieczeństwa Informacji
- **NIST CSF** — Framework Cyberbezpieczeństwa NIST

> Sekcja generowana automatycznie. Zweryfikuj trafność i uzupełnij o dodatkowe normy/regulacje specyficzne dla kontekstu projektu.
## Jak używać dokumentu
- Przeczytaj sekcje "Cel dokumentu" i "Zakres i granice" i upewnij się, że opisują Twój przypadek.
- Wypełniaj kolejne sekcje zgodnie z guidance i powiązaniami; korzystaj z kryteriów DoR/DoD w `reports/checklist_atomic.jsonl`.
- Aktualizuj statusy w checklistach (structure/clarity/links, DoR/DoD), gdy sekcje są gotowe lub oznaczone jako N/A.


## Checklisty jakości
- [ ] Cel i zakres opisują rodzaj ryzyk oraz ograniczenia (co poza zakresem).
- [ ] Risk appetite i tolerancje są jawne dla głównych domen (bezpieczeństwo, dostępność, koszt, regulacje).
- [ ] Skala P/I (i D jeśli użyta) jest zdefiniowana liczbowo z progami RAG.
- [ ] Kategorie ryzyk są dopasowane do projektu (biznes/tech/operacje/security/vendor/regulacje/AI).
- [ ] Role i RACI mają przypisanych właścicieli i zastępstwa.
- [ ] Proces reakcji na ryzyko ma terminy, kryteria eskalacji i wzory komunikatów.
- [ ] Raportowanie ma ustalony rytm, format i odbiorców; heatmapa generowana.
- [ ] Integracje (Test/Change/Release/Incident/Problem) są opisane i mają punkty kontrolne.
- [ ] Risk Register i Risk Acceptance Log są połączone linkiem/ID z tym planem.
- [ ] Kryteria DoR/DoD poniżej są spełnione lub oznaczone N/A z uzasadnieniem.

## Definicje robocze
- Prawdopodobieństwo (P) — subiektywny lub historyczny poziom szans wystąpienia; skala 1 (bardzo mało prawdopodobne) do 5 (pewne/≥50% w horyzoncie).
- Wpływ (I) — konsekwencja dla zakresu/czasu/kosztu/jakości/bezpieczeństwa/regulacji; skala 1 (pomijalne) do 5 (katastrofalne).
- Akceptacja ryzyka — formalna zgoda sponsora/Steering Committee na pozostawienie ryzyka z określonym terminem przeglądu i warunkami cofnięcia.

## Przykłady użycia
- Migracja do chmury: mapowanie ryzyk danych wrażliwych (lokalizacja, szyfrowanie, klucze), zależności sieciowych, cutover i rollback.
- Wprowadzenie nowego dostawcy: ocena ryzyk SLA, ciągłości usług, lock‑in, poddostawców, zgodności (SOC 2/ISO 27001), plan wyjścia.

## Ryzyka i ograniczenia
- Brak spójnej skali P/I w zespołach → ujednolicić skale i dodać przykłady progu dla każdej domeny.
- Akceptacje bez daty wygaśnięcia → wymagaj daty przeglądu, warunków cofnięcia, właściciela.
- Ryzyka bezpieczeństwa nieuwzględnione w harmonogramie → dodać bufory i warunki „no‑go” dla brakujących mitygacji krytycznych.

## Decyzje i uzasadnienia
- Wybór metodyki P×I (bez D) dla prostoty — uzasadnienie: spójność z resztą portfela; D dodawane tylko dla FMEA systemów krytycznych.
- Progi RAG: zielony ≤5/żółty 6–12/czerwony ≥15 — uzasadnienie: zgodne z ISO 27005 i stosowane w raportowaniu do zarządu.

## Założenia
- Zespoły używają jednego narzędzia do rejestru ryzyk (np. tracker w DB lub arkusz powiązany).
- Wszystkie mitygacje mają testy regresji bezpieczeństwa lub scenariusze UAT odzwierciedlające ryzyko.

## Otwarte pytania
- Czy dla tego projektu potrzebna jest ocena TPRM (Third‑Party Risk Management) dla nowych vendorów?
- Czy heatmapa ma być publikowana w raportach dla regulatora (jeśli tak, w jakim formacie)?

## Powiązania z innymi dokumentami
- Risk Register — dostarcza listę ryzyk i statusów → ten plan definiuje metodę i akceptacje.
- Security/Compliance Requirements — źródło obowiązków prawnych/regulacyjnych.
- Test Strategy / Security Testing Plan — używa priorytetów z ryzyk do kolejności testów.
- Change Management Plan — wymaga oceny ryzyka dla każdego change request.

## Powiązania z sekcjami innych dokumentów
- Incident Response Plan → Lessons Learned/Postmortem → aktualizacja ryzyk czerwonych i żółtych.
- Architecture Decision Records → decyzje o kryptografii/IAM → ryzyka projektowe i bezpieczeństwa.
- Service Level Objectives → sekcja dostępności → wpływ na I (impact) i tolerancje.

## Słownik pojęć w dokumencie
- RTO/RPO — Recovery Time / Recovery Point Objective; źródło: BCP/DR standard.
- Residual Risk — ryzyko po wdrożeniu mitygacji; akceptowane formalnie przez sponsora.
- Single Point of Failure (SPOF) — element, którego awaria zatrzymuje usługę; należy zmapować i mitygować.

## Wymagane odwołania do standardów
- ISO 31000 / ISO 27005 — metodyka zarządzania ryzykiem i scoring.
- NIST SP 800‑30 — proces oceny ryzyk; uzupełnia sekcję metodyki.
- SOC 2 / ISO 27001 A.8 / PCI DSS — wymagają dowodów istnienia procesu zarządzania ryzykiem i akceptacji.

## Mapa relacji sekcja→sekcja
- Risk Appetite -> Metodyka oceny : progi RAG zależą od tolerancji.
- Metodyka oceny -> Raportowanie : heatmapa i dashboard bazują na scoringu.
- Proces reakcji -> Harmonogram : mitygacje dodają bufory i warunki „go/no‑go”.
- Raportowanie -> Eskalacja : czerwone ryzyka eskalowane do Steering Committee.

## Mapa relacji dokument→dokument
- Risk Management Plan -> Risk Register : definiuje sposób uzupełniania.
- Risk Management Plan -> Change/Release Plan : nakłada obowiązek oceny ryzyk przed wdrożeniem.
- Risk Management Plan -> Incident/Postmortem : wymusza aktualizację ryzyk po incydencie.

## Ścieżki informacji
- „Nowy vendor chmurowy” → Identyfikacja ryzyk → Kategoria vendor/TPRM → Plan mitygacji + testy dostawcy → Aktualizacja Risk Register i warunki SLA.
- „Zmiana architektury (monolit → mikroserwisy)” → Analiza techniczna → Kategoria techniczne/operacyjne → Bufory wdrożenia + testy regresji → warunki release „go/no‑go”.
- „Regulator żąda raportu” → Ryzyka regulacyjne → Raportowanie → Streszczenie top ryzyk + dowody mitygacji → Komunikacja z C‑level/regulatorem.

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
- **Project Manager** — prowadzi projekt, raportuje status i zarządza ryzykami
- **Project Sponsor** — akceptuje kluczowe decyzje i zapewnia zasoby
- **Development Team** — realizuje zadania zgodnie z planem
- **Stakeholders / Interesariusze** — odbierają raportowanie i zgłaszają zmiany zakresu

## Ścieżka akceptacji
- [Kto zatwierdza] → [kryteria akceptacji] → [status]
- [Kto zatwierdza] → [kryteria akceptacji] → [status]

## Kryteria ukończenia (DoD)
- DoR spełnione; risk appetite/tolerancje wpisane.
- Skala P/I (i D jeśli stosowana) oraz progi RAG opisane.
- Kategorie ryzyk i RACI uzupełnione; właściciele przypisani.
- Proces reakcji i eskalacji opisany z czasami i kanałami komunikacji.
- Raportowanie: format + cadence + odbiorcy wpisani; heatmapa zdefiniowana.
- Linki do Risk Register i Risk Acceptance Log działają.
- Standardy/regulacje zmapowane; brak sekcji N/A bez uzasadnienia.
- Status, wersja, data, właściciel zaktualizowane w metadanych.

## Kryteria wejścia (DoR)
- Zakres projektu i kluczowe cele zdefiniowane.
- Wstępna lista ryzyk (brainstorm/lessons learned) istnieje.
- Architektura wysokonapięciowych komponentów dostępna (diagramy).
- Wymagania bezpieczeństwa/regulacyjne są znane lub wskazane źródła.
- Dostępne kanały raportowania (dashboard/arkusz/DB) i osoba do utrzymania.
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
