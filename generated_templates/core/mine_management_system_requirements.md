---
title: Mine Management System Requirements
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Mine Management System Requirements


## Metadane

- Właściciel: Product Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Definiuje wymagania biznesowe i techniczne dla systemu zarządzania kopalnią (podziemną/odkrywkową): produkcja, bezpieczeństwo, środowisko, sprzęt, łączność, raportowanie i zgodność regulacyjna. Ma zapewnić kompletność, bezpieczeństwo oraz możliwość audytu.


## Zakres i granice

- Obejmuje: wydobycie/produktywność, planowanie i dyspozycję (dispatch), tracking floty, czujniki IoT/OT, bezpieczeństwo pracowników (tagi, SOS, gaz), geotechnika i stabilność, środowisko (emisje, hałas, woda), łączność (LTE/5G/WiFi/mesh), integracje SCADA/ERP/MES, analityka/raporty, bezpieczeństwo/cyber dla OT/IT, ciągłość działania.
- Poza zakresem: szczegółowe projekty sieci i SCADA (oddzielne dokumenty), szczegółowe procedury bezpieczeństwa pracy (w playbookach HSE).


## Użytkownicy i interesariusze

- Operations, HSE, OT/IT, Security, Maintenance, Finance/Compliance, Regulator.


## Wejścia i wyjścia

- Wejścia: cele produkcyjne, KPI/HSE, wymagania prawne (górnictwo/środowisko), inwentarz sprzętu i czujników, mapy geologiczne, profile łączności, polityki bezpieczeństwa/OT, wymagania raportowe regulatora, integracje ERP/MES/SCADA, SLA/hałas/pył.
- Wyjścia: katalog wymagań funkcjonalnych/niefunkcjonalnych, priorytety i krytyczność, integracje i interfejsy, wymagania bezpieczeństwa/cyber/BCP, metryki i raporty, kryteria akceptacji.


## Założenia

- Dostępne są dane geologiczne/strefy i źródła zasilania/UPS.
- Zespół OT/Security jest zaangażowany; polityki patchingu/antymalware istnieją.


## Otwarte pytania

- Czy wymagane jest lokalne przetwarzanie edge dla bezpieczeństwa przy utracie łączności?
- Jakie są wymagane częstotliwości raportów do regulatorów?


## Powiązania (meta)

- Key Documents: hse_policy, ot_security_baseline, connectivity_plan_mine, fleet_management, environmental_compliance, bcp_drp.
- Key Document Structures: funkcjonalne, niefunkcjonalne, bezpieczeństwo, integracje, raporty.
- Document Dependencies: SCADA/PLC, sieć łączności, IoT czujniki, ERP/MES, identity/access, monitoring/observability.


## Zależności dokumentu

Wymaga listy procesów górniczych, systemów OT/IT, wymagań prawnych (HSE/środowisko), dostępności łączności, danych geologicznych, polityk bezpieczeństwa i BCP/DRP. Bez tych danych DoR otwarte.


## Fazy cyklu życia

- Analiza: cele produkcyjne/HSE, regulacje, mapy procesów.
- Projekt: wymagania, interfejsy, bezpieczeństwo, BCP/DR, łączność.
- Implementacja: konfiguracja systemu, integracje, testy.
- Testy/odbiór: funkcjonalne, HSE, wydajność, łączność awaryjna.
- Operacje: monitoring, raporty, utrzymanie, aktualizacje.
- Postmortem: incydenty HSE/IT/OT, lekcje i poprawki.



## Struktura sekcji (szkielet)
- Cel i kontekst biznesowy
- Interesariusze, persony i scenariusze
- Wymagania funkcjonalne (priorytety, reguły, wyjątki)
- Wymagania niefunkcjonalne (wydajność, dostępność, bezpieczeństwo, zgodność)
- Dane i integracje
- Kryteria akceptacji i miary sukcesu
- Zależności, ryzyka i założenia
- Śledzenie (traceability) do epik/testów
## Szybkie powiązania

- linkage_index.jsonl (mining/ops/system_requirements)
- hse_policy, ot_security_baseline, connectivity_plan_mine, environmental_compliance, bcp_drp


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **IEEE 830** — Zalecana Praktyka dla Specyfikacji Wymagań Oprogramowania (SRS)
- **ISO 9001** — System Zarządzania Jakością (QMS)
- **ISO/IEC 12207** — Procesy Cyklu Życia Oprogramowania

> Sekcja generowana automatycznie. Zweryfikuj trafność i uzupełnij o dodatkowe normy/regulacje specyficzne dla kontekstu projektu.

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

1. Uzupełnij procesy/KPI, role i regulacje.
2. Opisz wymagania funkcjonalne/niefunkcjonalne i integracje.
3. Dodaj bezpieczeństwo/OT/IT, BCP/DR i kryteria akceptacji.
4. Sprawdź DoR/DoD, wprowadź do linkage_index i checklist.


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

- Dispatch, SCADA/PLC, OT security, Latency underground, SOS beacon.


## Przykłady użycia

- Wdrożenie systemu dispatch i tracking floty w kopalni odkrywkowej.
- Dodanie alarmów gazowych/SOS z integracją do systemu HSE i łączności awaryjnej.


## Ryzyka i ograniczenia

- Brak łączności awaryjnej → brak alarmów SOS; bezpieczeństwo OT (ransomware) wpływa na produkcję.
- Regulacje środowiskowe (emisje/hałas/woda) — konieczne raporty i limity.


## Decyzje i uzasadnienia

- [Decyzja] Priorytetyzacja funkcji (safety/production) — uzasadnienie HSE/KPI.
- [Decyzja] Wybór technologii łączności — uzasadnienie pokrycia i odporności.


## Powiązania z innymi dokumentami

- HSE Policy, OT Security Baseline, Connectivity Plan, Environmental Compliance, BCP/DR.


## Powiązania z sekcjami innych dokumentów

- Connectivity Plan → Łączność; OT Security → Bezpieczeństwo; Environmental Compliance → Raporty.


## Słownik pojęć w dokumencie

- Dispatch, SCADA, OT, LTE/5G mesh, Gas sensor, Geotechnical monitoring.


## Wymagane odwołania do standardów

- Regulacje górnicze i HSE lokalne, normy środowiskowe, standardy OT security (ISA/IEC 62443), BHP.


## Mapa relacji sekcja→sekcja

- Procesy/KPI → Wymagania → Integracje/Łączność → Bezpieczeństwo/BCP → Raporty.


## Mapa relacji dokument→dokument

- Mine Management Requirements → Connectivity/OT Security → BCP/DR → HSE/Environmental Compliance.


## Ścieżki informacji

- Cele/KPI → Wymagania → Projekt/Implementacja → Testy/Odbiór → Operacje/Monitoring → Raporty.


## Weryfikacja spójności

- [ ] Wymagania pokrywają cele produkcyjne i HSE.
- [ ] Łączność/BCP adekwatne do alarmów/bezpieczeństwa.
- [ ] Integracje i bezpieczeństwo OT są zgodne z politykami i regulacjami.


## Lista kontrolna spójności relacji

- [ ] Każde wymaganie ma właściciela/prioritet i powiązanie z KPI/HSE.
- [ ] Każda integracja ma format/protokół i zabezpieczenia.
- [ ] Relacje cross‑doc opisane z uzasadnieniem.


## Artefakty powiązane

- Mapy stref/geologiczne, inwentarz sprzętu/IoT, raporty HSE/środowiskowe, integracje SCADA/ERP/MES.


## Ścieżka decyzji

- [Decyzja] → [Uzasadnienie] → [Konsekwencje] → [Właściciel] → [Data].


## Ścieżka akceptacji

- Operations/HSE → OT/Security → IT → Compliance/Regulator (jeśli wymagane) → Owner sign‑off.


## Metryki jakości

| Metryka | Cel | Narzędzie |
|---------|-----|-----------|
| Kompletność sekcji | ≥ 90% wypełnionych | template_auditor.py |
| Aktualność | < 6 miesięcy od ostatniej rewizji | changelog_tracker.py |
| Spójność terminologii | 0 niespójności vs. słownik | bulk_section_patcher.py |
| Pokrycie standardami | ≥ 1 standard / regulacja | doc_standard_mapping |

## Kryteria ukończenia

- [ ] Wymagania kompletne i powiązane z KPI/HSE; integracje opisane.
- [ ] Bezpieczeństwo/BCP/Łączność określone; ryzyka i decyzje zapisane.
- [ ] Dokument w linkage_index i checklistach; wersja/data/właściciel aktualne.


## Powiązania sekcja↔sekcja

- Procesy i KPI → Wymagania funkcjonalne → Metryki i raporty.
- Bezpieczeństwo HSE/OT → Alarmy/SOS → Łączność i zasilanie awaryjne.
- Integracje → Interfejsy/formaty → Bezpieczeństwo danych i audyt.


## Struktura sekcji

1) Kontekst i cele (produkcja, HSE, środowisko)  
2) Procesy górnicze i użytkownicy (role, RACI)  
3) Wymagania funkcjonalne (dispatch, tracking, alarmy, raporty)  
4) Wymagania niefunkcjonalne (SLA, dostępność, latency, offline mode)  
5) Łączność i infrastruktura (LTE/5G/WiFi/mesh, coverage, redundancja)  
6) Integracje (SCADA/PLC, ERP/MES, GIS, czujniki, identity)  
7) Bezpieczeństwo i compliance (HSE, cyber OT/IT, audyt, prywatność)  
8) Dane i raportowanie (metryki, dashboardy, regulator)  
9) BCP/DR i bezpieczeństwo fizyczne/awaryjne  
10) Kryteria akceptacji, priorytety, ryzyka i decyzje  


## Wymagane rozwinięcia

- Lista KPI (produkcyjne, HSE, środowiskowe) i progi alarmów.
- Wymagania łączności (coverage pod ziemią, redundancja, latencja).
- Wymagania bezpieczeństwa OT (sieć, access, patching, monitoring).


## Wymagane streszczenia

- Regulacje kluczowe (HSE/środowisko) i ich implikacje.
- Top krytyczne procesy i alarmy (SOS/gaz/stabilność) z wymaganiami łączności.


## Guidance (skrót)

- Zacznij od celów produkcyjnych i HSE; zmapuj procesy i role.
- Ustal KPI i alarmy; zaplanuj łączność i zasilanie awaryjne pod ziemią.
- Wymagania bezpieczeństwa OT/IT: segmentacja, IAM, logging, patching, safety interlocks.
- Integracje opisuj z formatami/protokołami; zapewnij audyt i zgodność.
- Zaplanuj tryb offline/degraded i BCP/DR.


## Checklisty Definition of Ready (DoR)

- [ ] Procesy/KPI/HSE zebrane; regulacje znane.
- [ ] Inwentarz systemów OT/IT i łączności dostępny.
- [ ] Polityki bezpieczeństwa/BCP/DR dostępne.
- [ ] Struktura sekcji wypełniona/N/A.


## Checklisty Definition of Done (DoD)

- [ ] Wymagania funkcjonalne/niefunkcjonalne kompletne; priorytety przyznane.
- [ ] Integracje i bezpieczeństwo opisane; formaty/protokoły wskazane.
- [ ] BCP/DR i tryb offline zdefiniowane; właściciele przypisani.
- [ ] Ryzyka/decyzje udokumentowane; linki działają; dokument w linkage_index.
- [ ] Wersja/data/właściciel zaktualizowane.

