# one_rational vs all_llm: unanimity against all_llm_quorum_4's quorum rule

All intervals are 95% bootstrap intervals clustered on the 24 parameter sets. Every contrast is paired on `(instance_id, episode_seed)`; the DiD is paired across all four arms at once.

| metric | treated cost under unanimity | treated cost under quorum | DiD (quorum − unanimity) |
|---|---:|---:|---:|
| deal_rate | -0.192 [-0.275, -0.108] | -0.017 [-0.042, 0.000] | 0.175 [0.092, 0.258] |
| below_threshold_episode | 0.000 [0.000, 0.000] | 0.133 [0.025, 0.242] | 0.133 [0.025, 0.242] |
| normalized_primary | -0.186 [-0.266, -0.105] | -0.056 [-0.091, -0.025] | 0.130 [0.053, 0.208] |
| normalized_nash_welfare | -0.124 [-0.187, -0.065] | -0.089 [-0.139, -0.038] | 0.035 [-0.052, 0.124] |
| below_threshold_accept | 0.000 [0.000, 0.000] | 0.144 [0.042, 0.248] | 0.133 [0.000, 0.262] |
| worst_off | -0.011 [-0.043, 0.021] | -0.590 [-1.626, -0.048] | -0.348 [-1.102, 0.042] |
| worst_off_share | -0.004 [-0.015, 0.006] | -0.043 [-0.079, -0.017] | -0.010 [-0.037, 0.019] |
| dist_to_nbs | -0.048 [-0.142, 0.042] | 0.098 [0.056, 0.139] | 0.134 [0.029, 0.240] |
| dist_to_ks | -0.012 [-0.096, 0.069] | 0.092 [0.043, 0.140] | 0.090 [-0.012, 0.196] |
| normalized_gini | 0.005 [-0.015, 0.026] | 0.076 [0.037, 0.122] | 0.032 [-0.013, 0.073] |
| normalized_nash_welfare_conditional | -0.024 [-0.066, 0.015] | -0.086 [-0.135, -0.035] | -0.048 [-0.137, 0.041] |
| max_share | 0.000 [-0.009, 0.010] | 0.038 [0.017, 0.063] | 0.018 [-0.008, 0.041] |

## Arm levels

| arm | deal_rate | below_threshold_episode | normalized_primary | normalized_nash_welfare |
|---|---:|---:|---:|---:|
| all_llm | 0.958 [0.925, 0.992] | 0.000 [0.000, 0.000] | 0.873 [0.833, 0.912] | 0.512 [0.431, 0.587] |
| one_rational | 0.767 [0.683, 0.842] | 0.000 [0.000, 0.000] | 0.686 [0.613, 0.761] | 0.388 [0.320, 0.451] |
| all_llm_quorum_4 | 1.000 [1.000, 1.000] | 0.242 [0.133, 0.358] | 0.924 [0.902, 0.946] | 0.367 [0.283, 0.447] |
| one_rational_quorum_4 | 0.983 [0.958, 1.000] | 0.375 [0.258, 0.500] | 0.868 [0.824, 0.909] | 0.279 [0.207, 0.352] |

## The protocol's own effect on each lineup (quorum minus unanimity)

| lineup | deal_rate | below_threshold_episode | normalized_primary | normalized_nash_welfare |
|---|---:|---:|---:|---:|
| all_llm | 0.042 [0.008, 0.075] | 0.242 [0.133, 0.367] | 0.052 [0.005, 0.099] | -0.145 [-0.227, -0.068] |
| one_rational | 0.217 [0.150, 0.292] | 0.375 [0.258, 0.492] | 0.182 [0.119, 0.248] | -0.110 [-0.177, -0.046] |
