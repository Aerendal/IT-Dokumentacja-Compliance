---
title: Checklista zakupowa
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Checklista zakupowa


## Metadane

- Właściciel: Document Owner
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved



## Cel dokumentu

Ustandaryzować proces zakupu/wytargowania produktu/usługi: wymagania, ocena dostawcy, bezpieczeństwo/prywatność, zgodność prawna, koszt/TCO, umowa (SLA/SoW/DPA) i plan wdrożenia, tak aby minimalizować ryzyka (lock‑in, bezpieczeństwo, zgodność, finansowe) i przyspieszyć decyzję go/conditional/no‑go.


## Zakres i granice

- Obejmuje: wymagania biznesowe/techniczne, kryteria wyboru, due diligence dostawcy (finanse, referencje, support), bezpieczeństwo/prywatność (DPA, certyfikaty, testy), zgodność prawna/licencyjna (licencje, eksport, branżowe normy), koszt/TCO i warunki płatności, przegląd umów (SLA/SoW/DPA, exit/lock‑in), plan wdrożenia i integracji, plan ryzyk/awaryjny.
- Poza zakresem: szczegółowa implementacja techniczna (runbook), negocjacje prawne linia‑po‑linii (prowadzone przez Legal), pełna ocena bezpieczeństwa (oddzielny Security Assessment Report).


## Użytkownicy i interesariusze

- Business/Product, Procurement, Legal, Security/Privacy, FinOps, Architecture/Integration, Operations/Support.


## Wejścia i wyjścia

- Wejścia: wymagania biznesowe/techniczne, kryteria oceny, shortlist dostawców, materiały RFP/RFI, raporty finansowe/referencje, wyniki testów/demo/PoC, polityki bezpieczeństwa/prywatności, wymagania regulatora, cenniki i modele rozliczeń, draft umów (SLA/SoW/DPA/Aneks licencyjny), plan integracji/migracji.
- Wyjścia: wypełniona checklista, ocena punktowa/kwalifikacyjna, lista ryzyk i rekomendacji (go/conditional/no‑go), wymagane poprawki do umowy/DPA/SLA, lista wyjątków z datą przeglądu, plan wdrożenia (owner/ETA), decyzje i ich uzasadnienia.


## Założenia

- Polityki bezpieczeństwa/prywatności i proc. są obowiązujące; zespoły Legal/Security/FinOps dostępne do konsultacji.


## Otwarte pytania

- Czy wymagane są dodatkowe certyfikaty/regulacje (np. branżowe/eksport)?
- Jakie są akceptowalne limity liability i exit notice?


## Powiązania (meta)

- Key Documents: procurement_policy, vendor_risk_assessment, sla_template, sow_template, dpa_template, security_requirements, data_protection_requirements, finops_policy, integration_plan, rollout_plan.
- Key Document Structures: wymagania, due diligence, bezpieczeństwo/prywatność, koszty/TCO, umowy, ryzyka i decyzje.
- Document Dependencies: lista wymagań, shortlist dostawców, dane finansowe/referencje, polityki bezpieczeństwa/prywatności, draft umów, plan integracji.


## Zależności dokumentu

Wymaga: zdefiniowanych wymagań i kryteriów oceny, shortlist dostawców, materiałów ofertowych/draftów umów, polityk bezpieczeństwa/prywatności i zgodności, danych o kosztach/TCO, wstępnego planu integracji. Bez tego DoR pozostaje otwarte.


## Fazy cyklu życia

- Przygotowanie: wymagania, kryteria, shortlist, materiały.
- Ocena: due diligence, bezpieczeństwo/prywatność, zgodność, koszt/TCO.
- Negocjacja: umowy SLA/SoW/DPA, warunki płatności, exit/lock‑in.
- Decyzja: go/conditional/no‑go, wyjątki, plan wdrożenia.
- Follow‑up: wdrożenie, monitoring SLA, przegląd wyjątków.



## Struktura sekcji (szkielet)
- Cel i zakres
- Definicje i role/RACI
- Standardy/zasady i narzędzia
- Kroki procesu / checklisty
- Kryteria jakości/DoD i wyjątki
- Komunikacja i eskalacje
- Rejestr zmian i utrzymanie
## Szybkie powiązania

- linkage_index.jsonl (procurement/checklist)
- procurement_policy, vendor_risk_assessment, sla_template, sow_template, dpa_template, security_requirements, data_protection_requirements, finops_policy, integration_plan, rollout_plan


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

1. Wypełnij wymagania/kryteria i dane ofert; przejdź sekcje oceny i umów.
2. Zapisz ryzyka/wyjątki, decyzje (go/conditional/no‑go) i plan wdrożenia.
3. Utrzymuj dokument w trakcie negocjacji i po decyzji (monitoring SLA, przegląd wyjątków).


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

- SLA, SoW, DPA, TCO, lock‑in, exit clause, overage, egress, liability cap, credits.


## Przykłady użycia

- Zakup SaaS: ocena SOC2/ISO, DPA, lokalizacja danych, model seat vs usage, kary SLA.
- Zakup sprzętu: gwarancja/serwis, zgodność CE/EMC, koszt utrzymania/parts, plan wdrożenia.


## Ryzyka i ograniczenia

- Niejasne kryteria → subiektywna decyzja; brak DPA/SLA → ryzyko prawne/operacyjne; ukryte koszty (egress/overage) → budżet; brak exit → lock‑in.


## Decyzje i uzasadnienia

- [Decyzja] Wybór dostawcy/warunki kluczowe — uzasadnienie wartości/ryzyka/kosztu.
- [Decyzja] Wyjątki akceptowane — uzasadnienie i plan kompensacji.


## Powiązania z innymi dokumentami

- Procurement Policy, Vendor Risk Assessment, SLA/SoW/DPA Templates, Security/Data Protection Requirements, FinOps Policy, Integration Plan, Rollout Plan.


## Powiązania z sekcjami innych dokumentów

- Security Requirements → sekcja bezpieczeństwo; FinOps Policy → TCO; Integration Plan → integracja/operacje; Vendor Risk → ryzyka.


## Słownik pojęć w dokumencie

- SLA, SoW, DPA, TCO, lock‑in, exit clause, overage, egress, liability cap, credits.


## Wymagane odwołania do standardów

- SOC2/ISO 27001/ISO 27701, PCI/HIPAA/branżowe jeśli dotyczy, eksport/ITAR/EAR (jeśli dotyczy), lokalne przepisy ochrony danych.


## Mapa relacji sekcja→sekcja

- Wymagania/kryteria → Ocena dostawcy → Bezpieczeństwo/prywatność → Koszt/TCO → Umowy → Ryzyka/wyjątki → Decyzja → Plan wdrożenia.


## Mapa relacji dokument→dokument

- Checklista zakupowa → Vendor Risk Assessment / Security Assessment / FinOps → SLA/SoW/DPA → Integration/Rollout.


## Ścieżki informacji

- Wymagania → Ocena → Ryzyka/wyjątki → Decyzja → Plan wdrożenia → Monitoring SLA.


## Weryfikacja spójności

- [ ] Kryteria/wagi spójne z oceną; ryzyka mają rekomendacje/owner.
- [ ] Umowy odzwierciedlają wymagania (SLA/DPA/IP/exit); TCO spójne z planem budżetu.
- [ ] Dokument w linkage_index/checklistach.


## Lista kontrolna spójności relacji

- [ ] Każde ryzyko ma mitigację lub świadomą akceptację (owner, data).
- [ ] Każdy wyjątek ma datę przeglądu i plan kompensacji.
- [ ] Decyzja go/conditional/no‑go ma uzasadnienie i powiązanie z ryzykami/kosztem.


## Artefakty powiązane

- RFP/RFI, scoring sheet, raporty testów/PoC, drafty SLA/SoW/DPA, analiza TCO, log decyzji, plan wdrożenia, rejestr wyjątków.


## Ścieżka decyzji

- [Decyzja] → [Uzasadnienie] → [Konsekwencje] → [Właściciel] → [Data].


## Ścieżka akceptacji

- Procurement → Security/Privacy → Legal → FinOps → Business/Owner sign‑off.


## Metryki jakości

- Czas od RFP do decyzji, liczba wyjątków otwartych/zamkniętych, realizacja SLA po wdrożeniu, różnica planowany vs rzeczywisty TCO, częstotliwość przeglądu wyjątków.

## Kryteria ukończenia

- [ ] Checklista kompletna, decyzja podjęta i udokumentowana, plan wdrożenia zapisany.
- [ ] Wersja/data/właściciel aktualne; dokument w linkage_index.


## Powiązania sekcja↔sekcja

- Wymagania/kryteria → Ocena dostawcy → Bezpieczeństwo/prywatność → Zgodność/licencje → Koszt/TCO → Umowy (SLA/SoW/DPA) → Ryzyka/wyjątki → Decyzja → Plan wdrożenia.


## Struktura sekcji

1) Wymagania i kryteria oceny  
2) Dane o dostawcy (finanse, referencje, support/SLA)  
3) Bezpieczeństwo i prywatność (certyfikaty, DPA, testy, SOC2/ISO, lokalizacja danych)  
4) Zgodność prawna/licencyjna (licencje, eksport, normy branżowe)  
5) Koszt i TCO (cennik, rabaty, model rozliczeń, prognoza 3‑letnia, egress/ukryte koszty)  
6) Umowy: SLA/SoW/DPA, IP, lock‑in/exit, odpowiedzialność/ubezpieczenie  
7) Integracja/operacje (API, migracja, dane, utrzymanie, wsparcie)  
8) Ryzyka, wyjątki i decyzje (go/conditional/no‑go)  
9) Plan wdrożenia i monitoringu (owner, ETA, KPI/SLA)  
10) Załączniki (RFP/RFI, raporty testów/PoC, log decyzji)


## Wymagane rozwinięcia

- Kryteria oceny i scoring (wagi biznes/techniczne/bezpieczeństwo/koszt).
- Lista ryzyk z priorytetem i planem mitigacji; wyjątki z datą przeglądu.
- Macierz kosztów/TCO (CAPEX/OPEX, rabaty, egress, overage) i porównanie ofert.
- Kluczowe klauzule umowne (SLA, DPA, IP, exit, liability) z decyzją/komentarzem.


## Wymagane streszczenia

- Podsumowanie punktowe (top 5 czynników), decyzja go/conditional/no‑go, główne ryzyka/wyjątki, koszt/TCO i kluczowe klauzule.


## Guidance (skrót)

- Zaczynaj od jasnych wymagań i wag scoringu; bez tego ocena jest nieporównywalna.
- Zabezpiecz bezpieczeństwo/prywatność (DPA, lokalizacja danych, testy, certyfikaty) i klauzule exit/lock‑in.
- Patrz na TCO, a nie tylko cenę katalogową; uwzględnij egress/overage i koszty migracji/operacji.
- Wymagaj dowodów SLA (historyczne KPI, kary, credits) i planu wsparcia.
- Każdy wyjątek musi mieć właściciela, datę przeglądu i plan kompensacji ryzyka.


## Checklisty Definition of Ready (DoR)

- [ ] Wymagania/kryteria i wagi scoringu zdefiniowane.
- [ ] Shortlist dostawców i materiały (RFP/RFI, drafty umów) zebrane.
- [ ] Polityki bezpieczeństwa/prywatności i wymogi regulatora dostępne.
- [ ] Struktura sekcji wypełniona/N/A.


## Checklisty Definition of Done (DoD)

- [ ] Ocena kompletna (wymagania, bezpieczeństwo/prywatność, zgodność, koszt/TCO, umowy).
- [ ] Ryzyka/wyjątki z owner/ETA; decyzja go/conditional/no‑go z uzasadnieniem.
- [ ] Plan wdrożenia i monitoring SLA/KPI zapisane; dokument w linkage_index.
- [ ] Wersja/data/właściciel zaktualizowane.

