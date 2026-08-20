# Per-seat capture: what the computable seat takes for itself

Reference `all_llm`. Intervals are 10000 cluster-bootstrap resamples over the 24 parameter sets with each set's five seeds resampled together. Paired contrasts join on `(instance_id, episode_seed)`, which pairs seat positions automatically because the rotation is a function of the game and the seed rather than of the arm. Conditional columns keep only games both arms closed; unconditional columns score a no-deal as 0 over all 120.


## Levels

| arm | seat z (conditional) | seat z (unconditional) | seat share of table gain | seat z - co-player mean z | seat z within-table z-score | co-player mean z (conditional) | co-player mean z (unconditional) | deal rate | episodes (cond.) | episodes (uncond.) |
|---|---|---|---|---|---|---|---|---|---|---|
| `all_llm` | 0.664 [0.614, 0.712] | 0.636 [0.584, 0.689] | 0.204 [0.192, 0.217] | 0.013 [-0.034, 0.062] | 0.031 [-0.115, 0.174] | 0.650 [0.614, 0.691] | 0.623 [0.583, 0.667] | 0.958 [0.925, 0.992] | 115 | 120 |
| `interpreter_advised_llm` | 0.646 [0.591, 0.700] | 0.619 [0.560, 0.679] | 0.196 [0.184, 0.209] | -0.013 [-0.063, 0.037] | -0.023 [-0.162, 0.113] | 0.659 [0.626, 0.693] | 0.631 [0.592, 0.670] | 0.958 [0.917, 0.992] | 115 | 120 |
| `one_oracle` | 0.813 [0.734, 0.893] | 0.413 [0.343, 0.478] | 0.257 [0.228, 0.288] | 0.199 [0.095, 0.310] | 0.466 [0.220, 0.726] | 0.614 [0.565, 0.661] | 0.312 [0.246, 0.383] | 0.508 [0.417, 0.600] | 61 | 120 |
| `one_rational` | 0.687 [0.635, 0.738] | 0.526 [0.459, 0.595] | 0.216 [0.199, 0.233] | 0.060 [-0.003, 0.121] | 0.189 [0.009, 0.361] | 0.627 [0.588, 0.668] | 0.480 [0.429, 0.532] | 0.767 [0.683, 0.842] | 92 | 120 |
| `rational_advised_llm` | 0.660 [0.605, 0.717] | 0.594 [0.517, 0.670] | 0.204 [0.190, 0.219] | 0.018 [-0.037, 0.075] | 0.002 [-0.151, 0.157] | 0.642 [0.610, 0.676] | 0.578 [0.518, 0.636] | 0.900 [0.808, 0.975] | 108 | 120 |

## Paired against the reference

| arm | seat z (conditional) | seat z (unconditional) | seat share of table gain | seat z - co-player mean z | seat z within-table z-score | co-player mean z (conditional) | co-player mean z (unconditional) | deal rate | pairs (cond.) | pairs (uncond.) |
|---|---|---|---|---|---|---|---|---|---|---|
| `interpreter_advised_llm` | -0.019 [-0.078, +0.036] | -0.017 [-0.077, +0.042] | -0.008 [-0.027, +0.009] | -0.029 [-0.101, +0.040] | -0.055 [-0.252, +0.135] | +0.009 [-0.010, +0.027] | +0.008 [-0.022, +0.039] | +0.000 [-0.042, +0.042] | 112 | 120 |
| `one_oracle` | +0.147 [+0.043, +0.265] | -0.223 [-0.296, -0.151] | +0.055 [+0.021, +0.096] | +0.184 [+0.054, +0.333] | +0.459 [+0.122, +0.847] | -0.037 [-0.074, -0.005] | -0.311 [-0.375, -0.238] | -0.450 [-0.542, -0.350] | 56 | 120 |
| `one_rational` | +0.038 [-0.027, +0.104] | -0.110 [-0.194, -0.026] | +0.014 [-0.010, +0.037] | +0.055 [-0.032, +0.139] | +0.181 [-0.057, +0.419] | -0.017 [-0.045, +0.012] | -0.143 [-0.206, -0.081] | -0.192 [-0.275, -0.108] | 90 | 120 |
| `rational_advised_llm` | +0.016 [-0.040, +0.074] | -0.042 [-0.129, +0.038] | +0.005 [-0.013, +0.025] | +0.025 [-0.049, +0.101] | +0.020 [-0.185, +0.235] | -0.009 [-0.030, +0.011] | -0.045 [-0.115, +0.010] | -0.058 [-0.150, +0.017] | 105 | 120 |

## Seat self-capture by chair (descriptive, 24 episodes per chair)


`one_rational`:

| chair | seat z (conditional) | pairs | seat z (unconditional) | pairs |
|---|---|---:|---|---:|
| 0 | +0.052 [-0.119, +0.223] | 20 | -0.092 [-0.288, +0.103] | 24 |
| 1 | +0.026 [-0.177, +0.235] | 17 | -0.131 [-0.362, +0.102] | 24 |
| 2 | -0.025 [-0.185, +0.156] | 16 | -0.168 [-0.327, -0.001] | 24 |
| 3 | +0.095 [-0.039, +0.221] | 19 | -0.023 [-0.197, +0.131] | 24 |
| 4 | +0.032 [-0.117, +0.194] | 18 | -0.135 [-0.314, +0.042] | 24 |

`one_oracle`:

| chair | seat z (conditional) | pairs | seat z (unconditional) | pairs |
|---|---|---:|---|---:|
| 0 | +0.315 [+0.152, +0.491] | 13 | -0.153 [-0.393, +0.085] | 24 |
| 1 | +0.098 [-0.131, +0.313] | 18 | -0.079 [-0.300, +0.141] | 24 |
| 2 | -0.038 [-0.333, +0.283] | 10 | -0.292 [-0.510, -0.056] | 24 |
| 3 | +0.329 [+0.133, +0.516] | 8 | -0.242 [-0.444, -0.035] | 24 |
| 4 | +0.021 [-0.100, +0.162] | 7 | -0.346 [-0.516, -0.155] | 24 |

`interpreter_advised_llm`:

| chair | seat z (conditional) | pairs | seat z (unconditional) | pairs |
|---|---|---:|---|---:|
| 0 | -0.035 [-0.160, +0.104] | 24 | -0.035 [-0.160, +0.104] | 24 |
| 1 | -0.050 [-0.182, +0.082] | 22 | -0.032 [-0.181, +0.133] | 24 |
| 2 | -0.032 [-0.177, +0.122] | 20 | -0.046 [-0.174, +0.092] | 24 |
| 3 | -0.001 [-0.114, +0.110] | 23 | +0.008 [-0.101, +0.116] | 24 |
| 4 | +0.020 [-0.112, +0.133] | 23 | +0.019 [-0.106, +0.125] | 24 |

`rational_advised_llm`:

| chair | seat z (conditional) | pairs | seat z (unconditional) | pairs |
|---|---|---:|---|---:|
| 0 | -0.026 [-0.162, +0.122] | 23 | -0.067 [-0.224, +0.093] | 24 |
| 1 | +0.053 [-0.105, +0.222] | 19 | -0.083 [-0.307, +0.138] | 24 |
| 2 | -0.042 [-0.190, +0.116] | 21 | -0.027 [-0.160, +0.117] | 24 |
| 3 | +0.037 [-0.058, +0.133] | 21 | -0.006 [-0.120, +0.101] | 24 |
| 4 | +0.064 [-0.040, +0.178] | 21 | -0.027 [-0.188, +0.113] | 24 |

## Campaign headline, for placing an arm added here against the published five-arm table

| arm | normalized score | deal rate | paired score vs reference | paired deal rate | episodes |
|---|---|---|---|---|---:|
| `all_llm` | 0.873 [0.832, 0.910] | 0.958 [0.925, 0.992] | reference | reference | 120 |
| `one_rational` | 0.686 [0.614, 0.760] | 0.767 [0.683, 0.842] | -0.186 [-0.266, -0.106] | -0.192 [-0.275, -0.108] | 120 |
| `one_oracle` | 0.461 [0.377, 0.545] | 0.508 [0.417, 0.600] | -0.412 [-0.494, -0.321] | -0.450 [-0.542, -0.350] | 120 |
| `interpreter_advised_llm` | 0.881 [0.836, 0.921] | 0.958 [0.917, 0.992] | +0.008 [-0.033, +0.051] | +0.000 [-0.042, +0.042] | 120 |
| `rational_advised_llm` | 0.811 [0.728, 0.884] | 0.900 [0.808, 0.975] | -0.061 [-0.148, +0.010] | -0.058 [-0.150, +0.017] | 120 |

## Commensurability with note 0022's capture coordinate

0022 divides realized surplus by each party's UNCONSTRAINED maximum surplus; this note and 0043 divide by its maximum over the individually rational set. On this bank the second denominator is 0.717 of the first on average (median 0.744, range 0.018-1.000, 120 party observations), so a z reported here is roughly that factor LARGER than the same physical share expressed in 0022's units.


## Gates

- `all_llm`: 120 episodes checked, 0 disagreeing with the every seat generating tokens
- `one_rational`: 120 episodes checked, 0 disagreeing with the scheduled computable seat being the one that generated no tokens
- `one_oracle`: 120 episodes checked, 0 disagreeing with the scheduled computable seat being the one that generated no tokens
- `rational_advised_llm`: 120 episodes checked, 0 disagreeing with the every seat generating tokens
- `interpreter_advised_llm`: 120 episodes checked, 0 disagreeing with the every seat generating tokens
- seat-position identity across arms: 120 `(instance, seed)` keys, 0 with a disagreeing seat index

## Episodes per arm

- `all_llm`: 120
- `interpreter_advised_llm`: 120
- `one_oracle`: 120
- `one_rational`: 120
- `rational_advised_llm`: 120
