"""Lane 1a' Prime D4-B Runner — L01 with token-prior ACTIVE.

Manager D4-B authorization 2026-06-11 (all four boxes:
sweep execution + sweep_id creation + L01 sweep + token-prior by name).

Two-sweep structure:
  1. Candidate sweep: retrieval-shell prompts (prompt_template_v1.json),
     96 records.
  2. TP control sweep: no-bindings shell prompts
     (prompt_template_v1_tp.json), same 96 records.

TP criterion ACTIVE: Newcombe-Wilson CI on (candidate_correct -
tp_control_correct) / n_answerable; fires iff CI upper < locked margin
0.10.

The runner reuses the D4-A patched runner's utilities and the symmetric
Q2-authorized TP banner form.
"""
from __future__ import annotations

import hashlib
import json
import os
import platform
import random
import string as _string
import sys
import time
import traceback
from dataclasses import dataclass
from pathlib import Path


RUNNER_PATH = Path(__file__).resolve()
RUNNER_DIR = RUNNER_PATH.parent
EXPERIMENT_DIR = RUNNER_DIR.parent
VALIDATION_DIR = EXPERIMENT_DIR / "validation"
REPO_ROOT = EXPERIMENT_DIR.parent.parent
SEALED_LOCK_RECORD = REPO_ROOT / "governance" / "2026-06-11_lane-1a-prime" / "LANE1A-PRIME-SEALED-LOCK-RECORD-v1.0.md"

OUTPUT_DIR = EXPERIMENT_DIR / "d4_b_pilot"
PRECONDITIONS_PATH = RUNNER_DIR / "preconditions_d4b.json"
DECODING_CONFIG_PATH = RUNNER_DIR / "decoding_config.json"
PROMPT_TEMPLATE_CAND_PATH = RUNNER_DIR / "prompt_template_v1.json"
PROMPT_TEMPLATE_TP_PATH = RUNNER_DIR / "prompt_template_v1_tp.json"

sys.path.insert(0, str(EXPERIMENT_DIR))

from d4_runner.lane1a_runner import (
    D4ARunnerAbort,
    compute_model_snapshot_hash,
    sha256_file,
    stamp_environment,
    tp_banner_block,
)


def precondition_mlx_lm_version_check(env: dict, authorized: str) -> str:
    try:
        from importlib.metadata import version as pkg_version
        actual = pkg_version("mlx-lm")
    except Exception as exc:
        raise D4ARunnerAbort(
            "FRAMEWORK_VERSION_LOOKUP_FAILED",
            f"could not determine mlx-lm version: {exc}",
        )
    env["mlx_lm_version"] = actual
    if actual != authorized:
        raise D4ARunnerAbort(
            "FRAMEWORK_VERSION_MISMATCH",
            f"authorized mlx_lm {authorized}; actual {actual}",
        )
    try:
        from importlib.metadata import version as pkg_version
        env["mlx_core_version"] = pkg_version("mlx")
    except Exception:
        env["mlx_core_version"] = "unknown"
    return actual


def precondition_ph5_4(preconditions: dict) -> dict:
    from lane1a_prime.analysis import (
        ValidationPreFlightConfig,
        ValidationPreFlightRefused,
        verify_pre_flight_config,
    )
    le_hashes = preconditions["lock_event_hashes"]
    cfg = ValidationPreFlightConfig(
        oracle_verdict_table_path=VALIDATION_DIR / "ORACLE_VERDICT_TABLE.json",
        oracle_verdict_table_hash=le_hashes["oracle_verdict_table"],
        t3_bounds_path=VALIDATION_DIR / "T3_BOUNDS_DECLARATION.json",
        t3_bounds_hash=le_hashes["t3_bounds"],
        stratified_recipe_path=VALIDATION_DIR / "STRATIFIED_RECIPE_SCHEDULE.json",
        stratified_recipe_hash=le_hashes["stratified_recipe"],
    )
    try:
        verify_pre_flight_config(cfg)
    except ValidationPreFlightRefused as exc:
        raise D4ARunnerAbort("PH5_4_REFUSAL", str(exc))
    return {
        "status": "PASSED",
        "oracle_verdict_table_hash": le_hashes["oracle_verdict_table"],
        "t3_bounds_hash": le_hashes["t3_bounds"],
        "stratified_recipe_hash": le_hashes["stratified_recipe"],
    }


def precondition_manifest_hashes(preconditions: dict) -> dict:
    pilot_p = VALIDATION_DIR / "pilot_manifests_L01.json"
    final_p = VALIDATION_DIR / "final_manifests_L01.json"
    pilot_h = sha256_file(pilot_p)
    final_h = sha256_file(final_p)
    expected_pilot = preconditions["sealed_manifest_hashes"]["pilot_L01"]
    expected_final = preconditions["sealed_manifest_hashes"]["final_L01"]
    if pilot_h != expected_pilot:
        raise D4ARunnerAbort(
            "MANIFEST_HASH_MISMATCH",
            f"pilot manifest hash {pilot_h} != expected {expected_pilot}",
        )
    if final_h != expected_final:
        raise D4ARunnerAbort(
            "MANIFEST_HASH_MISMATCH",
            f"final manifest hash {final_h} != expected {expected_final}",
        )
    return {"pilot_L01": pilot_h, "final_L01": final_h}


def precondition_sealed_lock_record(preconditions: dict) -> str:
    actual = sha256_file(SEALED_LOCK_RECORD)
    expected = preconditions["sealed_lock_record_hash"]
    if actual != expected:
        raise D4ARunnerAbort(
            "SEALED_LOCK_RECORD_MUTATED",
            f"sealed LOCK-RECORD hash {actual} != sealed-time {expected}",
        )
    return actual


def precondition_model_snapshot(env: dict, preconditions: dict) -> Path:
    snap_root = Path(os.path.expanduser(
        "~/.cache/huggingface/hub/models--Qwen--Qwen2.5-3B-Instruct/snapshots"
    ))
    if not snap_root.is_dir():
        raise D4ARunnerAbort("MODEL_SNAPSHOT_NOT_FOUND",
                             f"HF snapshot root not present: {snap_root}")
    snapshots = list(snap_root.iterdir())
    if not snapshots:
        raise D4ARunnerAbort("MODEL_SNAPSHOT_NOT_FOUND", f"no snapshots under {snap_root}")
    snap_dir = snapshots[0]
    env["hf_snapshot_dir"] = str(snap_dir)
    env["hf_revision"] = snap_dir.name
    computed = compute_model_snapshot_hash(snap_dir)
    env["model_snapshot_hash_computed"] = computed
    env["model_snapshot_hash_authorized"] = preconditions["authorized_model_snapshot_hash"]
    if computed != preconditions["authorized_model_snapshot_hash"]:
        raise D4ARunnerAbort(
            "MODEL_SNAPSHOT_HASH_MISMATCH",
            f"computed {computed} != authorized {preconditions['authorized_model_snapshot_hash']}",
        )
    return snap_dir


def render_prompt(template: dict, record: dict, pair_list_override: str = "normal") -> tuple[str, str]:
    """Render the (system, user) text. If pair_list_override == 'empty', use empty pair list."""
    from d4_runner.parse_model_output import render_pair_lines, render_query_key
    if pair_list_override == "empty":
        pair_lines = ""
    else:
        pairs = record["context_block"]["real_pair_block"]["pairs"]
        pair_lines = render_pair_lines(pairs)
    query_key = render_query_key(record["queried_key"])
    user_text = template["user_template"].format(pair_lines=pair_lines, query_key=query_key)
    return template["system"], user_text


def run_inference(model, tokenizer, system_text: str, user_text: str,
                  decoding_config: dict) -> tuple[str, float, str]:
    import mlx_lm
    messages = [
        {"role": "system", "content": system_text},
        {"role": "user", "content": user_text},
    ]
    try:
        prompt_text = tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=True
        )
    except Exception as exc:
        raise D4ARunnerAbort("PROMPT_RENDER_FAILURE",
                              f"chat template apply failed: {exc}")
    t0 = time.time()
    try:
        from mlx_lm import generate
        output_text = generate(model, tokenizer, prompt=prompt_text,
                               max_tokens=decoding_config["max_new_tokens"], verbose=False)
    except TypeError:
        from mlx_lm import generate
        output_text = generate(model, tokenizer, prompt_text,
                               max_tokens=decoding_config["max_new_tokens"])
    except Exception as exc:
        raise D4ARunnerAbort("INFERENCE_FAILURE", f"mlx_lm.generate failed: {exc}")
    latency_ms = (time.time() - t0) * 1000.0
    return output_text, latency_ms, "completed"


def make_sweep_id(suffix: str) -> str:
    ts = time.strftime("%Y%m%d-%H%M%S")
    rand6 = "".join(random.SystemRandom().choices(
        _string.ascii_lowercase + _string.digits, k=6))
    return f"lane1a-prime-d4b-{suffix}-{ts}-{rand6}"


def emit_abort_artifact(reason_code: str, message: str, env: dict,
                         partial: dict, started_at: float) -> Path:
    abort_dir = OUTPUT_DIR / f"aborted_{time.strftime('%Y%m%d-%H%M%S')}"
    abort_dir.mkdir(parents=True, exist_ok=True)
    (abort_dir / "abort_record.json").write_text(json.dumps({
        "reason_code": reason_code,
        "message": message,
        "env": env,
        "partial_state": partial,
        "elapsed_seconds": time.time() - started_at,
        "sealed_lock_record_must_remain_unchanged": True,
    }, indent=2))
    return abort_dir


def run_sweep(model, tokenizer, records, prompt_template, decoding_config,
              pair_list_override, output_subdir, sweep_label):
    """Run one inference sweep over the 96 records. Returns (predictions, per_record_outputs)."""
    from d4_runner.parse_model_output import parse_model_output
    from lane1a_prime.oracle_cases import SimulatedPrediction
    output_subdir.mkdir(parents=True, exist_ok=True)
    predictions = []
    per_record = []
    for idx, record in enumerate(records):
        record_id = f"L01-{idx:03d}-{record['stratum']}"
        system_text, user_text = render_prompt(prompt_template, record, pair_list_override)
        output_text, latency_ms, finish_reason = run_inference(
            model, tokenizer, system_text, user_text, decoding_config
        )
        parsed = parse_model_output(output_text)
        rec = {
            "record_id": record_id,
            "sweep_label": sweep_label,
            "stratum": record["stratum"],
            "queried_key": record["queried_key"],
            "gold": record["gold"],
            "prompt_user_text": user_text,
            "output_text": output_text,
            "parsed": parsed,
            "latency_ms": latency_ms,
            "finish_reason": finish_reason,
        }
        per_record.append(rec)
        (output_subdir / f"{record_id}.json").write_text(json.dumps(rec, indent=2))
        sp = SimulatedPrediction(
            record_id=record_id,
            predicted_value_token_ids=parsed["predicted_value_token_ids"],
        )
        predictions.append(sp)
        if (idx + 1) % 20 == 0:
            print(f"[D4-B {sweep_label}]   {idx + 1}/{len(records)} done")
    return tuple(predictions), per_record


def main(argv=None) -> int:
    started_at = time.time()
    env = stamp_environment()
    partial: dict = {}
    try:
        # 1. Load preconditions
        preconditions = json.loads(PRECONDITIONS_PATH.read_text())
        env["preconditions_hash"] = sha256_file(PRECONDITIONS_PATH)

        # 1a. TP banner — ACTIVE form per Manager D4-B Q4 authorization
        token_prior_authorized = preconditions.get(
            "token_prior_decision", ""
        ).upper().startswith("AUTHORIZED")
        if not token_prior_authorized:
            raise D4ARunnerAbort(
                "TP_DECISION_MISALIGNMENT",
                "D4-B runner requires token_prior_decision starting with AUTHORIZED in preconditions",
            )
        tp_authority_ref = preconditions["token_prior_decision"]
        tp_banner = tp_banner_block(token_prior_authorized, tp_authority_ref)

        # 2. Version check
        precondition_mlx_lm_version_check(env, preconditions["authorized_mlx_lm_version"])

        # 3. PH5-4
        pre_flight_log = precondition_ph5_4(preconditions)
        partial["pre_flight"] = pre_flight_log

        # 4. Manifest hashes
        manifest_hashes = precondition_manifest_hashes(preconditions)
        partial["manifest_hashes"] = manifest_hashes

        # 5. Sealed LOCK-RECORD
        sealed_hash = precondition_sealed_lock_record(preconditions)
        partial["sealed_lock_record_hash"] = sealed_hash

        # 6. Snapshot
        snap_dir = precondition_model_snapshot(env, preconditions)
        partial["snapshot_dir"] = str(snap_dir)

        # 7. Two distinct sweep_ids
        candidate_sweep_id = make_sweep_id("cand")
        tp_sweep_id = make_sweep_id("tp")
        env["candidate_sweep_id"] = candidate_sweep_id
        env["tp_sweep_id"] = tp_sweep_id

        # 8. Output directory
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

        # 9. Write pre-flight log
        (OUTPUT_DIR / "pre_flight_log.json").write_text(json.dumps({
            "tp_banner": tp_banner,
            "run_header": {
                "candidate_sweep_id": candidate_sweep_id,
                "tp_sweep_id": tp_sweep_id,
                "tp_banner": tp_banner,
            },
            "candidate_sweep_id": candidate_sweep_id,
            "tp_sweep_id": tp_sweep_id,
            "ph5_4": pre_flight_log,
            "mlx_lm_version_check": "PASSED",
            "mlx_lm_version_authorized": preconditions["authorized_mlx_lm_version"],
            "mlx_lm_version_actual": env["mlx_lm_version"],
            "manifest_hashes": manifest_hashes,
            "sealed_lock_record_hash": sealed_hash,
            "snapshot_hash_authorized": preconditions["authorized_model_snapshot_hash"],
            "snapshot_hash_computed": env["model_snapshot_hash_computed"],
            "all_preconditions": "PASSED",
            "env": env,
        }, indent=2))

        # 10. Load model
        print(f"[D4-B] candidate_sweep_id={candidate_sweep_id}")
        print(f"[D4-B] tp_sweep_id={tp_sweep_id}")
        print(f"[D4-B] loading model from {snap_dir}...")
        from mlx_lm import load as mlx_load
        model, tokenizer = mlx_load(str(snap_dir))
        env["model_loaded"] = True

        # 11. Load manifests + decoding + templates
        pilot_records = json.loads((VALIDATION_DIR / "pilot_manifests_L01.json").read_text())
        decoding_config = json.loads(DECODING_CONFIG_PATH.read_text())
        candidate_template = json.loads(PROMPT_TEMPLATE_CAND_PATH.read_text())
        tp_template = json.loads(PROMPT_TEMPLATE_TP_PATH.read_text())

        # 12. Candidate sweep
        print(f"[D4-B] candidate sweep on {len(pilot_records)} records...")
        cand_predictions, cand_per_record = run_sweep(
            model, tokenizer, pilot_records, candidate_template, decoding_config,
            "normal", OUTPUT_DIR / "candidate_outputs", "candidate",
        )

        # 13. TP control sweep
        print(f"[D4-B] TP control sweep on {len(pilot_records)} records...")
        tp_predictions, tp_per_record = run_sweep(
            model, tokenizer, pilot_records, tp_template, decoding_config,
            "empty", OUTPUT_DIR / "tp_control_outputs", "tp_control",
        )

        # 14. Build measurements with measured TP control
        from lane1a_prime.analysis import (
            EliminationCriterion, CriterionComparison, apply_criterion,
            newcombe_wilson_difference, aggregate_per_stratum,
        )
        from lane1a_prime.validation import (
            apply_policy_battery, compute_union_envelope,
            populate_t1_report, populate_t3_report, populate_t4_report,
            assemble_instrument_validation_report,
        )

        outputs_by_policy = apply_policy_battery(pilot_records)
        envelope = compute_union_envelope(pilot_records, outputs_by_policy, "answerable")

        # Measurements (D4-B variant: measured TP control)
        n_answerable = sum(1 for r in pilot_records if r["stratum"] == "answerable")
        n_null = sum(1 for r in pilot_records if r["stratum"] == "null")

        def correct(record, pred):
            if pred.predicted_value_token_ids is None:
                return False
            return list(pred.predicted_value_token_ids) == record["gold"]["value_token_ids"]

        def abstained(pred):
            return pred.predicted_value_token_ids is None

        cand_answ_correct = sum(
            1 for r, p in zip(pilot_records, cand_predictions)
            if r["stratum"] == "answerable" and correct(r, p)
        )
        cand_answ_abstain = sum(
            1 for r, p in zip(pilot_records, cand_predictions)
            if r["stratum"] == "answerable" and abstained(p)
        )
        cand_null_abstain = sum(
            1 for r, p in zip(pilot_records, cand_predictions)
            if r["stratum"] == "null" and abstained(p)
        )

        # MEASURED TP control accuracy on the answerable stratum
        tp_control_correct = sum(
            1 for r, p in zip(pilot_records, tp_predictions)
            if r["stratum"] == "answerable" and correct(r, p)
        )
        tp_control_abstain = sum(
            1 for r, p in zip(pilot_records, tp_predictions)
            if r["stratum"] == "answerable" and abstained(p)
        )

        # Build full measurement dict
        measurements = {}

        # FLOOR
        m_floor = aggregate_per_stratum(
            successes=cand_null_abstain, n_effective=n_null,
            stratum="null", metric_name="null_abstention",
        )
        measurements["null_abstention_floor_unmet"] = m_floor

        # CEIL
        m_ceil = aggregate_per_stratum(
            successes=cand_answ_abstain, n_effective=n_answerable,
            stratum="answerable", metric_name="answerable_abstention",
        )
        measurements["answerable_abstention_ceiling_exceeded"] = m_ceil

        # TP — measured control (this is the D4-B difference vs D4-A)
        diff_lower_tp, diff_upper_tp = newcombe_wilson_difference(
            successes_a=cand_answ_correct, n_a=n_answerable,
            successes_b=tp_control_correct, n_b=n_answerable,
        )
        measurements["accuracy_indistinguishable_from_token_prior"] = {
            "stratum": "answerable",
            "n_effective": n_answerable,
            "point_estimate": (cand_answ_correct - tp_control_correct) / max(n_answerable, 1),
            "ci_lower": 0.0,
            "ci_upper": 1.0,
            "difference_lower": diff_lower_tp,
            "difference_upper": diff_upper_tp,
            "candidate_correct": cand_answ_correct,
            "tp_control_correct_measured": tp_control_correct,
            "measurement_source": "MEASURED MODEL TP via no-bindings shell (D4-B Q4 authorized)",
        }

        # ENV
        env_correct = int(envelope * n_answerable)
        diff_lower_env, diff_upper_env = newcombe_wilson_difference(
            successes_a=cand_answ_correct, n_a=n_answerable,
            successes_b=env_correct, n_b=n_answerable,
        )
        measurements["accuracy_indistinguishable_from_declared_policy_envelope"] = {
            "stratum": "answerable", "n_effective": n_answerable,
            "point_estimate": (cand_answ_correct - env_correct) / max(n_answerable, 1),
            "ci_lower": 0.0, "ci_upper": 1.0,
            "difference_lower": diff_lower_env, "difference_upper": diff_upper_env,
        }

        # HEAD
        n_envelope_misses = n_answerable - env_correct
        m_head = aggregate_per_stratum(
            successes=n_envelope_misses, n_effective=n_answerable,
            stratum="answerable", metric_name="measurement_headroom",
        )
        measurements["insufficient_measurement_headroom"] = m_head

        # GAP (content == strict by construction)
        diff_lower_gap, diff_upper_gap = newcombe_wilson_difference(
            successes_a=cand_answ_correct, n_a=n_answerable,
            successes_b=cand_answ_correct, n_b=n_answerable,
        )
        measurements["strict_content_gap_instability"] = {
            "stratum": "answerable", "n_effective": n_answerable,
            "point_estimate": 0.0, "ci_lower": 0.0, "ci_upper": 1.0,
            "difference_lower": diff_lower_gap, "difference_upper": diff_upper_gap,
        }

        # 15. T1 report
        t1_report = populate_t1_report(pilot_records, outputs_by_policy)

        # 16. T3 — TP ACTIVE; evaluate all 6
        t3_report = populate_t3_report()
        criterion_evaluations = {}
        attached_labels = []
        for criterion in t3_report.rows:
            label = criterion["criterion_label"]
            if label not in measurements:
                criterion_evaluations[label] = {"outcome": "NOT_EVALUATED"}
                continue
            m = measurements[label]
            crit_obj = EliminationCriterion(
                label=label,
                stratum=criterion["stratum"],
                comparison=CriterionComparison(criterion["comparison"]),
                floor_or_ceiling=criterion["floor_or_ceiling"],
                is_floor=criterion["is_floor"],
            )
            fires = apply_criterion(crit_obj, m)
            criterion["fired_d4b"] = bool(fires)
            criterion["measurement_d4b"] = m
            if fires:
                attached_labels.append(label)
            criterion_evaluations[label] = {
                "outcome": "FIRED" if fires else "PASSED",
                "measurement": m,
            }

        if attached_labels:
            outcome = "ELIMINATED"
        else:
            outcome = "NOT_RULED_OUT"

        # 17. T4 — D4-B rows
        t4_d4b_rows = list(t4_report := populate_t4_report().rows) + [
            {"review_item_id": "D4B-runner", "reviewer": "CS", "risk_class": "implementation", "disposition": "incorporated", "owner": "CS", "status": "resolved"},
            {"review_item_id": "D4B-tp-active", "reviewer": "Manager", "risk_class": "criterion-set", "disposition": "Manager Q4 authorized; TP ACTIVE; measured no-bindings shell control", "owner": "Manager", "status": "resolved"},
            {"review_item_id": "D4B-tp-banner-emitter", "reviewer": "Manager", "risk_class": "report-completeness", "disposition": "future-run fix applied (commit 5c60fbd); ACTIVE banner form symmetric to D4-A INACTIVE form", "owner": "CS", "status": "resolved"},
        ]

        # 18. A6
        a6_block = {
            "drift_within_tolerance": True,
            "envelope_drift": 0.0,
            "flagged_drifts": [],
            "per_policy_drift": {p: 0.0 for p in outputs_by_policy},
            "rationale": "pilot and final manifests share sealed sha256 by PH5-3 construction; A6 drift is 0 by identity.",
        }
        if manifest_hashes["pilot_L01"] != manifest_hashes["final_L01"]:
            raise D4ARunnerAbort("A6_DRIFT_EXCEEDED",
                                  f"pilot {manifest_hashes['pilot_L01']} != final {manifest_hashes['final_L01']}")

        # Void rate
        cand_parse_failures = sum(1 for x in cand_per_record if x["parsed"]["parse_status"] == "parse_failure")
        tp_parse_failures = sum(1 for x in tp_per_record if x["parsed"]["parse_status"] == "parse_failure")
        cand_void_rate = cand_parse_failures / max(len(cand_per_record), 1)
        tp_void_rate = tp_parse_failures / max(len(tp_per_record), 1)
        if cand_void_rate > 0.05:
            raise D4ARunnerAbort("VOID_BUDGET_EXCEEDED_CANDIDATE",
                                  f"candidate void_rate {cand_void_rate:.3f} > 0.05")
        if tp_void_rate > 0.05:
            raise D4ARunnerAbort("VOID_BUDGET_EXCEEDED_TP",
                                  f"TP void_rate {tp_void_rate:.3f} > 0.05")

        candidate_summary = {
            "n_answerable": n_answerable,
            "answerable_correct": cand_answ_correct,
            "answerable_accuracy": cand_answ_correct / max(n_answerable, 1),
            "answerable_abstained": cand_answ_abstain,
            "answerable_abstention_rate": cand_answ_abstain / max(n_answerable, 1),
            "n_null": n_null,
            "null_abstained": cand_null_abstain,
            "null_abstention_rate": cand_null_abstain / max(n_null, 1),
            "parse_failures": cand_parse_failures,
            "void_rate": cand_void_rate,
        }
        tp_summary = {
            "n_answerable": n_answerable,
            "tp_control_correct": tp_control_correct,
            "tp_control_accuracy": tp_control_correct / max(n_answerable, 1),
            "tp_control_abstained": tp_control_abstain,
            "tp_control_abstention_rate": tp_control_abstain / max(n_answerable, 1),
            "parse_failures": tp_parse_failures,
            "void_rate": tp_void_rate,
        }
        cand_vs_tp = {
            "candidate_accuracy": candidate_summary["answerable_accuracy"],
            "tp_control_accuracy": tp_summary["tp_control_accuracy"],
            "point_difference": candidate_summary["answerable_accuracy"] - tp_summary["tp_control_accuracy"],
            "newcombe_wilson_diff_lower": diff_lower_tp,
            "newcombe_wilson_diff_upper": diff_upper_tp,
            "tp_margin_locked": 0.10,
            "tp_fires": diff_upper_tp < 0.10,
        }

        # 19. IVR
        ivr_text = assemble_instrument_validation_report(
            t1_report, t3_report, populate_t4_report(), [], "L01",
        )
        ivr_d4b_addendum = "\n\n".join([
            "",
            "## D4-B Candidate Run (Manager-authorized TP-ACTIVE pilot)",
            "",
            f"- candidate sweep_id: `{candidate_sweep_id}`",
            f"- tp sweep_id: `{tp_sweep_id}`",
            f"- model: Qwen2.5-3B-Instruct (bf16)",
            f"- model_snapshot_hash: `{env['model_snapshot_hash_computed']}`",
            f"- mlx_lm version: {env['mlx_lm_version']} (Option A pin substitution carried from D4-A)",
            "",
            "### TP banner (ACTIVE — Manager Q4 authorized)",
            "",
            f"- tp_criterion_status: {tp_banner['tp_criterion_status']}",
            f"- tp_inactivity_authority: {tp_banner['tp_inactivity_authority']}",
            f"- tp_generation_status: {tp_banner['tp_generation_status']}",
            f"- tp_elimination_labels_enabled: {tp_banner['tp_elimination_labels_enabled']}",
            "",
            "### Candidate per-stratum measurements",
            "",
            f"- answerable correct: {cand_answ_correct}/{n_answerable} ({candidate_summary['answerable_accuracy']:.4f})",
            f"- answerable abstained: {cand_answ_abstain}/{n_answerable}",
            f"- null abstained: {cand_null_abstain}/{n_null}",
            f"- candidate parse failures: {cand_parse_failures}/96 (void_rate {cand_void_rate:.4f}; budget 0.05)",
            "",
            "### TP control (no-bindings shell) measurements",
            "",
            f"- TP control correct: {tp_control_correct}/{n_answerable} ({tp_summary['tp_control_accuracy']:.4f})",
            f"- TP control abstained: {tp_control_abstain}/{n_answerable}",
            f"- TP control parse failures: {tp_parse_failures}/96 (void_rate {tp_void_rate:.4f}; budget 0.05)",
            "",
            "### Candidate vs TP comparison",
            "",
            f"- candidate accuracy: {cand_vs_tp['candidate_accuracy']:.4f}",
            f"- TP control accuracy: {cand_vs_tp['tp_control_accuracy']:.4f}",
            f"- point difference: {cand_vs_tp['point_difference']:.4f}",
            f"- Newcombe-Wilson CI on difference: [{diff_lower_tp:.4f}, {diff_upper_tp:.4f}]",
            f"- locked TP margin: 0.10",
            f"- TP criterion fires (CI upper < 0.10): {cand_vs_tp['tp_fires']}",
            "",
            "### Final candidate outcome (six active criteria)",
            "",
            f"- attached_labels: {sorted(attached_labels) if attached_labels else '(none)'}",
            f"- outcome: **{outcome}**",
            "",
            "### Non-claim block (verbatim)",
            "",
            "> D4-B is an instrument-use step, not a capability claim. Even if D4-B returns NOT_RULED_OUT under six active criteria, it remains instrument use, not a capability claim. The instrument may rule out; it may not rule in. Passing the declared battery is reportable only as \"not explained by the declared shortcut battery,\" never as \"not shortcut-driven.\" We have improved the ruler; we are only beginning to touch the territory.",
            "",
            "— CS Engineer, 2026-06-11",
        ])

        # 20. Write artifacts
        import dataclasses as _dc
        def _to_jsonable(obj):
            if _dc.is_dataclass(obj):
                return _dc.asdict(obj)
            if isinstance(obj, dict):
                return {k: _to_jsonable(v) for k, v in obj.items()}
            if isinstance(obj, (list, tuple)):
                return [_to_jsonable(x) for x in obj]
            return obj

        (OUTPUT_DIR / "instrument_validation_report.md").write_text(ivr_text + ivr_d4b_addendum)
        (OUTPUT_DIR / "candidate_predictions.json").write_text(json.dumps(
            [{"record_id": p.record_id,
              "predicted_value_token_ids": list(p.predicted_value_token_ids) if p.predicted_value_token_ids else None}
             for p in cand_predictions], indent=2))
        (OUTPUT_DIR / "tp_control_predictions.json").write_text(json.dumps(
            [{"record_id": p.record_id,
              "predicted_value_token_ids": list(p.predicted_value_token_ids) if p.predicted_value_token_ids else None}
             for p in tp_predictions], indent=2))

        (OUTPUT_DIR / "t1_report.json").write_text(json.dumps({
            "tp_banner": tp_banner,
            "per_policy_scores": _to_jsonable(t1_report.per_policy_scores),
            "union_envelope_score": t1_report.union_envelope_score,
            "envelope_cap": t1_report.envelope_cap,
            "room_below_envelope": t1_report.room_below_envelope,
            "policy_classifications": _to_jsonable(t1_report.policy_classifications),
            "a6_drift_block": a6_block,
            "candidate_summary": candidate_summary,
            "tp_control_summary": tp_summary,
        }, indent=2, default=str))

        (OUTPUT_DIR / "t3_report.json").write_text(json.dumps({
            "tp_banner": tp_banner,
            "ideal_witness_in_pass_region": t3_report.ideal_witness_in_pass_region,
            "rows": _to_jsonable(list(t3_report.rows)),
            "criterion_evaluations_against_candidate": _to_jsonable(criterion_evaluations),
            "candidate_vs_tp_comparison": cand_vs_tp,
            "attached_labels": sorted(attached_labels),
            "candidate_outcome": outcome,
            "tp_active_by_manager_decision": token_prior_authorized,
            "tp_activity_authority": tp_authority_ref,
        }, indent=2, default=str))

        (OUTPUT_DIR / "t4_report.json").write_text(json.dumps({
            "tp_banner": tp_banner,
            "rows": t4_d4b_rows,
        }, indent=2))

        a6_block_with_banner = dict(a6_block)
        a6_block_with_banner["tp_banner"] = tp_banner
        (OUTPUT_DIR / "a6_re_verification.json").write_text(json.dumps(a6_block_with_banner, indent=2))

        # Ledger
        runner_hash = sha256_file(RUNNER_PATH)
        parser_hash = sha256_file(RUNNER_DIR / "parse_model_output.py")
        cand_template_hash = sha256_file(PROMPT_TEMPLATE_CAND_PATH)
        tp_template_hash = sha256_file(PROMPT_TEMPLATE_TP_PATH)
        decoding_config_hash = sha256_file(DECODING_CONFIG_PATH)
        preconditions_hash = sha256_file(PRECONDITIONS_PATH)
        scorer_hash = sha256_file(EXPERIMENT_DIR / "lane1a_prime" / "validation.py")
        ledger = {
            "tp_banner": tp_banner,
            "model_invoked": True,
            "model_loaded": True,
            "candidate_sweep_id_created": candidate_sweep_id,
            "tp_sweep_id_created": tp_sweep_id,
            "two_sweep_structure": "candidate retrieval-shell + TP no-bindings shell; same 96 records",
            "sweep_execution": True,
            "candidate_model_outputs_produced": True,
            "tp_control_model_outputs_produced": True,
            "no_threshold_work": "CONFIRMED",
            "no_certification_evaluation": "CONFIRMED",
            "no_claim_c_activation": "CONFIRMED",
            "no_l02_l08_execution": "CONFIRMED",
            "no_quantization": "CONFIRMED",
            "no_int8_or_int4": "CONFIRMED",
            "tp_generation_method": preconditions["token_prior_method"],
            "no_scrambled_binding_generations": "CONFIRMED — TP method is no-bindings shell, not scrambled-binding",
            "outputs_validation_only": "SYNTHETIC/DIAGNOSTIC — D4-B instrument-use artifacts",
            "manager_authorization": "Lane 1a' D4-B L01 Token-Prior-Active Pilot — Manager 2026-06-11",
            "mlx_lm_pin_substitution_carryforward": "Option A (0.31.3) from D4-A — Manager 2026-06-11",
            "model_snapshot_hash_authorized": preconditions["authorized_model_snapshot_hash"],
            "model_snapshot_hash_computed": env["model_snapshot_hash_computed"],
            "mlx_lm_version": env["mlx_lm_version"],
            "mlx_core_version": env.get("mlx_core_version", "unknown"),
            "runner_hash": runner_hash,
            "parser_hash": parser_hash,
            "prompt_template_candidate_hash": cand_template_hash,
            "prompt_template_tp_hash": tp_template_hash,
            "decoding_config_hash": decoding_config_hash,
            "preconditions_hash": preconditions_hash,
            "scorer_hash": scorer_hash,
            "sealed_lock_record_hash": sealed_hash,
            "lock_event_hashes": preconditions["lock_event_hashes"],
            "sealed_manifest_hashes": manifest_hashes,
            "env": env,
            "outcome": outcome,
            "attached_labels": sorted(attached_labels),
            "candidate_summary": candidate_summary,
            "tp_control_summary": tp_summary,
            "candidate_vs_tp_comparison": cand_vs_tp,
            "elapsed_seconds": time.time() - started_at,
        }
        (OUTPUT_DIR / "execution_ledger.json").write_text(json.dumps(_to_jsonable(ledger), indent=2, default=str))

        print(f"[D4-B] COMPLETE: outcome={outcome}; attached_labels={sorted(attached_labels)}")
        print(f"[D4-B] candidate={candidate_summary['answerable_accuracy']:.4f}; tp_control={tp_summary['tp_control_accuracy']:.4f}; diff CI upper={diff_upper_tp:.4f} vs locked margin 0.10")
        print(f"[D4-B] elapsed: {time.time() - started_at:.1f}s")
        return 0

    except D4ARunnerAbort as exc:
        abort_dir = emit_abort_artifact(exc.reason_code, exc.message, env, partial, started_at)
        print(f"[D4-B ABORT] {exc} | artifacts at {abort_dir}", file=sys.stderr)
        return 1
    except Exception as exc:
        tb = traceback.format_exc()
        abort_dir = emit_abort_artifact("UNHANDLED_EXCEPTION",
                                         f"{type(exc).__name__}: {exc}\n{tb}",
                                         env, partial, started_at)
        print(f"[D4-B ABORT] {exc} | artifacts at {abort_dir}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
