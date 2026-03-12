---
title: Vendor Risk Assessment
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# Vendor Risk Assessment

## Metadane
- Właściciel: Document Owner
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


> Powiązania: linkage_index.jsonl

## Cel dokumentu
Ocenić ryzyka związane z dostawcą (vendor/partner/SaaS) przed wyborem, w trakcie współpracy i cyklicznie, uwzględniając bezpieczeństwo, ciągłość usług, zgodność (SOC2/ISO 27001/PCI/HIPAA), ochronę danych i lock‑in. Wyniki zasilają TPRM, umowy (SLA/OLA), plan mitygacji i akceptacje.

## Zakres i granice
- Obejmuje: oceny due diligence, przedłużenia/renewal, zmiany zakresu usług, incydenty vendorów, integracje z naszym systemem (dane/identity/network), plan exit/BCP/DR dostawcy, kontrole bezpieczeństwa i prywatności, raporty zgodności, wyniki testów/scanów.
- Poza zakresem: ocena wewnętrznych projektów (inna ścieżka), szczegółowe mitygacje po stronie naszej organizacji (w Risk Mitigation Plan).

## Wejścia i wyjścia
- Wejścia: zapytanie ofertowe/SoW, architektura integracji, klasyfikacja danych, wyniki TPRM questionnaire, SOC2/ISO 27001 raporty, PCI AoC (jeśli płatności), DPIA (jeśli dane osobowe), wyniki pen‑testów/scanów, SLA/OLA draft.
- Wyjścia: ocena RAG z uzasadnieniem, lista ryzyk vendorowych (Security/Privacy/Availability/Compliance/Operational/Financial/Lock‑in), wymagane mitygacje/kompensacje, rekomendacja (go/conditional/no‑go), aktualizacje do SLA/OLA/DPA, wejścia do Risk Register/Acceptance/TPRM planu.

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
- Profil dostawcy: usługa, lokalizacje danych, poddostawcy, certyfikaty (SOC2/ISO 27001/PCI/HIPAA), rejestry (Cloud/Marketplace).
- Klasyfikacja danych i dostępów: typy danych, PII/PHI/PCI, integracje IAM (SSO/MFA/SCIM/JIT), sieć (peering/VPN/private link).
- Ryzyka i kontrole (propozycja tabeli):
  - Domeny: Security (IAM, szyfrowanie, klucze), Privacy (DPA, DPIA, transfery), Availability/DR/BCP (RTO/RPO, DR testy), Compliance (SOC2/ISO/PCI/HIPAA/21 CFR 11), Operational (proces zmian, incident handling), Financial/Lock‑in (exit, escrow, portability), Vendor management (SLA, wskaźniki, kary).
  - Kolumny: Ryzyko, P/I/RAG, Dowody (raporty, testy), Braki, Wymagane mitygacje/kompensacje, Właściciel, Termin, Status.
- Wyniki due diligence: podsumowanie ryzyk czerwonych/żółtych, wymagane warunki umowy, rekomendacja.
- Plan monitoringu: cadence przeglądów (np. roczny audyt SOC2, kwartalne SLA), sygnały wczesne (SLO breach, incidenty), wymagania raportowe.
- Exit/continuity: plan wyjścia (dane, klucze, formaty, okres notice), testy DR/backup, procedury przeniesienia.

## Wymagane rozwinięcia
- Standardy i raporty: SOC 2, ISO 27001/27701, PCI DSS, HIPAA, 21 CFR Part 11 (jeśli dotyczy), CSA STAR, raporty audytu.
- DPA/Privacy: DPIA, SCC/IDTA (transfery), ROPA.
- Kontrole kryptograficzne: KMS/HSM, rotacja, BYOK/Externally Managed Keys.
- DR/BCP: testy dostawcy, RTO/RPO, geo-redundancja.
- TPRM: Vendor Management Plan, SLA/OLA, eskalacje.

## Wymagane streszczenia
- Streszczenie top ryzyk i warunków kontraktowych (SLA, kary, exit, dane, compliance).
- Streszczenie ryzyk czerwonych/żółtych z wymaganymi mitygacjami przed „go”.

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
- [ ] Klasyfikacja danych i dostępów (SSO/MFA/SCIM) opisana.
- [ ] Raporty zgodności (SOC2/ISO/PCI/HIPAA) zebrane; braki/wyłączenia wskazane.
- [ ] Ryzyka czerwone/żółte mają mitygacje/kompensacje i właścicieli.
- [ ] Warunki kontraktowe (SLA/OLA, kary, exit, notice, RTO/RPO) zapisane.
- [ ] Plan monitoringu i cadence przeglądów (SLA, audyty) zdefiniowane.
- [ ] Exit/continuity opisane (dane, klucze, formaty, DR testy).
- [ ] Powiązania z TPRM, Risk Register, Acceptance, Change/Release wskazane; sekcje N/A uzasadnione.
- [ ] Kryteria DoR/DoD poniżej spełnione; metadane aktualne.

## Definicje robocze
- TPRM — Third‑Party Risk Management; proces oceny i monitorowania dostawców.
- Compensating Control — kontrola zastępcza, gdy vendor ma lukę.
- Exit Plan — procedura opuszczenia dostawcy (dane, klucze, okres notice).

## Przykłady użycia
- SaaS CRM: ocena SOC2/ISO 27001, DPA/SCC, RTO/RPO, testy DR, SSO/MFA, DLP, exit i portability.
- Dostawca płatności: PCI AoC, tokenizacja, segregacja danych, klucze/BYOK, kary SLA, plan awaryjny i dual vendor.

## Ryzyka i ograniczenia
- Brak dowodów (SOC2/ISO/pen‑test) → wymagaj przed „go” lub zastosuj kontrolę zastępczą.
- Lock‑in (brak exit/portability) → negocjuj formaty, notice, escrow, dual vendor.
- Niepełna kontrola nad danymi/kluczami → BYOK/HSM, szyfrowanie end‑to‑end, logging/audyt dostępu.

## Decyzje i uzasadnienia
- Wymóg SSO/MFA/SCIM dla dostawców z dostępem do danych wrażliwych — redukcja ryzyk IAM.
- Wymóg exit planu i testów DR — redukcja ryzyk dostępności/lock‑in.

## Założenia
- Dostawca udostępnia raporty i współpracuje w testach (pen‑test/DR).
- Mamy zasoby do przeglądów SLA/audytów i do wdrożenia kontroli kompensujących.

## Otwarte pytania
- Jaka jest częstotliwość odświeżania dowodów (SOC2/ISO/pen‑test) — roczna/po większej zmianie?
- Czy wymagamy BYOK/Externally Managed Keys dla tego dostawcy?

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
- SOC 2, ISO 27001/27701, PCI DSS, HIPAA, 21 CFR Part 11 (jeśli dotyczy), CSA STAR.
- NIST SP 800‑171 / 800‑53 jeśli dane rządowe/contractor.

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
- Profil dostawcy, klasyfikacja danych/dostępów uzupełnione.
- Tabela ryzyk/controli wypełniona (RAG, dowody, mitygacje, właściciele, terminy).
- Warunki kontraktowe (SLA/OLA, exit, kary) i plan monitoringu/DR opisane.
- Powiązania do TPRM, Risk Register, Acceptance, Change/Release wskazane.
- Metadane aktualne; sekcje N/A uzasadnione.

## Kryteria wejścia (DoR)
- Dostępne materiały vendor (SOC2/ISO/PCI/HIPAA, pen‑test, architektura, DPA/SLA draft).
- Znana klasyfikacja danych i zakres integracji (IAM/sieć/dane).
- Uzgodnione progi RAG/appetite i wymagania compliance.

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
