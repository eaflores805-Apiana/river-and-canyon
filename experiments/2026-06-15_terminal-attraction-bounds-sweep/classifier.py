#!/usr/bin/env python3
"""
classifier.py — TERMINAL-ATTRACTION-BOUNDS-SWEEP-v0.1

Pre-registered structural classifier per preregistration §5(b). Locked BEFORE
any results were seen. Implements the function verbatim as filed in §5.
No tuning; no post-hoc modification.

Outputs a category label per (raw_output, query_type, item) triple, supplying
the "attraction-type" columns the scorer doesn't tag.
"""
from __future__ import annotations

import re


_FORMAT_RE = re.compile(r"^ANSWER:\s+(.+?)\s*$", re.IGNORECASE)


def extract_token(raw_output: str) -> str | None:
    """Extract the answer token from a raw output. Returns 'NULL' for the abstain
    form, or the raw token text. Returns None on format failure."""
    m = _FORMAT_RE.match(raw_output.strip())
    if not m:
        return None
    return m.group(1).strip()


def classify(token: str | None,
             query_type: str,
             target_A: str,
             target_B: str,
             target_C: str,
             all_terminals: set[str],
             all_intermediates: set[str]) -> str:
    """Pre-registered classifier (preregistration §5(b)). Returns one of:

      hop1:   CORRECT · TARGET_TERMINAL_GRAB · DECOY_TERMINAL_GRAB · ANCHOR_ECHO · ABSTAIN · OTHER · FORMAT_FAIL
      hop2:   CORRECT · OTHER_TERMINAL · ABSTAIN · OTHER · FORMAT_FAIL
      composite: CORRECT · DECOY_TERMINAL_GRAB · STOPPED_SHORT · ABSTAIN · OTHER · FORMAT_FAIL
    """
    if token is None:
        return "FORMAT_FAIL"
    if token == "NULL":
        return "ABSTAIN"

    if query_type == "hop1":
        # Expected = target_B (an INTERMEDIATE; never a terminal).
        if token == target_B:                  return "CORRECT"
        if token == target_C:                  return "TARGET_TERMINAL_GRAB"
        if token in all_terminals:             return "DECOY_TERMINAL_GRAB"
        if token == target_A:                  return "ANCHOR_ECHO"
        return "OTHER"

    if query_type == "hop2":
        # Expected = target_C (single-fact control).
        if token == target_C:                  return "CORRECT"
        if token in all_terminals:             return "OTHER_TERMINAL"
        return "OTHER"

    if query_type == "composite":
        # Expected = target_C (requires chaining).
        # NOTE: at k=1, "correct" is distinguishability-limited — see §6.
        if token == target_C:                  return "CORRECT"
        if token in all_terminals:             return "DECOY_TERMINAL_GRAB"
        if token in all_intermediates:         return "STOPPED_SHORT"
        return "OTHER"

    raise ValueError(f"unknown query_type: {query_type}")


def classify_item(raw_output: str, query_type: str, item: dict) -> dict:
    """Convenience: classify a raw output against an item from items_materialized.json.
    Returns {token, category}."""
    token = extract_token(raw_output)
    target_A = item["target_chain"]["A"]
    target_B = item["target_chain"]["B"]
    target_C = item["target_chain"]["C"]
    all_terminals = set(item["all_terminals"])
    all_intermediates = set(item["all_intermediates"])
    cat = classify(token, query_type, target_A, target_B, target_C,
                   all_terminals, all_intermediates)
    return {"token": token, "category": cat}
