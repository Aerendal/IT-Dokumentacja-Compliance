---
title: Design SSO/federacji
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Design SSO/federacji


## Metadane

- Właściciel: Document Owner
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved
- Repo / moduł: [link]


## Cel dokumentu

Zaprojektować logikę SSO/federacji (SAML/OIDC) dla aplikacji/usług: doświadczenie użytkownika, bezpieczeństwo i integracje z IdP partnerów.


## Zakres i granice

- Obejmuje: wybór protokołu (SAML/OIDC), role IdP/SP, flow (B2E/B2B/B2C), multi-tenant, claim/attribute mapping, provisioning (JIT/SCIM), MFA/policy enforcement, session/logout/timeout, trust (certy/klucze/rotation), error handling, UX (login chooser), bezpieczeństwo (replay, token binding, PKCE), zgodność (PII/RODO), testy i rollout.
- Poza zakresem: pełny IAM design (osobny dokument), polityka haseł.


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia
- Wejścia: wymagania biznesowe, IdP/SP listy, polityki bezpieczeństwa, wymagania regulatora (PII/RODO), schemat atrybutów, certyfikaty/klucze, flow UX, SLA.  
- Wyjścia: architektura federacji, matryca IdP↔SP, konfiguracje trust/metadata, polityki atrybutów/claims, plan rotacji certów, MFA i IdP discovery, runbooki operacyjne, checklisty DoR/DoD.
## Założenia
- IdP i SP wspierają wybrane protokoły.  
- Polityki bezpieczeństwa i privacy obowiązują.  
- Monitoring i audyt są dostępne.
## Otwarte pytania
- Jakie są wymagania klientów/partnerów dot. MFA/claims?  
- Jak długo ważne są sesje/tokeny?  
- Jakie fallbacki przy awarii IdP?
## Powiązania (meta)
- Key Documents: identity_architecture, access_control_policy, privacy_policy, mfa_adoption_plan, incident_response_runbook, audit_trail_maintenance.  
- Key Document Structures: protokoły, atrybuty, security, UX, operacje, DR.  
- Document Dependencies: IdP/IdaaS, SP apps, certificate management, logging/monitoring, DNS/routing, metadata exchange.
## Zależności dokumentu
Wymaga: listy IdP/SP i protokołów, polityk security/privacy, cert management, schematu atrybutów, SLA i wymagań UX, narzędzi monitoringu/logów. Braki = DoR otwarte.
## Fazy cyklu życia
- Projekt protokołów i trust.  
- Implementacja/konfiguracja IdP/SP.  
- Testy (security/UX) i rollout.  
- Operacje, rotacje cert, audyt, DR.
## Struktura sekcji (szkielet)

- Use-case’y i flow (B2E/B2B/B2C)
- Protokoły i role (IdP/SP)
- Atrybuty/claims i provisioning (JIT/SCIM)
- MFA/polityki i session management
- Trust/certy/rotacja i bezpieczeństwo
- UX i obsługa błędów
- Testy, rollout i monitoring


## Szybkie powiązania

- IAM Design, Authentication Requirements, API Security, Privacy/RODO, Audit Trail.


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
1. Zdefiniuj protokoły, atrybuty i trust dla IdP/SP.  
2. Skonfiguruj rotacje certów, monitoring i MFA/UX.  
3. Przetestuj security/UX; opublikuj runbooki; uzupełnij DoR/DoD i linkage_index.
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
- IdP: Identity Provider.  
- SP: Service Provider.  
- Home realm discovery: wybór IdP użytkownika.
## Przykłady użycia
- Federacja B2B SAML z partnerami.  
- OIDC do aplikacji wewnętrznych i mobilnych.  
- SCIM provisioning grup dla SaaS.
## Ryzyka i ograniczenia
- Expired cert → outage.  
- Nadmiar atrybutów → ryzyko privacy.  
- Brak MFA/risk → fraud/compromise.
## Decyzje i uzasadnienia
- SAML vs OIDC dla danego SP.  
- Zakres claims/atrybutów i mapping.  
- Rotacja cert/metadata automatyczna vs manual.
## Powiązania z innymi dokumentami
- access_control_policy — autoryzacja.  
- identity_architecture — topologia.  
- audit_trail_maintenance — logi.
## Powiązania z sekcjami innych dokumentów

- [Dokument X → Sekcja Y] — [powód powiązania i kierunek przepływu informacji]
- [Dokument Z → Sekcja W] — [powód powiązania i kierunek przepływu informacji]

## Słownik pojęć w dokumencie

- [Pojęcie 1] — [definicja i źródło normalizacyjne lub wewnętrzne]
- [Pojęcie 2] — [definicja i źródło normalizacyjne lub wewnętrzne]

## Wymagane odwołania do standardów
- OIDC/SAML/SCIM spec, RODO/PII, polityki bezpieczeństwa.  
- Wytyczne regulatorów/branżowe (np. PSD2/PCI).
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

## Wejścia

- IdP organizacji/partnerów, wymagania UX/bezpieczeństwa, katalog aplikacji, polityki PII/RODO, modele tenantów, SLO/SLA auth.


## Wyjścia

- Architektura SSO/federacji, mapping atrybutów, polityki MFA/session, plan rollout i testów, checklisty integracji.



## Jak używać (checklista)

- Wybierz flow i protokół; skonfiguruj trust/certy; zmapuj atrybuty.
- Ustal MFA/polityki i sesje; skonfiguruj provisioning; przetestuj z partnerami.
- Przygotuj UX (login chooser, błędy), monitoring i plan rotacji kluczy.


## Wymagane rozwinięcia / powiązania

- Diagramy flow, mapping atrybutów, polityka MFA/session, procedura rotacji cert, test cases, checklisty integracji IdP.


## Kryteria DoR

- IdP i aplikacje w scope, wymagania UX/bezpieczeństwa zebrane.


## Kryteria DoD

- Konfiguracje opisane/przetestowane, mappingi zatwierdzone, MFA/session/policy ustawione, plan rollout i monitoring gotowy.


## Artefakty

- Dokument design, mappingi, konfiguracje IdP/SP, testy, logi audytu.


## Walidacja

- Testy SSO z partnerami, rotacja cert, testy MFA/session, audyt PII w tokenach, monitoring błędów.


## Metryki

- SSO success rate, błędy auth, czas logowania, pokrycie MFA, incydenty bezpieczeństwa.


## Utrzymanie

- Rotacja cert/kluczy; przegląd mappingów i polityk; testy po zmianach IdP/app; audyt PII.


## Zakończenie

Projekt SSO/federacji zapewnia bezpieczne i wygodne logowanie; utrzymuj go z rotacją, testami i audytami.

