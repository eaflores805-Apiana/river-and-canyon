# CS Response to New Senior Co-Review — INH-2 and Targeted Edits

```text
DRAFT / REVIEW ONLY
D2 PACKET-PREPARATION ARTIFACT
NO D2 ACCEPTANCE GRANTED
NO EXECUTION AUTHORIZED
NO SWEEP_ID CREATED
NO MODEL RUNS
NO DATA GENERATED
NO VALIDATION OUTPUTS POPULATED
NO CODE IMPLEMENTATION BEGUN
```

From: CS Engineer
To: Team Lead (filter)
Cc: New Senior Engineer (co-owner), Senior Engineer, Manager
Date: 2026-06-11
Re: CS response to NS co-review of CS D2 proposed dispositions; required answers per Team Lead filter §8
Status: Joint disposition set ready for Team Lead filter; no code implementation; no model invoked

---

## 0. Documents under review

| Doc | Source | sha256 |
|---|---|---|
| CS-PROPOSED-DISPOSITIONS-INH-AND-PROMPT-SHELL (this is the predecessor; CS proposed) | commit `acf73a3` | `45f2e246…` |
| NS-COREVIEW-CS-D2-DISPOSITIONS (NS co-review; primary input) | apiana-papers / mirror | `66328f4a…` |
| D2-PACKET-STAGE-DESIGN-MATERIALS-v0.2 (NS design materials with declared values) | apiana-papers / mirror | `ffbf86fa…` |
| TEAMLEAD-FILTER-NS-COREVIEW-CS-D2 (this filter, requesting CS response) | this folder | filed |

---

## 1. CS Verdict — summary

```text
CS accepts NS's three-way outcome model in full.
CS accepts boundary_proximity_flag in full.
CS accepts all of TL's targeted edits and confirmations.
CS confirms all four boundary statements (no code; no validation
  execution; no sweep_id; no model invocation).
Joint disposition set is now ready for Team Lead filter.
```

The CS substantive position has shifted on INH-2: NS's three failure
modes of the four-tier model are correct, and the three-way structure
better preserves the no-survivor-ranking doctrine. §3 below records
the substantive reasoning.

---

## 2. Eleven required CS responses (per Team Lead §8)

### §8.1 — Accept / reject / modify NS three-way outcome model

**ACCEPT in full.**

```text
Outcome totality (three-way):
  INCONCLUSIVE | ELIMINATED | NOT_RULED_OUT

ELIMINATED:
  carries one or more attached descriptive elimination labels.

NOT_RULED_OUT:
  serializes the inherited label string "requires_further_investigation";
  fires iff the rung is measurable and no elimination label attached.

labels(rung) == {requires_further_investigation}
  iff outcome == NOT_RULED_OUT.

K = |{rung : outcome == NOT_RULED_OUT}|.
```

Why CS accepts (substantive reasoning):

1. **No survivor ranking.** CS's four-tier model created an implicit
   gradation inside the survivor set: "cleanly non-eliminated" vs
   "RFI" / "uncertain". That is exactly the rule-in surface the
   doctrine's unordered-non-eliminated-set rule exists to prevent.
   NS is right.

2. **K=0 statement consistency.** CS's four-tier model could emit
   the K=0 "reconnaissance-negative" statement while RFI rungs sit
   flagged. The lane would simultaneously declare "no rung was
   non-eliminated" AND carry rungs in an uncertain state. NS's
   self-contradiction objection is concrete and correct.

3. **Re-execution semantics.** "Flagged for re-execution" as an
   output behavior is a road-to-winner surface even when framed as
   a future Manager decision. Re-execution is a Manager-authorization
   question, not a lane output. NS is right.

4. **Preservation of CS design value.** The boundary-visibility
   information CS was trying to capture survives intact via
   `boundary_proximity_flag` (per-criterion diagnostic field). The
   information is preserved; the doctrine is preserved. Cleaner.

5. **Equality predicate clarity.** Under the three-way model, the
   non-eliminated predicate `labels(rung) == {requires_further_investigation}`
   is precise and verifiable. CS implements as a typed exhaustiveness
   check (per NS materials v0.2 §4: "every rung maps to exactly one
   of {inconclusive, eliminated, non-eliminated}; CS encodes this
   as a unit-tested exhaustiveness property, not a convention").

### §8.2 — Accept / reject / modify boundary_proximity_flag

**ACCEPT in full.**

```text
boundary_proximity_flag:
  per-criterion diagnostic field in the per-rung record.
  Set when a measurement falls within the criterion's pre-declared
  proximity zone.
  
  Diagnostic-only and non-eliminating:
    - excluded from outcome determination
    - excluded from K
    - excluded from all fixed language
    - reported in the diagnostics appendix only.
  
  No elimination label, outcome, or statement may reference it.
```

Why CS accepts:

This is the right protection layer. CS was trying to surface
boundary information as a fourth outcome tier (wrong layer — outcome
determination should be hard-Boolean). The diagnostic-only flag puts
boundary information where it belongs: in the diagnostics appendix,
visible to reviewers but structurally walled off from outcome
determination.

**CS implementation note:** the diagnostic appendix consumer (analysis
script's reporting code) must be type-disjoint from the outcome-
determination code, parallel to the DE-2 typed boundary for
`scrambled_binding_retrieval`. Source-level grep test asserts no call
site routes `boundary_proximity_flag` into outcome determination.

### §8.3 — Confirm descriptive serialized label strings

**CONFIRM.** The six descriptive strings are correct:

```text
accuracy_indistinguishable_from_token_prior
accuracy_indistinguishable_from_declared_policy_envelope
insufficient_measurement_headroom
strict_content_gap_instability
null_abstention_floor_unmet
answerable_abstention_ceiling_exceeded
```

CS implementation:

- Internal Python enum member names are CS's implementation choice
  (CS may use short snake_case names for code clarity).
- **Serialized values** (the `.value` of each enum member) carry the
  descriptive strings exactly.
- Schema enums, sidecars, serialized records, fixed language, and
  output artifacts emit only the descriptive strings.
- **No `fails` token in any output artifact label.** Source-level
  grep test asserts no string literal in the emission path contains
  the token "fails".

CS deletes the prior `CLEARLY_FAILS_*` value names from the proposed
disposition. The internal enum may keep its short names (e.g.,
`TOKEN_PRIOR_INDISTINGUISHABLE`) but the `.value` is the descriptive
string.

CS notes NS's correction: the last two strings split the v1
`abstention_contract_instability` label into the two re-formed
criteria from §I.6. CS implements the split as two distinct enum
members with two distinct descriptive `.value` strings.

### §8.4 — Confirm evaluation-time inconclusive triggers vs lock blockers

**CONFIRM.**

**Evaluation-time `INCONCLUSIVE` triggers (per rung):**

```text
- void_budget_exceeded
- required_policy_or_control_outputs_missing_from_sidecar
- harness_anomaly
```

**Lock-blocking conditions (refuse seal; never appear as rung outcomes):**

```text
- unresolved_pilot_log_failures (addendum E11 retention + C1 disposition)
- manifest_validation_failure (addendum A6 + schema invariants)
- A6_drift_exceedance (addendum A6 + IS-7 pre-declared tolerance)
```

CS implementation footprint:

- Lock-blocking conditions are checked in `lock_packet()` (CS-EP v0.2
  §9) before any rung evaluation. If any fires, `lock_packet()` raises
  `PacketLockRefused` with the specific condition. The LOCK-RECORD
  cannot reach SEALED.
- Evaluation-time INCONCLUSIVE triggers are checked per-rung in the
  outcome chooser after lock. If any fires for a given rung, the
  rung's outcome is `INCONCLUSIVE`.
- The two sets are code-disjoint; no condition appears in both code
  paths.

CS removes the prior conflation in its proposed disposition.

### §8.5 — Confirm INH-1 targeted governance sentence

**CONFIRM.** The governance sentence added to the T1 plan:

> **Accuracy and abstention metrics are forbidden from cross-stratum
> aggregation. No declared exception exists at packet stage; any
> future exception is a must-fix requiring C1 disposition.**

Pooled N=96 diagnostics are limited to: `distinct_outputs`,
`copy_completion` agreement, `void_accounting`.

CS implementation incorporates the void-adjustment refinement from
NS D2 materials v0.2 §3:

```text
N_eff_answerable = 80 − void_answerable
N_eff_null       = 16 − void_null
N_eff_pooled     = 96 − void_total (for the three permitted pooled diagnostics)
```

The per-rung record carries the three `N_eff_*` fields explicitly so
the auditor can verify denominators at a glance.

### §8.6 — Confirm INH-3 point-estimate / CI-bound declaration requirement

**CONFIRM.** Each T3 criterion must declare, at packet stage before
lock, whether it compares the **point estimate** or a **CI bound**
against its declared floor / ceiling.

CS implementation:

```python
class CriterionComparison(Enum):
    POINT_ESTIMATE = "point_estimate"
    CI_LOWER_BOUND = "ci_lower_bound"
    CI_UPPER_BOUND = "ci_upper_bound"

class CriterionDeclaration:
    criterion_id: str
    stratum: Literal["answerable", "null"]
    floor_or_ceiling: float                # the locked value
    comparison: CriterionComparison        # which value compares against floor_or_ceiling
    # ... other fields
```

The declaration is locked in T1 / T3 at packet seal; hashed into
LOCK-RECORD via `t3_sealed_hash` (D3) and `t3_plan_hash` (D1). Post-
pilot change is a must-fix event per anti-tuning rule.

### §8.7 — Confirm prompt-shell targeted edits

**CONFIRM.**

```text
VALUE_POOL is global. |VALUE_POOL| = 26. The value pool is constant
across rungs.

Ordering is lexicographic by token-id sequence.

The tokenizer and canonicalization are the same declared objects
used for prefix_neighbor_confusion equality (IS-9 carry).

Format-preserving definition:
  - The locked header, instruction block, format contract, and
    Q/A scaffold are byte-identical to the answerable prompt.
  - Exactly one substitution: the key-value pairs block is replaced
    by the "Available values" flat list.
  - The queried key is absent from the Q scaffold.

Standing taxonomy preserved:
  format-conditioned (full scaffold present) but binding-free
  (zero task-relevant bindings).

Baseline:
  1 / |VALUE_POOL| = 1/26 ≈ 0.038 [SWEEP-PARAMETER — NOT A THRESHOLD VALUE]

Empirical validation:
  ideal-random-emitter oracle in A5 must score within IS-7 tolerance
  of 1/26; any deviation is itself a finding about pool design and
  is documented in T1 sealed table.
```

CS implementation footprint:

- `VALUE_POOL` is a module-level constant in the runner module;
  hashed into LOCK-RECORD via `control_prompt_shell_hash` field
  (new at LOCK-RECORD v0.3, to be added when CS moves to v0.3).
- The shell template is byte-identical to the answerable prompt
  template except for the single substitution; a source-level diff
  test asserts the byte-identity.
- The `Available values:` list is rendered as a deterministic
  lexicographic sequence by token-id; an ordering test asserts the
  sequence is stable across pilot and final manifests.
- Tokenizer / canonicalization function used here is shared with
  `prefix_neighbor_confusion` equality predicate; a source-level
  cross-reference test asserts both use the same imported name and
  version pin.

### §8.8 — Confirm no code implementation has begun

**CONFIRM.** No source file under any execution-side path has been
created or modified. Specifically:

```text
No lane1a_prime_runner.py exists.
No lane1a_prime_runner_wrapper.py exists.
No manifest schema validator code exists.
No policy module source exists.
No control module source exists.
No analysis-script code exists.
No outcome-chooser code exists.
No test file exists.
No CI configuration changes.
```

Code implementation remains on hold pending Team Lead filter of this
joint disposition set, and (per TL §7) pending Manager confirmation
of D2 model-free validation scope.

### §8.9 — Confirm no validation execution occurred

**CONFIRM.** No pilot manifest construction. No oracle pre-flight
execution. No deterministic policy execution. No A6 re-verification.
No validation result-field population. CS holds per TL §7 and NS
materials v0.2 §9 / §9a until Manager confirms D2 model-free
validation scope.

### §8.10 — Confirm no sweep_id was created

**CONFIRM.** No `sweep_id` field has been populated with a value. No
directory bearing a `sweep_id`-implying name has been created.
LOCK-RECORD `identity.sweep_id` remains `<placeholder; NOT CREATED
UNDER D2 PACKAGE ASSEMBLY>`.

### §8.11 — Confirm no model was invoked

**CONFIRM.** No subprocess invoking any model has been spawned. No
model has been loaded. No prompt has been rendered against any model.
No model output has been produced.

---

## 3. CS sign-off on NS D2 Packet-Stage Design Materials v0.2 (joint dispositions)

NS materials v0.2 §§1–5 list "PROPOSED pending CS co-owner sign-off"
for the joint items. CS signs off on:

| § | Item | NS proposed | CS sign-off |
|---|---|---|---|
| 1 | Prompt-shell visibility | pool-visible; baseline = 1/26 | **CO-ENDORSE** |
| 2 | Per-policy cap | 0.50 (≥2.5× above intended structural hit-rates) | **CO-ENDORSE**; Wilson half-width margin at p̂=0.5, N=80 is ~0.11, providing reasonable detection power |
| 2 | Union-envelope cap | 0.80 (preserves ≥0.20 room) | **CO-ENDORSE**; "a floor against a 1.000 envelope is no floor" frame is right |
| 2 | IS-7 drift tolerance | ±0.05 per policy and for envelope | **CO-ENDORSE**; tolerance is in-scale with sampling-variation margin |
| 2 | Battery coverage minimum | ≥4 discriminative policies | **CO-ENDORSE**; corrected battery fields 4 envelope policies + `copy_completion` outside |
| 3 | INH-1 per-stratum table | void-adjusted N_eff per stratum | **CO-ENDORSE**; CS uses N_eff = N − void semantics; per-rung record carries N_eff_* fields |
| 4 | INH-2 three-way outcome | INCONCLUSIVE / elimination labels / RFI; equality predicate | **CO-ENDORSE** (per §8.1 above) |
| 5 | INH-3 SE interval method | Wilson + Newcombe-Wilson + Jeffreys fallback | **CO-ENDORSE** (per §8.6 above; Wilson without continuity correction) |
| 6 | D4 token-prior gate | carried; opens by name only | **CO-ENDORSE**; LOCK-RECORD slot stands |
| 7 | OPT-2 | dispositioned non-blocking | **CO-ENDORSE** |
| 8 | Remaining register items | dispositioned as listed | **CO-ENDORSE** |

CS notes all numeric values in §§1–2 are correctly marked
`[SWEEP-PARAMETER — NOT A THRESHOLD VALUE]` per the standing
non-authorizations carve-out. They are sweep parameters that
must be reviewable before lock and immutable after.

CS also endorses §9 / §9a / §9b boundary discipline:

- §9 boundary question (D2 model-free validation scope) — CS endorses
  surfacing this question to Manager. The Manager D2 memo's §1.2
  ("populating T1–T4 as appropriate") is ambiguous on whether the
  addendum's offline validation steps (A1 pilot battery; A5 oracle
  pre-flight; A6 re-verification) are authorized. The conservative
  read is the right read until Manager confirms.
- §9a model-free validation boundary language — CS endorses the
  Team-Lead-formulated scope statement (model-free validation ≠ model
  evaluation; SYNTHETIC/DIAGNOSTIC labels; lock-eligibility only;
  no candidate / threshold / certification / retention claims).
- §9b execution-ledger template — CS endorses the template as the
  required format for the first validation return, if/when Manager
  confirms scope.

---

## 4. Updated CS-side INH-2 implementation (incorporates NS counter-proposal)

For the work-trail, CS records the updated INH-2 implementation that
will land at code time:

```python
class RungOutcome(Enum):
    """Three-way outcome enum. No passes_X value; no fails_X value
    in serialized form (descriptive strings only at the value level).
    """
    INCONCLUSIVE = "inconclusive_not_actionable"
    ELIMINATED   = "eliminated"        # carries attached label set; see ELIMINATION_LABELS
    NOT_RULED_OUT = "not_ruled_out"    # serializes "requires_further_investigation"

class EliminationLabel(Enum):
    """Descriptive labels attached to ELIMINATED rungs. Serialized
    values are the .value strings; no `fails` token.
    """
    TOKEN_PRIOR_INDISTINGUISHABLE = "accuracy_indistinguishable_from_token_prior"
    ENVELOPE_INDISTINGUISHABLE    = "accuracy_indistinguishable_from_declared_policy_envelope"
    HEADROOM_INSUFFICIENT          = "insufficient_measurement_headroom"
    STRICT_CONTENT_INSTABILITY    = "strict_content_gap_instability"
    NULL_ABSTENTION_FLOOR_UNMET    = "null_abstention_floor_unmet"
    ANSWERABLE_CEILING_EXCEEDED    = "answerable_abstention_ceiling_exceeded"

# Outcome determination:
def compute_rung_outcome(rung: RungEvaluation) -> tuple[RungOutcome, frozenset[EliminationLabel]]:
    """
    Returns (outcome, attached_labels).
    
    Evaluation precedence (per NS materials v0.2 §4):
      1. INCONCLUSIVE preempts; rung excluded from K and reported separately.
      2. ELIMINATED if any elimination label attaches; labels(rung) = the attached set.
      3. NOT_RULED_OUT iff measurable and no elimination label attached;
         labels(rung) = {"requires_further_investigation"}.
    
    Totality obligation: every rung maps to exactly one outcome.
    Implementation: typed exhaustiveness property, unit-tested.
    """

# K computation:
def compute_K(rungs: list[Rung]) -> int:
    return sum(1 for r in rungs if r.outcome == RungOutcome.NOT_RULED_OUT)

# boundary_proximity_flag is a per-criterion diagnostic field on
# RungEvaluation; never enters compute_rung_outcome's code path.
```

Three fixed-language constants (text revised per NS counter-proposal
to use "not ruled out" instead of "non-eliminated"):

```python
K_EQUALS_ZERO_STATEMENT = (
    "Under the sealed Validation Report, the Lane 1a' sweep returned "
    "K=0: no rung was not-ruled-out under the pre-registered "
    "negative-use diagnostics. Per the symmetric finality rule "
    "(Lane 1a' Design Proposal v0.2 §10), this is the lane's "
    "substantive reconnaissance-negative finding for this task "
    "family at this scale, for this construction. It is not a "
    "Paper 3 certification verdict and not evidence of model "
    "incapability."
)

SINGLE_NOT_RULED_OUT_RUNG_STATEMENT = (
    "The Lane 1a' sweep returned K=1: one rung was not-ruled-out "
    "under the pre-registered negative-use diagnostics. Per the "
    "no-positive-use rule (Lane 1a' Design Proposal v0.2 §10), "
    "this outcome is not promising, viable, candidate-ready, "
    "near-certifiable, or suitable for positive selection. It does "
    "not rank, support candidate selection, support threshold work, "
    "or constitute certification evidence."
)

MULTIPLE_NOT_RULED_OUT_STATEMENT_TEMPLATE = (
    "The Lane 1a' sweep returned K={k}: {k} rungs were not-ruled-out "
    "under the pre-registered negative-use diagnostics. Per the "
    "no-positive-use rule (Lane 1a' Design Proposal v0.2 §10), this "
    "outcome is not promising, viable, candidate-ready, near-"
    "certifiable, or suitable for positive selection. Not-ruled-out "
    "rungs are listed in rung-ID order; no rank fields or "
    "computations are emitted; the unordered not-ruled-out set "
    "carries no positive evidence weight."
)
```

NS may suggest finer wording at packet-stage T3 review. The constants
remain typed-string immutables hashed into LOCK-RECORD via
`analysis_script_hash`.

---

## 5. Boundaries preserved

```text
No execution authorized.
No new sweep_id.
No model runs.
No data generation (in the model-output sense).
No code implementation begun.
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
No D3 / D4 / D5 implied or solicited.
```

Per TL §7 + NS materials v0.2 §9 / §9a: **D2 model-free validation
work remains on hold pending Manager confirmation.** CS will not
construct pilot manifests, run oracle pre-flight, execute deterministic
policies, run A6 re-verification, or populate validation result fields
until Manager files explicit confirmation.

Semantic co-drafting and non-executing packet refinement continue.

All execution gates remain CLOSED.

---

## 6. CS posture

```text
NS counter-proposal on INH-2:           ACCEPTED IN FULL
boundary_proximity_flag:                 ACCEPTED IN FULL
Descriptive serialized labels:           CONFIRMED (6 strings)
Inconclusive triggers vs lock blockers:  CONFIRMED (split adopted)
INH-1 governance sentence:               CONFIRMED + void-adjusted N_eff
INH-3 point-estimate/CI-bound decl rule: CONFIRMED + CriterionComparison enum
Prompt-shell targeted edits:             CONFIRMED (global VALUE_POOL, |26|, etc.)

NS materials v0.2 joint dispositions:    CO-ENDORSED (all 11 line items)
NS materials §9/§9a/§9b boundary disc:   ENDORSED

Joint disposition set:                   ready for Team Lead filter

Status confirmations (TL §8.8-§8.11):
  No code implementation begun:          CONFIRMED
  No validation execution occurred:      CONFIRMED
  No sweep_id was created:               CONFIRMED
  No model was invoked:                  CONFIRMED

Next:                                    Team Lead filter on joint
                                          disposition set; on Team
                                          Lead PASS + Manager
                                          model-free validation
                                          scope confirmation, CS
                                          proceeds to code
                                          implementation per
                                          semantics-first ordering

Lane 1a close-out v1.2 (parallel):       CLOSED-PENDING-ADOPTION
                                          (Senior owns)

All execution gates:                     CLOSED
```

— CS Engineer, 2026-06-11
