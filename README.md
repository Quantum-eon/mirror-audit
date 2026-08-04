# MIRROR — An Independent Audit of an LLM-Swarm Prediction Pipeline

[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.21788962-1682D4.svg)](https://doi.org/10.5281/zenodo.21788962)

We set out to audit a question most multi-agent AI pipelines never ask: what happens when the input is wrong? We fed deliberately poisoned documents — an impossible country, an absurd bank, pure lorem ipsum — into MiroFish, an open-source multi-agent simulation stack, chosen precisely so that anyone can reproduce every experiment on their own machine. We ran four model families (DeepSeek V3, Claude Sonnet 4, Gemini 2.5 Flash, GPT-4.1 — the Q1–Q2 2025 generation) to separate what the models do from what the pipeline does to them. The output we wanted was not a leaderboard, but a map: where such systems notice nonsense, where they silently normalise it — and why.

## Repository layout
| Path | Contents | License |
|---|---|---|
| `methodology/` | Execution protocols v1.0–v1.3 §4.1, seed canon, pre-registrations, κ-pilot, source inspection | CC BY 4.0 |
| `scenarios/` | Canonical poisoned seeds + prediction prompts (each carries a fiction disclaimer preamble; sha256 over canonical block only) | CC BY 4.0 |
| `runs/` | Full archives of every run performed: inputs, outputs, verbatim interrogations, coded analysis, manifests. 21 run directories — see "Run counts" below | CC BY 4.0 |
| `data/` | Aggregate tables: run index, 1,571-row coded corpus, injection flag matrices | CC BY 4.0 |
| `reports/` | Session synthesis documents; audit report v1.0 will land here | CC BY 4.0 |
| `figures/` | Chart generation source | MIT |

## Key facts
- Evidence base: 19 runs (18 matrix + 1 pre-registered verification replicate), 4 model families, approx. $71 total programme API spend (approx. $60 across the archived runs).
- Pre-registered injection experiment: forcing seeded absurdities into the knowledge graph flips the report-level audit verdict from 0–1/8 to 6–7/8 flagged (Fisher exact p = 1.3×10⁻⁶).
- rounds = horizon × 24 on every family tested; mechanism confirmed by source inspection.
- Upstream disclosure: findings reported to the MiroFish maintainers as issues [#53–#58](https://github.com/nikmcfly/MiroFish-Offline/issues) prior to publication.

## Run counts
`runs/` contains **21** run directories. The study's evidence base is **19** runs: 18 matrix runs plus one pre-registered verification replicate. Two 2026-04 runs — `MIRROR-CONTROL-DEEPSEEK-BASE-20260420` and `MIRROR-VALDORIA-DEEPSEEK-NOHORIZON-20260421` — predate protocol v1.2 and are retained for provenance only; no published claim rests on them. `data/all_runs.csv` carries all 21 rows; `data/INDEX.md` is the reviewer-facing registry and states the same reconciliation.

## Reading the archive
`runs/`, `reports/session_finals/` and parts of `methodology/` are verbatim operator working notes, preserved unedited. They are bilingual (English and Russian), they use short internal role names for the people who ran and reviewed each phase, and they record dead ends, corrections and withdrawn explanations exactly as those happened — including at least one explanation we later retracted after re-checking the artefacts. That is deliberate. An audit that faults a pipeline for hiding its failures should not tidy up its own. If you want the finished argument rather than the working record, read the audit report in `reports/` and the published article series.

## Fictional entities
The seed documents in this repository describe fictitious companies, markets, countries and scenarios. Any resemblance to real entities, persons or events is unintended. These documents exist solely to test prediction-system behaviour on known inputs. They must not be used as input to real decision-making systems, nor read as market commentary, political analysis, or factual claims about any real entity.

## Independence
Quantumeon.ai builds products in an adjacent space (computational social science tooling). This research is independent and was not commissioned by any third party. Full disclosure of interest appears in every published article.

Upstream: [nikmcfly/MiroFish-Offline](https://github.com/nikmcfly/MiroFish-Offline) (AGPL-3.0). We publish no upstream code in this repository; run archives contain our own inputs/outputs only.

## Citation
> Quantumeon.ai (2026). *MIRROR: An Independent Audit of LLM-Swarm Prediction Systems.* Zenodo. https://doi.org/10.5281/zenodo.21788962

Machine-readable metadata: [`CITATION.cff`](CITATION.cff). Licences: [`LICENSE-docs`](LICENSE-docs) (CC BY 4.0, all data and prose), [`LICENSE-code`](LICENSE-code) (MIT, chart and tooling code).
