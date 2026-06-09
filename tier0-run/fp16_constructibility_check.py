#!/usr/bin/env python3
"""
fp16_constructibility_check.py — Synthetic Key-Value Selection Constructibility
Two-rung frozen-construction constructibility check: 3B and 7B.

Track name:      Synthetic Key-Value Selection Constructibility
Operational q:   Given a synthetic key, select and emit its paired synthetic value
                 from a fixed five-fact context under a fixed output contract.
Authorized rungs: 3B → 7B (FP16 feasibility, n=8 only)

Frozen construction: imports items, scorer, and validator unchanged from tasks_exp8.py.
Any modification to tasks_exp8.py triggers STOP-1 (manifest hash mismatch).

Decision-token top-k logs are provenance and diagnostic artifacts only.
They are NOT used to make capability or mechanism claims.

Usage:
  python3 fp16_constructibility_check.py --size 3b
  python3 fp16_constructibility_check.py --size 7b
"""

import argparse
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
from tasks_exp8 import (
    ITEMS,
    score_arm2_content,
    score_arm2_format,
    score_arm2_scaffold,
    validate_tasks,
    get_manifest_hash,
)

# ── Approved manifest hash (covers items + scorer + validator) ───────────────
APPROVED_MANIFEST_HASH = "sha256:4036b1ad0819be74e32521cea8f9117b503c6d9d79142969820175ecde95a1bc"

# ── Authorized model IDs ─────────────────────────────────────────────────────
AUTHORIZED_MODELS = {
    "3b": "Qwen/Qwen2.5-3B-Instruct",
    "7b": "Qwen/Qwen2.5-7B-Instruct",
}

# ── Fixed decoding (frozen) ──────────────────────────────────────────────────
DECODING = {"temperature": 0.0, "max_tokens": 16}

# ── Top-k depth (pre-registered) ─────────────────────────────────────────────
TOP_K_DEPTH = 10

# ── Pass/fail criterion (frozen) ─────────────────────────────────────────────
FEASIBILITY_N = 7  # ≥7/8 content PASS required


# ── Hash utilities ────────────────────────────────────────────────────────────

def _hash_bytes(data: bytes) -> str:
    return f"sha256:{hashlib.sha256(data).hexdigest()}"


def compute_tokenizer_hash(tokenizer) -> str:
    """
    Compute a deterministic tokenizer hash from vocab size + round-trip
    encoding of a fixed reference string. Captures tokenizer identity
    without requiring file-system access to the model cache.
    """
    ref = "ANSWER: ICVLX OBLVX OICVX PCIVX SCIVX"
    ids = tokenizer.encode(ref, add_special_tokens=False)
    payload = f"vocab_size={tokenizer.vocab_size}|ref_ids={ids}"
    return _hash_bytes(payload.encode())


def compute_runner_hash() -> str:
    return _hash_bytes(Path(__file__).read_bytes())


# ── Prompt formatting ─────────────────────────────────────────────────────────

def format_prompt(tokenizer, content: str):
    """Apply chat template if available, else pass content as-is."""
    if getattr(tokenizer, "chat_template", None) is not None:
        messages = [{"role": "user", "content": content}]
        return tokenizer.apply_chat_template(messages, add_generation_prompt=True)
    return content


# ── Generation with top-k logging ─────────────────────────────────────────────

def run_with_topk(model, tokenizer, content: str, max_tokens: int, top_k: int):
    """
    Run generation via stream_generate, collecting per-token top-k logprobs.

    Returns:
        raw_output (str): full generated text
        top_k_log (list): one entry per generated token, each with top-k ranked
                          token IDs, decoded strings, and log-probabilities
    """
    prompt = format_prompt(tokenizer, content)

    full_text = ""
    top_k_log = []
    pos = 0

    for response in stream_generate(
        model,
        tokenizer,
        prompt=prompt,
        max_tokens=max_tokens,
        sampler=make_sampler(temp=0.0),
    ):
        token_text = response.text
        full_text += token_text

        logprobs = response.logprobs  # mx.array, shape [vocab_size]

        # Extract top-k indices by descending logprob
        top_indices = mx.argsort(-logprobs)[:top_k].tolist()
        top_lp = [float(logprobs[i].item()) for i in top_indices]

        top_k_entry = {
            "response_pos": pos,
            "token_id": response.token,
            "token_str": tokenizer.decode([response.token]),
            "top_k": [
                {
                    "rank": rank + 1,
                    "token_id": tid,
                    "token_str": tokenizer.decode([tid]),
                    "logprob": lp,
                }
                for rank, (tid, lp) in enumerate(zip(top_indices, top_lp))
            ],
        }
        top_k_log.append(top_k_entry)
        pos += 1

    # Annotate decision token: first response position whose decoded token
    # begins the answer value (appears after "ANSWER: " in accumulated text)
    _annotate_decision_token(top_k_log, tokenizer)

    return full_text, top_k_log


def _annotate_decision_token(top_k_log: list, tokenizer) -> None:
    """
    Mark the first generated token that starts the answer value
    (the token immediately following the 'ANSWER: ' scaffold prefix).

    Annotation is in-place: adds 'is_decision_token' boolean to each entry.
    """
    accumulated = ""
    decision_marked = False
    scaffold_prefix = "ANSWER: "

    for entry in top_k_log:
        entry["is_decision_token"] = False
        accumulated += entry["token_str"]
        # Once scaffold prefix is complete and this token extends beyond it,
        # this position is the start of the answer value
        if not decision_marked and scaffold_prefix in accumulated:
            after = accumulated.split(scaffold_prefix, 1)[1]
            if after.strip():
                entry["is_decision_token"] = True
                decision_marked = True


# ── Preflight ─────────────────────────────────────────────────────────────────

def run_preflight(model_id: str, tokenizer, manifest_hash: str, size: str) -> dict:
    """
    Emit and verify all preflight fields. Returns preflight record.
    Raises SystemExit on any mismatch (STOP-1).
    """
    runner_hash     = compute_runner_hash()
    tokenizer_hash  = compute_tokenizer_hash(tokenizer)
    scorer_hash     = manifest_hash   # scorer lives in tasks_exp8.py
    validator_hash  = manifest_hash   # validator lives in tasks_exp8.py

    # Manifest gate
    if manifest_hash != APPROVED_MANIFEST_HASH:
        raise SystemExit(
            f"[STOP-1] Manifest hash mismatch.\n"
            f"  computed: {manifest_hash}\n"
            f"  approved: {APPROVED_MANIFEST_HASH}\n"
            "tasks_exp8.py was modified after approval. Do not proceed."
        )

    # Validator gate: run all static checks before any model call
    print("Running validator (tasks_exp8.py validate_tasks)...")
    ok = validate_tasks()
    if not ok:
        raise SystemExit("[STOP-1] Validator failed. Do not proceed.")
    print()

    record = {
        "preflight_ok":     True,
        "model_id":         model_id,
        "size":             size,
        "manifest_hash":    manifest_hash,
        "approved_hash":    APPROVED_MANIFEST_HASH,
        "hash_match":       True,
        "scorer_hash":      scorer_hash,
        "validator_hash":   validator_hash,
        "tokenizer_hash":   tokenizer_hash,
        "runner_hash":      runner_hash,
        "decoding":         DECODING,
        "top_k_depth":      TOP_K_DEPTH,
        "n_items":          len(ITEMS),
        "feasibility_n":    FEASIBILITY_N,
        "note_scorer_validator": (
            "scorer_hash and validator_hash are identical to manifest_hash: "
            "scorer and validator are defined in tasks_exp8.py (same file as items)."
        ),
    }

    print("=== PREFLIGHT ===")
    for k, v in record.items():
        if k != "note_scorer_validator":
            print(f"  {k:<25} {v}")
    print(f"  note: {record['note_scorer_validator']}")
    print()

    return record


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Synthetic Key-Value Selection Constructibility — FP16 check"
    )
    parser.add_argument(
        "--size", required=True, choices=["3b", "7b"],
        help="Model size rung to run (3b or 7b)"
    )
    args = parser.parse_args()

    size     = args.size
    model_id = AUTHORIZED_MODELS[size]
    run_ts   = int(time.time())

    print(f"=== Synthetic Key-Value Selection Constructibility ===")
    print(f"Track:           Two-rung frozen-construction constructibility check")
    print(f"Rung:            {size.upper()} — {model_id}")
    print(f"Frozen construction: tasks_exp8.py (Exp8-lineage, n=8)")
    print(f"Top-k depth:     {TOP_K_DEPTH} (pre-registered)")
    print(f"Note:            Decision-token top-k logs are provenance/diagnostic only.")
    print(f"                 Not used to make capability or mechanism claims.")
    print()

    # ── Manifest check (pre-load) ─────────────────────────────────────────────
    manifest_hash = get_manifest_hash()
    if manifest_hash != APPROVED_MANIFEST_HASH:
        raise SystemExit(
            f"[STOP-1] Manifest hash mismatch (pre-load check).\n"
            f"  computed: {manifest_hash}\n"
            f"  approved: {APPROVED_MANIFEST_HASH}"
        )

    # ── Load model ────────────────────────────────────────────────────────────
    print(f"Loading {model_id} at FP16...")
    model, tokenizer = load(model_id)
    print()

    # ── Preflight (post-load — includes tokenizer hash) ───────────────────────
    preflight = run_preflight(model_id, tokenizer, manifest_hash, size)

    # ── Run items ────────────────────────────────────────────────────────────
    results      = []
    pass_count   = 0
    numeric_ooc_count = 0

    for item in ITEMS:
        pid  = item["id"]
        ts   = int(time.time())

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

        # Prefix-family metadata (diagnostic annotation — not a scorer class)
        subj_prefixes = sorted({s[0] for s, _ in item["facts"]})
        obj_prefixes  = sorted({o[0] for _, o in item["facts"]})
        homogeneous_subj_prefix = len(subj_prefixes) == 1
        homogeneous_obj_prefix  = len(obj_prefixes) == 1

        print(f"--- {pid}  target_pos={item['target_pos']}  "
              f"target={item['target_subj']}→{item['target_obj']} ---")
        print(f"  raw_output:             {raw_output!r}")
        print(f"  scaffold_class:         {sc['scaffold_class']}")
        print(f"  format_class:           {f['format_class']}")
        print(f"  content_class:          {c['content_class']}")
        print(f"  returned_token:         {c['returned_token']}")
        print(f"  returned_fact_position: {c['returned_fact_position']}")
        print(f"  homogeneous_subj_pfx:   {homogeneous_subj_prefix}  ({subj_prefixes})")
        print(f"  numeric_ooc:            {is_numeric_ooc}")
        print(f"  PASS:                   {is_pass}")

        # Print top-k at decision token position only
        decision_entries = [e for e in top_k_log if e.get("is_decision_token")]
        if decision_entries:
            de = decision_entries[0]
            print(f"  decision_token_pos:     {de['response_pos']}  "
                  f"(generated: {de['token_str']!r})")
            top3 = de["top_k"][:3]
            print(f"  top-3 at decision:      "
                  + ", ".join(
                      f"{e['token_str']!r}({e['logprob']:.3f})" for e in top3
                  ))
        print()

        results.append({
            "id":                        pid,
            "target_pos":                item["target_pos"],
            "target_subj":               item["target_subj"],
            "target_obj":                item["target_obj"],
            "prompt_hash":               item["prompt_hash"],
            "raw_output":                raw_output,
            "scaffold_class":            sc["scaffold_class"],
            "format_class":              f["format_class"],
            "content_class":             c["content_class"],
            "returned_token":            c["returned_token"],
            "returned_token_role":       c["returned_token_role"],
            "returned_fact_position":    c["returned_fact_position"],
            "same_error_identity_key":   c["same_error_identity_key"],
            "is_numeric_ooc":            is_numeric_ooc,
            "is_correct":                is_pass,
            "diagnostic": {
                "subj_prefixes":             subj_prefixes,
                "obj_prefixes":              obj_prefixes,
                "homogeneous_subj_prefix":   homogeneous_subj_prefix,
                "homogeneous_obj_prefix":    homogeneous_obj_prefix,
            },
            "top_k_log":                 top_k_log,
            "timestamp":                 ts,
        })

    # ── Ladder rule evaluation ────────────────────────────────────────────────
    cond_met = pass_count >= FEASIBILITY_N

    # Content class breakdown
    class_counts: dict[str, int] = {}
    for r in results:
        cc = r["content_class"]
        class_counts[cc] = class_counts.get(cc, 0) + 1

    # Position subgroup breakdown
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

    print(f"=== SUMMARY — {size.upper()} rung ===")
    print(f"Pass count:          {pass_count}/{len(ITEMS)}")
    print(f"Feasibility gate:    >={FEASIBILITY_N}/{len(ITEMS)}")
    print(f"Result:              {'FEASIBLE' if cond_met else 'NOT FEASIBLE'}")
    print()
    print(f"Ladder rule:")
    if cond_met:
        print(f"  {size.upper()} PASSES → stop ladder, request Manager auth for n≥20")
    else:
        if size == "3b":
            print(f"  3B NOT FEASIBLE → record failure content, proceed to 7B")
        else:
            print(f"  7B NOT FEASIBLE → constructibility not achieved across authorized range")
    print()
    print(f"Content class breakdown:")
    for cc, n in sorted(class_counts.items()):
        print(f"  {cc}: {n}")
    print()
    print(f"Position subgroup (diagnostic only — does not modify pass/fail gate):")
    for p in sorted(pos_breakdown.keys()):
        pb = pos_breakdown[p]
        print(f"  pos={p}: {pb['pass']}/{pb['pass']+pb['fail']} pass  ({pb['items']})")
    print()
    print(f"Note: partial subgroup success does not license n≥20, INT8/INT4, or seam testing.")

    # ── Write JSON ────────────────────────────────────────────────────────────
    out_path = Path(f"fp16_constructibility_{size}_{run_ts}.json")
    out_data = {
        "track":             "Synthetic Key-Value Selection Constructibility",
        "run_type":          "two-rung frozen-construction constructibility check",
        "rung":              size,
        "model_id":          model_id,
        "bits":              16,
        "preflight":         preflight,
        "fresh_generation":  True,
        "decoding":          DECODING,
        "top_k_depth":       TOP_K_DEPTH,
        "top_k_note":        (
            "Decision-token top-k logs are provenance and diagnostic artifacts only. "
            "Not used to make capability or mechanism claims."
        ),
        "run_timestamp":     run_ts,
        "n_items":           len(ITEMS),
        "pass_count":        pass_count,
        "feasibility_n":     FEASIBILITY_N,
        "feasible":          cond_met,
        "numeric_ooc_count": numeric_ooc_count,
        "content_class_breakdown": class_counts,
        "position_subgroup": pos_breakdown,
        "ladder_rule_note":  (
            "Partial subgroup success is diagnostic only. "
            "Does not license n>=20, INT8/INT4, or seam testing."
        ),
        "results":           results,
    }
    out_path.write_text(json.dumps(out_data, indent=2))
    print(f"\nWrote: {out_path}")


if __name__ == "__main__":
    main()
