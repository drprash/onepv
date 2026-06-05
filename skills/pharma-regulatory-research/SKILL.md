---
name: pharma-regulatory-research
description: >
  Research pharmaceutical product registration requirements for a specific country and produce
  a structured business-plan-ready summary. Use this skill whenever the user asks about:
  drug registration, pharmaceutical regulatory approval, medicine registration pathways,
  product dossier submission, regulatory authority requirements, pharma market entry,
  registration fees or costs, drug approval timelines, or how to register a pharmaceutical
  product in any country. Also trigger for queries like "how do I register my drug in [country]",
  "what are the regulatory requirements for [country]", "pharma market entry in [country]",
  "cost of drug registration in [country]", or any request to evaluate the regulatory feasibility
  or cost-benefit of entering a pharmaceutical market. Always use this skill when pharmaceutical
  registration research is involved — even if the user only mentions one section (e.g., just costs
  or just timelines), apply the full structured workflow below.
---

# Pharmaceutical Regulatory Research Skill

## Purpose
Produce a structured, business-plan-ready summary of pharmaceutical product registration requirements
for a given country. The output supports cost-benefit analysis and go/no-go market entry decisions.

The applicant's role in the target market materially changes which pathways are open, which fees apply,
and whether a local agent or manufacturer is mandatory. This skill therefore **elicits the company's
role from the user** and tailors the entire analysis to it.

---

## Workflow

### Step 1 — Clarify Inputs (ask the user; never assume)

Before researching, confirm the following. **Do not hardcode or guess the company role** — it must come
from the user. Ask all questions together in one prompt.

- **Country / target market** (required)
- **Product type** — small molecule, biologic, biosimilar, generic, OTC, medical device, combination
  product, etc.
- **Origin / reference approval** — Is the product already approved in a reference jurisdiction
  (US FDA, EMA, ICH member, WHO PQ, etc.)? This affects abridged/recognition pathway eligibility.
- **Company role in the target market** (required — this drives pathway, fee, and obligation analysis):
  - **Local manufacturer** — manufactures within the target country
  - **Foreign manufacturer (MAH/marketing authorization holder)** — manufactures abroad, holds the registration
  - **Local agent / authorized representative** — represents a foreign MAH locally
  - **Distributor / importer** — imports and distributes an already- or to-be-registered product
  - **Licensing-in / in-country partner** — registers under a local partner arrangement
  - **Other** — capture in the user's own words
- **Stage / objective** — new registration, renewal, variation, or feasibility/cost-benefit study only

If any required field is missing, ask before proceeding. Tailor everything downstream to the stated role
(see "Role-Based Tailoring" below).

---

### Step 2 — Identify the Regulatory Authority

Search for the **official regulatory authority** responsible for pharmaceutical registration in the target
country. Examples:
- UAE → EDE (Emirates Drug Establishment, federal — now the primary authority for marketing
  authorizations, establishment licensing, import/export permits, GMP, and pharmacovigilance under
  Federal Decree-Law No. 38 of 2024); MOHAP retains community/compounding pharmacies; emirate-level
  authorities (DHA, DoH Abu Dhabi) relevant for local licensing/pricing
- Saudi Arabia → SFDA (Saudi Food and Drug Authority)
- Egypt → EDA (Egyptian Drug Authority)
- India → CDSCO (Central Drugs Standard Control Organization)
- EU → EMA (centralized) plus national competent authorities
- US → FDA (CDER for drugs, CBER for biologics)
- UK → MHRA

**Search queries to use:**
- `"[country] pharmaceutical drug registration authority official site"`
- `"[country] medicine regulatory agency drug approval"`

Always find and use **official government / authority URLs** (.gov, .gov.xx, or known authority domains).
Avoid third-party summaries as primary sources — fetch the primary-source pages directly.

---

### Step 3 — Research Each Section

Use `web_search` and `web_fetch`. **Always include the current year in time-sensitive queries** (fees,
timelines, latest guidance) to avoid stale results — e.g., `"[country] drug registration fees 2026"`.
For each section, track every **source URL** accessed and the **last-updated date** of each page where
visible — all will be listed in the References section.

**Source priority rules:**
- **Registration Pathways & Procedures:** Use official government/authority sources first and exclusively
  where available.
- **Fee schedules & Timelines:** Use official sources first. If official sources do not publish fee
  schedules or timelines, **unofficial sources are permitted** (regulatory consultancy sites, RAPS,
  industry publications, law-firm regulatory summaries, etc.) — but must be clearly labeled as
  `[Unofficial source: name]` inline wherever the data is cited.
- **Recency:** Prefer pages updated within the last 18–24 months. Flag any figure drawn from an older page.
- **Never fabricate data.** If no source (official or unofficial) is found for a specific figure, state:
  *"Not publicly available — recommend direct inquiry with [Authority Name]."*

#### Section 1: Registration Pathways
Identify ALL available registration pathways relevant to the product type AND the company's stated role,
such as:
- **Standard / Full Review** — complete dossier, no prior reference approval
- **Abridged / Expedited** — based on approval in a reference country (US FDA, EMA, ICH, WHO PQ)
- **Mutual Recognition / Reliance** — based on another regulator's approval
- **Fast Track / Priority Review** — for urgent or unmet medical needs
- **Biosimilar pathway** (if applicable)
- **Generic registration pathway**
- **OTC vs. Prescription pathways**
- **Parallel import** (if applicable)
- **Renewal / Variation pathways**

For each pathway, note:
- Eligibility criteria
- Reference jurisdictions accepted (if any)
- Whether local clinical / bridging data is required
- **Role-specific restrictions** — e.g., whether a local agent is mandatory for a foreign manufacturer,
  whether a distributor can be the applicant, local-manufacturing prerequisites, etc.

#### Section 2: Procedures for Registration (per pathway)

For each identified pathway, document:

**Registration Steps** (numbered sequence):
1. Pre-submission / dossier preparation requirements
2. Account / portal setup (if online submission)
3. Application submission (format: eCTD, NeeS, paper, etc.)
4. Screening / completeness check
5. Technical / scientific review
6. Inspection (if required — GMP, site, manufacturing)
7. Pricing & reimbursement review (if part of registration)
8. Approval & certificate issuance
9. Post-approval obligations (pharmacovigilance, PSUR/PBRER, renewals, etc.)

**Costs per Step** (in local currency AND USD equivalent):
- Application fees
- Review fees
- GMP inspection fees (local vs. overseas inspection)
- Certificate fees
- Annual registration / renewal fees
- Agent / local representative fees (if mandatory)
- Any other official fees

Search specifically for the authority's **official fee schedule** page (often called "tariff",
"fee schedule", "registration fees", or similar). If unavailable, use reputable consultancy/industry
sources labeled `[Unofficial source: name]`.

#### Section 3: Timelines

For each pathway, document:
- Screening / completeness review: X weeks
- Scientific review: X months
- Clock-stop periods (when the clock pauses for applicant responses)
- GMP inspection scheduling: X months
- Total typical timeline: X–Y months
- Any published regulatory targets (KPIs) vs. real-world experience if available

If official timeline targets are not published, use reputable consultancy/industry estimates labeled
`[Unofficial source: name]`.

#### Section 4: Total Cost Summary

Produce a consolidated cost table:

| Cost Item | Amount (Local Currency) | Amount (USD) | Source | Notes |
|-----------|------------------------|--------------|--------|-------|
| Application fee | | | | |
| Dossier review fee | | | | |
| GMP inspection (if required) | | | | |
| Registration certificate | | | | |
| Annual renewal fee | | | | |
| Local agent fee (estimate) | | | | |
| **TOTAL (one-time)** | | | | |
| **TOTAL (annual recurring)** | | | | |

Include ranges where costs vary by product type, pathway, or company role.

---

### Step 4 — Format the Output

Produce the final report in this structure:

---

## Pharmaceutical Registration Research: [Country]
**Product Type:** [as specified]
**Company Role:** [as specified by user]
**Regulatory Authority:** [Name + official website]
**Research Date:** [today's date]

---

### 1. Registration Pathways
[Pathway table or structured list with eligibility criteria and role-specific restrictions]

### 2. Registration Procedures

#### Pathway A: [Name]
**Steps:**
1. ...

**Costs:**
- Step X fee: [amount]

#### Pathway B: [Name]
...

### 3. Timelines
[Timeline table per pathway — label any unofficial figures as `[Unofficial source: name]`]

### 4. Total Cost Summary
[Cost table as defined above — label any unofficial figures as `[Unofficial source: name]`]

### 5. Business Considerations
Provide a brief (3–5 bullet) business-plan-oriented summary tailored to the company's role:
- Is the registration environment favorable or complex for this role?
- Any notable risks (local clinical data, long timelines, mandatory local agent/manufacturer)?
- Estimated time-to-market
- Key cost drivers
- Competitive / strategic notes (e.g., reliance shortcuts available, first-mover considerations)

### 6. Confidence & Caveats
- Note where data is official vs. unofficial vs. unavailable.
- Flag any figures from pages older than ~2 years.
- State that fees/timelines change and should be confirmed with the authority before final decisions.

---

### References

List **every URL consulted**, grouped by type. Include all sources — official and unofficial — with the
page's last-updated date where available.

**Official Sources**
1. [Authority Name] — [Full URL] — [What was found] — [Last updated: date]

**Unofficial Sources**
1. [Site/Publication Name] — [Full URL] — [What was found; fees or timelines?] — [Last updated: date]

> Note: Unofficial sources are used solely where official fee schedules or timeline data were not publicly
> available. All unofficial data is labeled inline throughout the report.

---

## Role-Based Tailoring (apply throughout)

The stated company role changes the analysis. Apply these lenses:

- **Local manufacturer** — focus on domestic manufacturing license + GMP, typically lower fees, no foreign
  inspection, may unlock local-manufacturer-only pathways or incentives.
- **Foreign manufacturer (MAH)** — almost always requires a local agent/authorized representative; expect
  overseas GMP inspection fees and legalization/apostille of documents.
- **Local agent / authorized representative** — clarify liability, who holds the registration, and agent
  appointment requirements; relevant when the user acts on behalf of a foreign MAH.
- **Distributor / importer** — focus on import licensing, whether the distributor can be the applicant, and
  product-already-registered scenarios.
- **Licensing-in / partner** — focus on technology-transfer and partner-as-applicant arrangements.

If the role implies a mandatory local entity the user may not have, flag it explicitly as a market-entry
prerequisite.

---

## Research Quality Standards

- **Official sources first, always.** For pathways and procedures, use only official government/authority sources.
- **Unofficial sources permitted for fees & timelines only**, labeled `[Unofficial source: name]` inline.
- **Track every URL** in the References section, with last-updated dates where visible.
- **Currency conversion.** Use the approximate current exchange rate; state the rate and date used
  (e.g., "1 USD ≈ 3.67 AED as of [date]"). Verify the rate via search rather than assuming.
- **Recency.** Include the current year in fee/timeline searches. Flag any page last updated more than
  2 years ago as potentially outdated.
- **Don't fabricate.** If no source is found, state: *"Not publicly available — recommend direct inquiry
  with [Authority Name]."*
- **Cite sources** for every figure that comes from search results.

---

## Common Official Source Patterns to Search

| Country | Authority | Typical URL pattern |
|---------|-----------|-------------------|
| UAE | EDE (federal; MOHAP for community/compounding pharmacies) | ede.gov.ae · mohap.gov.ae |
| Saudi Arabia | SFDA | sfda.gov.sa |
| Egypt | EDA | edaegypt.gov.eg |
| Jordan | JFDA | jfda.jo |
| Kuwait | MOH | moh.gov.kw |
| Pakistan | DRAP | dra.gov.pk |
| India | CDSCO | cdsco.gov.in |
| UK | MHRA | gov.uk/government/organisations/medicines-and-healthcare-products-regulatory-agency |
| EU | EMA | ema.europa.eu |
| US | FDA | fda.gov |
| Canada | Health Canada | canada.ca/en/health-canada |
| Australia | TGA | tga.gov.au |
| Singapore | HSA | hsa.gov.sg |
| South Africa | SAHPRA | sahpra.org.za |
| Nigeria | NAFDAC | nafdac.gov.ng |
| Kenya | PPB | pharmacyboardkenya.org |

For unlisted countries, search: `"[country] pharmaceutical regulatory authority official"` and look for
`.gov` or equivalent government domains. Verify the current official domain by search, as authority URLs
and agency names change over time.

> **Authority changes are common — verify before relying on prior knowledge.** Regulators are reorganized,
> renamed, and merged. (Example: in the UAE, the **EDE** progressively absorbed pharmaceutical functions
> from MOHAP through end-2025 under Federal Decree-Law No. 38 of 2024 — many sources still cite MOHAP.)
> Always confirm the current responsible authority and portal by search rather than assuming.

---

## Output Format Notes

- Use tables wherever data has multiple attributes (pathways, costs, timelines)
- Use numbered steps for procedures
- Use clear headers matching the required sections
- Keep the Business Considerations section concise — it's for executive readers
- If producing as a document (Word/PDF), use the docx or pdf skill accordingly
