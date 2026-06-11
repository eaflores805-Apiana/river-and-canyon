# CS Interface Alignment Response — Lane 1a′ D1 Bundle

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
To: Team Lead
Cc: New Senior Engineer, Senior Engineer, Manager
Date: 2026-06-11
Re: CS interface alignment response — Lane 1a′ D1 Design-Packet Bundle v0.1
Status: Alignment provided; no execution authorized; no validation outputs populated

---

## 0. Document under review

| Field | Value |
|---|---|
| Title | Lane 1a′ D1 Design-Packet Bundle v0.1 (New Senior) |
| Source | `apiana-papers/C6_Proposal/D1-DESIGN-PACKET-BUNDLE-v0.1 (2).md` |
| Local mirror | `governance/2026-06-11_lane-1a-prime/D1-DESIGN-PACKET-BUNDLE-v0.1.md` |
| sha256 | `07eb713b716c578eaed09db32423465427f609274b473abfc332fc85c131cc31` (`cmp` IDENTICAL) |
| Team Lead disposition | PASS WITH TARGETED EDITS (small v0.2 revision requested of New Senior) |
| Request type | CS interface alignment (parallel to New Senior v0.2 revision) |
| Companion CS artifacts | `CS-EXECUTION-PACKET-PROPOSAL-v0.1.md` (sha256 `af2b8dac…`); `LOCK-RECORD-DRAFT-STRUCTURE-v0.1.md` (sha256 `6c07d2e7…`); `NON-AUTHORIZATION-CONSUMPTION-SIDE-EXCLUSION-LANGUAGE-v0.1.md` (sha256 `7c072cc6…`) |

---

## 1. Answers to Part VII (six interface questions)

### Q1 — Runner assembly dry-run (no-model)

**Answer: YES.**

The standalone-runner skeleton exposes a no-model assembly dry-run by
adding a `--dry-run` flag to `lane1a_prime_runner.py` and a callable
`render_prompt()` interface on the runner module. Concrete addition
to CS Execution-Packet Proposal v0.1 §3 (drafted in this response for
incorporation at v0.2):

```python
def render_prompt(record: ManifestRecord) -> RenderedPrompt:
    """
    Renders a prompt for a single manifest record using the locked
    template. Pure function; no model invocation; no I/O beyond
    reading the record and template.
    
    Returns RenderedPrompt with:
      - text: str                       # the rendered prompt
      - template_id_hash: str           # locked template hash
      - record_id: str                  # source record id
      - conformance_check: ConformanceResult
    """
```

**Wrapper-side dry-run mode:**

```python
# lane1a_prime_runner_wrapper.py
parser.add_argument("--dry-run", action="store_true",
                    help="Render prompts and conformance-check; do not invoke model.")
```

In dry-run mode:
- `write_sidecar()` is bypassed (no model output exists to attest).
- Output goes to a dry-run report file with label
  `SYNTHETIC — NON-BINDING — NOT FOR THRESHOLD DERIVATION` and
  sub-classifier `dry_run: true`.
- The interface-contract test (Path A.1 carry) calls `render_prompt()`
  directly on synthetic ideal-retriever oracle manifests and asserts
  conformance + structural match to the T2 prompt-shell declarations.

**Schema / runner-shell implications:**

- `RenderedPrompt` carries `template_id_hash` so dry-run results can
  be cross-referenced to the locked template hash at lock time via
  the sibling-artifact rule.
- The dry-run output schema is a distinct subschema of the
  validation report (not a sweep output), so it does not pollute the
  `RECONNAISSANCE` artifact class.
- No `sweep_id` is created by running `--dry-run`; the dry-run is
  pre-lock interface testing and inherits the same no-sweep_id rule
  the full runner inherits at D1.

**Conditions:** none beyond standard D1 boundary preservation. The
dry-run is the right structural placement for pre-lock interface
testing and CS endorses adding it explicitly to v0.2 §3.

### Q2 — Schema enforcement for diagnostic boundary (DE-2)

**Answer: YES, by three layers of machine enforcement. Review-only is rejected as the weakest layer per the standing protection-layer taxonomy.**

The three layers (already drafted in CS Execution-Packet Proposal v0.1 §7;
this response makes the schema layer explicit):

**Layer 1 — typed boundary (code-level; v0.1 §7):**
- `LabelInput` is a closed type that does not carry any field
  accepting `ControlOutput`.
- `emit_elimination_label(label_input: LabelInput) -> ...` accepts
  only `LabelInput`.
- Test: `test_label_input_does_not_carry_control_outputs` (Path A.1
  pattern; sibling-artifact source grep).

**Layer 2 — schema-level enforcement (NEW for v0.2 of CS Execution-Packet Proposal):**

Sidecar schema (the relevant field):

```yaml
sidecar:
  elimination_label_basis:        # enum closed over policy ids only
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
            # NOTE: copy_completion is OMITTED (it is outside the
            #       union envelope per v0.2 §5; not an elimination basis).
            # NOTE: NO control names appear in this enum.
            #       scrambled_binding_retrieval is structurally
            #       unrepresentable here.
```

Per-rung result schema (the relevant field):

```yaml
rung_result:
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
        # control_id field deliberately ABSENT;
        # cannot be added by additionalProperties: false rule.
```

**Layer 3 — analyzer check (defense in depth; v0.1 §7):**
- Source-level grep test in the analysis script: no call site routes
  a `ControlOutput` (or any field carrying a control name) into the
  elimination-label code path.
- Pre-lock analyzer scans the analysis script source for any
  reference to `scrambled_binding_retrieval` inside any function
  reachable from `emit_elimination_label`.

**Enforcement matrix:**

| Mechanism | Available? | CS recommendation |
|---|---|---|
| enum / reference validation | YES (Layer 2) | **REQUIRED** at packet stage |
| analyzer check (source-level grep + reachability) | YES (Layer 3) | **REQUIRED** at packet stage |
| schema field restriction (`additionalProperties: false`) | YES (Layer 2) | **REQUIRED** at packet stage |
| review-only rule | available but NOT SUFFICIENT alone | **REJECTED** as sole mechanism |

CS confirms the mechanical rule is schema-enforced by construction
and analyzer-enforced as defense in depth. The DE-2 v0.2 verbatim
"Mechanical rule: no elimination label may reference
`scrambled_binding_retrieval`, directly or indirectly" lands at
**code + schema + analyzer**, not at wording.

### Q3 — Equality predicate for `prefix_neighbor_confusion`

**Answer: NO stricter rule proposed at this time. The current rule (token-id-sequence equality after tokenizer canonicalization) is implementable and appropriate.**

CS confirms IS-9 (CS v0.2 review): the token-id-sequence-equality-
after-tokenizer-canonicalization predicate is the right semantic for
"exact queried key" in this construction. CS proposes no stricter
rule at design level.

**Reservation:** CS reserves the option to propose a stricter rule at
packet stage if any of the following tokenizer edge cases surface
during pilot construction:

- Unicode-normalization-form boundary (NFC vs NFD treatment when
  manifest keys originate from outside the runner's tokenizer canon).
- Byte-level fallback tokens that could produce two distinct
  token-id sequences for visually identical surface forms.
- Tokenizer-version drift between manifest construction time and
  runtime (mitigated by the LOCK-RECORD `bound_versions` pin on
  `model_snapshot`, but worth a packet-stage test).

If any edge case surfaces, CS will propose the stricter rule in the
packet-stage review and v0.2 §5's `"unless CS proposes a stricter
implementable rule"` clause routes the proposal cleanly.

### Q4 — `copy_completion` agreement-rate diagnostic location

**Answer: diagnostic sidecar (preferred). Confirms it stays outside the union envelope.**

Recommendation matrix:

| Placement | CS read | Verdict |
|---|---|---|
| per-item log only | viable; mixes diagnostic with provenance content in the main audit log | **second choice** |
| **diagnostic sidecar** | clean separation; carries per-item agreement alongside other diagnostic data; parallel pattern to runner-attested sidecar; preserves "outside the union envelope" boundary by structural separation | **CS recommendation** |
| gate / analyzer record only | too coarse; loses per-item information needed for analysis | not recommended alone |
| separate non-eliminating diagnostic report | viable for final aggregation; per-item data still needs a home (the diagnostic sidecar feeds the report) | **fine as a downstream aggregator** of the sidecar data |

**Implementation (NEW for CS Execution-Packet Proposal v0.2):**

```yaml
diagnostic_sidecar:
  # Parallel to the runner-attested sidecar; for non-eliminating
  # diagnostics only.
  record_id: <placeholder>
  diagnostic_class: copy_completion_agreement | ...
  artifact_class: lane-1a-prime-diagnostic
  artifact_label: "DIAGNOSTIC — NON-BINDING — NOT FOR THRESHOLD DERIVATION"
  per_item:
    - item_id: <placeholder>
      diagnostic_value: <placeholder>      # e.g., agreement: 1 | 0
      runner_output_ref: <placeholder>     # link to runner-attested sidecar
```

**Code-level invariant:** the diagnostic-sidecar reader cannot feed
the union-envelope computation. The union-envelope computation
function accepts only inputs of type `EnvelopePolicyOutput`, which is
disjoint from `DiagnosticSidecar`. (Schema enforcement matches the
DE-2 typed-boundary pattern from Q2.)

**Confirmation:** `copy_completion` remains outside the union envelope
unless separately authorized. Per v0.2 §5 verbatim and CS Execution-
Packet Proposal v0.1 §12 / §16 #cross-ref. CS endorses.

### Q5 — LOCK-RECORD slots

**Answer: ALL SIX SLOTS PRESENT in CS LOCK-RECORD Draft Structure v0.1.** Cross-reference table:

| Slot requested | CS LOCK-RECORD v0.1 location | Status |
|---|---|---|
| D4 by-name token-prior resolution | §2 `token_prior_authorization` + §5 detail (state machine; required Manager-memo fields; "by name, never by bundle" verbatim slot) | **PRESENT** |
| Sealed-hash binding | §2 `bound_hashes` (15 hash fields enumerated) + §4 binding rules (5 rules) | **PRESENT** |
| C2 considered-memos enumeration | §2 `c2_considered_memos` + §6 detail (standing C2 rule quoted; per-memo path + sha256 + review_state + considered_for_gate) | **PRESENT** |
| R6 inheritance screen reference | §2 `r6_inheritance_screen` | **PRESENT** |
| T1–T4 validation artifact references | §2 `bound_hashes`: `t1_plan_hash`, `t2_plan_hash`, `t3_plan_hash`, `t4_plan_hash` (design-stage plans, D1 hashes) + `instrument_validation_report_hash` (sealed report containing populated T1–T4 tables, D3 hash) | **PRESENT** |
| Non-authorization block | §11 references companion artifact `NON-AUTHORIZATION-CONSUMPTION-SIDE-EXCLUSION-LANGUAGE-v0.1.md` with verbatim summary | **PRESENT** |

**No hash values populated under D1.** Per CS LOCK-RECORD §10
no-population-under-D1 rule and the explicit `<placeholder>` markers
throughout §2.

**Optional v0.2 enhancement (not blocking):** CS could break the
`instrument_validation_report_hash` into a per-table sub-block for
cleaner audit trail at D3 seal:

```yaml
validation_artifact_hashes:
  t1_sealed_hash:                    <placeholder>  # populated T1 table
  t2_sealed_hash:                    <placeholder>  # populated T2 sheets
  t3_sealed_hash:                    <placeholder>  # populated T3 checklist
  t4_sealed_hash:                    <placeholder>  # populated T4 dispositions
  ideal_witness_record_hash:         <placeholder>  # T3-locked ideal-witness
  pilot_iteration_log_hash:          <placeholder>  # E11 log
  oracle_case_verdict_table_hash:    <placeholder>  # A5 pre-flight verdicts
```

This breakdown is parallel to the `bound_hashes` block but specific
to populated validation artifacts (D3 seal time, not D1). If Team
Lead prefers the breakdown, CS will add it at LOCK-RECORD v0.2.
Either form is acceptable; both produce the same audit guarantees.

### Q6 — Path conventions and directory naming

**Answer: Governance directory in use; experiment directory DEFER to D2.**

**Governance directory (in use):** `governance/2026-06-11_lane-1a-prime/`
matches the adopted Path Conventions standing rule (`governance/<date>_<lane>/`).
All current D1 work lives here. CS endorses.

**Experiment directory (CS recommends deferring until D2):**

The v1 lane used `experiments/2026-06-10_lane-1a-sweep/`. Following
that convention, Lane 1a′ would presumably use
`experiments/<date>_lane-1a-prime-sweep/` (or similar). **CS
recommends deferring the experiment directory name until D2.** Three
reasons:

1. The directory date should match the date when CS execution-packet
   preparation actually begins, not the design-proposal date (the
   v1 convention).
2. Creating an `experiments/` subdirectory under D1 — even an empty
   one — risks being read as implicit packet authorization or sweep
   activation.
3. The directory name doesn't affect any current D1 work; all D1
   artifacts are governance/ work.

**CS agrees with the reading that naming a directory in a draft does
not create a sweep_id** — but the safer posture under D1 is to not
propose an experiment directory name at all. Per CS LOCK-RECORD §2
`identity.sweep_id: <placeholder; NOT CREATED UNDER D1>` and v0.2
§11 non-authorizations enumeration.

**Suggested wording for New Senior v0.2 Bundle:** if New Senior
wishes to name the experiment directory in the D1 bundle as a
forward reference, CS suggests phrasing:

> "Experiment directory name is proposed `experiments/<YYYY-MM-DD>_lane-1a-prime-sweep/`
> at the date of CS execution-packet preparation; the name is provisional
> and is not finalized under D1; naming does not create a sweep_id."

Or, simpler: defer the name entirely until D2.

---

## 2. Implementability check on the four targeted edits to New Senior

CS confirms all four Team Lead edits are implementability-clean.

| # | Edit | CS implementability check | Verdict |
|---|---|---|---|
| 1 | Add D2 references as future-review references only | D2 is the next gate per v0.2 §12 and Manager D1 memo. References framed as future-review-gate (not current authorization) carry no execution implication. CS LOCK-RECORD §9 state machine and CS Execution-Packet Proposal §18 already treat D2 as the next gate. | **CLEAN** |
| 2 | Add directory-name / sweep_id boundary | The boundary CS confirms in Q6 above. Directory naming does not create a sweep_id; per CS LOCK-RECORD §2 `identity.sweep_id: <placeholder; NOT CREATED UNDER D1>`. CS recommends specific wording in Q6 above. | **CLEAN** |
| 3 | Add CS co-ownership for INH-1 and INH-2 | INH-1 (per-diagnostic stratum semantics over 96/80/16) affects CS analysis-script aggregation code and the `manifest_record.stratum` field handling. INH-2 (outcome-chooser totality: non-eliminated predicate, RFI-only behavior, inconclusive class, fixed language) affects CS outcome-chooser code and the fixed-language emission. CS confirms co-ownership for both. Aligns with CS Execution-Packet Proposal §16 cross-reference map ownership pattern. | **CLEAN — CS accepts co-ownership** |
| 4 | Mark Wilson as proposed, not selected | Wilson, Jeffreys, and other CI methods are all implementable; CS can implement any reasonable confidence-interval method at packet stage. "Proposed, not selected" preserves the gate-design optionality until the packet-stage T1 plan locks the choice. CS endorses. | **CLEAN** |

---

## 3. Findings classification

### 3a. D1 alignment blockers

**NONE.**

The Bundle v0.1 is structurally consistent with the three CS-owned
D1 skeleton artifacts. All six Part VII questions answered with
implementable specifications. All four Team Lead targeted edits are
implementability-clean. No interface conflict surfaces.

### 3b. D2 packet-stage concerns (CS-side; for incorporation into CS Execution-Packet Proposal v0.2 after New Senior bundle v0.2 lands)

| ID | Concern | Source | CS plan |
|---|---|---|---|
| **AL-Q1** | Add `render_prompt()` + `--dry-run` to CS Execution-Packet Proposal §3 | Q1 answer | Incorporate at CS proposal v0.2 |
| **AL-Q2-schema** | Make sidecar + per-rung schema enforcement of DE-2 explicit in CS Execution-Packet Proposal §7 (layer 2) | Q2 answer | Incorporate at CS proposal v0.2 |
| **AL-Q4** | Add diagnostic-sidecar pattern to CS Execution-Packet Proposal §5 | Q4 answer | Incorporate at CS proposal v0.2 |
| **AL-Q5-opt** | Optional `validation_artifact_hashes` per-table sub-block in CS LOCK-RECORD §2 | Q5 optional enhancement | Incorporate at CS LOCK-RECORD v0.2 IF Team Lead prefers the breakdown |
| **AL-INH-1 co-own** | CS co-ownership of INH-1: per-stratum aggregation in analysis script | Targeted-edit check #3 | CS picks up at packet-stage T1 plan review |
| **AL-INH-2 co-own** | CS co-ownership of INH-2: outcome-chooser code; fixed-language emission | Targeted-edit check #3 | CS picks up at packet-stage T1 plan review |

### 3c. Optional implementation suggestions

| ID | Suggestion | Notes |
|---|---|---|
| **OPT-1** | Bundle could add a 1-sentence link to the three CS-owned D1 artifacts (`CS-EXECUTION-PACKET-PROPOSAL-v0.1.md`, `LOCK-RECORD-DRAFT-STRUCTURE-v0.1.md`, `NON-AUTHORIZATION-CONSUMPTION-SIDE-EXCLUSION-LANGUAGE-v0.1.md`) so the work-trail closes both directions | Nice-to-have; matches the sibling-artifact cross-reference rule's spirit |
| **OPT-2** | Part V T4 table could add `commit_or_file_reference` column explicitly per addendum C1 schema | Nice-to-have; addendum C1 requires the field at lock; adding now improves audit clarity |
| **OPT-3** | Part II A6 drift block could be paired with the IS-7 pre-declared tolerance values placeholder | Coordinates with CS proposal §8; nice-to-have at v0.2 |

None of OPT-1/2/3 affects D1 alignment.

---

## 4. Recommended wording for New Senior v0.2 Bundle (CS-suggested, non-binding)

### For Q6 directory-naming boundary (Edit #2)

Insert at Bundle I.3 or Part VI #6 (where appropriate):

> *"Governance directory `governance/2026-06-11_lane-1a-prime/` is in use under Path Conventions. Experiment directory naming is deferred to D2 packet preparation: naming a directory in a D1 draft does not create or imply a sweep_id; no `experiments/` subdirectory is created under D1."*

### For INH-1 and INH-2 co-ownership (Edit #3)

In Part V T4 table:

```
| INH-1 | inherited (v1 close-out) | semantics | ... | OPEN | ... | New Senior + CS | must resolve before lock |
| INH-2 | inherited (v1 close-out) | totality  | ... | OPEN | ... | New Senior + CS | must resolve before lock |
| INH-3 | inherited (v1 close-out) | statistics| ... | OPEN | ... | New Senior + CS | must resolve before lock |
```

### For Wilson "proposed not selected" (Edit #4)

In Part VI #3:

> *"INH-3 proposal: Wilson (preferred; not yet selected — final SE method declared at packet-stage T1 plan)."*

CS suggests but does not require these exact phrasings.

---

## 5. Boundaries preserved

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

This response creates no execution artifacts, populates no validation
outputs, generates no manifests, assigns no sweep_id, and runs no
validation process. All execution gates remain CLOSED.

---

## 6. CS posture

```text
Lane 1a' D1 Design-Packet Bundle v0.1:    PASS WITH TARGETED EDITS
                                           (Team Lead disposition; CS
                                            agrees; small v0.2 revision
                                            requested of New Senior)

CS interface alignment:                    DELIVERED (this document)
  - 6 Part VII questions answered
  - 4 targeted-edit implementability
    checks: ALL CLEAN
  - 0 D1 alignment blockers
  - 6 D2 packet-stage concerns logged for
    CS proposal v0.2 incorporation
  - 3 optional implementation suggestions

CS LOCK-RECORD v0.1 slot confirmation:    ALL SIX SLOTS PRESENT
  - D4 by-name token-prior resolution
  - sealed-hash binding
  - C2 considered-memos enumeration
  - R6 inheritance screen reference
  - T1-T4 validation artifact references
  - non-authorization block

CS-owned D1 artifacts in force:
  CS-EXECUTION-PACKET-PROPOSAL-v0.1.md (sha256 af2b8dac...)
  LOCK-RECORD-DRAFT-STRUCTURE-v0.1.md  (sha256 6c07d2e7...)
  NON-AUTHORIZATION-CONSUMPTION-SIDE-EXCLUSION-LANGUAGE-v0.1.md
                                       (sha256 7c072cc6...)

Next:                                      hold for New Senior Bundle
                                           v0.2 (Team Lead-routed
                                           revision); on bundle v0.2
                                           landing, CS incorporates
                                           AL-Q1, AL-Q2-schema, AL-Q4,
                                           AL-Q5-opt (if requested),
                                           AL-INH-1, AL-INH-2 into
                                           CS proposal v0.2 +
                                           LOCK-RECORD v0.2 and
                                           returns at joint return
                                           for D2 review

Lane 1a close-out v1.2 (parallel):        CLOSED-PENDING-ADOPTION
                                           (Senior owns)

All execution gates:                       CLOSED
```

— CS Engineer, 2026-06-11
