"""
Two-hop Constructibility Level-1 — deterministic scorer.
Stage 0 instrument.

FAILURE_TAXONOMY_VERSION = "v1.0"

Priority order (approved + anchor_echo correction — see implementation note):
  1. format_scaffold_failure
  2. non_context_return
  3. correct_chain_stopped_short   (composite only)
  4. anchor_echo                   (before wrong_neighbor — see note)
  5. wrong_chain_selection
  6. target_chain_wrong_neighbor
  7. UNCLASSIFIED_OFF_FRAME

Implementation note — anchor_echo priority correction:
  The approved residual priority order placed anchor_echo at position 6 (after
  wrong_neighbor at position 5). For target-chain objects, wrong_neighbor always
  fires first under that order, making anchor_echo unreachable for anchor_A returns
  on composite/hop2 queries. anchor_echo is the more specific classification and
  must precede wrong_neighbor. Corrected to position 4. Flagged to Team Lead.
"""

import re
import hashlib
from pathlib import Path
from typing import Optional

FAILURE_TAXONOMY_VERSION = "v1.0"

# ── Role tags (must match tasks_twohop_l1.py) ─────────────────────────────────
ROLE_ANSWER_C                      = "answer_C"
ROLE_HOP1_B                        = "hop1_B"
ROLE_ANCHOR_A                      = "anchor_A"
ROLE_TARGET_NEIGHBOR_DECOY         = "target_neighbor_decoy"
ROLE_DISTRACTOR_CHAIN_ENDPOINT     = "distractor_chain_endpoint"
ROLE_DISTRACTOR_CHAIN_INTERMEDIATE = "distractor_chain_intermediate"
ROLE_INERT_FILLER                  = "inert_filler"
ROLE_OTHER_CONTEXT                 = "other_context"
ROLE_NULL_NO_LINK                  = "null_no_link"

TARGET_CHAIN_ROLES = {ROLE_ANSWER_C, ROLE_HOP1_B, ROLE_ANCHOR_A}
DECOY_CHAIN_ROLES  = {ROLE_DISTRACTOR_CHAIN_ENDPOINT, ROLE_DISTRACTOR_CHAIN_INTERMEDIATE}

# ── Failure class constants ───────────────────────────────────────────────────
FC_CORRECT         = "correct"
FC_FORMAT_SCAFFOLD = "format_scaffold_failure"
FC_NON_CONTEXT     = "non_context_return"
FC_STOPPED_SHORT   = "correct_chain_stopped_short"
FC_ANCHOR_ECHO     = "anchor_echo"
FC_WRONG_CHAIN     = "wrong_chain_selection"
FC_WRONG_NEIGHBOR  = "target_chain_wrong_neighbor"
FC_UNCLASSIFIED    = "UNCLASSIFIED_OFF_FRAME"

ALL_FAILURE_CLASSES = {
    FC_CORRECT, FC_FORMAT_SCAFFOLD, FC_NON_CONTEXT, FC_STOPPED_SHORT,
    FC_ANCHOR_ECHO, FC_WRONG_CHAIN, FC_WRONG_NEIGHBOR, FC_UNCLASSIFIED,
}

# ── Query type constants ──────────────────────────────────────────────────────
QT_HOP1           = "hop1"
QT_HOP2           = "hop2"
QT_COMPOSITE      = "composite"
QT_NEG_GRAPH      = "negative_graph"
QT_LENGTH_MATCHED = "length_matched"

# ── Output contract ───────────────────────────────────────────────────────────
_SCAFFOLD  = "ANSWER:"
_FORMAT_RE = re.compile(r'^ANSWER:\s+[A-Z]{4,8}$')
_NULL_TOKENS = {"NULL"}


# ── Contract and format scoring ───────────────────────────────────────────────
def score_scaffold(output: str) -> str:
    if _SCAFFOLD in output and len(output.split(_SCAFFOLD, 1)[1].strip()) > 0:
        return "SCAFFOLD_PRESENT"
    return "SCAFFOLD_ABSENT"


def score_format(output: str) -> str:
    return "FORMAT_PASS" if _FORMAT_RE.match(output.strip()) else "FORMAT_FAIL"


def _extract_answer_token(output: str) -> Optional[str]:
    s = output.strip()
    if _FORMAT_RE.match(s):
        return s.split(None, 1)[1]
    return None


# ── Manifest lookup helpers ───────────────────────────────────────────────────
def get_object_role(token: str, item: dict) -> Optional[str]:
    return item.get("object_roles", {}).get(token)


def get_query_anchor(item: dict, query_type: str) -> Optional[str]:
    return item.get("queries", {}).get(query_type, {}).get("query_anchor")


def get_target_B(item: dict) -> Optional[str]:
    for chain in item.get("chains", []):
        if chain.get("role") == "target":
            return chain.get("B_object")
    return None


# ── Priority-order classifier ─────────────────────────────────────────────────
def classify_output(raw_output: str, item: dict, query_type: str) -> dict:
    """
    Classify a single raw model output against the item manifest.
    Returns a dict with failure_class, scaffold_class, format_class,
    returned_token, returned_role, is_correct.

    Priority order:
      1. format_scaffold_failure
      2. non_context_return
      3. correct_chain_stopped_short  (composite only)
      4. anchor_echo                  (corrected: before wrong_neighbor)
      5. wrong_chain_selection
      6. target_chain_wrong_neighbor
      7. UNCLASSIFIED_OFF_FRAME
    """
    stripped = raw_output.strip()
    scaffold_class = score_scaffold(raw_output)

    # 1. Format / scaffold check
    if not _FORMAT_RE.match(stripped):
        return {
            "failure_class":  FC_FORMAT_SCAFFOLD,
            "scaffold_class": scaffold_class,
            "format_class":   "FORMAT_FAIL",
            "returned_token": None,
            "returned_role":  None,
            "is_correct":     False,
        }

    token = stripped.split(None, 1)[1]
    expected = item["queries"][query_type]["expected_answer"]
    is_null = token in _NULL_TOKENS
    role = get_object_role(token, item)

    def _result(fc, ret_role=role):
        return {
            "failure_class":  fc,
            "scaffold_class": scaffold_class,
            "format_class":   "FORMAT_PASS",
            "returned_token": token,
            "returned_role":  ret_role,
            "is_correct":     fc == FC_CORRECT,
        }

    # 2. Correct
    if token == expected:
        ret_role = ROLE_NULL_NO_LINK if is_null else role
        return _result(FC_CORRECT, ret_role)

    # 3. Non-context: token not in registry and not a NULL token
    #    Also catches NULL returned on a non-negative-graph query
    if is_null and query_type != QT_NEG_GRAPH:
        return _result(FC_NON_CONTEXT, ROLE_NULL_NO_LINK)
    if not is_null and role is None:
        return _result(FC_NON_CONTEXT, None)

    # 4. Stopped-short: composite only, returns B_target
    if query_type == QT_COMPOSITE:
        b_target = get_target_B(item)
        if b_target and token == b_target:
            return _result(FC_STOPPED_SHORT)

    # 5. Anchor echo (corrected priority: before wrong_neighbor)
    anchor = get_query_anchor(item, query_type)
    if anchor and token == anchor:
        return _result(FC_ANCHOR_ECHO)

    # 6. Wrong-chain selection
    if role in DECOY_CHAIN_ROLES:
        return _result(FC_WRONG_CHAIN)

    # 7. Target-chain wrong-neighbor (includes target_neighbor_decoy)
    if role in TARGET_CHAIN_ROLES or role == ROLE_TARGET_NEIGHBOR_DECOY:
        return _result(FC_WRONG_NEIGHBOR)

    # 8. UNCLASSIFIED
    return _result(FC_UNCLASSIFIED)


# ── Uniform-random-expected (query-role-conditioned) ──────────────────────────
def compute_uniform_random_expected(item: dict, query_type: str) -> Optional[float]:
    """
    Denominator = count of eligible answer-role objects for this query type.

    hop1:          hop1_B + distractor_chain_intermediate objects
    hop2:          answer_C + distractor_chain_endpoint objects
    composite:     answer_C + distractor_chain_endpoint objects
    negative_graph: answer_C + distractor_chain_endpoint + 1 for NULL
    length_matched: N/A → None

    Excludes: anchor_A, inert_filler, target_neighbor_decoy, other_context.
    """
    if query_type == QT_LENGTH_MATCHED:
        return None

    roles = item.get("object_roles", {})

    if query_type == QT_HOP1:
        n = sum(1 for r in roles.values()
                if r in (ROLE_HOP1_B, ROLE_DISTRACTOR_CHAIN_INTERMEDIATE))
    elif query_type in (QT_HOP2, QT_COMPOSITE):
        n = sum(1 for r in roles.values()
                if r in (ROLE_ANSWER_C, ROLE_DISTRACTOR_CHAIN_ENDPOINT))
    elif query_type == QT_NEG_GRAPH:
        n = sum(1 for r in roles.values()
                if r in (ROLE_ANSWER_C, ROLE_DISTRACTOR_CHAIN_ENDPOINT)) + 1
    else:
        return None

    return round(1.0 / n, 6) if n > 0 else None


# ── Dummy baseline scores ─────────────────────────────────────────────────────
def _c_objects_by_context_position(item: dict) -> list:
    """Return C-role objects sorted by position of their introducing hop2 fact."""
    chains = item.get("chains", [])
    facts = item.get("context", {}).get("ordered_facts", [])
    chain_map = {c["chain_id"]: c for c in chains}

    c_pos = {}
    for f in facts:
        if f.get("fact_role") in ("hop2", "hop2_fact", "decoy_hop2_fact"):
            chain = chain_map.get(f.get("chain_id"), {})
            c_obj = chain.get("C_object")
            if c_obj:
                pos = f.get("position_index", 9999)
                if c_obj not in c_pos or pos < c_pos[c_obj]:
                    c_pos[c_obj] = pos

    return [obj for obj, _ in sorted(c_pos.items(), key=lambda x: x[1])]


def compute_dummy_baseline_scores(item: dict, query_type: str) -> dict:
    """
    Expected score for each approved dummy baseline under this item/query.
    Score is 1.0 if the dummy answer matches expected_answer, else 0.0.
    uniform_random_expected is the closed-form chance score.

    Amendment 2026-06-08 (Cell03 scorer amendment, Manager-authorized):
      Added ceiling-bearing: always_return_second_C, always_return_third_C
      Added reference-only:  always_return_ct
      already_return_NULL:   already present; reference-only status documented
      Disambiguation rule:   _c_objects_by_context_position() uses earliest
                             position_index if a C-object appears in multiple
                             hop2-type facts (defensive; not expected in practice).
      R = 3 for Two-Hop L1: third_C == last_C; both reported explicitly.
    """
    expected = item["queries"][query_type]["expected_answer"]
    chains = item.get("chains", [])

    def score(ans):
        return 1.0 if ans == expected else 0.0

    target_chain = next((c for c in chains if c.get("role") == "target"), {})
    decoy_chains  = [c for c in chains if c.get("role") == "decoy"]

    b_target  = target_chain.get("B_object")
    anchor_a  = target_chain.get("A_object")
    c_target  = target_chain.get("C_object")
    c_by_pos  = _c_objects_by_context_position(item)

    baselines = {
        "always_return_B_target":  score(b_target),
        "always_return_anchor_A":  score(anchor_a),
        "always_return_first_C":   score(c_by_pos[0])  if c_by_pos else 0.0,
        "always_return_second_C":  score(c_by_pos[1])  if len(c_by_pos) >= 2 else 0.0,
        "always_return_third_C":   score(c_by_pos[2])  if len(c_by_pos) >= 3 else 0.0,
        "always_return_last_C":    score(c_by_pos[-1]) if c_by_pos else 0.0,
        "always_return_ct":        score(c_target),
        "always_return_NULL":      score("NULL"),
        "uniform_random_expected": compute_uniform_random_expected(item, query_type),
    }

    for i, decoy in enumerate(decoy_chains, start=1):
        baselines[f"always_return_C_decoy_{i}"] = score(decoy.get("C_object"))

    return baselines


# ── Scorer hash ───────────────────────────────────────────────────────────────
def get_scorer_hash() -> str:
    return "sha256:" + hashlib.sha256(Path(__file__).read_bytes()).hexdigest()


# ── Unit tests ────────────────────────────────────────────────────────────────
_TEST_ITEM = {
    "item_id": "UNIT_01",
    "chains": [
        {"chain_id": "target",  "role": "target",
         "A_object": "ARVUX", "B_object": "BMNIX", "C_object": "CPQVX"},
        {"chain_id": "decoy_1", "role": "decoy",
         "A_object": "DXQNV", "B_object": "EJMRX", "C_object": "FVPLX"},
    ],
    "object_roles": {
        "ARVUX": ROLE_ANCHOR_A,
        "BMNIX": ROLE_HOP1_B,
        "CPQVX": ROLE_ANSWER_C,
        "DXQNV": ROLE_OTHER_CONTEXT,               # decoy chain A-position (source)
        "EJMRX": ROLE_DISTRACTOR_CHAIN_INTERMEDIATE,   # decoy chain B-position
        "FVPLX": ROLE_DISTRACTOR_CHAIN_ENDPOINT,
        "CPQWX": ROLE_TARGET_NEIGHBOR_DECOY,
        "NULL":  ROLE_NULL_NO_LINK,
    },
    "queries": {
        QT_HOP1:      {"expected_answer": "BMNIX", "query_anchor": "ARVUX"},
        QT_HOP2:      {"expected_answer": "CPQVX", "query_anchor": "BMNIX"},
        QT_COMPOSITE: {"expected_answer": "CPQVX", "query_anchor": "ARVUX"},
        QT_NEG_GRAPH: {"expected_answer": "NULL",  "query_anchor": "ARVUX"},
    },
    "context": {"ordered_facts": []},
}

_UNIT_CASES = [
    # (raw_output, query_type, expected_failure_class, description)
    ("ANSWER: CPQVX", QT_COMPOSITE, FC_CORRECT,         "composite correct"),
    ("ANSWER: BMNIX", QT_HOP1,      FC_CORRECT,         "hop1 correct"),
    ("ANSWER: CPQVX", QT_HOP2,      FC_CORRECT,         "hop2 correct"),
    ("ANSWER: NULL",  QT_NEG_GRAPH, FC_CORRECT,         "negative graph NULL correct"),
    ("XONBX",         QT_COMPOSITE, FC_FORMAT_SCAFFOLD,  "no scaffold prefix"),
    ("ANSWER: ZZZQX", QT_COMPOSITE, FC_NON_CONTEXT,     "token not in context"),
    ("ANSWER: NULL",  QT_COMPOSITE, FC_NON_CONTEXT,     "NULL on positive query"),
    ("ANSWER: BMNIX", QT_COMPOSITE, FC_STOPPED_SHORT,   "composite stopped-short"),
    ("ANSWER: ARVUX", QT_COMPOSITE, FC_ANCHOR_ECHO,     "composite anchor echo (A)"),
    ("ANSWER: ARVUX", QT_HOP1,      FC_ANCHOR_ECHO,     "hop1 anchor echo (A)"),
    ("ANSWER: BMNIX", QT_HOP2,      FC_ANCHOR_ECHO,     "hop2 anchor echo (B is anchor)"),
    ("ANSWER: FVPLX", QT_COMPOSITE, FC_WRONG_CHAIN,     "decoy chain endpoint"),
    ("ANSWER: EJMRX", QT_COMPOSITE, FC_WRONG_CHAIN,     "decoy chain intermediate"),
    ("ANSWER: CPQWX", QT_COMPOSITE, FC_WRONG_NEIGHBOR,  "target neighbor decoy"),
]


def run_unit_tests() -> bool:
    passed, failed = 0, 0
    for raw, qt, expected_fc, desc in _UNIT_CASES:
        result = classify_output(raw, _TEST_ITEM, qt)
        actual_fc = result["failure_class"]
        if actual_fc == expected_fc:
            passed += 1
        else:
            print(f"  FAIL [{desc}]: expected {expected_fc!r}, got {actual_fc!r}")
            failed += 1
    print(f"Unit tests: {passed}/{len(_UNIT_CASES)} passed")
    if failed:
        raise AssertionError(f"{failed} unit test(s) failed")
    return True


# ── Dummy-baseline test fixtures (amendment 2026-06-08) ───────────────────────
# Fixture_A: ct at rank 2 (second_C = ct)
# c_by_pos = ["FVPLX"(pos2), "CPQVX"(pos6), "IMNCX"(pos7)]
_TEST_ITEM_DUMMY_A = {
    "item_id": "UNIT_DUMMY_A",
    "chains": [
        {"chain_id": "decoy_1", "role": "decoy",
         "A_object": "DXQNV", "B_object": "EJMRX", "C_object": "FVPLX"},
        {"chain_id": "target",  "role": "target",
         "A_object": "ARVUX", "B_object": "BMNIX", "C_object": "CPQVX"},
        {"chain_id": "decoy_2", "role": "decoy",
         "A_object": "GVPQX", "B_object": "HJKLX", "C_object": "IMNCX"},
    ],
    "queries": {
        QT_HOP1:      {"expected_answer": "BMNIX", "query_anchor": "ARVUX"},
        QT_HOP2:      {"expected_answer": "CPQVX", "query_anchor": "BMNIX"},
        QT_COMPOSITE: {"expected_answer": "CPQVX", "query_anchor": "ARVUX"},
        QT_NEG_GRAPH: {"expected_answer": "NULL",  "query_anchor": "ARVUX"},
    },
    "context": {"ordered_facts": [
        {"fact_role": "decoy_hop2_fact", "chain_id": "decoy_1", "position_index": 2},
        {"fact_role": "hop2",            "chain_id": "target",  "position_index": 6},
        {"fact_role": "decoy_hop2_fact", "chain_id": "decoy_2", "position_index": 7},
    ]},
}

# Fixture_B: ct at rank 1 (first_C = ct)
# c_by_pos = ["CPQVX"(pos2), "FVPLX"(pos5), "IMNCX"(pos7)]
_TEST_ITEM_DUMMY_B = {
    "item_id": "UNIT_DUMMY_B",
    "chains": [
        {"chain_id": "target",  "role": "target",
         "A_object": "ARVUX", "B_object": "BMNIX", "C_object": "CPQVX"},
        {"chain_id": "decoy_1", "role": "decoy",
         "A_object": "DXQNV", "B_object": "EJMRX", "C_object": "FVPLX"},
        {"chain_id": "decoy_2", "role": "decoy",
         "A_object": "GVPQX", "B_object": "HJKLX", "C_object": "IMNCX"},
    ],
    "queries": {
        QT_HOP1:      {"expected_answer": "BMNIX", "query_anchor": "ARVUX"},
        QT_HOP2:      {"expected_answer": "CPQVX", "query_anchor": "BMNIX"},
        QT_COMPOSITE: {"expected_answer": "CPQVX", "query_anchor": "ARVUX"},
        QT_NEG_GRAPH: {"expected_answer": "NULL",  "query_anchor": "ARVUX"},
    },
    "context": {"ordered_facts": [
        {"fact_role": "hop2",            "chain_id": "target",  "position_index": 2},
        {"fact_role": "decoy_hop2_fact", "chain_id": "decoy_1", "position_index": 5},
        {"fact_role": "decoy_hop2_fact", "chain_id": "decoy_2", "position_index": 7},
    ]},
}

_DUMMY_BASELINE_CASES = [
    # (item, query_type, dummy_key, expected_score, description)
    (_TEST_ITEM_DUMMY_A, QT_COMPOSITE, "always_return_second_C", 1.0,
     "T_new_1: second_C functionality — ct at rank 2, composite"),
    (_TEST_ITEM_DUMMY_B, QT_COMPOSITE, "always_return_second_C", 0.0,
     "T_new_2: second_C tautology guard — ct at rank 1, second_C scores 0"),
    (_TEST_ITEM_DUMMY_A, QT_COMPOSITE, "always_return_third_C",  0.0,
     "T_new_3: third_C functionality — third_C=cd2 != ct"),
    (_TEST_ITEM,         QT_COMPOSITE, "always_return_third_C",  0.0,
     "T_new_4: third_C guard — empty c_by_pos, no IndexError"),
    (_TEST_ITEM_DUMMY_A, QT_HOP1,      "always_return_ct",       0.0,
     "T_new_5: always_return_ct hop1 reference — ct != bt, scores 0.0"),
    (_TEST_ITEM_DUMMY_A, QT_COMPOSITE, "always_return_ct",       1.0,
     "T_new_6: always_return_ct composite reference — trivially correct by construction"),
]


def run_dummy_baseline_tests() -> bool:
    passed, failed = 0, 0
    for item, qt, key, expected_score, desc in _DUMMY_BASELINE_CASES:
        result = compute_dummy_baseline_scores(item, qt)
        actual = result.get(key)
        if actual == expected_score:
            passed += 1
        else:
            print(f"  FAIL [{desc}]: expected {expected_score}, got {actual}")
            failed += 1
    print(f"Dummy baseline tests: {passed}/{len(_DUMMY_BASELINE_CASES)} passed")
    if failed:
        raise AssertionError(f"{failed} dummy baseline test(s) failed")
    return True


if __name__ == "__main__":
    run_unit_tests()
    run_dummy_baseline_tests()
    print(f"FAILURE_TAXONOMY_VERSION: {FAILURE_TAXONOMY_VERSION}")
    print(f"scorer_hash: {get_scorer_hash()}")
