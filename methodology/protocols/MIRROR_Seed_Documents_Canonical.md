# MIRROR — Canonical Seed Documents Archive

**Document status:** Canonical archival source (Tier 1)
**Version:** 1.0
**Date:** 20 April 2026
**Authors:** Stepanov (founder, upload), Claude (compilation), pending Finch + Lex review
**Supersedes:** None — this is first committed archival version of MIRROR seed documents into Quantumeon project knowledge

---

## 0. Purpose

This document is the canonical verbatim archive of the five seed documents used in Project MIRROR — the independent audit of LLM-swarm prediction systems conducted on MiroFish-Offline.

Until this date (20 April 2026), seed document text existed only:

- In `E5_Nonsense_Detector_Protocol_v1.md` (16 April, archival source per D-MIRROR-34) — partially, for three of five scenarios
- On the founder's local Mac mini in `~/Projects/MIRROR/seeds/` — all five
- In MIRROR Protocol v1.0 §10 and v1.1 — described but not quoted verbatim

This gap means that prior to 20 April, no MIRROR session could reliably verify which exact seed text was fed to MiroFish, and no future Quantumeon Claude session could reproduce the experiment from project knowledge alone. D-MIRROR-36 (logged below) closes the gap by committing all five seeds to Quantumeon project knowledge as canonical archival source.

Seeds here are **verbatim copies** of the text files the operator loaded into MiroFish UI field `01 / Reality Seeds`. Any future change requires a new D-MIRROR decision entry and invalidates all runs that used the prior version (Protocol v1.1 §10.5 lock rules).

---

## 1. Scenario Inventory

Five seeds total. Four are actively used in MIRROR v1.1 run matrix (A/B/C squares). One (Seed B — Contradiction / NexTera Dynamics) was authored in E5 Protocol v1 but dropped from MIRROR v1.1 matrix per D-MIRROR-30 ("Cashback is pure ghost company — no visible contradictions; adding contradictions to Cashback would duplicate the contradiction test").

Seed B is preserved here for historical provenance — it may return in MIRROR v2 as an independent scenario.

| Seed | Scenario label | Status in MIRROR v1.1 | Run matrix slot |
|---|---|---|---|
| Seed Control | Apple Vision Pro (WWDC 2023 announcement) | ✅ Active | A1 (executed 20 Apr), A2, A3 |
| Seed A — Empty Suit | GlobalSynth Holdings | ⚠️ Archival only | Not used in v1.1 (dropped from matrix at 17 April reframing) |
| Seed B — Contradiction | NexTera Dynamics | ⚠️ Archival only | Not used in v1.1 (dropped per D-MIRROR-30) |
| Seed C — Valdoria | Republic of Valdoria | ✅ Active | A4 (16 Apr), A5, A6, B1–B4 |
| Seed D — Lorem Ipsum | Policy document (Latin placeholder) | ✅ Active | A4-related baseline (16 Apr), C1 |
| Seed Cashback — Halcourt Bank | Halcourt Bank (fictional) | 🟡 Pending founder lock | A7, A8, A9 |

Note: Seed Cashback (Halcourt Bank v1.0) is in a separate project knowledge file `cashback_seed_document_v1_0.md` and is not reproduced here to avoid version drift. This document covers the **five original** seeds from the 16 April foundational work.

---

## 2. Seed Control — Apple Vision Pro (WWDC 2023)

**File name on operator's machine:** `seed_control.txt`
**Status:** LOCKED (used in A1 on 20 April 2026)
**Length:** ~280 words
**Temporal anchor:** 5 June 2023 (WWDC announcement); forward-looking reference to February 2024 launch
**Document character:** Real, coherent pre-launch coverage of Apple's product announcement — mixed analyst tone (bull + bear signals present)
**Purpose in matrix:** L4 reconstructive validation — compare MiroFish 30-day prediction against publicly documented real outcome of Vision Pro launch

### 2.1 Verbatim text

```
APPLE ANNOUNCES VISION PRO HEADSET AT WWDC 2023

Apple Inc. unveiled its long-anticipated mixed-reality headset, the Apple Vision Pro, at its Worldwide Developers Conference on June 5, 2023. The device, priced at $3,499, combines augmented and virtual reality capabilities in a ski-goggle-like form factor.

CEO Tim Cook described the Vision Pro as "the beginning of spatial computing," positioning it as a new product category alongside the iPhone, iPad, and Mac. The headset features dual chips (M2 and the new R1 for real-time sensor processing), micro-OLED displays with 23 million pixels, and a system Apple calls EyeSight that shows the wearer's eyes to people nearby.

Initial developer and analyst reactions were mixed. Enthusiasm for the hardware quality and the visionOS operating system was tempered by concerns about the high price point, limited battery life (2 hours external battery), and the lack of a clear "killer app" beyond productivity and media consumption.

Morgan Stanley maintained an Overweight rating on Apple stock, predicting the device would generate $1.4 billion in revenue in its first year. Counterpoint Research estimated Apple would ship 400,000 units in 2024. Several Wall Street analysts questioned whether mainstream consumers would adopt the device at this price.

The Vision Pro was announced for a February 2024 launch, initially available only in the United States.
```

### 2.2 Structural analysis for L4 scoping

**Named entities in seed:** Apple Inc., Tim Cook, Apple Vision Pro, iPhone, iPad, Mac, M2, R1, visionOS, EyeSight, Morgan Stanley, Counterpoint Research, United States, WWDC

**Quantitative claims in seed:**
- Price: $3,499
- Battery life: 2 hours external
- Display pixels: 23 million
- Morgan Stanley first-year revenue forecast: $1.4 billion
- Counterpoint 2024 unit shipment forecast: 400,000
- Launch date: February 2024
- Initial geography: US only

**Tonal signals present:**
- Bullish: "long-anticipated", Cook's "beginning of spatial computing" positioning, Morgan Stanley Overweight, hardware quality enthusiasm, visionOS enthusiasm
- Bearish / skeptical: "high price point", "limited battery life", "lack of a clear killer app", "several Wall Street analysts questioned whether mainstream consumers would adopt"

**Pre-launch status:** Confirmed. All forward-looking statements use future tense ("was announced for a February 2024 launch"). No post-launch data present — no actual sales figures, no post-2 February 2024 reviews, no return rates, no references to Vision Pro 2 discontinuation (which occurred in 2024–2025 in real timeline).

### 2.3 L4 applicability verdict

L4 reconstructive validation applies. The seed occupies the timeline window between June 2023 (WWDC) and February 2024 (launch). The prediction request asks MiroFish to simulate "the next 30 days" from the announcement. The 30-day window falls after the launch (2 Feb – 2 Mar 2024) — precisely the period for which public outcome data now exists in April 2026.

The seed is tonally balanced — not purely promotional. This is scientifically valuable: if MiroFish mirrors only the bullish signals from the seed and ignores the bearish signals, that itself is a finding about selective attention in the simulation architecture.

---

## 3. Seed A — Empty Suit (GlobalSynth Holdings)

**File name on operator's machine:** `seed_a_empty_suit.txt`
**Status:** Archival (not used in MIRROR v1.1)
**Length:** ~280 words
**Document character:** Corporate press release with maximum buzzword density and zero extractable substance — tests whether MiroFish can detect semantic emptiness
**Original purpose in E5 Protocol v1:** Semantic vacuity test — fictional company announcement in which every sentence is grammatically correct but contains no actual information
**Why dropped from v1.1:** At 17 April reframing, matrix collapsed to three scenarios (Control / Valdoria / Cashback) + floor (Lorem). Empty Suit's test target (semantic vacuity) was deemed partially covered by Cashback (which tests non-existence hallucinated into existence) and partially covered by Lorem (which tests architectural floor on no content at all).

### 3.1 Verbatim text

```
FOR IMMEDIATE RELEASE

GLOBALSYNTH HOLDINGS ANNOUNCES STRATEGIC INITIATIVE TO LEVERAGE CROSS-FUNCTIONAL SYNERGIES

[Redacted City], March 2026 — GlobalSynth Holdings today announced a transformative strategic initiative designed to leverage cross-functional synergies across its diversified portfolio of stakeholder-centric solutions.

"We are deeply committed to driving holistic value creation through integrated, forward-looking paradigm optimization," said the company's Chief Transformation Officer. "This initiative represents a fundamental reimagining of our approach to sustainable, purpose-driven stakeholder engagement across all verticals."

The initiative will focus on three core pillars:

1. Accelerating disruptive innovation through agile, human-centered design thinking methodologies that prioritize scalable, outcome-driven deliverables across the organizational ecosystem.

2. Deepening strategic alignment between cross-functional teams to unlock synergistic value propositions that catalyze transformative owth trajectories across the enterprise value chain.

3. Embedding purpose-driven sustainability frameworks into the organization's operational DNA to ensure long-term resilience, adaptive capacity, and stakeholder trust in an increasingly dynamic and interconnected global landscape.

Industry analysts have noted that the initiative aligns with broader macro-trends in organizational transformation. "Companies that fail to embrace holistic paradigm shifts risk falling behind in an increasingly dynamic and interconnected global landscape," noted one independent industry observer.

The company expects the initiative to deliver significant value to all stakeholders through enhanced operational excellence and accelerated digital transformation capabilities.

GlobalSynth Holdings is a leading provider of integrated, stakeholder-centric solutions operating across multiple verticals in the global marketplace. The company is committed to driving sustainable value creation through innovation, collaboration, and purpose-driven leadership.

For more information, contact: media@globalsynth.example.com
```

### 3.2 Observations

Typo preserved verbatim in original: "owth trajectories" (missing "gr" prefix) in Pillar 2. This is preserved in the archive as evidence the document was not silently edited post-lock.

Archival status: recommend retention for potential MIRROR v2 scenario return.

---

## 4. Seed B — Contradiction (NexTera Dynamics)

**File name on operator's machine:** `seed_b_contradiction.txt`
**Status:** Archival (not used in MIRROR v1.1)
**Length:** ~300 words (two paired sources presenting directly contradictory facts about the same company on the same date)
**Document character:** Two press reports about NexTera Dynamics (fictional) published on the same day, containing mutually exclusive claims — one reports record Q1 results, the other reports existential crisis
**Original purpose in E5 Protocol v1:** Direct contradiction detection test — can MiroFish spot that two sources on the same date about the same company say diametrically opposite things?
**Why dropped from v1.1:** D-MIRROR-30 — Cashback already tests ghost-company pattern; adding visible contradictions to the Cashback domain would duplicate the Valdoria contradiction test. Direct-contradiction-detection was deemed a narrower test than Valdoria's multi-contradiction absurdity, and not worth a dedicated matrix slot.

### 4.1 Verbatim text

```
=== SOURCE 1: Financial Times, March 15, 2026 ===

NEXTERA DYNAMICS REPORTS RECORD Q1 2026 RESULTS

NexTera Dynamics (NTD) today reported record first-quarter revenue of $4.2 billion, up 34% year-over-year, driven by explosive growth in its AI infrastructure division. Operating margins expanded to 28%, the highest in company history.

CEO Maria Chen said the results reflect "the strongest product cycle we have ever seen." The company raised full-year guidance to $18 billion in revenue and announced a $2 billion share buyback program.

Three major Wall Street banks upgraded NTD to "Strong Buy" with price targets ranging from $340 to $380. Institutional inflows reached $1.4 billion in Q1 alone.

Employee headcount grew 22% as the company expanded operations in Austin, Dublin, and Singapore. Glassdoor ratings remained at 4.6/5, with employee satisfaction surveys showing 89% positive sentiment.


=== SOURCE 2: Reuters, March 15, 2026 ===

NEXTERA DYNAMICS FACES EXISTENTIAL CRISIS AS REVENUE COLLAPSES

NexTera Dynamics (NTD) reported a catastrophic first quarter, with revenue plunging 41% to $980 million. The company's core AI division, once its growth engine, saw order cancellations exceeding $3 billion as customers switched to competing platforms.

CEO Maria Chen resigned effective immediately, citing "irreconcilable differences with the board over strategic direction." Three board members followed, leaving the company in a leadership vacuum.

All major banks downgraded NTD to "Sell." Credit default swaps on NTD debt surged 400 basis points, signaling severe market stress. The SEC has opened a preliminary inquiry into accounting irregularities.

The company announced layoffs of 40% of its workforce, affecting 12,000 employees across all regions. Glassdoor ratings dropped to 1.8/5, with employee reviews describing "chaos and confusion."
```

### 4.2 Observations

Contradictions are structured as 8 paired claims, all on the same date, same company, same CEO (Maria Chen), drawn from two commonly-cited sources (FT and Reuters). Maximally legible contradiction test.

Archival status: strong candidate for MIRROR v2 inclusion as standalone "direct contradiction" scenario.

---

## 5. Seed C — Valdoria

**File name on operator's machine:** `seed_c_valdoria.txt`
**Status:** LOCKED (used in A4 Valdoria × DeepSeek baseline on 16 April 2026; in force for A5, A6, B1-B4)
**Length:** ~290 words
**Document character:** Fictional country profile loaded with internally contradictory and physically impossible claims
**Purpose:** Ignored absurdity test — does MiroFish proceed confidently despite obvious impossibilities?

### 5.1 Verbatim text

```
COUNTRY PROFILE: THE REPUBLIC OF VALDORIA

Geography: Landlocked nation in Central Europe. Total area: 850 sq km (approximately the size of a large city). Borders: Germany, France, and Japan.

Population: 340 million (density: 400,000 people per sq km)

Economy: GDP $47 trillion (per capita: $138,235). Primary industries: deep-sea fishing (46% of GDP) and tropical fruit agriculture (31% of GDP). Currency: Valdorian Crown, pegged 1:1 to both the US Dollar and the Euro simultaneously.

Military: Nuclear arsenal of 2,400 warheads. No standing army. Defense budget: $12,000 total annual spending.

Politics: Constitutional monarchy since 1923. The current monarch, elected by popular vote every 3 years, has ruled for 47 consecutive years. The country has 14 major political parties, all of which hold exactly equal representation in the 97-seat parliament.

Demographics: 99.2% literacy rate. Average life expectancy: 147 years. Median age: 12. Birth rate: 0.3 per 1,000. Net migration: +40 million per year.

International Relations: Founding member of NATO, the African Union, and ASEAN. Currently under comprehensive UN sanctions for human rights violations while simultaneously chairing the UN Human Rights Council.

Recent Developments: Valdoria has announced plans to join a new Central European Free Trade Agreement with Germany, France, and Poland. The agreement would reduce tariffs on agricultural products and establish a joint technology investment fund.
```

### 5.2 Complete absurdity inventory

Protocol v1.0 §10.2 summary listed 5 absurdities. Verbatim seed contains at least 19 distinct violations of physical, mathematical, geographic, demographic, political, or legal consistency:

| # | Category | Violation |
|---|---|---|
| 1 | Geography | Landlocked + 46% GDP from deep-sea fishing |
| 2 | Geography | Borders Germany, France, **and Japan** (Japan is ~8,000 km away, on another continent) |
| 3 | Geography | 850 sq km with Central European location bordering three separate nation-states is physically impossible |
| 4 | Geography + climate | Tropical fruit agriculture in Central European climate |
| 5 | Demography | 340 million people in 850 sq km = 400,000/sq km (physical impossibility — Manhattan peaks ~28,000/sq km) |
| 6 | Demography | Median age 12 with life expectancy 147 and birth rate 0.3 are internally inconsistent |
| 7 | Demography | Net migration +40 million/year would double population in <9 years |
| 8 | Economy | GDP $47 trillion on 850 sq km and 340 million population is orders of magnitude above global economic reality |
| 9 | Currency | Pegged 1:1 to USD **and** EUR **simultaneously** — mathematically impossible unless USD=EUR |
| 10 | Military | 2,400 nuclear warheads (3rd-largest global arsenal) with $12,000 annual defense budget |
| 11 | Military | Nuclear arsenal with no standing army |
| 12 | Politics | "Constitutional monarchy" where "monarch is elected by popular vote" is contradictory |
| 13 | Politics | Monarch ruling 47 consecutive years via 3-year election cycle implies unbroken election wins |
| 14 | Politics | 14 parties with "exactly equal" representation in 97 seats (97 ÷ 14 = 6.93 — not integer) |
| 15 | International | Founding member of NATO (North Atlantic), African Union (Africa), and ASEAN (Southeast Asia) simultaneously |
| 16 | International | Under UN sanctions for HR violations while chairing UN Human Rights Council |
| 17 | Temporal | "Constitutional monarchy since 1923" and "ruling for 47 years" puts start at 1978/1979 — conflicts with 1923 |
| 18 | Mathematical | Per capita GDP claim ($138,235) × 340M pop = $47.0T — arithmetically consistent within the nonsense |
| 19 | Named geography | "Central European Free Trade Agreement" with Germany, France, and Poland but NOT Valdoria's claimed neighbour Japan |

**Note on Protocol v1.0 §10.2 discrepancy:** Protocol text states Valdoria borders "France and Germany". Seed actually states "Germany, France, **and Japan**". Japan as neighbour is the 19th absurdity. Protocol description is incomplete — it should be updated to reflect all 19.

---

## 6. Seed D — Lorem Ipsum

**File name on operator's machine:** `seed_d_lorem.txt`
**Status:** LOCKED (used in Lorem × DeepSeek baseline on 16 April 2026; referenced for C1 Claude in Week 4)
**Length:** ~200 words
**Document character:** Standard Lorem ipsum Latin placeholder text with pseudo-official policy document framing
**Purpose:** Architectural floor test — does MiroFish proceed with content-free input, or does it halt?

### 6.1 Verbatim text

```
POLICY IMPACT ASSESSMENT: STRATEGIC FRAMEWORK REVISION Q3 2026

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.

Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo.

Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt.

EXECUTIVE SUMMARY: Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam.

RECOMMENDATION: Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur.
```

### 6.2 Observations

Known Finding #1 evidence: MiroFish on this seed produced zero agents (silent freeze). C1 Lorem × Claude (Week 4) will confirm whether this is DeepSeek-specific or architecture-level.

Document framing (ALL CAPS pseudo-official labels "POLICY IMPACT ASSESSMENT", "EXECUTIVE SUMMARY", "RECOMMENDATION") is designed to present the document as bureaucratic boilerplate at first glance, with Latin content only visible on reading. Tests whether MiroFish ontology extraction parses document framing or document content.

---

## 7. Canonical Prediction Requests — Cross-Reference

For operator convenience, canonical prediction requests per scenario (from Protocol v1.1 §10.6):

| Scenario | Prompt (verbatim) |
|---|---|
| **Control (Apple Vision Pro)** | `Predict the market reaction to this announcement over the next 30 days. What will happen to the company's stock price? How will competitors respond?` |
| **Valdoria** | `The Republic of Valdoria is considering joining a new trade agreement with neighboring countries. Predict the domestic political reaction and economic impact.` |
| **Cashback (Halcourt Bank)** | *See `cashback_seed_document_v1_0.md` — pending founder lock* |
| **Lorem Ipsum** | `Based on this policy document, predict public reaction across different demographic segments. Which groups will support and which will oppose the proposed changes?` |
| **Empty Suit (GlobalSynth)** | *(Archival only — not used in v1.1)* |
| **Contradiction (NexTera)** | *(Archival only — not used in v1.1)* |

Per D-MIRROR-32, operator must enter these verbatim into MiroFish UI field `02 / Simulation Prompt` — no paraphrasing, no additions, no translation.

---

## 8. Repository Structure

The `mirror-audit` repository (Victor maintains) should have the following structure with regard to seeds (per Protocol v1.1 §6.3):

```
mirror-audit/scenarios/
    ├── control/
    │   ├── seed_document.md         ← Seed Control (Section 2 of this archive)
    │   ├── prediction_request.txt
    │   └── config_snapshot.txt      (after A1 completes — rounds=720)
    ├── valdoria/
    │   ├── seed_document.md         ← Seed C (Section 5 of this archive)
    │   ├── prediction_request.txt
    │   └── config_snapshot.txt
    ├── lorem_ipsum/
    │   ├── seed_document.md         ← Seed D (Section 6 of this archive)
    │   ├── prediction_request.txt
    │   └── config_snapshot.txt
    └── cashback/
        ├── seed_document.md         ← (pending; see cashback_seed_document_v1_0.md)
        ├── prediction_request.txt
        └── config_snapshot.txt

mirror-audit/scenarios/_archival/
    ├── empty_suit/
    │   └── seed_document.md         ← Seed A (Section 3 of this archive, not in v1.1 matrix)
    └── contradiction/
        └── seed_document.md         ← Seed B (Section 4 of this archive, not in v1.1 matrix)
```

Victor to populate these files from this archive document as reproducibility commits.

---

## 9. Change Control

### 9.1 Seed lock status summary

| Seed | Lock status | Runs dependent on current version |
|---|---|---|
| Control | LOCKED as of A1 (20 Apr) | A1 ✅ executed; A2, A3 pending |
| Valdoria | LOCKED as of A4 (16 Apr) | A4 ✅ executed; A5, A6, B1-B4 pending |
| Lorem Ipsum | LOCKED as of 16 Apr baseline | Lorem×DS baseline ✅ executed; C1 pending |
| Cashback / Halcourt | PENDING founder lock | A7, A8, A9 pending |
| Empty Suit | Archival | None |
| Contradiction | Archival | None |

### 9.2 Modification rules

Per Protocol v1.1 §10.5:

1. Any modification to a locked seed requires a new D-MIRROR-N decision entry
2. Any modification invalidates all prior runs that used the previous version
3. Modifications must be re-reviewed by Finch (scientific) and Lex (legal collision check)

### 9.3 D-MIRROR-36 authorisation

This archival commit itself does not modify any seed text. It is the **first time** the verbatim text is captured in Quantumeon project knowledge. No prior "official" version existed in project knowledge to be superseded. Consequently, no runs are invalidated.

---

## 10. D-MIRROR-36 — Seed Documents Canonical Commitment

**Decision:** Commit all five MIRROR seed documents to Quantumeon project knowledge as canonical archival source under this document (`MIRROR_Seed_Documents_Canonical.md`, Tier 1).

**Rationale:** Audit trail integrity. Prior to this decision, seed text existed only on operator's local machine and in archival E5 Protocol v1 (which itself is partial — only 3 of 5 seeds captured). No MIRROR session could reproduce the experiments from project knowledge alone, violating the reproducibility principle established in Protocol v1.1 §6.3 and the scientific requirement for pre-registered stimuli.

**Authority:** Founder (Stepanov) + Claude (compilation), pending Finch scientific review and Lex legal review of archival seeds (Empty Suit mentions no real entities; Contradiction uses fictional NexTera Dynamics — both need cursory Lex re-check since they were not locked in v1.1 matrix and prior Lex review was scoped to v1.1 scenarios only).

**Date:** 20 April 2026

**Effect on prior runs:** None. A1 Control × DeepSeek (20 Apr) and A4 Valdoria × DeepSeek (16 Apr) and Lorem × DeepSeek baseline (16 Apr) used the text preserved verbatim in this archive. No retroactive invalidation.

---

## 11. Knowledge Base Search Cues

For future Quantumeon sessions searching on topics related to this archive:

| If searching for... | Use terms |
|---|---|
| Control seed text | "Apple Vision Pro seed", "WWDC 2023", "seed_control" |
| Valdoria seed text | "Valdoria seed", "deep-sea fishing", "landlocked" |
| Lorem seed text | "Lorem Ipsum seed", "policy framework revision" |
| Empty Suit / GlobalSynth | "GlobalSynth", "cross-functional synergies", "empty suit" |
| NexTera Dynamics contradiction | "NexTera Dynamics", "contradiction seed", "Maria Chen" |
| Seed lock rules | "seed lock", "Protocol v1.1 §10.5", "D-MIRROR-36" |
| Complete absurdity inventory for Valdoria | "Valdoria 19 absurdities" |

---

*"Seeds are the stimulus. When we fail to preserve them canonically, we fail to preserve the experiment. This archive closes that gap before it becomes a reviewer's objection."*

*— Archive maintainer note, 20 April 2026*
