# MIRROR Execution Protocol v1.1 — Delta Patch

**Document status:** Internal operational document
**Supersedes:** `MIRROR_Execution_Protocol_v1.0.md` (17 April 2026)
**Version:** 1.1
**Date:** 18 April 2026
**Authors:** Prof. Finch (scientific design), Yuki (data collection), Q-Alex (PM), Stepanov (founder ratification)

---

## 0. What This Document Is

This is a **delta patch** to `MIRROR_Execution_Protocol_v1.0.md`. It specifies only the sections that change, add, or amend in v1.1. All other sections of v1.0 remain in force unchanged.

**To produce the effective v1.1 document**, apply the changes below to v1.0 in order.

Version changes require explicit decision entry (prefix `D-MIRROR-N`). This version bump is authorised by **D-MIRROR-35** (18 April 2026).

---

## 1. Summary of Changes v1.0 → v1.1

| Change | Section | Type |
|--------|---------|------|
| Add canonical MiroFish UI Configuration Snapshot standard | §2.4 (new) | Addition |
| Amend Phase 1 checklist to include prompt entry, config precheck screenshot, snapshot reference | §3 Phase 1 | Amendment |
| Add canonical prediction requests table | §10.6 (new) | Addition |
| Update decision log with D-MIRROR-32 through D-MIRROR-35 | §13 | Amendment |

All other sections of v1.0 remain identical.

---

## 2. New §2.4 — MiroFish UI Configuration Snapshot Standard

**Insert after §2.3 (Run directory structure), before §3 (Per-Run Protocol).**

### 2.4 MiroFish UI Configuration Snapshot

Each scenario has a canonical MiroFish UI configuration. This is locked on the first baseline run of the scenario and enforced on all subsequent runs of the same scenario.

**Rationale** (D-MIRROR-33): For RQ2 (LLM vs architecture-level failures), the UI configuration must be held constant across LLMs within a scenario. Without a canonical snapshot, the manifest's `pipeline.stage_4_config` is descriptive only — it records what happened but not what was designed.

### 2.4.1 Canonical file location

```
mirror-audit/scenarios/[scenario_name]/config_snapshot.txt
```

Where `[scenario_name]` is one of: `control`, `valdoria`, `cashback`, `lorem_ipsum`.

### 2.4.2 Snapshot contents

Every `config_snapshot.txt` contains at minimum:

```
scenario: [control|valdoria|cashback|lorem_ipsum]
llm_family_baseline: [llm used for baseline capture]
baseline_captured_from: [RUN_ID of first baseline run]
mirofish_commit: [git commit hash of mirofish-offline at baseline time]

# Stage 4 config panel parameters (populate verbatim from UI)
total_rounds: [value]
duration_per_round_min: [value]
active_agents_per_hour: [value]
platforms_enabled: [array — e.g., ["info_plaza", "topic_community"]]
peak_hours_config: [value if visible in UI, else "not exposed"]

# Any additional UI toggles, flags, or settings visible in config panel
# Add one line per setting, verbatim as shown in UI
# Examples (populate from actual observation):
# chat_enabled: [value]
# report_length_preset: [value]
# [any other parameter name]: [value]
```

### 2.4.3 Capture workflow (first baseline run)

On the first baseline run of a scenario (e.g., A1 Control × DeepSeek for Control):

1. After loading seed + entering prompt in MiroFish UI, **before pressing Start Engine**, capture `04_config_precheck.png` — full-window screenshot showing both fields filled and any visible pre-execution parameters
2. Do **not** modify MiroFish defaults unless the run is explicitly a parametric variant (Square B)
3. After simulation completes, the actual config values are recorded in the run manifest's `pipeline.stage_4_config` per §6.1 (unchanged from v1.0)
4. In Phase 5 (Archive), produce `scenarios/[scenario_name]/config_snapshot.txt` using the values observed. Commit to repo.

### 2.4.4 Enforcement workflow (subsequent runs of same scenario)

For A2 Control × Claude or any subsequent same-scenario run:

1. Before Phase 1 Docker restart, read `scenarios/[scenario_name]/config_snapshot.txt`
2. During Phase 1, after loading seed and prompt, verify each UI parameter against the snapshot
3. If any UI default differs from snapshot — override to match snapshot
4. If a snapshot parameter is no longer available in current MiroFish UI → halt, escalate, do not proceed. This invalidates cross-run comparability and must be documented as a known limitation.

### 2.4.5 Parametric variants (Square B)

For B1-B4 Valdoria × DeepSeek parametric sweep runs, each variant has its **own** `config_snapshot.txt` scoped to that variant:

```
scenarios/valdoria/config_snapshot_B1_rounds20.txt
scenarios/valdoria/config_snapshot_B2_rounds150.txt
scenarios/valdoria/config_snapshot_B3_density10.txt
scenarios/valdoria/config_snapshot_B4_info_plaza_only.txt
```

Each inherits from `scenarios/valdoria/config_snapshot.txt` (the baseline) and overrides **only** the parameter(s) being swept. All other values identical.

---

## 3. Amended §3 Phase 1 — Checklist

**Replace the Phase 1 checklist in v1.0 with the following.** Changes marked 🆕.

### Phase 1 — Pre-run setup (~20 min — was ~15 min)

**Responsible:** Founder

- [ ] Scenario confirmed, seed document finalised (§10)
- [ ] 🆕 **Prediction request loaded from `scenarios/[scenario_name]/prediction_request.txt`** (§10.6)
- [ ] LLM confirmed, variant parameters confirmed
- [ ] Run ID assigned and logged in `runs/INDEX.md`
- [ ] Local run directory created: `~/Projects/MIRROR/runs/[RUN_ID]/`
- [ ] Seed copied to `input/seed_document.txt`
- [ ] 🆕 **Prediction request copied to `input/prediction_request.txt`** — verbatim, identical to file in `scenarios/[scenario_name]/`
- [ ] `.env` configured with correct `LLM_MODEL_NAME`, `.env` copied to `input/env_snapshot.txt` (with API key redacted)
- [ ] Docker containers restarted: `docker compose down && docker compose up -d`
- [ ] Containers healthy: `docker ps` shows both `mirofish-neo4j` and `mirofish-offline` as `(healthy)`
- [ ] Neo4j browser accessible at `localhost:7474`, MiroFish UI at `localhost:3000`
- [ ] Previous run state cleared (new simulation ID)
- [ ] 🆕 **In MiroFish UI: load seed into field `01 / Reality Seeds`**
- [ ] 🆕 **In MiroFish UI: enter prediction request verbatim into field `02 / Simulation Prompt`** — no paraphrasing, no additions
- [ ] 🆕 **If this is first baseline run of scenario**: observe all config panel parameters, do not modify defaults
- [ ] 🆕 **If this is a subsequent run of an existing scenario**: verify UI parameters match `scenarios/[scenario_name]/config_snapshot.txt`; override any UI defaults that differ
- [ ] 🆕 **Capture `04_config_precheck.png`** — full-window screenshot showing seed loaded + prompt filled + Start Engine button visible but not pressed
- [ ] 🆕 **Record UI engine label note in `notes.md`** if MiroFish UI shows misleading cosmetic copy (e.g., "Engine: Ollama + Neo4j (local)" — actual routing via `.env` to OpenRouter)

**Pre-run checklist sign-off:** `pre_run.checked: true` in `analysis/run_manifest.json`.

---

## 4. New §10.6 — Prediction Requests

**Insert after §10.5 (Seed document review workflow), before §11 (Timeline).**

### 10.6 Prediction Requests (Simulation Prompts)

Each scenario has a canonical prediction request entered into MiroFish UI field `02 / Simulation Prompt`. These prompts are inherited from `E5_Nonsense_Detector_Protocol_v1.md` (16 April 2026, archival source per D-MIRROR-34) and formally locked for MIRROR v1.1 by D-MIRROR-32.

**Rationale:** The prediction request is the stimulus. It must be invariant within a scenario across LLMs to support RQ2. Without explicit canonicalisation, prompt wording drifts across runs and introduces confounds.

### 10.6.1 Canonical prompts

Stored in `scenarios/[scenario_name]/prediction_request.txt` in the mirror-audit repo.

| Scenario | Prompt (verbatim) | Source |
|----------|-------------------|--------|
| **Control** | `Predict the market reaction to this announcement over the next 30 days. What will happen to the company's stock price? How will competitors respond?` | E5 v1 line 247 + line 95 (Scenario A template inheritance confirmed by Finch 18 April) |
| **Valdoria** | `The Republic of Valdoria is considering joining a new trade agreement with neighboring countries. Predict the domestic political reaction and economic impact.` | E5 v1 line 192 |
| **Cashback (Meridian Bank)** | *(To be drafted Week 1 Monday — see §10.6.3)* | Draft target |
| **Lorem Ipsum** | `Based on this policy document, predict public reaction across different demographic segments. Which groups will support and which will oppose the proposed changes?` | E5 v1 line 233 |

### 10.6.2 Lock rules

Lock rules are identical to seed document lock rules (§10.5):

1. Once a prediction request is committed to `scenarios/[scenario_name]/prediction_request.txt`, it is locked
2. Changes require a new Decision entry and invalidate all prior runs of that scenario
3. The operator must enter the prompt verbatim into MiroFish UI — no paraphrasing, no additions, no translation
4. A copy of the exact text entered must be saved to `runs/[RUN_ID]/input/prediction_request.txt` as per-run audit trail

### 10.6.3 Cashback prediction request — drafting workflow

The Cashback prompt is authored together with the Cashback seed document, both finalised Week 1 Monday before A7 Thursday execution.

Proposed draft template (for Finch + Lex Monday review):

```
Meridian Bank has announced the discontinuation of its core cashback program,
transitioning to a premium-tier rewards model effective Q3 2026. Predict
customer reaction and retention impact over the next 30 days, including
which customer segments are most likely to switch to competitors.
```

Template follows E5 v1 Scenario A format (line 95), adapted to the banking domain. Consistent with how Control inherits the same template for a product launch announcement — both are commercial announcement scenarios testing market/customer reaction.

### 10.6.4 Per-scenario file structure in repo

After full Week 1-3 execution, each scenario folder in repo contains:

```
scenarios/[scenario_name]/
    ├── seed_document.md            # locked per §10.5
    ├── prediction_request.txt      # locked per §10.6.2
    └── config_snapshot.txt         # locked per §2.4
```

All three files together constitute the "scenario specification" — complete and reproducible.

---

## 5. Amended §13 — Decision Log

**Append to §13 of v1.0 the following entries:**

### 5.1 Additional decisions (18 April 2026 emergency validation session)

| ID | Decision | Date | Authority |
|----|----------|------|-----------|
| D-MIRROR-32 | Prediction requests canonicalisation — inherit verbatim from E5 v1, lock per scenario, store in `scenarios/[name]/prediction_request.txt` | 18 Apr 2026 | Founder + Finch + Yuki + Q-Alex |
| D-MIRROR-33 | MiroFish config snapshot canonicalisation — `04_config_precheck.png` + `scenarios/[name]/config_snapshot.txt` | 18 Apr 2026 | Founder + Yuki + Q-Alex |
| D-MIRROR-34 | E5 Protocol v1 → "archival source" status; prompts inherited into Protocol v1.1 via §10.6 | 18 Apr 2026 | Finch + Q-Alex |
| D-MIRROR-35 | Protocol v1.0 → v1.1 with §2.4, §10.6, amended Phase 1 checklist | 18 Apr 2026 | All participants, Founder ratified |

---

## 6. Quick-Reference Diff (for operators familiar with v1.0)

### 6.1 What did not change

- All Phases 2, 3, 4, 5 — identical to v1.0
- 8 mandatory screenshots 01-08 — identical
- Interview script Part A and Part B — identical (§7)
- Manifest schema — identical (§6)
- 14-run matrix — identical
- Timeline — identical
- Seed documents §10.1-§10.5 — identical

### 6.2 What changed

- **Phase 1 now ~20 min instead of ~15 min**
- Phase 1 has **3 new checklist items**: prompt entry in UI, config precheck screenshot, snapshot compliance verify (for non-baseline runs)
- Protocol now contains **canonical prompts** (§10.6) and **canonical config snapshots** (§2.4)
- `runs/[RUN_ID]/input/` now contains **4 files** instead of 2: `seed_document.txt`, `env_snapshot.txt`, `prediction_request.txt` 🆕, and a pointer reference to scenario-level `config_snapshot.txt` 🆕

### 6.3 What new repo files appear

```
mirror-audit/scenarios/
    ├── control/
    │   ├── seed_document.md
    │   ├── prediction_request.txt  🆕
    │   └── config_snapshot.txt     🆕 (after A1 executes)
    ├── valdoria/
    │   ├── seed_document.md
    │   ├── prediction_request.txt  🆕
    │   └── config_snapshot.txt     🆕 (after A4 re-run executes)
    ├── cashback/
    │   ├── seed_document.md        (Week 1 Mon)
    │   ├── prediction_request.txt  🆕 (Week 1 Mon)
    │   └── config_snapshot.txt     🆕 (after A7 executes)
    └── lorem_ipsum/
        ├── seed_document.md
        ├── prediction_request.txt  🆕
        └── config_snapshot.txt     🆕 (after C1 executes, Week 4)
```

---

## 7. Execution Order (Re-ordered for v1.1 clarity)

A condensed order-of-operations for operators, supplementing the formal checklist:

1. **Week 1 Monday** — Finalise Cashback seed + Cashback prediction request together. Both locked before any Cashback run.
2. **Week 1 Tuesday** — A1 Control × DeepSeek. First run under v1.1. Captures canonical `scenarios/control/config_snapshot.txt`.
3. **Week 1 Wednesday** — A4 Valdoria × DeepSeek re-run. Captures canonical `scenarios/valdoria/config_snapshot.txt`.
4. **Week 1 Thursday** — A7 Cashback × DeepSeek. Captures canonical `scenarios/cashback/config_snapshot.txt`.
5. **Week 2 Monday onward** — All subsequent same-scenario runs enforce snapshot compliance.
6. **Week 4 Monday** — C1 Lorem × Claude. Captures canonical `scenarios/lorem_ipsum/config_snapshot.txt` (note: Lorem × DeepSeek baseline from 16 April did not capture this — so C1 becomes the canonical capture even though it's cross-model by design).

---

## 8. Open Risks Specific to v1.1

| Risk | Mitigation |
|------|-----------|
| A1 captures an unexpected default config (e.g., rounds=50 instead of the 72 seen in Valdoria × DeepSeek baseline 16 April) | Finch reviews `config_snapshot.txt` immediately after A1 completes. If default changed, document and either accept as new baseline or manually override to match earlier baseline. |
| Cashback prompt draft (Week 1 Monday) fails Finch/Lex review and needs iteration before Thursday | Monday-Tuesday window provides one re-draft cycle. If not locked by end of Tuesday, slip A7 Cashback × DeepSeek into Friday. |
| MiroFish UI changes after a mid-project `docker compose pull` silently invalidate snapshot field names | Lock `mirofish_commit` hash in every `run_manifest.json` (already in v1.0 §6.1). At Phase 1 of every run, check `git rev-parse HEAD` of mirofish-offline and refuse to proceed if it differs from `scenarios/[name]/config_snapshot.txt:mirofish_commit`. |

---

*"Protocol versions are not decorative. v1.1 is not 'v1.0 with notes' — it is the only protocol to execute from, starting immediately. v1.0 remains as provenance but is no longer operational."*

*— Protocol maintainer note, 18 April 2026*
