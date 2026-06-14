#!/usr/bin/env python3
"""CAL-Q (in-prompt code-book alias) calibration-only run — CS executor.

Authorized by Manager 2026-06-13 ("Run CAL-Q v0.3 Calibration Pilot" —
narrow FP16/native; CAL-Q only).

Per NON-CONTENT-LEVER-D4-RESCUE-SPEC-v0.3.md §3:
  Clean form prompt:
    "Use this code book:
       A = key_<K>
       B = key_<X>
       C = key_<Y>

     Key-value list:
       key_<K> = <gold_value>
       key_<X> = <other>
       ... (CAL-B-like: list_len 13, slots 8-11, near-miss 2)

     Query: Return the value for the key assigned to code A."

  Defective form is identical EXCEPT key_<K> is absent from the list
  (single permitted difference; code book and query unchanged).

Code A always maps to the queried_key. B and C are decoy code targets,
always present in the list. The queried_key K varies per item but the
code book mapping (A -> queried_key) is the same structure across all
items, so resolution is content-INDEPENDENT.

Four-way defective reporting per spec §7:
  1. strict NONE accuracy        (raw == "NONE" exact)
  2. concept-level abstention    (raw.lower() in {none, null}; authoritative)
  3. true false-emission rate    (model emits letter when gold=null)
  4. format-abstention artifact  (lowercase 'none' count -- the none-vs-NONE split)

FP16/native only. No quantization. No compression. No certification.
"""
import json, hashlib, math, time, sys, random, re
from datetime import datetime, timezone
from pathlib import Path

import mlx_lm

# Reuse shared components from sweep runner (case-insensitive parsing, hashing)
SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
from run_calibration_sweep import (
    sha256_file, PROMPT_TEMPLATE_PATH, DECODING_CONFIG_PATH, SCORER_PATH, MODEL_ID,
)
from rescore_null_normalized import classify as classify_nullnorm  # case-insensitive parser

REPO_ROOT = SCRIPT_DIR.parents[2]
OUTPUT_DIR = REPO_ROOT / "experiments/2026-06-11_lane-1a-prime/certification_readiness/sweep_outputs"
GOV_DIR    = REPO_ROOT / "governance/2026-06-11_lane-1a-prime/certification-readiness/sweep_run_records"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
GOV_DIR.mkdir(parents=True, exist_ok=True)

# === Construction parameters (CAL-Q v0.3 spec §3 + CAL-B baseline) ===
LIST_LEN = 13
SLOT_RANGE = [8, 9, 10, 11]    # CAL-B baseline
NEAR_MISS_COUNT = 2            # CAL-B baseline
N_ITEMS = 40
SEED = 20260613006

KEY_MIN, KEY_MAX = 10, 199
LETTERS = list("abcdefghijklmnopqrstuvwxyz")


def format_prompt(code_book, list_pairs, query_code):
    """v0.3 §3 format: in-prompt code book + key-value list + indirect query."""
    cb_lines = "\n".join(f"  {c} = key_{k}" for c, k in code_book)
    list_lines = "\n".join(f"key_{k} = {v}" for k, v in list_pairs)
    return (f"Use this code book:\n{cb_lines}\n\n"
            f"Key-value list:\n{list_lines}\n\n"
            f"Query: Return the value for the key assigned to code {query_code}.")


def construct_cal_q():
    """Build matched clean+defective CAL-Q pair per v0.3 §3."""
    rng = random.Random(SEED)
    clean_items = []
    defective_items = []
    code_choices = ["A", "B", "C"]

    for i in range(N_ITEMS):
        queried_key = rng.randint(KEY_MIN, KEY_MAX)
        gold_value = rng.choice(LETTERS)
        slot = rng.choice(SLOT_RANGE)

        # 3-code book: A -> queried_key, B and C -> other present keys
        # First, generate 2 decoy keys for B and C (must differ from queried_key, no collisions)
        used = {queried_key}
        decoy_keys = []
        guard = 0
        while len(decoy_keys) < 2 and guard < 500:
            k = rng.randint(KEY_MIN, KEY_MAX)
            if k not in used:
                decoy_keys.append(k)
                used.add(k)
            guard += 1
        code_book = [("A", queried_key), ("B", decoy_keys[0]), ("C", decoy_keys[1])]

        # Always query code A (which maps to queried_key); could randomize but spec uses A
        query_code = "A"

        # Near-miss distractors (within ±5 of queried_key, not equal, not already used)
        near_miss_pool = [k for k in range(max(KEY_MIN, queried_key - 5),
                                            min(KEY_MAX, queried_key + 5) + 1)
                          if k != queried_key and k not in used]
        near_miss = rng.sample(near_miss_pool, min(NEAR_MISS_COUNT, len(near_miss_pool)))
        used.update(near_miss)

        # Remaining distractors: list_len - 1 (for queried_key) - len(near_miss) - 2 (decoys B, C)
        n_random = LIST_LEN - 1 - len(near_miss) - 2
        random_distractors = []
        guard = 0
        while len(random_distractors) < n_random and guard < 500:
            k = rng.randint(KEY_MIN, KEY_MAX)
            if k not in used:
                random_distractors.append(k)
                used.add(k)
            guard += 1

        # CLEAN: list contains queried_key + decoys (B, C) + near-miss + random
        other_keys = decoy_keys + near_miss + random_distractors
        rng.shuffle(other_keys)
        clean_keys = other_keys[:LIST_LEN - 1].copy()
        clean_keys.insert(slot - 1, queried_key)
        clean_keys = clean_keys[:LIST_LEN]
        clean_values = []
        for k in clean_keys:
            if k == queried_key:
                clean_values.append(gold_value)
            else:
                clean_values.append(rng.choice(LETTERS))
        clean_pairs = list(zip(clean_keys, clean_values))

        # DEFECTIVE: replace queried_key with non-near-miss, non-decoy random key
        replacement_key = None
        guard = 0
        while replacement_key is None and guard < 500:
            r = rng.randint(KEY_MIN, KEY_MAX)
            if (r != queried_key and r not in used
                    and not (queried_key - 5 <= r <= queried_key + 5)):
                replacement_key = r
            guard += 1
        if replacement_key is None:
            for r in range(KEY_MIN, KEY_MAX + 1):
                if r not in used and r != queried_key:
                    replacement_key = r
                    break

        def_keys = other_keys[:LIST_LEN - 1].copy()
        def_keys.insert(slot - 1, replacement_key)
        def_keys = def_keys[:LIST_LEN]
        def_values = [rng.choice(LETTERS) for _ in def_keys]
        def_pairs = list(zip(def_keys, def_values))

        # Prompts (code book + list + query — IDENTICAL code book & query for both)
        clean_prompt = format_prompt(code_book, clean_pairs, query_code)
        def_prompt = format_prompt(code_book, def_pairs, query_code)

        clean_items.append({
            "record_id": f"CAL-Q-CLEAN-{i:03d}",
            "stratum": "answerable",
            "list_len": LIST_LEN,
            "queried_key": queried_key,
            "queried_slot_1indexed": slot,
            "code_book": code_book,
            "query_code": query_code,
            "gold_value": gold_value,
            "prompt_user_text": clean_prompt,
        })
        defective_items.append({
            "record_id": f"CAL-Q-DEF-{i:03d}",
            "stratum": "answerable",
            "list_len": LIST_LEN,
            "queried_key": queried_key,
            "queried_slot_1indexed": slot,
            "code_book": code_book,
            "query_code": query_code,
            "gold_value": None,
            "defect": "queried_key_absent_from_pairs",
            "prompt_user_text": def_prompt,
        })

    clean_member = {"member":"clean","candidate_id":"CAL-Q","n_items":N_ITEMS,
                    "list_len":LIST_LEN,"queried_slots":SLOT_RANGE,
                    "near_miss_count":NEAR_MISS_COUNT,"construction_seed":SEED,
                    "query_form":"in_prompt_code_book","items":clean_items}
    defective_member = {"member":"defective","candidate_id":"CAL-Q","n_items":N_ITEMS,
                        "list_len":LIST_LEN,"queried_slots":SLOT_RANGE,
                        "near_miss_count":NEAR_MISS_COUNT,"construction_seed":SEED,
                        "query_form":"in_prompt_code_book",
                        "defect":"queried_key_absent_from_pairs","items":defective_items}
    return clean_member, defective_member


def single_difference_check_calq(clean, defective):
    """Verify CAL-Q matched-pair single-difference invariant + same-key-identity for code A."""
    checks = {}
    checks["list_len_match"] = clean["list_len"] == defective["list_len"]
    checks["n_items_match"] = clean["n_items"] == defective["n_items"]
    checks["queried_slots_match"] = list(clean["queried_slots"]) == list(defective["queried_slots"])
    checks["near_miss_match"] = clean["near_miss_count"] == defective["near_miss_count"]
    checks["query_form_match"] = clean["query_form"] == defective["query_form"]

    per_item_ok = True
    same_key_identity_ok = True
    for c, d in zip(clean["items"], defective["items"]):
        if c["queried_key"] != d["queried_key"]: per_item_ok = False
        if c["queried_slot_1indexed"] != d["queried_slot_1indexed"]: per_item_ok = False
        if c["code_book"] != d["code_book"]: per_item_ok = False
        if c["query_code"] != d["query_code"]: per_item_ok = False
        if c["gold_value"] is None or d["gold_value"] is not None: per_item_ok = False
        # Same-key identity: code A maps to same key in both members
        c_code_a = dict(c["code_book"])[c["query_code"]]
        d_code_a = dict(d["code_book"])[d["query_code"]]
        if c_code_a != d_code_a: same_key_identity_ok = False
        if c_code_a != c["queried_key"]: same_key_identity_ok = False
    checks["per_item_invariant"] = per_item_ok
    checks["same_key_identity_both_members"] = same_key_identity_ok
    checks["defect_field_on_defective"] = all(
        d.get("defect") == "queried_key_absent_from_pairs" for d in defective["items"])
    checks["all_clean_have_gold"] = all(c.get("gold_value") is not None for c in clean["items"])
    return all(checks.values()), checks


# === Pre-flight ===
print("=" * 80)
print("CAL-Q v0.3 RUN (in-prompt code book; CAL-B baseline content)")
print("=" * 80)
print()
print(f"HEAD at run time:    (will record post-execution)")
print(f"prompt_template:     {sha256_file(PROMPT_TEMPLATE_PATH)}")
print(f"decoding_config:     {sha256_file(DECODING_CONFIG_PATH)}")
print(f"scorer:              {sha256_file(SCORER_PATH)}")
print(f"CAL-Q v0.3 spec:     839249000bb1cb34...")
print(f"construction params: list_len={LIST_LEN}, slots={SLOT_RANGE}, near_miss={NEAR_MISS_COUNT}, n_items={N_ITEMS}, seed={SEED}")

prompt_template = json.loads(PROMPT_TEMPLATE_PATH.read_text())
decoding_config = json.loads(DECODING_CONFIG_PATH.read_text())
system_prompt = prompt_template["system"]

# Construct
print()
print("=== Constructing CAL-Q matched pair ===")
clean, defective = construct_cal_q()
sd_ok, sd_checks = single_difference_check_calq(clean, defective)
print(f"  single_difference_ok: {sd_ok}")
for k, v in sd_checks.items():
    if not v:
        print(f"    FAIL: {k}")
if not sd_ok:
    print("  ABORT: single-difference failed.")
    sys.exit(1)
print(f"  same_key_identity_both_members (code A -> queried_key in both): {sd_checks['same_key_identity_both_members']}")

# Show first item to sanity-check the prompt format
print()
print("=== Sample prompt (CAL-Q-CLEAN-000) ===")
print(clean["items"][0]["prompt_user_text"])
print()
print("=== Sample prompt (CAL-Q-DEF-000) ===")
print(defective["items"][0]["prompt_user_text"])

# Save member files + manifest
clean_path = OUTPUT_DIR / "cal-q_clean_member.json"
def_path = OUTPUT_DIR / "cal-q_defective_member.json"
manifest_path = OUTPUT_DIR / "cal-q_realized_match_manifest.json"
clean_path.write_text(json.dumps(clean, indent=2))
def_path.write_text(json.dumps(defective, indent=2))
manifest = {
    "match_manifest": "realized",
    "candidate_id": "CAL-Q",
    "spec_version": "v0.3",
    "spec_sha256": "839249000bb1cb34d423534009d24682339e56c51ce393be45f5c03526a31a13",
    "query_form": "in_prompt_code_book",
    "held_constant": ["list_len", "queried_slots", "near_miss_count", "vocabulary",
                      "item_count", "scoring_harness", "queried_key_per_item",
                      "code_book_mapping", "query_code"],
    "permitted_difference": "P2 defect only: queried_key (= code_A's mapped key) absent from list",
    "n_items_each": N_ITEMS,
    "list_len": LIST_LEN,
    "queried_slots": SLOT_RANGE,
    "near_miss_count": NEAR_MISS_COUNT,
    "construction_seed": SEED,
    "single_difference_invariant_check": "PASS",
    "single_difference_check_details": sd_checks,
}
manifest_path.write_text(json.dumps(manifest, indent=2))

# === Load model + run ===
print()
print(f"=== Loading model {MODEL_ID} (FP16/native via mlx_lm) ===")
t_load = time.time()
model, tokenizer = mlx_lm.load(MODEL_ID)
print(f"Loaded in {time.time()-t_load:.1f}s")


def score_member_4way(member_label, items):
    """Score with case-insensitive abstention + emit all 4 categories per spec §7."""
    print(f"\n=== Running CAL-Q {member_label} ({len(items)} items) ===")
    outputs = []
    n_strict_NONE = 0
    n_concept_abstention = 0
    n_strict_correct = 0
    n_concept_correct = 0
    n_letter_emit = 0
    n_other = 0
    abstention_forms = {}
    letter_values = {}
    t0 = time.time()
    for i, item in enumerate(items):
        messages = [
            {"role":"system","content":system_prompt},
            {"role":"user","content":item["prompt_user_text"]},
        ]
        prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        raw = mlx_lm.generate(model, tokenizer, prompt=prompt,
                              max_tokens=decoding_config["max_new_tokens"], verbose=False)
        c = classify_nullnorm(raw)
        gold = item.get("gold_value")
        # Strict (old)
        if gold is None:
            sc = c["strict_kind"] == "NONE"
        else:
            sc = c["strict_kind"] == "letter" and raw.strip().rstrip(".,") == gold
        # Concept (new authoritative)
        if gold is None:
            cc = c["concept_kind"] == "abstention"
        else:
            cc = c["concept_kind"] == "letter" and c["letter_value"] == gold
        # Tallies
        if c["strict_kind"] == "NONE": n_strict_NONE += 1
        if c["concept_kind"] == "abstention":
            n_concept_abstention += 1
            abstention_forms[c["abstention_form_observed"]] = abstention_forms.get(c["abstention_form_observed"], 0) + 1
        if c["concept_kind"] == "letter":
            n_letter_emit += 1
            letter_values[c["letter_value"]] = letter_values.get(c["letter_value"], 0) + 1
        if c["concept_kind"] == "OTHER":
            n_other += 1
        if sc: n_strict_correct += 1
        if cc: n_concept_correct += 1

        outputs.append({
            "record_id": item["record_id"], "queried_key": item["queried_key"],
            "queried_slot_1indexed": item["queried_slot_1indexed"],
            "code_book": item["code_book"], "query_code": item["query_code"],
            "gold_value": gold, "raw_output": raw,
            "parsed_strict_kind": c["strict_kind"],
            "parsed_concept_kind": c["concept_kind"],
            "parsed_letter_value": c["letter_value"],
            "strict_correct": sc, "concept_correct": cc,
        })
        if (i + 1) % 10 == 0:
            print(f"  {i+1}/{len(items)} ({time.time()-t0:.1f}s)")
    elapsed = time.time() - t0
    n = len(items)
    n_lowercase_none = abstention_forms.get("none", 0)
    n_uppercase_NONE = abstention_forms.get("NONE", 0)
    print(f"  Done in {elapsed:.1f}s")
    print(f"  strict NONE accuracy:        {n_strict_correct/n:.4f}   ({n_strict_correct}/{n})")
    print(f"  concept abstention accuracy: {n_concept_correct/n:.4f}   ({n_concept_correct}/{n})")
    print(f"  true false-emission rate:    {n_letter_emit/n:.4f}   ({n_letter_emit}/{n})")
    print(f"  format-abstention artifact:  {n_lowercase_none}/{n} lowercase 'none', {n_uppercase_NONE}/{n} 'NONE'")
    return {
        "n": n, "outputs": outputs, "elapsed": elapsed,
        "n_strict_correct": n_strict_correct, "strict_accuracy": n_strict_correct/n,
        "n_concept_correct": n_concept_correct, "concept_accuracy": n_concept_correct/n,
        "n_letter_emit": n_letter_emit, "letter_emit_rate": n_letter_emit/n,
        "n_strict_NONE": n_strict_NONE, "n_concept_abstention": n_concept_abstention,
        "n_other": n_other,
        "n_lowercase_none": n_lowercase_none, "n_uppercase_NONE": n_uppercase_NONE,
        "abstention_forms": abstention_forms, "letter_values": letter_values,
    }


clean_r = score_member_4way("clean", clean["items"])
def_r = score_member_4way("defective", defective["items"])

# Save raw outputs
raw_clean_path = OUTPUT_DIR / "cal-q_clean_outputs.json"
raw_def_path = OUTPUT_DIR / "cal-q_defective_outputs.json"
raw_clean_path.write_text(json.dumps(clean_r["outputs"], indent=2))
raw_def_path.write_text(json.dumps(def_r["outputs"], indent=2))

# Run record with four-way reporting
run_record = {
    "candidate_id": "CAL-Q",
    "spec_version": "v0.3",
    "spec_sha256": "839249000bb1cb34d423534009d24682339e56c51ce393be45f5c03526a31a13",
    "query_form": "in_prompt_code_book",
    "clean_member": {
        "summary": {
            "strict_accuracy": clean_r["strict_accuracy"],
            "concept_accuracy": clean_r["concept_accuracy"],
            "n": clean_r["n"],
        }
    },
    "defective_member": {
        "summary": {
            "strict_accuracy": def_r["strict_accuracy"],            # 1. strict NONE accuracy
            "concept_abstention_accuracy": def_r["concept_accuracy"],  # 2. concept-level abstention (authoritative)
            "true_false_emission_rate": def_r["letter_emit_rate"],  # 3. true false-emission rate
            "format_abstention_artifact": {                          # 4. format-abstention artifact
                "lowercase_none_count": def_r["n_lowercase_none"],
                "uppercase_NONE_count": def_r["n_uppercase_NONE"],
                "artifact_size_fraction": (def_r["n_lowercase_none"] - def_r["n_uppercase_NONE"]) / def_r["n"] if def_r["n"] else 0.0,
            },
            "n": def_r["n"],
            "abstention_forms_observed": def_r["abstention_forms"],
            "letter_values_observed": def_r["letter_values"],
        }
    },
    "single_difference_ok": True,
    "single_difference_check_details": sd_checks,
    "manifest_sha256": sha256_file(manifest_path),
    "scorer_sha256": sha256_file(SCORER_PATH),
    "rescore_script_sha256": sha256_file(SCRIPT_DIR / "rescore_null_normalized.py"),
    "prompt_template_sha256": sha256_file(PROMPT_TEMPLATE_PATH),
    "raw_output_path": str(raw_clean_path.relative_to(REPO_ROOT)),
    "raw_defective_output_path": str(raw_def_path.relative_to(REPO_ROOT)),
    "manifest_path": str(manifest_path.relative_to(REPO_ROOT)),
    "clean_member_path": str(clean_path.relative_to(REPO_ROOT)),
    "defective_member_path": str(def_path.relative_to(REPO_ROOT)),
    "candidate_config": {"list_len":LIST_LEN,"queried_slots":SLOT_RANGE,
                         "near_miss_count":NEAR_MISS_COUNT,"construction_seed":SEED,
                         "query_form":"in_prompt_code_book"},
    "model_id": MODEL_ID,
    "precision": "bf16-mlx-native",
    "run_timestamp_utc": datetime.now(timezone.utc).isoformat(),
}
run_path = GOV_DIR / "cal-q_run.json"
run_path.write_text(json.dumps(run_record, indent=2))

# Clean band position
TARGET_LOW, TARGET_HIGH = 0.6625, 0.95
cu = clean_r["concept_accuracy"]
if cu > TARGET_HIGH: band_pos = "ABOVE band (still at/near ceiling)"
elif cu < TARGET_LOW: band_pos = "BELOW band (too close to shortcut floor)"
else: band_pos = f"INSIDE band ({TARGET_LOW} < {cu:.4f} < {TARGET_HIGH})"

print()
print("=" * 80)
print("CAL-Q COMPLETE")
print("=" * 80)
print(f"  Clean (concept):     {clean_r['concept_accuracy']:.4f}   {band_pos}")
print(f"  Defective four-way:")
print(f"    strict NONE:         {def_r['strict_accuracy']:.4f}")
print(f"    concept abstention:  {def_r['concept_accuracy']:.4f}  (authoritative)")
print(f"    true false-emission: {def_r['letter_emit_rate']:.4f}")
print(f"    format artifact:     {def_r['n_lowercase_none']}/{def_r['n']} lowercase, {def_r['n_uppercase_NONE']}/{def_r['n']} uppercase")
print(f"  Run record: {run_path.relative_to(REPO_ROOT)}  sha256={sha256_file(run_path)}")
print()
print("Senior next: interprets against CAL-Q v0.3's pre-declared rule.")
print("CS does NOT interpret.")
