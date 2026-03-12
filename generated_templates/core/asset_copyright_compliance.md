---
title: Asset Copyright Compliance
status: needs_content
aligned: true
aligned_rev: 2
aligned_at: 2026-02-09
aligned_by: codex
---

# Asset Copyright Compliance

## Metadane
- Właściciel: Document Owner
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


> Powiązania: linkage_index.jsonl

## Cel dokumentu
Zapewnić, że wszystkie użyte zasoby (grafika, audio, wideo, fonty, kod, modele 3D/AI/stock) są legalnie licencjonowane, właściwie atrybuowane, zgodne z umowami/OSS i że istnieją dowody zakupu/zgód. Minimalizuje ryzyko roszczeń IP, DMCA, wycofań aplikacji i kar umownych.

## Zakres i granice
- Obejmuje: zasoby własne, stock, OSS, licencje komercyjne, fonty, modele AI/3D, dźwięki, wideo, teksty; dowody zakupu/umów; ograniczenia pól eksploatacji; atrybucje; whitelist/blacklist; kontrolę zmian i audyt.
- Poza zakresem: szczegółowe procesy zakupu (procurement) i budżet (linki), implementacja systemów DRM (referencja).

## Wejścia i wyjścia
- Wejścia: lista zasobów (typ, źródło, właściciel), licencje/umowy/ToS stock/OSS, dowody zakupu, informacje o polach eksploatacji, wymagania klientów/umów, rejestry użycia w projektach/buildach.
- Wyjścia: rejestr zgodności (asset → licencja/umowa/dowód/atrybucja/ograniczenia), checklisty release, raport ryzyk IP, plan remediacji (zamiana/usunięcie), instrukcje atrybucji, whitelist/blacklist.

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
- Inwentaryzacja: spis zasobów (typ, źródło, licencja, właściciel, data, projekt).
- Licencje/umowy: typ licencji (komercyjna, royalty-free, OSS), pola eksploatacji, ograniczenia (no-resale, seat, domain, app count), terminy, sublicencje.
- OSS: licencje (MIT/Apache/GPL/CC), obowiązki (NOTICE, disclosure, copyleft), transitive deps, trzeci-party notices.
- Atrybucje: wymogi tekstowe/graficzne/credits, lokalizacja w produkcie.
- Dowody i przechowywanie: faktury, zrzuty ToS, dowód zakupu, hash pliku, ścieżka w repo, kontrola dostępu.
- AI/stock/3D: prawa do datasetów/promptów/modeli, ograniczenia komercyjne, zakazy generowania logo/twarzy/real persons, usage caps.
- Kontrola zmian i audyt: kto może dodać asset, workflow review, wersjonowanie, log zmian, period review.
- Ryzyka i remediacja: identyfikacja braków, plan usunięcia/podmiany/licencji, DMCA response.
- Checklista release: potwierdzenie licencji/atrybucji/dowodów dla releasu/buildu.

## Wymagane rozwinięcia
- OSS compliance → Third-Party Notices, OSS policy, legal review.
- Stock/AI → ToS dostawców, ograniczenia komercyjne, dataset/usage.
- Atrybucje → Design System/Content Guidelines.
- Dowody → Storage/Retention policy, Access control.

## Wymagane streszczenia
- Streszczenie braków licencyjnych i ich ryzyka/planów naprawy.
- Streszczenie wymogów atrybucji dla releasu.

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
- **COBIT 2019** — Kontrola nad Informacją i Technologiami (ISACA)
- **ISO/IEC 38500** — Ład Informatyczny Organizacji
- **TOGAF ADM** — Framework Architektury Korporacyjnej (The Open Group)

> Sekcja generowana automatycznie. Zweryfikuj trafność i uzupełnij o dodatkowe normy/regulacje specyficzne dla kontekstu projektu.
## Jak używać dokumentu
- Przeczytaj sekcje "Cel dokumentu" i "Zakres i granice" i upewnij się, że opisują Twój przypadek.
- Wypełniaj kolejne sekcje zgodnie z guidance i powiązaniami; korzystaj z kryteriów DoR/DoD w `reports/checklist_atomic.jsonl`.
- Aktualizuj statusy w checklistach (structure/clarity/links, DoR/DoD), gdy sekcje są gotowe lub oznaczone jako N/A.


## Checklisty jakości (DoR/DoD skrót)
- DoR:
  - [ ] Lista assetów i źródeł dostępna; zebrane licencje/umowy/ToS.
  - [ ] Ustalony właściciel procesu i repo dowodów; narzędzia do inwentaryzacji.
- DoD:
  - [ ] Każdy asset ma licencję/umowę, dowód, ograniczenia i (jeśli wymagane) atrybucję.
  - [ ] OSS ma spełnione obowiązki (NOTICE/disclosure), atrybucje i decyzje copyleft.
  - [ ] Stock/AI/3D mają potwierdzone pola eksploatacji i ograniczenia.
  - [ ] Checklista release wypełniona; ryzyka/plan remediacji opisane; dokument wersjonowany.

## Definicje robocze
- Jurysdykcja, Waiver, DSR, AOC, Accessibility (WCAG), Regulatory reporting.
## Przykłady użycia
- Nowy rynek UE: RODO/DSR, lokalizacja danych, accessibility, AOC dostawców.
- Produkt finansowy: PCI DSS + raporty regulacyjne, SoD, logi/audyt.
## Ryzyka i ograniczenia
- Niepełne mapowanie → kary; waivery bez dat → trwałe ryzyko; brak dowodów → audyt niezaliczony.
## Decyzje i uzasadnienia
- [Decyzja 1 — uzasadnienie]
- [Decyzja 2 — uzasadnienie]

## Założenia
- Legal/Compliance zapewnia interpretację; dane/flow są aktualne; istnieją polityki security/privacy.
## Otwarte pytania
- Jakie raporty regulacyjne (format/SLA/kanał) są wymagane? 
- Czy istnieją dodatkowe wymogi sektorowe (fin/health/public/ot)?
## Powiązania z innymi dokumentami
- Privacy Policy, Data Classification, Key Management, Audit Logging, TPRM, Accessibility Standards, Security Baseline, Incident Response, DRP/BCP, Regulatory Reporting.
## Powiązania z sekcjami innych dokumentów
- Privacy → DSR/retencja; Security → IAM/crypto/logi; TPRM → umowy.
## Słownik pojęć w dokumencie
- Jurysdykcja, Waiver, DSR, AOC, Accessibility, Regulatory reporting.
## Wymagane odwołania do standardów
- RODO/CCPA, PCI, HIPAA/sector, DORA/NIS2 jeśli dotyczy, WCAG.
## Mapa relacji sekcja→sekcja
- Regulacje → Wymagania → Kontrolki → Luki/Waivery → Plan/Monitoring.
## Mapa relacji dokument→dokument
- Legal Requirements → Privacy/Security/Accessibility/TPRM → Audit/Reporting.
## Ścieżki informacji
- Regulacje → Wymagania/Kontrolki → Dowody → Raporty → Monitorowanie zmian.
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
- Rejestr regulacji, mapping wymaganie→kontrolka→dowód, waivery, raporty.
## Ścieżka decyzji
- [Decyzja] → [Uzasadnienie] → [Konsekwencje]
- [Decyzja] → [Uzasadnienie] → [Konsekwencje]

## Użytkownicy i interesariusze
- Legal/Compliance, Security/Privacy, Product/Engineering, Audit, TPRM/Vendor Mgmt.
## Ścieżka akceptacji
- Legal/Compliance → Security/Privacy → Product/Engineering → Audit/Owner sign‑off.
## Kryteria ukończenia
- [ ] Wymagania, kontrolki, luki/waivery opisane; plan monitoringu zmian istnieje.
- [ ] Dokument w linkage_index/checklistach; wersja/data/właściciel aktualne.
## Metryki jakości
- Liczba/istotność luk, terminowość SLA/dowodów, liczba/ważność waiver, wynik audytów, czas reakcji na zmiany regulacyjne.
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
