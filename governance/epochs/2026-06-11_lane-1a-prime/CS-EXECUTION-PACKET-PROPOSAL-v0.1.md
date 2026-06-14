# CS Execution-Packet Proposal v0.1 — Lane 1a′

```text
DRAFT / REVIEW ONLY
D1 PACKET-PREPARATION ARTIFACT
NO EXECUTION AUTHORIZED
NO SWEEP_ID CREATED
NO MODEL RUNS
NO DATA GENERATED
NO VALIDATION OUTPUTS POPULATED
```

From: CS Engineer
To: Team Lead, New Senior Engineer
Cc: Senior Engineer, Contributor 5, Contributor 6, Manager
Date: 2026-06-11
Re: CS Execution-Packet Proposal v0.1 — Lane 1a′ (skeleton, per D1 packet-preparation authorization)
Status: DRAFT v0.1; structure and interfaces only; concrete values await New Senior design packet + T1–T4 plans

---

## 1. Scope

This proposal defines the **execution-side** of the Lane 1a′ packet at
the structure / interface / audit-scaffold level. It pairs with New
Senior's design packet + T1–T4 plans (which name semantic content);
this document names the runtime contract that those plans bind to.

Skeleton-quality. All concrete values that depend on the design packet,
T1–T4 plans, or downstream gate authorizations are marked `<placeholder>`
and are not finalized in v0.1.

Authority: D1 design authorization (Manager memo of 2026-06-11; commit
`d80ad4b`); Team Lead direction of 2026-06-11 (CS may begin CS-owned
proposal artifacts in skeleton form).

## 2. Inheritance from Lane 1a v1

**B1-equivalent provenance discipline (enumerated, not asserted; per v0.2 §2):**

1. Runner attestation (runner self-signs each generation event)
2. Artifact hashes (every output is hashed; hashes recorded in audit)
3. Append-only audit log (NDJSON; no in-place edits)
4. Lock / access timestamps (created_at, sealed_at, accessed_at)
5. Sidecar records (per-record metadata, byte-disjoint from runner output)
6. Model identity (MODEL_ID + tokenizer commit + framework version)
7. Prompt/config identity (prompt template hash + runner config hash)
8. Raw output preservation (runner output byte-preserved; no wrapper rewrite)
9. No wrapper-rewrite of runner-attested outputs (architectural invariant)

**Architectural inheritance (carried verbatim from v1):**

- Standalone generation runner. B1 v2 cannot consume this manifest family — established, not re-litigated.
- Interface-contract tests (sibling-artifact cross-reference rule, standing).
- Production-path subprocess smoke test (standing rule).
- G1-open production rule (standing).
- Ladder-order execution (carried).
- Append-only audit (carried).
- Locked plotting with code-level refusals (carried; this packet only authorizes the scaffolding; no plot is rendered under D1).

**Three standing CS production rules in force:**

| Rule | Where this proposal applies it |
|---|---|
| G1-open production rule | §16 G1-open check before every draft cycle |
| Sibling-artifact cross-reference | §11 cross-reference tests against B1 v2 / addendum / v1 sources |
| Production-path subprocess smoke test | §10 PRODUCTION_PYTHON + EXPECTED_MLX_LM_VERSION + smoke test |

## 3. Runner architecture

```text
lane1a_prime_runner.py
  MODEL_ID = "<placeholder; locked at packet via sibling-artifact rule>"
  ─ no implicit interpreter resolution: caller passes prompt + config
  ─ deterministic generation parameters (temperature, top_k, top_p, max_tokens) per v1 pattern
  ─ output: raw model output + minimal runner-attested fields
  ─ NEVER edits or appends to its own outputs after attestation

lane1a_prime_runner_wrapper.py
  PRODUCTION_PYTHON = "<placeholder; locked at packet>"
  EXPECTED_MLX_LM_VERSION = "<placeholder; locked at packet>"
  ─ subprocess invocation pattern carried from v1 Path E.1
  ─ wrapper does NOT rewrite runner output (architectural rule)
  ─ wrapper writes sidecar via write_sidecar() per record
```

Concrete `MODEL_ID`, interpreter path, and `mlx_lm` version values
are NOT specified in v0.1. They are locked at packet preparation
under the sibling-artifact cross-reference and production-path
subprocess smoke test rules; the test scaffolding in §10 and §11
enforces consistency at lock time.

## 4. Manifest interface contract

Skeleton schema (concrete field names await New Senior design packet):

```yaml
manifest_record:
  rung_id: <neutral; placeholder for v0.2 §4 ladder IDs L01..L08>
  context_block:
    padding_prefix: <placeholder; padding prepended per v0.2 §4>
    real_pair_block:
      start_idx: <placeholder; per IS-2 boundary labeling>
      end_idx:   <placeholder; per IS-2 boundary labeling>
      pairs:
        - key_token_ids: [...]    # token-id-sequence, per DE-3
          value_token_ids: [...]
  queried_key:
    key_token_ids: [...]          # canonical form per DE-3
  gold:
    value_token_ids: [...]
  stratum: answerable | null      # per v0.2 §4 stratum split
  metadata:
    construction_recipe_hash: <placeholder>
    pilot_or_final: pilot | final
```

**Critical interface invariants (CS-enforced at execution-packet stage):**

- The `real_pair_block` start/end indices are **explicit fields**, not
  computed at runtime. Policies that operate on the recency-relevant
  tail (e.g., `recency_excluding_target`, `prefix_neighbor_confusion`)
  read these indices directly — they do not attempt to infer the
  block from positional heuristics. (Closes IS-2 from CS v0.2 review.)
- `queried_key.key_token_ids` is the tokenizer-canonicalized form
  the equality predicate operates on. (Closes DE-3 / IS-9.)
- The schema is hashed and binds into the LOCK-RECORD via
  `manifest_schema_hash`.

Schema validator interface:

```python
def validate_manifest_record(record: dict, schema: ManifestSchema) -> ValidationResult:
    """
    Validates a single manifest record against the locked schema.
    Returns ValidationResult with pass/fail + per-field diagnostics.

    NOTE: this validator interface differs from B1 v2's flat-list
    manifest validator. Lane 1a' manifests inherit Lane 1a v1's
    nested-dict family. The interface deviation is established by
    v1 (see CS-DEVIATION-REPORT-B1V2-MANIFEST-INTERFACE-2026-06-10.md)
    and is not re-litigated here.
    """
```

## 5. Sidecar attestation pattern

Carried from v1 Path E.1 (`lane1a_runner_wrapper.py::write_sidecar()`).
The pattern in v0.1 skeleton form:

```python
def write_sidecar(record_id: str, runner_output_hash: str, lane1a_prime_metadata: dict) -> None:
    """
    Writes a sidecar record byte-disjoint from runner output.
    
    Invariant: write_sidecar() NEVER reads, edits, or rewrites runner output.
    The runner output is byte-preserved on disk; Lane 1a' metadata
    (rung_id, sweep_id, sidecar fields) lives only in the sidecar.
    """
```

Sidecar fields (placeholder skeleton; final list at packet lock):

```yaml
sidecar:
  record_id: <placeholder>
  runner_output_hash: <placeholder>
  sweep_id: <placeholder; NOT CREATED UNDER D1>
  rung_id: <placeholder>
  stratum: <placeholder>
  policies_applied: []           # policies that scored this record
  controls_applied: []           # controls that scored this record
  artifact_label: <placeholder>  # per E15; e.g., "RECONNAISSANCE — NON-BINDING — NOT FOR THRESHOLD DERIVATION"
  audit:
    written_at: <placeholder>
    written_by_wrapper_hash: <placeholder>
```

## 6. Policy execution interface (DE-1 blinding)

Per v0.2 §5 and CS v0.2 review DE-1, policy matching functions are
blinded to exact queried-key identity by **interface construction**,
not by wording.

```python
class PolicyInputView:
    """
    A view of a manifest record exposed to a policy matching function.
    
    INVARIANT: the queried-key token-id-sequence is NOT exposed on this view.
    Policies receive only the .candidates_excluding_queried_key list,
    which is computed by the interface itself before the policy is invoked.
    
    The interface guarantee:
      assert queried_key.key_token_ids not in [c.key_token_ids for c in view.candidates_excluding_queried_key]
    """
    record_id: str
    candidates_excluding_queried_key: list[ManifestPair]
    real_pair_block_indices: tuple[int, int]
    # NOT EXPOSED: queried_key (deliberately not a field)

def apply_policy(policy: Policy, record: ManifestRecord) -> PolicyOutput:
    view = PolicyInputView.from_record(record)  # interface excludes queried_key
    return policy(view)
```

**Required test:** `test_policy_view_excludes_queried_key` — for every
policy in the battery, `apply_policy` on the synthetic ideal-retriever
oracle scores 0 on the answerable items where retrieval would equal
self-match. (This is the structural complement to A5's oracle-case
pre-flight; v0.1 names the test, packet stage implements it.)

## 7. Control execution interface (DE-2 typed boundary)

Per v0.2 §6 "Mechanical rule: no elimination label may reference
`scrambled_binding_retrieval`, directly or indirectly" — CS implements
this as a typed boundary:

```python
class ControlOutput:
    """Output of a control. Not consumable by elimination-label code."""
    control_name: str
    value: float
    metadata: dict

class LabelInput:
    """Input to the elimination-label scoring code."""
    rung_id: str
    policy_outputs: list[PolicyOutput]
    # NO control_outputs field by type — controls cannot enter labeling

class DiagnosticInterpretation:
    """Output of diagnostic interpretation; informs reading, not labeling."""
    control_outputs: list[ControlOutput]
    policy_outputs: list[PolicyOutput]
    # consumed by interpretation/reporting, NOT by emit_elimination_label
```

**Required tests:**

- `test_label_input_does_not_carry_control_outputs` — type-level check that `LabelInput` has no field accepting `ControlOutput`.
- `test_emit_elimination_label_signature` — source-level grep asserts the elimination-label emitter accepts `LabelInput`, not any superset that could carry `ControlOutput`.
- `test_no_module_passes_control_output_to_labeler` — source-level grep asserts no call site routes a `ControlOutput` into `emit_elimination_label`.

This is the code-level enforcement of DE-2. Wording-only protection
is the weakest layer per the standing protection-layer taxonomy; this
section makes the diagnostic-only mark unrepresentable in the label
emission path.

## 8. Final-manifest re-verification (A6 + IS-7)

Per addendum A6 and CS v0.2 review IS-7:

```python
def a6_final_manifest_reverification(
    pilot_battery_scores: dict[str, float],
    pilot_envelope: float,
    final_manifest_hash: str,
    final_battery_scores: dict[str, float],
    final_envelope: float,
    declared_drift_tolerance: DriftTolerance,
) -> A6Result:
    """
    Per-policy and union-envelope re-verification on final locked manifests.
    
    Computes:
      drift_per_policy = abs(final - pilot) per policy
      drift_envelope = abs(final_envelope - pilot_envelope)
    
    Compares each drift against declared_drift_tolerance (PRE-DECLARED
    PER ANTI-TUNING RULE, IS-7).
    
    Returns A6Result with:
      caps_hold_on_final_manifests: bool
      per_policy_drift: dict[str, float]
      envelope_drift: float
      drift_within_tolerance: bool
      flagged_drifts: list[str]  # any drift exceeding tolerance
    """
```

**Drift tolerance pre-declaration (IS-7):** the tolerance values
(per-policy and envelope) are declared in the T1 declared-caps block
BEFORE pilot execution. Post-pilot tolerance change is a must-fix
event under the C1 disposition rule. (Anti-tuning rule, addendum §9.)

**Tolerance values:** `<placeholder>` — declared by Senior in T1 plan.

## 9. Operation-equivalence lock-time refusal (IS-8 structural)

Per v0.2 §5 "Operation-equivalence consequence" and CS v0.2 review IS-8:

```python
def lock_packet(packet: Packet) -> LockResult:
    """
    Lock-time refusal: structurally cannot proceed if any negative-battery
    policy is classified operation_equivalent.
    
    INVARIANT (hard refusal at code level):
      for policy in packet.negative_battery:
          if policy.classification == "operation_equivalent":
              raise PacketLockRefused(
                  f"Operation-equivalent policy {policy.name} in negative battery; "
                  f"removal or reclassification required before lock."
              )
    """
```

This converts the v0.2 §5 written consequence into a code-level lock
refusal — not a reviewer attestation. The refusal point fires between
A4 classification and packet seal; the LOCK-RECORD cannot reach
`SEALED` if the refusal triggers.

**Required test:** `test_lock_refuses_operation_equivalent_in_negative_battery`
— synthetic packet with one operation-equivalent dummy policy; assert
`lock_packet` raises `PacketLockRefused`.

## 10. Production-path subprocess smoke test (standing rule)

Carried from v1 Path E.1, applied to Lane 1a′:

```python
class TestProductionSubprocess:
    """
    Tests that the production subprocess invocation succeeds.
    
    Three required tests (carried from v1):
    
    test_interpreter_path_matches_config:
      cross-references lane1a_prime_runner_wrapper.PRODUCTION_PYTHON
      against runner_config.yaml production.python_interpreter.
    
    test_expected_mlx_lm_version_matches_config:
      cross-references the expected mlx_lm version.
    
    test_production_subprocess_smoke:
      spawns the production subprocess; runs
        import mlx_lm; from mlx_lm.sample_utils import make_sampler; print(mlx_lm.__version__)
      verifies the version equals expected.
    
    test_wrapper_does_not_use_sys_executable_for_subprocess:
      source-level grep asserts wrapper subprocess argv[0] is
      PRODUCTION_PYTHON, not sys.executable.
    """
```

Concrete `PRODUCTION_PYTHON` and `EXPECTED_MLX_LM_VERSION` values are
`<placeholder>` at v0.1; locked at packet preparation.

## 11. Sibling-artifact cross-reference tests (standing rule)

Carried from v1 Path A.1, applied to Lane 1a′:

```python
class TestSiblingArtifactCrossReference:
    """
    test_model_id_matches_<sibling>:
      reads sibling source directly; extracts MODEL_ID via regex;
      asserts equality with lane1a_prime_runner.MODEL_ID.
      Sibling source: <placeholder; New Senior design packet specifies
                       which sibling artifact Lane 1a' MODEL_ID binds to>.
    
    test_manifest_schema_shape_matches_recipe:
      reads the manifest recipe source directly; asserts the schema
      validator's required-field set matches the recipe's emitted-field set.
    
    test_addendum_path_constant_resolves:
      asserts addendum source-of-record path constant resolves to the
      adopted standing path
      (governance/standing/PRE-LOCK-INSTRUMENT-VALIDATION-ADDENDUM.md,
       sha256 124f6046... at adoption commit e76e7f8).
    
    test_paper3_tag_value_matches_d2_quote:
      reads Paper 3 v1.1 tag bytes; asserts the §D2 D2-ancestor quote
      is present verbatim (the v0.2 §8 R6 inheritance basis).
    """
```

## 12. Artifact labels (E15) — code-level enforcement

```python
def emit_artifact(artifact: Artifact, classification: ArtifactClassification) -> EmittedArtifact:
    """
    Artifact emission requires the appropriate label by interface construction.
    
    Label map (per addendum E15):
      ArtifactClassification.ORACLE_PILOT_CANARY  -> "SYNTHETIC — NON-BINDING — NOT FOR THRESHOLD DERIVATION"
      ArtifactClassification.SWEEP_OUTPUT         -> "RECONNAISSANCE — NON-BINDING — NOT FOR THRESHOLD DERIVATION"
                                                  | "DIAGNOSTIC — NON-BINDING — NOT FOR THRESHOLD DERIVATION"
                                                    (CS proposes RECONNAISSANCE for Lane 1a' per v0.2 §8)
    
    INVARIANT: emit_artifact REQUIRES classification; there is no code path
    that emits an artifact without a label.
    """
```

**Required test:** `test_emit_artifact_requires_label` — source-level
check that no call site emits an artifact without specifying
classification.

## 13. Pilot-iteration logging (E11)

Per addendum E11 and CS v0.2 review IS-6:

```yaml
pilot_iteration_log:
  pilot_iteration_count: <int>
  failed_pilot_records_retained:
    - iteration_index: <int>
      records: [<retained records of the failed pilot>]
      reason_for_repilot: <str>
      changed_fields_between_pilots: [<list of field names>]
  final_pilot:
    iteration_index: <int>
    records: [<final passing pilot>]
```

**Schema location:** to be housed at `governance/standing/templates/`
post-PA-3 from the addendum adoption. v0.1 here records the
field-level skeleton; the YAML schema definition lands in the
standing templates folder at PA-3 execution.

## 14. Audit log structure

Append-only NDJSON, carried from v1:

```
.audit.ndjson  (one line per event)

event_schema:
  ts: <ISO 8601>
  event_type: runner_invocation | sidecar_write | lock_attempt
            | a6_reverification | g1_open_check | policy_apply
            | control_apply | label_emit | artifact_emit
            | test_run | etc.
  state_before: <hash | enum>
  state_after:  <hash | enum>
  actor: <runner | wrapper | analysis_script | test_suite>
  metadata: {...}
```

**Invariant:** no in-place audit-log edits. Any correction is a new
append event. Audit log hash anchors into LOCK-RECORD.

## 15. Test scaffolding overview

| Test class | Concern | Standing rule rooted |
|---|---|---|
| Interface-contract tests | manifest, policy, control interfaces | sibling-artifact (Path A.1) |
| Sibling-artifact cross-reference | MODEL_ID, schema shapes, addendum path, Paper 3 D2 quote | sibling-artifact (standing) |
| Production-path subprocess smoke | interpreter resolution, mlx_lm version, import surface | production-path subprocess smoke (standing) |
| Policy zero-self-match | DE-1 + A5 oracle-case pre-flight | addendum A5 |
| Control no-elimination-reference | DE-2 typed boundary | addendum B-correction |
| Drift-tolerance | A6 + IS-7 | addendum A6 |
| Operation-equivalence lock-time refusal | IS-8 | addendum A4 / §5 consequence |
| Label-presence | E15 | addendum E15 |
| Audit-log append-only | provenance discipline | v1 + B1-equivalent |

Test counts and concrete fixtures `<placeholder>` at v0.1.

## 16. Cross-reference map: packet-stage concerns → proposal sections

| Source | Concern | Proposal section addressing it |
|---|---|---|
| v0.2 §10 #1 | exact prompt-shell content for `unconditioned_token_prior` | Awaits New Senior T2 plan; §4 manifest interface admits the field |
| v0.2 §10 #2 | manifest-schema labeling of real-pair-block boundary | **§4** (explicit start_idx/end_idx fields; closes IS-2) |
| v0.2 §10 #3 | mixture-oracle commit-and-hash ceremony | §11 sibling-artifact tests bind mixture-oracle hash into LOCK-RECORD; ceremony details await T1 plan |
| v0.2 §10 #4 | A6 final-manifest re-verification mechanics | **§8** (function signature + invariants + IS-7) |
| v0.2 §10 #5 | synthetic ideal-witness record format | Awaits New Senior T3 plan; §15 reserves test class |
| v0.2 §10 #6 | pilot-iteration logging schema/template location | **§13** (per-record skeleton) + PA-3 standing templates folder |
| v0.2 §10 #7 | validation artifact labels + evidence-bundle exclusion | **§12** (E15 code-level enforcement) + exclusion language artifact (separate document) |
| CS IS-7 | A6 drift tolerance pre-declaration | **§8** declared_drift_tolerance pre-declaration requirement |
| CS IS-8 | operation-equivalence lock-time hard refusal | **§9** `PacketLockRefused` raise + lock_packet invariant |
| CS IS-9 | equality-predicate veto path reservation | **§4** queried_key.key_token_ids comment; CS proposes no stricter rule at this time |

## 17. Non-authorizations

Refer to the companion artifact
`NON-AUTHORIZATION-CONSUMPTION-SIDE-EXCLUSION-LANGUAGE-v0.1.md` (CS, same
folder) for the verbatim block. Summary:

```text
No execution authorized.
No new sweep_id.
No model runs.
No data generation.
No execution packet execution.
No offline pilot execution.
No oracle pre-flight execution.
No candidate selection.
No candidate ranking.
No threshold-sheet work.
No certification evaluation.
No stress-retention testing.
No B1 v2.1 implementation.
No Paper 3 revision.
No Claim C activation.
No Fork A reactivation.
No Paper 6 activation.
No public benchmark packaging.
```

All execution gates remain CLOSED.

## 18. CS sign-off

```text
Proposal status:                  DRAFT v0.1 — skeleton form
D1 packet-preparation artifact:   YES
Execution authorized:             NO
sweep_id created:                 NO
Model runs:                       NO
Data generated:                   NO
Validation outputs populated:     NO

Next:                             cross-review with New Senior design
                                   packet + T1-T4 plans;
                                   incorporate interface concrete
                                   values once available;
                                   joint return to Manager at D2 gate

Dependencies on New Senior artifacts (placeholders to be replaced):
  - manifest schema field names (§4)
  - T2 control-spec field names (§7)
  - T1 declared drift tolerance values (§8)
  - T3 ideal-witness record format (§15)
  - design packet sibling-artifact identity (§11)

CS-owned artifacts at v0.1:
  - CS-EXECUTION-PACKET-PROPOSAL-v0.1.md (this file)
  - LOCK-RECORD-DRAFT-STRUCTURE-v0.1.md
  - NON-AUTHORIZATION-CONSUMPTION-SIDE-EXCLUSION-LANGUAGE-v0.1.md
```

— CS Engineer, 2026-06-11
