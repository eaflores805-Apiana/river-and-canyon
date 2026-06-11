"""Lane 1a' Phase 4 lock_packet tests.

SYNTHETIC / DIAGNOSTIC -- NON-BINDING -- NOT FOR THRESHOLD DERIVATION
D2 IMPLEMENTATION ARTIFACT
NO MODEL INVOKED -- NO MODEL LOADED -- NO SWEEP EXECUTION

Validates:
  - IS-8 closure: PacketLockRefused fires for operation_equivalent
    policy in negative battery
  - IS-7 closure: A6 drift tolerance machinery
  - per-policy drift flags
  - envelope drift flags
"""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from lane1a_prime.lock_packet import (  # noqa: E402
    A6Result,
    DriftToleranceDeclaration,
    PacketLockRefused,
    PolicyClassification,
    a6_final_manifest_reverification,
    lock_packet,
)

LOCK_PACKET_SOURCE = (Path(__file__).resolve().parent.parent / "lane1a_prime" / "lock_packet.py").read_text()


# ---------- IS-8: operation-equivalence lock-time hard refusal ----------

def test_lock_packet_refuses_operation_equivalent_policy():
    """IS-8 closure: lock_packet raises PacketLockRefused when any
    negative-battery policy is classified operation_equivalent."""
    classifications = (
        PolicyClassification("pure_last_position", "discriminative"),
        PolicyClassification("salient_endpoint", "discriminative"),
        PolicyClassification("recency_excluding_target", "operation_equivalent"),
    )
    with pytest.raises(PacketLockRefused, match="recency_excluding_target"):
        lock_packet(classifications)


def test_lock_packet_proceeds_when_no_operation_equivalent():
    """When all negative-battery policies are discriminative (or
    degenerate_constant or structurally_undefined), lock_packet
    returns normally. Note: degenerate_constant and
    structurally_undefined would be flagged by other A4 checks,
    but lock_packet's specific IS-8 check is operation_equivalent."""
    classifications = (
        PolicyClassification("pure_last_position", "discriminative"),
        PolicyClassification("salient_endpoint", "discriminative"),
        PolicyClassification("recency_excluding_target", "discriminative"),
        PolicyClassification("prefix_neighbor_confusion", "discriminative"),
    )
    # Should not raise
    lock_packet(classifications)


def test_lock_packet_message_names_the_offending_policy():
    """The PacketLockRefused exception message names the offending
    policy to make the lock failure diagnosable."""
    classifications = (
        PolicyClassification("salient_endpoint", "operation_equivalent"),
    )
    with pytest.raises(PacketLockRefused) as exc_info:
        lock_packet(classifications)
    assert "salient_endpoint" in str(exc_info.value)


def test_lock_packet_refuses_on_first_operation_equivalent():
    """Multiple operation_equivalent classifications still raise.
    The first one encountered is named in the exception."""
    classifications = (
        PolicyClassification("policy_a", "operation_equivalent"),
        PolicyClassification("policy_b", "operation_equivalent"),
    )
    with pytest.raises(PacketLockRefused):
        lock_packet(classifications)


def test_lock_packet_accepts_empty_battery():
    """An empty negative battery has no operation_equivalent policy
    to refuse on. Other A4 checks (battery coverage minimum) would
    block lock separately."""
    lock_packet(())


# ---------- IS-7: A6 drift tolerance ----------

DEFAULT_TOLERANCE = DriftToleranceDeclaration()


def test_drift_tolerance_default_values_match_joint_disposition():
    """Joint disposition (NS materials v0.2 §2): per_policy = 0.05;
    envelope = 0.05."""
    assert DEFAULT_TOLERANCE.per_policy == 0.05
    assert DEFAULT_TOLERANCE.envelope == 0.05


def test_a6_drift_within_tolerance():
    """A6: per-policy drifts and envelope drift all within tolerance.
    No drift flag."""
    pilot_scores = {"p1": 0.20, "p2": 0.30}
    final_scores = {"p1": 0.22, "p2": 0.28}  # drift 0.02 each
    result = a6_final_manifest_reverification(
        pilot_battery_scores=pilot_scores,
        pilot_envelope=0.40,
        final_battery_scores=final_scores,
        final_envelope=0.42,  # envelope drift 0.02
        declared_drift_tolerance=DEFAULT_TOLERANCE,
    )
    assert result.drift_within_tolerance is True
    assert result.flagged_drifts == ()


def test_a6_drift_exceeds_per_policy_tolerance():
    """A6: per-policy drift > 0.05 -> flagged."""
    pilot_scores = {"p1": 0.20}
    final_scores = {"p1": 0.30}  # drift = 0.10
    result = a6_final_manifest_reverification(
        pilot_battery_scores=pilot_scores,
        pilot_envelope=0.40,
        final_battery_scores=final_scores,
        final_envelope=0.41,
        declared_drift_tolerance=DEFAULT_TOLERANCE,
    )
    assert result.drift_within_tolerance is False
    assert "p1" in result.flagged_drifts


def test_a6_drift_exceeds_envelope_tolerance():
    """A6: envelope drift > 0.05 -> envelope flagged."""
    pilot_scores = {"p1": 0.20}
    final_scores = {"p1": 0.22}  # within per-policy tolerance
    result = a6_final_manifest_reverification(
        pilot_battery_scores=pilot_scores,
        pilot_envelope=0.40,
        final_battery_scores=final_scores,
        final_envelope=0.55,  # envelope drift = 0.15
        declared_drift_tolerance=DEFAULT_TOLERANCE,
    )
    assert result.drift_within_tolerance is False
    assert "envelope" in result.flagged_drifts


def test_a6_rejects_mismatched_policy_sets():
    """A6: pilot and final must have identical policy sets."""
    pilot_scores = {"p1": 0.2, "p2": 0.3}
    final_scores = {"p1": 0.2, "p3": 0.3}  # p2 vs p3 mismatch
    with pytest.raises(ValueError, match="different policy"):
        a6_final_manifest_reverification(
            pilot_battery_scores=pilot_scores,
            pilot_envelope=0.4,
            final_battery_scores=final_scores,
            final_envelope=0.41,
            declared_drift_tolerance=DEFAULT_TOLERANCE,
        )


def test_a6_drift_per_policy_keyed_by_policy_name():
    pilot_scores = {"pure_last_position": 0.1, "salient_endpoint": 0.2}
    final_scores = {"pure_last_position": 0.12, "salient_endpoint": 0.19}
    result = a6_final_manifest_reverification(
        pilot_battery_scores=pilot_scores,
        pilot_envelope=0.3,
        final_battery_scores=final_scores,
        final_envelope=0.31,
        declared_drift_tolerance=DEFAULT_TOLERANCE,
    )
    assert "pure_last_position" in result.per_policy_drift
    assert "salient_endpoint" in result.per_policy_drift
    assert abs(result.per_policy_drift["pure_last_position"] - 0.02) < 1e-9
    assert abs(result.per_policy_drift["salient_endpoint"] - 0.01) < 1e-9


def test_a6_drift_envelope_is_absolute_difference():
    result = a6_final_manifest_reverification(
        pilot_battery_scores={"p1": 0.1},
        pilot_envelope=0.50,
        final_battery_scores={"p1": 0.1},
        final_envelope=0.55,
        declared_drift_tolerance=DEFAULT_TOLERANCE,
    )
    assert abs(result.envelope_drift - 0.05) < 1e-9


def test_a6_tolerance_boundary_at_exactly_tolerance():
    """Drift exactly equal to tolerance is NOT flagged (strict >).
    """
    pilot_scores = {"p1": 0.0}
    final_scores = {"p1": 0.05}  # drift = 0.05 = tolerance
    result = a6_final_manifest_reverification(
        pilot_battery_scores=pilot_scores,
        pilot_envelope=0.1,
        final_battery_scores=final_scores,
        final_envelope=0.1,
        declared_drift_tolerance=DEFAULT_TOLERANCE,
    )
    assert result.drift_within_tolerance is True


# ---------- PolicyClassification ----------

def test_policy_classification_accepts_valid_values():
    """Classification literal values per addendum A4."""
    valid = (
        "discriminative",
        "operation_equivalent",
        "degenerate_constant",
        "structurally_undefined",
    )
    for v in valid:
        c = PolicyClassification(policy_name="p", classification=v)
        assert c.classification == v


# ---------- source-level invariants ----------

def test_no_model_loading_imports_in_lock_packet_source():
    forbidden = [
        "import mlx_lm",
        "from mlx_lm",
        "from_pretrained",
        "torch.load",
        "load_model",
    ]
    for f in forbidden:
        assert f not in LOCK_PACKET_SOURCE


def test_no_fails_token_in_lock_packet_source():
    assert "fails" not in LOCK_PACKET_SOURCE.lower()


def test_no_sealed_state_write_in_lock_packet_source():
    """Phase 4 D2 boundary: lock_packet.py does not write a SEALED
    state. The SEALED-state write path lives outside this module
    and is not authorized under D2."""
    # Source-level grep: no string literal "SEALED" written as a
    # value assignment.
    import re
    pattern = re.compile(
        r"['\"]SEALED['\"]\s*$",
        re.MULTILINE,
    )
    matches = pattern.findall(LOCK_PACKET_SOURCE)
    assert matches == [], (
        f"Found SEALED state write in lock_packet.py: {matches}"
    )
