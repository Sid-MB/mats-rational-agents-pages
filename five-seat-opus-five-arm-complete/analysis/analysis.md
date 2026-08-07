# Five-seat private-information campaign

All intervals are 95% instance-clustered bootstrap intervals; no-deal scores zero.

| logical arm | n | normalized score [95% CI] | deal rate [95% CI] | paired score gain vs all-LLM |
|---|---:|---:|---:|---:|
| all_llm | 120 | 0.873 [0.833, 0.910] | 0.958 [0.925, 0.992] | reference |
| one_rational | 120 | 0.686 [0.613, 0.759] | 0.767 [0.692, 0.842] | -0.186 [-0.267, -0.106] |
| one_oracle | 120 | 0.461 [0.377, 0.544] | 0.508 [0.417, 0.600] | -0.412 [-0.493, -0.323] |
| all_rational | 120 | 0.189 [0.110, 0.278] | 0.233 [0.133, 0.342] | -0.684 [-0.786, -0.580] |
| all_oracle | 120 | 0.791 [0.734, 0.842] | 0.875 [0.817, 0.925] | -0.082 [-0.146, -0.022] |

Direct all-rational minus one-rational paired normalized-score effect: -0.498 [-0.590, -0.404] (positive favors five rational agents).

## Difficulty-tag strata

Paired normalized-score effects versus all-LLM:

| tag | one rational [95% CI] | n pairs |
|---|---:|---:|
| easy | -0.096 [-0.197, 0.027] | 40 |
| hard | -0.342 [-0.435, -0.259] | 40 |
| high-conflict | -0.220 [-0.327, -0.110] | 30 |
| large-frontier | -0.149 [-0.364, 0.066] | 30 |
| medium | -0.120 [-0.274, 0.010] | 40 |
| no-clear-win-win | -0.305 [-0.466, -0.143] | 30 |
| pivotal-seat | -0.356 [-0.467, -0.260] | 30 |
| small-frontier | -0.130 [-0.271, 0.027] | 30 |

Selected complete-episode API cost: $461.28.
Campaign ledger spend (including failed/retried attempts): $466.61 of $1800.00.

Difficulty correlations are descriptive and stored with their per-instance points in `summary.json`.
