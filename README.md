# onepv

A collection of open-source scripts, tools, and AI skills to aid in pharmacovigilance, regulatory affairs, and clinical research.

---

## Contents

- [HighLit — Safety Literature Highlight Tool](#highlit--safety-literature-highlight-tool)
- [Claude Code Skills](#claude-code-skills)
  - [Clinical 2×2 Study Analyzer](#clinical-22-study-analyzer)
  - [Pharmaceutical Regulatory Research](#pharmaceutical-regulatory-research)
  - [Pharmacovigilance Regulatory Research](#pharmacovigilance-regulatory-research)
  - [Serialization & Track and Trace Research](#serialization--track-and-trace-research)
  - [Veterinary Regulatory Research](#veterinary-regulatory-research)

---

## HighLit — Safety Literature Highlight Tool

**Location:** [`HighLit/`](HighLit/)

An Excel/VBA tool that speeds up safety literature review in pharmacovigilance. It highlights safety-relevant keywords across literature abstracts and full-texts to help analysts quickly identify potential adverse event case reports — in line with EU GVP Module VI weekly literature monitoring requirements.

**Key features:**
- Highlights and colorizes safety keywords (severity, toxicity, study type, special populations)
- Identifies targeted medicinal products
- Flags potential case reports, meta-analyses, systematic reviews, and animal/in-vitro studies
- Converts PubMed `.txt` exports into formatted, highlighted Word documents
- Fully customizable keyword and drug lists

See the [HighLit README](HighLit/README.md) for installation and usage instructions.

---

## Claude Code Skills

**Location:** [`skills/`](skills/)

A set of structured AI skills for use with [Claude Code](https://claude.ai/code). Each skill encodes a specialist research or analysis workflow that Claude follows step-by-step.

See the [skills README](skills/README.md) for the full list and descriptions.

### Clinical 2×2 Study Analyzer

**Location:** [`skills/clinical-2x2-study-analyzer/`](skills/clinical-2x2-study-analyzer/)

Extracts binary outcome data from clinical study text and produces a full epidemiological analysis: 2×2 contingency table, relative risk, odds ratio, absolute risk reduction, NNT/NNH, 95% confidence intervals, and chi-square or Fisher exact tests. Outputs publication-ready tables and manuscript summaries.

### Pharmaceutical Regulatory Research

**Location:** [`skills/pharma-regulatory-research/`](skills/pharma-regulatory-research/)

Researches pharmaceutical product registration requirements for any country. Produces a business-plan-ready report covering registration pathways, step-by-step procedures, official fees (local currency + USD), timelines, and go/no-go business considerations — tailored to the applicant's role (local manufacturer, foreign MAH, local agent, distributor, etc.).

### Pharmacovigilance Regulatory Research

**Location:** [`skills/pv-regulatory-research/`](skills/pv-regulatory-research/)

Researches pharmacovigilance obligations for any country. Covers QPPV/local PV contact requirements, PSMF, expedited ICSR reporting timelines, PSUR/PBRER schedules, signal management, risk management plans, literature monitoring, and whether international documents (EU PSUR, EU RMP, E2B(R3)) are accepted locally. Includes a consolidated PV obligations summary table and an optional compliance readiness checklist.

### Serialization & Track and Trace Research

**Location:** [`skills/serialization-regulatory-research/`](skills/serialization-regulatory-research/)

Researches serialization and track & trace requirements for any product category in any country. Covers unique identifier structure, barcode/label technical specifications, aggregation, supply chain obligations by role, national repository registration, anti-counterfeiting requirements, implementation timelines, fees, and penalties. Includes reference tables for EU FMD/EMVS, US DSCSA, EAEU MDLP, GCC (Tatmeen/Salama), LATAM, Africa, and India.

### Veterinary Regulatory Research

**Location:** [`skills/vet-regulatory-research/`](skills/vet-regulatory-research/)

Researches veterinary product registration requirements for any country across all product categories — medicines, vaccines, medicated feed, feed additives, nutritional supplements, diagnostics, disinfectants, and pet food. Accounts for multi-authority structures, species-specific requirements (MRL and withdrawal periods for food-producing animals), and vaccine batch release obligations.

---

## License

[GNU General Public License v3.0](LICENSE)
