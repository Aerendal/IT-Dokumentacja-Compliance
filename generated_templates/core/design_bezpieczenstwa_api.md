---
title: Design bezpieczeństwa API
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Design bezpieczeństwa API


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Projekt zabezpieczeń API obejmujący uwierzytelnianie, autoryzację, ochronę przed nadużyciami, prywatność danych oraz obserwowalność i audyt.


## Zakres i granice

- Obejmuje: AuthN (OAuth2/OIDC, mTLS, API keys przypadki), AuthZ (scopes/roles/ABAC), ochronę (rate limiting/throttling, WAF, input validation/schema enforcement, idempotencja, replay protection, signing/HMAC), dane i prywatność (PII minimization, masking, FLE), obserwowalność/audyt (trace/log/audit events), bezpieczeństwo operacyjne (secret management, supply chain/SCA, CI/CD security gates, wersjonowanie/deprecjacja).  
- Poza zakresem: testy penetracyjne (osobny runbook), monitoring ogólny (logging_strategy), szczegóły kontraktów API (specyfikacja_wymagan_api).


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia

- Wejścia: wymagania compliance (PCI/RODO), katalog usług/zasobów, model uprawnień, profil ruchu i limity, lista danych wrażliwych, polityka secretów/rotacji, architektura sieci.  
- Wyjścia: wzorzec zabezpieczeń API, matryca wymagań AuthN/AuthZ, polityki rate limit/WAF/validation, zasady logowania/audytu, lista kontroli CI/CD, linki w linkage_index.


## Założenia

- [Założenie 1 — co przyjmujemy za prawdziwe bez weryfikacji]
- [Założenie 2 — warunki brzegowe, które muszą być spełnione]

## Otwarte pytania

- [Pytanie 1 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]
- [Pytanie 2 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]

## Powiązania (meta)

- Key Documents: api_security_assessment, specyfikacja_wymagan_api, strategia_wersjonowania_api, audit_logging, logging_strategy, secrets_management, design_abac, rate_limiting_requirements.  
- Key Document Structures: AuthN, AuthZ, ochrona, dane/prywatność, observability/audyt, operacje.  
- Document Dependencies: IdP/OIDC, gateway/WAF, SIEM, secret manager, PKI, CI/CD pipeline, CMDB usług.



## Zależności dokumentu
- Konsumuje: System/Technical Design, Data Model, Security requirements.
- Dostarcza do: Implementation, Contract tests, Client SDK/Integration guides, Monitoring (SLO/SLI).
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

- Kontekst i cele API
- Zakres i odpowiedzialność usług
- Modele danych (schematy, typy, walidacje)
- Endpointy/metody lub kanały/eventy (z parametrami)
- Autoryzacja i uwierzytelnianie (scopes, role, klucze)
- Limity i throttling, retry/idempotencja
- Wersjonowanie i kompatybilność
- Kody błędów i format odpowiedzi
- SLA/SLO oraz wymagania monitoringu
- Przykłady użycia i scenariusze edge-case
- [Sekcja 3]
## Struktura sekcji (szkielet)
- Kontekst i cele
- Wzorce zasobów i nazewnictwo
- Wersjonowanie/kompatybilność
- Błędy/retries/timeouts
- Pagination/filtry/sortowanie
- Idempotency i bezpieczeństwo
- Event/async patterns
- Ryzyka i wyjątki
## Szybkie powiązania

- linkage_index.jsonl (security/api_security_design)  
- api_security_assessment, audit_logging, logging_strategy, specyfikacja_wymagan_api, strategia_wersjonowania_api


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **CIS Controls v8** — Krytyczne Mechanizmy Bezpieczeństwa (CIS)
- **IEEE 1016** — Standard dla Opisów Projektowania Oprogramowania (SDD)
- **IEEE 42010** — Opis Architektoniczny Systemów i Oprogramowania
- **ISO/IEC 15288** — Procesy Cyklu Życia Systemów
- **ISO/IEC 27001** — System Zarządzania Bezpieczeństwem Informacji (ISMS)
- **ISO/IEC 27002** — Wytyczne Praktyk Bezpieczeństwa Informacji
- **ISO/IEC 27005** — Zarządzanie Ryzykiem Bezpieczeństwa Informacji
- **NIST CSF** — Framework Cyberbezpieczeństwa NIST
- **TOGAF ADM** — Framework Architektury Korporacyjnej (The Open Group)

### Polskie normy i regulacje
- **CERT-PL-WYTYCZNE** — Wytyczne CERT Polska (CSIRT NASK) dot. cyberbezpieczeństwa
- **KSC-PL** — Ustawa o Krajowym Systemie Cyberbezpieczeństwa

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

1. Zmapuj usługi/endpoints i dane wrażliwe; wybierz flows AuthN i model AuthZ.  
2. Ustal polityki ochrony (rate limit/WAF/validation), logowanie i audyt; skonfiguruj CI/CD gates.  
3. Dodaj powiązania w linkage_index, odhacz DoR/DoD po wypełnieniu sekcji.


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

- [ ] Każdy endpoint ma AuthN/AuthZ i politykę limitów; schemat walidowany.  
- [ ] Dane wrażliwe maskowane; logi/audyt bez PII; anti‑replay/ signing włączone.  
- [ ] CI/CD blokuje brak testów bezpieczeństwa/SCA; deprecjacje mają plan i komunikację.


## Lista kontrolna spójności relacji

- [ ] Czy każda sekcja z relacją ma wskazaną sekcję źródłową?
- [ ] Czy relacje nie tworzą sprzecznych wymagań?
- [ ] Czy wszystkie wymagane standardy mają odwołania?
- [ ] Czy RACI jest kompletne dla kluczowych działań?

## Artefakty powiązane

- OpenAPI/AsyncAPI, polityki WAF/rate limit, matryca scopes/claims, config gateway, log/audit schematy, CI/CD policy files, ADR/waiver log.


## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji

- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status: oczekuje/zatwierdzone/odrzucone]
- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status]

## Metryki jakości

- Pokrycie endpoints AuthN/AuthZ, liczba nadużyć/1k req, średni czas rotacji sekretów, odsetek logów bez PII, compliance pass rate, liczba rollbacków zmian bezpieczeństwa.

## Kryteria ukończenia

- [ ] Dokument pozwala wdrożyć spójne zabezpieczenia API (AuthN, AuthZ, ochrona, prywatność, audyt) i jest osadzony w linkage_index.


## Struktura sekcji

1) Uwierzytelnianie (OAuth2/OIDC flows, mTLS, rotacja/TTL tokenów, klucze API – kiedy dozwolone)  
2) Autoryzacja (scopes/roles, ABAC, decyzje default, least privilege, delegacja)  
3) Ochrona i odporność (rate limit, WAF, validation/schema, idempotency keys, anti‑replay, signing)  
4) Dane wrażliwe i prywatność (minimalizacja, FLE/masking, payload size, log redaction)  
5) Observability i audyt (request/trace id, audit events, detekcja anomalii, alerty nadużyć)  
6) Bezpieczeństwo operacyjne (secret mgmt, SCA/Dependabot, CI/CD gates, versioning/deprecation)  
7) Załączniki (polityki, przykładowe configi gateway/WAF, ADR/waiver log)


## Wymagane rozwinięcia

- Tabela flows OAuth2/OIDC per kanał (public/confidential, mobile, M2M) i wymogi PKCE/DPoP.  
- Matryca scopes/claims → zasoby/endpoints; zasady ABAC dla danych wrażliwych.  
- Polityki limitów (global, per klient, burst) i sygnatur/anti‑replay.  
- Checklist logowania/redaction i audytu; integracja z SIEM.  
- CI/CD: skan SCA/secret, podpisy artifactów, policy-as-code.


## Wymagane streszczenia

- Executive: poziom pokrycia zabezpieczeń API, główne ryzyka (auth, abuse, PII), stan rolloutu gateway/WAF.


## Guidance (skrót)

- Domyślnie blokuj (default deny) i stosuj najmniej uprzywilejowane scopes.  
- Wymuś PKCE/DPoP dla publicznych klientów; mTLS między usługami.  
- Wymagaj idempotency key dla operacji mutujących; waliduj schemat (JSON Schema/OpenAPI).  
- Loguj bez PII; audit events dla authZ changes, admin calls, eksportów danych.  
- Automatyzuj rotację sekretów i kluczy; każdy breaking change z planem deprecjacji.


## Checklisty Definition of Ready (DoR)

- [ ] Usługi/endpoints i dane wrażliwe zidentyfikowane; wymagania compliance znane.  
- [ ] IdP/OIDC i gateway/WAF dostępne; polityka secretów/rotacji określona.


## Checklisty Definition of Done (DoD)

- [ ] AuthN/AuthZ zaprojektowane; polityki ochrony i prywatności opisane; logi/audyt skonfigurowane.  
- [ ] CI/CD security gates i SCA określone; linkage_index zaktualizowany; status/metadane aktualne.  
- [ ] Checklisty DoR/DoD odhaczone.

