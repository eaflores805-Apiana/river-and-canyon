# Block D — Positive-Control / Evidence Inventory Return (v0.1)

```text
LAYER-1 (CRITERION-FIRING):  POSITIVE CONTROL PRESENT with PARTIAL on comparable-condition-class
LAYER-2 (REAL-CANDIDATE ELIMINATION):  POSITIVE CONTROL ABSENT
COMBINED:  ASYMMETRIC — synthetic-scope evidence on the criterion side; zero real-candidate evidence
RECOMMENDATION FOR BLOCK E DESIGN QUESTION:  SUFFICIENT (the Layer-2 ABSENT premise is established)
INVENTORY ONLY — NO REGENERATION, RERUN, REFRESH, MODEL EXECUTION, OR SUITE EXECUTION
SEALED LOCK-RECORD v1.0 UNCHANGED · SEALED SCHEDULE UNCHANGED
PHASE LEDGER REFERENCE: SEMANTIC-READ-OPERATIONALIZATION-LEDGER-v0.2.1.md
```

To: Team Lead · Cc: Manager, Senior, NS, C4, C5, C6
From: CS Engineer
Date: 2026-06-13
Re: Block D deliverable — positive-control / evidence inventory return (Semantic-Read Operationalization)

CS files the Block D evidence inventory per TL Block D authorization.
The inventory enumerates existing artifacts by item under the §9
consolidation rule (incorporation by reference is not enumeration);
each Layer-1 item is classified by the E8 three-criterion bar
(same-instrument-version / comparable-condition-class /
instrument-reason-traceability); Layer-2 is enumerated as NONE
under the same bar, with explicit pre-classification of D4-B and
Path A TP control outcomes as control-channel evidence per
Manager-binding language and v0.4 E14.

No artifact was regenerated, rerun, refreshed, or executed for
this inventory. Every sha256 below was recomputed from the
on-disk artifact at the time of this return.

---

## §1. TL #1 — Existing artifacts inventoried

Layer 1 (criterion-firing evidence) inventoried artifacts:

```text
1. oracle_validation_results.json
   path:    experiments/2026-06-11_lane-1a-prime/validation/oracle_validation_results.json
   sha256:  37759f9acfffd676... (9,204 bytes; recomputed at filing time)
   purpose: PH5-1 model-free validation outcomes against the locked oracle table

2. B1 v2 test-suite results (per B1-V2-LOCK-NOTE.md and the
   B1 v2 merge-readiness BRANCH-EVIDENCE-PACKET.md)
   path:    governance/2026-06-10_b1-harness-v2-merge-and-lock/B1-V2-LOCK-NOTE.md
            governance/2026-06-09_b1-harness-v2-merge-readiness/BRANCH-EVIDENCE-PACKET.md
   sha256:  (not recomputed in this filing; CS confirms presence;
             NS or Senior verify counts against framework if needed)
   purpose: harness validity — criterion code-path coverage by test fixtures
```

Layer 2 (real-candidate elimination evidence) inventoried artifacts:

```text
1. D4-A run-of-record (experiments/2026-06-11_lane-1a-prime/d4_a_pilot/)
2. D4-B run-of-record (experiments/2026-06-11_lane-1a-prime/d4_b_pilot/)
3. Path A (rung-uniform) run-of-record (experiments/2026-06-11_lane-1a-prime/path_a_run/)
```

All three classified in §3 below.

---

## §2. TL #2 — Layer 1 criterion-firing evidence status

### Item 1: oracle_validation_results.json (12/12 ORC matches)

CS read the on-disk artifact and enumerates the actual oracle-case
outcomes by row (per the §9 enumeration rule):

```text
ORC-ID  Oracle case type                            Expected           Actual            Match
─────── ─────────────────────────────────────────── ──────────────────  ──────────────────  ─────
ORC-01  ideal_retriever                             not_ruled_out      not_ruled_out      YES
ORC-02  pure_last_position_shortcut                 eliminated         eliminated         YES
ORC-03  salient_endpoint_shortcut                   eliminated         eliminated         YES
ORC-04  recency_excluding_target_shortcut           eliminated         eliminated         YES
ORC-05  prefix_neighbor_confusion_shortcut          eliminated         eliminated         YES
ORC-06  token_prior_emitter                         eliminated         eliminated         YES
ORC-07  universal_answerer                          eliminated         eliminated         YES
ORC-08  universal_abstainer                         eliminated         eliminated         YES
ORC-09  perfect_null_on_null_handler                not_ruled_out      not_ruled_out      YES
ORC-10  malformed_control_semantic_separation_guard not_ruled_out      not_ruled_out      YES
ORC-11  mixture_shortcut_heavy                      eliminated         eliminated         YES
ORC-12  mixture_retrieval_heavy                     not_ruled_out      not_ruled_out      YES

Total cases:   12
Overall match: 12 of 12
```

E8 three-criterion bar:

```text
Criterion 1 — Same instrument version:
  Bounds:                     T3_BOUNDS_DECLARATION.json sha256 45565d0b... (sealed; matches current)
  Recipe:                     STRATIFIED_RECIPE_SCHEDULE.json sha256 7ad3ccdd... (sealed; matches current)
  Oracle table:               ORACLE_VERDICT_TABLE.json sha256 9c6cbda9... (sealed; matches current)
  LOCK-RECORD anchor:         51e18fa9... (sealed; matches current)
  Verdict on Criterion 1:     PASS

Criterion 2 — Comparable condition class:
  Real-candidate condition?   NO — oracle cases are synthetic emitters / handlers (ideal retriever,
                              shortcut policies, universal answerer, universal abstainer, prior
                              emitter, mixture cases, malformed control)
  L01-equivalent surface?     YES — the validation pipeline runs the oracle cases against the
                              L01 manifest, so the surface class matches; only the candidate
                              class differs (synthetic vs real model)
  Verdict on Criterion 2:     PARTIAL — synthetic-emitter scope, not real-candidate scope

Criterion 3 — Instrument-reason traceability:
  Per-case label trace?       YES — each row in oracle_validation_results.json names the
                              attached_labels and the required/permitted/required-absent label
                              constraints; each match decomposes to specific criterion firings
                              (e.g., ORC-02 attached `accuracy_indistinguishable_from_declared_
                              policy_envelope` and `null_abstention_floor_unmet`, matching
                              `required_labels: ["...declared_policy_envelope"]` and
                              `permitted_co_labels: ["...token_prior", "...null_abstention_floor"]`)
  Verdict on Criterion 3:     PASS

Item 1 overall: POSITIVE CONTROL PRESENT (criterion-firing layer) with PARTIAL on Criterion 2
```

### Item 2: B1 v2 test-suite criterion-firing behavior

CS confirms by-name presence of the B1 v2 harness lock + branch
evidence packet. Test counts referenced in upstream materials
(passdown letter 2026-06-10: *"26/26 tests; full Paper 2 regression
96/96 raw-output bit-identical"*); the exact count cited in NS's
TL-intake 2026-06-12 (*"241-test suite"*) does not match the
26/26 figure CS sees in the passdown — CS reports the discrepancy
and recommends NS or Senior reconcile against the test-framework
artifacts directly.

```text
Criterion 1 — Same instrument version:
  B1 v2 harness is the locked-in instrument version that runs both Paper 2 regression and
  Paper 3-substrate (inert). Bit-identical Paper 2 regression confirms the harness preserves
  instrument behavior across the lock.
  Verdict on Criterion 1:     PASS

Criterion 2 — Comparable condition class:
  Test fixtures are synthetic by construction; not real candidates on real surfaces
  Verdict on Criterion 2:     PARTIAL — synthetic test-fixture scope, not real-candidate scope

Criterion 3 — Instrument-reason traceability:
  Each test names a specific check; the BRANCH-EVIDENCE-PACKET maps each test name to a
  controlled property (e.g., B1-T17 framework_version validation; B1-T18 threshold-sheet
  hash verification; etc.)
  Verdict on Criterion 3:     PASS

Item 2 overall: POSITIVE CONTROL PRESENT (criterion-firing layer) with PARTIAL on Criterion 2
```

**Layer-1 combined verdict:**

```text
POSITIVE CONTROL PRESENT (criterion-firing layer)
with explicit PARTIAL on the comparable-condition-class criterion
   (Items 1 and 2 are both synthetic-scope; neither demonstrates
   criterion-firing on a real-candidate surface)
```

The PARTIAL is the *honest scope*, not a deficiency: the
criterion-firing evidence comprehensively covers synthetic /
oracle / test-fixture conditions and explicitly does not extend
to real-candidate conditions.

---

## §3. TL #3 — Layer 2 real-candidate elimination evidence status

```text
Evidence items:  NONE
```

Per-run enumeration (incorporation by reference is not enumeration):

### D4-A run-of-record

```text
path:                              experiments/2026-06-11_lane-1a-prime/d4_a_pilot/
candidate accuracy:                1.0000 (80/80) — NOT_RULED_OUT
elimination labels attached:       0
t1_report.json sha256:             ebe0a95246a5dfc4...
t3_report.json sha256:             a4e0236bfd6a85e5...
t4_report.json sha256:             6d265d25d1bd6852...
a6_re_verification.json sha256:    3c2e09b18e609e4f...
execution_ledger.json sha256:      f75db02c3080939f...
instrument_validation_report sha256: 7510c06a6dcddf09...
candidate_predictions sha256:      ba276b0539a4e7ee...
classification:                    NOT real-candidate elimination evidence (candidate was NOT eliminated)
```

### D4-B run-of-record

```text
path:                              experiments/2026-06-11_lane-1a-prime/d4_b_pilot/
candidate accuracy:                1.0000 (80/80) — NOT_RULED_OUT
elimination labels attached:       0
TP control accuracy:               0.0125 (1/80) — TP control eliminated
NW-diff CI [lower, upper]:         [0.9159, 0.9978] (candidate vs TP control)
t1_report.json sha256:             03b14a8e37a73f27...
t3_report.json sha256:             6a74ae78a96212ed...
t4_report.json sha256:             ed723a8fc59baa61...
a6_re_verification.json sha256:    3538412be4a58eb2...
execution_ledger.json sha256:      d8b8b7a9d75cf026...
instrument_validation_report sha256: 70c26b2371e730ca...
tp_control_predictions sha256:     3bc7621c7b0bddf1...
classification (candidate side):   NOT real-candidate elimination evidence (candidate was NOT eliminated)
classification (TP control side):  control-channel evidence per v0.4 E14
                                   (TP control is a no-bindings shell DESIGNED to fail;
                                    its elimination measures the control machinery, not the
                                    candidate; NOT upgradeable to real-candidate elimination)
```

### Path A (rung-uniform) run-of-record

```text
path:                              experiments/2026-06-11_lane-1a-prime/path_a_run/
per-rung candidate accuracy:       1.0000 (80/80) per rung, all 8 rungs — NOT_RULED_OUT per rung
                                   (under Manager binding characterization: an L01-equivalent
                                    surface repeated under eight rung labels)
per-rung TP control accuracy:      0.0125 (1/80) per rung — TP control eliminated per rung
elimination labels attached:       0 (per rung; do NOT aggregate per Manager close-out §5)
per-rung NW-diff CI:               [0.9159, 0.9978] per rung (8 rungs × 1 surface = 8 bounded sentences)
classification (candidate side):   NOT real-candidate elimination evidence (candidate was NOT eliminated)
classification (TP control side):  control-channel evidence per v0.4 E14
classification (combined):         schedule-layer finding per Manager close-out §2 — "Path A
                                   (rung-uniform) showed that, under the sealed rung-uniform
                                   schedule, the active six-criterion instrument attached no
                                   elimination label to an L01-equivalent surface repeated under
                                   eight rung labels."
```

**Layer-2 verdict:**

```text
POSITIVE CONTROL ABSENT (real-candidate-elimination layer)

The E8 three-criterion bar is vacuous at this layer because there is no
real-candidate elimination evidence to evaluate. Across D4-A, D4-B, and
Path A (rung-uniform), candidate side outcomes are uniformly
NOT_RULED_OUT; no real candidate has ever been attached an elimination
label under the active six-criterion instrument.

The eight Path A (rung-uniform) per-rung outcomes do NOT aggregate into
generality / robustness / replication-in-the-strong-sense per Manager
close-out §5 + §11. They are bounded sentences about one L01-equivalent
surface repeated under eight rung labels.
```

---

## §4. TL #4 — Comparable-condition limitation

The asymmetry is explicit:

```text
LAYER 1: criterion-firing evidence is PRESENT but SYNTHETIC-SCOPE only.
  - All 12 oracle cases are synthetic emitters / handlers
  - All B1 v2 test fixtures are synthetic by construction
  - Neither establishes criterion-firing on a real candidate

LAYER 2: real-candidate elimination evidence is ABSENT.
  - Every model-facing run (D4-A, D4-B, Path A) produced a NOT_RULED_OUT
    candidate outcome
  - TP control elimination is control-channel evidence, not real-candidate
    elimination evidence

LIMITATION:
  The active six-criterion instrument has demonstrated CAN-FIRE on
  synthetic conditions (Layer 1) and has NEVER ELIMINATED a real
  candidate (Layer 2). The IS-SENSITIVE-TO-REAL-CANDIDATE-FAILURE
  question is not established by current evidence.
  (Parallel to v0.4 E10 "can fire ≠ is sensitive" distinction; the
  same shape carries from Block E's design space to Block D's
  inventory.)
```

---

## §5. TL #5 — Non-upgradeable evidence (explicitly listed)

The following evidence items are **NOT upgradeable** to real-candidate
elimination evidence under any current interpretation:

```text
NU-1.  D4-B TP control elimination (accuracy 0.0125; CI upper 0.998)
       Reason: TP control is a no-bindings shell DESIGNED to fail; its
       elimination is control-channel evidence, NOT real-candidate
       elimination. Per v0.4 E14: "control machinery measured the
       intended channel."

NU-2.  Path A (rung-uniform) per-rung TP control elimination outcomes
       (× 8 rungs)
       Reason: same as NU-1, applied per rung; does NOT aggregate to
       real-candidate elimination evidence.

NU-3.  Path A (rung-uniform) per-rung candidate NOT_RULED_OUT outcomes
       (× 8 rungs)
       Reason: non-elimination is not elimination evidence (it is the
       absence of any criterion firing). Even aggregated, eight
       non-eliminations are eight bounded NOT-EVIDENCE statements,
       not evidence about instrument sensitivity. Per Manager close-out
       §5: "they do NOT AGGREGATE."

NU-4.  Oracle ORC-01 / ORC-09 / ORC-10 / ORC-12 NOT_RULED_OUT outcomes
       (4 of 12)
       Reason: these are EXPECTED NOT_RULED_OUT cases (ideal retriever,
       perfect null handler, malformed control, mixture retrieval heavy);
       their non-elimination is criterion-firing evidence about how the
       instrument behaves on synthetic NOT_RULED_OUT controls, not
       elimination evidence and not real-candidate evidence.

NU-5.  B1 v2 test passes
       Reason: tests confirm harness validity; they do not demonstrate
       criterion firing on a real candidate.

NU-6.  Paper 2 cells 01-03 baseline-correctness measurements
       Reason: these are pre-stress baseline measurements, not
       instrument-elimination outcomes.
```

---

## §6. TL #6 — Recommendation for Block E constructed-positive design question

**SUFFICIENT for the constructed-positive design question.**

Block E asks (per v0.4 §1 Q1 and TL Block E authorization):
*"If positive-control evidence is absent, what constructed-positive
surface would be required to show that the battery can fire on a
real-candidate-class condition?"*

Block D establishes the if-condition: Layer-2 positive-control
evidence IS absent (no real-candidate elimination has occurred).
The premise of Block E's design question is established. Block E
can proceed (when authorized) without needing additional Layer-2
inventory.

CS notes that Block E is currently sequenced after Block D and
Block F per TL §Block E remains sequenced ("Block E waits for
Block D and Block F" because "we should not design a
constructed-positive against the wrong premise"). Block D's
inventory confirms the premise; Block E's design question is now
well-posed, but Block E does not begin until Block F also returns
and TL re-routes.

---

## §7. TL #7 — Non-authorization / prohibition block carried (FULL)

This inventory memo does not authorize, request, or initiate:

```text
model-facing execution
model loading
sweep_id creation
token-prior generations
constructed-positive generation
seeded-defect exercise
surplus-signature validation
schedule v2 drafting
schedule supersession
true breadth rerun
Path B readiness or execution
Path D execution
quantization stress
INT8 / INT4
candidate selection
ranking
threshold work
certification evaluation
Claim C activation
public benchmark packaging
funder-facing release
SBIR submission
```

Standing constraints carry per the Lane 1a' Prime INDEX. Process
acceleration SUSPENDED for model-facing gates. Semantic-read gate
ACTIVE.

---

## §8. TL #8 — Language-perimeter check

**Language perimeter: CLEAN.**

```text
Forbidden positive over-reads (13):  ALL ABSENT
  (no "L01–L08 breadth result" / "full-surface NOT_RULED_OUT" /
   "8/8 survived" / "eight rungs NOT_RULED_OUT" / "breadth passed" /
   "result replicated across rungs" / "robust across the schedule" /
   "consistent across all rungs" / "task family viable" / "candidate
   certified" / "Claim C progress" / "seam evidence" / "public
   benchmark result")
Forbidden negative over-reads (4):   ALL ABSENT
  (no "Path A failed" / "the lane is broken" / "constructibility was
   answered negatively" / "task family shows no breadth")
Path A reference qualifier:          PRESENT throughout — cited as
                                     "Path A (rung-uniform)" or
                                     "Path A (rung-uniform) close-out"
                                     in every reference
Standing scope sentence:             Block D scope is not breadth-
                                     describing per se; the §3
                                     Path A (rung-uniform) classification
                                     section carries the binding
                                     characterization verbatim per
                                     Manager close-out §2
§4 quoted-shed-claim rule:           "L01–L08 breadth" appears nowhere
                                     in this memo
§13 internal citation rule:          Path A references limited to the
                                     binding-characterization sentence
                                     and the standing rung-uniform
                                     designator
```

---

## §9. TL #9 — Path / commit / sha256 / INDEX reference

```text
This memo (Block D return):
  path:        governance/2026-06-11_lane-1a-prime/BLOCK-D-POSITIVE-CONTROL-INVENTORY-v0.1.md
  sha256:      (computed at commit time; reported in CS delivery message + INDEX)
  commit:      (reported after this commit lands)
  INDEX:       row added in this filing commit; references the phase ledger
               SEMANTIC-READ-OPERATIONALIZATION-LEDGER-v0.2.1.md

Inventoried artifacts (sha256s above in §1–§3).

Phase ledger reference (TL-stated):
  SEMANTIC-READ-OPERATIONALIZATION-LEDGER-v0.2.1.md
  (workspace artifact; CS does not currently see this ledger filed in
   the repo; cross-reference added when ledger commits)
```

---

## §10. CS flags for Senior / NS reconciliation (informational, not blocking)

Two minor enumeration discrepancies between NS's TL-intake (2026-06-12)
and the on-disk evidence:

```text
DISCREPANCY 1: oracle-case match count
  NS proposed wording:  "eight-of-nine oracle-case matches from Phase 5
                        model-free validation"
  On-disk artifact:     12 oracle cases (ORC-01 through ORC-12), 12 of 12
                        matched per oracle_validation_results.json
  CS recommendation:    NS confirm or amend the wording before TL
                        incorporates it into the Manager-facing proposal.
                        CS uses the actual on-disk count in this return.

DISCREPANCY 2: B1 v2 test-suite count
  NS proposed wording:  "criterion-firing behavior in the 241-test suite"
  Upstream materials:   passdown letter 2026-06-10 references
                        "26/26 tests; full Paper 2 regression 96/96
                        raw-output bit-identical"
  CS recommendation:    NS or Senior reconcile the count against the
                        test-framework artifact directly. The "241"
                        figure may include cells beyond what CS sees
                        in the passdown; CS does not assert which count
                        is correct.
```

Both flags are non-blocking for Block D's verdict (POSITIVE CONTROL
PRESENT with PARTIAL on Layer 1; ABSENT on Layer 2). The Layer-1
verdict carries regardless of the exact numeric count of Layer-1
items; the criterion-firing layer has DEMONSTRATED firing on at
least the 12 actually-recorded oracle cases.

---

## §11. State invariants (≈32nd survival check)

```text
Sealed LOCK-RECORD v1.0    sha256 51e18fa9f45379a3...  UNCHANGED
Sealed STRATIFIED_RECIPE   sha256 7ad3ccddecd07007...  UNCHANGED
Sealed ORACLE_VERDICT      sha256 9c6cbda9eb5b6e85...  UNCHANGED
Sealed T3_BOUNDS           sha256 45565d0b46c05da4...  UNCHANGED
Sealed L01 manifests       sha256 afe0e545c318132a...  UNCHANGED
oracle_validation_results  sha256 37759f9acfffd676...  UNCHANGED (Layer-1 evidence file)
Filed Hash Integrity v0.7.2 bundle                       UNCHANGED
D4-A / D4-B / D4-synthesis / Path A run-of-record       UNMUTATED
```

— CS Engineer, 2026-06-13 (Block D positive-control inventory: Layer-1 PRESENT with PARTIAL on comparable-condition-class (12/12 ORCs + B1 v2 tests, synthetic scope); Layer-2 ABSENT (no real-candidate elimination); 6 NU items enumerated as non-upgradeable; Block E design-question premise SUFFICIENT; two minor enumeration discrepancies flagged for NS reconciliation; language perimeter CLEAN; standing carry intact)
