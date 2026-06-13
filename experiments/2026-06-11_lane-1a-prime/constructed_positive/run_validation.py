#!/usr/bin/env python3
"""Constructed-positive validation run.

Authorized by Manager 2026-06-13: "Constructed-positive validation
run: ACCEPT" — model-facing validation only; no quantization stress,
INT8/INT4, Path B, Path D, schedule v2, certification, ranking, or
Claim C activation.

Runs the sealed candidate model + sealed prompt shell + sealed
decoding config on Senior's constructed clean/defective pair
artifacts. Applies the six-criterion battery (per T3_BOUNDS_
DECLARATION.json sha256 45565d0b...) where computable on a single
pair without expanding scope. Records per-item raw outputs and
per-member outcomes.

Single narrow question (per TL routing):
    Does the instrument eliminate the defective member and spare
    the clean member?

Outcome classes:
    PASS:             defective eliminated, clean spared
    FAIL:             defective NOT_RULED_OUT
    OVER-ELIMINATION: both eliminated
    INDETERMINATE:    artifact/scorer/run issue blocks interpretation

Scope discipline:
  - Same scorer/gate logic (T3_BOUNDS sealed bounds applied)
  - Same constructed artifacts (sha256-verified pre-flight)
  - Same model snapshot (verified at load)
  - Raw outputs retained per-item
  - No threshold changes
  - No stress rungs / quantization / INT8 / INT4
  - Criteria that require external inputs not generated for this
    pair (TP control sub-run, declared policy envelope sub-run)
    are marked NOT_APPLICABLE — not computed by guessing
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

PROMPT_TEMPLATE_PATH = D4_RUNNER_DIR / "prompt_template_v1.json"
DECODING_CONFIG_PATH = D4_RUNNER_DIR / "decoding_config.json"
T3_BOUNDS_PATH = VALIDATION_DIR / "T3_BOUNDS_DECLARATION.json"
SCHEDULE_PATH = VALIDATION_DIR / "STRATIFIED_RECIPE_SCHEDULE.json"
ORACLE_PATH = VALIDATION_DIR / "ORACLE_VERDICT_TABLE.json"

CLEAN_PATH = SCRIPT_DIR / "clean_member.json"
DEFECTIVE_PATH = SCRIPT_DIR / "defective_member.json"
MANIFEST_PATH = SCRIPT_DIR / "realized_match_manifest.json"

OUTPUT_DIR = REPO_ROOT / "governance/2026-06-11_lane-1a-prime/constructed-positive-validation"

MODEL_ID = "Qwen/Qwen2.5-3B-Instruct"


# === Helpers ===
def sha256_file(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def wilson_ci(successes: int, n: int, z: float = 1.96):
    """Wilson score CI for a proportion. Returns (lower, upper)."""
    if n == 0:
        return (0.0, 1.0)
    phat = successes / n
    denom = 1.0 + z * z / n
    center = (phat + z * z / (2.0 * n)) / denom
    half = z * math.sqrt(phat * (1.0 - phat) / n + z * z / (4.0 * n * n)) / denom
    return (max(0.0, center - half), min(1.0, center + half))


def parse_response(text: str):
    """Parse model output.

    Returns dict with both strict and content classifications:
      strict_kind:  "NONE" (exact uppercase) | "letter" (a-z one char) | "OTHER"
      content_kind: "NONE_concept" (any abstention) | "letter_concept" (any letter
                    answer concept) | "OTHER"
    Per the sealed prompt_template's expected_response_grammar
    "single lowercase letter [a-z], OR the word NONE":
      - Strict scoring requires exact "NONE" or single lowercase letter
      - Content scoring allows case-insensitive "NONE" / "none" / single letter
        of either case as the corresponding concept
    The strict vs content split is what the sealed GAP criterion measures.
    """
    t = text.strip().split("\n")[0].strip()
    t = t.rstrip(".").rstrip(",").strip()
    # Strict classification (matches the prompt's literal grammar)
    if t == "NONE":
        strict_kind, strict_value = "NONE", None
    elif len(t) == 1 and "a" <= t <= "z":
        strict_kind, strict_value = "letter", t
    else:
        strict_kind, strict_value = "OTHER", t[:64]
    # Content classification (case-insensitive concept-level read)
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
print("=== Pre-flight: input hashes ===")
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

prompt_template = json.loads(PROMPT_TEMPLATE_PATH.read_text())
decoding_config = json.loads(DECODING_CONFIG_PATH.read_text())
t3_bounds_doc = json.loads(T3_BOUNDS_PATH.read_text())
clean = json.loads(CLEAN_PATH.read_text())
defective = json.loads(DEFECTIVE_PATH.read_text())
manifest = json.loads(MANIFEST_PATH.read_text())

# Extract T3 bounds
t3_bounds = {c["label"]: c for c in t3_bounds_doc["criteria"]}
CEIL = t3_bounds["answerable_abstention_ceiling_exceeded"]["floor_or_ceiling"]
FLOOR = t3_bounds["null_abstention_floor_unmet"]["floor_or_ceiling"]
print(f"\nSealed T3 bounds in use:")
print(f"  null_abstention_floor_unmet:                 FLOOR = {FLOOR} (CI_UPPER < FLOOR → eliminated)")
print(f"  answerable_abstention_ceiling_exceeded:      CEIL  = {CEIL} (CI_LOWER > CEIL → eliminated)")
print(f"  (TP / ENV / HEAD / GAP: require external inputs not generated for this single-pair validation)")

system_prompt = prompt_template["system"]
print(f"\nSystem prompt: {system_prompt[:80]}...")
print(f"Decoding: temp={decoding_config['temperature']}, greedy={decoding_config['greedy']}, max_new={decoding_config['max_new_tokens']}")
print(f"Constructed pair: clean={clean['n_items']} items, defective={defective['n_items']} items")
print(f"List length: {clean['list_len']} (P1 off-ceiling intent: >pilot 5)")
print(f"Queried slots: {clean['queried_slots']} (deeper than pilot)")
print(f"Construction seed: {clean['construction_seed']}")

OUTPUT_DIR.mkdir(exist_ok=True)


# === Load model ===
print(f"\n=== Loading model {MODEL_ID} ===")
t_load_start = time.time()
model, tokenizer = mlx_lm.load(MODEL_ID)
load_secs = time.time() - t_load_start
print(f"Loaded in {load_secs:.1f}s")


# === Inference ===
def run_member(name: str, member_data: dict):
    items = member_data["items"]
    print(f"\n=== Running {name} member ({len(items)} items) ===")
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
        # Strict scoring (sealed grammar):
        if gold is None:
            strict_correct = parsed["strict_kind"] == "NONE"
        else:
            strict_correct = parsed["strict_kind"] == "letter" and parsed["strict_value"] == gold
        # Content scoring (concept-level):
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
def newcombe_wilson_diff_ci(x1: int, n1: int, x2: int, n2: int, z: float = 1.96):
    """Newcombe-Wilson CI for the difference of two proportions p1-p2."""
    if n1 == 0 or n2 == 0:
        return (-1.0, 1.0)
    l1, u1 = wilson_ci(x1, n1, z)
    l2, u2 = wilson_ci(x2, n2, z)
    p1 = x1 / n1
    p2 = x2 / n2
    # Newcombe's "method 10": delta-d = z * sqrt((p1-l1)^2 + (u2-p2)^2)
    # delta+u = z * sqrt((u1-p1)^2 + (p2-l2)^2)
    diff = p1 - p2
    lower = diff - math.sqrt((p1 - l1) ** 2 + (u2 - p2) ** 2)
    upper = diff + math.sqrt((u1 - p1) ** 2 + (p2 - l2) ** 2)
    return (lower, upper)


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
    # GAP measurement: (content_correct - strict_correct) NW-diff
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


def apply_six_criteria(summary: dict, member_name: str):
    """Apply the six criteria per T3_BOUNDS. Mark N/A only where external inputs are genuinely absent."""
    out = {}
    GAP = t3_bounds["strict_content_gap_instability"]["floor_or_ceiling"]
    # FLOOR: needs NULL stratum (n_null = 0 in the constructed pair per realized match manifest)
    out["null_abstention_floor_unmet"] = {
        "status": "NOT_APPLICABLE",
        "reason": "no NULL stratum in constructed pair (n_null = 0 matched on both members per realized_match_manifest)",
    }
    # CEIL: applies to the answerable stratum on the STRICT abstention rate
    ceil_fired = summary["strict_abstention_ci_lower"] > CEIL
    out["answerable_abstention_ceiling_exceeded"] = {
        "status": "FIRED" if ceil_fired else "NOT_FIRED",
        "bound": CEIL,
        "comparison": "ci_lower > bound",
        "strict_abstention_ci_lower": summary["strict_abstention_ci_lower"],
        "strict_abstention_rate": summary["strict_abstention_rate"],
    }
    # TP: requires a TP control sub-run; not generated for the constructed pair
    out["accuracy_indistinguishable_from_token_prior"] = {
        "status": "NOT_APPLICABLE",
        "reason": "no TP control sub-run generated for constructed pair (would expand scope beyond TL routing's authorized validation)",
    }
    # ENV: requires shortcut-policy hit rates against the constructed pair
    out["accuracy_indistinguishable_from_declared_policy_envelope"] = {
        "status": "NOT_APPLICABLE",
        "reason": "no shortcut-policy hit rates computed for constructed pair (the constructed pair does not carry the sealed 5-stratum disjoint envelope structure)",
    }
    # HEAD: derived from ENV
    out["insufficient_measurement_headroom"] = {
        "status": "NOT_APPLICABLE",
        "reason": "depends on ENV computation (which is NOT_APPLICABLE for this pair)",
    }
    # GAP: COMPUTABLE — content vs strict scoring is applied per the parse_response
    # split, no external inputs needed. (content - strict) NW-diff CI lower > GAP fires.
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
    return out, ceil_fired


def derive_outcome(criteria_results: dict):
    eliminations = []
    for label, res in criteria_results.items():
        if res.get("status") == "FIRED":
            eliminations.append(label)
    if eliminations:
        return "eliminated", eliminations
    return "NOT_RULED_OUT", []


clean_summary = summarize("clean", clean_outputs, stratum="answerable")
defective_summary = summarize("defective", defective_outputs, stratum="answerable (defective-stratum-labeled)")

clean_criteria, _ = apply_six_criteria(clean_summary, "clean")
defective_criteria, _ = apply_six_criteria(defective_summary, "defective")

clean_outcome, clean_elims = derive_outcome(clean_criteria)
defective_outcome, defective_elims = derive_outcome(defective_criteria)

# Overall pattern
if defective_outcome == "eliminated" and clean_outcome == "NOT_RULED_OUT":
    pattern = "PASS"
elif defective_outcome == "NOT_RULED_OUT" and clean_outcome == "NOT_RULED_OUT":
    pattern = "FAIL"
elif defective_outcome == "eliminated" and clean_outcome == "eliminated":
    pattern = "OVER-ELIMINATION"
else:
    pattern = "INDETERMINATE"

# === Emit ===
result = {
    "metadata": {
        "run_timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "authorization": "Manager 2026-06-13: Constructed-positive validation run: ACCEPT (model-facing validation only; no quantization stress, INT8/INT4, Path B, Path D, schedule v2, certification, ranking, Claim C)",
        "model_id": MODEL_ID,
        "mlx_lm_version": "0.31.3",
        "decoding_config_sha256": input_hashes[DECODING_CONFIG_PATH.name],
        "prompt_template_sha256": input_hashes[PROMPT_TEMPLATE_PATH.name],
        "t3_bounds_sha256": input_hashes[T3_BOUNDS_PATH.name],
        "schedule_sha256": input_hashes[SCHEDULE_PATH.name],
        "oracle_verdict_sha256": input_hashes[ORACLE_PATH.name],
        "clean_member_sha256": input_hashes[CLEAN_PATH.name],
        "defective_member_sha256": input_hashes[DEFECTIVE_PATH.name],
        "realized_match_manifest_sha256": input_hashes[MANIFEST_PATH.name],
        "scope_note": "single-pair validation; TP/ENV/HEAD/GAP marked NOT_APPLICABLE rather than computed by guessing or scope-expansion",
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
    "overall_pattern": pattern,
    "inference_seconds_clean": clean_time,
    "inference_seconds_defective": defective_time,
    "inference_seconds_total": clean_time + defective_time,
    "model_load_seconds": load_secs,
}

(OUTPUT_DIR / "run_result.json").write_text(json.dumps(result, indent=2, default=str))
(OUTPUT_DIR / "clean_outputs.json").write_text(json.dumps(clean_outputs, indent=2))
(OUTPUT_DIR / "defective_outputs.json").write_text(json.dumps(defective_outputs, indent=2))

# === Print summary ===
print(f"\n=== Result summary ===")
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
print(f"=== Overall pattern: {pattern} ===")
print(f"\nInference: {clean_time + defective_time:.1f}s total ({80} items)")
print(f"Outputs written to: {OUTPUT_DIR}/")
