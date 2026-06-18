# CS FINAL FEASIBILITY RE-REVIEW — V3 Composite Gate Package (Prereg v0.2 + Verified Tooling)

**Date:** 2026-06-18
**From:** CS Engineer
**To:** Team Lead; Cc: Senior Engineer, C5, Manager
**Re:** TL ACTION 2026-06-18 — "Final Feasibility Re-Review — V3 Composite Gate Tooling Verified"
**Status:** **PASS — executable and mechanically lockable as written, with the existing MAX_DELTA caveat carried forward**

---

## Record status

```text
verdict                  PASS — executable and mechanically lockable as written
caveat (carried)         MAX_DELTA = 8 ↔ current token-width / Manager-values /
                          relation-naming scheme (recorded at floor-check approval;
                          carried verbatim — no new caveat introduced)
review object            v0.2 prereg (df26dc65…) + 3 verified composite-gate tools +
                          UNCHANGED v0.2 §T-cited reused tools + current inspector/constants
authority                TL ACTION 2026-06-18 (final feasibility re-review only)
predecessor CS verdicts  v0.1 HOLD (E1 fresh-seed) → v0.2 PASS-with-notes (generator
                          patch routed as tooling-build deliverable) → tooling built
                          (cc07e5a2/3a3e954e/2ed46628) → SE tooling PASS → THIS
                          final feasibility verdict
C5 lane                  v0.1 + v0.2 ARTIFACT-ACCESS HOLDs; both now byte-accessible
                          since the prior CS sweep pushed v0.2 to origin/main
ready for approval       YES, contingent on TL recording the MAX_DELTA caveat at the
                          §T lock (same caveat that's already recorded for the
                          floor-check tooling per
                          governance/2026-06-18_v3-floor-check-final-feasibility-
                          review/CS-FINAL-FEASIBILITY-REVIEW-2026-06-18.md §2)
```

---

## 1. The eight required checks

### Check 1 — Fresh materialization 097..192 is now mechanically executable

**YES.** Live re-verified this turn:

```text
$ python3 path-a/build/v3_composite_gate_item_generator.py \
    --out-dir /tmp/v3cg_final/items --start-index 97 --count 96
wrote 96 items to /tmp/v3cg_final/items (indices 97..192)

  realizer on 097..192:
    items: 96
    gate-pass: 96/96
    max char_delta: 8
    all_gate_pass: True
```

96 spec JSONs produced at indices 097..192, deterministic, byte-identical re-runs across two independent invocations (re-verified in the previous tooling-build smoke test). The wrapper's ≤999 invariant enforces v0.2 §4's token-width constraint by hard-cap.

### Check 2 — Disjointness from floor-check 001..096 enforceable and byte-checkable

**YES — provable AND byte-verified.**

```text
Live byte check (re-run this turn):
  diff /tmp/v3cg_final/items/item_097.json
       experiments/2026-06-18_v3-floor-check-run/items/item_007.json
  → byte-distinct (different per-item prefix i097_ vs i007_)

Live token-set intersection check:
  shared role tokens between item_097 and item_007: 0  (none)

Provable: the per-item prefix scheme `i{N:03d}_` is injective on N;
  for any N ∈ {097..192} and M ∈ {001..096}, "i{N:03d}_" ≠ "i{M:03d}_",
  so the role-token namespaces are mechanically disjoint. (Already
  established in v3_token_pool.md §3 disjointness proof; re-confirmed
  empirically on the wrapped items here.)
```

### Check 3 — MAX_DELTA = 8 remains valid under 097..192

**YES — preserved + verified.**

```text
Live verification on the wrapped {097..192} batch:
  v3_prompt_realizer.py: items 96, gate-pass 96/96, max_delta 8, min 8
  v3_prompt_conformance_checker.py: items 96, pass 96/96, §9(vi) gate PASS

Mechanical reasoning:
  Max index 192 → "i192_" prefix (5 chars; same as "i007_", "i096_")
  Role-token widths unchanged
  Wrapper enforces ≤999 invariant by hard-cap (exit 2 with precise error
    message if violated)

THE MAX_DELTA = 8 CAVEAT IS NOT REOPENED by the {097..192} range — this is
exactly the property the caveat was crafted to preserve (any change to
token-width / Manager-values / relation-naming reopens conformance; the
{097..192} change touches NONE of these). No new caveat introduced.
```

### Check 4 — Composite-gate analyzer implements v0.2 §7/§8 branch logic

**YES — verified by spec mapping AND live re-run.**

```text
Spec mapping (v0.2 §7 conditions → analyzer):
  (a) composite-correct lower Wilson > 0.75   →  analyzer cond_a
       COMPOSITE_PRIMARY_GATE = 0.75 hard-coded
  (b) composite-correct lower Wilson > 0.45   →  analyzer cond_b
       COMPOSITE_FLOOR_GATE = 0.45 hard-coded (= F + margin = 0.20 + 0.25)
  (c) preconditions hold (hop2, hop1, dq)     →  analyzer cond_c_{hop2, hop1, dq}
       HOP_FLOOR = 0.75 (strict Wilson lower)
       DQ_POINT_CEILING_COUNT = 19
  (d) construct clean (C1-C9 + conformance +
       invalidated)                            →  analyzer cond_d_{admissibility,
                                                                    conformance,
                                                                    invalidated}
       INVALIDATED_THRESHOLD = 10 (< threshold → tolerated)
  (e) error-structure non-pathological         →  analyzer cond_e
       reads error_log["pathological_error_structure"] from the error logger

Spec mapping (v0.2 §8 branches → analyzer 3-way switch):
  GATE-CLEARED-THIS-RUN              all of (a)-(e) pass
  COMPOSITE-DOES-NOT-CLEAR-THIS-RUN  (c)+(d)+(e) hold; (a) and/or (b) fail
                                     sub-message recorded if 0.45 < lo ≤ 0.75
  PRECONDITION-FAIL                  (c) fails
  CONSTRUCT-FAIL                     (d) or (e) fails (priority: precondition first)

Live re-run on committed build_verification/composite_gate/test_a/ this turn:
  branch:               GATE-CLEARED-THIS-RUN
  n_total / n_included: 96 / 96
  composite k/n:        96 / 96  Wilson lower 0.9615  primary 0.75  floor 0.45
  re-run vs committed:  BYTE-IDENTICAL decision JSON
                        (sha unchanged; determinism PASS)
```

All four §8 branches were exercised in the tooling-build's build_verification/test_{a,b,c,d}/ run. CS re-verified test_a + test_d this turn; test_b + test_c remain on origin/main at the recorded sha and were live-verified during the tooling-build smoke tests.

### Check 5 — Error logger implements v0.2 §9 same-error / wrong-address logging

**YES — verified by spec mapping AND live re-run.**

```text
Spec mapping (v0.2 §9 → logger):
  WHERE the output token lands:
    correct_chain_wrong_depth     predicted ∈ {target.B, target.T}
    decoy_chain_depth_2            predicted ∈ {d.answer for d in decoy_chains}
    competitor_or_other            otherwise
  CO-OCCURRENCE with hop2:
    inherited_component_failure    composite=F, hop2=F
    composition_specific           composite=F, hop2=T
    composition_specific_success   composite=T, hop2=F (PATHOLOGICAL signal)
    fully_correct                  composite=T, hop2=T

Pathological-error-structure flag (v0.2 §7e):
  pathological IFF composition_specific_success_count > 0
  (strict mechanical interpretation: even one item where composite "succeeds"
   without component success indicates the output may not be traceable through
   traversal — a coincidence signal that would invalidate the "success via
   correct chain under controls" reading in v0.2 §3)

Live re-run on committed build_verification/composite_gate/test_d/ this turn:
  items:                                  96
  composite match:                        96
  composition_specific_success count:     2
  pathological_error_structure:           True
  landed token distribution:              {'correct': 96}

  (the 2 pathological cases: item explicitly synthesized at the 50th index
   plus the natural case where composite=96/96 but hop2=95/96 → item 96 has
   composite=T but hop2=F. The logger correctly identifies both.)

  re-run vs committed:  BYTE-IDENTICAL error log JSON
                        (sha unchanged; determinism PASS)
```

### Check 6 — Reused tools UNCHANGED where prereg says reused unchanged

**YES — re-verified live this turn.** All six v0.2 §T-cited reused-tool digests exact:

```text
v0.2 §T cites                      live shasum 2026-06-18                          status
6a2ceee1...   v3_item_generator    6a2ceee15442ebbd1f6cc4bbbd14a76d1264af9904ad3e5d6062c1554f530c53   ✓ MATCH
fb561fdc...   v3_prompt_realizer   fb561fdc526115da94c6137b739e8bb3b6adf30825d83f864cda713bc0750909   ✓ MATCH
b8afa3f8...   v3_prompt_conformance b8afa3f89dd7f375058500820bdf2bf58a46384d2283c8f2a31f1b8c92ad2b82  ✓ MATCH
bc2020c2...   v3_neutral_token_pool bc2020c2c4e1293f62c9f83a9b24a61f98c1ede35d5a071ee8cfd72a316ab0d9   ✓ MATCH
cb4b0b60...   inspector.py         cb4b0b60bd6dc2b5f1d7ee6c4eaf3fc274cbb10254b5a548c637c84ca27348a9   ✓ MATCH
1d761c3d...   constants.py         1d761c3d1c56e7aca9ef32a3f8b05c310e2aa5f35c6d91e67fd7fd81468915dd   ✓ MATCH
```

Critically, `v3_item_generator.py` is **byte-identical** to what v0.2 §T cites — the wrapper approach preserved the underlying generator. v0.2 §T's "REUSED UNCHANGED" claim stays literally true (this was the primary reason TL preferred the wrapper over a patch).

### Check 7 — TL-approval-ready digests available and stable

**YES — three new tooling digests stable on origin/main.**

```text
v3_composite_gate_item_generator.py   cc07e5a2c49757e9171831af7944b5f7f8b1de235c7cb35cb18e48b06ce534a2
v3_composite_gate_analyzer.py          3a3e954e1988ec3331d3e405bf2cbd90eae11d132d6ae9276cba10e1ca7e7c5f
v3_composite_error_logger.py           2ed466281c949ca3a47843934c031b87e4d016b15d6d1db0ac83db6d4687c226
```

These three digests EXACTLY match the digests Senior verified and cited in the TL ACTION. They are the digests to be locked into v0.2 §T at TL approval, alongside the six unchanged-reused digests in Check 6.

### Check 8 — No hidden run / prompt / model / compression / materialization-for-execution

**CONFIRMED across all four surfaces:**

```text
Code surface (the 3 new tools):
  grep -lE "transformers|torch|mlx|openai|anthropic|httpx|requests.|urllib|socket"
    path-a/build/v3_composite_gate_item_generator.py
    path-a/build/v3_composite_gate_analyzer.py
    path-a/build/v3_composite_error_logger.py
  → zero matches. Only stdlib + the wrapper's in-build import of v3_item_generator
    (which is itself zero-model-imports).

Build surface (path-a/build/build_verification/composite_gate/):
  Contains: items_097_192 (96 specs), prompts (384 prompt files, demonstration
    artifacts), admissibility/realization/conformance summaries (build-only),
    test_{a,b,c,d}/ (synthetic scored sets for the 4-branch analyzer test).
  Does NOT contain: any run_record.json (no actual model run occurred), any
    .raw.json (no model output bytes), any reference to Qwen2.5/inference/
    compression.

Materialization surface:
  experiments/2026-06-18_v3-composite-gate-run/ (the production composite-gate
    run path) does NOT exist on disk. Confirmed: the only experiments dir is
    experiments/2026-06-18_v3-floor-check-run/ (the previously completed
    floor-check run). The fresh-N=96 composite-gate materialization for
    execution has NOT occurred and is correctly gated behind Manager by-name
    authorization per v0.2 §E.

Review surface (this memo):
  No code executed beyond the deterministic re-verification of the existing
  tooling (wrapper / realizer / checker / inspector / analyzer / error logger
  on the build_verification batch). No model loaded. No new fresh prompts
  generated for execution.

  All four surfaces are clean. No hidden execution.
```

---

## 2. Verdict — synthesis

```text
verdict                       PASS — executable and mechanically lockable as written
caveat (carried, not new)     MAX_DELTA = 8 binding to current scheme — same caveat
                               already recorded at the floor-check approval lock
                               (CS-FINAL-FEASIBILITY-REVIEW-2026-06-18.md §2).
                               No new caveat introduced.
all 8 required checks         PASS
   1. Fresh materialization 097..192 mechanically executable        ✓
   2. Disjointness from 001..096 enforceable and byte-checkable     ✓
   3. MAX_DELTA = 8 remains valid under 097..192                    ✓
   4. Analyzer implements v0.2 §7/§8 branch logic                   ✓
   5. Error logger implements v0.2 §9                               ✓
   6. Reused tools UNCHANGED at v0.2 §T-cited digests               ✓
   7. TL-approval-ready digests available and stable                ✓
   8. No hidden execution / materialization                         ✓

ready for TL approval         YES, with the MAX_DELTA caveat recorded at the
                               §T lock alongside the three new tooling digests.
ready for Manager run         pending TL approval. CS will NOT proceed to fresh
                               N=96 {097..192} materialization for execution
                               without explicit Manager by-name authorization.
```

---

## 3. What this PASS does NOT mean

```text
Does NOT authorize anything operational:
  no fresh N=96 run, no fresh materialization for execution, no prompt
  generation for execution, no compression, no certification, no Claim C,
  no Paper B, no capability claim, no mechanism claim.

Does NOT alter any C5-cleared claim boundary from v0.2:
  bounded validity language ("certify the V3 composite baseline as behavior
  consistent with two-hop composition under foreclose-all controls"), output
  token + cleared controls (no internal-path claim), seen floor-check
  composite barred from gate use, two separate lower-Wilson gates, GATE-
  CLEARED-THIS-RUN ≠ FINAL certification, strengthened forbidden interpretations
  (no seam/compression/capability/mechanism leakage).

Does NOT lock anything:
  the three new tooling digests are CS-produced and SE-verified; the lock
  itself is TL + Manager at the next gate. CS only attests the digests are
  accurate at HEAD 8b4a41b8...

Routing after this PASS:
  → TL approval consideration (with MAX_DELTA caveat recorded; new tooling
     digests locked at §T)
  → Manager by-name run authorization (only if approved — the fresh N=96
     {097..192} composite-gate run)
  → CS execution
  → SE verification
```

## 4. Clean-fetch confirmation

To be appended after the commit lands.

---

## Non-authorizations (carried forward, per TL ACTION boundary)

```text
- fresh N=96 run                              blocked
- prompt generation for execution             blocked
- model run                                   blocked
- compression / INT8 / INT4                   blocked
- Claim C, Paper B                            blocked
- certification claim                         blocked
- capability claim, mechanism claim           blocked
- candidate selection, threshold values, multi-model, Fork A reactivation,
  public benchmark packaging, artifact mutation, Paper 6, Paper 3 execution
  as experiment                               all carried per standing card

Protected surfaces:
- Paper 2 v1.0 tag (paper2-cells01-03-v1.0, 41c033fc…) +
  tagged manuscript blob                      never moved
- tier0-run/ directory                        sealed; no new files

The Path A FP16 K=5 FAIL remains closed and untouched by this review.
```

---

— CS Engineer, 2026-06-18
