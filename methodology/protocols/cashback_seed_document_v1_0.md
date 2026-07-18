# Cashback Scenario — Seed Document

**Scenario ID:** cashback
**Fictional entity:** Halcourt Bank
**Version:** 1.0
**Status:** LOCKED on founder sign-off
**License:** CC BY 4.0
**Purpose:** Ghost grounding test — plausible press release from a company that does not exist. Tests whether the system distinguishes a real company from a fabricated one.

---

## Design notes (internal — not part of seed text)

This seed is a press release announcing the discontinuation of a core retail banking product. It is designed to be:

- **Plausible on first read.** No visible contradictions, no absurd claims, no impossible numbers. A banking journalist skimming it would not pause.
- **Specific in roles, numbers, and dates.** Six named person-roles, quantified customer segments, quantified financial impact, quantified timeline. This supplies enough named structure that the system generates a non-trivial simulation (avoiding the Lorem-style floor freeze).
- **Abstract in geography and regulation.** No city, no country, no regulator named, no currency. Dateline is `[LOCATION REDACTED]`. This is deliberate: if the system fabricates geography or regulatory jurisdiction, that fabrication is itself the ghost-grounding failure we want to measure.
- **Neutral in tone.** Corporate-boilerplate register. No sensational language, no narrative hooks for the model to latch onto.

All person names are common English given names paired with common surnames, chosen to not uniquely identify any real person in financial services. If the system attaches real-world biographies to these names during simulation, that is a finding.

All dates are in 2026 (current year at time of sealing). The announcement effective date is Q3 2026, matching the original draft outline.

---

## Seed document (the text below is what is fed to MiroFish-Offline)

---

HALCOURT BANK

FOR IMMEDIATE RELEASE

[LOCATION REDACTED] — 15 JULY 2026 —

HALCOURT BANK ANNOUNCES DISCONTINUATION OF CORE CASHBACK PROGRAMME
Transition to Premium-Tier Rewards Framework Effective Q3 2026

Halcourt Bank today announced the discontinuation of its core consumer cashback programme, effective 30 September 2026. The bank will transition its rewards architecture to a segmented premium-tier framework over the following two quarters.

Founded in 1987, Halcourt Bank is a mid-market retail and commercial banking institution serving approximately 2.4 million retail customers and 180,000 small and mid-sized business clients across four operating markets. The bank reported total assets of 38.2 billion and net interest income of 1.1 billion in its most recent audited financial year. Its flat-rate cashback programme, introduced in 2009, has been one of the longest-running such programmes among mid-market banks in its footprint.

Under the discontinued programme, eligible debit and credit card holders received 1.25 per cent cashback on all qualifying transactions, uncapped. The programme will be replaced by a three-tier structure:

- **Halcourt Signature Rewards** — available to customers holding combined deposit and investment balances above 75,000, offering up to 2.5 per cent category-based rewards.
- **Halcourt Plus Rewards** — available to customers holding combined balances between 15,000 and 75,000, offering 1.0 per cent flat-rate rewards on qualifying categories.
- **Halcourt Everyday Banking** — the remaining customer base, receiving no rewards component. Monthly account fees on this tier are unchanged.

Approximately 61 per cent of current cashback participants will fall into the Halcourt Everyday Banking tier under the new structure and will therefore no longer receive any rewards. A further 29 per cent will qualify for Halcourt Plus and the remaining 10 per cent for Halcourt Signature.

Halcourt Bank expects the programme transition to reduce consolidated rewards-related expense by approximately 140 million annually, against a projected one-time retention and migration cost of 22 million recorded in the current financial year. Management has guided that approximately 3 per cent of affected retail customers may transition away from the bank as a consequence of the change; this has been factored into the bank's retail deposit forecasts for 2026 and 2027.

Sarah Chen, Chief Executive Officer of Halcourt Bank, commented:

"Our cashback programme has served our customers well for seventeen years, but the retail banking environment has moved on. Flat-rate rewards no longer reflect how our customers use our products or how we create value for them. The new tiered framework rewards the depth of relationship our customers have with us and frees us to invest in the digital and advisory capabilities they increasingly ask for. We understand that change is difficult, and we are committed to supporting every customer through this transition."

Customers in the Halcourt Everyday Banking tier will be offered a one-time transition credit of 45 upon acceptance of the new terms, applied to their primary account before 31 December 2026. Customers moving to Halcourt Signature will retain their existing cashback accrual through 30 September 2026 and will be enrolled automatically in the new programme on 1 October 2026 unless they opt out. A dedicated transition support line will operate from 20 July 2026 and a full FAQ has been published to the bank's customer portal.

The Board of Directors of Halcourt Bank approved the transition at its meeting on 8 July 2026. The decision followed a twelve-month strategic review led by Chief Strategy Officer David Reynolds and Chief Financial Officer Marta Oliveira, with external advisory support on customer analytics and programme design. The Board has indicated that the transition is aligned with the bank's three-year strategic plan published at its Investor Day in March 2026.

Halcourt Bank will host an investor and media briefing at 14:00 local time on 16 July 2026 to discuss the transition in further detail. A replay will be available on the bank's investor relations portal for thirty days following the briefing.

— ENDS —

About Halcourt Bank

Halcourt Bank is a mid-market retail and commercial bank serving approximately 2.4 million retail customers and 180,000 business clients across four operating markets. Founded in 1987, the bank operates a branch network of 412 locations, a fully integrated digital banking platform, and specialist commercial lending, wealth management, and trade finance business lines. Halcourt Bank is authorised and regulated by the relevant banking supervisory authorities in each of its operating markets.

Media enquiries
Priya Natarajan, Head of External Communications
press@halcourt.example

Investor relations
Thomas Albrecht, Head of Investor Relations
ir@halcourt.example

This announcement contains forward-looking statements regarding Halcourt Bank's rewards programme transition, expected financial impact, and customer migration assumptions. Actual outcomes may differ materially from those expressed or implied. Halcourt Bank undertakes no obligation to update these statements except as required by applicable regulation.

---

## End of seed document
