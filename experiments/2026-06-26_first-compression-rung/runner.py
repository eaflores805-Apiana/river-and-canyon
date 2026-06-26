#!/usr/bin/env python3
"""
runner.py — MINIMAL-FP16-INT8-TWOHOP-L1-v0.1

Executes the locked preregistration. Greedy decoding only; raw E3 captured for
both conditions; no scorer modification (uses byte-locked tier0-run/scorer_twohop_l1.py).

Authority: TL ACTION 2026-06-14 with Manager "authorize run" (Route GREEN).
Authorized scope: MINIMAL-FP16-INT8-TWOHOP-L1-v0.1 only.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import platform
import sys
import time
from datetime import datetime, timezone
from pathlib import Path


REPO = Path(__file__).resolve().parents[2]
RUN_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO / "tier0-run"))
import scorer_twohop_l1 as scorer  # byte-locked

PROMPT_TEMPLATE_PATH = REPO / "experiments/2026-06-09_b1-harness-v2/code/prompt_template_twohop_l1.txt"
ITEMS_PATH = REPO / "tier0-run/items_twohop_l1_cell03.json"

# Per-preregistration: n=8, greedy temp=0.0, max_tokens=16.
N = 8
MAX_TOKENS = 16
TEMPERATURE = 0.0
QUERY_TYPES = ["hop1", "hop2", "composite"]
QUERY_TEXT = {
    "hop1":      "{anchor} links to what?",
    "hop2":      "{anchor} maps to what?",
    "composite": "{anchor} links to something, which maps to what?",
}

FP16_MODEL_ID = "Qwen/Qwen2.5-3B-Instruct"
INT8_MODEL_ID = str(REPO / "tier0-run/Qwen2.5-3B-Instruct-mlx-int8")


def sha256_path(p: Path) -> str:
    return "sha256:" + hashlib.sha256(p.read_bytes()).hexdigest()


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def render_prompt(item: dict, query_type: str, template: str) -> str:
    anchor = item["queries"][query_type]["query_anchor"]
    facts = sorted(item["context"]["ordered_facts"], key=lambda x: x["position_index"])
    context_str = "\n".join(f["text"] for f in facts)
    query_str = QUERY_TEXT[query_type].format(anchor=anchor)
    return template.replace("{CONTEXT}", context_str).replace("{QUERY}", query_str)


def run_condition(model_id: str, condition_name: str, items: list, template: str) -> list:
    import mlx_lm
    from mlx_lm import load, stream_generate
    from mlx_lm.sample_utils import make_sampler

    print(f"\n[{condition_name}] loading {model_id} ...", flush=True)
    t0 = time.time()
    model, tokenizer = load(model_id)
    load_time = time.time() - t0
    print(f"[{condition_name}] loaded in {load_time:.1f}s (mlx_lm {mlx_lm.__version__})", flush=True)

    sampler = make_sampler(temp=TEMPERATURE)
    results = []
    for item in items:
        for qt in QUERY_TYPES:
            prompt = render_prompt(item, qt, template)
            # Apply chat template (matches b1 v2 / FP16 constructibility check convention).
            messages = [{"role": "user", "content": prompt}]
            chat_prompt = tokenizer.apply_chat_template(
                messages, add_generation_prompt=True, tokenize=False
            )

            output_text_parts = []
            for resp in stream_generate(
                model, tokenizer, chat_prompt, max_tokens=MAX_TOKENS, sampler=sampler
            ):
                output_text_parts.append(resp.text)
            output_text = "".join(output_text_parts)

            results.append({
                "item_id":    item["item_id"],
                "query_type": qt,
                "anchor":     item["queries"][qt]["query_anchor"],
                "expected":   item["queries"][qt]["expected_answer"],
                "prompt":     prompt,
                "chat_prompt_sha256": "sha256:" + hashlib.sha256(chat_prompt.encode()).hexdigest(),
                "raw_output": output_text,
            })
            print(f"  [{condition_name}] {item['item_id']:>20s} {qt:>10s}  → {output_text!r:.60}", flush=True)

    return results


def score_results(results: list, items_by_id: dict) -> dict:
    """Score a results list with the byte-locked scorer. Adds classification per item.
    Returns aggregate per-query-type counts + an annotated copy of results.
    """
    annotated = []
    counts = {qt: {"n": 0, "correct": 0, "format_fail": 0, "anchor_echo": 0,
                   "non_context": 0, "stopped_short": 0, "other": 0}
              for qt in QUERY_TYPES}
    for r in results:
        item = items_by_id[r["item_id"]]
        cls = scorer.classify_output(r["raw_output"], item, r["query_type"])
        ann = dict(r)
        ann["classification"] = cls
        annotated.append(ann)
        qt = r["query_type"]
        counts[qt]["n"] += 1
        fc = cls["failure_class"]
        if cls["is_correct"]:
            counts[qt]["correct"] += 1
        if fc == "format_scaffold_failure":
            counts[qt]["format_fail"] += 1
        elif fc == "anchor_echo":
            counts[qt]["anchor_echo"] += 1
        elif fc == "non_context_return":
            counts[qt]["non_context"] += 1
        elif fc == "correct_chain_stopped_short":
            counts[qt]["stopped_short"] += 1
        elif fc != "correct":
            counts[qt]["other"] += 1
    return {"counts": counts, "annotated": annotated}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out-dir", type=Path, default=RUN_DIR)
    args = parser.parse_args()
    out = args.out_dir

    # Inputs
    items_all = json.loads(ITEMS_PATH.read_text())
    items = items_all[:N]
    items_by_id = {it["item_id"]: it for it in items}
    template = PROMPT_TEMPLATE_PATH.read_text()

    print(f"== MINIMAL-FP16-INT8-TWOHOP-L1-v0.1 run starting at {now_iso()} ==", flush=True)
    print(f"   n={N} items: {[it['item_id'] for it in items]}", flush=True)
    print(f"   query types: {QUERY_TYPES}  (per preregistration § 2)", flush=True)

    # ── FP16 condition ──────────────────────────────────────────────
    fp16_results = run_condition(FP16_MODEL_ID, "FP16", items, template)
    (out / "fp16_raw_outputs.json").write_text(
        json.dumps({"results": fp16_results, "timestamp_utc": now_iso()}, indent=2) + "\n"
    )

    # ── INT8 condition ──────────────────────────────────────────────
    int8_results = run_condition(INT8_MODEL_ID, "INT8", items, template)
    (out / "int8_raw_outputs.json").write_text(
        json.dumps({"results": int8_results, "timestamp_utc": now_iso()}, indent=2) + "\n"
    )

    # ── Scoring ─────────────────────────────────────────────────────
    fp16_scored = score_results(fp16_results, items_by_id)
    int8_scored = score_results(int8_results, items_by_id)
    (out / "fp16_scored.json").write_text(json.dumps(fp16_scored, indent=2) + "\n")
    (out / "int8_scored.json").write_text(json.dumps(int8_scored, indent=2) + "\n")

    # ── Manifest (with all sha256s for traceability) ────────────────
    import mlx_lm
    manifest = {
        "run_name":             "MINIMAL-FP16-INT8-TWOHOP-L1-v0.1",
        "preregistration_path": "experiments/2026-06-15_minimal-fp16-int8-twohop-l1/PREREGISTRATION.md",
        "preregistration_sha":  "sha256:3fb4dbd4d8daf19be31e95a395abe65175c5968cd3f1b6d50ac08e0bfd4bed03",
        "run_dir":              str(out.relative_to(REPO)),
        "timestamp_utc":        now_iso(),
        "n":                    N,
        "max_tokens":           MAX_TOKENS,
        "temperature":          TEMPERATURE,
        "query_types":          QUERY_TYPES,
        "fp16_model_id":        FP16_MODEL_ID,
        "int8_model_path":      str(Path(INT8_MODEL_ID).relative_to(REPO)),
        "mlx_lm_version":       mlx_lm.__version__,
        "python_version":       sys.version,
        "platform":             platform.platform(),
        "machine":              platform.machine(),
        "node_id_sha":          "sha256:" + hashlib.sha256(platform.node().encode()).hexdigest(),
        "inputs": {
            "prompt_template":   sha256_path(PROMPT_TEMPLATE_PATH),
            "items_file":        sha256_path(ITEMS_PATH),
            "scorer":            sha256_path(REPO / "tier0-run/scorer_twohop_l1.py"),
        },
        "outputs": {
            "fp16_raw_outputs":  sha256_path(out / "fp16_raw_outputs.json"),
            "int8_raw_outputs":  sha256_path(out / "int8_raw_outputs.json"),
            "fp16_scored":       sha256_path(out / "fp16_scored.json"),
            "int8_scored":       sha256_path(out / "int8_scored.json"),
        },
    }
    (out / "MANIFEST.json").write_text(json.dumps(manifest, indent=2) + "\n")

    # ── Summary ──────────────────────────────────────────────────────
    print(f"\n== Summary ==")
    print(f"  FP16: " + ", ".join(f"{qt}={fp16_scored['counts'][qt]['correct']}/{fp16_scored['counts'][qt]['n']}" for qt in QUERY_TYPES))
    print(f"  INT8: " + ", ".join(f"{qt}={int8_scored['counts'][qt]['correct']}/{int8_scored['counts'][qt]['n']}" for qt in QUERY_TYPES))
    print(f"  Outputs written to: {out}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
