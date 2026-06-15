#!/usr/bin/env python3
"""
build_path_a_fixtures.py — Generate the 6 contrast fixtures for Path A v0.3.

Produces synthetic but rule-consistent inputs for inspector + G6 v0.3 evaluator
testing. NOT a task-item generator. NOT prompts. NOT a model run. Pure static
data designed so the evaluator emits each of the pre-declared outcomes given
the corresponding fixture.

Authority: TL ACTION 2026-06-15 ("Build Path A Inspector + G6 v0.3").
"""
from __future__ import annotations

import json
from pathlib import Path


N_ITEMS = 8   # small per-fixture sample; not the Manager-approved n=96 (real runs use that)
QUERIES = ["composite", "hop1", "hop2", "direct_query"]


def build_valid_spec(construction_id: str) -> dict:
    """Build a construction spec that passes ALL inspector checks. Used as the
    base for fixtures 1-5; fixture 6 mutates it to force a rejection.

    All fixtures carry `_fixture_mode: true` per the value-lock patch — they are
    explicitly excluded from real-run admissibility. A real-run preregistration
    must use a spec without this flag, and the inspector + evaluator will then
    enforce the Manager lock."""
    return {
        "_fixture_mode":   True,
        "construction_id": construction_id,
        "params": {"k": 5, "D": 5, "p": 5, "m": 10, "margin": 0.25},
        "target": {
            "A": "tokA", "B": "tokB", "C_star": "tokCstar", "T": "tokT",
            "r1": "r1", "r2": "r2",
            "post_C_star_relations": ["rX", "rY"],
        },
        "depth_2_competitors": [
            {"head_relation": "s1", "B_competitor": "tokB2", "second_relation": "s2", "X": "tokX2"},
            {"head_relation": "t1", "B_competitor": "tokB3", "second_relation": "t2", "X": "tokX3"},
            {"head_relation": "u1", "B_competitor": "tokB4", "second_relation": "u2", "X": "tokX4"},
            {"head_relation": "v1", "B_competitor": "tokB5", "second_relation": "v2", "X": "tokX5"},
            {"head_relation": "w1", "B_competitor": "tokB6", "second_relation": "w2", "X": "tokX6"},
        ],
        "decoy_chains": [
            {"head": "P1", "bridge": "Q1", "answer": "S1", "T_i": "tokTi1"},
            {"head": "P2", "bridge": "Q2", "answer": "S2", "T_i": "tokTi2"},
            {"head": "P3", "bridge": "Q3", "answer": "S3", "T_i": "tokTi3"},
            {"head": "P4", "bridge": "Q4", "answer": "S4", "T_i": "tokTi4"},
            {"head": "P5", "bridge": "Q5", "answer": "S5", "T_i": "tokTi5"},
        ],
        "relation_balance": {
            "frequency": {
                "r1": 1, "r2": 1,
                "s1": 1, "s2": 1, "t1": 1, "t2": 1,
                "u1": 1, "u2": 1, "v1": 1, "v2": 1,
                "w1": 1, "w2": 1,
            },
            "order_positions": {
                "r1": [0], "s1": [0], "t1": [0], "u1": [0], "v1": [0], "w1": [0],
                "r2": [1], "s2": [1], "t2": [1], "u2": [1], "v2": [1], "w2": [1],
            },
        },
        "direct_query": {
            "withhold_fact_role": "B_to_C_star",
            "filler_form": "{W} holds {V}",
            "filler_contains_B_or_C_star": False,
        },
        "contexts": {
            "composite":     {"present_facts": "full"},
            "hop1":          {"context_isolated_from_composite": True},
            "hop2":          {"context_isolated_from_composite": True},
            "direct_query":  {"context_isolated_from_composite": True},
            "load_matched":  True,
        },
    }


def make_result(item_id: str, query_type: str, expected: str, raw: str) -> dict:
    return {
        "item_id":    item_id,
        "query_type": query_type,
        "expected":   expected,
        "raw_output": raw,
    }


# ── Fixture 1: clean-certify-like ──────────────────────────────────────────
def fixture_01_clean_certify() -> tuple[dict, dict, dict]:
    spec = build_valid_spec("path_a_fixture_01_clean_certify_v0.1")
    results = []
    for i in range(N_ITEMS):
        item = f"item_{i+1:02d}"
        # Composite returns C* (correct composition); controls all pass; direct-query returns NULL.
        results.append(make_result(item, "composite",    "tokCstar", "ANSWER: tokCstar"))
        results.append(make_result(item, "hop1",         "tokB",     "ANSWER: tokB"))
        results.append(make_result(item, "hop2",         "tokCstar", "ANSWER: tokCstar"))
        results.append(make_result(item, "direct_query", "NULL",     "ANSWER: NULL"))
    expected = {
        "_purpose": "Pre-declared expected outcome. Designed so the evaluator emits CERTIFY: all composite items return C*, controls pass, direct-query abstains, no constant-token across queries.",
        "outcome": "CERTIFY",
        "_expected_R1_rate": 1.0,
    }
    return spec, {"results": results}, expected


# ── Fixture 2: terminal-grab failure ───────────────────────────────────────
def fixture_02_terminal_grab() -> tuple[dict, dict, dict]:
    spec = build_valid_spec("path_a_fixture_02_terminal_grab_v0.1")
    results = []
    for i in range(N_ITEMS):
        item = f"item_{i+1:02d}"
        # Composite returns T (target terminal). hop1/hop2 still pass; direct-query NULL.
        results.append(make_result(item, "composite",    "tokCstar", "ANSWER: tokT"))
        results.append(make_result(item, "hop1",         "tokB",     "ANSWER: tokB"))
        results.append(make_result(item, "hop2",         "tokCstar", "ANSWER: tokCstar"))
        results.append(make_result(item, "direct_query", "NULL",     "ANSWER: NULL"))
    expected = {
        "_purpose": "Pre-declared expected outcome. Designed so the evaluator emits FAIL with R2 dominant: composite returns target terminal token for every item.",
        "outcome": "FAIL",
        "_expected_dominant_signature": "R2_dominant_target_terminal_attraction",
    }
    return spec, {"results": results}, expected


# ── Fixture 3: depth-competitor / R4b failure ──────────────────────────────
def fixture_03_depth_competitor() -> tuple[dict, dict, dict]:
    spec = build_valid_spec("path_a_fixture_03_depth_competitor_v0.1")
    results = []
    for i in range(N_ITEMS):
        item = f"item_{i+1:02d}"
        # Composite returns one of the X_i tokens (depth-2 competitor). Rotate
        # across X2..X6 so the signature is purely R4b, not just one specific X.
        x_choices = ["tokX2", "tokX3", "tokX4", "tokX5", "tokX6"]
        x_picked = x_choices[i % len(x_choices)]
        results.append(make_result(item, "composite",    "tokCstar", f"ANSWER: {x_picked}"))
        results.append(make_result(item, "hop1",         "tokB",     "ANSWER: tokB"))
        results.append(make_result(item, "hop2",         "tokCstar", "ANSWER: tokCstar"))
        results.append(make_result(item, "direct_query", "NULL",     "ANSWER: NULL"))
    expected = {
        "_purpose": "Pre-declared expected outcome. Designed so the evaluator emits FAIL with R4b dominant: composite returns a depth-2 competitor token for every item, rotating across X2..X6.",
        "outcome": "FAIL",
        "_expected_dominant_signature": "R4b_dominant_depth_selection",
    }
    return spec, {"results": results}, expected


# ── Fixture 4: direct-query shortcut ───────────────────────────────────────
def fixture_04_direct_query_shortcut() -> tuple[dict, dict, dict]:
    spec = build_valid_spec("path_a_fixture_04_direct_query_shortcut_v0.1")
    results = []
    for i in range(N_ITEMS):
        item = f"item_{i+1:02d}"
        # Composite returns C* (looks correct) BUT direct-query ALSO returns C*,
        # so R6c invalidates R1 on every item. controls pass.
        results.append(make_result(item, "composite",    "tokCstar", "ANSWER: tokCstar"))
        results.append(make_result(item, "hop1",         "tokB",     "ANSWER: tokB"))
        results.append(make_result(item, "hop2",         "tokCstar", "ANSWER: tokCstar"))
        results.append(make_result(item, "direct_query", "NULL",     "ANSWER: tokCstar"))   # !!
    expected = {
        "_purpose": "Pre-declared expected outcome. Composite looks correct but every item's direct-query control returns C* → R6c invalidates R1 on every item → net R1 = 0 → FAIL (R1 below floor; no positive failure-signature dominance because composite still shows raw R1-category by token).",
        "outcome": "FAIL",
        "_expected_invalidator": "R6c_direct_query_shortcut",
    }
    return spec, {"results": results}, expected


# ── Fixture 5: constant-token failure ──────────────────────────────────────
def fixture_05_constant_token() -> tuple[dict, dict, dict]:
    spec = build_valid_spec("path_a_fixture_05_constant_token_v0.1")
    results = []
    for i in range(N_ITEMS):
        item = f"item_{i+1:02d}"
        # Model emits the SAME TOKEN across all 4 queries — the i06 signature.
        # Token happens to == C*, so composite looks correct, BUT R6e invalidates.
        results.append(make_result(item, "composite",    "tokCstar", "ANSWER: tokCstar"))
        results.append(make_result(item, "hop1",         "tokB",     "ANSWER: tokCstar"))
        results.append(make_result(item, "hop2",         "tokCstar", "ANSWER: tokCstar"))
        results.append(make_result(item, "direct_query", "NULL",     "ANSWER: tokCstar"))
    expected = {
        "_purpose": "Pre-declared expected outcome. Model emits the SAME token (C*) across all 4 queries per item — the i06 flat-heuristic signature. R6e invalidates R1 on every item AND cross_query_constant_token signature is dominant → FAIL.",
        "outcome": "FAIL",
        "_expected_dominant_signature": "cross_query_constant_token_prevalent",
    }
    return spec, {"results": results}, expected


# ── Fixture 6: rejected-construction (admissibility breach) ────────────────
def fixture_06_rejected_construction() -> tuple[dict, dict, dict]:
    """C* token aliased to the target terminal T → R8.1 breach at admissibility."""
    spec = build_valid_spec("path_a_fixture_06_rejected_construction_v0.1")
    # Force C* == T (R8.1 breach).
    spec["target"]["T"] = spec["target"]["C_star"]
    expected = {
        "_purpose": "Pre-declared expected outcome. C* is aliased to the target terminal T → C1 check (C* is any terminal) fires + C2 (pairwise distinct) fires → inspector REJECTs the construction before any item is written.",
        "disposition": "REJECT",
        "_expected_breached_checks": ["C1_C_star_not_terminal", "C2_pairwise_distinct"],
    }
    # No raw outputs needed; the construction never runs.
    return spec, None, expected


# ── Fixture 7: real-run lock-violation (Manager-lock binding fires) ────────
def fixture_07_lock_violation() -> tuple[dict, dict, dict]:
    """A spec WITHOUT `_fixture_mode: true` whose `params.margin` deviates from
    the Manager lock → C9 inspector check REJECTS at admissibility, AND the
    evaluator's compute_floor returns LOCK_VIOLATION rather than computing F."""
    spec = build_valid_spec("path_a_fixture_07_lock_violation_v0.1")
    # Remove the fixture-mode flag → real-run mode.
    del spec["_fixture_mode"]
    # Deviate margin from the Manager lock (0.25 → 0.10).
    spec["params"]["margin"] = 0.10
    expected = {
        "_purpose": "Spec is in real-run mode (no `_fixture_mode` flag) but margin = 0.10 ≠ Manager-locked 0.25. Inspector C9 fires → REJECT. If the evaluator is also run against this spec (with any minimal synthetic raw_outputs), compute_floor returns lock_violation = true and the outcome is LOCK_VIOLATION before any composite-correct count is interpreted.",
        "disposition":                "REJECT",     # inspector
        "outcome":                    "LOCK_VIOLATION",  # evaluator
        "_expected_breached_checks": ["C9_manager_lock_binding"],
    }
    # No raw outputs needed for the inspector; the lock fires before evaluation.
    # An evaluator probe (with a minimal synthetic fp16_raw_outputs.json) confirms
    # LOCK_VIOLATION; the probe file is NOT included in the fixture by default to
    # avoid suggesting this fixture has model data.
    return spec, None, expected


# ── Driver ──────────────────────────────────────────────────────────────────
def write_fixture(out_dir: Path, name: str, spec: dict, raw: dict | None, expected: dict) -> None:
    fixture_dir = out_dir / name
    fixture_dir.mkdir(parents=True, exist_ok=True)
    (fixture_dir / "construction_spec.json").write_text(json.dumps(spec, indent=2) + "\n")
    if raw is not None:
        (fixture_dir / "fp16_raw_outputs.json").write_text(json.dumps(raw, indent=2) + "\n")
    (fixture_dir / "expected.json").write_text(json.dumps(expected, indent=2) + "\n")
    print(f"  wrote fixture {name}")


def main() -> int:
    out = Path(__file__).resolve().parent / "fixtures" / "path_a"
    out.mkdir(parents=True, exist_ok=True)
    print(f"writing 6 fixtures to {out}")
    fixtures = [
        ("01_clean_certify",        fixture_01_clean_certify()),
        ("02_terminal_grab",        fixture_02_terminal_grab()),
        ("03_depth_competitor",     fixture_03_depth_competitor()),
        ("04_direct_query_shortcut", fixture_04_direct_query_shortcut()),
        ("05_constant_token",       fixture_05_constant_token()),
        ("06_rejected_construction", fixture_06_rejected_construction()),
        ("07_lock_violation",       fixture_07_lock_violation()),
    ]
    for name, (spec, raw, expected) in fixtures:
        write_fixture(out, name, spec, raw, expected)
    print("done.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
