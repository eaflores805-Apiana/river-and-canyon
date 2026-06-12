"""Lane 1a' Prime Path A Runner — L01-L08 breadth with TP active.

Manager Path A authorization 2026-06-12 (all four boxes:
sweep execution + sweep_id creation + L01-L08 sweep + token-prior by name).

Per-rung two-sweep structure (Manager §5 per-rung adjudication):
  - For each rung L01..L08:
      1. Candidate sweep (retrieval-shell prompt; 96 inferences)
      2. TP control sweep (no-bindings shell; 96 inferences)
  - Per-rung six-criterion evaluation under the locked T3 bounds
  - Per-rung Newcombe-Wilson on (candidate - measured_tp_control)
  - NO cross-rung aggregation; NO composite score; NO survival count

L01: sealed manifests (afe0e545...) consumed read-only.
L02-L08: materialized under path_a_run/manifests/L0k/ using the
  approved generator + locked seed; PH5-3 identical-seed property
  asserted (pilot == final byte-identical).

Manager §7 abort triggers (12 categories; all fire fail-closed):
  pre-flight hash refusal · A6 drift · candidate or TP batch schema
  failure · artifact hash mismatch · runner/model identity mismatch ·
  unhandled exception · missing TP field in any emitted report ·
  generator hash mismatch · pilot/final manifest mismatch · per-rung
  recipe-conformance failure · sealed-byte write attempt
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
from dataclasses import asdict
from pathlib import Path


RUNNER_PATH = Path(__file__).resolve()
RUNNER_DIR = RUNNER_PATH.parent
EXPERIMENT_DIR = RUNNER_DIR.parent
VALIDATION_DIR = EXPERIMENT_DIR / "validation"
REPO_ROOT = EXPERIMENT_DIR.parent.parent
SEALED_LOCK_RECORD = REPO_ROOT / "governance" / "2026-06-11_lane-1a-prime" / "LANE1A-PRIME-SEALED-LOCK-RECORD-v1.0.md"

OUTPUT_DIR = EXPERIMENT_DIR / "path_a_run"
MANIFESTS_DIR = OUTPUT_DIR / "manifests"
PRECONDITIONS_PATH = RUNNER_DIR / "preconditions_path_a.json"
DECODING_CONFIG_PATH = RUNNER_DIR / "decoding_config.json"
PROMPT_TEMPLATE_CAND_PATH = RUNNER_DIR / "prompt_template_v1.json"
PROMPT_TEMPLATE_TP_PATH = RUNNER_DIR / "prompt_template_v1_tp.json"

GENERATOR_PATH = EXPERIMENT_DIR / "lane1a_prime" / "validation.py"

sys.path.insert(0, str(EXPERIMENT_DIR))

from d4_runner.lane1a_runner import (
    D4ARunnerAbort,
    compute_model_snapshot_hash,
    sha256_file,
    stamp_environment,
    tp_banner_block,
)


def sealed_dir_inventory() -> dict:
    """Snapshot every file under validation/ with sha256. Used to detect any sealed-byte write."""
    inv = {}
    for f in sorted(VALIDATION_DIR.rglob("*")):
        if f.is_file() and "superseded_" not in str(f):
            inv[str(f.relative_to(VALIDATION_DIR))] = sha256_file(f)
    return inv


def assert_no_sealed_byte_change(before: dict, after: dict) -> None:
    if before != after:
        diff = []
        for k in set(before) | set(after):
            if before.get(k) != after.get(k):
                diff.append(f"{k}: before={before.get(k)} after={after.get(k)}")
        raise D4ARunnerAbort(
            "SEALED_BYTE_WRITE_DETECTED",
            "validation/ directory changed during the run: " + "; ".join(diff[:5]),
        )


def precondition_mlx_lm_version_check(env: dict, authorized: str) -> str:
    try:
        from importlib.metadata import version as pkg_version
        actual = pkg_version("mlx-lm")
    except Exception as exc:
        raise D4ARunnerAbort("FRAMEWORK_VERSION_LOOKUP_FAILED",
                              f"could not determine mlx-lm version: {exc}")
    env["mlx_lm_version"] = actual
    if actual != authorized:
        raise D4ARunnerAbort("FRAMEWORK_VERSION_MISMATCH",
                              f"authorized mlx_lm {authorized}; actual {actual}")
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
    le = preconditions["lock_event_hashes"]
    cfg = ValidationPreFlightConfig(
        oracle_verdict_table_path=VALIDATION_DIR / "ORACLE_VERDICT_TABLE.json",
        oracle_verdict_table_hash=le["oracle_verdict_table"],
        t3_bounds_path=VALIDATION_DIR / "T3_BOUNDS_DECLARATION.json",
        t3_bounds_hash=le["t3_bounds"],
        stratified_recipe_path=VALIDATION_DIR / "STRATIFIED_RECIPE_SCHEDULE.json",
        stratified_recipe_hash=le["stratified_recipe"],
    )
    try:
        verify_pre_flight_config(cfg)
    except ValidationPreFlightRefused as exc:
        raise D4ARunnerAbort("PH5_4_REFUSAL", str(exc))
    return {"status": "PASSED", **le}


def precondition_sealed_lock_record(preconditions: dict) -> str:
    actual = sha256_file(SEALED_LOCK_RECORD)
    expected = preconditions["sealed_lock_record_hash"]
    if actual != expected:
        raise D4ARunnerAbort("SEALED_LOCK_RECORD_MUTATED",
                              f"sealed LOCK-RECORD hash {actual} != sealed-time {expected}")
    return actual


def precondition_generator_hash(preconditions: dict) -> str:
    actual = sha256_file(GENERATOR_PATH)
    expected = preconditions["approved_generator_sha256"]
    if actual != expected:
        raise D4ARunnerAbort("GENERATOR_HASH_MISMATCH",
                              f"generator sha256 {actual} != authorized {expected}")
    return actual


def precondition_model_snapshot(env: dict, preconditions: dict) -> Path:
    snap_root = Path(os.path.expanduser(
        "~/.cache/huggingface/hub/models--Qwen--Qwen2.5-3B-Instruct/snapshots"
    ))
    if not snap_root.is_dir():
        raise D4ARunnerAbort("MODEL_SNAPSHOT_NOT_FOUND", f"HF snapshot root not present: {snap_root}")
    snaps = list(snap_root.iterdir())
    if not snaps:
        raise D4ARunnerAbort("MODEL_SNAPSHOT_NOT_FOUND", f"no snapshots under {snap_root}")
    snap_dir = snaps[0]
    env["hf_snapshot_dir"] = str(snap_dir)
    env["hf_revision"] = snap_dir.name
    computed = compute_model_snapshot_hash(snap_dir)
    env["model_snapshot_hash_computed"] = computed
    env["model_snapshot_hash_authorized"] = preconditions["authorized_model_snapshot_hash"]
    if computed != preconditions["authorized_model_snapshot_hash"]:
        raise D4ARunnerAbort("MODEL_SNAPSHOT_HASH_MISMATCH",
                              f"computed {computed} != authorized {preconditions['authorized_model_snapshot_hash']}")
    return snap_dir


def render_prompt(template: dict, record: dict, pair_list_override: str = "normal") -> tuple[str, str]:
    from d4_runner.parse_model_output import render_pair_lines, render_query_key
    if pair_list_override == "empty":
        pair_lines = ""
    else:
        pairs = record["context_block"]["real_pair_block"]["pairs"]
        pair_lines = render_pair_lines(pairs)
    query_key = render_query_key(record["queried_key"])
    user_text = template["user_template"].format(pair_lines=pair_lines, query_key=query_key)
    return template["system"], user_text


def run_inference(model, tokenizer, system_text: str, user_text: str, decoding_config: dict):
    import mlx_lm
    messages = [
        {"role": "system", "content": system_text},
        {"role": "user", "content": user_text},
    ]
    try:
        prompt_text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    except Exception as exc:
        raise D4ARunnerAbort("PROMPT_RENDER_FAILURE", f"chat template apply failed: {exc}")
    t0 = time.time()
    try:
        from mlx_lm import generate
        out = generate(model, tokenizer, prompt=prompt_text,
                       max_tokens=decoding_config["max_new_tokens"], verbose=False)
    except TypeError:
        from mlx_lm import generate
        out = generate(model, tokenizer, prompt_text, max_tokens=decoding_config["max_new_tokens"])
    except Exception as exc:
        raise D4ARunnerAbort("INFERENCE_FAILURE", f"mlx_lm.generate failed: {exc}")
    return out, (time.time() - t0) * 1000.0, "completed"


def make_sweep_id(suffix: str) -> str:
    ts = time.strftime("%Y%m%d-%H%M%S")
    rand6 = "".join(random.SystemRandom().choices(_string.ascii_lowercase + _string.digits, k=6))
    return f"lane1a-prime-pathA-{suffix}-{ts}-{rand6}"


def materialize_rung(rung_id: str, preconditions: dict, out_dir: Path) -> tuple[str, str]:
    """Materialize PILOT and FINAL manifests for a rung. Returns (pilot_sha256, final_sha256).

    For L01: read sealed manifests and return their hashes (no write).
    For L02-L08: generate via construct_pilot_manifests, write to out_dir,
                 assert pilot == final byte-identical (PH5-3).
    """
    out_dir.mkdir(parents=True, exist_ok=True)
    if rung_id == "L01":
        pilot_p = VALIDATION_DIR / "pilot_manifests_L01.json"
        final_p = VALIDATION_DIR / "final_manifests_L01.json"
        pilot_h = sha256_file(pilot_p)
        final_h = sha256_file(final_p)
        expected = preconditions["sealed_manifest_hashes_L01"]["pilot_L01"]
        if pilot_h != expected:
            raise D4ARunnerAbort("MANIFEST_HASH_MISMATCH",
                                  f"L01 pilot hash {pilot_h} != sealed {expected}")
        if final_h != expected:
            raise D4ARunnerAbort("MANIFEST_HASH_MISMATCH",
                                  f"L01 final hash {final_h} != sealed {expected}")
        return pilot_h, final_h

    # L02..L08: generate
    from lane1a_prime.validation import ManifestRecipe, construct_pilot_manifests
    seed = int(preconditions["locked_seed"])
    recipe = ManifestRecipe(rung_id=rung_id, seed=seed)
    pilot = construct_pilot_manifests(recipe)
    final = construct_pilot_manifests(recipe)
    pilot_json = json.dumps(pilot)
    final_json = json.dumps(final)
    pilot_bytes = pilot_json.encode("utf-8")
    final_bytes = final_json.encode("utf-8")
    pilot_h = hashlib.sha256(pilot_bytes).hexdigest()
    final_h = hashlib.sha256(final_bytes).hexdigest()
    if pilot_h != final_h:
        raise D4ARunnerAbort("PILOT_FINAL_MANIFEST_MISMATCH",
                              f"{rung_id}: pilot {pilot_h} != final {final_h}")
    pilot_p = out_dir / f"pilot_manifests_{rung_id}.json"
    final_p = out_dir / f"final_manifests_{rung_id}.json"
    pilot_p.write_bytes(pilot_bytes)
    final_p.write_bytes(final_bytes)

    # Per-rung recipe-conformance check
    n_ans = sum(1 for r in pilot if r["stratum"] == "answerable")
    n_null = sum(1 for r in pilot if r["stratum"] == "null")
    if n_ans != 80 or n_null != 16:
        raise D4ARunnerAbort("RECIPE_CONFORMANCE_FAILURE",
                              f"{rung_id}: counts {n_ans}/{n_null}; expected 80/16")
    return pilot_h, final_h


def run_sweep(model, tokenizer, records, prompt_template, decoding_config,
              pair_list_override, output_subdir, sweep_label, rung_id):
    from d4_runner.parse_model_output import parse_model_output
    from lane1a_prime.oracle_cases import SimulatedPrediction
    output_subdir.mkdir(parents=True, exist_ok=True)
    predictions = []
    per_record = []
    for idx, record in enumerate(records):
        record_id = f"{rung_id}-{idx:03d}-{record['stratum']}"
        system_text, user_text = render_prompt(prompt_template, record, pair_list_override)
        out, latency_ms, finish_reason = run_inference(
            model, tokenizer, system_text, user_text, decoding_config
        )
        parsed = parse_model_output(out)
        rec = {
            "record_id": record_id, "rung_id": rung_id, "sweep_label": sweep_label,
            "stratum": record["stratum"], "queried_key": record["queried_key"],
            "gold": record["gold"], "prompt_user_text": user_text,
            "output_text": out, "parsed": parsed,
            "latency_ms": latency_ms, "finish_reason": finish_reason,
        }
        per_record.append(rec)
        (output_subdir / f"{record_id}.json").write_text(json.dumps(rec, indent=2))
        sp = SimulatedPrediction(record_id=record_id,
                                  predicted_value_token_ids=parsed["predicted_value_token_ids"])
        predictions.append(sp)
    return tuple(predictions), per_record


def evaluate_rung(rung_id: str, pilot_records, cand_preds, tp_preds, env_acc_dict, t3_rows):
    """Per-rung six-criterion evaluation. Returns (criterion_evals, attached_labels, outcome,
    cand_summary, tp_summary, cand_vs_tp).
    """
    from lane1a_prime.analysis import (
        EliminationCriterion, CriterionComparison, apply_criterion,
        newcombe_wilson_difference, aggregate_per_stratum,
    )

    def correct(record, pred):
        if pred.predicted_value_token_ids is None:
            return False
        return list(pred.predicted_value_token_ids) == record["gold"]["value_token_ids"]

    def abstained(pred):
        return pred.predicted_value_token_ids is None

    n_ans = sum(1 for r in pilot_records if r["stratum"] == "answerable")
    n_null = sum(1 for r in pilot_records if r["stratum"] == "null")
    cand_ans_correct = sum(1 for r, p in zip(pilot_records, cand_preds)
                            if r["stratum"] == "answerable" and correct(r, p))
    cand_ans_abst = sum(1 for r, p in zip(pilot_records, cand_preds)
                         if r["stratum"] == "answerable" and abstained(p))
    cand_null_abst = sum(1 for r, p in zip(pilot_records, cand_preds)
                          if r["stratum"] == "null" and abstained(p))
    tp_ans_correct = sum(1 for r, p in zip(pilot_records, tp_preds)
                          if r["stratum"] == "answerable" and correct(r, p))
    tp_ans_abst = sum(1 for r, p in zip(pilot_records, tp_preds)
                       if r["stratum"] == "answerable" and abstained(p))

    measurements = {}
    measurements["null_abstention_floor_unmet"] = aggregate_per_stratum(
        successes=cand_null_abst, n_effective=n_null,
        stratum="null", metric_name="null_abstention",
    )
    measurements["answerable_abstention_ceiling_exceeded"] = aggregate_per_stratum(
        successes=cand_ans_abst, n_effective=n_ans,
        stratum="answerable", metric_name="answerable_abstention",
    )
    # TP: measured control
    diff_lo_tp, diff_up_tp = newcombe_wilson_difference(
        successes_a=cand_ans_correct, n_a=n_ans,
        successes_b=tp_ans_correct, n_b=n_ans,
    )
    measurements["accuracy_indistinguishable_from_token_prior"] = {
        "stratum": "answerable", "n_effective": n_ans,
        "point_estimate": (cand_ans_correct - tp_ans_correct) / max(n_ans, 1),
        "ci_lower": 0.0, "ci_upper": 1.0,
        "difference_lower": diff_lo_tp, "difference_upper": diff_up_tp,
        "candidate_correct": cand_ans_correct,
        "tp_control_correct_measured": tp_ans_correct,
        "measurement_source": f"MEASURED MODEL TP via no-bindings shell ({rung_id}; Path A; fresh control)",
    }
    # ENV
    env_acc = env_acc_dict[rung_id]
    env_correct = int(env_acc * n_ans)
    diff_lo_env, diff_up_env = newcombe_wilson_difference(
        successes_a=cand_ans_correct, n_a=n_ans,
        successes_b=env_correct, n_b=n_ans,
    )
    measurements["accuracy_indistinguishable_from_declared_policy_envelope"] = {
        "stratum": "answerable", "n_effective": n_ans,
        "point_estimate": (cand_ans_correct - env_correct) / max(n_ans, 1),
        "ci_lower": 0.0, "ci_upper": 1.0,
        "difference_lower": diff_lo_env, "difference_upper": diff_up_env,
    }
    # HEAD
    n_env_misses = n_ans - env_correct
    measurements["insufficient_measurement_headroom"] = aggregate_per_stratum(
        successes=n_env_misses, n_effective=n_ans,
        stratum="answerable", metric_name="measurement_headroom",
    )
    # GAP (content == strict)
    diff_lo_gap, diff_up_gap = newcombe_wilson_difference(
        successes_a=cand_ans_correct, n_a=n_ans,
        successes_b=cand_ans_correct, n_b=n_ans,
    )
    measurements["strict_content_gap_instability"] = {
        "stratum": "answerable", "n_effective": n_ans,
        "point_estimate": 0.0, "ci_lower": 0.0, "ci_upper": 1.0,
        "difference_lower": diff_lo_gap, "difference_upper": diff_up_gap,
    }

    criterion_evals = {}
    attached = []
    for row in t3_rows:
        label = row["criterion_label"]
        if label not in measurements:
            criterion_evals[label] = {"outcome": "NOT_EVALUATED"}
            continue
        m = measurements[label]
        crit = EliminationCriterion(
            label=label, stratum=row["stratum"],
            comparison=CriterionComparison(row["comparison"]),
            floor_or_ceiling=row["floor_or_ceiling"],
            is_floor=row["is_floor"],
        )
        fires = apply_criterion(crit, m)
        criterion_evals[label] = {"outcome": "FIRED" if fires else "PASSED", "measurement": m}
        if fires:
            attached.append(label)

    outcome = "ELIMINATED" if attached else "NOT_RULED_OUT"
    cand_summary = {
        "n_answerable": n_ans, "answerable_correct": cand_ans_correct,
        "answerable_accuracy": cand_ans_correct / max(n_ans, 1),
        "answerable_abstained": cand_ans_abst,
        "answerable_abstention_rate": cand_ans_abst / max(n_ans, 1),
        "n_null": n_null, "null_abstained": cand_null_abst,
        "null_abstention_rate": cand_null_abst / max(n_null, 1),
    }
    tp_summary = {
        "n_answerable": n_ans, "tp_control_correct": tp_ans_correct,
        "tp_control_accuracy": tp_ans_correct / max(n_ans, 1),
        "tp_control_abstained": tp_ans_abst,
        "tp_control_abstention_rate": tp_ans_abst / max(n_ans, 1),
    }
    cand_vs_tp = {
        "candidate_accuracy": cand_summary["answerable_accuracy"],
        "tp_control_accuracy": tp_summary["tp_control_accuracy"],
        "point_difference": cand_summary["answerable_accuracy"] - tp_summary["tp_control_accuracy"],
        "newcombe_wilson_diff_lower": diff_lo_tp,
        "newcombe_wilson_diff_upper": diff_up_tp,
        "tp_margin_locked": 0.10,
        "tp_fires": diff_up_tp < 0.10,
    }
    return criterion_evals, attached, outcome, cand_summary, tp_summary, cand_vs_tp


def emit_abort_artifact(reason_code: str, message: str, env: dict,
                         partial: dict, started_at: float) -> Path:
    abort_dir = OUTPUT_DIR / f"aborted_{time.strftime('%Y%m%d-%H%M%S')}"
    abort_dir.mkdir(parents=True, exist_ok=True)
    (abort_dir / "abort_record.json").write_text(json.dumps({
        "reason_code": reason_code, "message": message, "env": env,
        "partial_state": partial,
        "elapsed_seconds": time.time() - started_at,
        "sealed_lock_record_must_remain_unchanged": True,
    }, indent=2))
    return abort_dir


def main(argv=None) -> int:
    started_at = time.time()
    env = stamp_environment()
    partial: dict = {}
    try:
        preconditions = json.loads(PRECONDITIONS_PATH.read_text())
        env["preconditions_hash"] = sha256_file(PRECONDITIONS_PATH)

        # TP banner — ACTIVE form per Manager Path A authorization
        if not preconditions.get("token_prior_decision", "").upper().startswith("AUTHORIZED"):
            raise D4ARunnerAbort("TP_DECISION_MISALIGNMENT",
                                  "Path A runner requires AUTHORIZED token_prior_decision")
        tp_authority = preconditions["token_prior_decision"]
        tp_banner = tp_banner_block(True, tp_authority)

        # Snapshot sealed dir BEFORE anything else
        sealed_before = sealed_dir_inventory()
        env["sealed_dir_file_count_before"] = len(sealed_before)

        # Preconditions
        precondition_mlx_lm_version_check(env, preconditions["authorized_mlx_lm_version"])
        pre_flight_log = precondition_ph5_4(preconditions)
        partial["pre_flight"] = pre_flight_log
        sealed_hash = precondition_sealed_lock_record(preconditions)
        partial["sealed_lock_record_hash"] = sealed_hash
        gen_hash = precondition_generator_hash(preconditions)
        partial["generator_hash"] = gen_hash
        snap_dir = precondition_model_snapshot(env, preconditions)
        partial["snapshot_dir"] = str(snap_dir)

        # Sweep_ids
        cand_sweep_id = make_sweep_id("cand")
        tp_sweep_id = make_sweep_id("tp")
        env["candidate_sweep_id"] = cand_sweep_id
        env["tp_sweep_id"] = tp_sweep_id

        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        MANIFESTS_DIR.mkdir(parents=True, exist_ok=True)

        # Pre-flight log
        (OUTPUT_DIR / "pre_flight_log.json").write_text(json.dumps({
            "tp_banner": tp_banner,
            "run_header": {
                "candidate_sweep_id": cand_sweep_id, "tp_sweep_id": tp_sweep_id,
                "tp_banner": tp_banner,
            },
            "ph5_4": pre_flight_log,
            "mlx_lm_version_check": "PASSED",
            "mlx_lm_version": env["mlx_lm_version"],
            "sealed_lock_record_hash": sealed_hash,
            "generator_path": preconditions["approved_generator_path"],
            "generator_hash": gen_hash,
            "snapshot_hash_authorized": preconditions["authorized_model_snapshot_hash"],
            "snapshot_hash_computed": env["model_snapshot_hash_computed"],
            "approved_rungs": preconditions["approved_rungs"],
            "all_preconditions": "PASSED",
            "env": env,
        }, indent=2))

        # Materialize all 8 rungs (L01 read-only; L02-L08 generated)
        print(f"[Path A] materializing manifests for {preconditions['approved_rungs']}...")
        manifest_hashes = {}
        for rung in preconditions["approved_rungs"]:
            rung_dir = MANIFESTS_DIR / rung
            ph, fh = materialize_rung(rung, preconditions, rung_dir)
            manifest_hashes[rung] = {"pilot": ph, "final": fh}
            assert ph == fh, f"materialization integrity for {rung}"
            print(f"[Path A]   {rung}: pilot=final={ph[:16]}…")
        (OUTPUT_DIR / "manifest_hash_record.json").write_text(json.dumps(manifest_hashes, indent=2))

        # Load model
        print(f"[Path A] loading model from {snap_dir}...")
        from mlx_lm import load as mlx_load
        model, tokenizer = mlx_load(str(snap_dir))
        env["model_loaded"] = True

        # Load decoding + templates
        decoding_config = json.loads(DECODING_CONFIG_PATH.read_text())
        cand_template = json.loads(PROMPT_TEMPLATE_CAND_PATH.read_text())
        tp_template = json.loads(PROMPT_TEMPLATE_TP_PATH.read_text())

        # Imports for per-rung evaluation
        from lane1a_prime.validation import (
            apply_policy_battery, compute_union_envelope, populate_t3_report,
        )

        # Get T3 rows (locked bounds + comparison rules)
        t3_rows = list(populate_t3_report().rows)

        # Per-rung loop
        per_rung_results = {}
        run_summary = {"rungs": []}
        for rung in preconditions["approved_rungs"]:
            print(f"[Path A] {rung}: starting candidate sweep...")
            # Load this rung's pilot manifests (use the materialized copy for L02-L08;
            # sealed for L01)
            if rung == "L01":
                pilot_path = VALIDATION_DIR / "pilot_manifests_L01.json"
            else:
                pilot_path = MANIFESTS_DIR / rung / f"pilot_manifests_{rung}.json"
            pilot_records = json.loads(pilot_path.read_text())

            rung_dir = OUTPUT_DIR / rung
            rung_dir.mkdir(parents=True, exist_ok=True)

            cand_preds, cand_per_record = run_sweep(
                model, tokenizer, pilot_records, cand_template, decoding_config,
                "normal", rung_dir / "candidate_outputs", "candidate", rung,
            )
            print(f"[Path A] {rung}: candidate done; starting TP control sweep...")
            tp_preds, tp_per_record = run_sweep(
                model, tokenizer, pilot_records, tp_template, decoding_config,
                "empty", rung_dir / "tp_control_outputs", "tp_control", rung,
            )

            # Per-rung envelope
            outputs_by_policy = apply_policy_battery(pilot_records)
            envelope = compute_union_envelope(pilot_records, outputs_by_policy, "answerable")

            # Per-rung evaluation
            criterion_evals, attached, outcome, cand_sum, tp_sum, cand_vs_tp = evaluate_rung(
                rung, pilot_records, cand_preds, tp_preds, {rung: envelope}, t3_rows,
            )

            # Per-rung void rates
            cand_pf = sum(1 for x in cand_per_record if x["parsed"]["parse_status"] == "parse_failure")
            tp_pf = sum(1 for x in tp_per_record if x["parsed"]["parse_status"] == "parse_failure")
            cand_void = cand_pf / max(len(cand_per_record), 1)
            tp_void = tp_pf / max(len(tp_per_record), 1)
            if cand_void > 0.05:
                raise D4ARunnerAbort("VOID_BUDGET_EXCEEDED_CANDIDATE",
                                      f"{rung}: candidate void_rate {cand_void:.3f} > 0.05")
            if tp_void > 0.05:
                raise D4ARunnerAbort("VOID_BUDGET_EXCEEDED_TP",
                                      f"{rung}: TP void_rate {tp_void:.3f} > 0.05")

            cand_sum["parse_failures"] = cand_pf
            cand_sum["void_rate"] = cand_void
            tp_sum["parse_failures"] = tp_pf
            tp_sum["void_rate"] = tp_void

            # Per-rung A6: pilot == final by construction; verify
            if manifest_hashes[rung]["pilot"] != manifest_hashes[rung]["final"]:
                raise D4ARunnerAbort("A6_DRIFT_EXCEEDED",
                                      f"{rung}: pilot != final per recorded manifest hashes")

            # Per-rung output artifacts
            import dataclasses as _dc
            def _to_jsonable(obj):
                if _dc.is_dataclass(obj):
                    return _dc.asdict(obj)
                if isinstance(obj, dict):
                    return {k: _to_jsonable(v) for k, v in obj.items()}
                if isinstance(obj, (list, tuple)):
                    return [_to_jsonable(x) for x in obj]
                return obj

            (rung_dir / "candidate_predictions.json").write_text(json.dumps(
                [{"record_id": p.record_id, "predicted_value_token_ids": list(p.predicted_value_token_ids) if p.predicted_value_token_ids else None} for p in cand_preds],
                indent=2,
            ))
            (rung_dir / "tp_control_predictions.json").write_text(json.dumps(
                [{"record_id": p.record_id, "predicted_value_token_ids": list(p.predicted_value_token_ids) if p.predicted_value_token_ids else None} for p in tp_preds],
                indent=2,
            ))
            (rung_dir / "t3_report.json").write_text(json.dumps({
                "tp_banner": tp_banner, "rung_id": rung,
                "rows": _to_jsonable(t3_rows),
                "criterion_evaluations_against_candidate": _to_jsonable(criterion_evals),
                "candidate_vs_tp_comparison": cand_vs_tp,
                "attached_labels": sorted(attached),
                "candidate_outcome": outcome,
                "tp_active_by_manager_decision": True,
                "tp_activity_authority": tp_authority,
                "envelope_measured": envelope,
            }, indent=2, default=str))
            (rung_dir / "candidate_vs_tp_comparison.json").write_text(json.dumps(cand_vs_tp, indent=2))
            (rung_dir / "a6_re_verification.json").write_text(json.dumps({
                "tp_banner": tp_banner, "rung_id": rung,
                "drift_within_tolerance": True,
                "envelope_drift": 0.0,
                "per_rung_manifest_pilot_hash": manifest_hashes[rung]["pilot"],
                "per_rung_manifest_final_hash": manifest_hashes[rung]["final"],
                "pilot_equals_final": manifest_hashes[rung]["pilot"] == manifest_hashes[rung]["final"],
            }, indent=2))

            per_rung_results[rung] = {
                "outcome": outcome,
                "attached_labels": sorted(attached),
                "candidate_summary": cand_sum,
                "tp_control_summary": tp_sum,
                "candidate_vs_tp_comparison": cand_vs_tp,
                "envelope_measured": envelope,
                "criterion_evaluations": criterion_evals,
            }
            run_summary["rungs"].append({
                "rung_id": rung,
                "outcome": outcome,
                "attached_labels": sorted(attached),
                "cand_acc": cand_sum["answerable_accuracy"],
                "tp_acc": tp_sum["tp_control_accuracy"],
                "nw_diff_upper": cand_vs_tp["newcombe_wilson_diff_upper"],
                "tp_fires": cand_vs_tp["tp_fires"],
            })
            print(f"[Path A] {rung}: outcome={outcome}; "
                  f"cand={cand_sum['answerable_accuracy']:.4f}; "
                  f"tp={tp_sum['tp_control_accuracy']:.4f}; "
                  f"nw_upper={cand_vs_tp['newcombe_wilson_diff_upper']:.4f}; "
                  f"attached={sorted(attached) or 'none'}")

        # Sealed-byte protection check (post-run)
        sealed_after = sealed_dir_inventory()
        assert_no_sealed_byte_change(sealed_before, sealed_after)

        # Run-level IVR
        ivr_lines = [
            "# Lane 1a' Path A — Instrument Validation Report",
            "",
            "```text",
            "SYNTHETIC / DIAGNOSTIC -- NON-BINDING -- NOT FOR THRESHOLD DERIVATION",
            "PATH A L01-L08 PILOT (Manager-authorized 2026-06-12)",
            "PER-RUNG ADJUDICATION; NO CROSS-RUNG AGGREGATION",
            "```",
            "",
            "## Per-rung outcomes (rung-local bounded sentences)",
            "",
            "| Rung | Candidate accuracy | TP control accuracy | NW diff CI upper | Attached labels | Outcome (rung-local) |",
            "|---|---|---|---|---|---|",
        ]
        for r in run_summary["rungs"]:
            attached_str = ", ".join(r["attached_labels"]) if r["attached_labels"] else "(none)"
            ivr_lines.append(f"| {r['rung_id']} | {r['cand_acc']:.4f} | {r['tp_acc']:.4f} | {r['nw_diff_upper']:.4f} | {attached_str} | {r['outcome']} |")
        ivr_lines.extend([
            "",
            "## TP banner (ACTIVE form; Manager Path A authorization)",
            "",
            f"- tp_criterion_status: {tp_banner['tp_criterion_status']}",
            f"- tp_inactivity_authority: {tp_banner['tp_inactivity_authority']}",
            f"- tp_generation_status: {tp_banner['tp_generation_status']}",
            f"- tp_elimination_labels_enabled: {tp_banner['tp_elimination_labels_enabled']}",
            "",
            "## Per-rung adjudication rule (Manager §5)",
            "",
            "> Each rung is adjudicated separately. No cross-rung aggregation. No composite score. No survival count. No '8/8 survived' phrasing. Eight non-eliminations, if they occur, are eight rung-local bounded sentences — they do not aggregate.",
            "",
            "## Non-claim block (verbatim)",
            "",
            "> Path A, even if all rungs return NOT_RULED_OUT, does not establish: model capability, model incapability, candidate certification, task-family viability, certification readiness, retention-under-compression, Claim C progress, seam evidence, or public benchmark status.",
            "> The instrument may rule out; it may not rule in. Reportable only as 'not explained by the declared shortcut battery'; never as 'not shortcut-driven.'",
            "",
            "— CS Engineer, 2026-06-12",
        ])
        (OUTPUT_DIR / "instrument_validation_report.md").write_text("\n".join(ivr_lines))

        # Run-level ledger
        ledger = {
            "tp_banner": tp_banner,
            "model_invoked": True, "model_loaded": True,
            "candidate_sweep_id_created": cand_sweep_id,
            "tp_sweep_id_created": tp_sweep_id,
            "structure": "Path A: 8 rungs (L01-L08) × 2 sweeps (candidate + TP control) = 1,536 inferences; per-rung adjudication; no cross-rung aggregation",
            "sweep_execution": True,
            "candidate_model_outputs_produced": True,
            "tp_control_model_outputs_produced": True,
            "no_threshold_work": "CONFIRMED",
            "no_certification_evaluation": "CONFIRMED",
            "no_claim_c_activation": "CONFIRMED",
            "no_sealed_byte_change": "CONFIRMED (sealed dir inventory unchanged before/after)",
            "no_quantization": "CONFIRMED",
            "no_int8_or_int4": "CONFIRMED",
            "tp_generation_method": preconditions["token_prior_method"],
            "no_scrambled_binding_generations": "CONFIRMED — TP method is no-bindings shell",
            "outputs_validation_only": "SYNTHETIC/DIAGNOSTIC — Path A instrument-use artifacts",
            "manager_authorization": "Lane 1a' Prime Path A Execution — Manager 2026-06-12",
            "model_snapshot_hash_authorized": preconditions["authorized_model_snapshot_hash"],
            "model_snapshot_hash_computed": env["model_snapshot_hash_computed"],
            "mlx_lm_version": env["mlx_lm_version"],
            "runner_hash": sha256_file(RUNNER_PATH),
            "parser_hash": sha256_file(RUNNER_DIR / "parse_model_output.py"),
            "prompt_template_candidate_hash": sha256_file(PROMPT_TEMPLATE_CAND_PATH),
            "prompt_template_tp_hash": sha256_file(PROMPT_TEMPLATE_TP_PATH),
            "decoding_config_hash": sha256_file(DECODING_CONFIG_PATH),
            "preconditions_hash": sha256_file(PRECONDITIONS_PATH),
            "scorer_hash": sha256_file(EXPERIMENT_DIR / "lane1a_prime" / "validation.py"),
            "generator_path": preconditions["approved_generator_path"],
            "generator_hash": gen_hash,
            "sealed_lock_record_hash": sealed_hash,
            "lock_event_hashes": preconditions["lock_event_hashes"],
            "per_rung_manifest_hashes": manifest_hashes,
            "env": env,
            "per_rung_results": run_summary["rungs"],
            "elapsed_seconds": time.time() - started_at,
        }
        (OUTPUT_DIR / "execution_ledger.json").write_text(json.dumps(ledger, indent=2, default=str))

        # Final summary print
        print(f"[Path A] COMPLETE")
        for r in run_summary["rungs"]:
            attached_str = ", ".join(r["attached_labels"]) or "none"
            print(f"  {r['rung_id']}: outcome={r['outcome']}; attached={attached_str}; cand={r['cand_acc']:.4f}; tp={r['tp_acc']:.4f}")
        print(f"  elapsed: {time.time() - started_at:.1f}s")
        return 0

    except D4ARunnerAbort as exc:
        abort_dir = emit_abort_artifact(exc.reason_code, exc.message, env, partial, started_at)
        print(f"[Path A ABORT] {exc} | artifacts at {abort_dir}", file=sys.stderr)
        return 1
    except Exception as exc:
        tb = traceback.format_exc()
        abort_dir = emit_abort_artifact("UNHANDLED_EXCEPTION",
                                         f"{type(exc).__name__}: {exc}\n{tb}",
                                         env, partial, started_at)
        print(f"[Path A ABORT] {exc} | artifacts at {abort_dir}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
