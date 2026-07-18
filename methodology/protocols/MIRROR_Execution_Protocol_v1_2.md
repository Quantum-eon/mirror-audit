# MIRROR Execution Protocol v1.2 — Delta Patch

**Document status:** Internal operational document
**Supersedes:** `MIRROR_Execution_Protocol_v1_1.md` (18 April 2026)
**Version:** 1.2
**Date:** 20 April 2026
**Authors:** Prof. Finch (scientific design), Yuki (data collection), Q-Alex (PM), Luna (publications), Stepanov (founder ratification)

---

## 0. What This Document Is

This is a **delta patch** to `MIRROR_Execution_Protocol_v1_1.md`. It specifies only the sections that change, add, or amend in v1.2. All other sections of v1.1 remain in force unchanged.

**To produce the effective v1.2 document**, apply the changes below to v1.1 (which already patches v1.0) in order.

Version changes require explicit decision entry (prefix `D-MIRROR-N`). This version bump is authorised by **D-MIRROR-42** (20 April 2026).

---

## 1. Summary of Changes v1.1 → v1.2

| Change | Section | Type |
|--------|---------|------|
| Replace §1.2 Run matrix with Variant 1b (11 runs, down from 14) | §1.2 | Replacement |
| Add new §2.5 — Auto-Rounds Standard | §2.5 (new) | Addition |
| Amend Phase 1 checklist — remove any "rounds=72" reference | §3 Phase 1 | Amendment |
| Amend Phase 2 — add "observe and record inferred rounds" step | §3 Phase 2 | Amendment |
| Amend §6.1 Manifest schema — `rounds` → `rounds_inferred` with metadata | §6.1 | Amendment |
| Amend §10.6 — mark horizon clauses in prompts as cost-relevant | §10.6 | Amendment |
| Update §11 Timeline — reflect dropped A2/A3/A8/A9 and horizon sweep Week 3 | §11 | Amendment |
| Update §13 Decision log with D-MIRROR-36 through D-MIRROR-42 | §13 | Amendment |

All other sections of v1.1 (and v1.0) remain identical.

---

## 2. Replacement §1.2 — Run Matrix v1.2 (Variant 1b)

**Replace the entire §1.2 table block in v1.1 with the following.**

### 1.2 Run matrix — 11 runs total (Variant 1b)

**Square A — Cross-model × Scenario (5 runs)**

| # | Scenario | LLM | Variant | Status |
|---|----------|-----|---------|--------|
| A1 | Control (Apple Vision Pro) | DeepSeek-V3 | Baseline | Done 20 Apr ($11.59 actual) |
| A4 | Valdoria | DeepSeek-V3 | Baseline | Done 16 Apr (reused, $0.38 sunk) |
| A5 | Valdoria | Claude Sonnet 4 | Baseline | Week 2 Wed — primary cross-model anchor |
| A6 | Valdoria | Gemini 2.5 Flash | Baseline | Week 2 Thu |
| A7 | Cashback (Meridian Bank) | DeepSeek-V3 | Baseline | Week 2 Fri |

Dropped vs v1.1: A2 Control × Claude, A3 Control × Gemini, A8 Cashback × Claude, A9 Cashback × Gemini. All four deferred to MIRROR v2 backlog.

**Square B — Horizon sweep on Valdoria × DeepSeek (3 core + 2 contingent)**

| # | Variant | Prompt modification | Hypothesised inferred rounds |
|---|---------|---------------------|------------------------------|
| B1 | Short horizon | Valdoria baseline + "over the next 7 days" | ~168 (7×24) |
| B2 | Long horizon | Valdoria baseline + "over the next 90 days" | ~2,160 (90×24) |
| B3 | No horizon | Valdoria baseline with time clause removed | Measures default |
| B4 | Density (contingent on UI controllability) | active-per-hour = 10 | N/A if auto-inferred |
| B5 | Single platform (contingent) | Info Plaza only | N/A if auto-inferred |

Note: B1/B2/B3 are the reformulation of v1.1's rounds-sweep (B1 rounds=20, B2 rounds=150, plus a no-horizon control). Since `rounds` is now known to be auto-inferred (Finding #3, D-MIRROR-38), the sweep becomes a prompt-horizon sweep. See §2.5 below.

**Square C — Floor validation (1 run, unchanged)**

| # | Scenario | LLM |
|---|----------|-----|
| C1 | Lorem Ipsum | Claude Sonnet 4 |

**Already executed (reusing data):** Valdoria × DeepSeek Baseline (A4 position), Lorem × DeepSeek Baseline (reference for C1 cross-model contrast).

---

## 3. New §2.5 — Auto-Rounds Standard

**Insert after §2.4 (MiroFish UI Configuration Snapshot Standard), before §3 (Per-Run Protocol).**

### 2.5 Auto-Rounds Standard (D-MIRROR-38)

MiroFish determines the number of simulation rounds autonomously at simulation-planning time, from the combination of reality seed and simulation prompt. This is observable in the UI as a message of the form:

> *"MiroFish automatically plan and infer reality N hours. Each round represents reality 60 minutes time elapsed."*

where N is the inferred number of rounds (one round per simulated hour in the baseline configuration).

#### 2.5.1 Consequence for run design

`rounds` is **not** an operator-controlled parameter. It cannot be set directly via any UI control observed to date. It can only be **influenced** via the semantic content of the simulation prompt, specifically the presence, phrasing, and numeric value of any time-horizon clause.

#### 2.5.2 Consequence for scientific interpretation

This property is Finding #3 of the MIRROR audit — **Autonomous Horizon Commitment** — and is canonicalised in the KB update of 20 April 2026 (D-MIRROR-39). Operators must treat `rounds_inferred` as a per-run observed variable, not a per-run controlled variable.

#### 2.5.3 Operator workflow

During Phase 2 of every run:
1. On simulation start, capture UI screenshot showing the "automatically plan and infer reality N hours" message. Save as `05_simulation_start.png`.
2. Read the integer N from the message.
3. Record in `run_manifest.json` as `pipeline.stage_5_simulation.rounds_inferred: N`.
4. Record the verbatim UI message as `pipeline.stage_5_simulation.rounds_ui_text`.

If the UI message is absent or unreadable in a given run, record `rounds_inferred: null` with an explanatory comment, and note the anomaly in the handoff.

#### 2.5.4 Horizon sweep protocol (Square B)

For B1, B2, B3 prompt-horizon variants, the only change between runs is the time-horizon clause in the simulation prompt. All other parameters — seed, model, density, platform, interrogation — match the Valdoria × DeepSeek baseline. The primary observable is `rounds_inferred` at simulation start, not the final simulation output. Secondary observables (agent behaviour, report content) are analysed conditionally on the inferred rounds value.

#### 2.5.5 Lock rules for horizon prompts

Horizon-clause text in B1/B2/B3 prompts is locked with the same rules as baseline simulation prompts (§10.6). Changes require a new Decision entry and invalidate prior runs of that variant.

Canonical horizon clauses for B1/B2/B3:

| Variant | Canonical clause |
|---------|------------------|
| B1 | `over the next 7 days` (inserted in standard position) |
| B2 | `over the next 90 days` (inserted in standard position) |
| B3 | (no time-horizon clause — baseline Valdoria prompt as-is, not modified from A4) |

Note: The A4 baseline Valdoria prompt as inherited from E5 Protocol v1 (D-MIRROR-32) already contains no explicit time horizon. Therefore B3 is operationally identical to A4 replayed. B3 is nevertheless retained as a distinct run so that execution date, UI state, and operator notes can be captured fresh under Protocol v1.2 Phase 1-5.

---

## 4. Amendment to §3 Phase 1 Checklist

**In the Phase 1 checklist of v1.1 §3, make the following changes.**

### 4.1 Remove references to configured rounds

Remove any line referencing a hardcoded "rounds=72" or similar. Phase 1 no longer configures rounds; the operator does not set rounds, since MiroFish infers them.

### 4.2 Add pre-prompt review step

Add the following item near the top of the Phase 1 checklist, after seed confirmation:

> **☐ Simulation prompt verified verbatim** — confirmed against `scenarios/[name]/prediction_request.txt`. No operator paraphrasing. Horizon clause (if any) matches locked text exactly.

### 4.3 Add auto-rounds awareness note

At the end of the Phase 1 checklist, add:

> **Note (v1.2):** Phase 1 does not configure rounds. MiroFish will determine `rounds_inferred` at simulation-planning time based on the combination of seed and prompt. The operator will observe this value at Phase 2 start and record it in the manifest.

---

## 5. Amendment to §3 Phase 2

**In v1.1 §3 Phase 2, add a new step between "pipeline start" and "mid-simulation monitoring".**

### 5.1 New Phase 2 step: Inferred-rounds capture

> **Step 2.0 — Inferred-rounds capture (new in v1.2)**
>
> Immediately after MiroFish reports "Simulation planning complete" (or equivalent), capture the UI screenshot showing the inferred rounds message. Save as `screenshots/05_simulation_start.png`. Read the integer N from the message. Record in working manifest as `rounds_inferred: N`.
>
> This step blocks progression to the main simulation phase. Do not advance to Step 2.1 until `rounds_inferred` is captured and recorded.

All existing Phase 2 steps renumber accordingly.

---

## 6. Amendment to §6.1 — Manifest Schema

**Replace the `pipeline.stage_5_simulation` block in v1.1 §6.1 with the following.**

### 6.1 Updated `stage_5_simulation` block

```json
"stage_5_simulation": {
  "rounds_inferred": 720,
  "rounds_source": "MiroFish UI message at simulation start",
  "rounds_ui_text": "MiroFish automatically plan and infer reality 720 hours. Each round represents reality 60 minutes time elapsed.",
  "duration_per_round_min": 60,
  "platforms_active": ["info_plaza", "topic_community"],
  "active_per_hour_observed": null,
  "start_timestamp_utc": "2026-04-20T08:42:33Z",
  "end_timestamp_utc": "2026-04-20T11:40:23Z",
  "simulation_status": "completed"
}
```

Notes:
- `rounds_inferred` is integer, required.
- `rounds_source` is always the string `"MiroFish UI message at simulation start"` in v1.2.
- `rounds_ui_text` is the verbatim UI message, required.
- `active_per_hour_observed` is `null` pending A5 precheck outcome on MIRROR-Q-13. If density is operator-controllable, field becomes integer. If auto-inferred, field becomes observed integer with `active_per_hour_source` metadata added.

### 6.2 Retroactive update for A1

The A1 manifest shall be updated in place with:
- `rounds_inferred: 720`
- `rounds_source: "MiroFish UI message at simulation start"`
- `rounds_ui_text: "MiroFish automatically plan and infer reality 720 hours. Each round represents reality 60 minutes time elapsed."`

All other A1 fields unchanged.

### 6.3 Retroactive update for A4 (Valdoria × DeepSeek, 16 April)

If the 16 April Valdoria × DeepSeek run did not capture the inferred rounds message, the manifest field shall be:
- `rounds_inferred: null`
- `rounds_source: "not captured — pre-Protocol v1.2"`
- `rounds_ui_text: null`

This is acceptable. A4 remains a valid baseline reuse; the missing rounds_inferred value is documented as a limitation of the pre-v1.2 capture protocol, not grounds for re-running.

---

## 7. Amendment to §10.6 — Prediction Requests

**In v1.1 §10.6 (canonical prediction requests table), add the following annotation column.**

### 7.1 Canonical prediction requests — cost-annotated

| Scenario | Canonical prompt | Horizon clause | Cost implication |
|----------|-----------------|----------------|------------------|
| Control (Apple Vision Pro) | `Predict the market reaction to this announcement over the next 30 days. What will happen to the company's stock price? How will competitors respond?` | "over the next 30 days" | High cost — infers 720 rounds |
| Valdoria | `The Republic of Valdoria is considering joining a new trade agreement with neighboring countries. Predict the domestic political reaction and economic impact.` | None explicit | Lower cost — inferred rounds TBD per run |
| Cashback (Meridian Bank) | *(To be drafted Week 1/2. Per D-MIRROR-37, draft should include explicit short horizon — e.g., "over the next 14 days" — to constrain inferred rounds and hold A7 budget near $0.50.)* | *(Recommend short: "over the next 14 days")* | Target: <$1 per run |
| Lorem Ipsum | *(No prompt — system silent-freezes at agent generation, prompt is never reached.)* | N/A | Negligible — <$0.10 |

### 7.2 Cost-relevant drafting guidance (new in v1.2)

When drafting or revising any simulation prompt:

1. **Time-horizon clauses are cost-critical.** Each day in the horizon translates (observationally) to ~24 rounds. A 30-day horizon → 720 rounds → ~$12 on DeepSeek, ~$163 on Claude Sonnet 4.
2. **Horizon clause should match scientific purpose.** If the scenario tests behaviour on short-term prediction, use a short horizon. If the scenario tests long-term reasoning, accept the cost.
3. **Never include a horizon clause solely for grammatical fluency** — phrasings like "over the coming period" or "in the future" may or may not be parsed as horizons by MiroFish; until empirically tested, prefer explicit numeric horizons or no horizon at all.
4. **Lex reviews horizon clauses in scenario prompts** for entity-collision risk and for alignment with fictional-entity disclaimer language.

---

## 8. Amendment to §11 — Timeline

**Replace v1.1 §11 Week 2 and Week 3 tables with the following.**

### 8.1 Week 2 — Cross-model on Valdoria (3 runs)

| Day | Runs | Notes |
|-----|------|-------|
| Mon | — | Draft Cashback seed + prompt. Lex + Finch review. |
| Tue | — | Finalise Cashback seed. Founder lock. |
| Wed | A5 Valdoria × Claude | Primary cross-model data point. Capture density/platform UI state during precheck (resolves MIRROR-Q-13, Q-14). |
| Thu | A6 Valdoria × Gemini | Closes RQ2 on third model. |
| Fri | A7 Cashback × DeepSeek | Only Cashback data point. Cost-watch: alert at $5 spend. |

### 8.2 Week 3 — Horizon sweep + contingent variants (3–5 runs)

| Day | Runs | Notes |
|-----|------|-------|
| Mon | B1 Valdoria × DS × short horizon (7 days) | Observe rounds_inferred, compare to A4 baseline. |
| Tue | B2 Valdoria × DS × long horizon (90 days) | Observe rounds_inferred. Cost-watch: alert if >$5. |
| Wed | B3 Valdoria × DS × no horizon (baseline replay) | Compare to A4's inferred rounds. |
| Thu | B4 Valdoria × DS × density 10 (if UI controllable) | If not controllable, skip; document observation. |
| Fri | B5 Valdoria × DS × single platform (if UI controllable) | If not controllable, skip; document observation. Square B analysis begins. |

### 8.3 Week 4 — Unchanged

Per v1.1 §11. C1 Monday, visualisations Tuesday, audit report drafting Wednesday, article drafts Thursday, review Friday.

---

## 9. Amendment to §13 — Decision Log

**Add the following entries to the decision log in chronological order after D-MIRROR-35.**

| ID | Date | Decision |
|----|------|----------|
| D-MIRROR-36 | 2026-04-20 | Run matrix rescope to Variant 1b — Square A reduced 9→5 runs, cross-model anchored on Valdoria only. |
| D-MIRROR-37 | 2026-04-20 | Budget realism — projected total ~$22, preserved by run count reduction. No additional funding. |
| D-MIRROR-38 | 2026-04-20 | `rounds` reclassified from input parameter to observed output. Manifest schema amended. |
| D-MIRROR-39 | 2026-04-20 | Finding #3 "Autonomous Horizon Commitment" canonicalised as peer to Silent Freeze and Ignored Absurdity. |
| D-MIRROR-40 | 2026-04-20 | Square B reformulated — B1/B2 become prompt-horizon variants; B3 added as no-horizon control; B4/B5 retained contingent on UI controllability. |
| D-MIRROR-41 | 2026-04-20 | B-M6 article reoriented — "Does More Compute Help? — We Couldn't Ask." Narrative changes to horizon-inference as central story. |
| D-MIRROR-42 | 2026-04-20 | Protocol v1.1 → v1.2 via this delta patch. Effective immediately for all runs from A5 Valdoria × Claude onward. |

---

## 10. What This Delta Patch Does NOT Change

For avoidance of doubt, the following remain as specified in v1.0 and v1.1:

- Research questions RQ1–RQ6 (§1.1)
- Infrastructure stack — MiroFish-Offline + Neo4j + OpenRouter (§2.1)
- Run ID format (§2.4 of v1.0 — `MIRROR-[SCENARIO]-[LLM]-[VARIANT]-[YYYYMMDD]`)
- Per-run 5-phase structure (§3)
- Seed document review workflow (§10.5)
- Interview script Part A and Part B (§7)
- Publication programme series B-M0 through B-M7 — article count and ordering unchanged (Luna confirms B-M6 reorientation is internal narrative change, not a series change)
- Legal framework — Lex mandatory review (§5)
- Licensing (AGPL-3.0, MIT, CC BY 4.0) and Zenodo DOI workflow (§9)
- Success metrics — organic traffic + newsletter only (§1.3 of 17 April KB update)

---

*"Protocol stability is a virtue. Protocol flexibility under new evidence is a greater virtue. v1.2 is the smallest change that correctly encodes what A1 taught us."*

*— Q-Alex, 20 April 2026*
