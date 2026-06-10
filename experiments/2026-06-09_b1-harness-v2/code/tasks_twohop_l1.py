"""
Two-hop Constructibility Level-1 manifest schema, constants, and validator.
Stage 0 instrument — schema and validation machinery only; no items loaded.

Hashing this file pins schema version and all validation behavior.
Scorer: scorer_twohop_l1.py (separate hash, separate lock).

MANIFEST_SCHEMA_VERSION = "v1.0"
"""

import hashlib
import unicodedata
from pathlib import Path

MANIFEST_SCHEMA_VERSION = "v1.0"

# ── Object role tags (canonical set) ─────────────────────────────────────────
ROLE_ANSWER_C                      = "answer_C"
ROLE_HOP1_B                        = "hop1_B"
ROLE_ANCHOR_A                      = "anchor_A"
ROLE_TARGET_NEIGHBOR_DECOY         = "target_neighbor_decoy"
ROLE_DISTRACTOR_CHAIN_ENDPOINT     = "distractor_chain_endpoint"
ROLE_DISTRACTOR_CHAIN_INTERMEDIATE = "distractor_chain_intermediate"
ROLE_INERT_FILLER                  = "inert_filler"
ROLE_OTHER_CONTEXT                 = "other_context"
ROLE_NULL_NO_LINK                  = "null_no_link"

ALL_ROLES = {
    ROLE_ANSWER_C, ROLE_HOP1_B, ROLE_ANCHOR_A,
    ROLE_TARGET_NEIGHBOR_DECOY, ROLE_DISTRACTOR_CHAIN_ENDPOINT,
    ROLE_DISTRACTOR_CHAIN_INTERMEDIATE, ROLE_INERT_FILLER,
    ROLE_OTHER_CONTEXT, ROLE_NULL_NO_LINK,
}

TARGET_CHAIN_ROLES = {ROLE_ANSWER_C, ROLE_HOP1_B, ROLE_ANCHOR_A}
DECOY_CHAIN_ROLES  = {ROLE_DISTRACTOR_CHAIN_ENDPOINT, ROLE_DISTRACTOR_CHAIN_INTERMEDIATE}

# ── Query type constants ──────────────────────────────────────────────────────
QT_HOP1          = "hop1"
QT_HOP2          = "hop2"
QT_COMPOSITE     = "composite"
QT_NEG_GRAPH     = "negative_graph"
QT_LENGTH_MATCHED = "length_matched"

REQUIRED_QUERY_TYPES = {QT_HOP1, QT_HOP2, QT_COMPOSITE, QT_NEG_GRAPH}

# ── Context hash (canonical serialization) ────────────────────────────────────
def compute_context_hash(item: dict) -> str:
    """
    SHA-256 of canonical context-block serialization.

    Canonical form: for each fact in ordered_facts sorted ascending by
    position_index, produce the row:
        "{fact_id}|{chain_id}|{fact_role}|{text.strip()}"
    Join rows with '\n', apply NFC normalization, encode UTF-8, hash.

    This definition is independent of YAML/JSON serialization format and
    is human-verifiable from the stored ordered_facts list.
    """
    facts = item.get("context", {}).get("ordered_facts", [])
    rows = []
    for f in sorted(facts, key=lambda x: x["position_index"]):
        text = unicodedata.normalize("NFC", f["text"].strip())
        rows.append(f"{f['fact_id']}|{f['chain_id']}|{f['fact_role']}|{text}")
    canonical = "\n".join(rows)
    return "sha256:" + hashlib.sha256(canonical.encode("utf-8")).hexdigest()


# ── String metrics (token construction audit) ─────────────────────────────────
def levenshtein(a: str, b: str) -> int:
    """Case-insensitive Levenshtein edit distance."""
    a, b = a.upper(), b.upper()
    m, n = len(a), len(b)
    dp = list(range(n + 1))
    for i in range(1, m + 1):
        prev = dp[:]
        dp[0] = i
        for j in range(1, n + 1):
            cost = 0 if a[i - 1] == b[j - 1] else 1
            dp[j] = min(dp[j] + 1, dp[j - 1] + 1, prev[j - 1] + cost)
    return dp[n]


def trigram_set(s: str) -> set:
    s = s.upper()
    if len(s) < 3:
        return {s}
    return {s[i:i + 3] for i in range(len(s) - 2)}


def trigram_jaccard(a: str, b: str) -> float:
    """Trigram-Jaccard similarity for char_overlap_group connected components."""
    ta, tb = trigram_set(a), trigram_set(b)
    union = len(ta | tb)
    return len(ta & tb) / union if union > 0 else 0.0


def audit_near_miss(tok_a: str, tok_b: str) -> dict:
    """
    Compute near-miss metrics between two tokens.
    Threshold application is deferred to threshold-setting phase.
    BPE-Jaccard requires locked tokenizer (caller must supply).
    """
    return {
        "char_edit_distance": levenshtein(tok_a, tok_b),
        "trigram_jaccard": round(trigram_jaccard(tok_a, tok_b), 4),
    }


def audit_round_trip(token: str, tokenizer) -> bool:
    """Verify token round-trips through tokenizer: encode → decode == original."""
    ids = tokenizer.encode(token, add_special_tokens=False)
    decoded = tokenizer.decode(ids)
    return decoded.strip() == token


# ── Validation helpers ────────────────────────────────────────────────────────
def validate_required_fields(item: dict) -> list:
    errors = []
    required_top = [
        "item_id", "chains", "object_roles", "queries", "context",
        "positive_sufficiency_exclusion", "same_context_controls",
        "negative_graph_control", "dummy_baselines",
    ]
    for f in required_top:
        if f not in item:
            errors.append(f"missing required top-level field: '{f}'")

    queries = item.get("queries", {})
    for qt in REQUIRED_QUERY_TYPES:
        if qt not in queries:
            errors.append(f"missing required query type: '{qt}'")
        else:
            for qf in ("expected_answer", "query_anchor"):
                if qf not in queries[qt]:
                    errors.append(f"queries.{qt}: missing field '{qf}'")

    chains = item.get("chains", [])
    n_target = sum(1 for c in chains if c.get("role") == "target")
    if n_target != 1:
        errors.append(f"item must have exactly 1 target chain, found {n_target}")

    return errors


def validate_object_roles(item: dict) -> list:
    errors = []
    roles = item.get("object_roles", {})
    chains = item.get("chains", [])

    if not roles:
        errors.append("object_roles registry is empty")
        return errors

    for tok, role in roles.items():
        if role not in ALL_ROLES:
            errors.append(f"object_roles: '{tok}' has unknown role '{role}'")

    target_chain = next((c for c in chains if c.get("role") == "target"), None)
    if target_chain:
        for obj, expected_role in [
            (target_chain.get("A_object"), ROLE_ANCHOR_A),
            (target_chain.get("B_object"), ROLE_HOP1_B),
            (target_chain.get("C_object"), ROLE_ANSWER_C),
        ]:
            if obj and roles.get(obj) != expected_role:
                errors.append(
                    f"target chain '{obj}' has role '{roles.get(obj)}', expected '{expected_role}'"
                )

    target_objects = set()
    if target_chain:
        target_objects = {
            target_chain.get("A_object"),
            target_chain.get("B_object"),
            target_chain.get("C_object"),
        } - {None}

    for decoy in (c for c in chains if c.get("role") == "decoy"):
        for obj in [decoy.get("A_object"), decoy.get("B_object"), decoy.get("C_object")]:
            if obj and obj in target_objects:
                errors.append(
                    f"object collision: '{obj}' in both target and decoy chains "
                    f"(no object collisions unless explicitly declared)"
                )

    for tok, role in roles.items():
        if role == ROLE_TARGET_NEIGHBOR_DECOY:
            is_decoy_endpoint = any(
                tok == c.get("C_object") for c in chains if c.get("role") == "decoy"
            )
            if is_decoy_endpoint:
                errors.append(
                    f"'{tok}': role is target_neighbor_decoy but object is a "
                    f"distractor_chain_endpoint — roles must be disjoint"
                )

    return errors


def validate_positive_sufficiency(item: dict) -> list:
    errors = []
    pse = item.get("positive_sufficiency_exclusion", {})

    if pse.get("answer_from_hop1_alone_possible") is True:
        errors.append("positive_sufficiency_exclusion: answer_from_hop1_alone_possible is True")
    if pse.get("answer_from_hop2_alone_possible") is True:
        errors.append("positive_sufficiency_exclusion: answer_from_hop2_alone_possible is True")
    if not pse.get("composite_requires_hop1"):
        errors.append("positive_sufficiency_exclusion: composite_requires_hop1 must be True")
    if not pse.get("composite_requires_hop2"):
        errors.append("positive_sufficiency_exclusion: composite_requires_hop2 must be True")

    queries = item.get("queries", {})
    composite_ans = queries.get(QT_COMPOSITE, {}).get("expected_answer")
    hop1_ans = queries.get(QT_HOP1, {}).get("expected_answer")
    if composite_ans and hop1_ans and composite_ans == hop1_ans:
        errors.append(
            f"positive_sufficiency_exclusion: composite answer '{composite_ans}' "
            f"== hop1 answer — shortcut possible"
        )

    return errors


def validate_context_hash(item: dict) -> list:
    errors = []
    declared = item.get("same_context_controls", {}).get("identical_context_hash")
    if not declared:
        errors.append("same_context_controls.identical_context_hash is missing")
        return errors
    computed = compute_context_hash(item)
    if computed != declared:
        errors.append(
            f"identical_context_hash mismatch: "
            f"declared={declared}, computed={computed}"
        )
    return errors


def validate_negative_graph_control(item: dict) -> list:
    """
    Structural validation of negative_graph_control fields.
    Graph traversal (path verification) is performed by the runner before
    any scored run — not repeated here.
    """
    errors = []
    neg = item.get("negative_graph_control", {})
    if not neg:
        errors.append("negative_graph_control block is missing")
        return errors

    for field in ("negative_graph_source_cell", "removed_edge",
                  "independently_constructed", "valid_A_to_C_path_exists"):
        if field not in neg:
            errors.append(f"negative_graph_control: missing required field '{field}'")

    if neg.get("valid_A_to_C_path_exists") is True:
        errors.append(
            "negative_graph_control: valid_A_to_C_path_exists must be False"
        )
    if not neg.get("independently_constructed"):
        errors.append(
            "negative_graph_control: independently_constructed must be True"
        )

    return errors


# ── Full item and manifest validators ─────────────────────────────────────────
def validate_item(item: dict) -> list:
    """Run all structural validation checks. Returns list of error strings."""
    errors = []
    errors += validate_required_fields(item)
    errors += validate_object_roles(item)
    errors += validate_positive_sufficiency(item)
    errors += validate_context_hash(item)
    errors += validate_negative_graph_control(item)
    return errors


def validate_manifest(items: list) -> dict:
    all_errors = {}
    pass_count = 0
    for item in items:
        errs = validate_item(item)
        if errs:
            all_errors[item.get("item_id", "UNKNOWN")] = errs
        else:
            pass_count += 1
    return {
        "schema_version": MANIFEST_SCHEMA_VERSION,
        "total": len(items),
        "pass_count": pass_count,
        "fail_count": len(all_errors),
        "errors": all_errors,
        "all_pass": len(all_errors) == 0,
    }


# ── Manifest hash ─────────────────────────────────────────────────────────────
def get_manifest_hash() -> str:
    return "sha256:" + hashlib.sha256(Path(__file__).read_bytes()).hexdigest()


# ── Items (Stage 0 — no items authorized yet) ─────────────────────────────────
ITEMS = []


if __name__ == "__main__":
    result = validate_manifest(ITEMS)
    print(f"Manifest validation: {result['pass_count']}/{result['total']} pass")
    print(f"manifest_hash: {get_manifest_hash()}")
