"""Lane 1a' lock-packet machinery.

SYNTHETIC / DIAGNOSTIC -- NON-BINDING -- NOT FOR THRESHOLD DERIVATION
D2 IMPLEMENTATION ARTIFACT (PHASE 4)
NO MODEL INVOKED -- NO MODEL LOADED
NO SWEEP_ID CREATED -- NO SWEEP EXECUTION AUTHORIZED
NO LOCK-RECORD SEALED STATE PERMITTED UNDER D2

Phase 4 implements:

  IS-8 closure: operation-equivalence lock-time hard refusal.
    lock_packet() structurally refuses to proceed if any
    negative-battery policy is classified operation_equivalent.

  IS-7 closure: A6 final-manifest re-verification with
    pre-declared drift tolerance.
    a6_final_manifest_reverification() compares per-policy and
    union-envelope scores between pilot and final manifests against
    the declared tolerance; exceedance sets drift_flag.

Under D2 the lock_packet() function exists but cannot produce a
SEALED LOCK-RECORD: the function is structurally permitted to
RAISE (PacketLockRefused) but the path that writes the SEALED
LOCK-RECORD lives outside this module (Phase 5 or post-D2).
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal, Optional


# Policy classification values per addendum A4.
PolicyClassificationLiteral = Literal[
    "discriminative",
    "operation_equivalent",
    "degenerate_constant",
    "structurally_undefined",
]


class PacketLockRefused(Exception):
    """Raised by lock_packet() when the structural lock-time check
    refuses to proceed.

    Per IS-8 (commit 019a964 joint disposition): "Operation-
    equivalence consequence: a negative dummy that becomes operation-
    equivalent on pilot or final manifests is removed or reclassified
    as a positive oracle before lock; it may not remain in the union
    envelope. CS implements this as a lock-time hard refusal at code
    level."

    A battery containing an operation-equivalent policy cannot seal.
    """
    pass


@dataclass(frozen=True)
class PolicyClassification:
    """Classification of a policy per addendum A4.

    discriminative:        contributes to declared battery-coverage minima
    operation_equivalent:  reaches the declared cap; not a valid detector
    degenerate_constant:   constant output regardless of input
    structurally_undefined: undefined on the construction
    """
    policy_name: str
    classification: PolicyClassificationLiteral


def lock_packet(
    negative_battery_classifications: tuple[PolicyClassification, ...],
) -> None:
    """IS-8: Hard refusal for operation-equivalent policies.

    INVARIANT: structurally refuses to proceed if any negative-battery
    policy is classified operation_equivalent. Removal or
    reclassification (to a positive oracle) is required before lock.

    Per joint disposition, this is a CODE-LEVEL hard refusal, not a
    reviewer attestation. The refusal point fires between A4
    classification and packet seal; LOCK-RECORD cannot reach SEALED
    if this raises.

    Under D2 Phase 4, the function exists but cannot transition any
    LOCK-RECORD to SEALED (the SEALED-state write path lives outside
    this module and is not authorized under D2).
    """
    for c in negative_battery_classifications:
        if c.classification == "operation_equivalent":
            raise PacketLockRefused(
                f"Operation-equivalent policy {c.policy_name!r} in "
                f"negative battery; removal or reclassification as a "
                f"positive oracle required before lock. Lock cannot "
                f"proceed."
            )
    # If we reach here, the IS-8 check passes. (Other lock-time
    # checks — G1-open count == 0; recompute-and-verify hashes;
    # token_prior_authorization resolved by name — are handled
    # elsewhere and not bundled into this function.)


@dataclass(frozen=True)
class DriftToleranceDeclaration:
    """IS-7: pre-declared drift tolerance per anti-tuning rule.

    Per joint disposition (NS materials v0.2 §2), the declared
    values are:
      per_policy: 0.05  (|pilot - final| per policy)
      envelope:   0.05  (|pilot - final| for union envelope)

    Both are [SWEEP-PARAMETER -- NOT A THRESHOLD VALUE]. Adjustable
    at packet review BEFORE pilot; post-pilot change is a must-fix
    event requiring C1 disposition.
    """
    per_policy: float = 0.05
    envelope: float = 0.05


@dataclass(frozen=True)
class A6Result:
    """Result of A6 final-manifest re-verification.

    drift_within_tolerance is True iff all per-policy drifts AND
    envelope drift are within the declared tolerance.
    Otherwise the result.flagged_drifts lists the policies (and
    "envelope") that exceeded tolerance; the rung is marked
    INCONCLUSIVE upstream (lock-blocking; see joint disposition).
    """
    per_policy_drift: dict[str, float]
    envelope_drift: float
    drift_within_tolerance: bool
    flagged_drifts: tuple[str, ...]


def a6_final_manifest_reverification(
    pilot_battery_scores: dict[str, float],
    pilot_envelope: float,
    final_battery_scores: dict[str, float],
    final_envelope: float,
    declared_drift_tolerance: DriftToleranceDeclaration,
) -> A6Result:
    """A6 closure: per-policy and union-envelope re-verification on
    final locked manifests.

    Computes:
      drift_per_policy = |final - pilot| per policy
      drift_envelope   = |final_envelope - pilot_envelope|

    Compares each drift against declared_drift_tolerance (per IS-7,
    declared pre-pilot per anti-tuning rule).

    Returns A6Result with:
      per_policy_drift: dict
      envelope_drift: float
      drift_within_tolerance: bool
      flagged_drifts: tuple[str, ...] (any drift exceeding tolerance)
    """
    if pilot_battery_scores.keys() != final_battery_scores.keys():
        raise ValueError(
            f"Pilot and final battery scores have different policy "
            f"sets: {sorted(pilot_battery_scores)} vs "
            f"{sorted(final_battery_scores)}"
        )

    per_policy_drift = {
        name: abs(final_battery_scores[name] - pilot_battery_scores[name])
        for name in pilot_battery_scores
    }
    envelope_drift = abs(final_envelope - pilot_envelope)

    flagged: list[str] = []
    for name, drift in per_policy_drift.items():
        if drift > declared_drift_tolerance.per_policy:
            flagged.append(name)
    if envelope_drift > declared_drift_tolerance.envelope:
        flagged.append("envelope")

    return A6Result(
        per_policy_drift=per_policy_drift,
        envelope_drift=envelope_drift,
        drift_within_tolerance=(len(flagged) == 0),
        flagged_drifts=tuple(flagged),
    )
