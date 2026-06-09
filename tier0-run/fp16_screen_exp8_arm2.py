#!/usr/bin/env python3
"""
fp16_screen_exp8_arm2.py — FP16 feasibility screen for Exp8 Arm 2 (n=8).

Runs each item once at FP16, scores with score_arm2_content + score_arm2_format,
writes full provenance JSON, prints per-item packet to stdout.

Feasibility criterion: ≥7/8 content PASS (RETURNED_TARGET_OBJ).
"""

import hashlib
import json
import sys
import time
from pathlib import Path

try:
    from mlx_lm import load, generate
    from mlx_lm.sample_utils import make_sampler
except ImportError:
    raise SystemExit("mlx-lm not found. Install with: pip install mlx-lm")

sys.path.insert(0, str(Path(__file__).parent))
from tasks_exp8 import ITEMS, score_arm2_content, score_arm2_format, get_manifest_hash

MODEL_ID       = "Qwen/Qwen2.5-1.5B-Instruct"
APPROVED_HASH  = "sha256:14129d0bfe2cae1c3e4d817a8423eaf5513665741c04f1d388ac8da34a9074de"
FEASIBILITY_N  = 7   # ≥7/8 required
DECODING       = {"temperature": 0.0, "max_tokens": 16}


def run_prompt(model, tokenizer, prompt: str, max_tokens: int = 16) -> str:
    if tokenizer.chat_template is not None:
        messages = [{"role": "user", "content": prompt}]
        formatted = tokenizer.apply_chat_template(messages, add_generation_prompt=True)
    else:
        formatted = prompt
    return generate(
        model, tokenizer, prompt=formatted,
        max_tokens=max_tokens,
        sampler=make_sampler(temp=0.0),
        verbose=False,
    )


def main():
    # ── Hash gate ────────────────────────────────────────────────────────────
    manifest_hash = get_manifest_hash()
    if manifest_hash != APPROVED_HASH:
        raise SystemExit(
            f"[ABORT] Manifest hash mismatch.\n"
            f"  computed: {manifest_hash}\n"
            f"  approved: {APPROVED_HASH}\n"
            "Tasks file was modified after approval. Do not proceed."
        )

    screen_ts = int(time.time())

    print(f"=== Exp8 Arm 2 — FP16 Feasibility Screen ===")
    print(f"Model:           {MODEL_ID}")
    print(f"Manifest hash:   {manifest_hash}  [MATCH]")
    print(f"n_items:         {len(ITEMS)}")
    print(f"fresh_generation: True")
    print(f"decoding:        temp={DECODING['temperature']}, max_tokens={DECODING['max_tokens']}")
    print(f"feasibility:     ≥{FEASIBILITY_N}/{len(ITEMS)}\n")

    # ── Load model ───────────────────────────────────────────────────────────
    print(f"=== loading {MODEL_ID} at FP16 ===")
    model, tokenizer = load(MODEL_ID)
    print()

    # ── Run items ────────────────────────────────────────────────────────────
    results = []
    pass_count = 0

    for item in ITEMS:
        pid = item["id"]
        ts  = int(time.time())

        raw_output = run_prompt(model, tokenizer, item["prompt"], DECODING["max_tokens"])

        c = score_arm2_content(raw_output, item)
        f = score_arm2_format(raw_output)

        is_pass = c["is_correct"]
        if is_pass:
            pass_count += 1

        print(f"--- {pid}  target_pos={item['target_pos']} ---")
        print(f"  target_subj:            {item['target_subj']}")
        print(f"  target_obj:             {item['target_obj']}")
        print(f"  raw_output:             {raw_output!r}")
        print(f"  content_class:          {c['content_class']}")
        print(f"  format_class:           {f['format_class']}")
        print(f"  returned_token:         {c['returned_token']}")
        print(f"  returned_token_role:    {c['returned_token_role']}")
        print(f"  returned_fact_position: {c['returned_fact_position']}")
        print(f"  same_error_identity:    {c['same_error_identity_key']}")
        print(f"  PASS: {is_pass}")
        print()

        results.append({
            "id":                      pid,
            "target_pos":              item["target_pos"],
            "target_subj":             item["target_subj"],
            "target_obj":              item["target_obj"],
            "prompt":                  item["prompt"],
            "raw_output":              raw_output,
            "content_class":           c["content_class"],
            "format_class":            f["format_class"],
            "returned_token":          c["returned_token"],
            "returned_token_role":     c["returned_token_role"],
            "returned_fact_position":  c["returned_fact_position"],
            "same_error_identity_key": c["same_error_identity_key"],
            "same_wrong_token_count":  c["same_wrong_token_count"],
            "same_wrong_position_count": c["same_wrong_position_count"],
            "is_correct":              is_pass,
            "timestamp":               ts,
        })

    # ── Summary ──────────────────────────────────────────────────────────────
    feasible = pass_count >= FEASIBILITY_N
    print(f"=== SUMMARY ===")
    print(f"Arm 2 FP16 pass count: {pass_count}/{len(ITEMS)}")
    print(f"Feasibility criterion: ≥{FEASIBILITY_N}/{len(ITEMS)}")
    print(f"Result: {'[FEASIBLE] Construction verified.' if feasible else '[NOT FEASIBLE] Threshold not met.'}")

    # Content class breakdown
    class_counts: dict[str, int] = {}
    for r in results:
        cc = r["content_class"]
        class_counts[cc] = class_counts.get(cc, 0) + 1
    print(f"\nContent class breakdown:")
    for cc, n in sorted(class_counts.items()):
        print(f"  {cc}: {n}")

    # ── Write JSON ───────────────────────────────────────────────────────────
    out_path = Path(f"fp16_screen_exp8_arm2_{screen_ts}.json")
    out_data = {
        "experiment":          "Exp8",
        "arm":                 2,
        "model":               MODEL_ID,
        "bits":                16,
        "manifest_hash":       manifest_hash,
        "approved_hash":       APPROVED_HASH,
        "hash_match":          manifest_hash == APPROVED_HASH,
        "fresh_generation":    True,
        "decoding":            DECODING,
        "screen_timestamp":    screen_ts,
        "n_items":             len(ITEMS),
        "pass_count":          pass_count,
        "feasibility_threshold": FEASIBILITY_N,
        "feasible":            feasible,
        "results":             results,
    }
    out_path.write_text(json.dumps(out_data, indent=2))
    print(f"\nWrote: {out_path}")


if __name__ == "__main__":
    main()
