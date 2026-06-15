#!/usr/bin/env python3
"""
inspector.py — Path A construction inspector (v0.1).

Validates a Path A construction SCHEMA against the v0.3 construct-definition
admissibility checks BEFORE any items are generated or any model is queried.
Static, deterministic, model-free. Rejection produces a structured rejection
note that an auditor can verify mechanically.

Authority: TL ACTION 2026-06-15 ("Build Path A Inspector + G6 v0.3").
Inputs:  TARGET-CONSTRUCT-DEFINITION-v0.3 (sha eb72abb2…)
         PATH-A-CANDIDATE-CONSTRUCTION-DESIGN-v0.3 (sha 38e05460…)

Checks (rejection-by-inspection per TL):
  C1. C* is any terminal
  C2. {C*, B, T, T_i, X_i, B_competitors} not pairwise distinct
  C3. R1/R2/R3/R4/R4b/R5/R6cat not mechanically separable
  C4. A's r1 edge not unique
  C5. Same-depth competitors absent or D mismatch (default 5)
  C6. Relation frequency/order/position not balanced across target/competitor paths
  C7. Direct-query bridge withholding + neutral length-matched filler not representable
  C8. Four separate clutter-matched contexts not representable

Schema spec (JSON) input shape:
  {
    "construction_id":     str,
    "params":              {"k":int, "D":int, "p":int, "m":int},
    "target":              {"A":str, "B":str, "C_star":str, "T":str,
                            "r1":str, "r2":str,
                            "post_C_star_relations":[str], ...},
    "depth_2_competitors": [{"head_relation":str, "B_competitor":str,
                              "second_relation":str, "X":str}, ...]  (length == D),
    "decoy_chains":        [{"head":str, "bridge":str, "answer":str, "T_i":str},
                             ...]  (length == k),
    "relation_balance": {
        "frequency": dict[relation -> count],
        "order_positions": dict[relation -> list[int]],
        "position_within_paths": dict[relation -> list[int]],
    },
    "direct_query": {
        "withhold_fact_role": "B_to_C_star" | "A_to_B",
        "filler_form": str,        # template like "{W} holds {V}"
        "filler_contains_B_or_C_star": bool,   # must be false
    },
    "contexts": {
        "composite":     {"present_facts": "full"},
        "hop1":          {"context_isolated_from_composite": bool},
        "hop2":          {"context_isolated_from_composite": bool},
        "direct_query":  {"context_isolated_from_composite": bool},
        "load_matched":  bool,
    }
  }
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

# Local constants
sys.path.insert(0, str(Path(__file__).resolve().parent))
import constants


# ── Disposition vocabulary ──────────────────────────────────────────────────
PASS = "PASS"
REJECT = "REJECT"


def _err(check: str, reason: str, detail: dict | None = None) -> dict:
    out = {"check": check, "ok": False, "reason": reason}
    if detail is not None:
        out["detail"] = detail
    return out


def _ok(check: str) -> dict:
    return {"check": check, "ok": True}


# ── Individual checks ───────────────────────────────────────────────────────
def check_C1_C_star_not_terminal(spec: dict) -> dict:
    """C1: C* must not be any terminal (target T or any decoy T_i)."""
    C_star = spec["target"]["C_star"]
    target_T = spec["target"]["T"]
    decoy_terminals = [d["T_i"] for d in spec.get("decoy_chains", [])]
    if C_star == target_T:
        return _err("C1_C_star_not_terminal",
                    f"C* ({C_star!r}) == target T ({target_T!r}); R8.1 breach.")
    if C_star in decoy_terminals:
        return _err("C1_C_star_not_terminal",
                    f"C* ({C_star!r}) appears in decoy terminals {decoy_terminals}; R8.1 breach.")
    return _ok("C1_C_star_not_terminal")


def check_C2_pairwise_distinct(spec: dict) -> dict:
    """C2: {C*, B, T, T_i_*, X_*, B_competitor_*} all pairwise distinct."""
    tokens: list[tuple[str, str]] = [
        (spec["target"]["A"], "A"),
        (spec["target"]["B"], "B"),
        (spec["target"]["C_star"], "C_star"),
        (spec["target"]["T"], "T"),
    ]
    for i, d in enumerate(spec.get("decoy_chains", [])):
        tokens.append((d["T_i"], f"decoy_T_{i+1}"))
    for i, c in enumerate(spec.get("depth_2_competitors", [])):
        tokens.append((c["X"], f"X_{i+1}"))
        tokens.append((c["B_competitor"], f"B_competitor_{i+1}"))

    by_token: dict[str, list[str]] = {}
    for tok, role in tokens:
        by_token.setdefault(tok, []).append(role)
    collisions = {tok: roles for tok, roles in by_token.items() if len(roles) > 1}
    if collisions:
        return _err("C2_pairwise_distinct",
                    f"token collisions found: {collisions}", {"collisions": collisions})
    return _ok("C2_pairwise_distinct")


def check_C3_categories_separable(spec: dict) -> dict:
    """C3: All seven scorer categories R1/R2/R3/R4/R4b/R5/R6cat must be
    mechanically distinguishable. Operationally: the known entity sets each
    category resolves to must be non-overlapping. R1↔R6cat overlap is the
    common failure mode; if X_i tokens equal C* or B, R4b cannot separate."""
    C_star = spec["target"]["C_star"]
    B      = spec["target"]["B"]
    T      = spec["target"]["T"]
    decoy_terminals = {d["T_i"] for d in spec.get("decoy_chains", [])}
    competitors_X   = {c["X"]   for c in spec.get("depth_2_competitors", [])}
    competitors_B   = {c["B_competitor"] for c in spec.get("depth_2_competitors", [])}

    if C_star in competitors_X:
        return _err("C3_categories_separable",
                    "C* appears in X_i set; R1 vs R4b would collapse.")
    if B in competitors_B:
        return _err("C3_categories_separable",
                    "B appears in B_competitor set; R3 vs R4b would collapse.")
    if competitors_X & (decoy_terminals | {T}):
        return _err("C3_categories_separable",
                    "X_i overlaps with terminals; R4b vs R4/R2 would collapse.")
    if competitors_B & (decoy_terminals | {T} | competitors_X):
        return _err("C3_categories_separable",
                    "B_competitor overlaps with terminal/X set; categories not separable.")
    return _ok("C3_categories_separable")


def check_C4_r1_edge_unique(spec: dict) -> dict:
    """C4: A's r1 edge must be unique (so r1(A) = B is well-posed). The
    competitor relations s1, t1, ... must be DISJOINT from r1."""
    r1 = spec["target"]["r1"]
    competitor_relations = [c["head_relation"] for c in spec.get("depth_2_competitors", [])]
    if r1 in competitor_relations:
        return _err("C4_r1_edge_unique",
                    f"r1 ({r1!r}) appears in competitor head_relations {competitor_relations}; r1(A) not unique.")
    if len(competitor_relations) != len(set(competitor_relations)):
        return _err("C4_r1_edge_unique",
                    f"competitor head_relations not unique: {competitor_relations}")
    return _ok("C4_r1_edge_unique")


def check_C5_competitor_count(spec: dict, expected_D: int = constants.D_DEPTH_COMPETITORS) -> dict:
    """C5: Same-depth competitors must be present at the configured D count.

    In real-run mode, the Manager-lock binding (C9) enforces D = expected_D.
    In fixture mode, this check still verifies that the declared D matches the
    actual competitor list length (a structural consistency check, separate
    from the Manager-lock binding)."""
    competitors = spec.get("depth_2_competitors", [])
    declared_D = spec.get("params", {}).get("D", expected_D)
    if not competitors:
        return _err("C5_competitor_count",
                    "depth_2_competitors absent or empty; the depth-selection control is missing.")
    if len(competitors) != declared_D:
        return _err("C5_competitor_count",
                    f"depth_2_competitors length ({len(competitors)}) != declared D ({declared_D}).")
    # In real-run mode the Manager lock additionally enforces declared_D == expected_D;
    # see C9_manager_lock_binding. In fixture mode, declared_D may deviate.
    return _ok("C5_competitor_count")


def check_C9_manager_lock_binding(spec: dict) -> dict:
    """C9: Bind threshold-determining values to the Manager lock.

    Real-run mode (default; spec lacks `_fixture_mode: true`):
      - p, D, m, margin must all be present and match the Manager lock
      - Missing or deviating params → fail-closed REJECT (no silent fallback)

    Fixture mode (`_fixture_mode: true` set on spec):
      - Lock is not enforced; fixtures may vary params for testing
      - The flag explicitly excludes the construction from real-run admissibility
    """
    validation = constants.validate_manager_lock(spec)
    if validation["ok"]:
        if validation["mode"] == "fixture":
            return {"check": "C9_manager_lock_binding", "ok": True,
                    "mode": "fixture",
                    "note": "spec marked `_fixture_mode: true` — Manager lock not enforced; construction excluded from real-run admissibility."}
        return {"check": "C9_manager_lock_binding", "ok": True, "mode": "real-run"}
    parts = []
    if validation["missing"]:
        parts.append(f"missing params: {validation['missing']}")
    if validation["deviations"]:
        parts.append(f"deviations from Manager lock: {validation['deviations']}")
    return _err("C9_manager_lock_binding",
                f"real-run Manager-lock binding failed -- {'; '.join(parts)}. Set `_fixture_mode: true` to exclude from real-run admissibility.",
                {"validation": validation})


def check_C6_relation_balance(spec: dict) -> dict:
    """C6: Relation frequency, order, and position must be balanced across target
    and competitor paths (E8 binding admissibility property). Mechanically:
      - frequency: every queried/competitor relation appears the same number of times
      - role-grouped order: "head" relations (queried r1 + competitor head_relations)
        all appear at the same path-position; same for "tail" relations.
    """
    rb = spec.get("relation_balance")
    if rb is None:
        return _err("C6_relation_balance",
                    "relation_balance block absent; E8 binding admissibility property not declared.")

    freq = rb.get("frequency", {})
    if not freq:
        return _err("C6_relation_balance", "relation_balance.frequency missing.")
    head_relations = [spec["target"]["r1"]] + [c["head_relation"]   for c in spec.get("depth_2_competitors", [])]
    tail_relations = [spec["target"]["r2"]] + [c["second_relation"] for c in spec.get("depth_2_competitors", [])]

    if not head_relations or not tail_relations:
        return _err("C6_relation_balance",
                    "head_relations or tail_relations could not be assembled from spec.")

    # Frequency balance: every relation appears the same number of times.
    all_relations = head_relations + tail_relations
    all_freqs = [freq.get(r, 0) for r in all_relations]
    if len(set(all_freqs)) != 1:
        return _err("C6_relation_balance",
                    f"relation frequencies not balanced across queried+competitor paths: { {r: freq.get(r, 0) for r in all_relations} }")

    # Role-grouped order positions: every head relation must appear at the SAME
    # set of path-positions; every tail relation likewise. (heads vs tails may
    # differ — heads are slot 0 of their path, tails are slot 1.)
    order = rb.get("order_positions", {})
    if not order:
        return _err("C6_relation_balance",
                    "relation_balance.order_positions missing.")
    head_positions = {r: sorted(order.get(r, [])) for r in head_relations}
    tail_positions = {r: sorted(order.get(r, [])) for r in tail_relations}
    if len({tuple(v) for v in head_positions.values()}) != 1:
        return _err("C6_relation_balance",
                    f"head-relation order positions not balanced: {head_positions}")
    if len({tuple(v) for v in tail_positions.values()}) != 1:
        return _err("C6_relation_balance",
                    f"tail-relation order positions not balanced: {tail_positions}")
    return _ok("C6_relation_balance")


def check_C7_direct_query_filler(spec: dict) -> dict:
    """C7: Direct-query context must withhold the bridge AND substitute with
    neutral, length-matched filler that contains NEITHER B NOR C*."""
    dq = spec.get("direct_query")
    if dq is None:
        return _err("C7_direct_query_filler",
                    "direct_query block absent; control cannot be implemented.")
    if dq.get("withhold_fact_role") not in ("B_to_C_star", "A_to_B"):
        return _err("C7_direct_query_filler",
                    f"withhold_fact_role must be 'B_to_C_star' or 'A_to_B'; got {dq.get('withhold_fact_role')!r}")
    if not dq.get("filler_form"):
        return _err("C7_direct_query_filler", "filler_form template missing.")
    if dq.get("filler_contains_B_or_C_star") is not False:
        return _err("C7_direct_query_filler",
                    "filler_contains_B_or_C_star must be explicitly false (E5 binding).")
    return _ok("C7_direct_query_filler")


def check_C8_four_contexts(spec: dict) -> dict:
    """C8: Four separate clutter-matched contexts must be representable, with
    composite uncontaminated by prior controls."""
    ctx = spec.get("contexts")
    if ctx is None:
        return _err("C8_four_contexts", "contexts block absent.")
    required = ["composite", "hop1", "hop2", "direct_query"]
    missing = [name for name in required if name not in ctx]
    if missing:
        return _err("C8_four_contexts",
                    f"context blocks missing: {missing}")
    for name in ("hop1", "hop2", "direct_query"):
        if ctx[name].get("context_isolated_from_composite") is not True:
            return _err("C8_four_contexts",
                        f"{name}.context_isolated_from_composite must be true; got {ctx[name].get('context_isolated_from_composite')!r}")
    if ctx.get("load_matched") is not True:
        return _err("C8_four_contexts",
                    "contexts.load_matched must be true (E4 / OI-6).")
    return _ok("C8_four_contexts")


# ── Inspect entrypoint ──────────────────────────────────────────────────────
ALL_CHECKS = [
    check_C1_C_star_not_terminal,
    check_C2_pairwise_distinct,
    check_C3_categories_separable,
    check_C4_r1_edge_unique,
    check_C5_competitor_count,
    check_C6_relation_balance,
    check_C7_direct_query_filler,
    check_C8_four_contexts,
    check_C9_manager_lock_binding,
]


def inspect(spec: dict) -> dict:
    """Run all checks. Return disposition dict with PASS or REJECT."""
    results = [check(spec) for check in ALL_CHECKS]
    failures = [r for r in results if not r["ok"]]
    disposition = REJECT if failures else PASS

    out = {
        "inspector_version":       "0.1",
        "construction_id":         spec.get("construction_id", "<unknown>"),
        "disposition":             disposition,
        "checks":                  results,
        "n_checks":                len(results),
        "n_passes":                len(results) - len(failures),
        "n_failures":              len(failures),
        "manager_approved_values": constants.values_summary(),
    }
    if failures:
        out["rejection_note"] = {
            "construction_id":     spec.get("construction_id", "<unknown>"),
            "breached_checks":     [f["check"] for f in failures],
            "breach_reasons":      {f["check"]: f["reason"] for f in failures},
            "disposition_options": ["archive", "iterate", "abandon"],
            "decision_seat":       "Manager / TL under role-separation (per construct-definition v0.3 §8.4)",
        }
    return out


def main() -> int:
    p = argparse.ArgumentParser(description="Path A construction inspector.")
    p.add_argument("--spec",     type=Path, required=True, help="construction spec JSON")
    p.add_argument("--output",   type=Path, required=True, help="output disposition JSON")
    p.add_argument("--expected", type=Path, default=None,  help="optional expected disposition for comparison")
    args = p.parse_args()

    spec = json.loads(args.spec.read_text())
    result = inspect(spec)
    result["timestamp_utc"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    result["input_spec_path"] = str(args.spec)

    if args.expected and args.expected.exists():
        exp = json.loads(args.expected.read_text())
        result["_expected_disposition"] = exp.get("disposition")
        result["_expected_match"] = (result["disposition"] == exp.get("disposition"))

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n")

    print(f"disposition: {result['disposition']}")
    print(f"checks: {result['n_passes']}/{result['n_checks']} pass; {result['n_failures']} fail")
    if result["n_failures"]:
        for f in result["checks"]:
            if not f["ok"]:
                print(f"  REJECT [{f['check']}]: {f['reason']}")
    print(f"output: {args.output}")
    return 0 if result["disposition"] == PASS else 1


if __name__ == "__main__":
    sys.exit(main())
