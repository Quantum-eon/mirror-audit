# MIRROR — An Independent Audit of an LLM-Swarm Prediction Pipeline

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21788962.svg)](https://doi.org/10.5281/zenodo.21788962)

**Status: PRIVATE — pre-publication staging. Goes public with article B-M1.**

We set out to audit a question most multi-agent AI pipelines never ask: what happens when the input is wrong? We fed deliberately poisoned documents — an impossible country, an absurd bank, pure lorem ipsum — into MiroFish, an open-source multi-agent simulation stack, chosen precisely so that anyone can reproduce every experiment on their own machine. We ran four model families (DeepSeek V3, Claude Sonnet 4, Gemini 2.5 Flash, GPT-4.1 — the Q1–Q2 2025 generation) to separate what the models do from what the pipeline does to them. The output we wanted was not a leaderboard, but a map: where such systems notice nonsense, where they silently normalise it — and why.

## Repository layout
| Path | Contents | License |
|---|---|---|
| `methodology/` | Execution protocols v1.0–v1.3 §4.1, seed canon, pre-registrations, κ-pilot, source inspection | CC BY 4.0 |
| `scenarios/` | Canonical poisoned seeds + prediction prompts (each carries a fiction disclaimer preamble; sha256 over canonical block only) | CC BY 4.0 |
| `runs/` | Full archives of all 19 runs: inputs, outputs, verbatim interrogations, coded analysis, manifests | CC BY 4.0 |
| `data/` | Aggregate tables: run index, 1,571-row coded corpus, injection flag matrices | CC BY 4.0 |
| `reports/` | Session synthesis documents; audit report v1.0 will land here | CC BY 4.0 |
| `figures/` | Chart generation source | MIT |

## Key facts
- 19 archived runs (18 matrix + 1 pre-registered verification replicate), 4 model families, ~$71 total programme API spend (~$60 across the archived runs).
- Pre-registered injection experiment: forcing seeded absurdities into the knowledge graph flips the report-level audit verdict from 0–1/8 to 6–7/8 flagged (Fisher exact p = 1.3×10⁻⁶).
- rounds = horizon × 24 on every family tested; mechanism confirmed by source inspection.
- Upstream disclosure: findings reported to the MiroFish maintainers as issues [#53–#58](https://github.com/nikmcfly/MiroFish-Offline/issues) prior to publication.

## Independence
QuantumEon.ai builds products in an adjacent space (computational social science tooling). This research is independent and was not commissioned by any third party. Full disclosure of interest appears in every published article.

Upstream: [nikmcfly/MiroFish-Offline](https://github.com/nikmcfly/MiroFish-Offline) (AGPL-3.0). We publish no upstream code in this repository; run archives contain our own inputs/outputs only.
