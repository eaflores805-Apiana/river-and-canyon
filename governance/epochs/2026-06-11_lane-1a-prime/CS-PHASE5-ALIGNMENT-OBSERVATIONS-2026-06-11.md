# CS Phase 5 Alignment Observations — NS Validation Prerequisites

```text
DRAFT / REVIEW ONLY
D2 PHASE 5 ALIGNMENT MEMO
NO MODEL INVOKED -- NO SWEEP_ID -- NO SWEEP EXECUTION
NO CANDIDATE/MODEL OUTPUTS -- LOCK-RECORD REMAINS PENDING
```

From: CS Engineer
To: Team Lead, New Senior Engineer
Cc: Senior Engineer, Manager
Date: 2026-06-11
Re: Alignment between Phase 5 implementation (CS, commit `618e217`) and NS-filed validation prerequisites
Status: CS surfaces gap; awaits user direction on reconciliation path

---

## 1. New NS materials filed in this commit cycle

Seven NS-filed materials were committed to `apiana-papers/C6_Proposal/`
during or before CS Phase 5 execution. CS did NOT incorporate them
during the Phase 5 run (commit `618e217`). They are now mirrored
into `governance/2026-06-11_lane-1a-prime/`:

| File | sha256 (mirror) |
|---|---|
| `C6-CONTROL-TAXONOMY-AND-PRELOCK-VALIDATION-RATIONALE-v0.1.md` | (mirror) |
| `C6-CONTROL-TAXONOMY-AND-PRELOCK-VALIDATION-RATIONALE-v0.2.md` | (mirror) |
| `C6-CONTROL-TAXONOMY-AND-PRELOCK-VALIDATION-RATIONALE-v0.3.md` | (mirror) |
| `C6-CONTROL-TAXONOMY-AND-PRELOCK-VALIDATION-RATIONALE-v0.4.md` | `0f9357ff…` |
| `D2-APPROVED-DISPOSITIONS-AND-VALIDATION-PREREQS-v0.1.md` | (mirror) |
| `D2-APPROVED-DISPOSITIONS-AND-VALIDATION-PREREQS-v0.2.md` | `7d77ba52…` |
| `NEW-SENIOR-ORACLE-EXPECTED-VERDICT-DECLARATION-PROPOSED-2026-06-11.md` | `59148510…` |

The current canonical NS materials are v0.4 (C6) and v0.2 (D2-APPROVED).

## 2. CS substantive observations

### 2.1 Uniform comparison principle (load-bearing for Phase 5 apply_criterion)

**D2-APPROVED v0.2 §B uniform principle** (NS, accepted joint disposition):

> "Elimination requires the FULL confidence interval on the eliminating
> side. Uncertainty resolves toward `NOT_RULED_OUT`, never toward
> elimination; data insufficiency resolves toward `INCONCLUSIVE`. A
> point estimate on the eliminating side with a straddling interval
> does not eliminate — it sets `boundary_proximity_flag`."

**NS-specified comparison rules** (D2-APPROVED §B table):

| Criterion | NS comparison rule |
|---|---|
| `null_abstention_floor_unmet` | eliminates iff abstention-CI **upper bound** < declared floor |
| `answerable_abstention_ceiling_exceeded` | eliminates iff abstention-CI **lower bound** > declared ceiling |
| `accuracy_indistinguishable_from_token_prior` | Newcombe-Wilson upper bound on (candidate − control) < declared margin |
| `accuracy_indistinguishable_from_declared_policy_envelope` | Newcombe-Wilson upper bound on (candidate − envelope) < declared margin |
| `insufficient_measurement_headroom` | Wilson upper bound < declared required headroom |
| `strict_content_gap_instability` | Newcombe-Wilson lower bound > declared gap bound |

**CS Phase 5 implementation comparison rules** (`analysis.py::apply_criterion`):

```python
if criterion.is_floor:
    return value < floor_or_ceiling  # "value" is whichever bound the criterion declares
else:
    return value > floor_or_ceiling
```

with `DEFAULT_T3_CRITERIA` setting:

- `null_abstention_floor_unmet`: `is_floor=True`, `comparison=CI_LOWER_BOUND`
  → fires when `ci_lower < floor`
- `answerable_abstention_ceiling_exceeded`: `is_floor=False`, `comparison=CI_UPPER_BOUND`
  → fires when `ci_upper > ceiling`

**Gap (load-bearing):** CS used the WRONG CI bound per the uniform principle.

| Criterion | NS rule | CS implementation | Gap |
|---|---|---|---|
| null_abstention_floor_unmet | `ci_upper < floor` | `ci_lower < floor` | CS eliminates too easily (any CI bound below floor; should require entire CI below) |
| answerable_abstention_ceiling_exceeded | `ci_lower > ceiling` | `ci_upper > ceiling` | CS eliminates too easily (any CI bound above ceiling; should require entire CI above) |

**Effect on Phase 5 results:** the synthetic universal_answerer and
universal_abstainer extreme cases produced the same outcome under
both rules (the entire CI is on the elimination side for both
extreme cases). The mismatch matters for borderline cases — where
the principle prescribes `boundary_proximity_flag` (CS's flag is
implemented but is never set by the wrong comparison rule).

CS Phase 5 tests verified the harness behavior against CS's own
implementation; they did NOT verify alignment with the NS uniform
principle. The CS Phase 5 oracle results (8/9 matched) are
structurally informative but the criterion semantics differ from
the joint-disposition-approved uniform principle.

### 2.2 Full T3 criteria set (CS used 2 of 6)

NS materials list **six descriptive elimination labels** (per joint
disposition + D2-APPROVED §B comparison-rule table). CS Phase 5
default criteria set has **two** (the symmetric abstention pair).

CS rationale at Phase 5: simplified the default set because the
other four labels' threshold values are sweep-parameters declared
at packet seal; CS used only the two abstention criteria that have
sane default values for synthetic-data demo.

**NS-declared default value placeholders** (per D2-APPROVED §B,
read together with C6 §10 open-before-D3):

- separation margin (token-prior): [SWEEP-PARAMETER]
- envelope margin: [SWEEP-PARAMETER]
- required measurement headroom: [SWEEP-PARAMETER]
- strict-content gap bound: [SWEEP-PARAMETER]
- abstention floor / ceiling: [SWEEP-PARAMETER]

NS materials do not declare values; they declare comparison rules
and require the values to be locked at packet seal as a single lock
event (joint expected-verdict declaration co-signature). So CS
deferring values was correct in spirit; the gap is that CS did not
implement the comparison-rule SHAPES correctly even when running
with placeholder values.

### 2.3 Oracle expected-verdict table — 12 cases, not 9

**NS-PROPOSED oracle expected-verdict declaration** lists 12 oracle
cases (ORC-01 through ORC-12). CS Phase 5 `ORACLE_CASE_CATALOG` has
9 cases.

NS table additions not in CS catalog:
- ORC-04 recency_excluding_target shortcut (declared shortcut, not currently in CS catalog)
- ORC-05 prefix_neighbor_confusion shortcut (declared shortcut, not currently in CS catalog)
- ORC-11 mixture oracle 0.75 shortcut / 0.25 retrieval (shortcut-heavy)
- ORC-12 mixture oracle 0.25 shortcut / 0.75 retrieval (retrieval-heavy)

NS-PROPOSED defines ORC-10 (malformed-control) as "post-scramble-gold
behavior presented as candidate" with expected verdict `pass`
(rebinding-following sits far above prior baseline). CS Phase 5
`malformed_control` predicate is `predict_malformed_control_case`
returning the queried_key as predicted value (copy shortcut). The
**semantic differs**: NS's intent is to verify that the v1
mislabeling cannot recur; CS's implementation tests a different
malformed pattern.

The NS table also requires CS co-signature: *"The anti-tuning rule
requires every oracle case's expected verdict declared before
pre-flight execution. This is the NS half of the joint declaration;
it binds nothing until CS co-signs and the table is hashed into the
validation packet."*

**CS has not co-signed.** Phase 5 ran with CS-declared expected
verdicts in `ORACLE_CASE_CATALOG` (9 cases). The NS-PROPOSED table
(12 cases) is **not yet locked**.

### 2.4 Full-instrument oracle record fields

NS-required eight-field record (C6 v0.4 §7):

```text
oracle_case_id | oracle_case_type | expected_verdict |
actual_full_instrument_outcome | attached_labels |
boundary_proximity_flags | expected_verdict_matched |
failure_interpretation_if_mismatch
```

CS Phase 5 `OracleVerification` carries all 8 fields ✓. No gap here.

### 2.5 Ideal-witness specification (D2-APPROVED §C)

NS supplies a JSON ideal-witness specification record (D2-APPROVED
§C) that should be locked into T3. CS Phase 5 did not consume an
ideal-witness specification record (the harness operates on
synthetic predictions directly).

This is a packet-stage prerequisite that CS would consume at packet
seal; Phase 5 demo's reliance on synthetic oracle predictions is a
reasonable substitute for the demo run but the production validation
flow should consume the locked ideal-witness record.

### 2.6 IVR packet-stage form (D2-APPROVED §D)

NS supplies the IVR packet-stage form with 8 sections (D.1–D.8). CS
Phase 5 `instrument_validation_report.md` covers T1, T3, T4, oracle
table, non-claim — but does NOT include:

- D.3 T2 control-spec conformance fields (CS has T2 specs in
  `controls.py` but did not populate a conformance section in the
  report)
- D.6 pilot iteration log (CS Phase 5 produced one iteration; no
  failed pilots retained because the synthetic recipe is
  deterministic)
- D.7 execution ledger (CS produced it as a separate file
  `execution_ledger.json`; NS expects it inside the IVR)

These are presentational gaps; the underlying data exists in CS
Phase 5 outputs.

## 3. Phase 5 vs NS prerequisites: gap summary

| NS prerequisite | CS Phase 5 status | Gap severity |
|---|---|---|
| Uniform comparison principle (CI upper for floor; CI lower for ceiling) | CS used CI lower for floor; CI upper for ceiling | **load-bearing**: inverted CI bound logic; mismatch on borderline cases |
| Full T3 criteria set (6 labels) | CS used 2 abstention criteria | **non-load-bearing for the 8/9 synthetic results, but production validation needs all 6** |
| Joint oracle expected-verdict table (12 cases co-signed) | CS used 9 cases with own expected verdicts; no CS co-signature | **non-load-bearing for Phase 5 demo; load-bearing at packet seal** |
| Malformed-control case semantics | CS used copy-shortcut variant; NS-PROPOSED uses post-scramble-gold variant | semantic mismatch on one case |
| 8-field oracle record | CS has all 8 fields | aligned ✓ |
| Ideal-witness specification record (D2-APPROVED §C) | CS Phase 5 operates on synthetic predictions directly | structural gap; packet-stage consumes IW record |
| IVR packet-stage form sections (8) | CS report covers 5; data exists for the other 3 | presentational gap |

## 4. CS root-cause acknowledgement

CS executed Phase 5 without checking for new NS materials in
`apiana-papers/C6_Proposal/` between Phase 4 completion and Phase 5
execution. The new NS materials filed during that window (C6 v0.1–v0.4;
D2-APPROVED v0.1–v0.2; ORACLE-EXPECTED-VERDICT) contained the
**uniform comparison principle**, the **full T3 criteria set**, and
the **NS-proposed oracle expected-verdict table** — all of which
should have informed Phase 5 execution.

CS root cause: did not poll the apiana-papers/C6_Proposal/ directory
for new materials between Team Lead Phase 4 PASS authorization and
Phase 5 execution. Mitigation: add a "check for new NS materials"
step to the standard CS phase-start procedure (proposed standing
rule extension; not yet filed).

## 5. Reconciliation paths

### 5a. Path A — Re-execute Phase 5 with NS prerequisites

CS updates the harness to align with NS materials:

1. Update `analysis.py::apply_criterion` to apply the uniform
   principle (CI upper for floor; CI lower for ceiling).
2. Expand `DEFAULT_T3_CRITERIA` to include the full 6-criterion set
   with placeholder [SWEEP-PARAMETER] threshold values.
3. Expand `ORACLE_CASE_CATALOG` to NS's 12 cases (add ORC-04, ORC-05,
   ORC-11, ORC-12; reconcile malformed-control semantics with
   NS-PROPOSED ORC-10).
4. Update `validation.py::run_full_instrument_oracle_validation` to
   consume the joint expected-verdict table (requires CS
   co-signature first).
5. Re-execute `run_validation.py`; emit Phase 5 v0.2 artifacts.
6. Update Phase 5 completion summary; re-file at v0.2.

Cost: ~2-3 turns of work. Re-runs the entire validation pipeline.

### 5b. Path B — Defer reconciliation to Team Lead filter

CS files this alignment memo. Team Lead filters Phase 5 v0.1 with
the gap noted. Path-forward decision (re-execute v0.2 vs accept v0.1
as-is) lives with Team Lead at filter.

Cost: minimal CS work now; Team Lead carries the decision.

### 5c. Path C — Hybrid: file errata + co-sign oracle table; defer re-execution

CS files this alignment memo (already drafted as this file). CS also
**co-signs the NS oracle expected-verdict table** (after CS review
finds it sound — see §6 below). Path-forward on re-execution lives
with Team Lead.

## 6. CS preliminary review of NS-PROPOSED oracle table

CS has read the NS-PROPOSED oracle expected-verdict declaration. CS
preliminary observations on co-signature readiness:

| Item | CS observation |
|---|---|
| 12-case enumeration | Comprehensive; matches the C6 §4 taxonomy + Bundle v0.3 Part II requirements |
| `expected_verdict` vocabulary (pass / detect / flag-indeterminate) | Clean; aligns with INH-2 three-way model (pass↔NOT_RULED_OUT; detect↔ELIMINATED; flag-indeterminate↔either-acceptable) |
| ORC-01 ideal retriever (pass, no label expected) | Correct; CS endorses |
| ORC-02..05 declared shortcuts (detect, envelope label) | Correct; CS endorses; requires the envelope criterion to be in the T3 set (currently missing from CS DEFAULT_T3_CRITERIA) |
| ORC-06 token-prior emitter (detect, token-prior label) | Correct; co-attachment of abstention-floor label noted; CS endorses |
| ORC-07 universal answerer (detect, null floor label) | Correct; CS endorses |
| ORC-08 universal abstainer (detect, ceiling label) | Correct; headroom co-attachment noted; CS endorses |
| ORC-09 perfect NULL-on-NULL handler (pass; regression test for v1) | **Critical regression test**; CS endorses |
| ORC-10 malformed-control (post-scramble-gold; pass; mechanical check on scrambled control non-reference) | Semantic differs from CS Phase 5; CS endorses NS semantic |
| ORC-11 / ORC-12 mixture oracle bracket | Clean bracket design; CS endorses |

**CS preliminary co-signature posture:** CS recommends co-signing
NS-PROPOSED oracle expected-verdict table with the following
qualifications:

1. The [SWEEP-PARAMETER] bound values for separation margin /
   envelope margin / floor / ceiling must be locked at the same
   co-signature event (one lock).
2. The ORC-10 malformed-control semantic adopts NS's post-scramble-gold
   variant; CS's current Phase 5 catalog `malformed_control` predicate
   (copy-shortcut) is superseded.
3. The packet's single tokenizer+canonicalization identity must be
   declared by name and version in T1 (per NS materials).
4. The `control_prompt_shell_hash` LOCK-RECORD field is concurrent
   per the joint disposition.

CS treats this as preliminary; formal co-signature awaits user/Team
Lead direction.

## 7. CS recommendation

**Path C (hybrid)** appears the most sensible:
- File this alignment memo (filed).
- CS co-signs the NS-PROPOSED oracle table (with qualifications in §6).
- Phase 5 v0.1 stays committed (commit `618e217`); the gaps are
  documented here for Team Lead filter.
- If Team Lead requires re-execution before D3, CS executes Path A
  on Team Lead direction.

This preserves the work-trail (Phase 5 v0.1 exists and is reviewable);
captures the gaps explicitly; positions the joint oracle expected-verdict
table for lock-event signing; defers the re-execution decision to
Team Lead.

## 8. Confirmations

```text
No model invoked.
No sweep_id created.
No sweep execution.
No candidate/model outputs.
LOCK-RECORD remains PENDING.
```

CS confirms.

## 9. CS posture

```text
NS materials (7 files):          MIRRORED at this commit
CS alignment gap:                IDENTIFIED + DOCUMENTED (§§2-3)
CS root-cause acknowledged:      did not poll C6_Proposal/ between
                                  Phase 4 PASS and Phase 5 execution
Path forward:                    CS recommends Path C; awaits user
                                  direction
CS co-signature on NS oracle:    preliminary endorsement with 4
                                  qualifications (§6); awaits user
                                  direction on formal co-signature

All execution gates:             CLOSED
```

CS holds for user direction on:
- (A) Re-execute Phase 5 with NS prerequisites (commit Phase 5 v0.2)
- (B) Defer to Team Lead filter; Phase 5 v0.1 stands
- (C) Hybrid — file this memo, co-sign oracle table, defer re-execution
- (D) Other path

— CS Engineer, 2026-06-11
