# scorable_negotiation — `scorable_negotiation-moves_chat-704a21d7d6`

**model** one_rational · **arm** moves_chat · **instance** scorable_negotiation-L4-d49e5fe070 · **seed** 0 · **status** done
**protocol/scaffold** `{"cell": "five_seat_robustness__qwen_datacenter__one_rational", "fill_policy": "bayes-rational", "robustness_schema": "five-seat-robustness-cell-v1", "robustness_condition": "qwen_datacenter", "source_bank_position_schedule": "treated=(source_bank_position+2*episode_seed) mod 5", "framing": "datacenter", "framing_map": {"framing": "datacenter", "title": "Northgate data-centre siting agreement", "issue_names": ["Location", "Power supply", "Build schedule", "Hiring"], "option_labels": [["Anvil Ridge", "Dunlow Yard", "Kestrel Park", "Weir Flats"], ["on-site turbines", "solar with storage", "grid tie-in", "shared substation"], ["five years", "three years", "phased over eight years", "eighteen months"], ["apprenticeship programme", "union hall referral", "local hiring pact", "open recruitment"]], "party_roles": ["Anvil Ridge Landholding (the owner of record of the candidate parcels)", "Northgate Water Board (the utility that supplies cooling water)", "Electrical Workers' Union (the construction and maintenance workforce)", "Office of the County Executive (the county-level executive)", "Riverside Residents' Assembly (the neighbourhood association beside the candidate sites)"]}}`

## Game setup

**Issues:** Location (Anvil Ridge, Dunlow Yard, Kestrel Park, Weir Flats); Power supply (on-site turbines, solar with storage, grid tie-in, shared substation); Build schedule (five years, three years, phased over eight years, eighteen months); Hiring (apprenticeship programme, union hall referral, local hiring pact, open recruitment)

**Private score sheets (threshold):**

- **Anvil Ridge Landholding (the owner of record of the candidate parcels)** (τ=112): Location: Anvil Ridge=18, Dunlow Yard=37, Kestrel Park=55, Weir Flats=0; Power supply: on-site turbines=0, solar with storage=15, grid tie-in=30, shared substation=45; Build schedule: five years=0, three years=97, phased over eight years=65, eighteen months=32; Hiring: apprenticeship programme=0, union hall referral=0, local hiring pact=0, open recruitment=0
- **Northgate Water Board (the utility that supplies cooling water)** (τ=93): Location: Anvil Ridge=18, Dunlow Yard=36, Kestrel Park=53, Weir Flats=0; Power supply: on-site turbines=0, solar with storage=9, grid tie-in=18, shared substation=27; Build schedule: five years=0, three years=0, phased over eight years=0, eighteen months=0; Hiring: apprenticeship programme=0, union hall referral=85, local hiring pact=57, open recruitment=28
- **Electrical Workers' Union (the construction and maintenance workforce)** (τ=51): Location: Anvil Ridge=37, Dunlow Yard=19, Kestrel Park=0, Weir Flats=56; Power supply: on-site turbines=0, solar with storage=11, grid tie-in=22, shared substation=32; Build schedule: five years=0, three years=0, phased over eight years=0, eighteen months=0; Hiring: apprenticeship programme=0, union hall referral=0, local hiring pact=0, open recruitment=0
- **Office of the County Executive (the county-level executive)** (τ=79): Location: Anvil Ridge=16, Dunlow Yard=32, Kestrel Park=48, Weir Flats=0; Power supply: on-site turbines=0, solar with storage=9, grid tie-in=17, shared substation=26; Build schedule: five years=69, three years=46, phased over eight years=23, eighteen months=0; Hiring: apprenticeship programme=0, union hall referral=0, local hiring pact=0, open recruitment=0
- **Riverside Residents' Assembly (the neighbourhood association beside the candidate sites)** (τ=129): Location: Anvil Ridge=61, Dunlow Yard=30, Kestrel Park=0, Weir Flats=91; Power supply: on-site turbines=0, solar with storage=17, grid tie-in=34, shared substation=51; Build schedule: five years=0, three years=0, phased over eight years=0, eighteen months=0; Hiring: apprenticeship programme=65, union hall referral=97, local hiring pact=32, open recruitment=0

## Turns

### [0] Avery — turn (round 1)
- **action:** PROPOSE {"Location": "Kestrel Park", "Power supply": "shared substation", "Build schedule": "three years", "Hiring": "open recruitment"}
- **message:** I propose Kestrel Park location, shared substation power, three-year build schedule, and open recruitment hiring.
- **scratchpad/reasoning:** Maximizing my points: Kestrel Park (55) + shared substation (45) + three-year schedule (97) = 197 > 112 threshold. Hiring defaults to 0.
- **oracle regret:** threshold=+0, acceptance=+0, bestresponse=+3.35

### [1] Blake — turn (round 1)
- **action:** ACCEPT P1
- **message:** P1 meets my threshold. I accept.
- **scratchpad/reasoning:** P1 scores 108 (above threshold). Accepting secures my support and moves the deal forward.
- **oracle regret:** threshold=+0, acceptance=+21.8, bestresponse=+0

### [2] Casey — turn (round 1)
- **action:** WALK
- **message:** P1 doesn't meet my threshold. I'm walking.
- **scratchpad/reasoning:** P1 scores 32, below my threshold. Must walk to avoid accepting a deal worse than no deal.
- **oracle regret:** threshold=+0, acceptance=+0, bestresponse=+0

## Outcome

- **no deal** (no_deal)
- **primary** 0.0 · **USW** 0.0 · **ESW** 0.0 · **NSW** 0.0 · **Gini** 0.0
- **per-party surplus:** [0.0, 0.0, 0.0, 0.0, 0.0]
- **parse errors:** syntax 0, legality 0, economic 0
