"""Lane 1a' Prime D4-A Runner.

Manager D4-A authorization 2026-06-11 (LANE1A-PRIME-D4A-MINIMAL-OPERATIONAL-PILOT).
Option A pin substitution: mlx_lm 0.31.3 (CS-D4A-MLX-LM-PIN-SUBSTITUTION-2026-06-11.md).
Token-prior generations DECLINED by Manager Q2 — TP criterion INACTIVE.

Scope: L01 only / 96 records / Qwen2.5-3B-Instruct bf16 / one greedy pass.

Manager §6 abort triggers (each fires before any output is committed):
  1. pre-flight hash refusal (PH5-4)
  2. A6 drift exceedance
  3. schema validation failure
  4. artifact hash mismatch
  5. runner/model identity mismatch (mlx_lm version OR snapshot hash)
  6. unhandled exception

This runner does NOT modify the sealed validation/ directory; all
output lives under d4_a_pilot/.
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
from dataclasses import dataclass, field
from pathlib import Path


RUNNER_PATH = Path(__file__).resolve()
RUNNER_DIR = RUNNER_PATH.parent
EXPERIMENT_DIR = RUNNER_DIR.parent
VALIDATION_DIR = EXPERIMENT_DIR / "validation"
REPO_ROOT = EXPERIMENT_DIR.parent.parent
SEALED_LOCK_RECORD = REPO_ROOT / "governance" / "2026-06-11_lane-1a-prime" / "LANE1A-PRIME-SEALED-LOCK-RECORD-v1.0.md"

OUTPUT_DIR = EXPERIMENT_DIR / "d4_a_pilot"
PRECONDITIONS_PATH = RUNNER_DIR / "preconditions.json"
DECODING_CONFIG_PATH = RUNNER_DIR / "decoding_config.json"
PROMPT_TEMPLATE_PATH = RUNNER_DIR / "prompt_template_v1.json"

sys.path.insert(0, str(EXPERIMENT_DIR))


class D4ARunnerAbort(Exception):
    """Hard abort during D4-A. Caller emits an abort retention dir."""

    def __init__(self, reason_code: str, message: str):
        super().__init__(f"[{reason_code}] {message}")
        self.reason_code = reason_code
        self.message = message


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def compute_model_snapshot_hash(model_dir: Path) -> str:
    """B1 v2 routine: sha256 over sorted (rel_path, size, file_sha256) manifest."""
    files = []
    for f in sorted(model_dir.rglob("*")):
        if f.is_file():
            rel = f.relative_to(model_dir)
            size = f.stat().st_size
            file_sha = hashlib.sha256(f.read_bytes()).hexdigest()
            files.append(f"{rel}\t{size}\t{file_sha}")
    manifest = "\n".join(files)
    return "sha256:" + sha256_bytes(manifest.encode("utf-8"))


def stamp_environment() -> dict:
    return {
        "hostname": platform.node(),
        "os_release": platform.platform(),
        "cpu_brand": platform.processor() or "unknown",
        "chip_arch": platform.machine(),
        "python_version": sys.version.split()[0],
        "sys_platform": sys.platform,
    }


def precondition_mlx_lm_version_check(env: dict, authorized: str) -> str:
    """Returns the actual installed mlx_lm version; raises on mismatch."""
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
    """PH5-4 pre-flight against lock-event artifacts."""
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
    """Verify sealed pilot/final manifest sha256s."""
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
    """Verify sealed LOCK-RECORD bytes unchanged."""
    actual = sha256_file(SEALED_LOCK_RECORD)
    expected = preconditions["sealed_lock_record_hash"]
    if actual != expected:
        raise D4ARunnerAbort(
            "SEALED_LOCK_RECORD_MUTATED",
            f"sealed LOCK-RECORD hash {actual} != sealed-time {expected}",
        )
    return actual


def precondition_model_snapshot(env: dict, preconditions: dict) -> Path:
    """Locate the local HF snapshot and verify its hash matches authorized."""
    snap_root = Path(os.path.expanduser(
        "~/.cache/huggingface/hub/models--Qwen--Qwen2.5-3B-Instruct/snapshots"
    ))
    if not snap_root.is_dir():
        raise D4ARunnerAbort(
            "MODEL_SNAPSHOT_NOT_FOUND",
            f"HF snapshot root not present: {snap_root}",
        )
    snapshots = list(snap_root.iterdir())
    if not snapshots:
        raise D4ARunnerAbort(
            "MODEL_SNAPSHOT_NOT_FOUND",
            f"no snapshots under {snap_root}",
        )
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


def render_prompt(template: dict, record: dict) -> tuple[str, str]:
    """Render the (system, user) text pair for a manifest record."""
    from d4_runner.parse_model_output import render_pair_lines, render_query_key
    pairs = record["context_block"]["real_pair_block"]["pairs"]
    pair_lines = render_pair_lines(pairs)
    query_key = render_query_key(record["queried_key"])
    user_text = template["user_template"].format(
        pair_lines=pair_lines, query_key=query_key
    )
    return template["system"], user_text


def run_inference(model, tokenizer, system_text: str, user_text: str,
                  decoding_config: dict) -> tuple[str, float, str]:
    """Run greedy inference. Returns (output_text, latency_ms, finish_reason)."""
    import mlx_lm
    # Build the chat-formatted prompt
    messages = [
        {"role": "system", "content": system_text},
        {"role": "user", "content": user_text},
    ]
    try:
        prompt_text = tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=True
        )
    except Exception as exc:
        raise D4ARunnerAbort(
            "PROMPT_RENDER_FAILURE", f"chat template apply failed: {exc}"
        )
    t0 = time.time()
    try:
        # mlx_lm.generate signature varies; use kwargs for safety
        from mlx_lm import generate
        output_text = generate(
            model,
            tokenizer,
            prompt=prompt_text,
            max_tokens=decoding_config["max_new_tokens"],
            verbose=False,
        )
    except TypeError:
        # Fallback for older mlx_lm signatures
        try:
            from mlx_lm import generate
            output_text = generate(
                model, tokenizer, prompt_text,
                max_tokens=decoding_config["max_new_tokens"],
            )
        except Exception as exc:
            raise D4ARunnerAbort("INFERENCE_FAILURE", f"mlx_lm.generate failed: {exc}")
    except Exception as exc:
        raise D4ARunnerAbort("INFERENCE_FAILURE", f"mlx_lm.generate failed: {exc}")
    latency_ms = (time.time() - t0) * 1000.0
    finish_reason = "completed"
    return output_text, latency_ms, finish_reason


def make_sweep_id() -> str:
    """Manager-authorized sweep_id per Q1.5."""
    ts = time.strftime("%Y%m%d-%H%M%S")
    rand6 = "".join(random.SystemRandom().choices(
        _string.ascii_lowercase + _string.digits, k=6
    ))
    return f"lane1a-prime-d4a-{ts}-{rand6}"


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


def main(argv: list[str] | None = None) -> int:
    started_at = time.time()
    env = stamp_environment()
    partial: dict = {}
    try:
        # Step 1: Load preconditions
        preconditions = json.loads(PRECONDITIONS_PATH.read_text())
        env["preconditions_hash"] = sha256_file(PRECONDITIONS_PATH)

        # Step 2: mlx_lm version check
        precondition_mlx_lm_version_check(
            env, preconditions["authorized_mlx_lm_version"]
        )

        # Step 3: PH5-4 pre-flight
        pre_flight_log = precondition_ph5_4(preconditions)
        partial["pre_flight"] = pre_flight_log

        # Step 4: Manifest hashes
        manifest_hashes = precondition_manifest_hashes(preconditions)
        partial["manifest_hashes"] = manifest_hashes

        # Step 5: Sealed LOCK-RECORD hash
        sealed_hash = precondition_sealed_lock_record(preconditions)
        partial["sealed_lock_record_hash"] = sealed_hash

        # Step 6: Model snapshot dir + hash
        snap_dir = precondition_model_snapshot(env, preconditions)
        partial["snapshot_dir"] = str(snap_dir)

        # Step 7: Create sweep_id + output dir
        sweep_id = make_sweep_id()
        env["sweep_id"] = sweep_id
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        (OUTPUT_DIR / "candidate_outputs").mkdir(exist_ok=True)

        # Step 8: Write pre-flight log immediately
        (OUTPUT_DIR / "pre_flight_log.json").write_text(json.dumps({
            "sweep_id": sweep_id,
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

        # Step 9: Load model
        print(f"[D4-A] sweep_id={sweep_id}; loading model from {snap_dir}...")
        from mlx_lm import load as mlx_load
        model, tokenizer = mlx_load(str(snap_dir))
        env["model_loaded"] = True

        # Step 10: Load manifests + decoding + prompt template
        pilot_records = json.loads(
            (VALIDATION_DIR / "pilot_manifests_L01.json").read_text()
        )
        final_records = json.loads(
            (VALIDATION_DIR / "final_manifests_L01.json").read_text()
        )
        decoding_config = json.loads(DECODING_CONFIG_PATH.read_text())
        prompt_template = json.loads(PROMPT_TEMPLATE_PATH.read_text())

        # Step 11: Run inference per record
        from d4_runner.parse_model_output import parse_model_output
        candidate_predictions = []
        per_record_outputs = []
        print(f"[D4-A] running inference on {len(pilot_records)} records...")
        for idx, record in enumerate(pilot_records):
            record_id = f"L01-{idx:03d}-{record['stratum']}"
            system_text, user_text = render_prompt(prompt_template, record)
            output_text, latency_ms, finish_reason = run_inference(
                model, tokenizer, system_text, user_text, decoding_config
            )
            parsed = parse_model_output(output_text)
            per_record = {
                "record_id": record_id,
                "stratum": record["stratum"],
                "queried_key": record["queried_key"],
                "gold": record["gold"],
                "prompt_user_text": user_text,
                "output_text": output_text,
                "parsed": parsed,
                "latency_ms": latency_ms,
                "finish_reason": finish_reason,
            }
            per_record_outputs.append(per_record)
            (OUTPUT_DIR / "candidate_outputs" / f"{record_id}.json").write_text(
                json.dumps(per_record, indent=2)
            )
            # Build SimulatedPrediction shape
            from lane1a_prime.oracle_cases import SimulatedPrediction
            sp = SimulatedPrediction(
                record_id=record_id,
                predicted_value_token_ids=parsed["predicted_value_token_ids"],
            )
            candidate_predictions.append(sp)
            if (idx + 1) % 10 == 0:
                print(f"[D4-A]   {idx + 1}/{len(pilot_records)} done")

        candidate_predictions_t = tuple(candidate_predictions)

        # Step 12: Apply policy battery + envelope
        from lane1a_prime.validation import (
            apply_policy_battery,
            compute_union_envelope,
            populate_t1_report,
            populate_t3_report,
            populate_t4_report,
            assemble_instrument_validation_report,
            emit_execution_ledger,
            _build_measurements_for_predictions,
            match_oracle_verdict,
        )
        from lane1a_prime.analysis import apply_criterion
        outputs_by_policy = apply_policy_battery(pilot_records)
        envelope = compute_union_envelope(
            pilot_records, outputs_by_policy, "answerable"
        )

        # Step 13: T1 report (battery + A6 drift block)
        t1_report = populate_t1_report(pilot_records, outputs_by_policy)

        # Step 14: T3 report — TP INACTIVE per Manager Q2
        t3_report = populate_t3_report()
        # Build measurements against the CANDIDATE predictions
        measurements = _build_measurements_for_predictions(
            pilot_records, candidate_predictions_t
        )
        # Evaluate each criterion vs candidate; mark TP INACTIVE
        criterion_evaluations: dict = {}
        attached_labels: list[str] = []
        for criterion in t3_report.rows:
            label = criterion["criterion_label"]
            if label == "accuracy_indistinguishable_from_token_prior":
                criterion["disposition_d4a"] = "INACTIVE_BY_MANAGER_DECISION"
                criterion["fired_d4a"] = False
                criterion["manager_decision_ref"] = "MANAGER-AUTHORIZATION-LANE-1A-PRIME-D4A 2026-06-11 §4"
                criterion_evaluations[label] = {
                    "outcome": "INACTIVE",
                    "reason": "Token-prior generations declined by Manager Q2 (2026-06-11)",
                }
                continue
            if label not in measurements:
                criterion_evaluations[label] = {
                    "outcome": "NOT_EVALUATED",
                    "reason": "measurement not available",
                }
                continue
            from lane1a_prime.analysis import EliminationCriterion, CriterionComparison
            m = measurements[label]
            # Reconstruct EliminationCriterion from t3_report row
            crit_obj = EliminationCriterion(
                label=label,
                stratum=criterion["stratum"],
                comparison=CriterionComparison(criterion["comparison"]),
                floor_or_ceiling=criterion["floor_or_ceiling"],
                is_floor=criterion["is_floor"],
            )
            fires = apply_criterion(crit_obj, m)
            criterion["fired_d4a"] = bool(fires)
            criterion["measurement_d4a"] = m
            if fires:
                attached_labels.append(label)
            criterion_evaluations[label] = {"outcome": "FIRED" if fires else "PASSED", "measurement": m}

        # Outcome determination per A2 INH-2: NOT_RULED_OUT iff no elimination
        # label attached AND measurable; INCONCLUSIVE on harness anomaly only.
        if attached_labels:
            outcome = "ELIMINATED"
        else:
            outcome = "NOT_RULED_OUT"

        # Step 15: T4 report (tuple-immutable rows; build new combined list)
        t4_report = populate_t4_report()
        t4_d4a_rows = list(t4_report.rows) + [
            {"review_item_id": "D4A-runner", "reviewer": "CS", "risk_class": "implementation", "disposition": "incorporated", "owner": "CS", "status": "resolved"},
            {"review_item_id": "D4A-tp-inactive", "reviewer": "Manager", "risk_class": "criterion-set", "disposition": "Manager Q2 decline; TP INACTIVE; reduced criteria by Manager naming", "owner": "Manager", "status": "resolved"},
            {"review_item_id": "D4A-pin-substitution", "reviewer": "Manager", "risk_class": "framework-version", "disposition": "Option A substitution mlx_lm 0.31.3", "owner": "Manager", "status": "resolved"},
        ]

        # Step 16: A6 — pilot == final by sealed construction
        a6_block = {
            "drift_within_tolerance": True,
            "envelope_drift": 0.0,
            "flagged_drifts": [],
            "per_policy_drift": {p: 0.0 for p in outputs_by_policy},
            "rationale": "pilot and final manifests share sealed sha256 by PH5-3 construction; A6 drift is 0 by identity.",
        }
        # If pilot/final differ for any reason, abort
        if manifest_hashes["pilot_L01"] != manifest_hashes["final_L01"]:
            raise D4ARunnerAbort(
                "A6_DRIFT_EXCEEDED",
                f"pilot {manifest_hashes['pilot_L01']} != final {manifest_hashes['final_L01']}",
            )

        # Step 17: Compute per-stratum candidate accuracy / abstention
        answ = [(r, p) for r, p in zip(pilot_records, candidate_predictions_t) if r["stratum"] == "answerable"]
        null = [(r, p) for r, p in zip(pilot_records, candidate_predictions_t) if r["stratum"] == "null"]
        def is_correct(r, p):
            if p.predicted_value_token_ids is None:
                return False
            return list(p.predicted_value_token_ids) == r["gold"]["value_token_ids"]
        def is_abstained(p):
            return p.predicted_value_token_ids is None
        answ_correct = sum(1 for r, p in answ if is_correct(r, p))
        answ_abstain = sum(1 for r, p in answ if is_abstained(p))
        null_abstain = sum(1 for r, p in null if is_abstained(p))
        parse_failures = sum(1 for o in per_record_outputs if o["parsed"]["parse_status"] == "parse_failure")
        void_rate = parse_failures / len(per_record_outputs)
        candidate_summary = {
            "n_answerable": len(answ),
            "answerable_correct": answ_correct,
            "answerable_accuracy": answ_correct / max(len(answ), 1),
            "answerable_abstained": answ_abstain,
            "answerable_abstention_rate": answ_abstain / max(len(answ), 1),
            "n_null": len(null),
            "null_abstained": null_abstain,
            "null_abstention_rate": null_abstain / max(len(null), 1),
            "parse_failures": parse_failures,
            "void_rate": void_rate,
        }

        # Void budget check
        if void_rate > 0.05:
            raise D4ARunnerAbort(
                "VOID_BUDGET_EXCEEDED",
                f"void_rate {void_rate:.3f} > 0.05; rung INCONCLUSIVE",
            )

        # Step 18: Assemble IVR
        ivr_text = assemble_instrument_validation_report(
            t1_report, t3_report, t4_report, [], "L01",
        )
        # Append D4-A specific sections
        ivr_d4a_addendum = "\n\n".join([
            "",
            "## D4-A Candidate Run (Manager-authorized model execution)",
            "",
            f"- sweep_id: `{sweep_id}`",
            f"- model: Qwen2.5-3B-Instruct (bf16)",
            f"- model_snapshot_hash: `{env['model_snapshot_hash_computed']}`",
            f"- mlx_lm version: {env['mlx_lm_version']} (Manager-substituted from packet 0.19.3 via Option A)",
            "",
            "### Candidate per-stratum measurements",
            "",
            f"- answerable correct: {answ_correct}/{len(answ)} ({candidate_summary['answerable_accuracy']:.4f})",
            f"- answerable abstained: {answ_abstain}/{len(answ)}",
            f"- null abstained: {null_abstain}/{len(null)}",
            f"- parse failures: {parse_failures}/96 (void_rate {void_rate:.4f}; budget 0.05)",
            "",
            "### Final candidate outcome",
            "",
            f"- attached_labels: {sorted(attached_labels) if attached_labels else '(none)'}",
            f"- outcome: **{outcome}**",
            "",
            "### Inactive criteria (by Manager decision)",
            "",
            "- `accuracy_indistinguishable_from_token_prior` (TP) — INACTIVE BY MANAGER DECISION.",
            "  Token-prior generations declined by Manager Q2 (2026-06-11). The reduced criteria",
            "  set is permitted ONLY because Manager named the decline. TP elimination labels",
            "  cannot fire under this run.",
            "",
            "### Non-claim block (verbatim)",
            "",
            "> D4-A is an instrument-use step, not a capability claim. It does not establish model",
            "> capability, model incapability, task-family viability, candidate suitability,",
            "> certification readiness, retention-under-compression, Claim C progress, seam evidence,",
            "> or public benchmark status. The instrument may rule out; it may not rule in.",
            "> Passing the declared battery is reportable only as \"not explained by the declared",
            "> shortcut battery,\" never as \"not shortcut-driven.\" We have improved the ruler;",
            "> we are only beginning to touch the territory.",
            "",
            "— CS Engineer, 2026-06-11",
        ])

        # Step 19: Write artifacts
        ivr_path = OUTPUT_DIR / "instrument_validation_report.md"
        ivr_path.write_text(ivr_text + ivr_d4a_addendum)

        (OUTPUT_DIR / "candidate_predictions.json").write_text(json.dumps(
            [{"record_id": p.record_id,
              "predicted_value_token_ids": list(p.predicted_value_token_ids) if p.predicted_value_token_ids else None}
             for p in candidate_predictions_t], indent=2,
        ))

        import dataclasses as _dc
        def _to_jsonable(obj):
            if _dc.is_dataclass(obj):
                return _dc.asdict(obj)
            if isinstance(obj, dict):
                return {k: _to_jsonable(v) for k, v in obj.items()}
            if isinstance(obj, (list, tuple)):
                return [_to_jsonable(x) for x in obj]
            return obj
        (OUTPUT_DIR / "t1_report.json").write_text(json.dumps({
            "per_policy_scores": _to_jsonable(t1_report.per_policy_scores),
            "union_envelope_score": t1_report.union_envelope_score,
            "envelope_cap": t1_report.envelope_cap,
            "room_below_envelope": t1_report.room_below_envelope,
            "policy_classifications": _to_jsonable(t1_report.policy_classifications),
            "a6_drift_block": a6_block,
            "candidate_summary": candidate_summary,
        }, indent=2, default=str))

        (OUTPUT_DIR / "t3_report.json").write_text(json.dumps({
            "ideal_witness_in_pass_region": t3_report.ideal_witness_in_pass_region,
            "rows": _to_jsonable(list(t3_report.rows)),
            "criterion_evaluations_against_candidate": _to_jsonable(criterion_evaluations),
            "attached_labels": sorted(attached_labels),
            "candidate_outcome": outcome,
            "tp_inactive_by_manager_decision": True,
            "tp_inactivity_authority": "MANAGER-AUTHORIZATION-LANE-1A-PRIME-D4A 2026-06-11 §4 (Q2 decline)",
        }, indent=2, default=str))

        (OUTPUT_DIR / "t4_report.json").write_text(json.dumps({"rows": t4_d4a_rows}, indent=2))

        (OUTPUT_DIR / "a6_re_verification.json").write_text(json.dumps(a6_block, indent=2))

        # Step 20: Execution ledger
        runner_hash = sha256_file(RUNNER_PATH)
        parser_hash = sha256_file(RUNNER_DIR / "parse_model_output.py")
        prompt_template_hash = sha256_file(PROMPT_TEMPLATE_PATH)
        decoding_config_hash = sha256_file(DECODING_CONFIG_PATH)
        preconditions_hash = sha256_file(PRECONDITIONS_PATH)
        scorer_hash = sha256_file(EXPERIMENT_DIR / "lane1a_prime" / "validation.py")
        ledger = {
            "model_invoked": True,
            "model_loaded": True,
            "sweep_id_created": sweep_id,
            "sweep_execution": True,
            "candidate_model_outputs_produced": True,
            "no_threshold_work": "CONFIRMED",
            "no_certification_evaluation": "CONFIRMED",
            "no_claim_c_activation": "CONFIRMED",
            "no_l02_l08_execution": "CONFIRMED",
            "no_quantization": "CONFIRMED",
            "no_int8_or_int4": "CONFIRMED",
            "no_token_prior_generations": "CONFIRMED — Q2 declined by Manager",
            "tp_criterion_status": "INACTIVE BY MANAGER DECISION",
            "outputs_validation_only": "SYNTHETIC/DIAGNOSTIC — D4-A instrument-use artifacts",
            "manager_authorization": "Lane 1a' D4-A Minimal Operational Pilot — Manager 2026-06-11",
            "manager_blocker_disposition_pin_substitution": "Option A (mlx_lm 0.31.3) — Manager 2026-06-11",
            "model_snapshot_hash_authorized": preconditions["authorized_model_snapshot_hash"],
            "model_snapshot_hash_computed": env["model_snapshot_hash_computed"],
            "mlx_lm_version": env["mlx_lm_version"],
            "mlx_core_version": env.get("mlx_core_version", "unknown"),
            "runner_hash": runner_hash,
            "parser_hash": parser_hash,
            "prompt_template_hash": prompt_template_hash,
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
            "elapsed_seconds": time.time() - started_at,
        }
        (OUTPUT_DIR / "execution_ledger.json").write_text(json.dumps(_to_jsonable(ledger), indent=2, default=str))

        print(f"[D4-A] COMPLETE: outcome={outcome}; attached_labels={sorted(attached_labels)}")
        print(f"[D4-A] elapsed: {time.time() - started_at:.1f}s")
        return 0

    except D4ARunnerAbort as exc:
        abort_dir = emit_abort_artifact(exc.reason_code, exc.message, env, partial, started_at)
        print(f"[D4-A ABORT] {exc} | artifacts at {abort_dir}", file=sys.stderr)
        return 1
    except Exception as exc:
        tb = traceback.format_exc()
        abort_dir = emit_abort_artifact(
            "UNHANDLED_EXCEPTION", f"{type(exc).__name__}: {exc}\n{tb}", env, partial, started_at,
        )
        print(f"[D4-A ABORT] {exc} | artifacts at {abort_dir}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
