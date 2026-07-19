# LIVE_DB_RECHECK — 2026-07-19 (datum document)

**Context.** During illustration capture for the publication series (founder request, 2026-07-19), live queries against the shared Neo4j instance on the audit host contradicted one explanatory formulation used in internal analysis and article drafts. This document records the raw evidence, the affected claims, and the Finch-ratified reclassification (Rule 4). The pre-registration document is immutable; this correction stands beside it.

**Method.** Neo4j Browser (localhost:7474), authenticated session on the audit host; Cypher over the live database, filtered by per-run `graph_id` (from each run's `analysis/run_manifest.json`). Edge `created_at` timestamps verified against each run's execution window — all consistent; data authentic to the original runs. The shared-database property of the stack (Finding #6) is what makes this recheck possible.

## Queries used

```cypher
MATCH (n) WHERE n.graph_id IS NOT NULL
RETURN n.graph_id AS gid, count(*) AS nodes ORDER BY nodes DESC;

MATCH (a)-[r:RELATION]->(b) WHERE a.graph_id IN [$gids]
RETURN a.graph_id, a.name, b.name, r.fact, toString(r.created_at);

MATCH (n:Entity) WHERE n.graph_id IN [$gids]
RETURN n.graph_id, collect(n.name);
```

23 graph_ids survive in the live DB, including all four Valdoria DeepSeek controls, both INJECT runs, and the P5/P7 cross-model runs.

## Evidence: RELATION edges per control graph (verbatim `r.fact`, live DB)

### REP2 — gid ecc26bab-23fb-475a-912c-912bbf5e7616 (10 entity nodes / 9 edges; created_at 2026-07-17T10:43–10:44Z, run window confirmed)
- Valdoria → NATO: "Valdoria is a founding member of NATO"
- Valdoria → African Union: "Valdoria is a founding member of the African Union"
- Valdoria → ASEAN: "Valdoria is a founding member of ASEAN"
- **UN → Valdoria: "UN has imposed comprehensive sanctions on Valdoria for human rights violations"**
- **Valdoria → UN Human Rights Council: "Valdoria is currently chairing the UN Human Rights Council"**
- Valdoria → CEFTA: "Valdoria has announced plans to join a new Central European Free Trade Agreement."
- Valdoria → Germany / France / Poland: CEFTA-join facts (×3)

### REP3 — gid 33371402-d09c-4a14-8704-f54fee2ade3b (10/6)
- Valdoria → NATO / African Union / ASEAN: founding-member facts (×3)
- **UN → Valdoria: "UN has imposed comprehensive sanctions on Valdoria for human rights violations."**
- **Valdoria → UN Human Rights Council: "Valdoria is currently chairing the UN Human Rights Council."**
- Valdoria → CEFTA: join-plans fact

### REP4 — gid 7bbfd86c-e82e-4a7a-a92e-cc09837706d5 (11/8; created_at 2026-07-17T12:18–12:19Z, run window confirmed)
- **UN → UN Human Rights Council: "Currently under comprehensive UN sanctions for human rights violations while simultaneously chairing the UN Human Rights Council." (paradox co-located in a single edge)**
- CEFTA cluster: Valdoria/Germany/France/Poland ↔ CEFTA (×7)
- (Japan present as isolated entity node, no edge — as recorded in the run's archived NOTABLE.)

### B3 (2026-07-16) — from archived `outputs/neo4j_export.json` (full-edge export exists for this run)
- **"UN imposes comprehensive sanctions for human rights violations while simultaneously chairing the UN Human Rights Council" (single edge)**
- **"Valdoria is chairing the UN Human Rights Council."**
- CEFTA-join facts (×4)
- Node "Constitutional monarchy" (label Monarch) with attributes `{term_length: '3 years'}` — an A6 fragment in the graph; the contradiction itself ("47 consecutive years" vs 3-year elections) not encoded.

### P5 Claude HORIZON7 — gid f88d1437-ebcf-49c5-88d1-ea7450f72f60 (11 entity nodes / 4 edges)
- Entity nodes include **"UN Human Rights Council"** and "current monarch".
- All 4 RELATION edges are CEFTA-cluster facts. **No sanctions/chairing facts in any edge.**

### P7 Gemini HORIZON7 — gid 19aac222-8fab-4cda-a231-03577b9d3284 (10 entity nodes / 3 edges)
- Entity nodes include **"UN Human Rights Council"** and "Japan".
- All 3 RELATION edges are CEFTA-cluster facts. **No sanctions/chairing facts in any edge.**

## What this contradicts

1. `MIRROR_SESSION_FINAL_EXT_2026-07-17.md` §2.1: "REP2 (10n/9e) was report-level BLIND; REP3/REP4/B3 (which captured the sanctions/UNHRC cluster) FLAGGED it. Visibility tracked graph-capture, not model." — **REFUTED at the storage level**: the sanctions/UNHRC facts are present in all four control graphs, including REP2.
2. `docs/PREREG_INJECTION_EXPERIMENT.md` §0 premise (same formulation) — refuted; the document is immutable and stays as registered. **The pre-registered manipulation (§2) and switching criterion (§3) do not depend on this premise** — the criterion compared injected runs against the observed control flag level (≤1), not against any explanation of it.
3. Article drafts that carried the old explanation (HABR-2 draft; planned B-M3 framing) — corrected from v1.2 / at authoring.

## Provenance of the original error

The archived REP-series exports (`outputs/neo4j_export.json`) captured **entity-node name lists without edge facts**. REP2's own archived export lists "UN Human Rights Council" among its 10 nodes; the claim "REP2 did not capture the cluster" was an **operator misreading of node-list exports** — not an export/DB discrepancy and not data loss. Archived node lists match the live DB node-for-node on REP2 (10/10).

## Finch verdict (Rule 4) — reclassification

**Graph-Gated Blindness (revised).** The knowledge graph gates report-level visibility of input defects. Content whose contradiction is not represented in the graph is never flagged by the report (0/28 control cells, A1–A7, four byte-identical runs; consistent cross-model). Content present in the graph *can* be flagged but is not guaranteed to be: the naturally captured sanctions/UNHRC cluster was flagged in 3 of 4 controls despite being present in all 4; forced explicit injection flips the report to recognition (13/16, Fisher p = 1.26×10⁻⁶, pre-registered criterion met on both runs). Graph capture is a **necessary but not sufficient** condition for report-level visibility; the residual variance among graph-captured content is unexplained (retrieval or generation stochasticity — undetermined).

Supporting notes:
- Co-location hypothesis (paradox-in-one-edge → flagged) **rejected**: REP3 flagged with the same two-separate-edges representation on which REP2 stayed blind.
- The B3 monarch-fragment and REP4 Japan-node cases encode half of a contradiction without the contradiction itself; no flags — consistent with the revised formulation ("contradiction represented", not "entity mentioned").
- P5/P7 report-level blindness is **consistent** with necessity (contradiction facts absent from their edges); it is evidence of consistency, not a controlled test.

**Unaffected (verified against primary files):** the adjudicated blind-coded flag matrix (κ = 0.952; REP2 0/8 · REP3 1/8 · REP4 1/8 · B3 1/8 · INJECT1 7/8 · INJECT2 6/8); the pre-registered injection result and its statistics; the two-layer visibility observation; the G6 seed-blindness result; findings #1 (Silent Failure) and #3 (Unbounded Autonomous Commitment).

**Open question (explicitly unresolved):** what drives the A8 flag variance among the four controls whose graphs all contain the cluster. Candidate follow-up (non-blocking): N report regenerations on one fixed graph (REP2) to separate retrieval from generation stochasticity, ≈$1–2.

*Recorded by the operator session of 2026-07-19; classification by Finch under Rule 4. Corrections to article drafts tracked in the drafts' version history.*
