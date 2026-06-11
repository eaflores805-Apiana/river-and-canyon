"""Lane 1a declared dummy-policy battery (locked; hash-recorded in LOCK-RECORD.md).

Five deterministic offline policies. Each takes a manifest item and
returns a predicted value (string). Computed pre-execution from
manifest content alone; no inference required.

Per §13 recipe §8: every policy must yield a well-defined non-constant
prediction vector on every rung's manifest before lock; the recipe
acceptance check is lock-blocking.
"""

from __future__ import annotations

from typing import Any


# Item shape (per manifest_generator output):
# {
#   "item_id": str,
#   "stratum": "answerable" | "null",
#   "in_context_pairs": [(key, value), ...],   # ordered list of (key, value) pairs
#   "queried_key": str,
#   "expected_answer": str | "NULL",
# }


def pure_last_position(item: dict[str, Any]) -> str:
    """Predict the value at the last position in the in-context list."""
    pairs = item["in_context_pairs"]
    if not pairs:
        return ""
    return pairs[-1][1]


def target_recency(item: dict[str, Any]) -> str:
    """Predict the value of the most-recently-mentioned key sharing the
    first character with the queried key. If none, fall back to the last
    in-context value (recency baseline)."""
    qk_first = (item["queried_key"] or "")[:1]
    if not qk_first:
        return pure_last_position(item)
    candidates = [
        (i, k, v)
        for i, (k, v) in enumerate(item["in_context_pairs"])
        if k.startswith(qk_first)
    ]
    if not candidates:
        return pure_last_position(item)
    candidates.sort(key=lambda t: t[0])
    return candidates[-1][2]


def salient_endpoint(item: dict[str, Any]) -> str:
    """Predict the value at the first or last position by declared
    salience. For Lane 1a, declared salience = last position
    (Qwen-class instruction models bias toward recency); chosen at
    construction time."""
    pairs = item["in_context_pairs"]
    if not pairs:
        return ""
    return pairs[-1][1]


def copy_completion(item: dict[str, Any]) -> str:
    """Predict by 'copying' the queried key as the answer (degenerate
    completion). Used as a copy-bias prediction surface."""
    return item["queried_key"]


def homogeneous_prefix_completion(item: dict[str, Any]) -> str:
    """Predict the value of the in-context key sharing the longest
    common prefix with the queried key. Tie-break: lowest in-context
    index. Designed to fire on K=high (shared-prefix family)."""
    qk = item["queried_key"]
    best_len = -1
    best_idx = -1
    best_val = ""
    for i, (k, v) in enumerate(item["in_context_pairs"]):
        # common prefix length
        n = 0
        for a, b in zip(qk, k):
            if a != b:
                break
            n += 1
        if n > best_len or (n == best_len and best_idx == -1):
            best_len = n
            best_idx = i
            best_val = v
    return best_val


DECLARED_POLICIES = {
    "pure_last_position": pure_last_position,
    "target_recency": target_recency,
    "salient_endpoint": salient_endpoint,
    "copy_completion": copy_completion,
    "homogeneous_prefix_completion": homogeneous_prefix_completion,
}


def policy_predictions(
    policy_name: str, items: list[dict[str, Any]]
) -> list[str]:
    """Return the prediction vector for `policy_name` over `items`."""
    policy = DECLARED_POLICIES[policy_name]
    return [policy(it) for it in items]


def is_nondegenerate(predictions: list[str], min_distinct: int = 3) -> bool:
    """Recipe acceptance check (§13 §8): predictions must be
    well-defined (no None / no ill-formed) and have at least
    `min_distinct` distinct values."""
    if any(p is None for p in predictions):
        return False
    return len(set(predictions)) >= min_distinct
