---
title: Risk Report
status: needs_content
aligned: true
aligned_rev: 2
aligned_at: 2026-02-09
aligned_by: codex
---

# Risk Report

## Metadane
- Właściciel: Document Owner
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


> Powiązania: linkage_index.jsonl

## Cel dokumentu
Przedstawić skondensowany raport ryzyk (RAG, trend, top 10, status mitygacji, akceptacje, decyzje) dla interesariuszy projektu/produktu. Ma wspierać decyzje „go/conditional/no‑go”, priorytetyzację mitygacji i komunikację z zarządem/audytorem.

## Zakres i granice
- Obejmuje: ryzyka z Risk Register (top/czerwone/żółte), status mitygacji, akceptacje z sunset, powiązania z releasami/zmianami/testami, decyzje/eskalacje.
- Poza zakresem: szczegółowe wpisy i pełne tabele rejestru (są w systemie źródłowym).

## Wejścia i wyjścia
- Wejścia: Risk Register, Risk Mitigation Plan/Status, Risk Acceptance Log, Incident/Postmortem, Change/Release status, Test/QA raporty.
- Wyjścia: raport (deck/CSV/DB snapshot), lista decyzji/eskalacji, sygnały do Release/Change gating, aktualizacja Risk & Issue Report.

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
- Executive summary: # ryzyk czerwonych/żółtych, trend, top 5, wygasające akceptacje, decyzje do podjęcia.
- Tabela top ryzyk: ID, tytuł, kategoria, RAG, trend, owner, status mitygacji, ETA, dowody, akceptacja (sunset), link do źródła.
- Akceptacje i wyjątki: lista z datą wygaśnięcia/warunkami, kompensacje, właściciel.
- Decyzje i eskalacje: wymagane decyzje (go/conditional/no‑go), właściciel, termin, konsekwencje.
- Powiązania z releasami/zmianami/testami: blokery, warunki odblokowania.
- Załączniki/odniesienia: linki do Risk Register, Mitigation, Acceptance, Incident/Postmortem, Test/QA.

## Wymagane rozwinięcia
- RAG/metodyka → Risk Management Plan.
- Dane źródłowe → Risk Register/Mitigation/Acceptance, Incident/Postmortem.
- Gating → Release/Change Plan.

## Wymagane streszczenia
- Streszczenie top 10 ryzyk (RAG, ETA, owner).
- Streszczenie akceptacji wygasających 30/60 dni.
- Streszczenie decyzji/eskalacji z terminami.

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
- [ ] Top ryzyka mają RAG/trend, ownerów, status mitygacji i dowody/ETA.
- [ ] Akceptacje mają sunset/warunki i kompensacje; wyróżnione wygasające.
- [ ] Decyzje/eskalacje mają właścicieli i terminy; konsekwencje opisane.
- [ ] Powiązania do źródeł (register/mitigation/acceptance/incident/test/release) są wskazane.
- [ ] Raport ma ustaloną cadence/format/odbiorców; metadane aktualne; sekcje N/A uzasadnione.

## Definicje robocze
- RAG — Red/Amber/Green.
- Sunset — data wygaśnięcia akceptacji/wyjątku.
- Conditional Go — dopuszczenie release pod warunkiem spełnienia mitygacji/dowodów.

## Przykłady użycia
- Tygodniowy raport programu chmurowego: top ryzyka danych/IAM/sieć, wygasające akceptacje, blokery release.
- Miesięczny raport dla zarządu: trend RAG, decyzje inwestycyjne/zasobowe, akceptacje do odnowienia.

## Ryzyka i ograniczenia
- Rozjazd z danymi źródłowymi → wskazać source of truth i timestamp snapshotu.
- Brak dowodów → wymagaj linków do testów/scanów/runbooków.

## Decyzje i uzasadnienia
- Użycie skrótu top 10 + wygasające akceptacje — fokus na decyzje i zgodność.
- Uwzględnianie conditional go — pozwala na kontrolowany postęp z ryzykiem.

## Założenia
- Dane w Risk Register/Mitigation/Acceptance są aktualne.
- Odbiorcy znają metodykę RAG z Risk Management Plan.

## Otwarte pytania
- Jaka cadence raportu (tyg./mies.) dla tego projektu/programu?
- Czy raport obejmuje vendorów i ryzyka TPRM, czy są w osobnym raporcie?

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
- ISO 31000 / ISO 27005 — raportowanie ryzyk.
- SOC 2 / ISO 27001 / PCI DSS — dowody istnienia raportów ryzyka i akceptacji.

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
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Ścieżka akceptacji
- [Kto zatwierdza] → [kryteria akceptacji] → [status]
- [Kto zatwierdza] → [kryteria akceptacji] → [status]

## Kryteria ukończenia (DoD)
- Top ryzyka, akceptacje, decyzje/eskalacje uzupełnione; linki do źródeł działają.
- Cadence/format/odbiorcy zapisane; snapshot datowany.
- Metadane aktualne; sekcje N/A uzasadnione.

## Kryteria wejścia (DoR)
- Aktualny Risk Register/Mitigation/Acceptance, Incident/Postmortem i Release status dostępne.
- Uzgodnione KPI/KRI i progi z właścicielami/Steering.

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
