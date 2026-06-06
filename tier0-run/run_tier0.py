#!/usr/bin/env python3
"""
Tier 0 runner — matched-pair retention probe on Apple Silicon via MLX.

This is a SCAFFOLD, not a finished experiment. The intellectual work — building
good matched task pairs — is yours and lives in `tasks.py`. This file handles the
mechanical part: quantize a model across bit-depths, run every task, score it,
compute retention and the paired ΔR with bootstrap CIs, and write results in the
format of RESULTS-INTAKE-TEMPLATE.md.

REQUIREMENTS (verified):
  - macOS 15.0+ (MLX requirement)
  - pip install mlx-lm numpy
  - ~14GB free for a 7B at FP16; ~4GB at INT4. A 48GB Mac runs all rungs.

USAGE:
  1. Fill tasks.py with your matched pairs + counterexamples (a starter is provided).
  2. python run_tier0.py --model Qwen/Qwen2.5-7B-Instruct --bits 16 8 4 --calib code
  3. Repeat with --calib prose, then check ranking invariance (the required gate).

WHAT THIS DOES NOT DO (on purpose):
  - It does not build your pairs. Bad pairs = a clean-looking false result.
  - It does not interpret. It produces numbers; you classify outcomes A/B/C/flat.
  - It does not pre-register for you. Lock tasks.py + scoring BEFORE you look at results.
"""

import argparse
import json
import hashlib
import time
from pathlib import Path

import numpy as np

try:
    from mlx_lm import load, generate
    from mlx_lm.utils import quantize_model  # available in recent mlx-lm
    import mlx.nn as nn
except ImportError:
    raise SystemExit(
        "mlx-lm not found. On macOS 15+: pip install mlx-lm numpy\n"
        "If quantize_model import fails, update mlx-lm: pip install -U mlx-lm"
    )

from tasks import PAIRS  # your matched pairs live here


# ----------------------------------------------------------------------------- 
# Scoring. Keep strictness SYMMETRIC across narrow/broad arms — this is the
# single most important confound guard. Both arms scored the same way.
# -----------------------------------------------------------------------------

def score_exact(output: str, answer: str) -> int:
    """Exact-match after normalization. For narrow tasks with one valid answer."""
    norm = lambda s: "".join(s.lower().split())
    return int(norm(answer) in norm(output))

def score_checklist(output: str, required_facts: list) -> float:
    """Fraction of required facts present. For broad tasks — but note this is a
    STRICT checklist, not a tolerant judge, so it matches narrow-arm strictness."""
    norm = output.lower()
    hits = sum(1 for f in required_facts if f.lower() in norm)
    return hits / len(required_facts) if required_facts else 0.0

def score_item(output: str, item: dict) -> float:
    if item["score_type"] == "exact":
        return float(score_exact(output, item["answer"]))
    elif item["score_type"] == "checklist":
        return score_checklist(output, item["required_facts"])
    else:
        raise ValueError(f"unknown score_type: {item['score_type']}")


# ----------------------------------------------------------------------------- 
# Generation
# -----------------------------------------------------------------------------

def run_prompt(model, tokenizer, prompt: str, max_tokens: int = 512) -> str:
    if tokenizer.chat_template is not None:
        messages = [{"role": "user", "content": prompt}]
        prompt = tokenizer.apply_chat_template(messages, add_generation_prompt=True)
    return generate(model, tokenizer, prompt=prompt, max_tokens=max_tokens, verbose=False)


def load_at_bits(model_repo: str, bits: int):
    """Load FP16, or load+quantize to 8/4-bit. Returns (model, tokenizer)."""
    model, tokenizer = load(model_repo)
    if bits == 16:
        return model, tokenizer
    # quantize in place to the requested bit-width
    group_size = 64
    quantize_model(model, group_size=group_size, bits=bits)
    return model, tokenizer


# ----------------------------------------------------------------------------- 
# Retention + paired ΔR with bootstrap CI
# -----------------------------------------------------------------------------

def bootstrap_paired_diff(broad_R: np.ndarray, narrow_R: np.ndarray,
                          iters: int = 1000, seed: int = 0):
    """Bootstrap CI on ΔR = mean(R_broad) - mean(R_narrow)."""
    rng = np.random.default_rng(seed)
    n = len(broad_R)
    diffs = []
    for _ in range(iters):
        idx = rng.integers(0, n, n)
        diffs.append(broad_R[idx].mean() - narrow_R[idx].mean())
    diffs = np.array(diffs)
    point = broad_R.mean() - narrow_R.mean()
    lo, hi = np.percentile(diffs, [2.5, 97.5])
    return point, (lo, hi)


# ----------------------------------------------------------------------------- 
# Main run
# -----------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True)
    ap.add_argument("--bits", type=int, nargs="+", default=[16, 8, 4])
    ap.add_argument("--calib", default="unspecified",
                    help="label for this calibration run (code / prose) — for the invariance gate")
    ap.add_argument("--max-tokens", type=int, default=512)
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    out_path = Path(args.out or f"results_{args.calib}_{int(time.time())}.json")

    # baseline must be the highest bit-depth present
    baseline_bits = max(args.bits)
    if baseline_bits != 16:
        print(f"[warn] no FP16 baseline in --bits; using {baseline_bits}-bit as baseline")

    # raw_scores[pair_id][arm][bits] = score
    raw = {}
    for bits in sorted(args.bits, reverse=True):
        print(f"\n=== loading {args.model} at {bits}-bit ===")
        model, tokenizer = load_at_bits(args.model, bits)
        for pair in PAIRS:
            pid = pair["id"]
            raw.setdefault(pid, {"narrow": {}, "broad": {}, "counterexample": {}})
            for arm in ("narrow", "broad"):
                item = pair[arm]
                out = run_prompt(model, tokenizer, item["prompt"], args.max_tokens)
                s = score_item(out, item)
                raw[pid][arm][bits] = {"score": s, "output": out[:500]}
                print(f"  {pid}/{arm} @ {bits}b -> {s:.2f}")
            # counterexample (correctness check) — run if present
            if "counterexample" in pair:
                ce = pair["counterexample"]
                out = run_prompt(model, tokenizer, ce["prompt"], args.max_tokens)
                s = score_item(out, ce)
                raw[pid]["counterexample"][bits] = {"score": s, "output": out[:500]}
        del model, tokenizer  # free unified memory before next bit-depth

    # compute retention + ΔR
    summary = {"calib": args.calib, "model": args.model, "baseline_bits": baseline_bits, "rungs": {}}
    for bits in sorted([b for b in args.bits if b != baseline_bits], reverse=True):
        broad_R, narrow_R = [], []
        for pid, d in raw.items():
            b0 = d["broad"][baseline_bits]["score"]
            n0 = d["narrow"][baseline_bits]["score"]
            # retention only defined where baseline was nonzero; else flag
            broad_R.append(d["broad"][bits]["score"] / b0 if b0 > 0 else np.nan)
            narrow_R.append(d["narrow"][bits]["score"] / n0 if n0 > 0 else np.nan)
        broad_R = np.array(broad_R); narrow_R = np.array(narrow_R)
        mask = ~(np.isnan(broad_R) | np.isnan(narrow_R))
        if mask.sum() < 2:
            summary["rungs"][bits] = {"note": "too few pairs with nonzero baseline for ΔR"}
            continue
        point, (lo, hi) = bootstrap_paired_diff(broad_R[mask], narrow_R[mask])
        outcome = "flat" if (lo <= 0 <= hi) else ("A (ΔR>0)" if point > 0 else "negative ΔR — inspect")
        summary["rungs"][bits] = {
            "mean_R_broad": float(np.nanmean(broad_R)),
            "mean_R_narrow": float(np.nanmean(narrow_R)),
            "delta_R": float(point),
            "ci95": [float(lo), float(hi)],
            "n_pairs_used": int(mask.sum()),
            "outcome_hint": outcome,
        }

    # robust-wrong flags: baseline wrong on counterexample, stays wrong under stress
    robust_wrong = []
    for pid, d in raw.items():
        if not d["counterexample"]:
            continue
        ce_base = d["counterexample"].get(baseline_bits, {}).get("score", None)
        if ce_base is not None and ce_base == 0:  # wrong at baseline
            stays_wrong = all(
                d["counterexample"].get(b, {}).get("score", 1) == 0
                for b in args.bits if b in d["counterexample"]
            )
            if stays_wrong:
                robust_wrong.append(pid)
    summary["robust_wrong_flags"] = robust_wrong

    out_path.write_text(json.dumps({"summary": summary, "raw": raw}, indent=2))
    print(f"\n=== wrote {out_path} ===")
    print(json.dumps(summary, indent=2))
    print("\nNext: run again with the OTHER calibration set, then compare rung rankings.")
    print("The fragility signal counts ONLY if the pair ranking by ΔR is invariant across both.")


if __name__ == "__main__":
    main()
