# CS Co-Signature — Oracle Expected-Verdict Declaration v0.2

```text
DRAFT / REVIEW ONLY
CS CO-SIGNATURE ON NS ORACLE VERDICT TABLE v0.2
PH5-1 JOINT LOCK-EVENT ARTIFACT — VERDICT TABLE SIDE
NO MODEL INVOKED -- NO MODEL LOADED
NO SWEEP_ID -- NO SWEEP EXECUTION
NO CANDIDATE/MODEL OUTPUTS -- LOCK-RECORD REMAINS PENDING
```

From: CS Engineer
To: New Senior Engineer, Team Lead
Cc: Senior Engineer, Manager
Date: 2026-06-11
Re: CS co-signature on NS-PROPOSED Oracle Expected-Verdict Declaration v0.2 (mirror at `governance/2026-06-11_lane-1a-prime/NEW-SENIOR-ORACLE-EXPECTED-VERDICT-DECLARATION-v0.2-PROPOSED-2026-06-11.md`, sha256 `a5d95065c497025b9d07f3b65ffd6d6477a5f94a70323f4abf462a810df32f85`)
Status: CS CO-SIGNS v0.2; partial PH5-1 closure (verdict-table side); bounds-declaration still owing for full PH5-1

---

## 0. CS co-signature verdict

```text
CS CO-SIGNS the NS Oracle Expected-Verdict Declaration v0.2 in full.

The v0.2 table cleanly implements the 4-field label-set structure
agreed in CS co-signature §5 of the corrective disposition memo:
  required_labels · permitted_co_labels · required_absent_labels
matched against attached_labels via the 4-clause match predicate
already implementable in lane1a_prime/validation.py::match_oracle_verdict.

CS sha256 attestation of the table bytes:
  a5d95065c497025b9d07f3b65ffd6d6477a5f94a70323f4abf462a810df32f85

CS endorses this hash for inclusion in the validation pre-flight
config (PH5-4) as the verdict-table side of the lock event.
```

---

## 1. v0.1 → v0.2 substantive changes (CS verification)

| Change | v0.1 | v0.2 | CS verification |
|---|---|---|---|
| Verdict vocabulary | pass / detect / flag-indeterminate | NOT_RULED_OUT / ELIMINATED / NOT_RULED_OUT (mapped to INH-2 three-way enum) | **ALIGNED** with RungOutcome enum from controls.py |
| Label-set fields | descriptive notes only | 4 explicit fields per case (required_labels, permitted_co_labels, required_absent_labels — plus attached_labels at run time) | **ALIGNED** with CS co-signature §5 match predicate |
| Anti-tuning | implied | "Verdict expectations are defined against the FULL six-criterion set only — no expectation is ever defined relative to a reduced criteria set" | **CS endorses** — explicit anti-tuning posture |
| ORC-01 ideal_retriever | pass; no labels | NOT_RULED_OUT; required_absent = all 6 labels | **STRONGER** than v0.1; CS endorses (every elimination label must be absent) |
| ORC-02..05 declared shortcuts | detect; envelope label primary | ELIMINATED; required=ENV; permitted_co=FLOOR, TP | **CO-SIGNS**; FLOOR co-attach reflects synthetic shortcuts' real no-abstain behavior |
| ORC-06 token_prior | detect; TP primary | ELIMINATED; required=TP; permitted_co=FLOOR, ENV | **CO-SIGNS**; same multi-attach principle |
| ORC-07 universal_answerer | detect; NULL floor primary | ELIMINATED; required=FLOOR; permitted_co=TP, ENV | **CO-SIGNS**; v0.2 makes FLOOR the load-bearing primary as expected |
| ORC-08 universal_abstainer | detect; ceiling primary | ELIMINATED; required=CEIL; permitted_co=TP, ENV, HEAD | **CO-SIGNS** |
| ORC-09 perfect_null_handler | pass | NOT_RULED_OUT; required_absent = all 6 | **CO-SIGNS** — ideal-corner closure regression guard |
| ORC-10 malformed_control | pass; not-TP | NOT_RULED_OUT; required_absent = **{TP} (the defining check)**; permitted: boundary_proximity_flags only | **CO-SIGNS**; TP-absence is the v1-mislabeling regression test |
| ORC-11 mixture-shortcut-heavy | detect | ELIMINATED; required=ENV; required_absent={FLOOR, CEIL} | **CO-SIGNS**; mixture's abstention is contract-correct, so FLOOR/CEIL must NOT fire |
| ORC-12 mixture-retrieval-heavy | flag-indeterminate | **NOT_RULED_OUT**; permitted = boundary_proximity_flag on ENV; required_absent={TP, FLOOR, CEIL} | **CO-SIGNS** — cleaner than v0.1's flag-indeterminate, maps to INH-2 three-way enum directly; boundary flag on ENV criterion is the v0.2 mechanism for the boundary case |

CS notes: v0.2 retires the "flag-indeterminate" verdict in favor of a
clean three-way mapping (INCONCLUSIVE / ELIMINATED / NOT_RULED_OUT
only), with the boundary_proximity_flag carrying the "boundary case"
information per joint disposition (boundary_proximity_flag is the
diagnostic mechanism; never enters outcome or K). This is a
**better** mapping than v0.1's external "flag-indeterminate" verdict.

---

## 2. CS implementation alignment confirmations

### 2.1 Match-predicate alignment

CS confirms `match_oracle_verdict` in CS co-signature §5 implements
the v0.2 table's pass rule exactly:

```python
overall_matched = (
    outcome_matched
    and required_labels_present
    and required_absent_labels_absent
    and only_required_or_permitted_attached
)
```

For each case the predicate evaluates:
- `outcome_matched`: `actual_outcome == oracle_case.expected_outcome`
- `required_labels_present`: every `required_labels` entry attached
- `required_absent_labels_absent`: no `required_absent_labels` entry attached
- `only_required_or_permitted_attached`: every attached label ∈ (required ∪ permitted_co)

For ORC-01 / ORC-09 (NOT_RULED_OUT; required=(); permitted_co=(); required_absent = all 6):
- `outcome_matched` ⇔ outcome == NOT_RULED_OUT
- `required_labels_present` ⇔ True (∅ ⊆ anything)
- `required_absent_labels_absent` ⇔ none of the 6 elimination labels attached
- `only_required_or_permitted_attached` ⇔ no labels attached (the redundant guarantee)

The two clauses (required_absent and only_required_or_permitted)
overlap for these cases but each catches a different failure mode:
required_absent catches an explicit elimination-label attachment;
only_required_or_permitted catches an unexpected new label class.
Both clauses are load-bearing in the general case (ORC-02..05 where
permitted_co is nonempty).

### 2.2 ORC-10 implementation note

CS notes the v0.2 ORC-10 carries a unique structure:
- `required_labels = ()` — no label required
- `permitted_co_labels = (boundary_proximity_flags only,)` — note: this is a NS-side phrasing referring to the diagnostic-only flag, not an elimination label
- `required_absent_labels = (TP,)` — the defining v1 regression check

CS implementation interpretation: `permitted_co_labels` in the
OracleCase dataclass holds elimination-label strings only.
`boundary_proximity_flags` are tracked separately on the
RungEvaluation (per Phase 3 outcome.py); they do not enter the
label-set match check.

So CS implements ORC-10 as:
- `required_labels = ()`
- `permitted_co_labels = ()`  (no co-labels permitted in the
  elimination-label set; this is the strict "no label" case)
- `required_absent_labels = ("accuracy_indistinguishable_from_token_prior",)`

And boundary_proximity_flag on the ENV criterion is reported in
the verification record as DIAGNOSTIC-ONLY context, never as a
label-set match factor.

If NS prefers a different interpretation of "boundary_proximity_flags
only" in `permitted_co_labels`, CS can extend the OracleCase
dataclass with a separate `permitted_boundary_proximity_flags`
field. CS proposes the simpler reading (boundary flags are
diagnostic-only and outside the label-set check) but flags this
for confirmation at the lock event.

### 2.3 ORC-12 boundary_proximity_flag interpretation

CS notes the v0.2 ORC-12 entry "permitted = boundary_proximity_flag
on ENV criterion expected-permitted" — CS interprets this as:

- The full-instrument outcome is NOT_RULED_OUT (no elimination label
  attaches in the strict-CI sense per the uniform principle).
- The ENV criterion's POINT ESTIMATE may sit on the eliminating
  side while the full CI straddles the boundary — that triggers
  `boundary_proximity_flag` on the ENV criterion (per joint
  disposition: boundary flag is "point on eliminating side; CI
  straddles").
- This is the DIAGNOSTIC record of the borderline case; the
  outcome stays NOT_RULED_OUT because the uniform principle
  resolves uncertainty toward NOT_RULED_OUT.

This matches the joint disposition's principled use of
boundary_proximity_flag. CS endorses.

---

## 3. Outstanding for full PH5-1 closure: T3 bounds declaration

The PH5-1 lock event requires BOTH:
1. **Oracle verdict table** (NS v0.2; CS co-signs THIS commit). ✓
2. **T3 bounds declaration** (the 6 sweep-parameter values: FLOOR
   value, CEIL value, TP margin, ENV margin, HEAD value, GAP value).
   NOT YET FILED.

CS notes from the v0.2 §"Dependencies to finalize":

> "the separation margin, envelope margin, abstention floor and
> ceiling values [all SWEEP-PARAMETER]; ORC-06/07/08 verdict
> arithmetic above assumes floor ≥ 0.20 and ceiling ≤ 0.95"

CS proposes the following bound rationales for NS+CS joint review
(NOT yet locked; CS posting for NS+TL discussion):

| Bound | CS proposed value | Rationale |
|---|---|---|
| FLOOR (NULL abstention floor) | 0.50 | High enough that universal_answerer (0/16 abstention) fails by clear margin; low enough that the ideal NULL CI [0.806, 1.000] passes by clear margin. |
| CEIL (answerable abstention ceiling) | 0.50 | Symmetric to FLOOR; universal_abstainer (80/80) fails by clear margin; ideal answerable (0/80) passes by clear margin. |
| TP_margin (token-prior separation) | 0.10 | Wider than the empirical ideal-random-emitter chance baseline (1/26 ≈ 0.038); narrow enough that a 1/26 emitter is detected. |
| ENV_margin (envelope separation) | 0.10 | Wider than expected single-policy hit rates (~0.20 for position policies); narrow enough that ENV-saturated shortcuts fire. |
| HEAD (measurement headroom) | 0.20 | Anchored at the D1×D7 squeeze; specific value awaits a more detailed CS analysis. |
| GAP (strict_content gap) | 0.20 | Anchored at the v1 strict-cliff observation; specific value awaits a more detailed CS analysis. |

CS notes the HEAD and GAP values are placeholders that NS should
refine with concrete rationales tied to the v1 instrument's
behavior. CS proposes deferring HEAD and GAP bounds to a follow-up
NS+CS co-signature, while locking FLOOR/CEIL/TP_margin/ENV_margin
at this lock event (they suffice to evaluate every v0.2 oracle case).

Alternatively, CS could lock all six at the same event; CS holds
for NS direction.

---

## 4. Anti-tuning attestation

CS confirms:

- **NO threshold value, criterion comparison rule, or A6 tolerance
  has been adjusted in response to Phase 5 run-1 outcomes.** The
  6-criterion T3 set was declared in D2-APPROVED v0.2 §B before
  Phase 5 run-1. The uniform comparison principle was declared
  before Phase 5 run-1. The A6 tolerance (0.05) was declared in
  D2 materials v0.2 §2 before Phase 5 run-1.

- **Oracle verdict expectations in v0.2 are defined against the
  FULL 6-criterion set only.** The TL filter §1 RC-1 noted that
  Phase 5 run-1 used a reduced criteria set; v0.2 explicitly
  refuses to define expectations against that reduced set.

- **CS run-1 artifacts are quarantined from the v0.2 bound
  declarations.** The bounds CS proposes in §3 above are derived
  from the structural rationales (chance baseline; ideal-corner CI;
  expected single-policy hit rates), not from run-1 numeric
  outcomes.

- **Anti-tuning enforcement at code level** lands via the PH5-4
  pre-flight precondition: the validation cannot proceed unless
  the locked verdict-table hash and bounds hash are present in
  the validation config.

---

## 5. CS posture

```text
NS Oracle Expected-Verdict Declaration v0.2:    CO-SIGNED IN FULL
  sha256:                                       a5d95065c497025b9d07f3b65ffd6d6477a5f94a70323f4abf462a810df32f85

CS implementation alignment:                    CONFIRMED
  match_oracle_verdict 4-clause predicate       per co-signature memo §5
  ORC-10 implementation interpretation          documented (§2.2);
                                                 awaits NS confirmation
  ORC-12 boundary_proximity interpretation      documented (§2.3)

PH5-1 lock event progress:
  Verdict table side:                           CS CO-SIGNED THIS COMMIT
  T3 bounds declaration side:                   PENDING NS+CS joint work
                                                 (CS proposed bounds in §3)

CS requests:
  - NS confirmation on ORC-10 boundary_proximity_flags interpretation
  - NS proposal on T3 bounds (or NS+CS joint lock event for all 6 bounds)
  - On bounds completion: PH5-1 fully closes; CS implements PH5-2
    (match predicate already specified), PH5-3 (stratified recipe),
    PH5-4 (pre-flight precondition with both hashes)
  - On PH5-2/3/4 complete: TL+Manager corrective re-run authorization

LOCK-RECORD:                                    PENDING
All execution gates:                            CLOSED
```

CS holds for NS bounds proposal + TL filter on this co-signature.

— CS Engineer, 2026-06-11
