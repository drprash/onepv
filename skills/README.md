# Claude Skills

A collection of Claude skills for pharmacovigilance, regulatory affairs, and clinical research.

**To install a skill on claude.ai**, download its ready-made `.zip` and follow the step-by-step guide in the [main README](../README.md#how-to-install-on-claudeai).

## Skills

### [clinical-2x2-study-analyzer](clinical-2x2-study-analyzer/SKILL.md)
Extracts binary outcome data from raw clinical study text and produces a full epidemiological analysis. Builds a 2×2 contingency table, calculates relative risk, odds ratio, absolute risk reduction, NNT/NNH, 95% confidence intervals, and runs chi-square or Fisher exact tests. Confirms the extracted numbers before calculating and uses a bundled, dependency-free Python script (`scripts/analyze_2x2.py`) for exact results, falling back to the written formulas if code execution is unavailable. Outputs publication-ready tables, manuscript-ready summaries, and meta-analysis inputs (logRR, SE).

### [pharma-regulatory-research](pharma-regulatory-research/SKILL.md)
Researches pharmaceutical product registration requirements for any country and produces a structured, business-plan-ready report led by a Key Facts at a Glance table. Covers the regulatory framework (legal basis, ICH/WHO/PIC/S status), registration pathways (standard, abridged, reliance, fast track, biosimilar, generic), reliance and reference-approval acceptance (FDA, EMA, WHO PQ/CRP, regional procedures, CPP, GMP inspection waivers), step-by-step procedures, required documents, timelines, pricing approval, fees in local currency and USD, and business considerations. Tailored to the applicant's role (local manufacturer, foreign MAH, local agent, distributor, etc.). Includes an optional registration readiness checklist; known authorities and reliance mechanisms are in `references/authorities.md`.

### [pv-regulatory-research](pv-regulatory-research/SKILL.md)
Researches pharmacovigilance regulatory obligations for any country. Covers QPPV/local PV contact requirements, PSMF, expedited ICSR reporting (7-day/15-day), PSUR/PBRER aggregate reports, signal management, risk management plans, literature monitoring, and reliance on international documents. Produces a consolidated PV obligations summary table and an optional compliance readiness checklist. Regional reference notes for GCC, EU, US, LATAM, and Africa are in `references/` and loaded only for the target country's region.

### [serialization-regulatory-research](serialization-regulatory-research/SKILL.md)
Researches serialization and track & trace (T&T) requirements for any product category in any country. Covers unique identifier structure, barcode/label technical specifications, aggregation, supply chain obligations by role (MAH, manufacturer, importer, wholesaler, dispenser), national repository registration, anti-counterfeiting features, implementation timelines, fees, and penalties. Regional reference notes for EU FMD/EMVS, US DSCSA, EAEU MDLP, GCC (Tatmeen/Salama), LATAM, Africa, and India are in `references/` and loaded only for the target country's region.

### [vet-regulatory-research](vet-regulatory-research/SKILL.md)
Researches veterinary product registration requirements for any country across all product categories — veterinary medicines, vaccines and biologics, medicated feed, feed additives, nutritional supplements, diagnostics, disinfectants, and pet food. Accounts for multi-authority structures (vet medicines and feed additives are often regulated separately), species-specific requirements (MRL/withdrawal periods for food-producing animals vs. companion animals), and vaccine batch release obligations. The report is led by a Key Facts at a Glance table and includes reliance and reference-approval acceptance (EU, FDA/CVM, USDA CVB, VICH-based dossiers, Codex MRLs, local field trials), required documents, timelines, costs, and an optional registration readiness checklist. Tailored to the applicant's role and target species; known authorities by country and category are in `references/authorities.md`.
