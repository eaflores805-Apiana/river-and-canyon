# CS Co-Signature — Phase 5 Corrective Disposition (NS-drafted v0.1)

```text
DRAFT / REVIEW ONLY
CS CO-SIGNATURE ON JOINT CORRECTIVE PROPOSAL
NO MODEL INVOKED -- NO MODEL LOADED
NO SWEEP_ID -- NO SWEEP EXECUTION
NO CANDIDATE/MODEL OUTPUTS -- LOCK-RECORD REMAINS PENDING
```

From: CS Engineer
To: Team Lead
Cc: New Senior Engineer, Senior Engineer, Manager
Date: 2026-06-11
Re: CS co-signature + implementability assessment of NS-drafted Phase 5 Corrective Disposition Proposal v0.1 (mirror at `governance/2026-06-11_lane-1a-prime/NEW-SENIOR-PHASE5-CORRECTIVE-DISPOSITION-PROPOSAL-v0.1-2026-06-11.md`, sha256 `542a52b2…`)
Status: CS co-signs with no changes; requests corrective Phase 5 re-run authorization

---

## 0. Co-signature verdict (one line)

```text
CS CO-SIGNS the NS-drafted Phase 5 Corrective Disposition Proposal
v0.1 in full. All five corrective items (PH5-1 through PH5-5) are
implementable without reopening Phases 1-4.
```

---

## 1. Accept / reject / modify RC-1

**ACCEPT in full.**

NS's RC-1 framing — "Phase 5 evaluated a reduced criteria set …
joint expected-verdict + bounds lock event was never held … Phase 5
ran on a CS-local verdict table instead" — is exactly the gap CS
flagged in the alignment observations memo (commit `d23b063` §2.1–2.3).

NS's three concrete consequences (a/b/c) are correct:
- (a) non-abstaining shortcuts eliminated via NULL floor because it was the only live eliminative path
- (b) malformed_control mismatched because CS+NS tables disagreed on semantics; the criteria that would test the question weren't running
- (c) mixture proximity flag absent because the envelope criterion wasn't in the run

The root cause is unambiguous: CS ran with a CS-local 2-criterion
default set instead of waiting for the joint NS+CS lock event on
the full 6-criterion set + 12-case oracle table + locked bounds.

CS root-cause acknowledgement (from alignment observations memo
§4): CS did not poll `apiana-papers/C6_Proposal/` between Team
Lead Phase 4 PASS and Phase 5 execution. The mitigation that should
follow (PH5-4 below) makes this kind of skip mechanically impossible
at re-run time.

## 2. Accept / reject / modify RC-2

**ACCEPT in full.** CS modifies my own original proposal's correction
recommendation to ADOPT NS's stratified-recipe correction.

NS's RC-2 framing — "structural hit-rates are currently per-draw
random variables, not construction constants" — is more principled
than CS's original "identical seeds" proposal. CS's identical-seeds
correction would trivially produce drift=0 but would not exercise
A6's drift-detection mechanism at all. NS's stratified-recipe
correction produces drift=0 **by construction** (structural hit-rates
are recipe constants), and A6 then verifies **implementation
fidelity** rather than sampling luck. That is the right semantic.

CS quantitative confirmation of the drift mechanism (already in CS
proposal §1.2):
- pure_last_position drift 0.1375 ≈ 3σ at N=80 under uniform
  random position placement
- The position-based policy's hit-rate is per-draw random because
  the recipe leaves gold-position assignment to chance
- A6 correctly flagged this with the joint-disposition tolerance

The recipe fix removes the per-draw randomness; A6 will then
verify only "did pilot and final score the same on identical
structural draws" — implementation fidelity, not sampling luck.

---

## 3. Stratified recipe — implementable without reopening Phases 1–4

**CONFIRMED implementable.** Change is localized to one module +
one test file.

| Module | Change |
|---|---|
| `lane1a_prime/validation.py::ManifestRecipe` | Add stratification fields: `n_at_last_position`, `n_at_salient_endpoint`, `n_in_prefix_neighborhood`, `n_at_none` (sum = `n_answerable`). All [SWEEP-PARAMETER]. |
| `lane1a_prime/validation.py::construct_pilot_manifests` | Replace uniform-shuffle position assignment with stratified placement: for each stratum, generate that many items with the gold pair placed in the corresponding structural position; shuffle within stratum. |
| `tests/test_validation.py` | Update `test_construct_pilot_manifests_*` to verify stratified counts; assert structural hit-rates equal recipe constants. |

**Phases 1–4 NOT touched:**
- Schema layer (manifest_schema.yaml): the schema already validates
  any conformant manifest record. Stratification is an internal
  recipe property, not a schema field.
- Policy / control typed boundaries: unchanged.
- Three-way outcome model: unchanged.
- Wilson / Newcombe–Wilson: unchanged.
- Runner / wrapper / lock_packet machinery: unchanged.
- LOCK-RECORD PENDING boundary: unchanged.

No re-test of Phases 1–4 required.

---

## 4. Verdict-table hash + bounds hash precondition — implementable

**CONFIRMED implementable.** Pattern-equivalent to
`PacketLockRefused` (IS-8 closure from Phase 4); CS implements as a
mechanical refusal in the validation pre-flight.

```python
# lane1a_prime/validation.py

class ValidationPreFlightRefused(Exception):
    """Raised when the validation pre-flight check refuses to proceed.

    Pattern-equivalent to PacketLockRefused; converts the "lock
    event held" procedural requirement into a code-level refusal.
    """
    pass


@dataclass(frozen=True)
class ValidationPreFlightConfig:
    """Required inputs for a validation run. The hashes guarantee
    that the verdict table and bounds were locked at the joint
    NS+CS co-signature event (not adjusted post-hoc)."""
    oracle_verdict_table_path: Path
    oracle_verdict_table_hash: str  # sha256 of the locked table bytes
    t3_bounds_path: Path
    t3_bounds_hash: str  # sha256 of the locked bounds
    co_signature_record_path: Path  # path to the CS+NS co-signature memo
    co_signature_record_hash: str  # sha256


def verify_pre_flight_config(config: ValidationPreFlightConfig) -> None:
    """Verify the on-disk files match the declared hashes.

    Raises ValidationPreFlightRefused if any hash mismatches or any
    required file is missing. Validation cannot proceed without this
    check passing.
    """
    for path, expected_hash, name in [
        (config.oracle_verdict_table_path, config.oracle_verdict_table_hash, "oracle verdict table"),
        (config.t3_bounds_path, config.t3_bounds_hash, "T3 bounds"),
        (config.co_signature_record_path, config.co_signature_record_hash, "co-signature record"),
    ]:
        if not path.exists():
            raise ValidationPreFlightRefused(
                f"Required pre-flight artifact missing: {name} at {path}"
            )
        actual = hashlib.sha256(path.read_bytes()).hexdigest()
        if actual != expected_hash:
            raise ValidationPreFlightRefused(
                f"{name} hash mismatch: declared {expected_hash}; actual {actual}"
            )
```

`run_full_instrument_oracle_validation` (and the top-level
`run_validation.py`) call `verify_pre_flight_config()` first. The
function MUST raise if the lock event was not held; the pre-flight
cannot be silently skipped.

CS unit test: `test_validation_pre_flight_refuses_missing_artifact`,
`test_validation_pre_flight_refuses_hash_mismatch`,
`test_validation_pre_flight_proceeds_when_hashes_match`.

---

## 5. required_labels / permitted_co_labels / required_absent_labels — implementable

**CONFIRMED implementable.** Change is localized to one dataclass +
one match function + tests.

```python
# lane1a_prime/oracle_cases.py

@dataclass(frozen=True)
class OracleCase:
    """A synthetic oracle case for full-instrument validation."""
    oracle_case_id: str
    oracle_case_type: str
    expected_outcome: str          # one of RUNG_OUTCOME_VALUES
    required_labels: tuple[str, ...]      # MUST attach
    permitted_co_labels: tuple[str, ...]  # MAY also attach
    required_absent_labels: tuple[str, ...]  # MUST NOT attach
    description: str
```

```python
# lane1a_prime/validation.py

@dataclass(frozen=True)
class OracleVerification:
    """Per-case verification result with full label-set accounting."""
    oracle_case_id: str
    oracle_case_type: str
    expected_outcome: str
    actual_outcome: str
    required_labels: tuple[str, ...]
    permitted_co_labels: tuple[str, ...]
    required_absent_labels: tuple[str, ...]
    attached_labels: tuple[str, ...]
    outcome_matched: bool
    required_labels_present: bool
    required_absent_labels_absent: bool
    only_required_or_permitted_attached: bool
    overall_matched: bool
    failure_interpretation: str


def match_oracle_verdict(
    oracle_case: OracleCase,
    actual_outcome: str,
    attached_labels: frozenset[str],
) -> OracleVerification:
    """Full label-set match predicate per joint disposition.

    A case passes iff:
      1. actual_outcome == expected_outcome
      2. every label in required_labels is in attached_labels
      3. no label in required_absent_labels is in attached_labels
      4. every label in attached_labels is in required_labels
         ∪ permitted_co_labels
    """
    outcome_matched = actual_outcome == oracle_case.expected_outcome
    required_labels_present = (
        set(oracle_case.required_labels).issubset(attached_labels)
    )
    required_absent_labels_absent = (
        not (set(oracle_case.required_absent_labels) & attached_labels)
    )
    allowed = set(oracle_case.required_labels) | set(oracle_case.permitted_co_labels)
    only_required_or_permitted_attached = attached_labels.issubset(allowed)
    overall_matched = (
        outcome_matched
        and required_labels_present
        and required_absent_labels_absent
        and only_required_or_permitted_attached
    )
    failure = ""
    if not overall_matched:
        parts = []
        if not outcome_matched:
            parts.append(
                f"outcome {actual_outcome!r} != expected "
                f"{oracle_case.expected_outcome!r}"
            )
        if not required_labels_present:
            missing = sorted(set(oracle_case.required_labels) - attached_labels)
            parts.append(f"required labels not attached: {missing}")
        if not required_absent_labels_absent:
            present = sorted(set(oracle_case.required_absent_labels) & attached_labels)
            parts.append(f"required-absent labels attached: {present}")
        if not only_required_or_permitted_attached:
            unexpected = sorted(attached_labels - allowed)
            parts.append(f"unexpected labels attached: {unexpected}")
        failure = "; ".join(parts)
    return OracleVerification(
        oracle_case_id=oracle_case.oracle_case_id,
        oracle_case_type=oracle_case.oracle_case_type,
        expected_outcome=oracle_case.expected_outcome,
        actual_outcome=actual_outcome,
        required_labels=oracle_case.required_labels,
        permitted_co_labels=oracle_case.permitted_co_labels,
        required_absent_labels=oracle_case.required_absent_labels,
        attached_labels=tuple(sorted(attached_labels)),
        outcome_matched=outcome_matched,
        required_labels_present=required_labels_present,
        required_absent_labels_absent=required_absent_labels_absent,
        only_required_or_permitted_attached=only_required_or_permitted_attached,
        overall_matched=overall_matched,
        failure_interpretation=failure,
    )
```

CS unit tests cover each predicate clause independently and the
combined `overall_matched` rule.

---

## 6. Malformed_control as ORC-10 NOT_RULED_OUT with required-absence

**CONFIRMED.** CS co-signs NS's ORC-10 disposition:

```python
OracleCase(
    oracle_case_id="ORC-10",
    oracle_case_type="malformed_control_semantic_separation_guard",
    expected_outcome="not_ruled_out",
    required_labels=(),
    permitted_co_labels=(),
    required_absent_labels=("accuracy_indistinguishable_from_token_prior",),
    description=(
        "Semantic-separation guard. Behavior = perfect rebinding-"
        "following presented as candidate (post-scramble-gold). "
        "Verifies that the v1 mislabeling cannot recur: with the "
        "corrected control specs, rebinding-following must NOT "
        "fire the token-prior label."
    ),
)
```

CS confirms NS's framing: a case that "must eliminate" is the job
of ORC-02..ORC-05 (the declared shortcut oracles) under the full
T3 set. ORC-10's purpose is regression on the v1 mislabeling — a
PASS case with explicit required-absence on the token-prior label.

No new oracle case is needed for "malformed that eliminates"; the
declared shortcut oracles fill that role.

---

## 7. Full six-criterion T3 activation — implementable

**CONFIRMED implementable.**

```python
# lane1a_prime/analysis.py (revised under Path A)

# Uniform comparison principle per D2-APPROVED §B:
# elimination requires the FULL confidence interval on the
# eliminating side.

def apply_criterion(criterion, measurement):
    if criterion.is_floor:
        # Fires iff CI_UPPER < floor (entire CI below floor)
        value = measurement["ci_upper"]
        return value < criterion.floor_or_ceiling
    else:
        # Fires iff CI_LOWER > ceiling (entire CI above ceiling)
        value = measurement["ci_lower"]
        return value > criterion.floor_or_ceiling


DEFAULT_T3_CRITERIA = (
    EliminationCriterion(
        label="null_abstention_floor_unmet",
        stratum="null",
        comparison=CriterionComparison.CI_UPPER_BOUND,
        floor_or_ceiling=<LOCKED at co-signature>,
        is_floor=True,
    ),
    EliminationCriterion(
        label="answerable_abstention_ceiling_exceeded",
        stratum="answerable",
        comparison=CriterionComparison.CI_LOWER_BOUND,
        floor_or_ceiling=<LOCKED at co-signature>,
        is_floor=False,
    ),
    EliminationCriterion(
        label="accuracy_indistinguishable_from_token_prior",
        stratum="answerable",
        comparison=CriterionComparison.DIFFERENCE_INTERVAL,
        floor_or_ceiling=<LOCKED at co-signature>,
        is_floor=True,  # fires when difference UPPER < margin
    ),
    EliminationCriterion(
        label="accuracy_indistinguishable_from_declared_policy_envelope",
        stratum="answerable",
        comparison=CriterionComparison.DIFFERENCE_INTERVAL,
        floor_or_ceiling=<LOCKED at co-signature>,
        is_floor=True,
    ),
    EliminationCriterion(
        label="insufficient_measurement_headroom",
        stratum="answerable",
        comparison=CriterionComparison.CI_UPPER_BOUND,
        floor_or_ceiling=<LOCKED at co-signature>,
        is_floor=True,
    ),
    EliminationCriterion(
        label="strict_content_gap_instability",
        stratum="answerable",
        comparison=CriterionComparison.DIFFERENCE_INTERVAL,
        floor_or_ceiling=<LOCKED at co-signature>,
        is_floor=False,
    ),
)
```

Bound values are loaded from the locked T3 bounds file (hashed per
PH5-4 pre-flight check). Anti-tuning preserved: bounds locked once
at the co-signature event; no post-hoc adjustment.

---

## 8. Exact files expected to change

| File | Change |
|---|---|
| `lane1a_prime/oracle_cases.py` | Expand `OracleCase` with `required_labels`/`permitted_co_labels`/`required_absent_labels`. Add ORC-04, ORC-05 (recency_excluding_target_shortcut, prefix_neighbor_confusion_shortcut). Add ORC-11, ORC-12 (mixture shortcut-heavy / retrieval-heavy). Redefine ORC-10 per NS semantic. |
| `lane1a_prime/analysis.py` | Update `apply_criterion` to uniform principle (CI_UPPER for floor; CI_LOWER for ceiling; DIFFERENCE_INTERVAL upper-bound check for difference criteria). Expand `DEFAULT_T3_CRITERIA` to 6 criteria. Add `ValidationPreFlightConfig` + `ValidationPreFlightRefused` + `verify_pre_flight_config`. |
| `lane1a_prime/validation.py` | Update `ManifestRecipe` with stratification fields. Update `construct_pilot_manifests` to stratify gold position. Add `match_oracle_verdict` predicate. Update `OracleVerification` dataclass with full label-set fields. Update `run_full_instrument_oracle_validation` to call pre-flight + use match predicate + load locked verdict table + load locked bounds. |
| `validation/run_validation.py` | Load locked verdict table + bounds via `ValidationPreFlightConfig`. Use stratified recipe. Identical seed for pilot/final (irrelevant after stratification). Remove demo-tolerance fallback. |
| `validation/ORACLE_VERDICT_TABLE.json` (NEW) | 12 oracle cases × {oracle_case_id, oracle_case_type, expected_outcome, required_labels, permitted_co_labels, required_absent_labels, description}. CS+NS co-signed. Hashed into validation config. |
| `validation/T3_BOUNDS_DECLARATION.json` (NEW) | 6 criteria × {label, floor_or_ceiling}. Locked at co-signature event. Hashed into validation config. |
| `governance/2026-06-11_lane-1a-prime/CS-NS-CO-SIGNATURE-RECORD-2026-06-11.md` (NEW) | The CS+NS co-signature record memo for the verdict table + bounds; carries both signatures + the verdict-table sha256 + bounds sha256 + the rationale-block freezing pre-pilot. |
| `tests/test_validation.py` | Update for stratified recipe; new label-set match tests; pre-flight refusal tests. |
| `tests/test_analysis.py` | Update `apply_criterion` for uniform principle (CI bounds inverted from current implementation). |
| `tests/test_oracle_cases.py` (NEW) | Tests for the new ORCs and the expanded OracleCase dataclass. |

**Phases 1–4 NOT touched:** schemas, policy/control typed
boundaries, three-way outcome model, runner/wrapper/lock-packet
machinery, LOCK-RECORD PENDING boundary all remain accepted and
unchanged.

---

## 9. Supersession plan for Phase 5 run-1 artifacts

Per E11 retention discipline and TL §7:

| Action | Detail |
|---|---|
| Move run-1 outputs to retention directory | `experiments/2026-06-11_lane-1a-prime/validation/superseded_run-1/` contains: pilot_manifests_L01.json, final_manifests_L01.json, oracle_validation_results.json, t1_report.json, t3_report.json, t4_report.json, instrument_validation_report.md, execution_ledger.json |
| Retain a RUN-1-RETENTION.md | Documents the run-1 hashes (originals at commit `618e217`; A6-corrected at `b071b37`); reasons for re-pilot per E11; changed fields between iterations |
| `pilot_iteration_count` field in run-2 IVR | Set to 2 (one failed iteration retained; one successful iteration to come) |
| `reason_for_each_repilot` field in run-2 IVR | Verbatim per NS Q11: "reduced-criteria run; unlocked verdict table; unstratified recipe; A6 drift exceedance" |
| `changed_fields_between_pilots` field in run-2 IVR | Verbatim per NS Q10 + CS §8 above: recipe stratification; T3 criteria set 2→6 + comparison-direction uniform principle; oracle case table 9→12 + ORC-10 semantic; pre-flight hash precondition (new); match predicate (new); run_validation.py tolerance + seed strategy |

The failed run-1 IS NOT erased. It IS quarantined from numeric
contamination of the run-2 bounds (the bounds are declared from
pre-registered rationales per the anti-tuning attestation, not from
run-1 outcomes).

---

## 10. Confirmations

```text
No model was invoked.
No model was loaded.
No sweep_id was created.
No sweep execution occurred.
No candidate/model outputs were produced.
LOCK-RECORD remains PENDING.
```

CS confirms.

---

## 11. Implementability summary (NS Q10's process scope re-confirmed)

CS confirms NS Q10's framing: "Phases 1–4 acceptance is not reopened
… the changes are config, recipe, case declarations, and one
match-predicate function."

The corrective re-run is implementable as:

- **5 new T4 rows** (PH5-1 through PH5-5) — all OPEN, all CS-implementable
- **2 new artifacts** (oracle verdict table; T3 bounds; both hashed at lock event)
- **1 new co-signature record** (CS+NS; references both hashes)
- **2 module modifications** (analysis.py + validation.py + oracle_cases.py)
- **1 entry-point modification** (run_validation.py)
- **3 test-file updates** (test_validation.py + test_analysis.py + new test_oracle_cases.py)
- **Stratified recipe in validation.py::construct_pilot_manifests**
- **Pre-flight refusal in validation.py::run_full_instrument_oracle_validation**
- **Run-1 retention in superseded_run-1/ + retention block in run-2 IVR**

No re-test of Phases 1-4. Existing 211 Phase 1-4 tests remain green
across the change (verified before the corrective re-run).

---

## 12. CS request for corrective Phase 5 re-run authorization

Per TL §6 ("Corrective re-run: not yet authorized") and TL §13.5
("CS should return … whether corrective Phase 5 re-run is
requested"):

**CS REQUESTS corrective Phase 5 re-run authorization.**

The corrective re-run scope is exactly the joint NS+CS corrective
proposal (NS v0.1 mirrored at sha256 `542a52b2…`; CS co-signature
this file). The five PH5-* items are tractable as a single CS work
unit; sequencing:

1. NS+CS hold the joint lock event: declare the 12-case oracle
   verdict table, the 6-criterion T3 bounds, with attached
   rationales per criterion. CS+NS co-sign the record memo. The
   verdict table and bounds are hashed.

2. CS implements PH5-2 (label-set match predicate), PH5-3
   (stratified recipe), PH5-4 (pre-flight hash precondition).
   Existing 211 tests stay green; new tests added per §8.

3. CS executes the corrective Phase 5 re-run under D2 model-free
   validation scope (offline; deterministic; no model invocation).

4. Run-1 artifacts moved to `validation/superseded_run-1/`; run-2
   IVR carries the E11 retention block.

5. CS returns Phase 5 v0.2 completion summary with 17 required items.

Per the standing model-free validation scope confirmed by Manager
at the D2 disposition approval (TEAMLEAD-D2-WORK-ORDERING-DIRECTION;
commit `3398fa9`), this corrective re-run requires no fresh Manager
authorization for model-free validation; it stays within already-
granted D2 scope. **The Team Lead's specific corrective-re-run
authorization is what is being requested** so the work proceeds
under explicit TL direction rather than CS-initiated continuation.

---

## 13. CS posture

```text
NS-drafted corrective proposal:    CO-SIGNED IN FULL
CS implementability review:         all 5 PH5-items implementable
                                    without reopening Phases 1-4
CS modifies own proposal:           adopts NS stratified recipe over
                                    CS's identical-seeds correction
Anti-tuning attestation:            preserved (no tolerance change;
                                    bounds locked once at co-signature
                                    event; run-1 quarantined)

CS requests:                        corrective Phase 5 re-run
                                    authorization

CS holds for:                       TL filter on this co-signature +
                                    Manager / TL decision on
                                    corrective re-run

LOCK-RECORD:                       PENDING
All execution gates:                CLOSED
```

CS holds for joint return after TL filters this co-signature.

— CS Engineer, 2026-06-11
