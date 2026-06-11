"""Lane 1a' Phase 5 corrective model-free validation pipeline entry point (v0.2).

SYNTHETIC / DIAGNOSTIC -- NON-BINDING -- NOT FOR THRESHOLD DERIVATION
D2 PHASE 5 v0.2 VALIDATION ARTIFACT (CORRECTIVE RE-RUN)
NO MODEL INVOKED -- NO MODEL LOADED
NO SWEEP_ID CREATED -- NO SWEEP EXECUTION AUTHORIZED

Executes the Phase 5 corrective re-run pipeline under PH5-4 pre-flight:
  1. verify lock-event artifact hashes (PH5-4)
  2. construct stratified pilot + final manifests (PH5-3)
  3. apply policy battery (deterministic; no model)
  4. run full-instrument oracle validation against 12 oracle cases
     using label-set match predicate (PH5-2)
  5. run A6 final-manifest re-verification at 0.05 tolerance
  6. populate T1, T3, T4 reports
  7. assemble Instrument Validation Report draft with PH5-5 run-1
     retention block
  8. emit execution ledger
"""
from __future__ import annotations

import dataclasses
import json
import sys
from dataclasses import asdict
from pathlib import Path

# Add package directory to path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from lane1a_prime.analysis import (
    ValidationPreFlightConfig,
    load_t3_bounds,
    verify_pre_flight_config,
)
from lane1a_prime.lock_packet import (
    DriftToleranceDeclaration,
    a6_final_manifest_reverification,
)
from lane1a_prime.oracle_cases import load_oracle_verdict_table
from lane1a_prime.validation import (
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

# PH5-1 lock event artifact hashes (post-corrective; CS+NS+TL co-signed at
# governance/2026-06-11_lane-1a-prime/PH5-1-JOINT-LOCK-EVENT-RECORD-v0.1.md).
# Provisional hashes from run-2 superseded; these reference the v2
# locked artifacts under the NS bounds-side review.
ORACLE_VERDICT_TABLE_HASH = "9c6cbda9eb5b6e850b88451529bb989dee6355ce145c31d1fca5d7b0f3a7fba5"
T3_BOUNDS_HASH = "45565d0b46c05da4f7d5c13956ac3a6331cc0748dfba4546f8f1d6cc46addd39"
STRATIFIED_RECIPE_HASH = "7ad3ccddecd070074e666ffaf2178aa0afd3cfda78fc08ef375fe68a907130c5"


def _json_default(obj):
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

    # PH5-4: pre-flight hash precondition
    pre_flight = ValidationPreFlightConfig(
        oracle_verdict_table_path=OUTPUT_DIR / "ORACLE_VERDICT_TABLE.json",
        oracle_verdict_table_hash=ORACLE_VERDICT_TABLE_HASH,
        t3_bounds_path=OUTPUT_DIR / "T3_BOUNDS_DECLARATION.json",
        t3_bounds_hash=T3_BOUNDS_HASH,
        stratified_recipe_path=OUTPUT_DIR / "STRATIFIED_RECIPE_SCHEDULE.json",
        stratified_recipe_hash=STRATIFIED_RECIPE_HASH,
    )
    verify_pre_flight_config(pre_flight)
    print("PH5-4 pre-flight: PASSED (all lock-event artifact hashes match)")

    # PH5-3: stratified recipe; identical for pilot and final (drift = 0
    # under construction-constant structural hit-rates).
    pilot_recipe = ManifestRecipe(rung_id=rung_id, seed=0)
    final_recipe = ManifestRecipe(rung_id=rung_id, seed=0)

    pilot_records = construct_pilot_manifests(pilot_recipe)
    final_records = construct_pilot_manifests(final_recipe)

    pilot_outputs = apply_policy_battery(pilot_records)
    final_outputs = apply_policy_battery(final_records)

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

    # A6 under joint-disposition tolerance 0.05 (unchanged from declared)
    a6 = a6_final_manifest_reverification(
        pilot_battery_scores=pilot_battery_scores,
        pilot_envelope=pilot_envelope,
        final_battery_scores=final_battery_scores,
        final_envelope=final_envelope,
        declared_drift_tolerance=DriftToleranceDeclaration(
            per_policy=0.05,
            envelope=0.05,
        ),
    )

    # PH5-2: full-instrument oracle validation with label-set matching
    verifications = run_full_instrument_oracle_validation(
        pilot_records,
        pre_flight_config=pre_flight,
    )

    # Load locked criteria for T3 report
    criteria = load_t3_bounds(OUTPUT_DIR / "T3_BOUNDS_DECLARATION.json")

    t1 = populate_t1_report(pilot_records, pilot_outputs, a6_result=a6)
    t3 = populate_t3_report(criteria=criteria)
    t4 = populate_t4_report()

    # Emit JSON artifacts
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

    report_md = assemble_instrument_validation_report(
        t1, t3, t4, verifications, rung_id,
        run_1_retention_pointer="validation/superseded_run-1/",
    )
    report_path.write_text(report_md)

    files_created = [
        pilot_manifest_path, final_manifest_path,
        oracle_results_path, t1_path, t3_path, t4_path, report_path,
    ]
    ledger = emit_execution_ledger(
        files_created=files_created,
        what_was_generated=(
            f"stratified pilot + final manifests (seed=0, rung={rung_id}, n=96, "
            f"stratified counts 20/20/20/20); 12 oracle case predictions; "
            f"per-policy scores; envelope; A6 drift block under 0.05 tolerance; "
            f"T1 / T3 / T4 reports with PH5-5 retention block"
        ),
        what_was_computed=(
            "per-policy answerable + null accuracy; distinct outputs; "
            "classifications; union envelope; Wilson + Newcombe-Wilson CIs; "
            "uniform-principle apply_criterion (6-criterion T3 set under "
            "locked bounds); full-instrument outcome per oracle via "
            "emit_elimination_label + compute_rung_outcome + "
            "match_oracle_verdict (4-clause label-set predicate); "
            "A6 per-policy and envelope drift at 0.05 tolerance"
        ),
    )
    ledger_path.write_text(json.dumps(ledger, indent=2))

    print(f"Phase 5 v0.2 corrective validation pipeline complete.")
    print(f"Files created in {OUTPUT_DIR}:")
    for f in files_created:
        print(f"  {f.name}")
    print(f"  execution_ledger.json")
    matched = sum(1 for v in verifications if v.overall_matched)
    print(f"\nOracle validation (label-set matching): "
          f"{matched}/{len(verifications)} overall_matched")
    print(f"A6 drift within tolerance (0.05): {a6.drift_within_tolerance}")
    print(f"Union envelope (pilot answerable): {pilot_envelope:.4f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
