#!/usr/bin/env python3
"""
fp16_screen_exp8b.py — FP16 feasibility screen for Exp8B (n=8).

Exp8B is a single-variable wording test on exact Exp8A items.
Only the query wording changed:
  Exp8A: "Which value is associated with SUBJ_T?"
  Exp8B: "Which token is assigned to SUBJ_T?"

Scoring: three-axis (scaffold_class / format_class / content_class),
  unchanged from Exp8A amendment.

Feasibility criterion:
  1. FP16 Arm 2B content pass count >=7/8
  2. Zero numeric out-of-context returns (ANSWER: 0, ANSWER: 10, etc.)

Scope limits: no n>=20, no INT8/INT4, no seam claim, no Exp8C.
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
from tasks_exp8b import ITEMS, score_arm2_content, score_arm2_format, score_arm2_scaffold, get_manifest_hash

MODEL_ID      = "Qwen/Qwen2.5-1.5B-Instruct"
APPROVED_HASH = "sha256:695b1ac90aa0745765f9785435f527757a248f4ad27a85ce8f249230610ec56e"
FEASIBILITY_N = 7    # >=7/8 required
DECODING      = {"temperature": 0.0, "max_tokens": 16}


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

    print(f"=== Exp8B — FP16 Feasibility Screen ===")
    print(f"Model:            {MODEL_ID}")
    print(f"Manifest hash:    {manifest_hash}  [MATCH]")
    print(f"n_items:          {len(ITEMS)}")
    print(f"fresh_generation: True")
    print(f"decoding:         temp={DECODING['temperature']}, max_tokens={DECODING['max_tokens']}")
    print(f"feasibility:      >={FEASIBILITY_N}/{len(ITEMS)} content PASS AND zero numeric OOC\n")

    # ── Load model ───────────────────────────────────────────────────────────
    print(f"=== loading {MODEL_ID} at FP16 ===")
    model, tokenizer = load(MODEL_ID)
    print()

    # ── Run items ────────────────────────────────────────────────────────────
    results = []
    pass_count = 0
    numeric_ooc_count = 0

    for item in ITEMS:
        pid = item["id"]
        ts  = int(time.time())

        raw_output = run_prompt(model, tokenizer, item["prompt"], DECODING["max_tokens"])

        sc = score_arm2_scaffold(raw_output)
        f  = score_arm2_format(raw_output)
        c  = score_arm2_content(raw_output, item)

        is_pass = c["is_correct"]
        if is_pass:
            pass_count += 1

        # Numeric OOC: scaffold present, format fail, token not in context and not alpha-only
        is_numeric_ooc = (
            sc["scaffold_class"] == "SCAFFOLD_PRESENT"
            and f["format_class"] == "FORMAT_FAIL"
            and c["content_class"] == "RETURNED_NON_CONTEXT_TOKEN"
            and c["returned_token"] is not None
            and not str(c["returned_token"]).isalpha()
        )
        if is_numeric_ooc:
            numeric_ooc_count += 1

        print(f"--- {pid}  target_pos={item['target_pos']} ---")
        print(f"  prompt (query line): {item['prompt'].split(chr(10)+chr(10))[1]}")
        print(f"  raw_output:             {raw_output!r}")
        print(f"  scaffold_class:         {sc['scaffold_class']}")
        print(f"  format_class:           {f['format_class']}")
        print(f"  content_class:          {c['content_class']}")
        print(f"  returned_token:         {c['returned_token']}")
        print(f"  returned_token_role:    {c['returned_token_role']}")
        print(f"  returned_fact_position: {c['returned_fact_position']}")
        print(f"  same_error_identity:    {c['same_error_identity_key']}")
        print(f"  numeric_ooc:            {is_numeric_ooc}")
        print(f"  PASS: {is_pass}")
        print()

        results.append({
            "id":                       pid,
            "target_pos":               item["target_pos"],
            "target_subj":              item["target_subj"],
            "target_obj":               item["target_obj"],
            "prompt":                   item["prompt"],
            "prompt_hash":              item["prompt_hash"],
            "raw_output":               raw_output,
            "scaffold_class":           sc["scaffold_class"],
            "format_class":             f["format_class"],
            "content_class":            c["content_class"],
            "returned_token":           c["returned_token"],
            "returned_token_role":      c["returned_token_role"],
            "returned_fact_position":   c["returned_fact_position"],
            "same_error_identity_key":  c["same_error_identity_key"],
            "same_wrong_token_count":   c["same_wrong_token_count"],
            "same_wrong_position_count": c["same_wrong_position_count"],
            "is_numeric_ooc":           is_numeric_ooc,
            "is_correct":               is_pass,
            "timestamp":                ts,
        })

    # ── Pass condition evaluation ─────────────────────────────────────────────
    cond1_met = pass_count >= FEASIBILITY_N
    cond2_met = numeric_ooc_count == 0
    feasible  = cond1_met and cond2_met

    # ── Summary ──────────────────────────────────────────────────────────────
    print(f"=== SUMMARY ===")
    print(f"Arm 2B FP16 pass count:    {pass_count}/{len(ITEMS)}")
    print(f"Feasibility criterion 1:   >={FEASIBILITY_N}/{len(ITEMS)} content PASS  →  {'MET' if cond1_met else 'NOT MET'}")
    print(f"Numeric OOC count:         {numeric_ooc_count}")
    print(f"Feasibility criterion 2:   zero numeric OOC  →  {'MET' if cond2_met else 'NOT MET'}")
    print(f"Result: {'[FEASIBLE] Both conditions met.' if feasible else '[NOT FEASIBLE] One or more conditions failed.'}")

    # Content class breakdown
    class_counts: dict[str, int] = {}
    for r in results:
        cc = r["content_class"]
        class_counts[cc] = class_counts.get(cc, 0) + 1
    print(f"\nContent class breakdown:")
    for cc, n in sorted(class_counts.items()):
        print(f"  {cc}: {n}")

    # ── Write JSON ───────────────────────────────────────────────────────────
    out_path = Path(f"fp16_screen_exp8b_{screen_ts}.json")
    out_data = {
        "experiment":           "Exp8B",
        "arm":                  "2B",
        "model":                MODEL_ID,
        "bits":                 16,
        "manifest_hash":        manifest_hash,
        "approved_hash":        APPROVED_HASH,
        "hash_match":           manifest_hash == APPROVED_HASH,
        "fresh_generation":     True,
        "decoding":             DECODING,
        "screen_timestamp":     screen_ts,
        "n_items":              len(ITEMS),
        "pass_count":           pass_count,
        "numeric_ooc_count":    numeric_ooc_count,
        "feasibility_threshold": FEASIBILITY_N,
        "cond1_content_pass":   cond1_met,
        "cond2_zero_numeric_ooc": cond2_met,
        "feasible":             feasible,
        "results":              results,
    }
    out_path.write_text(json.dumps(out_data, indent=2))
    print(f"\nWrote: {out_path}")


if __name__ == "__main__":
    main()
