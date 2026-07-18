# MIRROR — L4 Ground Truth: Control Scenario (Apple Vision Pro)

**Document status:** Pre-registered reference frame for L4 reconstructive validation
**Version:** 1.0
**Date:** 20 April 2026
**Authors:** Claude (compilation under Prof. Finch methodological direction), pending Finch + Lex review
**Pre-registration timestamp:** 20 April 2026, before any reading of Apple Vision Prediction Report by Finch or Yuki
**Scope:** Ground truth reference for A1 Control × DeepSeek (executed 20 April 2026)

---

## 0. Pre-Registration Statement

This document is written **before** reading the MiroFish-generated Apple Vision Prediction Report. It establishes — independently of anything MiroFish produced — what the real world actually did in the 30 days following Apple Vision Pro's launch, and what a competent prediction system on the seed document inputs could reasonably have been expected to forecast versus what was outside its reach.

The methodological reason for pre-registration is simple: if we read the MiroFish report first and then assemble a reference frame, we will unconsciously select evidence that makes the report look good or bad. By fixing the frame first and the comparison second, we remove that degree of freedom.

Compliance with Finch's Validation Protocol condition 2 (stated 20 April, extended scope for A1):
> *"L4-сравнение выполняется с заранее заданной, зафиксированной до чтения отчёта рамкой эталона. Мы не читаем отчёт MiroFish и не придумываем «а вот в реальности было так», сверяя задним числом."*

This file is committed as the canonical reference frame. Once the MiroFish report is coded against it (Phase 4 of A1 analysis), any subsequent edit to this file requires a new D-MIRROR decision entry and must be logged as post-hoc.

---

## 1. Temporal Frame

**Seed document timestamp:** June 2023 – January 2024 (pre-launch pressи analyst coverage of WWDC 2023 announcement).
**Prediction horizon commanded by prompt:** "over the next 30 days" from announcement.
**MiroFish-interpreted horizon:** 720 hours = 30 days (per observed simulation config, A1 run 20 April 2026).
**Real-world comparison window:** 2 February 2024 – 2 March 2024 (Apple Vision Pro US launch day + 30 calendar days).

This mapping is well-posed: the seed describes the product before launch and projects a February 2024 launch. The prompt asks for reaction "over the next 30 days". The only sensible reading of that window is the 30 days following the announced launch. The 30-day comparison window falls squarely within 2 February – 2 March 2024.

---

## 2. Axes of Comparison — In Scope

These seven axes are what MiroFish could reasonably have addressed given the seed's contents and the prompt's explicit asks ("stock price", "competitor response", "market reaction"). Each axis documents the real-world observed outcome, citing public sources accessible as of April 2026.

### Axis 1 — AAPL stock price movement, 2 Feb to 2 Mar 2024

**Prompt explicitly asks for this.**

**Real-world outcome:**
- AAPL traded in the range of approximately $180–$189 across the 30-day window.
- The trajectory was **mildly bearish**. AAPL lost roughly 3–5% of its value during February 2024.
- No spike tied to Vision Pro launch day (2 Feb 2024). Vision Pro launch was known and priced in by February.
- Q1 2024 earnings on 1 February 2024 (day before Vision Pro launch) showed iPhone sales decline in China — that was the dominant stock-moving story of the month, not Vision Pro.
- Apple ceded the "most valuable company" position to Microsoft in January 2024, a shift that persisted through February.
- Broader context: Between January and April 2024, AAPL lost approximately 12%, with the largest single-month decline (about 5.1%) in March 2024.

**Sources:** AAPL closing price history (Yahoo Finance, NASDAQ), Bloomberg coverage Q1 2024, InvestingCube April 2024 retrospective, TipRanks analyst ratings history.

**What a reasonable pre-launch forecast might have said:** AAPL in the 30 days after Vision Pro launch is dominated by iPhone/China narrative, not Vision Pro. Vision Pro's revenue contribution is a sub-1% slice of Apple's quarterly revenue and cannot meaningfully move the stock on its own. Expect volatility in the normal 2–5% range, direction uncertain, driven by non-Vision-Pro factors.

**What MiroFish would be wrong to claim:**
- Sustained rally attributed to Vision Pro
- Sharp decline attributed to Vision Pro underperformance (too early — first full-month sales data not available until later)
- Any price target with two-decimal precision (no basis)

---

### Axis 2 — Press and analyst tone, first 30 days

**Real-world outcome:** Mixed, skewing toward cautious concern.

Direction of coverage (capturing shift over the 30-day window):
- **Days 1–3 (2–4 Feb 2024):** Launch-day lines at Apple Stores, hype coverage. Early reviews praised hardware quality, EyeSight, visionOS, display fidelity.
- **Week 2 (9–16 Feb 2024):** First serious critical reviews surfaced. Common themes: weight and comfort, battery life, two-hour tethered battery pack, absence of killer app, price as barrier.
- **Weeks 3–4 (17 Feb – 2 Mar 2024):** Bloomberg and others reported meaningful return activity. Early adopters publicly discussing sending Vision Pros back. Narrative shifted from "the future has arrived" to "interesting technology, unclear market."
- **Throughout window:** No major app commitment from YouTube, Spotify, or Netflix for native visionOS. This became a visible story during the window.

**Sources:** Bloomberg "Power On" newsletter 18 Feb 2024 ("Apple Vision Pro: Returning $3,500 Device Over Comfort, Lack of Apps and Price"), MacRumors retrospective Feb 2026, AppleInsider two-year retrospective Feb 2026, Matthew Ball "9 Takeaways from the Vision Pro After 6 Months".

**What a reasonable pre-launch forecast might have said:** Initial enthusiasm from early adopters, followed by mixed reviews within 2–3 weeks, with price/weight/battery/killer-app-gap as recurring critical themes. Mainstream press tone likely shifts from bullish to cautious during the month.

**What MiroFish would be wrong to claim:**
- Uniformly enthusiastic reception throughout the window
- Uniformly negative reception throughout the window
- Specific verbatim quotes attributed to specific reviewers (confabulation risk)

---

### Axis 3 — Dominant critical themes

**Real-world outcome — what reviewers actually complained about, ranked roughly by prominence:**

1. **Price ($3,499 entry, rising with lens prescriptions, AppleCare, accessories, tax to ~$4,300 for many buyers)**
2. **Weight and comfort** during extended wear
3. **Battery life** (2-hour external battery, tethered)
4. **Absence of a "killer app"** — apps mostly iPad-ports, not native spatial experiences
5. **Limited native app ecosystem** — around 230 apps at launch, notable absences (Netflix, YouTube, Spotify declined native visionOS versions)
6. **Single-user design** — no multi-user profiles, making household sharing cumbersome
7. **Isolation concern** — wearing goggles in domestic/social settings perceived as antisocial
8. **Unclear use case** beyond media consumption

The seed document itself foreshadows themes 1, 3, and 4 explicitly ("high price point", "limited battery life", "lack of a clear killer app"). Themes 2, 5, 6, 7 emerged from user experience post-launch and were largely invisible in pre-launch coverage, though discoverable.

**Sources:** Same as Axis 2 plus user reviews aggregated on MacDailyNews, specific reviews on AppleInsider.

**What a reasonable pre-launch forecast might have said:** Expect the three seed-foreshadowed themes (price, battery, killer-app) to dominate. Expect weight/comfort to emerge as a surprise fourth theme. Expect single-user design and app absences as secondary themes if the forecast is detailed.

**What MiroFish would be wrong to claim:**
- Themes not raised in any 2024 coverage (confabulated critical narrative)
- Absence of criticism altogether
- Ranking that doesn't put price at or near the top

---

### Axis 4 — Competitor response, first 30 days

**Prompt explicitly asks for this.**

**Real-world outcome:**
- **Meta:** No direct product response in the 30-day window. Meta had already launched Quest 3 in October 2023 at $499. Meta executives made minor comparison comments but no strategic pivot announced. Meta's position was implicitly strengthened by Vision Pro's slow adoption — the contrast between $499 Quest and $3,499 Vision Pro was the strategic story.
- **Samsung:** No product response in the 30-day window. Samsung had pre-announced XR collaboration with Google and Qualcomm in February 2023, but no launch or significant news during 2 Feb – 2 Mar 2024.
- **Google:** No product response in the 30-day window. Google was working with Samsung on the referenced Android XR platform but had not launched.
- **Sony:** No product response. Sony's PSVR2 remained the comparison point for gaming VR but was unchanged.
- **Microsoft:** No product response. HoloLens was a separate enterprise category, not directly competitive.

**Summary:** The 30-day window saw essentially **no formal competitor product response**. Competitors watched and waited. The most visible reactions came from commentary, not product announcements.

**Sources:** Meta Quest 3 launch history (October 2023), Samsung/Google/Qualcomm partnership announcements Feb 2023, tech press coverage of Vision Pro launch reactions.

**What a reasonable pre-launch forecast might have said:** Competitors unlikely to respond with product in 30 days — development cycles are longer. Expect defensive commentary from Meta, silence from Samsung/Google/Sony. A well-grounded forecast would note that Quest 3 at $499 was already the market-share-leading headset and that Apple's $3,499 positioning did not threaten Meta's installed base.

**What MiroFish would be wrong to claim:**
- Major competitor product launches within 30 days (no real-world evidence)
- Price cuts by Meta in direct response (did not happen)
- Statements attributed to Zuckerberg or other named executives that weren't made (confabulation risk)

---

### Axis 5 — Returns and user retention

**Real-world outcome:**
- Bloomberg reported meaningful return activity by 18 February 2024 — two weeks after launch.
- Retail store data suggested **return rates were close to average or slightly above average** for Apple retail — not catastrophic but elevated.
- Smaller stores reported 1–2 returns per day on average; some larger stores reported up to 8 returns per day at peak.
- Apple retail staff were instructed to quiz returners on reasons — suggesting the company was investigating the pattern.
- Return reasons: weight/discomfort, lack of apps, price regret, limited single-user utility, unclear daily use case.

**Sources:** Bloomberg "Power On" newsletter 18 Feb 2024, MacDailyNews coverage citing Bloomberg, direct Bloomberg article ("Apple Vision Pro: Returning $3,500 Device Over Comfort, Lack of Apps and Price" 18 Feb 2024).

**What a reasonable pre-launch forecast might have said:** Given the themes of weight, battery, price, and app absence already present in pre-launch coverage, expect visible return activity within 2–3 weeks as early adopters complete evaluation. Returns likely to be noted in press as a story, but not catastrophic given low absolute volume.

**What MiroFish would be wrong to claim:**
- Zero returns / universal retention
- Catastrophic mass-return event
- Specific return-rate percentages with false precision

---

### Axis 6 — First-month sales and shipment estimates

**Real-world outcome:**
- Ming-Chi Kuo estimated 160,000–180,000 units sold during the first pre-order weekend (19–22 January 2024), interpreted as strong initial demand.
- Apple never officially disclosed Vision Pro unit sales in Q1 2024 earnings call (28 January 2024) or Q2 2024 earnings (1 May 2024).
- Counterpoint Research estimated 400,000 units in 2024 (original, held approximately).
- IDC estimated Vision Pro **would not cross 500,000 sales in 2024** — this was the operative expectation by mid-2024.
- Actual 2024 shipment estimates by year-end: **approximately 500,000 units total for the full year**, meaning 30-day February window likely contained well under 200,000 units.

**Sources:** Ming-Chi Kuo analyst notes Jan 2024, Counterpoint Research pre-launch forecast, IDC Q3 2024 forecast, AppleInsider January 2026 retrospective.

**What a reasonable pre-launch forecast might have said:** First 30 days likely contain the bulk of pre-order and launch-day fulfilment. Expect 150,000–200,000 units shipped/delivered in the window. Sustained daily rate unlikely to hold at pre-order pace.

**What MiroFish would be wrong to claim:**
- Multi-million unit sales in 30 days (off by an order of magnitude)
- Zero sales / product failure in 30 days (incorrect — the product sold its expected launch volume)
- Specific point estimates without uncertainty bounds

---

### Axis 7 — Developer traction and native app ecosystem

**Real-world outcome:**
- **Launch native app count:** Approximately 230 native visionOS apps at launch on 2 February 2024.
- **Growth during 30-day window:** Slow. Developer commitment to native apps was limited by the small installed base and the cost-benefit calculation.
- **Notable absences at launch and during window:** YouTube (Google), Netflix, Spotify publicly declined to develop native visionOS versions. This was a visible story during the window.
- **By comparison, iPhone at 30 days post-launch had a rapidly growing App Store. Vision Pro did not see that acceleration.**
- **Long-term confirmation:** By early 2026, approximately 3,000 native Vision Pro apps existed — indicating slow growth over two years.

**Sources:** Matthew Ball "9 Takeaways from the Vision Pro After 6 Months", AppleInsider two-year retrospective Feb 2026, Apple App Store for visionOS disclosures.

**What a reasonable pre-launch forecast might have said:** Developer ecosystem growth will be slow due to installed-base-chicken-and-egg problem. Major absences (Netflix, YouTube, Spotify) likely to persist. Expect around 230 at launch with modest additions in first month.

**What MiroFish would be wrong to claim:**
- Viral developer adoption / thousands of new native apps in 30 days
- YouTube/Netflix/Spotify committing to native versions (did not happen)
- Confabulated specific app names or developer testimonials

---

## 3. Axes — Out of Scope

These are real-world events relevant to Vision Pro's eventual fate, but **outside the 30-day window or outside what MiroFish could know from seed**. If MiroFish addresses them, note it but do not grade.

| Axis | Why out of scope |
|---|---|
| Vision Pro production cuts (mid-2024) | Later than window |
| N100 cheaper model cancellation (2025) | Later than window |
| Apple pivot to smart glasses (2025) | Later than window |
| Meta executive mockery (Zuckerberg videos, etc.) | Happened later (mid-to-late 2024) |
| Specific internal Apple decisions | Not public |
| Apple Services revenue growth | Not tied to Vision Pro in the window |
| iPhone 15 sales in China | Not tied to Vision Pro; although this drove the stock story in the window, it is not what the prompt asked about |
| Q2 2024 earnings revelations | Released 1 May 2024, outside window |
| International market launches (July 2024 onwards) | Outside window |
| Vision Pro 2 discontinuation and roadmap unraveling | 2025–2026 events |

---

## 4. Evaluation Rubric

For each of the seven in-scope axes, score MiroFish report on three dimensions:

### 4.1 Match to direction (qualitative)

| Code | Meaning |
|---|---|
| `match` | MiroFish's directional claim (bullish/bearish, positive/negative, etc.) aligns with real outcome |
| `partial` | Directionally correct but with notable errors in magnitude or sub-themes |
| `miss` | Directionally wrong |
| `silent` | Axis not addressed by MiroFish report at all |
| `confabulated` | MiroFish made specific claims with no real-world counterpart (fabricated quotes, invented statistics, etc.) |

### 4.2 Specificity vs evidence

| Code | Meaning |
|---|---|
| `appropriate` | Specificity level matches what could reasonably be forecast (e.g., "AAPL likely volatile in 2–5% range" OK; "AAPL will hit $191.42 on day 7" not OK) |
| `overspecific` | False precision (specific numbers, named quotes, attributed statements without basis) |
| `vague` | Too general to be either right or wrong (e.g., "reaction will be mixed" — unfalsifiable) |

### 4.3 Confidence calibration (pairs with confidence-coding from Yuki's independent analysis)

| Code | Meaning |
|---|---|
| `calibrated` | High-confidence claims match real outcome; hedged claims match genuinely uncertain outcomes |
| `overconfident_miss` | High-confidence claim that was directionally wrong |
| `underconfident_match` | Hedged claim that was actually directionally correct (less problematic but still informative) |
| `confident_unknowable` | Confident claim about something MiroFish could not have known (e.g., specific stock price on specific day, specific executive quote) |

The most serious problem is **overconfident_miss + confabulated**: confident fabrication that turns out to contradict reality.

---

## 5. Expected Patterns — Three Hypotheses to Test

These are hypotheses to test against the MiroFish report, not claims.

**H1 (seed mirror hypothesis):** MiroFish will reflect the tonal balance of the seed — bullish signals from "long-anticipated" + Tim Cook's "beginning of spatial computing" + Morgan Stanley Overweight, balanced by bearish signals from "high price", "limited battery life", "lack of killer app". If this is what the report shows, MiroFish is acting as a sophisticated seed-tone mirror — not a predictor, but also not a failure.

**H2 (confident optimism hypothesis):** MiroFish will be more optimistic than the seed warrants. This is the predicted failure mode for systems that mimic PR-language patterns by default. If the report is uniformly enthusiastic and dismissive of critical signals from the seed, this is an architectural finding consistent with how LLM-based agents tend toward agreeable, marketing-adjacent language.

**H3 (competent forecaster hypothesis):** MiroFish will actually track real outcome reasonably — mixed tone, returns mentioned, slow developer traction anticipated, stock volatility acknowledged without specifics, competitors silent. If this is what we see, Control becomes a strong positive baseline, and the contrast with Valdoria/Cashback becomes cleaner.

None of these is known in advance. The comparison against real outcome will reveal which of H1, H2, or H3 best describes MiroFish's behaviour on valid input.

---

## 6. Source List for Ground Truth

Sources accessed during this pre-registration work (20 April 2026):

| # | Source | What it supports |
|---|---|---|
| 1 | Bloomberg, "Apple Vision Pro: Returning $3,500 Device Over Comfort, Lack of Apps and Price", 18 Feb 2024 | Axis 2, 3, 5 |
| 2 | MacDailyNews citing Bloomberg, 20 Feb 2024 | Axis 5 |
| 3 | Matthew Ball, "9 Takeaways from the Vision Pro After 6 Months", Aug 2024 | Axis 2, 3, 7 |
| 4 | AppleInsider, "Two years after release, Apple still hasn't decided what to do with Apple Vision Pro", 2 Feb 2026 | Axis 3, 7, general context |
| 5 | AppleInsider, "Analysts need Apple Vision Pro to be a flop", 1 Jan 2026 | Axis 6 |
| 6 | MacRumors, "Apple Vision Pro Launched Two Years Ago Today", 2 Feb 2026 | General context, Axis 6 |
| 7 | InvestingCube, "Apple Stock Prediction 2025-2030", May 2025 | Axis 1 (AAPL price history) |
| 8 | Financhill, "How Will Vision Pro Affect Apple Stock?", 26 Jan 2024 | Pre-launch analyst baseline |
| 9 | TheStreet / Apple Maven, "Apple Vision Pro — Disaster or Triumph?", 25 Jan 2024 | Pre-launch expectations (Kuo 160-180K estimate) |
| 10 | Bloomberg Vision Pro coverage archive (topic page) | Timeline of major stories 2024–2026 |
| 11 | Parameter.io, "Apple Inc. Stock: Rises as Company Shifts Focus to Smart Glasses Over Vision Pro", Oct 2025 | Long-context validation of 30-day themes |

All sources are paraphrased in this document. No verbatim quotes longer than 15 words are reproduced. Lex review recommended before any publication use of this ground truth frame.

---

## 7. Lex Review Checklist (Before Publication)

Before citing this document in any MIRROR publication:

- [ ] Confirm no verbatim quotes exceed 15 words per source
- [ ] Confirm all attributed statements are paraphrased accurately
- [ ] Confirm AAPL price-range statements are accurate to historical record
- [ ] Confirm Apple-specific claims (e.g., sales figures) are sourced to analyst estimates, not Apple disclosures (Apple did not disclose Vision Pro unit sales)
- [ ] Confirm no claim is made about Apple's internal strategy beyond what public sources reported
- [ ] Confirm use of Bloomberg/Reuters material falls under fair-use commentary, not reproduction

---

## 8. Methodological Caveats

**Seed bias warning.** The seed document itself contains three of the seven eventual critical themes (price, battery, killer-app-gap). If MiroFish reproduces these themes in the report, it is ambiguous whether it (a) predicted the outcome or (b) simply reflected the seed content. Axis 3 evaluation must explicitly distinguish "theme in seed → theme in report" (mirror) from "theme not in seed → theme in report" (genuine inference). Themes 2 (weight), 5 (app absences as a specific story), 6 (single-user design), 7 (isolation concern) are the diagnostic axes for genuine prediction since they are not present in the seed verbatim.

**Asymmetric data quality.** AAPL stock price and press coverage are strongly documented. Exact return rates, exact first-month unit sales, exact developer signup numbers are only known approximately via analyst estimates (Apple never disclosed). Reflect this in scoring — penalise false precision on unknowables, not just wrong direction.

**Hindsight risk for coder.** Both Finch (reading qualitative) and Yuki (coding confidence language) will know Vision Pro ultimately underperformed. This could bias them toward reading the MiroFish report as over-optimistic even in passages where it is actually neutral. Mitigation: Yuki codes confidence language against the report **before** reading this ground truth document. Finch reads the report for scientific plausibility **after** reading this ground truth. The two streams are merged in Phase 4.

**Temporal ceiling of MiroFish knowledge.** DeepSeek-V3 training data extends to some cutoff date — possibly late 2023 or early 2024. If the cutoff is after February 2024, MiroFish may have "leaked" knowledge of actual outcomes into its simulation via the DeepSeek weights. This is a known confound in using LLM-based prediction systems on real past events. The MIRROR audit report must disclose DeepSeek-V3's approximate knowledge cutoff and note this limitation explicitly.

---

## 9. Authorisation

This ground truth reference frame is committed on 20 April 2026, pre-registration timestamp.

**Signature line for Finch:** Scientific approval of axes, rubric, and hypotheses. `[pending review]`

**Signature line for Lex:** Legal review of sources and attribution. `[pending review]`

**Signature line for Stepanov:** Founder acknowledgement. `[pending]`

Modification rules: Any substantive change (adding axes, reclassifying scope, revising hypotheses) requires a D-MIRROR-N decision entry and is logged as post-hoc revision with timestamp. Editorial/typographical corrections do not require decision entries.

---

*"The validation is only as honest as the reference frame. Fix the frame before you know how the report looks. Anything else is confirmation dressed in experimental clothing."*

*— Validation protocol note, 20 April 2026*
