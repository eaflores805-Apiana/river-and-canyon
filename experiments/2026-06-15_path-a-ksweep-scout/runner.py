#!/usr/bin/env python3
"""
runner.py -- Path A K-Sweep Scout FP16 inference (authorized model execution).

Per LOCKED PREREGISTRATION v1.0 (sha 248581f6...) + Manager by-name run
authorization 2026-06-15. Route GREEN for THIS NAMED SCOUT ONLY. FP16-only.
No compression. No retry. One run per cell.

Reads prompts_rendered_K{K}.json per cell, generates FP16 outputs for all
96 items × 4 contexts = 384 generations per cell, writes raw E3 to
fp16_raw_outputs_K{K}.json. No scoring -- analyze.py performs per-item
validation + Wilson CI per cell after this completes.

Loads the model ONCE and iterates all 5 cells in one process to avoid
5x model-load overhead. Per-cell timing is recorded separately in the output.
"""
from __future__ import annotations

import argparse
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
LOCKED_K_LIST = [1, 2, 3, 4, 5]


def run_cell(model, tokenizer, sampler, K_cell: int, mlx_lm_version: str):
    prompts_doc = json.loads((RUN_DIR / f"prompts_rendered_K{K_cell}.json").read_text())
    renderings = prompts_doc["renderings"]
    n_items = len(renderings)
    n_contexts = len(prompts_doc["contexts"])
    n_total = n_items * n_contexts

    print(f"\n== K={K_cell} starting at {datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')} ==", flush=True)
    print(f"   n_items={n_items}  contexts={prompts_doc['contexts']}  n_total={n_total}", flush=True)

    from mlx_lm import stream_generate

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
            print(f"   [K={K_cell}  {idx:3d}/{n_items}] {item_id}  elapsed={elapsed:.0f}s  eta={eta:.0f}s", flush=True)

    wall = time.time() - t_start
    out_doc = {
        "run_name":      f"PATH-A-KSWEEP-SCOUT-2026-06-15-K{K_cell}",
        "K_cell":        K_cell,
        "timestamp_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "model_id":      FP16_MODEL_ID,
        "mlx_lm_version": mlx_lm_version,
        "n_generations": len(results),
        "decoding":      {"temperature": TEMPERATURE, "max_tokens": MAX_TOKENS,
                           "sampler": "make_sampler(temp=0.0)"},
        "wall_clock_s":  wall,
        "results":       results,
    }
    out_path = RUN_DIR / f"fp16_raw_outputs_K{K_cell}.json"
    out_path.write_text(json.dumps(out_doc, indent=2) + "\n")
    sha = hashlib.sha256(out_path.read_bytes()).hexdigest()
    print(f"   K={K_cell} wrote {len(results)} outputs to {out_path.name}  sha {sha[:16]}...  wall={wall:.0f}s", flush=True)
    return {"K": K_cell, "wall_s": wall, "n_generations": len(results), "output_sha256": sha}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--cells", default="1,2,3,4,5",
                    help="Comma-separated list of K cells to run (default: 1,2,3,4,5)")
    args = ap.parse_args()
    cells = [int(c) for c in args.cells.split(",")]
    for c in cells:
        assert c in LOCKED_K_LIST, f"K={c} not in locked list {LOCKED_K_LIST}"

    print(f"== Path A K-Sweep Scout starting at {datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')} ==", flush=True)
    print(f"   cells={cells}  FP16 only  greedy  max_tokens={MAX_TOKENS}", flush=True)

    import mlx_lm
    from mlx_lm import load
    from mlx_lm.sample_utils import make_sampler

    print(f"   loading {FP16_MODEL_ID} (mlx_lm {mlx_lm.__version__}) once for all cells ...", flush=True)
    t0 = time.time()
    model, tokenizer = load(FP16_MODEL_ID)
    print(f"   loaded in {time.time() - t0:.1f}s", flush=True)

    sampler = make_sampler(temp=TEMPERATURE)

    t_sweep = time.time()
    per_cell_summary = []
    for K in cells:
        per_cell_summary.append(run_cell(model, tokenizer, sampler, K, mlx_lm.__version__))

    total_wall = time.time() - t_sweep
    summary = {
        "run_name":      "PATH-A-KSWEEP-SCOUT-2026-06-15",
        "timestamp_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "total_wall_s":  total_wall,
        "cells_run":     cells,
        "per_cell":      per_cell_summary,
    }
    (RUN_DIR / "RUN_SWEEP_SUMMARY.json").write_text(json.dumps(summary, indent=2) + "\n")
    print(f"\n== Sweep complete: {len(cells)} cells in {total_wall:.0f}s ({total_wall/60:.1f} min) ==", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
