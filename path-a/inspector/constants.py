#!/usr/bin/env python3
"""
constants.py — Manager-approved Path A values (locked).

Per TL ACTION 2026-06-15 ("Build Path A Inspector + G6 v0.3"), Manager approved
the core Path A values:

    k = 5            chain-level decoys
    D = 5            same-depth competitors at the head
    p = 5            C* prompt-position slots (layout diagnostic)
    m_min = 10       minimum equal-salience candidates (token-pick floor)
    n = 96           items per cell (powered against F)
    margin = 0.25    pre-declared margin above the heuristic floor

Derived floor (per construct definition v0.3 §8):
    F = max(1/p, 1/m, 1/D) = max(0.20, 0.10, 0.20) = 0.20
    success threshold = F + margin = 0.45

Per TL: if implementation uses m > 10, log actual; floor remains dominated by
1/p and 1/D unless m < 5, which is not allowed.

These values are LOCKED here — the inspector and the G6 v0.3 evaluator read them
from this module, not from inline constants. Changing the Manager-approved set
requires a new TL ACTION + Manager authorization.
"""
from __future__ import annotations


# ── Manager-approved values (locked) ────────────────────────────────────────
K_DECOY_CHAINS                    = 5
D_DEPTH_COMPETITORS               = 5
P_POSITION_SLOTS                  = 5
M_MIN_EQUAL_SALIENCE_CANDIDATES   = 10
M_MIN_FLOOR                       = 5      # m < 5 is not allowed
N_ITEMS_PER_CELL                  = 96
MARGIN                            = 0.25


# ── Derived ──────────────────────────────────────────────────────────────────
def heuristic_floor(p: int = P_POSITION_SLOTS,
                    m: int = M_MIN_EQUAL_SALIENCE_CANDIDATES,
                    D: int = D_DEPTH_COMPETITORS) -> float:
    """F = max(1/p, 1/m, 1/D). All inputs must be ≥ 1; m must be ≥ M_MIN_FLOOR."""
    if m < M_MIN_FLOOR:
        raise ValueError(
            f"m = {m} < M_MIN_FLOOR ({M_MIN_FLOOR}); not allowed per TL ACTION."
        )
    if p < 1 or D < 1:
        raise ValueError(f"p and D must be ≥ 1; got p={p}, D={D}")
    return max(1.0 / p, 1.0 / m, 1.0 / D)


def success_threshold(p: int = P_POSITION_SLOTS,
                      m: int = M_MIN_EQUAL_SALIENCE_CANDIDATES,
                      D: int = D_DEPTH_COMPETITORS,
                      margin: float = MARGIN) -> float:
    """Success threshold = F + margin (derived; not freely declared)."""
    return heuristic_floor(p, m, D) + margin


# ── Public summary (for manifest emission) ──────────────────────────────────
def values_summary() -> dict:
    """Single dict summarizing the locked Manager-approved values + derived F + threshold."""
    return {
        "manager_approved": {
            "k": K_DECOY_CHAINS,
            "D": D_DEPTH_COMPETITORS,
            "p": P_POSITION_SLOTS,
            "m_min": M_MIN_EQUAL_SALIENCE_CANDIDATES,
            "n": N_ITEMS_PER_CELL,
            "margin": MARGIN,
        },
        "derived": {
            "F": heuristic_floor(),
            "success_threshold": success_threshold(),
            "F_formula": "max(1/p, 1/m, 1/D)",
            "threshold_formula": "F + margin",
        },
        "policy_notes": {
            "m_floor": f"m < {M_MIN_FLOOR} not allowed; m > 10 acceptable (log actual; floor unchanged unless m < {M_MIN_FLOOR})",
            "authority": "TL ACTION 2026-06-15 + Manager approval",
        },
    }
