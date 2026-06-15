# G6 Case 1 Evaluator — Minimal Build

> **The first G6 software in the program.** Static, deterministic, model-free.
> Reads the constructed Case 1 bundle and returns a G6 disposition per the
> 8 pre-declared checks named in TL ACTION 2026-06-14.

---

## 1. What this is — and what it is NOT

**It is:**
- A ~120-line Python script that opens two JSON files, reads recorded boolean
  fields, applies pre-declared logic, and emits a disposition.
- Hard-coded to Case 1 (Missing-Channel Trap). Not a general G6 implementation.
- Self-contained. Standard library only. No dependencies.

**It is NOT:**
- A model run. The evaluator does not call any model, perform inference, or
  query anything beyond local files.
- A general G6. It does not implement CH1 / CH2 / CH3 channel deployment, nor
  the full §11 disposition vocabulary. It evaluates one bundle, one case.
- A certification or stress evaluation. Route state remains YELLOW.
- A general validity claim for G6.

## 2. Boundary lift — transparent audit-trail acknowledgment

Multiple artifacts I filed earlier this session asserted "no G6 software build
authorized" as a held boundary:

```text
G6-OPTION-B-READINESS-NOTE-v0.1                 41a416b  §8
G6-INTERNAL-CONSISTENCY-EXERCISE-CLOSEOUT-v0.1  502a45f  §7
G6-OPTION-B-CASE-1-MISSING-CHANNEL-DESIGN-v0.1  60b0d32  §8
G6-NON-DESIGN-TARGET-CANDIDATE-INVENTORY-v0.1   1893a63  §7
G6-HOLD-REVIEW-SUPERSEDED-VALIDATION-RUNS-v0.2  7d880c5  §7
G6 Case 1 bundle (PROVENANCE-NOTE)              467debb  §6
```

**TL ACTION 2026-06-14** ("Build Minimal G6 Evaluator and Run Case 1") explicitly
lifts that boundary for **this minimal build only**. The lift is consistent
with YELLOW route state because the build is static and model-free; no
execution-class boundary is touched.

**Boundaries that remain unchanged and still hold:**

```text
- no model execution
- no new model run
- no certification authorized
- no compression / INT8 / INT4 authorized
- no Paper B activation
- no D4 reopening
- no general G6 validity claim
- no product / funder-facing claim
- no stress evidence produced
- sealed bytes do not move (this evaluator lives outside experiments/)
```

The Route-State Gate stays YELLOW; execution stays RED.

## 3. Files

```text
g6_case1_evaluator.py    the evaluator
results/                 output dir for run results
  case-1-disposition.json one run's disposition (the most recent)
README.md                this file
```

## 4. How to run

```text
cd tier-1-instrument/modules/g6-standing-rejection-audit/evaluator/
python3 g6_case1_evaluator.py
```

Defaults read the in-tree Case 1 bundle (`../case-1-missing-channel/`) and
write the result to `results/case-1-disposition.json`. Override with
`--bundle <dir>` and `--output <file>` if needed.

## 5. The 8 checks (from TL ACTION; pre-declared)

```text
1. refusal record exists                       (file existence)
2. case is in G6 audit scope                   (record field)
3. raw E3 is unavailable                       (record field)
4. only E2 labels are available                (record field)
5. CH1 is unavailable                          (manifest field)
6. CH2 is unavailable                          (manifest field)
7. channel absence is verifiable property      (record field)
8. no unrelated defect forces QUARANTINED      (record field)
```

Each check reads a recorded boolean from the bundle. The evaluator does NOT
re-derive these from raw evidence — the bundle's role IS to record these as
verifiable properties of itself (per design §7 crux). Re-deriving would
require running the model, which is barred.

## 6. Disposition logic (pre-declared, deterministic)

```text
if NOT in_scope:                                   -> AUDIT-INCONCLUSIVE
elif unrelated defect / unrelated quarantine:      -> REFUSAL-QUARANTINED / AUDIT-INCONCLUSIVE
elif checks 3+4+5+6+7 all hold (no channel):       -> AUDIT-CIRCULARITY / LIMITED   (fail-closed PASS)
else (channel apparently available):               -> REFUSAL-CONFIRMED              (fail-open FAIL)
```

## 7. Most recent result

```text
disposition: AUDIT-CIRCULARITY / LIMITED
all 8 checks: PASS
```

This is the expected fail-closed disposition for Case 1 per the design.
A future run that returned REFUSAL-CONFIRMED on this bundle would expose
a fail-open G6 failure (confirming by inheriting the original read — the
E2 circularity the spec exists to prevent). The disposition is correct.

## 8. What this run means — and does not mean

**It means:**
- For the constructed Case 1 record, this minimal evaluator returns the
  spec's design-target disposition (AUDIT-CIRCULARITY).
- The first G6 software ever built in the program emits the correct
  fail-closed answer on its first run, against the design's first case.
- The bundle's "absence as a verifiable property of the record" pattern
  is mechanically readable — the evaluator can decide from recorded
  fields alone, without model execution.

**It does NOT mean:**
- That G6 generally validates. This evaluator hard-codes Case 1's structure;
  it does not implement general channel deployment, general disposition
  logic, or general fail-closed handling.
- That G6 has been certified. No certification authorization was granted.
- That the program is closer to a certified baseline. The certification
  track remains exactly where it was before this build.
- That AUDIT-CIRCULARITY on a constructed case = G6 works on real refusals.
  Per the design §2 load-bearing caveat: this is a fail-closed DISCIPLINE
  test on a known-by-construction case, NOT a generalization test.

## 9. Authority + audit trail

```text
TL ACTION:    2026-06-14 ("Build Minimal G6 Evaluator and Run Case 1")
Boundary lift: explicit; documented in §2 above
Constructor:  CS Engineer (this is a CS construction step)
Bundle:       Case 1 bundle (constructed at 467debb under prior TL ACTION)
Design:       G6-OPTION-B-CASE-1-MISSING-CHANNEL-DESIGN-v0.1 @ 60b0d32
Spec:         g6-standing-rejection-audit-spec-v0.1.md
Route state:  YELLOW (model-free).  Execution: RED.
```

— CS Engineer, 2026-06-14
