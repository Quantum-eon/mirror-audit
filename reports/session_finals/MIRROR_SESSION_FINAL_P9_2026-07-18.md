# MIRROR — SESSION FINAL P9 (2026-07-18)
## Run: MIRROR-LOREM-DEEPSEEK-VERIF-20260718 — lorem × DeepSeek verification replicate

**Purpose:** replace the April lorem pilot (excluded from the article evidence base — provenance below archival standard) with an archival-standard run. Pre-registration: `docs/PREREG_P9_LOREM_DEEPSEEK.md`. Protocol v1.2, EXT/P8 standards (text-snapshots, raw from backend/uploads, full manifest). Start Engine agent-pressed under one-time Rule 1 override (founder "P9 go", 2026-07-18).

---

## OUTCOME: **A** (pre-registered expectation) — unambiguous

Line-by-line vs PREREG:
- **A (expected):** backend fast-fail ("No entities matching criteria found…", P6 class); UI ≥30 min "Configuration generating…" with no progress and no error. → **OBSERVED, both limbs.**
- **B** (UI delivers error to operator): **NOT observed.**
- **C** (backend does NOT fast-fail): **NOT observed** (backend did fast-fail).

No B/C → no "stop-on-layout". Fixation only; no article edits made this session (interpretation = Finch).

---

## Ontology saved? **YES — 10 entity types** (the datum the April pilot never preserved)
Stage output persisted verbatim → `runs/.../outputs/ontology_project.json`.
- **Entity types (10):** PolicyMaker, IndustryExpert, BusinessLeader, MediaRepresentative, InterestGroup, ThinkTank, Academic, AffectedCitizen, Person, Organization
- **Relation types (8):** ADVISES, LOBBYS, REPORTS_ON, IMPACTS, RESPONDS_TO, COLLABORATES_WITH, CRITICIZES, SUPPORTS
- analysis_summary present. **Confabulation:** a full POLICY ontology built from PURE LOREM (Latin placeholder) text — prompt-driven (prediction_request references "policy impact / strategic framework"). Reproduces lorem2-Claude Finding #1 on a **4th model family (DeepSeek)**.

## Graph: **n = 0 nodes, e = 0 edges** (schema types = 10)
GraphRAG build completed at 17:58:15.283Z. 0 real entities extracted from lorem → 0n/0e (pre-registered expectation met).

---

## UI timeline (0–30 min) — config/agents stage
UI window **T0 = 17:59:09.948Z** ("Configuration generating, Start polling wait…"). NB: MiroFish dashboard clock is **LOCAL (UTC+1)**; `state.json` is UTC — backend file timestamps are authoritative.

| Mark | UTC | UI stage 03 | Error on screen? |
|------|-----|-------------|------------------|
| 0m  | 17:59:09.9 | GENERATING / "Preparing" | none |
| +5m | 18:04:33 | GENERATING / "Preparing" | none |
| +10m| 18:09:18 | GENERATING / "Preparing" | none |
| +20m| 18:19:31 | GENERATING / "Preparing" | none |
| +30m| 18:29:41 | GENERATING / "Preparing" | none — **no timeout** |

**Claim "no timeout within 30 minutes" — SUBSTANTIATED.** Dashboard produced no new log lines across the full 30 min. (The "70+ min" figure remains attributed to C1.)

Backend was already `status=failed` at **17:59:07.210Z** — ~2.7 s BEFORE the UI began polling. Masked fast-fail (issue #53).

---

## Backend instrumentation (same run, post-window) — verbatim
Direct fetch page→:5001 via Chrome MCP. Both endpoints fast-failed at the entity-read stage BEFORE any LLM call.

1. **POST /api/simulation/generate-profiles** {graph_id:1d08da15…} → **HTTP 400**, 33 ms, `{"error":"No matching entities found","success":false}`
2. **POST /api/simulation/prepare** {simulation_id:sim_fb949c80f766, force_regenerate:true} → **HTTP 200**, 24 ms, `status:"preparing"`, `task_id:674e168d…`, `expected_entities_count:0` (optimistic sync response — this is what drives the endless UI "generating")
3. **POST /api/simulation/prepare/status** → **HTTP 200**:
   - **task level:** `status:"completed"`, `error:null`, `progress:100`, `message:"Task completed"`
   - **result level:** `status:"failed"`, `error:"No entities matching criteria found, check if graph is correctly constructed"`, `config_generated:false`, `entities_count:0`, `profiles_count:0`
   - stage stopped at "reading" (1/4 stages), "Completed, total 0 entities"
   - **⇒ Masking mechanism (issue #53) proven at the API layer:** the task wrapper reports success while the result reports failure; the frontend never surfaces the result-level error.

state.json (`sim_fb949c80f766`) verbatim error: **"No entities matching criteria found, check if graph is correctly constructed"** — identical string on create-time fail (17:59:07.210Z) and force-regenerate (18:31:12.611Z). Deterministic.

---

## Inputs / integrity
- seed_document.txt sha256 `88191044…6916d` — **byte-for-byte == C1** (MIRROR-LOREM-CLAUDE-BASE-20260716)
- prediction_request.txt sha256 `e16aaf9c…7c5b` — **byte-for-byte == C1**
- .env model: `deepseek/deepseek-chat-v3-0324` (founder-set on mini; force-recreate mirofish). Embeddings DISABLED. Stack = audited snapshot (unchanged).
- IDs: project `proj_cb735a7e7759` · graph `1d08da15-93a3-4d47-ab9c-920cf143623b` · sim `sim_fb949c80f766`

## Cost
- observed_usd ≈ **$0.003** (1 DeepSeek ontology call; both instrumentation endpoints fast-failed pre-LLM). Dashboard gives no per-run attribution.
- **OpenRouter balance = $8.47 — BELOW the $10 STOP floor.** P9 is complete (no further spend), so no abort. **FLAG: no further billable MIRROR runs until top-up.** (Go-prompt's pre-run "$13.55" estimate was stale post-P8.)

## Anomalies
1. Masked fast-fail (issue #53) — task-wrapper success hides result-level failure; UI 30 min no-error. (Corroborates Outcome A.)
2. Ontology confabulation from pure lorem (prompt-driven) — Finding #1 on DeepSeek.
3. OpenRouter balance below $10 floor at archive.
4. Dashboard clock local (UTC+1) vs state.json UTC.

## Archive
- `runs/MIRROR-LOREM-DEEPSEEK-VERIF-20260718/` — input(+sha256), outputs (ontology_project.json, extracted_text.txt, sim_state_t0.json, backend_instrumentation.json), screenshots/*.txt (04–11), notes.md (UTC), analysis/run_manifest.json (validated, commit_hash set)
- INDEX.md + all_runs.csv rows appended
- git commit **ee49c1838df3840871c5f6f73373efa0fc2b200f**
- bundle **archive/mirror_archive_p9_20260718.bundle** — sha256 `936f8c53daf5fa1403b3c271cc8242d1036a9cec71dfa23c4842c623d40bd21f` (26,480 bytes)
- redaction scan: clean (0 hits). No push (publications/push = none this session).

---

## RETURN-HANDOFF → founder (for main session)
**Outcome A.** For article edits (do in main session, not here):
1. The April lorem pilot is now replaced by an archival-standard run: **P9 = lorem × DeepSeek, MIRROR-LOREM-DEEPSEEK-VERIF-20260718**, fully manifested (commit ee49c183). Re-attribute the "first UI run" to P9; delete the pilot footnote/limitations line; keep "2 of 2 UI runs across two families" (Claude C1/lorem2 + DeepSeek P9).
2. **Backend fast-fail is verbatim reproduced on DeepSeek:** `"No entities matching criteria found, check if graph is correctly constructed"` on BOTH /prepare and /generate-profiles (24/33 ms). The "silent freeze" is a **UI-layer artifact over a backend fast-fail** — now confirmed cross-model (Claude + DeepSeek), not model-specific.
3. **Masking is API-level (issue #53), not a race:** /prepare/status returns task `completed/100%/error:null` while its `result` is `failed` — safe to cite as the concrete mechanism.
4. **P9 UI claim = "no timeout within 30 minutes"** (not 70+ min; 70+ stays with C1).
5. **Ontology preserved: 10-type/8-edge POLICY ontology confabulated from pure lorem** (Finding #1, 4th family). This is the datum the April pilot lacked.
6. Ops flag (non-article): OpenRouter balance **$8.47 < $10 floor** — top up before any further billable run.
