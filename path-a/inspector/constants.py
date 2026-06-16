#!/usr/bin/env python3
"""
constants.py — Manager-approved Path A values + scorer constants (shared lock).

Per TL ACTION 2026-06-15 ("Build Path A Inspector + G6 v0.3") + the value-lock
patch ACTION, Manager approved the core Path A values:

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

THIS MODULE IS THE SINGLE LOCK. Both the inspector and the G6 v0.3 evaluator
import these values and validate spec params against them. Changing the
Manager-approved set requires a new TL ACTION + Manager authorization.

Operational modes (per the value-lock patch + sweep patch):
  REAL-RUN MODE  (default; spec lacks `_fixture_mode` and `_sweep_mode`)
    All threshold-determining params (p, D, m, margin, k) MUST be declared in the
    spec AND MUST match this lock (m may exceed M_MIN_EQUAL_SALIENCE_CANDIDATES
    but must be ≥ M_MIN_FLOOR). Deviation or absence → fail-closed REJECT.
  FIXTURE MODE  (spec sets `_fixture_mode: true`)
    Fixtures may vary params for testing purposes. The flag explicitly excludes
    the construction from real-run admissibility — pre-registration must not
    consume a spec with `_fixture_mode: true`.
  SWEEP MODE  (spec sets `_sweep_mode: true` AND `_sweep_locked_K_list: [..]`)
    K varies across cells, but p, D, m, margin still bind to the Manager lock.
    K must be one of the values in `_sweep_locked_K_list`; the list itself is
    the locked object recorded as under test. Authority: TL ACTION 2026-06-16
    ("Path A Load Scout K=1..5"). Sweep mode does not lift any other Manager-
    lock binding; it loosens ONLY the K-equality clause and only against a
    pre-declared K-list.

Dominance threshold (DOMINANT_RATE_THRESHOLD):
  The scorer constant that decides when a per-category rate is "dominant" in
  the §11 failure-signature sense. Recorded here so the inspector and the
  evaluator share the same value. PROVENANCE FLAG: this value (0.25) is
  currently a scorer-code constant; it is NOT recorded in
  `TARGET-CONSTRUCT-DEFINITION-v0.3` or any pre-registration. Senior-flagged
  for promotion to the definition / pre-registration before real-run use; see
  `DOMINANT_RATE_THRESHOLD_PROVENANCE` below.
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


# ── Scorer constants (shared between inspector and evaluator) ───────────────
DOMINANT_RATE_THRESHOLD = 0.25

DOMINANT_RATE_THRESHOLD_PROVENANCE = {
    "value":            DOMINANT_RATE_THRESHOLD,
    "source":           "TARGET-CONSTRUCT-DEFINITION-v0.4 §11 + checklist #7 (of-record)",
    "status":           "PROMOTED",
    "promoted_to":      "TARGET-CONSTRUCT-DEFINITION-v0.4",
    "promoted_to_sha256": "4b616afb919114ee6e0b524e030172cc6f9a96ea8e206fc65bcbd0571eb23c29",
    "promoted_to_path": "path-a/of-record/TARGET-CONSTRUCT-DEFINITION-v0.4.md",
    "promotion_authority": "TL ACTION 2026-06-15 + Manager approval (Elevate v0.4 and Lock Prereg v0.3)",
    "definition_text":  "A failure category is 'dominant' when its rate is >= 0.25 over the pre-declared analysis unit (definition v0.4 §11).",
    "rationale": (
        "Closes the v0.3-prior scorer-code-only provenance gap CS raised in the "
        "value-lock-patch review. The 0.25 threshold is now declared with the "
        "failure signatures it governs (definition R11), qualified by a "
        "pre-declared analysis unit (R11), not buried in scorer code. The "
        "scorer code still imports this constant from here for shared use; the "
        "code is the implementation, the definition is the source of truth."
    ),
}


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


# ── Manager-lock validation (shared between inspector and evaluator) ────────
def is_fixture_mode(spec: dict) -> bool:
    """True iff the spec explicitly sets `_fixture_mode: true`. Fixtures so
    marked are excluded from real-run admissibility by definition."""
    return bool(spec.get("_fixture_mode") is True)


def is_sweep_mode(spec: dict) -> bool:
    """True iff the spec explicitly sets `_sweep_mode: true` and declares
    `_sweep_locked_K_list: [..]`. Sweep mode allows K to vary across cells
    while binding p, m, margin to the Manager lock (and D to the Manager lock,
    since D is NOT a sweep dimension on Path A). The locked K-list itself is
    the object recorded as locked; any K outside the list deviates.

    Authority: TL ACTION 2026-06-16 ("Team Lead Sign-Off — Path A Load Scout
    K=1..5"). The K-sweep prereg's §2 'CONSTANTS' clause asks for this fast-path
    patch. Sweep mode does not lift any other Manager-lock binding."""
    return (bool(spec.get("_sweep_mode") is True)
            and isinstance(spec.get("_sweep_locked_K_list"), list))


def validate_manager_lock(spec: dict) -> dict:
    """Validate the threshold-determining params against the Manager lock.

    Returns:
      {
        "ok":           bool,
        "mode":         "real-run" | "fixture" | "sweep",
        "deviations":   list[str],   # empty if ok
        "missing":      list[str],   # empty if ok
      }

    Fixture-mode specs always return ok=True with mode="fixture" (the flag
    explicitly excludes them from real-run admissibility, so the binding
    does not apply). Sweep-mode specs bind p/D/m/margin to the Manager lock
    AND bind K to the declared `_sweep_locked_K_list` (one-of), preserving
    the locked K-list as the object under test. Real-run specs (neither
    fixture nor sweep) must have p == P_POSITION_SLOTS, D == D_DEPTH_
    COMPETITORS, m >= M_MIN_EQUAL_SALIENCE_CANDIDATES (with m >= M_MIN_FLOOR
    floor), and margin == MARGIN. Missing params are treated as fail-closed
    REJECT (no silent fallback in real-run or sweep modes).
    """
    if is_fixture_mode(spec):
        return {"ok": True, "mode": "fixture", "deviations": [], "missing": []}

    sweep = is_sweep_mode(spec)
    params = spec.get("params") or {}
    missing = []
    deviations = []

    if "p" not in params:
        missing.append("params.p")
    elif params["p"] != P_POSITION_SLOTS:
        deviations.append(f"params.p = {params['p']} != Manager-locked P_POSITION_SLOTS = {P_POSITION_SLOTS}")

    if "D" not in params:
        missing.append("params.D")
    elif params["D"] != D_DEPTH_COMPETITORS:
        deviations.append(f"params.D = {params['D']} != Manager-locked D_DEPTH_COMPETITORS = {D_DEPTH_COMPETITORS}")

    if "m" not in params:
        missing.append("params.m")
    else:
        m = params["m"]
        if m < M_MIN_FLOOR:
            deviations.append(f"params.m = {m} < M_MIN_FLOOR ({M_MIN_FLOOR}); not allowed")
        elif m < M_MIN_EQUAL_SALIENCE_CANDIDATES:
            deviations.append(f"params.m = {m} < Manager-locked M_MIN_EQUAL_SALIENCE_CANDIDATES = {M_MIN_EQUAL_SALIENCE_CANDIDATES}")
        # m > M_MIN is allowed (logged elsewhere)

    if "margin" not in params:
        missing.append("params.margin")
    elif params["margin"] != MARGIN:
        deviations.append(f"params.margin = {params['margin']} != Manager-locked MARGIN = {MARGIN}")

    # Sweep mode: bind K to the locked K-list rather than the single K value.
    # Standard real-run mode: bind K to the single Manager-locked K value.
    if sweep:
        locked_K_list = spec["_sweep_locked_K_list"]
        if "k" not in params:
            missing.append("params.k")
        elif params["k"] not in locked_K_list:
            deviations.append(
                f"params.k = {params['k']} not in declared _sweep_locked_K_list "
                f"{locked_K_list} (sweep mode binds K to the locked list, not to the "
                f"Manager-single K = {K_DECOY_CHAINS})"
            )
        mode = "sweep"
    else:
        if "k" in params and params["k"] != K_DECOY_CHAINS:
            deviations.append(
                f"params.k = {params['k']} != Manager-locked K_DECOY_CHAINS = {K_DECOY_CHAINS} "
                f"(real-run mode; set `_sweep_mode: true` + `_sweep_locked_K_list: [...]` to vary K)"
            )
        mode = "real-run"

    ok = not (missing or deviations)
    return {"ok": ok, "mode": mode, "deviations": deviations, "missing": missing}


# ── Public summary (for manifest emission) ──────────────────────────────────
def values_summary() -> dict:
    """Single dict summarizing the locked Manager-approved values + derived F +
    threshold + scorer constants + provenance flags."""
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
        "scorer_constants": {
            "DOMINANT_RATE_THRESHOLD": DOMINANT_RATE_THRESHOLD,
        },
        "policy_notes": {
            "m_floor":      f"m < {M_MIN_FLOOR} not allowed; m > 10 acceptable (log actual; floor unchanged unless m < {M_MIN_FLOOR})",
            "authority":    "TL ACTION 2026-06-15 + Manager approval + value-lock patch ACTION + TL ACTION 2026-06-16 (sweep mode for Path A Load Scout K=1..5)",
            "fixture_mode": "spec.`_fixture_mode: true` excludes a construction from real-run admissibility; allows param variation for testing",
            "real_run_mode": "real-run specs must declare p, D, m, margin, k and match the Manager lock; missing or deviating params -> fail-closed REJECT (no silent fallback)",
            "sweep_mode":   "spec.`_sweep_mode: true` + `_sweep_locked_K_list: [..]` allows K to vary across the declared list; p/D/m/margin still bind to the Manager lock; K outside the list -> fail-closed REJECT",
        },
        "provenance_flags": {
            "DOMINANT_RATE_THRESHOLD": DOMINANT_RATE_THRESHOLD_PROVENANCE,
        },
    }
