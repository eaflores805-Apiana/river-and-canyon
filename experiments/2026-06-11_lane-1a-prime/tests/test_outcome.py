"""Lane 1a' Phase 3 outcome tests.

SYNTHETIC / DIAGNOSTIC -- NON-BINDING -- NOT FOR THRESHOLD DERIVATION
D2 IMPLEMENTATION ARTIFACT
NO MODEL INVOKED -- NO SWEEP_ID CREATED -- NO SWEEP EXECUTION AUTHORIZED

Validates the INH-2 three-way outcome model implementation:
  - RungOutcome three-way enum (no passes_X value)
  - compute_rung_outcome precedence (INCONCLUSIVE -> ELIMINATED -> NOT_RULED_OUT)
  - compute_K counts NOT_RULED_OUT only
  - boundary_proximity_flags do NOT affect outcome
  - Three fixed-language constants
  - emit_outcome_statement K=0 / K=1 / K>=2
"""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from lane1a_prime.outcome import (  # noqa: E402
    K_EQUALS_ZERO_STATEMENT,
    MULTIPLE_NOT_RULED_OUT_STATEMENT_TEMPLATE,
    RungEvaluation,
    RungOutcome,
    SINGLE_NOT_RULED_OUT_RUNG_STATEMENT,
    compute_K,
    compute_rung_outcome,
    emit_outcome_statement,
)
from lane1a_prime.controls import NOT_RULED_OUT_LABEL  # noqa: E402

OUTCOME_SOURCE = (Path(__file__).resolve().parent.parent / "lane1a_prime" / "outcome.py").read_text()


# ---------- RungOutcome enum ----------

def test_rung_outcome_has_three_values():
    values = {o.value for o in RungOutcome}
    assert values == {
        "inconclusive_not_actionable",
        "eliminated",
        "not_ruled_out",
    }


def test_rung_outcome_has_no_passes_value():
    for outcome in RungOutcome:
        assert "passes" not in outcome.value.lower(), (
            f"RungOutcome value carries `passes` token: {outcome.value}"
        )


# ---------- compute_rung_outcome precedence ----------

def test_compute_rung_outcome_inconclusive_preempts():
    """INCONCLUSIVE preempts even when elimination labels are
    present (data insufficient means we can't trust those labels)."""
    eval_ = RungEvaluation(
        rung_id="L01",
        is_data_sufficient=False,
        attached_elimination_labels=(
            "accuracy_indistinguishable_from_token_prior",
        ),
        boundary_proximity_flags={},
    )
    outcome, labels = compute_rung_outcome(eval_)
    assert outcome == RungOutcome.INCONCLUSIVE
    assert labels == ()


def test_compute_rung_outcome_eliminated_when_labels_attached():
    eval_ = RungEvaluation(
        rung_id="L02",
        is_data_sufficient=True,
        attached_elimination_labels=(
            "accuracy_indistinguishable_from_token_prior",
            "insufficient_measurement_headroom",
        ),
        boundary_proximity_flags={},
    )
    outcome, labels = compute_rung_outcome(eval_)
    assert outcome == RungOutcome.ELIMINATED
    assert set(labels) == {
        "accuracy_indistinguishable_from_token_prior",
        "insufficient_measurement_headroom",
    }


def test_compute_rung_outcome_not_ruled_out_when_no_label():
    eval_ = RungEvaluation(
        rung_id="L03",
        is_data_sufficient=True,
        attached_elimination_labels=(),
        boundary_proximity_flags={},
    )
    outcome, labels = compute_rung_outcome(eval_)
    assert outcome == RungOutcome.NOT_RULED_OUT
    assert labels == ("requires_further_investigation",)


def test_compute_rung_outcome_boundary_proximity_does_not_affect_outcome():
    """boundary_proximity_flag is diagnostic-only and must NOT enter
    outcome determination. Setting all flags to True must not alter
    the outcome derived from is_data_sufficient + attached labels."""
    eval_ = RungEvaluation(
        rung_id="L04",
        is_data_sufficient=True,
        attached_elimination_labels=(),
        boundary_proximity_flags={
            "null_abstention_floor": True,
            "answerable_abstention_ceiling": True,
            "token_prior_separation": True,
        },
    )
    outcome, labels = compute_rung_outcome(eval_)
    # Boundary flags set; outcome must still be NOT_RULED_OUT
    assert outcome == RungOutcome.NOT_RULED_OUT
    assert labels == ("requires_further_investigation",)


def test_compute_rung_outcome_boundary_proximity_does_not_affect_eliminated():
    eval_ = RungEvaluation(
        rung_id="L05",
        is_data_sufficient=True,
        attached_elimination_labels=("insufficient_measurement_headroom",),
        boundary_proximity_flags={"headroom_criterion": True},
    )
    outcome, _labels = compute_rung_outcome(eval_)
    # Outcome is ELIMINATED regardless of boundary flag
    assert outcome == RungOutcome.ELIMINATED


def test_rung_evaluation_rejects_unknown_label():
    with pytest.raises(ValueError, match="Unknown elimination label"):
        RungEvaluation(
            rung_id="L06",
            is_data_sufficient=True,
            attached_elimination_labels=("clearly_fails_X",),
            boundary_proximity_flags={},
        )


# ---------- compute_K ----------

def test_compute_K_counts_not_ruled_out_only():
    outcomes = [
        ("L01", RungOutcome.NOT_RULED_OUT),
        ("L02", RungOutcome.ELIMINATED),
        ("L03", RungOutcome.NOT_RULED_OUT),
        ("L04", RungOutcome.INCONCLUSIVE),
        ("L05", RungOutcome.NOT_RULED_OUT),
    ]
    assert compute_K(outcomes) == 3


def test_compute_K_excludes_inconclusive():
    outcomes = [
        ("L01", RungOutcome.INCONCLUSIVE),
        ("L02", RungOutcome.INCONCLUSIVE),
    ]
    assert compute_K(outcomes) == 0


def test_compute_K_excludes_eliminated():
    outcomes = [
        ("L01", RungOutcome.ELIMINATED),
        ("L02", RungOutcome.ELIMINATED),
    ]
    assert compute_K(outcomes) == 0


def test_compute_K_empty():
    assert compute_K([]) == 0


# ---------- fixed-language constants ----------

def test_k_zero_statement_uses_not_ruled_out_phrasing():
    assert "not-ruled-out" in K_EQUALS_ZERO_STATEMENT
    assert "K=0" in K_EQUALS_ZERO_STATEMENT
    assert "reconnaissance-negative" in K_EQUALS_ZERO_STATEMENT


def test_single_not_ruled_out_statement_uses_not_ruled_out_phrasing():
    assert "K=1" in SINGLE_NOT_RULED_OUT_RUNG_STATEMENT
    assert "not-ruled-out" in SINGLE_NOT_RULED_OUT_RUNG_STATEMENT
    # No-positive-use rule referenced
    assert "no-positive-use" in SINGLE_NOT_RULED_OUT_RUNG_STATEMENT


def test_multiple_not_ruled_out_template_formats_k_and_rung_ids():
    formatted = MULTIPLE_NOT_RULED_OUT_STATEMENT_TEMPLATE.format(
        k=3, rung_ids="L01, L04, L07"
    )
    assert "K=3" in formatted
    assert "L01, L04, L07" in formatted
    assert "not-ruled-out" in formatted


def test_no_passes_token_in_outcome_constants():
    for c in (
        K_EQUALS_ZERO_STATEMENT,
        SINGLE_NOT_RULED_OUT_RUNG_STATEMENT,
        MULTIPLE_NOT_RULED_OUT_STATEMENT_TEMPLATE,
    ):
        # The constants describe what was/wasn't ruled out; they must
        # not carry passes_X labels of any kind.
        assert "passes_" not in c


# ---------- emit_outcome_statement ----------

def test_emit_outcome_statement_k_zero():
    out = emit_outcome_statement(0)
    assert out == K_EQUALS_ZERO_STATEMENT


def test_emit_outcome_statement_k_one():
    out = emit_outcome_statement(1, ("L05",))
    assert out == SINGLE_NOT_RULED_OUT_RUNG_STATEMENT


def test_emit_outcome_statement_k_two():
    out = emit_outcome_statement(2, ("L03", "L05"))
    assert "K=2" in out
    # Rung IDs listed in sorted order
    assert "L03, L05" in out


def test_emit_outcome_statement_k_geq_2_orders_rung_ids():
    out = emit_outcome_statement(3, ("L07", "L01", "L04"))
    assert "L01, L04, L07" in out


def test_emit_outcome_statement_rejects_negative_k():
    with pytest.raises(ValueError):
        emit_outcome_statement(-1)


# ---------- source-level invariants ----------

def test_no_fails_token_in_outcome_source():
    # The source includes the descriptive label vocabulary but no
    # rejection-shape token.
    # We check the lowercased source contains no "fails" word.
    # Note: descriptive labels do not contain "fails".
    assert "fails" not in OUTCOME_SOURCE.lower(), (
        "`fails` token found in outcome.py source"
    )


def test_outcome_source_imports_not_ruled_out_label_from_controls():
    """outcome.py reuses the canonical NOT_RULED_OUT_LABEL constant
    from controls.py rather than redefining the string."""
    assert "from lane1a_prime.controls import" in OUTCOME_SOURCE
    assert "NOT_RULED_OUT_LABEL" in OUTCOME_SOURCE


def test_outcome_constants_only_three():
    """Closure: outcome module exports exactly three fixed-language
    constants. Any new constant requires explicit Team Lead approval
    per the no-survivor-ranking doctrine."""
    # Source-level grep: count standalone uppercase top-level assignments
    # ending in _STATEMENT / _TEMPLATE.
    import re
    pattern = re.compile(r"^(K_EQUALS_ZERO_STATEMENT|SINGLE_NOT_RULED_OUT_RUNG_STATEMENT|MULTIPLE_NOT_RULED_OUT_STATEMENT_TEMPLATE)\s*=", re.MULTILINE)
    matches = pattern.findall(OUTCOME_SOURCE)
    assert len(matches) == 3
    assert set(matches) == {
        "K_EQUALS_ZERO_STATEMENT",
        "SINGLE_NOT_RULED_OUT_RUNG_STATEMENT",
        "MULTIPLE_NOT_RULED_OUT_STATEMENT_TEMPLATE",
    }
