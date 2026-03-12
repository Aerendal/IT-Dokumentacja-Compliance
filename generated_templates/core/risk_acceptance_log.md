---
title: Risk Acceptance Log
status: needs_content
aligned: true
aligned_rev: 6
aligned_at: 2026-02-09
aligned_by: codex
---
# Risk Acceptance Log


## Metadane

- Właściciel: Document Owner
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Rejestrować formalne akceptacje ryzyk wraz z uzasadnieniem, zakresem, datą wygaśnięcia i warunkami cofnięcia. Zapewnia dowody dla audytu/regulatora i spójność z Risk Register oraz planami zmian/releasów.


## Zakres i granice

- Obejmuje: akceptacje ryzyk czerwonych/żółtych, tymczasowe wyjątki (security/compliance/availability/budget), rozszerzenie na ryzyka vendor/TPRM. Zawiera warunki, odpowiedzialność i przeglądy.
- Poza zakresem: definicja metodyki scoringu (Risk Management Plan), wybór mitygacji (Risk Mitigation Plan), bieżący status mitygacji (Risk Mitigation Status).


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia
- Wejścia: cele projektu, WBS/harmonogram, architektura, wymagania (FRS/NFR), polityki korporacyjne, lekcje z postmortemów.
- Wyjścia: zasady oceny i akceptacji ryzyk, cykl przeglądów, szablon raportowania, powiązania z planem testów, zmian i releasów.
## Założenia
- Zespoły używają jednego narzędzia do rejestru ryzyk (np. tracker w DB lub arkusz powiązany).
- Wszystkie mitygacje mają testy regresji bezpieczeństwa lub scenariusze UAT odzwierciedlające ryzyko.
## Otwarte pytania
- Czy dla tego projektu potrzebna jest ocena TPRM (Third‑Party Risk Management) dla nowych vendorów?
- Czy heatmapa ma być publikowana w raportach dla regulatora (jeśli tak, w jakim formacie)?
## Powiązania (meta)
- Wymaga odniesienia do: Key Documents
- Wymaga odniesienia do: Key Document Structures
- Wymaga odniesienia do: Document Dependencies
- Wymaga odniesienia do: RACI i role
- Wymaga odniesienia do: Standardy i compliance
## Zależności dokumentu
- Konsumuje: Project Charter, Risk Assessment, Postmortem learnings, Security/Compliance wymagania.
- Dostarcza do: Risk Register, Harmonogram (bufory), Test Strategy/Plans, Change/Release plans, Communication plan.
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
## Struktura sekcji (szkielet)

- Zasady akceptacji: progi, kto zatwierdza (Steering/Exec/Sponsor), wymagane dowody przed akceptacją.
- Tabela akceptacji (propozycja kolumn):
  - Risk ID/tytuł, Kategoria, RAG, Trend.
  - Właściciel ryzyka, Właściciel akceptacji, Backup.
  - Uzasadnienie akceptacji, Kompensujące kontrole (compensating controls).
  - Data decyzji, Data wygaśnięcia (sunset), Termin przeglądu.
  - Warunki cofnięcia akceptacji (triggery), Plan wyjścia (exit plan).
  - Dowody/artefakty: minutes, ticket, raport testu, SLA/vendor.
  - Powiązania: Risk Register, Risk Mitigation Plan/Status, Change/Release, Test Strategy, TPRM.
- Proces przeglądu: cadence (np. czerwone co 30 dni, żółte co 60 dni), kryteria przedłużenia lub zakończenia akceptacji.
- Raportowanie i audyt: format executive (Top accepted), log zmian (kto/kiedy/co), przechowywanie dowodów.


## Szybkie powiązania
- risk-tracking
- risk-report
- risk-register
- risk-assessment
- experiments-log

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
1. Zdefiniuj kryteria (funkcjonalne + NFR) wraz z danymi i dowodami.  
2. W trakcie testów odhaczaj spełnienie; zbieraj dowody.  
3. Przed release wypełnij snapshot, podejmij decyzję go/no‑go, zaktualizuj DoD.
## Checklisty jakości

- [ ] Każda akceptacja ma uzasadnienie, datę wygaśnięcia i warunki cofnięcia.
- [ ] Kompensujące kontrole są wskazane i działają (dowody).
- [ ] Powiązania do Risk Register i Change/Release/Test są uzupełnione.
- [ ] Przeglądy zaplanowane (daty) i właściciel przeglądu wskazany.
- [ ] Log zmian (kto/kiedy/co) jest prowadzony; metadane aktualne.


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

## Wymagane rozwinięcia

- Progi i tolerancje → Risk Management Plan.
- Kontrole zastępcze → Security/Compliance Requirements, Cloud Security Baseline.
- Warunki go/no-go → Change/Release Plan.
- Wymagane testy → Test Strategy / Security Testing Plan.


## Wymagane streszczenia

- Streszczenie „Top accepted risks” (tytuł, RAG, sunset, warunki cofnięcia, właściciel).
- Streszczenie akceptacji vendor/TPRM dla Legal/Privacy/Compliance.


## Kryteria ukończenia (DoD)

- Tabela akceptacji uzupełniona lub sekcje N/A z uzasadnieniem.
- Daty wygaśnięcia i przeglądów wpisane; właściciele i kompensacje wskazane.
- Linki do Risk Register, Risk Mitigation Plan/Status, Change/Release, Test Evidence działają.
- Raportowanie/eksport do dashboardu ustalone.


## Kryteria wejścia (DoR)

- Risk Register zawiera ocenę i właścicieli.
- Progi akceptacji (z Risk Management Plan) są uzgodnione.
- Dostępne narzędzie/DB do przechowywania logu oraz repo dowodów.
