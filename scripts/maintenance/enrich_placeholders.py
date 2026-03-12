#!/usr/bin/env python3
"""
enrich_placeholders.py — wypełnia szablony-placeholdery
treścią opisującą: cel, co zawierają, dlaczego i mechanizmy wpływu.
"""

import argparse
import re
import sqlite3
import sys
from pathlib import Path

DB_PATH = Path(__file__).parent.parent.parent / "reports/it_doc_matrix.db"
TDIR = Path(__file__).parent.parent.parent / "generated_templates"
PLACEHOLDER = "opisuje cel dokumentu, decyzje do podjęcia"

# ── Archetypy dokumentów ─────────────────────────────────────────────────────
# Każdy archetypów: (keywords_in_title, cel, wejscia, wyjscia, wplywa_na, zalezy_od, sekcje_relacje)
ARCHETYPES = [
    # === INCYDENT / RESPONSE ===
    (
        [
            "incident response",
            "response plan",
            "reagowanie na incydent",
            "obsługa incydentu",
            "incident handling",
            "response procedure",
            "outage response",
            "breach response",
            "alert response",
            "failure response",
        ],
        (
            "Definiuje procedurę reagowania na incydenty — od wykrycia przez analizę, izolację i eliminację "
            "do odtworzenia i wnioskowania poreaktywnego. Zawiera: klasyfikację incydentów (P1–P4), "
            "macierz eskalacji, role i odpowiedzialności (RACI), kroki runbooka, kryteria powiadomień regulacyjnych."
        ),
        "Polityka bezpieczeństwa informacji, rejestr ryzyk, plany komunikacji, dane z systemów monitorowania (SIEM/alerting), kontakty zewnętrzne (CSIRT, vendor).",
        "Wypełniony ticket incydentu, raport postmortem, aktualizacja rejestru incydentów, wnioski do planu zarządzania ryzykiem.",
        "Raport postmortem, plan zarządzania ryzykiem, polityka bezpieczeństwa (aktualizacje), plany ciągłości działania (BCP).",
        "Polityka bezpieczeństwa, rejestr zasobów, plany testów penetracyjnych, kontrakty z dostawcami (SLA).",
        (
            '"Klasyfikacja incydentu" **determines** "Eskalację i notyfikacje".\n'
            '- "Izolacja" **precedes** "Eliminację" i **feeds** "Analizę przyczyn źródłowych".\n'
            '- "Wnioski" **feeds** "Aktualizację polityki bezpieczeństwa" i "Rejestr ryzyk".'
        ),
    ),
    # === DISASTER RECOVERY / BCP ===
    (
        [
            "disaster recovery",
            "odtwarzanie po awarii",
            "business continuity",
            "ciągłość działania",
            "bcp",
            "drp",
            "recovery plan",
            "business impact",
            "bia",
        ],
        (
            "Określa cele odtworzeniowe (RTO, RPO) i procedury przywracania usług po katastrofie lub poważnej awarii. "
            "Zawiera: krytyczne systemy i priorytety odtworzenia, kolejność działań, alternatywne lokalizacje/środowiska, "
            "harmonogram testów BCP/DR."
        ),
        "Analiza wpływu na biznes (BIA), inwentarz systemów (CMDB), umowy SLA z dostawcami, wyniki ostatnich testów DR, topologia sieci i infrastruktury.",
        "Plan testów DR, harmonogram ćwiczeń, raporty z testów, zaktualizowane procedury runbooka, metryki RTO/RPO.",
        "Plany testów DR, raporty z ćwiczeń, umowy z dostawcami cloud/hostingiem, polityki retencji backupów, plany komunikacji kryzysowej.",
        "Analiza BIA, rejestr zasobów (CMDB), polityka backupów, plany zarządzania incydentami.",
        (
            '"BIA i priorytety" **drives** "Kolejność odtworzenia".\n'
            '- "Procedury odtworzenia" **feeds** "Runbooki operacyjne".\n'
            '- "Wyniki testów DR" **updates** "RTO/RPO i cele odtworzeniowe".'
        ),
    ),
    # === ARCHITEKTURA ADR ===
    (
        ["architecture decision", "adr", "architectural decision", "decision record"],
        (
            "Dokumentuje pojedynczą decyzję architektoniczną — kontekst, problem, rozważane opcje, podjętą decyzję, "
            "uzasadnienie i konsekwencje. Format ADR umożliwia śledzenie ewolucji architektury i rozumienie "
            "historycznych wyborów projektowych."
        ),
        "Wymagania systemowe, ograniczenia techniczne i biznesowe, dostępne technologie, istniejąca architektura, wyniki spike'ów/prototypów.",
        "Zatwierdzona decyzja architektoniczna z uzasadnieniem, lista odrzuconych alternatyw z powodami, implikacje dla innych komponentów.",
        "Dokumenty projektowe systemów, specyfikacje API, plany migracji, konfiguracje infrastruktury, wymagania niefunkcjonalne (NFR).",
        "Wymagania systemowe, istniejące ADR (kontekst), wyniki proof-of-concept, standardy technologiczne organizacji.",
        (
            '"Kontekst i problem" **drives** "Opcje do rozważenia".\n'
            '- "Wybrana opcja" **constrains** "Implementację i konfigurację".\n'
            '- "Konsekwencje" **feeds** "Kolejne ADR i risk register".'
        ),
    ),
    # === ARCHITEKTURA SYSTEMU ===
    (
        [
            "system architecture",
            "architektura systemu",
            "architecture overview",
            "high-level design",
            "hld",
            "architektura platformy",
            "architektura aplikacji",
            "architektura rozwiązania",
            "solution architecture",
        ],
        (
            "Opisuje strukturę wysokiego poziomu systemu — komponenty, ich odpowiedzialności, wzajemne zależności "
            "i przepływy danych. Stanowi kontrakt architektoniczny dla zespołów implementujących, "
            "podstawę dla ADR i wejście do szczegółowego projektowania."
        ),
        "Wymagania biznesowe i niefunkcjonalne, ograniczenia (budżet, czas, regulacje), istniejące systemy i integracje, standardy technologiczne organizacji.",
        "Diagram architektoniczny (C4/UML), opis komponentów i interfejsów, macierz decyzji, lista ADR do podjęcia, wytyczne dla projektowania szczegółowego.",
        "Szczegółowe projekty komponentów, specyfikacje API, plany testów (NFR), dokumentacja wdrożeniowa, plany migracji.",
        "Wymagania funkcjonalne i NFR, polityki bezpieczeństwa, ograniczenia compliance, istniejąca architektura (as-is).",
        (
            '"Wymagania NFR" **constrains** "Wybory architektoniczne".\n'
            '- "Diagram komponentów" **drives** "Specyfikacje interfejsów".\n'
            '- "Decyzje architektoniczne" **feeds** "ADR log".'
        ),
    ),
    # === WYMAGANIA ===
    (
        [
            "wymagania",
            "requirements specification",
            "software requirements",
            "business requirements",
            "functional requirements",
            "system requirements",
            "specyfikacja wymagań",
        ],
        (
            "Definiuje kompletny, weryfikowalny zbiór wymagań funkcjonalnych i niefunkcjonalnych. "
            "Każde wymaganie powinno być: unikalne (ID), jednoznaczne, testowalnie zdefiniowane, "
            "przypisane do priorytetu (MoSCoW) i powiązane z przypadkiem użycia lub epikiem."
        ),
        "Wizja produktu, cele biznesowe, wywiady ze stakeholderami, analiza rynku/konkurencji, ograniczenia prawne i techniczne, istniejące systemy (as-is).",
        "Rejestr wymagań z ID i priorytetami, macierz śledzności (traceability), kryteria akceptacji, lista pytań otwartych, baseline dla zarządzania zmianami.",
        "Specyfikacje projektowe, plany testów akceptacyjnych (UAT), backlog produktu, dokumentacja API, szacowania pracochłonności.",
        "Wywiady ze stakeholderami, analiza procesów as-is, standardy regulacyjne/branżowe, architektura to-be.",
        (
            '"Wymagania funkcjonalne" **drives** "Przypadki testowe UAT".\n'
            '- "Wymagania NFR" **constrains** "Architekturę systemu".\n'
            '- "Priorytety MoSCoW" **feeds** "Backlog i planowanie sprintów".'
        ),
    ),
    # === USER STORIES ===
    (
        ["user stor", "user stories", "historia użytkownika", "story mapping", "user story"],
        (
            "Zawiera zbiór historyjek użytkownika (user stories) w formacie: Jako [rola] chcę [akcja] po to, żeby [wartość]. "
            "Każda story powinna mieć kryteria akceptacji (Given-When-Then), estymację (story points) "
            "i powiązanie z epikiem."
        ),
        "Wizja produktu, persona użytkownika, wyniki badań UX, cele sprintu/releasu, feedback z poprzednich sprintów.",
        "Wyspecyfikowane stories gotowe do sprintu (DoR), kryteria akceptacji per story, estymacje, macierz zależności między stories.",
        "Sprint backlog, plan sprintu, testy akceptacyjne, dokumentacja zmian w produkcie.",
        "Epiki i cel sprintu, persona użytkownika, wyniki testów użyteczności, techniczne spike'i.",
        (
            '"Kryterium akceptacji" **drives** "Testy automatyczne i manualne".\n'
            '- "Story points" **feeds** "Velocity i planowanie kapacytetu".\n'
            '- "Zależności stories" **constrains** "Kolejność sprintów".'
        ),
    ),
    # === TESTOWANIE ===
    (
        ["test plan", "plan testów", "test strategy", "strategia testowania", "qa plan"],
        (
            "Definiuje podejście do testowania — scope, typy testów (jednostkowe, integracyjne, systemowe, UAT, regresja), "
            "narzędzia, środowiska, role i harmonogram. Stanowi kontrakt jakościowy między QA a projektem."
        ),
        "Wymagania funkcjonalne i NFR, architektura systemu, harmonogram projektu, dostępne zasoby QA, kryteria wejścia i wyjścia (DoR/DoD).",
        "Strategia testowania z zakresem, macierz typów testów i odpowiedzialności, plan środowisk testowych, harmonogram faz testowania, kryteria go/no-go.",
        "Przypadki testowe (test cases), raporty z testów, bug tracker, metryki jakości (defect density, coverage), decyzja go-live.",
        "Specyfikacja wymagań, architektura systemu, plan projektu, polityki jakości organizacji.",
        (
            '"Scope testów" **constrains** "Zbiór przypadków testowych".\n'
            '- "Kryteria wyjścia" **drives** "Decyzję go/no-go".\n'
            '- "Raporty z testów" **feeds** "Analizę ryzyk projektu".'
        ),
    ),
    (
        ["test case", "przypadki testowe", "test scenario", "scenariusze testowe", "test cases"],
        (
            "Zawiera szczegółowe przypadki testowe: warunki wstępne, kroki, dane wejściowe, oczekiwany rezultat "
            "i kryteria zaliczenia. Każdy przypadek powinien być powiązany z wymaganiem (traceability) "
            "i posiadać priorytet."
        ),
        "Specyfikacja wymagań, user stories z kryteriami akceptacji, projekt UI/UX, dane testowe, środowisko testowe.",
        "Zestaw przypadków testowych gotowych do wykonania, dane testowe, wyniki wykonania (pass/fail), raporty defektów.",
        "Bug tracker (nowe defekty), raport z testów, metryki pokrycia wymagań, status release.",
        "Wymagania funkcjonalne, kryteria akceptacji user stories, projekt UI, dostęp do środowiska testowego.",
        (
            '"Warunki wstępne" **must precede** "Wykonanie kroków testowych".\n'
            '- "Oczekiwany vs rzeczywisty wynik" **drives** "Raport defektu".\n'
            '- "Pokrycie wymagań" **feeds** "Raport z testów i decyzję release".'
        ),
    ),
    # === PROJECT CHARTER ===
    (
        ["project charter", "inicjacja projektu", "karta projektu", "business case"],
        (
            "Autoryzuje projekt i definiuje jego granice — cel biznesowy, zakres wysokiego poziomu, budżet, "
            "sponsor, kluczowych interesariuszy i PM. Stanowi mandat dla PM do angażowania zasobów."
        ),
        "Business case, analiza wykonalności, zatwierdzenia budżetowe, dostępność zasobów, strategic roadmap.",
        "Zatwierdzona karta projektu, wyznaczony PM i sponsor, wstępny rejestr interesariuszy, kamienie milowe.",
        "Plan zarządzania projektem, rejestr interesariuszy, plan komunikacji, WBS, plan zarządzania ryzykiem.",
        "Business case, analiza CBA, strategic roadmap, portfolio projektów organizacji.",
        (
            '"Cel biznesowy" **drives** "Zakres i kryteria sukcesu".\n'
            '- "Budżet i zasoby" **constrains** "Plan harmonogramu".\n'
            '- "Karta projektu" **authorizes** "Wszystkie kolejne dokumenty projektowe".'
        ),
    ),
    # === HARMONOGRAM ===
    (
        [
            "harmonogram",
            "project schedule",
            "gantt",
            "timeline",
            "roadmap",
            "milestone",
            "kamień milowy",
        ],
        (
            "Przedstawia sekwencję zadań, zależności, kamienie milowe i daty dostarczenia. "
            "Stanowi podstawę do monitorowania postępu, zarządzania zmianami zakresu i komunikacji statusu."
        ),
        "WBS, szacowania pracochłonności, dostępność zasobów, zależności między zadaniami, kamienie milowe kontraktowe.",
        "Harmonogram bazowy (baseline), ścieżka krytyczna, macierz zasobów, kamienie milowe do raportowania, plan rezerwowy.",
        "Raporty statusu projektu, wnioski o zmiany (change requests), alokacje zasobów, plan testów i wdrożenia.",
        "WBS, szacowania pracochłonności, karta projektu, plan zarządzania ryzykiem.",
        (
            '"Zależności zadań" **determines** "Ścieżkę krytyczną".\n'
            '- "Kamienie milowe" **drives** "Raportowanie statusu i go/no-go gates".\n'
            '- "Rzeczywisty postęp" **updates** "Prognozę terminu zakończenia".'
        ),
    ),
    # === RUNBOOK / SOP ===
    (
        [
            "runbook",
            "playbook",
            "procedura operacyjna",
            "operational procedure",
            "sop",
            "instrukcja",
        ],
        (
            "Zawiera krok po kroku instrukcje dla operatorów IT do wykonania powtarzalnych zadań lub reagowania "
            "na zdarzenia. Każdy krok powinien: być atomowy, zawierać oczekiwany rezultat, wskazywać akcję "
            "przy błędzie i określać czas wykonania."
        ),
        "Architektura systemu, topologia sieci, dane dostępu (vault/secrets), poprzednie incydenty (lessons learned), wymagania SLA.",
        "Udokumentowana procedura gotowa do wykonania, lista wymaganych uprawnień, kryteria sukcesu/niepowodzenia, log wykonania.",
        "Log operacji (audit trail), metryki dostępności systemu, raporty z testów DR, baza wiedzy.",
        "Architektura systemu, CMDB, polityki bezpieczeństwa (zasada najmniejszych uprawnień), wymagania SLA/OLA.",
        (
            '"Warunki wstępne i dostępy" **must precede** "Wykonaniem kroków".\n'
            '- "Kryteria sukcesu" **determines** "Kontynuację lub eskalację".\n'
            '- "Log wykonania" **feeds** "Audyt i metryki operacyjne".'
        ),
    ),
    # === MONITORING ===
    (
        [
            "monitoring",
            "alerting",
            "observability",
            "dashb",
            "alert",
            "metryki systemowe",
            "metryki operacyjne",
        ],
        (
            "Definiuje co, jak i kiedy monitorować — metryki (RED: Rate, Errors, Duration; "
            "USE: Utilization, Saturation, Errors), progi alertów, kanały powiadomień, "
            "procedury eskalacji i dashboardy operacyjne."
        ),
        "SLA/SLO, architektura systemu, wymagania dostępności, poprzednie incydenty, narzędzia monitorowania (Prometheus, Grafana, Datadog).",
        "Zdefiniowane metryki i alerty z progami, konfiguracja dashboardów, macierz eskalacji, procedury on-call, raporty SLO compliance.",
        "Runbooki (triggered by alerts), raporty postmortem, plany pojemności, SLA reporting dla klientów.",
        "SLA/SLO, architektura systemu, plan zarządzania incydentami, polityki retencji logów.",
        (
            '"SLA/SLO" **defines** "Progi alertów".\n'
            '- "Alerty" **triggers** "Runbook lub eskalację".\n'
            '- "Historia alertów" **feeds** "Przegląd progów i tuning fałszywych alarmów".'
        ),
    ),
    # === CAPACITY PLANNING ===
    (
        ["capacity plan", "planowanie pojemności", "capacity management", "skalowanie", "scaling"],
        (
            "Prognozuje wzrost obciążenia i określa kiedy oraz jakie zasoby należy rozbudować, "
            "by utrzymać SLA. Zawiera: aktualne zużycie zasobów, modele wzrostu, progi alarmowe, "
            "plan rozbudowy i budżet."
        ),
        "Aktualne metryki wykorzystania (CPU, RAM, storage), prognozy biznesowe, koszty zasobów, harmonogram projektu.",
        "Plan rozbudowy infrastruktury z datami i kosztami, progi alarmowe, rekomendacje architektoniczne, budżet CapEx/OpEx.",
        "Wnioski zakupowe, plan budżetowy IT, konfiguracje auto-scalingu, plany DR.",
        "Metryki monitoringu, SLA/SLO, prognoza biznesowa, architektura systemu, analiza TCO.",
        (
            '"Trend wykorzystania zasobów" **drives** "Prognozę i datę rozbudowy".\n'
            '- "Progi alarmowe" **feeds** "Konfigurację monitoringu".\n'
            '- "Plan rozbudowy" **updates** "Budżet IT i plan zakupów".'
        ),
    ),
    # === SECURITY POLICY ===
    (
        [
            "security policy",
            "polityka bezpieczeństwa",
            "information security",
            "isms policy",
            "polityka dostępu",
            "access policy",
            "password policy",
        ],
        (
            "Ustanawia zasady, wymagania i odpowiedzialności w zakresie bezpieczeństwa informacji. "
            "Stanowi najwyższy dokument ISMS, z którego wynikają szczegółowe standardy i procedury. "
            "Każda zasada powinna zawierać: wymaganie, uzasadnienie i sposób egzekwowania."
        ),
        "Wymagania regulacyjne (ISO 27001, NIS2, GDPR), analiza ryzyk, wyniki audytów, incydenty (lessons learned), cel biznesowy.",
        "Zatwierdzona polityka z zakresem ISMS, role i odpowiedzialności (RACI), wytyczne do standardów i procedur, harmonogram przeglądów.",
        "Wszystkie standardy i procedury bezpieczeństwa (hierarchia polityk), szkolenia z bezpieczeństwa, audyty, plany reagowania na incydenty.",
        "Wymagania regulacyjne, analiza ryzyk organizacyjnych, zobowiązania kontraktowe, strategia IT.",
        (
            '"Cel i zakres ISMS" **constrains** "Wszystkie procedury bezpieczeństwa".\n'
            '- "Wymagania dotyczące ryzyka" **drives** "Dobór kontroli bezpieczeństwa".\n'
            '- "Incydenty i audyty" **feeds** "Przegląd i aktualizację polityki".'
        ),
    ),
    # === REJESTR RYZYK ===
    (
        [
            "risk register",
            "rejestr ryzyk",
            "risk assessment",
            "ocena ryzyk",
            "risk management",
            "risk log",
            "analiza ryzyka",
        ],
        (
            "Centralny rejestr zidentyfikowanych ryzyk z oceną (prawdopodobieństwo × wpływ = ryzyko inherentne), "
            "strategią mitigacji, właścicielem, ryzykiem rezydualnym i statusem. "
            "Stanowi podstawę do świadomych decyzji inwestycyjnych w kontrole."
        ),
        "Wyniki analizy zagrożeń (threat modeling), audyty, incydenty, zmiany systemów, wymagania regulacyjne, oceny dostawców.",
        "Macierz ryzyk (heat map), priorytety mitigacji, plan działań naprawczych z terminami i właścicielami, raport dla zarządu.",
        "Plan zarządzania incydentami (priorytety), plany testów bezpieczeństwa, decyzje o kontrolach, raportowanie do zarządu.",
        "Wyniki audytów, threat intelligence, BIA, architektura systemu, rejestry zmian.",
        (
            '"Prawdopodobieństwo i wpływ" **determines** "Priorytet mitigacji".\n'
            '- "Zaakceptowane ryzyka" **requires** "Formalną akceptację właściciela".\n'
            '- "Zrealizowane ryzyka" **triggers** "Aktualizację rejestru i analizę efektywności kontroli".'
        ),
    ),
    # === VULNERABILITY / PENTEST ===
    (
        [
            "vulnerability",
            "podatność",
            "cve",
            "pentest",
            "penetration test",
            "security scan",
            "security assessment",
            "hardening",
        ],
        (
            "Dokumentuje wyniki skanowania lub testu penetracyjnego — zidentyfikowane podatności "
            "(CVE, CVSS score), opis exploita, wpływ, dowody i zalecenia remediacji z priorytetami."
        ),
        "Wyniki skanera (Nessus, Qualys, Trivy), wyniki testu penetracyjnego, CVSS scores, polityki bezpieczeństwa, harmonogram patch management.",
        "Lista podatności z oceną ryzyka (CVSS), plan remediacji z priorytetami i terminami, rekomendacje konfiguracji, raport dla zarządu.",
        "Plan patch management, rejestr ryzyk (nowe pozycje), polityki hardening, wymagania do skanu weryfikacyjnego.",
        "Polityka zarządzania podatnościami, CMDB, SLA remediacji, wyniki poprzednich skanów.",
        (
            '"CVSS score" **determines** "Priorytet i termin remediacji".\n'
            '- "Znalezione podatności" **updates** "Rejestr ryzyk".\n'
            '- "Weryfikacja remediacji" **closes** "Pozycję rejestru podatności".'
        ),
    ),
    # === API ===
    (
        [
            "api",
            "openapi",
            "rest",
            "graphql",
            "asyncapi",
            "sdk",
            "endpoint",
            "swagger",
            "api reference",
            "api design",
            "api specification",
            "api documentation",
        ],
        (
            "Definiuje kontrakt interfejsu programistycznego — endpointy, metody HTTP, schematy "
            "żądań/odpowiedzi, kody błędów, autentykację, wersjonowanie i przykłady użycia. "
            "Stanowi źródło prawdy dla konsumentów i producentów API."
        ),
        "Wymagania funkcjonalne konsumentów API, model danych (schema), polityki bezpieczeństwa (OAuth2/JWT/API key), wymagania wydajności (rate limiting).",
        "Specyfikacja OpenAPI/AsyncAPI (machine-readable), dokumentacja developerska, sandbox/mock, changelog wersji API.",
        "Klienci API (SDK, integracje), testy kontraktowe, dokumentacja developerska, konfiguracje API gateway.",
        "Wymagania biznesowe, model danych, polityki bezpieczeństwa, architektura systemu, SLA wydajności.",
        (
            '"Schematy danych wejściowych/wyjściowych" **constrains** "Implementację klientów".\n'
            '- "Kody błędów" **drives** "Logikę obsługi błędów w klientach".\n'
            '- "Wersja API" **requires** "Strategię kompatybilności wstecznej".'
        ),
    ),
    # === MODEL DANYCH ===
    (
        [
            "data model",
            "model danych",
            "schema",
            "data dictionary",
            "słownik danych",
            "erd",
            "entity",
            "database schema",
            "schemat bazy danych",
        ],
        (
            "Opisuje strukturę danych — encje, atrybuty, typy, ograniczenia (constraints) i relacje. "
            "Stanowi kontrakt między zespołami (frontend, backend, BI/analytics) "
            "i podstawę do migracji schematów."
        ),
        "Wymagania funkcjonalne dot. danych, analiza procesów biznesowych, systemy źródłowe, wymagania GDPR (które pola to dane osobowe).",
        "Diagram ERD, słownik danych, skrypty DDL, macierz klasyfikacji danych (sensitivity), plan migracji schematu.",
        "Specyfikacje API (request/response schemas), skrypty migracji DB, dokumentacja integracji, polityki retencji, raporty BI.",
        "Wymagania biznesowe, analiza procesów, polityki ochrony danych (GDPR), architektura systemu.",
        (
            '"Encje i relacje" **constrains** "Schematy API i integracji".\n'
            '- "Klasyfikacja danych (sensitivity)" **drives** "Kontrole dostępu i szyfrowania".\n'
            '- "Zmiany schematu" **requires** "Skrypt migracji i plan rollback".'
        ),
    ),
    # === DEPLOYMENT / RELEASE ===
    (
        [
            "deployment",
            "wdrożenie",
            "release plan",
            "release notes",
            "deployment plan",
            "go-live",
            "rollout",
            "launch plan",
        ],
        (
            "Opisuje plan wdrożenia nowej wersji systemu — kroki, zależności, rollback plan, "
            "kryteria go/no-go, komunikację do interesariuszy i weryfikację post-deploy."
        ),
        "Specyfikacja release (changelog, scope zmian), wyniki testów QA, konfiguracja środowisk, okno zmian (change window), listy powiadomień.",
        "Zatwierdzone okno zmian (CAB), kroki wdrożeniowe z odpowiedzialnościami, plan rollback z kryteriami aktywacji, smoke tests, raport z wdrożenia.",
        "Rejestr zmian, metryki monitoringu post-deploy, plan komunikacji z użytkownikami, dokumentacja operacyjna.",
        "Raport z testów QA, polityka zarządzania zmianami (ITIL), harmonogram releaseów, konfiguracja CI/CD.",
        (
            '"Kryteria go/no-go" **gates** "Wdrożenie na produkcję".\n'
            '- "Rollback plan" **must precede** "Każdym krokiem wdrożenia".\n'
            '- "Post-deploy checks" **validates** "Sukces wdrożenia i zamknięcie change request".'
        ),
    ),
    # === SETUP / KONFIGURACJA ===
    (
        [
            "setup",
            "konfiguracja",
            "configuration guide",
            "installation",
            "instalacja",
            "getting started",
            "quick start",
            "environment setup",
        ],
        (
            "Przeprowadza przez proces instalacji, konfiguracji i pierwszego uruchomienia systemu lub narzędzia. "
            "Zawiera wymagania wstępne (prereqs), krok po kroku instrukcje z weryfikacją każdego etapu "
            "i typowe problemy (troubleshooting)."
        ),
        "Wymagania systemowe (hardware/software prereqs), dostępy i uprawnienia, pliki konfiguracyjne i secrets, dokumentacja zależności.",
        "Skonfigurowane i działające środowisko, log instalacji, lista przeprowadzonych weryfikacji, znane problemy i obejścia.",
        "Runbooki operacyjne, dokumentacja administracyjna, plany testów środowiska, onboarding nowych członków.",
        "Architektura systemu, polityki bezpieczeństwa (minimalne uprawnienia), specyfikacja wymagań sprzętowych/softwarowych.",
        (
            '"Prereqs i weryfikacja środowiska" **must precede** "Instalacją komponentów".\n'
            '- "Każdy krok" **requires** "Weryfikację powodzenia przed kontynuacją".\n'
            '- "Sekcja troubleshooting" **feeds** "Bazę wiedzy i FAQ operacyjne".'
        ),
    ),
    # === CHANGE MANAGEMENT ===
    (
        [
            "change request",
            "wniosek o zmianę",
            "change management",
            "formularz zgłoszenia zmiany",
            "ocena wpływu zmiany",
            "change control",
            "change log",
        ],
        (
            "Formalny wniosek o zmianę w systemie lub procesie — opis zmiany, uzasadnienie biznesowe, "
            "analiza wpływu (techniczny, operacyjny, bezpieczeństwo), plan wdrożenia, plan rollback i ocena ryzyka."
        ),
        "Opis problemu lub potrzeby biznesowej, analiza wpływu na powiązane systemy, wyniki testów w środowisku niższym, szacowanie pracochłonności.",
        "Zatwierdzony lub odrzucony wniosek zmiany (z uzasadnieniem CAB), plan wdrożenia zmiany, zaktualizowana dokumentacja.",
        "Harmonogram wdrożenia (change window), plan testów regresji, aktualizacje CMDB, powiadomienia dla użytkowników.",
        "Zgłoszenie incydentu lub wymagania nowej funkcjonalności, polityka zarządzania zmianami, harmonogram releaseów.",
        (
            '"Analiza wpływu" **determines** "Kategorię zmiany (standard/normal/emergency)".\n'
            '- "Ocena ryzyka" **drives** "Wymaganą ścieżkę akceptacji (CAB)".\n'
            '- "Plan rollback" **must exist** "Przed zatwierdzeniem każdej zmiany produkcyjnej".'
        ),
    ),
    # === AUDIT / COMPLIANCE ===
    (
        ["audit", "audyt", "compliance check", "kontrola jakości", "review", "przegląd"],
        (
            "Dokumentuje wyniki audytu lub przeglądu — zakres, metody, dowody, odchylenia od wymagań "
            "(nonconformities) i rekomendacje naprawcze (CAPA). "
            "Każde odchylenie powinno mieć właściciela, termin i plan korekcyjny."
        ),
        "Plan audytu, wymagania standardu (ISO 27001, GDPR, NIS2), polityki i procedury wewnętrzne, wyniki poprzednich audytów, dowody.",
        "Raport z audytu, lista odchyleń z klasyfikacją (major/minor), plan CAPA z terminami, certyfikat lub potwierdzenie zgodności.",
        "Plan CAPA (Corrective and Preventive Actions), aktualizacje polityk i procedur, rejestr ryzyk, raport dla zarządu.",
        "Polityki i procedury wewnętrzne, wymagania standardu, poprzednie raporty audytów i statusy CAPA.",
        (
            '"Zakres audytu" **determines** "Dobór dowodów i technik".\n'
            '- "Odchylenia" **requires** "Plan CAPA z właścicielem i terminem".\n'
            '- "Status CAPA" **feeds** "Kolejny audyt follow-up".'
        ),
    ),
    # === SLA / KPI / METRYKI ===
    (
        [
            "sla",
            "ola",
            "service level",
            "poziom usług",
            "kpi",
            "metryki jakości",
            "performance metrics",
            "scorecard",
            "dashboard kpi",
        ],
        (
            "Definiuje mierzalne cele poziomu usług — dostępność, czas odpowiedzi, throughput, "
            "czas rozwiązania incydentów i konsekwencje niespełnienia (penaly, eskalacje). "
            "Stanowi podstawę do pomiaru jakości usług."
        ),
        "Wymagania biznesowe dot. dostępności, dane historyczne o wydajności, możliwości techniczne systemu, wymagania kontraktowe.",
        "Zdefiniowane SLA/OLA z progami i metodami pomiaru, macierz eskalacji przy naruszeniu, raport compliance z SLA, harmonogram przeglądów.",
        "Konfiguracja monitoringu (alerty na progi SLA), raporty dla klientów, plany pojemności, procesy rozliczania kontraktów.",
        "Wymagania klientów, architektura systemu (co możliwe technicznie), historyczne metryki, polityki zarządzania incydentami.",
        (
            '"Progi SLA" **defines** "Alerty monitoringu".\n'
            '- "Naruszenie SLA" **triggers** "Eskalację i analizę przyczyn".\n'
            '- "Raport compliance SLA" **feeds** "Przeglądy kontraktowe i relacje z klientami".'
        ),
    ),
    # === COST BENEFIT / TCO ===
    (
        [
            "cost benefit",
            "koszty i korzyści",
            "analiza kosztów",
            "tco",
            "total cost",
            "roi",
            "cba",
            "analiza finansowa",
            "budżet",
            "planowanie wydatków",
        ],
        (
            "Porównuje koszty i korzyści decyzji inwestycyjnej w horyzoncie 3–5 lat. "
            "Zawiera: koszty jednorazowe i operacyjne, kwantyfikację korzyści (oszczędności, przychody, "
            "ryzyko uniknięte), NPV/IRR/payback period i rekomendację."
        ),
        "Warianty architektury lub zakupu, cenniki vendorów, stawki pracownicze, wolumeny biznesowe, wymagania compliance, horyzont analizy.",
        "Porównanie TCO per wariant, NPV i payback period, analiza wrażliwości na założenia, ryzyko i mitigacje, rekomendacja z uzasadnieniem.",
        "Decyzja inwestycyjna (make/buy/partner), plan projektu (budżet), negocjacje z vendorami, zarządzanie ryzykiem finansowym.",
        "Cele strategiczne i biznesowe, wymagania funkcjonalne i NFR, cenniki i kontrakty, dane historyczne kosztów.",
        (
            '"Struktura kosztów" **must align with** "Modelem budżetowania (CapEx vs OpEx)".\n'
            '- "Analiza wrażliwości" **quantifies** "Ryzyko finansowe decyzji".\n'
            '- "Rekomendacja" **drives** "Decyzję architektoniczną i wybór vendora".'
        ),
    ),
    # === SZKOLENIA / ONBOARDING ===
    (
        ["training", "szkolenie", "onboarding", "learning", "kompetencje", "certification", "kurs"],
        (
            "Opisuje program szkoleniowy — cel (jaka luka kompetencyjna jest adresowana), treść, "
            "format (e-learning/classroom/hands-on), odbiorców, harmonogram, materiały "
            "i sposób weryfikacji skuteczności (test/certyfikat)."
        ),
        "Analiza luk kompetencyjnych (skill gap analysis), wymagania projektu/organizacji, dostępność uczestników, budżet szkoleniowy, materiały.",
        "Plan szkolenia z harmonogramem i listą uczestników, materiały szkoleniowe, testy weryfikacji wiedzy, certyfikaty, raport z realizacji.",
        "Macierz kompetencji zespołu, plany rekrutacji, plany projektów, audyty zgodności (dowód competence dla ISO 9001).",
        "Analiza wymagań projektu, macierz ról, wymagania certyfikacyjne (ISO 27001/PCI-DSS/GDPR), feedback z poprzednich szkoleń.",
        (
            '"Zidentyfikowane luki kompetencyjne" **drives** "Dobór treści i formatu szkolenia".\n'
            '- "Wyniki testu weryfikacyjnego" **feeds** "Macierz kompetencji i plany sukcesji".\n'
            '- "Certyfikaty ukończenia" **serves as** "Dowód zgodności dla audytów ISO 9001 kl.7.2".'
        ),
    ),
    # === AI/ML ===
    (
        [
            "machine learning",
            "ml model",
            "ai model",
            "neural",
            "llm",
            "generative ai",
            "genai",
            "bias",
            "fairness",
            "algorithm",
            "model card",
            "adversarial",
            "recommendation engine",
        ],
        (
            "Dokumentuje cykl życia modelu AI/ML — cel (problem biznesowy), zbiór danych (provenance, split), "
            "architekturę modelu, metryki jakości (accuracy, F1, AUC), analizę biasu/fairness, "
            "procedury re-treningu i wycofania."
        ),
        "Definicja problemu biznesowego, dane treningowe z metadanymi (provenance, licencje), wymagania dot. biasu i fairness (AI Act/ISO 42001), metryki sukcesu.",
        "Wytrenowany i walidowany model (artefakt), karta modelu (model card), raport z analizy biasu, procedury re-treningu, plan monitoringu dryfu.",
        "Systemy produkcyjne (wdrożenie modelu), dashboardy monitoringu modelu, plany walidacji, raporty zgodności (EU AI Act, ISO 42001).",
        "Dane treningowe i ich dokumentacja, wymagania regulacyjne (AI Act risk tier), wymagania biznesowe, infrastruktura MLOps.",
        (
            '"Jakość i reprezentatywność danych" **determines** "Wydajność i bias modelu".\n'
            '- "Metryki walidacyjne" **gates** "Wdrożenie na produkcję".\n'
            '- "Monitoring dryfu" **triggers** "Re-trening lub wycofanie modelu".'
        ),
    ),
    # === INTEGRACJE ===
    (
        [
            "integration",
            "integracja",
            "middleware",
            "event",
            "messaging",
            "kafka",
            "rabbitmq",
            "webhook",
            "event-driven",
            "microservice",
            "service mesh",
        ],
        (
            "Definiuje kontrakt integracyjny między systemami — przepływ danych, format komunikatów, "
            "protokół (REST/AMQP/Kafka), topologię (sync/async/event-driven), "
            "obsługę błędów i idempotentność."
        ),
        "Wymagania biznesowe dot. przepływu danych, schematy systemów źródłowych i docelowych, SLA wydajności, polityki bezpieczeństwa.",
        "Specyfikacja kontraktu integracyjnego, schematy komunikatów (Avro/JSON Schema/Protobuf), diagram DFD, plan testów integracyjnych.",
        "Konfiguracja message broker (Kafka topics, queues), testy kontraktowe, monitorowanie opóźnień i błędów, dokumentacja operacyjna.",
        "Modele danych systemów, wymagania biznesowe, SLA, polityki bezpieczeństwa.",
        (
            '"Schemat komunikatu" **constrains** "Implementację producenta i konsumenta".\n'
            '- "Obsługa błędów i DLQ" **determines** "Niezawodność integracji".\n'
            '- "Monitorowanie opóźnień" **feeds** "Alerty SLA i diagnozę bottlenecków".'
        ),
    ),
    # === SCRUM / AGILE ===
    (
        [
            "sprint",
            "retrospective",
            "retrospektywa",
            "velocity",
            "burndown",
            "burnup",
            "sprint review",
        ],
        (
            "Podsumowuje sprint lub retrospektywę — co poszło dobrze, co wymaga poprawy, "
            "action items z właścicielami i terminami oraz metryki sprintu (velocity, burndown, defect rate)."
        ),
        "Ukończone i nieukończone stories sprintu, feedback zespołu (Start/Stop/Continue lub 4Ls), metryki poprzednich sprintów.",
        "Lista action items z właścicielami i terminami, zaktualizowana velocity i prognoza release, wnioski do kolejnego planowania.",
        "Planowanie kolejnego sprintu, backlog refinement, raportowanie postępu projektu, metryki jakości zespołu.",
        "Definicja ukończenia (DoD), backlog produktu, metryki poprzednich sprintów, alokacje zasobów.",
        (
            '"Zidentyfikowane przeszkody" **requires** "Action item z właścicielem i terminem".\n'
            '- "Velocity" **feeds** "Prognozę daty zakończenia i planowanie pojemności".\n'
            '- "Action items" **updates** "Team improvement backlog".'
        ),
    ),
    (
        [
            "backlog",
            "product backlog",
            "epic",
            "feature",
            "priorytetyzacja",
            "prioritization",
            "product roadmap",
        ],
        (
            "Zawiera uporządkowaną listę epików i stories do realizacji — z opisem wartości biznesowej, "
            "priorytetem (MoSCoW/WSJF), kryterium akceptacji i szacunkiem rozmiaru. "
            "Stanowi jedyne źródło prawdy o zakresie produktu."
        ),
        "Wizja produktu, cele biznesowe i OKR, feedback użytkowników, wyniki sprintów, techniczny dług (tech debt).",
        "Priorytyzowany backlog gotowy do planowania sprintu, kryteria DoR dla top stories, roadmapa releaseów, raport postępu.",
        "Planowanie sprintu, komunikacja z interesariuszami (roadmapa), szacowania budżetowe, plany testów akceptacyjnych.",
        "Wizja produktu, OKR/KPI, feedback z retrospektyw, wyniki testów użyteczności, analiza konkurencji.",
        (
            '"Priorytet biznesowy" **determines** "Kolejność realizacji w sprintach".\n'
            '- "Kryteria DoR" **gates** "Wejście story do sprintu".\n'
            '- "Velocity zespołu" **calibrates** "Realność roadmapy releaseów".'
        ),
    ),
    # === VENDOR / CONTRACT ===
    (
        [
            "vendor",
            "dostawc",
            "supplier",
            "contract",
            "umowa",
            "rfp",
            "rfi",
            "rfc",
            "przetarg",
            "oferta",
        ],
        (
            "Dokumentuje wymagania wobec dostawcy, warunki kontraktowe lub wyniki oceny ofert. "
            "Zawiera: kryteria oceny (techniczne, finansowe, compliance), wymagania SLA, "
            "klauzule bezpieczeństwa i warunki zakończenia współpracy."
        ),
        "Wymagania biznesowe i techniczne, polityki zarządzania dostawcami (ISO 27001 A.15), budżet, harmonogram wyboru, lista kandydatów.",
        "Zatwierdzona umowa lub ocena dostawcy z uzasadnieniem, SLA/OLA z dostawcą, plan onboardingu dostawcy, rejestr dostawców.",
        "Rejestr dostawców (vendor register), plany audytów dostawców, plany zarządzania ryzykiem łańcucha dostaw, raporty compliance.",
        "Polityka zarządzania dostawcami, wymagania bezpieczeństwa informacji, standardy regulacyjne (GDPR, NIS2), budżet IT.",
        (
            '"Kryteria oceny" **determines** "Ranking ofert i wybór dostawcy".\n'
            '- "SLA z dostawcą" **feeds** "Konfigurację monitoringu i eskalacji".\n'
            '- "Audyty dostawcy" **updates** "Rejestr ryzyk łańcucha dostaw".'
        ),
    ),
    # === LOG / REJESTR / AUDIT TRAIL ===
    (
        [
            "log",
            "rejestr",
            "audit trail",
            "audit log",
            "ścieżka audytowa",
            "event log",
            "activity log",
        ],
        (
            "Zawiera format i wymagania dla rejestru zdarzeń/operacji — co jest logowane, "
            "przez kogo, w jakim formacie, przez jaki czas przechowywane i jak chronione przed modyfikacją. "
            "Kluczowy element dowodowy dla audytów bezpieczeństwa."
        ),
        "Polityki bezpieczeństwa (ISO 27001 A.12.4), wymagania regulacyjne (GDPR, NIS2 art.21), retencja danych, wymagania SIEM.",
        "Schemat logu z wymaganymi polami (timestamp, actor, action, resource, outcome), polityka retencji, konfiguracja SIEM/log aggregation.",
        "SIEM (alerty na anomalie), raporty audytów, śledztwa incydentów, dowody compliance dla regulatora.",
        "Polityka bezpieczeństwa informacji, wymagania regulacyjne, architektura systemu (co generuje zdarzenia), polityki dostępu.",
        (
            '"Wymagane pola logu" **constrains** "Konfigurację systemów generujących zdarzenia".\n'
            '- "Retencja i ochrona" **ensures** "Integralność dowodów audytowych".\n'
            '- "Agregacja w SIEM" **enables** "Wykrywanie anomalii i korelację zdarzeń".'
        ),
    ),
    # === ANALIZA ===
    (
        ["analiza", "analysis", "assessment", "ocena", "badanie", "analityka"],
        (
            "Zawiera wyniki systematycznej analizy — metodologię, dane źródłowe, znaleziska, "
            "wnioski i rekomendacje. Każdy wniosek powinien być poparty danymi i zawierać "
            "propozycję działań z priorytetami."
        ),
        "Zakres analizy i pytania badawcze, dane źródłowe (metryki, logi, wywiady, obserwacje), kryteria oceny, benchmarki branżowe.",
        "Raport z analizy z uzasadnionymi wnioskami, macierz priorytetów rekomendacji, plan działań, wizualizacje danych.",
        "Plany naprawcze i improvement initiatives, aktualizacje polityk i procesów, raporty zarządcze, decyzje inwestycyjne.",
        "Dane operacyjne i metryki, poprzednie analizy, wymagania regulacyjne, cel strategiczny analizy.",
        (
            '"Dane źródłowe" **determines** "Jakość i pewność wniosków".\n'
            '- "Rekomendacje" **drives** "Plan działań z priorytetami".\n'
            '- "Wnioski analizy" **feeds** "Decyzje strategiczne i aktualizacje rejestrów".'
        ),
    ),
    # === DOKUMENTACJA / GUIDE ===
    (
        [
            "guide",
            "documentation",
            "developer guide",
            "user guide",
            "technical guide",
            "best practices",
            "wytyczne",
            "przewodnik",
            "instrukcja",
            "handbook",
        ],
        (
            "Dostarcza kompleksowej dokumentacji lub wytycznych dla określonej grupy odbiorców. "
            "Zawiera: kontekst i cel, kroki lub zasady, przykłady użycia i typowe problemy (FAQ). "
            "Powinien być utrzymywany aktualnym i powiązanym z kodem/systemem."
        ),
        "Zakres tematyczny, docelowi odbiorcy i ich poziom wiedzy, kod/system/proces do udokumentowania, polityki i standardy.",
        "Kompletna dokumentacja z przykładami, sekcja FAQ/troubleshooting, changelog aktualizacji, feedback od użytkowników.",
        "Onboarding nowych członków zespołu/użytkowników, plany szkoleń, baza wiedzy, portale developerskie.",
        "Specyfikacja systemu/procesu, feedback od użytkowników, polityki i standardy, poprzednia wersja dokumentacji.",
        (
            '"Cel i odbiorcy" **constrains** "Poziom szczegółowości i język techniczny".\n'
            '- "Przykłady użycia" **reduces** "Pytania do supportu i czas onboardingu".\n'
            '- "Changelog" **enables** "Śledzenie ewolucji dokumentacji względem systemu".'
        ),
    ),
    # === FALLBACK ===
    (
        [],  # zawsze pasuje jako ostatni
        (
            "Opisuje cel, zakres i zastosowanie tego dokumentu w kontekście procesu lub systemu IT. "
            "Zawiera: definicję problemu lub potrzeby biznesowej adresowanej przez ten dokument, "
            "kluczowe decyzje które wspiera, ryzyka które ogranicza "
            "i wartość dostarczaną interesariuszom."
        ),
        "Cele biznesowe i wymagania projektu, istniejące dokumenty powiązane, wymagania standardów i regulacji, ograniczenia i założenia środowiskowe.",
        "Zatwierdzona wersja dokumentu z kompletnymi sekcjami, lista otwartych pytań i decyzji do podjęcia, action items z właścicielami i terminami.",
        "Dokumenty powiązane (downstream): plany realizacji, specyfikacje techniczne, raporty i rejestry wynikające z decyzji tego dokumentu.",
        "Dokumenty wejściowe (upstream): wymagania, polityki, standardy, wyniki analiz będące podstawą dla treści tego dokumentu.",
        (
            '"Cel i zakres" **constrains** "Wszystkie pozostałe sekcje dokumentu".\n'
            '- "Wejścia" **must be available** "Przed wypełnieniem sekcji merytorycznych".\n'
            '- "Decyzje i uzasadnienia" **feeds** "Downstream documents i rejestry zmian".'
        ),
    ),
]


def find_archetype(title: str, content: str):
    tl = title.lower()
    cl = content.lower()
    # Dla placeholderow: najpierw samo dopasowanie tytulu
    for row in ARCHETYPES[:-1]:
        kws = row[0]
        if any(k in tl for k in kws):
            return row[1:]
    # Jezeli tytul nie pasuje, sprawdz tez tresc (nie-generyczna)
    if PLACEHOLDER not in content:
        for row in ARCHETYPES[:-1]:
            kws = row[0]
            if any(k in cl for k in kws):
                return row[1:]
    return ARCHETYPES[-1][1:]


def enrich_content(title: str, content: str, standard: str, parent_title: str = "") -> str:
    cel, wej, wyj, wplyw, zalezny, sekcje = find_archetype(title, content)

    std_blok = f"\nTen szablon jest zgodny ze standardem **{standard}**." if standard else ""
    parent_note = (
        f'\n\n> Dokument satelitarny do: "{parent_title}" - rozszerza lub uszczegolawia jego tresc.'
        if parent_title
        else ""
    )

    new_cel = f"{title} — szablon dokumentu IT.\n\n{cel}{std_blok}{parent_note}"

    new_wej_wyj = (
        f"- **Wejścia** (co musi być dostępne przed wypełnieniem): {wej}\n"
        f"- **Wyjścia** (co dokument wytwarza jako rezultat): {wyj}"
    )

    new_zal = (
        f"- **Wpływa na** (downstream — co zależy od tego dokumentu): {wplyw}\n"
        f"- **Zależy od** (upstream — co musi istnieć przed tym dokumentem): {zalezny}"
    )

    new_sekcje = f"- {sekcje}"

    # Zamień placeholder w Cel dokumentu
    content = re.sub(
        r"(## Cel dokumentu\s*\n\n?)([^\n].*?" + re.escape(PLACEHOLDER) + r".*?\n)",
        r"\g<1>" + new_cel + "\n",
        content,
        flags=re.DOTALL,
    )

    # Zamień Wejścia i wyjścia
    content = re.sub(
        r"(## Wejścia i wyjścia\s*\n\n?)(- Wejścia:.*?\n- Wyjścia:.*?\n)",
        r"\g<1>" + new_wej_wyj + "\n",
        content,
        flags=re.DOTALL,
    )

    # Zamień Zależności dokumentu
    content = re.sub(
        r"(## Zależności dokumentu\s*\n\n?)(- Upstream:.*?\n- Downstream:.*?\n- Zewnętrzne:.*?\n)",
        r"\g<1>" + new_zal + "\n",
        content,
        flags=re.DOTALL,
    )

    # Zamień Powiązania sekcja↔sekcja
    content = re.sub(
        r"(## Powiązania sekcja↔sekcja\s*\n\n?)(- Wymagania →.*?\n- Ryzyka.*?\n\n)",
        r"\g<1>" + new_sekcje + "\n\n",
        content,
        flags=re.DOTALL,
    )

    return content


def main():
    parser = argparse.ArgumentParser(
        description="Wzbogacaj placeholder szablony o semantyczne opisy"
    )
    parser.add_argument(
        "--dry-run", action="store_true", help="Pokaż co zostałoby zmienione (bez zapisu)"
    )
    parser.add_argument(
        "--limit", type=int, default=0, help="Przetwórz max N dokumentów (0=wszystkie)"
    )
    parser.add_argument("--path-filter", default="", help="Filtruj ścieżki zawierające podciąg")
    args = parser.parse_args()

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    rows = conn.execute("""
        SELECT d.path, d.title,
               m.standard_code,
               s.parent_path,
               pd.title as parent_title
        FROM docs d
        LEFT JOIN doc_standard_mapping m ON d.path = m.doc_path
        LEFT JOIN doc_satellites s ON d.path = s.satellite_path
        LEFT JOIN docs pd ON pd.path = s.parent_path
        WHERE m.standard_code IS NOT NULL OR s.parent_path IS NOT NULL
        GROUP BY d.path
        ORDER BY d.path
    """).fetchall()

    processed = enriched = errors = 0

    for row in rows:
        if args.path_filter and args.path_filter not in row["path"]:
            continue

        fpath = TDIR / row["path"]
        if not fpath.exists():
            continue

        try:
            content = fpath.read_text(encoding="utf-8", errors="replace")
        except Exception:
            errors += 1
            continue

        if PLACEHOLDER not in content:
            processed += 1
            continue

        new_content = enrich_content(
            row["title"] or "", content, row["standard_code"] or "", row["parent_title"] or ""
        )

        if new_content == content:
            processed += 1
            continue

        if args.dry_run:
            print(f"  [DRY] {row['path']}")
        else:
            try:
                fpath.write_text(new_content, encoding="utf-8")
                enriched += 1
            except Exception as e:
                print(f"  [ERR] {row['path']}: {e}", file=sys.stderr)
                errors += 1

        processed += 1
        if args.limit and enriched >= args.limit:
            break

    conn.close()
    print(f"\nPrzetworzone: {processed}  |  Wzbogacone: {enriched}  |  Błędy: {errors}")


if __name__ == "__main__":
    main()
