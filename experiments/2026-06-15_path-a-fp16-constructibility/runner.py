#!/usr/bin/env python3
"""
runner.py — Path A FP16 Constructibility Run (authorized model execution).

Per TL ACTION 2026-06-15 ("Execute Locked Path A FP16 Constructibility Run") +
Manager authorization. Route GREEN for THIS NAMED RUN ONLY. FP16-only. No INT8.
No INT4. No compression. No retry. No second run.

Reads pre-materialized prompts (prompts_rendered.json), generates FP16 outputs
for all 96 items × 4 contexts = 384 generations, writes raw E3 to fp16_raw_outputs.json.
No scoring in this script — analyze.py performs the per-item validation +
Wilson CI + decision-rule application after this completes.
"""
from __future__ import annotations

import hashlib
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parent
FP16_MODEL_ID = "Qwen/Qwen2.5-3B-Instruct"
MAX_TOKENS = 16
TEMPERATURE = 0.0


def main() -> int:
    prompts_doc = json.loads((RUN_DIR / "prompts_rendered.json").read_text())
    renderings = prompts_doc["renderings"]
    n_items = len(renderings)
    n_contexts = len(prompts_doc["contexts"])
    n_total = n_items * n_contexts

    print(f"== Path A FP16 Constructibility Run starting at "
          f"{datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')} ==", flush=True)
    print(f"   n_items={n_items} ; contexts={prompts_doc['contexts']} ; "
          f"n_total={n_total} generations", flush=True)

    import mlx_lm
    from mlx_lm import load, stream_generate
    from mlx_lm.sample_utils import make_sampler

    print(f"   loading {FP16_MODEL_ID} (mlx_lm {mlx_lm.__version__}) ...", flush=True)
    t0 = time.time()
    model, tokenizer = load(FP16_MODEL_ID)
    print(f"   loaded in {time.time() - t0:.1f}s", flush=True)

    sampler = make_sampler(temp=TEMPERATURE)
    t_start = time.time()
    results = []

    for idx, item_rendering in enumerate(renderings, 1):
        item_id = item_rendering["item_id"]
        for qt in ("composite", "hop1", "hop2", "direct_query"):
            ctx = item_rendering["contexts"][qt]
            user_prompt = ctx["prompt"]
            messages = [{"role": "user", "content": user_prompt}]
            chat_prompt = tokenizer.apply_chat_template(
                messages, add_generation_prompt=True, tokenize=False
            )
            out_parts = []
            for resp in stream_generate(model, tokenizer, chat_prompt,
                                        max_tokens=MAX_TOKENS, sampler=sampler):
                out_parts.append(resp.text)
            raw_output = "".join(out_parts)

            results.append({
                "item_id":            item_id,
                "query_type":         qt,
                "anchor":             ctx["anchor"],
                "expected_answer":    ctx["expected_answer"],
                "prompt_sha256":      ctx["prompt_sha256"],
                "chat_prompt_sha256": "sha256:" + hashlib.sha256(chat_prompt.encode()).hexdigest(),
                "raw_output":         raw_output,
            })

        if idx % 12 == 0 or idx == n_items:
            elapsed = time.time() - t_start
            rate = idx / elapsed
            eta = (n_items - idx) / rate if rate > 0 else float("inf")
            print(f"   [{idx:3d}/{n_items}] {item_id}  "
                  f"elapsed={elapsed:.0f}s  eta={eta:.0f}s", flush=True)

    out_doc = {
        "run_name":      "PATH-A-FP16-CONSTRUCTIBILITY-2026-06-15",
        "timestamp_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "model_id":      FP16_MODEL_ID,
        "mlx_lm_version": mlx_lm.__version__,
        "n_generations": len(results),
        "decoding":      {"temperature": TEMPERATURE, "max_tokens": MAX_TOKENS,
                           "sampler": "make_sampler(temp=0.0)"},
        "wall_clock_s":  time.time() - t_start,
        "results":       results,
    }
    (RUN_DIR / "fp16_raw_outputs.json").write_text(json.dumps(out_doc, indent=2) + "\n")
    print(f"   wrote {len(results)} raw outputs to {RUN_DIR / 'fp16_raw_outputs.json'}", flush=True)
    print(f"   total wall-clock: {time.time() - t_start:.0f}s", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
