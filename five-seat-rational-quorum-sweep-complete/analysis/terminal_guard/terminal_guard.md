# Terminal-accept guard: exposure of the quorum sweep

A **violation** is a forced-final vote in which a seat rejected the offer under vote while its own TRUE surplus on that offer was >= 0 — the move the base terminal rule forbids. **Deals lost** corrects every violation to an Accept and re-applies that cell's own agreement rule (min_accept backers including every veto seat); an episode with no deal that would then have closed is a deal the guard cost. Rates are per episode, with 95% instance-clustered intervals.

The last column drops the essential-party requirement from the replay. It is NOT this sweep's rule — it is what `--quorum majority_no_veto` would enforce — and it is here because a zero cost that rests on the veto is a fact about this grid rather than about the defect.

| cell | k | episodes at a terminal vote | violating votes | episodes with a violation | deals lost | deals lost / episode | deals lost if veto dissolved |
|---|---:|---:|---:|---|---:|---|---:|
| all_rational__majority_r16 | 3 | 31 | 4 | 0.097 [0.000, 0.231] | 0 | 0.000 [0.000, 0.000] | 2 |
| all_rational__majority_r4 | 3 | 32 | 6 | 0.125 [0.000, 0.314] | 0 | 0.000 [0.000, 0.000] | 4 |
| all_rational__supermajority_r16 | 4 | 113 | 54 | 0.319 [0.231, 0.409] | 0 | 0.000 [0.000, 0.000] | 9 |
| all_rational__supermajority_r4 | 4 | 109 | 52 | 0.321 [0.217, 0.426] | 0 | 0.000 [0.000, 0.000] | 8 |
| all_rational__unanimity_r16 | 5 | 120 | 139 | 0.683 [0.592, 0.767] | 0 | 0.000 [0.000, 0.000] | 0 |
| all_rational__unanimity_r4 | 5 | 119 | 120 | 0.639 [0.550, 0.723] | 0 | 0.000 [0.000, 0.000] | 0 |
