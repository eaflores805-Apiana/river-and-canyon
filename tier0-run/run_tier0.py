#!/usr/bin/env python3
"""
Tier 0 runner — matched-pair retention probe on Apple Silicon via MLX.

Experiment 4+ dual-scoring update: every item is scored with both
strict_format_score and content_slot_score. See PREREGISTRATION-EXP4.md
for the locked definitions and the pre-registered unit tests that run
automatically at startup before any model is loaded.

Scoring hierarchy (locked in PREREGISTRATION-EXP4.md §3.4):
  content_slot_score  →  primary for content/capability claims
  strict_format_score →  primary for format-compliance claims only

A strict-only drop that does not appear under content scoring is a
format-compliance artifact, not a seam signal.

REQUIREMENTS (verified):
  - macOS 15.0+ (MLX requirement)
  - pip install mlx-lm numpy
  - ~14GB free for a 7B at FP16; ~4GB at INT4. A 48GB Mac runs all rungs.

USAGE:
  python run_tier0.py --model Qwen/Qwen2.5-1.5B-Instruct --bits 16 8 4 \\
      --calib code --tasks tasks_exp3 \\
      --model-4bit mlx-community/Qwen2.5-1.5B-Instruct-4bit
"""

import argparse
import json
import re
import time
from pathlib import Path

import numpy as np

try:
    from mlx_lm import load, generate
    from mlx_lm.utils import quantize_model
    from mlx_lm.sample_utils import make_sampler
    import mlx.nn as nn
except ImportError:
    raise SystemExit(
        "mlx-lm not found. On macOS 15+: pip install mlx-lm numpy\n"
        "If quantize_model import fails, update mlx-lm: pip install -U mlx-lm"
    )

# PAIRS loaded dynamically via --tasks argument (see main())


# =============================================================================
# Scoring — dual scorer
# Definitions locked in PREREGISTRATION-EXP4.md §3. Do not modify.
# =============================================================================

def _norm_strict(s: str) -> str:
    return "".join(s.lower().split())

def _norm_content(s: str) -> str:
    return re.sub(r'[^a-z0-9\s]', '', s.lower()).strip()

def _extract_value(expected_answer: str) -> str:
    """Everything after 'ANSWER:' in the expected string; full string if absent."""
    if "ANSWER:" in expected_answer:
        return expected_answer.split("ANSWER:", 1)[1].strip()
    return expected_answer.strip()


def strict_format_score(output: str, expected_answer: str) -> float:
    """Exact-match after whitespace/case normalization.
    Primary scorer for format-compliance claims only.
    """
    return float(_norm_strict(expected_answer) in _norm_strict(output))


def content_slot_score(output: str, expected_answer: str) -> float:
    """Check if the expected VALUE appears anywhere in the output.
    Primary scorer for content/capability claims.
    Uses token-phrase matching (not substring) to avoid false positives where
    the value is a substring of an unrelated token (e.g. "active" in "inactive").
    Falls back to strict_format_score when no 'ANSWER:' prefix is present.
    """
    value = _extract_value(expected_answer)
    norm_value = _norm_content(value)
    if not norm_value:
        return strict_format_score(output, expected_answer)
    value_tokens = norm_value.split()
    output_tokens = _norm_content(output).split()
    v_len = len(value_tokens)
    for i in range(len(output_tokens) - v_len + 1):
        if output_tokens[i:i + v_len] == value_tokens:
            return 1.0
    return 0.0


def partial_content_score(output: str, expected_answer: str) -> float:
    """Fraction of expected value tokens found in output.
    Diagnostic only — used for COMPOUND_NOUN_DROP detection.
    Not a primary metric; logged but not aggregated.
    """
    value = _extract_value(expected_answer)
    norm_value = _norm_content(value)
    tokens = norm_value.split()
    if not tokens:
        return 0.0
    output_tokens = set(_norm_content(output).split())
    return sum(1 for t in tokens if t in output_tokens) / len(tokens)


def classify_failure(strict: float, content: float, partial: float) -> str:
    """Deterministic row-level failure classification.
    Priority order (locked in PREREGISTRATION-EXP4.md §4):
      PASS > FORMAT_COMPLIANCE_LOSS > COMPOUND_NOUN_DROP > CONTENT_LOSS
    ROBUST_WRONG is a cross-rung classification; never assigned here.
    """
    if strict == 1:
        return "PASS"
    if content == 1:
        return "FORMAT_COMPLIANCE_LOSS"
    if partial > 0:
        return "COMPOUND_NOUN_DROP"
    return "CONTENT_LOSS"


def score_item_dual(output: str, item: dict) -> dict:
    """Score one item with both scorers. Returns a dict with all fields."""
    expected = item.get("answer", "")
    if item["score_type"] == "exact":
        s = strict_format_score(output, expected)
        c = content_slot_score(output, expected)
        p = partial_content_score(output, expected)
        fc = classify_failure(s, c, p)
        return {"strict": s, "content": c, "partial": p, "failure_class": fc, "expected": expected}
    elif item["score_type"] == "checklist":
        norm = output.lower()
        hits = sum(1 for f in item["required_facts"] if f.lower() in norm)
        score = hits / len(item["required_facts"]) if item["required_facts"] else 0.0
        fc = "PASS" if score == 1.0 else "CONTENT_LOSS"
        return {"strict": score, "content": score, "partial": score,
                "failure_class": fc, "expected": str(item.get("required_facts", []))}
    else:
        raise ValueError(f"unknown score_type: {item['score_type']}")


# Legacy single-score helpers — kept for callers outside this file (run_stability_screen.py).
def score_exact(output: str, answer: str) -> int:
    norm = lambda s: "".join(s.lower().split())
    return int(norm(answer) in norm(output))

def score_checklist(output: str, required_facts: list) -> float:
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


# =============================================================================
# Scorer unit tests
# Pre-registered in PREREGISTRATION-EXP4.md §9. Do not modify test cases.
# =============================================================================

def run_unit_tests():
    """Run all pre-registered scorer unit tests. Raises SystemExit on failure.
    Called automatically before any model loading in main().
    """
    failures = []

    def check(label, got, want):
        if got != want:
            failures.append(f"  FAIL [{label}]: got {got!r}, expected {want!r}")

    # PASS: strict=1, content=1
    check("PASS/1 strict",  strict_format_score("ANSWER: File K",       "ANSWER: File K"),       1.0)
    check("PASS/1 content", content_slot_score( "ANSWER: File K",       "ANSWER: File K"),       1.0)
    check("PASS/2 strict",  strict_format_score("ANSWER: APPROVED",     "ANSWER: APPROVED"),     1.0)
    check("PASS/2 content", content_slot_score( "ANSWER: APPROVED",     "ANSWER: APPROVED"),     1.0)
    check("PASS/3 strict",  strict_format_score("ANSWER: silver token", "ANSWER: silver token"), 1.0)
    check("PASS/3 content", content_slot_score( "ANSWER: silver token", "ANSWER: silver token"), 1.0)

    # FORMAT_COMPLIANCE_LOSS: strict=0, content=1
    for label, output, expected in [
        ("FCL/1", "ANSWER: amber box stores File K.",             "ANSWER: File K"),
        ("FCL/2", "ANSWER: obsidian drawer stores Log 3",         "ANSWER: Log 3"),
        ("FCL/3", "ANSWER: The blue locker contains the silver disk.", "ANSWER: silver disk"),
    ]:
        s = strict_format_score(output, expected)
        c = content_slot_score(output, expected)
        p = partial_content_score(output, expected)
        check(f"{label} strict",  s, 0.0)
        check(f"{label} content", c, 1.0)
        check(f"{label} class",   classify_failure(s, c, p), "FORMAT_COMPLIANCE_LOSS")

    # COMPOUND_NOUN_DROP: strict=0, content=0, partial>0
    for label, output, expected in [
        ("CND/1", "ANSWER: token",   "ANSWER: silver token"),
        ("CND/2", "ANSWER: jade",    "ANSWER: jade pass"),
        ("CND/3", "ANSWER: cabinet", "ANSWER: Cabinet 3"),
    ]:
        s = strict_format_score(output, expected)
        c = content_slot_score(output, expected)
        p = partial_content_score(output, expected)
        check(f"{label} strict",    s, 0.0)
        check(f"{label} content",   c, 0.0)
        check(f"{label} partial>0", float(p > 0), 1.0)
        check(f"{label} class",     classify_failure(s, c, p), "COMPOUND_NOUN_DROP")

    # CONTENT_LOSS: strict=0, content=0, partial=0
    for label, output, expected in [
        ("CL/1", "ANSWER: INACTIVE",        "ANSWER: ACTIVE"),
        ("CL/2", "ANSWER: OFF",             "ANSWER: ON"),
        ("CL/3", "ANSWER: <status>UNKNOWN", "ANSWER: PENDING"),
    ]:
        s = strict_format_score(output, expected)
        c = content_slot_score(output, expected)
        p = partial_content_score(output, expected)
        check(f"{label} strict",  s, 0.0)
        check(f"{label} content", c, 0.0)
        check(f"{label} partial", p, 0.0)
        check(f"{label} class",   classify_failure(s, c, p), "CONTENT_LOSS")

    if failures:
        print("\n=== SCORER UNIT TEST FAILURES ===")
        for f in failures:
            print(f)
        raise SystemExit(
            f"\n{len(failures)} unit test(s) failed. "
            "Fix the scorer before running live data. "
            "Do not modify the test cases — they are pre-registered in PREREGISTRATION-EXP4.md §9."
        )

    print("=== scorer unit tests: all 9 pre-registered cases passed ===\n")


# =============================================================================
# Generation
# =============================================================================

def run_prompt(model, tokenizer, prompt: str, max_tokens: int = 512) -> str:
    if tokenizer.chat_template is not None:
        messages = [{"role": "user", "content": prompt}]
        prompt = tokenizer.apply_chat_template(messages, add_generation_prompt=True)
    return generate(model, tokenizer, prompt=prompt, max_tokens=max_tokens,
                    sampler=make_sampler(temp=0.0), verbose=False)


def load_at_bits(model_repo: str, bits: int, prequant_repos: dict = None):
    """Load FP16, or load+quantize to 8/4-bit. Returns (model, tokenizer)."""
    if prequant_repos and bits in prequant_repos:
        print(f"  [using pre-quantized repo for {bits}b: {prequant_repos[bits]}]")
        model, tokenizer = load(prequant_repos[bits])
        return model, tokenizer
    model, tokenizer, config = load(model_repo, return_config=True)
    if bits == 16:
        return model, tokenizer
    quantize_model(model, config, group_size=64, bits=bits)
    return model, tokenizer


# =============================================================================
# Statistics
# =============================================================================

def bootstrap_paired_diff(broad_R: np.ndarray, narrow_R: np.ndarray,
                          iters: int = 1000, seed: int = 0):
    """Bootstrap CI on ΔR = mean(R_broad) - mean(R_narrow)."""
    rng = np.random.default_rng(seed)
    n = len(broad_R)
    diffs = [broad_R[rng.integers(0, n, n)].mean() - narrow_R[rng.integers(0, n, n)].mean()
             for _ in range(iters)]
    diffs = np.array(diffs)
    point = broad_R.mean() - narrow_R.mean()
    lo, hi = np.percentile(diffs, [2.5, 97.5])
    return point, (lo, hi)


def bootstrap_mean_ci(values: np.ndarray, iters: int = 1000, seed: int = 0):
    """Bootstrap CI on mean of an array of per-pair values (used for G(w))."""
    rng = np.random.default_rng(seed)
    n = len(values)
    samples = np.array([values[rng.integers(0, n, n)].mean() for _ in range(iters)])
    point = values.mean()
    lo, hi = np.percentile(samples, [2.5, 97.5])
    return point, (lo, hi)


def _outcome_hint(lo: float, hi: float, point: float) -> str:
    if lo > 0:
        return "positive — seam candidate (A)"
    if hi < 0:
        return "negative — inverse seam (C)"
    return "flat (CI includes zero)"


# =============================================================================
# Main run
# =============================================================================

def main():
    # Unit tests run before argument parsing so a bad scorer never touches a model.
    run_unit_tests()

    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True)
    ap.add_argument("--bits", type=int, nargs="+", default=[16, 8, 4])
    ap.add_argument("--calib", default="unspecified",
                    help="label for this calibration run (code / prose)")
    ap.add_argument("--max-tokens", type=int, default=512)
    ap.add_argument("--out", default=None)
    ap.add_argument("--model-4bit", default=None,
                    help="HF repo of pre-quantized 4-bit model")
    ap.add_argument("--model-8bit", default=None,
                    help="HF repo of pre-quantized 8-bit model (optional)")
    ap.add_argument("--tasks", default="tasks",
                    help="tasks module name without .py")
    args = ap.parse_args()

    import importlib, sys
    sys.path.insert(0, str(Path(__file__).parent))
    PAIRS = importlib.import_module(args.tasks).PAIRS

    # Build item-role lookup structures.
    # included_in_G defaults to True for backward compatibility with pre-Exp6 task files.
    g_pids   = {p["id"] for p in PAIRS if p.get("included_in_G", True)}
    nc_pids  = {p["id"] for p in PAIRS if p.get("flag_if_content_nonzero")}
    de_pairs = [p for p in PAIRS if p.get("family") == "DE"]

    out_path = Path(args.out or f"results_{args.calib}_{int(time.time())}.json")

    baseline_bits = max(args.bits)
    if baseline_bits != 16:
        print(f"[warn] no FP16 baseline in --bits; using {baseline_bits}-bit as baseline")

    prequant_repos = {}
    if args.model_4bit:
        prequant_repos[4] = args.model_4bit
    if args.model_8bit:
        prequant_repos[8] = args.model_8bit

    # Provenance fields — written before any model is loaded.
    summary = {
        "calib":             args.calib,
        "model":             args.model,
        "model_4bit":        args.model_4bit,
        "tasks":             args.tasks,
        "bits_swept":        args.bits,
        "run_timestamp":     int(time.time()),
        "unit_tests_passed": True,
        "baseline_bits":     baseline_bits,
        "items_in_G":        sorted(g_pids),
        "rungs":             {},
    }

    # raw[pid][arm][bits] = {strict, content, partial, failure_class, output, expected, timestamp}
    # raw[pid]["components"][ck][bits] = same + hop
    raw = {}

    for bits in sorted(args.bits, reverse=True):
        print(f"\n=== loading {args.model} at {bits}-bit ===")
        model, tokenizer = load_at_bits(args.model, bits, prequant_repos)

        for pair in PAIRS:
            pid = pair["id"]
            raw.setdefault(pid, {"narrow": {}, "broad": {}, "counterexample": {}, "components": {}})

            for arm in ("narrow", "broad"):
                item = pair[arm]
                out = run_prompt(model, tokenizer, item["prompt"], args.max_tokens)
                scored = score_item_dual(out, item)
                scored["output"]    = out[:500]
                scored["timestamp"] = int(time.time())
                raw[pid][arm][bits] = scored
                print(f"  {pid}/{arm} @ {bits}b -> strict={scored['strict']:.2f} "
                      f"content={scored['content']:.2f} [{scored['failure_class']}]")

                # NC halt: if the scorer finds the null-control token in the output,
                # the token was absent from context — something is wrong.
                if arm == "narrow" and pid in nc_pids and scored["content"] > 0:
                    out_path.write_text(json.dumps(
                        {"summary": summary, "raw": raw, "HALT": "NC_CONTENT_NONZERO"}, indent=2))
                    raise SystemExit(
                        f"\n[HALT] {pid} content_slot_score={scored['content']:.2f} at {bits}b. "
                        "The scorer found the null-control expected token in the output, "
                        "but that token is absent from the item's context. "
                        "Scorer or model-hallucination audit required. "
                        "See PREREGISTRATION-EXP6.md §8. "
                        f"Partial results written to: {out_path}"
                    )

            if "counterexample" in pair:
                ce = pair["counterexample"]
                out = run_prompt(model, tokenizer, ce["prompt"], args.max_tokens)
                scored = score_item_dual(out, ce)
                scored["output"]    = out[:500]
                scored["timestamp"] = int(time.time())
                raw[pid]["counterexample"][bits] = scored

            for j, comp in enumerate(pair.get("component_checks", [])):
                ck = f"comp_{j}"
                raw[pid]["components"].setdefault(ck, {})
                out = run_prompt(model, tokenizer, comp["prompt"], args.max_tokens)
                scored = score_item_dual(out, comp)
                scored["output"]    = out[:300]
                scored["timestamp"] = int(time.time())
                scored["hop"]       = comp.get("hop", ck)
                raw[pid]["components"][ck][bits] = scored
                hop = comp.get("hop", ck)
                print(f"  {pid}/comp[{hop}] @ {bits}b -> strict={scored['strict']:.2f} "
                      f"content={scored['content']:.2f} [{scored['failure_class']}]")

        del model, tokenizer

    # -------------------------------------------------------------------------
    # G computation — items with included_in_G=True only
    # -------------------------------------------------------------------------
    stressed_bits = sorted([b for b in args.bits if b != baseline_bits], reverse=True)

    for bits in stressed_bits:
        G_strict_per_pair, G_content_per_pair = [], []
        format_compliance_narrow = []
        format_compliance_broad  = []
        format_compliance_comps  = []
        pair_details = {}

        for pid, d in raw.items():
            if pid not in g_pids:
                continue  # diagnostics/controls excluded from G

            n0_s = d["narrow"][baseline_bits]["strict"]
            n0_c = d["narrow"][baseline_bits]["content"]
            n_s  = d["narrow"][bits]["strict"]
            n_c  = d["narrow"][bits]["content"]
            b_s  = d["broad"][bits]["strict"]

            format_compliance_narrow.append(n_s)
            format_compliance_broad.append(b_s)

            comps = d["components"]
            if not comps:
                continue

            comp_base_strict   = [v[baseline_bits]["strict"]  for v in comps.values()
                                   if baseline_bits in v and v[baseline_bits]["strict"] > 0]
            comp_stress_strict  = [v[bits]["strict"]  for v in comps.values()
                                   if baseline_bits in v and v[baseline_bits]["strict"] > 0 and bits in v]
            comp_base_content  = [v[baseline_bits]["content"] for v in comps.values()
                                   if baseline_bits in v and v[baseline_bits]["content"] > 0]
            comp_stress_content = [v[bits]["content"] for v in comps.values()
                                   if baseline_bits in v and v[baseline_bits]["content"] > 0 and bits in v]

            for v in comps.values():
                if bits in v:
                    format_compliance_comps.append(v[bits]["strict"])

            if not comp_base_strict or not comp_stress_strict or n0_s == 0:
                continue

            R_comp_strict  = (sum(comp_stress_strict)  / len(comp_stress_strict))  / \
                             (sum(comp_base_strict)     / len(comp_base_strict))
            R_compo_strict = n_s / n0_s

            R_comp_content  = None
            R_compo_content = None
            if comp_base_content and comp_stress_content and n0_c > 0:
                R_comp_content  = (sum(comp_stress_content)  / len(comp_stress_content)) / \
                                  (sum(comp_base_content)     / len(comp_base_content))
                R_compo_content = n_c / n0_c

            G_s = R_comp_strict - R_compo_strict
            G_c = (R_comp_content - R_compo_content) \
                  if (R_comp_content is not None and R_compo_content is not None) else None

            G_strict_per_pair.append(G_s)
            if G_c is not None:
                G_content_per_pair.append(G_c)

            seam_flag = None
            if (R_compo_content is not None and R_compo_content < 0.5 and
                    comp_stress_content and min(comp_stress_content) >= 0.5):
                seam_flag = "composite content-failed while components held — seam candidate"

            pair_details[pid] = {
                "G_strict":            float(G_s),
                "G_content":           float(G_c) if G_c is not None else None,
                "R_composite_strict":  float(R_compo_strict),
                "R_composite_content": float(R_compo_content) if R_compo_content is not None else None,
                "seam_flag":           seam_flag,
            }

        G_s_arr = np.array(G_strict_per_pair)
        G_c_arr = np.array(G_content_per_pair)

        rung_out = {"bits": bits, "pair_details": pair_details}

        if len(G_s_arr) >= 2:
            pt_gs, (lo_gs, hi_gs) = bootstrap_mean_ci(G_s_arr)
            rung_out["G_strict"] = {
                "mean": float(pt_gs), "ci95": [float(lo_gs), float(hi_gs)],
                "n_pairs": len(G_s_arr),
                "outcome": _outcome_hint(lo_gs, hi_gs, pt_gs),
            }

        if len(G_c_arr) >= 2:
            pt_gc, (lo_gc, hi_gc) = bootstrap_mean_ci(G_c_arr)
            rung_out["G_content"] = {
                "mean": float(pt_gc), "ci95": [float(lo_gc), float(hi_gc)],
                "n_pairs": len(G_c_arr),
                "outcome": _outcome_hint(lo_gc, hi_gc, pt_gc),
            }

        rung_out["format_compliance_rate"] = {
            "narrow":     float(np.mean(format_compliance_narrow)) if format_compliance_narrow else None,
            "broad":      float(np.mean(format_compliance_broad))  if format_compliance_broad  else None,
            "components": float(np.mean(format_compliance_comps))  if format_compliance_comps  else None,
        }

        summary["rungs"][str(bits)] = rung_out

    # -------------------------------------------------------------------------
    # DE echo diagnostic summary
    # -------------------------------------------------------------------------
    qe_eligible, qe_errors = 0, 0
    pi_eligible, pi_errors = 0, 0
    int4_rung = min(stressed_bits) if stressed_bits else None

    for pair in de_pairs:
        pid      = pair["id"]
        etype    = pair.get("echo_type", "QE")
        echo_tok = pair.get("echo_wrong_value", "")

        fp16_content = raw.get(pid, {}).get("narrow", {}).get(baseline_bits, {}).get("content", 0)
        if fp16_content < 1:
            raw[pid]["_diagnostic_gate_status"] = "FLOOR_DIAGNOSTIC"
            continue
        raw[pid]["_diagnostic_gate_status"] = "ELIGIBLE"

        if int4_rung is None:
            continue
        rung_data = raw.get(pid, {}).get("narrow", {}).get(int4_rung, {})
        out_text  = rung_data.get("output", "")
        content   = rung_data.get("content", 1)
        is_echo   = bool(echo_tok and echo_tok.upper() in out_text.upper() and content == 0)

        if is_echo:
            raw[pid]["narrow"][int4_rung]["failure_class"] = "INPUT_ECHO_ERROR"

        if etype == "QE":
            qe_eligible += 1
            if is_echo:
                qe_errors += 1
        elif etype == "PI":
            pi_eligible += 1
            if is_echo:
                pi_errors += 1

    summary["echo_diagnostic"] = {
        "qe_eligible":         qe_eligible,
        "qe_echo_errors_int4": qe_errors,
        "qe_echo_rate_int4":   (qe_errors / qe_eligible) if qe_eligible > 0 else None,
        "pi_eligible":         pi_eligible,
        "pi_echo_errors_int4": pi_errors,
        "pi_echo_rate_int4":   (pi_errors / pi_eligible) if pi_eligible > 0 else None,
    }

    # -------------------------------------------------------------------------
    # NC validation summary
    # -------------------------------------------------------------------------
    nc_validation = {}
    for pid in nc_pids:
        d = raw.get(pid, {})
        nc_validation[pid] = {
            str(b): d.get("narrow", {}).get(b, {}).get("content") for b in args.bits
        }
    summary["nc_validation"] = nc_validation

    # -------------------------------------------------------------------------
    # Cross-rung ROBUST_WRONG detection (G items only)
    # -------------------------------------------------------------------------
    robust_wrong = []
    for pid in g_pids:
        d = raw.get(pid)
        if d is None:
            continue
        for arm in ("narrow", "broad"):
            base_content = d[arm].get(baseline_bits, {}).get("content", None)
            if base_content is None or base_content > 0:
                continue
            stressed_outputs = [d[arm][b]["output"] for b in stressed_bits if b in d[arm]]
            stressed_content = [d[arm][b]["content"] for b in stressed_bits if b in d[arm]]
            if stressed_content and all(c == 0 for c in stressed_content):
                base_out = _norm_content(d[arm][baseline_bits]["output"])
                if all(_norm_content(o) == base_out for o in stressed_outputs):
                    robust_wrong.append({"pid": pid, "arm": arm,
                                         "row_class": "CONTENT_LOSS",
                                         "cross_rung_class": "ROBUST_WRONG"})
    summary["robust_wrong_flags"] = robust_wrong

    # -------------------------------------------------------------------------
    # Failure class distribution (all items, for completeness)
    # -------------------------------------------------------------------------
    failure_counts = {}
    for bits in args.bits:
        counts = {"PASS": 0, "FORMAT_COMPLIANCE_LOSS": 0,
                  "COMPOUND_NOUN_DROP": 0, "CONTENT_LOSS": 0, "INPUT_ECHO_ERROR": 0}
        for d in raw.values():
            for arm in ("narrow", "broad"):
                fc = d[arm].get(bits, {}).get("failure_class")
                if fc and fc in counts:
                    counts[fc] += 1
            for ck_data in d["components"].values():
                fc = ck_data.get(bits, {}).get("failure_class")
                if fc and fc in counts:
                    counts[fc] += 1
        failure_counts[str(bits)] = counts
    summary["failure_class_distribution"] = failure_counts

    out_path.write_text(json.dumps({"summary": summary, "raw": raw}, indent=2))
    print(f"\n=== wrote {out_path} ===")

    # Print readable summary
    print(f"\n--- Summary: calib={args.calib} model={args.model} ---")
    print(f"    G computed over: {sorted(g_pids)}")
    for bits_str, rung in summary["rungs"].items():
        print(f"\n  [{bits_str}b vs {baseline_bits}b]")
        if "G_content" in rung:
            g = rung["G_content"]
            print(f"    G_content : {g['mean']:+.4f}  CI [{g['ci95'][0]:+.4f}, {g['ci95'][1]:+.4f}]  → {g['outcome']}")
        if "G_strict" in rung:
            g = rung["G_strict"]
            print(f"    G_strict  : {g['mean']:+.4f}  CI [{g['ci95'][0]:+.4f}, {g['ci95'][1]:+.4f}]  → {g['outcome']}")
        if "format_compliance_rate" in rung:
            fcr = rung["format_compliance_rate"]
            print(f"    fmt_compliance: narrow={fcr['narrow']:.3f}  broad={fcr['broad']:.3f}  comps={fcr['components']}")

    # Echo diagnostic
    ed = summary["echo_diagnostic"]
    print(f"\n  [echo diagnostic @ INT4]")
    qr = ed["qe_echo_rate_int4"]
    pr = ed["pi_echo_rate_int4"]
    print(f"    QE echo rate: {ed['qe_echo_errors_int4']}/{ed['qe_eligible']}" +
          (f"  ({qr:.0%})" if qr is not None else "  (no eligible items)"))
    print(f"    PI echo rate: {ed['pi_echo_errors_int4']}/{ed['pi_eligible']}" +
          (f"  ({pr:.0%})" if pr is not None else "  (no eligible items)"))

    # NC validation
    if nc_validation:
        print(f"\n  [null-control validation]")
        for pid, scores in nc_validation.items():
            score_str = "  ".join(f"{b}b={v}" for b, v in scores.items())
            print(f"    {pid}: {score_str}  (expected all 0)")
            if any(v is not None and v > 0 for v in scores.values()):
                print(f"    !! {pid} content>0 at some rung — should have triggered HALT above")

    print("\nNext: repeat with the OTHER calibration, then compare G_content rankings.")
    print("Seam claim requires G_content CI lower bound > 0, calibration-invariant.")


if __name__ == "__main__":
    main()
