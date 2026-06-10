"""
Paper 2 Regression Test (Manager C1)
====================================

Verifies that the B1 v2 runner produces v1-shape output AND bit-identical gate
decisions when run in Paper 2 reproduction context against the same Cell03
manifest used in the locked Paper 2 v1.0 result.

Per Manager C1 (B1 v2 authorization, 2026-06-09):
  Paper 2 context output equals the v1 shape PLUS additive fields only.
  Gate decisions remain bit-identical.
  Paper 2 reproduction behavior is not changed by Paper 3 substrate additions.

Reference artifact (locked, Paper 2 v1.0 Appendix B):
  tier0-run/RESULTS-TWOHOP-L1-cell03-1780948339.json
  sha256: f29783622fb14caca1c2a5829da8b874836add5d111356ea42be1f7d4a7b73f7
  Cell03 FP16: hop1 6/24, hop2 23/24, composite 15/24, neg_graph 6/24
  Gate 1 PASS, Gate 2 FAIL (Branch 3, NOT stress-eligible)

Modes
-----
  --mode smoke   Single item run; validates that runner loads the model and
                 produces v1-shape output. Fast (~1 min). Does NOT validate gate
                 decision bit-identity (single item is insufficient).
  --mode full    All 24 items, 4 query types each (96 inferences). Slow (~10-30
                 min). Validates v1-shape preservation AND gate decision
                 bit-identity against the locked reference.

Known limitations
-----------------
  - Environment runs mlx_lm 0.31.3; Paper 2 ran 0.19.3. Inference behavior is
    expected to be bit-identical given identical weights and decoding (greedy,
    temp=0.0), but cross-version drift is possible. Any divergence is flagged
    rather than treated as a B1 v2 regression.

— CS Engineer, 2026-06-09
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import runner_b1_v2 as r


# Locked reference (Paper 2 v1.0 Appendix B)
REFERENCE_RESULT_PATH = (
    HERE.parent.parent.parent / "tier0-run" / "RESULTS-TWOHOP-L1-cell03-1780948339.json"
)
REFERENCE_RESULT_HASH = (
    "sha256:f29783622fb14caca1c2a5829da8b874836add5d111356ea42be1f7d4a7b73f7"
)

# Paper 2 v1.0 gate decisions for Cell03 (recorded ground truth)
REFERENCE_GATE_DECISIONS = {
    "hop1_correct":          6,
    "hop2_correct":          23,
    "composite_correct":     15,
    "neg_graph_correct":     6,
    "gate_1":                "pass",
    "gate_2":                "fail",
    "stress_eligible":       False,
}

# Additive v2 fields expected on top of v1 shape
V2_ADDITIVE_FIELDS_TOP_LEVEL = {
    "gate_summary", "stress_eligible", "eligibility_reason_code", "voided_run_log",
}
V2_ADDITIVE_FIELDS_PROVENANCE = {
    "mlx_lm_version", "python_version", "model_snapshot_hash", "precision_rung",
    "quant_method", "analysis_script_hash",
    "first_candidate_data_access_timestamp", "framework_version", "threshold_sheet_hash",
}
V2_ADDITIVE_FIELDS_PER_ITEM = {
    "fp16_raw_output", "exact_output_match", "same_error_identity_key",
    "structural_proxies",
}


def load_reference() -> dict:
    """Load the locked Paper 2 reference result. Verify hash before trusting content."""
    if not REFERENCE_RESULT_PATH.exists():
        raise FileNotFoundError(f"Reference not found: {REFERENCE_RESULT_PATH}")
    actual_hash = r.sha256_file(REFERENCE_RESULT_PATH)
    if actual_hash != REFERENCE_RESULT_HASH:
        raise ValueError(
            f"Reference hash mismatch.\n"
            f"  expected: {REFERENCE_RESULT_HASH}\n"
            f"  actual:   {actual_hash}\n"
            f"Tier0-run/ files may have been modified, or the wrong reference is loaded."
        )
    return json.loads(REFERENCE_RESULT_PATH.read_text())


def validate_v1_shape_preservation(output: dict) -> dict:
    """Check that v1 fields are present and v2 additions are additive only.

    Returns dict of {check: status}.
    """
    checks = {}

    # v1 top-level fields (must be present)
    v1_top = {"provenance", "results"}
    actual_top = set(output.keys())
    checks["v1_top_fields_present"] = v1_top.issubset(actual_top)

    # v2 additive top-level fields (must be present too)
    checks["v2_top_fields_present"] = V2_ADDITIVE_FIELDS_TOP_LEVEL.issubset(actual_top)

    # No unexpected new fields at top level
    expected_top = v1_top | V2_ADDITIVE_FIELDS_TOP_LEVEL
    unexpected_top = actual_top - expected_top
    checks["v1_no_unexpected_top_fields"] = (len(unexpected_top) == 0)
    if unexpected_top:
        checks["v1_unexpected_top_fields_list"] = sorted(unexpected_top)

    # v1 provenance fields (a subset for spot-check)
    v1_prov = {"manifest_hash", "scorer_hash", "validator_hash", "runner_hash",
               "prompt_template_hash", "failure_taxonomy_version", "model_id",
               "decoding_settings", "run_timestamp"}
    prov = output.get("provenance", {})
    checks["v1_provenance_fields_present"] = v1_prov.issubset(set(prov.keys()))

    # v2 additive provenance fields
    checks["v2_provenance_fields_present"] = V2_ADDITIVE_FIELDS_PROVENANCE.issubset(set(prov.keys()))

    # Per-item v1 fields and v2 additions
    if output.get("results"):
        sample = output["results"][0]
        v1_item = {"item_id", "query_type", "prompt_rendered_hash", "raw_output",
                   "failure_class", "scaffold_class", "format_class",
                   "returned_token", "returned_role", "is_correct",
                   "dummy_baselines"}
        checks["v1_per_item_fields_present"] = v1_item.issubset(set(sample.keys()))
        checks["v2_per_item_fields_present"] = V2_ADDITIVE_FIELDS_PER_ITEM.issubset(set(sample.keys()))

    return checks


def compare_gate_decisions(output: dict, reference_gate_decisions: dict) -> dict:
    """Compare current run's gate decisions to Paper 2 ground truth."""
    gs = output.get("gate_summary", {})
    results = output.get("results", [])

    def count_correct(qt):
        items = [x for x in results if x["query_type"] == qt and x["format_class"] == "FORMAT_PASS"]
        return sum(1 for x in items if x["is_correct"])

    checks = {}
    checks["hop1_correct_match"] = (count_correct("hop1") == reference_gate_decisions["hop1_correct"])
    checks["hop1_correct_observed"] = count_correct("hop1")
    checks["hop1_correct_expected"] = reference_gate_decisions["hop1_correct"]

    checks["hop2_correct_match"] = (count_correct("hop2") == reference_gate_decisions["hop2_correct"])
    checks["hop2_correct_observed"] = count_correct("hop2")
    checks["hop2_correct_expected"] = reference_gate_decisions["hop2_correct"]

    checks["composite_correct_match"] = (count_correct("composite") == reference_gate_decisions["composite_correct"])
    checks["composite_correct_observed"] = count_correct("composite")
    checks["composite_correct_expected"] = reference_gate_decisions["composite_correct"]

    checks["neg_graph_correct_match"] = (count_correct("negative_graph") == reference_gate_decisions["neg_graph_correct"])
    checks["neg_graph_correct_observed"] = count_correct("negative_graph")
    checks["neg_graph_correct_expected"] = reference_gate_decisions["neg_graph_correct"]

    checks["gate_1_match"]   = (gs.get("gate_1", {}).get("status") == reference_gate_decisions["gate_1"])
    checks["gate_2_match"]   = (gs.get("gate_2", {}).get("status") == reference_gate_decisions["gate_2"])
    checks["stress_eligible_match"] = (output.get("stress_eligible") == reference_gate_decisions["stress_eligible"])

    checks["all_gate_decisions_match"] = all(
        v for k, v in checks.items() if k.endswith("_match")
    )
    return checks


def main():
    parser = argparse.ArgumentParser(description="Paper 2 regression test (Senior C1)")
    parser.add_argument("--mode", choices=["smoke", "full"], default="smoke",
                        help="smoke: 1 item validation; full: 24-item bit-identity check")
    parser.add_argument("--output-dir", default=str(HERE.parent / "results"),
                        help="Output directory for new run result")
    args = parser.parse_args()

    print(f"Paper 2 Regression Test — mode={args.mode}")

    # Step 0: Verify reference is loadable and hash-matches
    print("\nStep 0: Loading locked Paper 2 reference...")
    try:
        reference = load_reference()
        print(f"  reference loaded: {REFERENCE_RESULT_PATH.name}")
        print(f"  reference hash:   {REFERENCE_RESULT_HASH}")
    except (FileNotFoundError, ValueError) as e:
        print(f"FATAL: {e}", file=sys.stderr)
        return 2

    # Step 1: Run the B1 v2 runner
    print("\nStep 1: Running B1 v2 runner in Paper 2 reproduction context...")
    runner_argv = ["--mode", "live", "--context", "paper2-reproduction",
                   "--output-dir", args.output_dir,
                   "--output-prefix", f"RESULTS-B1V2-REGRESSION-{args.mode}"]
    if args.mode == "smoke":
        # For smoke mode we'd need to subset the manifest. Implementing this would
        # require runner support for --manifest-subset; for now smoke = full but
        # we just don't compare counts.
        print("  (smoke mode: running full manifest; comparison limited to v1 shape only)")
    rc = r.main(runner_argv)
    # rc 0 = stress-eligible, 1 = not stress-eligible (informational, expected for Cell03)
    if rc >= 2:
        print(f"FATAL: runner exited with code {rc}", file=sys.stderr)
        return rc

    # Find the most recent output
    out_dir = Path(args.output_dir)
    candidates = sorted(out_dir.glob(f"RESULTS-B1V2-REGRESSION-{args.mode}-cell03-*.json"),
                        key=lambda p: p.stat().st_mtime, reverse=True)
    if not candidates:
        print("FATAL: no output produced", file=sys.stderr)
        return 2
    output_path = candidates[0]
    output = json.loads(output_path.read_text())
    print(f"  output:        {output_path}")
    print(f"  runner_hash:   {output['provenance'].get('runner_hash')}")
    print(f"  mlx_lm_version:{output['provenance'].get('mlx_lm_version')}")

    # Step 2: v1 shape preservation
    print("\nStep 2: Validating v1 shape preservation...")
    shape_checks = validate_v1_shape_preservation(output)
    shape_pass = all(v for k, v in shape_checks.items() if isinstance(v, bool))
    for k, v in shape_checks.items():
        marker = "✓" if v is True else ("✗" if v is False else "ℹ")
        print(f"  {marker} {k}: {v}")

    # Step 3: Gate decision bit-identity (full mode only)
    gate_checks = None
    if args.mode == "full":
        print("\nStep 3: Comparing gate decisions to Paper 2 ground truth...")
        gate_checks = compare_gate_decisions(output, REFERENCE_GATE_DECISIONS)
        for k, v in gate_checks.items():
            if k.endswith("_match"):
                marker = "✓" if v else "✗"
                print(f"  {marker} {k}: {v}")
            else:
                print(f"    {k}: {v}")

    # Summary
    print("\n=== Regression Summary ===")
    print(f"  mode: {args.mode}")
    print(f"  v1 shape preserved: {shape_pass}")
    if gate_checks is not None:
        print(f"  gate decisions bit-identical: {gate_checks['all_gate_decisions_match']}")
        if not gate_checks["all_gate_decisions_match"]:
            print("  NOTE: gate decision drift may be due to mlx_lm version (0.19.3 -> 0.31.3),")
            print("        not B1 v2 substrate. Investigate before concluding regression failure.")

    overall_pass = shape_pass and (gate_checks is None or gate_checks["all_gate_decisions_match"])
    return 0 if overall_pass else 1


if __name__ == "__main__":
    sys.exit(main())
