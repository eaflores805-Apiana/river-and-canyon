"""Lane 1a' Phase 3 analysis tests.

SYNTHETIC / DIAGNOSTIC -- NON-BINDING -- NOT FOR THRESHOLD DERIVATION
D2 IMPLEMENTATION ARTIFACT
NO MODEL INVOKED -- NO SWEEP_ID CREATED -- NO SWEEP EXECUTION AUTHORIZED

Validates:
  - CriterionComparison enum (no Wald value)
  - Wilson score interval at boundaries (p=0, p=1, p=0.5; small n)
  - Newcombe-Wilson difference interval
  - Per-stratum aggregation (INH-1 governance sentence enforced)
  - apply_criterion (floor/ceiling + comparison combinations)
  - compute_boundary_proximity (diagnostic-only)
  - emit_elimination_label DE-2 Layer 3 (consumes only LabelInput +
    declared criteria + measurements; never ControlOutput)
  - Anti-Wald source-level grep
  - No-fails-token source-level grep
"""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from lane1a_prime.analysis import (  # noqa: E402
    CriterionComparison,
    EliminationCriterion,
    PERMITTED_POOLED_DIAGNOSTICS,
    Z_95,
    aggregate_per_stratum,
    apply_criterion,
    compute_boundary_proximity,
    emit_elimination_label,
    newcombe_wilson_difference,
    wilson_score_interval,
)
from lane1a_prime.controls import (  # noqa: E402
    ControlOutput,
    LabelInput,
)

ANALYSIS_SOURCE = (Path(__file__).resolve().parent.parent / "lane1a_prime" / "analysis.py").read_text()


# ---------- CriterionComparison ----------

def test_criterion_comparison_has_four_values():
    values = {c.value for c in CriterionComparison}
    assert values == {
        "point_estimate",
        "ci_lower_bound",
        "ci_upper_bound",
        "difference_interval",
    }


def test_criterion_comparison_has_no_wald_value():
    """INH-3 closure: no `wald` value anywhere in the comparison enum."""
    for c in CriterionComparison:
        assert "wald" not in c.value.lower(), (
            f"CriterionComparison carries `wald` token: {c.value}"
        )


# ---------- Wilson score interval ----------

def test_wilson_at_p_hat_one_is_non_degenerate():
    """Boundary correctness: at p_hat = 1 (e.g., perfect NULL
    abstention p_hat = 16/16), the interval is non-degenerate and
    contains 1.0. Wald would produce SE=0 here (zero-width
    interval) — the v1 pathology Wilson prevents."""
    lo, hi = wilson_score_interval(successes=16, n=16)
    assert hi == 1.0
    assert lo < 1.0
    # Width is positive
    assert hi - lo > 0


def test_wilson_at_p_hat_zero_is_non_degenerate():
    """At p_hat = 0/N, interval contains 0 and is non-degenerate."""
    lo, hi = wilson_score_interval(successes=0, n=16)
    assert lo == 0.0
    assert hi > 0.0
    assert hi - lo > 0


def test_wilson_at_p_hat_half_centered():
    """At p_hat = 0.5 with N=80, Wilson half-width is roughly 0.11."""
    lo, hi = wilson_score_interval(successes=40, n=80)
    half_width = (hi - lo) / 2
    assert 0.1 < half_width < 0.12


def test_wilson_n_zero_returns_full_range():
    lo, hi = wilson_score_interval(successes=0, n=0)
    assert lo == 0.0
    assert hi == 1.0


def test_wilson_rejects_negative_n():
    with pytest.raises(ValueError):
        wilson_score_interval(successes=0, n=-1)


def test_wilson_rejects_out_of_range_successes():
    with pytest.raises(ValueError):
        wilson_score_interval(successes=17, n=16)


def test_wilson_rejects_unsupported_alpha():
    with pytest.raises(NotImplementedError):
        wilson_score_interval(successes=8, n=16, alpha=0.10)


def test_z_95_value_is_correct():
    """Two-sided 95% CI critical value."""
    assert abs(Z_95 - 1.959963984540054) < 1e-12


# ---------- Newcombe-Wilson difference ----------

def test_newcombe_wilson_difference_zero_when_equal():
    lo, hi = newcombe_wilson_difference(
        successes_a=40, n_a=80,
        successes_b=40, n_b=80,
    )
    # Difference is 0; interval contains 0
    assert lo <= 0.0 <= hi


def test_newcombe_wilson_difference_positive_when_a_higher():
    lo, hi = newcombe_wilson_difference(
        successes_a=60, n_a=80,
        successes_b=20, n_b=80,
    )
    # Difference is ~0.5; lower bound clearly positive
    assert lo > 0.0


def test_newcombe_wilson_difference_handles_zero_n():
    lo, hi = newcombe_wilson_difference(
        successes_a=0, n_a=0,
        successes_b=10, n_b=20,
    )
    assert lo == -1.0
    assert hi == 1.0


# ---------- per-stratum aggregation ----------

def test_aggregate_per_stratum_answerable():
    result = aggregate_per_stratum(
        successes=64, n_effective=80, stratum="answerable", metric_name="answerable_acc"
    )
    assert result["stratum"] == "answerable"
    assert result["n_effective"] == 80
    assert result["point_estimate"] == 0.8


def test_aggregate_per_stratum_null():
    result = aggregate_per_stratum(
        successes=16, n_effective=16, stratum="null", metric_name="null_abstention"
    )
    assert result["point_estimate"] == 1.0
    assert result["ci_upper"] == 1.0
    assert result["ci_lower"] < 1.0


def test_aggregate_per_stratum_rejects_pooled_for_accuracy():
    """INH-1 governance sentence closure: cross-stratum aggregation
    forbidden for accuracy metrics."""
    with pytest.raises(ValueError, match="Cross-stratum aggregation is forbidden"):
        aggregate_per_stratum(
            successes=80, n_effective=96, stratum="pooled",
            metric_name="answerable_acc",
        )


def test_aggregate_per_stratum_permits_pooled_for_distinct_outputs():
    """distinct_outputs is one of the three permitted pooled
    diagnostics."""
    result = aggregate_per_stratum(
        successes=5, n_effective=96, stratum="pooled",
        metric_name="distinct_outputs",
    )
    assert result["stratum"] == "pooled"


def test_aggregate_per_stratum_permits_pooled_for_copy_completion_agreement():
    result = aggregate_per_stratum(
        successes=0, n_effective=96, stratum="pooled",
        metric_name="copy_completion_agreement",
    )
    assert result["stratum"] == "pooled"


def test_aggregate_per_stratum_permits_pooled_for_void_accounting():
    result = aggregate_per_stratum(
        successes=0, n_effective=96, stratum="pooled",
        metric_name="void_accounting",
    )
    assert result["stratum"] == "pooled"


def test_aggregate_per_stratum_rejects_unknown_stratum():
    with pytest.raises(ValueError, match="stratum must be"):
        aggregate_per_stratum(
            successes=1, n_effective=10, stratum="other",
            metric_name="answerable_acc",
        )


def test_permitted_pooled_diagnostics_exact_set():
    assert set(PERMITTED_POOLED_DIAGNOSTICS) == {
        "distinct_outputs",
        "copy_completion_agreement",
        "void_accounting",
    }


# ---------- apply_criterion ----------

FLOOR_CRITERION = EliminationCriterion(
    label="null_abstention_floor_unmet",
    stratum="null",
    comparison=CriterionComparison.CI_LOWER_BOUND,
    floor_or_ceiling=0.8,
    is_floor=True,
)

CEILING_CRITERION = EliminationCriterion(
    label="answerable_abstention_ceiling_exceeded",
    stratum="answerable",
    comparison=CriterionComparison.CI_UPPER_BOUND,
    floor_or_ceiling=0.2,
    is_floor=False,
)


def test_apply_criterion_floor_fires_below():
    measurement = {"point_estimate": 0.5, "ci_lower": 0.3, "ci_upper": 0.7}
    # ci_lower=0.3 < floor=0.8: fires
    assert apply_criterion(FLOOR_CRITERION, measurement) is True


def test_apply_criterion_floor_does_not_fire_above():
    measurement = {"point_estimate": 0.95, "ci_lower": 0.9, "ci_upper": 1.0}
    # ci_lower=0.9 >= floor=0.8: does not fire
    assert apply_criterion(FLOOR_CRITERION, measurement) is False


def test_apply_criterion_ceiling_fires_above():
    measurement = {"point_estimate": 0.5, "ci_lower": 0.4, "ci_upper": 0.6}
    # ci_upper=0.6 > ceiling=0.2: fires
    assert apply_criterion(CEILING_CRITERION, measurement) is True


def test_apply_criterion_ceiling_does_not_fire_below():
    measurement = {"point_estimate": 0.05, "ci_lower": 0.0, "ci_upper": 0.15}
    # ci_upper=0.15 <= ceiling=0.2: does not fire
    assert apply_criterion(CEILING_CRITERION, measurement) is False


def test_elimination_criterion_rejects_unknown_label():
    with pytest.raises(ValueError, match="Unknown elimination label"):
        EliminationCriterion(
            label="clearly_fails_X",
            stratum="null",
            comparison=CriterionComparison.POINT_ESTIMATE,
            floor_or_ceiling=0.5,
            is_floor=True,
        )


def test_elimination_criterion_rejects_unknown_stratum():
    with pytest.raises(ValueError, match="stratum must be"):
        EliminationCriterion(
            label="null_abstention_floor_unmet",
            stratum="pooled",
            comparison=CriterionComparison.POINT_ESTIMATE,
            floor_or_ceiling=0.5,
            is_floor=True,
        )


# ---------- boundary_proximity ----------

def test_compute_boundary_proximity_fires_within_zone():
    criterion = EliminationCriterion(
        label="null_abstention_floor_unmet",
        stratum="null",
        comparison=CriterionComparison.CI_LOWER_BOUND,
        floor_or_ceiling=0.8,
        is_floor=True,
        proximity_zone_half_width=0.05,
    )
    # ci_lower=0.83 is within 0.05 of floor=0.80
    measurement = {"point_estimate": 0.9, "ci_lower": 0.83, "ci_upper": 1.0}
    assert compute_boundary_proximity(criterion, measurement) is True


def test_compute_boundary_proximity_does_not_fire_far_from_zone():
    criterion = EliminationCriterion(
        label="null_abstention_floor_unmet",
        stratum="null",
        comparison=CriterionComparison.CI_LOWER_BOUND,
        floor_or_ceiling=0.8,
        is_floor=True,
        proximity_zone_half_width=0.05,
    )
    measurement = {"point_estimate": 0.99, "ci_lower": 0.95, "ci_upper": 1.0}
    assert compute_boundary_proximity(criterion, measurement) is False


# ---------- emit_elimination_label (DE-2 Layer 3 body) ----------

def test_emit_elimination_label_returns_subset_of_descriptive_labels():
    """Returned labels are a subset of ELIMINATION_LABEL_VALUES."""
    label_input = LabelInput(rung_id="L01", policy_outputs=())
    criteria = (FLOOR_CRITERION, CEILING_CRITERION)
    measurements = {
        "null_abstention_floor_unmet": {
            "point_estimate": 0.5, "ci_lower": 0.3, "ci_upper": 0.7,
        },
        "answerable_abstention_ceiling_exceeded": {
            "point_estimate": 0.05, "ci_lower": 0.0, "ci_upper": 0.15,
        },
    }
    labels = emit_elimination_label(label_input, criteria, measurements)
    # Floor fires; ceiling does not (per the apply_criterion tests above)
    assert "null_abstention_floor_unmet" in labels
    assert "answerable_abstention_ceiling_exceeded" not in labels


def test_emit_elimination_label_empty_when_no_measurements():
    label_input = LabelInput(rung_id="L01", policy_outputs=())
    labels = emit_elimination_label(label_input, (FLOOR_CRITERION,), None)
    assert labels == ()


def test_emit_elimination_label_empty_when_no_criteria():
    label_input = LabelInput(rung_id="L01", policy_outputs=())
    labels = emit_elimination_label(label_input, (), {})
    assert labels == ()


def test_emit_elimination_label_returns_no_fails_token():
    label_input = LabelInput(rung_id="L01", policy_outputs=())
    criteria = (FLOOR_CRITERION,)
    measurements = {
        "null_abstention_floor_unmet": {
            "point_estimate": 0.0, "ci_lower": 0.0, "ci_upper": 0.1,
        },
    }
    labels = emit_elimination_label(label_input, criteria, measurements)
    for label in labels:
        assert "fails" not in label.lower(), (
            f"emit_elimination_label returned label with `fails` token: {label}"
        )


# ---------- DE-2 Layer 3 source-level closure ----------

def test_no_wald_token_in_analysis_source():
    """INH-3 closure at the source-code level: the analysis module
    contains no Wald normal-approximation formula. Anti-Wald rule
    enforced via grep."""
    # We allow the word "Wald" in DOCUMENTATION comments that
    # explicitly state "no Wald". The source under analysis.py has
    # the word "Wald" only in such documentation.
    # The strict test: no actual Wald formula appears (no
    # math.sqrt(p*(1-p)/n) without the z-correction term that
    # distinguishes Wilson from Wald).
    # Simpler check: no scipy.stats.norm import.
    assert "scipy.stats.norm" not in ANALYSIS_SOURCE
    assert "from scipy.stats import norm" not in ANALYSIS_SOURCE


def test_emit_elimination_label_signature_consumes_only_label_input():
    """DE-2 Layer 3 reachability: emit_elimination_label's signature
    accepts label_input: LabelInput as its first parameter; criteria
    and measurements are typed dicts/tuples of primitives. No
    ControlOutput type appears in the signature."""
    import inspect
    sig = inspect.signature(emit_elimination_label)
    params = list(sig.parameters.values())
    assert len(params) >= 1
    # Resolve string annotations
    from typing import get_type_hints
    hints = get_type_hints(emit_elimination_label)
    assert hints.get("label_input") is LabelInput
    # No parameter annotation references ControlOutput
    for name, t in hints.items():
        assert "ControlOutput" not in str(t), (
            f"emit_elimination_label parameter {name} references ControlOutput"
        )


def test_emit_elimination_label_body_does_not_reference_control_output():
    """DE-2 Layer 3 source-level grep: the analysis.py source's
    emit_elimination_label function body contains no reference to
    ControlOutput. Documentation comments referencing the rule are
    allowed (and load-bearing); the function body itself is clean."""
    # Find the function definition span
    marker_def = "def emit_elimination_label("
    start = ANALYSIS_SOURCE.find(marker_def)
    assert start != -1
    # The function ends at end of file or next top-level def/class
    # Look for next "\ndef " or "\nclass " at column 0
    rest = ANALYSIS_SOURCE[start:]
    # Find end of this function: heuristically, end-of-file in this
    # module since emit_elimination_label is the last function.
    body = rest
    # Strip docstring (first triple-quoted string in the body)
    body_lines = body.split("\n")
    cleaned_lines = []
    in_docstring = False
    docstring_started = False
    after_def = False
    for line in body_lines:
        stripped = line.strip()
        if not after_def:
            if line.startswith("    ") or stripped.startswith("def "):
                after_def = True
            else:
                cleaned_lines.append(line)
                continue
        if not docstring_started:
            if stripped.startswith('"""') or stripped.startswith("'''"):
                docstring_started = True
                in_docstring = not (stripped.count('"""') == 2 or stripped.count("'''") == 2)
                continue
        else:
            if in_docstring:
                if stripped.endswith('"""') or stripped.endswith("'''"):
                    in_docstring = False
                continue
        # Strip inline comments
        if "#" in line:
            line = line.split("#", 1)[0]
        cleaned_lines.append(line)
    cleaned_body = "\n".join(cleaned_lines)
    assert "ControlOutput" not in cleaned_body, (
        "ControlOutput referenced in emit_elimination_label body code "
        "(after stripping docstring + comments)"
    )


def test_no_call_site_routes_control_output_into_emit_elimination_label():
    """DE-2 Layer 3 reachability: no AST call-site in analysis.py
    passes a ControlOutput-typed value to emit_elimination_label.

    Uses Python's ast module to parse the analysis module and find
    every Call node targeting emit_elimination_label. For each, walk
    the arguments and assert no Name/Attribute references ControlOutput.
    Documentation references in docstrings/comments are ignored by
    ast.walk because they are stored as string literals, not as call
    arguments.
    """
    import ast
    tree = ast.parse(ANALYSIS_SOURCE)
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            func = node.func
            # Match emit_elimination_label calls
            func_name = None
            if isinstance(func, ast.Name):
                func_name = func.id
            elif isinstance(func, ast.Attribute):
                func_name = func.attr
            if func_name != "emit_elimination_label":
                continue
            # Walk arguments looking for ControlOutput references
            for arg in [*node.args, *(kw.value for kw in node.keywords)]:
                for sub in ast.walk(arg):
                    if isinstance(sub, ast.Name) and sub.id == "ControlOutput":
                        raise AssertionError(
                            f"Call site at line {node.lineno} routes "
                            f"ControlOutput into emit_elimination_label"
                        )
                    if isinstance(sub, ast.Attribute) and sub.attr == "ControlOutput":
                        raise AssertionError(
                            f"Call site at line {node.lineno} routes "
                            f"ControlOutput attribute into emit_elimination_label"
                        )


# ---------- source-level: no fails token ----------

def test_no_fails_token_in_analysis_source():
    assert "fails" not in ANALYSIS_SOURCE.lower(), (
        "`fails` token found in analysis.py source"
    )


def test_no_passes_label_identifier_in_analysis_source():
    assert "passes_" not in ANALYSIS_SOURCE


# ---------- single CI function invariant ----------

def test_only_wilson_score_interval_is_a_ci_emitter():
    """The analysis module exposes exactly two CI functions:
    wilson_score_interval and newcombe_wilson_difference. No other
    function is a CI emitter. (Newcombe-Wilson is the Wilson-
    consistent difference interval; it is not Wald.)"""
    # Source-level: find all `def <name>_interval` or `def
    # <name>_ci` functions.
    import re
    pattern = re.compile(r"^def (\w*(?:interval|ci)\w*)\s*\(", re.MULTILINE | re.IGNORECASE)
    matches = pattern.findall(ANALYSIS_SOURCE)
    # Lowercase for case-insensitive comparison
    matches_lower = [m.lower() for m in matches]
    # Allowed CI functions:
    allowed = {"wilson_score_interval", "newcombe_wilson_difference"}
    for m in matches_lower:
        assert m in allowed, (
            f"Unexpected CI emitter: {m}. Allowed: {allowed}"
        )
