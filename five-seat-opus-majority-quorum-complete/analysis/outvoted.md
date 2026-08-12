# Outvoted-seat endpoints under a k-of-n closure rule

A **quorum close** is a deal that passed without every seat's support; the **outvoted seat** is a seat absent from the closing offer's final support set. Every column below the deal rate is conditional on a quorum close and is undefined under unanimity, where none exist.

| arm | episodes | deals | quorum closes | outvoted below threshold | outvoted z | outvoted dissented (vs abstained) |
|---|---:|---:|---:|---:|---:|---:|
| all_llm | 120 | 115 | 0 | — | — | — |
| one_rational | 120 | 92 | 0 | — | — | — |
| all_llm_quorum_4 | 120 | 120 | 118 | 0.246 [0.134, 0.370] | 0.164 [0.108, 0.221] | 0.059 [0.017, 0.109] |
| one_rational_quorum_4 | 120 | 118 | 112 | 0.402 [0.276, 0.527] | 0.056 [-0.010, 0.122] | 0.054 [0.018, 0.091] |

## The treated seat's own behaviour

`reject share` is the share of the treated seat's committed actions that are rejections. It is the measure that survives the protocol change: under unanimity a dissent is what PREVENTS a close, so "rejected the closing offer" is structurally missing exactly where the behaviour occurred. If the reject share is unchanged while the table now closes over the seat, the majority rule removed the PRICE of dissent without changing the dissent. The accept share sits beside it because under unanimity a seat blocks just as effectively by never accepting as by rejecting — the veto is exercisable passively.

| arm | treated reject share | treated accept share | rejected the closing offer | treated seat outvoted | treated seat below threshold |
|---|---:|---:|---:|---:|---:|
| one_rational | 0.027 [0.015, 0.040] | 0.351 [0.312, 0.391] | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] |
| one_rational_quorum_4 | 0.000 [0.000, 0.000] | 0.313 [0.267, 0.358] | 0.000 [0.000, 0.000] | 0.542 [0.470, 0.615] | 0.203 [0.134, 0.271] |

## Support size of closing offers

| arm | 4 supporters | 5 supporters |
|---|---:|---:|
| all_llm | 0 | 115 |
| one_rational | 0 | 92 |
| all_llm_quorum_4 | 118 | 2 |
| one_rational_quorum_4 | 112 | 6 |
