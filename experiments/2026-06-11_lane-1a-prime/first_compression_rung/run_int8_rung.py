#!/usr/bin/env python3
"""First compression rung — FP16 baseline → INT8 comparison.

Authorized by TL routing 2026-06-13: "First Compression Rung Execution
Authorized" — INT8-only first compression rung on the byte-verified
constructed-positive pair; no INT4, no full ladder, no Claim C
activation.

Mirrors `experiments/2026-06-11_lane-1a-prime/constructed_positive/
run_validation.py` byte-for-byte on scorer/gate/parser/criteria.
The only deltas:
  - MODEL_ID points to the sealed local INT8 snapshot under tier0-run/
  - OUTPUT_DIR points to governance/.../first-compression-rung/
  - metadata.identity = "INT8"
  - pre-flight also verifies the INT8 model snapshot hash

Narrow question (per TL routing):
    Under INT8, does the instrument still eliminate the defective
    member and spare the clean member?

Secondary question:
    Does criterion identity change under compression, especially
    through abstention-format behavior?

Outcome classes (per TL routing):
    RETENTION-PASS:        defective still eliminated, clean spared
    DEFECT-LOSS:           defective no longer eliminated
    OVER-ELIMINATION:      both eliminated
    CRITERION-SHIFT-ONLY:  pattern preserved; firing criterion changed
    INDETERMINATE:         artifact/scorer/run issue blocks interpretation

(The runner emits the per-member elimination outcome + criterion label;
the comparison classification is performed in the return memo, not in
the runner.)

Scope discipline:
  - Same scorer/gate logic (T3_BOUNDS sealed bounds applied)
  - Same constructed artifacts (sha256-verified pre-flight)
  - Same prompt template + decoding config (sha256-verified pre-flight)
  - INT8 model snapshot sha256-verified at load
  - Raw outputs retained per-item
  - No threshold changes
  - INT4 / full ladder / second rung / Claim C: forbidden
"""

import json
import hashlib
import math
import time
import sys
from datetime import datetime, timezone
from pathlib import Path

import mlx_lm

# === Paths ===
SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parents[2]

VALIDATION_DIR = REPO_ROOT / "experiments/2026-06-11_lane-1a-prime/validation"
D4_RUNNER_DIR = REPO_ROOT / "experiments/2026-06-11_lane-1a-prime/d4_runner"
CONSTRUCTED_DIR = REPO_ROOT / "experiments/2026-06-11_lane-1a-prime/constructed_positive"

PROMPT_TEMPLATE_PATH = D4_RUNNER_DIR / "prompt_template_v1.json"
DECODING_CONFIG_PATH = D4_RUNNER_DIR / "decoding_config.json"
T3_BOUNDS_PATH = VALIDATION_DIR / "T3_BOUNDS_DECLARATION.json"
SCHEDULE_PATH = VALIDATION_DIR / "STRATIFIED_RECIPE_SCHEDULE.json"
ORACLE_PATH = VALIDATION_DIR / "ORACLE_VERDICT_TABLE.json"

CLEAN_PATH = CONSTRUCTED_DIR / "clean_member.json"
DEFECTIVE_PATH = CONSTRUCTED_DIR / "defective_member.json"
MANIFEST_PATH = CONSTRUCTED_DIR / "realized_match_manifest.json"

# INT8 sealed snapshot (read-only; tier0-run/ is SEALED — never write)
INT8_SNAPSHOT_DIR = REPO_ROOT / "tier0-run/Qwen2.5-3B-Instruct-mlx-int8"
INT8_MODEL_SAFETENSORS = INT8_SNAPSHOT_DIR / "model.safetensors"
INT8_CONFIG = INT8_SNAPSHOT_DIR / "config.json"
INT8_TOKENIZER_CONFIG = INT8_SNAPSHOT_DIR / "tokenizer_config.json"

OUTPUT_DIR = REPO_ROOT / "governance/2026-06-11_lane-1a-prime/first-compression-rung"

# MODEL_ID is the local INT8 snapshot path (mlx_lm.load accepts a local dir)
MODEL_ID = str(INT8_SNAPSHOT_DIR)
IDENTITY_LABEL = "INT8"

# Expected INT8 snapshot hashes (captured pre-flight 2026-06-13)
INT8_EXPECTED = {
    "model.safetensors": "78cdda52f8c84884",
    "config.json": "0a73a0b1727e55ef",
    "tokenizer_config.json": "ee8f6d44bf2353e6",
    "model.safetensors.index.json": "3aaeed01b82210ba",
    "generation_config.json": "ea35dfb6fc5051b0",
}


# === Helpers ===
def sha256_file(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def wilson_ci(successes: int, n: int, z: float = 1.96):
    if n == 0:
        return (0.0, 1.0)
    phat = successes / n
    denom = 1.0 + z * z / n
    center = (phat + z * z / (2.0 * n)) / denom
    half = z * math.sqrt(phat * (1.0 - phat) / n + z * z / (4.0 * n * n)) / denom
    return (max(0.0, center - half), min(1.0, center + half))


def newcombe_wilson_diff_ci(x1: int, n1: int, x2: int, n2: int, z: float = 1.96):
    if n1 == 0 or n2 == 0:
        return (-1.0, 1.0)
    l1, u1 = wilson_ci(x1, n1, z)
    l2, u2 = wilson_ci(x2, n2, z)
    p1 = x1 / n1
    p2 = x2 / n2
    diff = p1 - p2
    lower = diff - math.sqrt((p1 - l1) ** 2 + (u2 - p2) ** 2)
    upper = diff + math.sqrt((u1 - p1) ** 2 + (p2 - l2) ** 2)
    return (lower, upper)


def parse_response(text: str):
    t = text.strip().split("\n")[0].strip()
    t = t.rstrip(".").rstrip(",").strip()
    if t == "NONE":
        strict_kind, strict_value = "NONE", None
    elif len(t) == 1 and "a" <= t <= "z":
        strict_kind, strict_value = "letter", t
    else:
        strict_kind, strict_value = "OTHER", t[:64]
    t_lower = t.lower()
    if t_lower == "none":
        content_kind, content_value = "NONE_concept", None
    elif len(t) == 1 and t.isalpha():
        content_kind, content_value = "letter_concept", t.lower()
    else:
        content_kind, content_value = "OTHER", t[:64]
    return {
        "strict_kind": strict_kind,
        "strict_value": strict_value,
        "content_kind": content_kind,
        "content_value": content_value,
    }


# === Pre-flight ===
print(f"=== Pre-flight: input hashes ({IDENTITY_LABEL} rung) ===")
input_hashes = {}
for p, expected_prefix in [
    (PROMPT_TEMPLATE_PATH, "f1956e7d"),
    (DECODING_CONFIG_PATH, "a20391d8"),
    (T3_BOUNDS_PATH, "45565d0b"),
    (SCHEDULE_PATH, "7ad3ccdd"),
    (ORACLE_PATH, "9c6cbda9"),
    (CLEAN_PATH, "f412d04c"),
    (DEFECTIVE_PATH, "4ea3c277"),
    (MANIFEST_PATH, "49cd6451"),
]:
    h = sha256_file(p)
    match = "OK" if h.startswith(expected_prefix) else "MISMATCH"
    print(f"  [{match}] {h[:16]}... {p.name}")
    input_hashes[p.name] = h
    if not h.startswith(expected_prefix):
        print(f"  ABORTING: pre-flight hash mismatch on {p.name}")
        sys.exit(1)

print(f"\n=== Pre-flight: INT8 snapshot hashes (tier0-run/ — SEALED) ===")
int8_hashes = {}
for name, expected_prefix in INT8_EXPECTED.items():
    p = INT8_SNAPSHOT_DIR / name
    if not p.exists():
        print(f"  ABORTING: INT8 file missing: {p}")
        sys.exit(1)
    h = sha256_file(p)
    match = "OK" if h.startswith(expected_prefix) else "MISMATCH"
    print(f"  [{match}] {h[:16]}... {name}")
    int8_hashes[name] = h
    if not h.startswith(expected_prefix):
        print(f"  ABORTING: INT8 hash mismatch on {name}")
        sys.exit(1)

prompt_template = json.loads(PROMPT_TEMPLATE_PATH.read_text())
decoding_config = json.loads(DECODING_CONFIG_PATH.read_text())
t3_bounds_doc = json.loads(T3_BOUNDS_PATH.read_text())
clean = json.loads(CLEAN_PATH.read_text())
defective = json.loads(DEFECTIVE_PATH.read_text())
manifest = json.loads(MANIFEST_PATH.read_text())

t3_bounds = {c["label"]: c for c in t3_bounds_doc["criteria"]}
CEIL = t3_bounds["answerable_abstention_ceiling_exceeded"]["floor_or_ceiling"]
FLOOR = t3_bounds["null_abstention_floor_unmet"]["floor_or_ceiling"]
GAP = t3_bounds["strict_content_gap_instability"]["floor_or_ceiling"]
print(f"\nSealed T3 bounds in use: FLOOR={FLOOR} CEIL={CEIL} GAP={GAP}")

system_prompt = prompt_template["system"]
print(f"Decoding: temp={decoding_config['temperature']}, greedy={decoding_config['greedy']}, max_new={decoding_config['max_new_tokens']}")
print(f"Constructed pair: clean={clean['n_items']} items, defective={defective['n_items']} items")

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


# === Load model ===
print(f"\n=== Loading INT8 model from local sealed snapshot: {INT8_SNAPSHOT_DIR.relative_to(REPO_ROOT)} ===")
t_load_start = time.time()
model, tokenizer = mlx_lm.load(MODEL_ID)
load_secs = time.time() - t_load_start
print(f"Loaded in {load_secs:.1f}s")


# === Inference ===
def run_member(name: str, member_data: dict):
    items = member_data["items"]
    print(f"\n=== Running {name} member ({len(items)} items) under {IDENTITY_LABEL} ===")
    outputs = []
    t0 = time.time()
    for i, item in enumerate(items):
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": item["prompt_user_text"]},
        ]
        prompt = tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=True
        )
        raw = mlx_lm.generate(
            model,
            tokenizer,
            prompt=prompt,
            max_tokens=decoding_config["max_new_tokens"],
            verbose=False,
        )
        parsed = parse_response(raw)
        gold = item.get("gold_value")
        if gold is None:
            strict_correct = parsed["strict_kind"] == "NONE"
        else:
            strict_correct = parsed["strict_kind"] == "letter" and parsed["strict_value"] == gold
        if gold is None:
            content_correct = parsed["content_kind"] == "NONE_concept"
        else:
            content_correct = parsed["content_kind"] == "letter_concept" and parsed["content_value"] == gold
        strict_abstained = parsed["strict_kind"] == "NONE"
        content_abstained = parsed["content_kind"] == "NONE_concept"
        outputs.append(
            {
                "record_id": item["record_id"],
                "queried_key": item["queried_key"],
                "queried_slot_1indexed": item["queried_slot_1indexed"],
                "gold_value": gold,
                "raw_output": raw,
                "parsed_strict_kind": parsed["strict_kind"],
                "parsed_strict_value": parsed["strict_value"],
                "parsed_content_kind": parsed["content_kind"],
                "parsed_content_value": parsed["content_value"],
                "strict_correct": strict_correct,
                "content_correct": content_correct,
                "strict_abstained": strict_abstained,
                "content_abstained": content_abstained,
            }
        )
        if (i + 1) % 10 == 0:
            print(f"  {i+1}/{len(items)} ({time.time()-t0:.1f}s)")
    elapsed = time.time() - t0
    print(f"  Done in {elapsed:.1f}s")
    return outputs, elapsed


clean_outputs, clean_time = run_member("clean", clean)
defective_outputs, defective_time = run_member("defective", defective)


# === Score + apply criteria ===
def summarize(name: str, outputs: list, stratum: str):
    n = len(outputs)
    n_strict_correct = sum(1 for o in outputs if o["strict_correct"])
    n_content_correct = sum(1 for o in outputs if o["content_correct"])
    n_strict_abstained = sum(1 for o in outputs if o["strict_abstained"])
    n_content_abstained = sum(1 for o in outputs if o["content_abstained"])
    n_letter_strict = sum(1 for o in outputs if o["parsed_strict_kind"] == "letter")
    n_other_strict = sum(1 for o in outputs if o["parsed_strict_kind"] == "OTHER")
    strict_accuracy = n_strict_correct / n if n else 0.0
    content_accuracy = n_content_correct / n if n else 0.0
    strict_abstention_rate = n_strict_abstained / n if n else 0.0
    content_abstention_rate = n_content_abstained / n if n else 0.0
    strict_ab_ci_low, strict_ab_ci_high = wilson_ci(n_strict_abstained, n)
    strict_acc_ci_low, strict_acc_ci_high = wilson_ci(n_strict_correct, n)
    gap_ci_low, gap_ci_high = newcombe_wilson_diff_ci(n_content_correct, n, n_strict_correct, n)
    return {
        "member": name,
        "stratum_label": stratum,
        "n": n,
        "n_strict_correct": n_strict_correct,
        "n_content_correct": n_content_correct,
        "n_strict_abstained": n_strict_abstained,
        "n_content_abstained": n_content_abstained,
        "n_letter_response_strict": n_letter_strict,
        "n_other_response_strict": n_other_strict,
        "strict_accuracy": strict_accuracy,
        "content_accuracy": content_accuracy,
        "strict_abstention_rate": strict_abstention_rate,
        "content_abstention_rate": content_abstention_rate,
        "strict_accuracy_ci_lower": strict_acc_ci_low,
        "strict_accuracy_ci_upper": strict_acc_ci_high,
        "strict_abstention_ci_lower": strict_ab_ci_low,
        "strict_abstention_ci_upper": strict_ab_ci_high,
        "content_minus_strict_correct": content_accuracy - strict_accuracy,
        "content_minus_strict_ci_lower": gap_ci_low,
        "content_minus_strict_ci_upper": gap_ci_high,
    }


def apply_six_criteria(summary: dict):
    out = {}
    out["null_abstention_floor_unmet"] = {
        "status": "NOT_APPLICABLE",
        "reason": "no NULL stratum in constructed pair (n_null = 0 matched on both members per realized_match_manifest)",
    }
    ceil_fired = summary["strict_abstention_ci_lower"] > CEIL
    out["answerable_abstention_ceiling_exceeded"] = {
        "status": "FIRED" if ceil_fired else "NOT_FIRED",
        "bound": CEIL,
        "comparison": "ci_lower > bound",
        "strict_abstention_ci_lower": summary["strict_abstention_ci_lower"],
        "strict_abstention_rate": summary["strict_abstention_rate"],
    }
    out["accuracy_indistinguishable_from_token_prior"] = {
        "status": "NOT_APPLICABLE",
        "reason": "no TP control sub-run on the constructed pair (would expand scope beyond TL routing authorization)",
    }
    out["accuracy_indistinguishable_from_declared_policy_envelope"] = {
        "status": "NOT_APPLICABLE",
        "reason": "no shortcut-policy hit rates on the constructed pair (no sealed 5-stratum envelope here)",
    }
    out["insufficient_measurement_headroom"] = {
        "status": "NOT_APPLICABLE",
        "reason": "depends on ENV computation (NOT_APPLICABLE for this pair)",
    }
    gap_fired = summary["content_minus_strict_ci_lower"] > GAP
    out["strict_content_gap_instability"] = {
        "status": "FIRED" if gap_fired else "NOT_FIRED",
        "bound": GAP,
        "comparison": "nw_diff_ci_lower > bound",
        "content_minus_strict": summary["content_minus_strict_correct"],
        "nw_diff_ci_lower": summary["content_minus_strict_ci_lower"],
        "nw_diff_ci_upper": summary["content_minus_strict_ci_upper"],
        "note": "content abstention = any case of NONE; strict = uppercase NONE exact (per prompt template's expected_response_grammar)",
    }
    return out


def derive_outcome(criteria_results: dict):
    eliminations = [label for label, res in criteria_results.items() if res.get("status") == "FIRED"]
    if eliminations:
        return "eliminated", eliminations
    return "NOT_RULED_OUT", []


clean_summary = summarize("clean", clean_outputs, stratum="answerable")
defective_summary = summarize("defective", defective_outputs, stratum="answerable (defective-stratum-labeled)")

clean_criteria = apply_six_criteria(clean_summary)
defective_criteria = apply_six_criteria(defective_summary)

clean_outcome, clean_elims = derive_outcome(clean_criteria)
defective_outcome, defective_elims = derive_outcome(defective_criteria)

if defective_outcome == "eliminated" and clean_outcome == "NOT_RULED_OUT":
    intra_run_pattern = "PASS"
elif defective_outcome == "NOT_RULED_OUT" and clean_outcome == "NOT_RULED_OUT":
    intra_run_pattern = "FAIL"
elif defective_outcome == "eliminated" and clean_outcome == "eliminated":
    intra_run_pattern = "OVER-ELIMINATION"
else:
    intra_run_pattern = "INDETERMINATE"


# === Emit ===
result = {
    "metadata": {
        "run_timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "authorization": "TL routing 2026-06-13: First Compression Rung Execution Authorized — INT8-only first compression rung; no INT4 / full ladder / second rung / Claim C / certification / ranking / public benchmark / funder release / SBIR / Path B / Path D / schedule v2",
        "identity": IDENTITY_LABEL,
        "rung_label": "FP16_baseline_to_INT8_first_compression_rung",
        "model_source": str(INT8_SNAPSHOT_DIR.relative_to(REPO_ROOT)),
        "mlx_lm_version": "0.31.3",
        "decoding_config_sha256": input_hashes[DECODING_CONFIG_PATH.name],
        "prompt_template_sha256": input_hashes[PROMPT_TEMPLATE_PATH.name],
        "t3_bounds_sha256": input_hashes[T3_BOUNDS_PATH.name],
        "schedule_sha256": input_hashes[SCHEDULE_PATH.name],
        "oracle_verdict_sha256": input_hashes[ORACLE_PATH.name],
        "clean_member_sha256": input_hashes[CLEAN_PATH.name],
        "defective_member_sha256": input_hashes[DEFECTIVE_PATH.name],
        "realized_match_manifest_sha256": input_hashes[MANIFEST_PATH.name],
        "int8_snapshot_hashes": int8_hashes,
        "fp16_baseline_run_result_sha256": "268ed175db47b7949fae18889bf0700366bd0900ecec81bf60e5b8c8a3f9f2ac",
        "scope_note": "INT8 first compression rung on the byte-verified constructed-positive pair; TP/ENV/HEAD/FLOOR N/A by pair construction",
    },
    "clean_member": {
        "summary": clean_summary,
        "criteria_outcomes": clean_criteria,
        "outcome": clean_outcome,
        "elimination_labels": clean_elims,
    },
    "defective_member": {
        "summary": defective_summary,
        "criteria_outcomes": defective_criteria,
        "outcome": defective_outcome,
        "elimination_labels": defective_elims,
    },
    "intra_run_pattern": intra_run_pattern,
    "inference_seconds_clean": clean_time,
    "inference_seconds_defective": defective_time,
    "inference_seconds_total": clean_time + defective_time,
    "model_load_seconds": load_secs,
}

(OUTPUT_DIR / "int8_run_result.json").write_text(json.dumps(result, indent=2, default=str))
(OUTPUT_DIR / "int8_clean_outputs.json").write_text(json.dumps(clean_outputs, indent=2))
(OUTPUT_DIR / "int8_defective_outputs.json").write_text(json.dumps(defective_outputs, indent=2))


# === Print summary ===
print(f"\n=== INT8 result summary ===")
for name, summary, criteria, outcome_v, elims_v in [
    ("Clean", clean_summary, clean_criteria, clean_outcome, clean_elims),
    ("Defective", defective_summary, defective_criteria, defective_outcome, defective_elims),
]:
    print(f"{name} member:")
    print(f"  strict accuracy={summary['strict_accuracy']:.4f} ({summary['n_strict_correct']}/{summary['n']}), content accuracy={summary['content_accuracy']:.4f}")
    print(f"  strict abstention={summary['strict_abstention_rate']:.4f}, content abstention={summary['content_abstention_rate']:.4f}")
    print(f"  (content - strict) correct = {summary['content_minus_strict_correct']:.4f}; NW-diff CI = [{summary['content_minus_strict_ci_lower']:.4f}, {summary['content_minus_strict_ci_upper']:.4f}]")
    ceil = criteria['answerable_abstention_ceiling_exceeded']
    gap = criteria['strict_content_gap_instability']
    print(f"  CEIL: {ceil['status']} (strict_abstention_ci_lower={ceil['strict_abstention_ci_lower']:.4f} vs bound {ceil['bound']})")
    print(f"  GAP:  {gap['status']} (nw_diff_ci_lower={gap['nw_diff_ci_lower']:.4f} vs bound {gap['bound']})")
    print(f"  Outcome: {outcome_v}  labels: {elims_v}")
    print()
print(f"=== INT8 intra-run pattern: {intra_run_pattern} ===")
print(f"\nInference: {clean_time + defective_time:.1f}s total (80 items)")
print(f"Outputs written to: {OUTPUT_DIR}/")
print(f"\n(Comparison to FP16 baseline + outcome classification handled in the return memo, not the runner.)")
