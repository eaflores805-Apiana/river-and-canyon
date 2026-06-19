# V3 COMPOSITE-GATE TOOLING VERIFICATION — SE RETURN

**To:** Team Lead **Cc:** CS Engineer, C5, Manager **From:** Senior Engineer **Re:** TL ACTION 2026-06-18 (Verify V3 Composite-Gate Tooling)
**E. A. Flores**, Apiana AI, Inc. — June 18, 2026 · *Verification only (YELLOW). No run. Certifies nothing.*

## VERDICT: **PASS** — V3 composite-gate tooling verified from bytes.

All three new tools implement the v0.2 prereg contract; the wrapper produces the fresh disjoint set without touching the underlying generator; the four decision branches reproduce; everything is deterministic and model-free. The MAX_DELTA=8 brittleness I flagged during floor-check tooling verification is now **structurally guarded** by the wrapper's ≤999 enforcement (§T4).

## 1. Files inspected + hashes recomputed (clone at HEAD `8b4a41b8`)

```text
v3_composite_gate_item_generator.py   cc07e5a2…   matches CS-reported  ✓
v3_composite_gate_analyzer.py         3a3e954e…   matches CS-reported  ✓
v3_composite_error_logger.py          2ed46628…   matches CS-reported  ✓
v3_item_generator.py (underlying)     6a2ceee1…   UNCHANGED, byte-identical pre/post  ✓ (task 2)
```

## 2. Commands run

```text
git fetch && checkout 8b4a41b8
python3 v3_composite_gate_item_generator.py --out-dir … --start-index 97 --count 96   (+ start-index 1; + twice for determinism; + start-index 950 for the ≤999 guard test)
python3 v3_prompt_realizer.py / v3_prompt_conformance_checker.py  on the fresh 097..192 set
python3 v3_composite_error_logger.py + v3_composite_gate_analyzer.py  on 4 synthetic branch cases (+ twice for determinism)
sha256sum ; diff ; field-level JSON compare ; import scan
```

## 3. Task-by-task

```text
(1) WRAPPER APPROACH — VERIFIED. v3_composite_gate_item_generator.py imports `v3_item_generator as _gen`
    and calls _gen.generate_item(n, position, seed) directly. It does NOT reimplement or modify the
    generator. Pure function of (--start-index, --count).

(2) UNDERLYING GENERATOR UNCHANGED — VERIFIED. v3_item_generator.py = 6a2ceee1…, byte-identical.

(3) FRESH DISJOINTNESS — VERIFIED. Generated 097..192 (96 items) and regenerated 001..096; the two sets
    are FULLY byte-distinct (0 byte-overlapping items) with disjoint index sets. This gives the provable
    independence the v0.2 lock-before-look design requires (the fresh composite is unseen).

(4) TOKEN-WIDTH / MAX_DELTA — VERIFIED. 097..192 keep 3-digit prefixes (i{NNN}_). Prompt realization +
    conformance on the fresh set = 96/96 PASS, char_delta min=max=8 (MAX_DELTA=8 holds at the structural
    minimum, as on the floor-check set). The wrapper ENFORCES ≤999: a range whose end-index exceeds 999 is
    REJECTED with a message citing the MAX_DELTA=8 token-width binding (behaviorally tested with
    --start-index 950 --count 96 -> rejected). The brittleness I flagged earlier is now structurally guarded.

(5) COMPOSITE-GATE ANALYZER — VERIFIED. Computes composite-correct rate + Wilson 95% CI; the 0.75 primary
    reliability gate and the 0.45 not-shortcut floor (= F + margin) are SEPARATE lower-Wilson rules,
    reported separately; re-confirms fresh preconditions (hop2/hop1 lower Wilson > 0.75, dq ≤ 19); applies
    the v0.2 §8 invalidator rules; emits the four-branch decision; emits GATE-CLEARED-THIS-RUN at most
    (FINAL is a separate decision, per v0.2 §7). No model imports.

(6) ERROR LOGGER — VERIFIED. Classifies the landed output token as correct_chain_wrong_depth /
    decoy_chain_depth_2 / competitor_or_other, and co-occurrence as inherited_component_failure /
    composition_specific / composition_specific_success (the PATHOLOGICAL flag = composite success while
    hop2 failed). Explicitly labeled positional/structural — NOT mechanism. No model imports.

(7) BRANCH COVERAGE — REPRODUCED (synthetic inputs, error-logger -> analyzer):
      all correct (comp 90/96, hop2 96)            -> GATE-CLEARED-THIS-RUN
      composite 70/96 with components OK           -> COMPOSITE-DOES-NOT-CLEAR-THIS-RUN
      hop2 60/96 below floor                       -> PRECONDITION-FAIL
      5 pathological composite-success/hop2-fail   -> CONSTRUCT-FAIL
    All four match the v0.2 §7/§8 contract.

(8) DETERMINISM — VERIFIED. Wrapper (097..192 regenerated twice), analyzer, and error logger are each
    BYTE-IDENTICAL across two runs on fixed inputs.

(9) IMPORT / EXECUTION BOUNDARY — VERIFIED. No torch / mlx / transformers / openai / anthropic / requests /
    urllib / http / subprocess in any of the three tools. No model execution, no prompt execution, no run.
    (The tools generate specs, score outputs, and classify — none invokes a model.)
```

## 4. Fresh-seed / disjointness verification (summary)

```text
floor-check seeds 001..096 (byte-confirmed earlier) vs composite-gate seeds 097..192: index sets disjoint;
item bytes 0/96 overlapping. Provable independence established. Indices ≤999 (wrapper-enforced) -> MAX_DELTA=8 valid.
```

## 5. MAX_DELTA verification (summary)

```text
char_delta on the fresh 097..192 set = 8 for every item (min=max=8); conformance 96/96. The ≤8 gate holds at
its structural minimum, and the wrapper's ≤999 guard prevents any index range that would break it. The
standing lock-scope caveat (the ≤8 tolerance is bound to the 3-digit token scheme) is now enforced in code.
```

## 6. Recommended next route

```text
PASS -> proceed per the v0.2 routing:
  CS files v0.2 to a readable in-review path -> C5 reviews actual bytes -> CS feasibility review -> TL
  approval consideration -> Manager by-name RUN authorization (only if approved) -> CS execution -> SE verification.
The tooling is verified; the fresh composite-gate run remains gated and is NOT authorized by this verification.
```

## 7. Boundary

```text
- Verification only. No fresh N=96 run, no prompt generation for execution, no model run, no compression,
  no INT8/INT4, no Claim C, no Paper B, no certification claim, no capability claim, no mechanism claim.
- The Path A FP16 K=5 FAIL remains closed and untouched. SE verifies; SE authorizes nothing.
```

— Senior Engineer (composite-gate tooling verification; PASS)
