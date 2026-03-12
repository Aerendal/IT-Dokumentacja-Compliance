---
title: Legal Risk Assessment
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# Legal Risk Assessment

## Metadane
- Właściciel: Document Owner
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


> Powiązania: linkage_index.jsonl

## Cel dokumentu
Zidentyfikować i ocenić ryzyka prawne/regulacyjne związane z systemem/produktem/projektem (umowy, dane, własność intelektualna, regulacje sektorowe), zaproponować mitygacje/akceptacje i warunki go/conditional/no‑go. Dostarczyć dowody zgodności dla audytu/regulatora i zasilić Risk Register/Mitigation/Acceptance.

## Zakres i granice
- Obejmuje: ryzyka kontraktowe (SLA, kary, odpowiedzialność, IP/licencje), dane i prywatność (DPA/GDPR/RODO, HIPAA/PHI, transfery), branżowe (PCI DSS, 21 CFR 11, SOX, sektorowe), licencje OSS/komercyjne, AI/ML (data rights, bias), prawo pracy (jeśli relewantne), TPRM (poddostawcy), warunki exit.
- Poza zakresem: szczegółowe postanowienia umowne (w kontrakcie), testy techniczne (w planach testów).

## Wejścia i wyjścia
- Wejścia: drafty umów (SLA/OLA/DPA/MSA/SoW), klasyfikacja danych, mapy przepływów i lokalizacji danych, licencje/OSS BOM, wyniki TPRM, regulacje branżowe, polityka prywatności, DPIA/ROPA (jeśli istnieją), rejestr AI (jeśli dotyczy).
- Wyjścia: tabela ryzyk prawnych (RAG, uzasadnienie), wymagane mitygacje/warunki kontraktowe, decyzje (go/conditional/no‑go), lista akceptacji z sunset, aktualizacje do Risk Register/Mitigation/Acceptance i do kontraktów (SLA/DPA/warunki IP/exit).

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
- Zakres i kontekst prawny: jurysdykcje, kategorie danych, sektor/regulacje, poddostawcy.
- Tabela ryzyk prawnych:
  - Domeny: kontraktowe (SLA/kary/odpowiedzialność/ubezpieczenia), dane/prywatność (RODO/GDPR/SCC/IDTA, PHI/HIPAA), compliance sektorowe (PCI/21 CFR 11/SOX/fin/health), IP/licencje/OSS, AI/ML (data rights/bias/wyjaśnialność), employment (jeśli relewantne), lokalizacja/transfery danych, TPRM/poddostawcy, exit/portability.
  - Kolumny: Ryzyko, Kategoria, P/I/RAG, Źródło (umowa/regulacja/audyt), Uzasadnienie, Wymagane mitygacje/klauzule, Właściciel, Termin, Status, Dowody (raport, klauzula, test).
- Wymagane mitygacje/klauzule: przykłady zapisów (SLA/kary, DPA/SCC, IP/indemnity, escrow, exit plan, audit rights, security schedule).
- Akceptacje: które ryzyka mogą być zaakceptowane, sunset/warunki cofnięcia, kompensacje.
- Warunki go/conditional/no‑go: zależne od podpisania kluczowych klauzul, dostarczenia raportów, spełnienia wymogów transferowych/testów.
- Monitoring i przeglądy: cadence na odświeżanie dowodów (SOC2, PCI AoC, DPIA, SCC), audyt klauzul przy zmianach zakresu/jurysdykcji.

## Wymagane rozwinięcia
- Regulacje/dane: GDPR/RODO, HIPAA, 21 CFR Part 11, LGPD (jeśli), CCPA/CPRA, PCI DSS.
- Kontraktowe/IP: MSA/SLA/DPA/SOW, licencje OSS, indemnity, escrow, ubezpieczenia.
- Transfery: SCC/IDTA/TIA, lokalizacja danych, chmura (by design).
- AI/ML: wytyczne AI Act/ISO/IEEE, data provenance, bias, explainability.

## Wymagane streszczenia
- Streszczenie top ryzyk prawnych (RAG, klauzule/mitygacje wymagane, właściciel).
- Streszczenie ryzyk wymagających akceptacji (sunset, warunki, kompensacje).
- Streszczenie warunków go/conditional/no‑go kontraktowych/transferowych.

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
- [ ] Jurysdykcje, kategorie danych, poddostawcy opisane.
- [ ] Ryzyka mają kategorie prawne, P/I/RAG, właścicieli, mitygacje/klauzule.
- [ ] Klauzule krytyczne (SLA/kary, DPA/SCC, IP/indemnity, audit rights, exit) opisane lub oznaczone jako blocker.
- [ ] Akceptacje mają sunset/warunki i kompensacje; link do Acceptance Log.
- [ ] Warunki go/conditional/no‑go i wymagane dowody wskazane.
- [ ] Cadence przeglądów dowodów/regulacji zapisane.
- [ ] Powiązania do Register/Mitigation/Acceptance/TPRM/Change/Release/Test wskazane; sekcje N/A uzasadnione.
- [ ] Kryteria DoR/DoD poniżej spełnione; metadane aktualne.

## Definicje robocze
- DPA — umowa powierzenia danych osobowych; reguluje role, środki techniczne, poddostawców.
- SCC/IDTA — standardowe klauzule transferowe / UK IDTA dla transferów poza EOG/UK.
- Indemnity — klauzula zwolnienia z odpowiedzialności (np. za naruszenie IP).

## Przykłady użycia
- SaaS w UE/US: ocena DPA, SCC/IDTA, SOC2, PCI (jeśli płatności), klauzule audit/exit, poddostawcy, lokalizacja danych.
- Produkt medyczny: HIPAA/PHI, 21 CFR 11, GxP, DPA/SCC, kary SLA, escrow, testy walidacyjne jako dowody.

## Ryzyka i ograniczenia
- Brak klauzul transferowych/danych → blocker go/no‑go.
- Brak audit rights / brak raportów SOC2/PCI → wymagaj lub kompensuj (kontrole własne).
- Licencje OSS niezweryfikowane → ryzyko naruszenia IP; potrzebny SBOM i review licencji.

## Decyzje i uzasadnienia
- Wymóg SCC/IDTA + TIA przy transferach poza EOG/UK — zgodność z RODO.
- Wymóg audit rights i raportów SOC2/PCI — dowody dla audytu/regulatora.

## Założenia
- Dostępne są drafty umów, dane o lokalizacji i poddostawcach.
- Legal/Privacy/Compliance współpracują przy ocenie.

## Otwarte pytania
- Czy wymagane jest DPIA/ROPA dla zakresu danych?
- Jak często odnawiać audyty/raporty vendorów (SOC2/PCI)?

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
- GDPR/RODO, HIPAA, 21 CFR Part 11, CCPA/CPRA (jeśli dotyczy).
- PCI DSS (gdy płatności), SOC 2, ISO 27001/27701.
- AI Act/ISO/IEEE (jeśli AI/ML), OSS licencje (MIT/Apache/GPL), prawo autorskie/patentowe.

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
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Ścieżka akceptacji
- [Kto zatwierdza] → [kryteria akceptacji] → [status]
- [Kto zatwierdza] → [kryteria akceptacji] → [status]

## Kryteria ukończenia (DoD)
- Tabela ryzyk prawnych wypełniona (kategorie, P/I/RAG, mitygacje/klauzule, właściciele, terminy).
- Warunki go/conditional/no‑go i akceptacje opisane; linki do Register/Mitigation/Acceptance/TPRM/Change/Release/Test działają.
- Dowody/regulacje/raporty wymagane wyspecyfikowane; cadence przeglądów podane.
- Metadane aktualne; sekcje N/A uzasadnione.

## Kryteria wejścia (DoR)
- Dostępne drafty umów (SLA/DPA/MSA/SoW), klasyfikacja danych, mapy lokalizacji/transferów, lista poddostawców.
- Uzgodnione progi RAG i appetite prawne; zespół Legal/Privacy/Compliance dostępny.

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
