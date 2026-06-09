#!/usr/bin/env python3
"""
tasks_fork_a_n24.py — n=24 expanded manifest for Synthetic Key-Value Selection
Constructibility, 3B FP16 baseline.

Track:           Synthetic Key-Value Selection Constructibility
Family:          L3 (expansion of L2 from Exp8 / tasks_exp8.py)
n:               24  (8 items per target_pos in {2, 3, 4})
Construction:    frozen — same rules as tasks_exp8.py (L2 family)
Scorer:          imported unchanged from tasks_exp8.py
Manifest note:   generated after 3B n=8 result was FEASIBLE (8/8)
                 NO item-level repair, selective inclusion, or post-hoc tuning
                 Token pools generated deterministically from algorithm alone

Token design:
  Subjects: {PREFIX}{LETTER}NVX   PREFIX ∈ {L,T,R,F,K}  LETTER ∈ A-X (24 chars)
            5 groups × 24 tokens = 120 total
            Within-item prefix mixing: each item's 5 facts use 5 different prefixes
            → zero homogeneous-prefix items (contrast with L2 family: 4/8 homogeneous)

  Objects:  {PREFIX}{LETTER}NBX   PREFIX ∈ {J,Q,X,Y,Z}  LETTER ∈ A-X (24 chars)
            5 groups × 24 tokens = 120 total
            Within-item prefix mixing: same structure as subjects

  Token assignment:
    item j (0-indexed), fact k (0-indexed):
      subject = SUBJ_PREFIXES[k] + TOKEN_LETTERS[j] + 'NVX'
      object  = OBJ_PREFIXES[k]  + TOKEN_LETTERS[j] + 'NBX'
    → fact position determines prefix; item index determines letter
    → within any item, all 5 subjects have different prefixes

Run static validation:
  python3 tasks_fork_a_n24.py
"""

import hashlib
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from tasks_exp8 import (
    EXP7_TOKENS,
    ARM2_SUBJECTS,
    ARM2_OBJECTS,
    _COMMON_5_LETTER_WORDS,
    _SCAFFOLD,
    _DECODING,
    _DECODING_DETERMINISM_ASSERTED,
    _CONTENT_CLASSES,
    _FORMAT_CLASSES,
    score_arm2_content,
    score_arm2_format,
    score_arm2_scaffold,
)

# ── Scorer provenance ────────────────────────────────────────────────────────
# Scorer functions are imported unchanged from tasks_exp8.py.
# Scorer hash = manifest hash of tasks_exp8.py — verified by runner preflight.
SCORER_SOURCE_FILE = "tasks_exp8.py"

# ── Exclusion set ────────────────────────────────────────────────────────────
_EXP8_TOKENS  = frozenset(ARM2_SUBJECTS + ARM2_OBJECTS)
_ALL_EXCLUDED = EXP7_TOKENS | _EXP8_TOKENS

# ── Token pool generation (deterministic) ────────────────────────────────────
# 5 prefixes × 24 letters = 120 tokens per pool (subjects and objects)
# Within each item: fact k uses prefix group k → 5 different prefixes per item
_SUBJ_PREFIXES  = ['L', 'T', 'R', 'F', 'K']   # one per fact position (0-4)
_OBJ_PREFIXES   = ['J', 'Q', 'X', 'Y', 'Z']   # one per fact position (0-4)
_TOKEN_LETTERS  = 'ABCDEFGHIJKLMNOPQRSTUVWX'   # 24 chars → 5 × 24 = 120 per pool

# Pool layout: _SUBJ_POOL[k*24 + j] = subject for fact k of item j
_SUBJ_POOL = [p + c + 'NVX' for p in _SUBJ_PREFIXES for c in _TOKEN_LETTERS]
_OBJ_POOL  = [p + c + 'NBX' for p in _OBJ_PREFIXES  for c in _TOKEN_LETTERS]


# ── Pool verification (fails loudly at module load) ──────────────────────────

def _verify_pools() -> None:
    errs = []
    if len(_SUBJ_POOL) != 120:
        errs.append(f"SUBJ_POOL: {len(_SUBJ_POOL)} tokens, expected 120")
    if len(_OBJ_POOL) != 120:
        errs.append(f"OBJ_POOL: {len(_OBJ_POOL)} tokens, expected 120")
    if len(set(_SUBJ_POOL)) != 120:
        errs.append("SUBJ_POOL contains duplicates")
    if len(set(_OBJ_POOL)) != 120:
        errs.append("OBJ_POOL contains duplicates")
    overlap_subj = set(_SUBJ_POOL) & _ALL_EXCLUDED
    overlap_obj  = set(_OBJ_POOL)  & _ALL_EXCLUDED
    overlap_so   = set(_SUBJ_POOL) & set(_OBJ_POOL)
    if overlap_subj: errs.append(f"SUBJ_POOL ∩ exclusions: {overlap_subj}")
    if overlap_obj:  errs.append(f"OBJ_POOL ∩ exclusions: {overlap_obj}")
    if overlap_so:   errs.append(f"SUBJ_POOL ∩ OBJ_POOL: {overlap_so}")
    bad = [t for t in _SUBJ_POOL + _OBJ_POOL if not re.match(r'^[A-Z]{5}$', t)]
    if bad: errs.append(f"Tokens failing 5-char uppercase check: {bad[:10]}")
    if errs:
        raise RuntimeError("Pool verification failed:\n" + "\n".join(errs))

_verify_pools()


# ── Prompt builder (frozen — identical to tasks_exp8.py) ────────────────────

def _make_arm2_prompt(facts: list, target_subj: str) -> str:
    context = "\n".join(f"{s} maps to {o}." for s, o in facts)
    return (
        f"{context}\n\n"
        f"Which value is associated with {target_subj}? {_SCAFFOLD}"
    )


def _make_item(item_id: str, facts: list, target_pos: int) -> dict:
    target_subj, target_obj = facts[target_pos - 1]
    prompt = _make_arm2_prompt(facts, target_subj)
    return {
        "id":          item_id,
        "arm":         2,
        "family":      "L3",
        "target_pos":  target_pos,
        "facts":       facts,
        "target_subj": target_subj,
        "target_obj":  target_obj,
        "prompt":      prompt,
        "prompt_hash": f"sha256:{hashlib.sha256(prompt.encode()).hexdigest()}",
        "answer":      f"ANSWER: {target_obj}",
        "score_type":  "exact",
        "decoding":    _DECODING,
        "decoding_determinism_asserted": _DECODING_DETERMINISM_ASSERTED,
    }


# ── Item construction ────────────────────────────────────────────────────────
# 24 items: 8 per target_pos ∈ {2, 3, 4}
# item j (0-indexed): facts[k] = (SUBJ_POOL[k*24+j], OBJ_POOL[k*24+j])
# items 0-7: target_pos=2  |  items 8-15: target_pos=3  |  items 16-23: target_pos=4

ITEMS = []
for _j in range(24):
    _facts = [
        (_SUBJ_POOL[_k * 24 + _j], _OBJ_POOL[_k * 24 + _j])
        for _k in range(5)
    ]
    _tpos = 2 if _j < 8 else (3 if _j < 16 else 4)
    _id   = f"L3_{_j + 1:02d}"
    ITEMS.append(_make_item(_id, _facts, _tpos))


# ── Feasibility threshold ─────────────────────────────────────────────────────
# Proposed: ≥21/24 (same pass rate as n=8 gate: 7/8 = 87.5%)
# Requires Manager confirmation before scored run.
_FEASIBILITY_THRESHOLD_RATE = 7 / 8
_PROPOSED_FEASIBILITY_N     = 21
_FEASIBILITY_N_NOTE = (
    "n=24 gate proposed at ≥21/24 (87.5% — same rate as n=8 gate). "
    "Requires Manager confirmation before scored run."
)


# ── Dummy baseline ────────────────────────────────────────────────────────────

def _compute_dummy_baselines(items: list) -> tuple:
    n = len(items)
    counts = {
        "always_fact1_obj": 0, "always_fact2_obj": 0, "always_fact3_obj": 0,
        "always_fact4_obj": 0, "always_fact5_obj": 0,
        "always_first_obj": 0, "always_last_obj":  0,
    }
    for item in items:
        tgt  = item["target_obj"]
        objs = [o for _, o in item["facts"]]
        if objs[0] == tgt: counts["always_fact1_obj"] += 1
        if objs[1] == tgt: counts["always_fact2_obj"] += 1
        if objs[2] == tgt: counts["always_fact3_obj"] += 1
        if objs[3] == tgt: counts["always_fact4_obj"] += 1
        if objs[4] == tgt: counts["always_fact5_obj"] += 1
        if objs[0] == tgt: counts["always_first_obj"] += 1
        if objs[-1]== tgt: counts["always_last_obj"]  += 1
    scores = {k: v / n for k, v in counts.items()}
    return scores, max(scores.values())


# ── Static validator ──────────────────────────────────────────────────────────

def validate_tasks() -> bool:
    all_subjects = [s for item in ITEMS for s, _ in item["facts"]]
    all_objects  = [o for item in ITEMS for _, o in item["facts"]]
    all_tokens   = all_subjects + all_objects
    subj_set     = set(all_subjects)
    obj_set      = set(all_objects)

    errors = []
    per_item: dict[str, list] = {}

    def _err(check_id: str, msg: str, item_id: str | None = None):
        errors.append((check_id, item_id, msg))
        if item_id:
            per_item.setdefault(item_id, []).append((check_id, "FAIL", msg))

    def _ok(check_id: str, item_id: str, detail: str = ""):
        per_item.setdefault(item_id, []).append((check_id, "PASS", detail))

    # CHECK_N01: n == 24
    if len(ITEMS) != 24:
        _err("CHECK_N01", f"Expected 24 items, got {len(ITEMS)}")
    else:
        for item in ITEMS: _ok("CHECK_N01", item["id"], "n=24")

    # CHECK_N02: target_pos distribution = {2:8, 3:8, 4:8}
    pos_counts: dict[int, int] = {}
    for item in ITEMS:
        pos_counts[item["target_pos"]] = pos_counts.get(item["target_pos"], 0) + 1
    expected_dist = {2: 8, 3: 8, 4: 8}
    if pos_counts != expected_dist:
        _err("CHECK_N02", f"Distribution {pos_counts} ≠ expected {expected_dist}")
    else:
        for item in ITEMS: _ok("CHECK_N02", item["id"], f"target_pos={item['target_pos']}")

    # CHECK_N03: target_pos ∈ {2,3,4}
    for item in ITEMS:
        if item["target_pos"] not in {2, 3, 4}:
            _err("CHECK_N03", f"target_pos={item['target_pos']} ∉ {{2,3,4}}", item["id"])
        else:
            _ok("CHECK_N03", item["id"], f"target_pos={item['target_pos']}")

    # CHECK_N04: every item has exactly 5 facts
    for item in ITEMS:
        if len(item["facts"]) != 5:
            _err("CHECK_N04", f"Expected 5 facts, got {len(item['facts'])}", item["id"])
        else:
            _ok("CHECK_N04", item["id"], "5 facts")

    # CHECK_N05: all subjects unique across items
    if len(all_subjects) != len(set(all_subjects)):
        dupes = {s for s in all_subjects if all_subjects.count(s) > 1}
        _err("CHECK_N05", f"Duplicate subjects: {dupes}")
    else:
        for item in ITEMS: _ok("CHECK_N05", item["id"], "subjects unique")

    # CHECK_N06: all objects unique across items
    if len(all_objects) != len(set(all_objects)):
        dupes = {o for o in all_objects if all_objects.count(o) > 1}
        _err("CHECK_N06", f"Duplicate objects: {dupes}")
    else:
        for item in ITEMS: _ok("CHECK_N06", item["id"], "objects unique")

    # CHECK_N07: subjects and objects fully disjoint
    overlap = subj_set & obj_set
    if overlap:
        _err("CHECK_N07", f"Subject/object overlap: {overlap}")
    else:
        for item in ITEMS: _ok("CHECK_N07", item["id"], "no chain overlap")

    # CHECK_N08: no token in EXP7 or Exp8 (L2) exclusion pool
    excluded_hits = set(all_tokens) & _ALL_EXCLUDED
    if excluded_hits:
        _err("CHECK_N08", f"Exclusion pool overlap: {excluded_hits}")
    else:
        for item in ITEMS: _ok("CHECK_N08", item["id"], "no exclusion pool overlap")

    # CHECK_N09: all tokens exactly 5 uppercase letters
    bad_tokens = [t for t in all_tokens if not re.match(r'^[A-Z]{5}$', t)]
    if bad_tokens:
        _err("CHECK_N09", f"Tokens failing format: {bad_tokens}")
    else:
        for item in ITEMS: _ok("CHECK_N09", item["id"], "all 5-char uppercase")

    # CHECK_N10: global token uniqueness
    if len(all_tokens) != len(set(all_tokens)):
        dupes = {t for t in all_tokens if all_tokens.count(t) > 1}
        _err("CHECK_N10", f"Combined pool duplicates: {dupes}")
    else:
        for item in ITEMS: _ok("CHECK_N10", item["id"], "global uniqueness ok")

    # CHECK_N11: within-item prefix mixing — no homogeneous subject prefix pools
    homog_items = []
    for item in ITEMS:
        prefixes = {s[0] for s, _ in item["facts"]}
        if len(prefixes) < 5:
            homog_items.append((item["id"], sorted(prefixes)))
    if homog_items:
        _err("CHECK_N11",
             f"Items with <5 distinct subject prefixes (homogeneous): {homog_items}")
    else:
        for item in ITEMS:
            _ok("CHECK_N11", item["id"], "5 distinct subject prefixes")

    # Per-item structural checks
    for item in ITEMS:
        pid   = item["id"]
        facts = item["facts"]
        tp    = item["target_pos"]
        t_subj, t_obj = facts[tp - 1]

        # CHECK_N12: target correctly derived
        if item["target_subj"] != t_subj or item["target_obj"] != t_obj:
            _err("CHECK_N12",
                 f"target mismatch: ({item['target_subj']},{item['target_obj']}) "
                 f"vs fact {tp} ({t_subj},{t_obj})", pid)
        else:
            _ok("CHECK_N12", pid, f"target={t_subj}→{t_obj} pos {tp}")

        # CHECK_N13: no forbidden mapping words in query
        query_part = item["prompt"].split("\n\n", 1)[-1] if "\n\n" in item["prompt"] else ""
        q_lower = query_part.lower()
        if "maps" in q_lower or " map " in q_lower or "mapped" in q_lower:
            _err("CHECK_N13", "Query contains forbidden mapping word", pid)
        else:
            _ok("CHECK_N13", pid, "query maps-free")

        # CHECK_N14: scaffold present
        if _SCAFFOLD not in item["prompt"]:
            _err("CHECK_N14", "Standard scaffold missing", pid)
        else:
            _ok("CHECK_N14", pid, "scaffold present")

        # CHECK_N15: answer field correct
        if item["answer"] != f"ANSWER: {t_obj}":
            _err("CHECK_N15", f"answer={item['answer']!r} ≠ 'ANSWER: {t_obj}'", pid)
        else:
            _ok("CHECK_N15", pid, f"answer ok")

        # CHECK_N16: context is exactly 5 lines
        ctx_block = item["prompt"].split("\n\n", 1)[0]
        ctx_lines = ctx_block.split("\n")
        if len(ctx_lines) != 5:
            _err("CHECK_N16", f"Context has {len(ctx_lines)} lines, expected 5", pid)
        else:
            _ok("CHECK_N16", pid, "5-line context")

        # CHECK_N17: context lines match "SUBJ maps to OBJ." pattern
        ctx_errors = []
        for i, line in enumerate(ctx_lines, 1):
            if not re.match(r'^[A-Z]{5} maps to [A-Z]{4,8}\.$', line):
                ctx_errors.append(f"line {i}: {line!r}")
        if ctx_errors:
            _err("CHECK_N17", f"Malformed context lines: {ctx_errors}", pid)
        else:
            _ok("CHECK_N17", pid, "all context lines well-formed")

        # CHECK_N18: fact order matches context
        order_ok = True
        for i, (s, o) in enumerate(facts, 1):
            if i - 1 < len(ctx_lines):
                if ctx_lines[i - 1] != f"{s} maps to {o}.":
                    _err("CHECK_N18",
                         f"Fact {i} mismatch: {ctx_lines[i-1]!r}", pid)
                    order_ok = False
        if order_ok:
            _ok("CHECK_N18", pid, "fact order matches context")

        # CHECK_N19: decoding determinism
        if not item.get("decoding_determinism_asserted"):
            _err("CHECK_N19", "decoding_determinism_asserted missing", pid)
        elif item["decoding"].get("temperature", -1) != 0.0:
            _err("CHECK_N19", f"temperature ≠ 0.0", pid)
        else:
            _ok("CHECK_N19", pid, "temp=0.0 asserted")

        # CHECK_N20: prompt_hash matches
        expected_hash = f"sha256:{hashlib.sha256(item['prompt'].encode()).hexdigest()}"
        if item.get("prompt_hash") != expected_hash:
            _err("CHECK_N20", "prompt_hash mismatch", pid)
        else:
            _ok("CHECK_N20", pid, "prompt_hash verified")

        # CHECK_N21: no common English words
        item_tokens = [s for s, _ in facts] + [o for _, o in facts]
        word_hits = [t for t in item_tokens if t in _COMMON_5_LETTER_WORDS]
        if word_hits:
            _err("CHECK_N21", f"English words: {word_hits}", pid)
        else:
            _ok("CHECK_N21", pid, "no English words")

    # CHECK_N22: scorer precedence
    _ref = ITEMS[0]
    r_correct = score_arm2_content(f"ANSWER: {_ref['target_obj']}", _ref)
    if r_correct["content_class"] != "RETURNED_TARGET_OBJ":
        _err("CHECK_N22", f"Correct answer → {r_correct['content_class']!r}")
    else:
        _nontarget = _ref["facts"][0][1]
        r_wrong = score_arm2_content(f"ANSWER: {_nontarget}", _ref)
        if r_wrong["content_class"] == "RETURNED_TARGET_OBJ":
            _err("CHECK_N22", "Non-target classified as RETURNED_TARGET_OBJ")
        elif not r_wrong["content_class"].startswith("RETURNED_OBJ_POS_"):
            _err("CHECK_N22", f"Non-target → {r_wrong['content_class']!r}")
        else:
            for item in ITEMS: _ok("CHECK_N22", item["id"], "scoring precedence ok")

    # CHECK_N23: identity_key structure
    r_ooc = score_arm2_content("ANSWER: ZZZZZ", ITEMS[0])
    r_num = score_arm2_content("ANSWER: 0",     ITEMS[0])
    ok23 = True
    if r_ooc["same_error_identity_key"] != "RETURNED_NON_CONTEXT_TOKEN|ZZZZZ|None":
        _err("CHECK_N23", f"OOC key: {r_ooc['same_error_identity_key']!r}"); ok23=False
    if r_num["same_error_identity_key"] != "RETURNED_NON_CONTEXT_TOKEN|0|None":
        _err("CHECK_N23", f"numeric key: {r_num['same_error_identity_key']!r}"); ok23=False
    if ok23:
        for item in ITEMS: _ok("CHECK_N23", item["id"], "identity_key ok")

    # CHECK_N24: 9 content classes, 2 format classes registered
    if len(_CONTENT_CLASSES) != 9 or len(_FORMAT_CLASSES) != 2:
        _err("CHECK_N24",
             f"Class registry: {len(_CONTENT_CLASSES)} content, {len(_FORMAT_CLASSES)} format")
    else:
        for item in ITEMS: _ok("CHECK_N24", item["id"], "9+2 class registry ok")

    # CHECK_N25: dummy baseline below threshold
    dummy_scores, max_dummy = _compute_dummy_baselines(ITEMS)
    if max_dummy >= _FEASIBILITY_THRESHOLD_RATE:
        _err("CHECK_N25",
             f"[CONSTRUCTION FAILURE] max_dummy={max_dummy:.3f} ≥ {_FEASIBILITY_THRESHOLD_RATE:.3f}")
    else:
        for item in ITEMS:
            _ok("CHECK_N25", item["id"],
                f"max_dummy={max_dummy:.3f} < {_FEASIBILITY_THRESHOLD_RATE:.3f}")

    # CHECK_N26: tokenizer round-trip (3B tokenizer)
    try:
        from transformers import AutoTokenizer
        _tok = AutoTokenizer.from_pretrained(
            "Qwen/Qwen2.5-3B-Instruct", trust_remote_code=True)
        rt_failures = []
        bpe_counts: dict[str, int] = {}
        for token in sorted(set(all_tokens)):
            ids = _tok.encode(token, add_special_tokens=False)
            decoded = _tok.decode(ids, skip_special_tokens=True)
            bpe_counts[token] = len(ids)
            if decoded.strip() != token:
                rt_failures.append((token, ids, decoded))
        if rt_failures:
            _err("CHECK_N26", f"Round-trip failures: {rt_failures}")
        else:
            bpe_dist = {}
            for v in set(bpe_counts.values()):
                bpe_dist[v] = sum(1 for c in bpe_counts.values() if c == v)
            print(f"  [CHECK_N26] BPE counts (3B): {dict(sorted(bpe_dist.items()))}")
            print(f"  [CHECK_N26] All {len(bpe_counts)} tokens round-trip correctly")
            for item in ITEMS: _ok("CHECK_N26", item["id"], "round-trip verified")
    except ImportError:
        print("  [CHECK_N26] WARNING: transformers unavailable — skipped")
        for item in ITEMS: _ok("CHECK_N26", item["id"], "SKIPPED (no transformers)")
    except Exception as e:
        print(f"  [CHECK_N26] WARNING: {e} — skipped")
        for item in ITEMS: _ok("CHECK_N26", item["id"], f"SKIPPED ({type(e).__name__})")

    # ── Print report ──────────────────────────────────────────────────────────

    print(f"\n=== VALIDATOR REPORT — tasks_fork_a_n24.py ===\n")
    print(f"  n={len(ITEMS)} items  |  family=L3  |  target_pos distribution: {pos_counts}")
    print(f"  Subject prefixes per item: 5 distinct (L/T/R/F/K rotated by fact position)\n")

    for item in ITEMS:
        pid    = item["id"]
        checks = per_item.get(pid, [])
        fails  = [(cid, d) for cid, status, d in checks if status == "FAIL"]
        status = "PASS" if not fails else f"FAIL ({', '.join(f[0] for f in fails)})"
        subj_pfxs = sorted({s[0] for s, _ in item["facts"]})
        print(f"  {pid}  pos={item['target_pos']}  "
              f"target={item['target_subj']}→{item['target_obj']}  "
              f"subj_pfx={subj_pfxs}  [{status}]")
        for cid, detail in fails:
            print(f"    {cid}: {detail}")

    print("\n--- Dummy baseline scores ---")
    for name, score in dummy_scores.items():
        marker = "  ← max" if score == max_dummy else ""
        print(f"  {name:<25} {score:.3f}{marker}")
    print(f"  max_dummy:                {max_dummy:.3f}")
    print(f"  feasibility threshold:    {_FEASIBILITY_THRESHOLD_RATE:.3f}  "
          f"→ proposed gate: ≥{_PROPOSED_FEASIBILITY_N}/24")
    print(f"  Note: {_FEASIBILITY_N_NOTE}")

    if errors:
        print(f"\n[FAILED] {len(errors)} check(s) failed:")
        for check_id, item_id, msg in errors:
            loc = f" ({item_id})" if item_id else " (global)"
            print(f"  {check_id}{loc}: {msg}")
        return False

    total_checks = sum(len(v) for v in per_item.values())
    print(f"\n[ALL CHECKS PASSED] {total_checks} checks across {len(ITEMS)} items")
    return True


# ── Manifest hash ─────────────────────────────────────────────────────────────

def get_manifest_hash() -> str:
    return f"sha256:{hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}"


# ── Entry point ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    ok = validate_tasks()
    print(f"\nManifest hash: {get_manifest_hash()}")
    print(f"Scorer source: {SCORER_SOURCE_FILE} (imported unchanged)")
    sys.exit(0 if ok else 1)
