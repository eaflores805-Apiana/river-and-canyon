# V3 Seed Plan — open-slot realization (1 of 5)

**Date:** 2026-06-17
**Author:** CS Engineer
**Scope:** Build-realization only. Authority: TL/Manager ACTION 2026-06-17 ("Begin V3 Build Open Slots"). Does not authorize a model run.

---

## The mapping (one rule)

```text
for each item_index N in 1..n:
    c_star_position(N) = ((N - 1) mod p) + 1
    seed(N)            = N
    direct_query_filler_form(N) = _FILLER_FORMS[N mod len(_FILLER_FORMS)]
    construction_id(N) = f"path_a_v3_item_{N:03d}_pos{position}_seed{seed:03d}_v0.1"
```

`p = 5` (Manager-locked), so positions cycle uniformly through `{1, 2, 3, 4, 5}`. Implemented at `v3_item_generator.py:slot_for_index()` and `seed_for_index()`.

## Why this rule

```text
- Determinism: byte-identical reproduction at the same (N, position, seed)
  tuple. No clock, no RNG state, no environment dependence.
- Uniform position coverage: at n = 96, each of the p = 5 positions is
  represented either floor(96/5) = 19 or ceil(96/5) = 20 times. Specifically:
    position 1 → items {1, 6, 11, 16, 21, 26, 31, 36, 41, 46, 51, 56, 61,
                        66, 71, 76, 81, 86, 91, 96}  (20 items)
    position 2 → items 2, 7, 12, …, 92               (19 items)
    position 3 → items 3, 8, 13, …, 93               (19 items)
    position 4 → items 4, 9, 14, …, 94               (19 items)
    position 5 → items 5, 10, 15, …, 95              (19 items)
  Layout-diagnostic per-position breakdowns (per prereg v0.3 §12) remain
  comparable across positions because the per-position n is balanced
  within ±1.
- Seed-distinct per item: each item gets its own seed even at the same
  position, so position rotation is independent from seed rotation; this
  matters because seed selects the direct_query filler form (§5 of design
  v0.3, E5 filler realization).
- Token independence across items: the per-item prefix `i{N:03d}_`
  (v3_item_generator.py:_item_prefix) guarantees cross-item token
  collisions are impossible by construction. Item N's tokens cannot alias
  item M's, regardless of seed.
```

## Scaling from the demonstration batch to n=96

The demonstration batch this build ships contains **8 items** (N = 1..8). The seed plan above applies unchanged to N = 1..96 (and beyond). To materialize the locked n = 96, downstream of a Manager by-name run authorization, run:

```bash
python3 path-a/build/v3_item_generator.py --out-dir <run_items_dir> --count 96
```

The generator imports the Manager-locked values from its own module constants (`LOCKED_K=5, LOCKED_D=5, LOCKED_P=5, LOCKED_M=10, LOCKED_MARGIN=0.25`). The inspector C9 binding is the enforcer; the generator's constants are a redundant sanity guard. Drift between the two would be caught at conformance (every item would REJECT on C9) before any run could start.

## What this plan does NOT do

```text
- Does NOT authorize a run. The generator outputs JSON specs; a model run
  requires (a) Manager by-name authorization, (b) a downstream prompt-
  materialization layer that consumes specs and emits the four contexts'
  prompts, (c) a model load + execution step. None of those are in this
  build, and none are in scope for this ACTION.
- Does NOT lock the generator. The seed plan is a build artifact, not a
  Manager-lock. The locked artifacts are the inspector + constants
  (per v0.4 binding). If the generator drifts, conformance catches it.
- Does NOT pre-materialize prompt strings. Specs are schema-level JSON.
  Composing them into prompts (the four contexts) is a separate downstream
  realization step, gated on Manager by-name authorization.
```

— CS Engineer, 2026-06-17
