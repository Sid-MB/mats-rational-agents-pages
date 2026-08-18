# Outvoted-seat endpoints under a k-of-n closure rule

A **quorum close** is a deal that passed without every seat's support; the **outvoted seat** is a seat absent from the closing offer's final support set. Every column below the deal rate is conditional on a quorum close and is undefined under unanimity, where none exist.

| arm | episodes | deals | quorum closes | outvoted below threshold | outvoted z | outvoted dissented (vs abstained) |
|---|---:|---:|---:|---:|---:|---:|
| all_rational__unanimity_r4 | 120 | 26 | 0 | — | — | — |
| all_rational__unanimity_r16 | 120 | 26 | 0 | — | — | — |
| all_rational__supermajority_r4 | 120 | 59 | 53 | 0.547 [0.370, 0.712] | 0.113 [-0.044, 0.279] | 0.396 [0.275, 0.510] |
| all_rational__supermajority_r16 | 120 | 57 | 54 | 0.648 [0.534, 0.759] | -0.014 [-0.134, 0.106] | 0.537 [0.400, 0.667] |
| all_rational__majority_r4 | 120 | 109 | 107 | 0.654 [0.537, 0.761] | -0.083 [-0.178, 0.017] | 0.065 [0.019, 0.123] |
| all_rational__majority_r16 | 120 | 109 | 106 | 0.675 [0.544, 0.793] | -0.104 [-0.202, -0.002] | 0.071 [0.028, 0.121] |

## Support size of closing offers

| arm | 3 supporters | 4 supporters | 5 supporters |
|---|---:|---:|---:|
| all_rational__unanimity_r4 | 0 | 0 | 26 |
| all_rational__unanimity_r16 | 0 | 0 | 26 |
| all_rational__supermajority_r4 | 0 | 53 | 6 |
| all_rational__supermajority_r16 | 0 | 54 | 3 |
| all_rational__majority_r4 | 93 | 14 | 2 |
| all_rational__majority_r16 | 93 | 13 | 3 |
