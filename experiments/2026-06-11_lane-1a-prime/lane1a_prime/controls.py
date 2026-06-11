"""Lane 1a' control modules.

SYNTHETIC / DIAGNOSTIC -- NON-BINDING -- NOT FOR THRESHOLD DERIVATION
D2 IMPLEMENTATION ARTIFACT (PHASE 2)
NO MODEL INVOKED -- NO SWEEP_ID CREATED -- NO SWEEP EXECUTION AUTHORIZED

Implements the DE-2 typed boundary (Bundle v0.3 §I.5 mechanical rule):
  "no elimination label may reference scrambled_binding_retrieval,
   directly or indirectly"

Mechanism (three machine layers per CS-EP v0.2 §7):

  Layer 1 (this module): typed-boundary classes.
    - ControlOutput is the output type of a control invocation.
    - LabelInput is the input type for elimination-label emission.
    - LabelInput does NOT carry a field of type ControlOutput.
    - emit_elimination_label accepts ONLY LabelInput.

  Layer 2 (schemas/sidecar_schema.yaml): closed-enum on
  elimination_label_basis.basis_policies; control names are
  STRUCTURALLY UNREPRESENTABLE in that enum.

  Layer 3 (analysis script, Phase 3): source-level grep + reachability
  analyzer asserting no call site routes ControlOutput into the
  elimination-label code path.

Phase 2 establishes Layers 1 here. Layer 2 already in place
(schemas/sidecar_schema.yaml). Layer 3 lands at Phase 3 (analysis
script).

The control modules under D2 are SPECIFICATIONS plus typed-boundary
classes; model invocation is NOT authorized under D2 and the
control-execution function bodies remain NotImplementedError stubs
until a separately authorized D4 by-name decision opens model
invocation for the unconditioned_token_prior control.

The scrambled_binding_retrieval control is permanently
non-eliminating per the joint disposition; its output cannot reach
the elimination-label path even if a future authorization opens its
invocation.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal


# ---------- T2 control specifications ----------

@dataclass(frozen=True)
class ControlSpec:
    """Per-control T2 specification per Bundle v0.3 §III.

    Eliminative status enum:
      "referenced_by_elimination_criteria_per_t3" : control is
        referenced by a T3 elimination criterion at packet seal.
      "none_diagnostic_only" : control is NEVER referenced by an
        elimination label. Schema-enforced unrepresentability of the
        control name in the sidecar's elimination_label_basis enum
        backs this.
    """
    control_name: str
    semantic_target: str
    isolates: str
    must_not_reward: str
    binding_handling: Literal["preserved", "scrambled", "removed", "replaced"]
    scoring_target: str
    expected_baseline: str
    expected_ideal_behavior: str
    expected_shortcut_behavior: str
    failure_interpretation: str
    eliminative_status: Literal[
        "referenced_by_elimination_criteria_per_t3",
        "none_diagnostic_only",
    ]
    non_claim: str
    unconditioned_definition: str = ""


UNCONDITIONED_TOKEN_PRIOR_SPEC = ControlSpec(
    control_name="unconditioned_token_prior",
    semantic_target="surface emission bias without task-relevant bindings",
    isolates="what the model emits when retrieval cannot resolve",
    must_not_reward="retrieval of any in-context binding",
    binding_handling="removed",
    scoring_target="gold value of mirrored answerable item",
    expected_baseline=(
        "derived from declared shell visibility, value pool, and scoring "
        "contract; baseline = 1 / |VALUE_POOL| = 1/26 under the joint "
        "disposition (pool-visible shell; VALUE_POOL global; |pool| = 26)"
    ),
    expected_ideal_behavior=(
        "at-chance correctness or contract abstention (descriptive)"
    ),
    expected_shortcut_behavior="above-chance via surface/frequency bias only",
    failure_interpretation=(
        "candidate-vs-control separation below the pre-registered "
        "descriptive margin is consistent with prior-driven correctness"
    ),
    eliminative_status="referenced_by_elimination_criteria_per_t3",
    non_claim=(
        "measures emission bias on this construction only; supports no "
        "capability claim"
    ),
    unconditioned_definition=(
        "format-conditioned but binding-free (standing taxonomy)"
    ),
)


SCRAMBLED_BINDING_RETRIEVAL_SPEC = ControlSpec(
    control_name="scrambled_binding_retrieval",
    semantic_target="binding-following after rebinding",
    isolates="whether current bindings are followed",
    must_not_reward="stale or prior-favored value return",
    binding_handling="scrambled",
    scoring_target="post-scramble gold",
    expected_baseline="n/a (diagnostic)",
    expected_ideal_behavior="high correctness",
    expected_shortcut_behavior="stale or prior-favored values",
    failure_interpretation="informs interpretation only",
    eliminative_status="none_diagnostic_only",
    non_claim=(
        "strictly diagnostic; no capability, viability, suitability, "
        "certifiability, or threshold claim; does not rehabilitate any "
        "v1 result. Mechanical rule: no elimination label may reference "
        "this control, directly or indirectly."
    ),
    unconditioned_definition="",
)


CONTROL_SPECS = {
    UNCONDITIONED_TOKEN_PRIOR_SPEC.control_name: UNCONDITIONED_TOKEN_PRIOR_SPEC,
    SCRAMBLED_BINDING_RETRIEVAL_SPEC.control_name: SCRAMBLED_BINDING_RETRIEVAL_SPEC,
}


# ---------- DE-2 typed boundary ----------

@dataclass(frozen=True)
class ControlOutput:
    """Output of a control invocation.

    By type construction, ControlOutput is NOT consumable by
    elimination-label emission code. The emit_elimination_label
    function accepts only LabelInput, which has no field of type
    ControlOutput.
    """
    control_name: str
    value: float
    metadata: dict


@dataclass(frozen=True)
class LabelInput:
    """Input to the elimination-label emitter.

    INVARIANT: this dataclass has NO field of type ControlOutput.
    Adding such a field would be a DE-2 boundary violation and is
    enforced against by:
      - Layer 1 (this module): the field set below is closed and
        does not include a ControlOutput-typed field.
      - Layer 2 (sidecar_schema.yaml): elimination_label_basis enum
        excludes control names by construction.
      - Layer 3 (Phase 3 analysis script): source-level grep test
        asserts no call site routes a ControlOutput into the
        elimination-label code path.
    """
    rung_id: str
    # policy_outputs is the ONLY input channel for elimination-label
    # emission. The values are policy-derived; controls are absent.
    policy_outputs: tuple  # tuple[PolicyOutput, ...] -- avoid circular import

    # The schema's elimination_label_basis.basis_policies enum lists
    # exactly the four envelope policies and excludes control names.


@dataclass(frozen=True)
class DiagnosticInterpretation:
    """Output of diagnostic interpretation; informs reading, not
    elimination labeling.

    Both control_outputs and policy_outputs may be present here, but
    this type is consumed only by the diagnostic reporting code; it
    is NOT routed into emit_elimination_label by any module.
    """
    rung_id: str
    control_outputs: tuple  # tuple[ControlOutput, ...]
    policy_outputs: tuple  # tuple[PolicyOutput, ...]


# ---------- emit_elimination_label signature ----------

def emit_elimination_label(label_input: LabelInput) -> tuple[str, ...]:
    """Emit elimination labels for a rung based on the LabelInput.

    INVARIANT (DE-2 Layer 1): the signature accepts ONLY LabelInput.
    Any caller attempting to pass a ControlOutput is a type error.
    Any caller attempting to pass a DiagnosticInterpretation is a
    type error.

    Phase 2 (this commit): establishes the signature; body is
    NotImplementedError. Phase 3 (analysis script) implements the
    body and applies the six descriptive elimination labels per the
    locked T3 rules.

    The returned tuple contains zero or more descriptive label
    strings drawn from the closed set:
      - accuracy_indistinguishable_from_token_prior
      - accuracy_indistinguishable_from_declared_policy_envelope
      - insufficient_measurement_headroom
      - strict_content_gap_instability
      - null_abstention_floor_unmet
      - answerable_abstention_ceiling_exceeded
    All labels are descriptive; no rejection-shape token (per joint
    disposition vocabulary rule).
    """
    raise NotImplementedError(
        "Phase 3 (analysis script) implements emit_elimination_label. "
        "Phase 2 establishes the signature only. No model invocation "
        "occurs in either phase."
    )


# ---------- control invocation stubs ----------

def invoke_unconditioned_token_prior(record) -> ControlOutput:
    """Invoke the unconditioned_token_prior control.

    UNDER D2: model invocation is NOT authorized. This function body
    is a NotImplementedError until a separately authorized D4 by-name
    Manager decision opens token-prior generations.
    """
    raise NotImplementedError(
        "unconditioned_token_prior model invocation requires Manager "
        "D4 by-name authorization. Not authorized under D2."
    )


def invoke_scrambled_binding_retrieval(record) -> ControlOutput:
    """Invoke the scrambled_binding_retrieval control (diagnostic-only).

    UNDER D2: model invocation is NOT authorized. This control is
    permanently non-eliminating; its output cannot reach the
    elimination-label code path regardless of when invocation is
    authorized. Layers 1-3 enforce this rule.
    """
    raise NotImplementedError(
        "scrambled_binding_retrieval model invocation is not authorized "
        "under D2. Note: this control is diagnostic-only; its output "
        "cannot reach emit_elimination_label by DE-2 typed boundary."
    )


# The closed set of descriptive elimination labels per the joint
# disposition (commit 019a964). Labels are descriptive; no
# rejection-shape token appears in any value.
ELIMINATION_LABEL_VALUES = (
    "accuracy_indistinguishable_from_token_prior",
    "accuracy_indistinguishable_from_declared_policy_envelope",
    "insufficient_measurement_headroom",
    "strict_content_gap_instability",
    "null_abstention_floor_unmet",
    "answerable_abstention_ceiling_exceeded",
)

# Inherited v1 label for not-ruled-out outcomes (the only label
# attached to NOT_RULED_OUT rungs under the INH-2 three-way model).
NOT_RULED_OUT_LABEL = "requires_further_investigation"

# Closed RungOutcome value set per the joint INH-2 disposition.
RUNG_OUTCOME_VALUES = (
    "inconclusive_not_actionable",
    "eliminated",
    "not_ruled_out",
)
