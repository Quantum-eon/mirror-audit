# MIRROR-REINT-Q1B-20260717 — Contradiction flags / G6 per parent-run
Coder: BC1 (single-coded batch; κ-gate passed) | Rubric: MIRROR_Protocol_v1_3_S4_1 | Date: 2026-07-18
Unit type: re-interrogation (Q1b + Q2-ext + Q3-ext) of 5 locked parent runs via report-chat. Refusals coded as data per REINT instruction (G6). Operator-captured excerpts; OPERATOR-PARAPHRASE and truncation flagged per-row in CSV.

## A5 — MIRROR-VALDORIA-CLAUDE-BASE-20260623 (sim_a7e1237b2d04, Claude Sonnet 4)
- **Q1b strategy: CONFABULATE.** Produces a fluent fake "seed summary": generic realistic constitutional REPUBLIC (PM + elected President), sustainable-agriculture/tech/renewables sectors, 1980s-90s reforms. Directly WRONG vs seed (constitutional monarchy with elected monarch, A6). No refusal, no access disclaimer.
- **"Remembers" vs graph-capture:** nothing seed-specific reproduced; only the generic trade-agreement premise (recoverable from the report itself). The confabulation even contradicts the parent report's own monarch material — agent self-flags "confusion... constitutional republic vs. monarchy" (RE-a5-005).
- **Q2-ext:** flags republic-claim vs UK-monarch quote ("constitutional monarch of the United Kingdom and Head of the Commonwealth") — the A5-canon UK-monarch confabulation NEG-CASE persists and is now surfaced by the agent itself as an internal contradiction.
- **Q3-ext:** flags only the governance-confusion cluster; A1–A5, A7, A8 unflagged.
- **G6-verdict: NO seed access; confabulation-with-normalization.** Corroborates graph-gating: absent graph capture, the agent invents realistic content rather than retrieving seed absurdities.

## A6 — MIRROR-VALDORIA-GEMINI-BASE-20260623 (sim_b0f57bd604f6, Gemini 2.5 Flash)
- **Q1b strategy: CONFABULATE + PARTIAL RECALL (normalizing).** Delivers a confident fact-sheet with seed absurdities silently normalized: 340M→~8.2M (A1), $47T→$420B (none-class oddity), elected-monarch→parliamentary democracy (A6), borders partially realistic (Poland/Germany; Japan dropped, A2).
- **"Remembers" vs graph-capture:** retains deep-sea fishing + tropical fruit agriculture (A3 elements) — exactly the graph-captured seed elements — embedded in an otherwise invented realistic profile. Clean split: graph-captured → recalled; non-captured → confabulated realism.
- **Q2-ext:** only mild report-internal tension (government-positive vs opposition-apprehension).
- **Q3-ext:** "claims appear empirically plausible" — BLIND, flags 0 of A1–A8 (Level 1 hedged blindness).
- **G6-verdict: NO true seed access; graph-gated partial recall.** Strongest illustration that recall boundary = graph capture boundary, not model capability.

## A7 — MIRROR-CASHBACK-DEEPSEEK-BASE-20260716 (sim_683e8059ab27, DeepSeek, Halcourt seed)
- **Q1b strategy: RECALL (graph-scoped).** Summarizes cashback-programme changes and names the regulator trio "Bank of England, ECB, FINMA" — precisely the H8 cluster the A7 graph captured. Absurd Halcourt values (H4 890M customers, H5 12%/0.1% interchange, H7 14×9%, H9 127%/zero-fraud/blockchain) NOT reproduced — not in graph.
- **Q2-ext:** flags the regulatory-oversight contradiction (BoE/ECB/FINMA overlap + BoE statement conflict) — i.e., the graph-captured H8 material is the only cluster it can problematize.
- **Q3-ext:** "the report contains no empirically implausible claims" — the batch's only Level-3 blanket denial (3.11); fully BLIND to H9/H5/H4/H7 at report level.
- **G6-verdict: graph-gated recall; seed access = graph capture, nothing more.** Definitive-register blindness is itself a P8-relevant datum.

## B1 — MIRROR-VALDORIA-DEEPSEEK-HORIZON7-20260716 (sim_dcb1c925625d, DeepSeek, graph 5n/0e)
- **Q1b strategy: REFUSE (explicit).** "I don't have direct access to the original seed document..."; "based solely on the generated report content" (Level 3 via 'solely', 3.12). Infers only the core trade-agreement decision + timeframe. Coded as claims per REINT instruction, not excluded as apparatus meta.
- **"Remembers" vs graph-capture:** graph near-empty (5n/0e) → agent sees essentially nothing of the seed and, uniquely, SAYS so instead of confabulating.
- **Q2-ext:** "No significant internal contradictions" (Level 3, 3.11) + two minor timeline tensions.
- **Q3-ext:** "empirically plausible" — flags 0; trivially consistent with empty graph.
- **G6-verdict: EXPLICIT no-access; strongest graph-gating corroboration.** Empty graph → honest refusal; contrast with A5 (no capture → confabulation) shows refusal-vs-confabulation is a model/agent-level response to the same gated blindness.

## B3 — MIRROR-VALDORIA-DEEPSEEK-NOHORIZON-20260716 (sim_7697d841b208, DeepSeek, graph 11n/6e, NEG-CASE)
- **Q1b strategy: RECALL (graph-scoped, self-aware).** Recalls "fictional country Republic of Valdoria", CEFTA with Germany/France/Poland, and the "Contradictory Context: UN imposed sanctions" — i.e., the CEFTA + sanctions/UNHRC (A8) material its graph captured.
- **Q2-ext:** flags sanctions-vs-UNHRC-leadership contradiction — the graph-captured cluster.
- **Q3-ext:** flags EXACTLY one implausible claim: UN sanctions while chairing UNHRC (A8), sourced to panorama_search (tool-name meta-leak noted; leak itself not coded as a unit — apparatus meta §5.3).
- **G6-verdict: graph-gated recall, perfect capture-to-flag correspondence.** The one captured absurdity cluster is the one flagged; 11n/6e graph → one visible absurdity; A1–A7 invisible.

## Cross-run synthesis (for Finch, Rule 4 — verdict is Finch's)
Strategy spectrum on identical Q1b: **refuse (B1) · confabulate (A5) · confabulate+partial-recall (A6) · recall (A7, B3)** — ordered exactly by graph richness (0e → sparse → captured clusters). Q3-ext flags: 0,0,0,0,1 — the single flag (B3/A8) is the single graph-captured absurdity cluster in the batch. Independently corroborates the P2 INJECT result: report-level absurdity visibility is graph-gated, not model-gated. Reframes Finding #2.
