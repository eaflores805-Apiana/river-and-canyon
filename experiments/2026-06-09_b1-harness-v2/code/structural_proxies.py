"""
structural_proxies.py
=====================

D5 substrate: deterministic, model-free structural difficulty proxies computed
from manifest JSON only.

Per Paper 3 v0.4 D5: difficulty proxies must be derived from manifest / item
metadata only. Proxies derived from model outputs, observed accuracy, or
failure rates are NOT admissible.

Each function takes one item (dict from the manifest) and returns a numeric or
structural value. All functions are pure and deterministic — calling them twice
on the same input yields the same output (B1-T24).

This module ships at v2 with function signatures and unit tests but no candidate-
specific calling convention. The candidate's threshold sheet (Paper 3 A.1
`D5_structural_difficulty_proxies` field) declares which proxies are computed for
a given certification attempt.

— CS Engineer, 2026-06-09
"""

from __future__ import annotations

from collections import Counter
from typing import Any


# ─────────────────────────────────────────────────────────────────────────────
# Proxy implementations
# ─────────────────────────────────────────────────────────────────────────────

def token_length(item: dict) -> int:
    """Number of whitespace-separated tokens in the rendered context (sum across facts)."""
    facts = item.get("context", {}).get("ordered_facts", [])
    total = 0
    for f in facts:
        total += len(f.get("text", "").split())
    return total


def context_window_utilization(item: dict, window_size: int = 32768) -> float:
    """Approximate context-window utilization: total context token count / window_size.

    Uses whitespace tokenization as an approximation. Returns fraction in [0, 1].
    """
    if window_size <= 0:
        return 0.0
    tokens = token_length(item)
    return min(1.0, tokens / window_size)


def graph_distance(item: dict) -> int:
    """Hop count of the target chain (e.g., two-hop = 2)."""
    chains = item.get("chains", [])
    target = next((c for c in chains if c.get("role") == "target"), None)
    if target is None:
        return 0
    # Two-hop construction has A -> B -> C; hop count = 2 by construction.
    # General form: count facts in target chain.
    facts = item.get("context", {}).get("ordered_facts", [])
    target_facts = [f for f in facts
                    if f.get("chain_id") == "target_chain"
                    and f.get("fact_role", "").endswith("_fact")]
    # Two-hop semantics: hop1_fact + hop2_fact = 2
    return len(target_facts)


def number_of_hops(item: dict) -> int:
    """Alias for graph_distance — explicit name for D5 declaration."""
    return graph_distance(item)


def number_of_keys(item: dict) -> int:
    """Total number of distinct entity tokens (object_roles map size)."""
    return len(item.get("object_roles", {}))


def nesting_depth(item: dict) -> int:
    """Maximum nesting depth of the context structure.

    For Two-Hop L1 (flat fact list), depth = 1. Provided for forward
    compatibility with nested constructions.
    """
    # Two-Hop L1 manifests are flat fact lists; depth always 1.
    # Generalized depth measurement would inspect a nested 'facts' tree.
    facts = item.get("context", {}).get("ordered_facts", [])
    return 1 if facts else 0


def distractor_count(item: dict) -> int:
    """Number of decoy chains plus any standalone distractor facts."""
    chains = item.get("chains", [])
    decoy_chains = sum(1 for c in chains if c.get("role") == "decoy")
    facts = item.get("context", {}).get("ordered_facts", [])
    standalone_distractors = sum(
        1 for f in facts
        if f.get("fact_role") == "neighbor_decoy_fact"
        or f.get("fact_role") == "inert_filler_fact"
    )
    return decoy_chains + standalone_distractors


def distractor_entropy(item: dict) -> float:
    """Shannon entropy of distractor-token role distribution (nats).

    Higher entropy = more uniform distractor distribution across roles.
    Returns 0 if no distractors or only one role.
    """
    obj_roles = item.get("object_roles", {})
    # Filter to distractor-class roles only
    distractor_roles = [
        r for r in obj_roles.values()
        if r in (
            "distractor_chain_intermediate",
            "distractor_chain_endpoint",
            "target_neighbor_decoy",
            "inert_filler",
            "other_context",
        )
    ]
    if not distractor_roles:
        return 0.0
    counts = Counter(distractor_roles)
    total = sum(counts.values())
    import math
    entropy = 0.0
    for c in counts.values():
        p = c / total
        if p > 0:
            entropy -= p * math.log(p)
    return entropy


def answer_position_distribution(item: dict) -> dict:
    """Distribution of correct-answer token positions across the four query types.

    Returns a dict mapping query_type -> position_index of the expected answer
    (or None if not found in context).
    """
    facts = item.get("context", {}).get("ordered_facts", [])
    queries = item.get("queries", {})
    distribution = {}
    for qt, q in queries.items():
        expected = q.get("expected_answer")
        if expected is None or expected == "NULL":
            distribution[qt] = None
            continue
        # Find the earliest position of any fact text containing the expected answer
        pos = None
        for f in facts:
            if expected in f.get("text", ""):
                fp = f.get("position_index")
                if pos is None or (fp is not None and fp < pos):
                    pos = fp
        distribution[qt] = pos
    return distribution


def token_prefix_overlap(item: dict) -> dict:
    """Pairwise leading-character overlap among answer-relevant tokens.

    Returns a dict with max_prefix_overlap (int) and mean_prefix_overlap (float)
    across pairs of C-objects from all chains.
    """
    chains = item.get("chains", [])
    c_objects = [c.get("C_object") for c in chains if c.get("C_object")]
    if len(c_objects) < 2:
        return {"max_prefix_overlap": 0, "mean_prefix_overlap": 0.0, "pairs": 0}
    overlaps = []
    for i in range(len(c_objects)):
        for j in range(i + 1, len(c_objects)):
            a, b = c_objects[i], c_objects[j]
            ov = 0
            for ca, cb in zip(a, b):
                if ca == cb:
                    ov += 1
                else:
                    break
            overlaps.append(ov)
    return {
        "max_prefix_overlap":  max(overlaps),
        "mean_prefix_overlap": sum(overlaps) / len(overlaps),
        "pairs":               len(overlaps),
    }


def null_non_null_balance(item: dict) -> dict:
    """Balance between NULL-valid and non-NULL queries across query types.

    Returns dict with counts and ratio. For Two-Hop L1, negative_graph is the
    NULL-eligible query; others are non-NULL.
    """
    queries = item.get("queries", {})
    null_count    = sum(1 for q in queries.values()
                        if q.get("expected_answer") == "NULL")
    non_null      = len(queries) - null_count
    ratio = null_count / max(1, len(queries))
    return {"null_count": null_count, "non_null_count": non_null, "null_ratio": ratio}


# ─────────────────────────────────────────────────────────────────────────────
# Registry — used by runner / threshold sheet
# ─────────────────────────────────────────────────────────────────────────────

PROXY_REGISTRY = {
    "token_length":                  token_length,
    "context_window_utilization":    context_window_utilization,
    "graph_distance":                graph_distance,
    "number_of_hops":                number_of_hops,
    "number_of_keys":                number_of_keys,
    "nesting_depth":                 nesting_depth,
    "distractor_count":              distractor_count,
    "distractor_entropy":            distractor_entropy,
    "answer_position_distribution":  answer_position_distribution,
    "token_prefix_overlap":          token_prefix_overlap,
    "null_non_null_balance":         null_non_null_balance,
}


def compute_proxies(item: dict, proxy_names: list[str]) -> dict:
    """Compute the requested proxies for one item.

    proxy_names is a list of registered names (typically from a candidate's
    threshold sheet `D5_structural_difficulty_proxies` field). Unknown names are
    skipped silently — invocation is the caller's responsibility to validate.
    """
    out = {}
    for name in proxy_names:
        fn = PROXY_REGISTRY.get(name)
        if fn is not None:
            out[name] = fn(item)
    return out
