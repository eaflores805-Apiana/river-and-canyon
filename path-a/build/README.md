# Path A — V3 Build Package

**Date:** 2026-06-17
**Author:** CS Engineer
**Authority:** TL / Manager ACTION 2026-06-17 ("Begin V3 Build Open Slots") — **AUTHORIZED — build effort only**.
**Status:** Build complete. Conformance: **8/8 items PASS inspector C1–C9 in REAL-RUN mode** under v0.4-pinned inspector (`cb4b0b60…`) and constants (`1d761c3d…`). Ready for Senior verification.

---

## What this package realizes

The four open slots from `PREREGISTRATION-PATH-A-CONSTRUCTIBILITY-v0.3` §"Open slots still requiring CS realization" (carried unchanged in v0.4):

| Open slot | File | Status |
|---|---|---|
| 1. Item generator + seed | `v3_item_generator.py` + `v3_seed_plan.md` | realized |
| 2. Concrete token pool | `v3_token_pool.md` (constructive scheme; implemented in generator) | realized |
| 3. Direct-query filler realization | `v3_direct_query_filler.md` (5 length-matched templates, per-seed rotation; implemented in generator) | realized |
| 4. Relation-balancing realization | `v3_relation_balance.md` (frequency/order/position balanced; implemented in generator) | realized |
| 5. Conformance-checkable build artifacts | `v3_conformance_runner.py` + `conformance_summary.json` + `conformance/item_*_inspection.json` | realized; **8/8 PASS** |

## Package layout

```text
path-a/build/
├── README.md                          ← this file
├── v3_item_generator.py               ← generator code (Python; deterministic)
├── v3_conformance_runner.py           ← drives inspector against every generated item
├── v3_seed_plan.md                    ← seed → (item_index, position) mapping; n=96 scaling note
├── v3_token_pool.md                   ← per-item prefix scheme + invariants
├── v3_direct_query_filler.md          ← E5 filler templates + length-matching
├── v3_relation_balance.md             ← E8 frequency/order/position balance
├── items/
│   ├── item_001.json   …   item_008.json     ← 8 generated V3 specs (demonstration batch)
├── conformance/
│   ├── item_001_inspection.json   …   item_008_inspection.json
└── conformance_summary.json           ← aggregate result (n_pass / n_reject / all_pass)
```

## Conformance result (full summary in `conformance_summary.json`)

```text
inspector_path  path-a/inspector/inspector.py
inspector sha   cb4b0b60bd6dc2b5f1d7ee6c4eaf3fc274cbb10254b5a548c637c84ca27348a9
constants sha   1d761c3d1c56e7aca9ef32a3f8b05c310e2aa5f35c6d91e67fd7fd81468915dd
                (matches PREREGISTRATION-PATH-A-CONSTRUCTIBILITY-v0.4 of-record pins)

items processed 8
disposition     PASS for every item (8/8)
checks          9/9 pass per item (C1–C9)
mode            real-run for every item
                (verified: no item has _fixture_mode or _sweep_mode;
                 every item's params.{k,D,p,m,margin} matches Manager lock)
expected_mode   real-run (no _fixture_mode, no _sweep_mode)
all_pass        true
```

## Manager-locked values honored

The generator's hard-coded constants match the v0.4-of-record binding's locked values:

```text
LOCKED_K       = 5   (clutter chains; constants.K_DECOY_CHAINS)
LOCKED_D       = 5   (same-depth competitors; constants.D_DEPTH_COMPETITORS)
LOCKED_P       = 5   (C* position slots; constants.P_POSITION_SLOTS)
LOCKED_M       = 10  (equal-salience candidates min; constants.M_MIN_EQUAL_SALIENCE_CANDIDATES)
LOCKED_MARGIN  = 0.25 (constants.MARGIN)
```

The inspector C9 is the enforcer; the generator's constants are a redundant sanity guard. Drift between the two would surface as C9 REJECT on every item at conformance — not as silent divergence.

## Determinism

The generator is **fully deterministic** under fixed inputs (item count). Re-running:

```bash
python3 path-a/build/v3_item_generator.py --out-dir <tmp> --count 8
```

produces byte-identical output to the items in `items/` (verified this turn: sha256 match across two independent runs into separate directories).

## Reproducing the build from scratch

```bash
# from repo root:
python3 path-a/build/v3_item_generator.py \
    --out-dir path-a/build/items --count 8

python3 path-a/build/v3_conformance_runner.py \
    --items-dir      path-a/build/items \
    --results-dir    path-a/build/conformance \
    --inspector-path path-a/inspector/inspector.py \
    --summary-path   path-a/build/conformance_summary.json
```

## Scaling from demonstration batch to n=96

The build ships 8 items as a demonstration batch — enough to:
- exercise every C* position slot (positions 1, 2, 3 are hit twice; 4 and 5 once)
- demonstrate per-position seed variation (items 1 + 6 share position 1, different seeds and filler forms)
- run all conformance checks against real generated output

Scaling to the locked n = 96 requires only `--count 96`. Per `v3_seed_plan.md`, every C* position is covered 19 or 20 times under that count. Materializing n = 96 here would extend beyond build-realization into run-preparation; the demonstration batch is the deliberate scope for this ACTION.

## Unresolved feasibility blockers

```text
NONE identified.

All eight items PASS C1–C9 in real-run mode under the v0.4-pinned
inspector. The construction (V3 same-depth-competitor, foreclose-all
standard) is buildable at the schema level under the locked Manager
values, with deterministic generation, length-matched neutral filler,
and balanced relations.

The empirical question — does V3 elicit composition-consistent behavior
above the success threshold under FP16, on this model — remains open and
is the floor check's responsibility, not the build's.
```

## What this package does NOT do

This package is a **build artifact only**. It does not authorize, claim, or enable:

```text
- a model run / model execution / GPU work / inference of any kind
- floor-check execution (Senior drafts prereg AFTER this build's verification)
- prompt materialization for runtime (specs are schema-level; downstream
  realization layer is out of scope)
- compression / quantization / INT8 / INT4 / any stress rung
- Claim C activation
- Paper B activation
- capability claim or mechanism claim of any kind
```

The Path A FP16 K=5 FAIL remains closed and untouched. V3 conformance to the foreclose-all standard ≠ V3 certification; the floor check remains the empirical question.

## Ready-for-Senior-verification statement

```text
READY: YES.

The build package is complete, conformance-passing, deterministic, and
byte-identical-reproducible. Senior may verify from bytes by:
  (a) reading v3_item_generator.py and confirming the schema mapping
      matches PATH-A-CANDIDATE-CONSTRUCTION-DESIGN-v0.3 (§2 schema,
      §5 filler, §8 floor derivation) and constants.py (locked values)
  (b) running v3_conformance_runner.py against path-a/build/items/ and
      verifying 8/8 PASS, 9/9 checks per item, mode real-run
  (c) re-generating with the same args and confirming byte-identical
      output (determinism check)

After Senior verifies, the next step in the §4 route (per
PHILOSOPHY-DECISION-RECORD-PATH-A-GATE-STANDARD-v0.1) is for Senior to
draft the V3 floor-check pre-registration — a separately gated step
(SE drafts → CS feasibility → C5 claim-risk → TL approve → Manager
by-name run authorization).
```

---

— CS Engineer, 2026-06-17
