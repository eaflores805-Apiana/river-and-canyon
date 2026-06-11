"""Lane 1a' Phase 2 control tests.

SYNTHETIC / DIAGNOSTIC -- NON-BINDING -- NOT FOR THRESHOLD DERIVATION
D2 IMPLEMENTATION ARTIFACT
NO MODEL INVOKED -- NO SWEEP_ID CREATED -- NO SWEEP EXECUTION AUTHORIZED

Validates the DE-2 typed boundary (Bundle v0.3 §I.5):

  Layer 1 (this module's coverage): LabelInput has NO field of type
  ControlOutput; emit_elimination_label accepts only LabelInput; the
  CONTROL_SPECS dictionary marks scrambled_binding_retrieval as
  none_diagnostic_only.

  Layer 2 (covered in test_schemas.py): the sidecar schema's
  elimination_label_basis.basis_policies enum excludes control names.

  Layer 3 (Phase 3): source-level grep on the analysis script (not
  written yet).
"""
from __future__ import annotations

import dataclasses
import inspect
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from lane1a_prime.controls import (  # noqa: E402
    CONTROL_SPECS,
    ControlOutput,
    ControlSpec,
    DiagnosticInterpretation,
    ELIMINATION_LABEL_VALUES,
    LabelInput,
    NOT_RULED_OUT_LABEL,
    RUNG_OUTCOME_VALUES,
    SCRAMBLED_BINDING_RETRIEVAL_SPEC,
    UNCONDITIONED_TOKEN_PRIOR_SPEC,
    emit_elimination_label,
    invoke_scrambled_binding_retrieval,
    invoke_unconditioned_token_prior,
)

CONTROLS_SOURCE = (Path(__file__).resolve().parent.parent / "lane1a_prime" / "controls.py").read_text()


# ---------- T2 control specifications ----------

def test_control_specs_registry_has_two_entries():
    assert set(CONTROL_SPECS.keys()) == {
        "unconditioned_token_prior",
        "scrambled_binding_retrieval",
    }


def test_unconditioned_token_prior_spec_is_eliminative():
    assert UNCONDITIONED_TOKEN_PRIOR_SPEC.eliminative_status == (
        "referenced_by_elimination_criteria_per_t3"
    )


def test_scrambled_binding_retrieval_spec_is_diagnostic_only():
    """Joint disposition closure: scrambled_binding_retrieval is
    permanently diagnostic-only and non-eliminating."""
    assert SCRAMBLED_BINDING_RETRIEVAL_SPEC.eliminative_status == (
        "none_diagnostic_only"
    )


def test_unconditioned_token_prior_spec_baseline_references_value_pool_size():
    """Joint disposition closure: pool-visible shell; baseline =
    1/|VALUE_POOL| = 1/26."""
    spec = UNCONDITIONED_TOKEN_PRIOR_SPEC
    assert "1/26" in spec.expected_baseline


def test_unconditioned_token_prior_spec_binding_removed():
    assert UNCONDITIONED_TOKEN_PRIOR_SPEC.binding_handling == "removed"


def test_scrambled_binding_retrieval_spec_binding_scrambled():
    assert SCRAMBLED_BINDING_RETRIEVAL_SPEC.binding_handling == "scrambled"


# ---------- DE-2 typed boundary ----------

def test_label_input_has_no_field_of_type_control_output():
    """DE-2 Layer 1 closure (structural): LabelInput dataclass fields
    do NOT include any field annotated as ControlOutput."""
    fields = dataclasses.fields(LabelInput)
    for field in fields:
        # The type annotation may be a string or a class. We check
        # both forms to catch any ControlOutput reference.
        type_str = str(field.type)
        assert "ControlOutput" not in type_str, (
            f"LabelInput field {field.name} references ControlOutput"
        )


def test_emit_elimination_label_accepts_only_label_input():
    """DE-2 Layer 1 closure: emit_elimination_label signature accepts
    a single parameter of type LabelInput. No other type."""
    sig = inspect.signature(emit_elimination_label)
    params = list(sig.parameters.values())
    assert len(params) == 1
    # Resolve string annotations (from __future__ import annotations)
    # to actual types.
    from typing import get_type_hints
    hints = get_type_hints(emit_elimination_label)
    assert hints["label_input"] is LabelInput


def test_emit_elimination_label_not_implemented_under_d2():
    """Phase 2 establishes the signature; body is NotImplementedError
    until Phase 3 (analysis script). This test verifies the body has
    not been silently implemented."""
    li = LabelInput(rung_id="L01", policy_outputs=())
    with pytest.raises(NotImplementedError):
        emit_elimination_label(li)


def test_invoke_unconditioned_token_prior_blocked_under_d2():
    """D2 boundary: model invocation is not authorized. The control
    invocation function raises NotImplementedError until a separately
    authorized D4 by-name Manager decision opens it."""
    with pytest.raises(NotImplementedError):
        invoke_unconditioned_token_prior({})


def test_invoke_scrambled_binding_retrieval_blocked_under_d2():
    """D2 boundary: model invocation is not authorized. Note: this
    control is permanently diagnostic-only regardless of authorization."""
    with pytest.raises(NotImplementedError):
        invoke_scrambled_binding_retrieval({})


# ---------- diagnostic interpretation ----------

def test_diagnostic_interpretation_carries_both_control_and_policy_outputs():
    """DiagnosticInterpretation may carry both control and policy
    outputs, because it is consumed by DIAGNOSTIC reporting only;
    it is not routed to emit_elimination_label by any module."""
    interp = DiagnosticInterpretation(
        rung_id="L01",
        control_outputs=(),
        policy_outputs=(),
    )
    assert interp.rung_id == "L01"


# ---------- elimination label vocabulary ----------

def test_elimination_label_values_match_joint_disposition():
    """Six descriptive labels per the joint disposition (commit 019a964)."""
    expected = {
        "accuracy_indistinguishable_from_token_prior",
        "accuracy_indistinguishable_from_declared_policy_envelope",
        "insufficient_measurement_headroom",
        "strict_content_gap_instability",
        "null_abstention_floor_unmet",
        "answerable_abstention_ceiling_exceeded",
    }
    assert set(ELIMINATION_LABEL_VALUES) == expected


def test_no_fails_token_in_elimination_label_values():
    for value in ELIMINATION_LABEL_VALUES:
        assert "fails" not in value.lower(), (
            f"`fails` token in elimination label value: {value}"
        )


def test_not_ruled_out_label_is_requires_further_investigation():
    assert NOT_RULED_OUT_LABEL == "requires_further_investigation"


def test_rung_outcome_values_three_way():
    """INH-2 three-way outcome closure."""
    assert set(RUNG_OUTCOME_VALUES) == {
        "inconclusive_not_actionable",
        "eliminated",
        "not_ruled_out",
    }


def test_rung_outcome_values_no_passes_value():
    for value in RUNG_OUTCOME_VALUES:
        assert "passes" not in value.lower(), (
            f"`passes` token in rung outcome value: {value}"
        )


# ---------- source-level invariants ----------

def test_no_fails_token_in_controls_source():
    """Joint disposition rule at source level."""
    assert "fails" not in CONTROLS_SOURCE.lower(), (
        "`fails` token found in controls.py source"
    )


def test_no_passes_label_identifier_in_controls_source():
    """Source-level: no identifier of the form passes_X."""
    assert "passes_" not in CONTROLS_SOURCE


def test_emit_elimination_label_signature_in_source():
    """Source-level grep: the function emit_elimination_label is
    defined with signature (label_input: LabelInput). The DE-2
    invariant lives both in the test above (Layer 1) and here as
    defense-in-depth."""
    assert "def emit_elimination_label(label_input: LabelInput)" in CONTROLS_SOURCE


def test_label_input_dataclass_definition_excludes_control_output_field():
    """Source-level grep: the LabelInput dataclass definition does
    not include a field annotated as ControlOutput."""
    # Locate the LabelInput class definition.
    marker_start = CONTROLS_SOURCE.find("class LabelInput:")
    assert marker_start != -1
    # The class definition ends at the next top-level class/def.
    next_top = CONTROLS_SOURCE.find("\n@dataclass", marker_start + 1)
    if next_top == -1:
        next_top = CONTROLS_SOURCE.find("\ndef ", marker_start + 1)
    body = CONTROLS_SOURCE[marker_start:next_top if next_top != -1 else len(CONTROLS_SOURCE)]
    # Inside the LabelInput body, the type ControlOutput must not
    # appear in any field annotation. (References in docstring/comments
    # are allowed and load-bearing.)
    # Strip docstring section (triple quotes).
    body_lines = body.split("\n")
    # Remove docstring lines
    cleaned = []
    in_docstring = False
    for line in body_lines:
        stripped = line.strip()
        if stripped.startswith('"""') or stripped.startswith("'''"):
            in_docstring = not in_docstring
            continue
        if in_docstring:
            continue
        # Strip inline comments
        if "#" in line:
            line = line.split("#", 1)[0]
        cleaned.append(line)
    cleaned_text = "\n".join(cleaned)
    # No active code line in LabelInput body mentions ControlOutput
    assert "ControlOutput" not in cleaned_text, (
        "ControlOutput referenced in LabelInput dataclass field definitions"
    )
