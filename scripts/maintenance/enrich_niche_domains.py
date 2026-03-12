#!/usr/bin/env python3
"""
enrich_niche_domains.py — wzbogaca 734 szablony niszowych domen
o treść opisującą cel, zakres i mechanizmy wpływu.
Użycie:
    python3 enrich_niche_domains.py --dry-run
    python3 enrich_niche_domains.py --apply
    python3 enrich_niche_domains.py --apply --path-filter quantum
"""
import re, argparse, sys
from pathlib import Path

TDIR        = Path(__file__).parent.parent.parent / "generated_templates"
PLACEHOLDER = "Opisuje cel, zakres i zastosowanie tego dokumentu"

# ── Archetypy domenowe ─────────────────────────────────────────────────────────
# (keywords_in_title, guidance_text)  — pierwsze pasujące wygrywa
ARCHETYPES = [
    # QUANTUM
    (["quantum key", "qkd"],
     "Opisuje architekturę dystrybucji klucza kwantowego (QKD) — protokoły BB84/E91, "
     "wymagania sprzętowe (nadajniki fotonów, detektory), integrację z sieciami kryptograficznymi, "
     "zarządzanie kanałem kwantowym i klasycznym oraz politykę rotacji kluczy."),
    (["post-quantum", "post_quantum", "post quantum"],
     "Definiuje strategię migracji kryptografii do algorytmów odpornych na ataki kwantowe (PQC) — "
     "harmonogram przejścia z RSA/ECC na CRYSTALS-Kyber/Dilithium, inwentaryzację systemów "
     "kryptograficznych, priorytety migracji i plan testów kompatybilności."),
    (["quantum circuit", "circuit transpil"],
     "Opisuje procesy kompilacji i optymalizacji obwodów kwantowych — transpilację bramek logicznych "
     "na docelowe bramki sprzętowe, strategie redukcji głębokości obwodu, obsługę szumów kwantowych "
     "(error mitigation) i metryki jakości (fidelity, gate error rate)."),
    (["quantum", "classical-quantum", "classical_quantum"],
     "Opisuje architekturę interfejsu między systemami klasycznymi a kwantowymi — protokoły "
     "komunikacji, zarządzanie kolejką obliczeń kwantowych, obsługę wyników pomiarów, "
     "integrację z platformami (IBM Quantum, AWS Braket) i monitoring zasobów obliczeniowych."),
    # AVIATION
    (["aircraft maintenance"],
     "Opisuje procesy zarządzania utrzymaniem statków powietrznych — harmonogramy przeglądów "
     "(A/B/C/D-check), śledzenie historii napraw (CAMP/MRO), zarządzanie certyfikatami techników "
     "(EASA Part-66), logistykę części zamiennych (AOG handling) i dokumentację wymaganą przez "
     "przepisy lotnicze (EASA Part-M, FAR-43)."),
    (["flight operations", "flight management"],
     "Definiuje procedury operacyjne lotów — planowanie tras (FMS), zarządzanie załogą (CRM), "
     "procedury awaryjne, dokumentację wymaganą przez ICAO/EASA (OFP, NOTAM, MEL), "
     "metryki OTP (On-Time Performance) i raportowanie zdarzeń lotniczych."),
    (["certyfikacja faa", "certyfikacja easa", "faa", "easa"],
     "Opisuje proces certyfikacji systemów/oprogramowania lotniczego — wymagania DO-178C "
     "(software) i DO-254 (hardware), poziomy DAL (Design Assurance Level), "
     "dokumentację certyfikacyjną (PSAC, SDP, SVP) i relację z autoryzowanymi "
     "przedstawicielami FAA/EASA."),
    # MARITIME
    (["cargo handling", "cargo operations", "cargo tracking"],
     "Opisuje zarządzanie operacjami cargo — śledzenie ładunków (Bill of Lading, AWB), "
     "integrację z systemami portowymi (EDI/EDIFACT), kontrolę celną i fitosanitarną, "
     "obsługę kontenerów (FCL/LCL), raportowanie IMO i powiązania z systemami TOS."),
    (["fleet management", "fleet tracking", "vessel", "zarządzanie flotą"],
     "Definiuje zarządzanie flotą jednostek pływających — śledzenie pozycji (AIS/LRIT), "
     "planowanie tras i optymalizację zużycia paliwa, harmonogramy przeglądów technicznych "
     "(ISM Code, SOLAS), zarządzanie certyfikatami jednostek i dokumentacją Port State Control."),
    (["port integration", "integracji portowej"],
     "Opisuje architekturę integracji systemów portowych — interfejsy z Port Community System "
     "(PCS), wymianę komunikatów EDI (COPARN, COARRI, CUSCAR), obsługę manifesty celnych, "
     "synchronizację z terminalami przeładunkowymi i systemami planowania zawinięć."),
    # IoT / SCADA
    (["ota update", "ota service", "firmware update", "over-the-air", "uslugi ota", "aktywacja uslugi ota"],
     "Opisuje proces bezpiecznej aktualizacji oprogramowania urządzeń w terenie (OTA) — "
     "podpisywanie firmware (secure boot chain), delta updates, zarządzanie wersjami, "
     "rollback w przypadku awarii, metryki powodzenia wdrożenia i wymagania bezpieczeństwa "
     "(PSA Certified, IEC 62443)."),
    (["edge device"],
     "Definiuje kryteria doboru i zarządzania urządzeniami brzegowymi — wymagania sprzętowe "
     "(procesory, pamięć, łączność), systemy operacyjne (RTOS, Linux embedded), "
     "protokoły komunikacji (MQTT, OPC-UA, Modbus), zarządzanie cyklem życia urządzenia "
     "i wymagania środowiskowe (temperature range, certyfikaty EMC/CE)."),
    (["alarm management"],
     "Opisuje strategię zarządzania alarmami w systemach przemysłowych/SCADA — "
     "hierarchię alarmów (EEMUA 191, ISA-18.2), rationalization (flooding prevention), "
     "priorytety eskalacji, suppression logic, metryki jakości alarmów "
     "(AAR, flood rate) i proces zarządzania zmianami konfiguracji alarmów."),
    (["scada", "industrial control", "plc", "hmi"],
     "Opisuje architekturę systemu sterowania przemysłowego — topologię sieci OT "
     "(strefy Purdue Model), integrację PLC/DCS z systemami nadzoru (SCADA/HMI), "
     "wymagania bezpieczeństwa IEC 62443, strategie redundancji i procedury testowania "
     "zmian w środowisku produkcyjnym."),
    # HEALTHCARE
    (["clinical trial"],
     "Opisuje zarządzanie dokumentacją badań klinicznych — zgodność z ICH-GCP (E6 R2), "
     "zarządzanie protokołem badania, randomizację i zaślepienie, zbieranie danych "
     "(EDC/eCRF), monitorowanie (monitoring visit reports), raportowanie zdarzeń "
     "niepożądanych (SAE) do EMA/FDA."),
    (["clinical data", "clinical_data"],
     "Definiuje architekturę hurtowni danych klinicznych — integrację z EHR (HL7 FHIR "
     "R4, HL7 v2), modele danych OMOP CDM, anonimizację danych (HIPAA Safe Harbor, "
     "pseudonimizacja wg RODO), procesy ETL z systemów szpitalnych i metryki jakości danych."),
    (["medical records", "ehr", "patient records"],
     "Opisuje zarządzanie dokumentacją medyczną pacjenta — wymagania prawne (ustawa o "
     "prawach pacjenta), struktury danych HL7 FHIR, uprawnienia dostępu (RBAC dla "
     "personelu medycznego), retencję danych i procesy wymiany dokumentacji między placówkami."),
    (["lims", "laboratory", "lab management"],
     "Opisuje zarządzanie procesami laboratoryjnymi — śledzenie próbek (chain of custody), "
     "integrację z aparaturą analityczną, kalibrację instrumentów, zarządzanie odczynnikami, "
     "dokumentację GLP/GMP i walidację metod analitycznych (IQ/OQ/PQ)."),
    # LEGAL TECH
    (["attorney", "privilege"],
     "Opisuje zasady ochrony tajemnicy adwokackiej w systemach IT — klasyfikację dokumentów "
     "objętych privilege, kontrolę dostępu, procedury e-discovery z zachowaniem privilege "
     "i wymagania dla systemów DMS w kancelariach prawnych."),
    (["legal research", "legal tech", "ai ethics in legal"],
     "Definiuje procesy i narzędzia wspomagające pracę prawników — systemy wyszukiwania "
     "orzecznictwa, automatyzację analizy dokumentów (AI-assisted review), etyczne zasady "
     "stosowania AI w praktyce prawnej (Bar Association guidelines) i zgodność z RODO "
     "w kontekście danych klientów."),
    # GAMING / EVENTS
    (["game breaking", "game-breaking", "player feedback", "game flow", "esport"],
     "Opisuje procesy zarządzania jakością w produkcji gier — klasyfikację bugów "
     "(critical/blocker/major), pipeline raportowania defektów, priorytety hotfixów, "
     "zbieranie feedbacku graczy, metryki retencji i metryki stabilności (crash rate, ANR rate)."),
    (["venue management", "attendee satisfaction"],
     "Opisuje zarządzanie obiektami i wydarzeniami — planowanie pojemności, harmonogramowanie "
     "rezerwacji sal, zarządzanie dostawcami AV/catering, systemy rejestracji uczestników, "
     "metryki satysfakcji (NPS post-event) i powiązania z systemami ticketingowymi."),
    # BIM / REAL ESTATE
    (["bim", "building information"],
     "Opisuje standardy zarządzania modelami BIM — wymagania ISO 19650, poziomy szczegółowości "
     "(LOD 100-500), formaty wymiany (IFC, BCF), protokoły koordynacji modeli (clash detection), "
     "Common Data Environment (CDE) i zarządzanie prawami dostępu do modeli."),
    (["smart building", "building maintenance", "tenant portal", "facility"],
     "Opisuje systemy zarządzania nieruchomościami — integrację z BMS (Building Management "
     "System), obsługę zgłoszeń serwisowych, zarządzanie dostępem, metryki zużycia mediów "
     "i raportowanie efektywności energetycznej budynku."),
    # E-GOVERNMENT
    (["citizen app", "citizen digital", "citizen portal", "portal obywatel", "obywatela"],
     "Opisuje projektowanie i wdrożenie usług cyfrowych dla obywateli — architekturę e-usług "
     "(ePUAP/gov.pl API), integrację z węzłem krajowym (profil zaufany, mObywatel), "
     "dostępność WCAG 2.1 AA, zarządzanie wnioskami administracyjnymi i wymagania RODO."),
    (["government", "public sector", "danych rzad", "digital government", "przetwarzanie wnioskow"],
     "Opisuje systemy informacyjne administracji publicznej — architekturę opartą o standardy "
     "GovIT, integrację z rejestrami państwowymi (PESEL, KRS), wymagania KSC, zgodność z RODO "
     "i przepisami o dostępie do informacji publicznej."),
    # HR
    (["ats", "applicant tracking", "recruitment system"],
     "Opisuje wdrożenie systemu śledzenia kandydatów (ATS) — pipeline rekrutacyjny "
     "(requisition-to-offer), integrację z tablicami ogłoszeń, procesy scoringu CV "
     "(AI-assisted screening), RODO dla danych kandydatów i metryki efektywności rekrutacji."),
    (["payroll", "placow", "przetwarzanie payroll"],
     "Opisuje procesy przetwarzania wynagrodzeń — integrację z systemami HR, kalkulację "
     "składek ZUS i zaliczek PIT, obsługę świadczeń pracowniczych, generowanie przelewów "
     "i raportów GUS, wymagania bezpieczeństwa danych płacowych."),
    (["attendance", "workforce management", "benefits admin", "administracja benefitami"],
     "Opisuje zarządzanie czasem pracy i świadczeniami — ewidencję czasu pracy (zgodną z "
     "Kodeksem pracy), integrację z czytnikami RCP, zarządzanie wnioskami urlopowymi, "
     "administrację kafeteriami benefitów i powiązania z systemami kadrowo-płacowymi."),
    # ESG / ENERGY
    (["carbon", "carbon offset", "emission"],
     "Opisuje zarządzanie śladem węglowym i offsetami emisji CO2 — metodologię pomiarów "
     "(GHG Protocol Scope 1/2/3), integrację z licznikami energii, weryfikację certyfikatów "
     "offsetowych (Gold Standard, VCS), raportowanie ESG (GRI, CSRD) i śledzenie celów net-zero."),
    (["green software", "sustainability", "circular economy", "ai for sustainability", "ai energy"],
     "Opisuje praktyki zrównoważonego rozwoju w IT — wskaźniki efektywności energetycznej "
     "(PUE, SCI), strategie optymalizacji zużycia mocy przez systemy AI/ML, circular economy "
     "w zarządzaniu sprzętem i raportowanie ESG (CSRD, TCFD)."),
    # AUTONOMOUS VEHICLES
    (["autonomous vehicle", "autonomous haul", "self-driving"],
     "Opisuje wymagania bezpieczeństwa pojazdów autonomicznych — poziomy autonomii (SAE J3016 "
     "L1-L5), architekturę systemów percepcji (LIDAR/kamera/radar fusion), testowanie "
     "(ISO 26262, ISO 21448 SOTIF), wymagania regulacyjne (UE 2019/2144) i zarządzanie incydentami."),
    (["battery power", "battery management"],
     "Opisuje zarządzanie systemami bateryjnymi — monitoring BMS, algorytmy estymacji SoC/SoH, "
     "protokoły ładowania (CCS/CHAdeMO/ISO 15118), zarządzanie termiczne, cykl życia baterii "
     "i wymagania bezpieczeństwa (UN 38.3, IEC 62619)."),
    # ADTECH
    (["ad optimization", "ad platform", "budget pacing", "aktywacja platform reklamowych"],
     "Opisuje zarządzanie platformami reklamowymi — integrację z DSP/SSP (programmatic), "
     "strategie bidowania (target CPA, ROAS), zarządzanie budżetem (pacing, allocation), "
     "brand safety, pomiar viewability (MRC standards) i raportowanie IAB Tech Lab."),
    (["attribution engine"],
     "Definiuje modele atrybucji konwersji — metodologie (Last-Click, Data-Driven, Shapley "
     "Value), integrację ze źródłami danych (GA4, Meta Pixel, server-side tagging), "
     "zarządzanie oknem atrybucji, obsługę ograniczeń prywatności (cookieless) i raportowanie ROI."),
    (["audience management", "cdp development", "customer data platform", "clienteling"],
     "Opisuje zarządzanie danymi o odbiorcach — segmentację, architekturę CDP, integrację ze "
     "źródłami first-party data, zarządzanie zgodami RODO (consent management platform), "
     "aktywację segmentów w kanałach reklamowych i metryki jakości danych audience."),
    # ML / AI
    (["ml use case", "ai use case", "big data use case", "blockchain use case"],
     "Opisuje definiowanie i ocenę przypadków użycia systemów AI/ML — Canvas modelu biznesowego "
     "(problem, dane, metryki sukcesu), ocenę wykonalności technicznej (data readiness), "
     "analizę ryzyk etycznych (AI Act EU), plan pilotażu i kryteria skalowania."),
    (["data pipeline", "real-time data pipeline", "bioinformatics pipeline"],
     "Opisuje architekturę potoku danych — źródła i formaty ingestion, transformacje "
     "(batch vs. streaming), orkiestrację (Airflow, Prefect), monitoring jakości danych, "
     "zarządzanie schematem (schema registry), testy i SLA czasu dostarczenia danych."),
    (["digital twin", "twin optim"],
     "Opisuje architekturę cyfrowego bliźniaka — synchronizację z fizycznym obiektem (sensory "
     "IoT, OPC-UA), modele symulacyjne (physics-based + ML), API do zapytań o stan, scenariusze "
     "what-if, zarządzanie dryftem modelu i integrację z systemami SCADA/ERP."),
    # BIOINFORMATICS
    (["bioinformatics", "genomic", "sequencing", "scientific data"],
     "Opisuje infrastrukturę obliczeniową dla danych biologicznych — pipeline analizy sekwencji "
     "(NGS: alignment, variant calling, annotation), zarządzanie danymi genomicznymi (FAIR, "
     "GA4GH), obliczenia HPC/cloud, zarządzanie wersjami narzędzi bioinformatycznych i wymogi ELSI."),
    # BLOCKCHAIN
    (["blockchain", "smart contract", "distributed ledger", "web3"],
     "Opisuje wdrożenie rozwiązań blockchain — wybór platformy (Ethereum, Hyperledger Fabric, "
     "Solana), architekturę smart kontraktów, zarządzanie kluczami i portfelami, audyt "
     "bezpieczeństwa kontraktów (Slither, Mythril), optymalizację gas i integrację off-chain."),
    # RETAIL / E-COMMERCE
    (["bopis", "buy online", "order fulfillment", "order management"],
     "Opisuje zarządzanie zamówieniami omnichannel — przepływ BOPIS (Buy Online, Pick Up In "
     "Store), integrację OMS z POS i WMS, obsługę wyjątków (stockout, late pickup), "
     "metryki SLA fulfilmentu i powiadomienia klienta."),
    (["checkout", "payment", "billing system", "billing"],
     "Opisuje procesy płatności i fakturowania — integrację z bramkami płatniczymi (Stripe, "
     "PayU, Przelewy24), obsługę błędów transakcji, zgodność PCI DSS, zarządzanie zwrotami, "
     "fakturowanie elektroniczne (KSeF) i raportowanie finansowe."),
    (["booking engine", "channel manager", "channel sync", "reservation"],
     "Opisuje systemy zarządzania rezerwacjami — integrację z Channel Manager (Booking.com, "
     "Expedia), zarządzanie dostępnością i cenami (rate parity), obsługę konfliktów rezerwacji, "
     "API dla GDS (Amadeus, Sabre) i procesy rozliczeń z kanałami dystrybucji."),
    # HOSPITALITY
    (["guest services", "hotel", "property management system", "housekeeping"],
     "Opisuje procesy obsługi gości i zarządzanie obiektem hotelowym — integrację z PMS "
     "(Opera, Protel), procedury check-in/check-out, zarządzanie pokojami (housekeeping), "
     "upselling, obsługę reklamacji gości, metryki (RevPAR, NPS) i systemy lojalnościowe."),
    # BROADCASTING / MEDIA
    (["broadcast production", "broadcast workflow", "media production", "c2 platform"],
     "Opisuje zarządzanie produkcją medialną — workflow produkcji (pre-production, production, "
     "post-production), zarządzanie zasobami medialnymi (MAM/DAM), integrację z systemami "
     "emisji (playout, MCR), standardy branżowe (SMPTE, EBU) i archiwizację materiałów."),
    # NETWORK / INFRASTRUCTURE
    (["network segmentation", "network security", "networking for virtual"],
     "Opisuje architekturę i bezpieczeństwo sieci — strategie segmentacji (VLAN, micro-segmentation, "
     "zero trust), polityki firewall i ACL, zarządzanie certyfikatami TLS, monitoring ruchu "
     "(NetFlow, SIEM) i procedury zmiany konfiguracji sieci."),
    (["server virtualization", "virtual infrastructure", "virtualization"],
     "Opisuje zarządzanie infrastrukturą wirtualizowaną — architekturę hypervisorów "
     "(VMware vSphere, Proxmox, KVM), zarządzanie zasobami (CPU/RAM/storage provisioning), "
     "wysoką dostępność (HA/DRS), snapshoty, migrację live i monitoring wydajności VM."),
    # FINANCE
    (["budget proposal", "budget tracking", "budget pacing", "client assets", "claims management",
      "broker maintenance", "finansow"],
     "Opisuje zarządzanie budżetem i aktywami finansowymi — planowanie budżetu (top-down / "
     "bottom-up), śledzenie wydatków vs. planu, raportowanie CFO, zarządzanie roszczeniami "
     "i reconciliation z systemami księgowymi (ERP)."),
    # CUSTOMER SERVICE / SUPPORT
    (["help desk", "itsm tools", "case management", "support operations", "client service"],
     "Opisuje procesy centrum wsparcia — zarządzanie zgłoszeniami (ITIL Service Desk), "
     "SLA per priorytet (P1-P4), escalation matrix, zarządzanie bazą wiedzy (Knowledge Base), "
     "metryki jakości (CSAT, First Contact Resolution) i integrację z systemami ITSM."),
    # SMART CITY / GEOSPATIAL
    (["geospatial", "geocoding", "map data", "spatial data", "gis"],
     "Opisuje zarządzanie danymi przestrzennymi — systemy GIS i API (Google Maps, HERE, "
     "OpenStreetMap), procesy aktualizacji map, jakość danych geocodingu, standardy "
     "OGC (WMS, WFS, GeoJSON), bezpieczeństwo danych lokalizacyjnych i RODO."),
    # IoT CONNECTED / SMART
    (["connected services", "smart city", "smart grid", "smart", "iot"],
     "Opisuje architekturę połączonych urządzeń i usług IoT — platformy zarządzania "
     "urządzeniami (AWS IoT Core, Azure IoT Hub), protokoły (MQTT, CoAP, LwM2M), "
     "zarządzanie tożsamością urządzeń (X.509, TPM), przetwarzanie brzegowe i edge-to-cloud "
     "pipeline oraz bezpieczeństwo (IEC 62443, PSA Certified)."),
    # COMPETITVE INTEL / ANALYTICS
    (["competitive intelligence", "customer journey analytics", "analytics approach", "query success"],
     "Opisuje procesy i metodologię analityki — źródła danych (1st, 2nd, 3rd party), "
     "modele analityczne (descriptive, predictive, prescriptive), narzędzia BI (Tableau, "
     "Power BI, Looker), governance danych analitycznych, metryki jakości analiz i procesy "
     "dystrybucji insightów do interesariuszy."),
]



# ── Pattern matchers dla typowych struktur tytułów ─────────────────────────────

def match_archetype(title: str) -> str | None:
    """Dopasowuje tytuł do archetypu. Zwraca guidance text lub None."""
    tl = title.lower()
    for keywords, guidance in ARCHETYPES:
        if any(kw in tl for kw in keywords):
            return guidance
    return None


def pattern_guidance(title: str) -> str:
    """Generuje guidance na podstawie wzorca tytułu (fallback po ARCHETYPES)."""
    tl = title.lower()

    # Common X Issues and Solutions
    m = re.search(r"common (.+?) issues", tl)
    if m:
        domain = m.group(1).strip().title()
        return (
            f"Opisuje typowe problemy i sprawdzone rozwiązania w obszarze {domain} — "
            f"klasyfikację problemów według priorytetu i częstości występowania, "
            f"kroki diagnostyczne (decision tree), znane obejścia (workarounds), "
            f"warunki eskalacji do wyższego poziomu wsparcia oraz linki do artykułów "
            f"bazy wiedzy i dokumentacji producenta."
        )

    # Access Control for X
    m = re.search(r"access control for (.+)", tl)
    if m:
        resource = m.group(1).strip().title()
        return (
            f"Opisuje politykę kontroli dostępu do {resource} — model uprawnień "
            f"(RBAC/ABAC), macierz ról i dozwolonych operacji, procedury nadawania "
            f"i odbierania dostępu, procesy certyfikacji dostępu (access review), "
            f"logowanie i audyt prób dostępu oraz wymagania zgodności "
            f"(ISO 27001, SOC 2, RODO)."
        )

    # X Failure / X Error Response
    if re.search(r"(failure|error|outage)\b", tl):
        obj = re.sub(r"\b(failure|error|outage|response)\b", "", title, flags=re.I).strip(" -_")
        return (
            f"Opisuje procedurę reagowania na awarie systemu {obj} — klasyfikację "
            f"awarii (severity P1-P4), kroki diagnostyczne i izolacji przyczyn, "
            f"escalation path (L1 → L2 → L3 → vendor), procedury komunikacji "
            f"z interesariuszami, kryteria przywrócenia serwisu i format postmortem."
        )

    # X Tracking / X Tracker
    if re.search(r"\btracking\b|\btracker\b", tl):
        obj = re.sub(r"\b(tracking|tracker)\b", "", title, flags=re.I)
        obj = re.sub(r"\s{2,}", " ", obj).strip(" -_")
        return (
            f"Opisuje system śledzenia i raportowania dla {obj} — metryki kluczowe "
            f"(KPI/OKR), źródła danych i częstotliwość aktualizacji, format dashboardu "
            f"i raportów, progi alertów, właścicieli metryk i procesy przeglądów "
            f"(weekly/monthly review cycle)."
        )

    # X Analytics / X Dashboard
    if re.search(r"\banalytics\b|\bdashboard\b|\breport\b|\bmetrics\b", tl):
        obj = re.sub(r"\b(analytics|dashboard|report|metrics)\b", "", title, flags=re.I)
        obj = re.sub(r"\s{2,}", " ", obj).strip(" -_")
        return (
            f"Opisuje metodologię i implementację analityki dla {obj} — definicję "
            f"mierników (KPI/metrics dictionary), architekturę zbierania danych, "
            f"narzędzia BI i wizualizacji, procesy weryfikacji jakości danych, "
            f"cykl raportowania i dystrybucji insightów do interesariuszy."
        )

    # X Management System / X System
    if re.search(r"\bmanagement system\b|\bsystem\b", tl) and len(tl) > 10:
        obj = re.sub(r"\b(management system|system)\b", "", title, flags=re.I)
        obj = re.sub(r"\s{2,}", " ", obj).strip(" -_")
        return (
            f"Definiuje wymagania i architekturę systemu zarządzania {obj} — "
            f"zakres funkcjonalności, integracje z systemami zewnętrznymi, "
            f"model danych, role użytkowników i macierz uprawnień, "
            f"wymagania niefunkcjonalne (wydajność, dostępność, bezpieczeństwo) "
            f"i plan wdrożenia."
        )

    # X Operations / X Workflow / X Runbook
    if re.search(r"\boperations\b|\bworkflow\b|\brunbook\b", tl):
        obj = re.sub(r"\b(operations|workflow|runbook|operational)\b", "", title, flags=re.I)
        obj = re.sub(r"\s{2,}", " ", obj).strip(" -_")
        return (
            f"Opisuje procedury operacyjne dla {obj} — zakres odpowiedzialności, "
            f"harmonogramy i SLA, listy kontrolne do rutynowych zadań, "
            f"procedury eskalacji, metryki jakości i procesy ciągłego doskonalenia "
            f"(blameless postmortems, kaizen)."
        )

    # X Development / X Platform Development
    if re.search(r"\bdevelopment\b|\bimplementation\b", tl):
        obj = re.sub(r"\b(development|implementation|platform)\b", "", title, flags=re.I)
        obj = re.sub(r"\s{2,}", " ", obj).strip(" -_")
        return (
            f"Opisuje proces projektowania i budowy {obj} — wymagania funkcjonalne "
            f"i niefunkcjonalne, architekturę rozwiązania, stack technologiczny, "
            f"plan iteracji (roadmap / sprint backlog), kryteria akceptacji "
            f"i plan testów (unit, integration, E2E)."
        )

    # Announcement / Bulletin / Communication
    if re.search(r"\bannouncement\b|\bbulletin\b|\bcommunication\b|\bupdate\b", tl):
        return (
            f"Opisuje szablon komunikatu dla {title} — strukturę przekazu "
            f"(co, dlaczego, kiedy, kto jest odbiorcą), kanały dystrybucji "
            f"(e-mail, intranet, Teams/Slack), tone of voice, wymagania dotyczące "
            f"zatwierdzenia przed wysyłką i archiwizacji komunikatów."
        )

    # Policy / Standard / Guidelines / Best Practices
    if re.search(r"\bpolicy\b|\bstandard\b|\bguidelines\b|\bbest practices\b", tl):
        obj = re.sub(r"\b(policy|standard|guidelines|best practices)\b", "", title, flags=re.I).strip(" -_")
        return (
            f"Definiuje politykę i standardy dla {obj} — zasady obowiązujące "
            f"wszystkich pracowników i systemy objęte polityką, wymagania minimalne, "
            f"procedury wyjątków (exception process), właściciel polityki, "
            f"cykl przeglądu i aktualizacji oraz konsekwencje naruszeń."
        )

    # Migration / Deployment / Release / Rollout
    if re.search(r"\bmigration\b|\bdeployment\b|\brelease\b|\brollout\b", tl):
        obj = re.sub(r"\b(migration|deployment|release|rollout)\b", "", title, flags=re.I).strip(" -_")
        return (
            f"Opisuje plan wdrożenia lub migracji dla {obj} — zakres zmian, "
            f"harmonogram i kamienie milowe, strategie wdrożenia (blue-green, "
            f"canary, rolling), kryteria go/no-go, plan rollback, "
            f"komunikację do użytkowników i monitoring po wdrożeniu."
        )

    # Security / Bezpieczeństwo
    if re.search(r"\bsecurity\b|\bbezpiecze\b|\bsafety\b", tl):
        obj = re.sub(r"\b(security|safety|bezpiecze[a-z]*)\b", "", title, flags=re.I).strip(" -_")
        return (
            f"Opisuje wymagania i środki bezpieczeństwa dla {obj} — model zagrożeń "
            f"(threat modeling), wymagania kontroli dostępu i szyfrowania, "
            f"procedury audytu i testów bezpieczeństwa (pentesty, vulnerability scanning), "
            f"zarządzanie incydentami bezpieczeństwa i wymagania zgodności "
            f"(ISO 27001, KSC, NIS2)."
        )

    # Generic smart fallback — interpolacja tytułu
    return (
        f"Definiuje cel, zakres i wymagania dla {title} — kontekst biznesowy "
        f"i techniczny, kluczowe decyzje projektowe i operacyjne, role odpowiedzialne, "
        f"kryteria sukcesu, powiązania z innymi dokumentami i procesami "
        f"oraz wymagania standardów i regulacji obowiązujących w danym obszarze."
    )


def enrich_file(fpath: Path, dry_run: bool) -> bool:
    """Wzbogaca jeden plik. Zwraca True jeśli plik został (lub zostałby) zmieniony."""
    try:
        content = fpath.read_text(encoding="utf-8")
    except Exception as e:
        print(f"  BŁĄD odczytu {fpath}: {e}", file=sys.stderr)
        return False

    if PLACEHOLDER not in content:
        return False

    # Wyciągnij tytuł z frontmatter
    m = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    title = ""
    if m:
        try:
            import yaml
            fm = yaml.safe_load(m.group(1))
            title = fm.get("title", "")
        except Exception:
            pass
    if not title:
        title = fpath.stem.replace("_", " ").replace("-", " ").title()

    # Dobierz guidance
    guidance = match_archetype(title)
    if guidance is None:
        guidance = pattern_guidance(title)

    # Zbuduj nowy blok celu — zachowaj pierwszą linię (tytuł + "— szablon dokumentu IT.")
    # i zastąp placeholder nowym tekstem
    # Placeholder pojawia się jako osobny paragraf — może być wieloliniowy
    placeholder_re = re.compile(
        r"(Opisuje cel, zakres i zastosowanie tego dokumentu[^\n]*\n?"
        r"(?:[^\n]+\n)*?)"
        r"(?=\n\n|\n>|\n##|\Z)",
        re.DOTALL
    )
    new_content = content.replace(
        "Opisuje cel, zakres i zastosowanie tego dokumentu w kontekście procesu lub systemu IT. "
        "Zawiera: definicję problemu lub potrzeby biznesowej adresowanej przez ten dokument, "
        "kluczowe decyzje które wspiera, ryzyka które ogranicza i wartość dostarczaną interesariuszom.",
        guidance,
        1
    )

    if new_content == content:
        # Spróbuj bardziej agresywnego dopasowania
        idx = content.find("Opisuje cel, zakres i zastosowanie")
        if idx == -1:
            return False
        end_idx = content.find("\n\n", idx)
        if end_idx == -1:
            end_idx = len(content)
        old_para = content[idx:end_idx]
        new_content = content[:idx] + guidance + content[end_idx:]

    if dry_run:
        return True

    try:
        fpath.write_text(new_content, encoding="utf-8")
        return True
    except Exception as e:
        print(f"  BŁĄD zapisu {fpath}: {e}", file=sys.stderr)
        return False


def main():
    parser = argparse.ArgumentParser(description="Wzbogaca niszowe szablony dokumentów IT.")
    parser.add_argument("--dry-run", action="store_true", help="Pokaż co zostanie zmienione bez zapisu")
    parser.add_argument("--apply", action="store_true", help="Zastosuj zmiany")
    parser.add_argument("--path-filter", default="", help="Filtruj po fragmencie ścieżki")
    args = parser.parse_args()

    if not args.dry_run and not args.apply:
        parser.error("Podaj --dry-run lub --apply")

    files = sorted(TDIR.rglob("*.md"))
    if args.path_filter:
        files = [f for f in files if args.path_filter.lower() in str(f).lower()]

    changed = 0
    errors  = 0
    skipped = 0

    for fpath in files:
        if PLACEHOLDER not in fpath.read_text(encoding="utf-8", errors="ignore"):
            skipped += 1
            continue
        result = enrich_file(fpath, dry_run=args.dry_run)
        if result:
            changed += 1
            if args.dry_run:
                print(f"  DRY: {fpath.relative_to(TDIR)}")
        else:
            errors += 1

    mode = "DRY-RUN" if args.dry_run else "ZASTOSOWANO"
    print(f"\n{mode}: zmienionych={changed}  błędów={errors}  pominiętych={skipped}")


if __name__ == "__main__":
    main()
