# onepv

A collection of open-source scripts, tools, and AI skills to aid in pharmacovigilance, regulatory affairs, and clinical research.

---

## Contents

- [HighLit — Safety Literature Highlight Tool](#highlit--safety-literature-highlight-tool)
- [Claude Skills](#claude-skills)
  - [How to install on claude.ai](#how-to-install-on-claudeai)
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

## Claude Skills

**Location:** [`skills/`](skills/)

A set of structured AI skills for use with [Claude](https://claude.ai). Each skill encodes a specialist research or analysis workflow that Claude follows step-by-step. Once installed, you just ask Claude your question in a normal chat (for example, *"What are the PV requirements in Saudi Arabia?"*) and it uses the right skill automatically.

See the [skills README](skills/README.md) for the full list and descriptions.

### How to install on claude.ai

No technical knowledge is needed. You do this once per skill.

**1. Download the skill you want** (each link downloads a `.zip` file — do not unzip it):

| Skill | Download |
|-------|----------|
| Clinical 2×2 Study Analyzer | [clinical-2x2-study-analyzer.zip](https://github.com/drprash/onepv/releases/latest/download/clinical-2x2-study-analyzer.zip) |
| Pharmaceutical Regulatory Research | [pharma-regulatory-research.zip](https://github.com/drprash/onepv/releases/latest/download/pharma-regulatory-research.zip) |
| Pharmacovigilance Regulatory Research | [pv-regulatory-research.zip](https://github.com/drprash/onepv/releases/latest/download/pv-regulatory-research.zip) |
| Serialization & Track and Trace Research | [serialization-regulatory-research.zip](https://github.com/drprash/onepv/releases/latest/download/serialization-regulatory-research.zip) |
| Veterinary Regulatory Research | [vet-regulatory-research.zip](https://github.com/drprash/onepv/releases/latest/download/vet-regulatory-research.zip) |

**2. Turn on code execution** (one-time setup)
- Go to **Settings → Capabilities** and switch on **Code execution and file creation**.
- On a Team or Enterprise plan, your workspace owner may need to enable **Skills** and code execution for the organisation first.

**3. Upload the skill**
- Go to **Customize → Skills**.
- Click **+**, then **+ Create skill**, then **Upload a skill**.
- Choose the `.zip` file you downloaded.
- The skill now appears in your skills list. Make sure its switch is **on**.

**4. Use it**
- Start a new chat and ask your question in plain language.
- For the regulatory research skills, make sure **Web search** is turned on in the chat's tools menu — these skills look up current official sources.
- Claude will first ask a few questions about your product and situation. Answer them as best you can; the answers shape the whole report.

**Tips**
- **One country per chat.** For a multi-country comparison, research each country in its own chat, then compare the results.
- **Updating a skill.** The download links above always give the newest version (see [Releases](https://github.com/drprash/onepv/releases) for what changed). To update, download the `.zip` again, delete the old skill from **Customize → Skills**, and upload the new one.
- **Upload failed?** Make sure you uploaded the `.zip` file exactly as downloaded, without unzipping or renaming it.

> Menu names on claude.ai change from time to time. If anything above doesn't match what you see, follow Anthropic's official guide: [Using Skills in Claude](https://support.claude.com/en/articles/12512180-using-skills-in-claude).

**For maintainers:** pushing a change under `skills/` to `main` automatically validates and packages every skill and publishes a new GitHub Release ([workflow](.github/workflows/release-skills.yml)). To check a skill locally before pushing, run `python3 scripts/package_skills.py` (writes `dist/*.zip`, which is git-ignored).

### Clinical 2×2 Study Analyzer

**Location:** [`skills/clinical-2x2-study-analyzer/`](skills/clinical-2x2-study-analyzer/)

Extracts binary outcome data from clinical study text and produces a full epidemiological analysis: 2×2 contingency table, relative risk, odds ratio, absolute risk reduction, NNT/NNH, 95% confidence intervals, and chi-square or Fisher exact tests. Confirms the extracted numbers with you first, then uses a bundled calculation script for exact results. Outputs publication-ready tables and manuscript summaries.

### Pharmaceutical Regulatory Research

**Location:** [`skills/pharma-regulatory-research/`](skills/pharma-regulatory-research/)

Researches pharmaceutical product registration requirements for any country. Produces a business-plan-ready report that opens with a key-facts summary, then covers the regulatory framework, registration pathways, which foreign approvals are accepted (FDA, EMA, WHO, regional procedures, CPP), step-by-step procedures, required documents, timelines, pricing approval, official fees (local currency + USD), and go/no-go business considerations — tailored to the applicant's role (local manufacturer, foreign MAH, local agent, distributor, etc.). Includes an optional registration readiness checklist.

### Pharmacovigilance Regulatory Research

**Location:** [`skills/pv-regulatory-research/`](skills/pv-regulatory-research/)

Researches pharmacovigilance obligations for any country. Covers QPPV/local PV contact requirements, PSMF, expedited ICSR reporting timelines, PSUR/PBRER schedules, signal management, risk management plans, literature monitoring, and whether international documents (EU PSUR, EU RMP, E2B(R3)) are accepted locally. Includes a consolidated PV obligations summary table, an optional compliance readiness checklist, and reference notes for GCC, EU, US, LATAM, and Africa.

### Serialization & Track and Trace Research

**Location:** [`skills/serialization-regulatory-research/`](skills/serialization-regulatory-research/)

Researches serialization and track & trace requirements for any product category in any country. Covers unique identifier structure, barcode/label technical specifications, aggregation, supply chain obligations by role, national repository registration, anti-counterfeiting requirements, implementation timelines, fees, and penalties. Includes reference tables for EU FMD/EMVS, US DSCSA, EAEU MDLP, GCC (Tatmeen/Salama), LATAM, Africa, and India.

### Veterinary Regulatory Research

**Location:** [`skills/vet-regulatory-research/`](skills/vet-regulatory-research/)

Researches veterinary product registration requirements for any country across all product categories — medicines, vaccines, medicated feed, feed additives, nutritional supplements, diagnostics, disinfectants, and pet food. Produces a report that opens with a key-facts summary and covers which authorities govern the product, registration pathways, which foreign approvals and dossiers are accepted, required documents, timelines, and costs. Accounts for multi-authority structures, species-specific requirements (MRL and withdrawal periods for food-producing animals), and vaccine batch release obligations. Includes an optional registration readiness checklist.

---

## License

[GNU General Public License v3.0](LICENSE)
