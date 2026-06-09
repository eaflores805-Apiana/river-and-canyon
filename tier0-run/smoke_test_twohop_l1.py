"""
Stage 0 smoke test — scorer and validator correctness on hand-constructed items.
No model inference. Schema and instrument correctness only.

Run:  python3 smoke_test_twohop_l1.py
Exit: 0 = all pass, 1 = failures present
"""

import sys
from tasks_twohop_l1 import (
    validate_item, compute_context_hash, levenshtein, trigram_jaccard,
    ROLE_ANCHOR_A, ROLE_HOP1_B, ROLE_ANSWER_C,
    ROLE_DISTRACTOR_CHAIN_ENDPOINT, ROLE_DISTRACTOR_CHAIN_INTERMEDIATE,
    ROLE_TARGET_NEIGHBOR_DECOY, ROLE_NULL_NO_LINK, ROLE_OTHER_CONTEXT,
    QT_HOP1, QT_HOP2, QT_COMPOSITE, QT_NEG_GRAPH,
)
from scorer_twohop_l1 import (
    classify_output, compute_dummy_baseline_scores, compute_uniform_random_expected,
    run_unit_tests,
    FC_CORRECT, FC_STOPPED_SHORT, FC_ANCHOR_ECHO,
    FC_WRONG_CHAIN, FC_WRONG_NEIGHBOR, FC_NON_CONTEXT,
)

_passed = 0
_failed = 0


def check(label: str, condition: bool):
    global _passed, _failed
    if condition:
        _passed += 1
    else:
        print(f"  SMOKE FAIL: {label}")
        _failed += 1


# ── Minimal well-formed test item ─────────────────────────────────────────────
def make_test_item() -> dict:
    facts = [
        {"fact_id": "f1", "chain_id": "target",  "fact_role": "hop1",
         "text": "ARVUX maps_to BMNIX.", "position_index": 0,
         "token_start": 0,  "token_end": 5},
        {"fact_id": "f2", "chain_id": "decoy_1", "fact_role": "hop1",
         "text": "DXQNV maps_to EJMRX.", "position_index": 1,
         "token_start": 6,  "token_end": 11},
        {"fact_id": "f3", "chain_id": "target",  "fact_role": "hop2",
         "text": "BMNIX maps_to CPQVX.", "position_index": 2,
         "token_start": 12, "token_end": 17},
        {"fact_id": "f4", "chain_id": "decoy_1", "fact_role": "hop2",
         "text": "EJMRX maps_to FVPLX.", "position_index": 3,
         "token_start": 18, "token_end": 23},
    ]
    item = {
        "item_id": "SMOKE_01",
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
            "DXQNV": ROLE_OTHER_CONTEXT,              # decoy chain A-position (source)
            "EJMRX": ROLE_DISTRACTOR_CHAIN_INTERMEDIATE,  # decoy chain B-position
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
        "context": {
            "ordered_facts": facts,
            "total_fact_count": 4,
            "total_token_count": 80,
            "target_chain_fact_positions": [0, 2],
            "decoy_chain_fact_positions": [[1, 3]],
        },
        "positive_sufficiency_exclusion": {
            "composite_requires_hop1": True,
            "composite_requires_hop2": True,
            "answer_from_hop1_alone_possible": False,
            "answer_from_hop2_alone_possible": False,
            "validation_method": "manifest_structure",
        },
        "negative_graph_control": {
            "control_id":                    "SMOKE_01_neg",
            "negative_graph_source_cell":    "SMOKE_01",
            "removed_edge":                  "BMNIX→CPQVX",
            "valid_A_to_C_path_exists":      False,
            "independently_constructed":     True,
        },
        "same_context_controls": {
            "hop1_control_query_id":   "SMOKE_01_hop1",
            "hop2_control_query_id":   "SMOKE_01_hop2",
            "composite_query_id":      "SMOKE_01_composite",
            "only_question_differs":   True,
            "identical_context_hash":  None,  # set below
        },
        "target_neighbor_decoy": {
            "object":           "CPQWX",
            "near_miss_target": "CPQVX",
            "near_miss_metrics": {"char_edit_distance": 1, "token_overlap": 0.67},
        },
        "dummy_baselines": {
            "always_return_B_target":  {"expected_score": None},
            "always_return_anchor_A":  {"expected_score": None},
            "always_return_first_C":   {"expected_score": None},
            "always_return_last_C":    {"expected_score": None},
            "always_return_NULL":      {"expected_score": None},
            "uniform_random_expected": {"expected_score": None},
            "always_return_C_decoy_1": {"expected_score": None},
        },
    }
    item["same_context_controls"]["identical_context_hash"] = compute_context_hash(item)
    return item


def run_smoke_tests() -> bool:
    item = make_test_item()

    # ── Validator: well-formed item ───────────────────────────────────────────
    errors = validate_item(item)
    check("well-formed item validates clean", errors == [])

    # ── Context hash stability ────────────────────────────────────────────────
    recomputed = compute_context_hash(item)
    check("context_hash stable on recompute",
          recomputed == item["same_context_controls"]["identical_context_hash"])

    # ── Validator: context hash mismatch caught ───────────────────────────────
    bad_hash = dict(item)
    bad_hash["same_context_controls"] = dict(item["same_context_controls"])
    bad_hash["same_context_controls"]["identical_context_hash"] = "sha256:BADHASH"
    errs_hash = validate_item(bad_hash)
    check("context hash mismatch caught", any("mismatch" in e for e in errs_hash))

    # ── Validator: invalid positive_sufficiency caught ────────────────────────
    bad_pse = dict(item)
    bad_pse["positive_sufficiency_exclusion"] = {
        "composite_requires_hop1": True,
        "composite_requires_hop2": True,
        "answer_from_hop1_alone_possible": True,
        "answer_from_hop2_alone_possible": False,
        "validation_method": "manifest_structure",
    }
    errs_pse = validate_item(bad_pse)
    check("invalid positive_sufficiency caught", any("hop1_alone" in e for e in errs_pse))

    # ── Validator: role collision caught ──────────────────────────────────────
    # CPQWX has role target_neighbor_decoy but is also the C_object of a decoy
    # chain — these roles must be disjoint.
    bad_roles = dict(item)
    bad_roles["object_roles"] = dict(item["object_roles"])
    # Keep CPQWX as target_neighbor_decoy (original role)
    bad_roles["chains"] = [
        item["chains"][0],
        dict(item["chains"][1], **{"C_object": "CPQWX"}),  # decoy C = CPQWX
    ]
    errs_role = validate_item(bad_roles)
    check("disjoint role violation caught",
          any("disjoint" in e or "target_neighbor_decoy" in e for e in errs_role))

    # ── String metrics ────────────────────────────────────────────────────────
    check("levenshtein: identical = 0", levenshtein("CPQVX", "CPQVX") == 0)
    check("levenshtein: 1-edit = 1",    levenshtein("CPQVX", "CPQWX") == 1)
    check("levenshtein: 2-edit = 2",    levenshtein("CPQVX", "CPQWY") == 2)
    check("trigram_jaccard: identical = 1.0", trigram_jaccard("CPQVX", "CPQVX") == 1.0)
    check("trigram_jaccard: disjoint < 1.0",  trigram_jaccard("ABCDE", "XYZUV") < 1.0)
    # CPQVX / CPQWX: trigrams {CPQ,PQV,QVX} vs {CPQ,PQW,QWX}, Jaccard = 1/5 = 0.2
    check("trigram_jaccard: 1-edit has shared trigrams", trigram_jaccard("CPQVX", "CPQWX") > 0.0)

    # ── Scorer unit tests ─────────────────────────────────────────────────────
    try:
        run_unit_tests()
        check("scorer unit tests all pass", True)
    except AssertionError as e:
        check(f"scorer unit tests: {e}", False)

    # ── Dummy baselines ───────────────────────────────────────────────────────
    # Composite query: expected = CPQVX
    baselines_comp = compute_dummy_baseline_scores(item, QT_COMPOSITE)
    check("dummy always_return_B_target = 0 on composite",
          baselines_comp["always_return_B_target"] == 0.0)
    check("dummy always_return_anchor_A = 0 on composite",
          baselines_comp["always_return_anchor_A"] == 0.0)
    check("dummy always_return_NULL = 0 on composite",
          baselines_comp["always_return_NULL"] == 0.0)
    check("dummy always_return_C_decoy_1 = 0 (FVPLX != CPQVX)",
          baselines_comp.get("always_return_C_decoy_1") == 0.0)

    # first_C = CPQVX (target, position 2 in context) — should be 1.0
    # last_C  = FVPLX (decoy, position 3) — should be 0.0
    check("dummy always_return_first_C = 1.0 on composite (CPQVX first by position)",
          baselines_comp["always_return_first_C"] == 1.0)
    check("dummy always_return_last_C = 0.0 on composite (FVPLX last)",
          baselines_comp["always_return_last_C"] == 0.0)

    # ── uniform_random_expected ───────────────────────────────────────────────
    # composite: answer_C (CPQVX) + distractor_chain_endpoint (FVPLX) = 2 → 0.5
    ure_comp = compute_uniform_random_expected(item, QT_COMPOSITE)
    check("uniform_random_expected composite = 0.5", abs(ure_comp - 0.5) < 1e-6)

    # hop1: hop1_B (BMNIX) + distractor_chain_intermediate (EJMRX) = 2 → 0.5
    ure_h1 = compute_uniform_random_expected(item, QT_HOP1)
    check("uniform_random_expected hop1 = 0.5", abs(ure_h1 - 0.5) < 1e-6)

    # neg_graph: 2 C-role objects + 1 NULL = 3 → 0.333...
    ure_neg = compute_uniform_random_expected(item, QT_NEG_GRAPH)
    check("uniform_random_expected neg_graph = 1/3", abs(ure_neg - (1 / 3)) < 1e-6)

    # length_matched: None
    check("uniform_random_expected length_matched = None",
          compute_uniform_random_expected(item, "length_matched") is None)

    print(f"\nSmoke tests: {_passed}/{_passed + _failed} passed")
    return _failed == 0


if __name__ == "__main__":
    ok = run_smoke_tests()
    sys.exit(0 if ok else 1)
