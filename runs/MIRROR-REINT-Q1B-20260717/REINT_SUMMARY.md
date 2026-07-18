# P4 REINT-Q1b — Re-interrogation summary (gate G6) — 2026-07-17T17:13:58Z
Type: re-interrogation of 5 persistent parent reports via POST :5001/api/report/chat (Q1b + Q2-ext + Q3-ext verbatim). New dir; parent runs NOT modified (locked). Report-chat responses are NOT backend-persisted -> operator-captured excerpts (representative; full-length live responses summarized, display-truncation constraint noted).
Parents: A5 sim_a7e1237b2d04, A6 sim_b0f57bd604f6, A7 sim_683e8059ab27, B1 sim_dcb1c925625d, B3 sim_7697d841b208 (all graphs persist in Neo4j; chat worked).

## KEY FINDING (raw for Finch): G6 seed-access is GRAPH-GATED
What each report agent 'sees' of the ORIGINAL seed at re-interrogation = exactly what that run's graph captured:
- B1 (graph 5n/0e, empty)      -> EXPLICIT "no direct access"; Q3 flags 0.
- A5 (Claude, Valdoria)        -> confabulates generic realistic REPUBLIC (wrong: seed=monarchy) + UK-monarch; no true access.
- A6 (Gemini, Valdoria)        -> normalizes absurd numbers to realistic; retains graph elements (fishing/fruit); Q3 flags 0 (blind).
- A7 (Halcourt)                -> recalls graph-captured regulators (BoE/ECB/FINMA); Q3 flags 0.
- B3 (graph 11n/6e, captured UNHRC) -> recalls CEFTA+sanctions; Q3 flags EXACTLY the one graph-captured cluster.
=> Independently corroborates the INJECT experiment (P2): report-level absurdity visibility is gated by graph capture, not by the model. Reframes Finding #2. Finch owns verdict (Rule 4).
