# HOP1-STABILITY RUN — SE VERIFICATION RETURN (HOP1-STABLE-INADMISSIBLE)

**To:** Team Lead **Cc:** CS Engineer, C5, Manager **From:** Senior Engineer **Re:** SE verification of the Hop1 Stability Investigation run (final branch HOP1-STABLE-INADMISSIBLE)
**E. A. Flores**, Apiana AI, Inc. — June 19, 2026 · *Verification only. Certifies nothing, authorizes nothing.*

## VERDICT: **PASS** — Hop1 Stability result verified from bytes.

I re-ran the locked analyzer and reproduced a **byte-identical decision** (branch **HOP1-STABLE-INADMISSIBLE**); the F2-row watchpoint is resolved (all six rows present, F2 = 23/96); and I scrutinized the surprising hop1 collapse the way I scrutinize a perfect score — it is **honestly scored, real model behavior** (the raw output token is the emitted P token), not an artifact. So the result is a **valid** outcome.

## A. The six-block table (recomputed from raw scored files) + F2 confirmation

```text
 block    hop1        rate     hop1 Wilson lo   hop2
 F1      50/96      0.5208        0.4220        96/96
 F2      23/96      0.2396        0.1653        96/96   <-- F2 PRESENT (the pasted-table omission was cosmetic)
 F3      35/96      0.3646        0.2752        96/96
 F4      39/96      0.4062        0.3135        96/96
 F5      54/96      0.5625        0.4628        96/96
 F6      23/96      0.2396        0.1653        96/96
 TOTAL  224/576  correct ; 352 wrong            hop2 576/576
 All six hop1 blocks FAIL the 0.75 floor (even F5's Wilson lower 0.4628 << 0.75). hop2 clears every block.
 P-role among wrong hop1 predictions: 352/352 = 1.000.
```

## B. Is the hop1 collapse real or an artifact? (surprising-result scrutiny)

```text
HONEST SCORING: match == (ground_truth == predicted) for all 576 (0 disagreements); 0 empty predictions.
REAL OUTPUT (not a parse artifact): the scored .raw.json carries raw_response = the emitted token, and it
  EQUALS the parsed prediction (e.g., item_194 raw_response "i194_P1" == predicted "i194_P1"); ground_truth
  is the correct r1-object B (i194_B1). The model genuinely emits the P-role token.
SAME CONSTRUCTION: items 193..768 are the locked V3 construction via the unchanged generator/realizer (the
  abstract structure matches the floor-check / composite-gate items verified earlier).
=> hop1's failure across all six fresh blocks is REAL behavior on well-formed, honestly-scored items.
   HOP1-STABLE-INADMISSIBLE is a VALID verified outcome, not a broken run.
```

## C. Task-by-task (13 + the manifest)

```text
(1)  clean-fetch at final remote HEAD fe677158                                              ✓
(2)  576 fresh items, seeds 193..768 (items_193_768: 576 specs)                              ✓
(3)  hop1 + hop2 only, 1,152 calls (576 x 2); scored contexts are hop1/hop2 only            ✓
(4)  profile: Qwen/Qwen2.5-3B-Instruct, rev aa8e7253, FP16, greedy                          ✓
(5)  no composite/direct_query entered scoring or covariate logging (absent from scored)     ✓
(6)  re-ran the locked hop1-stability analyzer (command in §D)                               ✓
(7)  final branch HOP1-STABLE-INADMISSIBLE; decision.json reproduces BYTE-IDENTICAL          ✓
(8)  per-block hop1 rates/Wilson + hop2 control reproduced (table §A); all hop1 blocks fail,
     hop2 clears each block; hop2-control-fail [], construct-fail []                         ✓
(9)  P-role covariate 352/352; covariate_log.json reproduces BYTE-IDENTICAL (with the
     realization-summary input); raw_response confirms real emission                         ✓
(10) covariate logger uses only positional/structural fields (role classes P_decoy_head / B) ✓
(11) no forbidden mechanism/capability labels in outputs (only forbidden-list declarations)  ✓
(12) tooling digests UNCHANGED post-run (analyzer 31224f6f, logger b9532490, wrapper cc07e5a2,
     realizer fb561fdc)                                                                       ✓
(13) no rerun / prompt edit / regeneration / slicing / threshold change / tooling edit
     (single run; locked profile; prompts consumed as committed; no regeneration)            ✓
MANIFEST: present and COMPLETE — lists the digests of decision.json, covariate_log.json, run_record.json,
     and the scored files (admissibility 576/576 PASS, conformance 576/576 PASS).
```

## D. Analyzer rerun command

```text
python3 path-a/build/v3_hop1_stability_analyzer.py \
  --scored-dir <run>/scored --items-dir <run>/items_193_768 \
  --admissibility <run>/admissibility_summary.json --prompt-conformance <run>/prompt_conformance_summary.json \
  --start-index 193 --block-size 96 --n-blocks 6 --output /tmp/h1_dec.json
-> final_branch HOP1-STABLE-INADMISSIBLE ; byte-identical to committed decision.json.
(covariate logger reproduced byte-identical with the additional --realization-summary input.)
```

## E. Allowed interpretation (per TL) + bounded context

```text
ALLOWED (positional/structural):
  "Across the six fresh V3 materializations tested here, hop1 did not clear its admissibility floor in any
   block, while hop2 remained admissible in every block."
  "Among wrong hop1 predictions in the fresh blocks, outputs landed on the P-role distractor class in all
   logged cases (352/352)."

DESCRIPTIVE CONTEXT (data, not mechanism): per-block hop1 rates span 0.24–0.56 (all below the 0.75 floor).
  With the anchors — floor-check 001..096 hop1 0.906 (cleared) and composite-gate 097..192 hop1 0.292
  (failed) — the floor-check clearing is the LONE clearing across the eight materializations and is anomalous
  relative to the fresh map. (Anchors are descriptive; the branch is decided on the six fresh blocks only.)
```

## F. Forbidden interpretations (per TL — explicitly not claimed)

```text
NOT: the model cannot do hop1 | the model is unstable | a mechanism claim | binding/attention/reasoning
failure | shortcut | the model cannot compose | composite-gate evidence | certification | compression
readiness | Claim C | Paper B. The C0 K=5 FAIL stays closed; V3 ≠ C0.
```

## G. Methodological observation (no overclaim)

```text
This confirms the composite-gate PRECONDITION-FAIL was not a fluke: hop1-isolated admissibility is NOT met
across fresh V3 materializations at K=5, and the floor-check's hop1 clearing was materialization-specific.
This is the lock-before-look + fresh-run discipline doing its job again — a precondition that one early run
appeared to establish does not hold on fresh, disjoint draws.
```

## H. Recommended next route (SE recommends; authorizes nothing)

```text
1. Record this as a negative FINDING OF RECORD: under V3 at K=5 with Qwen2.5-3B-Instruct (FP16, greedy),
   hop1-isolated admissibility is not met across the six fresh materializations tested; wrong hop1 predictions
   land on the P-role distractor class in all logged cases. hop2 remains admissible throughout. (Positional.)
2. The composite-gate route AS DESIGNED is blocked: its hop1 precondition is now shown stable-inadmissible on
   fresh materializations, so the composite gate is not reliably testable as constructed.
3. Whether to (a) close the composite line on this finding, or (b) reconsider the V3 hop1 construction under a
   NEW pre-registration, is a TL/Manager/Elias decision. NOT a rerun of this study or the composite gate.
4. The program remains PRE-STRESS (FP16). Nothing here bears on compression / INT4 / INT8 / Claim C / Paper B.
All of the above are TL/Manager calls. SE recommends; SE does not authorize.
```

## I. Boundary

```text
- Verification only. No rerun, no prompt edits, no regeneration, no slicing, no threshold change, no tooling
  edit, no composite-gate retry, no compression, no INT8/INT4, no Claim C, no Paper B, no certification claim,
  no capability claim, no mechanism claim.
- The Path A FP16 K=5 FAIL remains closed and untouched. SE verifies; SE authorizes nothing.
```

— Senior Engineer (hop1-stability run verification; PASS — HOP1-STABLE-INADMISSIBLE verified, valid, bounded)
