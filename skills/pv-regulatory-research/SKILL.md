---
name: pv-regulatory-research
description: >
  Research pharmacovigilance (PV) regulatory requirements for a specific country and produce
  a structured, decision-ready summary. Use this skill whenever the user asks about:
  pharmacovigilance obligations, QPPV or local PV contact requirements, PSMF requirements,
  expedited ICSR reporting timelines, PSUR/PBRER/aggregate report schedules, signal management
  obligations, risk management plan (RMP/REMS) requirements, literature monitoring obligations,
  or PV inspection readiness for any country or market. Also trigger for queries like
  "what are the PV requirements in [country]", "do I need a local QPPV in [country]",
  "PSUR submission schedule for [country]", "is an RMP required in [country]",
  "PV system setup for [country] launch", or any request to evaluate PV compliance obligations
  for market entry or ongoing licence maintenance. Always apply the full structured workflow
  even if the user asks about only one area (e.g., just QPPV or just expedited timelines).
---

# Pharmacovigilance Regulatory Research Skill

## Purpose
Produce a structured, decision-ready summary of pharmacovigilance obligations for a given
country. The output serves three audiences simultaneously:
- **QPPV / PV experts** — precise regulatory text references, timelines, formats, portals
- **Regulatory / RA teams** — actionable requirements with source citations
- **Business stakeholders** — compliance complexity, cost drivers, time-to-readiness for
  market entry decisions

The MA holder bears full PV obligations. Who holds the MA and who is designated as the local
PV contact are the two questions that determine everything else. This skill elicits both
explicitly and tailors the entire analysis to them.

---

## Workflow

### Step 1 — Clarify Inputs (ask the user; never assume)

Before researching, confirm the following in a single prompt. Flag which are required vs. helpful.

**Required:**
- **Country / target market**
- **Product type** — default is human medicines; confirm if different:
  - Small molecule / chemical entity
  - Biologic / biosimilar
  - Vaccine
  - OTC / non-prescription
  - Medical device or combination product
  - Other (specify)
- **MA status** — which scenario applies?
  - New MA being sought — setting up PV system pre-launch
  - Existing MA — assessing or auditing current obligations
  - Variation / renewal — checking for changed PV obligations
  - Feasibility only — cost/complexity estimate for business case
- **MA holder identity and location** — who holds (or will hold) the MA in this country?
  - Local entity (subsidiary / affiliate of a foreign company)
  - Foreign company directly (no local entity)
  - Local agent / authorized representative holding MA on behalf of foreign manufacturer
  - Licensing-in partner / co-MAH
- **QPPV / local PV contact designation** — what is the current situation?
  - No one designated yet — researching what is required
  - EU QPPV exists — checking whether they satisfy local obligations
  - Local PV contact already designated — auditing whether setup is compliant
  - Other (describe)

**Helpful (ask; proceed with best assumptions if not provided):**
- **Reference jurisdiction approvals** — Is this product approved in EU, US, or another ICH
  market? Existing PSUR, RMP, PSMF from those markets may satisfy local requirements.
- **Product safety profile** — Any known signals, RMP already in place, or PSUR currently
  on a rolling submission schedule? Affects aggregate report workload.
- **Compliance readiness checklist requested?** — If the user is planning a market launch or
  PV system setup, offer a readiness checklist at the end (see Step 4, optional section).

If any required field is missing, ask before proceeding. Tailor all sections to the stated MA
holder and QPPV designation (see "PV Role Tailoring" below).

---

### Step 2 — Identify the PV Regulatory Authority

Search for the **competent authority responsible for pharmacovigilance oversight** in the target
country. This may be the same as the marketing authorization authority or a separate body.

Also identify:
- The **national PV database or reporting portal** (e.g., VigiFlow, EudraVigilance, national
  portal, MedWatch)
- Any **national PV guidelines** or GVP-equivalent published by the authority
- The authority's **ICH membership or observer status** — directly determines which ICH
  guidelines are legally binding vs. aspirational
- Any **regional harmonization framework** the country participates in (GCC, ASEAN, SADC,
  PANDRH for LATAM, etc.)

**Search queries to use:**
- `"[country] pharmacovigilance regulatory requirements [current year]"`
- `"[country] adverse drug reaction reporting authority guidelines"`
- `"[country] QPPV local pharmacovigilance contact requirement"`
- `"[country] PSUR submission requirement [authority name]"`

Always use **official authority URLs** (.gov or known authority domains). Fetch primary-source
guideline documents directly rather than relying on third-party summaries.

> **Authority and portal changes are common.** PV portals, reporting systems, and even the
> designated PV authority can change (e.g., UAE: PV responsibilities transitioning from MOHAP
> to EDE under Federal Decree-Law No. 38 of 2024). Always verify the current active authority
> and submission portal by search before proceeding.

---

### Step 3 — Research Each Section

Use `web_search` and `web_fetch`. **Always include the current year in time-sensitive queries**
to avoid stale guidance. Track every source URL and its last-updated date for the References
section.

**Source priority rules:**
- **Obligations and timelines:** Official authority guidelines, legislation, and circulars first
  and exclusively where available.
- **Practical detail (portals, formats, templates):** Official sources first; if unavailable,
  reputable PV consultancy or industry sources permitted — label as `[Unofficial source: name]`.
- **Recency:** Prefer pages updated within the last 18–24 months. Flag older pages.
- **Never fabricate.** If no source is found: *"Not publicly available — recommend direct
  inquiry with [Authority Name]."*

**Immature / unpublished framework protocol (apply when a country lacks published PV guidance):**
1. **Flag the gap explicitly** — state that no standalone PV guideline was found.
2. **Research proxy framework** — identify which ICH guidelines (E2A, E2B, E2C, E2D, E2E, E2F),
   GVP modules, WHO PV guidelines, or regional harmonization standards (GCC, ASEAN, etc.) the
   country has formally adopted by legislation, circular, or policy. These become the operative
   framework until country-specific guidance is published.
3. **Recommend direct inquiry** — provide the authority's contact details and suggest engaging
   a local regulatory consultant familiar with the authority's unpublished expectations.

---

#### Section 1: PV Regulatory Authority & Legal Framework

- Full name of the competent authority for PV oversight + official website
- Primary legislation governing PV (law/decree number and year)
- National PV guidelines published (titles, version, year)
- ICH guidelines formally adopted: E2A (expedited reporting), E2B(R3) (ICSR format),
  E2C/E2D (PSUR/PBRER), E2E (PV planning), E2F (DSUR)
- GVP modules formally adopted (if EU-aligned country)
- Regional harmonization framework membership (GCC, ASEAN, SADC, PANDRH, etc.)
- National ADR / PV database or reporting portal (name + URL)
- Whether the country participates in WHO VigiBase / Uppsala Monitoring Centre network
- Any recent regulatory changes to PV framework (last 2–3 years) — flag these prominently

---

#### Section 2: QPPV / Local PV Contact Requirements

This is a **required** section regardless of product or market. Address every sub-point.

- **Is a QPPV or local PV contact mandatory?** (yes / no / conditional on product type or
  company structure)
- **Title used locally** — "QPPV", "Responsible Person for PV", "Local Safety Officer",
  "Drug Safety Representative", or other
- **Qualifications required:**
  - Minimum educational background (medical, pharmacy, life sciences degree?)
  - Professional experience requirements (years, field)
  - Any mandatory training or certification?
- **Residency / location requirements:**
  - Must the person be resident in-country?
  - Can the EU QPPV or a regional QPPV serve, or is a locally-resident person mandatory?
  - Can the role be outsourced to a CRO / PV service provider in-country?
- **Registration / notification to authority:**
  - Must the QPPV/contact be formally notified or registered with the authority?
  - Is the name included in the MA dossier / licence?
  - What happens if the designated person changes — is a variation / notification required?
- **Accountability scope:**
  - Is the person personally accountable to the authority (liability)?
  - Are deputy / backup QPPV requirements specified?
- **Role-specific note:** Tailor this section to the stated MA holder and designation situation
  (see "PV Role Tailoring" below)

---

#### Section 3: PSMF Requirements

- **Is a Pharmacovigilance System Master File (PSMF) or local equivalent mandatory?**
- **Local name / equivalent** — "PSMF", "PV System File", "Drug Safety Master File", or other
- **Format requirements:**
  - GVP Module II compliant PSMF accepted?
  - Local format required instead of or in addition to GVP Module II?
  - Language requirements (local language vs. English accepted?)
- **Hosting requirements:**
  - Must the PSMF be hosted in-country?
  - EU-hosted PSMF accepted if accessible to local authority on request?
  - Cloud / remote hosting permitted?
- **Submission vs. availability:**
  - Is the PSMF submitted to the authority at MA or on a schedule?
  - Or is it maintained internally and provided only on inspection / request?
- **Update frequency obligations:**
  - Annual update required?
  - Triggered updates on significant change?
- **Inspection readiness:**
  - Is the PSMF subject to routine GVP/PV inspection in this country?
  - What is the authority's announced inspection frequency or trigger criteria?

---

#### Section 4: Expedited Reporting (ICSRs)

Address each sub-point for the specific product type and species.

- **Reportable events — definition used locally:**
  - Serious unexpected ADRs: timeline (7-day fatal/life-threatening; 15-day other serious?)
  - Serious expected ADRs: required? Timeline?
  - Non-serious ADRs: required? Timeline?
  - Special situations: pregnancy exposure, overdose, misuse, medication error, off-label use,
    lack of efficacy (if required), occupational exposure — which are reportable locally?
- **Reporting format:**
  - E2B(R3) required / accepted?
  - E2B(R2) still accepted?
  - Paper / local XML format required?
  - Local narrative language requirement?
- **Reporting portal / channel:**
  - National reporting portal (name + URL)
  - EudraVigilance gateway (if EU member/associate)?
  - Email / paper submission still permitted?
- **Direct HCP / patient reporting:**
  - Do HCPs and patients report directly to the authority (separate from MAH obligations)?
  - Does the MAH have an obligation to facilitate or promote direct reporting?
- **Clock-start rules:**
  - Day 0 = date of first receipt by any employee / agent of the company?
  - Or local definition differs?
- **Worldwide serious unexpected ADRs (WWSUSARs):**
  - Must non-local WWSUSARs be reported to this authority?
  - Or only locally-sourced cases?

---

#### Section 5: Aggregate Reporting

- **PSUR / PBRER:**
  - Is PSUR/PBRER submission mandatory, accepted, or not required?
  - Submission trigger: routine (on a fixed schedule), on request, at renewal only?
  - Frequency: 6-monthly (first 2 years), annual (years 3–5), 3-yearly (thereafter)?
    Or a different local schedule?
  - Data lock point and submission deadline (e.g., 60 or 90 days post-DLP?)
  - International birth date (IBD) vs. local birth date (LBD) — which governs the schedule?
  - Format: ICH E2C(R2)/PBRER accepted, or local PSUR format required?
- **Local aggregate report equivalent:**
  - Does the country require a country-specific annual / periodic report instead of or in
    addition to PSUR/PBRER?
  - Format, content, and submission deadline for any local equivalent
- **DSUR (Development Safety Update Report):**
  - Required for clinical trials / investigational products?
  - Format and submission schedule
- **EPAR / public assessment equivalent:**
  - Does the authority publish any public safety summary or assessment?
- **Reliance on international documents:**
  - Is an EU/ICH PSUR accepted in lieu of a local report?
  - Any bridging document or cover letter required to accompany the international document?
  - (Research and state explicitly — see "Reliance & International Document Acceptance")

---

#### Section 6: Signal Management

- **Formal signal detection obligation:**
  - Is the MAH required to conduct proactive signal detection (beyond spontaneous reporting)?
  - Is this obligation explicitly stated in national guidelines or implied from ICH E2D adoption?
- **Data sources required:**
  - Access to / mining of national PV database (VigiFlow, national portal)?
  - EudraVigilance access and ICSR mining (EU/EEA only)?
  - Internal company safety database?
  - Published literature?
- **Signal evaluation and documentation:**
  - Must signal assessments be formally documented?
  - Standard format required (disproportionality analysis, case narratives, causality)?
- **Regulatory submission of signal reports:**
  - Must evaluated signals be proactively submitted to the authority?
  - Or reported only within PSURs/PBRERs?
  - Expedited signal notification required for any category (e.g., new serious risk)?
- **Signal management within PSUR / RMP:**
  - Confirmed signals expected to trigger PSUR addendum, RMP update, or urgent safety
    restriction — is this process defined locally?

---

#### Section 7: Risk Management (RMP / REMS)

- **Is a Risk Management Plan (RMP) or local equivalent mandatory?**
  - Trigger criteria: all new MAs? Specific product types (biologics, high-risk medicines)?
    Known safety concerns? Authority discretion?
- **Local name / format:**
  - EU GVP Module V RMP format accepted?
  - US REMS format accepted (if applicable)?
  - Local format required instead of or in addition?
  - Language requirements
- **Routine vs. additional risk minimization measures (RMMs):**
  - Routine RMMs (SmPC/PIL, labeling) — who approves locally?
  - Additional RMMs required (educational materials, controlled access programs, pregnancy
    prevention programs, registries)?
- **Effectiveness evaluation:**
  - Is the MAH required to evaluate the effectiveness of additional RMMs?
  - Format and submission schedule for effectiveness reports?
- **Reliance on international RMP:**
  - Is the EU RMP accepted in lieu of a locally-developed risk management document?
  - (Research and state explicitly — see "Reliance & International Document Acceptance")

---

#### Section 8: Literature Monitoring

- **Is a formal literature monitoring obligation specified?**
- **Scope:**
  - Worldwide literature (Medline, Embase, etc.) vs. local literature only?
  - Specific databases mandated by the authority?
- **Local language monitoring:**
  - Must literature in the local language be monitored?
  - Which local journals or databases are specified?
- **Frequency:**
  - Weekly search (common standard), monthly, or other?
- **Literature ICSRs:**
  - Must cases identified from literature be reported as ICSRs to this authority?
  - Same 15-day timeline as spontaneous cases?
  - Or included only in aggregate reports?
- **Documentation:**
  - Must literature monitoring records be maintained and available for inspection?

---

#### Section 9: Reliance & International Document Acceptance

Research and state explicitly for **each** of the following whether the country accepts the
international document in lieu of a local equivalent, requires it with modifications, or
requires a separate local document:

| International Document | Accepted as-is? | Accepted with cover/bridge? | Local equivalent required instead? | Notes |
|------------------------|-----------------|---------------------------|-------------------------------------|-------|
| EU PSUR / ICH PBRER | | | | |
| EU RMP (GVP Module V) | | | | |
| US REMS | | | | |
| GVP Module II PSMF | | | | |
| E2B(R3) ICSR format | | | | |
| DSUR (ICH E2F) | | | | |
| ICH E2A expedited timelines | | | | |

Also research:
- Any mutual recognition agreement (MRA) covering PV inspections with this country
- Any bilateral PV cooperation agreement (e.g., EU-US, GCC cross-recognition)
- Whether the country is a WHO Programme for International Drug Monitoring member (VigiBase)

---

### Step 4 — Format the Output

Produce the final report in this structure. Adjust depth per audience: use precise regulatory
references for expert readers; include plain-language summaries for business stakeholders.

---

## Pharmacovigilance Requirements Research: [Country]
**Product Type:** [as specified]
**MA Holder:** [local entity / foreign company / local agent — as stated]
**QPPV / PV Contact Situation:** [as stated by user]
**Competent Authority:** [Name + official website]
**National PV Portal:** [Name + URL]
**Research Date:** [today's date]

---

### 1. PV Regulatory Authority & Legal Framework
[Authority, legislation, ICH adoption status, harmonization membership, recent changes]

### 2. QPPV / Local PV Contact
[Full detail per Section 2 above — tailored to stated MA holder and designation situation]

### 3. PSMF Requirements
[Full detail per Section 3 above]

### 4. Expedited Reporting (ICSRs)
[Timelines, formats, portals, special situations, clock-start rules]

### 5. Aggregate Reporting
[PSUR/PBRER, local equivalents, DSUR, schedules, DLP/submission deadlines]

### 6. Signal Management
[Detection obligations, data sources, documentation, submission requirements]

### 7. Risk Management (RMP / REMS)
[Mandatory triggers, format, RMMs, effectiveness evaluation]

### 8. Literature Monitoring
[Scope, databases, local language requirements, ICSR obligations]

### 9. Reliance & International Document Acceptance
[Completed reliance table — every row filled; no row left blank]

### 10. PV Obligations Summary Table

Produce a single consolidated table for at-a-glance compliance planning:

| Obligation | Required? | Format | Deadline / Schedule | Submission Portal | Source |
|------------|-----------|--------|--------------------|--------------------|--------|
| Local QPPV / PV contact | | | | | |
| PSMF | | | | | |
| Expedited report — 7-day | | | | | |
| Expedited report — 15-day | | | | | |
| PSUR / aggregate report | | | | | |
| DSUR | | | | | |
| RMP / REMS | | | | | |
| Signal management report | | | | | |
| Literature monitoring | | | | | |
| PV inspection readiness | | | | | |

### 11. Business / Compliance Considerations
Concise (4–6 bullet) summary tailored to the MA holder and QPPV situation:
- Overall PV complexity for this market (low / moderate / high)
- Most operationally demanding obligations (cost, effort, specialist resource)
- Any obligations that differ significantly from EU/ICH baseline — flag as "watch points"
- Estimated time to establish a compliant PV system before first MA / launch
- Key risks of non-compliance (licence suspension, financial penalties, public disclosure?)
- Any obligations triggered specifically by the MA holder's structure (e.g., local entity
  required, EU QPPV insufficient for local obligations)

### 12. Confidence & Caveats
- Distinguish official guidance (binding) vs. unofficial sources (indicative)
- Flag any sections where guidance was unavailable and proxy framework was used
- Flag any authority or portal in active transition
- State that PV requirements change; confirm with authority or local regulatory counsel
  before launch

### [Optional] 13. Compliance Readiness Checklist
*Include only if the user asked for market entry / go-live planning support.*

Present as a numbered pre-launch checklist tied to this country's specific obligations:
1. [ ] Designate qualified local QPPV/PV contact meeting [qualification + residency criteria]
2. [ ] Notify/register QPPV with [Authority Name] via [process]
3. [ ] Establish or localise PSMF — confirm [hosting / language / submission] requirements
4. [ ] Set up local ICSR collection and [portal name] submission capability
5. [ ] Establish literature monitoring covering [local language / databases]
6. [ ] Confirm PSUR schedule (IBD vs. LBD) and set data lock point calendar
7. [ ] Assess RMP requirement — confirm trigger criteria with authority
8. [ ] Confirm whether [EU PSUR / EU RMP / PSMF] satisfies local obligation or needs bridging
9. [ ] Establish signal management procedure aligned with local obligations
10. [ ] Document PV system in PSMF and confirm inspection readiness

---

### References

List every URL consulted, grouped by type, with last-updated dates where visible.

**Official Sources**
1. [Authority Name] — [Full URL] — [What was found] — [Last updated: date]

**Unofficial Sources**
1. [Site/Publication Name] — [Full URL] — [What was found] — [Last updated: date]

> Unofficial sources used solely where official guidance was unavailable. All unofficial data
> labeled inline. Proxy frameworks (ICH/WHO/regional guidelines) used where country-specific
> guidance was absent — labeled clearly throughout.

---

## PV Role Tailoring (apply throughout)

The MA holder structure and QPPV designation situation change the analysis substantially:

- **Local entity (subsidiary) holds MA:**
  Nearly always bears full local PV obligations. QPPV/PV contact typically must be an employee
  or contractor of the local entity. Confirm whether parent company QPPV satisfies or whether
  a locally-resident person is required. Local entity's PSMF may need to cover local operations
  as a satellite PSMF to the global system.

- **Foreign company holds MA directly (no local entity):**
  Research whether this is legally permitted (some countries require a local entity to hold
  an MA). If permitted, identify whether a local authorized representative is required for PV
  purposes. Clarify whether the foreign QPPV satisfies local obligations or a local PV contact
  must be separately designated.

- **Local agent / authorized representative holds MA:**
  Clarify whether PV obligations rest with the agent (as nominal MAH) or the foreign
  manufacturer (as the beneficial MAH). Agent liability for PV can be significant. Confirm
  QPPV must be affiliated with the agent or can be the foreign manufacturer's QPPV.

- **Licensing-in partner / co-MAH:**
  PV data-sharing agreement between the licensor and licensee is typically mandatory. Clarify
  who is the single point of contact to the authority for PV. Research whether a joint PSMF
  or separate PSMFs are required.

- **QPPV situation — EU QPPV exists, checking local sufficiency:**
  Research explicitly whether the EU QPPV can serve as the local PV contact. Many countries
  (GCC, LATAM, Africa) require a locally-resident person regardless of EU QPPV designation.
  This is a critical market entry question — flag clearly if a new appointment is required.

If the MA holder structure implies a local entity or local PV contact that the user does not
yet have, **flag it explicitly as a pre-launch prerequisite** before the obligations discussion.

---

## Regional PV Authority Reference

### GCC (Gulf Cooperation Council)

The GCC Pharmacovigilance Guidelines provide a shared regional framework. Member states may
add country-specific requirements on top. Always research country-level obligations separately.

| Country | PV Authority | PV Portal / Reporting | Key Framework | URL |
|---------|-------------|----------------------|---------------|-----|
| UAE | EDE (Emirates Drug Establishment) — PV transferred from MOHAP under Federal Decree-Law No. 38 of 2024 | ede.gov.ae | GCC PV Guidelines + EDE-specific circulars | ede.gov.ae |
| Saudi Arabia | SFDA (Saudi Food and Drug Authority) | SFDA PV portal; national ADR reporting | SFDA PV Guidelines (GCC-aligned) | sfda.gov.sa |
| Kuwait | NCDSA / MOH | MOH Kuwait ADR reporting | GCC PV Guidelines | moh.gov.kw |
| Qatar | MOPH (Ministry of Public Health) | MOPH portal | GCC PV Guidelines | moph.gov.qa |
| Bahrain | NHRA (National Health Regulatory Authority) | NHRA portal | GCC PV Guidelines | nhra.bh |
| Oman | MOH / DGSM | MOH Oman ADR portal | GCC PV Guidelines | moh.gov.om |

**GCC-specific PV notes:**
- Local QPPV/PV representative requirement: most GCC states require a locally-resident PV
  contact affiliated with the local agent or MAH — verify per country
- PSUR submission: GCC framework requires PSUR on ICH E2C schedule; some states accept
  EU PSUR directly; confirm country-by-country
- Expedited reporting: 15-day timeline for serious unexpected; confirm local portal vs. paper
- PSMF: not all GCC states have published explicit PSMF requirements — apply immature
  framework protocol where guidance is absent

---

### EU / EEA

| Entity | Role | Key Tools | URL |
|--------|------|-----------|-----|
| EMA | Central procedure MAs; GVP guidelines; EudraVigilance | GVP Modules I–XVI; EudraVigilance ICSR database | ema.europa.eu |
| National CAs | Nationally authorised products; local PV inspections | VigiFlow or national databases | Varies by member state |

**EU-specific PV notes:**
- QPPV: must be permanently and continuously available; EU/EEA resident required for centrally
  authorised products; GVP Module I
- PSMF: mandatory; hosted in EU/EEA; single location stated in MA; GVP Module II
- Expedited: E2B(R3) via EudraVigilance; 7-day fatal/life-threatening; 15-day other serious
- PSUR/PBRER: EU PSUR procedure; IBD-based; GVP Module VII; PSURs for CAPs submitted to EMA
- RMP: mandatory for new active substances, biosimilars, generics with safety concerns;
  GVP Module V; effectiveness evaluation required for additional RMMs
- Signal management: EudraVigilance access and routine ICSR mining mandatory; GVP Module IX
- Literature monitoring: weekly Medline/Embase search; literature ICSRs reportable

---

### US FDA

| Area | Details |
|------|---------|
| PV Authority | FDA / CDER (drugs) or CBER (biologics) |
| Reporting Portal | MedWatch (voluntary); FDA Safety Reporting Portal; FAERS (Adverse Event Reporting System) |
| Expedited reporting | 15-day alert reports for serious unexpected ADRs (21 CFR 314.81 / 600.80); 7-day for fatal/life-threatening on request |
| Periodic reporting | NDA / BLA Annual Report (not PSUR format); PSUR not required but may be submitted |
| REMS | Risk Evaluation and Mitigation Strategy; required for high-risk products by FDA mandate; no EU RMP equivalent accepted as REMS |
| QPPV equivalent | None — no formal QPPV requirement; US regulatory contact / agent required for foreign applicants |
| PSMF equivalent | None — no formal PSMF requirement; internal pharmacovigilance SOPs expected |
| Signal management | FDA monitors FAERS; MAH expected to conduct signal detection; formal obligation less prescriptive than EU GVP |
| Literature monitoring | Obligation implied; literature cases reportable as ICSRs |

---

### LATAM

| Country | PV Authority | Key Framework | Expedited Timeline | PSUR Required? | QPPV / Local Contact | URL |
|---------|-------------|---------------|-------------------|----------------|----------------------|-----|
| Brazil | ANVISA | RDC 406/2020 (PV guideline); ICTQ-aligned | 15 days serious unexpected | Yes — PSUR on IBD-based schedule | Responsável Técnico (local pharmacist or equivalent) required; PV Technical Responsible | anvisa.gov.br |
| Mexico | COFEPRIS | NOM-220-SSA1 (PV) | 15 days serious; 7-day fatal | PSUR required; local report (IPPA) may also be required | Local PV representative required; in-country presence | gob.mx/cofepris |
| Colombia | INVIMA | Decree 677/1995 + INVIMA circulars | 15 days serious unexpected | Periodic safety reports required; PSUR may be accepted | Local PV representative required | invima.gov.co |

**LATAM-specific PV notes:**
- Local language (Spanish / Portuguese) requirements for ICSR narratives and labeling updates
  are common across the region — verify per country
- Brazil's ANVISA requires a Brazilian-resident Responsável Técnico who may carry PV
  accountability; EU QPPV does not satisfy this obligation
- Many LATAM countries have adopted ICH E2A/E2B conceptually but may not require E2B(R3)
  format electronically — verify portal and format per country
- PSUR acceptance varies: some countries require local bridging data or local-language summary

---

### Africa

| Country | PV Authority | Key Framework | Reporting Portal | PSUR Required? | URL |
|---------|-------------|---------------|-----------------|----------------|-----|
| Nigeria | NAFDAC | NAFDAC PV guidelines (WHO-aligned) | NAFDAC ADR portal; WHO VigiBase member | Yes — periodic reports required; schedule may differ from ICH | nafdac.gov.ng |
| South Africa | SAHPRA | BN 69 of 2019 (PV regulations); NDA 42 | MedSafety / VigiFlow | PSUR required on IBD-based schedule | sahpra.org.za |
| Kenya | PPB (Pharmacy and Poisons Board) | PPB PV guidelines; WHO-aligned | VigiFlow / national portal | Periodic reports required | pharmacyboardkenya.org |
| Egypt | EDA (Egyptian Drug Authority) | EDA PV guidelines | EDA ADR portal | PSUR required | edaegypt.gov.eg |

**Africa-specific PV notes:**
- Many African markets have adopted WHO PV guidelines as the operative framework; use as
  proxy where country-specific guidance is absent (apply immature framework protocol)
- Local PV representative or responsible pharmacist requirements are common — verify
  per country; EU QPPV typically insufficient
- E2B(R3) electronic submission is not yet uniformly implemented; paper or email submission
  may still be the primary channel — verify active portal per country
- PSUR schedules may follow ICH conceptually but with local submission deadlines that differ —
  always verify the exact DLP and submission window

---

## Research Quality Standards

- **Official sources first, always.** Legislation, authority guidelines, and circulars are
  primary. Third-party summaries are supporting only.
- **Unofficial sources permitted** for practical detail (portal URLs, form names, templates)
  when official sources are silent. Label clearly as `[Unofficial source: name]`.
  Reputable PV sources: RAPS, DIA, ISOP, PV Monitor (SCRIP), Keller & Heckman,
  regulatory authority newsletters, ICH secretariat.
- **Track every URL** in the References section, with last-updated dates where visible.
- **Currency conversion.** If fees are involved, state the rate and date. Verify by search.
- **Recency.** Include the current year in all queries. Flag pages older than 2 years.
- **Immature framework.** Apply the three-step protocol (flag, proxy, recommend inquiry) — do
  not leave gaps unfilled without attempting the proxy-framework approach.
- **Reliance table must be complete.** Every row in the reliance table must be filled. "Not
  found" is an acceptable answer only after a genuine search attempt; pair it with the
  "recommend direct inquiry" note.
- **Don't fabricate.** If no source is found: *"Not publicly available — recommend direct
  inquiry with [Authority Name]."*
- **Cite sources** for every specific obligation, timeline, or format requirement.

---

## Output Format Notes

- Use the PV Obligations Summary Table (Section 10) as the executive-facing anchor — it
  must be complete and accurate before anything else in the report
- Use precise regulatory references (law number, GVP module, ICH guideline) for expert readers
- Add plain-language bracketed notes where relevant for non-expert readers,
  e.g., "15-day timeline [i.e., the MAH must submit the report within 15 calendar days of
  first becoming aware of the case]"
- Use tables for timelines, formats, and the reliance matrix
- Use numbered steps for procedural sequences
- Flag any obligation that differs from the EU/ICH baseline with ⚠️ so expert readers can
  quickly identify non-standard requirements
- Flag any item sourced from a proxy framework (not country-specific guidance) with 🔶
- Keep Business Considerations concise — it is for executive readers
- The optional Compliance Readiness Checklist uses checkbox format tied to this country's
  actual obligations — do not use a generic template
- If producing as a document (Word/PDF), use the docx or pdf skill accordingly
