#!/usr/bin/env python3
"""
run_step_5.py — Hop1 Stability Investigation inference runner (hop1 + hop2 only).

Loads Qwen2.5-3B-Instruct (FP16, revision aa8e72537993ba99e69dfaafa59ed015b17504d1)
via mlx_lm, runs greedy inference on every committed hop1 + hop2 prompt for
items 193..768 (576 items × 2 contexts = 1152 calls), scores predicted vs
locked ground truth, writes per-context scored JSONs per the analyzer-input
contract.

Authority: Manager by-name authorization 2026-06-19 ("Execute Hop1 Stability
Investigation"). FP16 only; no compression; no rerun; no prompt edits; no
tooling edits after data.

N1.A discipline: prompts for composite/direct_query were RENDERED (all 4
contexts; per realizer's behavior) but are NEVER EXECUTED here. Only hop1
and hop2 prompts are consumed.

Scoring rule + system instruction match the V3 floor-check + composite-gate
runs verbatim, so the fresh blocks are directly comparable to the anchors.

— CS Engineer, 2026-06-19
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
import platform
import socket
from datetime import datetime, timezone
from pathlib import Path


def _load_inference():
    from mlx_lm import load as _load, generate as _generate
    return _load, _generate


MODEL_ID       = "Qwen/Qwen2.5-3B-Instruct"
MODEL_REVISION = "aa8e72537993ba99e69dfaafa59ed015b17504d1"
MAX_NEW_TOKENS = 24
DECODING       = "greedy"

SYSTEM_INSTRUCTION = (
    "You complete structured fact-triple queries. The input is a list of FACTS "
    "given as (subject, relation, object) triples followed by a single QUERY "
    "line of the form `QUERY: (subject, relation, ?)`. The `?` denotes a "
    "single unknown token to be inferred from the FACTS list using the given "
    "relation(s). Respond with exactly that one token and nothing else: no "
    "explanation, no punctuation, no parentheses, no extra whitespace."
)

# N1.A: only hop1 + hop2 are executed. composite + direct_query are
# rendered but NOT consumed by this runner.
EXECUTED_CONTEXTS = ("hop1", "hop2")


def _ground_truth(spec: dict, context: str) -> str:
    t = spec["target"]
    if context == "hop2":
        return t["C_star"]
    elif context == "hop1":
        return t["B"]
    else:
        raise ValueError(f"unknown / out-of-scope context: {context!r}")


_ID_TOKEN_RE = re.compile(r"[A-Za-z][\w]*")


def _extract_predicted(response_text: str) -> str:
    s = response_text.strip()
    m = _ID_TOKEN_RE.search(s)
    return m.group(0) if m else s[:32]


def _build_chat_messages(prompt: str) -> list[dict]:
    return [
        {"role": "system", "content": SYSTEM_INSTRUCTION},
        {"role": "user",   "content": prompt},
    ]


def _apply_chat_template(tokenizer, prompt: str) -> str:
    return tokenizer.apply_chat_template(
        _build_chat_messages(prompt),
        tokenize=False,
        add_generation_prompt=True,
    )


def _generate_one(model, tokenizer, generate_fn, prompt_text: str) -> str:
    chat = _apply_chat_template(tokenizer, prompt_text)
    try:
        out = generate_fn(model, tokenizer, prompt=chat,
                          max_tokens=MAX_NEW_TOKENS, verbose=False, temp=0.0)
    except TypeError:
        try:
            from mlx_lm.sample_utils import make_sampler
            sampler = make_sampler(temp=0.0)
        except ImportError:
            sampler = None
        kwargs = {"max_tokens": MAX_NEW_TOKENS, "verbose": False}
        if sampler is not None:
            kwargs["sampler"] = sampler
        out = generate_fn(model, tokenizer, prompt=chat, **kwargs)
    return out


def run_one_context(model, tokenizer, generate_fn,
                     spec: dict, context: str, prompt_text: str,
                     item_stem: str) -> dict:
    gt        = _ground_truth(spec, context)
    response  = _generate_one(model, tokenizer, generate_fn, prompt_text)
    predicted = _extract_predicted(response)
    return {
        "item":         item_stem,
        "context":      context,
        "ground_truth": gt,
        "predicted":    predicted,
        "match":        predicted == gt,
        "raw_response": response,
    }


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--items-dir",     type=Path, required=True)
    p.add_argument("--prompts-dir",   type=Path, required=True)
    p.add_argument("--scored-dir",    type=Path, required=True)
    p.add_argument("--run-record",    type=Path, required=True)
    p.add_argument("--only",          type=str, default=None,
                    help="optional: restrict to a single item stem for smoke testing")
    p.add_argument("--progress-every", type=int, default=20,
                    help="emit a progress line every N prompts (default 20)")
    args = p.parse_args(argv)

    args.scored_dir.mkdir(parents=True, exist_ok=True)
    items = sorted(args.items_dir.glob("item_*.json"))
    if args.only:
        items = [pth for pth in items if pth.stem == args.only]
        if not items:
            print(f"no item matching --only={args.only!r}", file=sys.stderr)
            return 2

    print(f"Loading model {MODEL_ID} @ rev {MODEL_REVISION} ...", flush=True)
    t_load_start = time.time()
    load_fn, generate_fn = _load_inference()
    model, tokenizer = load_fn(MODEL_ID)
    t_load_elapsed = time.time() - t_load_start
    print(f"Model loaded in {t_load_elapsed:.1f}s", flush=True)

    t_run_start = time.time()
    n_total = len(items) * len(EXECUTED_CONTEXTS)
    n_done  = 0

    for spec_path in items:
        spec = json.loads(spec_path.read_text())
        item_stem = spec_path.stem
        item_out_dir = args.scored_dir / item_stem
        item_out_dir.mkdir(parents=True, exist_ok=True)
        for ctx in EXECUTED_CONTEXTS:
            prompt_path = args.prompts_dir / item_stem / f"{ctx}.txt"
            prompt_text = prompt_path.read_text()
            scored = run_one_context(model, tokenizer, generate_fn,
                                      spec, ctx, prompt_text, item_stem)
            contract = {k: scored[k] for k in ("item", "context", "ground_truth", "predicted", "match")}
            (item_out_dir / f"{ctx}.json").write_text(json.dumps(contract, indent=2) + "\n")
            (item_out_dir / f"{ctx}.raw.json").write_text(json.dumps(
                {**contract, "raw_response": scored["raw_response"],
                 "model": MODEL_ID, "revision": MODEL_REVISION}, indent=2) + "\n")
            n_done += 1
            if n_done % args.progress_every == 0 or n_done == n_total:
                elapsed = time.time() - t_run_start
                rate = n_done / elapsed if elapsed > 0 else 0.0
                eta = (n_total - n_done) / rate if rate > 0 else 0.0
                print(f"  progress: {n_done}/{n_total}  elapsed {elapsed:.1f}s  rate {rate:.2f} prompt/s  eta {eta:.1f}s", flush=True)

    t_run_elapsed = time.time() - t_run_start

    import mlx_lm
    import transformers
    import torch
    run_record = {
        "model_name":           MODEL_ID,
        "model_revision_sha":   MODEL_REVISION,
        "precision":            "FP16 (mlx_lm default for non-quantized Qwen2.5)",
        "decoding":             "greedy (temp=0.0 / argmax sampler)",
        "max_new_tokens":       MAX_NEW_TOKENS,
        "execution_host":       socket.gethostname(),
        "host_platform":        platform.platform(),
        "host_machine":         platform.machine(),
        "runtime_versions": {
            "python":          platform.python_version(),
            "mlx_lm":          mlx_lm.__version__,
            "transformers":    transformers.__version__,
            "torch":           torch.__version__,
        },
        "model_load_time_s":     t_load_elapsed,
        "inference_time_s":      t_run_elapsed,
        "n_items":               len(items),
        "n_contexts_per_item":   len(EXECUTED_CONTEXTS),
        "executed_contexts":     list(EXECUTED_CONTEXTS),
        "rendered_but_not_executed_contexts": ["composite", "direct_query"],
        "n_prompts_total":       n_done,
        "timestamp_utc":         datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "operator":              "CS Engineer (Claude Code; M2 Max host)",
        "prompts_consumed_as_committed":   True,
        "prompt_regeneration_occurred":    False,
        "system_instruction":    SYSTEM_INSTRUCTION,
        "scoring_rule":          "exact string equality between extracted first id-like token from model response and locked ground truth",
        "ground_truth_rule":     "hop1 -> spec.target.B ; hop2 -> spec.target.C_star",
        "tooling_edits_after_data": False,
        "scope":                "Hop1 Stability run; FP16 only; no compression authorized; "
                                "N1.A: composite + direct_query rendered but NEVER executed by this runner",
        "n1A_discipline":       "hop1 + hop2 only; composite + direct_query NOT consumed; "
                                "analyzer + covariate logger ALSO refuse them structurally",
        "authority":            "Manager by-name authorization 2026-06-19",
    }
    args.run_record.write_text(json.dumps(run_record, indent=2) + "\n")
    print(f"run_record written: {args.run_record}", flush=True)
    print(f"DONE. {n_done} prompts scored in {t_run_elapsed:.1f}s (load: {t_load_elapsed:.1f}s).", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
