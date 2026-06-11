"""Lane 1a' outcome chooser.

SYNTHETIC / DIAGNOSTIC -- NON-BINDING -- NOT FOR THRESHOLD DERIVATION
D2 IMPLEMENTATION ARTIFACT (PHASE 3)
NO MODEL INVOKED -- NO SWEEP_ID CREATED -- NO SWEEP EXECUTION AUTHORIZED

Implements the INH-2 three-way outcome model per joint disposition
(commit 019a964):

  RungOutcome.INCONCLUSIVE  - data insufficient; preempts evaluation
  RungOutcome.ELIMINATED    - one or more elimination labels attached
  RungOutcome.NOT_RULED_OUT - measurable; no elimination label attached;
                              attached label is the inherited
                              "requires_further_investigation" string

K = |{rung : outcome == NOT_RULED_OUT}|.

boundary_proximity_flag values are CARRIED on the RungEvaluation but
DO NOT participate in outcome determination. They are diagnostic-only
fields excluded from outcome / K / fixed language.

Three fixed-language constants emit at most one statement per sweep:

  K_EQUALS_ZERO_STATEMENT
  SINGLE_NOT_RULED_OUT_RUNG_STATEMENT
  MULTIPLE_NOT_RULED_OUT_STATEMENT_TEMPLATE

`emit_outcome_statement(K, not_ruled_out_rung_ids)` selects exactly
one of the three.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

from lane1a_prime.controls import (
    ELIMINATION_LABEL_VALUES,
    NOT_RULED_OUT_LABEL,
)


class RungOutcome(Enum):
    """Three-way outcome enum per INH-2 joint disposition.

    No `passes_X` value. The doctrine "may rule out, may not rule in"
    is enforced structurally by the absence of any positive outcome
    value.
    """
    INCONCLUSIVE = "inconclusive_not_actionable"
    ELIMINATED = "eliminated"
    NOT_RULED_OUT = "not_ruled_out"


@dataclass(frozen=True)
class RungEvaluation:
    """Per-rung evaluation; input to compute_rung_outcome.

    Fields:
      rung_id: neutral rung identifier (L01..L08)
      is_data_sufficient: False iff data-sufficiency check failed
                          (void budget exceeded; required outputs
                          missing from sidecar; harness anomaly).
                          False -> INCONCLUSIVE.
      attached_elimination_labels: tuple of descriptive label strings
                                   (subset of ELIMINATION_LABEL_VALUES).
                                   Non-empty -> ELIMINATED.
      boundary_proximity_flags: per-criterion {criterion_id -> bool}.
                                DIAGNOSTIC-ONLY. Does NOT enter
                                outcome determination, K computation,
                                or fixed-language emission.
    """
    rung_id: str
    is_data_sufficient: bool
    attached_elimination_labels: tuple[str, ...]
    boundary_proximity_flags: dict[str, bool] = field(default_factory=dict)

    def __post_init__(self) -> None:
        # Validate that any attached labels are descriptive
        valid = set(ELIMINATION_LABEL_VALUES)
        for label in self.attached_elimination_labels:
            if label not in valid:
                raise ValueError(
                    f"Unknown elimination label: {label!r}. "
                    f"Must be one of {sorted(valid)}."
                )


def compute_rung_outcome(
    eval_result: RungEvaluation,
) -> tuple[RungOutcome, tuple[str, ...]]:
    """Determine RungOutcome from a RungEvaluation.

    Precedence per joint disposition (commit 019a964):

      1. INCONCLUSIVE preempts: if is_data_sufficient == False,
         return (INCONCLUSIVE, ()). The rung is excluded from K
         and reported separately.

      2. ELIMINATED next: if attached_elimination_labels is non-empty,
         return (ELIMINATED, attached_elimination_labels). All
         descriptive elimination labels attach to this rung.

      3. NOT_RULED_OUT otherwise: return
         (NOT_RULED_OUT, ("requires_further_investigation",)).
         The inherited v1 label string attaches as the singleton.

    boundary_proximity_flags do NOT affect this decision.
    """
    if not eval_result.is_data_sufficient:
        return (RungOutcome.INCONCLUSIVE, ())

    if eval_result.attached_elimination_labels:
        return (
            RungOutcome.ELIMINATED,
            tuple(eval_result.attached_elimination_labels),
        )

    return (RungOutcome.NOT_RULED_OUT, (NOT_RULED_OUT_LABEL,))


def compute_K(outcomes: list[tuple[str, RungOutcome]]) -> int:
    """K = count of rungs with NOT_RULED_OUT outcome.

    INCONCLUSIVE rungs are excluded from K.
    ELIMINATED rungs are excluded from K.
    boundary_proximity_flag has no effect on K.

    Per joint disposition: K = |{rung : outcome == NOT_RULED_OUT}|.
    """
    return sum(
        1 for _rung_id, outcome in outcomes
        if outcome == RungOutcome.NOT_RULED_OUT
    )


# ---------- fixed-language constants ----------
#
# These three constants are the ONLY outcome statements the
# lane emits. The outcome-chooser code emits exactly one of them.
# They are hashed into LOCK-RECORD via analysis_script_hash.
#
# Wording uses "not ruled out" / "not-ruled-out" per joint disposition
# (NS counter-proposal accepted; commit 019a964).

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
    "rungs are listed in rung-ID order: {rung_ids}. No rank fields "
    "or computations are emitted; the unordered not-ruled-out set "
    "carries no positive evidence weight."
)


def emit_outcome_statement(
    K: int,
    not_ruled_out_rung_ids: tuple[str, ...] = (),
) -> str:
    """Emit exactly one of the three fixed-language statements.

    K >= 0. If K == 0, the K=0 statement is returned (and
    not_ruled_out_rung_ids should be empty). If K == 1, the
    single-not-ruled-out statement is returned. If K >= 2, the
    multiple-not-ruled-out template is formatted with k and a
    rung-ID-ordered listing.

    The lane emits exactly ONE statement per sweep.
    """
    if K < 0:
        raise ValueError(f"K must be non-negative, got {K!r}.")
    if K == 0:
        return K_EQUALS_ZERO_STATEMENT
    if K == 1:
        return SINGLE_NOT_RULED_OUT_RUNG_STATEMENT
    # K >= 2
    ordered_rung_ids = ", ".join(sorted(not_ruled_out_rung_ids))
    return MULTIPLE_NOT_RULED_OUT_STATEMENT_TEMPLATE.format(
        k=K, rung_ids=ordered_rung_ids
    )
