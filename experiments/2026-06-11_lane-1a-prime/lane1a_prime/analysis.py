"""Lane 1a' analysis script.

SYNTHETIC / DIAGNOSTIC -- NON-BINDING -- NOT FOR THRESHOLD DERIVATION
D2 IMPLEMENTATION ARTIFACT (PHASE 3)
NO MODEL INVOKED -- NO SWEEP_ID CREATED -- NO SWEEP EXECUTION AUTHORIZED

Implements:

  - CriterionComparison enum (no Wald value).
  - EliminationCriterion dataclass (pre-registered T3 declarations).
  - wilson_score_interval (single CI emitter in the analysis pipeline;
    no continuity correction; boundary-correct).
  - newcombe_wilson_difference (CI for difference between two
    proportions; used by the token-prior separation criterion).
  - aggregate_per_stratum (INH-1 per-stratum aggregation; enforces
    the cross-stratum aggregation prohibition for accuracy and
    abstention metrics).
  - apply_criterion (compares measurement against floor/ceiling
    per the declared CriterionComparison).
  - compute_boundary_proximity (diagnostic-only; never enters
    outcome determination).
  - emit_elimination_label (DE-2 Layer 3 body; consumes LabelInput
    and locked criteria/measurements; never consumes ControlOutput).

DE-2 Layer 3 closure: this module's source contains no reference
to ControlOutput in any function body. A source-level grep test
in tests/test_analysis.py enforces this rule. The
emit_elimination_label body operates only on LabelInput and the
explicitly-passed criteria + measurements (which are derived from
LabelInput.policy_outputs by upstream code, never from controls).
"""
from __future__ import annotations

import math
from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

from lane1a_prime.controls import (
    ELIMINATION_LABEL_VALUES,
    LabelInput,
)


# Two-sided z critical value for 95% confidence (alpha=0.05).
# Hardcoded for the lane's single confidence level. Adding other
# alphas at packet stage extends this constant set; does not
# introduce Wald.
Z_95 = 1.959963984540054


class CriterionComparison(Enum):
    """Per-criterion comparison rule per joint disposition (commit 019a964).

    Each T3 criterion declares which value compares against its
    floor/ceiling. The enum is the closed set of permitted comparisons.

    Note: there is no "wald" value. The single CI emitter in this
    module is wilson_score_interval; the difference CI emitter is
    newcombe_wilson_difference. A source-level grep test asserts
    no Wald normal-approximation appears in this module.
    """
    POINT_ESTIMATE = "point_estimate"
    CI_LOWER_BOUND = "ci_lower_bound"
    CI_UPPER_BOUND = "ci_upper_bound"
    DIFFERENCE_INTERVAL = "difference_interval"


@dataclass(frozen=True)
class EliminationCriterion:
    """A pre-registered T3 elimination criterion.

    All fields are declared at packet seal (Phase 4/5 lock); locked
    into T3 plan and hashed into LOCK-RECORD via t3_plan_hash.
    Post-pilot change is a must-fix event per anti-tuning rule.
    """
    label: str  # one of ELIMINATION_LABEL_VALUES (descriptive)
    stratum: str  # "answerable" | "null"
    comparison: CriterionComparison
    floor_or_ceiling: float  # the locked threshold
    is_floor: bool  # True if floor (criterion fires when measurement < floor);
                    # False if ceiling (criterion fires when measurement > ceiling)
    proximity_zone_half_width: float = 0.05  # boundary_proximity zone (diagnostic-only)

    def __post_init__(self) -> None:
        valid_labels = set(ELIMINATION_LABEL_VALUES)
        if self.label not in valid_labels:
            raise ValueError(
                f"Unknown elimination label: {self.label!r}. "
                f"Must be one of {sorted(valid_labels)}."
            )
        if self.stratum not in ("answerable", "null"):
            raise ValueError(
                f"stratum must be 'answerable' or 'null', got {self.stratum!r}."
            )


# ---------- Wilson score interval (single CI emitter) ----------

def wilson_score_interval(
    successes: int,
    n: int,
    alpha: float = 0.05,
) -> tuple[float, float]:
    """Wilson score interval without continuity correction.

    The SINGLE confidence-interval emitter for binomial proportions
    in the analysis pipeline. Boundary-correct: at p_hat in {0, 1}
    the interval is non-degenerate and contained in [0, 1].

    Per INH-3 joint disposition. No Wald normal-approximation
    appears in this function.

    For n == 0 returns the full interval (0.0, 1.0) — no information.

    Currently supports alpha == 0.05 (Z_95). Additional alphas
    require explicit z critical values, never silent Wald.
    """
    if n < 0:
        raise ValueError(f"n must be non-negative, got {n!r}.")
    if successes < 0 or successes > n:
        raise ValueError(
            f"successes must be in [0, n]={n!r}, got {successes!r}."
        )
    if alpha != 0.05:
        raise NotImplementedError(
            f"Only alpha=0.05 is implemented; got alpha={alpha!r}. "
            f"Adding additional alphas requires explicit z values."
        )

    if n == 0:
        return (0.0, 1.0)

    z = Z_95
    p_hat = successes / n
    z2 = z * z
    denominator = 1.0 + z2 / n
    center = (p_hat + z2 / (2.0 * n)) / denominator
    margin = (z / denominator) * math.sqrt(
        p_hat * (1.0 - p_hat) / n + z2 / (4.0 * n * n)
    )
    lo = max(0.0, center - margin)
    hi = min(1.0, center + margin)
    return (lo, hi)


def newcombe_wilson_difference(
    successes_a: int,
    n_a: int,
    successes_b: int,
    n_b: int,
    alpha: float = 0.05,
) -> tuple[float, float]:
    """Newcombe-Wilson hybrid CI for the difference (p_a - p_b).

    Uses Wilson intervals on each proportion separately, then
    combines per Newcombe's method 10. Boundary-correct at p in
    {0, 1}.

    Used by the token_prior separation criterion (candidate
    accuracy minus control accuracy).
    """
    lo_a, hi_a = wilson_score_interval(successes_a, n_a, alpha=alpha)
    lo_b, hi_b = wilson_score_interval(successes_b, n_b, alpha=alpha)

    if n_a == 0 or n_b == 0:
        # No information; return full range.
        return (-1.0, 1.0)

    p_a = successes_a / n_a
    p_b = successes_b / n_b

    # Newcombe method 10: combine Wilson intervals.
    lower = (p_a - p_b) - math.sqrt(
        (p_a - lo_a) ** 2 + (hi_b - p_b) ** 2
    )
    upper = (p_a - p_b) + math.sqrt(
        (hi_a - p_a) ** 2 + (p_b - lo_b) ** 2
    )
    return (max(-1.0, lower), min(1.0, upper))


# ---------- per-stratum aggregation (INH-1) ----------

# Pooled-N=96 diagnostics permitted per joint disposition.
# All other metrics are per-stratum and may NOT aggregate cross-stratum.
PERMITTED_POOLED_DIAGNOSTICS = (
    "distinct_outputs",
    "copy_completion_agreement",
    "void_accounting",
)


def aggregate_per_stratum(
    successes: int,
    n_effective: int,
    stratum: str,
    metric_name: str,
) -> dict:
    """Compute per-stratum aggregate with Wilson CI.

    INH-1 closure: enforces that accuracy and abstention metrics
    operate on stratum-specific N_effective. The metric_name argument
    is checked against PERMITTED_POOLED_DIAGNOSTICS; any metric not
    in that list and a stratum of "pooled" raises ValueError.

    Returns:
      {
        "stratum": str,
        "n_effective": int,
        "successes": int,
        "point_estimate": float,
        "ci_lower": float,
        "ci_upper": float,
      }
    """
    if stratum == "pooled":
        if metric_name not in PERMITTED_POOLED_DIAGNOSTICS:
            raise ValueError(
                f"Cross-stratum aggregation is forbidden for {metric_name!r}. "
                f"Only {PERMITTED_POOLED_DIAGNOSTICS} may compute over pooled N. "
                f"Any future exception is a must-fix requiring C1 disposition "
                f"(joint disposition governance sentence)."
            )
    elif stratum not in ("answerable", "null"):
        raise ValueError(
            f"stratum must be 'answerable', 'null', or 'pooled', "
            f"got {stratum!r}."
        )

    if n_effective == 0:
        return {
            "stratum": stratum,
            "n_effective": 0,
            "successes": successes,
            "point_estimate": 0.0,
            "ci_lower": 0.0,
            "ci_upper": 1.0,
        }

    point_estimate = successes / n_effective
    ci_lower, ci_upper = wilson_score_interval(successes, n_effective)
    return {
        "stratum": stratum,
        "n_effective": n_effective,
        "successes": successes,
        "point_estimate": point_estimate,
        "ci_lower": ci_lower,
        "ci_upper": ci_upper,
    }


# ---------- criterion application ----------

def apply_criterion(
    criterion: EliminationCriterion,
    measurement: dict,
) -> bool:
    """Return True iff the criterion fires given a measurement.

    measurement should be a dict from aggregate_per_stratum or
    equivalent, containing 'point_estimate', 'ci_lower', 'ci_upper'.

    For DIFFERENCE_INTERVAL criteria the measurement dict should
    additionally carry 'difference_lower' and 'difference_upper'
    from newcombe_wilson_difference.
    """
    floor_or_ceiling = criterion.floor_or_ceiling

    if criterion.comparison == CriterionComparison.POINT_ESTIMATE:
        value = measurement["point_estimate"]
    elif criterion.comparison == CriterionComparison.CI_LOWER_BOUND:
        value = measurement["ci_lower"]
    elif criterion.comparison == CriterionComparison.CI_UPPER_BOUND:
        value = measurement["ci_upper"]
    elif criterion.comparison == CriterionComparison.DIFFERENCE_INTERVAL:
        # For differences, "fires" rule depends on whether the
        # interval contains the floor/ceiling boundary.
        # For Phase 3 skeleton: criterion fires iff the
        # difference_lower exceeds the floor (or
        # difference_upper falls below the ceiling).
        if criterion.is_floor:
            value = measurement.get("difference_lower", 0.0)
        else:
            value = measurement.get("difference_upper", 0.0)
    else:
        raise ValueError(
            f"Unknown CriterionComparison: {criterion.comparison!r}"
        )

    if criterion.is_floor:
        # Criterion fires when measurement falls BELOW the floor.
        return value < floor_or_ceiling
    else:
        # Criterion fires when measurement exceeds the ceiling.
        return value > floor_or_ceiling


def compute_boundary_proximity(
    criterion: EliminationCriterion,
    measurement: dict,
) -> bool:
    """Return True iff measurement falls within the criterion's
    pre-declared proximity zone.

    DIAGNOSTIC-ONLY: this value is reported on the RungEvaluation's
    boundary_proximity_flags dict and the diagnostics appendix; it
    does NOT enter compute_rung_outcome's decision path.
    """
    if criterion.comparison == CriterionComparison.POINT_ESTIMATE:
        value = measurement["point_estimate"]
    elif criterion.comparison == CriterionComparison.CI_LOWER_BOUND:
        value = measurement["ci_lower"]
    elif criterion.comparison == CriterionComparison.CI_UPPER_BOUND:
        value = measurement["ci_upper"]
    elif criterion.comparison == CriterionComparison.DIFFERENCE_INTERVAL:
        value = (
            measurement.get("difference_lower", 0.0)
            if criterion.is_floor
            else measurement.get("difference_upper", 0.0)
        )
    else:
        return False

    distance = abs(value - criterion.floor_or_ceiling)
    return distance <= criterion.proximity_zone_half_width


# ---------- emit_elimination_label (DE-2 Layer 3 body) ----------

def emit_elimination_label(
    label_input: LabelInput,
    criteria: tuple[EliminationCriterion, ...] = (),
    measurements: Optional[dict[str, dict]] = None,
) -> tuple[str, ...]:
    """Apply pre-registered elimination criteria; return attached labels.

    DE-2 Layer 3 invariant: this function consumes ONLY:
      - label_input: LabelInput (whose policy_outputs are derived
        from envelope policies in policies.py; no control outputs)
      - criteria: tuple[EliminationCriterion, ...] (locked T3 declarations)
      - measurements: dict[label, dict] (pre-aggregated per-stratum
        measurements; derived from policy outputs only by upstream
        code in this module)

    This function does NOT consume ControlOutput. The criteria and
    measurements arguments are typed dicts/tuples of declared
    primitives; ControlOutput never reaches this code path. Verified
    by source-level grep test in test_analysis.py.

    Returns a tuple of descriptive labels (subset of
    ELIMINATION_LABEL_VALUES) for criteria that fired. All labels
    are descriptive; no rejection-shape token appears in any returned
    value.
    """
    if measurements is None:
        # No criteria can fire without measurements; return empty.
        return ()

    attached_labels: list[str] = []

    # Reference label_input.rung_id only for downstream telemetry,
    # if needed; this function uses it as a no-op so the parameter
    # is not unused.
    _rung_id = label_input.rung_id

    for criterion in criteria:
        measurement = measurements.get(criterion.label)
        if measurement is None:
            # No measurement available for this criterion; skip.
            # (Data-sufficiency checks upstream may have already
            # set the rung to INCONCLUSIVE; emit_elimination_label
            # returns empty here regardless.)
            continue
        if apply_criterion(criterion, measurement):
            attached_labels.append(criterion.label)

    return tuple(attached_labels)
