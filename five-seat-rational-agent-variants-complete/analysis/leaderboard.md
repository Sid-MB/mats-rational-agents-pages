<!-- [implement: pure-arm rounds sweep] 2026-08-17 — agent-variant design loop. -->
<!-- Reads the audit in ../research-notes/0057-bayesian-closure-audit.md; edits no frozen file. -->

# Agent-variant leaderboard — driving the private-information negotiator to 100% closure

## What this is, in one paragraph

**The setup.** Five automated negotiators must agree unanimously on one package out of 256 within four rounds. Each holds a private score sheet and a private walk-away threshold. The published Bayesian agent infers its counterparts from their offers; the omniscient reference is handed every sheet.

**The problem.** The published agent closes 0.180 of these games while the omniscient one closes 1.000 on the identical bank, so every failure is a *missed feasible* deal ([note 0043](../research-notes/0043-five-arm-fairness-basket-and-correct-walks.md)). [Note 0057](../research-notes/0057-bayesian-closure-audit.md) traced the cause: the agent's belief learns only from an opponent *conceding*, which happens under one time per seat per episode, so its posterior stays near-uniform, it never believes any package can pass, and it therefore proposes selfishly and never converges. The objective for this loop is deal rate with a target of **1.000** — a package sitting at every seat's exact walk-away value counts as a win.

**What we did.** Eleven designs, each a subclass of the frozen code (nothing under `libs/interlens` or the campaign runner is edited, because the rounds sweep executes from this same tree), scored on a fixed ten-instance subset x five seeds = 50 episodes. Two levers: give the agent **more signal** (fold in the public accept/reject votes it currently discards; concede on a clock; propose for the worst-off seat; re-table a live package at the final vote) or let it **share preferences outright** (publish the true sheet on the public message channel and read everyone else's).

**The result.** **Preference sharing reaches the target exactly: deal rate 1.000, zero individual-rationality violations, welfare 0.869 against the omniscient reference's 0.906.** Everything that avoids revelation falls well short — the best no-sharing design closes 0.400, a 2.2x improvement on the published 0.180 but not close to 1.0. The signal levers behave as note 0057 predicted in direction and magnitude: the vote channel alone moves 0.180 → 0.220, and conceding on a clock (the mechanical version of what the LLM arm does) is the strongest non-revelation lever at 0.400. The components do **not** compose additively — stacking the vote channel and final-offer support on top of conceding makes it *worse* (0.400 → 0.300).

**One-sentence version.** Letting the agents state their true preferences closes 100% of the games with no IR violations, while every design that keeps them guessing tops out at 0.400 — the inference problem, not the bargaining problem, is what was blocking closure.

## Leaderboard

50 episodes each (10 fixed instances x seeds 0-4), four rounds, unanimity, all-rational tables. `IRviol` is the fraction of episodes closing below any seat's own threshold and **must stay 0**. `IR-all props` is the audit's early tell — the fraction of tabled packages that clear *every* seat's threshold — at round 1 and at rounds 3+.

| # | variant | DEAL | score | USW | min seat | IRviol | close rnd | IR-all r1 | IR-all r3+ |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|
| — | **`oracle` (ceiling)** | **1.000** | **0.906** | 185.2 | 8.28 | 0.000 | 1.32 | 0.926 | 1.000 |
| 1 | **`declaring`** | **1.000** | 0.869 | 176.8 | 7.16 | 0.000 | 4.98 | 0.268 | 1.000 |
| 1 | **`declaring_egalitarian`** | **1.000** | 0.869 | 176.8 | 7.16 | 0.000 | 4.98 | 0.430 | 1.000 |
| 1 | **`declaring_conceding`** | **1.000** | 0.869 | 176.8 | 7.16 | 0.000 | 4.94 | 0.117 | 0.696 |
| 4 | `conceding_novotes` | 0.400 | 0.312 | 64.9 | 4.14 | 0.000 | 5.00 | 0.070 | 0.201 |
| 5 | `conceding` | 0.360 | 0.282 | 59.3 | 3.78 | 0.000 | 5.00 | 0.074 | 0.200 |
| 6 | `final_support` | 0.320 | 0.237 | 49.0 | 2.88 | 0.000 | 5.00 | 0.070 | 0.202 |
| 7 | `best_effort_nosharing` | 0.300 | 0.223 | 46.6 | 3.22 | 0.000 | 5.00 | 0.074 | 0.204 |
| 8 | `votes` | 0.220 | 0.132 | 29.6 | 2.46 | 0.000 | 5.00 | 0.136 | 0.201 |
| 9 | **`published` (reference)** | 0.180 | 0.144 | 30.9 | 2.12 | 0.000 | 4.98 | 0.070 | 0.129 |
| 9 | `terminal` | 0.180 | 0.144 | 30.9 | 2.12 | 0.000 | 4.98 | 0.070 | 0.129 |
| 9 | `egalitarian` | 0.180 | 0.112 | 25.1 | 1.74 | 0.000 | 4.64 | 0.188 | 0.212 |

**Zero IR violations in every design.** Nothing on this board buys closure by trampling a seat.

## Mechanism, one sentence each

- **`declaring` — 1.000.** Each seat publishes its true sheet once, on its first turn, as a structured block on the same public message channel the LLM arms talk on; every other seat parses the declarations out of its view and, once all five are in, plans on a full-information table — so the private-information agent *becomes* the omniscient agent without any decision rule changing.
- **`declaring_egalitarian` / `declaring_conceding` — 1.000.** Sharing plus a different proposal rule. Identical outcomes to plain `declaring`: once every sheet is known the composed policy converges on the same closing package regardless of how proposals are ranked, so the extra machinery is inert here (it does move the round-1 tell, 0.268 → 0.430).
- **`conceding_novotes` — 0.400.** Demand at least `(1 − t/T)` of your own attainable surplus and, subject to that floor, table whatever is best for the believed worst-off seat: the mechanical version of the LLM arm's "concede first, learn incidentally". Strongest non-revelation lever, and it needs no better beliefs at all.
- **`final_support` — 0.320.** At the forced-final proposal, re-table the most passable package already live instead of a fresh one. Targets note 0057's selection-side failure (37–42% of no-deals had a signable package on the table and voted on something else) but recovers only part of it.
- **`votes` — 0.220.** Fold every public accept/reject into the posterior via `BeliefState.observe_response`, the channel measured at 5.3–13.2x denser than concessions. Real but small: **+0.040** over published, at the bottom of note 0057's predicted 0.5–0.8 range, which that prediction now stands corrected on.
- **`terminal` — 0.180.** Restore the base-class terminal accept rule (accept anything at or above own threshold). Exactly 0 change, as note 0057 predicted: the guard it removes only ever fires after a legitimate refusal has already killed the package. Kept in every stack for correctness.
- **`egalitarian` — 0.180.** Rank proposals by the believed worst-off seat. No gain alone — with a near-uniform posterior the "believed worst-off seat" is noise, which is exactly why it only works once beliefs are real (`declaring_egalitarian`) or once a concession floor supplies the structure (`conceding_novotes`).

## Three things worth flagging

**Revelation is a design choice, not an equilibrium claim.** These agents are cooperative by construction: `declaring` emits numbers read straight off its own sheet, and the readers trust them. Nothing here shows a self-interested agent *would* reveal truthfully, or that truthful revelation survives an incentive to misreport — a seat that overstates its threshold would be handed a larger slice by these readers. Robustness to strategic misreporting is future work and is **not** claimed by this loop.

**The components do not compose.** `conceding` (0.400) gets *worse* when the vote channel is added (0.360) and worse again with final-support stacked on (0.300). Each addition perturbs the concession path that was doing the work. Take the no-revelation number as 0.400 from the single best lever, not from a stack.

**Sharing closes everything but closes it late.** `declaring` agrees at round 4.98 against the oracle's 1.32, and scores 0.869 against 0.906. Declarations only complete after round 1, and the composed full-information policy still runs its optimal-stopping holdout to the deadline. The remaining 0.037 of welfare is a *timing* gap, not a closure gap; closing it would mean declaring before the first proposal or shortening the holdout.

## What should graduate

**`declaring` to a full-bank 120-episode confirmation** (24 instances x 5 seeds, four rounds), against the published `all_rational` cell and the `all_oracle` ceiling on the same bank. It is the only design that hits the target, it is the simplest of the three that do, and it carries zero IR violations. Report deal rate, normalized score, USW and min-seat surplus with instance-clustered intervals, and state the revelation caveat above in the same table.

Recommended second row: **`conceding_novotes`**, as the honest "how far can you get *without* revelation" comparator. The scientific content of this loop is the contrast between the two — 1.000 with sharing against 0.400 without — and the confirmation should carry both.

## Reproduce

```
uv run python -m agent_variants.bench --variant published oracle
uv run python -m agent_variants.bench --variant declaring declaring_egalitarian declaring_conceding
uv run python -m agent_variants.bench --variant votes terminal egalitarian conceding conceding_novotes
uv run python -m agent_variants.bench --variant final_support best_effort_nosharing
uv run python -m agent_variants.bench --variant declaring --transcripts     # winner, transcripts saved
```

**Subset** (frozen on first run, never re-chosen): [`subset.json`](subset.json) — 10 instances from [`instances_five_seat_private_v2/`](../instances_five_seat_private_v2/), sorted by `(level, instance_id)` and taken round-robin across levels so L0–L4 are all represented. **Code:** [`bench.py`](bench.py), [`variants.py`](variants.py). **Transcripts:** `/nlp/scr/siddharth/ii_mats/transcripts/rational_agent_variants/<variant>/` (standing convention; override with `$VARIANT_TRANSCRIPTS`). **Raw aggregate rows:** written by `--out`.

**Frozen-file rule observed.** Every variant subclasses `BayesianRationalPolicy` / `PolicyParticipant` / `SeedAwareMixin` from the frozen tree. No file under `libs/interlens/`, and no campaign runner, was edited — the rounds sweep was executing from this working tree throughout. No variant required an edit to a frozen file.
