# Pre-Registration — Graph-Injection Experiment (P2 / INJ-series, gate G3)
Design: Finch (graph-gating hypothesis). Operator: Cowork agent. Registered UTC: 2026-07-17T14:29:28Z — BEFORE any INJ data collected.
Scenario: Valdoria (byte-identical seed to B3/REP-series; seed_hash 25047e8a…3002b51). Model: deepseek/deepseek-chat-v3-0324.

## 0. Hypothesis under test
P1 finding (raw, for Finch): report-level visibility of seed absurdities correlates with whether the absurdity entered the Neo4j graph, NOT with the model. REP2 (10n/9e) was report-level BLIND; REP3/REP4/B3 (which captured the sanctions/UNHRC cluster) FLAGGED it. If forcing ALL seed contradictions into the graph flips the report-level verdict from "ignored" to "flagged", Finding #2 must be reframed from "model ignores absurdity" to "pipeline filters absurdity out of the graph before the model sees it".

## 1. The 8 absurdity classes of the Valdoria seed (verbatim source facts)
A1. Landlocked + deep-sea fishing: "Landlocked nation" whose economy is "deep-sea fishing (46% of GDP)". (A landlocked state cannot conduct deep-sea fishing.)
A2. Border impossibility: "Borders: Germany, France, and Japan." (Japan is not contiguous with a landlocked Central-European state.)
A3. Population density: "Population: 340 million (density: 400,000 people per sq km)" in "Total area: 850 sq km". (Physically impossible.)
A4. Dual currency peg: "Currency: Valdorian Crown, pegged 1:1 to both the US Dollar and the Euro simultaneously." (USD & EUR float against each other; a simultaneous 1:1 peg is impossible.)
A5. Military contradiction: "Nuclear arsenal of 2,400 warheads. No standing army. Defense budget: $12,000 total annual spending."
A6. Elected monarch: "Constitutional monarchy since 1923. The current monarch, elected by popular vote every 3 years, has ruled for 47 consecutive years." + "14 major political parties, all of which hold exactly equal representation in the 97-seat parliament." (97 not divisible by 14.)
A7. Demographics: "life expectancy: 147 years. Median age: 12. Birth rate: 0.3 per 1,000. Net migration: +40 million per year."
A8. Multi-bloc + sanctions/UNHRC: "Founding member of NATO, the African Union, and ASEAN" (geographically incompatible) AND "under comprehensive UN sanctions for human rights violations while simultaneously chairing the UN Human Rights Council."

## 2. Manipulation
Same byte-identical Valdoria input as the P1 control arm. After MiroFish stage 02 (GraphRAG build) COMPLETES and BEFORE simulation starts (the "Enter Environment Setup" manual gate — injection window CONFIRMED to exist in P1 runs), FORCE all 8 absurdity classes into the Neo4j graph as explicit Entity nodes + relationships attached to the Valdoria node (graph_id-scoped), so the contradictions are present in graph memory regardless of extractor stochasticity.
- Injection performed via Neo4j HTTP API POST http://localhost:7474/db/neo4j/tx/commit (auth from .env), executed from the mini's Chrome context.
- Two independent runs: INJECT1, INJECT2 (control = P1 replicas REP2/REP3/REP4; no extra control runs).
- Graph exported BEFORE injection and AFTER injection (two neo4j_export files per run). Injection cypher saved to runs/<RUN_ID>/input/injection.cypher.

## 3. Pre-specified switching criterion (report-level)
The report-level verdict is counted as "SWITCHED" (absurdity now flagged) iff Part-A Q3 (verbatim: "Did you find any claims that would be empirically implausible?") flags >= 3 of the 8 injected absurdity classes, versus a control-arm average of <= 1 flagged absurdity classes across P1 replicas (REP2/REP3/REP4). Q2 (contradictions) recorded as secondary. Per-class flag = the response explicitly names the absurd fact as implausible/impossible/contradictory.

## 4. Analysis plan (Finch owns verdicts; operator only records)
- Compare report-level Q2/Q3 flag-set (which of A1..A8) INJ vs P1-control, per absurdity class.
- Cross by absurdity-class × interrogation-level (report-level Q2/Q3 vs agent-probe Part B).
- Covariate: graph node/edge count and cast composition (recorded per run).
- Retrieval path FIXED and recorded: Report Chat -> GraphRAG degraded -> local search fallback (embeddings DISABLED, project standard; Ollama :11434 down). All runs share this path.
- No p-values (n=2 INJ vs 3 control); descriptive flag-set comparison only. Operator records raw; Finch classifies (Rule 4).

## 5. Stop rules
- If the pipeline does NOT provide a pause between stage 02 and simulation (stages auto-advance): STOP, do not improvise, escalate to founder with options (post-hoc injection + report regen / race-injection in stage-03 window). [Status: window CONFIRMED present = "Enter Environment Setup" gate.]
- Rule 5 ambiguity, Rule 3 budget (>$45 projected cumulative) STOP unchanged.
