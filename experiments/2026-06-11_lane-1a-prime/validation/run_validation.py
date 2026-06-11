"""Lane 1a' Phase 5 model-free validation pipeline entry point.

SYNTHETIC / DIAGNOSTIC -- NON-BINDING -- NOT FOR THRESHOLD DERIVATION
D2 PHASE 5 VALIDATION ARTIFACT
NO MODEL INVOKED -- NO MODEL LOADED
NO SWEEP_ID CREATED -- NO SWEEP EXECUTION AUTHORIZED

Executes the Phase 5 model-free validation pipeline against the
single rung L01 (representative). Per Manager-confirmed D2 scope:
  - construct pilot + final manifests (deterministic seeds)
  - apply policy battery (deterministic; no model)
  - run full-instrument oracle validation against all 9 oracle cases
  - run A6 final-manifest re-verification
  - populate T1, T3, T4 reports
  - assemble Instrument Validation Report draft
  - emit execution ledger

All emitted artifacts are SYNTHETIC / DIAGNOSTIC; lock-eligibility
determination only; no candidate / threshold / certification evidence.
"""
from __future__ import annotations

import dataclasses
import json
import sys
from dataclasses import asdict
from pathlib import Path

# Add package directory to path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from lane1a_prime.lock_packet import (
    DriftToleranceDeclaration,
    a6_final_manifest_reverification,
)
from lane1a_prime.validation import (
    DEFAULT_T3_CRITERIA,
    ManifestRecipe,
    apply_policy_battery,
    assemble_instrument_validation_report,
    compute_union_envelope,
    construct_pilot_manifests,
    emit_execution_ledger,
    populate_t1_report,
    populate_t3_report,
    populate_t4_report,
    run_full_instrument_oracle_validation,
    score_policy_outputs,
)


OUTPUT_DIR = Path(__file__).resolve().parent


def _json_default(obj):
    """JSON serializer for dataclasses and tuples."""
    if dataclasses.is_dataclass(obj):
        return asdict(obj)
    if isinstance(obj, tuple):
        return list(obj)
    return str(obj)


def _serialize_t1(t1):
    return {
        "per_policy_scores": {
            policy_name: {
                stratum_name: dataclasses.asdict(score)
                for stratum_name, score in strata.items()
            }
            for policy_name, strata in t1.per_policy_scores.items()
        },
        "union_envelope_score": t1.union_envelope_score,
        "envelope_cap": t1.envelope_cap,
        "room_below_envelope": t1.room_below_envelope,
        "policy_classifications": t1.policy_classifications,
        "a6_drift_block": t1.a6_drift_block,
    }


def main():
    rung_id = "L01"
    pilot_recipe = ManifestRecipe(rung_id=rung_id, seed=0)
    final_recipe = ManifestRecipe(rung_id=rung_id, seed=1)

    # 1. Construct manifests
    pilot_records = construct_pilot_manifests(pilot_recipe)
    final_records = construct_pilot_manifests(final_recipe)

    # 2. Apply policy battery
    pilot_outputs = apply_policy_battery(pilot_records)
    final_outputs = apply_policy_battery(final_records)

    # 3. Compute per-policy scores for A6
    pilot_battery_scores = {
        p: score_policy_outputs(pilot_records, outs, "answerable").accuracy
        for p, outs in pilot_outputs.items()
        if p != "copy_completion"
    }
    final_battery_scores = {
        p: score_policy_outputs(final_records, outs, "answerable").accuracy
        for p, outs in final_outputs.items()
        if p != "copy_completion"
    }
    pilot_envelope = compute_union_envelope(pilot_records, pilot_outputs)
    final_envelope = compute_union_envelope(final_records, final_outputs)

    # 4. A6 re-verification
    a6 = a6_final_manifest_reverification(
        pilot_battery_scores=pilot_battery_scores,
        pilot_envelope=pilot_envelope,
        final_battery_scores=final_battery_scores,
        final_envelope=final_envelope,
        declared_drift_tolerance=DriftToleranceDeclaration(
            per_policy=0.30,  # synthetic data; generous tolerance for Phase 5 demo
            envelope=0.30,
        ),
    )

    # 5. Full-instrument oracle validation
    verifications = run_full_instrument_oracle_validation(pilot_records)

    # 6. T1 / T3 / T4 reports
    t1 = populate_t1_report(pilot_records, pilot_outputs, a6_result=a6)
    t3 = populate_t3_report(criteria=DEFAULT_T3_CRITERIA)
    t4 = populate_t4_report()

    # 7. Emit JSON artifacts
    pilot_manifest_path = OUTPUT_DIR / "pilot_manifests_L01.json"
    final_manifest_path = OUTPUT_DIR / "final_manifests_L01.json"
    oracle_results_path = OUTPUT_DIR / "oracle_validation_results.json"
    t1_path = OUTPUT_DIR / "t1_report.json"
    t3_path = OUTPUT_DIR / "t3_report.json"
    t4_path = OUTPUT_DIR / "t4_report.json"
    report_path = OUTPUT_DIR / "instrument_validation_report.md"
    ledger_path = OUTPUT_DIR / "execution_ledger.json"

    pilot_manifest_path.write_text(json.dumps(pilot_records, indent=2))
    final_manifest_path.write_text(json.dumps(final_records, indent=2))
    oracle_results_path.write_text(json.dumps(
        [dataclasses.asdict(v) for v in verifications],
        indent=2, default=_json_default,
    ))
    t1_path.write_text(json.dumps(_serialize_t1(t1), indent=2))
    t3_path.write_text(json.dumps(dataclasses.asdict(t3), indent=2))
    t4_path.write_text(json.dumps(dataclasses.asdict(t4), indent=2))

    # 8. Assemble Instrument Validation Report
    report_md = assemble_instrument_validation_report(t1, t3, t4, verifications, rung_id)
    report_path.write_text(report_md)

    # 9. Execution ledger
    files_created = [
        pilot_manifest_path, final_manifest_path,
        oracle_results_path, t1_path, t3_path, t4_path, report_path,
    ]
    ledger = emit_execution_ledger(
        files_created=files_created,
        what_was_generated=(
            f"pilot manifests (seed=0, rung={rung_id}, n=96); "
            f"final manifests (seed=1, rung={rung_id}, n=96); "
            f"oracle case predictions for 9 oracle types; "
            f"per-policy score tables; union envelope scores; "
            f"A6 drift block; T1 / T3 / T4 reports"
        ),
        what_was_computed=(
            "per-policy answerable + null accuracy; distinct outputs; "
            "policy classifications (discriminative / operation_equivalent / "
            "degenerate_constant); union envelope at answerable stratum; "
            "Wilson score intervals; aggregate_per_stratum; "
            "full-instrument outcome per oracle case via "
            "emit_elimination_label + compute_rung_outcome; "
            "A6 per-policy and envelope drift; drift_within_tolerance flag"
        ),
    )
    ledger_path.write_text(json.dumps(ledger, indent=2))

    print(f"Phase 5 validation pipeline complete.")
    print(f"Files created in {OUTPUT_DIR}:")
    for f in files_created:
        print(f"  {f.name}")
    print(f"  execution_ledger.json")
    print(f"\nOracle validation: "
          f"{sum(1 for v in verifications if v.verdict_matched)}/{len(verifications)} matched")
    print(f"A6 drift within tolerance: {a6.drift_within_tolerance}")
    print(f"Union envelope (pilot answerable): {pilot_envelope:.4f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
