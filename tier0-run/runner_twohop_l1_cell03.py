"""
Stage 1 runner — Two-Hop Level 1 Cell 03
FP16 constructibility run, Qwen2.5-3B-Instruct

Authorization: Manager / Team Lead memo
  "Authorized — Execute One Cell03 FP16 Run Only" 2026-06-08

Amendment from runner_twohop_l1_cell02.py:
  ITEMS_PATH:          items_twohop_l1_cell03.json
  EXPECTED_SCORER_HASH: sha256:b65c6803... (amended scorer, Manager-authorized 2026-06-08)
  AXIS_CONFIGURATION:  adjacency/proximity (broken all 24 items, gap=2);
                       ct C-rank balanced 8+8+8; ct position balanced pos 3/5/7
  output filename:     RESULTS-TWOHOP-L1-cell03-{ts}.json
  §8 diagnostics:      added per-result endpoint-intrusion diagnostic fields
                       (mandatory per Team Lead standing requirement)
  API amendment:       mlx_lm sampler API update — temp kwarg removed; use
                       make_sampler(temp=0.0) for greedy decoding; stream_generate
                       yields GenerationResponse objects (use .text field).

All other constants frozen from Cell02 runner:
  EXPECTED_VALIDATOR_HASH, EXPECTED_TOKENIZER_HASH, MODEL_ID,
  DECODING_SETTINGS, FROZEN_SETTINGS, QUERY_TEXT, all rendering logic.

One-axis constraint: only ITEMS_PATH, EXPECTED_SCORER_HASH, AXIS_CONFIGURATION,
output filename, §8 diagnostic computation, and mlx_lm API compatibility changed.

No model inference is performed in dry-run mode.
"""

import argparse
import hashlib
import json
import sys
import time
from pathlib import Path
from typing import Optional

# ── Provenance ────────────────────────────────────────────────────────────────
RUNNER_PATH          = Path(__file__)
ITEMS_PATH           = Path("items_twohop_l1_cell03.json")
PROMPT_TEMPLATE_PATH = Path("prompt_template_twohop_l1.txt")
VALIDATOR_PATH       = Path("tasks_twohop_l1.py")
SCORER_PATH          = Path("scorer_twohop_l1.py")

EXPECTED_VALIDATOR_HASH = (
    "sha256:bcc26ca04b0c5a21db496d08c9307d2e6257315a9376f04473ea68ae36ca349b"
)
EXPECTED_SCORER_HASH = (
    "sha256:b65c6803017b8b04ac25d4bd84c5fb5ff61692ed41d609e099b181fa58e4ddde"
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
    "Primary axis: adjacency/proximity. "
    "Neighbor fact (fl holds cn) interposed between target hop1 and hop2 in ALL 24 items. "
    "hop1-hop2 gap = 2 (adjacency broken). "
    "ct C-rank balanced: 8 first_C (Group A, ct pos 3) / "
    "8 second_C (Group B, ct pos 5) / 8 third_C-last_C (Group C, ct pos 7). "
    "ct absolute-position balanced: 8 at pos 3 / 8 at pos 5 / 8 at pos 7. "
    "Token identities new (RNG seed 20260615); all other variables frozen from Cell02."
)
FROZEN_SETTINGS = (
    "relation_hop1='links to'; relation_hop2='maps to'; relation_hold='holds'; "
    "context_length=7 facts; chains_per_item=3 (target + decoy_1 + decoy_2); "
    "query_phrasing=template; "
    "instruction_prefix=prompt_template_twohop_l1.txt"
)

QUERY_TYPES = ["hop1", "hop2", "composite", "negative_graph"]

GATE5_REFERENCE_ONLY = {"always_return_ct", "always_return_NULL"}


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
    anchor      = item["queries"][query_type]["query_anchor"]
    facts       = get_facts_for_query(item, query_type)
    context_str = render_context(facts)
    query_str   = QUERY_TEXT[query_type].format(anchor=anchor)
    return template.replace("{CONTEXT}", context_str).replace("{QUERY}", query_str)


# ── §8 Endpoint-intrusion diagnostics ────────────────────────────────────────
def _build_token_pos_map(item: dict,
                         role_neighbor: str = "target_neighbor_decoy",
                         role_filler:   str = "inert_filler") -> dict:
    """
    Map every token in the item context to its earliest position_index.
    Uses chain A/B/C objects for chain facts; object_roles for neighbor/filler.
    Disambiguation rule: earliest position_index when a token appears in
    multiple facts (defensive; not expected in Cell03 construction).
    """
    chain_map    = {c["chain_id"]: c for c in item.get("chains", [])}
    obj_roles    = item.get("object_roles", {})
    neighbor_tok = next((t for t, r in obj_roles.items() if r == role_neighbor), None)
    filler_tok   = next((t for t, r in obj_roles.items() if r == role_filler),   None)

    token_pos: dict = {}

    def _reg(tok, pos):
        if tok is not None and (tok not in token_pos or pos < token_pos[tok]):
            token_pos[tok] = pos

    for fact in item["context"]["ordered_facts"]:
        pos = fact["position_index"]
        cid = fact.get("chain_id", "")
        fr  = fact.get("fact_role", "")
        ch  = chain_map.get(cid, {})

        if fr in ("hop1_fact", "decoy_hop1_fact"):
            _reg(ch.get("A_object"), pos)
            _reg(ch.get("B_object"), pos)
        elif fr in ("hop2_fact", "decoy_hop2_fact"):
            _reg(ch.get("B_object"), pos)
            _reg(ch.get("C_object"), pos)
        elif fr == "neighbor_decoy_fact":
            _reg(filler_tok,   pos)
            _reg(neighbor_tok, pos)

    return token_pos


def _find_target_chain_fact_pos(item: dict, fact_role_key: str) -> Optional[int]:
    """Return position_index of the target_chain fact with the given fact_role."""
    for f in item["context"]["ordered_facts"]:
        if f.get("chain_id") == "target_chain" and f.get("fact_role") == fact_role_key:
            return f["position_index"]
    return None


def compute_s8_diagnostics(item: dict, query_type: str,
                            scored: dict,
                            c_by_pos_fn) -> dict:
    """
    Compute §8 endpoint-intrusion diagnostic fields for one item/query result.

    Returns a dict with all mandatory §8 fields.
    Fields with value None or "N/A" indicate non-applicable or non-endpoint cases.

    Required output fields (per Team Lead standing requirement):
      query_type, expected_answer, returned_token, returned_role,
      ct_vs_other_C, b_vs_c_endpoint,
      returned_abs_position, returned_c_rank,
      returned_hop1_proximity, returned_hop2_proximity,
      neg_graph_endpoint_intrusion
    """
    returned_token = scored.get("returned_token")
    returned_role  = scored.get("returned_role")
    expected       = item["queries"][query_type]["expected_answer"]

    # Identify ct, cd1, cd2 by chain role
    ct  = next((c["C_object"] for c in item.get("chains", []) if c.get("role") == "target"), None)
    cds = [c["C_object"] for c in item.get("chains", []) if c.get("role") == "decoy"]

    # ── ct vs other-C endpoint ────────────────────────────────────────────────
    if returned_token is None:
        ct_vs_other_C = "N/A"
    elif returned_token == ct:
        ct_vs_other_C = "ct"
    elif returned_token in cds:
        ct_vs_other_C = "other_C"
    else:
        ct_vs_other_C = "not_C"

    # ── B endpoint vs C endpoint ──────────────────────────────────────────────
    if returned_token is None:
        b_vs_c = "N/A"
    elif returned_role == "hop1_B":
        b_vs_c = "B_endpoint"
    elif returned_role == "answer_C":
        b_vs_c = "C_target_endpoint"
    elif returned_role == "distractor_chain_endpoint":
        b_vs_c = "C_decoy_endpoint"
    else:
        b_vs_c = "other"

    # ── Is this an endpoint return? ───────────────────────────────────────────
    is_endpoint = returned_role in ("hop1_B", "answer_C", "distractor_chain_endpoint")

    # ── Absolute position ─────────────────────────────────────────────────────
    if returned_token is None or not is_endpoint:
        ret_abs_pos = "N/A"
    else:
        tok_pos = _build_token_pos_map(item)
        ret_abs_pos = tok_pos.get(returned_token, "N/A")

    # ── C-rank ────────────────────────────────────────────────────────────────
    if returned_token is None or not is_endpoint:
        ret_c_rank = "N/A"
    else:
        c_by_pos = c_by_pos_fn(item)
        if returned_token in c_by_pos:
            ret_c_rank = c_by_pos.index(returned_token) + 1  # 1-based
        else:
            ret_c_rank = "N/A"

    # ── Adjacency / proximity ─────────────────────────────────────────────────
    if not is_endpoint or ret_abs_pos == "N/A":
        ret_hop1_prox = "N/A"
        ret_hop2_prox = "N/A"
    else:
        hop1_pos = _find_target_chain_fact_pos(item, "hop1_fact")
        hop2_pos = _find_target_chain_fact_pos(item, "hop2_fact")
        ret_hop1_prox = abs(ret_abs_pos - hop1_pos) if hop1_pos is not None else "N/A"
        ret_hop2_prox = abs(ret_abs_pos - hop2_pos) if hop2_pos is not None else "N/A"

    # ── negative_graph endpoint intrusion ─────────────────────────────────────
    if query_type == "negative_graph":
        neg_intrusion = (returned_token is not None
                         and returned_token not in ("NULL", "null", "Null"))
    else:
        neg_intrusion = "N/A"

    return {
        "query_type":                query_type,
        "expected_answer":           expected,
        "returned_token":            returned_token,
        "returned_role":             returned_role,
        "ct_vs_other_C":             ct_vs_other_C,
        "b_vs_c_endpoint":           b_vs_c,
        "returned_abs_position":     ret_abs_pos,
        "returned_c_rank":           ret_c_rank,
        "returned_hop1_proximity":   ret_hop1_prox,
        "returned_hop2_proximity":   ret_hop2_prox,
        "neg_graph_endpoint_intrusion": neg_intrusion,
    }


# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(description="Stage 1 runner — Two-Hop L1 Cell03")
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
        _c_objects_by_context_position,
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
        print("\nSample §8 diagnostic (item[0], composite, dry-run):")
        sample_scored = {
            "returned_token": None, "returned_role": None,
            "failure_class": "dry_run", "scaffold_class": "dry_run",
            "format_class": "dry_run", "is_correct": False,
        }
        s8 = compute_s8_diagnostics(items[0], "composite", sample_scored,
                                    _c_objects_by_context_position)
        for k, v in s8.items():
            print(f"    {k}: {v}")
        print("No model inference performed.")
        print(f"runner_hash: {runner_hash}")
        return

    # ── Step 4: Load model ─────────────────────────────────────────────────────
    print("\nStep 4: Loading FP16 model...")
    from mlx_lm import load, stream_generate
    from mlx_lm.sample_utils import make_sampler
    model, tokenizer = load(MODEL_ID)
    print(f"  Model loaded: {MODEL_ID}")
    sampler = make_sampler(temp=DECODING_SETTINGS["temperature"])

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
            prompt              = render_prompt(item, qt, template)
            prompt_hash_rendered = sha256_string(prompt)

            chat_prompt = prompt
            if getattr(tokenizer, "chat_template", None) is not None:
                chat_prompt = tokenizer.apply_chat_template(
                    [{"role": "user", "content": prompt}],
                    add_generation_prompt=True, tokenize=False,
                )
            raw_output = ""
            for _resp in stream_generate(
                model, tokenizer,
                prompt=chat_prompt,
                max_tokens=DECODING_SETTINGS["max_tokens"],
                sampler=sampler,
            ):
                raw_output += _resp.text
            raw_output = raw_output.strip()

            scored = classify_output(raw_output, item, qt)
            dummy  = compute_dummy_baseline_scores(item, qt)
            s8     = compute_s8_diagnostics(item, qt, scored,
                                             _c_objects_by_context_position)

            all_results.append({
                "item_id":               item_id,
                "query_type":            qt,
                "prompt_rendered_hash":  prompt_hash_rendered,
                "raw_output":            raw_output,
                "failure_class":         scored["failure_class"],
                "scaffold_class":        scored["scaffold_class"],
                "format_class":          scored["format_class"],
                "returned_token":        scored["returned_token"],
                "returned_role":         scored["returned_role"],
                "is_correct":            scored["is_correct"],
                "dummy_baselines":       dummy,
                "s8_diagnostics":        s8,
            })
            status = "✓" if scored["is_correct"] else "✗"
            print(f"  {item_id}/{qt}: {status} {scored['failure_class']}"
                  f" (returned: {scored['returned_token']})")

    # ── Step 7: Write output artifacts ────────────────────────────────────────
    print("\nStep 7: Writing output artifacts...")
    ts       = int(time.time())
    output   = {"provenance": provenance, "results": all_results}
    out_path = out_dir / f"RESULTS-TWOHOP-L1-cell03-{ts}.json"
    out_path.write_text(json.dumps(output, indent=2))
    output_hash = sha256_file(out_path)
    print(f"  Results written: {out_path}")
    print(f"  output_hash: {output_hash}")
    print(f"  runner_hash: {runner_hash}")

    # ── Step 8: Quick score summary ────────────────────────────────────────────
    print("\nStep 8: Score summary...")
    for qt in QUERY_TYPES:
        qt_results = [r for r in all_results if r["query_type"] == qt]
        fp   = [r for r in qt_results if r["format_class"] == "FORMAT_PASS"]
        corr = [r for r in fp if r["is_correct"]]
        fsf  = [r for r in qt_results if r["failure_class"] == "format_scaffold_failure"]
        print(f"  {qt}: {len(corr)}/{len(fp)} FORMAT_PASS correct"
              f"  ({len(fsf)} FSF)")

    # §8 endpoint-intrusion summary (hop1 and negative_graph)
    print("\n§8 endpoint-intrusion summary:")
    hop1_fp = [r for r in all_results
               if r["query_type"] == "hop1" and r["format_class"] == "FORMAT_PASS"]
    hop1_ct_anchored = [r for r in hop1_fp
                        if r["s8_diagnostics"]["ct_vs_other_C"] == "ct"]
    print(f"  hop1 FORMAT_PASS:        {len(hop1_fp)}/24")
    print(f"  hop1 returned ct (ct-anchoring): {len(hop1_ct_anchored)}/{len(hop1_fp)}")

    neg_fp = [r for r in all_results
              if r["query_type"] == "negative_graph" and r["format_class"] == "FORMAT_PASS"]
    neg_intruded = [r for r in neg_fp
                    if r["s8_diagnostics"]["neg_graph_endpoint_intrusion"] is True]
    print(f"  neg_graph FORMAT_PASS:   {len(neg_fp)}/24")
    print(f"  neg_graph endpoint intrusion: {len(neg_intruded)}/{len(neg_fp)}")

    print("\nAuthorization boundary:")
    print("  One FP16 run only. No rerun, INT8, INT4, or stress-eligibility declaration authorized.")
    print("  §8 diagnostics are mandatory non-blocking diagnostic output.")
    print("  Gate 3 endpoint-intrusion threshold amendment required before any future")
    print("  stress-eligibility declaration (Option B guardrail, Team Lead 2026-06-08).")


if __name__ == "__main__":
    main()
