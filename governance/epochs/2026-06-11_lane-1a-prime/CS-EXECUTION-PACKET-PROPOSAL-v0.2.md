# CS Execution-Packet Proposal v0.2 — Lane 1a′

```text
DRAFT / REVIEW ONLY
D2 PACKAGE-ASSEMBLY ARTIFACT
NO D2 AUTHORIZATION GRANTED
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
Re: CS Execution-Packet Proposal v0.2 — Lane 1a′ (D2 package-assembly artifact)
Status: D2 package assembly — incorporates the 6 AL-* alignment carry-forward concerns and 3 CS notes (IS-7/8/9) into the v0.1 skeleton

---

**Supersession record.**
This document supersedes `CS-EXECUTION-PACKET-PROPOSAL-v0.1.md` (sha256 `af2b8dac…`). The v0.1 file remains on disk as historical record per "supersede, don't rewrite". v0.2 changes from v0.1 are catalogued in §0 below.

---

## 0. v0.1 → v0.2 changes

| Change | v0.1 location | v0.2 location | Source carry-forward |
|---|---|---|---|
| Banner change (D1 → D2 PACKAGE-ASSEMBLY) | top | top | Team Lead memo of 2026-06-11 §6 |
| Add `render_prompt()` interface + `--dry-run` flag | — | **§3.1** | **AL-Q1** |
| Add diagnostic-sidecar pattern for copy_completion + non-eliminating diagnostics | §5 (sidecar) | **§5.1** | **AL-Q4** |
| Make Layer 2 schema enforcement of DE-2 explicit (sidecar enum + per-rung schema + `additionalProperties: false`) | §7 (typed boundary only) | **§7.2** | **AL-Q2-schema** |
| IS-7 drift tolerance pre-declaration explicit reference | §8 | §8 (clarified) | **IS-7 CS note** |
| IS-8 operation-equivalence lock-time hard refusal explicit reference | §9 | §9 (clarified) | **IS-8 CS note** |
| IS-9 equality-predicate veto reservation explicit reference | §4 (queried_key comment) | §4 (clarified) | **IS-9 CS note** |
| §16 cross-reference map updated with v0.2 incorporations | §16 | **§16** (updated) | this document |
| Companion artifact references updated to v0.2 | §17 | §17 | this document |
| **Cross-references to NS bundle updated from v0.2 to v0.3** | various | various | **NS D2 supersession of 2026-06-11 (Bundle v0.3 sha256 `03564001…`)** |

No section is structurally removed from v0.1. All v0.1 invariants
remain in force in v0.2. CS-EP v0.2 was drafted while New Senior was
in parallel shipping Bundle v0.3 (the D2 package-assembly supersession
of Bundle v0.2); references in this document now point to Bundle v0.3
rather than v0.2. NS Bundle v0.3 Part VIII cross-review record
documents 1:1 ALIGNED mapping between Bundle v0.3 design rows and
CS-EP v0.2 / LOCK-RECORD v0.2 mechanisms (closes the design-side
acknowledgement of CS work).

---

## 1. Scope

This proposal defines the **execution-side** of the Lane 1a′ packet at
the structure / interface / audit-scaffold level. It pairs with New
Senior's D2 Design-Packet Bundle v0.3 (sha256 `03564001ffce4b6f8bf35cd20f6542e1952543abf06c8e9095b06c144e2f4d31`,
which supersedes Bundle v0.2 sha256 `a9615dac…`); this document names
the runtime contract that bundle binds to.

D2 package-assembly artifact. All concrete values that depend on
later gates remain `<placeholder>`. No execution authorized.

Authority: D1 design authorization (Manager memo of 2026-06-11; commit
`d80ad4b`); Team Lead D2 package assembly authorization of 2026-06-11.

## 2. Inheritance from Lane 1a v1 (unchanged from v0.1)

**B1-equivalent provenance discipline (enumerated per Bundle v0.3 §I.8):**

1. Runner attestation
2. Artifact hashes
3. Append-only audit log
4. Lock / access timestamps
5. Sidecar records
6. Model identity
7. Prompt / config identity
8. Raw output preservation
9. No wrapper-rewrite of runner-attested outputs

Three standing CS production rules in force: G1-open; sibling-artifact cross-reference; production-path subprocess smoke test.

## 3. Runner architecture

Same as v0.1:

```text
lane1a_prime_runner.py
  MODEL_ID = "<placeholder; locked at packet via sibling-artifact rule>"
  deterministic generation parameters per v1
  output: raw model output + minimal runner-attested fields
  NEVER edits its own outputs after attestation

lane1a_prime_runner_wrapper.py
  PRODUCTION_PYTHON = "<placeholder; locked at packet>"
  EXPECTED_MLX_LM_VERSION = "<placeholder; locked at packet>"
  subprocess invocation per Path E.1
  writes sidecar via write_sidecar() per record
```

### 3.1 No-model assembly dry-run (NEW for v0.2, AL-Q1)

The runner module exposes a pure-function `render_prompt()` callable
directly (no subprocess, no model). Used by:

- the interface-contract test (Path A.1 carry) at packet-stage pre-lock;
- the wrapper's `--dry-run` flag for end-to-end assembly verification
  without any generation event.

```python
def render_prompt(record: ManifestRecord) -> RenderedPrompt:
    """
    Renders a prompt for a single manifest record using the locked
    template. Pure function; no model invocation; no I/O beyond
    reading the record and template.
    """

class RenderedPrompt:
    text: str
    template_id_hash: str     # hash-locked at packet seal; sibling-artifact rule
    record_id: str
    conformance_check: ConformanceResult
```

Wrapper-side dry-run mode:

```python
parser.add_argument("--dry-run", action="store_true",
                    help="Render prompts and conformance-check; do not invoke model.")
```

In dry-run mode:
- `write_sidecar()` is bypassed (no model output exists to attest).
- Output goes to a dry-run report file with label
  `SYNTHETIC — NON-BINDING — NOT FOR THRESHOLD DERIVATION` and
  sub-classifier `dry_run: true`.
- **No `sweep_id` is created.** Dry-run is pre-lock interface testing
  and inherits the no-sweep_id rule at every level.

**Required tests (v0.2):**

- `test_render_prompt_pure` — no I/O beyond record + template read; deterministic for fixed inputs.
- `test_dry_run_does_not_invoke_model` — source-level grep on wrapper invocation path under `--dry-run` asserts no subprocess invocation reaches the model entrypoint.
- `test_dry_run_does_not_create_sweep_id` — assertion that dry-run output carries `sweep_id: null`.

## 4. Manifest interface contract

Same schema as v0.1:

```yaml
manifest_record:
  rung_id: <neutral; placeholder for Bundle v0.3 §I.3 ladder IDs L01..L08>
  context_block:
    padding_prefix: <placeholder; padding prepended per Bundle v0.3 §I.3>
    real_pair_block:
      start_idx: <placeholder; per IS-2 boundary labeling>
      end_idx:   <placeholder; per IS-2 boundary labeling>
      pairs:
        - key_token_ids: [...]    # token-id-sequence, per IS-9
          value_token_ids: [...]
  queried_key:
    key_token_ids: [...]
  gold:
    value_token_ids: [...]
  stratum: answerable | null
  metadata:
    construction_recipe_hash: <placeholder>
    pilot_or_final: pilot | final
```

**IS-9 equality-predicate veto reservation (clarified v0.2):**
`queried_key.key_token_ids` is the tokenizer-canonicalized form the
equality predicate operates on. CS currently proposes no stricter
rule than token-id-sequence equality after tokenizer canonicalization
(per Bundle v0.3 §I.4). CS reserves the option at packet stage if
unicode-normalization, byte-fallback, or tokenizer-version-drift edge
cases surface during pilot construction; the Bundle v0.3 §I.4 *"unless
CS proposes stricter"* clause routes such a proposal cleanly through D2
review. Bundle v0.3 §I.4 explicitly cites this as IS-9 reservation.

## 5. Sidecar attestation pattern

```python
def write_sidecar(record_id: str, runner_output_hash: str, lane1a_prime_metadata: dict) -> None:
    """
    Writes a sidecar record byte-disjoint from runner output.

    Invariant: write_sidecar() NEVER reads, edits, or rewrites runner output.
    """
```

Runner-attested sidecar fields (skeleton; final at packet lock):

```yaml
sidecar:
  record_id: <placeholder>
  runner_output_hash: <placeholder>
  sweep_id: <placeholder; NOT CREATED UNDER D2 PACKAGE ASSEMBLY>
  rung_id: <placeholder>
  stratum: <placeholder>
  policies_applied: []
  controls_applied: []
  elimination_label_basis:    # see §7.2 enum constraint
    basis_policies: []
  artifact_label: <placeholder>  # e.g., "RECONNAISSANCE — NON-BINDING — NOT FOR THRESHOLD DERIVATION"
  audit:
    written_at: <placeholder>
    written_by_wrapper_hash: <placeholder>
```

### 5.1 Diagnostic sidecar pattern (NEW for v0.2, AL-Q4)

For non-eliminating diagnostics — currently `copy_completion`
agreement-rate and any future diagnostic added without entering the
union envelope — a separate diagnostic sidecar pattern.

```yaml
diagnostic_sidecar:
  record_id: <placeholder>
  diagnostic_class: copy_completion_agreement | ...
  artifact_class: lane-1a-prime-diagnostic
  artifact_label: "DIAGNOSTIC — NON-BINDING — NOT FOR THRESHOLD DERIVATION"
  per_item:
    - item_id: <placeholder>
      diagnostic_value: <placeholder>      # e.g., agreement: 1 | 0
      runner_output_ref: <placeholder>     # link to runner-attested sidecar
  audit:
    written_at: <placeholder>
    written_by_wrapper_hash: <placeholder>
```

**Code-level invariant:** the diagnostic-sidecar reader cannot feed
the union-envelope computation. The union-envelope computation
function accepts only inputs of type `EnvelopePolicyOutput`, which is
disjoint from `DiagnosticSidecar`. This is the structural equivalent
of the §7 typed-boundary pattern, applied to keep `copy_completion`
outside the union envelope by construction.

**`copy_completion` placement is the diagnostic sidecar.** Per
Bundle v0.3 §I.4: *"`copy_completion` outside the union envelope as a
candidate-output-pattern (agreement-rate) diagnostic unless a
separate pre-registered diagnostic is defined"*. CS endorses; the
diagnostic-sidecar pattern is the implementation home.

**Required tests:**

- `test_diagnostic_sidecar_disjoint_from_envelope` — type-level check that no envelope-policy function signature accepts `DiagnosticSidecar`.
- `test_copy_completion_writes_diagnostic_sidecar_only` — code-path check that `copy_completion`'s output flows to the diagnostic sidecar and not the runner-attested sidecar's `policies_applied` list.

## 6. Policy execution interface (DE-1 blinding)

Same as v0.1:

```python
class PolicyInputView:
    """
    INVARIANT: queried-key token-id-sequence NOT exposed on this view.
    Interface guarantee:
      assert queried_key.key_token_ids not in [c.key_token_ids for c in view.candidates_excluding_queried_key]
    """
    record_id: str
    candidates_excluding_queried_key: list[ManifestPair]
    real_pair_block_indices: tuple[int, int]

def apply_policy(policy: Policy, record: ManifestRecord) -> PolicyOutput:
    view = PolicyInputView.from_record(record)
    return policy(view)
```

**Required test:** `test_policy_view_excludes_queried_key`.

## 7. Control execution interface (DE-2 typed boundary)

Per Bundle v0.3 §I.5 and §III T2 row `eliminative_status` for
`scrambled_binding_retrieval`: *"none — mechanical rule: no
elimination label may reference it, directly or indirectly"*. CS
implements this rule at **three machine layers**.

### 7.1 Layer 1 — typed boundary (carried from v0.1)

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
```

**Layer 1 tests:**
- `test_label_input_does_not_carry_control_outputs`
- `test_emit_elimination_label_signature`
- `test_no_module_passes_control_output_to_labeler`

### 7.2 Layer 2 — schema enforcement (NEW for v0.2, AL-Q2-schema)

Sidecar schema constraint on `elimination_label_basis`:

```yaml
elimination_label_basis:
  type: object
  additionalProperties: false
  properties:
    basis_policies:
      type: array
      items:
        type: string
        enum:
          - pure_last_position
          - salient_endpoint
          - recency_excluding_target
          - prefix_neighbor_confusion
          # NOTE: copy_completion is OMITTED (outside union envelope
          #       per Bundle v0.2 §I.4; not an elimination basis).
          # NOTE: NO control names appear in this enum.
          #       scrambled_binding_retrieval is STRUCTURALLY
          #       UNREPRESENTABLE here.
```

Per-rung result schema constraint on `elimination_basis_refs`:

```yaml
rung_result:
  type: object
  additionalProperties: false
  properties:
    elimination_basis_refs:
      type: array
      additionalProperties: false
      items:
        type: object
        additionalProperties: false
        properties:
          policy_id:
            type: string
            enum: [pure_last_position, salient_endpoint,
                   recency_excluding_target, prefix_neighbor_confusion]
          # control_id field DELIBERATELY ABSENT;
          # cannot be added by additionalProperties: false rule.
```

The DE-2 mechanical rule becomes a **schema-level structural
unrepresentability**. JSON-schema validation refuses any sidecar or
rung result that attempts to reference `scrambled_binding_retrieval`
in an elimination context.

**Layer 2 tests:**
- `test_sidecar_schema_rejects_control_in_basis_policies` — submit a sidecar with `basis_policies: [scrambled_binding_retrieval]`; expect schema rejection.
- `test_rung_result_schema_rejects_control_id_field` — submit a rung result with `elimination_basis_refs: [{control_id: ...}]`; expect schema rejection by `additionalProperties: false`.

### 7.3 Layer 3 — analyzer check (carried from v0.1)

Source-level grep + reachability analyzer in the analysis script:
- No call site routes a `ControlOutput` (or any field carrying a control name) into the elimination-label code path.
- Pre-lock analyzer scans for any reference to `scrambled_binding_retrieval` inside any function reachable from `emit_elimination_label`.

**Together (Layer 1 + 2 + 3):** the DE-2 rule lands at code + schema +
analyzer. Review-only is rejected as insufficient per the standing
protection-layer taxonomy.

## 8. Final-manifest re-verification (A6 + IS-7)

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
    Returns A6Result with:
      caps_hold_on_final_manifests: bool
      per_policy_drift: dict[str, float]
      envelope_drift: float
      drift_within_tolerance: bool
      flagged_drifts: list[str]
    """
```

**IS-7 drift tolerance pre-declaration (clarified v0.2):** the
tolerance values (per-policy and envelope) are declared in the T1
declared-caps block BEFORE pilot execution. Anti-tuning rule
applies. Post-pilot tolerance change is a must-fix event requiring
C1 disposition. Tolerance values remain `<placeholder>` in this v0.2
artifact; New Senior's T1 plan owns the declaration; CS verifies the
pre-declaration timestamp at packet seal.

## 9. Operation-equivalence lock-time refusal (IS-8 structural)

```python
def lock_packet(packet: Packet) -> LockResult:
    """
    INVARIANT (hard refusal at code level):
      for policy in packet.negative_battery:
          if policy.classification == "operation_equivalent":
              raise PacketLockRefused(
                  f"Operation-equivalent policy {policy.name} in negative battery; "
                  f"removal or reclassification required before lock."
              )
    """
```

**IS-8 (clarified v0.2):** this is the code-level conversion of
Bundle v0.3 §I.4 *"Operation-equivalence consequence"*. Bundle v0.3
explicitly cites the CS lock-time hard-refusal mechanism inline:
*"(IS-8: CS implements this as a lock-time hard refusal at code
level — a battery containing an operation-equivalent policy cannot
seal.)"* The refusal fires between A4 classification and packet
seal; LOCK-RECORD cannot reach `SEALED` if the refusal triggers.

**Required test:** `test_lock_refuses_operation_equivalent_in_negative_battery`.

## 10. Production-path subprocess smoke test (unchanged from v0.1)

Path E.1 pattern carried; `PRODUCTION_PYTHON`, `EXPECTED_MLX_LM_VERSION`
locked at packet stage.

## 11. Sibling-artifact cross-reference tests (unchanged from v0.1)

Path A.1 pattern carried.

New tests added in v0.2:

- `test_template_id_hash_matches_locked_template` — `RenderedPrompt.template_id_hash` cross-referenced against the locked template at lock time (closes part of AL-Q1).

## 12. Artifact labels (E15) — code-level enforcement

```python
def emit_artifact(artifact: Artifact, classification: ArtifactClassification) -> EmittedArtifact:
    """
    Label map (per addendum E15):
      ORACLE_PILOT_CANARY -> "SYNTHETIC — NON-BINDING — NOT FOR THRESHOLD DERIVATION"
      SWEEP_OUTPUT        -> "RECONNAISSANCE — NON-BINDING — NOT FOR THRESHOLD DERIVATION"
      DIAGNOSTIC_SIDECAR  -> "DIAGNOSTIC — NON-BINDING — NOT FOR THRESHOLD DERIVATION"
                              (NEW for v0.2: covers AL-Q4 diagnostic sidecars)
    """
```

(Per Bundle v0.3 §I.7 + CS Non-Auth Language v0.2 §6.)

## 13. Pilot-iteration logging (E11) (unchanged from v0.1)

Schema location: `governance/standing/templates/` post-PA-3 from
addendum adoption.

## 14. Audit log structure (unchanged from v0.1)

Append-only NDJSON; per-record timestamp + state + hash.

## 15. Test scaffolding overview

| Test class | Concern | Standing rule rooted |
|---|---|---|
| Interface-contract tests | manifest, policy, control interfaces | sibling-artifact |
| Sibling-artifact cross-reference | MODEL_ID, schema shapes, addendum path, Paper 3 D2 quote, template hash | sibling-artifact |
| Production-path subprocess smoke | interpreter, mlx_lm version, import surface | subprocess smoke |
| Policy zero-self-match | DE-1 + A5 | addendum A5 |
| Control no-elimination-reference | DE-2 typed boundary + schema enum + analyzer | DE-2 |
| Drift-tolerance | A6 + IS-7 | addendum A6 |
| Operation-equivalence lock-time refusal | IS-8 | addendum A4 / consequence |
| Label-presence | E15 | addendum E15 |
| Audit-log append-only | provenance discipline | v1 + B1-equivalent |
| **Assembly dry-run (NEW v0.2)** | **§3.1 render_prompt purity + no-model invocation** | **AL-Q1** |
| **Schema rejection (NEW v0.2)** | **§7.2 sidecar/rung schema rejects control_id** | **AL-Q2-schema** |
| **Diagnostic sidecar disjointness (NEW v0.2)** | **§5.1 type-level check; envelope cannot consume diagnostic** | **AL-Q4** |

## 16. Cross-reference map: packet-stage concerns → v0.2 sections

| Source | Concern | v0.2 location |
|---|---|---|
| Bundle v0.3 §VI #1 | exact prompt-shell content for `unconditioned_token_prior` | T2 (NS) + §4 manifest interface admits the field |
| Bundle v0.3 §VI #2 | manifest-schema labeling of real-pair-block boundary | **§4** (explicit start_idx/end_idx) |
| Bundle v0.3 §VI #5 #3 | mixture-oracle commit-and-hash ceremony | §11 sibling-artifact tests bind mixture-oracle hash into LOCK-RECORD; ceremony at T1 plan |
| Bundle v0.3 §VI #5 #4 | A6 final-manifest re-verification mechanics | **§8** |
| Bundle v0.3 §VI #5 #5 | synthetic ideal-witness record format | T3 (NS) + §15 reserves test class |
| Bundle v0.3 §VI #5 #6 | pilot-iteration logging schema/template location | **§13** + standing templates folder |
| Bundle v0.3 §VI #5 #7 | validation artifact labels + evidence-bundle exclusion | **§12** + Non-Auth Language v0.2 §8 |
| Alignment AL-Q1 | runner dry-run | **§3.1 NEW** |
| Alignment AL-Q2-schema | Layer 2 schema enforcement of DE-2 | **§7.2 NEW** |
| Alignment AL-Q4 | diagnostic sidecar for copy_completion | **§5.1 NEW** |
| Alignment AL-Q5-opt | LOCK-RECORD validation_artifact_hashes | LOCK-RECORD v0.2 §2.1 NEW |
| Alignment AL-INH-1 co-own | CS co-ownership of per-stratum aggregation in analysis script | T1 plan + analysis_script (CS) |
| Alignment AL-INH-2 co-own | CS co-ownership of outcome-chooser code + fixed-language | T1 plan + outcome_chooser (CS) |
| CS IS-7 | A6 drift tolerance pre-declaration | **§8** (clarified v0.2) |
| CS IS-8 | operation-equivalence lock-time hard refusal | **§9** (clarified v0.2) |
| CS IS-9 | equality-predicate veto reservation | **§4** (clarified v0.2) |

## 17. Non-authorizations

Refer to companion artifact `NON-AUTHORIZATION-CONSUMPTION-SIDE-EXCLUSION-LANGUAGE-v0.2.md`.

Summary:

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
Proposal status:                  DRAFT v0.2 — D2 package-assembly artifact
D2 authorization granted:         NO
Execution authorized:             NO
sweep_id created:                 NO
Model runs:                       NO
Data generated:                   NO
Validation outputs populated:     NO

Carry-forward concerns dispositioned at v0.2:
  AL-Q1 dry-run:                  INCORPORATED (§3.1)
  AL-Q2-schema:                    INCORPORATED (§7.2)
  AL-Q4 diagnostic sidecar:       INCORPORATED (§5.1)
  AL-Q5-opt LOCK-RECORD:          INCORPORATED (LOCK-RECORD v0.2 §2.1)
  AL-INH-1 co-ownership:          ACCEPTED (CS co-owns analysis-script
                                   per-stratum aggregation; T1 plan +
                                   analysis_script.py)
  AL-INH-2 co-ownership:          ACCEPTED (CS co-owns outcome-chooser
                                   code + fixed-language emission)
  IS-7 drift tolerance pre-decl:  CLARIFIED (§8)
  IS-8 lock-time hard refusal:    CLARIFIED (§9)
  IS-9 equality-predicate veto:   CLARIFIED (§4)

Next:                             Team Lead filter on D2 package;
                                   on Team Lead PASS, Manager D2
                                   decision

Dependencies still requiring NS / future-gate values:
  - manifest schema field names (§4) — NS design packet
  - T2 control-spec field names (§7) — NS T2 plan
  - T1 declared drift tolerance values (§8) — NS T1 plan
  - T3 ideal-witness record format (§15) — NS T3 plan
  - design packet sibling-artifact identity (§11) — NS design packet
  - MODEL_ID, PRODUCTION_PYTHON, EXPECTED_MLX_LM_VERSION — D2 packet prep
  - sweep_id — D4 (and never under D2)
  - hash values — D2 / D3 packet lock
```

— CS Engineer, 2026-06-11
