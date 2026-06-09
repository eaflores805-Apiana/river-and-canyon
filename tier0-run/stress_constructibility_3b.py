#!/usr/bin/env python3
"""
stress_constructibility_3b.py — INT8 stress run, 3B n=24.

Track:           Synthetic Key-Value Selection Constructibility
Manifest:        tasks_fork_a_n24.py  (L3 family, n=24)
Model:           Qwen/Qwen2.5-3B-Instruct  (INT8)
Pass gate:       ≥21/24 content PASS  (87.5%)
FP16 reference:  fp16_constructibility_3b_n24_1780867214.json

Authorization:   INT8 (Manager authorization 2026-06-07)
                 INT4 (Manager authorization 2026-06-07)

Decision-token top-k logs are provenance and diagnostic artifacts only.
They are NOT used to make capability or mechanism claims.

Hardening corrections applied:
  (1) quant_model_manifest_hash: sha256 over sorted manifest (relative path,
      file size, per-file sha256) of all converted model files — proves
      weights are unchanged, not just config.json.
  (2) Exact-output agreement: fraction of items where stressed raw_output ==
      FP16 raw_output. Field named "exact_output_agreement" throughout.

Quant hash locking workflow:
  Pass 1  — APPROVED_QUANT_* constants are None → script converts model,
             prints computed hashes, and exits with locking instructions.
  Pass 2  — Copy printed values into constants below, re-run → script gates
             on match before any item is scored (STOP-2 on mismatch).
"""

import argparse
import hashlib
import json
import subprocess
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

# ── Approved manifest and scorer hashes ───────────────────────────────────────
APPROVED_MANIFEST_HASH = "sha256:28d249dc6a56fbad54be5606c4285eaa78f286f31acf22610357e40bf12a3481"
APPROVED_SCORER_HASH   = "sha256:4036b1ad0819be74e32521cea8f9117b503c6d9d79142969820175ecde95a1bc"

# ── Quant provenance hashes — per bits level (None until locked) ───────────────
# Locking workflow per bits level:
#   1. Run once with the entry for that bits set to None → computes and prints
#      hashes for that quantization, then exits.
#   2. Copy printed values into the appropriate dict entry and re-run →
#      gates on match (STOP-2 on mismatch).
APPROVED_QUANT_CONFIG_HASH: dict = {
    8: "sha256:0a73a0b1727e55ef5637e32e9897ad3f10b6d525f4d76c506ab7e9b87042d5f8",
    4: "sha256:9e79b9b727d0e06db1389f06c0b8e77fdb91fe00accfac0718db98fdeb7c5d3e",
}
APPROVED_QUANT_MODEL_MANIFEST_HASH: dict = {
    8: "sha256:3f94f6430eb5b2bed59a2500b38a3b42b554a146cc6cb89eb3468dddb833a023",
    4: "sha256:7ca665f0005a428d2826bc38b836ad566fe16744f9b7697cad57f384adcf2678",
}

# ── FP16 reference ────────────────────────────────────────────────────────────
FP16_REF_PATH = Path(__file__).parent / "fp16_constructibility_3b_n24_1780867214.json"

# ── Model ─────────────────────────────────────────────────────────────────────
MODEL_ID  = "Qwen/Qwen2.5-3B-Instruct"
QUANT_DIR = {
    8: Path(__file__).parent / "Qwen2.5-3B-Instruct-mlx-int8",
    4: Path(__file__).parent / "Qwen2.5-3B-Instruct-mlx-int4",
}

# ── Frozen settings ───────────────────────────────────────────────────────────
DECODING      = {"temperature": 0.0, "max_tokens": 16}
TOP_K_DEPTH   = 10
FEASIBILITY_N = 21   # ≥21/24 = 87.5%

# ── Authorization gate ────────────────────────────────────────────────────────
AUTHORIZED_BITS = {8, 4}   # INT4 authorized by Manager 2026-06-07


# ── Hash utilities ────────────────────────────────────────────────────────────

def _hash_bytes(data: bytes) -> str:
    return f"sha256:{hashlib.sha256(data).hexdigest()}"


def compute_quant_config_hash(model_dir: Path) -> str:
    return _hash_bytes((model_dir / "config.json").read_bytes())


def compute_quant_model_manifest_hash(model_dir: Path) -> str:
    """sha256 over sorted manifest of (relative path, file size, per-file sha256)."""
    entries = []
    for f in sorted(model_dir.rglob("*")):
        if f.is_file():
            rel       = str(f.relative_to(model_dir))
            size      = f.stat().st_size
            file_hash = hashlib.sha256(f.read_bytes()).hexdigest()
            entries.append(f"{rel}|{size}|{file_hash}")
    return _hash_bytes("\n".join(entries).encode())


def compute_tokenizer_hash(tokenizer) -> str:
    ref = "ANSWER: ICVLX OBLVX OICVX PCIVX SCIVX"
    ids = tokenizer.encode(ref, add_special_tokens=False)
    payload = f"vocab_size={tokenizer.vocab_size}|ref_ids={ids}"
    return _hash_bytes(payload.encode())


def compute_runner_hash() -> str:
    return _hash_bytes(Path(__file__).read_bytes())


# ── Model conversion ──────────────────────────────────────────────────────────

def convert_model(hf_path: str, mlx_path: Path, bits: int) -> None:
    print(f"Converting {hf_path} → INT{bits} at {mlx_path} ...")
    subprocess.run(
        [
            sys.executable, "-m", "mlx_lm.convert",
            "--hf-path",      hf_path,
            "--mlx-path",     str(mlx_path),
            "--quantize",
            "--q-bits",       str(bits),
            "--q-group-size", "64",
        ],
        check=True,
    )
    print(f"Conversion complete: {mlx_path}")
    print()


# ── FP16 reference loader ─────────────────────────────────────────────────────

def load_fp16_reference(ref_path: Path) -> dict:
    """Returns {item_id: {raw_output, content_class, format_class}}."""
    if not ref_path.exists():
        raise SystemExit(f"[STOP-1] FP16 reference not found: {ref_path}")
    data = json.loads(ref_path.read_text())
    return {
        r["id"]: {
            "raw_output":    r["raw_output"],
            "content_class": r["content_class"],
            "format_class":  r["format_class"],
        }
        for r in data["results"]
    }


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


# ── Quant hash locking workflow ───────────────────────────────────────────────

def run_hash_lock_workflow(model_dir: Path, bits: int) -> None:
    """Compute and print quant hashes for this bits level, then exit with locking instructions."""
    print("=" * 72)
    print(f"QUANT HASH LOCKING WORKFLOW  (INT{bits})")
    print("=" * 72)
    print()
    print(f"APPROVED_QUANT_CONFIG_HASH[{bits}] and/or")
    print(f"APPROVED_QUANT_MODEL_MANIFEST_HASH[{bits}] are None.")
    print("Computing hashes from converted model directory...")
    print()

    config_hash   = compute_quant_config_hash(model_dir)
    manifest_hash = compute_quant_model_manifest_hash(model_dir)

    print(f"  quant_config_hash         = {config_hash!r}")
    print(f"  quant_model_manifest_hash = {manifest_hash!r}")
    print()
    print(f"ACTION REQUIRED — copy these values into the INT{bits} dict entries:")
    print()
    print(f'  APPROVED_QUANT_CONFIG_HASH[{bits}]         = "{config_hash}"')
    print(f'  APPROVED_QUANT_MODEL_MANIFEST_HASH[{bits}] = "{manifest_hash}"')
    print()
    print("After locking, re-run to execute the scored stress run.")
    print("The runner will gate on these hashes before any item is scored.")
    raise SystemExit(0)


# ── Preflight ─────────────────────────────────────────────────────────────────

def run_preflight(tokenizer, model_dir: Path, bits: int) -> dict:
    manifest_hash  = get_manifest_hash()
    scorer_hash    = get_scorer_hash()
    runner_hash    = compute_runner_hash()
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

    quant_config_hash         = compute_quant_config_hash(model_dir)
    quant_model_manifest_hash = compute_quant_model_manifest_hash(model_dir)

    approved_cfg = APPROVED_QUANT_CONFIG_HASH.get(bits)
    approved_mfst = APPROVED_QUANT_MODEL_MANIFEST_HASH.get(bits)

    if approved_cfg is not None:
        if quant_config_hash != approved_cfg:
            raise SystemExit(
                f"[STOP-2] quant_config_hash mismatch (INT{bits}).\n"
                f"  computed: {quant_config_hash}\n"
                f"  approved: {approved_cfg}"
            )
    if approved_mfst is not None:
        if quant_model_manifest_hash != approved_mfst:
            raise SystemExit(
                f"[STOP-2] quant_model_manifest_hash mismatch (INT{bits}).\n"
                f"  computed: {quant_model_manifest_hash}\n"
                f"  approved: {approved_mfst}"
            )

    print("Running validator (tasks_fork_a_n24.py validate_tasks)...")
    ok = validate_tasks()
    if not ok:
        raise SystemExit("[STOP-1] Validator failed. Do not proceed.")
    print()

    record = {
        "preflight_ok":                    True,
        "model_id":                        MODEL_ID,
        "bits":                            bits,
        "manifest_hash":                   manifest_hash,
        "approved_manifest":               APPROVED_MANIFEST_HASH,
        "scorer_hash":                     scorer_hash,
        "approved_scorer":                 APPROVED_SCORER_HASH,
        "validator_hash":                  manifest_hash,
        "tokenizer_hash":                  tokenizer_hash,
        "runner_hash":                     runner_hash,
        "quant_config_hash":               quant_config_hash,
        "quant_model_manifest_hash":       quant_model_manifest_hash,
        "quant_config_hash_locked":        APPROVED_QUANT_CONFIG_HASH.get(bits) is not None,
        "quant_model_manifest_hash_locked": APPROVED_QUANT_MODEL_MANIFEST_HASH.get(bits) is not None,
        "decoding":                        DECODING,
        "top_k_depth":                     TOP_K_DEPTH,
        "n_items":                         len(ITEMS),
        "feasibility_n":                   FEASIBILITY_N,
        "scorer_source":                   SCORER_SOURCE_FILE,
    }

    print("=== PREFLIGHT ===")
    for k, v in record.items():
        print(f"  {k:<42} {v}")
    print()

    return record


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="INT8 stress run — Synthetic Key-Value Selection Constructibility, 3B n=24"
    )
    parser.add_argument(
        "--bits", type=int, choices=[8, 4], default=8,
        help="Quantization bits (default: 8)",
    )
    parser.add_argument(
        "--convert-only", action="store_true",
        help="Convert model and lock hashes only — do not execute scored run",
    )
    args = parser.parse_args()

    bits = args.bits

    if bits not in AUTHORIZED_BITS:
        raise SystemExit(
            f"[NOT-AUTHORIZED] INT{bits} is not authorized for this run.\n"
            f"  Authorized bits: {sorted(AUTHORIZED_BITS)}\n"
            f"  Requires Manager authorization."
        )

    run_ts    = int(time.time())
    quant_dir = QUANT_DIR[bits]

    print(f"=== Synthetic Key-Value Selection Constructibility ===")
    print(f"Track:           3B INT{bits} stress run")
    print(f"Manifest:        tasks_fork_a_n24.py  (L3 family, n=24)")
    print(f"Model:           {MODEL_ID}  (INT{bits})")
    print(f"Pass gate:       ≥{FEASIBILITY_N}/{len(ITEMS)} (87.5%)")
    print(f"FP16 reference:  {FP16_REF_PATH.name}")
    print(f"Top-k:           depth={TOP_K_DEPTH} — provenance/diagnostic only")
    print(f"Authorization:   INT{bits} (Manager 2026-06-07)")
    print()

    # Pre-load manifest hash check
    if get_manifest_hash() != APPROVED_MANIFEST_HASH:
        raise SystemExit("[STOP-1] Manifest hash mismatch (pre-load).")

    # Convert model if not already present
    if not quant_dir.exists():
        convert_model(MODEL_ID, quant_dir, bits)
    else:
        print(f"Using existing converted model: {quant_dir}")
        print()

    # Hash locking workflow (exits if hashes not yet locked for this bits level)
    if APPROVED_QUANT_CONFIG_HASH.get(bits) is None or APPROVED_QUANT_MODEL_MANIFEST_HASH.get(bits) is None:
        run_hash_lock_workflow(quant_dir, bits)
        # always raises SystemExit — unreachable

    if args.convert_only:
        print("--convert-only: exiting before scored run.")
        raise SystemExit(0)

    # Load FP16 reference
    fp16_ref = load_fp16_reference(FP16_REF_PATH)

    print(f"Loading INT{bits} model from {quant_dir} ...")
    model, tokenizer = load(str(quant_dir))
    print()

    preflight = run_preflight(tokenizer, quant_dir, bits)

    results              = []
    pass_count           = 0
    numeric_ooc_count    = 0
    exact_output_matches = 0

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

        fp16_entry  = fp16_ref.get(pid, {})
        fp16_raw    = fp16_entry.get("raw_output", "")
        exact_match = (raw_output == fp16_raw)
        if exact_match:
            exact_output_matches += 1

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
        print(f"  fp16_raw:               {fp16_raw!r}")
        print(f"  exact_output_match:     {exact_match}")
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
            "fp16_raw_output":          fp16_raw,
            "exact_output_match":       exact_match,
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
            "top_k_log":  top_k_log,
            "timestamp":  ts,
        })

    # ── Summary ───────────────────────────────────────────────────────────────
    cond_met = pass_count >= FEASIBILITY_N

    fp16_pass_count        = len(fp16_ref)   # 24/24 in reference
    retention              = pass_count / fp16_pass_count if fp16_pass_count > 0 else 0.0
    exact_output_agreement = exact_output_matches / len(results)

    class_counts: dict[str, int] = {}
    for r in results:
        cc = r["content_class"]
        class_counts[cc] = class_counts.get(cc, 0) + 1

    fp16_class_counts: dict[str, int] = {}
    for entry in fp16_ref.values():
        cc = entry["content_class"]
        fp16_class_counts[cc] = fp16_class_counts.get(cc, 0) + 1

    fp16_format_pass     = sum(1 for e in fp16_ref.values() if e["format_class"] == "FORMAT_PASS")
    stressed_format_pass = sum(1 for r in results if r["format_class"] == "FORMAT_PASS")
    strict_format_gap    = fp16_format_pass - stressed_format_pass
    content_gap          = fp16_pass_count - pass_count

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

    failure_records          = [r for r in results if not r["is_correct"]]
    failure_class_transition = []
    for r in failure_records:
        fp16_content = fp16_ref.get(r["id"], {}).get("content_class", "UNKNOWN")
        failure_class_transition.append({
            "id":                      r["id"],
            "fp16_class":              fp16_content,
            "stressed_class":          r["content_class"],
            "same_error_identity_key": r["same_error_identity_key"],
        })

    print(f"=== SUMMARY — 3B INT{bits} stress run ===")
    print(f"Pass count:               {pass_count}/{len(ITEMS)}  ({100*pass_count/len(ITEMS):.1f}%)")
    print(f"Gate:                     ≥{FEASIBILITY_N}/{len(ITEMS)} (87.5%)")
    print(f"Result:                   {'PASS' if cond_met else 'FAIL'}")
    print(f"Retention (vs FP16):      {pass_count}/{fp16_pass_count}  ({100*retention:.1f}%)")
    print(f"Exact-output agreement:   {exact_output_matches}/{len(results)}  ({100*exact_output_agreement:.1f}%)")
    print(f"Strict-format gap:        {strict_format_gap}  (FP16 FORMAT_PASS={fp16_format_pass}, stressed={stressed_format_pass})")
    print(f"Content gap (vs FP16):    {content_gap}")
    print(f"Numeric OOC count:        {numeric_ooc_count}")
    print()
    print(f"Content class breakdown (INT{bits}):")
    for cc, n in sorted(class_counts.items()):
        print(f"  {cc}: {n}")
    print()
    print(f"Content class breakdown (FP16 reference):")
    for cc, n in sorted(fp16_class_counts.items()):
        print(f"  {cc}: {n}")
    print()
    print(f"Position subgroup (diagnostic — does not modify gate):")
    for p in sorted(pos_breakdown.keys()):
        pb = pos_breakdown[p]
        print(f"  pos={p}: {pb['pass']}/{pb['pass']+pb['fail']} pass")
    print()
    if failure_class_transition:
        print(f"Failure-class transition (FP16 → INT{bits}):")
        for fc in failure_class_transition:
            print(f"  {fc['id']}: {fc['fp16_class']} → {fc['stressed_class']}")
            ik = fc["same_error_identity_key"]
            if ik:
                print(f"    same_error_identity_key: {ik}")
                print(f"    Note: comparison to prior L2 failure identities is diagnostic only")
                print(f"          and does not affect the stress interpretation.")
        print()
    print(f"Note: partial subgroup success does not license seam testing or mechanism claims.")

    # ── Write JSON ────────────────────────────────────────────────────────────
    out_path = Path(f"stress_constructibility_3b_int{bits}_{run_ts}.json")
    out_data = {
        "track":             "Synthetic Key-Value Selection Constructibility",
        "run_type":          f"3B INT{bits} stress run",
        "manifest_family":   "L3",
        "model_id":          MODEL_ID,
        "bits":              bits,
        "quant_dir":         str(quant_dir),
        "fp16_ref_path":     str(FP16_REF_PATH),
        "preflight":         preflight,
        "fresh_generation":  True,
        "decoding":          DECODING,
        "top_k_depth":       TOP_K_DEPTH,
        "top_k_note": (
            "Decision-token top-k logs are provenance and diagnostic artifacts only. "
            "Not used to make capability or mechanism claims."
        ),
        "authorization_note": (
            f"INT{bits} authorized by Manager 2026-06-07. "
            "INT8 and INT4 both authorized."
        ),
        "scope_note": (
            "Stress run on frozen L3 n=24 manifest. "
            "Same scoring contract as FP16 baseline. "
            "Not a seam, general retrieval, or mechanism result."
        ),
        "same_error_identity_note": (
            "Comparison to prior L2 failure identities is diagnostic only "
            "and does not affect the stress interpretation."
        ),
        "run_timestamp":              run_ts,
        "n_items":                    len(ITEMS),
        "pass_count":                 pass_count,
        "pass_rate":                  pass_count / len(ITEMS),
        "feasibility_n":              FEASIBILITY_N,
        "feasible":                   cond_met,
        "fp16_pass_count":            fp16_pass_count,
        "retention":                  retention,
        "exact_output_agreement":     exact_output_agreement,
        "exact_output_matches":       exact_output_matches,
        "strict_format_gap":          strict_format_gap,
        "content_gap":                content_gap,
        "numeric_ooc_count":          numeric_ooc_count,
        "content_class_breakdown":    class_counts,
        "fp16_class_breakdown":       fp16_class_counts,
        "failure_class_transition":   failure_class_transition,
        "position_subgroup":          pos_breakdown,
        "results":                    results,
    }
    out_path.write_text(json.dumps(out_data, indent=2))
    print(f"\nWrote: {out_path}")


if __name__ == "__main__":
    main()
