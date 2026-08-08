# Ten-arm fairness-led comparison

Reference arm for every paired contrast: `all_llm`. Intervals are 10000 cluster-bootstrap resamples over the 24 parameter sets (their five seeds resampled together). Paired contrasts join on `(instance_id, episode_seed)`; no-deal scores zero.


## Levels — both co-primaries side by side

`normalized_primary` is the utilitarian score the self-interested agents optimize; `normalized_nash_welfare` is the fairness objective's own coordinate. Each family is expected to lead on the metric it optimizes, which is why neither is reported alone.

| arm | normalized_primary | normalized_nash_welfare | deal_rate |
|---|---|---|---|
| `all_fairness_algorithmic` | 0.278 | 0.152 | 0.375 |
| `all_fairness_oracle` | 0.967 | 0.596 | 1.000 |
| `all_llm` | 0.873 | 0.512 | 0.958 |
| `all_oracle` | 0.791 | 0.370 | 0.875 |
| `all_rational` | 0.189 | 0.095 | 0.233 |
| `all_selfish_dp_oracle` | 0.871 | 0.397 | 1.000 |
| `one_fairness_algorithmic` | 0.697 | 0.408 | 0.808 |
| `one_fairness_oracle` | 0.850 | 0.492 | 0.933 |
| `one_oracle` | 0.461 | 0.240 | 0.508 |
| `one_rational` | 0.686 | 0.388 | 0.767 |

## Levels — the referee basket

`max_share` is the boundary-extraction detector (share of total normalized gain taken by the biggest winner); `worst_off` is the least-satisfied party's normalized gain. `walked_rate` and `expired_rate` split the no-deal episodes, which score identically on everything else.

| arm | dist_to_nbs | dist_to_ks | gini | worst_off | max_share | ir_rate | walked_rate | expired_rate |
|---|---|---|---|---|---|---|---|---|
| `all_fairness_algorithmic` | 0.567 | 0.537 | 0.324 | 0.129 | 0.334 | 0.375 | 0.000 | 0.625 |
| `all_fairness_oracle` | 0.091 | 0.092 | 0.252 | 0.357 | 0.275 | 1.000 | 0.000 | 0.000 |
| `all_llm` | 0.464 | 0.398 | 0.299 | 0.257 | 0.299 | 0.958 | 0.000 | 0.042 |
| `all_oracle` | 0.621 | 0.545 | 0.354 | 0.172 | 0.319 | 0.875 | 0.000 | 0.125 |
| `all_rational` | 0.600 | 0.590 | 0.311 | 0.147 | 0.314 | 0.233 | 0.000 | 0.767 |
| `all_selfish_dp_oracle` | 0.609 | 0.526 | 0.356 | 0.161 | 0.329 | 1.000 | 0.000 | 0.000 |
| `one_fairness_algorithmic` | 0.550 | 0.469 | 0.312 | 0.233 | 0.309 | 0.808 | 0.000 | 0.192 |
| `one_fairness_oracle` | 0.391 | 0.330 | 0.296 | 0.273 | 0.299 | 0.933 | 0.000 | 0.067 |
| `one_oracle` | 0.549 | 0.479 | 0.346 | 0.187 | 0.314 | 0.508 | 0.000 | 0.492 |
| `one_rational` | 0.444 | 0.414 | 0.294 | 0.239 | 0.301 | 0.767 | 0.000 | 0.233 |

## Levels — how agreement was reached

`turns_to_close` is conditional on a deal; `n_distinct_openers` counts the different deals proposed in the opening round, which is the focal-point statistic — agents optimizing the same table-level objective under the same information all open on one deal.

| arm | turns_to_close | n_distinct_openers | deal_rate |
|---|---|---|---|
| `all_fairness_algorithmic` | 13.000 | 2.300 | 0.375 |
| `all_fairness_oracle` | 5.000 | 1.000 | 1.000 |
| `all_llm` | 17.748 | 3.967 | 0.958 |
| `all_oracle` | 5.000 | 1.142 | 0.875 |
| `all_rational` | 24.821 | 3.600 | 0.233 |
| `all_selfish_dp_oracle` | 24.783 | 3.175 | 1.000 |
| `one_fairness_algorithmic` | 19.732 | 3.658 | 0.808 |
| `one_fairness_oracle` | 18.964 | 4.025 | 0.933 |
| `one_oracle` | 19.475 | 3.883 | 0.508 |
| `one_rational` | 21.391 | 3.917 | 0.767 |

## Paired effects vs `all_llm`

| arm | normalized_primary | normalized_nash_welfare | deal_rate | gini | worst_off | max_share |
|---|---|---|---|---|---|---|
| `all_fairness_algorithmic` | -0.595 | -0.361 | -0.583 | 0.058 | -0.134 | 0.032 |
| `all_fairness_oracle` | 0.094 | 0.083 | 0.042 | -0.053 | 0.108 | -0.024 |
| `all_oracle` | -0.082 | -0.143 | -0.083 | 0.053 | -0.075 | 0.019 |
| `all_rational` | -0.684 | -0.417 | -0.725 | 0.030 | -0.096 | 0.006 |
| `all_selfish_dp_oracle` | -0.001 | -0.116 | 0.042 | 0.054 | -0.090 | 0.031 |
| `one_fairness_algorithmic` | -0.175 | -0.104 | -0.150 | 0.006 | -0.021 | 0.008 |
| `one_fairness_oracle` | -0.023 | -0.020 | -0.025 | -0.004 | 0.018 | -0.001 |
| `one_oracle` | -0.412 | -0.273 | -0.450 | 0.040 | -0.070 | 0.018 |
| `one_rational` | -0.186 | -0.124 | -0.192 | -0.005 | -0.011 | 0.000 |

## Episodes per arm

- `all_fairness_algorithmic`: 120
- `all_fairness_oracle`: 120
- `all_llm`: 120
- `all_oracle`: 120
- `all_rational`: 120
- `all_selfish_dp_oracle`: 120
- `one_fairness_algorithmic`: 120
- `one_fairness_oracle`: 120
- `one_oracle`: 120
- `one_rational`: 120
