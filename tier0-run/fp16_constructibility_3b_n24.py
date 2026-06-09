#!/usr/bin/env python3
"""
fp16_constructibility_3b_n24.py — 3B FP16 n=24 baseline expansion.

Track:           Synthetic Key-Value Selection Constructibility
Manifest:        tasks_fork_a_n24.py  (L3 family, n=24)
Model:           Qwen/Qwen2.5-3B-Instruct  (FP16)
Pass gate:       ≥21/24 content PASS  (87.5% — same rate as n=8 gate)

Decision-token top-k logs are provenance and diagnostic artifacts only.
They are NOT used to make capability or mechanism claims.

Scope:
  This is an expanded n=24 L3 manifest run. Not a direct replication of L2 n=8.
  Result: 3B performance on the expanded baseline under the approved contract.
  Not a quantization, seam, general retrieval, or monotone threshold result.
"""

import hashlib
import json
import sys
import time
from pathlib import Path

import mlx.core as mx

try:
    from mlx_lm import load, stream_generate
    from mlx_lm.sample_utils import make_sampler
except ImportError:
    raise SystemExit("mlx-lm not found. Install with: pip install mlx-lm")

sys.path.insert(0, str(Path(__file__).parent))
from tasks_fork_a_n24 import (
    ITEMS,
    validate_tasks,
    get_manifest_hash,
    SCORER_SOURCE_FILE,
)
from tasks_exp8 import (
    score_arm2_content,
    score_arm2_format,
    score_arm2_scaffold,
    get_manifest_hash as get_scorer_hash,
)

# ── Approved hashes ───────────────────────────────────────────────────────────
APPROVED_MANIFEST_HASH = "sha256:28d249dc6a56fbad54be5606c4285eaa78f286f31acf22610357e40bf12a3481"
APPROVED_SCORER_HASH   = "sha256:4036b1ad0819be74e32521cea8f9117b503c6d9d79142969820175ecde95a1bc"

# ── Model ─────────────────────────────────────────────────────────────────────
MODEL_ID = "Qwen/Qwen2.5-3B-Instruct"

# ── Frozen settings ───────────────────────────────────────────────────────────
DECODING      = {"temperature": 0.0, "max_tokens": 16}
TOP_K_DEPTH   = 10
FEASIBILITY_N = 21   # ≥21/24 = 87.5%


# ── Hash utilities ────────────────────────────────────────────────────────────

def _hash_bytes(data: bytes) -> str:
    return f"sha256:{hashlib.sha256(data).hexdigest()}"


def compute_tokenizer_hash(tokenizer) -> str:
    ref = "ANSWER: ICVLX OBLVX OICVX PCIVX SCIVX"
    ids = tokenizer.encode(ref, add_special_tokens=False)
    payload = f"vocab_size={tokenizer.vocab_size}|ref_ids={ids}"
    return _hash_bytes(payload.encode())


def compute_runner_hash() -> str:
    return _hash_bytes(Path(__file__).read_bytes())


# ── Prompt formatting ─────────────────────────────────────────────────────────

def format_prompt(tokenizer, content: str):
    if getattr(tokenizer, "chat_template", None) is not None:
        messages = [{"role": "user", "content": content}]
        return tokenizer.apply_chat_template(messages, add_generation_prompt=True)
    return content


# ── Generation with top-k logging ─────────────────────────────────────────────

def run_with_topk(model, tokenizer, content: str, max_tokens: int, top_k: int):
    prompt    = format_prompt(tokenizer, content)
    full_text = ""
    top_k_log = []
    pos       = 0

    for response in stream_generate(
        model, tokenizer,
        prompt=prompt,
        max_tokens=max_tokens,
        sampler=make_sampler(temp=0.0),
    ):
        full_text += response.text
        logprobs   = response.logprobs

        top_indices = mx.argsort(-logprobs)[:top_k].tolist()
        top_lp      = [float(logprobs[i].item()) for i in top_indices]

        top_k_log.append({
            "response_pos": pos,
            "token_id":     response.token,
            "token_str":    tokenizer.decode([response.token]),
            "top_k": [
                {
                    "rank":      rank + 1,
                    "token_id":  tid,
                    "token_str": tokenizer.decode([tid]),
                    "logprob":   lp,
                }
                for rank, (tid, lp) in enumerate(zip(top_indices, top_lp))
            ],
        })
        pos += 1

    _annotate_decision_token(top_k_log)
    return full_text, top_k_log


def _annotate_decision_token(top_k_log: list) -> None:
    accumulated     = ""
    decision_marked = False
    scaffold_prefix = "ANSWER: "

    for entry in top_k_log:
        entry["is_decision_token"] = False
        accumulated += entry["token_str"]
        if not decision_marked and scaffold_prefix in accumulated:
            after = accumulated.split(scaffold_prefix, 1)[1]
            if after.strip():
                entry["is_decision_token"] = True
                decision_marked = True


# ── Preflight ─────────────────────────────────────────────────────────────────

def run_preflight(tokenizer) -> dict:
    manifest_hash = get_manifest_hash()
    scorer_hash   = get_scorer_hash()
    runner_hash   = compute_runner_hash()
    tokenizer_hash = compute_tokenizer_hash(tokenizer)

    if manifest_hash != APPROVED_MANIFEST_HASH:
        raise SystemExit(
            f"[STOP-1] Manifest hash mismatch.\n"
            f"  computed: {manifest_hash}\n"
            f"  approved: {APPROVED_MANIFEST_HASH}"
        )
    if scorer_hash != APPROVED_SCORER_HASH:
        raise SystemExit(
            f"[STOP-1] Scorer hash mismatch.\n"
            f"  computed: {scorer_hash}\n"
            f"  approved: {APPROVED_SCORER_HASH}"
        )

    print("Running validator (tasks_fork_a_n24.py validate_tasks)...")
    ok = validate_tasks()
    if not ok:
        raise SystemExit("[STOP-1] Validator failed. Do not proceed.")
    print()

    record = {
        "preflight_ok":      True,
        "model_id":          MODEL_ID,
        "manifest_hash":     manifest_hash,
        "approved_manifest": APPROVED_MANIFEST_HASH,
        "scorer_hash":       scorer_hash,
        "approved_scorer":   APPROVED_SCORER_HASH,
        "validator_hash":    manifest_hash,
        "tokenizer_hash":    tokenizer_hash,
        "runner_hash":       runner_hash,
        "decoding":          DECODING,
        "top_k_depth":       TOP_K_DEPTH,
        "n_items":           len(ITEMS),
        "feasibility_n":     FEASIBILITY_N,
        "scorer_source":     SCORER_SOURCE_FILE,
    }

    print("=== PREFLIGHT ===")
    for k, v in record.items():
        print(f"  {k:<26} {v}")
    print()

    return record


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    run_ts = int(time.time())

    print(f"=== Synthetic Key-Value Selection Constructibility ===")
    print(f"Track:           3B FP16 n=24 baseline expansion")
    print(f"Manifest:        tasks_fork_a_n24.py  (L3 family)")
    print(f"Model:           {MODEL_ID}")
    print(f"Pass gate:       ≥{FEASIBILITY_N}/{len(ITEMS)} (87.5%)")
    print(f"Top-k:           depth={TOP_K_DEPTH} — provenance/diagnostic only")
    print(f"Note:            Not a direct replication of L2 n=8 screen.")
    print(f"                 Not a quantization, seam, or threshold result.")
    print()

    # Pre-load manifest hash check
    manifest_hash = get_manifest_hash()
    if manifest_hash != APPROVED_MANIFEST_HASH:
        raise SystemExit(f"[STOP-1] Manifest hash mismatch (pre-load).")

    print(f"Loading {MODEL_ID} at FP16...")
    model, tokenizer = load(MODEL_ID)
    print()

    preflight = run_preflight(tokenizer)

    results           = []
    pass_count        = 0
    numeric_ooc_count = 0

    for item in ITEMS:
        pid = item["id"]
        ts  = int(time.time())

        raw_output, top_k_log = run_with_topk(
            model, tokenizer,
            item["prompt"],
            DECODING["max_tokens"],
            TOP_K_DEPTH,
        )

        sc = score_arm2_scaffold(raw_output)
        f  = score_arm2_format(raw_output)
        c  = score_arm2_content(raw_output, item)

        is_pass = c["is_correct"]
        if is_pass:
            pass_count += 1

        is_numeric_ooc = (
            sc["scaffold_class"] == "SCAFFOLD_PRESENT"
            and f["format_class"] == "FORMAT_FAIL"
            and c["content_class"] == "RETURNED_NON_CONTEXT_TOKEN"
            and c["returned_token"] is not None
            and not str(c["returned_token"]).isalpha()
        )
        if is_numeric_ooc:
            numeric_ooc_count += 1

        subj_prefixes = sorted({s[0] for s, _ in item["facts"]})
        obj_prefixes  = sorted({o[0] for _, o in item["facts"]})

        print(f"--- {pid}  pos={item['target_pos']}  "
              f"target={item['target_subj']}→{item['target_obj']} ---")
        print(f"  raw_output:             {raw_output!r}")
        print(f"  scaffold_class:         {sc['scaffold_class']}")
        print(f"  format_class:           {f['format_class']}")
        print(f"  content_class:          {c['content_class']}")
        print(f"  returned_token:         {c['returned_token']}")
        print(f"  returned_fact_position: {c['returned_fact_position']}")
        print(f"  subj_pfx:               {subj_prefixes}")
        print(f"  PASS:                   {is_pass}")

        decision_entries = [e for e in top_k_log if e.get("is_decision_token")]
        if decision_entries:
            de   = decision_entries[0]
            top3 = de["top_k"][:3]
            print(f"  decision_pos:           {de['response_pos']}  "
                  f"(token: {de['token_str']!r})")
            print(f"  top-3 at decision:      "
                  + ", ".join(
                      f"{e['token_str']!r}({e['logprob']:.3f})" for e in top3
                  ))
        print()

        results.append({
            "id":                       pid,
            "target_pos":               item["target_pos"],
            "target_subj":              item["target_subj"],
            "target_obj":               item["target_obj"],
            "prompt_hash":              item["prompt_hash"],
            "raw_output":               raw_output,
            "scaffold_class":           sc["scaffold_class"],
            "format_class":             f["format_class"],
            "content_class":            c["content_class"],
            "returned_token":           c["returned_token"],
            "returned_token_role":      c["returned_token_role"],
            "returned_fact_position":   c["returned_fact_position"],
            "same_error_identity_key":  c["same_error_identity_key"],
            "is_numeric_ooc":           is_numeric_ooc,
            "is_correct":               is_pass,
            "diagnostic": {
                "subj_prefixes": subj_prefixes,
                "obj_prefixes":  obj_prefixes,
            },
            "top_k_log":   top_k_log,
            "timestamp":   ts,
        })

    # ── Summary ───────────────────────────────────────────────────────────────
    cond_met = pass_count >= FEASIBILITY_N

    class_counts: dict[str, int] = {}
    for r in results:
        cc = r["content_class"]
        class_counts[cc] = class_counts.get(cc, 0) + 1

    pos_breakdown: dict[int, dict] = {}
    for r in results:
        p = r["target_pos"]
        if p not in pos_breakdown:
            pos_breakdown[p] = {"pass": 0, "fail": 0, "items": []}
        if r["is_correct"]:
            pos_breakdown[p]["pass"] += 1
        else:
            pos_breakdown[p]["fail"] += 1
        pos_breakdown[p]["items"].append(r["id"])

    print(f"=== SUMMARY — 3B n=24 ===")
    print(f"Pass count:     {pass_count}/{len(ITEMS)}  ({100*pass_count/len(ITEMS):.1f}%)")
    print(f"Gate:           ≥{FEASIBILITY_N}/{len(ITEMS)} (87.5%)")
    print(f"Result:         {'PASS' if cond_met else 'FAIL'}")
    print()
    print(f"Content class breakdown:")
    for cc, n in sorted(class_counts.items()):
        print(f"  {cc}: {n}")
    print()
    print(f"Position subgroup (diagnostic — does not modify gate):")
    for p in sorted(pos_breakdown.keys()):
        pb = pos_breakdown[p]
        print(f"  pos={p}: {pb['pass']}/{pb['pass']+pb['fail']} pass")
    print()
    print(f"Note: partial subgroup success does not license INT8/INT4 or seam testing.")

    # ── Write JSON ────────────────────────────────────────────────────────────
    out_path = Path(f"fp16_constructibility_3b_n24_{run_ts}.json")
    out_data = {
        "track":             "Synthetic Key-Value Selection Constructibility",
        "run_type":          "3B FP16 n=24 baseline expansion",
        "manifest_family":   "L3",
        "model_id":          MODEL_ID,
        "bits":              16,
        "preflight":         preflight,
        "fresh_generation":  True,
        "decoding":          DECODING,
        "top_k_depth":       TOP_K_DEPTH,
        "top_k_note": (
            "Decision-token top-k logs are provenance and diagnostic artifacts only. "
            "Not used to make capability or mechanism claims."
        ),
        "scope_note": (
            "Expanded L3 n=24 manifest. Not a direct replication of L2 n=8 screen. "
            "Not a quantization, seam, general retrieval, or monotone threshold result."
        ),
        "run_timestamp":          run_ts,
        "n_items":                len(ITEMS),
        "pass_count":             pass_count,
        "pass_rate":              pass_count / len(ITEMS),
        "feasibility_n":          FEASIBILITY_N,
        "feasible":               cond_met,
        "numeric_ooc_count":      numeric_ooc_count,
        "content_class_breakdown": class_counts,
        "position_subgroup":      pos_breakdown,
        "results":                results,
    }
    out_path.write_text(json.dumps(out_data, indent=2))
    print(f"\nWrote: {out_path}")


if __name__ == "__main__":
    main()
