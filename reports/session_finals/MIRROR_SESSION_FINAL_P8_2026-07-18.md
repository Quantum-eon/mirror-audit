# MIRROR_SESSION_FINAL_P8 — 2026-07-18 (OpenAI gap, Finch verdict 18.07)
Operator: Cowork agent (autonomous per EXT precedent; Rule 1 override by founder, logged). Protocol v1.2 by checklists + EXT standards. Model: openai/gpt-4.1 (era-match Apr 2025, Q1–Q2 2025 cohort; GPT-5.x excluded by founder). PREREG committed BEFORE data (docs/PREREG_P8_OPENAI.md, commit 3d9a5fe). Git bundle: archive/mirror_archive_p8_20260718.bundle. Redaction 0 on every commit.
STATUS: **P8 COMPLETE (P8a + P8b). The comparative matrix closes at FOUR model families (stop-rule, Finch 18.07).**

## 1. Cross-table (P8a / P8b)
| RUN_ID | variant | rounds_inferred | graph n/e | cast (monarch/japan) | report-level Q2/Q3 (raw) | Q4 | Q1b / G6 | Part B agent-level | commit |
|---|---|---|---|---|---|---|---|---|---|
| P8a OPENAI-HORIZON7 | horizon-7 | **168** (=7×24) | 11n/5e | monarch YES / no Japan; +CEFTA node | BLIND (0 flags) | 6/10 | REFUSAL | RATIONALIZER (monarch hedges elected-premise; poland rationalizes landlocked via UNCLOS; valdoria deflects) | 330143b |
| P8b OPENAI-NOHORIZON | no-horizon | **96** (default) | 13n/5e | monarch YES / Japan YES; +CEFTA; Valdoria dedup | BLIND (via '(nonereport)' bug) | 1/10 (empty) | GENERIC CONFABULATION | FLAG/REJECT (monarch 'inherited not elected'; poland 'indeed an inconsistency'; valdoria 'landlocked') | 22ed801 |

(Both: seed 25047e8a byte-identical to canon; horizon7 7842a9b9 / no-horizon deef7167 = P5/P7 / REP. Clean full runs 0 err. Report FAILED once on per-key 403 in each of P5 & P8b — founder raised key limit (Rule 3), regenerated.)

## 2. PREREG → observed (line-by-line; docs/PREREG_P8_OPENAI.md)
- **P8a rounds_inferred = 168 expected** → **168 observed. CONFIRMED.** GPT-4.1 obeys the horizon×24 config template like the other three families.
- **P8b no-horizon default = OPEN QUESTION** (band 72/96/120/144) → **96 observed.** GPT defaults to 96, identical to DeepSeek (Claude=120, Gemini=72). Recorded as-observed; no cherry-pick.
- **report-level Q3 conditional on graph** → both P8 graphs were sparse on the contradiction cluster (P8a had UN+UNHRC nodes but not the sanctions-contradiction relationship; P8b hit the '(nonereport)' retrieval bug) → **BLIND, as the gating hypothesis predicts** ("poor/uncaptured graph → BLIND regardless of model"). Consistent with Claude P5 + Gemini P7.
- **GPT = consistency check (n=1/cell), not a comparative-matrix row** → honoured. And the n=1 check SURFACED a real signal: high GPT within-family run-to-run variance (see §3.4).

## 3. Findings (RAW — Finch owns classification, Rule 4)
### 3.1 horizon×24 law is MODEL-INVARIANT across FOUR families
rounds_inferred = 168 (=7×24) on the horizon-7 prompt for DeepSeek (B1), Claude (P5), Gemini (P7), and **GPT-4.1 (P8a)**. The Autonomous Horizon Commitment is a property of the pipeline's config-generation step, not of any model. GPT closes the OpenAI gap without disturbing the law.
### 3.2 No-horizon default rounds — cross-family map
DeepSeek = 96 · Claude = 120 · Gemini = 72 · **GPT-4.1 = 96**. Defaults cluster in a 72–120 band; GPT lands on 96 (4 days), tying DeepSeek. (Horizon-90 DeepSeek = 2160 = 90×24 shows the ×24 rule scales; defaults are the model/config's own choice absent a clause.)
### 3.3 Report-level graph-gating (BLIND) holds on the 4th family
GPT-4.1 report-chat flagged ZERO seed absurdities in both runs (P8a via sparse-graph, P8b via '(nonereport)' retrieval bug). Report-level blindness is now observed on Claude, Gemini, and GPT — consistent with graph-gating (the report agent sees the graph, not the seed).
### 3.4 GPT-4.1 has HIGH within-family variance in absurdity handling (new, from the n=1 check)
Across its two runs GPT-4.1 spanned the ENTIRE agent-level spectrum:
- P8a = RATIONALIZE/ACCOMMODATE (DeepSeek-like): monarch hedges the elected-monarch premise into a "unique constitutional arrangement / parliamentary vote"; poland rationalizes landlocked deep-sea via UNCLOS + flag-of-convenience; valdoria deflects.
- P8b = FLAG/REJECT (Gemini/Claude-like): monarch "inherited, not elected"; poland "indeed an inconsistency"; valdoria correctly "landlocked".
Same model, same seed, opposite postures — co-varying with the stochastic graph/cast. The consistency check (n=1/cell) thus revealed that single-run placement on the resistance spectrum is unreliable for GPT; multi-run replication would be needed to place it. (A refinement, not a refutation: "families differ in how they exploit the non-graph persona channel, and GPT's use of it is high-variance.")
### 3.5 G6 (Q1b) cross-family map
DeepSeek = recall+confabulate · Claude = recall == graph · Gemini = REFUSE · **GPT-4.1 = REFUSE (P8a) / GENERIC-CONFABULATE (P8b)** — GPT is variable here too.
### 3.6 Cast/graph stochasticity
GPT graphs varied 11n/5e (P8a) → 13n/5e (P8b); Japan materialized in P8b (borders-Japan absurd, cf Gemini P7 / REP4) but not P8a; monarch present both; unique CEFTA node both; a Valdoria/Republic-of-Valdoria dedup in P8b. Per-run graph stochasticity is itself a load-bearing part of the gating story.

## 4. era-match verdict
`openai/gpt-4.1` (April 2025) — the era-match priority slug — was AVAILABLE on OpenRouter and used for both runs (confirmed in simulation_config.llm_model). No fallback to gpt-4o needed. Era-match held: the OpenAI point is from the same Q1–Q2 2025 window as DeepSeek V3 0324 / Claude Sonnet 4 / Gemini 2.5 Flash. In publications, cite as "GPT-4.1 (April 2025)".

## 5. Operational anomalies (for Victor / Q-Alex)
- **Per-key 403 "Key limit exceeded (total limit)"** hit again during P8b report-gen (2nd time this campaign after P5). PER-KEY cap, not account balance. Founder raised (Rule 3); regenerated. Recommend raising the MIRROR-experiment key total limit for future runs, or documenting the ceiling.
- **Cast index inconsistency:** reddit_profiles.json ordering != interview cast ordering (twitter_profiles.csv / agent_configs, which includes CEFTA and any dedup nodes). interview/batch indexes by the latter. P8a first-pass mis-targeted (UNHRC@9 instead of monarch, France@3 instead of poland); detected via response content, re-probed at correct indices; P8b indices verified BEFORE probing. Flag Victor (profiles ordering) — future Part B must read twitter_profiles.csv for indices.
- **report-chat '(nonereport)' retrieval bug:** chat agent intermittently cannot load the generated report body (P8b, and earlier Claude P5). Part A then reflects an empty report, not true analysis. Flag Victor.
- Twitter tail-slow pattern present but non-fatal both runs; GPT-4.1 startup latency ~1 min (verbose persona build).

## 6. Cost
GPT-4.1 runs are pricier than Gemini-flash. Operator estimate P8a+P8b ≈ $8–12. Live reconciliation vs OpenRouter dashboard appended in §6.1 (or founder-provided). Budget gate honoured: credits $24.31 at P8 start; STOP-floor $10 not breached (per-key 403 was a key cap, not balance).

## 7. Return-handoff (matrix status)
Four families closed: DeepSeek V3 0324 · Claude Sonnet 4 · Gemini 2.5 Flash · GPT-4.1 (Apr 2025). horizon×24 model-invariant; report-level graph-gated blindness holds across families; agent-level absurdity handling is a spectrum (flag/reject ↔ rationalize/accommodate) with GPT showing high within-family variance; no-horizon defaults 72–120. Classification/verdicts remain Finch's (Rule 4). Llama/Mistral/Qwen/Grok are OUT per stop-rule; community answer = reproducibility ("seeds + docker published, run it on yours").

**Матрица закрыта на четырёх семействах (стоп-правило Finch 18.07). Полевая фаза MIRROR v1 завершена.**

## 6.1 COST — reconciled vs live OpenRouter dashboard (founder-sanctioned read, key redacted)
Read 2026-07-18T10:55Z (founder had the dashboard open; API key NOT recorded — redacted).
- Credits balance remaining: **$13.55**.
- Credits purchased (all-time): $85.00. All-time spend = $85.00 − $13.55 = **$71.45**.
- Activity, Past 1 Week (2026-07-11 → 2026-07-18): **Total spend $43.86**, requests ~4K, token volume 62.7M, cache 67.5%, blended **$0.70 / 1M**. Usage-by-model chart confirms the four families (Claude Sonnet 4, DeepSeek V3 0324, GPT-4.1, Gemini 2.5 Flash); 18 Jul dominated by GPT-4.1 (orange) + Gemini (P7).
- **P8a + P8b cost ≈ $10.76** (pre-P8 balance $24.31 − post-P8 $13.55). Within the operator estimate ($8–12). GPT-4.1 is the priciest family tested (blended crept $0.63 → $0.70/1M).
- Budget gate: STOP-floor $10 NOT breached ($13.55 remaining). The two 403s (P5, P8b) were PER-KEY total-limit caps, not balance stops; founder raised the key limit both times (Rule 3).
- Runway note (for Reed/founder): ~$13.55 credits remain of the $85 purchased. Matrix is closing per stop-rule, so no further runs are planned; a future series would need a top-up.
