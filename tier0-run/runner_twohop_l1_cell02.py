"""
Stage 1 runner — Two-Hop Level 1 Cell 02
FP16 constructibility run, Qwen2.5-3B-Instruct

Authorization: requires explicit Manager authorization before execution.
This script is a locked preparation artifact. Do not execute without authorization.

Amendment from runner_twohop_l1.py (Cell01):
  ITEMS_PATH:        items_twohop_l1_cell02.json  (was: items_twohop_l1_cell01.json)
  AXIS_CONFIGURATION: all-C_target-last, T-hop2 at position 6, all 24 items
                      (was: 8+8+8 mixed ordering)
  output filename:   RESULTS-TWOHOP-L1-cell02-{ts}.json
  All other constants frozen from Cell01 runner.

One-axis constraint confirmation:
  Only ITEMS_PATH and AXIS_CONFIGURATION changed.
  EXPECTED_VALIDATOR_HASH, EXPECTED_SCORER_HASH, EXPECTED_TOKENIZER_HASH,
  MODEL_ID, DECODING_SETTINGS, FROZEN_SETTINGS, QUERY_TEXT, all rendering
  logic, and all other provenance constants are identical to runner_twohop_l1.py.

Provenance hashes recorded at startup before any model call.
"""

import argparse
import hashlib
import json
import sys
import time
from pathlib import Path

# ── Provenance ────────────────────────────────────────────────────────────────
RUNNER_PATH          = Path(__file__)
ITEMS_PATH           = Path("items_twohop_l1_cell02.json")
PROMPT_TEMPLATE_PATH = Path("prompt_template_twohop_l1.txt")
VALIDATOR_PATH       = Path("tasks_twohop_l1.py")
SCORER_PATH          = Path("scorer_twohop_l1.py")

EXPECTED_VALIDATOR_HASH = (
    "sha256:bcc26ca04b0c5a21db496d08c9307d2e6257315a9376f04473ea68ae36ca349b"
)
EXPECTED_SCORER_HASH = (
    "sha256:060afad9db6fc56dc222d8dc1e856fa28fd379811269d899317dbd660c4a91bd"
)
EXPECTED_TOKENIZER_HASH = (
    "sha256:c0382117ea329cdf097041132f6d735924b697924d6f6fc3945713e96ce87539"
)
# Note: local int4/int8 tokenizer.json hash is 3fd169731... — same vocabulary and
# normalized merges; file-format difference only (list vs string merge representation).
# Confirmed identical by normalized merge comparison 2026-06-08.

FAILURE_TAXONOMY_VERSION = "v1.0"
MODEL_ID = "Qwen/Qwen2.5-3B-Instruct"
DECODING_SETTINGS = {"temperature": 0.0, "max_tokens": 16}
AXIS_CONFIGURATION = (
    "Single axis: position / ordering only. "
    "All 24 items C_target-last: T-hop2 at context position 6. "
    "decoy_chain_2 hop2 at position 7 (Gate 5 forced). "
    "Token identities new (RNG seed 20260610); all other variables frozen from Cell01."
)
FROZEN_SETTINGS = (
    "relation_hop1='links to'; relation_hop2='maps to'; relation_hold='holds'; "
    "context_length=7 facts; chains_per_item=3 (target + decoy_1 + decoy_2); "
    "query_phrasing=template; "
    "instruction_prefix=prompt_template_twohop_l1.txt"
)

QUERY_TYPES = ["hop1", "hop2", "composite", "negative_graph"]


def sha256_file(path: Path) -> str:
    return "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()


def sha256_string(s: str) -> str:
    return "sha256:" + hashlib.sha256(s.encode("utf-8")).hexdigest()


# ── Prompt rendering ──────────────────────────────────────────────────────────
QUERY_TEXT = {
    "hop1":           "{anchor} links to what?",
    "hop2":           "{anchor} maps to what?",
    "composite":      "{anchor} links to something, which maps to what?",
    "negative_graph": "{anchor} links to something, which maps to what?",
}


def render_context(facts: list) -> str:
    return "\n".join(f["text"] for f in sorted(facts, key=lambda x: x["position_index"]))


def get_facts_for_query(item: dict, query_type: str) -> list:
    facts = item["context"]["ordered_facts"]
    if query_type == "negative_graph":
        facts = [f for f in facts
                 if not (f["chain_id"] == "target_chain"
                         and f["fact_role"] == "hop2_fact")]
    return facts


def render_prompt(item: dict, query_type: str, template: str) -> str:
    anchor = item["queries"][query_type]["query_anchor"]
    facts  = get_facts_for_query(item, query_type)
    context_str = render_context(facts)
    query_str   = QUERY_TEXT[query_type].format(anchor=anchor)
    return template.replace("{CONTEXT}", context_str).replace("{QUERY}", query_str)


# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(description="Stage 1 runner — Two-Hop L1 Cell02")
    parser.add_argument("--dry-run", action="store_true",
                        help="Verify provenance and validate manifest; skip model inference")
    parser.add_argument("--output-dir", default=".", help="Directory for output artifacts")
    args = parser.parse_args()

    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    # ── Step 1: Provenance hashes (before any model call) ─────────────────────
    print("Step 1: Recording provenance hashes...")
    runner_hash    = sha256_file(RUNNER_PATH)
    manifest_hash  = sha256_file(ITEMS_PATH)
    validator_hash = sha256_file(VALIDATOR_PATH)
    scorer_hash    = sha256_file(SCORER_PATH)
    prompt_hash    = sha256_file(PROMPT_TEMPLATE_PATH)

    print(f"  runner_hash:           {runner_hash}")
    print(f"  manifest_hash:         {manifest_hash}")
    print(f"  validator_hash:        {validator_hash}")
    print(f"  scorer_hash:           {scorer_hash}")
    print(f"  prompt_template_hash:  {prompt_hash}")

    if validator_hash != EXPECTED_VALIDATOR_HASH:
        print(f"FATAL: validator hash mismatch.\n"
              f"  expected: {EXPECTED_VALIDATOR_HASH}\n"
              f"  actual:   {validator_hash}")
        sys.exit(1)
    if scorer_hash != EXPECTED_SCORER_HASH:
        print(f"FATAL: scorer hash mismatch.\n"
              f"  expected: {EXPECTED_SCORER_HASH}\n"
              f"  actual:   {scorer_hash}")
        sys.exit(1)
    print("  validator_hash: OK")
    print("  scorer_hash: OK")

    # ── Step 2: Load and validate manifest ────────────────────────────────────
    sys.path.insert(0, str(Path(__file__).parent))
    from tasks_twohop_l1 import validate_manifest
    from scorer_twohop_l1 import (
        classify_output, compute_dummy_baseline_scores, get_scorer_hash,
    )

    print("\nStep 2: Loading and validating manifest...")
    items = json.loads(ITEMS_PATH.read_text())
    result = validate_manifest(items)
    print(f"  validate_manifest(): {result['pass_count']}/{result['total']} pass")
    if not result["all_pass"]:
        print("FATAL: manifest validation failed.")
        for iid, errs in result["errors"].items():
            for e in errs:
                print(f"  [{iid}] {e}")
        sys.exit(1)

    # ── Step 3: FP16 tokenizer hash confirmation ───────────────────────────────
    print("\nStep 3: Confirming FP16 tokenizer hash...")
    try:
        from mlx_lm import load
        _model, tokenizer = load(MODEL_ID)
        import os
        hf_cache = Path(os.environ.get("HF_HOME",
                        Path.home() / ".cache" / "huggingface" / "hub"))
        tok_file = None
        for candidate in hf_cache.rglob("tokenizer.json"):
            if "Qwen2.5-3B-Instruct" in str(candidate) and "mlx" not in str(candidate):
                tok_file = candidate
                break
        if tok_file is None:
            name_or_path = Path(getattr(tokenizer, "name_or_path", ""))
            tok_file = name_or_path / "tokenizer.json"
        if not tok_file.exists():
            print(f"FATAL: cannot locate tokenizer.json for {MODEL_ID}")
            sys.exit(1)
        tokenizer_hash_actual = sha256_file(tok_file)
        print(f"  tokenizer.json path: {tok_file}")
        print(f"  tokenizer_hash: {tokenizer_hash_actual}")
        if tokenizer_hash_actual != EXPECTED_TOKENIZER_HASH:
            print(f"FATAL: tokenizer hash mismatch.\n"
                  f"  expected: {EXPECTED_TOKENIZER_HASH}\n"
                  f"  actual:   {tokenizer_hash_actual}\n"
                  f"Halt and escalate to Team Lead.")
            sys.exit(1)
        print("  tokenizer_hash: OK")
        tokenizer_hash = tokenizer_hash_actual
    except ImportError:
        print("  mlx_lm not available in this environment.")
        if args.dry_run:
            print("  dry-run: skipping tokenizer load.")
            tokenizer_hash = EXPECTED_TOKENIZER_HASH + " [unconfirmed — dry-run]"
            tokenizer = None
        else:
            print("FATAL: mlx_lm required for live run.")
            sys.exit(1)

    if args.dry_run:
        template_dr = PROMPT_TEMPLATE_PATH.read_text()
        print("\nDry-run mode: provenance and manifest checks complete.")
        print("Rendering sample prompts (item[0], 4 query types) — chat-template format check:")
        sample_item = items[0]
        for qt in QUERY_TYPES:
            raw_text = render_prompt(sample_item, qt, template_dr)
            if tokenizer is not None and getattr(tokenizer, "chat_template", None) is not None:
                chat_text = tokenizer.apply_chat_template(
                    [{"role": "user", "content": raw_text}],
                    add_generation_prompt=True, tokenize=False,
                )
                print(f"  [{qt}] chat_template: OK  raw={len(raw_text)}chars  formatted={len(chat_text)}chars")
            else:
                print(f"  [{qt}] no chat_template  raw={len(raw_text)}chars")
        print("No model inference performed.")
        print(f"runner_hash: {runner_hash}")
        return

    # ── Step 4: Load model ─────────────────────────────────────────────────────
    print("\nStep 4: Loading FP16 model...")
    from mlx_lm import load, stream_generate
    model, tokenizer = load(MODEL_ID)
    print(f"  Model loaded: {MODEL_ID}")

    # ── Step 5: Load prompt template ───────────────────────────────────────────
    template = PROMPT_TEMPLATE_PATH.read_text()

    # ── Step 6: Run inference ──────────────────────────────────────────────────
    print("\nStep 6: Running inference...")
    provenance = {
        "manifest_hash":            manifest_hash,
        "scorer_hash":              scorer_hash,
        "validator_hash":           validator_hash,
        "runner_hash":              runner_hash,
        "tokenizer_hash":           tokenizer_hash,
        "prompt_template_hash":     prompt_hash,
        "failure_taxonomy_version": FAILURE_TAXONOMY_VERSION,
        "model_id":                 MODEL_ID,
        "decoding_settings":        DECODING_SETTINGS,
        "axis_configuration":       AXIS_CONFIGURATION,
        "frozen_settings":          FROZEN_SETTINGS,
        "run_timestamp":            int(time.time()),
    }

    all_results = []
    for item in items:
        item_id = item["item_id"]
        for qt in QUERY_TYPES:
            prompt = render_prompt(item, qt, template)
            prompt_hash_rendered = sha256_string(prompt)

            chat_prompt = prompt
            if getattr(tokenizer, "chat_template", None) is not None:
                chat_prompt = tokenizer.apply_chat_template(
                    [{"role": "user", "content": prompt}],
                    add_generation_prompt=True, tokenize=False,
                )
            raw_output = ""
            for _seg in stream_generate(
                model, tokenizer,
                prompt=chat_prompt,
                max_tokens=DECODING_SETTINGS["max_tokens"],
                temp=DECODING_SETTINGS["temperature"],
            ):
                raw_output += _seg
            raw_output = raw_output.strip()

            scored = classify_output(raw_output, item, qt)
            dummy  = compute_dummy_baseline_scores(item, qt)

            all_results.append({
                "item_id":              item_id,
                "query_type":           qt,
                "prompt_rendered_hash": prompt_hash_rendered,
                "raw_output":           raw_output,
                "failure_class":        scored["failure_class"],
                "scaffold_class":       scored["scaffold_class"],
                "format_class":         scored["format_class"],
                "returned_token":       scored["returned_token"],
                "returned_role":        scored["returned_role"],
                "is_correct":           scored["is_correct"],
                "dummy_baselines":      dummy,
            })
            status = "✓" if scored["is_correct"] else "✗"
            print(f"  {item_id}/{qt}: {status} {scored['failure_class']}"
                  f" (returned: {scored['returned_token']})")

    # ── Step 7: Write output artifacts ────────────────────────────────────────
    print("\nStep 7: Writing output artifacts...")
    output = {"provenance": provenance, "results": all_results}
    ts = int(time.time())
    out_path = out_dir / f"RESULTS-TWOHOP-L1-cell02-{ts}.json"
    out_path.write_text(json.dumps(output, indent=2))
    print(f"  Results written: {out_path}")
    print(f"  runner_hash: {runner_hash}")


if __name__ == "__main__":
    main()
