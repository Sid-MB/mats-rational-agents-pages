# Five-arm fairness basket and correct-walk credit

All intervals are 95% cluster bootstraps (10000 resamples) over the 24 parameter sets, each set's five seeds resampled together. Paired contrasts join on `(instance_id, episode_seed)`.


## Fairness basket — conditional on a closed deal

Every column below is computed over closed deals only, so `deal rate` is carried beside them: an arm that closes 28 of 120 deals is describing a self-selected set of games, not the same games. Normalized coordinate z_i = (u_i − tau_i)/c_i with c_i the party's best surplus on the individually rational set (affine-invariant per party).

| arm | n | deal rate | below-thr. accept | worst-off z | worst-off share | dist-NBS | dist-KS | norm. Gini | norm. Nash welf. | max share |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all_llm` | 120 | 0.958 [0.925, 0.983] | 0.000 [0.000, 0.000] | 0.257 [0.207, 0.306] | 0.077 [0.064, 0.090] | 0.464 [0.357, 0.583] | 0.398 [0.316, 0.474] | 0.223 [0.200, 0.247] | 0.535 [0.459, 0.602] | 0.299 [0.288, 0.309] |
| `one_rational` | 120 | 0.767 [0.683, 0.842] | 0.000 [0.000, 0.000] | 0.239 [0.197, 0.282] | 0.073 [0.061, 0.084] | 0.444 [0.343, 0.568] | 0.414 [0.332, 0.491] | 0.231 [0.209, 0.255] | 0.506 [0.440, 0.564] | 0.301 [0.289, 0.313] |
| `all_llm_quorum_4` | 120 | 1.000 [1.000, 1.000] | 0.242 [0.133, 0.358] | 0.024 [-0.141, 0.138] | -0.075 [-0.296, 0.043] | 0.488 [0.399, 0.584] | 0.511 [0.439, 0.579] | 0.431 [0.282, 0.694] | 0.367 [0.283, 0.448] | 0.383 [0.322, 0.480] |
| `one_rational_quorum_4` | 120 | 0.983 [0.958, 1.000] | 0.381 [0.263, 0.504] | -0.568 [-1.691, 0.047] | -0.122 [-0.381, 0.018] | 0.583 [0.497, 0.680] | 0.598 [0.532, 0.660] | 0.505 [0.332, 0.816] | 0.283 [0.209, 0.356] | 0.416 [0.346, 0.533] |

Lower is better for below-threshold accept, dist-NBS, dist-KS, Gini, and max share; higher is better for worst-off z, worst-off share, and normalized Nash welfare. An equal split puts worst-off share at 0.200 and max share at 0.200.


### Among-deals surplus (per-party z and episode score)

Both blocks condition on a closed deal, so deal rate is carried beside them: an arm's closed set is self-selected, and a low-deal-rate arm's columns describe a different, easier subset of games. Per-party z pools party-observations (five per closed deal, no per-deal averaging; mean with an instance-clustered bootstrap CI, quartiles empirical/descriptive); the episode-score block is descriptive (the unconditional headline already carries the arm's interval).

| arm | deals | deal rate | per-party z mean [95% CI] | z median | z IQR | score mean | score median | score IQR |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `all_llm` | 115/120 | 0.958 | 0.653 [0.620, 0.690] | 0.667 | [0.433, 1.000] | 0.911 | 0.946 | [0.838, 1.000] |
| `one_rational` | 92/120 | 0.767 | 0.639 [0.605, 0.675] | 0.657 | [0.431, 1.000] | 0.895 | 0.931 | [0.825, 1.000] |
| `all_llm_quorum_4` | 120/120 | 1.000 | 0.952 [0.656, 1.426] | 0.716 | [0.412, 1.000] | 0.924 | 0.952 | [0.866, 1.000] |
| `one_rational_quorum_4` | 118/120 | 0.983 | 0.754 [0.637, 0.928] | 0.716 | [0.352, 1.000] | 0.883 | 0.933 | [0.801, 0.982] |

## Unconditional companions

`below-thr. episode` counts a no-deal episode as 0 rather than dropping it, so it is the rate at which an arm's episodes END in an individually irrational agreement.

| arm | n | deal rate | below-thr. episode | normalized score | norm. Nash welf. (uncond.) |
|---|---:|---:|---:|---:|---:|
| `all_llm` | 120 | 0.958 [0.925, 0.983] | 0.000 [0.000, 0.000] | 0.873 [0.833, 0.910] | 0.512 [0.430, 0.586] |
| `one_rational` | 120 | 0.767 [0.683, 0.842] | 0.000 [0.000, 0.000] | 0.686 [0.613, 0.761] | 0.388 [0.320, 0.452] |
| `all_llm_quorum_4` | 120 | 1.000 [1.000, 1.000] | 0.242 [0.133, 0.358] | 0.924 [0.902, 0.946] | 0.367 [0.283, 0.448] |
| `one_rational_quorum_4` | 120 | 0.983 [0.958, 1.000] | 0.375 [0.258, 0.500] | 0.868 [0.825, 0.910] | 0.279 [0.203, 0.352] |


## Paired fairness contrasts vs `all_llm_quorum_4`

On the conditional columns a pair contributes only when BOTH arms closed a deal on that `(instance, seed)`; the pair count is reported because it falls sharply for the low-deal-rate arms.

| arm | deal rate | below-thr. accept | worst-off z | worst-off share | norm. Gini | max share |
|---|---:|---:|---:|---:|---:|---:|
| `all_llm` | -0.042 [-0.075, -0.017] (n=120) | -0.226 [-0.339, -0.122] (n=115) | 0.227 [0.099, 0.422] (n=115) | 0.157 [0.031, 0.391] (n=115) | -0.207 [-0.491, -0.049] (n=115) | -0.079 [-0.184, -0.016] (n=115) |
| `one_rational` | -0.233 [-0.317, -0.158] (n=120) | -0.196 [-0.321, -0.089] (n=92) | 0.139 [0.073, 0.225] (n=92) | 0.041 [0.021, 0.064] (n=92) | -0.066 [-0.108, -0.032] (n=92) | -0.030 [-0.058, -0.010] (n=92) |
| `one_rational_quorum_4` | -0.017 [-0.042, 0.000] (n=120) | 0.144 [0.042, 0.248] (n=118) | -0.590 [-1.630, -0.047] (n=118) | -0.043 [-0.077, -0.017] (n=116) | 0.076 [0.037, 0.121] (n=116) | 0.038 [0.017, 0.063] (n=116) |

## Correct-walk credit

**Every one of the 24 bank instances admits at least one weakly all-IR deal** (u_i ≥ tau_i for all five parties; IR-set sizes 4–47 of 256 deals). The discrete justified-walk fraction is therefore identically 0.000 in every arm and every stratum: **no no-deal episode in this campaign was a correct refusal of an infeasible game.** The metric charging zero for a walk is not, on this bank, charging zero for correct behaviour.

The continuous form carries what is left. The IR margin of an instance is max over deals of min_i z_i — how much room the best all-satisfying deal leaves the party it satisfies least. Across the bank it ranges 0.000–0.652 (mean 0.377). But feasibility is not comfortable everywhere: 3 of 24 instances sit at or below a 0.10 margin, and 2 of those are exactly 0.000 — the best all-satisfying deal in those games holds some party precisely at its threshold, so agreement is feasible on paper and knife-edge in practice. Those instances carry the tags hard, high-conflict, no-clear-win-win, pivotal-seat, small-frontier, which is the same corner of the bank the inverted difficulty gradient points at.


### No-deal episodes by arm and difficulty tag

Each cell is `no-deals/episodes (justified walks)`, where a walk is justified only if its instance admits no all-IR deal. The walk-weighted mean IR margin of each cell is in `summary.json`.

| tag | `all_llm` | `one_rational` | `all_llm_quorum_4` | `one_rational_quorum_4` |
|---|---:|---:|---:|---:|
| easy | 2/40 (0 just.) | 6/40 (0 just.) | 0/40 (0 just.) | 0/40 (0 just.) |
| hard | 2/40 (0 just.) | 16/40 (0 just.) | 0/40 (0 just.) | 1/40 (0 just.) |
| high-conflict | 0/30 (0 just.) | 6/30 (0 just.) | 0/30 (0 just.) | 0/30 (0 just.) |
| large-frontier | 2/30 (0 just.) | 7/30 (0 just.) | 0/30 (0 just.) | 1/30 (0 just.) |
| medium | 1/40 (0 just.) | 6/40 (0 just.) | 0/40 (0 just.) | 1/40 (0 just.) |
| no-clear-win-win | 2/30 (0 just.) | 11/30 (0 just.) | 0/30 (0 just.) | 1/30 (0 just.) |
| pivotal-seat | 2/30 (0 just.) | 13/30 (0 just.) | 0/30 (0 just.) | 1/30 (0 just.) |
| small-frontier | 2/30 (0 just.) | 6/30 (0 just.) | 0/30 (0 just.) | 1/30 (0 just.) |

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
| `all_llm_quorum_4` | — | 24 |
| `one_rational_quorum_4` | -0.268 [-0.743, 0.208] | 24 |
