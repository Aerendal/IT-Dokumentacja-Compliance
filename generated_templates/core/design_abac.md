---
title: Design ABAC
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Design ABAC (Attribute-Based Access Control)


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Projekt kontroli dostępu opartej na atrybutach (ABAC): model atrybutów, polityki, źródła danych, ewaluacja i egzekwowanie, audyt oraz governance.


## Zakres i granice

- Obejmuje: słownik atrybutów użytkownika/zasobu/kontekstu, model polityk (permit/deny, default), źródła i synchronizację atrybutów, PDP/PEP/cache, audyt decyzji, testy/regresje, proces zmian i przeglądów.  
- Poza zakresem: RBAC/SoD (oddzielny dokument), zarządzanie tożsamością (provisioning IdP), szczegółowe implementacje sieciowe.


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia

- Wejścia: katalog ról/tożsamości (IdP), klasyfikacja danych/zasobów, wymagania compliance (PII/PCI/SOX), mapy systemów i punktów egzekwowania, profile ryzyka, polityki privacy.  
- Wyjścia: zestaw atrybutów i schematów, wzorce polityk (OPA/Rego/XACML), decyzje default, architektura PDP/PEP, plan synchronizacji atrybutów i cache, testy/regresje, audyt i raporty, linki w linkage_index.


## Założenia

- [Założenie 1 — co przyjmujemy za prawdziwe bez weryfikacji]
- [Założenie 2 — warunki brzegowe, które muszą być spełnione]

## Otwarte pytania

- [Pytanie 1 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]
- [Pytanie 2 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]

## Powiązania (meta)

- Key Documents: access_control_matrix_reference, design_abac_policy_library, api_security_design, audit_logging, privacy_policy, incident_response_runbook, zero_trust_architecture_design.  
- Key Document Structures: atrybuty, polityki, źródła/sync, PDP/PEP, audyt, testy, governance.  
- Document Dependencies: IdP/SCIM, CMDB/tagi zasobów, katalog klasyfikacji danych, czas/NTP, SIEM, caching/edge gateways.



## Zależności dokumentu
- Upstream: AC goals, data classification, źródła atrybutów, SoD requirements, risk register.
- Downstream: policy-as-code, implementacja PEP w app/API/data, tokeny/claims, audyt/logi, testy AC, recertyfikacje.
- Zewnętrzne: dostawcy PDP/PEP, audytorzy/regulatorzy.
## Fazy cyklu życia
- Analiza atrybutów i źródeł; słowniki.
- Projekt polityk i architektury PDP/PEP.
- Implementacja/tokeny/PEP, testy (policy-as-code).
- Rollout, monitoring, recertyfikacje, iteracje.
## Struktura sekcji (szkielet)

- Kontekst i wymagania
- Decyzje architektoniczne (ADR)
- Komponenty i integracje
- Diagramy (C4/UML/flowchart)
- Bezpieczeństwo i compliance
- Skalowalność i ograniczenia

## Szybkie powiązania

- linkage_index.jsonl (security/design_abac)  
- design_abac_policy_library, audit_logging, zero_trust_architecture_design, privacy_policy


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **IEEE 1016** — Standard dla Opisów Projektowania Oprogramowania (SDD)
- **IEEE 42010** — Opis Architektoniczny Systemów i Oprogramowania
- **ISO/IEC 15288** — Procesy Cyklu Życia Systemów
- **TOGAF ADM** — Framework Architektury Korporacyjnej (The Open Group)

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

1. Zbierz wymagania i klasyfikacje zasobów; zbuduj słownik atrybutów i źródła.  
2. Zaprojektuj polityki i PDP/PEP z cache i logowaniem; zdecyduj default deny/fail‑closed.  
3. Uruchom testy/regresje, wdroż governance i rollout; zaktualizuj linkage_index.


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

- [Ryzyko 1 — prawdopodobieństwo, wpływ, sposób ograniczenia]
- [Ryzyko 2 — prawdopodobieństwo, wpływ, sposób ograniczenia]

## Decyzje i uzasadnienia

- [Decyzja 1 — uzasadnienie, alternatywy odrzucone, data]
- [Decyzja 2 — uzasadnienie, alternatywy odrzucone, data]

## Powiązania z innymi dokumentami

- [Dokument A] — [typ relacji: wymaga/uzupełnia/zastępuje/jest-częścią] — [uzasadnienie]
- [Dokument B] — [typ relacji] — [uzasadnienie]

## Powiązania z sekcjami innych dokumentów

- [Dokument X → Sekcja Y] — [powód powiązania i kierunek przepływu informacji]
- [Dokument Z → Sekcja W] — [powód powiązania i kierunek przepływu informacji]

## Słownik pojęć w dokumencie

- [Pojęcie 1] — [definicja i źródło normalizacyjne lub wewnętrzne]
- [Pojęcie 2] — [definicja i źródło normalizacyjne lub wewnętrzne]

## Wymagane odwołania do standardów

- [Standard 1, np. ISO 27001 §A.5] — [sekcja lub wymaganie, którego dotyczy to odwołanie]
- [Standard 2] — [sekcja lub wymaganie]

## Mapa relacji sekcja→sekcja

- [Sekcja A] -> [Sekcja B] : [typ relacji: rozszerza/streszcza/wymaga/wyklucza]
- [Sekcja C] -> [Sekcja D] : [typ relacji]

## Mapa relacji dokument→dokument

- [Dokument A] -> [Dokument B] : [typ relacji]
- [Dokument C] -> [Dokument D] : [typ relacji]

## Ścieżki informacji

- [Wejście] -> [Sekcja źródłowa] -> [Sekcja rozwinięcia] -> [Wyjście]
- [Wejście] -> [Sekcja źródłowa] -> [Sekcja streszczenia] -> [Wyjście]

## Weryfikacja spójności

- [ ] Atrybuty mają źródło prawdy i wersję; brak atrybutu nie daje dostępu.  
- [ ] Polityki pokrywają główne zasoby i są testowane; default deny egzekwowany.  
- [ ] Logi decyzji kompletne; metryki pokazują latency i deny rate; governance działa.


## Lista kontrolna spójności relacji

- [ ] Czy każda sekcja z relacją ma wskazaną sekcję źródłową?
- [ ] Czy relacje nie tworzą sprzecznych wymagań?
- [ ] Czy wszystkie wymagane standardy mają odwołania?
- [ ] Czy RACI jest kompletne dla kluczowych działań?

## Artefakty powiązane

- Słownik atrybutów, repo polityk (Rego/XACML), diagram PDP/PEP, konfiguracja cache, logi decyzji, metryki, ADR/waiver log.


## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji

- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status: oczekuje/zatwierdzone/odrzucone]
- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status]

## Metryki jakości

- Latency decyzji, hit/miss cache, deny rate vs oczekiwany, liczba bypass/waiver, czas propagacji zmian atrybutów, liczba incydentów eskalacji uprawnień.

## Kryteria ukończenia

- [ ] ABAC zaprojektowany z pełnym zestawem atrybutów, polityk, PDP/PEP, testów i audytu; powiązany w linkage_index.


## Struktura sekcji

1) Model atrybutów (user: role, dept, clearance; resource: classification, owner, sensitivity; context: location, device, time, network)  
2) Polityki i decyzje (model, język Rego/XACML, permit/deny, default deny, konflikt/precedencje)  
3) Źródła i synchronizacja atrybutów (IdP, katalog zasobów, tagi, częstotliwość, jakość danych)  
4) Ewaluacja i egzekwowanie (PDP/PEP, cache/TTL, push vs pull, fail‑open/closed)  
5) Audyt i obserwowalność (logi decyzji, korelacja, metryki hit/miss cache, latency)  
6) Testy i walidacja polityk (unit/regresja, simulacje, canary, property-based)  
7) Governance i zmiany (ownerzy polityk, code review, rollout, waivery, przeglądy okresowe)  
8) Załączniki (biblioteka polityk, słownik atrybutów, ADR/waiver log)


## Wymagane rozwinięcia

- Słownik atrybutów z typami, dopuszczalnymi wartościami i źródłem prawdy; zasady wersjonowania.  
- Standard polityk (naming, moduły, rego/xacml) i scenariusze priorytetyzacji/konfliktów.  
- Strategia cache (TTL, revalidation) i zachowanie fail‑open/closed dla PEP.  
- Wymagania logowania decyzji i metryk (latencja, deny rate, coverage).  
- Plan testów regresji i bezpieczeństwa (bypass, privilege escalation).


## Wymagane streszczenia

- Executive: pokrycie atrybutami i politykami, decyzja default, gotowość PDP/PEP, główne ryzyka (bypass, dane atrybutów).


## Guidance (skrót)

- Default deny + najmniejszy zestaw atrybutów konieczny do decyzji; ogranicz cardinality.  
- Źródła atrybutów muszą być wersjonowane i audytowane; brak atrybutu = brak dostępu.  
- Cache PEP z krótkim TTL i twardym odświeżeniem przy zmianie uprawnień; loguj wszystkie decyzje.  
- Polityki jako kod z code review i testami; każda zmiana wymaga rollout i możliwego canary.  
- Regularnie przeglądaj deny/allow outliers, buduj metryki dla drift atrybutów.


## Checklisty Definition of Ready (DoR)

- [ ] Słownik atrybutów i źródeł zidentyfikowany; wymagania compliance znane.  
- [ ] Punkty egzekwowania (PEP) zmapowane; decyzja default deny uzgodniona.  
- [ ] Kanały logowania/audytu dostępne.


## Checklisty Definition of Done (DoD)

- [ ] Polityki i słownik atrybutów opisane; PDP/PEP i cache zaprojektowane; logowanie decyzji działa.  
- [ ] Testy/regresje i proces rollout/waiver opisane; linkage_index zaktualizowany; status/metadane aktualne.  
- [ ] Checklisty DoR/DoD odhaczone.

