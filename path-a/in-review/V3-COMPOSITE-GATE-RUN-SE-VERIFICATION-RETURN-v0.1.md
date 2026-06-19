# V3 COMPOSITE-GATE RUN — SE VERIFICATION RETURN (PRECONDITION-FAIL)

**To:** Team Lead **Cc:** CS Engineer, C5, Manager **From:** Senior Engineer **Re:** SE verification of the V3 composite-gate run (final branch PRECONDITION-FAIL)
**E. A. Flores**, Apiana AI, Inc. — June 18, 2026 · *Verification only. Certifies nothing, authorizes nothing.*

## VERDICT: **PASS** — V3 Composite Gate PRECONDITION-FAIL verified from bytes.

I re-ran the locked analyzer and reproduced a **byte-identical decision** (`3924ff35…`), branch **PRECONDITION-FAIL**, with condition (c) failing on **hop1 only**. I scrutinized the *surprising* hop1 collapse (87/96 → 28/96) the same way I scrutinized the perfect score: hop1=28/96 is **honestly scored on well-formed, same-construction items**, so it is a **real behavioral result, not an artifact** — and therefore PRECONDITION-FAIL is a **valid** outcome. One discrepancy (a missing manifest) and one methodological observation are in §D/§E.

## A. Files inspected + hashes recomputed (clean clone at HEAD `09030b18`)

```text
run_record.json                  43369d92…  MATCH      analyzer_decision.json   3924ff35…  MATCH (reproduced)
r6_log.json                      646bf4cf…  MATCH      admissibility_summary    4449ccdd…  MATCH
error_log.json                   3a89243b…  MATCH      realization_summary      27df314f…  MATCH
prompt_conformance_summary       4e9402e4…  MATCH      run_step_6.log           0d798ba4…  MATCH
384 scored JSON files present; schema {ground_truth, predicted, match}.
Tooling digests UNCHANGED pre/post: generator-wrapper cc07e5a2, gate-analyzer 3a3e954e, error-logger 2ed46628,
  underlying generator 6a2ceee1, realizer fb561fdc, checker b8afa3f8 (the "no tooling edit after data" attestation).
```

## B. Task-by-task (TL's 10 + the manifest)

```text
(1)  clean-fetch at final remote HEAD 09030b18                                              ✓
(2)  384 scored files exist, schema matches                                                 ✓
(3)  prompts consumed as committed (prompts_consumed_as_committed=true, regeneration=false)  ✓
(4)  run profile: Qwen/Qwen2.5-3B-Instruct, rev aa8e7253…, FP16, greedy, 384 prompts once    ✓
(5)  r6_log invalidated count = 0                                                            ✓
(6)  re-ran the locked composite-gate analyzer (command in §C)                               ✓
(7)  analyzer_decision.json reproduces BYTE-IDENTICAL; final branch PRECONDITION-FAIL        ✓
(8)  condition (c) failure caused by HOP1 ONLY:
        hop2.precondition_pass = True   (Wilson lower 0.9615)
        hop1.precondition_pass = False  (Wilson lower 0.2102)   <- the sole failing input
        direct_query.precondition_pass = True
        conditions.(c)_preconditions_pass = False  ->  PRECONDITION-FAIL                     ✓
(9)  no tooling edit after data (all six digests unchanged)                                  ✓
(10) no rerun / prompt edit / regeneration / slicing / floor adjustment / compression /
     model-profile drift (single run; profile locked; prompts committed; tooling unchanged) ✓
MANIFEST: see §D — INCOMPLETE (artifact absent), not merely stale.
```

## C. Analyzer rerun command + reproduced metrics

```text
python3 path-a/build/v3_composite_gate_analyzer.py \
  --scored-dir <run>/scored --r6-log <run>/r6_log.json \
  --admissibility <run>/admissibility_summary.json \
  --prompt-conformance <run>/prompt_conformance_summary.json \
  --error-log <run>/error_log.json --output /tmp/cg_dec.json
-> byte-identical to committed analyzer_decision.json (3924ff35…)

Reproduced from RAW scored files (independent recount):
  hop1 28/96 = 0.292  (Wilson lower 0.2102)   FAILS precondition floor 0.75
  hop2 96/96 = 1.000  (Wilson lower 0.9615)   clears
  direct_query 0/96 ;  invalidated 0 ;  C1–C9 96/96 ;  prompt-conformance 96/96 ;  MAX_DELTA all = 8
  composite 63/96 = 0.6562 (Wilson lower 0.5569)  INFORMATIONAL ONLY (gate not read)
  final branch: PRECONDITION-FAIL
```

## D. Is hop1=28/96 real or an artifact? (surprising-result scrutiny) + the discrepancy

```text
HONEST SCORING: match == (ground_truth == predicted) for all 96 (0 disagreements); 96 distinct, non-empty
  predictions; ground_truth is correct (= the B token, the r1-object of A). Not vacuous, not constant.
WELL-FORMED ITEMS: the failing hop1 prompt (item_098) is well-formed (correct QUERY (A, r1, ?); correct facts).
SAME CONSTRUCTION: the floor-check (001..096) and composite-gate (097..192) hop1 prompts have IDENTICAL
  abstract structure (target chain + 5 distinct-relation competitor branches + 5 relation-reusing P-distractor
  chains). The two sets are the SAME construction realized with different seeds — so the contrast is a clean
  behavioral DATA contrast, NOT a structural artifact in the fresh set.
=> hop1=28/96 is a REAL behavioral result on well-formed, honestly-scored items. PRECONDITION-FAIL is VALID.

BOUNDED DATA (positional/structural — NOT mechanism): all 68 wrong hop1 predictions land on the "P" role
  token. The FACTS block contains distractor triples (P_i, r1, Q_i) that REUSE the queried relation r1; the
  model returns an r1-SUBJECT distractor (P) rather than the r1-OBJECT (B1). The error logger classifies these
  as competitor_or_other. WHY the model does this — and why hop1 differs from hop2 (96/96) on the same items —
  is NOT decidable from this run and is NOT claimed.

DISCREPANCY — MANIFEST: there is NO manifest.json in the composite-gate run dir (the floor-check run had one).
  The "Build run manifest with all artifact hashes" checklist item is INCOMPLETE (the artifact is absent), NOT
  merely stale. This does NOT undermine the result — every artifact hash is independently verified above — but
  it is a missing deliverable. Recommend CS produce the manifest.
```

## E. hop1 contrast + methodological observation

```text
CONTRAST (DATA):
  floor-check    001..096:  hop1 87/96 (clears)   hop2 96/96 (clears)
  composite-gate 097..192:  hop1 28/96 (FAILS)    hop2 96/96 (clears)
  hop1 admissibility did NOT replicate on the second materialization; hop2 did. (DATA, not mechanism.)

METHODOLOGICAL OBSERVATION (no overclaim): the floor-check's hop1 clearing was materialization-specific — it
  did NOT replicate on a fresh disjoint set. This VINDICATES the lock-before-look fresh-run requirement: had
  the already-seen floor-check composite (0.833) been reused as the gate (which C5/TL correctly BARRED), the
  hop1 non-replication would have been hidden and a baseline "certified" on a set where the precondition only
  happened to hold. It also echoes the program's standing discipline that one clean run = "this-run," not
  "established." (This is n=2 materializations; it shows hop1 admissibility is NOT yet shown stable — it does
  not, by itself, establish that hop1 is "generally unstable.")
```

## F. Interpretation boundary (per TL)

```text
THE RESULT MEANS (only):
  On the fresh 097..192 V3 composite-gate materialization, hop1 did not clear its precondition floor
  (28/96, Wilson lower 0.2102 < 0.75); therefore the composite gate was NOT read. A VALID PRECONDITION-FAIL.

IT DOES NOT MEAN:
  the model fails to compose | the composite gate failed | V3 is invalid | general capability failure |
  mechanism | seam evidence | compression readiness | Claim C | Paper B | final classification.
  The composite (63/96) is INFORMATIONAL ONLY (the gate was not read). The C0 K=5 FAIL stays closed; V3 ≠ C0.
```

## G. Recommended next route (SE recommends; authorizes nothing)

```text
1. Record the valid PRECONDITION-FAIL. The composite question remains OPEN — the gate was not read, so nothing
   is concluded about the composite either way.
2. Do NOT rerun-until-pass. Drawing fresh seed ranges until hop1 happens to clear is the forbidden
   "rerun until pass." A single re-materialization that cleared would not be informative against this failure.
3. The KEY thing to examine before any further composite-gate attempt is the hop1 INSTABILITY across the two
   materializations (87/96 vs 28/96, same construction). If hop1 admissibility is materialization-dependent,
   precondition (c) will not reliably hold and the composite gate is not reliably testable as designed. This
   likely warrants a NEW, separately PRE-REGISTERED investigation of hop1 stability across multiple
   materializations (not a rerun of this gate). That is a TL/Manager decision.
4. CS to produce the missing run manifest (§D).
All of the above are TL/Manager calls. SE recommends; SE does not authorize.
```

## H. Boundary

```text
- Verification only. No rerun, no prompt edits, no regeneration, no slicing, no floor adjustment, no tooling
  edit, no compression, no INT8/INT4, no Claim C, no Paper B, no certification claim, no capability claim,
  no mechanism claim.
- The Path A FP16 K=5 FAIL remains closed and untouched. SE verifies; SE authorizes nothing.
```

— Senior Engineer (composite-gate run verification; PASS — PRECONDITION-FAIL verified, valid, bounded)
