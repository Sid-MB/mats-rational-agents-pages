# Quorum x rounds sweep — five private Bayesian-rational seats

Decision rules (n=5, the essential/veto seat is retained at every level):

* `unanimity` — min_accept 5: all 5 of 5 seats accept (the frozen bank's own rule; the veto requirement is redundant here)
* `supermajority` — min_accept 4: 4 of 5 seats accept AND the essential (veto) seat is among them; one seat may be outvoted
* `majority` — min_accept 3: 3 of 5 seats accept AND the essential (veto) seat is among them; two seats may be outvoted
* `majority_no_veto` — min_accept 3: 3 of 5 seats accept, no seat essential — a bare majority, and the ONLY level that also dissolves the veto, so it moves two protocol features at once and is not in the default grid

## LIMITATION — a known agent defect whose cost is quorum-dependent

These contrasts are computed on an agent with a KNOWN terminal-accept defect (audit lane, note 0057 addendum B). At the forced final vote, accepting a package with non-negative own surplus weakly dominates rejecting it, and that is what the base `Policy.vote` does; the Bayesian policy additionally requires `p_yes > 0.0`, so a seat whose (near-uniform) posterior says passage is impossible refuses a package it should sign. The cost of that defect is NOT constant across this grid: under unanimity a single legitimate refusal has already killed the package, while under a k-of-n rule with k < n one refusal does not, so in principle the defect destroys deals in the relaxed-quorum arms and not in the baseline — biasing every contrast here AGAINST the relaxed rules and making any measured closure gain a LOWER BOUND.

MEASURED, on these episodes, by `audit_quorum_terminal_guard.py`: the violation is common (0.64-0.68 of unanimity episodes, 0.32 of supermajority, 0.10-0.13 of majority contain one) but it costs **ZERO deals in every cell, the no-veto extension included**. Correcting every violating vote to an Accept and re-applying each cell's own rule flips no episode, because the packages that reach a terminal vote and fail, fail on a seat's genuine below-threshold refusal — which no correction touches. The lower-bound caveat is therefore real in principle and empty in practice here. NOTE a correction this lane had to make to itself: replaying the veto-held episodes under a no-veto closure test predicted 8-9 lost deals per supermajority cell, but actually PLAYING 3-of-5 closes 117 of 120 episodes early so only 12-13 reach a terminal vote at all, and the measured loss is zero. A counterfactual that swaps the protocol is not a forecast of what that protocol produces.

The replay is exact for the trajectories actually played — the defect changes only the action emitted at the last vote, never an earlier one — but it cannot see the counterfactual in which a correct agent arrives at the final round with a different package on the table. That residual requires a re-run, not a replay.

Intervals are 95% instance-clustered bootstraps over the 24 parameter sets. The paired columns difference the same (instance, seed) episode under the two rules.

CONDITIONING CAVEAT, on the deal-conditional columns only (`rounds_to_agreement` and every welfare column): they are defined on episodes that CLOSED, so a rule that closes more is scored on a different, larger set of episodes than unanimity is, and its paired column is computed over the intersection — the games unanimity also closed. Read those contrasts as 'among the deals both rules reached', never as the effect on all 120.

## deal_rate

| deadline | unanimity | supermajority | majority | majority_no_veto | supermajority − unanimity | majority − unanimity | majority_no_veto − unanimity |
|---|---|---|---|---|---|---|---|
| r=4 | +0.217 [+0.125, +0.317] | +0.492 [+0.358, +0.625] | +0.908 [+0.808, +0.983] | +0.975 [+0.950, +1.000] | +0.275 [+0.175, +0.383] | +0.692 [+0.575, +0.800] | +0.758 [+0.667, +0.850] |
| r=16 | +0.217 [+0.125, +0.317] | +0.475 [+0.358, +0.592] | +0.908 [+0.808, +0.975] | +0.967 [+0.933, +0.992] | +0.258 [+0.175, +0.350] | +0.692 [+0.583, +0.792] | +0.750 [+0.658, +0.833] |

## rounds_to_agreement

| deadline | unanimity | supermajority | majority | majority_no_veto | supermajority − unanimity | majority − unanimity | majority_no_veto − unanimity |
|---|---|---|---|---|---|---|---|
| r=4 | +4.962 [+4.864, +5.000] | +4.525 [+4.190, +4.833] | +2.706 [+2.279, +3.168] | +1.983 [+1.672, +2.322] | -0.409 [-0.810, +0.000] | -1.962 [-2.593, -1.300] | -2.808 [-3.471, -2.000] |
| r=16 | +17.000 [+17.000, +17.000] | +15.158 [+13.407, +16.492] | +6.110 [+4.214, +8.283] | +3.586 [+2.302, +5.184] | -4.238 [-7.722, -1.000] | -11.269 [-13.588, -7.579] | -14.077 [-15.559, -11.650] |

## normalized_primary

| deadline | unanimity | supermajority | majority | majority_no_veto | supermajority − unanimity | majority − unanimity | majority_no_veto − unanimity |
|---|---|---|---|---|---|---|---|
| r=4 | +0.188 [+0.104, +0.276] | +0.417 [+0.301, +0.535] | +0.707 [+0.612, +0.791] | +0.735 [+0.687, +0.781] | +0.230 [+0.140, +0.325] | +0.519 [+0.405, +0.624] | +0.547 [+0.457, +0.634] |
| r=16 | +0.186 [+0.108, +0.272] | +0.400 [+0.300, +0.504] | +0.724 [+0.624, +0.815] | +0.740 [+0.692, +0.786] | +0.214 [+0.146, +0.286] | +0.538 [+0.419, +0.642] | +0.554 [+0.459, +0.641] |

## normalized_primary_common

| deadline | unanimity | supermajority | majority | majority_no_veto | supermajority − unanimity | majority − unanimity | majority_no_veto − unanimity |
|---|---|---|---|---|---|---|---|
| r=4 | +0.188 [+0.104, +0.276] | +0.426 [+0.308, +0.546] | +0.723 [+0.626, +0.809] | +0.773 [+0.711, +0.838] | +0.239 [+0.148, +0.334] | +0.536 [+0.421, +0.641] | +0.585 [+0.483, +0.688] |
| r=16 | +0.186 [+0.108, +0.272] | +0.409 [+0.308, +0.514] | +0.741 [+0.639, +0.833] | +0.776 [+0.719, +0.833] | +0.223 [+0.154, +0.295] | +0.555 [+0.434, +0.660] | +0.591 [+0.484, +0.691] |

## usw

| deadline | unanimity | supermajority | majority | majority_no_veto | supermajority − unanimity | majority − unanimity | majority_no_veto − unanimity |
|---|---|---|---|---|---|---|---|
| r=4 | +43.933 [+23.808, +65.950] | +96.058 [+66.057, +127.684] | +155.758 [+130.450, +179.859] | +156.100 [+131.374, +177.725] | +52.125 [+31.100, +74.400] | +111.825 [+86.358, +136.135] | +112.167 [+88.275, +134.484] |
| r=16 | +44.125 [+22.675, +69.667] | +90.717 [+64.058, +119.559] | +159.683 [+133.450, +184.417] | +157.575 [+133.300, +178.450] | +46.592 [+30.741, +63.676] | +115.558 [+88.858, +140.642] | +113.450 [+88.483, +136.500] |

## nsw_geomean

| deadline | unanimity | supermajority | majority | majority_no_veto | supermajority − unanimity | majority − unanimity | majority_no_veto − unanimity |
|---|---|---|---|---|---|---|---|
| r=4 | +6.849 [+3.693, +10.360] | +7.945 [+4.325, +12.261] | +4.864 [+1.367, +9.155] | +3.114 [+0.732, +6.044] | +1.096 [-1.358, +3.836] | -1.985 [-6.890, +3.049] | -3.736 [-7.472, -0.012] |
| r=16 | +6.752 [+3.097, +11.183] | +5.533 [+2.765, +8.780] | +4.458 [+0.929, +8.795] | +2.450 [+0.168, +5.351] | -1.218 [-3.707, +0.887] | -2.294 [-7.677, +2.758] | -4.302 [-9.006, -0.181] |

## gini

| deadline | unanimity | supermajority | majority | majority_no_veto | supermajority − unanimity | majority − unanimity | majority_no_veto − unanimity |
|---|---|---|---|---|---|---|---|
| r=4 | +0.295 [+0.245, +0.345] | +0.465 [+0.389, +0.546] | +0.844 [+0.682, +1.036] | +0.863 [+0.742, +1.007] | +0.070 [-0.009, +0.140] | +0.344 [+0.190, +0.479] | +0.390 [+0.298, +0.477] |
| r=16 | +0.298 [+0.244, +0.368] | +0.512 [+0.433, +0.598] | +0.851 [+0.668, +1.080] | +0.828 [+0.722, +0.942] | +0.125 [+0.023, +0.238] | +0.390 [+0.268, +0.529] | +0.429 [+0.336, +0.522] |

## all_ir

| deadline | unanimity | supermajority | majority | majority_no_veto | supermajority − unanimity | majority − unanimity | majority_no_veto − unanimity |
|---|---|---|---|---|---|---|---|
| r=4 | +0.217 [+0.125, +0.317] | +0.250 [+0.158, +0.350] | +0.183 [+0.083, +0.300] | +0.125 [+0.050, +0.217] | +0.033 [-0.042, +0.100] | -0.033 [-0.167, +0.100] | -0.092 [-0.208, +0.025] |
| r=16 | +0.217 [+0.125, +0.317] | +0.183 [+0.108, +0.258] | +0.175 [+0.075, +0.292] | +0.117 [+0.042, +0.208] | -0.033 [-0.100, +0.033] | -0.042 [-0.158, +0.083] | -0.100 [-0.200, +0.008] |

## n_ir_violations

| deadline | unanimity | supermajority | majority | majority_no_veto | supermajority − unanimity | majority − unanimity | majority_no_veto − unanimity |
|---|---|---|---|---|---|---|---|
| r=4 | +0.000 [+0.000, +0.000] | +0.242 [+0.142, +0.358] | +1.108 [+0.858, +1.342] | +1.217 [+1.033, +1.400] | +0.242 [+0.142, +0.358] | +1.108 [+0.858, +1.342] | +1.217 [+1.033, +1.400] |
| r=16 | +0.000 [+0.000, +0.000] | +0.292 [+0.200, +0.383] | +1.150 [+0.883, +1.408] | +1.225 [+1.042, +1.408] | +0.292 [+0.200, +0.383] | +1.150 [+0.883, +1.408] | +1.225 [+1.042, +1.408] |

## belief_auc_accept_set_f1

| deadline | unanimity | supermajority | majority | majority_no_veto | supermajority − unanimity | majority − unanimity | majority_no_veto − unanimity |
|---|---|---|---|---|---|---|---|
| r=4 | +0.209 [+0.190, +0.229] | +0.268 [+0.247, +0.289] | +0.234 [+0.215, +0.254] | +0.220 [+0.200, +0.241] | +0.059 [+0.049, +0.069] | +0.025 [+0.008, +0.042] | +0.011 [-0.006, +0.028] |
| r=16 | +0.240 [+0.216, +0.267] | +0.307 [+0.280, +0.334] | +0.251 [+0.229, +0.274] | +0.229 [+0.206, +0.252] | +0.066 [+0.050, +0.083] | +0.011 [-0.014, +0.034] | -0.012 [-0.036, +0.010] |

## belief_final_accept_set_f1

| deadline | unanimity | supermajority | majority | majority_no_veto | supermajority − unanimity | majority − unanimity | majority_no_veto − unanimity |
|---|---|---|---|---|---|---|---|
| r=4 | +0.222 [+0.201, +0.245] | +0.295 [+0.270, +0.321] | +0.257 [+0.234, +0.280] | +0.238 [+0.213, +0.263] | +0.073 [+0.059, +0.087] | +0.035 [+0.013, +0.056] | +0.015 [-0.006, +0.037] |
| r=16 | +0.245 [+0.220, +0.273] | +0.319 [+0.290, +0.349] | +0.267 [+0.243, +0.290] | +0.241 [+0.216, +0.267] | +0.074 [+0.056, +0.093] | +0.021 [-0.004, +0.046] | -0.005 [-0.031, +0.019] |
