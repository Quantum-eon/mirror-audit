# PROPOSED STANDARD — Embeddings disabled across MIRROR run matrix

Status: **proposed by operator (Stepanov), 2026-06-23** — pending formalization as a D-MIRROR entry by Q-Alex. Recorded by Cowork operator; NOT a unilateral protocol amendment.

## Decision
Embeddings (GraphRAG vector retrieval) remain **DISABLED for the entire MIRROR run matrix**. MiroFish-Offline's embedding layer (Ollama `/api/embed`, `nomic-embed-text`, via `EMBEDDING_BASE_URL`/`EMBEDDING_MODEL`) is left unconfigured. No per-run variation.

## Rationale
- The embedding model is independent of the chat LLM under test. Varying it per run (and the suggestion to route to Opus/DeepSeek) would (a) be technically invalid — Opus/DeepSeek/OpenRouter expose no embeddings endpoint — and (b) couple two variables, breaking the single-variable (chat-LLM) design.
- Holding embeddings OFF as a constant keeps all runs comparable.

## Consequences (apply going forward)
1. GraphRAG retrieval degrades uniformly: graph searches return 0 facts; graph edges = 0; reports synthesized from agent interviews + LLM priors. This is the **expected baseline condition**, recorded as a constant — not flagged as a per-run anomaly.
2. Manifests should carry `embeddings: disabled (project standard)` rather than an anomaly entry for the embedding failure.
3. Comparability: A1, A4, A5 already ran with embeddings OFF → consistent; **no re-runs required**. Do NOT enable embeddings selectively for A6/A7/B*/C1.
4. If embeddings are ever enabled later, ALL anchor runs (A1/A4/A5) must be re-run under the new condition for comparability — that is a separate D-MIRROR decision.

## Not changed
- No code or `.env` change required (embeddings already disabled; defaults point at an unrunning Ollama).
- Existing archived A5 run is unchanged: its embedding degradation is retained as valid data.
