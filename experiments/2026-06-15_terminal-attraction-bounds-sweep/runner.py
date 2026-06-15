#!/usr/bin/env python3
"""
runner.py — TERMINAL-ATTRACTION-BOUNDS-SWEEP-v0.1

Executes the model phase of the locked sweep. Reads the committed
items_materialized.json, renders prompts with the v0.1 prompt template
(byte-locked at sha c8a81a29...), runs all 216 generations under greedy
decoding, writes raw E3 to raw_outputs.json. NO SCORING in this script —
scoring is done by analyze.py after the model run completes.

Authority: TL ACTION 2026-06-14 + Manager "authorize TERMINAL-ATTRACTION-
BOUNDS-SWEEP-v0.1". Route GREEN for this named run only.

Forbidden boundaries per preregistration §9 + §13 are not lifted: this
script runs FP16 ONLY; no INT8; no compression arm; no certification.
"""
from __future__ import annotations

import hashlib
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parent
REPO = RUN_DIR.parents[1]

ITEMS_PATH = RUN_DIR / "items_materialized.json"
PROMPT_TEMPLATE_PATH = REPO / "experiments/2026-06-09_b1-harness-v2/code/prompt_template_twohop_l1.txt"

FP16_MODEL_ID = "Qwen/Qwen2.5-3B-Instruct"

QUERY_TYPES = ["hop1", "hop2", "composite"]
QUERY_TEXT = {
    "hop1":      "{anchor} links to what?",
    "hop2":      "{anchor} maps to what?",
    "composite": "{anchor} links to something, which maps to what?",
}

MAX_TOKENS = 16
TEMPERATURE = 0.0


def render_prompt(item: dict, query_type: str, template: str) -> str:
    anchor = item["queries"][query_type]["query_anchor"]
    facts_sorted = sorted(item["ordered_facts"], key=lambda x: x["position_index"])
    context_str = "\n".join(f["text"] for f in facts_sorted)
    query_str = QUERY_TEXT[query_type].format(anchor=anchor)
    return template.replace("{CONTEXT}", context_str).replace("{QUERY}", query_str)


def main() -> int:
    items = json.loads(ITEMS_PATH.read_text())
    template = PROMPT_TEMPLATE_PATH.read_text()

    print(f"== TERMINAL-ATTRACTION-BOUNDS-SWEEP-v0.1 run starting at "
          f"{datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')} ==", flush=True)
    print(f"   items: {len(items)}, query types: {QUERY_TYPES}, decoding: greedy temp=0.0 max_tokens={MAX_TOKENS}", flush=True)

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
    for idx, item in enumerate(items, 1):
        for qt in QUERY_TYPES:
            prompt = render_prompt(item, qt, template)
            messages = [{"role": "user", "content": prompt}]
            chat_prompt = tokenizer.apply_chat_template(
                messages, add_generation_prompt=True, tokenize=False
            )

            output_text_parts = []
            for resp in stream_generate(model, tokenizer, chat_prompt,
                                        max_tokens=MAX_TOKENS, sampler=sampler):
                output_text_parts.append(resp.text)
            output_text = "".join(output_text_parts)

            results.append({
                "item_id":            item["item_id"],
                "cell":               item["cell"],
                "k":                  item["k"],
                "position":           item["position"],
                "query_type":         qt,
                "anchor":             item["queries"][qt]["query_anchor"],
                "expected":           item["queries"][qt]["expected_answer"],
                "prompt":             prompt,
                "chat_prompt_sha256": "sha256:" + hashlib.sha256(chat_prompt.encode()).hexdigest(),
                "raw_output":         output_text,
            })
        if idx % 6 == 0 or idx == len(items):
            elapsed = time.time() - t_start
            rate = idx / elapsed
            eta = (len(items) - idx) / rate if rate > 0 else float("inf")
            print(f"   [{idx:3d}/{len(items)}] item {item['item_id']} cell={item['cell']}  "
                  f"elapsed={elapsed:.0f}s  eta={eta:.0f}s", flush=True)

    out = {
        "run_name":      "TERMINAL-ATTRACTION-BOUNDS-SWEEP-v0.1",
        "timestamp_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "n_generations": len(results),
        "results":       results,
    }
    (RUN_DIR / "raw_outputs.json").write_text(json.dumps(out, indent=2) + "\n")
    print(f"   wrote {len(results)} raw outputs to {RUN_DIR / 'raw_outputs.json'}", flush=True)
    print(f"   total wall-clock: {time.time() - t_start:.0f}s", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
