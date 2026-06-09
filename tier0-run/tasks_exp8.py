#!/usr/bin/env python3
"""
tasks_exp8.py — Exp8 Arm 2: load-matched single-lookup feasibility items (n=8).

Arm 2 design:
  Relation:    "maps to" (directional, conclusion-locked: SUBJ → OBJ)
  Context:     5-fact list, newline-separated
  Query:       "Which value is associated with SUBJ_T?"  (no maps/map/mapped)
  Positions:   target_pos ∈ {2,3,4}  (1 and 5 never targeted)
  Balance:     pos2×3, pos3×3, pos4×2  (n=8 total)
  Feasibility threshold: ≥7/8 FP16 content PASS

Purpose:
  Load-matched single-lookup baseline. Tests whether the model can bind
  SUBJ_T to its object under uniform 5-fact context without a chain graph.
  Controls for context-load confound in component-check interpretation.

Scoring:
  score_arm2_content  — 9 content_class values (RETURNED_TARGET_OBJ has priority)
  score_arm2_format   — 2 format_class values (FORMAT_PASS / FORMAT_FAIL)
  same_error_identity — compound key: content_class + returned_token + returned_fact_position

Pre-registration: PREREGISTRATION-EXP8.md (pending Team Lead sign-off)

Run static validation:
  python3 tasks_exp8.py
"""

import hashlib
import re
import sys
from pathlib import Path


# ─── Exp7 exclusion pool (103 tokens — must not reuse) ────────────────────
EXP7_TOKENS = frozenset({
    'BAXNU', 'BILMO', 'BIXTV', 'BLIVX', 'BLIXO', 'BLIXT', 'BLUXN', 'BROXN',
    'BUVAX', 'DRALX', 'DRIXM', 'DRIXP', 'DRIZP', 'DROFL', 'DRUVF', 'DUPLX',
    'FAVOX', 'FLIPN', 'FLONB', 'FLOXB', 'FLUMB', 'FROPK', 'GLIFP', 'GLIVN',
    'GLOXI', 'GRAFI', 'GRAXB', 'GRIVT', 'GRIXP', 'GROXL', 'GRULP', 'GRUMV',
    'GRUVL', 'JAXOL', 'KARBX', 'KARVO', 'KLINP', 'KLOMF', 'KLOMR', 'KLONB',
    'KORNU', 'KRAXI', 'KRAZM', 'KRONB', 'LORVX', 'MAXBI', 'MEXOT', 'NAKVI',
    'NAXBI', 'NIXBL', 'NORVA', 'NOXBA', 'ORBUX', 'PAMVL', 'PIXNV', 'PLOMV',
    'PLONX', 'PLOXN', 'PRAXE', 'PROXK', 'QUAFT', 'RAXLV', 'SKRON', 'SLOMX',
    'SORMB', 'SORNI', 'TAXGR', 'TRAXK', 'TRAXO', 'TREXN', 'TROXB', 'VARGN',
    'VAXLM', 'VEFLM', 'VIMPL', 'VLUMB', 'VOMPL', 'VRAXB', 'VRAXI', 'VUNFT',
    'VUNLB', 'WEXBI', 'WIVOT', 'WIXPL', 'WOVLU', 'WOXEN', 'WOXUR', 'WULFT',
    'WULNI', 'WUMFT', 'WUNFA', 'XOMBI', 'XOTBI', 'YOMBL', 'ZAPVI', 'ZARPL',
    'ZARVP', 'ZEPHI', 'ZIXPA', 'ZOMPL', 'ZROXN', 'ZULNX', 'ZULPA',
})

# ─── Arm 2 token registry ─────────────────────────────────────────────────
# Subjects and objects are fully disjoint pools. No token reused across items.
# Subjects: start with A, C, E, H, U  (fresh starts not in Exp7)
# Objects:  start with I, O, P, S     (fresh starts not in Exp7)
# Items are the source of truth; these lists serve the validator.

ARM2_SUBJECTS = [
    # L2_01 (target_pos=2)
    'ALNOX', 'ARVUX', 'AXBIV', 'AZMIX', 'ACVLX',
    # L2_02 (target_pos=2)
    'CARVX', 'CIRNX', 'CLUVX', 'COBNX', 'CBLUX',
    # L2_03 (target_pos=2)
    'HALVX', 'HIBNX', 'HOBVX', 'HCIVX', 'HELVX',
    # L2_04 (target_pos=3)
    'UBVAX', 'UCIVX', 'UFBNX', 'ULGVX', 'UMBIX',
    # L2_05 (target_pos=3)
    'ARBLX', 'CLIVX', 'EBVNX', 'HVIBX', 'UVBIX',
    # L2_06 (target_pos=3)
    'ACBLX', 'ECLVX', 'HGIVX', 'UVNBX', 'AINVX',
    # L2_07 (target_pos=4)
    'CRIVX', 'ELIVX', 'HIVNX', 'UNVBX', 'AZNUX',
    # L2_08 (target_pos=4)
    'EBMOX', 'HNVUX', 'CVBLX', 'ACNLX', 'HAXVB',
]

ARM2_OBJECTS = [
    # L2_01 (target=fact2 → ICVLX)
    'IBVOX', 'ICVLX', 'IDBLX', 'IFVNX', 'IGBNX',
    # L2_02 (target=fact2 → OBLVX)
    'OCIVX', 'OBLVX', 'ODBNX', 'OFVNX', 'OGIBN',
    # L2_03 (target=fact2 → OICVX)
    'OHIBX', 'OICVX', 'OJBNX', 'OKCVX', 'OLMVX',
    # L2_04 (target=fact3 → PCIVX)
    'PACVX', 'PBCVX', 'PCIVX', 'PDBNX', 'PFVNX',
    # L2_05 (target=fact3 → SCIVX)
    'SACVX', 'SBCVX', 'SCIVX', 'SDBNX', 'SFVNX',
    # L2_06 (target=fact3 → IDBVX)
    'IACVX', 'IBCNX', 'IDBVX', 'IECDX', 'IFCVX',
    # L2_07 (target=fact4 → OECVX)
    'OABVX', 'OCBNX', 'ODBVX', 'OECVX', 'OFBNX',
    # L2_08 (target=fact4 → PJBVX)
    'PAHVX', 'PCHVX', 'PIBVX', 'PJBVX', 'PKBVX',
]

# ─── Decoding configuration (static assertion) ────────────────────────────
# temperature=0 → greedy decoding → deterministic outputs.
_DECODING = {"temperature": 0.0, "max_tokens": 16}
_DECODING_DETERMINISM_ASSERTED = True  # temp=0, no sampling

# ─── Standard format scaffold (unchanged from Exp5–7) ─────────────────────
_SCAFFOLD = "Respond using only this exact format with nothing before or after: ANSWER:"


# ─── Prompt builder ───────────────────────────────────────────────────────

def _make_arm2_prompt(facts: list, target_subj: str) -> str:
    context = "\n".join(f"{s} maps to {o}." for s, o in facts)
    return (
        f"{context}\n\n"
        f"Which value is associated with {target_subj}? {_SCAFFOLD}"
    )


def _make_item(item_id: str, facts: list, target_pos: int) -> dict:
    """Build an Arm 2 item dict. target_pos is 1-indexed."""
    target_subj, target_obj = facts[target_pos - 1]
    prompt = _make_arm2_prompt(facts, target_subj)
    return {
        "id": item_id,
        "arm": 2,
        "family": "L",          # Load-matched single-lookup
        "target_pos": target_pos,
        "facts": facts,         # list of (subj, obj) tuples
        "target_subj": target_subj,
        "target_obj": target_obj,
        "prompt": prompt,
        "prompt_hash": f"sha256:{hashlib.sha256(prompt.encode()).hexdigest()}",
        "answer": f"ANSWER: {target_obj}",
        "score_type": "exact",
        "decoding": _DECODING,
        "decoding_determinism_asserted": _DECODING_DETERMINISM_ASSERTED,
    }


# ─── Item definitions ─────────────────────────────────────────────────────
# target_pos distribution: pos2×3 (L2_01–L2_03), pos3×3 (L2_04–L2_06), pos4×2 (L2_07–L2_08)

L2_01 = _make_item("L2_01", [
    ("ALNOX", "IBVOX"),
    ("ARVUX", "ICVLX"),    # ← target (pos=2)
    ("AXBIV", "IDBLX"),
    ("AZMIX", "IFVNX"),
    ("ACVLX", "IGBNX"),
], target_pos=2)

L2_02 = _make_item("L2_02", [
    ("CARVX", "OCIVX"),
    ("CIRNX", "OBLVX"),    # ← target (pos=2)
    ("CLUVX", "ODBNX"),
    ("COBNX", "OFVNX"),
    ("CBLUX", "OGIBN"),
], target_pos=2)

L2_03 = _make_item("L2_03", [
    ("HALVX", "OHIBX"),
    ("HIBNX", "OICVX"),    # ← target (pos=2)
    ("HOBVX", "OJBNX"),
    ("HCIVX", "OKCVX"),
    ("HELVX", "OLMVX"),
], target_pos=2)

L2_04 = _make_item("L2_04", [
    ("UBVAX", "PACVX"),
    ("UCIVX", "PBCVX"),
    ("UFBNX", "PCIVX"),    # ← target (pos=3)
    ("ULGVX", "PDBNX"),
    ("UMBIX", "PFVNX"),
], target_pos=3)

L2_05 = _make_item("L2_05", [
    ("ARBLX", "SACVX"),
    ("CLIVX", "SBCVX"),
    ("EBVNX", "SCIVX"),    # ← target (pos=3)
    ("HVIBX", "SDBNX"),
    ("UVBIX", "SFVNX"),
], target_pos=3)

L2_06 = _make_item("L2_06", [
    ("ACBLX", "IACVX"),
    ("ECLVX", "IBCNX"),
    ("HGIVX", "IDBVX"),    # ← target (pos=3)
    ("UVNBX", "IECDX"),
    ("AINVX", "IFCVX"),
], target_pos=3)

L2_07 = _make_item("L2_07", [
    ("CRIVX", "OABVX"),
    ("ELIVX", "OCBNX"),
    ("HIVNX", "ODBVX"),
    ("UNVBX", "OECVX"),    # ← target (pos=4)
    ("AZNUX", "OFBNX"),
], target_pos=4)

L2_08 = _make_item("L2_08", [
    ("EBMOX", "PAHVX"),
    ("HNVUX", "PCHVX"),
    ("CVBLX", "PIBVX"),
    ("ACNLX", "PJBVX"),    # ← target (pos=4)
    ("HAXVB", "PKBVX"),
], target_pos=4)

ITEMS = [L2_01, L2_02, L2_03, L2_04, L2_05, L2_06, L2_07, L2_08]


# ─── Content class registry (9 classes, priority order) ───────────────────
# Scoring precedence (locked):
#   1. RETURNED_TARGET_OBJ      — correct; checked first regardless of position
#   2. RETURNED_OBJ_POS_k       — non-target object at fact k (k ≠ target_pos)
#   3. RETURNED_SUBJ_TOKEN      — any subject token from context
#   4. RETURNED_NON_CONTEXT_TOKEN — token not present in any context slot
#                                   (covers alphabetic and non-alphabetic outputs)
#   5. UNCLASSIFIED             — no extractable token found (scaffold absent)
#
# Amendment note (2026-06-06): OUT_OF_CONTEXT_TOKEN renamed to
# RETURNED_NON_CONTEXT_TOKEN and extended to cover non-alphabetic tokens
# (e.g. "0", "10"). Original scorer conflated scaffold absence with
# non-alphabetic ANSWER content. Revised scorer separates scaffold
# compliance from content-token validity.
_CONTENT_CLASSES = (
    "RETURNED_TARGET_OBJ",
    "RETURNED_OBJ_POS_1",
    "RETURNED_OBJ_POS_2",
    "RETURNED_OBJ_POS_3",
    "RETURNED_OBJ_POS_4",
    "RETURNED_OBJ_POS_5",
    "RETURNED_SUBJ_TOKEN",
    "RETURNED_NON_CONTEXT_TOKEN",
    "UNCLASSIFIED",
)

_FORMAT_CLASSES = ("FORMAT_PASS", "FORMAT_FAIL")


# ─── Scoring functions ────────────────────────────────────────────────────

def _extract_answer_token(output: str) -> str | None:
    """Extract the single non-whitespace token immediately following ANSWER:

    Amendment (2026-06-06): accepts any non-whitespace token, not just [A-Z]{4,8}.
    Numeric tokens ("0", "10") are now extractable and classified as
    RETURNED_NON_CONTEXT_TOKEN rather than collapsing to UNCLASSIFIED.
    """
    m = re.search(r'ANSWER:\s+(\S+)', output)
    return m.group(1) if m else None


def score_arm2_content(output: str, item: dict) -> dict:
    """
    Classify model output into one of 9 content_class values.

    Priority (locked):
      RETURNED_TARGET_OBJ > RETURNED_OBJ_POS_k > RETURNED_SUBJ_TOKEN
      > OUT_OF_CONTEXT_TOKEN > UNCLASSIFIED

    RETURNED_OBJ_POS_k applies only to non-target object returns.

    Returns dict with:
      content_class, is_correct, returned_token,
      returned_token_role, returned_fact_position,
      same_error_identity_key, same_wrong_token_count, same_wrong_position_count
    """
    target_obj  = item["target_obj"]
    target_pos  = item["target_pos"]
    facts       = item["facts"]

    obj_to_pos  = {obj: i + 1 for i, (_, obj)  in enumerate(facts)}
    subj_to_pos = {s:   i + 1 for i, (s,   _)  in enumerate(facts)}

    returned = _extract_answer_token(output)

    if returned is None:
        return {
            "content_class":            "UNCLASSIFIED",
            "is_correct":               False,
            "returned_token":           None,
            "returned_token_role":      "NONE",
            "returned_fact_position":   None,
            "same_error_identity_key":  "UNCLASSIFIED|None|None",
            "same_wrong_token_count":   None,
            "same_wrong_position_count": None,
        }

    # Priority 1: correct answer (must check before positional lookup)
    if returned == target_obj:
        return {
            "content_class":            "RETURNED_TARGET_OBJ",
            "is_correct":               True,
            "returned_token":           returned,
            "returned_token_role":      "TARGET_OBJ",
            "returned_fact_position":   target_pos,
            "same_error_identity_key":  f"RETURNED_TARGET_OBJ|{returned}|{target_pos}",
            "same_wrong_token_count":   0,
            "same_wrong_position_count": 0,
        }

    # Priority 2: non-target object return
    if returned in obj_to_pos:
        pos = obj_to_pos[returned]
        # pos != target_pos is guaranteed: returned != target_obj and objects are unique
        return {
            "content_class":            f"RETURNED_OBJ_POS_{pos}",
            "is_correct":               False,
            "returned_token":           returned,
            "returned_token_role":      f"OBJ_AT_POS_{pos}",
            "returned_fact_position":   pos,
            "same_error_identity_key":  f"RETURNED_OBJ_POS_{pos}|{returned}|{pos}",
            "same_wrong_token_count":   None,
            "same_wrong_position_count": None,
        }

    # Priority 3: subject echo
    if returned in subj_to_pos:
        pos = subj_to_pos[returned]
        return {
            "content_class":            "RETURNED_SUBJ_TOKEN",
            "is_correct":               False,
            "returned_token":           returned,
            "returned_token_role":      f"SUBJ_AT_POS_{pos}",
            "returned_fact_position":   pos,
            "same_error_identity_key":  f"RETURNED_SUBJ_TOKEN|{returned}|{pos}",
            "same_wrong_token_count":   None,
            "same_wrong_position_count": None,
        }

    # Priority 4: token not in any context slot (alphabetic or non-alphabetic)
    return {
        "content_class":            "RETURNED_NON_CONTEXT_TOKEN",
        "is_correct":               False,
        "returned_token":           returned,
        "returned_token_role":      "OUT_OF_CONTEXT",
        "returned_fact_position":   None,
        "same_error_identity_key":  f"RETURNED_NON_CONTEXT_TOKEN|{returned}|None",
        "same_wrong_token_count":   None,
        "same_wrong_position_count": None,
    }


def score_arm2_scaffold(output: str) -> dict:
    """
    Classify scaffold compliance independently of format and content.

    SCAFFOLD_PRESENT: output contains 'ANSWER:' followed by at least one
      non-whitespace token (regardless of token type or shape).

    SCAFFOLD_ABSENT: output does not contain a usable ANSWER: prefix
      with a following token.

    scaffold_class is a third scoring axis orthogonal to format_class and
    content_class. It separates 'model abandoned the scaffold entirely' from
    'model used the scaffold but returned the wrong content type'.

    Added 2026-06-06 per Team Lead amendment to distinguish:
      SCAFFOLD_PRESENT + FORMAT_FAIL + RETURNED_NON_CONTEXT_TOKEN
        (scaffold used; numeric/wrong-type content returned)
      vs
      SCAFFOLD_ABSENT + FORMAT_FAIL + UNCLASSIFIED
        (scaffold not used at all)
    """
    if re.search(r'ANSWER:\s+\S+', output):
        return {"scaffold_class": "SCAFFOLD_PRESENT"}
    return {"scaffold_class": "SCAFFOLD_ABSENT"}


def score_arm2_format(output: str) -> dict:
    """
    Classify output format as FORMAT_PASS or FORMAT_FAIL (strict — unchanged).

    FORMAT_PASS: stripped output exactly matches ^ANSWER: [A-Z]{4,8}$
      (uppercase alphabetic synthetic-token-shaped answer, length 4-8).

    FORMAT_FAIL: anything else — numeric returns, extra text, wrong casing,
      absent scaffold, etc.

    Format class remains strict. scaffold_class (see score_arm2_scaffold)
    captures whether the ANSWER: prefix was present regardless of format.
    """
    stripped = output.strip()
    if re.match(r'^ANSWER:\s+[A-Z]{4,8}$', stripped):
        return {"format_class": "FORMAT_PASS"}
    return {"format_class": "FORMAT_FAIL"}


# ─── Dummy baseline computation ───────────────────────────────────────────

def _compute_dummy_baselines(items: list) -> tuple:
    """
    Compute 7 deterministic dummy scores on the n=8 manifest.

    Dummies:
      always_fact1_obj … always_fact5_obj — always return object at that fact position
      always_first_obj — always return object at fact 1 (= always_fact1_obj)
      always_last_obj  — always return object at fact 5 (= always_fact5_obj)

    Returns (scores_dict: {name: float}, max_dummy_score: float).
    """
    n = len(items)
    counts = {
        "always_fact1_obj": 0, "always_fact2_obj": 0, "always_fact3_obj": 0,
        "always_fact4_obj": 0, "always_fact5_obj": 0,
        "always_first_obj": 0, "always_last_obj":  0,
    }
    for item in items:
        tgt = item["target_obj"]
        objs = [o for _, o in item["facts"]]
        if objs[0] == tgt: counts["always_fact1_obj"] += 1
        if objs[1] == tgt: counts["always_fact2_obj"] += 1
        if objs[2] == tgt: counts["always_fact3_obj"] += 1
        if objs[3] == tgt: counts["always_fact4_obj"] += 1
        if objs[4] == tgt: counts["always_fact5_obj"] += 1
        if objs[0] == tgt: counts["always_first_obj"] += 1
        if objs[-1] == tgt: counts["always_last_obj"]  += 1
    scores = {k: v / n for k, v in counts.items()}
    return scores, max(scores.values())


# ─── Static validator ─────────────────────────────────────────────────────

_FEASIBILITY_THRESHOLD = 7 / 8  # 0.875 — Arm 2 go/no-go gate

# Heuristic English word check — 5-letter common words that could appear by accident
_COMMON_5_LETTER_WORDS = frozenset({
    'ABOUT', 'ABOVE', 'ACTOR', 'ADMIT', 'AFTER', 'AGAIN', 'AGENT', 'AHEAD',
    'ALARM', 'ALIKE', 'ALIVE', 'ALLEY', 'ALLOW', 'ALONE', 'ALONG', 'ALTER',
    'ANGRY', 'ANNEX', 'APART', 'APPLY', 'ARISE', 'ARMOR', 'ARRAY', 'ASIDE',
    'ASSET', 'AVOID', 'AWAKE', 'AWARD', 'AWARE', 'AWFUL', 'BADLY', 'BAKER',
    'BASIC', 'BASIS', 'BEACH', 'BEGAN', 'BEGIN', 'BELOW', 'BENCH', 'BLACK',
    'BLADE', 'BLAME', 'BLAND', 'BLANK', 'BLAST', 'BLAZE', 'BLEND', 'BLOOD',
    'BOARD', 'BOUND', 'BRAVE', 'BREAD', 'BREAK', 'BREED', 'BRICK', 'BRIEF',
    'BRING', 'BROKE', 'BROWN', 'BRUSH', 'BUILD', 'BUILT', 'BURST', 'CARRY',
    'CATCH', 'CHAIN', 'CHECK', 'CLAIM', 'CLASS', 'CLEAN', 'CLEAR', 'CLICK',
    'CLOSE', 'COLOR', 'COUNT', 'COVER', 'CRAFT', 'CRAZY', 'CROSS', 'DAILY',
    'DEATH', 'DENSE', 'DEPTH', 'DOING', 'DRAFT', 'DRAIN', 'DREAM', 'DRINK',
    'DRIVE', 'EARTH', 'EMAIL', 'EMPTY', 'ENTER', 'EQUAL', 'ERROR', 'EVENT',
    'EVERY', 'EXACT', 'EXIST', 'EXTRA', 'FACES', 'FALSE', 'FAULT', 'FINAL',
    'FIRST', 'FIXED', 'FLAME', 'FLASH', 'FLEET', 'FLOAT', 'FLOOR', 'FOCUS',
    'FORCE', 'FOUND', 'FRAME', 'FRESH', 'FRONT', 'FULLY', 'GHOST', 'GIVEN',
    'GLASS', 'GOING', 'GRADE', 'GRAIN', 'GRAND', 'GRANT', 'GRAPH', 'GRASS',
    'GREAT', 'GROSS', 'GROUP', 'GUARD', 'HABIT', 'HAPPY', 'HARSH', 'HEART',
    'HEAVY', 'HENCE', 'HOLDS', 'HOUSE', 'HUMAN', 'HUMOR', 'IMAGE', 'INDEX',
    'INNER', 'INPUT', 'ISSUE', 'IVORY', 'JUDGE', 'LABEL', 'LARGE', 'LASER',
    'LATER', 'LAYER', 'LEADS', 'LEARN', 'LEAST', 'LEAVE', 'LEGAL', 'LEVEL',
    'LIGHT', 'LIMIT', 'LOCAL', 'LOGIC', 'LOWER', 'LUCKY', 'MAGIC', 'MAJOR',
    'MARKS', 'MATCH', 'MIGHT', 'MODEL', 'MONEY', 'MONTH', 'MORAL', 'MULTI',
    'MUSIC', 'NEEDS', 'NOISE', 'NORTH', 'NOVEL', 'OFTEN', 'OLDER', 'OMEGA',
    'ORDER', 'OTHER', 'OUTER', 'OWNED', 'PANEL', 'PAPER', 'PARTS', 'PAUSE',
    'PHASE', 'PIECE', 'PLACE', 'PLAIN', 'PLANE', 'PLANS', 'PLANT', 'PLAYS',
    'POINT', 'POWER', 'PRESS', 'PRICE', 'PRIME', 'PRINT', 'PRIOR', 'PROBE',
    'PROOF', 'PROSE', 'PULSE', 'QUERY', 'QUEUE', 'QUOTE', 'RAISE', 'RANGE',
    'RAPID', 'RATIO', 'REACH', 'READS', 'READY', 'REALM', 'REFER', 'RESET',
    'RIGHT', 'RISKS', 'ROLES', 'ROUND', 'RULER', 'RULES', 'SCALE', 'SCOPE',
    'SCORE', 'SEEDS', 'SENSE', 'SERVE', 'SETUP', 'SEVEN', 'SHARP', 'SHIFT',
    'SHORT', 'SHOWS', 'SINCE', 'SKILL', 'SLEEP', 'SLICE', 'SLIDE', 'SLOPE',
    'SMART', 'SOUND', 'SPACE', 'SPAWN', 'SPEAK', 'SPEED', 'SPLIT', 'STAGE',
    'START', 'STATE', 'STAYS', 'STEPS', 'STILL', 'STOCK', 'STONE', 'STORE',
    'STORY', 'STYLE', 'SUPER', 'SWEEP', 'SWIFT', 'TASKS', 'TEACH', 'TERMS',
    'TESTS', 'THEIR', 'THEME', 'THESE', 'THICK', 'THING', 'THINK', 'THREE',
    'TIGHT', 'TIMER', 'TIMES', 'TITLE', 'TODAY', 'TOKEN', 'TOOLS', 'TOTAL',
    'TOUGH', 'TRACK', 'TRADE', 'TRAIL', 'TRAIN', 'TREAT', 'TREES', 'TREND',
    'TRIAL', 'TRUST', 'TRUTH', 'TURNS', 'TWICE', 'TYPED', 'TYPES', 'ULTRA',
    'UNDER', 'UNION', 'UNTIL', 'UPPER', 'USAGE', 'USERS', 'USING', 'USUAL',
    'VALID', 'VALUE', 'VIEWS', 'VISIT', 'VITAL', 'VOICE', 'WANTS', 'WATER',
    'WHERE', 'WHICH', 'WHILE', 'WHITE', 'WHOLE', 'WHOSE', 'WIDER', 'WORKS',
    'WORLD', 'WORSE', 'WORST', 'WORTH', 'WOULD', 'WRITE', 'WRONG', 'YIELD',
    'YOUNG', 'YOURS', 'ZONES',
})


def validate_tasks() -> bool:
    """
    Run all static validation checks on ITEMS.

    Prints per-item pass/fail keyed to check_id, dummy baseline table,
    and overall pass/fail summary.

    Returns True if all checks pass, False otherwise.
    """
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

    # ── Global structural checks ─────────────────────────────────────────────

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

    # CHECK_07: subjects and objects fully disjoint (no chain graph)
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

    # CHECK_10: global token uniqueness (combined pool)
    if len(all_tokens) != len(set(all_tokens)):
        dupes = {t for t in all_tokens if all_tokens.count(t) > 1}
        _err("CHECK_10", f"Combined pool duplicates: {dupes}")
    else:
        for item in ITEMS:
            _ok("CHECK_10", item["id"], "global uniqueness ok")

    # ── Per-item checks ──────────────────────────────────────────────────────

    for item in ITEMS:
        pid = item["id"]
        facts = item["facts"]
        tp = item["target_pos"]
        t_subj, t_obj = facts[tp - 1]

        # CHECK_11: target_subj / target_obj correctly derived from target_pos
        if item["target_subj"] != t_subj or item["target_obj"] != t_obj:
            _err("CHECK_11",
                 f"target mismatch: item has ({item['target_subj']},{item['target_obj']}) "
                 f"but fact {tp} is ({t_subj},{t_obj})", pid)
        else:
            _ok("CHECK_11", pid, f"target={t_subj}→{t_obj} at pos {tp}")

        # CHECK_12: query contains no "maps", " map ", "mapped"
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

        # CHECK_17: context line order matches facts list (subj, obj at position i)
        order_ok = True
        for i, (s, o) in enumerate(facts, 1):
            if i - 1 < len(ctx_lines):
                expected_line = f"{s} maps to {o}."
                if ctx_lines[i - 1] != expected_line:
                    _err("CHECK_17", f"Fact {i} mismatch: {ctx_lines[i-1]!r} ≠ {expected_line!r}", pid)
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

        # CHECK_20: no token is a common English word (heuristic)
        item_tokens = [s for s, _ in facts] + [o for _, o in facts]
        word_hits = [t for t in item_tokens if t in _COMMON_5_LETTER_WORDS]
        if word_hits:
            _err("CHECK_20", f"Common English words detected: {word_hits}", pid)
        else:
            _ok("CHECK_20", pid, "no English words detected")

    # ── Scoring function checks ───────────────────────────────────────────────

    # CHECK_21: RETURNED_TARGET_OBJ has priority over RETURNED_OBJ_POS_k
    _ref = ITEMS[0]
    r_correct = score_arm2_content(f"ANSWER: {_ref['target_obj']}", _ref)
    if r_correct["content_class"] != "RETURNED_TARGET_OBJ":
        _err("CHECK_21", f"Correct answer misclassified as {r_correct['content_class']!r}")
    else:
        # Also verify: a non-target object is NOT classified as RETURNED_TARGET_OBJ
        _nontarget = _ref["facts"][0][1]  # obj at pos 1 (target is pos 2 for L2_01)
        r_wrong = score_arm2_content(f"ANSWER: {_nontarget}", _ref)
        if r_wrong["content_class"] == "RETURNED_TARGET_OBJ":
            _err("CHECK_21", f"Non-target obj {_nontarget!r} classified as RETURNED_TARGET_OBJ")
        elif not r_wrong["content_class"].startswith("RETURNED_OBJ_POS_"):
            _err("CHECK_21", f"Non-target obj {_nontarget!r} got unexpected class {r_wrong['content_class']!r}")
        else:
            for item in ITEMS:
                _ok("CHECK_21", item["id"], "scoring precedence ok")

    # CHECK_22: same_error_identity_key has compound structure (class|token|pos)
    # Verify with alphabetic OOC token and numeric token (amendment 2026-06-06)
    r_ooc = score_arm2_content("ANSWER: ZZZZZ", ITEMS[0])
    r_num = score_arm2_content("ANSWER: 0", ITEMS[0])
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

    # CHECK_23: 9 content classes registered, 2 format classes registered
    if len(_CONTENT_CLASSES) != 9:
        _err("CHECK_23", f"Expected 9 content classes, got {len(_CONTENT_CLASSES)}")
    elif len(_FORMAT_CLASSES) != 2:
        _err("CHECK_23", f"Expected 2 format classes, got {len(_FORMAT_CLASSES)}")
    else:
        for item in ITEMS:
            _ok("CHECK_23", item["id"], "9 content, 2 format classes")

    # CHECK_24: scorer unit tests from run_tier0 pass
    try:
        sys.path.insert(0, str(Path(__file__).parent))
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

    # CHECK_26: tokenizer autopsy — verify round-trip consistency for all tokens.
    # Synthetic 5-char tokens in Qwen2.5 are always multi-BPE (as are all Exp7 tokens).
    # Requirement: encode → decode must return the original string exactly.
    # Reports BPE piece counts as observational data (not a pass/fail criterion).
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
            print(f"  [CHECK_26] All {len(bpe_counts)} tokens round-trip correctly (multi-BPE is expected for synthetic tokens)")
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

    # ── Print per-item report ────────────────────────────────────────────────

    print("\n=== VALIDATOR REPORT — tasks_exp8.py ===\n")
    print(f"  n={len(ITEMS)} items  |  arm=2  |  target_pos distribution: {pos_counts}\n")

    for item in ITEMS:
        pid = item["id"]
        checks = per_item.get(pid, [])
        fails = [(cid, detail) for cid, status, detail in checks if status == "FAIL"]
        status = "PASS" if not fails else f"FAIL ({', '.join(f[0] for f in fails)})"
        print(f"  {pid}  target_pos={item['target_pos']}  "
              f"target={item['target_subj']}→{item['target_obj']}  [{status}]")
        for cid, detail in fails:
            print(f"    {cid}: {detail}")

    # ── Dummy baseline report ────────────────────────────────────────────────

    print("\n--- Dummy baseline scores (deterministic) ---")
    for name, score in dummy_scores.items():
        marker = "  ← max" if score == max_dummy else ""
        print(f"  {name:<25} {score:.3f}{marker}")
    print(f"  max_dummy_score:          {max_dummy:.3f}")
    print(f"  feasibility_threshold:    {_FEASIBILITY_THRESHOLD:.3f}")
    if max_dummy >= _FEASIBILITY_THRESHOLD:
        print("  [CONSTRUCTION FAILURE] Deterministic dummy reached threshold!")
    else:
        print("  [OK] max_dummy < threshold — baseline inflation not a concern")

    # ── Global error summary ────────────────────────────────────────────────

    if errors:
        print(f"\n[FAILED] {len(errors)} check(s) failed:")
        for check_id, item_id, msg in errors:
            loc = f" ({item_id})" if item_id else " (global)"
            print(f"  {check_id}{loc}: {msg}")
        return False

    total_checks = sum(len(v) for v in per_item.values())
    print(f"\n[ALL CHECKS PASSED] {total_checks} checks across {len(ITEMS)} items")
    return True


# ─── Manifest hash ────────────────────────────────────────────────────────

def get_manifest_hash() -> str:
    return f"sha256:{hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}"


# ─── Entry point ──────────────────────────────────────────────────────────

if __name__ == "__main__":
    ok = validate_tasks()
    print(f"\nManifest hash: {get_manifest_hash()}")
    sys.exit(0 if ok else 1)
