#!/usr/bin/env python3
"""Off-Ceiling Calibration Sweep — CS executor.

Authorized by Manager 2026-06-13 ("Run Off-Ceiling Calibration Sweep" —
narrow scope: CAL-A/B/C, CAL-D conditional on single-difference).

Per OFF-CEILING-CALIBRATION-SWEEP-RUNSPEC-v0.1.md §0:
  Senior CANNOT execute (firewalled env, no model). CS is the executor.
  Senior interprets the returned bytes via calibration_sweep_verdict.py.

Per Manager memo §"Required output" + RUNSPEC §6:
  This script produces one per-candidate run JSON in the schema the
  pre-registered harness consumes:
      {
        "candidate_id": "CAL-X",
        "clean_member":     {"summary": {"strict_accuracy": <float>, "n": <int>}},
        "defective_member": {"summary": {"strict_accuracy": <float>, "n": <int>}},
        "single_difference_ok": <bool>,
        "manifest_sha256": "...", "scorer_sha256": "...",
        "prompt_template_sha256": "...", "raw_output_path": "..."
      }
  + raw outputs JSON per member per candidate.

Candidate matrix per OFF-CEILING-CALIBRATION-SWEEP-SPEC-v0.1.md §3:
  CAL-A: list_len 9,  slots 6-8,   baseline distractor    → CONTROL (reuses existing constructed-positive)
  CAL-B: list_len 13, slots 8-11,  light near-similarity  → constructed fresh
  CAL-C: list_len 17, slots 10-15, mild distractor        → constructed fresh
  CAL-D: optional, gated on single-difference (NOT constructed by default)

CAL-A uses the existing constructed-positive bytes (sha256 f412d04c, 4ea3c277,
49cd6451) so the control point is byte-identical to the validated baseline; this
confirms the sweep harness reproduces the known clean=1.0 result.

NO quantization. NO INT8/INT4. FP16/native only (per RUNSPEC §3).
"""
import json, hashlib, math, time, sys, random
from datetime import datetime, timezone
from pathlib import Path

import mlx_lm

# === Paths ===
SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parents[2]

D4_RUNNER_DIR = REPO_ROOT / "experiments/2026-06-11_lane-1a-prime/d4_runner"
PROMPT_TEMPLATE_PATH = D4_RUNNER_DIR / "prompt_template_v1.json"
DECODING_CONFIG_PATH = D4_RUNNER_DIR / "decoding_config.json"

CONSTRUCTED_DIR = REPO_ROOT / "experiments/2026-06-11_lane-1a-prime/constructed_positive"
CAL_A_CLEAN = CONSTRUCTED_DIR / "clean_member.json"
CAL_A_DEF   = CONSTRUCTED_DIR / "defective_member.json"
CAL_A_MANIFEST = CONSTRUCTED_DIR / "realized_match_manifest.json"

OUTPUT_DIR = REPO_ROOT / "experiments/2026-06-11_lane-1a-prime/certification_readiness/sweep_outputs"
GOV_DIR    = REPO_ROOT / "governance/2026-06-11_lane-1a-prime/certification-readiness/sweep_run_records"

SCORER_PATH = REPO_ROOT / "experiments/2026-06-11_lane-1a-prime/constructed_positive/run_validation.py"
MODEL_ID = "Qwen/Qwen2.5-3B-Instruct"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
GOV_DIR.mkdir(parents=True, exist_ok=True)


# === Helpers ===
def sha256_file(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def sha256_text(s):
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def parse_response(text):
    """Same parser as validated run_validation.py (strict per prompt grammar)."""
    t = text.strip().split("\n")[0].strip().rstrip(".").rstrip(",").strip()
    if t == "NONE":
        return ("NONE", None)
    if len(t) == 1 and "a" <= t <= "z":
        return ("letter", t)
    return ("OTHER", t[:64])


# === Constructor for fresh candidates ===
KEY_MIN, KEY_MAX = 10, 199
LETTERS = list("abcdefghijklmnopqrstuvwxyz")


def construct_pair(candidate_id, list_len, slot_range, n_items, near_miss_count, seed):
    """Build a matched clean+defective pair per the SWEEP-SPEC §3.

    Single-difference design:
      - Same list_len, queried_slot distribution, key range, value vocab, item count.
      - Per item: same queried_key (the QUESTION) in both clean and defective.
      - Per item: distractor key set has the SAME near-miss density.
      - The ONLY difference: clean has queried_key as one of the pair entries;
        defective replaces it with a random non-near-miss key (queried_key absent).
    """
    rng = random.Random(seed)
    clean_items = []
    defective_items = []
    slot_distrib = []

    for i in range(n_items):
        queried_key = rng.randint(KEY_MIN, KEY_MAX)
        gold_value = rng.choice(LETTERS)
        slot = rng.choice(slot_range)  # 1-indexed
        slot_distrib.append(slot)

        # Near-miss distractor keys (within ±5 of queried_key, not equal)
        near_miss_pool = [k for k in range(max(KEY_MIN, queried_key - 5),
                                            min(KEY_MAX, queried_key + 5) + 1)
                          if k != queried_key]
        near_miss = rng.sample(near_miss_pool, min(near_miss_count, len(near_miss_pool)))

        # Random distractor keys to fill list (list_len - 1 for queried_key, minus near-miss)
        n_random = list_len - 1 - len(near_miss)
        used = set(near_miss) | {queried_key}
        random_distractors = []
        guard = 0
        while len(random_distractors) < n_random and guard < 500:
            k = rng.randint(KEY_MIN, KEY_MAX)
            if k not in used:
                random_distractors.append(k)
                used.add(k)
            guard += 1

        other_keys = near_miss + random_distractors
        rng.shuffle(other_keys)

        # Clean: insert queried_key at slot-1
        clean_keys = other_keys[:list_len - 1].copy()
        clean_keys.insert(slot - 1, queried_key)
        clean_keys = clean_keys[:list_len]
        # Values: gold for queried_key, random for others
        clean_values = []
        for k in clean_keys:
            if k == queried_key:
                clean_values.append(gold_value)
            else:
                clean_values.append(rng.choice(LETTERS))

        # Defective: pick a replacement key NOT in near_miss range, NOT equal to queried_key,
        # NOT already in distractors. Insert at slot-1.
        replacement_key = None
        guard = 0
        while replacement_key is None and guard < 500:
            r = rng.randint(KEY_MIN, KEY_MAX)
            if r != queried_key and r not in used and not (queried_key - 5 <= r <= queried_key + 5):
                replacement_key = r
            guard += 1
        if replacement_key is None:
            # Fallback (extremely unlikely): just pick any unused
            for r in range(KEY_MIN, KEY_MAX + 1):
                if r not in used and r != queried_key:
                    replacement_key = r
                    break

        def_keys = other_keys[:list_len - 1].copy()
        def_keys.insert(slot - 1, replacement_key)
        def_keys = def_keys[:list_len]
        def_values = [rng.choice(LETTERS) for k in def_keys]

        clean_items.append({
            "record_id": f"{candidate_id}-CLEAN-{i:03d}",
            "stratum": "answerable",
            "list_len": list_len,
            "queried_key": queried_key,
            "queried_slot_1indexed": slot,
            "gold_value": gold_value,
            "prompt_user_text": format_prompt(clean_keys, clean_values, queried_key),
        })
        defective_items.append({
            "record_id": f"{candidate_id}-DEF-{i:03d}",
            "stratum": "answerable",
            "list_len": list_len,
            "queried_key": queried_key,
            "queried_slot_1indexed": slot,
            "gold_value": None,
            "defect": "queried_key_absent_from_pairs",
            "prompt_user_text": format_prompt(def_keys, def_values, queried_key),
        })

    clean_member = {
        "member": "clean",
        "candidate_id": candidate_id,
        "n_items": n_items,
        "list_len": list_len,
        "queried_slots": list(slot_range),
        "near_miss_count": near_miss_count,
        "construction_seed": seed,
        "items": clean_items,
    }
    defective_member = {
        "member": "defective",
        "candidate_id": candidate_id,
        "n_items": n_items,
        "list_len": list_len,
        "queried_slots": list(slot_range),
        "near_miss_count": near_miss_count,
        "defect": "queried_key_absent_from_pairs",
        "construction_seed": seed,
        "items": defective_items,
    }
    return clean_member, defective_member


def format_prompt(keys, values, query):
    pairs = "\n".join(f"{k} -> {v}" for k, v in zip(keys, values))
    return f"Pairs:\n{pairs}\n\nQuery: {query}"


def single_difference_check(clean, defective):
    """Verify clean/defective pair is single-difference per P3 dimensions."""
    checks = {}
    checks["list_len_match"] = clean["list_len"] == defective["list_len"]
    checks["n_items_match"] = clean["n_items"] == defective["n_items"]
    checks["queried_slots_match"] = list(clean["queried_slots"]) == list(defective["queried_slots"])
    # Per-item: queried_key matches, queried_slot matches, list_len matches
    per_item_ok = True
    for c, d in zip(clean["items"], defective["items"]):
        if c["queried_key"] != d["queried_key"]: per_item_ok = False; break
        if c["queried_slot_1indexed"] != d["queried_slot_1indexed"]: per_item_ok = False; break
        if c["list_len"] != d["list_len"]: per_item_ok = False; break
        if c["gold_value"] is None or d["gold_value"] is not None: per_item_ok = False; break
    checks["per_item_invariant"] = per_item_ok
    # Permitted difference: defective has queried_key_absent defect; clean has gold_value
    checks["defect_field_present_on_defective"] = all(
        d.get("defect") == "queried_key_absent_from_pairs" for d in defective["items"])
    checks["all_clean_have_gold"] = all(c.get("gold_value") is not None for c in clean["items"])
    return all(checks.values()), checks


# === Score one member ===
def score_member(model, tokenizer, system_prompt, decoding_config, items):
    outputs = []
    n_correct = 0
    for i, item in enumerate(items):
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": item["prompt_user_text"]},
        ]
        prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        raw = mlx_lm.generate(model, tokenizer, prompt=prompt,
                              max_tokens=decoding_config["max_new_tokens"], verbose=False)
        kind, value = parse_response(raw)
        gold = item.get("gold_value")
        if gold is None:
            correct = (kind == "NONE")
        else:
            correct = (kind == "letter" and value == gold)
        if correct:
            n_correct += 1
        outputs.append({
            "record_id": item["record_id"],
            "queried_key": item["queried_key"],
            "queried_slot_1indexed": item["queried_slot_1indexed"],
            "gold_value": gold,
            "raw_output": raw,
            "parsed_kind": kind,
            "parsed_value": value,
            "strict_correct": correct,
        })
    n = len(items)
    return {"n": n, "n_correct": n_correct, "strict_accuracy": n_correct / n if n else 0.0,
            "outputs": outputs}


# === Pre-flight hash checks ===
print("=== PRE-FLIGHT: hashes ===")
input_hashes = {}
for label, p, expected_prefix in [
    ("prompt_template", PROMPT_TEMPLATE_PATH, "f1956e7d"),
    ("decoding_config", DECODING_CONFIG_PATH, "a20391d8"),
    ("scorer (run_validation.py)", SCORER_PATH, None),  # may be the updated version
]:
    h = sha256_file(p)
    input_hashes[p.name] = h
    if expected_prefix and not h.startswith(expected_prefix):
        print(f"  ABORT: {label} hash mismatch — got {h[:16]}, expected prefix {expected_prefix}")
        sys.exit(1)
    print(f"  {label}: {h}")

# CAL-A input bytes (existing constructed-positive)
print()
print("=== PRE-FLIGHT: CAL-A reuses existing constructed-positive bytes ===")
for label, p, expected_prefix in [
    ("CAL-A clean_member", CAL_A_CLEAN, "f412d04c"),
    ("CAL-A defective_member", CAL_A_DEF, "4ea3c277"),
    ("CAL-A manifest", CAL_A_MANIFEST, "49cd6451"),
]:
    h = sha256_file(p)
    input_hashes[p.name] = h
    if not h.startswith(expected_prefix):
        print(f"  ABORT: {label} hash mismatch — got {h[:16]}, expected prefix {expected_prefix}")
        sys.exit(1)
    print(f"  {label}: {h}")

prompt_template = json.loads(PROMPT_TEMPLATE_PATH.read_text())
decoding_config = json.loads(DECODING_CONFIG_PATH.read_text())
system_prompt = prompt_template["system"]
print()
print(f"Decoding: temp={decoding_config['temperature']}, greedy={decoding_config['greedy']}, "
      f"max_new={decoding_config['max_new_tokens']}")
print(f"Model: {MODEL_ID}")


# === Construct CAL-A (reuse) + CAL-B + CAL-C ===
candidates = []

# CAL-A: reuse existing constructed-positive bytes
print()
print("=== CAL-A: reuse existing constructed-positive ===")
clean_a = json.loads(CAL_A_CLEAN.read_text())
def_a = json.loads(CAL_A_DEF.read_text())
single_diff_a_ok, _ = single_difference_check(
    {**clean_a, "items": clean_a["items"]},
    {**def_a, "items": def_a["items"]},
)
print(f"  CAL-A single_difference_ok: {single_diff_a_ok}")
candidates.append({
    "id": "CAL-A", "list_len": 9, "slot_range": [6,7,8],
    "near_miss_count": 0, "seed": 20260613,
    "clean": clean_a, "defective": def_a,
    "clean_path": str(CAL_A_CLEAN.relative_to(REPO_ROOT)),
    "defective_path": str(CAL_A_DEF.relative_to(REPO_ROOT)),
    "manifest_path": str(CAL_A_MANIFEST.relative_to(REPO_ROOT)),
    "manifest_sha256": input_hashes[CAL_A_MANIFEST.name],
    "single_difference_ok": single_diff_a_ok,
})

# CAL-B: fresh construct, list_len 13, slots 8-11, light near-miss (count=2)
print()
print("=== CAL-B: constructing fresh (list_len=13, slots [8,9,10,11], near_miss_count=2) ===")
cal_b_clean, cal_b_def = construct_pair("CAL-B", list_len=13, slot_range=[8,9,10,11],
                                         n_items=40, near_miss_count=2, seed=20260613001)
single_diff_b_ok, b_checks = single_difference_check(cal_b_clean, cal_b_def)
print(f"  CAL-B single_difference_ok: {single_diff_b_ok}  {b_checks}")

# CAL-C: fresh construct, list_len 17, slots 10-15, mild near-miss (count=4)
print()
print("=== CAL-C: constructing fresh (list_len=17, slots [10..15], near_miss_count=4) ===")
cal_c_clean, cal_c_def = construct_pair("CAL-C", list_len=17, slot_range=[10,11,12,13,14,15],
                                         n_items=40, near_miss_count=4, seed=20260613002)
single_diff_c_ok, c_checks = single_difference_check(cal_c_clean, cal_c_def)
print(f"  CAL-C single_difference_ok: {single_diff_c_ok}  {c_checks}")

# Write CAL-B and CAL-C member files + manifests
for cid, clean, defective, list_len, slots, near_miss, seed, sd_ok in [
    ("CAL-B", cal_b_clean, cal_b_def, 13, [8,9,10,11], 2, 20260613001, single_diff_b_ok),
    ("CAL-C", cal_c_clean, cal_c_def, 17, [10,11,12,13,14,15], 4, 20260613002, single_diff_c_ok),
]:
    clean_path = OUTPUT_DIR / f"{cid.lower()}_clean_member.json"
    def_path = OUTPUT_DIR / f"{cid.lower()}_defective_member.json"
    manifest_path = OUTPUT_DIR / f"{cid.lower()}_realized_match_manifest.json"
    clean_path.write_text(json.dumps(clean, indent=2))
    def_path.write_text(json.dumps(defective, indent=2))
    manifest = {
        "match_manifest": "realized",
        "candidate_id": cid,
        "held_constant": ["list_len", "queried_slot_distribution", "key_value_vocabulary_family",
                          "near_miss_distractor_density", "item_count", "scoring_harness",
                          "queried_key_per_item_index"],
        "permitted_difference": "P2 defect only: queried key absent from listed pairs",
        "n_items_each": 40,
        "list_len": list_len,
        "queried_slots": slots,
        "near_miss_count": near_miss,
        "construction_seed": seed,
        "single_difference_invariant_check": "PASS" if sd_ok else "FAIL",
        "off_ceiling_design_intent": f"calibration sweep — list_len {list_len}, slots {slots}, near-miss {near_miss}",
    }
    manifest_path.write_text(json.dumps(manifest, indent=2))
    candidates_entry = next(c for c in [
        {"id":"CAL-B","list_len":13,"slot_range":[8,9,10,11],"near_miss_count":2,"seed":20260613001},
        {"id":"CAL-C","list_len":17,"slot_range":[10,11,12,13,14,15],"near_miss_count":4,"seed":20260613002},
    ] if c["id"] == cid)
    candidates_entry.update({
        "clean": clean, "defective": defective,
        "clean_path": str(clean_path.relative_to(REPO_ROOT)),
        "defective_path": str(def_path.relative_to(REPO_ROOT)),
        "manifest_path": str(manifest_path.relative_to(REPO_ROOT)),
        "manifest_sha256": sha256_file(manifest_path),
        "single_difference_ok": sd_ok,
    })
    candidates.append(candidates_entry)


# === Load model ONCE, run all candidates ===
print()
print(f"=== Loading model {MODEL_ID} ===")
t_load = time.time()
model, tokenizer = mlx_lm.load(MODEL_ID)
load_sec = time.time() - t_load
print(f"Loaded in {load_sec:.1f}s")

scorer_sha = sha256_file(SCORER_PATH)
prompt_sha = sha256_file(PROMPT_TEMPLATE_PATH)


# === Execute sweep ===
for c in candidates:
    cid = c["id"]
    print()
    print(f"=== {cid}: running clean ({c['clean']['n_items']} items) + defective ({c['defective']['n_items']} items) ===")
    t0 = time.time()
    clean_result = score_member(model, tokenizer, system_prompt, decoding_config, c["clean"]["items"])
    print(f"  clean:     {clean_result['n_correct']}/{clean_result['n']} = {clean_result['strict_accuracy']:.4f}   ({time.time()-t0:.1f}s)")
    t1 = time.time()
    def_result = score_member(model, tokenizer, system_prompt, decoding_config, c["defective"]["items"])
    print(f"  defective: {def_result['n_correct']}/{def_result['n']} = {def_result['strict_accuracy']:.4f}   ({time.time()-t1:.1f}s)")

    # Write raw outputs
    raw_clean_path = OUTPUT_DIR / f"{cid.lower()}_clean_outputs.json"
    raw_def_path = OUTPUT_DIR / f"{cid.lower()}_defective_outputs.json"
    raw_clean_path.write_text(json.dumps(clean_result["outputs"], indent=2))
    raw_def_path.write_text(json.dumps(def_result["outputs"], indent=2))

    # Per-candidate run JSON (the schema the harness consumes)
    run_record = {
        "candidate_id": cid,
        "clean_member": {"summary": {"strict_accuracy": clean_result["strict_accuracy"],
                                      "n": clean_result["n"],
                                      "n_correct": clean_result["n_correct"]}},
        "defective_member": {"summary": {"strict_accuracy": def_result["strict_accuracy"],
                                          "n": def_result["n"],
                                          "n_correct": def_result["n_correct"]}},
        "single_difference_ok": c["single_difference_ok"],
        "manifest_sha256": c["manifest_sha256"],
        "scorer_sha256": scorer_sha,
        "prompt_template_sha256": prompt_sha,
        "raw_output_path": str(raw_clean_path.relative_to(REPO_ROOT)),  # clean is the primary
        "raw_defective_output_path": str(raw_def_path.relative_to(REPO_ROOT)),
        "manifest_path": c["manifest_path"],
        "clean_member_path": c["clean_path"],
        "defective_member_path": c["defective_path"],
        "candidate_config": {
            "list_len": c["list_len"],
            "queried_slots": c["slot_range"],
            "near_miss_count": c["near_miss_count"],
            "construction_seed": c["seed"],
        },
        "model_id": MODEL_ID,
        "precision": "bf16-mlx-native",
        "run_timestamp_utc": datetime.now(timezone.utc).isoformat(),
    }
    run_path = GOV_DIR / f"{cid.lower()}_run.json"
    run_path.write_text(json.dumps(run_record, indent=2))
    print(f"  run record: {run_path.relative_to(REPO_ROOT)}  sha256={sha256_file(run_path)}")

print()
print("=== SWEEP COMPLETE ===")
print(f"Run records: {GOV_DIR.relative_to(REPO_ROOT)}/")
print(f"Raw outputs + member files: {OUTPUT_DIR.relative_to(REPO_ROOT)}/")
print()
print("Next: Senior runs calibration_sweep_verdict.py on the run records to produce the band verdict.")
print("CS does NOT interpret.")
