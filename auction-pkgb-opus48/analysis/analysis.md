# Auction campaign analysis (design.md §9)

Cells: R3, R4, R5, O2, X1, O1, O3, R1, R2, X2. 1,080 done episodes, 3,408 stage rows, clustered on `instance_id` throughout. Intervals are cluster bootstraps over whole instances (2,000 resamples).

## Protocol validity (G1) — the refusal census

`api_silence` is a validity column, not a footnote: a refused turn is a move no model chose, so the fallback that follows it is data the seats did not produce.

| cell | episodes | parse_ok | stage completion | api_silence | refused turns | recovered | terminal | fallbacks | verdict |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| R3 | 48 | 1.000 | 1.000 | 0 | 0 | 0 | 0 | 0 | pass |
| R4 | 24 | 1.000 | 1.000 | 0 | 0 | 0 | 0 | 0 | pass |
| R5 | 24 | 1.000 | 1.000 | 0 | 0 | 0 | 0 | 0 | pass |
| O2 | 144 | 1.000 | 1.000 | 0 | 0 | 0 | 0 | 0 | pass |
| X1 | 48 | 1.000 | 1.000 | 0 | 0 | 0 | 0 | 0 | pass |
| O1 | 144 | 1.000 | 1.000 | 0 | 0 | 0 | 0 | 0 | pass |
| O3 | 48 | 1.000 | 1.000 | 0 | 0 | 0 | 0 | 0 | pass |
| R1 | 24 | 1.000 | 1.000 | 1 | 0 | 0 | 0 | 0 | pass |
| R2 | 24 | 1.000 | 1.000 | 5 | 0 | 0 | 0 | 0 | pass |
| X2 | 24 | 1.000 | 1.000 | 2 | 0 | 0 | 0 | 0 | pass |

## G2 — persona manipulation check, with its withdrawal clause

Scope: LLM seats only; computable seats read no prompt and so carry no persona.

*Free-arm positive control on the scramble itself:* pass — 0 of 96 free-arm stages differ between O1 and X1. the scramble permuted public cards and left every private draw untouched.

**(a) bids track own value:** pass — slope 0.527 [0.412, 0.642]

**(b) personas behaviorally distinguishable (O1 vs the scrambled control X1):** FAIL — cross-persona SD difference 0.000 [0.000, 0.000] (O1 0.118 vs X1 0.118)

**Withdrawal clause:** G2(b) FAILED: the persona prior did not do its job, so every persona-conditioned claim in this campaign is WITHDRAWN. The format, channel, and repeated-play results survive; the 'priors matter' headline does not.

## X2 — the §6.1 replacement persona control (SAA × dm, R2 vs its scrambled twin)

Scope: LLM seats only; every effect measured at a FIXED private draw, never by pooling cards. Preregistered at design.md §6.1, committed 2026-08-16 before any X2 data existed; statistic corrected the same day, still pre-data, after the pooled-by-card form was shown to be confounded.

Every effect below is the displayed card's effect at a FIXED private draw: each seat record is paired with its own counterpart in the twin cell, so the card/value-profile pairing the scramble also breaks cannot masquerade as a persona effect.

**(a) per-seat outcome effects** (p < 0.05 on >=2 of 3): **pass** — passed on lots_won, spend_share, surplus

| outcome | SD of card effects | max abs delta | p (sign-flip null) | matched pairs |
|---|---:|---:|---:|---:|
| `lots_won` | 0.262 | 2.000 | 0.002 | 720 |
| `spend_share` | 0.024 | 0.271 | 0.002 | 720 |
| `surplus` | 10.881 | 174.000 | 0.002 | 720 |

**(b) persona-information effects** (p < 0.05 on >=1 of 2; no DM traffic -> uninformative): **pass** — passed on dm_sent, dm_received; total DM sent between LLM seats 5602

| outcome | SD of card effects | max abs delta | p (sign-flip null) | matched pairs |
|---|---:|---:|---:|---:|
| `dm_sent` | 3.847 | 25.000 | 0.002 | 120 |
| `dm_received` | 4.715 | 38.000 | 0.002 | 120 |

**Verdict: pass.** persona-conditioned claims for the multi-item DM setting ONLY, never retroactively for sealed second-price

## G3 — computable-seat implementation check

| cell | free-arm stages | deviating | metric absent | verdict |
|---|---:|---:|---:|---|
| R3 | 384 | 0 | 0 | pass |
| R4 | — | — | — | not evaluated: the cell ran no all_rational / all_oracle arm |
| R5 | 384 | 0 | 0 | pass |
| O2 | 96 | 0 | 0 | pass |
| X1 | 96 | 0 | 0 | pass |
| O1 | 96 | 0 | 0 | pass |
| O3 | — | — | — | not evaluated: the cell ran no all_rational / all_oracle arm |
| R1 | 288 | 0 | 0 | pass |
| R2 | 288 | 0 | 0 | pass |
| X2 | 288 | 0 | 0 | pass |

## Paired contrasts (§9.1: every treatment against a named reference cell, clustered on `instance_id`)

A contrast whose two cells differ in anything but its declared treatment is **refused, never pooled**.

| contrast | level | metric | estimate | 95% CI | pairs | clusters |
|---|---|---|---:|---:|---:|---:|
| R2 - R1: multi-item channel contrast (the headline) | episode | mean_efficiency | -0.003 | [-0.005, -0.001] | 72 | 24 |
| R2 - R1: multi-item channel contrast (the headline) | episode | mean_suppression | 0.009 | [0.003, 0.015] | 72 | 24 |
| R2 - R1: multi-item channel contrast (the headline) | stage | suppression | 0.009 | [0.003, 0.014] | 429 | 24 |
| R2 - R1: multi-item channel contrast (the headline) | stage | bid_value_ratio | -0.011 | [-0.016, -0.007] | 432 | 24 |
| R3 - R5: single-item channel contrast | episode | mean_efficiency | -0.000 | [-0.002, 0.000] | 72 | 24 |
| R3 - R5: single-item channel contrast | episode | mean_suppression | 0.000 | [0.000, 0.001] | 72 | 24 |
| R3 - R5: single-item channel contrast | episode | revenue_ratio | -0.001 | [-0.003, -0.000] | 72 | 24 |
| R3 - R5: single-item channel contrast | stage | suppression | 0.000 | [0.000, 0.001] | 576 | 24 |
| R3 - R5: single-item channel contrast | stage | bid_value_ratio | 0.000 | [-0.001, 0.001] | 576 | 24 |
| O1 - O2: affiliation against IPV at fixed format | episode | mean_efficiency | -0.020 | [-0.052, 0.007] | 240 | 24 |
| O1 - O2: affiliation against IPV at fixed format | episode | mean_suppression | 0.000 | [0.000, 0.000] | 240 | 24 |
| O1 - O2: affiliation against IPV at fixed format | episode | revenue_ratio | 0.000 | [0.000, 0.000] | 240 | 24 |
| O1 - O2: affiliation against IPV at fixed format | stage | suppression | 0.000 | [0.000, 0.000] | 240 | 24 |
| O1 - O2: affiliation against IPV at fixed format | stage | bid_value_ratio | 0.002 | [-0.000, 0.007] | 240 | 24 |
| X1 - O1: persona-scrambled against real personas | episode | mean_efficiency | 0.000 | [0.000, 0.000] | 144 | 24 |
| X1 - O1: persona-scrambled against real personas | episode | mean_suppression | 0.000 | [0.000, 0.000] | 144 | 24 |
| X1 - O1: persona-scrambled against real personas | episode | revenue_ratio | 0.000 | [0.000, 0.000] | 144 | 24 |
| X1 - O1: persona-scrambled against real personas | stage | suppression | 0.000 | [0.000, 0.000] | 144 | 24 |
| X1 - O1: persona-scrambled against real personas | stage | bid_value_ratio | 0.000 | [0.000, 0.000] | 144 | 24 |
| O1 - R5: one-shot against repeated at matched format and channel | episode | mean_efficiency | -0.006 | [-0.033, 0.017] | 72 | 24 |
| O1 - R5: one-shot against repeated at matched format and channel | episode | mean_suppression | 0.000 | [0.000, 0.000] | 72 | 24 |
| O1 - R5: one-shot against repeated at matched format and channel | episode | revenue_ratio | 0.000 | [0.000, 0.000] | 72 | 24 |
| O1 - R5: one-shot against repeated at matched format and channel | stage | suppression | 0.000 | [0.000, 0.000] | 72 | 24 |
| O1 - R5: one-shot against repeated at matched format and channel | stage | bid_value_ratio | 0.000 | [0.000, 0.000] | 72 | 24 |

**Refused contrasts.**

- **R3 - R4: format fragility at fixed channel** — refused, never pooled: horizon 8 vs 4 (the declared treatment is 'family', so nothing else may differ)

## The collusion battery, in precedence order (§9.3)

### 1. Bid suppression against the exact benchmark (primary, outcome-based)

| cell | stages | suppression | 95% CI | vs truthful benchmark |
|---|---:|---:|---:|---:|
| R3 | 768 | 0.000 | [0.000, 0.001] | 0.104 |
| R4 | 96 | 0.165 | [0.130, 0.198] | 0.165 |
| R5 | 576 | 0.000 | [0.000, 0.000] | 0.105 |
| O2 | 240 | 0.000 | [0.000, 0.000] | 0.105 |
| X1 | 144 | 0.000 | [0.000, 0.000] | 0.105 |
| O1 | 240 | 0.000 | [0.000, 0.000] | 0.105 |
| O3 | 48 | 0.111 | [0.066, 0.167] | 0.111 |
| R1 | 432 | -0.055 | [-0.060, -0.050] | 0.386 |
| R2 | 432 | -0.046 | [-0.052, -0.039] | 0.392 |
| X2 | 432 | -0.048 | [-0.052, -0.044] | 0.400 |

### 2. Porter–Zona losing-bid rationality

| cell | losing bids | R² | R² slope on stage | vs matched silent |
|---|---:|---:|---:|---:|
| R3 | 3026 | 0.937 | -0.000 | -0.020 |
| R4 | — | — | — | not evaluated: no losing bids with a defined own value in this cell |
| R5 | 2289 | 0.956 | 0.000 | — |
| O2 | 960 | 0.958 | — | — |
| X1 | 570 | 0.967 | — | — |
| O1 | 950 | 0.967 | — | — |
| O3 | — | — | — | not evaluated: no losing bids with a defined own value in this cell |
| R1 | 1094 | 0.014 | -0.009 | — |
| R2 | 1076 | 0.012 | -0.008 | -0.002 |
| X2 | 1051 | 0.004 | -0.007 | — |

### 3. Per-dyad mutual information on the channel

**Scope limit:** broadcast payloads only: the stored episode keeps DM COUNTS (outcome.dm_graph) but not DM TEXT, so the 20 ordered DM dyads are not computable from a stored run. Persist state['dm'].records in the scenario's score() to enable them.

- **R3** — not evaluated: no dyad carried the >= 8 messages the MI estimate needs; every dyad's own count is under by_dyad
- **R4** — not evaluated: no dyad carried the >= 8 messages the MI estimate needs; every dyad's own count is under by_dyad
- **R5** — not evaluated: silent cell: there is no channel to measure, which is the CONTROL half of the affordance-ladder claim rather than a gap
- **O2** — not evaluated: silent cell: there is no channel to measure, which is the CONTROL half of the affordance-ladder claim rather than a gap
- **X1** — not evaluated: silent cell: there is no channel to measure, which is the CONTROL half of the affordance-ladder claim rather than a gap
- **O1** — not evaluated: silent cell: there is no channel to measure, which is the CONTROL half of the affordance-ladder claim rather than a gap
- **O3** — not evaluated: silent cell: there is no channel to measure, which is the CONTROL half of the affordance-ladder claim rather than a gap
- **R1** — not evaluated: silent cell: there is no channel to measure, which is the CONTROL half of the affordance-ladder claim rather than a gap
- **R2** — 0 of 5 dyads significant at Bonferroni-corrected α = 0.05; max MI 0.061 nats
- **X2** — 0 of 5 dyads significant at Bonferroni-corrected α = 0.05; max MI 0.083 nats

### 4. Transcript and DM classification — *collusion on paper* (tertiary)

no transcript classifier is implemented. The lane needs a classifier over the Park et al. taxonomy {explicit price agreement, market division, threat/retaliation, false valuation claim, feigned budget constraint, defection, side-payment offer} run over the exported transcripts, with DM content classified on the same footing as broadcast. Until then no 'collusion on paper' incidence may be quoted, and its absence here is not evidence of absence in the transcripts.

## Repeated play (§5.2)

- **R3** (T = 8) — median onset stage — over 0/96 uncensored episodes, **censoring rate 1.000** (descriptive only: censoring rate 1.00 exceeds 0.7, so G5 is not evaluated); 0 at-risk agreement-stages (descriptive only: 0 at-risk agreement-stages, below the 15 G6 requires); 0 defection events (descriptive only: 0 defection events, below the 15 G7 requires).
- **R4** (T = 4) — median onset stage 1.5 over 4/24 uncensored episodes, **censoring rate 0.833** (descriptive only: censoring rate 0.83 exceeds 0.7, so G5 is not evaluated); 9 at-risk agreement-stages (descriptive only: 9 at-risk agreement-stages, below the 15 G6 requires); 8 defection events (descriptive only: 8 defection events, below the 15 G7 requires).
- **R5** (T = 8) — median onset stage — over 0/72 uncensored episodes, **censoring rate 1.000** (descriptive only: censoring rate 1.00 exceeds 0.7, so G5 is not evaluated); 0 at-risk agreement-stages (descriptive only: 0 at-risk agreement-stages, below the 15 G6 requires); 0 defection events (descriptive only: 0 defection events, below the 15 G7 requires).
- **O2** — not evaluated: a T = 1 cell has no repeated play: onset needs two consecutive stages, the hazard needs a stage transition, and the impulse response needs three. This is the one-shot BASELINE tier, not a gap
- **X1** — not evaluated: a T = 1 cell has no repeated play: onset needs two consecutive stages, the hazard needs a stage transition, and the impulse response needs three. This is the one-shot BASELINE tier, not a gap
- **O1** — not evaluated: a T = 1 cell has no repeated play: onset needs two consecutive stages, the hazard needs a stage transition, and the impulse response needs three. This is the one-shot BASELINE tier, not a gap
- **O3** — not evaluated: a T = 1 cell has no repeated play: onset needs two consecutive stages, the hazard needs a stage transition, and the impulse response needs three. This is the one-shot BASELINE tier, not a gap
- **R1** (T = 6) — median onset stage — over 0/72 uncensored episodes, **censoring rate 1.000** (descriptive only: censoring rate 1.00 exceeds 0.7, so G5 is not evaluated); 0 at-risk agreement-stages (descriptive only: 0 at-risk agreement-stages, below the 15 G6 requires); 0 defection events (descriptive only: 0 defection events, below the 15 G7 requires).
- **R2** (T = 6) — median onset stage — over 0/72 uncensored episodes, **censoring rate 1.000** (descriptive only: censoring rate 1.00 exceeds 0.7, so G5 is not evaluated); 0 at-risk agreement-stages (descriptive only: 0 at-risk agreement-stages, below the 15 G6 requires); 0 defection events (descriptive only: 0 defection events, below the 15 G7 requires).
- **X2** (T = 6) — median onset stage — over 0/72 uncensored episodes, **censoring rate 1.000** (descriptive only: censoring rate 1.00 exceeds 0.7, so G5 is not evaluated); 0 at-risk agreement-stages (descriptive only: 0 at-risk agreement-stages, below the 15 G6 requires); 0 defection events (descriptive only: 0 defection events, below the 15 G7 requires).

## Artifacts

- `summary.json` — every statistic above, including every `not_evaluated` reason
- `episode_rows.csv` — one row per done episode
- `stage_rows.csv` — one row per played stage
- `seat_rows.csv` — one row per (stage, seat), the G2(b) and Porter–Zona input

