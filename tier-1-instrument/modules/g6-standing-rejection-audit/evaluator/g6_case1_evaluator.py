#!/usr/bin/env python3
"""
g6_case1_evaluator.py — Minimal G6 evaluator for Case 1 (Missing-Channel Trap).

Static, deterministic, model-free. Reads a Case 1 artifact bundle and emits a
G6 disposition per the 8 checks named in TL ACTION 2026-06-14. No model is
queried; no inference is performed; the program only reads JSON files and
applies pre-declared boolean logic against the field values the bundle
records as properties of itself.

Authority + scope:
  - TL ACTION 2026-06-14 explicitly authorized this minimal build under
    YELLOW route state. The "no software build" boundary asserted in prior
    G6-module artifacts is lifted FOR THIS MINIMAL BUILD ONLY.
  - Remaining boundaries unchanged: no model execution, no certification,
    no compression / INT8 / INT4, no Paper B activation, no D4 reopening,
    no general G6 validity claim. This evaluator runs only against the
    constructed Case 1 bundle and answers only one question: does the
    bundle's recorded state warrant AUDIT-CIRCULARITY / LIMITED?

Usage:
  python3 g6_case1_evaluator.py [--bundle <dir>] [--output <file>]

Defaults to the in-tree Case 1 bundle and a results/ output path.
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path


# Pre-declared disposition vocabulary (per G6 spec §5).
AUDIT_CIRCULARITY = "AUDIT-CIRCULARITY / LIMITED"
REFUSAL_CONFIRMED = "REFUSAL-CONFIRMED"
REFUSAL_QUARANTINED = "REFUSAL-QUARANTINED"
AUDIT_INCONCLUSIVE = "AUDIT-INCONCLUSIVE"
BUNDLE_INSUFFICIENT = "BUNDLE-INSUFFICIENT (cannot evaluate)"


def _load(path: Path) -> dict:
    with path.open() as f:
        return json.load(f)


def evaluate_case1(bundle_dir: Path) -> dict:
    """Apply the 8 Case 1 checks to a bundle and return a disposition dict.

    Returns a dict containing per-check booleans, the final disposition, and
    the verifying evidence each check read. Side-effect-free; no model call.
    """
    refusal_path = bundle_dir / "CASE-1-REFUSAL-RECORD-v0.1.json"
    manifest_path = bundle_dir / "CASE-1-CHANNEL-MANIFEST-v0.1.json"

    # CHECK 1 — refusal record exists.
    check_1 = refusal_path.exists() and manifest_path.exists()
    if not check_1:
        return {
            "disposition": BUNDLE_INSUFFICIENT,
            "reason": "Required bundle files not found.",
            "checks": {"1_refusal_record_exists": False},
            "bundle_dir": str(bundle_dir),
        }

    refusal = _load(refusal_path)
    manifest = _load(manifest_path)

    # CHECK 2 — case is in G6 audit scope.
    check_2 = bool(refusal.get("gate_decision_in_g6_scope"))

    # CHECK 3 — raw E3 is unavailable.
    orig = refusal["original_read"]
    check_3 = (orig.get("raw_outputs_retained") is False)

    # CHECK 4 — only E2 labels are available.
    check_4 = bool(orig.get("labels_are_E2")) and (orig.get("raw_outputs_retained") is False)

    # CHECK 5 — CH1 unavailable.
    check_5 = manifest["CH1_blind_human_reader"].get("available") is False

    # CHECK 6 — CH2 unavailable.
    check_6 = manifest["CH2_pre_registered_schema"].get("available") is False

    # CHECK 7 — channel absence recorded as verifiable property of record.
    check_7 = bool(refusal["raw_E3_status"].get("absence_is_property_of_record"))

    # CHECK 8 — no unrelated defect.
    iso = refusal["scope_isolation_check"]
    check_8 = (
        iso.get("introduces_unrelated_defects") is False
        and iso.get("is_quarantined_for_unrelated_reasons") is False
    )

    checks = {
        "1_refusal_record_exists":               check_1,
        "2_case_in_g6_audit_scope":              check_2,
        "3_raw_E3_unavailable":                  check_3,
        "4_only_E2_labels_available":            check_4,
        "5_CH1_unavailable":                     check_5,
        "6_CH2_unavailable":                     check_6,
        "7_channel_absence_verifiable_property": check_7,
        "8_no_unrelated_defect":                 check_8,
    }

    # Disposition logic (pre-declared, deterministic).
    if not check_2:
        disposition = AUDIT_INCONCLUSIVE
        reason = "Out of G6 audit scope (check 2 failed)."
    elif not check_8:
        # Unrelated defect or unrelated quarantine forces a different output.
        disposition = REFUSAL_QUARANTINED if iso.get("is_quarantined_for_unrelated_reasons") else AUDIT_INCONCLUSIVE
        reason = "Case did not cleanly isolate 'channel absent' (check 8 failed)."
    elif check_3 and check_4 and check_5 and check_6 and check_7:
        # The fail-closed case: no independent channel, absence is a record property.
        disposition = AUDIT_CIRCULARITY
        reason = (
            "No independent channel is available against this record (CH1/CH2 both unavailable; "
            "raw E3 not retained; only E2 labels present). Channel absence is recorded as a "
            "verifiable property of the record. Per G6 spec §5 essential pair, the only honest "
            "output is AUDIT-CIRCULARITY / LIMITED. Returning REFUSAL-CONFIRMED would inherit "
            "the original read (E2 circularity, K1)."
        )
    else:
        # If channel(s) were available, CONFIRMED would be reachable; in this bundle they're not.
        disposition = REFUSAL_CONFIRMED
        reason = "An independent channel appears available (one of checks 3/4/5/6/7 did not hold)."

    return {
        "disposition": disposition,
        "reason": reason,
        "checks": checks,
        "bundle_dir": str(bundle_dir),
        "refusal_record": str(refusal_path),
        "channel_manifest": str(manifest_path),
        "evaluator_authority": "TL ACTION 2026-06-14; minimal build under YELLOW route state",
        "execution_kind": "static deterministic file-read; no model query",
    }


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="Minimal G6 evaluator for Case 1.")
    here = Path(__file__).resolve().parent
    default_bundle = here.parent / "case-1-missing-channel"
    default_output = here / "results" / "case-1-disposition.json"
    parser.add_argument("--bundle", type=Path, default=default_bundle)
    parser.add_argument("--output", type=Path, default=default_output)
    args = parser.parse_args(argv)

    result = evaluate_case1(args.bundle)
    result["timestamp_utc"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w") as f:
        json.dump(result, f, indent=2, sort_keys=False)
        f.write("\n")

    print(f"disposition: {result['disposition']}")
    print(f"checks: {result['checks']}")
    print(f"output written to: {args.output}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
