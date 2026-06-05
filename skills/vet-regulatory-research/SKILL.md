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

Before researching, confirm the following. **Do not hardcode or guess the company role** — it must
come from the user. Ask all questions together in one prompt.

- **Country / target market** (required)
- **Product category** — which of the above categories? (required)
- **Species target** — food-producing animals (cattle, poultry, swine, fish/aquaculture) or companion
  animals (dogs, cats, horses) or both? This significantly affects pathways, MRL/withdrawal period
  requirements, and applicable regulatory framework.
- **Product type detail** — e.g., for medicines: small molecule, biologic, vaccine, antiparasitic;
  for feed additives: probiotic, enzyme, preservative, coccidiostat, etc.
- **Reference approval status** — Is the product already registered in a reference jurisdiction
  (EMA, US FDA/CVM, APVMA, VMD/UK, WOAH standards)? Affects abridged/reliance pathway eligibility.
- **Company role in the target market** (required — this drives pathway, fee, and obligation analysis):
  - **Local manufacturer** — manufactures within the target country
  - **Foreign manufacturer (MAH / marketing authorization holder)** — manufactures abroad, holds the registration
  - **Local agent / authorized representative / licensed warehouse** — represents a foreign manufacturer locally
  - **Distributor / importer** — imports and distributes an already- or to-be-registered product
  - **Licensing-in / in-country partner** — registers under a local partner arrangement
  - **Other** — capture in the user's own words
- **Stage / objective** — new registration, renewal, variation, or feasibility/cost-benefit study only

If any required field is missing, ask before proceeding. Tailor everything downstream to the stated
role and species category (see "Role-Based Tailoring" below).

---

### Step 2 — Identify the Regulatory Authority (or Authorities)

**Important:** Veterinary products are often regulated by **multiple authorities** in the same
country depending on category. Always identify ALL relevant authorities for the stated product
category — never assume a single authority covers everything.

Common authority splits by category:

| Product Category | Typical Governing Body |
|-----------------|----------------------|
| Veterinary medicines & vaccines | Veterinary medicines authority / Ministry of Agriculture |
| Medicated feed & feed additives | Feed/Agriculture authority or shared with veterinary medicines authority |
| Pet food / animal nutrition | Feed safety or food safety authority |
| Veterinary diagnostics | Veterinary authority and/or medical devices authority |
| Veterinary disinfectants | Biocides/pesticides authority or veterinary authority |

**Known authority examples (verify currency by search before use — see authority-change warning below):**

| Country | Authority for Vet Medicines | Authority for Feed/Additives |
|---------|----------------------------|------------------------------|
| UAE | EDE (Emirates Drug Establishment — federal authority for vet medicines, vaccines, establishment licensing, and import permits under Federal Decree-Law No. 21 of 2025; services transferred from MOCCAE to EDE) | EDE / MOCCAE (transition ongoing — verify current submission portal at ede.gov.ae) |
| Saudi Arabia | SFDA | SFDA / MEWA |
| Egypt | GOVS (General Organization for Veterinary Services) | GOVS / NFSA |
| EU | EMA (central) + national VMAs | EFSA (scientific assessment) + EC / national |
| USA | FDA/CVM (Center for Veterinary Medicine) | FDA/CVM + AAFCO (feed standards) |
| UK | VMD (Veterinary Medicines Directorate) | DEFRA / APHA |
| Australia | APVMA | APVMA / FSANZ |
| Canada | Health Canada / CVMA | CFIA |
| India | CDSCO | FSSAI / BIS |
| Brazil | MAPA | MAPA |
| South Africa | DAFF / SAHPRA | DAFF |
| Kenya | VMD Kenya | KEBS / PCPB |
| Nigeria | NAFDAC | NAFDAC / Federal Min of Agriculture |
| China | MARA | MARA |
| Japan | MAFF | MAFF |

> **Authority changes are common — verify before relying on prior knowledge.** Regulators are
> reorganized, renamed, and merged. (Example: in the UAE, EDE progressively absorbed veterinary
> product registration from MOCCAE under Federal Decree-Law No. 21 of 2025 — many sources and
> even the MOCCAE website still reference the old arrangement.) Always confirm the current
> responsible authority and active submission portal by search before proceeding.

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
- **Registration Pathways & Procedures:** Use official government/authority sources first and
  exclusively where available.
- **Fee schedules & Timelines:** Use official sources first. If official sources do not publish fee
  schedules or timelines, **unofficial sources are permitted** (regulatory consultancy sites,
  industry publications, law-firm regulatory summaries, etc.) — but must be clearly labeled as
  `[Unofficial source: name]` inline wherever the data is cited.
- **Recency:** Prefer pages updated within the last 18–24 months. Flag any figure drawn from an
  older page as potentially outdated.
- **Never fabricate data.** If no source is found for a specific figure, state:
  *"Not publicly available — recommend direct inquiry with [Authority Name]."*

---

#### Section 1: Regulatory Framework Overview

Provide a brief overview of how the country regulates veterinary products:
- Does the country distinguish between veterinary medicines and feed additives under separate laws?
- Is there a unified veterinary products act or multiple overlapping regulations?
- Any GMP / GLP / GCP requirements for manufacturers?
- Any local manufacturing or local agent / licensed warehouse requirements?
- Is the country a member of any international veterinary harmonization body?
  (VICH, Codex Alimentarius, WOAH/OIE, ASEAN harmonization, etc.)
- Any category-specific restrictions relevant to the product (e.g., antibiotic use restrictions,
  growth promoter bans, coccidiostat-approved lists)?

---

#### Section 2: Registration Pathways

Identify ALL available registration pathways relevant to the product category, type, species,
AND the company's stated role.

**For Veterinary Medicines:**
- Full / Standard Review — complete dossier
- Abridged / Reliance / Mutual Recognition — based on reference country approval
  (EMA, FDA/CVM, VMD, APVMA, WOAH)
- Generic veterinary medicine pathway
- Bibliographic application (well-established use)
- Fast Track / Priority Review (e.g., for exotic or emerging disease treatments)
- OTC vs. prescription-only classification pathways
- Minor use / minor species (MUMS) pathways (if applicable)
- Provisional / conditional registration (if applicable)
- Renewal / variation pathways

**For Vaccines & Biologics:**
- Note batch release requirements — many countries require batch-by-batch official testing
- Master seed lot registration requirements
- Platform technology pathways (if applicable)
- Import permits per consignment (if applicable)

**For Feed Additives:**
- Functional category classification (e.g., EU: preservatives, antioxidants, emulsifiers,
  coccidiostats, zootechnical additives, etc.)
- Zootechnical vs. sensory vs. nutritional additive pathways
- Maximum inclusion level / dosage approval
- Withdrawal period requirements (food-producing animals)
- Any pre-market authorization vs. notification-only pathways

**For Nutritional Supplements:**
- Is there a formal registration requirement or just notification / listing?
- Are ingredient positive lists used? (e.g., EU feed material register)
- Any claims restrictions?

For each pathway, note:
- Eligibility criteria
- Reference jurisdictions accepted (if any)
- Whether local safety / efficacy / bridging data is required
- Species-specific requirements (food-producing vs. companion animals)
- **Role-specific restrictions** — e.g., whether a local licensed warehouse is mandatory for
  foreign manufacturers, whether a distributor can be the applicant, local-manufacturing
  prerequisites, etc.

---

#### Section 3: Registration Procedures (per pathway)

For each identified pathway, document:

**Registration Steps** (numbered sequence):
1. Pre-submission / dossier preparation requirements
2. Account / portal setup (if online submission)
3. Application submission (format: eCTD, CTD-V, VICH format, paper, etc.)
4. Screening / administrative completeness check
5. Technical / scientific review (quality, safety, efficacy)
6. Residues / MRL (Maximum Residue Limit) review (food-producing animals)
7. Environmental risk assessment (if required)
8. GMP inspection (manufacturing site — local vs. overseas)
9. Batch release testing by authority (vaccines / biologics)
10. Labeling review / SPC / SmPC approval
11. Approval & marketing authorization / registration certificate issuance
12. Post-approval obligations (pharmacovigilance / adverse event reporting, periodic safety
    reports, renewals, variations)

**Costs per Step** (in local currency AND USD equivalent):
- Application fees
- Scientific review fees
- GMP inspection fees (local vs. overseas)
- Batch release testing fees (per batch; annual estimate)
- Certificate / license fees
- Annual registration / renewal fees
- Local agent / licensed warehouse fees (if mandatory)
- Any other official fees

Search specifically for the authority's **official fee schedule** page (often called "tariff",
"fee schedule", "registration fees"). If not publicly available, use reputable regulatory
consultancy sources — label these clearly as `[Unofficial source: source name]`.

---

#### Section 4: Timelines

For each pathway, document:
- Administrative screening: X weeks
- Scientific review: X months
- MRL / residues review: X months (food-producing animals; if applicable)
- GMP inspection scheduling: X months
- Batch release testing lead time (vaccines / biologics; if applicable)
- Clock-stop periods (when the clock pauses for applicant responses)
- Total typical timeline: X–Y months
- Any published regulatory KPI targets vs. real-world experience if available

If official timeline targets are not published, use estimates from reputable regulatory consultancy
or industry sources — label clearly as `[Unofficial source: name]`.

---

#### Section 5: Total Cost Summary

Produce a consolidated cost table:

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

Produce the final report in this structure:

---

## Veterinary Product Registration Research: [Country]
**Product Category:** [category — e.g., Veterinary Medicine / Feed Additive / Supplement]
**Product Type:** [as specified]
**Target Species:** [food-producing / companion animals / both]
**Company Role:** [as specified by user]
**Regulatory Authority:** [Name(s) + official website(s)]
**Research Date:** [today's date]

---

### 1. Regulatory Framework Overview
[Brief summary of legal framework, harmonization membership, GMP/local agent requirements,
category-specific restrictions]

### 2. Registration Pathways
[Pathway table or structured list with eligibility criteria, species notes, and role-specific
restrictions]

### 3. Registration Procedures

#### Pathway A: [Name]
**Steps:**
1. ...

**Costs:**
- Step X fee: [amount]

#### Pathway B: [Name]
...

### 4. Timelines
[Timeline table per pathway — label any unofficial figures as `[Unofficial source: name]`]

### 5. Total Cost Summary
[Cost table as defined above — label any unofficial figures as `[Unofficial source: name]`]

### 6. Business Considerations
Provide a brief (4–6 bullet) business-plan-oriented summary tailored to the company's role
and product category:
- Is the registration environment favorable or complex for this role and product category?
- Any notable risks (e.g., mandatory batch testing for vaccines, MRL/withdrawal period
  complexity for food animals, local agent / licensed warehouse requirements)?
- Estimated time-to-market
- Key cost drivers
- Competitive / strategic notes (e.g., reliance shortcuts available, first-mover considerations)
- Any category-specific issues (e.g., coccidiostat restrictions in EU, antibiotic use
  restrictions, growth promoter bans, withdrawal period labeling complexity)

### 7. Confidence & Caveats
- Note where data is official vs. unofficial vs. unavailable.
- Flag any figures from pages older than ~2 years as potentially outdated.
- Flag any authority in active transition (e.g., where submission portals are mid-migration).
- State that fees/timelines change and should be confirmed with the authority before final decisions.

---

### References

List **every URL consulted**, grouped by type. Include all sources — official and unofficial —
with the page's last-updated date where available.

**Official Sources**
1. [Authority Name] — [Full URL] — [What was found] — [Last updated: date]

**Unofficial Sources**
1. [Site/Publication Name] — [Full URL] — [What was found; fees or timelines?] — [Last updated: date]

> Note: Unofficial sources are used solely where official fee schedules or timeline data were not
> publicly available. All unofficial data is labeled inline throughout the report.

---

## Role-Based Tailoring (apply throughout)

The stated company role changes the analysis in the veterinary context. Apply these lenses:

- **Local manufacturer** — focus on domestic GMP licensing, manufacturing facility approval,
  typically lower fees, no overseas inspection, may unlock local-manufacturer-only pathways
  or pricing incentives.
- **Foreign manufacturer (MAH)** — almost always requires a local licensed agent or warehouse
  licensed by the authority; expect overseas GMP inspection fees, legalization/apostille of
  documents, and per-consignment import permits in some markets.
- **Local agent / authorized representative / licensed warehouse** — clarify who holds the
  registration (agent vs. MAH), agent appointment requirements, liability arrangements, and
  whether the licensed warehouse status requires separate approval from the authority.
- **Distributor / importer** — focus on import licensing, whether the distributor can be the
  applicant, and product-already-registered scenarios; per-shipment import permits are common
  for veterinary products.
- **Licensing-in / partner** — focus on technology-transfer and partner-as-applicant arrangements;
  clarify data exclusivity and who owns the dossier.

If the role implies a mandatory local entity (licensed agent, licensed warehouse, local
establishment) that the user may not have, **flag it explicitly as a market-entry prerequisite**
before discussing pathways and costs.

---

## Species-Specific Tailoring (apply throughout)

Species category creates fundamentally different requirements:

- **Food-producing animals (cattle, poultry, swine, aquaculture):**
  - MRL (Maximum Residue Limit) studies and Codex/national MRL compliance required
  - Withdrawal period determination and labeling is mandatory
  - Environmental risk assessment often required
  - Residue depletion studies may be needed
  - More regulatory scrutiny on antibiotic / growth promoter use
  - Batch release testing more common for vaccines

- **Companion animals (dogs, cats, horses):**
  - No MRL/withdrawal period requirements (non-food chain)
  - Often shorter review timelines
  - Horses are a special case — may be classified food-producing in some jurisdictions (EU)
    even if intended as companion animals; confirm classification explicitly

Always flag where the same product used across both categories creates dual compliance obligations.

---

## Research Quality Standards

- **Official sources first, always.** For pathways and procedures, use only official
  government/authority sources.
- **Unofficial sources permitted for fees & timelines only**, labeled `[Unofficial source: name]`
  inline. Reputable veterinary regulatory sources include: NOAH, IFAH/IPHA, IVIS, Keller &
  Heckman, Covington & Burling, Freyr, RAPS, VMD guidance documents.
- **Track every URL** in the References section, with last-updated dates where visible.
- **Currency conversion.** Use the approximate current exchange rate; state the rate and date
  used. Verify the rate via search rather than assuming.
- **Recency.** Include the current year in fee/timeline searches. Flag any page last updated
  more than 2 years ago as potentially outdated.
- **Species distinction matters.** Always flag where food-producing animal products face
  additional requirements (MRL, withdrawal periods, residue studies) versus companion animals.
- **Multi-authority awareness.** In countries where different authorities govern vet medicines
  vs. feed additives vs. pet food, clearly state which authority governs each aspect and whether
  separate applications/fees apply.
- **Don't fabricate.** If no source is found, state: *"Not publicly available — recommend direct
  inquiry with [Authority Name]."*
- **Cite sources** for every figure drawn from search results.

---

## Common International Harmonization Bodies

| Body | Relevance |
|------|-----------|
| **VICH** | EU, USA, Canada, Japan, Australia, NZ — harmonized CTD-V dossier format; check if target country accepts VICH-format dossiers |
| **WOAH / OIE** | Global animal health standards; disease classification affects vaccine registration; some countries adopt WOAH MRLs |
| **Codex Alimentarius** | MRL standards for food-producing animals adopted by many countries; key for withdrawal period and residue compliance |
| **ASEAN Harmonization** | ASEAN member states shared guidelines for vet products |
| **AU-NZ TTMRA** | Australia / New Zealand mutual recognition arrangement |
| **SADC** | Southern African Development Community harmonization efforts |
| **GCC Veterinary Products Law** | GCC member states shared framework for vet product registration; relevant for UAE, Saudi Arabia, Kuwait, Qatar, Bahrain, Oman |

Always check if the target country has adopted any of the above frameworks — it directly affects
dossier format requirements and whether reference approvals from other jurisdictions are accepted.

---

## Common Official Source Patterns to Search

| Country | Authority for Vet Medicines | Typical URL |
|---------|-----------------------------|-------------|
| UAE | EDE (federal) | ede.gov.ae |
| UAE | MOCCAE (transition portal, verify currency) | moccae.gov.ae |
| Saudi Arabia | SFDA | sfda.gov.sa |
| Egypt | GOVS | govs.gov.eg |
| EU | EMA | ema.europa.eu |
| USA | FDA/CVM | fda.gov/animal-veterinary |
| UK | VMD | gov.uk/government/organisations/veterinary-medicines-directorate |
| Australia | APVMA | apvma.gov.au |
| Canada | CFIA / HC | canada.ca |
| India | CDSCO | cdsco.gov.in |
| Brazil | MAPA | gov.br/agricultura |
| South Africa | DAFF / SAHPRA | dalrrd.gov.za |
| Nigeria | NAFDAC | nafdac.gov.ng |
| Kenya | VMD Kenya | kephis.org / kalro.org |
| China | MARA | moa.gov.cn |
| Japan | MAFF | maff.go.jp |

For unlisted countries, search: `"[country] veterinary medicine registration authority official"`
and look for `.gov` or equivalent government domains. Verify the current active portal by search.

---

## Output Format Notes

- Use tables wherever data has multiple attributes (pathways, costs, timelines)
- Use numbered steps for procedures
- Use clear headers matching the required sections
- Always note the product category and target species prominently in the report header —
  they determine which authority, pathway, and compliance obligations apply
- Always call out food-producing animal vs. companion animal distinctions wherever they create
  different requirements
- Flag any authority in active transition (new portal, migrated services) so the user knows
  to verify submission channels before acting
- Keep the Business Considerations section concise — it is for executive readers
- If producing as a document (Word/PDF), use the docx or pdf skill accordingly
