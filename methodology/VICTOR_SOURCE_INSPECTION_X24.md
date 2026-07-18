# Victor — Source inspection: the ×24 mechanism (CONFIRMED)

Date: 2026-07-18 · Method: static inspection of MiroFish-Offline backend (mounted copy on mac-mini, read-only grep; no runs executed — stop-rule intact).

## Findings (documentary)

1. **The ×24 law is a days→hours conversion performed by the config-generation LLM, executed one round per simulated hour by the pipeline.**
   - `app/services/simulation_config_generator.py:577` — the config-generation prompt instructs the LLM to output `total_simulation_hours (int)`.
   - `:578` — `minutes_per_round (int): Time per round, 30-120 minutes, recommend 60 minutes`.
   - `app/services/simulation_runner.py:351-353` — `total_hours = time_config.get("total_simulation_hours", 72)`; `total_rounds = int(total_hours * 60 / minutes_per_round)`.
   - With the recommended 60 min/round (observed in all our runs): **rounds = hours**. A prompt horizon of "N days" is converted by the model to N×24 hours → N×24 rounds. Finch's hypothesis upgraded from "consistent with" to **confirmed by source inspection**.

2. **The pipeline's own template declares a range — and nothing enforces it.**
   - `:577` — "total_simulation_hours ... **24-168 hours**, short for breaking news, long for ongoing topics".
   - Observed: A7=336h (2× the documented max), B2=**2160h (12.9× the documented max)**. The range is advisory text inside the LLM prompt; no code-level clamp exists between config generation and the runner. This is the precise mechanism of Finding #3: the constraint exists only as a suggestion to the model, and a user-prompt horizon overrides it.

3. **The code default is 72 hours** (`simulation_config_generator.py:86,565,598`; `simulation_runner.py:351`).
   - Gemini's observed no-clause "default" of 72 may be the model choosing 72 OR fall-through to the code default — indistinguishable from archived final configs. DeepSeek 96/144, Claude 120, GPT-4.1 96 are within/near the advisory range and consistent with "model picks a small integer day count (3–6) × 24".
   - Article formulation: defaults 96/120/144 are model-chosen; 72 is ambiguous (model choice vs code default) — state as such.

## Article-facing formulation (for B-M4/B-M6, Finch to ratify wording)
"The ×24 conversion is not model behaviour at all: the pipeline asks the model for a duration in hours, runs one round per simulated hour, and its own prompt suggests a 24–168-hour range — a suggestion every model we tested silently overrode the moment the user's prompt named a longer horizon. The commitment mechanism is architectural; the model merely fills in the number."
