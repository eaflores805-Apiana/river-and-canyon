#!/usr/bin/env python3
"""
tasks_exp8b.py — Exp8B: single-variable query wording test on Exp8A items.

Single-variable change from Exp8A:
  Exp8A query: "Which value is associated with SUBJ_T?"
  Exp8B query: "Which token is assigned to SUBJ_T?"

Exact item reuse from tasks_exp8.py:
  same subjects, objects, fact order, target positions,
  relation ("maps to"), item geometry.

All scoring functions (score_arm2_content, score_arm2_scaffold,
score_arm2_format) are imported unchanged from tasks_exp8.py.

Pass condition (Team Lead spec):
  1. FP16 Arm 2 content pass count ≥7/8
  2. Zero numeric out-of-context returns (ANSWER: 0, ANSWER: 10, etc.)

Scope limits:
  No n≥20 expansion. No INT8/INT4. No seam claim. No Exp8C.

Run static validation:
  python3 tasks_exp8b.py
"""

import hashlib
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

# ─── Import from Exp8A (scoring functions, constants, Exp8A items) ────────
from tasks_exp8 import (
    ITEMS          as EXP8A_ITEMS,
    _SCAFFOLD,
    _DECODING,
    _DECODING_DETERMINISM_ASSERTED,
    _CONTENT_CLASSES,
    _FORMAT_CLASSES,
    _FEASIBILITY_THRESHOLD,
    _COMMON_5_LETTER_WORDS,
    EXP7_TOKENS,
    score_arm2_content,
    score_arm2_scaffold,
    score_arm2_format,
    _compute_dummy_baselines,
)

# ─── Query wording (single variable) ─────────────────────────────────────
EXP8A_QUERY_PREFIX = "Which value is associated with "   # must NOT appear in 8B prompts
EXP8B_QUERY_PREFIX = "Which token is assigned to "       # must appear in all 8B prompts


# ─── Prompt builder (only wording change) ────────────────────────────────

def _make_arm2b_prompt(facts: list, target_subj: str) -> str:
    context = "\n".join(f"{s} maps to {o}." for s, o in facts)
    return (
        f"{context}\n\n"
        f"{EXP8B_QUERY_PREFIX}{target_subj}? {_SCAFFOLD}"
    )


def _make_item(item_id: str, facts: list, target_pos: int) -> dict:
    target_subj, target_obj = facts[target_pos - 1]
    prompt = _make_arm2b_prompt(facts, target_subj)
    return {
        "id":                             item_id,
        "arm":                            "2B",
        "family":                         "L",
        "target_pos":                     target_pos,
        "facts":                          facts,
        "target_subj":                    target_subj,
        "target_obj":                     target_obj,
        "prompt":                         prompt,
        "prompt_hash":                    f"sha256:{hashlib.sha256(prompt.encode()).hexdigest()}",
        "answer":                         f"ANSWER: {target_obj}",
        "score_type":                     "exact",
        "decoding":                       _DECODING,
        "decoding_determinism_asserted":  _DECODING_DETERMINISM_ASSERTED,
        "exp8a_item_reuse":               True,    # explicit reuse flag
    }


# ─── Build Exp8B items from Exp8A facts (exact reuse at source) ───────────
# facts and target_pos are taken directly from EXP8A_ITEMS.
# Only the prompt (and derived prompt_hash) changes.
ITEMS = [
    _make_item(a["id"], a["facts"], a["target_pos"])
    for a in EXP8A_ITEMS
]


# ─── Manifest hash ────────────────────────────────────────────────────────

def get_manifest_hash() -> str:
    return f"sha256:{hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}"


# ─── Static validator ─────────────────────────────────────────────────────

def validate_tasks() -> bool:
    """
    Full static validation for Exp8B items.

    Runs structural checks equivalent to tasks_exp8.py checks 01–26,
    plus Exp8B-specific checks (B01–B06) for exact item reuse and
    single-variable wording change.

    Returns True if all checks pass, False otherwise.
    """
    all_subjects = [s for item in ITEMS for s, _ in item["facts"]]
    all_objects  = [o for item in ITEMS for _, o in item["facts"]]
    all_tokens   = all_subjects + all_objects
    subj_set     = set(all_subjects)
    obj_set      = set(all_objects)

    errors: list = []
    per_item: dict[str, list] = {}

    def _err(check_id: str, msg: str, item_id: str | None = None):
        errors.append((check_id, item_id, msg))
        if item_id:
            per_item.setdefault(item_id, []).append((check_id, "FAIL", msg))

    def _ok(check_id: str, item_id: str, detail: str = ""):
        per_item.setdefault(item_id, []).append((check_id, "PASS", detail))

    # ── Global structural checks (mirror of tasks_exp8.py CHECK_01–10) ──────

    # CHECK_01: n == 8
    if len(ITEMS) != 8:
        _err("CHECK_01", f"Expected 8 items, got {len(ITEMS)}")
    else:
        for item in ITEMS:
            _ok("CHECK_01", item["id"], "n=8")

    # CHECK_02: target_pos distribution = {2:3, 3:3, 4:2}
    pos_counts: dict[int, int] = {}
    for item in ITEMS:
        pos_counts[item["target_pos"]] = pos_counts.get(item["target_pos"], 0) + 1
    expected_dist = {2: 3, 3: 3, 4: 2}
    if pos_counts != expected_dist:
        _err("CHECK_02", f"Distribution {pos_counts} ≠ expected {expected_dist}")
    else:
        for item in ITEMS:
            _ok("CHECK_02", item["id"], f"target_pos={item['target_pos']}")

    # CHECK_03: target_pos ∈ {2,3,4} for every item
    for item in ITEMS:
        if item["target_pos"] not in {2, 3, 4}:
            _err("CHECK_03", f"target_pos={item['target_pos']} ∉ {{2,3,4}}", item["id"])
        else:
            _ok("CHECK_03", item["id"], f"target_pos={item['target_pos']}")

    # CHECK_04: every item has exactly 5 facts
    for item in ITEMS:
        if len(item["facts"]) != 5:
            _err("CHECK_04", f"Expected 5 facts, got {len(item['facts'])}", item["id"])
        else:
            _ok("CHECK_04", item["id"], "5 facts")

    # CHECK_05: all subjects unique across items
    if len(all_subjects) != len(set(all_subjects)):
        dupes = {s for s in all_subjects if all_subjects.count(s) > 1}
        _err("CHECK_05", f"Duplicate subjects: {dupes}")
    else:
        for item in ITEMS:
            _ok("CHECK_05", item["id"], "subjects unique")

    # CHECK_06: all objects unique across items
    if len(all_objects) != len(set(all_objects)):
        dupes = {o for o in all_objects if all_objects.count(o) > 1}
        _err("CHECK_06", f"Duplicate objects: {dupes}")
    else:
        for item in ITEMS:
            _ok("CHECK_06", item["id"], "objects unique")

    # CHECK_07: subjects and objects fully disjoint
    overlap = subj_set & obj_set
    if overlap:
        _err("CHECK_07", f"Subject/object overlap: {overlap}")
    else:
        for item in ITEMS:
            _ok("CHECK_07", item["id"], "no chain overlap")

    # CHECK_08: no token appears in EXP7_TOKENS
    exp7_hits = set(all_tokens) & EXP7_TOKENS
    if exp7_hits:
        _err("CHECK_08", f"Exp7 token reuse: {exp7_hits}")
    else:
        for item in ITEMS:
            _ok("CHECK_08", item["id"], "no Exp7 overlap")

    # CHECK_09: all tokens are exactly 5 uppercase letters
    bad_tokens = [t for t in all_tokens if not re.match(r'^[A-Z]{5}$', t)]
    if bad_tokens:
        _err("CHECK_09", f"Tokens failing 5-char uppercase check: {bad_tokens}")
    else:
        for item in ITEMS:
            _ok("CHECK_09", item["id"], "all 5-char uppercase")

    # CHECK_10: global token uniqueness
    if len(all_tokens) != len(set(all_tokens)):
        dupes = {t for t in all_tokens if all_tokens.count(t) > 1}
        _err("CHECK_10", f"Combined pool duplicates: {dupes}")
    else:
        for item in ITEMS:
            _ok("CHECK_10", item["id"], "global uniqueness ok")

    # ── Per-item structural checks (mirror of CHECK_11–20) ──────────────────

    for item in ITEMS:
        pid   = item["id"]
        facts = item["facts"]
        tp    = item["target_pos"]
        t_subj, t_obj = facts[tp - 1]

        # CHECK_11: target_subj / target_obj correctly derived from target_pos
        if item["target_subj"] != t_subj or item["target_obj"] != t_obj:
            _err("CHECK_11",
                 f"target mismatch: item has ({item['target_subj']},{item['target_obj']}) "
                 f"but fact {tp} is ({t_subj},{t_obj})", pid)
        else:
            _ok("CHECK_11", pid, f"target={t_subj}→{t_obj} at pos {tp}")

        # CHECK_12: query part contains no "maps", " map ", "mapped"
        query_part = item["prompt"].split("\n\n", 1)[-1] if "\n\n" in item["prompt"] else ""
        q_lower = query_part.lower()
        if "maps" in q_lower or " map " in q_lower or "mapped" in q_lower:
            _err("CHECK_12", f"Query contains forbidden mapping word: {query_part[:80]!r}", pid)
        else:
            _ok("CHECK_12", pid, "query maps-free")

        # CHECK_13: standard scaffold present in prompt
        if _SCAFFOLD not in item["prompt"]:
            _err("CHECK_13", "Standard scaffold missing", pid)
        else:
            _ok("CHECK_13", pid, "scaffold present")

        # CHECK_14: answer field matches "ANSWER: {target_obj}"
        expected_ans = f"ANSWER: {t_obj}"
        if item["answer"] != expected_ans:
            _err("CHECK_14", f"answer={item['answer']!r} ≠ {expected_ans!r}", pid)
        else:
            _ok("CHECK_14", pid, f"answer={item['answer']!r}")

        # CHECK_15: context is exactly 5 newline-separated lines
        ctx_block = item["prompt"].split("\n\n", 1)[0]
        ctx_lines = ctx_block.split("\n")
        if len(ctx_lines) != 5:
            _err("CHECK_15", f"Context has {len(ctx_lines)} lines, expected 5", pid)
        else:
            _ok("CHECK_15", pid, "5-line context")

        # CHECK_16: every context line matches "SUBJ maps to OBJ." pattern
        ctx_errors = []
        for i, line in enumerate(ctx_lines, 1):
            if not re.match(r'^[A-Z]{5} maps to [A-Z]{4,8}\.$', line):
                ctx_errors.append(f"line {i}: {line!r}")
        if ctx_errors:
            _err("CHECK_16", f"Malformed context lines: {ctx_errors}", pid)
        else:
            _ok("CHECK_16", pid, "all context lines well-formed")

        # CHECK_17: context line order matches facts list
        order_ok = True
        for i, (s, o) in enumerate(facts, 1):
            if i - 1 < len(ctx_lines):
                expected_line = f"{s} maps to {o}."
                if ctx_lines[i - 1] != expected_line:
                    _err("CHECK_17",
                         f"Fact {i} mismatch: {ctx_lines[i-1]!r} ≠ {expected_line!r}", pid)
                    order_ok = False
        if order_ok:
            _ok("CHECK_17", pid, "fact order matches context")

        # CHECK_18: decoding determinism asserted (temp=0)
        if not item.get("decoding_determinism_asserted"):
            _err("CHECK_18", "decoding_determinism_asserted is False or missing", pid)
        elif item["decoding"].get("temperature", -1) != 0.0:
            _err("CHECK_18", f"temperature={item['decoding'].get('temperature')} ≠ 0.0", pid)
        else:
            _ok("CHECK_18", pid, f"temp=0.0, max_tokens={item['decoding']['max_tokens']}")

        # CHECK_19: prompt_hash matches actual prompt
        expected_hash = f"sha256:{hashlib.sha256(item['prompt'].encode()).hexdigest()}"
        if not item.get("prompt_hash", "").startswith("sha256:"):
            _err("CHECK_19", "prompt_hash missing or malformed", pid)
        elif item["prompt_hash"] != expected_hash:
            _err("CHECK_19", "prompt_hash mismatch (prompt was mutated?)", pid)
        else:
            _ok("CHECK_19", pid, "prompt_hash verified")

        # CHECK_20: no token is a common English word
        item_tokens = [s for s, _ in facts] + [o for _, o in facts]
        word_hits = [t for t in item_tokens if t in _COMMON_5_LETTER_WORDS]
        if word_hits:
            _err("CHECK_20", f"Common English words detected: {word_hits}", pid)
        else:
            _ok("CHECK_20", pid, "no English words detected")

    # ── Scoring function checks (mirror of CHECK_21–23) ─────────────────────

    # CHECK_21: RETURNED_TARGET_OBJ has priority over RETURNED_OBJ_POS_k
    _ref = ITEMS[0]
    r_correct = score_arm2_content(f"ANSWER: {_ref['target_obj']}", _ref)
    if r_correct["content_class"] != "RETURNED_TARGET_OBJ":
        _err("CHECK_21", f"Correct answer misclassified as {r_correct['content_class']!r}")
    else:
        _nontarget = _ref["facts"][0][1]
        r_wrong = score_arm2_content(f"ANSWER: {_nontarget}", _ref)
        if r_wrong["content_class"] == "RETURNED_TARGET_OBJ":
            _err("CHECK_21", f"Non-target obj {_nontarget!r} classified as RETURNED_TARGET_OBJ")
        elif not r_wrong["content_class"].startswith("RETURNED_OBJ_POS_"):
            _err("CHECK_21",
                 f"Non-target obj {_nontarget!r} got unexpected class {r_wrong['content_class']!r}")
        else:
            for item in ITEMS:
                _ok("CHECK_21", item["id"], "scoring precedence ok")

    # CHECK_22: same_error_identity_key structure (alpha + numeric OOC tokens)
    r_ooc = score_arm2_content("ANSWER: ZZZZZ", ITEMS[0])
    r_num = score_arm2_content("ANSWER: 0",     ITEMS[0])
    check22_ok = True
    if r_ooc["same_error_identity_key"] != "RETURNED_NON_CONTEXT_TOKEN|ZZZZZ|None":
        _err("CHECK_22",
             f"alpha OOC: got {r_ooc['same_error_identity_key']!r}, "
             f"expected 'RETURNED_NON_CONTEXT_TOKEN|ZZZZZ|None'")
        check22_ok = False
    if r_num["same_error_identity_key"] != "RETURNED_NON_CONTEXT_TOKEN|0|None":
        _err("CHECK_22",
             f"numeric OOC: got {r_num['same_error_identity_key']!r}, "
             f"expected 'RETURNED_NON_CONTEXT_TOKEN|0|None'")
        check22_ok = False
    if check22_ok:
        for item in ITEMS:
            _ok("CHECK_22", item["id"], "identity_key structure verified (alpha + numeric)")

    # CHECK_23: 9 content classes, 2 format classes
    if len(_CONTENT_CLASSES) != 9:
        _err("CHECK_23", f"Expected 9 content classes, got {len(_CONTENT_CLASSES)}")
    elif len(_FORMAT_CLASSES) != 2:
        _err("CHECK_23", f"Expected 2 format classes, got {len(_FORMAT_CLASSES)}")
    else:
        for item in ITEMS:
            _ok("CHECK_23", item["id"], "9 content, 2 format classes")

    # CHECK_24: run_tier0 unit tests pass (scorer unchanged)
    try:
        from run_tier0 import run_unit_tests as _rut
        _rut()
        for item in ITEMS:
            _ok("CHECK_24", item["id"], "run_unit_tests() passed")
    except AssertionError as e:
        _err("CHECK_24", f"Scorer unit test failed: {e}")
    except ImportError:
        _err("CHECK_24", "Could not import run_tier0 — run from working directory")

    # CHECK_25: dummy baseline does not reach feasibility threshold
    dummy_scores, max_dummy = _compute_dummy_baselines(ITEMS)
    if max_dummy >= _FEASIBILITY_THRESHOLD:
        _err("CHECK_25",
             f"[CONSTRUCTION FAILURE] max_dummy={max_dummy:.3f} ≥ threshold={_FEASIBILITY_THRESHOLD:.3f}")
    else:
        for item in ITEMS:
            _ok("CHECK_25", item["id"],
                f"max_dummy={max_dummy:.3f} < threshold={_FEASIBILITY_THRESHOLD:.3f}")

    # CHECK_26: tokenizer round-trip consistency (BPE audit)
    try:
        from transformers import AutoTokenizer
        _tok = AutoTokenizer.from_pretrained(
            "Qwen/Qwen2.5-1.5B-Instruct", trust_remote_code=True)
        roundtrip_failures = []
        bpe_counts: dict[str, int] = {}
        for token in sorted(set(all_tokens)):
            ids = _tok.encode(token, add_special_tokens=False)
            decoded = _tok.decode(ids, skip_special_tokens=True)
            bpe_counts[token] = len(ids)
            if decoded.strip() != token:
                roundtrip_failures.append((token, ids, decoded))
        if roundtrip_failures:
            _err("CHECK_26", f"Round-trip failures: {roundtrip_failures}")
        else:
            counts_summary = sorted(set(bpe_counts.values()))
            print(f"  [CHECK_26] BPE piece counts: {dict(sorted({v: sum(1 for c in bpe_counts.values() if c==v) for v in counts_summary}.items()))}")
            print(f"  [CHECK_26] All {len(bpe_counts)} tokens round-trip correctly")
            for item in ITEMS:
                _ok("CHECK_26", item["id"], "round-trip verified")
    except ImportError:
        print("  [CHECK_26] WARNING: transformers not available — tokenizer autopsy skipped")
        for item in ITEMS:
            _ok("CHECK_26", item["id"], "SKIPPED (no transformers)")
    except Exception as e:
        print(f"  [CHECK_26] WARNING: tokenizer load failed ({e}) — autopsy skipped")
        for item in ITEMS:
            _ok("CHECK_26", item["id"], f"SKIPPED ({type(e).__name__})")

    # ── Exp8B-specific reuse and wording checks ──────────────────────────────

    # CHECK_B01: Exp8B item count matches Exp8A item count
    if len(ITEMS) != len(EXP8A_ITEMS):
        _err("CHECK_B01", f"Exp8B n={len(ITEMS)} ≠ Exp8A n={len(EXP8A_ITEMS)}")
    else:
        for item in ITEMS:
            _ok("CHECK_B01", item["id"], f"Exp8B n={len(ITEMS)} == Exp8A n={len(EXP8A_ITEMS)}")

    # CHECK_B02: for each item, facts match Exp8A exactly (tuple-level comparison)
    a_by_id = {a["id"]: a for a in EXP8A_ITEMS}
    for item in ITEMS:
        pid = item["id"]
        a = a_by_id.get(pid)
        if a is None:
            _err("CHECK_B02", f"ID {pid!r} not found in Exp8A", pid)
        elif item["facts"] != a["facts"]:
            # Report first mismatch
            for i, (b_fact, a_fact) in enumerate(zip(item["facts"], a["facts"]), 1):
                if b_fact != a_fact:
                    _err("CHECK_B02",
                         f"Fact {i} mismatch: Exp8B={b_fact} ≠ Exp8A={a_fact}", pid)
                    break
        else:
            _ok("CHECK_B02", pid, "facts == Exp8A facts (tuple-exact)")

    # CHECK_B03: for each item, target_pos matches Exp8A exactly
    for item in ITEMS:
        pid = item["id"]
        a = a_by_id.get(pid)
        if a and item["target_pos"] != a["target_pos"]:
            _err("CHECK_B03",
                 f"target_pos={item['target_pos']} ≠ Exp8A target_pos={a['target_pos']}", pid)
        elif a:
            _ok("CHECK_B03", pid, f"target_pos={item['target_pos']} == Exp8A")

    # CHECK_B04: Exp8B query wording IS present in every prompt
    for item in ITEMS:
        pid = item["id"]
        if EXP8B_QUERY_PREFIX not in item["prompt"]:
            _err("CHECK_B04", f"Exp8B query prefix not found in prompt", pid)
        else:
            _ok("CHECK_B04", pid, f"Exp8B query prefix found: {EXP8B_QUERY_PREFIX!r}")

    # CHECK_B05: Exp8A query wording is NOT present in any Exp8B prompt
    for item in ITEMS:
        pid = item["id"]
        if EXP8A_QUERY_PREFIX in item["prompt"]:
            _err("CHECK_B05", f"Exp8A query prefix still present — wording not replaced", pid)
        else:
            _ok("CHECK_B05", pid, f"Exp8A query prefix absent (correct)")

    # CHECK_B06: prompt_hash differs from Exp8A prompt_hash for every item
    hash_collision = False
    for item in ITEMS:
        pid = item["id"]
        a = a_by_id.get(pid)
        if a and item["prompt_hash"] == a.get("prompt_hash"):
            _err("CHECK_B06",
                 f"Exp8B prompt_hash == Exp8A prompt_hash — prompt not changed", pid)
            hash_collision = True
        elif a:
            _ok("CHECK_B06", pid,
                f"prompt_hash differs from Exp8A (wording change confirmed)")
    if not hash_collision and not any(e[0] == "CHECK_B06" for e in errors):
        pass  # all per-item OK already recorded above

    # ── Print per-item report ────────────────────────────────────────────────

    print("\n=== VALIDATOR REPORT — tasks_exp8b.py ===\n")
    print(f"  n={len(ITEMS)} items  |  arm=2B  |  target_pos distribution: {pos_counts}\n")
    print(f"  Query change:")
    print(f"    Exp8A: {EXP8A_QUERY_PREFIX}<SUBJ>?")
    print(f"    Exp8B: {EXP8B_QUERY_PREFIX}<SUBJ>?\n")

    for item in ITEMS:
        pid    = item["id"]
        a      = a_by_id.get(pid, {})
        checks = per_item.get(pid, [])
        fails  = [(cid, detail) for cid, status, detail in checks if status == "FAIL"]
        status = "PASS" if not fails else f"FAIL ({', '.join(f[0] for f in fails)})"
        print(f"  {pid}  target_pos={item['target_pos']}  "
              f"target={item['target_subj']}→{item['target_obj']}  [{status}]")
        if not fails:
            print(f"    prompt_hash (8B): {item['prompt_hash']}")
            print(f"    prompt_hash (8A): {a.get('prompt_hash', 'N/A')}")
            print(f"    facts_match_8A:   {'YES' if item['facts'] == a.get('facts') else 'NO'}")
        else:
            for cid, detail in fails:
                print(f"    {cid}: {detail}")

    # ── Dummy baseline report ────────────────────────────────────────────────

    print("\n--- Dummy baseline scores (deterministic — item geometry identical to Exp8A) ---")
    for name, score in dummy_scores.items():
        marker = "  ← max" if score == max_dummy else ""
        print(f"  {name:<25} {score:.3f}{marker}")
    print(f"  max_dummy_score:          {max_dummy:.3f}")
    print(f"  feasibility_threshold:    {_FEASIBILITY_THRESHOLD:.3f}")
    if max_dummy >= _FEASIBILITY_THRESHOLD:
        print("  [CONSTRUCTION FAILURE] Deterministic dummy reached threshold!")
    else:
        print("  [OK] max_dummy < threshold — baseline inflation not a concern")

    # ── Changed fields summary ───────────────────────────────────────────────

    print("\n--- Changed fields relative to Exp8A ---")
    print("  arm:         2  →  2B")
    print("  query:       'Which value is associated with <SUBJ>?'")
    print("               →  'Which token is assigned to <SUBJ>?'")
    print("  prompt_hash: changed (new query; context unchanged)")
    print("  Unchanged:   facts, target_pos, target_subj, target_obj,")
    print("               answer, decoding, scaffold, context lines,")
    print("               scoring functions (score_arm2_content/scaffold/format)")

    # ── Global error summary ─────────────────────────────────────────────────

    if errors:
        print(f"\n[FAILED] {len(errors)} check(s) failed:")
        for check_id, item_id, msg in errors:
            loc = f" ({item_id})" if item_id else " (global)"
            print(f"  {check_id}{loc}: {msg}")
        return False

    total_checks = sum(len(v) for v in per_item.values())
    print(f"\n[ALL CHECKS PASSED] {total_checks} checks across {len(ITEMS)} items")
    return True


# ─── Entry point ──────────────────────────────────────────────────────────

if __name__ == "__main__":
    ok = validate_tasks()
    print(f"\nManifest hash: {get_manifest_hash()}")
    sys.exit(0 if ok else 1)
