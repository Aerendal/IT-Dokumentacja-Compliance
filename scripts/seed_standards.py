#!/usr/bin/env python3
"""
seed_standards.py
Wypelnia tabele `standards` i `compliance_regulations` w it_doc_matrix.db.

Standardy miedzynarodowe: ISO/IEC, IEEE, ITIL, TOGAF, PMBOK, COBIT, DORA, NIS2, OWASP, PCI DSS i inne.
Polskie regulacje: ustawy, normy PN, wytyczne krajowe.

Jezyk opisow: polski. Nazwy wlasne standardow pozostaja w oryginale.
"""

import sqlite3
import sys
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "reports" / "it_doc_matrix.db"

# ---------------------------------------------------------------------------
# STANDARDY MIEDZYNARODOWE
# Schemat: standard_id (auto), standard_code, standard_name (PL), standard_name_en,
#          version, description, applicable_industries, url
# ---------------------------------------------------------------------------
INTERNATIONAL_STANDARDS = [
    # --- ISO/IEC: Bezpieczenstwo informacji ---
    (
        "ISO/IEC 27001",
        "System Zarządzania Bezpieczeństwem Informacji (ISMS)",
        "Information Security Management Systems",
        "2022",
        "Określa wymagania dotyczące ustanowienia, wdrożenia, utrzymania i ciągłego doskonalenia systemu zarządzania bezpieczeństwem informacji (ISMS). Podstawa certyfikacji bezpieczeństwa IT.",
        "IT,Finanse,Zdrowie,Administracja,Telekomunikacja",
        "https://www.iso.org/standard/27001",
    ),
    (
        "ISO/IEC 27002",
        "Wytyczne Praktyk Bezpieczeństwa Informacji",
        "Information Security Controls",
        "2022",
        "Katalog 93 mechanizmów kontrolnych bezpieczeństwa informacji podzielonych na 4 tematy: organizacyjne, osobowe, fizyczne, technologiczne. Uzupełnienie ISO 27001.",
        "IT,Finanse,Zdrowie,Administracja",
        "https://www.iso.org/standard/75652",
    ),
    (
        "ISO/IEC 27005",
        "Zarządzanie Ryzykiem Bezpieczeństwa Informacji",
        "Information Security Risk Management",
        "2022",
        "Wytyczne dotyczące zarządzania ryzykiem bezpieczeństwa informacji. Opisuje proces identyfikacji, analizy, oceny i leczenia ryzyk. Powiązany z ISO 27001 klauzula 6.1.",
        "IT,Finanse,Zdrowie",
        "https://www.iso.org/standard/80585",
    ),
    (
        "ISO/IEC 27017",
        "Bezpieczeństwo w Chmurze Obliczeniowej",
        "Security for Cloud Services",
        "2015",
        "Wytyczne kontroli bezpieczeństwa dla usług chmurowych. Rozszerza ISO 27002 o specyficzne aspekty chmury: role dostawcy i klienta, wirtualizacja, monitorowanie.",
        "IT,Chmura",
        "https://www.iso.org/standard/43757",
    ),
    (
        "ISO/IEC 27018",
        "Ochrona Danych Osobowych w Chmurze (PII)",
        "Protection of PII in Public Clouds",
        "2019",
        "Wytyczne ochrony danych osobowych (PII) przetwarzanych przez publicznych dostawców chmury. Uzupełnienie ISO 27001/27002 w kontekście RODO.",
        "IT,Chmura,Finanse",
        "https://www.iso.org/standard/76559",
    ),
    (
        "ISO/IEC 27701",
        "Zarządzanie Informacjami o Prywatności (PIMS)",
        "Privacy Information Management",
        "2019",
        "Rozszerzenie ISO 27001/27002 o zarządzanie prywatnością danych (PIMS). Mapowanie na RODO i inne przepisy o ochronie prywatności. Certyfikowalny standard.",
        "IT,Finanse,Zdrowie,Administracja",
        "https://www.iso.org/standard/71670",
    ),
    (
        "ISO/IEC 27035",
        "Zarządzanie Incydentami Bezpieczeństwa Informacji",
        "Information Security Incident Management",
        "2023",
        "Opisuje proces zarządzania incydentami bezpieczeństwa: przygotowanie, wykrywanie, zgłaszanie, ocena, reakcja i wyciąganie wniosków.",
        "IT,Finanse,Zdrowie",
        "https://www.iso.org/standard/74007",
    ),
    # --- ISO/IEC: Jakosc oprogramowania ---
    (
        "ISO/IEC 25010",
        "Model Jakości Systemu i Oprogramowania (SQuaRE)",
        "System and Software Quality Models",
        "2023",
        "Definiuje model jakości oprogramowania i systemów z 8 charakterystykami (funkcjonalność, niezawodność, wydajność, bezpieczeństwo, kompatybilność, użyteczność, utrzymywalność, przenaszalność) i 39 podcharakterystykami.",
        "IT,Inzynieria oprogramowania",
        "https://www.iso.org/standard/78176",
    ),
    (
        "ISO/IEC 25040",
        "Proces Oceny Jakości Produktu",
        "Evaluation Process",
        "2011",
        "Definiuje wymagania i wytyczne dla procesu oceny jakości produktu oprogramowania i systemów. Część serii SQuaRE.",
        "IT,QA",
        "https://www.iso.org/standard/35765",
    ),
    # --- ISO/IEC: Inzynieria systemow i oprogramowania ---
    (
        "ISO/IEC 12207",
        "Procesy Cyklu Życia Oprogramowania",
        "Software Life Cycle Processes",
        "2017",
        "Ustanawia wspólny framework procesów cyklu życia oprogramowania: akwizycja, dostarczanie, wytwarzanie, eksploatacja, utrzymanie. Podstawa dla SDLC.",
        "IT,Inzynieria oprogramowania",
        "https://www.iso.org/standard/63712",
    ),
    (
        "ISO/IEC 15288",
        "Procesy Cyklu Życia Systemów",
        "System Life Cycle Processes",
        "2023",
        "Framework procesów dla inżynierii systemów obejmujący cały cykl życia systemu od koncepcji do wycofania. Stosowany w systemach złożonych i krytycznych.",
        "IT,Systemy wbudowane,Obronnosc",
        "https://www.iso.org/standard/82426",
    ),
    (
        "ISO/IEC 29110",
        "Profile Cyklu Życia dla Małych Jednostek",
        "Life Cycle Profiles for VSEs",
        "2016",
        "Normy dla bardzo małych organizacji (VSE, do 25 osób) dotyczące procesów inżynierii oprogramowania i systemów. Profil podstawowy i zaawansowany.",
        "IT,MMP,Startupy",
        "https://www.iso.org/standard/62711",
    ),
    (
        "ISO/IEC 42001",
        "System Zarządzania Sztuczną Inteligencją (AIMS)",
        "AI Management Systems",
        "2023",
        "Wymagania dla systemu zarządzania AI w organizacjach tworzących lub wdrażających AI. Analogia ISO 27001 dla sztucznej inteligencji. Certyfikowalny.",
        "IT,AI/ML,Finanse,Zdrowie",
        "https://www.iso.org/standard/81230",
    ),
    # --- ISO: Jakosc i zarzadzanie ---
    (
        "ISO 9001",
        "System Zarządzania Jakością (QMS)",
        "Quality Management Systems",
        "2015",
        "Określa wymagania dla systemu zarządzania jakością. Stosowany w każdej organizacji niezależnie od branży. Podstawa procesów wytwarzania i doskonalenia.",
        "Wszystkie branże",
        "https://www.iso.org/standard/62085",
    ),
    (
        "ISO 20000-1",
        "System Zarządzania Usługami IT (SMS)",
        "IT Service Management",
        "2018",
        "Wymagania dla systemu zarządzania usługami IT (SMS). Pokrywa planowanie, projektowanie, przejście, dostarczanie i doskonalenie usług IT. Podstawa certyfikacji ITSM.",
        "IT,Telekomunikacja",
        "https://www.iso.org/standard/70636",
    ),
    # --- IEEE ---
    (
        "IEEE 829",
        "Dokumentacja Testowania Oprogramowania i Systemów",
        "Software and System Test Documentation",
        "2008",
        "Standard definiujący treść i format dokumentów testowych: plan testów, specyfikacja przypadków testowych, raporty z testów. Szeroko stosowany w QA.",
        "IT,QA,Inzynieria oprogramowania",
        "https://standards.ieee.org/ieee/829",
    ),
    (
        "IEEE 830",
        "Zalecana Praktyka dla Specyfikacji Wymagań Oprogramowania (SRS)",
        "Recommended Practice for SRS",
        "1998",
        "Definiuje strukturę i zawartość dokumentu SRS (Software Requirements Specification). Podstawa dokumentacji wymagań. Zastąpiony częściowo przez ISO 29148.",
        "IT,Inzynieria oprogramowania",
        "https://standards.ieee.org/ieee/830",
    ),
    (
        "IEEE 1016",
        "Standard dla Opisów Projektowania Oprogramowania (SDD)",
        "Software Design Descriptions",
        "2009",
        "Określa wymagania dla dokumentów opisujących projekt oprogramowania (SDD). Obejmuje architekturę, komponenty, interfejsy i interakcje.",
        "IT,Architektura",
        "https://standards.ieee.org/ieee/1016",
    ),
    (
        "IEEE 1012",
        "Standard Weryfikacji i Walidacji Oprogramowania i Systemów",
        "System, Software, and Hardware V&V",
        "2016",
        "Wymagania dla procesów weryfikacji i walidacji (V&V) oprogramowania, systemów i sprzętu. Stosowany w systemach krytycznych bezpieczeństwa.",
        "IT,QA,Systemy krytyczne",
        "https://standards.ieee.org/ieee/1012",
    ),
    (
        "IEEE 42010",
        "Opis Architektoniczny Systemów i Oprogramowania",
        "Architecture Description",
        "2011",
        "Definiuje terminologię i wymagania dla tworzenia, analizy i utrzymania opisów architektonicznych systemów. Podstawa dokumentacji architekturalnej.",
        "IT,Architektura",
        "https://standards.ieee.org/ieee/42010",
    ),
    # --- Frameworki IT ---
    (
        "ITIL 4",
        "Biblioteka Infrastruktury IT (Zarządzanie Usługami)",
        "IT Infrastructure Library v4",
        "2019",
        "Framework najlepszych praktyk zarządzania usługami IT (ITSM). Obejmuje system wartości usług (SVS), łańcuch wartości usług i 34 praktyki ITSM. Podstawa dla ITSM i ServiceDesk.",
        "IT,Telekomunikacja,Finanse",
        "https://www.axelos.com/certifications/itil-service-management",
    ),
    (
        "TOGAF ADM",
        "Framework Architektury Korporacyjnej (The Open Group)",
        "The Open Group Architecture Framework",
        "10",
        "Framework architektury korporacyjnej definiujący metodę ADM (Architecture Development Method) z fazami A–H. Stosowany do planowania i zarządzania architekturą EA.",
        "IT,Architektura,Finanse,Administracja",
        "https://www.opengroup.org/togaf",
    ),
    (
        "PMBOK 7",
        "Przewodnik po Zarządzaniu Projektami (PMI)",
        "Project Management Body of Knowledge",
        "7",
        "Standard zarządzania projektami PMI obejmujący 12 zasad, 8 domen wydajności i modele/metody/artefakty. Edycja 7 kładzie nacisk na wyniki i zwinność.",
        "Wszystkie branże",
        "https://www.pmi.org/pmbok-guide-standards/foundational/pmbok",
    ),
    (
        "COBIT 2019",
        "Kontrola nad Informacją i Technologiami (ISACA)",
        "Control Objectives for Information and Related Technologies",
        "2019",
        "Framework ładu i zarządzania IT (EGIT) zawierający 40 celów zarządzania i governance. Łączy cele biznesowe z procesami IT i mechanizmami kontrolnymi.",
        "IT,Finanse,Administracja",
        "https://www.isaca.org/resources/cobit",
    ),
    (
        "DORA",
        "Ustawa o Cyfrowej Odporności Operacyjnej (UE)",
        "Digital Operational Resilience Act",
        "2022",
        "Rozporządzenie UE 2022/2554 wymagające od podmiotów sektora finansowego UE zarządzania ryzykiem ICT, zgłaszania incydentów, testów odporności i nadzoru nad dostawcami ICT. Stosowanie od 17.01.2025.",
        "Finanse,IT,Ubezpieczenia",
        "https://eur-lex.europa.eu/legal-content/PL/TXT/?uri=CELEX:32022R2554",
    ),
    (
        "NIS2",
        "Dyrektywa w sprawie Bezpieczeństwa Sieci i Systemów Informacyjnych (UE)",
        "Network and Information Security Directive 2",
        "2022",
        "Dyrektywa UE 2022/2555 ustanawiająca środki na rzecz wysokiego wspólnego poziomu cyberbezpieczeństwa w UE. Rozszerza zakres NIS1 na więcej sektorów i podmiotów.",
        "IT,Energia,Transport,Zdrowie,Finanse,Administracja",
        "https://eur-lex.europa.eu/legal-content/PL/TXT/?uri=CELEX:32022L2555",
    ),
    (
        "SOC 2",
        "Kontrole Organizacji Usług (Typ I i II)",
        "Service Organization Controls 2",
        "2017",
        "Standard AICPA dla audytu i raportowania kontroli bezpieczeństwa, dostępności, integralności przetwarzania, poufności i prywatności w organizacjach usługowych (SaaS, chmura).",
        "IT,SaaS,Chmura,Finanse",
        "https://www.aicpa-cima.com/resources/landing/system-and-organization-controls-soc-suite-of-services",
    ),
    (
        "CIS Controls v8",
        "Krytyczne Mechanizmy Bezpieczeństwa (CIS)",
        "CIS Critical Security Controls",
        "8",
        "18 priorytetowych mechanizmów kontrolnych cyberbezpieczeństwa opracowanych przez Center for Internet Security. Podzielone na 3 grupy wdrożeniowe (IG1-IG3) wg dojrzałości organizacji.",
        "IT,Finanse,Zdrowie,Administracja",
        "https://www.cisecurity.org/controls",
    ),
    (
        "OWASP ASVS",
        "Standard Weryfikacji Bezpieczeństwa Aplikacji (OWASP)",
        "Application Security Verification Standard",
        "4.0.3",
        "Standard definiujący wymagania bezpieczeństwa dla projektowania, wytwarzania i testowania bezpiecznych aplikacji webowych. 3 poziomy weryfikacji (L1-L3).",
        "IT,Aplikacje webowe,Finanse",
        "https://owasp.org/www-project-application-security-verification-standard",
    ),
    (
        "OWASP MASVS",
        "Standard Weryfikacji Bezpieczeństwa Aplikacji Mobilnych (OWASP)",
        "Mobile Application Security Verification Standard",
        "2.0",
        "Standard bezpieczeństwa dla aplikacji mobilnych (Android/iOS). Definiuje wymagania dla architektury, przechowywania danych, kryptografii, uwierzytelniania, komunikacji sieciowej.",
        "IT,Mobile",
        "https://mas.owasp.org/MASVS",
    ),
    (
        "PCI DSS",
        "Standard Bezpieczeństwa Danych Przemysłu Kart Płatniczych",
        "Payment Card Industry Data Security Standard",
        "4.0",
        "Standard bezpieczeństwa dla organizacji przetwarzających, przechowujących lub przesyłających dane kart płatniczych. 12 wymagań w 6 celach. Obowiązkowy dla akceptantów i procesorów.",
        "Finanse,Handel,IT,E-commerce",
        "https://www.pcisecuritystandards.org/document_library",
    ),
    (
        "HL7 FHIR",
        "Standard Wymiany Danych w Ochronie Zdrowia",
        "Fast Healthcare Interoperability Resources",
        "R4",
        "Standard interoperacyjności systemów ochrony zdrowia definiujący format i interfejs API REST do wymiany danych medycznych. Stosowany w systemach HIS, EHR, telemedycynie.",
        "Zdrowie,IT medyczne",
        "https://hl7.org/fhir",
    ),
    (
        "GDPR / RODO",
        "Ogólne Rozporządzenie o Ochronie Danych Osobowych (UE)",
        "General Data Protection Regulation",
        "2016",
        "Rozporządzenie UE 2016/679 regulujące przetwarzanie danych osobowych obywateli UE. Definiuje zasady przetwarzania, prawa podmiotów danych, obowiązki administratorów i procesorów.",
        "Wszystkie branże",
        "https://eur-lex.europa.eu/legal-content/PL/TXT/?uri=CELEX:32016R0679",
    ),
    (
        "NIST CSF",
        "Framework Cyberbezpieczeństwa NIST",
        "NIST Cybersecurity Framework",
        "2.0",
        "Dobrowolny framework NIST do zarządzania ryzykiem cyberbezpieczeństwa. 6 funkcji: Govern, Identify, Protect, Detect, Respond, Recover. Szeroko stosowany w USA i globalnie.",
        "IT,Energia,Infrastruktura krytyczna",
        "https://www.nist.gov/cyberframework",
    ),
    (
        "NIST SP 800-53",
        "Katalog Mechanizmów Bezpieczeństwa i Prywatności (NIST)",
        "Security and Privacy Controls for Systems",
        "Rev. 5",
        "Kompleksowy katalog mechanizmów bezpieczeństwa i prywatności dla systemów informacyjnych. Obowiązkowy dla agencji federalnych USA, szeroko stosowany globalnie.",
        "IT,Administracja,Obronnosc",
        "https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final",
    ),
    (
        "PRINCE2 7",
        "Projekty w Kontrolowanych Środowiskach",
        "Projects in Controlled Environments",
        "7",
        "Metodyka zarządzania projektami skupiona na uzasadnieniu biznesowym, zorganizowanej strukturze, opartym na produktach planowaniu i sterowalności etapami. Powszechna w UK i Europie.",
        "Wszystkie branże",
        "https://www.axelos.com/certifications/propath/prince2-project-management",
    ),
    (
        "SCRUM Guide",
        "Przewodnik Scrum",
        "The Scrum Guide",
        "2020",
        "Oficjalny przewodnik Scrum definiujący framework Scrum: role (Product Owner, Scrum Master, Deweloperzy), artefakty (Product Backlog, Sprint Backlog, Increment) i zdarzenia.",
        "IT,Wytwarzanie oprogramowania",
        "https://scrumguides.org",
    ),
    (
        "SAFe 6.0",
        "Scaled Agile Framework",
        "Scaled Agile Framework",
        "6.0",
        "Framework skalowania zwinności na poziomie korporacyjnym. Definiuje role, artefakty i ceremononie dla PI Planning, ART, Solution Train i Portfolio Level.",
        "IT,Korporacje",
        "https://scaledagileframework.com",
    ),
    (
        "ISO/IEC 38500",
        "Ład Informatyczny Organizacji",
        "Governance of IT for the Organization",
        "2015",
        "Zasady ładu informatycznego dla organów kierowniczych organizacji. 6 zasad: odpowiedzialność, strategia, pozyskiwanie, wydajność, zgodność, zachowanie ludzkie.",
        "IT,Administracja,Finanse",
        "https://www.iso.org/standard/62816",
    ),
    (
        "ISO 22301",
        "System Zarządzania Ciągłością Działania (BCMS)",
        "Business Continuity Management Systems",
        "2019",
        "Wymagania dla ustanowienia, wdrożenia, utrzymania i doskonalenia systemu zarządzania ciągłością działania (BCMS). Obejmuje BCP, DRP, RTO, RPO.",
        "Wszystkie branże",
        "https://www.iso.org/standard/75106",
    ),
    (
        "ISO/IEC 20546",
        "Technologie Informacyjne — Big Data",
        "Big Data Overview and Vocabulary",
        "2019",
        "Przegląd i słownictwo big data. Definiuje terminy, koncepcje i taksonomię dla technologii big data.",
        "IT,Data Engineering,AI/ML",
        "https://www.iso.org/standard/38145",
    ),
    (
        "ISO/IEC 23053",
        "Framework dla Systemów AI z Uczeniem Maszynowym",
        "Framework for AI Systems Using ML",
        "2022",
        "Opisuje framework dla systemów AI używających uczenia maszynowego. Definiuje komponenty, procesy i role w systemach ML.",
        "IT,AI/ML",
        "https://www.iso.org/standard/74438",
    ),
    (
        "OpenAPI 3.x",
        "Specyfikacja Interfejsu API (OpenAPI Initiative)",
        "OpenAPI Specification",
        "3.1",
        "Standard opisu interfejsów API REST. Umożliwia generowanie dokumentacji, klientów SDK i testów. Stosowany w projektowaniu i dokumentowaniu API.",
        "IT,Integracja,API",
        "https://spec.openapis.org/oas/latest.html",
    ),
    (
        "AsyncAPI 3.x",
        "Specyfikacja Asynchronicznych API",
        "AsyncAPI Specification",
        "3.0",
        "Standard opisu asynchronicznych interfejsów API (event-driven, messaging). Uzupełnienie OpenAPI dla brokerów wiadomości (Kafka, RabbitMQ, MQTT).",
        "IT,Integracja,Messaging",
        "https://www.asyncapi.com/docs/reference/specification/latest",
    ),
]

# ---------------------------------------------------------------------------
# POLSKIE REGULACJE I NORMY
# Schemat: regulation_code, regulation_name, jurisdiction, industry, key_requirements,
#          data_engineering_impact, penalty_info
# ---------------------------------------------------------------------------
POLISH_REGULATIONS = [
    # --- Ustawy i rozporzadzenia PL ---
    (
        "KSC-PL",
        "Ustawa o Krajowym Systemie Cyberbezpieczeństwa",
        "Polska",
        "IT,Telekomunikacja,Energia,Transport,Zdrowie,Administracja,Finanse",
        "Obowiązki operatorów usług kluczowych (OUK) i dostawców usług cyfrowych (DSP): zarządzanie ryzykiem cyberbezpieczeństwa, incydenty, audyty, raportowanie do CSIRT. Transpozycja dyrektywy NIS (UE).",
        "Wymagania bezpieczeństwa systemów ICT, obowiązek zgłaszania incydentów do CSIRT NASK/GOV/MON, audyty bezpieczeństwa.",
        "Kary administracyjne do 1 mln PLN dla OUK; do 200 tys. PLN dla DSP.",
    ),
    (
        "UODO-PL",
        "Ustawa o Ochronie Danych Osobowych (implementacja RODO)",
        "Polska",
        "Wszystkie branże",
        "Polska implementacja RODO (Dz.U. 2018 poz. 1000 ze zm.). Dodatkowe przepisy krajowe dot. przetwarzania danych osobowych: inspektor ochrony danych (IOD), rejestr czynności, ocena skutków (DPIA), zgłoszenia naruszeń do UODO.",
        "Wymogi dla systemów przetwarzających dane osobowe: privacy by design/default, pseudonimizacja, szyfrowanie, logi dostępu, retencja danych.",
        "Kary UODO do 20 mln EUR lub 4% globalnego obrotu (za naruszenie RODO); krajowe sankcje wg UODO.",
    ),
    (
        "PZP-PL",
        "Prawo Zamówień Publicznych",
        "Polska",
        "Administracja,IT,Budownictwo,Doradztwo",
        "Ustawa z 11 września 2019 r. (Dz.U. 2019 poz. 2019 ze zm.). Reguluje udzielanie zamówień publicznych przez zamawiających. Progi UE, tryby udzielania, specyfikacje techniczne, SIWZ/SWZ.",
        "Wymogi dla systemów zamawiania elektronicznego (e-zamówienia, platforma e-Zamówienia), specyfikacje techniczne w przetargach IT, interoperacyjność.",
        "Unieważnienie postępowania, kary dla zamawiających i wykonawców, odpowiedzialność za naruszenie dyscypliny finansów publicznych.",
    ),
    (
        "UŚUDE-PL",
        "Ustawa o Świadczeniu Usług Drogą Elektroniczną",
        "Polska",
        "IT,E-commerce,Media,Handel",
        "Ustawa z 18 lipca 2002 r. Reguluje świadczenie usług drogą elektroniczną: wymogi informacyjne, regulaminy, pliki cookies, spam, odpowiedzialność dostawców.",
        "Wymogi dla aplikacji webowych i mobilnych: regulamin, polityka prywatności, mechanizm cookies, rejestr danych, logi dostępu.",
        "Kary do 3 lat pozbawienia wolności za rozsyłanie spamu; sankcje administracyjne UOKIK/UKE.",
    ),
    (
        "PT-PL",
        "Prawo Telekomunikacyjne (Ustawa o komunikacji elektronicznej)",
        "Polska",
        "Telekomunikacja,IT,Media",
        "Ustawa z 16 lipca 2004 r. (zastępowana ustawą o komunikacji elektronicznej, wdrożenie dyrektywy EECC). Reguluje rynek telekomunikacyjny, bezpieczeństwo sieci, retencję danych, tajemnicę komunikacji.",
        "Wymogi bezpieczeństwa sieci i systemów telekomunikacyjnych, obowiązek retencji danych połączeń, zgłaszanie incydentów do UKE/CSIRT.",
        "Kary administracyjne UKE; sankcje za naruszenie tajemnicy komunikacji.",
    ),
    (
        "UoR-PL",
        "Ustawa o Rachunkowości",
        "Polska",
        "Finanse,Handel,IT,Wszystkie branże",
        "Ustawa z 29 września 1994 r. Reguluje zasady rachunkowości, prowadzenie ksiąg rachunkowych, sporządzanie sprawozdań finansowych i ich audyt. Wymogi dla systemów księgowych.",
        "Wymogi dla systemów ERP/FK: integralność danych, niezmienność zapisów, archiwizacja przez 5 lat, backupy, logi zmian.",
        "Odpowiedzialność karna za fałszowanie dokumentacji finansowej; grzywny.",
    ),
    (
        "KSH-IT-PL",
        "Wymogi IT w Kodeksie Spółek Handlowych (KSH)",
        "Polska",
        "Finanse,Handel,IT",
        "Kodeks Spółek Handlowych — przepisy dotyczące elektronicznej formy uchwał, głosowania elektronicznego, rejestrów spółek i dokumentacji korporacyjnej w systemach informatycznych.",
        "Wymogi dla systemów zarządzania dokumentacją korporacyjną, e-votingu, rejestrów wspólników, elektronicznych aktów notarialnych.",
        "Nieważność czynności prawnych wykonanych niezgodnie z wymogami formy elektronicznej.",
    ),
    (
        "KEP-PL",
        "Ustawa o Kwalifikowanej Usłudze Zaufania (eIDAS/KEP)",
        "Polska",
        "IT,Administracja,Finanse,Prawo",
        "Polska implementacja rozporządzenia eIDAS (UE 910/2014). Kwalifikowany podpis elektroniczny (KEP), pieczęć elektroniczna, znacznik czasu. Dostawcy zaufania: CERTUM, Szafir, SimplySign.",
        "Wymogi dla systemów wymagających podpisu kwalifikowanego: integracja z API dostawców KEP, weryfikacja certyfikatów, archiwizacja podpisanych dokumentów.",
        "Odpowiedzialność cywilna dostawców zaufania; wymogi wobec dostawców niekwalifikowanych.",
    ),
    (
        "MIFID2-PL",
        "MiFID II — Dyrektywa dot. Rynku Finansowego (implementacja PL)",
        "Polska",
        "Finanse,IT finansowe",
        "Polska implementacja dyrektywy MiFID II (2014/65/UE) przez ustawę o obrocie instrumentami finansowymi. Wymogi dla systemów transakcyjnych, raportowania transakcji, najlepszej realizacji.",
        "Wymogi dla systemów transakcyjnych i raportowania: logi transakcji, znaczniki czasu ms, nagrywanie rozmów, retencja 5–7 lat.",
        "Kary KNF do 5 mln EUR lub 10% obrotu.",
    ),
    (
        "SOLVENCY2-PL",
        "Solvency II — Wymogi IT dla Ubezpieczycieli (implementacja PL)",
        "Polska",
        "Ubezpieczenia,Finanse,IT",
        "Polska implementacja dyrektywy Solvency II. Wymogi dla systemów IT ubezpieczycieli: ORSA, SCR/MCR, raportowanie XBRL do KNF, zarządzanie danymi aktuarialnymi.",
        "Wymogi dla systemów aktuarialnych i raportowania regulacyjnego: XBRL/XBRL Taxonomy, integracja z KNF, audyt danych.",
        "Kary KNF; wymóg zatwierdzenia przez KNF planów naprawy.",
    ),
    # --- Normy PN ---
    (
        "PN-ISO/IEC-27001",
        "PN-ISO/IEC 27001:2023-09 — Systemy Zarządzania Bezpieczeństwem Informacji",
        "Polska (PKN)",
        "IT,Finanse,Zdrowie,Administracja",
        "Polska wersja ISO/IEC 27001:2022 opublikowana przez PKN. Wymagania dla ISMS. Certyfikacja przez akredytowane jednostki (PCA). Tożsama z wersją międzynarodową, z polskojęzyczną treścią.",
        "Identyczna z ISO 27001 — wymagania dla ISMS, zarządzania ryzykiem, mechanizmów kontrolnych.",
        "Brak odrębnych sankcji — sankcje wynikają z przepisów szczególnych (UODO, KSC).",
    ),
    (
        "PN-EN-ISO-9001",
        "PN-EN ISO 9001:2015-10 — Systemy Zarządzania Jakością",
        "Polska (PKN)",
        "Wszystkie branże",
        "Polska wersja ISO 9001:2015 opublikowana przez PKN. Wymagania dla QMS. Certyfikacja przez akredytowane jednostki (PCA). Tożsama z wersją EN ISO.",
        "Wymagania dla procesów wytwarzania oprogramowania i usług IT: dokumentacja procesów, nadzór nad dostawcami, pomiary jakości.",
        "Brak odrębnych sankcji.",
    ),
    (
        "PN-EN-ISO-IEC-20000-1",
        "PN-EN ISO/IEC 20000-1:2019 — Zarządzanie Usługami IT",
        "Polska (PKN)",
        "IT,Telekomunikacja",
        "Polska wersja ISO/IEC 20000-1:2018. Wymagania dla SMS (Service Management System). Certyfikacja ITSM. Powiązana z ITIL 4.",
        "Wymagania dla procesów ITSM: zarządzanie incydentami, problemami, zmianami, konfiguracją, poziomami usług (SLA).",
        "Brak odrębnych sankcji.",
    ),
    (
        "PN-ISO-IEC-25010",
        "PN-ISO/IEC 25010:2023 — Model Jakości Systemu i Oprogramowania",
        "Polska (PKN)",
        "IT,Inzynieria oprogramowania",
        "Polska wersja ISO/IEC 25010:2023. Model SQuaRE jakości oprogramowania. 8 charakterystyk jakości. Stosowana w ocenie jakości systemów i produktów.",
        "Model jakości dla wymagań niefunkcjonalnych: niezawodność, wydajność, bezpieczeństwo, użyteczność, utrzymywalność.",
        "Brak odrębnych sankcji.",
    ),
    (
        "PN-EN-ISO-IEC-12207",
        "PN-EN ISO/IEC 12207:2017 — Procesy Cyklu Życia Oprogramowania",
        "Polska (PKN)",
        "IT,Inzynieria oprogramowania",
        "Polska wersja ISO/IEC 12207:2017. Framework procesów SDLC. Stosowana jako podstawa dla procesów wytwarzania i utrzymania oprogramowania.",
        "Framework dla SDLC: planowanie, wymagania, projektowanie, implementacja, testowanie, utrzymanie, wycofanie.",
        "Brak odrębnych sankcji.",
    ),
    (
        "PN-ISO-22301",
        "PN-ISO 22301:2020-04 — Zarządzanie Ciągłością Działania",
        "Polska (PKN)",
        "Wszystkie branże",
        "Polska wersja ISO 22301:2019. Wymagania dla BCMS. Certyfikacja przez akredytowane jednostki (PCA). Stosowana przy wymaganiach regulacyjnych ciągłości działania.",
        "Wymogi dla BCP/DRP, RTO/RPO, testów odtworzeniowych, zarządzania dostawcami krytycznymi.",
        "Brak odrębnych sankcji — wymogi wynikają z KSC, DORA, Solvency II.",
    ),
    # --- Wytyczne krajowe ---
    (
        "CERT-PL-WYTYCZNE",
        "Wytyczne CERT Polska (CSIRT NASK) dot. cyberbezpieczeństwa",
        "Polska (CERT Polska / CSIRT NASK)",
        "IT,Telekomunikacja,Energia,Administracja",
        "Rekomendacje i wytyczne bezpieczeństwa publikowane przez CERT Polska: bezpieczeństwo aplikacji webowych, konfiguracja infrastruktury, reagowanie na incydenty, phishing, ransomware.",
        "Praktyczne wskazówki dla systemów IT: hardenig serwerów, konfiguracja DNS/SPF/DKIM/DMARC, obsługa incydentów, systemy backupu.",
        "Brak sankcji — charakter doradczy; powiązane z wymogami KSC.",
    ),
    (
        "KNF-REKOM-IT",
        "Rekomendacje KNF dot. systemów IT w sektorze finansowym",
        "Polska (KNF)",
        "Finanse,Ubezpieczenia,IT finansowe",
        "Rekomendacje Komisji Nadzoru Finansowego dla banków i instytucji finansowych: Rekomendacja D (zarządzanie IT), Rekomendacja M (ryzyko operacyjne), wytyczne chmurowe. Charakter soft-law — oczekiwania nadzorcze.",
        "Wymogi dla systemów bankowych: zarządzanie ryzykiem IT, testy penetracyjne, TLPT, outsourcing IT, chmura (Komunikat UKNF dot. chmury obliczeniowej), ciągłość działania.",
        "Brak bezpośrednich sankcji za naruszenie rekomendacji; wpływ na ocenę nadzorczą i wymogi kapitałowe.",
    ),
    (
        "UKE-WYTYCZNE",
        "Wytyczne UKE dot. bezpieczeństwa sieci telekomunikacyjnych",
        "Polska (UKE)",
        "Telekomunikacja,IT",
        "Wytyczne Urzędu Komunikacji Elektronicznej dla dostawców usług telekomunikacyjnych: bezpieczeństwo sieci, retencja danych, zgłaszanie incydentów, wymogi dla sieci 5G.",
        "Wymogi bezpieczeństwa sieci telekomunikacyjnych, certyfikacja urządzeń sieciowych, procedury retencji danych połączeń.",
        "Kary administracyjne UKE za naruszenie prawa telekomunikacyjnego.",
    ),
    (
        "MC-INTEROP-PL",
        "Wytyczne Ministerstwa Cyfryzacji dot. interoperacyjności systemów publicznych",
        "Polska (Ministerstwo Cyfryzacji)",
        "Administracja,IT publiczne",
        "Krajowe Ramy Interoperacyjności (KRI) — rozporządzenie dot. minimalnych wymagań dla rejestrów publicznych i wymiany informacji. Standardy techniczne, formaty danych, API publiczne.",
        "Wymogi dla systemów administracji publicznej: otwarte standardy (XML, JSON, REST), dostępność WCAG 2.1, elektroniczna skrzynka podawcza (ePUAP/mObywatel).",
        "Wymóg zgodności dla systemów finansowanych ze środków publicznych.",
    ),
    (
        "CYBERSEC-STRATEGIA-PL",
        "Strategia Cyberbezpieczeństwa RP 2019-2024 (aktualizacja 2025+)",
        "Polska (Rząd RP)",
        "IT,Administracja,Infrastruktura krytyczna",
        "Strategia określająca cele i działania w zakresie cyberbezpieczeństwa RP. Podstawa dla programów rządowych, wymogów dla systemów krytycznych, finansowania bezpieczeństwa IT.",
        "Kontekst strategiczny dla projektów IT w sektorze publicznym i krytycznym: priorytety bezpieczeństwa, finansowanie z KPO/REACT-EU, wymogi dla systemów kluczowych.",
        "Brak bezpośrednich sankcji — framework strategiczny.",
    ),
]


def seed_standards(conn: sqlite3.Connection, dry_run: bool = False):
    cur = conn.cursor()
    cur.execute("DELETE FROM standards")
    inserted = 0
    for row in INTERNATIONAL_STANDARDS:
        code, name_pl, name_en, version, desc, industries, url = row
        cur.execute(
            "INSERT INTO standards (standard_code, standard_name, standard_name_en, version, description, applicable_industries, url) VALUES (?,?,?,?,?,?,?)",
            (code, name_pl, name_en, version, desc, industries, url),
        )
        inserted += 1
    print(f"  [standards] Wstawiono: {inserted} standardów miedzynarodowych.")
    if not dry_run:
        conn.commit()


def seed_regulations(conn: sqlite3.Connection, dry_run: bool = False):
    cur = conn.cursor()
    cur.execute("DELETE FROM compliance_regulations")
    inserted = 0
    for row in POLISH_REGULATIONS:
        code, name, jurisdiction, industry, key_req, de_impact, penalty = row
        cur.execute(
            "INSERT INTO compliance_regulations (regulation_code, regulation_name, jurisdiction, industry, key_requirements, data_engineering_impact, penalty_info) VALUES (?,?,?,?,?,?,?)",
            (code, name, jurisdiction, industry, key_req, de_impact, penalty),
        )
        inserted += 1
    print(f"  [compliance_regulations] Wstawiono: {inserted} regulacji polskich.")
    if not dry_run:
        conn.commit()


def main():
    dry_run = "--dry-run" in sys.argv
    if dry_run:
        print("=== TRYB DRY-RUN ===")

    conn = sqlite3.connect(DB_PATH)
    seed_standards(conn, dry_run=dry_run)
    seed_regulations(conn, dry_run=dry_run)
    conn.close()
    print("Gotowe.")


if __name__ == "__main__":
    main()
