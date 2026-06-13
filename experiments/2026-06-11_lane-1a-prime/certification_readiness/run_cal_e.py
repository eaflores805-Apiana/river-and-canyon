#!/usr/bin/env python3
"""CAL-E Targeted Repair Run — CS executor.

Authorized by Manager 2026-06-13 ("Run CAL-E Targeted Repair Candidate" —
narrow FP16/native; CAL-E only).

Per CAL-E-TARGETED-REPAIR-SPEC-v0.1.md §4:
  list_len: 21          (longer than CAL-C's 17 -> more lookup load)
  queried_slots: 13-18  (deeper interior than CAL-C)
  near_miss_count: <=4  (CAPPED at CAL-C's level - do NOT increase)
  distractor placement: random shuffle (NOT clustered at queried slot)

Target: clean 0.88-0.92, defective <=0.10, separation >=0.78.

Imports constructor + scorer from run_calibration_sweep.py to keep the
construction protocol identical to CAL-B/CAL-C.
"""
import json, time, sys
from datetime import datetime, timezone
from pathlib import Path

import mlx_lm

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
from run_calibration_sweep import (
    construct_pair, single_difference_check, score_member, sha256_file,
    PROMPT_TEMPLATE_PATH, DECODING_CONFIG_PATH, SCORER_PATH, MODEL_ID,
)

REPO_ROOT = SCRIPT_DIR.parents[2]
OUTPUT_DIR = REPO_ROOT / "experiments/2026-06-11_lane-1a-prime/certification_readiness/sweep_outputs"
GOV_DIR    = REPO_ROOT / "governance/2026-06-11_lane-1a-prime/certification-readiness/sweep_run_records"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
GOV_DIR.mkdir(parents=True, exist_ok=True)

# Pre-flight
print("=== PRE-FLIGHT: CAL-E ===")
input_hashes = {
    "prompt_template": sha256_file(PROMPT_TEMPLATE_PATH),
    "decoding_config": sha256_file(DECODING_CONFIG_PATH),
    "scorer": sha256_file(SCORER_PATH),
}
for k, v in input_hashes.items():
    print(f"  {k}: {v}")

prompt_template = json.loads(PROMPT_TEMPLATE_PATH.read_text())
decoding_config = json.loads(DECODING_CONFIG_PATH.read_text())
system_prompt = prompt_template["system"]

# Construct CAL-E
print()
print("=== CAL-E: constructing fresh (list_len=21, slots [13..18], near_miss=4, seed=20260613005) ===")
cal_e_clean, cal_e_def = construct_pair(
    candidate_id="CAL-E",
    list_len=21,
    slot_range=[13, 14, 15, 16, 17, 18],
    n_items=40,
    near_miss_count=4,
    seed=20260613005,
)
single_diff_ok, checks = single_difference_check(cal_e_clean, cal_e_def)
print(f"  CAL-E single_difference_ok: {single_diff_ok}  {checks}")

if not single_diff_ok:
    print("  ABORT: single-difference check failed - do not run model (per Manager memo).")
    sys.exit(1)

clean_path = OUTPUT_DIR / "cal-e_clean_member.json"
def_path = OUTPUT_DIR / "cal-e_defective_member.json"
manifest_path = OUTPUT_DIR / "cal-e_realized_match_manifest.json"
clean_path.write_text(json.dumps(cal_e_clean, indent=2))
def_path.write_text(json.dumps(cal_e_def, indent=2))
manifest = {
    "match_manifest": "realized",
    "candidate_id": "CAL-E",
    "held_constant": ["list_len", "queried_slot_distribution", "key_value_vocabulary_family",
                      "near_miss_distractor_density", "item_count", "scoring_harness",
                      "queried_key_per_item_index"],
    "permitted_difference": "P2 defect only: queried key absent from listed pairs",
    "n_items_each": 40,
    "list_len": 21,
    "queried_slots": [13, 14, 15, 16, 17, 18],
    "near_miss_count": 4,
    "construction_seed": 20260613005,
    "single_difference_invariant_check": "PASS",
    "off_ceiling_design_intent": "CAL-E targeted repair - list_len 21 / slots 13-18 / near_miss 4 (capped at CAL-C level)",
    "expected_clean_target": "0.88-0.92",
    "expected_defective_target": "<=0.10",
}
manifest_path.write_text(json.dumps(manifest, indent=2))

print()
print(f"=== Loading model {MODEL_ID} ===")
t_load = time.time()
model, tokenizer = mlx_lm.load(MODEL_ID)
load_sec = time.time() - t_load
print(f"Loaded in {load_sec:.1f}s")

print()
print("=== CAL-E: running clean (40 items) + defective (40 items) ===")
t0 = time.time()
clean_result = score_member(model, tokenizer, system_prompt, decoding_config, cal_e_clean["items"])
print(f"  clean:     {clean_result['n_correct']}/{clean_result['n']} = {clean_result['strict_accuracy']:.4f}   ({time.time()-t0:.1f}s)")
t1 = time.time()
def_result = score_member(model, tokenizer, system_prompt, decoding_config, cal_e_def["items"])
print(f"  defective: {def_result['n_correct']}/{def_result['n']} = {def_result['strict_accuracy']:.4f}   ({time.time()-t1:.1f}s)")

separation = clean_result['strict_accuracy'] - def_result['strict_accuracy']
print(f"  separation (clean - defective): {separation:.4f}")

raw_clean_path = OUTPUT_DIR / "cal-e_clean_outputs.json"
raw_def_path = OUTPUT_DIR / "cal-e_defective_outputs.json"
raw_clean_path.write_text(json.dumps(clean_result["outputs"], indent=2))
raw_def_path.write_text(json.dumps(def_result["outputs"], indent=2))

run_record = {
    "candidate_id": "CAL-E",
    "clean_member": {"summary": {"strict_accuracy": clean_result["strict_accuracy"],
                                  "n": clean_result["n"], "n_correct": clean_result["n_correct"]}},
    "defective_member": {"summary": {"strict_accuracy": def_result["strict_accuracy"],
                                      "n": def_result["n"], "n_correct": def_result["n_correct"]}},
    "single_difference_ok": single_diff_ok,
    "manifest_sha256": sha256_file(manifest_path),
    "scorer_sha256": input_hashes["scorer"],
    "prompt_template_sha256": input_hashes["prompt_template"],
    "raw_output_path": str(raw_clean_path.relative_to(REPO_ROOT)),
    "raw_defective_output_path": str(raw_def_path.relative_to(REPO_ROOT)),
    "manifest_path": str(manifest_path.relative_to(REPO_ROOT)),
    "clean_member_path": str(clean_path.relative_to(REPO_ROOT)),
    "defective_member_path": str(def_path.relative_to(REPO_ROOT)),
    "candidate_config": {
        "list_len": 21,
        "queried_slots": [13, 14, 15, 16, 17, 18],
        "near_miss_count": 4,
        "construction_seed": 20260613005,
    },
    "model_id": MODEL_ID,
    "precision": "bf16-mlx-native",
    "separation": separation,
    "run_timestamp_utc": datetime.now(timezone.utc).isoformat(),
}
run_path = GOV_DIR / "cal-e_run.json"
run_path.write_text(json.dumps(run_record, indent=2))
print()
print("=== CAL-E COMPLETE ===")
print(f"run record: {run_path.relative_to(REPO_ROOT)}  sha256={sha256_file(run_path)}")
print()
print(f"Clean target 0.88-0.92: {'IN TARGET' if 0.88 <= clean_result['strict_accuracy'] <= 0.92 else 'OUT OF TARGET'} (clean={clean_result['strict_accuracy']:.4f})")
print(f"Defective target <=0.10: {'IN TARGET' if def_result['strict_accuracy'] <= 0.10 else 'OUT OF TARGET'} (defective={def_result['strict_accuracy']:.4f})")
print(f"Separation >= 0.78:      {'IN TARGET' if separation >= 0.78 else 'OUT OF TARGET'} (separation={separation:.4f})")
print()
print("Senior next: interprets against pre-declared CAL-E rule (BAND PLAUSIBLE / NEEDS REPAIR / PIVOT WATCH).")
print("CS does NOT interpret.")
