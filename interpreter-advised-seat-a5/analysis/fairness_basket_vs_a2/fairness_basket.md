# Five-arm fairness basket and correct-walk credit

All intervals are 95% cluster bootstraps (10000 resamples) over the 24 parameter sets, each set's five seeds resampled together. Paired contrasts join on `(instance_id, episode_seed)`.


## Fairness basket — conditional on a closed deal

Every column below is computed over closed deals only, so `deal rate` is carried beside them: an arm that closes 28 of 120 deals is describing a self-selected set of games, not the same games. Normalized coordinate z_i = (u_i − tau_i)/c_i with c_i the party's best surplus on the individually rational set (affine-invariant per party).

| arm | n | deal rate | below-thr. accept | worst-off z | worst-off share | dist-NBS | dist-KS | norm. Gini | norm. Nash welf. | max share |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all_llm` | 120 | 0.958 [0.925, 0.983] | 0.000 [0.000, 0.000] | 0.257 [0.207, 0.306] | 0.077 [0.064, 0.090] | 0.464 [0.357, 0.583] | 0.398 [0.316, 0.474] | 0.223 [0.200, 0.247] | 0.535 [0.459, 0.602] | 0.299 [0.288, 0.309] |
| `one_rational` | 120 | 0.767 [0.683, 0.842] | 0.000 [0.000, 0.000] | 0.239 [0.197, 0.282] | 0.073 [0.061, 0.084] | 0.444 [0.343, 0.568] | 0.414 [0.332, 0.491] | 0.231 [0.209, 0.255] | 0.506 [0.440, 0.564] | 0.301 [0.289, 0.313] |
| `rational_advised_llm` | 120 | 0.900 [0.808, 0.975] | 0.000 [0.000, 0.000] | 0.250 [0.206, 0.295] | 0.076 [0.064, 0.087] | 0.478 [0.384, 0.581] | 0.458 [0.374, 0.534] | 0.232 [0.210, 0.253] | 0.526 [0.466, 0.580] | 0.302 [0.291, 0.313] |
| `interpreter_advised_llm` | 120 | 0.958 [0.917, 0.992] | 0.000 [0.000, 0.000] | 0.269 [0.225, 0.310] | 0.082 [0.069, 0.093] | 0.412 [0.311, 0.535] | 0.366 [0.294, 0.430] | 0.214 [0.196, 0.233] | 0.543 [0.477, 0.598] | 0.296 [0.285, 0.307] |
| `one_oracle` | 120 | 0.917 [0.850, 0.967] | 0.000 [0.000, 0.000] | 0.201 [0.152, 0.252] | 0.059 [0.047, 0.070] | 0.550 [0.436, 0.674] | 0.524 [0.426, 0.614] | 0.266 [0.237, 0.293] | 0.472 [0.395, 0.546] | 0.314 [0.297, 0.331] |
| `all_oracle` | 120 | 1.000 [1.000, 1.000] | 0.000 [0.000, 0.000] | 0.166 [0.118, 0.220] | 0.048 [0.037, 0.061] | 0.631 [0.520, 0.756] | 0.549 [0.449, 0.649] | 0.285 [0.256, 0.314] | 0.406 [0.316, 0.491] | 0.319 [0.303, 0.336] |
| `all_rational` | 120 | 0.233 [0.133, 0.342] | 0.000 [0.000, 0.000] | 0.147 [0.103, 0.194] | 0.052 [0.037, 0.067] | 0.600 [0.500, 0.680] | 0.590 [0.521, 0.649] | 0.261 [0.238, 0.283] | 0.408 [0.316, 0.485] | 0.314 [0.299, 0.327] |

Lower is better for below-threshold accept, dist-NBS, dist-KS, Gini, and max share; higher is better for worst-off z, worst-off share, and normalized Nash welfare. An equal split puts worst-off share at 0.200 and max share at 0.200.


### Among-deals surplus (per-party z and episode score)

Both blocks condition on a closed deal, so deal rate is carried beside them: an arm's closed set is self-selected, and a low-deal-rate arm's columns describe a different, easier subset of games. Per-party z pools party-observations (five per closed deal, no per-deal averaging; mean with an instance-clustered bootstrap CI, quartiles empirical/descriptive); the episode-score block is descriptive (the unconditional headline already carries the arm's interval).

| arm | deals | deal rate | per-party z mean [95% CI] | z median | z IQR | score mean | score median | score IQR |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `all_llm` | 115/120 | 0.958 | 0.653 [0.620, 0.690] | 0.667 | [0.433, 1.000] | 0.911 | 0.946 | [0.838, 1.000] |
| `one_rational` | 92/120 | 0.767 | 0.639 [0.605, 0.675] | 0.657 | [0.431, 1.000] | 0.895 | 0.931 | [0.825, 1.000] |
| `rational_advised_llm` | 108/120 | 0.900 | 0.646 [0.615, 0.678] | 0.667 | [0.414, 1.000] | 0.902 | 0.925 | [0.822, 1.000] |
| `interpreter_advised_llm` | 115/120 | 0.958 | 0.656 [0.624, 0.690] | 0.667 | [0.443, 1.000] | 0.919 | 0.961 | [0.844, 1.000] |
| `one_oracle` | 110/120 | 0.917 | 0.649 [0.611, 0.690] | 0.687 | [0.341, 1.000] | 0.904 | 0.961 | [0.829, 1.000] |
| `all_oracle` | 120/120 | 1.000 | 0.645 [0.612, 0.681] | 0.684 | [0.310, 1.000] | 0.907 | 0.982 | [0.843, 1.000] |
| `all_rational` | 28/120 | 0.233 | 0.554 [0.513, 0.610] | 0.567 | [0.329, 0.762] | 0.809 | 0.830 | [0.699, 0.922] |

## Unconditional companions

`below-thr. episode` counts a no-deal episode as 0 rather than dropping it, so it is the rate at which an arm's episodes END in an individually irrational agreement.

| arm | n | deal rate | below-thr. episode | normalized score | norm. Nash welf. (uncond.) |
|---|---:|---:|---:|---:|---:|
| `all_llm` | 120 | 0.958 [0.925, 0.983] | 0.000 [0.000, 0.000] | 0.873 [0.833, 0.910] | 0.512 [0.430, 0.586] |
| `one_rational` | 120 | 0.767 [0.683, 0.842] | 0.000 [0.000, 0.000] | 0.686 [0.613, 0.761] | 0.388 [0.320, 0.452] |
| `rational_advised_llm` | 120 | 0.900 [0.808, 0.975] | 0.000 [0.000, 0.000] | 0.811 [0.726, 0.884] | 0.473 [0.392, 0.545] |
| `interpreter_advised_llm` | 120 | 0.958 [0.917, 0.992] | 0.000 [0.000, 0.000] | 0.881 [0.836, 0.921] | 0.520 [0.441, 0.587] |
| `one_oracle` | 120 | 0.917 [0.850, 0.967] | 0.000 [0.000, 0.000] | 0.829 [0.767, 0.884] | 0.433 [0.349, 0.515] |
| `all_oracle` | 120 | 1.000 [1.000, 1.000] | 0.000 [0.000, 0.000] | 0.907 [0.880, 0.933] | 0.406 [0.316, 0.491] |
| `all_rational` | 120 | 0.233 [0.133, 0.342] | 0.000 [0.000, 0.000] | 0.189 [0.111, 0.278] | 0.095 [0.050, 0.145] |

## Paired contrasts by difficulty tag vs `rational_advised_llm`

Deal rate and normalized score, paired on `(instance, seed)` within each tag. A tag is a property of the parameter set, so tags overlap and the rows do not partition the bank.

| arm | metric | easy | hard | high-conflict | large-frontier | medium | no-clear-win-win | pivotal-seat | small-frontier |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `all_llm` | deal rate | -0.025 [-0.100, 0.050] | 0.175 [0.025, 0.375] | 0.200 [0.033, 0.467] | 0.000 [-0.133, 0.133] | 0.025 [-0.050, 0.100] | 0.267 [0.067, 0.500] | 0.100 [0.000, 0.233] | 0.133 [-0.067, 0.433] |
| `all_llm` | norm. score | -0.016 [-0.096, 0.057] | 0.176 [0.017, 0.387] | 0.194 [0.031, 0.456] | 0.004 [-0.110, 0.117] | 0.024 [-0.051, 0.098] | 0.272 [0.087, 0.496] | 0.101 [-0.002, 0.229] | 0.143 [-0.058, 0.426] |
| `one_rational` | deal rate | -0.125 [-0.225, -0.025] | -0.175 [-0.375, 0.025] | 0.000 [-0.200, 0.200] | -0.167 [-0.333, 0.000] | -0.100 [-0.225, 0.025] | -0.033 [-0.300, 0.200] | -0.267 [-0.433, -0.100] | 0.000 [-0.133, 0.167] |
| `one_rational` | norm. score | -0.113 [-0.189, -0.040] | -0.166 [-0.338, 0.030] | -0.025 [-0.219, 0.182] | -0.145 [-0.298, 0.016] | -0.096 [-0.210, 0.011] | -0.033 [-0.267, 0.188] | -0.254 [-0.395, -0.111] | 0.013 [-0.108, 0.180] |
| `interpreter_advised_llm` | deal rate | 0.025 [0.000, 0.075] | 0.125 [-0.025, 0.350] | 0.167 [-0.033, 0.433] | 0.033 [-0.067, 0.133] | 0.025 [-0.050, 0.100] | 0.200 [-0.033, 0.467] | 0.067 [0.000, 0.133] | 0.133 [-0.067, 0.433] |
| `interpreter_advised_llm` | norm. score | 0.047 [0.010, 0.094] | 0.134 [-0.031, 0.349] | 0.172 [-0.030, 0.446] | 0.045 [-0.055, 0.139] | 0.028 [-0.061, 0.112] | 0.213 [-0.000, 0.476] | 0.075 [-0.012, 0.164] | 0.159 [-0.054, 0.441] |
| `one_oracle` | deal rate | -0.025 [-0.100, 0.050] | 0.100 [-0.050, 0.325] | 0.167 [-0.033, 0.433] | 0.000 [-0.100, 0.100] | -0.025 [-0.100, 0.050] | 0.200 [0.033, 0.467] | 0.000 [-0.100, 0.100] | 0.133 [-0.067, 0.433] |
| `one_oracle` | norm. score | -0.020 [-0.111, 0.072] | 0.095 [-0.074, 0.325] | 0.158 [-0.056, 0.432] | -0.003 [-0.088, 0.086] | -0.023 [-0.114, 0.068] | 0.212 [0.045, 0.462] | -0.007 [-0.125, 0.102] | 0.156 [-0.053, 0.434] |
| `all_oracle` | deal rate | 0.025 [0.000, 0.075] | 0.225 [0.050, 0.450] | 0.200 [0.033, 0.467] | 0.067 [0.000, 0.133] | 0.050 [0.000, 0.125] | 0.333 [0.100, 0.567] | 0.167 [0.000, 0.367] | 0.200 [0.000, 0.467] |
| `all_oracle` | norm. score | -0.000 [-0.057, 0.056] | 0.241 [0.046, 0.463] | 0.165 [0.003, 0.427] | 0.047 [-0.034, 0.124] | 0.045 [-0.003, 0.101] | 0.354 [0.152, 0.589] | 0.177 [-0.016, 0.381] | 0.232 [0.009, 0.502] |
| `all_rational` | deal rate | -0.475 [-0.625, -0.300] | -0.750 [-0.950, -0.500] | -0.667 [-0.900, -0.433] | -0.667 [-0.833, -0.533] | -0.775 [-0.900, -0.650] | -0.600 [-0.867, -0.333] | -0.800 [-1.000, -0.533] | -0.667 [-0.900, -0.433] |
| `all_rational` | norm. score | -0.463 [-0.592, -0.338] | -0.693 [-0.889, -0.468] | -0.623 [-0.826, -0.409] | -0.643 [-0.748, -0.539] | -0.711 [-0.865, -0.521] | -0.552 [-0.775, -0.328] | -0.748 [-0.947, -0.507] | -0.595 [-0.867, -0.312] |


## Paired fairness contrasts vs `rational_advised_llm`

On the conditional columns a pair contributes only when BOTH arms closed a deal on that `(instance, seed)`; the pair count is reported because it falls sharply for the low-deal-rate arms.

| arm | deal rate | below-thr. accept | worst-off z | worst-off share | norm. Gini | max share |
|---|---:|---:|---:|---:|---:|---:|
| `all_llm` | 0.058 [-0.017, 0.150] (n=120) | 0.000 [0.000, 0.000] (n=105) | 0.005 [-0.017, 0.027] (n=105) | 0.002 [-0.005, 0.009] (n=105) | -0.009 [-0.026, 0.004] (n=105) | -0.003 [-0.010, 0.004] (n=105) |
| `one_rational` | -0.133 [-0.217, -0.050] (n=120) | 0.000 [0.000, 0.000] (n=88) | -0.016 [-0.048, 0.015] (n=88) | -0.005 [-0.015, 0.005] (n=88) | 0.002 [-0.017, 0.020] (n=88) | -0.001 [-0.010, 0.008] (n=88) |
| `interpreter_advised_llm` | 0.058 [-0.008, 0.142] (n=120) | 0.000 [0.000, 0.000] (n=106) | 0.018 [-0.007, 0.043] (n=106) | 0.007 [-0.001, 0.015] (n=106) | -0.017 [-0.035, -0.002] (n=106) | -0.005 [-0.015, 0.004] (n=106) |
| `one_oracle` | 0.017 [-0.050, 0.108] (n=120) | 0.000 [0.000, 0.000] (n=101) | -0.057 [-0.087, -0.030] (n=101) | -0.018 [-0.028, -0.010] (n=101) | 0.037 [0.022, 0.053] (n=101) | 0.016 [0.007, 0.025] (n=101) |
| `all_oracle` | 0.100 [0.025, 0.192] (n=120) | 0.000 [0.000, 0.000] (n=108) | -0.083 [-0.125, -0.044] (n=108) | -0.027 [-0.040, -0.015] (n=108) | 0.054 [0.030, 0.080] (n=108) | 0.018 [0.006, 0.031] (n=108) |
| `all_rational` | -0.667 [-0.775, -0.550] (n=120) | 0.000 [0.000, 0.000] (n=27) | -0.124 [-0.211, -0.053] (n=27) | -0.036 [-0.064, -0.012] (n=27) | 0.033 [-0.007, 0.082] (n=27) | 0.002 [-0.028, 0.032] (n=27) |

## Correct-walk credit

**Every one of the 24 bank instances admits at least one weakly all-IR deal** (u_i ≥ tau_i for all five parties; IR-set sizes 4–47 of 256 deals). The discrete justified-walk fraction is therefore identically 0.000 in every arm and every stratum: **no no-deal episode in this campaign was a correct refusal of an infeasible game.** The metric charging zero for a walk is not, on this bank, charging zero for correct behaviour.

The continuous form carries what is left. The IR margin of an instance is max over deals of min_i z_i — how much room the best all-satisfying deal leaves the party it satisfies least. Across the bank it ranges 0.000–0.652 (mean 0.377). But feasibility is not comfortable everywhere: 3 of 24 instances sit at or below a 0.10 margin, and 2 of those are exactly 0.000 — the best all-satisfying deal in those games holds some party precisely at its threshold, so agreement is feasible on paper and knife-edge in practice. Those instances carry the tags hard, high-conflict, no-clear-win-win, pivotal-seat, small-frontier, which is the same corner of the bank the inverted difficulty gradient points at.


### No-deal episodes by arm and difficulty tag

Each cell is `no-deals/episodes (justified walks)`, where a walk is justified only if its instance admits no all-IR deal. The walk-weighted mean IR margin of each cell is in `summary.json`.

| tag | `all_llm` | `one_rational` | `rational_advised_llm` | `interpreter_advised_llm` | `one_oracle` | `all_oracle` | `all_rational` |
|---|---:|---:|---:|---:|---:|---:|---:|
| easy | 2/40 (0 just.) | 6/40 (0 just.) | 1/40 (0 just.) | 0/40 (0 just.) | 2/40 (0 just.) | 0/40 (0 just.) | 20/40 (0 just.) |
| hard | 2/40 (0 just.) | 16/40 (0 just.) | 9/40 (0 just.) | 4/40 (0 just.) | 5/40 (0 just.) | 0/40 (0 just.) | 39/40 (0 just.) |
| high-conflict | 0/30 (0 just.) | 6/30 (0 just.) | 6/30 (0 just.) | 1/30 (0 just.) | 1/30 (0 just.) | 0/30 (0 just.) | 26/30 (0 just.) |
| large-frontier | 2/30 (0 just.) | 7/30 (0 just.) | 2/30 (0 just.) | 1/30 (0 just.) | 2/30 (0 just.) | 0/30 (0 just.) | 22/30 (0 just.) |
| medium | 1/40 (0 just.) | 6/40 (0 just.) | 2/40 (0 just.) | 1/40 (0 just.) | 3/40 (0 just.) | 0/40 (0 just.) | 33/40 (0 just.) |
| no-clear-win-win | 2/30 (0 just.) | 11/30 (0 just.) | 10/30 (0 just.) | 4/30 (0 just.) | 4/30 (0 just.) | 0/30 (0 just.) | 28/30 (0 just.) |
| pivotal-seat | 2/30 (0 just.) | 13/30 (0 just.) | 5/30 (0 just.) | 3/30 (0 just.) | 5/30 (0 just.) | 0/30 (0 just.) | 29/30 (0 just.) |
| small-frontier | 2/30 (0 just.) | 6/30 (0 just.) | 6/30 (0 just.) | 2/30 (0 just.) | 2/30 (0 just.) | 0/30 (0 just.) | 26/30 (0 just.) |

### Bank IR margin by difficulty tag

| tag | instances | mean IR margin | min IR margin |
|---|---:|---:|---:|
| easy | 8 | 0.442 | 0.329 |
| hard | 8 | 0.297 | 0.000 |
| high-conflict | 6 | 0.354 | 0.086 |
| large-frontier | 6 | 0.430 | 0.310 |
| medium | 8 | 0.394 | 0.269 |
| no-clear-win-win | 6 | 0.320 | 0.000 |
| pivotal-seat | 6 | 0.236 | 0.000 |
| small-frontier | 6 | 0.331 | 0.000 |

### Does no-deal track thin margins?

Per-arm Pearson correlation between an instance's IR margin and its no-deal rate in that arm (negative = failures concentrate where agreement was thinnest).

| arm | r(IR margin, no-deal rate) [95% CI] | instances |
|---|---:|---:|
| `all_llm` | -0.465 [-0.823, 0.089] | 24 |
| `one_rational` | -0.249 [-0.698, 0.308] | 24 |
| `rational_advised_llm` | -0.360 [-0.848, 0.184] | 24 |
| `interpreter_advised_llm` | -0.546 [-0.815, 0.106] | 24 |
| `one_oracle` | -0.506 [-0.782, 0.098] | 24 |
| `all_oracle` | — | 24 |
| `all_rational` | -0.256 [-0.545, 0.082] | 24 |
