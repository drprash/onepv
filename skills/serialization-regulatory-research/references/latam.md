# Serialization Regional Reference: LATAM

| Country | Authority | System | Scope | Status | Key Feature | URL |
|---------|-----------|--------|-------|--------|-------------|-----|
| **Brazil** | ANVISA | SNCM (Sistema Nacional de Controle de Medicamentos) | Rx medicines; phased by therapeutic area and company size | Live; phased rollout per RDC 653/2022 | DataMatrix 2D; GS1 standard; ANVISA issues authorization codes; SNCM upload required | anvisa.gov.br |
| **Mexico** | COFEPRIS | National T&T system (in development) | Rx medicines | Requirement evolving — verify current status | Serialization mandated in concept; implementation guidance developing | gob.mx/cofepris |
| **Colombia** | INVIMA | INVIMA T&T system | Priority medicines (antibiotics, biologics, controlled substances) | Phased rollout underway | DataMatrix; national INVIMA portal reporting | invima.gov.co |

**LATAM-specific notes:**
- Brazil's SNCM requires ANVISA to issue product authorization codes (CNPJ-linked) before
  commissioning — this is not a company-generated serial; allow lead time for registration
- Local language requirements for human-readable information (Spanish / Portuguese)
- Customs integration with T&T status is developing in several LATAM markets — verify
  import clearance implications per country
