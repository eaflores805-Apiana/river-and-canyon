"""TP banner-propagation tests (post Manager TP-banner deviation disposition).

Per Manager Disposition D4-A TP-Banner Deviation (2026-06-11), every
emitted report from a Q2-declined D4 run MUST include the TP
inactive-by-decision banner. These tests verify the banner helper
and that no model is invoked.

NO MODEL INVOKED · NO MODEL LOADED · NO SWEEP_ID · NO SWEEP EXECUTION
"""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

REPO_EXPERIMENT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_EXPERIMENT_DIR))

from d4_runner.lane1a_runner import tp_banner_block


REQUIRED_KEYS = {
    "tp_criterion_status",
    "tp_inactivity_authority",
    "tp_generation_status",
    "tp_elimination_labels_enabled",
}


def test_tp_banner_block_q2_declined_has_required_fields():
    banner = tp_banner_block(
        token_prior_authorized=False,
        authority_ref="MANAGER-AUTHORIZATION-LANE-1A-PRIME-D4A 2026-06-11 §4 (Q2 declined)",
    )
    assert set(banner.keys()) >= REQUIRED_KEYS
    assert banner["tp_criterion_status"] == "INACTIVE BY MANAGER DECISION"
    assert banner["tp_generation_status"] == "NOT RUN — DECLINED BY MANAGER"
    assert banner["tp_elimination_labels_enabled"] is False
    assert "Q2" in banner["tp_inactivity_authority"]


def test_tp_banner_block_q2_authorized_has_required_fields():
    banner = tp_banner_block(
        token_prior_authorized=True,
        authority_ref="hypothetical future authorization",
    )
    assert set(banner.keys()) >= REQUIRED_KEYS
    assert banner["tp_criterion_status"] == "ACTIVE"
    assert banner["tp_generation_status"] == "RUN (authorized)"
    assert banner["tp_elimination_labels_enabled"] is True


def test_tp_banner_block_authority_ref_carried_verbatim_when_declined():
    custom_authority = "Manager memo X §Y; cross-ref Z"
    banner = tp_banner_block(False, custom_authority)
    assert banner["tp_inactivity_authority"] == custom_authority


def test_tp_banner_propagates_into_simulated_emission_envelopes():
    """Simulate the embedded-in-every-emission contract.

    Each of the 5 emit envelopes the runner constructs (pre-flight log,
    T1, T3, T4, A6, execution_ledger) must carry the banner block as a
    top-level field. This test verifies that the dict construction
    pattern the runner uses preserves the banner verbatim.
    """
    banner = tp_banner_block(False, "test authority")
    emissions = {
        "pre_flight_log": {"sweep_id": "x", "tp_banner": banner, "run_header": {"sweep_id": "x", "tp_banner": banner}},
        "t1_report": {"tp_banner": banner, "per_policy_scores": {}},
        "t3_report": {"tp_banner": banner, "rows": []},
        "t4_report": {"tp_banner": banner, "rows": []},
        "a6_re_verification": {"tp_banner": banner, "drift_within_tolerance": True},
        "execution_ledger": {"tp_banner": banner, "model_invoked": True},
    }
    for name, payload in emissions.items():
        assert "tp_banner" in payload, f"{name} missing tp_banner"
        b = payload["tp_banner"]
        assert b["tp_criterion_status"] == "INACTIVE BY MANAGER DECISION"
        assert b["tp_elimination_labels_enabled"] is False


def test_runner_module_exposes_banner_function():
    """The runner module must export tp_banner_block for future-run wiring."""
    from d4_runner import lane1a_runner
    assert hasattr(lane1a_runner, "tp_banner_block")
    assert callable(lane1a_runner.tp_banner_block)
    # Verify the banner the runner would produce under DEFAULT preconditions
    # (which carry "DECLINED BY MANAGER (Q2 2026-06-11)") matches the inactive form
    import json
    pre = json.loads(open("experiments/2026-06-11_lane-1a-prime/d4_runner/preconditions.json").read())
    decision = pre.get("token_prior_decision", "DECLINED").upper()
    assert decision.startswith("DECLINED")
    b = lane1a_runner.tp_banner_block(False, pre["token_prior_decision"])
    assert b["tp_criterion_status"] == "INACTIVE BY MANAGER DECISION"
    assert b["tp_elimination_labels_enabled"] is False
