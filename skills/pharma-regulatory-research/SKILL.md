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

Before researching, confirm the following in a single prompt. Flag which are required vs. helpful.
**Do not hardcode or guess the company role** — it must come from the user. Many users are not
regulatory specialists: offer the options below in plain language and accept "not sure".

**Required:**
- **Country / target market**
- **Product type:**
  - Small molecule / chemical medicine (new or innovator)
  - Generic medicine
  - Biologic / biosimilar
  - Vaccine
  - OTC / non-prescription medicine
  - Medical device or combination product — see scope note below
  - Not sure (describe the product)
- **Company role in the target market** (drives pathway, fee, and obligation analysis):
  - **Local manufacturer** — manufactures within the target country
  - **Foreign manufacturer (MAH / marketing authorization holder)** — manufactures abroad, holds the registration
  - **Local agent / authorized representative** — represents a foreign MAH locally
  - **Distributor / importer** — imports and distributes an already- or to-be-registered product
  - **Licensing-in / in-country partner** — registers under a local partner arrangement
  - **Other** — capture in the user's own words

**Helpful (ask; proceed with best assumptions if not provided):**
- **Reference approval** — Is the product already approved elsewhere (US FDA, EMA, UK MHRA, another
  ICH member, WHO PQ)? This drives reliance/abridged pathway eligibility (Section 3).
- **Stage / objective** — new registration, renewal, variation, or feasibility/cost-benefit study only.
  Default: new registration.
- **Registration readiness checklist wanted?** — If the user is preparing a submission, offer the
  optional checklist at the end of the report.

If a required field is missing, ask before proceeding. If the user answers "not sure" to a helpful
field, assume the most common case, state the assumption at the top of the report, and continue.
Tailor everything downstream to the stated role (see "Role-Based Tailoring" below).

> **Scope note — devices and combination products.** Medical devices and IVDs are usually regulated
> under a separate device framework (classification, conformity assessment, device registration).
> This skill is built for medicines. For a device, tell the user so and, if they still want it,
> research the device regime with the same report structure while flagging reduced coverage. For a
> combination product, first establish which regime applies (typically by primary mode of action).

---

### Step 2 — Identify the Regulatory Authority

Search for the **official regulatory authority** responsible for pharmaceutical registration in the
target country. Read `references/authorities.md` first — it lists known authorities and the common
reliance/harmonization mechanisms — and treat it as a starting point only.

Also identify:
- The authority's **submission portal** and accepted dossier format (eCTD, NeeS, ACTD, paper)
- **ICH membership / observer status** and **WHO GBT maturity level** (if benchmarked)
- **Regional harmonization or reliance frameworks** the country participates in (GCC, ASEAN, AMA /
  AVAREF, EAC, WHO CRP, Access Consortium, etc.)

**Search queries to use:**
- `"[country] pharmaceutical drug registration authority official site"`
- `"[country] medicine regulatory agency drug approval [current year]"`

Always find and use **official government / authority URLs** (.gov, .gov.xx, or known authority domains).
Avoid third-party summaries as primary sources — fetch the primary-source pages directly.

> **Authority changes are common — verify before relying on prior knowledge.** Regulators are
> reorganized, renamed, and merged (e.g., UAE: EDE took over registration from MOHAP under Federal
> Decree-Law No. 38 of 2024 — many sources still cite MOHAP). Always confirm the current responsible
> authority and portal by search.

---

### Step 3 — Research Each Section

Use `web_search` and `web_fetch`. **Always include the current year in time-sensitive queries** (fees,
timelines, latest guidance) to avoid stale results — e.g., `"[country] drug registration fees 2026"`.
For each section, track every **source URL** accessed and the **last-updated date** of each page where
visible — all will be listed in the References section.

**Source priority rules:**
- **Framework, Pathways, Reliance, Procedures & Documents:** Use official government/authority sources
  first and exclusively where available.
- **Fee schedules & Timelines:** Use official sources first. If official sources do not publish fee
  schedules or timelines, **unofficial sources are permitted** (regulatory consultancy sites, RAPS,
  industry publications, law-firm regulatory summaries, etc.) — but must be clearly labeled as
  `[Unofficial source: name]` inline wherever the data is cited.
- **Recency:** Prefer pages updated within the last 18–24 months. Flag any figure drawn from an older page.
- **Never fabricate data.** If no source (official or unofficial) is found for a specific figure, state:
  *"Not publicly available — recommend direct inquiry with [Authority Name]."*

**Immature / unpublished framework protocol (apply when the country lacks published guidance):**
1. **Flag the gap explicitly** — state that no published guideline was found for that area.
2. **Research the proxy framework** — identify which international or regional standards the country
   has formally adopted (ICH CTD, WHO guidelines, ASEAN ACTD, GCC guidelines, EAC/SADC harmonized
   requirements). These become the operative framework until country-specific guidance is published.
   Mark every proxy-derived item with 🔶.
3. **Recommend direct inquiry** — give the authority's contact details and suggest engaging a local
   regulatory consultant familiar with the authority's unpublished expectations.

#### Section 1: Regulatory Framework Overview
- Full name of the authority + official website + submission portal
- Primary legislation (law/decree number and year) and key implementing regulations
- ICH membership / observer status; WHO GBT maturity level; PIC/S membership
- Regional harmonization / reliance frameworks the country participates in
- Local-entity requirements (must the MAH be a local company? is a local agent mandatory?)
- Any recent regulatory changes (last 2–3 years) — flag prominently with ⚠️

#### Section 2: Registration Pathways
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

#### Section 3: Reliance & Reference Approval Acceptance

Research and state explicitly for **each** row whether the country accepts it, and what it changes.
Every row must be filled; "Not found" is acceptable only after a genuine search, paired with the
"recommend direct inquiry" note.

| Reference / Mechanism | Accepted? | Effect (abridged review / waiver / shorter timeline) | Conditions | Source |
|-----------------------|-----------|------------------------------------------------------|------------|--------|
| US FDA approval | | | | |
| EMA / EU approval | | | | |
| Other reference regulators (MHRA, Health Canada, TGA, Swissmedic, PMDA) | | | | |
| WHO Prequalification / Collaborative Registration Procedure | | | | |
| Regional procedure (GCC centralized, ASEAN, AMA / AVAREF, EAC, etc.) | | | | |
| Work-sharing (Access Consortium, Project Orbis) | | | | |
| CPP required? From which country? Must product be marketed there? | | | | |
| GMP inspection waiver based on reference / PIC/S inspection | | | | |
| Local clinical / bridging data waiver | | | | |

#### Section 4: Procedures for Registration (per pathway)

For each identified pathway, document:

**Registration Steps** (numbered sequence):
1. Pre-submission / dossier preparation requirements
2. Account / portal setup (if online submission)
3. Application submission (format: eCTD, NeeS, ACTD, paper, etc.)
4. Screening / completeness check
5. Technical / scientific review
6. Laboratory testing of samples (if required)
7. Inspection (if required — GMP, site, manufacturing)
8. Pricing approval (if linked to registration — see Section 7)
9. Approval & certificate issuance
10. Post-approval obligations (pharmacovigilance, PSUR/PBRER, renewals, etc.)

**Costs per Step** (in local currency AND USD equivalent):
- Application fees
- Review fees
- Laboratory analysis fees
- GMP inspection fees (local vs. overseas inspection)
- Certificate fees
- Annual registration / renewal fees
- Agent / local representative fees (if mandatory)
- Any other official fees

Search specifically for the authority's **official fee schedule** page (often called "tariff",
"fee schedule", "registration fees", or similar). If unavailable, use reputable consultancy/industry
sources labeled `[Unofficial source: name]`.

#### Section 5: Required Documents

List the documents the authority requires, using its published checklist where available:

| Document | Required? | Legalization / apostille? | Notes |
|----------|-----------|---------------------------|-------|
| CPP (WHO format) | | | Issuing country; validity period |
| GMP certificate (each manufacturing site) | | | Accepted issuing authorities |
| Free Sale Certificate | | | |
| Manufacturing licence | | | |
| Agent agreement / power of attorney | | | |
| Company / establishment licence (local) | | | |
| Dossier (CTD Modules 1–5 + local Module 1) | | | Format and language |
| Stability data | | | Required climatic zone (e.g., IVa / IVb) |
| Bioequivalence study (generics) | | | Local reference product required? |
| Labelling, PIL and artwork in local language | | | Language(s) required |
| Samples and reference standards | | | Quantity; for authority laboratory testing |
| Price certificates from other countries | | | Common in GCC / Egypt pricing |
| Certificate of analysis | | | |

Flag requirements that differ from common international practice with ⚠️.

#### Section 6: Timelines

For each pathway, document:
- Screening / completeness review: X weeks
- Scientific review: X months
- Clock-stop periods (when the clock pauses for applicant responses)
- GMP inspection scheduling: X months
- Total typical timeline: X–Y months
- Any published regulatory targets (KPIs) vs. real-world experience if available

If official timeline targets are not published, use reputable consultancy/industry estimates labeled
`[Unofficial source: name]`.

#### Section 7: Pricing Approval

- Is a price approval required before launch? Is it part of registration or a separate step?
- Pricing method (international reference pricing basket, cost-plus, tender, free pricing)
- Which authority sets/approves the price; required documents (e.g., price certificates)
- Timeline and any fee; periodic price review obligations

#### Section 8: Total Cost Summary

Produce a consolidated cost table:

| Cost Item | Amount (Local Currency) | Amount (USD) | Source | Notes |
|-----------|------------------------|--------------|--------|-------|
| Application fee | | | | |
| Dossier review fee | | | | |
| Laboratory analysis (if required) | | | | |
| GMP inspection (if required) | | | | |
| Registration certificate | | | | |
| Annual renewal fee | | | | |
| Local agent fee (estimate) | | | | |
| **TOTAL (one-time)** | | | | |
| **TOTAL (annual recurring)** | | | | |

Include ranges where costs vary by product type, pathway, or company role.

---

### Step 4 — Format the Output

Produce the final report in this structure. Use precise regulatory references for expert readers and
plain-language notes for business readers.

---

## Pharmaceutical Registration Research: [Country]
**Product Type:** [as specified]
**Company Role:** [as specified by user]
**Regulatory Authority:** [Name + official website]
**Submission Portal:** [Name + URL]
**Research Date:** [today's date]
**Assumptions:** [any "not sure" answers resolved by assumption — omit if none]

### Key Facts at a Glance

| Item | Finding |
|------|---------|
| Recommended pathway | |
| Reference approval accepted? | |
| Local agent / local entity required? | |
| CPP required? | |
| GMP inspection required? | |
| Pricing approval before launch? | |
| Typical total timeline | |
| One-time official cost (USD) | |
| Annual recurring cost (USD) | |
| Biggest risk / blocker | |

Complete this table last, from the findings below, but place it first in the report.

---

### 1. Regulatory Framework Overview
### 2. Registration Pathways
[Pathway table or structured list with eligibility criteria and role-specific restrictions]

### 3. Reliance & Reference Approval Acceptance
[Completed reliance table — every row filled]

### 4. Registration Procedures

#### Pathway A: [Name]
**Steps:**
1. ...

**Costs:**
- Step X fee: [amount]

#### Pathway B: [Name]
...

### 5. Required Documents
### 6. Timelines
[Timeline table per pathway — label any unofficial figures as `[Unofficial source: name]`]

### 7. Pricing Approval
### 8. Total Cost Summary
[Cost table as defined above — label any unofficial figures as `[Unofficial source: name]`]

### 9. Business Considerations
Provide a brief (3–5 bullet) business-plan-oriented summary tailored to the company's role:
- Is the registration environment favorable or complex for this role?
- Any notable risks (local clinical data, long timelines, mandatory local agent/manufacturer)?
- Estimated time-to-market
- Key cost drivers
- Competitive / strategic notes (e.g., reliance shortcuts available, first-mover considerations)

### 10. Confidence & Caveats
- Note where data is official vs. unofficial vs. unavailable.
- Flag any sections where a proxy framework was used (🔶).
- Flag any figures from pages older than ~2 years, and any authority or portal in active transition.
- State that fees/timelines change and should be confirmed with the authority before final decisions.

### [Optional] 11. Registration Readiness Checklist
(Include only if the user requested it or is preparing a submission.)

Numbered checklist in checkbox format, tied to this country's actual requirements — not a generic
template. Example items:
- [ ] Local agent appointed and agreement legalized (if required)
- [ ] CPP obtained from [reference country] and legalized
- [ ] Stability data for climatic zone [X] available
- [ ] Labelling and PIL translated into [language]
- [ ] Samples and reference standards prepared for authority testing
- [ ] Portal account created on [portal name]

---

### References

List **every URL consulted**, grouped by type. Include all sources — official and unofficial — with the
page's last-updated date where available.

**Official Sources**
1. [Authority Name] — [Full URL] — [What was found] — [Last updated: date]

**Unofficial Sources**
1. [Site/Publication Name] — [Full URL] — [What was found; fees or timelines?] — [Last updated: date]

> Note: Unofficial sources are used solely where official fee schedules or timeline data were not publicly
> available. All unofficial data is labeled inline throughout the report. Proxy frameworks are marked 🔶.

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

- **Official sources first, always.** For framework, pathways, reliance, procedures and documents, use only
  official government/authority sources.
- **Unofficial sources permitted for fees & timelines only**, labeled `[Unofficial source: name]` inline.
  Reputable sources include: RAPS, DIA, TOPRA, regulatory authority newsletters, WHO reliance
  publications, Freyr, Pharmexcil (India), and law-firm regulatory summaries (e.g., Baker McKenzie,
  Covington & Burling).
- **Track every URL** in the References section, with last-updated dates where visible.
- **Currency conversion.** Use the approximate current exchange rate; state the rate and date used
  (e.g., "1 USD ≈ 3.67 AED as of [date]"). Verify the rate via search rather than assuming.
- **Recency.** Include the current year in fee/timeline searches. Flag any page last updated more than
  2 years ago as potentially outdated.
- **Immature framework.** Apply the three-step protocol (flag, proxy, recommend inquiry) — do not leave
  gaps unfilled without attempting the proxy-framework approach.
- **Reliance table must be complete.** Every row filled after a genuine search attempt.
- **Don't fabricate.** If no source is found, state: *"Not publicly available — recommend direct inquiry
  with [Authority Name]."*
- **Cite sources** for every figure that comes from search results.

---

## Output Format Notes

- Lead with **Key Facts at a Glance** — the executive-facing anchor; it must agree with the detail below
- Use tables wherever data has multiple attributes (pathways, reliance, documents, costs, timelines)
- Use numbered steps for procedures
- Use clear headers matching the required sections
- Flag any requirement that differs from common international practice (ICH / EU / WHO baseline), or any
  change taking effect within 12 months, with ⚠️
- Flag any item sourced from a proxy framework (not country-specific guidance) with 🔶
- Add plain-language bracketed notes for non-expert readers where helpful, e.g., "CPP [i.e., a
  certificate from the reference country's regulator confirming the product is approved there]"
- Keep the Business Considerations section concise — it's for executive readers
- If producing as a document (Word/PDF), use the docx or pdf skill accordingly
- End the report with one line suggesting related research, if those skills are available:
  pharmacovigilance obligations (`pv-regulatory-research`) and serialization / track & trace
  (`serialization-regulatory-research`) for the same country
