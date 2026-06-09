#!/usr/bin/env python3
"""
run_stability_screen.py — Margin-aware FP16 stability screen.

For each task pair, runs the narrow arm twice at FP16:
  1. Original prompt (as written in the tasks module)
  2. Paraphrase: replaces --paraphrase-from string with --paraphrase-to string

Exp 5 defaults (PREREGISTRATION-EXP5.md §4, locked):
  FROM: "Respond using only this exact format with nothing before or after: ANSWER:"
  TO:   "Your entire response must be exactly this and nothing else: ANSWER:"

An item is STABLE if:
  - narrow original = 1.0
  - narrow paraphrase = 1.0
  - all component checks ≥ 0.5 (original prompt only)
  - broad arm ≥ 0.5 (original prompt only)

An item is BOUNDARY if narrow original = 1.0 but paraphrase < 1.0.
An item is FLOOR if narrow original < 1.0.

Outputs:
  - stability_screen_<timestamp>.json: full results
  - <out-tasks>: auto-generated filtered task file (STABLE items only)

USAGE:
  python3 run_stability_screen.py \\
      --model Qwen/Qwen2.5-1.5B-Instruct \\
      --tasks tasks_exp5 \\
      --model-4bit mlx-community/Qwen2.5-1.5B-Instruct-4bit \\
      --out-tasks tasks_exp5_stable.py
"""

import argparse
import importlib
import json
import sys
import time
from pathlib import Path

import numpy as np

try:
    from mlx_lm import load, generate
    from mlx_lm.sample_utils import make_sampler
except ImportError:
    raise SystemExit(
        "mlx-lm not found. On macOS 15+: pip install mlx-lm numpy"
    )


_DEFAULT_PARAPHRASE_FROM = "Respond using only this exact format with nothing before or after: ANSWER:"
_DEFAULT_PARAPHRASE_TO   = "Your entire response must be exactly this and nothing else: ANSWER:"


def paraphrase(prompt: str, from_str: str, to_str: str) -> str:
    return prompt.replace(from_str, to_str)


def run_prompt(model, tokenizer, prompt: str, max_tokens: int = 512) -> str:
    if tokenizer.chat_template is not None:
        messages = [{"role": "user", "content": prompt}]
        prompt = tokenizer.apply_chat_template(messages, add_generation_prompt=True)
    return generate(model, tokenizer, prompt=prompt, max_tokens=max_tokens,
                    sampler=make_sampler(temp=0.0), verbose=False)


def score_exact(output: str, answer: str) -> float:
    norm = lambda s: "".join(s.lower().split())
    return float(norm(answer) in norm(output))


def score_checklist(output: str, required_facts: list) -> float:
    norm = output.lower()
    hits = sum(1 for f in required_facts if f.lower() in norm)
    return hits / len(required_facts) if required_facts else 0.0


def score_item(output: str, item: dict) -> float:
    if item["score_type"] == "exact":
        return score_exact(output, item["answer"])
    elif item["score_type"] == "checklist":
        return score_checklist(output, item["required_facts"])
    raise ValueError(f"unknown score_type: {item['score_type']}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True,
                    help="HF repo for FP16 model (e.g. Qwen/Qwen2.5-1.5B-Instruct)")
    ap.add_argument("--tasks", default="tasks_exp5",
                    help="tasks module name without .py")
    ap.add_argument("--model-4bit", default=None,
                    help="HF repo for pre-quantized INT4 model (unused here; accepted for CLI consistency)")
    ap.add_argument("--max-tokens", type=int, default=512)
    ap.add_argument("--out-json", default=None)
    ap.add_argument("--out-tasks", default="tasks_exp5_stable.py",
                    help="output filtered tasks file (only STABLE pairs)")
    ap.add_argument("--paraphrase-from", default=_DEFAULT_PARAPHRASE_FROM,
                    help="format string to replace for paraphrase arm")
    ap.add_argument("--paraphrase-to", default=_DEFAULT_PARAPHRASE_TO,
                    help="replacement format string for paraphrase arm")
    args = ap.parse_args()

    sys.path.insert(0, str(Path(__file__).parent))
    PAIRS = importlib.import_module(args.tasks).PAIRS

    # Dual scorer — observability only; classification logic unchanged.
    from run_tier0 import score_item_dual as _score_dual

    # Provenance: hash the tasks file as used (must match approved manifest hash).
    import hashlib as _hashlib
    _tasks_file = Path(__file__).parent / f"{args.tasks}.py"
    _tasks_hash = f"sha256:{_hashlib.sha256(_tasks_file.read_bytes()).hexdigest()}"

    timestamp = int(time.time())
    out_json = Path(args.out_json or f"stability_screen_{timestamp}.json")

    print(f"=== loading {args.model} at FP16 ===")
    print(f"    tasks_manifest_hash: {_tasks_hash}")
    model, tokenizer = load(args.model)

    results = {}

    for pair in PAIRS:
        pid = pair["id"]
        print(f"\n--- {pid} ---")

        narrow = pair["narrow"]
        broad  = pair["broad"]
        comps  = pair.get("component_checks", [])

        # Narrow: original
        ts_orig = int(time.time())
        out_orig = run_prompt(model, tokenizer, narrow["prompt"], args.max_tokens)
        s_orig   = score_item(out_orig, narrow)
        d_orig   = _score_dual(out_orig, narrow)
        print(f"  narrow/original:   {s_orig:.2f}  strict={d_orig['strict']:.2f}  content={d_orig['content']:.2f}  [{d_orig['failure_class']}]  {repr(out_orig[:100])}")

        # Narrow: paraphrase
        ts_para = int(time.time())
        para_prompt = paraphrase(narrow["prompt"], args.paraphrase_from, args.paraphrase_to)
        out_para = run_prompt(model, tokenizer, para_prompt, args.max_tokens)
        s_para   = score_item(out_para, narrow)
        d_para   = _score_dual(out_para, narrow)
        print(f"  narrow/paraphrase: {s_para:.2f}  strict={d_para['strict']:.2f}  content={d_para['content']:.2f}  [{d_para['failure_class']}]  {repr(out_para[:100])}")

        # Broad: original
        ts_broad = int(time.time())
        out_broad = run_prompt(model, tokenizer, broad["prompt"], args.max_tokens)
        s_broad   = score_item(out_broad, broad)
        d_broad   = _score_dual(out_broad, broad)
        print(f"  broad/original:    {s_broad:.2f}  strict={d_broad['strict']:.2f}  content={d_broad['content']:.2f}  [{d_broad['failure_class']}]  {repr(out_broad[:100])}")

        # Component checks
        comp_results = []
        for j, comp in enumerate(comps):
            ts_comp  = int(time.time())
            out_comp = run_prompt(model, tokenizer, comp["prompt"], args.max_tokens)
            s_comp   = score_item(out_comp, comp)
            d_comp   = _score_dual(out_comp, comp)
            hop      = comp.get("hop", f"comp_{j}")
            print(f"  comp[{hop}]:  {s_comp:.2f}  strict={d_comp['strict']:.2f}  content={d_comp['content']:.2f}  [{d_comp['failure_class']}]  {repr(out_comp[:80])}")
            comp_results.append({
                "hop": hop, "score": s_comp,
                "strict": d_comp["strict"], "content": d_comp["content"],
                "partial": d_comp["partial"], "failure_class": d_comp["failure_class"],
                "expected": d_comp["expected"],
                "output": out_comp[:400], "timestamp": ts_comp,
            })

        # Classify — uses single score (= strict_format_score for exact-match items).
        # Classification logic unchanged from pre-registration.
        all_comps_ok = all(c["score"] >= 0.5 for c in comp_results)
        broad_ok = s_broad >= 0.5

        if s_orig < 1.0:
            classification = "FLOOR"
        elif s_para < 1.0:
            classification = "BOUNDARY"
        elif not all_comps_ok:
            classification = "COMP_FAIL"
        elif not broad_ok:
            classification = "BROAD_FAIL"
        else:
            classification = "STABLE"

        print(f"  → {classification}")

        results[pid] = {
            "narrow_original":  {
                "score": s_orig, "strict": d_orig["strict"], "content": d_orig["content"],
                "partial": d_orig["partial"], "failure_class": d_orig["failure_class"],
                "expected": d_orig["expected"], "output": out_orig[:500], "timestamp": ts_orig,
            },
            "narrow_paraphrase": {
                "score": s_para, "strict": d_para["strict"], "content": d_para["content"],
                "partial": d_para["partial"], "failure_class": d_para["failure_class"],
                "expected": d_para["expected"], "output": out_para[:500], "timestamp": ts_para,
            },
            "broad_original": {
                "score": s_broad, "strict": d_broad["strict"], "content": d_broad["content"],
                "partial": d_broad["partial"], "failure_class": d_broad["failure_class"],
                "expected": d_broad["expected"], "output": out_broad[:500], "timestamp": ts_broad,
            },
            "component_checks": comp_results,
            "classification": classification,
        }

    # Write JSON — includes provenance header
    out_json.write_text(json.dumps({
        "model": args.model, "tasks": args.tasks,
        "tasks_manifest_hash": _tasks_hash,
        "fresh_generation": True,
        "screen_timestamp": timestamp,
        "results": results,
    }, indent=2))
    print(f"\n=== wrote {out_json} ===")

    # Summary
    stable    = [pid for pid, r in results.items() if r["classification"] == "STABLE"]
    boundary  = [pid for pid, r in results.items() if r["classification"] == "BOUNDARY"]
    comp_fail = [pid for pid, r in results.items() if r["classification"] == "COMP_FAIL"]
    broad_fail= [pid for pid, r in results.items() if r["classification"] == "BROAD_FAIL"]
    floor     = [pid for pid, r in results.items() if r["classification"] == "FLOOR"]

    print(f"\nSTABLE     ({len(stable)}):    {stable}")
    print(f"BOUNDARY   ({len(boundary)}):  {boundary}")
    print(f"COMP_FAIL  ({len(comp_fail)}): {comp_fail}")
    print(f"BROAD_FAIL ({len(broad_fail)}): {broad_fail}")
    print(f"FLOOR      ({len(floor)}):    {floor}")

    # Exclude non-G items (diagnostics, controls) from the minimum count.
    # Uses included_in_G field; defaults True for backward compatibility.
    substantive_ids = {p["id"] for p in PAIRS if p.get("included_in_G", True)}
    n_stable_substantive = sum(1 for pid in stable if pid in substantive_ids)
    print(f"\nStable SA (included_in_G) pairs: {n_stable_substantive} / {len(substantive_ids)}")

    if n_stable_substantive < 6:
        print("\n[THRESHOLD NOT MET] Fewer than 6 stable SA (included_in_G) pairs.")
        print("Per PREREGISTRATION-EXP7.md §11: report Outcome E (task failure).")
        print("Do not proceed to stress sweep.")
    else:
        print(f"\n[THRESHOLD MET] Proceeding to stress sweep with {len(stable)} pairs.")

    # Auto-generate filtered tasks file (STABLE pairs only)
    if stable:
        out_stem = Path(args.out_tasks).stem
        _write_filtered_tasks(args.tasks, stable, args.out_tasks, out_stem)
        print(f"Wrote filtered task file: {args.out_tasks}")
        print(f"\nNext: python3 run_tier0.py --model {args.model} --bits 16 8 4 "
              f"--calib code --tasks {out_stem} --model-4bit <INT4_REPO>")
    else:
        print(f"No stable pairs. {args.out_tasks} not written.")


def _write_filtered_tasks(tasks_module_name: str, stable_ids: list, out_path: str, out_stem: str):
    """Generate filtered task file containing only stable pairs."""
    lines = [
        '"""',
        f'{out_stem}.py — Filtered task set.',
        '',
        'Auto-generated by run_stability_screen.py.',
        f'Contains only STABLE pairs from {tasks_module_name}.py.',
        'Do not edit after stress sweep begins.',
        '"""',
        '',
        f'from {tasks_module_name} import (',
    ]
    for pid in stable_ids:
        lines.append(f'    {pid},')
    lines.append(')')
    lines.append('')
    lines.append('PAIRS = [')
    for pid in stable_ids:
        lines.append(f'    {pid},')
    lines.append(']')
    lines.append('')

    Path(out_path).write_text('\n'.join(lines))


if __name__ == "__main__":
    main()
