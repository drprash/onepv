---
name: vet-regulatory-research
description: >
  Research veterinary product registration requirements for a specific country and produce
  a structured business-plan-ready summary. Use this skill for ANY query about: veterinary
  medicine/drug registration, animal feed additive approval, pet supplement registration,
  veterinary vaccine/biologic registration, medicated feed approval, veterinary product
  dossier submission, animal health regulatory requirements, veterinary market entry, or
  registration fees/costs/timelines for vet products. Covers ALL categories: veterinary
  medicines, vaccines, biologics, medicated feed, feed additives, supplements, diagnostics,
  antiparasitics, and disinfectants. Trigger for: "register vet product in [country]",
  "vet drug regulations [country]", "feed additive approval [country]", "pet supplement
  registration [country]". Always apply the full structured workflow even if the user only
  asks about one aspect (costs, timelines, or pathways).
---

# Veterinary Product Regulatory Research Skill

## Purpose
Produce a structured, business-plan-ready summary of veterinary product registration requirements
for a given country. The output supports cost-benefit analysis and go/no-go market entry decisions
across all veterinary product categories.

The applicant's role in the target market materially changes which pathways are open, which fees
apply, and whether a local agent, licensed warehouse, or in-country establishment is mandatory.
This skill therefore **elicits the company's role from the user** and tailors the entire analysis
to it.

---

## Product Category Scope

This skill covers the following veterinary product categories. Identifying the correct category
is critical because different categories are often regulated by **different authorities** and
subject to entirely different frameworks within the same country.

| Category | Examples |
|----------|---------|
| **Veterinary Medicines / Drugs** | Antibiotics, antiparasitics, analgesics, hormones, anesthetics |
| **Veterinary Vaccines & Biologics** | Live/inactivated vaccines, immunoglobulins, antisera |
| **Medicated Animal Feed** | Feed premixes containing active pharmaceutical ingredients |
| **Veterinary Feed Additives** | Probiotics, enzymes, flavors, preservatives, acidifiers, coccidiostats |
| **Animal Nutritional Supplements** | Vitamins, minerals, amino acids, omega-3 supplements |
| **Veterinary Diagnostics** | In-vitro diagnostic kits, test strips, PCR kits for animal disease |
| **Veterinary Medical Devices** | Surgical equipment, implants, monitoring devices (animal use) |
| **Veterinary Disinfectants / Biocides** | Disinfectants for animal housing, teat dips |
| **Pet Food / Specialty Animal Food** | Complete pet food, complementary food, treat products |
| **Growth Promoters / Production Enhancers** | Beta-agonists, anabolic steroids (where permitted) |

---

## Workflow

### Step 1 — Clarify Inputs (ask the user; never assume)

Before researching, confirm the following in a single prompt. Flag which are required vs. helpful.
**Do not hardcode or guess the company role** — it must come from the user. Many users are not
regulatory specialists: offer the options in plain language and accept "not sure".

**Required:**
- **Country / target market**
- **Product category** — which of the categories above? If unsure, ask the user to describe the
  product and what it is used for, then propose the category.
- **Target species:**
  - Food-producing animals (cattle, poultry, swine, sheep/goats, fish/aquaculture)
  - Companion animals (dogs, cats)
  - Horses (classification varies — see Species-Specific Tailoring)
  - Both food-producing and companion animals
- **Company role in the target market** (drives pathway, fee, and obligation analysis):
  - **Local manufacturer** — manufactures within the target country
  - **Foreign manufacturer (MAH / marketing authorization holder)** — manufactures abroad, holds the registration
  - **Local agent / authorized representative / licensed warehouse** — represents a foreign manufacturer locally
  - **Distributor / importer** — imports and distributes an already- or to-be-registered product
  - **Licensing-in / in-country partner** — registers under a local partner arrangement
  - **Other** — capture in the user's own words

**Helpful (ask; proceed with best assumptions if not provided):**
- **Product type detail** — e.g., for medicines: small molecule, biologic, antiparasitic; for feed
  additives: probiotic, enzyme, preservative, coccidiostat.
- **Reference approval** — Is the product already registered elsewhere (EMA / EU member state,
  US FDA/CVM or USDA, UK VMD, APVMA)? Drives reliance/abridged eligibility (Section 3).
- **Stage / objective** — new registration, renewal, variation, or feasibility/cost-benefit study only.
  Default: new registration.
- **Registration readiness checklist wanted?** — If the user is preparing a submission, offer the
  optional checklist at the end of the report.

If a required field is missing, ask before proceeding. If the user answers "not sure" to a helpful
field, assume the most common case, state the assumption at the top of the report, and continue.
Tailor everything downstream to the stated role and species (see the tailoring sections below).

---

### Step 2 — Identify the Regulatory Authority (or Authorities)

**Important:** Veterinary products are often regulated by **multiple authorities** in the same
country depending on category. Always identify ALL relevant authorities for the stated product
category — never assume a single authority covers everything.

Common authority splits by category:

| Product Category | Typical Governing Body |
|-----------------|----------------------|
| Veterinary medicines | Veterinary medicines authority / Ministry of Agriculture / medicines regulator |
| Veterinary vaccines & biologics | Often a separate biologics or animal-health body (e.g., USDA CVB in the US) |
| Medicated feed & feed additives | Feed/Agriculture authority or shared with veterinary medicines authority |
| Pet food / animal nutrition | Feed safety or food safety authority |
| Veterinary diagnostics | Veterinary authority and/or medical devices authority |
| Veterinary disinfectants | Biocides/pesticides authority or veterinary authority |

Read `references/authorities.md` first — it lists known authorities by country and category, plus
the international harmonization bodies — and treat it as a starting point only.

> **Authority changes are common — verify before relying on prior knowledge.** Regulators are
> reorganized, renamed, and merged (e.g., UAE: Federal Decree-Law No. 21 of 2025 reassigned
> veterinary product oversight between EDE and MOCCAE — many sources still reference the old
> arrangement). Always confirm the current responsible authority and active submission portal.

**Search queries to use:**
- `"[country] veterinary medicine registration authority official [current year]"`
- `"[country] animal feed additive registration authority"`
- `"[country] veterinary drug approval [authority name] site"`

Always find and use **official government / authority URLs**. Avoid third-party summaries as
primary sources — fetch the primary-source pages directly.

---

### Step 3 — Research Each Section

Use `web_search` and `web_fetch`. **Always include the current year in time-sensitive queries**
(fees, timelines, latest guidance) to avoid stale results — e.g.,
`"[country] veterinary drug registration fees 2026"`.
For each section, track every **source URL** accessed and the **last-updated date** of each page
where visible — all will be listed in the References section.

**Source priority rules:**
- **Framework, Pathways, Reliance, Procedures & Documents:** Use official government/authority
  sources first and exclusively where available.
- **Fee schedules & Timelines:** Use official sources first. If official sources do not publish fee
  schedules or timelines, **unofficial sources are permitted** (regulatory consultancy sites,
  industry publications, law-firm regulatory summaries, etc.) — but must be clearly labeled as
  `[Unofficial source: name]` inline wherever the data is cited.
- **Recency:** Prefer pages updated within the last 18–24 months. Flag older pages.
- **Never fabricate data.** If no source is found for a specific figure, state:
  *"Not publicly available — recommend direct inquiry with [Authority Name]."*

**Immature / unpublished framework protocol (apply when the country lacks published guidance):**
1. **Flag the gap explicitly** — state that no published guideline was found for that area.
2. **Research the proxy framework** — identify which international or regional standards the
   country has formally adopted (VICH guidelines, WOAH standards, Codex MRLs, GCC / ASEAN / SADC
   frameworks). These become the operative framework until country-specific guidance is
   published. Mark every proxy-derived item with 🔶.
3. **Recommend direct inquiry** — give the authority's contact details and suggest engaging a local
   regulatory consultant familiar with the authority's unpublished expectations.

#### Section 1: Regulatory Framework Overview
- Does the country distinguish between veterinary medicines and feed additives under separate laws?
- Is there a unified veterinary products act or multiple overlapping regulations?
- Any GMP / GLP / GCP requirements for manufacturers?
- Any local manufacturing or local agent / licensed warehouse requirements?
- Membership of international harmonization bodies (see `references/authorities.md`)
- Category-specific restrictions (e.g., antibiotic use restrictions, growth promoter bans,
  coccidiostat-approved lists)
- Any recent regulatory changes (last 2–3 years) — flag prominently with ⚠️

#### Section 2: Registration Pathways

Identify ALL available registration pathways relevant to the product category, type, species,
AND the company's stated role.

**For Veterinary Medicines:**
- Full / Standard Review — complete dossier
- Abridged / Reliance / Mutual Recognition — based on reference country approval
- Generic veterinary medicine pathway
- Bibliographic application (well-established use)
- Fast Track / Priority Review (e.g., for exotic or emerging disease treatments)
- OTC vs. prescription-only classification pathways
- Minor use / minor species (MUMS) pathways (if applicable)
- Provisional / conditional registration (if applicable)
- Renewal / variation pathways

**For Vaccines & Biologics:**
- Batch release requirements — many countries require batch-by-batch official testing
- Master seed lot registration requirements
- Platform technology pathways (if applicable)
- Import permits per consignment (if applicable)

**For Feed Additives:**
- Functional category classification (e.g., EU: technological, sensory, nutritional,
  zootechnical, coccidiostats/histomonostats)
- Maximum inclusion level / dosage approval
- Withdrawal period requirements (food-producing animals)
- Pre-market authorization vs. notification-only pathways

**For Nutritional Supplements:**
- Is there a formal registration requirement or just notification / listing?
- Are ingredient positive lists used? (e.g., EU feed material register)
- Any claims restrictions?

For each pathway, note: eligibility criteria; reference jurisdictions accepted; whether local
safety / efficacy / bridging data is required; species-specific requirements; and **role-specific
restrictions** (e.g., mandatory local licensed warehouse, whether a distributor can be the applicant).

#### Section 3: Reliance & Reference Approval Acceptance

Research and state explicitly for **each** row whether the country accepts it, and what it changes.
Every row must be filled; "Not found" is acceptable only after a genuine search, paired with the
"recommend direct inquiry" note.

| Reference / Mechanism | Accepted? | Effect (abridged review / waiver / shorter timeline) | Conditions | Source |
|-----------------------|-----------|------------------------------------------------------|------------|--------|
| EMA / EU member state approval | | | | |
| US FDA/CVM or USDA CVB approval | | | | |
| Other reference regulators (UK VMD, APVMA, Health Canada) | | | | |
| VICH-based / EU-format dossier accepted? | | | | |
| Regional procedure (GCC, ASEAN, SADC, etc.) | | | | |
| CPP / Free Sale Certificate required? From which country? | | | | |
| GMP inspection waiver based on reference / PIC/S inspection | | | | |
| Codex / reference-country MRLs accepted, or national residue studies required? | | | | |
| Local efficacy / field trial waiver (local strains, climate, husbandry) | | | | |

#### Section 4: Registration Procedures (per pathway)

For each identified pathway, document:

**Registration Steps** (numbered sequence):
1. Pre-submission / dossier preparation requirements
2. Account / portal setup (if online submission)
3. Application submission (format: VICH-based / EU format, national format, paper, etc.)
4. Screening / administrative completeness check
5. Technical / scientific review (quality, safety, efficacy)
6. Residues / MRL review (food-producing animals)
7. Environmental risk assessment (if required)
8. GMP inspection (manufacturing site — local vs. overseas)
9. Batch release testing by authority (vaccines / biologics)
10. Labeling review / SPC approval
11. Pricing approval (if required for veterinary medicines in this country)
12. Approval & marketing authorization / registration certificate issuance
13. Post-approval obligations (pharmacovigilance / adverse event reporting, periodic safety
    reports, renewals, variations)

**Costs per Step** (in local currency AND USD equivalent): application, scientific review,
GMP inspection (local vs. overseas), batch release testing (per batch; annual estimate),
certificate / license, annual registration / renewal, local agent / licensed warehouse (if
mandatory), and any other official fees.

Search specifically for the authority's **official fee schedule** page (often called "tariff",
"fee schedule", "registration fees"). If not publicly available, use reputable regulatory
consultancy sources — label these clearly as `[Unofficial source: source name]`.

#### Section 5: Required Documents

List the documents the authority requires, using its published checklist where available:

| Document | Required? | Legalization / apostille? | Notes |
|----------|-----------|---------------------------|-------|
| CPP / Free Sale Certificate | | | Issuing country; validity period |
| GMP certificate (each manufacturing site) | | | Accepted issuing authorities |
| Manufacturing licence | | | |
| Agent agreement / power of attorney | | | |
| Local establishment / licensed warehouse licence | | | |
| Dossier (quality, safety, efficacy parts) | | | Format and language |
| Residue depletion / MRL data | | | Food-producing animals only |
| Target animal safety and efficacy studies | | | Local field trials required? |
| Stability data | | | Required climatic zone |
| Labelling and leaflet in local language | | | Language(s); withdrawal period statement |
| Samples, reference standards, master seed (vaccines) | | | Quantity; for authority testing / batch release |
| Certificate of analysis | | | |

Flag requirements that differ from common international practice with ⚠️.

#### Section 6: Timelines

For each pathway: administrative screening; scientific review; MRL / residues review
(food-producing animals); GMP inspection scheduling; batch release testing lead time
(vaccines / biologics); clock-stop periods; total typical timeline (X–Y months); and any
published regulatory KPI targets vs. real-world experience.

If official timeline targets are not published, use estimates from reputable regulatory consultancy
or industry sources — label clearly as `[Unofficial source: name]`.

#### Section 7: Total Cost Summary

| Cost Item | Amount (Local Currency) | Amount (USD) | Source | Notes |
|-----------|------------------------|--------------|--------|-------|
| Application fee | | | | |
| Dossier review fee | | | | |
| GMP inspection (if required) | | | | |
| Batch release testing (annual estimate) | | | | |
| Registration certificate | | | | |
| Annual renewal fee | | | | |
| Local agent / warehouse fee (estimate) | | | | |
| **TOTAL (one-time)** | | | | |
| **TOTAL (annual recurring)** | | | | |

Include ranges where costs vary by product type, pathway, species category, or company role.

---

### Step 4 — Format the Output

Produce the final report in this structure. Use precise regulatory references for expert readers and
plain-language notes for business readers.

---

## Veterinary Product Registration Research: [Country]
**Product Category:** [category — e.g., Veterinary Medicine / Feed Additive / Supplement]
**Product Type:** [as specified]
**Target Species:** [food-producing / companion animals / both]
**Company Role:** [as specified by user]
**Regulatory Authority:** [Name(s) + official website(s)]
**Research Date:** [today's date]
**Assumptions:** [any "not sure" answers resolved by assumption — omit if none]

### Key Facts at a Glance

| Item | Finding |
|------|---------|
| Governing authority(ies) for this category | |
| Recommended pathway | |
| Reference approval accepted? | |
| Local agent / licensed warehouse required? | |
| GMP inspection required? | |
| Batch release testing (vaccines/biologics)? | |
| Residue / MRL studies required (food animals)? | |
| Typical total timeline | |
| One-time official cost (USD) | |
| Annual recurring cost (USD) | |
| Biggest risk / blocker | |

Complete this table last, from the findings below, but place it first in the report.

---

### 1. Regulatory Framework Overview
### 2. Registration Pathways
[Pathway table or list with eligibility criteria, species notes, and role-specific restrictions]

### 3. Reliance & Reference Approval Acceptance
[Completed reliance table — every row filled]

### 4. Registration Procedures
#### Pathway A: [Name]
**Steps:** 1. ...
**Costs:** - Step X fee: [amount]

### 5. Required Documents
### 6. Timelines
[Timeline table per pathway — label any unofficial figures as `[Unofficial source: name]`]

### 7. Total Cost Summary
[Cost table as defined above — label any unofficial figures as `[Unofficial source: name]`]

### 8. Business Considerations
Brief (4–6 bullet) business-plan-oriented summary tailored to the company's role and category:
- Is the registration environment favorable or complex for this role and product category?
- Notable risks (e.g., mandatory batch testing, MRL/withdrawal complexity, local agent / licensed
  warehouse requirements)
- Estimated time-to-market and key cost drivers
- Competitive / strategic notes (e.g., reliance shortcuts available, first-mover considerations)
- Category-specific issues (e.g., coccidiostat restrictions in EU, antibiotic use restrictions,
  growth promoter bans, withdrawal period labeling complexity)

### 9. Confidence & Caveats
- Note where data is official vs. unofficial vs. unavailable.
- Flag any sections where a proxy framework was used (🔶).
- Flag any figures from pages older than ~2 years as potentially outdated.
- Flag any authority in active transition (e.g., where submission portals are mid-migration).
- State that fees/timelines change and should be confirmed with the authority before final decisions.

### [Optional] 10. Registration Readiness Checklist
(Include only if the user requested it or is preparing a submission.) Numbered checklist in
checkbox format tied to this country's actual requirements — not a generic template, e.g.:
- [ ] Local agent / licensed warehouse appointed and licensed (if required)
- [ ] CPP / Free Sale Certificate obtained and legalized
- [ ] Residue depletion data supports the proposed withdrawal period (food animals)
- [ ] Labelling translated into [language] with withdrawal period statement
- [ ] Samples / master seed prepared for authority testing

---

### References

List **every URL consulted**, grouped by type, with the page's last-updated date where available.

**Official Sources**
1. [Authority Name] — [Full URL] — [What was found] — [Last updated: date]

**Unofficial Sources**
1. [Site/Publication Name] — [Full URL] — [What was found; fees or timelines?] — [Last updated: date]

> Note: Unofficial sources are used solely where official fee schedules or timeline data were not
> publicly available. All unofficial data is labeled inline. Proxy frameworks are marked 🔶.

---

## Role-Based Tailoring (apply throughout)

- **Local manufacturer** — domestic GMP licensing, manufacturing facility approval, typically lower
  fees, no overseas inspection; may unlock local-manufacturer-only pathways or pricing incentives.
- **Foreign manufacturer (MAH)** — almost always requires a local licensed agent or warehouse
  licensed by the authority; expect overseas GMP inspection fees, legalization/apostille of
  documents, and per-consignment import permits in some markets.
- **Local agent / authorized representative / licensed warehouse** — clarify who holds the
  registration (agent vs. MAH), agent appointment requirements, liability arrangements, and
  whether licensed warehouse status requires separate approval from the authority.
- **Distributor / importer** — import licensing, whether the distributor can be the applicant, and
  product-already-registered scenarios; per-shipment import permits are common for vet products.
- **Licensing-in / partner** — technology-transfer and partner-as-applicant arrangements; clarify
  data exclusivity and who owns the dossier.

If the role implies a mandatory local entity (licensed agent, licensed warehouse, local
establishment) that the user may not have, **flag it explicitly as a market-entry prerequisite**
before discussing pathways and costs.

---

## Species-Specific Tailoring (apply throughout)

- **Food-producing animals (cattle, poultry, swine, aquaculture):**
  - MRL (Maximum Residue Limit) studies and Codex/national MRL compliance required
  - Withdrawal period determination and labeling is mandatory
  - Environmental risk assessment often required; residue depletion studies may be needed
  - More regulatory scrutiny on antibiotic / growth promoter use
  - Batch release testing more common for vaccines

- **Companion animals (dogs, cats):**
  - No MRL/withdrawal period requirements (non-food chain)
  - Often shorter review timelines

- **Horses** — may be classified as food-producing in some jurisdictions (e.g., EU) even if kept
  as companions; confirm classification explicitly.

Always flag where the same product used across both categories creates dual compliance obligations.

---

## Research Quality Standards

- **Official sources first, always.** For framework, pathways, reliance, procedures and documents,
  use only official government/authority sources.
- **Unofficial sources permitted for fees & timelines only**, labeled `[Unofficial source: name]`
  inline. Reputable veterinary regulatory sources include: NOAH, HealthforAnimals, IVIS, Keller &
  Heckman, Covington & Burling, Freyr, RAPS, VMD guidance documents.
- **Track every URL** in the References section, with last-updated dates where visible.
- **Currency conversion.** Use the approximate current exchange rate; state the rate and date
  used. Verify the rate via search rather than assuming.
- **Recency.** Include the current year in fee/timeline searches. Flag any page last updated
  more than 2 years ago as potentially outdated.
- **Immature framework.** Apply the three-step protocol (flag, proxy, recommend inquiry).
- **Reliance table must be complete.** Every row filled after a genuine search attempt.
- **Species distinction matters.** Always flag where food-producing animal products face
  additional requirements (MRL, withdrawal periods, residue studies) versus companion animals.
- **Multi-authority awareness.** Where different authorities govern vet medicines vs. vaccines vs.
  feed additives vs. pet food, state which authority governs each aspect and whether separate
  applications/fees apply.
- **Don't fabricate.** If no source is found, state: *"Not publicly available — recommend direct
  inquiry with [Authority Name]."*
- **Cite sources** for every figure drawn from search results.

---

## Output Format Notes

- Lead with **Key Facts at a Glance** — the executive-facing anchor; it must agree with the detail below
- Use tables wherever data has multiple attributes (pathways, reliance, documents, costs, timelines)
- Use numbered steps for procedures and clear headers matching the required sections
- Always note the product category and target species prominently in the report header
- Always call out food-producing vs. companion animal distinctions wherever they create
  different requirements
- Flag any requirement that differs from common international practice (VICH / EU baseline), or any
  change taking effect within 12 months, with ⚠️
- Flag any item sourced from a proxy framework (not country-specific guidance) with 🔶
- Flag any authority in active transition (new portal, migrated services)
- Add plain-language bracketed notes for non-expert readers where helpful, e.g., "withdrawal period
  [i.e., the time after the last dose before the animal's meat, milk or eggs can enter the food chain]"
- Keep the Business Considerations section concise — it is for executive readers
- If producing as a document (Word/PDF), use the docx or pdf skill accordingly
- End the report with one line suggesting related research for the same country, if those skills
  are available: serialization / track & trace (`serialization-regulatory-research`), which also
  covers veterinary products
