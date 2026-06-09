#!/usr/bin/env python3
"""
regression_check_exp3.py

Offline regression check: apply the new dual scorer (strict_format_score,
content_slot_score, failure_class) to stored Exp 3 outputs and verify the
result matches the manual Option A verdict.

Expected result:
  strict:  G_strict(INT4) ≈ -0.0494, CI excludes zero
  content: G_content(INT4) ≈ -0.0123, CI touches/includes zero
  failure: mostly FORMAT_COMPLIANCE_LOSS; FC1/vault3_token = COMPOUND_NOUN_DROP

Inputs:
  results_code_1780745541.json   — stored Exp 3 outputs (old single-score schema)
  tasks_exp3.py                  — expected answers (joined by pid + hop name)

Usage:
  python3 regression_check_exp3.py
"""

import json
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).parent))
from run_tier0 import (
    strict_format_score, content_slot_score, partial_content_score,
    classify_failure, bootstrap_mean_ci, _outcome_hint, run_unit_tests,
)

# Gate: unit tests must pass before any rescoring
run_unit_tests()

# ---------------------------------------------------------------------------
# Load inputs
# ---------------------------------------------------------------------------
RESULTS_FILE = Path("results_code_1780745541.json")
results = json.loads(RESULTS_FILE.read_text())
raw = results["raw"]

import importlib
PAIRS = importlib.import_module("tasks_exp3").PAIRS
tasks_by_id = {p["id"]: p for p in PAIRS}

BASELINE = "16"
STRESSED = ["8", "4"]

# ---------------------------------------------------------------------------
# Build expected-answer lookup: (pid, arm, hop_or_arm) -> expected_answer
# ---------------------------------------------------------------------------
expected = {}  # (pid, arm, key) -> answer string
for pair in PAIRS:
    pid = pair["id"]
    expected[(pid, "narrow")] = pair["narrow"].get("answer", "")
    expected[(pid, "broad")]  = pair["broad"].get("answer", "")
    for comp in pair.get("component_checks", []):
        hop = comp.get("hop", "")
        expected[(pid, "component", hop)] = comp.get("answer", "")

# ---------------------------------------------------------------------------
# Apply dual scorer to every stored output
# ---------------------------------------------------------------------------
# scored[pid][arm][bits_str] = {strict, content, partial, failure_class, output, expected}
# arm is "narrow", "broad", or "comp_N"
scored = {}

for pid, d in raw.items():
    scored[pid] = {"narrow": {}, "broad": {}, "components": {}}

    for arm in ("narrow", "broad"):
        exp_ans = expected.get((pid, arm), "")
        for bits_str, rec in d[arm].items():
            out = rec["output"]
            s = strict_format_score(out, exp_ans)
            c = content_slot_score(out, exp_ans)
            p = partial_content_score(out, exp_ans)
            fc = classify_failure(s, c, p)
            scored[pid][arm][bits_str] = {
                "strict": s, "content": c, "partial": p,
                "failure_class": fc, "output": out, "expected": exp_ans,
                "old_score": rec["score"],
            }

    for ck, bits_data in d["components"].items():
        scored[pid]["components"][ck] = {}
        for bits_str, rec in bits_data.items():
            hop = rec.get("hop", "")
            exp_ans = expected.get((pid, "component", hop), "")
            out = rec["output"]
            s = strict_format_score(out, exp_ans)
            c = content_slot_score(out, exp_ans)
            p = partial_content_score(out, exp_ans)
            fc = classify_failure(s, c, p)
            scored[pid]["components"][ck][bits_str] = {
                "strict": s, "content": c, "partial": p,
                "failure_class": fc, "output": out, "expected": exp_ans,
                "hop": hop, "old_score": rec["score"],
            }

# ---------------------------------------------------------------------------
# Report: item-level changed classifications
# ---------------------------------------------------------------------------
print("=" * 72)
print("REGRESSION CHECK — Exp 3 outputs rescored with dual scorer")
print(f"input_file : {RESULTS_FILE}")
print(f"mode       : offline_rescore")
print(f"model_run  : Exp 3 (Qwen2.5-1.5B-Instruct, tasks_exp3.py)")
print("=" * 72)

print("\n--- Item-level failure classes where strict ≠ content ---\n")
print(f"{'Item':<30} {'bits':>4}  {'strict':>6}  {'content':>7}  {'class':<26}  output[:60]")
print("-" * 120)

changed_items = []
for pid, d in scored.items():
    for arm in ("narrow", "broad"):
        for bits_str, rec in d[arm].items():
            if rec["strict"] != rec["content"]:
                row = (pid, arm, bits_str, rec)
                changed_items.append(row)
                label = f"{pid}/{arm}"
                print(f"  {label:<28} {bits_str:>4}b  {rec['strict']:>6.1f}  {rec['content']:>7.1f}"
                      f"  {rec['failure_class']:<26}  {repr(rec['output'][:60])}")
    for ck, bits_data in d["components"].items():
        for bits_str, rec in bits_data.items():
            if rec["strict"] != rec["content"]:
                row = (pid, f"comp[{rec['hop']}]", bits_str, rec)
                changed_items.append(row)
                label = f"{pid}/comp[{rec['hop']}]"
                print(f"  {label:<28} {bits_str:>4}b  {rec['strict']:>6.1f}  {rec['content']:>7.1f}"
                      f"  {rec['failure_class']:<26}  {repr(rec['output'][:60])}")

if not changed_items:
    print("  (none — strict and content scores agree on all items)")

# ---------------------------------------------------------------------------
# Failure class distribution per rung
# ---------------------------------------------------------------------------
print("\n--- Failure class distribution ---\n")
for bits_str in [BASELINE] + STRESSED:
    counts = {"PASS": 0, "FORMAT_COMPLIANCE_LOSS": 0, "COMPOUND_NOUN_DROP": 0, "CONTENT_LOSS": 0}
    for d in scored.values():
        for arm in ("narrow", "broad"):
            fc = d[arm].get(bits_str, {}).get("failure_class")
            if fc in counts: counts[fc] += 1
        for bits_data in d["components"].values():
            fc = bits_data.get(bits_str, {}).get("failure_class")
            if fc in counts: counts[fc] += 1
    total = sum(counts.values())
    print(f"  [{bits_str}b]  ", end="")
    for k, v in counts.items():
        if v > 0:
            print(f"{k}={v}  ", end="")
    print()

# ---------------------------------------------------------------------------
# G_strict and G_content per rung
# ---------------------------------------------------------------------------
# Eligible pairs: substantive pairs only (exclude controls AC1, AC2, NC1)
CONTROL_IDS = {"AC1", "AC2", "NC1"}

print("\n--- G_strict and G_content per rung ---\n")
print(f"  (substantive pairs only, n={len([p for p in PAIRS if p['id'] not in CONTROL_IDS])})\n")

for bits_str in STRESSED:
    G_strict_vals, G_content_vals = [], []
    pair_rows = []

    for pid, d in scored.items():
        if pid in CONTROL_IDS:
            continue
        n16 = d["narrow"].get(BASELINE, {})
        nw  = d["narrow"].get(bits_str, {})
        if not n16 or not nw:
            continue

        n0_s = n16["strict"]; n_s = nw["strict"]
        n0_c = n16["content"]; n_c = nw["content"]

        comps = d["components"]
        if not comps:
            continue

        c_base_s  = [v[BASELINE]["strict"]  for v in comps.values() if BASELINE in v and v[BASELINE]["strict"]  > 0]
        c_str_s   = [v[bits_str]["strict"]  for v in comps.values() if BASELINE in v and v[BASELINE]["strict"]  > 0 and bits_str in v]
        c_base_c  = [v[BASELINE]["content"] for v in comps.values() if BASELINE in v and v[BASELINE]["content"] > 0]
        c_str_c   = [v[bits_str]["content"] for v in comps.values() if BASELINE in v and v[BASELINE]["content"] > 0 and bits_str in v]

        if not c_base_s or not c_str_s or n0_s == 0:
            continue

        R_comp_s  = (sum(c_str_s)  / len(c_str_s))  / (sum(c_base_s)  / len(c_base_s))
        R_compo_s = n_s / n0_s
        G_s = R_comp_s - R_compo_s
        G_strict_vals.append(G_s)

        if c_base_c and c_str_c and n0_c > 0:
            R_comp_c  = (sum(c_str_c)  / len(c_str_c))  / (sum(c_base_c)  / len(c_base_c))
            R_compo_c = n_c / n0_c
            G_c = R_comp_c - R_compo_c
            G_content_vals.append(G_c)
        else:
            G_c = float('nan')

        pair_rows.append((pid, G_s, G_c))

    G_s_arr = np.array(G_strict_vals)
    G_c_arr = np.array([x for x in G_content_vals if not np.isnan(x)])

    print(f"  [{bits_str}b vs {BASELINE}b]")
    if len(G_s_arr) >= 2:
        pt_s, (lo_s, hi_s) = bootstrap_mean_ci(G_s_arr)
        print(f"    G_strict  : {pt_s:+.4f}  CI [{lo_s:+.4f}, {hi_s:+.4f}]  → {_outcome_hint(lo_s, hi_s, pt_s)}")
    if len(G_c_arr) >= 2:
        pt_c, (lo_c, hi_c) = bootstrap_mean_ci(G_c_arr)
        print(f"    G_content : {pt_c:+.4f}  CI [{lo_c:+.4f}, {hi_c:+.4f}]  → {_outcome_hint(lo_c, hi_c, pt_c)}")

    print(f"\n    Pair-level breakdown:")
    print(f"    {'pid':<8}  {'G_strict':>9}  {'G_content':>10}")
    for pid, gs, gc in sorted(pair_rows):
        gc_str = f"{gc:+.4f}" if not np.isnan(gc) else "     nan"
        print(f"    {pid:<8}  {gs:+9.4f}  {gc_str:>10}")
    print()

# ---------------------------------------------------------------------------
# Verdict
# ---------------------------------------------------------------------------
print("=" * 72)
print("VERDICT")
print("=" * 72)

# Recompute for verdict comparison
int4_G_strict = []
int4_G_content = []
for pid, d in scored.items():
    if pid in CONTROL_IDS: continue
    n16 = d["narrow"].get(BASELINE, {}); n4 = d["narrow"].get("4", {})
    if not n16 or not n4 or n16.get("strict", 0) == 0: continue
    comps = d["components"]
    cb_s = [v[BASELINE]["strict"] for v in comps.values() if BASELINE in v and v[BASELINE]["strict"] > 0]
    cs_s = [v["4"]["strict"] for v in comps.values() if BASELINE in v and v[BASELINE]["strict"] > 0 and "4" in v]
    cb_c = [v[BASELINE]["content"] for v in comps.values() if BASELINE in v and v[BASELINE]["content"] > 0]
    cs_c = [v["4"]["content"] for v in comps.values() if BASELINE in v and v[BASELINE]["content"] > 0 and "4" in v]
    if cb_s and cs_s:
        G_s = (sum(cs_s)/len(cs_s))/(sum(cb_s)/len(cb_s)) - n4["strict"]/n16["strict"]
        int4_G_strict.append(G_s)
    if cb_c and cs_c and n16.get("content", 0) > 0:
        G_c = (sum(cs_c)/len(cs_c))/(sum(cb_c)/len(cb_c)) - n4["content"]/n16["content"]
        int4_G_content.append(G_c)

pt_s, (lo_s, hi_s) = bootstrap_mean_ci(np.array(int4_G_strict))
pt_c, (lo_c, hi_c) = bootstrap_mean_ci(np.array(int4_G_content))

PASS_STRICT  = lo_s < 0 and hi_s < 0    # CI fully negative = inverse seam
PASS_CONTENT = lo_c <= 0 <= hi_c         # CI includes zero = flat

# Check FC1/vault3_token is COMPOUND_NOUN_DROP at INT4
fc1_vault3 = scored.get("FC1", {}).get("components", {})
vault3_class = next((v["4"]["failure_class"] for ck, v in fc1_vault3.items()
                     if "4" in v and v["4"].get("hop") == "vault3_token"), None)

fmt_loss_count_4b = sum(
    1 for d in scored.values()
    for arm in ("narrow", "broad")
    if d[arm].get("4", {}).get("failure_class") == "FORMAT_COMPLIANCE_LOSS"
) + sum(
    1 for d in scored.values()
    for bits_data in d["components"].values()
    if bits_data.get("4", {}).get("failure_class") == "FORMAT_COMPLIANCE_LOSS"
)

print(f"\n  G_strict(INT4)  = {pt_s:+.4f}  CI [{lo_s:+.4f}, {hi_s:+.4f}]")
print(f"  G_content(INT4) = {pt_c:+.4f}  CI [{lo_c:+.4f}, {hi_c:+.4f}]")
print(f"\n  strict inverse seam (CI fully negative) : {'YES' if PASS_STRICT else 'NO'}")
print(f"  content seam dissolved (CI includes 0)  : {'YES' if PASS_CONTENT else 'NO'}")
print(f"  FC1/vault3_token failure class @ INT4   : {vault3_class}")
print(f"  FORMAT_COMPLIANCE_LOSS items @ INT4     : {fmt_loss_count_4b}")

all_pass = PASS_STRICT and PASS_CONTENT and vault3_class == "COMPOUND_NOUN_DROP"
print()
if all_pass:
    print("  *** REGRESSION CHECK PASSED ***")
    print("  Dual scorer reproduces the manual Option A verdict.")
    print("  Scorer is validated against historical Exp 3 output.")
    print("  Proceed to fresh Experiment 4.")
else:
    print("  *** REGRESSION CHECK FAILED ***")
    print("  Mismatch between dual scorer and manual Option A verdict.")
    print("  Do NOT proceed to Experiment 4. Investigate the discrepancy.")
    if not PASS_STRICT:
        print(f"  - strict CI [{lo_s:.4f}, {hi_s:.4f}] does not fully exclude zero below")
    if not PASS_CONTENT:
        print(f"  - content CI [{lo_c:.4f}, {hi_c:.4f}] does not include zero")
    if vault3_class != "COMPOUND_NOUN_DROP":
        print(f"  - FC1/vault3_token classified as {vault3_class}, expected COMPOUND_NOUN_DROP")
