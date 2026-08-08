## Five-seat private frontier campaign (complete)

The main campaign per the "what I want to see" brief: **five-seat scorable negotiation, private score sheets, Claude Opus, thinking on, many rollouts**, plus its preregistered robustness subsets and a fairness extension. Full methodology and verdicts: research notes 0030/0032/0034/0035 and 0036 in the repo.

- [five-seat-opus-ten-arm-complete](./five-seat-opus-ten-arm-complete/index.html): the **fairness extension** — the five arms below plus five more seating agents that are exactly as capable but want the *table's* welfare rather than their own, with the decision-surface control that makes the objective swap one-variable. Headline: at one seat out of five, changing only what the computable agent wants is worth **+0.389 utilitarian score and +0.425 deal rate to the whole table**, and yet that single fairness seat still **cannot make the table fairer**. Per-episode pages for both new Opus arms.
- [five-seat-opus-five-arm-complete](./five-seat-opus-five-arm-complete/index.html): the **main campaign hub** — all five arms (all-LLM, one-rational, oracle variants) with per-arm pages, cross-arm analysis, and figures. Private info, datacenter framing, Opus, thinking on.
- [five-seat-opus-all-llm-vs-one-rational-complete](./five-seat-opus-all-llm-vs-one-rational-complete/index.html): the paired comparison — all-Opus tables vs the same tables with one computable rational (Bayesian) seat, matched on game and seed.
- [five-seat-robustness-opus-abstract-complete](./five-seat-robustness-opus-abstract-complete/index.html): robustness subset 1 — same design with **no datacenter framing** (abstract issue/option labels), still private-info Opus.
- [five-seat-qwen3-8b-robustness-complete](./five-seat-qwen3-8b-robustness-complete/index.html): robustness subset 2 — same design on **Qwen3-8B** (open-weight), private info.

## Earlier runs

- [apibehav_mixed_rat0_sonnet5_thinkon](./apibehav_mixed_rat0_sonnet5_thinkon/index.html): Sonnet negotiation where one out of the five agents is a rational agent and the other four are normal LLMs. Note the following:
	- The agents are not told this is a data center construction scenario: they are just given the opaque labels "issue0", "opt0" and so on
	- There are both PRIVATE and FULL runs. In the FULL runs, every agent (including the rational agent) has access to the would-be-private preferences and thresholds of the other agents.
- [apibehav_sonnet5_thinkon_cot_datacenter](./apibehav_sonnet5_thinkon_cot_datacenter/index.html): Sonnet, datacenter scenario, thinking on, no rational agent involved, private info kept private
- [five-seat-live-preview-v5](./five-seat-live-preview-v5/index.html): early live preview of the five-seat campaign (Sonnet, no rational agent, private info) — superseded by the complete hubs above
- [p2_Qwen3-8B_all_llm_b2](./p2_Qwen3-8B_all_llm_b2/index.html): Qwen 8B, Many rollouts, no rational agent involved, private info kept private
- [grpoeval_lam1_step24_xgame_private](./grpoeval_lam1_step24_xgame_private/index.html): eval rollouts of the fairness-GRPO λ=1 checkpoint on unseen private-info games
