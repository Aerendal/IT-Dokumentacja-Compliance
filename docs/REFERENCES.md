# Źródła referencyjne i standardy odniesienia

Ten dokument zbiera **autorytatywne źródła**, do których odwołuje się repozytorium przy projektowaniu szablonów, zasad walidacji, praktyk dokumentacyjnych i kontroli jakości.

## Zasady korzystania z tego dokumentu

1. **Priorytet mają źródła pierwotne**:
   - akty prawne: oficjalny tekst w EUR-Lex / Komisji Europejskiej,
   - normy: oficjalna strona ISO / IEEE,
   - frameworki i wytyczne: oficjalne strony NIST, OWASP, Cucumber, RFC Editor.

2. **Nie kopiujemy treści norm płatnych.**  
   Dla norm ISO/IEC/IEEE i części standardów IEEE linkujemy do **oficjalnych stron standardów**, a nie reprodukujemy ich treści.

3. **Linki w dokumentach repo powinny prowadzić do stabilnych identyfikatorów**:
   - EUR-Lex / ELI / CELEX,
   - DOI NIST,
   - RFC Editor / RFC info,
   - oficjalne landing pages standardów.

4. Ten dokument ma pokazać, że repo **nie wymyśla standardów od nowa**, tylko opiera się na uznanych źródłach.

---

# 1. Bezpieczeństwo informacji / compliance / governance

## ISO / IEC

- [ISO/IEC 27001:2022 — Information security management systems — Requirements](https://www.iso.org/standard/27001)  
  Oficjalna strona normy dla ISMS. Podstawowy punkt odniesienia dla polityk, procedur, rejestrów ryzyk, SoA i dokumentacji bezpieczeństwa.

- [ISO/IEC 27002:2022 — Information security controls](https://www.iso.org/standard/75652.html)  
  Oficjalna strona normy opisującej katalog i logikę kontroli bezpieczeństwa wspierających wdrożenia zgodne z ISO/IEC 27001.

## NIST

- [NIST Cybersecurity Framework (CSF) 2.0 — project page](https://www.nist.gov/cyberframework)  
  Oficjalny punkt wejścia do CSF 2.0: framework, quick-start guides, profiles i mappings.

- [NIST CSF 2.0 — publikacja (NIST CSWP 29)](https://www.nist.gov/publications/nist-cybersecurity-framework-csf-20)  
  Oficjalna publikacja NIST dla CSF 2.0.

- [NIST Privacy Framework 1.0 — official page](https://www.nist.gov/privacy-framework/privacy-framework)  
  Oficjalny framework NIST do zarządzania ryzykiem prywatności.

- [NIST SP 800-53 Rev. 5 — Security and Privacy Controls](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)  
  Oficjalny katalog kontroli bezpieczeństwa i prywatności dla organizacji i systemów.

- [NIST SP 800-53A Rev. 5 — Assessing Security and Privacy Controls](https://csrc.nist.gov/pubs/sp/800/53/a/r5/final)  
  Oficjalne procedury i podejście do oceny kontroli z rodziny 800-53.

- [NIST SP 800-61 Rev. 3 — Incident Response Recommendations and Considerations](https://csrc.nist.gov/pubs/sp/800/61/r3/final)  
  Oficjalne wytyczne NIST dla reagowania na incydenty w powiązaniu z CSF 2.0.

- [NIST SP 800-115 — Technical Guide to Information Security Testing and Assessment](https://csrc.nist.gov/pubs/sp/800/115/final)  
  Oficjalny przewodnik do technicznych testów i ocen bezpieczeństwa.

- [NIST SP 800-218 — Secure Software Development Framework (SSDF)](https://csrc.nist.gov/pubs/sp/800/218/final)  
  Oficjalny framework bezpiecznego wytwarzania oprogramowania.

- [NIST AI RMF 1.0 — Artificial Intelligence Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)  
  Oficjalny framework zarządzania ryzykiem AI; przydatny, jeśli repo obejmuje dokumentację AI / ML.

- [NIST AI RMF 1.0 — publikacja (NIST AI 100-1)](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10)  
  Oficjalna publikacja NIST dla AI RMF 1.0.

## ENISA / UE — praktyka i otoczenie regulacyjne

- [ENISA — official website](https://www.enisa.europa.eu/)  
  Europejska Agencja ds. Cyberbezpieczeństwa; dobre źródło materiałów wdrożeniowych, raportów i kontekstu operacyjnego dla regulacji UE.

---

# 2. Prawo UE i źródła legislacyjne

## Akty prawne UE — teksty oficjalne

- [GDPR / RODO — Regulation (EU) 2016/679 (ELI)](https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng)  
  Oficjalny tekst rozporządzenia.

- [NIS2 — Directive (EU) 2022/2555 (ELI)](https://eur-lex.europa.eu/eli/dir/2022/2555/oj/eng)  
  Oficjalny tekst dyrektywy NIS2.

- [DORA — Regulation (EU) 2022/2554 (ELI)](https://eur-lex.europa.eu/eli/reg/2022/2554/oj/eng)  
  Oficjalny tekst rozporządzenia DORA.

## Portale i strony urzędowe UE

- [European Commission — Data protection](https://commission.europa.eu/law/law-topic/data-protection/eu-data-protection-rules_en)  
  Oficjalny portal Komisji Europejskiej do prawa ochrony danych.

- [European Commission — Legal framework of EU data protection](https://commission.europa.eu/law/law-topic/data-protection/data-protection-eu_en)  
  Oficjalne objaśnienia i punkt wejścia do ram prawnych ochrony danych w UE.

- [EUR-Lex — official portal](https://eur-lex.europa.eu/)  
  Oficjalny portal do prawa UE; podstawowe źródło dla CELEX / ELI / OJ.

---

# 3. Architektura, wymagania i dokumentacja techniczna

## Normy architektury i inżynierii systemów

- [ISO/IEC/IEEE 42010:2022 — Architecture description](https://www.iso.org/standard/74393.html)  
  Oficjalny punkt odniesienia dla opisu architektury, viewpoints i wymagań wobec architecture description.

- [ISO/IEC/IEEE 29148:2018 — Requirements engineering](https://www.iso.org/standard/72089.html)  
  Oficjalny punkt odniesienia dla inżynierii wymagań i informacji wynikowych requirements engineering.

- [ISO/IEC/IEEE 15288:2023 — System life cycle processes](https://www.iso.org/standard/81702.html)  
  Oficjalny punkt odniesienia dla procesów cyklu życia systemów.

- [ISO/IEC/IEEE 12207:2017 — Software life cycle processes](https://www.iso.org/standard/63712.html)  
  Oficjalny punkt odniesienia dla procesów cyklu życia oprogramowania.

## ADR — Architecture Decision Records

> Uwaga: ADR nie są formalną normą ISO/IEEE. To **uznana praktyka de facto** dokumentowania decyzji architektonicznych.

- [ADR organization / ADR knowledge hub](https://adr.github.io/)  
  Najbardziej użyteczny punkt wejścia do pojęcia ADR, motywacji, definicji i odnośników.

- [MADR — Markdown Architectural Decision Records](https://adr.github.io/madr/)  
  Uznany, lekki format ADR oparty o Markdown; dobry punkt odniesienia dla własnych szablonów decyzji.

- [Decision Capturing Tools](https://adr.github.io/adr-tooling/)  
  Przegląd narzędzi i praktyk wokół ADR; przydatne do wyboru stylu pracy z decyzjami.

---

# 4. BDD / Gherkin / specyfikacje wykonywalne

- [Gherkin — official documentation](https://cucumber.io/docs/gherkin/)  
  Oficjalna dokumentacja Gherkina jako języka specyfikacji wykonywalnych.

- [Gherkin Reference](https://cucumber.io/docs/gherkin/reference)  
  Oficjalny referencyjny opis składni, słów kluczowych, przykładów, `Scenario`, `Rule`, `Background`, tabel i doc strings.

---

# 5. Testowanie i jakość

## Normy i standardy testowania

- [ISO/IEC/IEEE 29119-2:2021 — Software testing — Part 2: Test processes](https://www.iso.org/standard/79428.html)  
  Oficjalny punkt odniesienia dla procesów testowych.

- [ISO/IEC/IEEE 29119-3:2021 — Software testing — Part 3: Test documentation](https://www.iso.org/standard/79429.html)  
  Oficjalny punkt odniesienia dla dokumentacji testowej i szablonów dokumentów testowych.

- [IEEE 1012-2024 — System, Software, and Hardware Verification and Validation](https://standards.ieee.org/ieee/1012/7324)  
  Oficjalny standard IEEE dla V&V.

## Praktyki NIST / AppSec / testy techniczne

- [NIST SP 800-115 — Technical Guide to Information Security Testing and Assessment](https://csrc.nist.gov/pubs/sp/800/115/final)  
  Oficjalny przewodnik NIST dla testów technicznych, assessmentów i testów bezpieczeństwa.

- [OWASP Application Security Verification Standard (ASVS)](https://owasp.org/www-project-application-security-verification-standard/)  
  Oficjalny standard OWASP dla wymagań bezpieczeństwa aplikacji i weryfikacji technicznych kontroli.

- [OWASP Web Security Testing Guide (project page)](https://owasp.org/www-project-web-security-testing-guide/)  
  Oficjalny punkt wejścia do WSTG.

- [OWASP Web Security Testing Guide — stable](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/)  
  Stabilna wersja WSTG do linkowania w repo i dokumentacji.

> Jeżeli odwołujesz się do konkretnych scenariuszy WSTG, używaj **linków wersjonowanych**, nie `latest`, aby uniknąć rozjazdów między wersjami.

---

# 6. Język normatywny i styl specyfikacji

- [RFC 2119 — Key words for use in RFCs to Indicate Requirement Levels](https://www.rfc-editor.org/info/rfc2119)  
  Oficjalne znaczenie słów typu MUST, SHOULD, MAY.

- [RFC 8174 — Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words](https://www.rfc-editor.org/info/rfc8174)  
  Uzupełnienie RFC 2119: znaczenie specjalne dotyczy słów zapisanych WIELKIMI LITERAMI.

---

# 7. Źródła pomocnicze dla dokumentacji bezpieczeństwa i prywatności

- [NIST Privacy Framework 1.0](https://www.nist.gov/privacy-framework/privacy-framework)  
  Przydatne jako uzupełnienie dla dokumentacji prywatności, DPIA, governance i ryzyka przetwarzania danych.

- [European Commission — data protection portal](https://commission.europa.eu/law/law-topic/data-protection/eu-data-protection-rules_en)  
  Dobry oficjalny punkt wejścia do objaśnień wokół GDPR / ochrony danych.

- [NIST SP 800-53A Rev. 5](https://csrc.nist.gov/pubs/sp/800/53/a/r5/final)  
  Przydatne, gdy repo ma wspierać nie tylko katalog kontroli, ale też sposób ich oceny.

---

# 8. Jak używać tych źródeł w repo

## Dla standardów i prawa
W dokumentach repo najlepiej odwoływać się do:
- **konkretnego aktu** (np. GDPR / NIS2 / DORA),
- **konkretnej normy** (np. ISO/IEC 27001, 27002, 29119, 42010),
- **konkretnej publikacji NIST** (np. CSF 2.0, SP 800-115, SP 800-218).

## Dla ADR
Odwołuj się do ADR jako do **praktyki dokumentacyjnej**, nie jako do normy formalnej.

## Dla testów
Łącz:
- normy procesowe i dokumentacyjne (ISO/IEC/IEEE 29119),
- standard V&V (IEEE 1012),
- praktyczne przewodniki techniczne (NIST, OWASP),
- specyfikacje wykonywalne (Gherkin / Cucumber).

---

# 9. Uwagi końcowe

1. Repo nie twierdzi, że samo posiadanie szablonów oznacza automatyczną zgodność certyfikacyjną lub regulacyjną.
2. Szablony i narzędzia powinny być interpretowane jako wsparcie procesu dokumentacyjnego, walidacyjnego i audytowego.
3. Ostateczna zgodność zależy od:
   - sposobu wdrożenia,
   - treści wypełnionych dokumentów,
   - kontekstu organizacyjnego,
   - audytu / oceny po stronie danej organizacji.
