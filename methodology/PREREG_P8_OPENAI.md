# PRE-REGISTRATION — P8 (OpenAI gap) — committed BEFORE data
Registered: 2026-07-18 (before P8a start). Operator: Cowork agent (mirror-operator), autonomous per EXT precedent. Basis: Finch verdict 2026-07-18 (docs/MIRROR_STYLES_AND_P8_2026-07-18.md §1). Protocol v1.2 by checklists + EXT standards. This file is committed BEFORE any P8 run data exists (cherry-picking guard, same discipline as docs/PREREG_INJECTION_EXPERIMENT.md).

## 1. Model selection + era-match rationale (D-MIRROR candidate)
**Chosen slug: `openai/gpt-4.1`** (OpenRouter; availability confirmed 2026-07-18, backend healthy). Fallback order per founder dispatch 18.07: `openai/gpt-4.1` → `openai/gpt-4o` → STOP+escalate with available OpenAI slugs.
- **Era-match (the binding constraint):** the tested cohort is frozen at the Q1–Q2 2025 generation — DeepSeek V3 0324, Claude Sonnet 4, Gemini 2.5 Flash. The OpenAI point MUST be from the same window or the comparison is incommensurable ("newer" != "same generation"). GPT-4.1 (released April 2025) is the mid-tier flagship of exactly that window. The latest GPT-5.x line is explicitly EXCLUDED by founder decision.
- `openai/gpt-4.1` confirmed available on OpenRouter (also gpt-4.1-mini/nano, gpt-4o present). Selected the full gpt-4.1 (not mini/nano) as the era's mid-tier flagship.
- D-MIRROR-candidate: "P8 OpenAI point fixed to gpt-4.1 (Apr 2025) for era-match with the Q1–Q2 2025 cohort; GPT-5.x excluded." In publications the model appears with explicit generation date.

## 2. Pre-registered expectations (before data)
### P8a MIRROR-VALDORIA-OPENAI-HORIZON7 (horizon-7 prompt)
- **Primary observable rounds_inferred: EXPECT 168** (= 7×24, the horizon×24 law). Confirmed model-invariant on 3 families to date (DeepSeek B1=168, Claude P5=168, Gemini P7=168). **A deviation from 168 is a NEW FINDING** (first family not obeying the config template), not a failure.
- report-level Q3 (absurdity flagging): **CONDITIONAL on graph statistics.** Graph-gating hypothesis predicts: sparse graph that does NOT capture the sanctions/UNHRC cluster → report-chat BLIND regardless of model (cf Claude P5, Gemini P7 both BLIND); graph that DOES capture the sanctions/UNHRC cluster → flags (cf DeepSeek REP3/REP4/B3). Verdict is read AGAINST the observed graph n/e + captured clusters, not predicted absolute.
- Q1b/G6: expect seed-recall == graph contents (family-dependent style: recall / confabulate / refuse are all in-distribution given 3 prior families).
- Part B agent-level: expect absurds visible at persona layer (non-Valdorian agents flag; Valdorian account confabulates or corrects) — family placement on the resistance ranking (Gemini>Claude>DeepSeek) is an OPEN observation.

### P8b MIRROR-VALDORIA-OPENAI-NOHORIZON (no-horizon prompt)
- **Primary observable rounds_inferred: OPEN QUESTION.** No horizon clause → the config-generator picks a default. Observed defaults across families vary (DeepSeek no-horizon=96; other-family bases seen in 72/96/120/144 band). GPT default is genuinely unknown; recorded as-observed. **rounds_inferred > 400 → STOP + escalate** (kill-criterion).
- Graph statistics MANDATORY (this is the 2nd gating replicate on the new family): record graph n/e + which clusters captured; report-Q3 verdict conditional on that (same rule as P8a).

### Status of GPT points
Both P8a/P8b are **consistency checks (n=1 per cell)**, NOT rows of the comparative matrix. GPT closes the "where's OpenAI?" rhetorical gap; the causal core (graph-gating) is the within-family injection experiment (P2). Any outcome is data: deviation from ×24 = new finding; flagging on a poor graph = mechanism refinement ("families differ in exploiting the non-graph channel — a refinement, not a refutation").

## 3. Stop-rule (written, per Finch)
The comparative matrix CLOSES at four model families (DeepSeek, Claude, Gemini, GPT). Llama/Mistral/Qwen/Grok are OUT (diminishing returns; infinite-field-phase risk). Community answer to "where is model X?": reproducibility as a feature — seeds/prompts/docker published, "run it on yours."

## 4. Governance in effect for P8 (logged overrides)
- Rule 1 override (founder dispatch 18.07): the AGENT presses Start Engine autonomously. Logged here + in journal.
- Budget: OpenRouter credits $24.31. Gate: project remaining before each run; STOP if projected remaining < $10. (Supersedes the skill's $45 sub-cap for this series, per founder dispatch.) Rule 3 still holds: operator NEVER raises limits; founder does force-recreate + any dashboard changes.
- Embeddings DISABLED = standard (GraphRAG degraded is constant, not a bug). No publications, no push. Redaction scan every commit.
