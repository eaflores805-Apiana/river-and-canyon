#!/usr/bin/env python3
"""
g6_evaluator_v0_2.py — G6 Evaluator v0.2 (general run evaluator)

Reads a run directory's artifacts and DERIVES a disposition from rules.
The known disposition for any specific run lives in `expected/<run>-expected.json`,
NOT inside this evaluator. The evaluator is generic; given different inputs it
returns different outputs (proven by the contrast fixture under tests/fixtures/).

Authority + scope:
  TL ACTION 2026-06-15: "Build G6 v0.2 Evaluator with Contrast Fixture."
  Static software / tooling only. No model execution. No new run. No compression.
  Reads existing artifacts; computes booleans + counts; classifies by pre-declared
  rules. The known v0.1 disposition is NOT hardcoded — it is the expected fixture
  the evaluator's output is compared against, after the fact.

Rule sources:
  PREREGISTRATION §6 of MINIMAL-FP16-INT8-TWOHOP-L1-v0.1 (FP16-baseline gate).
  Senior post-run breakdown v0.2 (terminal-attraction signature classification).
  Terminal-Attraction finding report (i06-style same-token-across-queries
  pattern as the structural shortcut signature).

Usage:
  python3 g6_evaluator_v0_2.py --run <dir> [--output <file>] [--expected <file>]
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path


# Pre-declared verdict vocabulary -------------------------------------------
RETENTION_INCONCLUSIVE = "INCONCLUSIVE"
RETENTION_NO_DROP      = "NO_DROP"
RETENTION_DROP         = "DROP"
RETENTION_UNDETERMINED = "UNDETERMINED"

CONSTRUCTION_NEGATIVE_TERMINAL_ATTRACTION = "NEGATIVE_TERMINAL_ATTRACTION"
CONSTRUCTION_OK                            = "OK"
CONSTRUCTION_UNDETERMINED                  = "UNDETERMINED"

COMPRESSION_SAME_ERROR_IDENTITY  = "SAME_ERROR_IDENTITY"
COMPRESSION_SAME_OUTPUT_HEALTHY  = "SAME_OUTPUT_HEALTHY"
COMPRESSION_DIVERGENCE           = "DIVERGENCE"
COMPRESSION_NA                   = "NA"

BUNDLE_INSUFFICIENT = "BUNDLE_INSUFFICIENT"


# Pre-declared thresholds (locked here, before any result file is written) ---
HOP1_COMPETENCE_THRESHOLD          = 0.50   # rule A: model must do single-hop better than chance-ish
COMPOSITE_SAME_TOKEN_TOLERANCE     = 0      # rule B: zero composite-correct items may use the
                                            #         same-token-across-queries shortcut
DROP_THRESHOLD_ITEMS               = 2      # NO_DROP requires INT8 within 1 item of FP16
BYTE_IDENTITY_THRESHOLD            = 1.0    # all 24/24 must match to call IDENTICAL


_ANSWER_RE = re.compile(r"^ANSWER:\s+(.+?)\s*$", re.IGNORECASE)


def extract_answer(raw_output: str) -> str | None:
    m = _ANSWER_RE.match(raw_output.strip())
    if not m:
        return None
    return m.group(1).strip()


def _group_by_item(results: list[dict]) -> dict[str, dict[str, dict]]:
    by_item: dict[str, dict[str, dict]] = {}
    for r in results:
        by_item.setdefault(r["item_id"], {})[r["query_type"]] = r
    return by_item


# ── Rule A: component competence ─────────────────────────────────────────────
def rule_a_component_competence(fp16_results: list[dict],
                                threshold: float = HOP1_COMPETENCE_THRESHOLD) -> dict:
    """The FP16 baseline must do single-hop retrieval at >= threshold."""
    hop1_results = [r for r in fp16_results if r["query_type"] == "hop1"]
    n = len(hop1_results)
    correct = sum(1 for r in hop1_results
                  if extract_answer(r["raw_output"]) == r["expected"])
    rate = correct / n if n else 0.0
    return {
        "pass":               rate >= threshold,
        "hop1_correct":       correct,
        "hop1_n":             n,
        "hop1_correct_rate":  rate,
        "threshold":          threshold,
    }


# ── Rule B: composite via chain-following ────────────────────────────────────
def rule_b_composite_chain_following(fp16_results: list[dict],
                                     tolerance: int = COMPOSITE_SAME_TOKEN_TOLERANCE) -> dict:
    """For any composite-correct item, the model's hop1 output must NOT equal
    its composite output. The 'same-token-across-queries' pattern (the i06
    signature) is the structural shortcut signal."""
    by_item = _group_by_item(fp16_results)
    composite_correct = []
    same_token_items = []
    for item_id, queries in by_item.items():
        if "composite" not in queries:
            continue
        c_ans = extract_answer(queries["composite"]["raw_output"])
        c_exp = queries["composite"]["expected"]
        if c_ans == c_exp:
            composite_correct.append(item_id)
            if "hop1" in queries:
                h1_ans = extract_answer(queries["hop1"]["raw_output"])
                if h1_ans == c_ans and h1_ans is not None:
                    same_token_items.append(item_id)
    return {
        "pass":                              len(same_token_items) <= tolerance,
        "composite_correct_total":           len(composite_correct),
        "same_token_across_queries_count":   len(same_token_items),
        "same_token_item_ids":               same_token_items,
        "tolerance":                         tolerance,
    }


# ── FP16-baseline gate ──────────────────────────────────────────────────────
def evaluate_baseline_gate(fp16_results: list[dict]) -> dict:
    a = rule_a_component_competence(fp16_results)
    b = rule_b_composite_chain_following(fp16_results)
    verdict = "PASS" if (a["pass"] and b["pass"]) else "FAIL"
    return {
        "verdict": verdict,
        "rule_a_component_competence": a,
        "rule_b_composite_chain_following": b,
    }


# ── Byte-identity (FP16 vs INT8 raw outputs) ─────────────────────────────────
def evaluate_byte_identity(fp16_results: list[dict],
                           int8_results: list[dict] | None) -> dict:
    if not int8_results:
        return {"identity": "NA", "differences": None, "total_generations": len(fp16_results)}
    by_fp16 = {(r["item_id"], r["query_type"]): r for r in fp16_results}
    by_int8 = {(r["item_id"], r["query_type"]): r for r in int8_results}
    keys = sorted(set(by_fp16) | set(by_int8))
    differences = 0
    diff_pairs: list[dict] = []
    for k in keys:
        a = by_fp16.get(k)
        b = by_int8.get(k)
        if a is None or b is None or a["raw_output"] != b["raw_output"]:
            differences += 1
            if len(diff_pairs) < 10:  # cap on noise
                diff_pairs.append({
                    "item_id":    k[0],
                    "query_type": k[1],
                    "fp16_raw":   a["raw_output"] if a else None,
                    "int8_raw":   b["raw_output"] if b else None,
                })
    rate = (len(keys) - differences) / len(keys) if keys else 0.0
    identity = "IDENTICAL" if rate >= BYTE_IDENTITY_THRESHOLD else "DIVERGENT"
    return {
        "identity":           identity,
        "differences":        differences,
        "total_generations":  len(keys),
        "match_rate":         rate,
        "diff_examples":      diff_pairs,
    }


# ── Verdict derivation (each from a pre-declared mapping over the above) ─────
def derive_construction_verdict(gate: dict) -> str:
    if gate["verdict"] == "FAIL":
        a_failed = not gate["rule_a_component_competence"]["pass"]
        b_failed = not gate["rule_b_composite_chain_following"]["pass"]
        if a_failed and b_failed:
            return CONSTRUCTION_NEGATIVE_TERMINAL_ATTRACTION
        return CONSTRUCTION_UNDETERMINED
    return CONSTRUCTION_OK


def derive_compression_observation(byte_identity: dict, gate: dict) -> str:
    if byte_identity["identity"] == "NA":
        return COMPRESSION_NA
    if byte_identity["identity"] == "IDENTICAL":
        if gate["verdict"] == "FAIL":
            return COMPRESSION_SAME_ERROR_IDENTITY
        return COMPRESSION_SAME_OUTPUT_HEALTHY
    return COMPRESSION_DIVERGENCE


def derive_retention_verdict(byte_identity: dict, gate: dict,
                             fp16_results: list[dict],
                             int8_results: list[dict] | None) -> str:
    if gate["verdict"] == "FAIL":
        return RETENTION_INCONCLUSIVE
    if not int8_results:
        return RETENTION_UNDETERMINED
    # Baseline passed and INT8 data is available — compare correct-counts.
    fp16_correct = sum(1 for r in fp16_results
                       if extract_answer(r["raw_output"]) == r["expected"])
    int8_correct = sum(1 for r in int8_results
                       if extract_answer(r["raw_output"]) == r["expected"])
    if fp16_correct - int8_correct <= DROP_THRESHOLD_ITEMS - 1:
        return RETENTION_NO_DROP
    return RETENTION_DROP


# ── Main evaluator ──────────────────────────────────────────────────────────
def evaluate(run_dir: Path) -> dict:
    prereg_path = run_dir / "PREREGISTRATION.md"
    fp16_path   = run_dir / "fp16_raw_outputs.json"
    int8_path   = run_dir / "int8_raw_outputs.json"

    has_prereg = prereg_path.exists()
    has_fp16   = fp16_path.exists()
    has_int8   = int8_path.exists()

    if not (has_prereg and has_fp16):
        return {
            "evaluator_version":         "0.2",
            "run_dir":                   str(run_dir),
            "status":                    BUNDLE_INSUFFICIENT,
            "preregistration_exists":    has_prereg,
            "fp16_raw_present":          has_fp16,
            "int8_raw_present":          has_int8,
            "reason":                    "PREREGISTRATION.md and fp16_raw_outputs.json are both required.",
        }

    fp16_data    = json.loads(fp16_path.read_text())
    fp16_results = fp16_data.get("results", [])
    int8_results = None
    if has_int8:
        int8_results = json.loads(int8_path.read_text()).get("results", [])

    gate            = evaluate_baseline_gate(fp16_results)
    byte_identity   = evaluate_byte_identity(fp16_results, int8_results)
    construction    = derive_construction_verdict(gate)
    compression     = derive_compression_observation(byte_identity, gate)
    retention       = derive_retention_verdict(byte_identity, gate, fp16_results, int8_results)

    forbidden = [
        "Claim C progress",
        "Paper B activation",
        "general compression robustness",
        "certified baseline",
        "task family viability",
        "model passed / capability established / not shortcut-driven",
        "product/funder-facing result",
        "mechanism / architecture / training-distribution claim",
    ]

    return {
        "evaluator_version":               "0.2",
        "run_dir":                         str(run_dir),
        "status":                          "EVALUATED",
        "preregistration_exists":          has_prereg,
        "preregistration_path":            str(prereg_path),
        "fp16_raw_present":                has_fp16,
        "int8_raw_present":                has_int8,
        "baseline_gate":                   gate,
        "byte_identity":                   byte_identity,
        "construction_task_verdict":       construction,
        "compression_observation":         compression,
        "retention_compression_verdict":   retention,
        "forbidden_interpretations":       forbidden,
        "rule_sources": [
            "PREREGISTRATION §6 of MINIMAL-FP16-INT8-TWOHOP-L1-v0.1 (FP16-baseline gate)",
            "Senior post-run breakdown v0.2 (terminal-attraction signature)",
            "Terminal-Attraction finding report (same-token-across-queries i06 signature)",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="G6 Evaluator v0.2 (general run evaluator).")
    parser.add_argument("--run",      type=Path, required=True, help="run directory")
    parser.add_argument("--output",   type=Path, required=True, help="output disposition JSON path")
    parser.add_argument("--expected", type=Path, default=None,  help="optional: expected disposition fixture (for comparison only)")
    args = parser.parse_args()

    result = evaluate(args.run)
    result["timestamp_utc"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n")

    # Optional: compare against expected (informational; never modifies output).
    if args.expected and args.expected.exists():
        exp = json.loads(args.expected.read_text())
        # Compare only the verdict-level fields (counts/diff-examples may shift on noise).
        keys_to_compare = (
            "retention_compression_verdict",
            "construction_task_verdict",
            "compression_observation",
        )
        match = all(result.get(k) == exp.get(k) for k in keys_to_compare)
        result["_expected_match"] = match
        result["_expected_compared_keys"] = list(keys_to_compare)
        # Rewrite with comparison appended (keeps the comparison auditable).
        args.output.write_text(json.dumps(result, indent=2) + "\n")
        print(f"emitted vs expected match (verdict fields): {match}")

    print(f"status:                          {result.get('status')}")
    print(f"baseline_gate verdict:           {result.get('baseline_gate', {}).get('verdict')}")
    print(f"byte_identity:                   {result.get('byte_identity', {}).get('identity')}")
    print(f"construction_task_verdict:       {result.get('construction_task_verdict')}")
    print(f"compression_observation:         {result.get('compression_observation')}")
    print(f"retention_compression_verdict:   {result.get('retention_compression_verdict')}")
    print(f"output: {args.output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
