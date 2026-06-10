"""
B1 v2 Harness Runner
====================

Bounded validity-harness infrastructure for Paper 2 reproduction and
Paper 3 certification substrate.

Authorization
-------------
Manager / Team Lead memo, 2026-06-09:
  "B1 v2 implementation is authorized as bounded validity-harness infrastructure."

Senior conditions (incorporated):
  C1 — Paper 2 regression protection (see paper2_regression.py).
  C2 — framework_version is config-driven; not hardcoded; validated against the locked
       threshold sheet.
  C3 — Threshold-sheet hash verified BEFORE trusting any sheet content.

Driving specs
-------------
  - B1 Implementation Plan v2 (governance/2026-06-09_b1-harness-plan-revision/)
  - Paper 3 "Certification Before Retention" v0.4 §8 (B1 dependency)
  - Paper 2 reproduction acceptance criteria

Operational contexts (config-driven)
------------------------------------
  paper2-reproduction:
    framework_version = "none"
    threshold sheet   = not required
    Output: v1-shape fields plus additive B1 v2 substrate.
  paper3-certification:
    framework_version = set in config; validated against threshold sheet
    threshold sheet   = required; hash verified before content trust (C3)
    firewall          = enforced (data access must postdate sheet lock)
    Output: full Paper 3 A.2 per-gate schema; firewall enforcement.

Scope
-----
This runner is a NEW file in experiments/2026-06-09_b1-harness-v2/code/. It does
not modify tier0-run/ files. Foundation files (scorer, tasks, prompt template,
manifest) are copies; hash-verified at boot against tier0-run/ originals.

— CS Engineer, 2026-06-09
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional


# ─────────────────────────────────────────────────────────────────────────────
# Constants
# ─────────────────────────────────────────────────────────────────────────────

RUNNER_PATH = Path(__file__).resolve()
CODE_DIR    = RUNNER_PATH.parent
EXP_DIR     = CODE_DIR.parent

SCORER_PATH  = CODE_DIR / "scorer_twohop_l1.py"
TASKS_PATH   = CODE_DIR / "tasks_twohop_l1.py"
PROMPT_PATH  = CODE_DIR / "prompt_template_twohop_l1.txt"
DEFAULT_MANIFEST_PATH = EXP_DIR / "manifest" / "items_twohop_l1_cell03.json"

# Expected hashes — must match tier0-run/ originals (sealed Paper 2 evidence record).
EXPECTED_SCORER_HASH = (
    "sha256:b65c6803017b8b04ac25d4bd84c5fb5ff61692ed41d609e099b181fa58e4ddde"
)
EXPECTED_TASKS_HASH = (
    "sha256:bcc26ca04b0c5a21db496d08c9307d2e6257315a9376f04473ea68ae36ca349b"
)
EXPECTED_PROMPT_HASH = (
    "sha256:c8a81a299d28c3fd47f4d6fc90c4c57537885d07f01464e68d6fbe2e94a2510e"
)
EXPECTED_TOKENIZER_HASH = (
    "sha256:c0382117ea329cdf097041132f6d735924b697924d6f6fc3945713e96ce87539"
)

# Two-Hop L1 gate thresholds (Manager-approved 2026-06-08, locked).
GATE2_HOP1_THRESHOLD       = 21   # >= 21/24 required for hop1
GATE2_COMPOSITE_THRESHOLD  = 21   # >= 21/24 required for composite
GATE5_MAX_DET_THRESHOLD    = 9    # max_det must be < 9/24

# Model and inference
MODEL_ID                   = "Qwen/Qwen2.5-3B-Instruct"
DECODING_SETTINGS          = {"temperature": 0.0, "max_tokens": 16}
FAILURE_TAXONOMY_VERSION   = "v1.0"
QUERY_TYPES                = ["hop1", "hop2", "composite", "negative_graph"]

# Per Cell03 scorer amendment (2026-06-08): excluded from Gate 5 max_det.
GATE5_REFERENCE_ONLY       = {"always_return_ct", "always_return_NULL"}
# Reference dummies that are not part of the discriminating-shortcut family.
GATE5_NONDETERMINISTIC     = {"uniform_random_expected"}

# Defaults for Paper 2 reproduction context.
FRAMEWORK_VERSION_NONE     = "none"
THRESHOLD_SHEET_HASH_NONE  = "none"

# Query rendering — identical to Cell03 runner.
QUERY_TEXT = {
    "hop1":           "{anchor} links to what?",
    "hop2":           "{anchor} maps to what?",
    "composite":      "{anchor} links to something, which maps to what?",
    "negative_graph": "{anchor} links to something, which maps to what?",
}


# ─────────────────────────────────────────────────────────────────────────────
# Hashing helpers
# ─────────────────────────────────────────────────────────────────────────────

def sha256_file(path: Path) -> str:
    return "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()


def sha256_bytes(b: bytes) -> str:
    return "sha256:" + hashlib.sha256(b).hexdigest()


def sha256_string(s: str) -> str:
    return sha256_bytes(s.encode("utf-8"))


def now_utc_iso() -> str:
    """Current UTC time as ISO-8601 string."""
    return datetime.now(timezone.utc).isoformat()


def compute_model_snapshot_hash(model_dir: Path) -> str:
    """sha256 over a sorted manifest of (relative path, file size, per-file sha256).

    Deterministic and excludes nothing. Mirrors quant_model_manifest_hash from the
    Fork A runner. Returns "sha256:[model-dir-not-found]" if path is invalid.
    """
    if not model_dir.exists() or not model_dir.is_dir():
        return "sha256:[model-dir-not-found]"
    files = []
    for f in sorted(model_dir.rglob("*")):
        if f.is_file():
            rel = f.relative_to(model_dir)
            size = f.stat().st_size
            file_sha = hashlib.sha256(f.read_bytes()).hexdigest()
            files.append(f"{rel}\t{size}\t{file_sha}")
    manifest = "\n".join(files)
    return sha256_bytes(manifest.encode("utf-8"))


def compute_analysis_script_hash() -> str:
    """For B1 v2, gate evaluation is in-runner — no separate analysis script.

    Returns "sha256:in-runner" sentinel. If an external analysis script is
    introduced in a future version, this returns its sha256 instead.
    """
    return "sha256:in-runner"


# ─────────────────────────────────────────────────────────────────────────────
# Locked-artifact hash registry verification (D6)
# ─────────────────────────────────────────────────────────────────────────────

DEFAULT_LOCKED_ARTIFACTS = [
    ("scorer",          SCORER_PATH,  EXPECTED_SCORER_HASH),
    ("tasks",           TASKS_PATH,   EXPECTED_TASKS_HASH),
    ("prompt_template", PROMPT_PATH,  EXPECTED_PROMPT_HASH),
]


class HashRegistryMismatch(Exception):
    """Raised by verify_locked_artifacts when strict mode is off but a caller
    wants programmatic notification of a mismatch."""


def verify_locked_artifacts(strict: bool = True,
                             artifacts: Optional[list] = None,
                             raise_on_mismatch: bool = False) -> dict:
    """Verify foundation files match expected hashes from tier0-run/ originals.

    artifacts: optional list of (name, path, expected_hash) tuples. Defaults to
      DEFAULT_LOCKED_ARTIFACTS (scorer / tasks / prompt template).
    strict: if True and any mismatch, prints and sys.exit(2). Default True.
    raise_on_mismatch: if True (and strict=False), raises HashRegistryMismatch
      instead of returning results with mismatch status. For testing.

    Returns dict of {name: {status, expected, actual}}.
    """
    arts = artifacts if artifacts is not None else DEFAULT_LOCKED_ARTIFACTS
    results = {}
    for name, path, expected in arts:
        if not path.exists():
            results[name] = {"status": "missing", "expected": expected, "actual": None}
        else:
            actual = sha256_file(path)
            status = "ok" if actual == expected else "mismatch"
            results[name] = {"status": status, "expected": expected, "actual": actual}

    bad = [(n, r) for n, r in results.items() if r["status"] != "ok"]
    if bad and strict:
        for n, r in bad:
            print(f"FATAL: {n} hash {r['status']}", file=sys.stderr)
            print(f"  expected: {r['expected']}", file=sys.stderr)
            print(f"  actual:   {r['actual']}",   file=sys.stderr)
        sys.exit(2)
    if bad and raise_on_mismatch:
        raise HashRegistryMismatch(f"Hash mismatch(es): {[n for n, _ in bad]}")
    return results


# ─────────────────────────────────────────────────────────────────────────────
# Paper 3 substrate: threshold sheet + firewall (D6, C2, C3)
# ─────────────────────────────────────────────────────────────────────────────

class FirewallViolation(Exception):
    """Raised when the Paper 3 D6 data-access firewall is violated."""


class ThresholdSheetError(Exception):
    """Raised on threshold-sheet hash mismatch or schema violation."""


def load_threshold_sheet(sheet_path: Path, expected_hash: str) -> dict:
    """Manager C3: verify content hash BEFORE trusting any sheet field.

    Order is critical:
      1. Read raw bytes.
      2. Compute sha256.
      3. Compare to expected_hash.
      4. ONLY if matched, json.loads and return.

    Raises ThresholdSheetError on mismatch or missing file. Caller must catch.
    """
    if not sheet_path.exists():
        raise ThresholdSheetError(f"Threshold sheet not found: {sheet_path}")

    sheet_bytes = sheet_path.read_bytes()
    actual_hash = sha256_bytes(sheet_bytes)

    if actual_hash != expected_hash:
        raise ThresholdSheetError(
            f"Threshold sheet hash mismatch — sheet contents NOT TRUSTED.\n"
            f"  path:     {sheet_path}\n"
            f"  expected: {expected_hash}\n"
            f"  actual:   {actual_hash}"
        )

    return json.loads(sheet_bytes.decode("utf-8"))


def enforce_data_access_firewall(
    threshold_sheet_timestamp: str,
    first_candidate_data_access_timestamp: str,
) -> None:
    """Paper 3 v0.4 D6: first candidate-data access must postdate sheet lock.

    Raises FirewallViolation with reason_code FIREWALL_VIOLATION_DATA_ACCESS_PRELOCK
    if access predates lock.
    """
    sheet_dt  = datetime.fromisoformat(threshold_sheet_timestamp)
    access_dt = datetime.fromisoformat(first_candidate_data_access_timestamp)

    if access_dt < sheet_dt:
        raise FirewallViolation(
            f"FIREWALL_VIOLATION_DATA_ACCESS_PRELOCK: "
            f"first candidate-data access at {access_dt.isoformat()} "
            f"predates threshold-sheet lock at {sheet_dt.isoformat()}. "
            f"Automatic not-certified per Paper 3 v0.4 D6."
        )


def validate_framework_version_agreement(
    config_framework_version: str,
    sheet_framework_version: str,
) -> None:
    """Manager C2: configured framework_version must match threshold sheet.

    Tests should verify config-vs-sheet agreement — not equality against a
    hardcoded string.
    """
    if config_framework_version != sheet_framework_version:
        raise ThresholdSheetError(
            f"framework_version mismatch — config does not match locked sheet.\n"
            f"  config: {config_framework_version}\n"
            f"  sheet:  {sheet_framework_version}"
        )


# ─────────────────────────────────────────────────────────────────────────────
# Paper 3 A.2 gate_summary schema wrapper
# ─────────────────────────────────────────────────────────────────────────────

def make_gate_record(
    gate_id: str,
    status: str,
    observed_value: Any,
    threshold_value: Any,
    reason_code: str,
    evidence_artifact_hash: str,
    *,
    evaluated_by: str = "runner-builtin",
    short_circuit: bool = False,
    framework_version: str = FRAMEWORK_VERSION_NONE,
    threshold_sheet_hash: str = THRESHOLD_SHEET_HASH_NONE,
    analysis_script_hash: Optional[str] = None,
) -> dict:
    """Build a Paper 3 A.2 schema-compliant gate record.

    Status values: "pass" | "fail" | "not_evaluated".
    Delta is computed as observed - threshold when both are numeric scalars.
    """
    assert status in ("pass", "fail", "not_evaluated"), f"Invalid status: {status}"

    if analysis_script_hash is None:
        analysis_script_hash = compute_analysis_script_hash()

    delta: Any = None
    if isinstance(observed_value, (int, float)) and isinstance(threshold_value, (int, float)):
        delta = observed_value - threshold_value

    return {
        "gate_id":                gate_id,
        "status":                 status,
        "observed_value":         observed_value,
        "threshold_value":        threshold_value,
        "delta":                  delta,
        "reason_code":            reason_code,
        "evidence_artifact_hash": evidence_artifact_hash,
        "evaluated_by":           evaluated_by,
        "evaluated_at":           now_utc_iso(),
        "short_circuit":          short_circuit,
        "framework_version":      framework_version,
        "threshold_sheet_hash":   threshold_sheet_hash,
        "analysis_script_hash":   analysis_script_hash,
    }


# ─────────────────────────────────────────────────────────────────────────────
# Two-Hop L1 gate evaluation (Paper 2 reproduction context)
# ─────────────────────────────────────────────────────────────────────────────

def _count_correct(results: list, qt: str) -> tuple[int, int, int]:
    """Returns (correct, format_pass, total) for a given query type."""
    items = [r for r in results if r["query_type"] == qt]
    format_pass = [r for r in items if r["format_class"] == "FORMAT_PASS"]
    correct = [r for r in format_pass if r["is_correct"]]
    return len(correct), len(format_pass), len(items)


def _count_fsf(results: list, qt: str) -> int:
    """FORMAT_SCAFFOLD_FAILURE count for a query type."""
    return sum(
        1 for r in results
        if r["query_type"] == qt and r["failure_class"] == "format_scaffold_failure"
    )


def _gate5_max_det(results: list) -> tuple[int, Optional[str], dict]:
    """Returns (max_det, max_det_dummy, per_dummy_composite_counts).

    Computed over composite items only; excludes Gate 5 reference-only dummies
    and the nondeterministic uniform_random_expected baseline.
    """
    composite = [r for r in results if r["query_type"] == "composite"]
    counts: dict = {}
    for r in composite:
        for name, score in r.get("dummy_baselines", {}).items():
            if name in GATE5_REFERENCE_ONLY or name in GATE5_NONDETERMINISTIC:
                continue
            counts[name] = counts.get(name, 0) + (1 if score and score >= 0.5 else 0)

    if not counts:
        return 0, None, {}
    max_dummy = max(counts, key=counts.get)
    return counts[max_dummy], max_dummy, counts


def evaluate_two_hop_l1_gates(
    all_results: list,
    evidence_artifact_hash: str,
    *,
    framework_version: str = FRAMEWORK_VERSION_NONE,
    threshold_sheet_hash: str = THRESHOLD_SHEET_HASH_NONE,
) -> dict:
    """Evaluate Two-Hop L1 gate ladder (gate_1, gate_2, gate_5).

    Records follow Paper 3 A.2 schema; framework_version and threshold_sheet_hash
    are passed through to each record.
    """
    # Gate 1: FORMAT_PASS = 1.000 per query type (zero FSF across all QTs)
    fsf_counts = {qt: _count_fsf(all_results, qt) for qt in QUERY_TYPES}
    total_fsf  = sum(fsf_counts.values())
    g1_pass    = (total_fsf == 0)
    gate_1 = make_gate_record(
        gate_id="gate_1",
        status="pass" if g1_pass else "fail",
        observed_value={"fsf_counts": fsf_counts, "total_fsf": total_fsf},
        threshold_value={"fsf_per_query_type": 0},
        reason_code=("GATE1_PASS_ZERO_FSF" if g1_pass
                     else f"GATE1_FAIL_FSF_TOTAL_{total_fsf}"),
        evidence_artifact_hash=evidence_artifact_hash,
        framework_version=framework_version,
        threshold_sheet_hash=threshold_sheet_hash,
    )

    # Gate 2: hop1 >= 21/24 AND composite >= 21/24 (FORMAT_PASS denominator)
    hop1_c, _, _ = _count_correct(all_results, "hop1")
    comp_c, _, _ = _count_correct(all_results, "composite")
    hop1_pass = hop1_c >= GATE2_HOP1_THRESHOLD
    comp_pass = comp_c >= GATE2_COMPOSITE_THRESHOLD
    g2_pass   = hop1_pass and comp_pass

    if g2_pass:
        g2_reason = f"GATE2_PASS_HOP1_{hop1_c}_COMPOSITE_{comp_c}"
    elif (not hop1_pass) and (not comp_pass):
        g2_reason = (f"GATE2_FAIL_BOTH_HOP1_{hop1_c}_BELOW_{GATE2_HOP1_THRESHOLD}_"
                     f"COMPOSITE_{comp_c}_BELOW_{GATE2_COMPOSITE_THRESHOLD}")
    elif not hop1_pass:
        g2_reason = f"GATE2_FAIL_HOP1_{hop1_c}_BELOW_{GATE2_HOP1_THRESHOLD}"
    else:
        g2_reason = f"GATE2_FAIL_COMPOSITE_{comp_c}_BELOW_{GATE2_COMPOSITE_THRESHOLD}"

    gate_2 = make_gate_record(
        gate_id="gate_2",
        status="pass" if g2_pass else "fail",
        observed_value={"hop1_correct": hop1_c, "composite_correct": comp_c},
        threshold_value={"hop1_threshold": GATE2_HOP1_THRESHOLD,
                         "composite_threshold": GATE2_COMPOSITE_THRESHOLD},
        reason_code=g2_reason,
        evidence_artifact_hash=evidence_artifact_hash,
        framework_version=framework_version,
        threshold_sheet_hash=threshold_sheet_hash,
    )

    # Gate 5: max_det (over non-reference-only dummies, composite QT) < 9
    max_det, max_dummy, counts = _gate5_max_det(all_results)
    g5_pass = max_det < GATE5_MAX_DET_THRESHOLD
    gate_5 = make_gate_record(
        gate_id="gate_5",
        status="pass" if g5_pass else "fail",
        observed_value={"max_det": max_det, "max_det_dummy": max_dummy,
                        "per_dummy_composite_counts": counts},
        threshold_value={"max_det_threshold": GATE5_MAX_DET_THRESHOLD},
        reason_code=("GATE5_PASS" if g5_pass
                     else f"GATE5_FAIL_MAX_DET_{max_det}_GE_{GATE5_MAX_DET_THRESHOLD}"),
        evidence_artifact_hash=evidence_artifact_hash,
        framework_version=framework_version,
        threshold_sheet_hash=threshold_sheet_hash,
    )

    return {"gate_1": gate_1, "gate_2": gate_2, "gate_5": gate_5}


def determine_stress_eligible(gate_summary: dict) -> tuple[bool, str]:
    """Determine stress_eligible from gate_summary.

    Per Paper 3 §8 and research-program-map §7: fail-closed must block on
    stress_eligible == false, not just Gate 2 alone.

    Stress-eligible only if ALL of Gate 1, Gate 2, Gate 5 pass.
    """
    g1 = gate_summary.get("gate_1", {}).get("status") == "pass"
    g2 = gate_summary.get("gate_2", {}).get("status") == "pass"
    g5 = gate_summary.get("gate_5", {}).get("status") == "pass"

    if g1 and g2 and g5:
        g2_obs = gate_summary["gate_2"]["observed_value"]
        return True, (f"STRESS_ELIGIBLE_GATE2_PASS_HOP1_{g2_obs['hop1_correct']}"
                      f"_COMPOSITE_{g2_obs['composite_correct']}")

    # Most informative failure: prefer Gate 2, then Gate 1, then Gate 5.
    if not g2:
        return False, gate_summary["gate_2"]["reason_code"]
    if not g1:
        return False, gate_summary["gate_1"]["reason_code"]
    if not g5:
        return False, gate_summary["gate_5"]["reason_code"]
    return False, "STRESS_INELIGIBLE_UNKNOWN"


def runtime_fail_closed_block(stress_eligible: bool, eligibility_reason_code: str,
                              gate_summary: dict) -> None:
    """Print clear stress-ineligibility message when fail-closed triggers."""
    if stress_eligible:
        return
    print("", file=sys.stderr)
    print("=== STRESS-ELIGIBILITY FAIL (fail-closed) ===", file=sys.stderr)
    print(f"  reason_code: {eligibility_reason_code}", file=sys.stderr)
    for gid in ("gate_1", "gate_2", "gate_5"):
        g = gate_summary.get(gid, {})
        if g.get("status") != "pass":
            print(f"  {gid}: {g.get('status')} — {g.get('reason_code', 'N/A')}",
                  file=sys.stderr)
    print("  Cell is NOT stress-eligible. Result file marked stress_eligible=false.",
          file=sys.stderr)
    print("  Do not proceed to stress runs.", file=sys.stderr)


# ─────────────────────────────────────────────────────────────────────────────
# Prompt rendering
# ─────────────────────────────────────────────────────────────────────────────

def render_context(facts: list) -> str:
    return "\n".join(
        f["text"] for f in sorted(facts, key=lambda x: x["position_index"])
    )


def get_facts_for_query(item: dict, query_type: str) -> list:
    facts = item["context"]["ordered_facts"]
    if query_type == "negative_graph":
        facts = [
            f for f in facts
            if not (f["chain_id"] == "target_chain" and f["fact_role"] == "hop2_fact")
        ]
    return facts


def render_prompt(item: dict, query_type: str, template: str) -> str:
    anchor      = item["queries"][query_type]["query_anchor"]
    facts       = get_facts_for_query(item, query_type)
    context_str = render_context(facts)
    query_str   = QUERY_TEXT[query_type].format(anchor=anchor)
    return template.replace("{CONTEXT}", context_str).replace("{QUERY}", query_str)


# ─────────────────────────────────────────────────────────────────────────────
# §8 endpoint-intrusion diagnostics (port from Cell03 runner)
# ─────────────────────────────────────────────────────────────────────────────

def _build_token_pos_map(item: dict,
                         role_neighbor: str = "target_neighbor_decoy",
                         role_filler:   str = "inert_filler") -> dict:
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
    for f in item["context"]["ordered_facts"]:
        if (f.get("chain_id") == "target_chain"
                and f.get("fact_role") == fact_role_key):
            return f["position_index"]
    return None


def compute_s8_diagnostics(item: dict, query_type: str, scored: dict,
                            c_by_pos_fn) -> dict:
    """§8 endpoint-intrusion diagnostic block (per Team Lead standing requirement)."""
    returned_token = scored.get("returned_token")
    returned_role  = scored.get("returned_role")
    expected       = item["queries"][query_type]["expected_answer"]

    ct = next((c["C_object"] for c in item.get("chains", []) if c.get("role") == "target"),
              None)
    cds = [c["C_object"] for c in item.get("chains", []) if c.get("role") == "decoy"]

    if returned_token is None:
        ct_vs_other_C = "N/A"
    elif returned_token == ct:
        ct_vs_other_C = "ct"
    elif returned_token in cds:
        ct_vs_other_C = "other_C"
    else:
        ct_vs_other_C = "not_C"

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

    is_endpoint = returned_role in ("hop1_B", "answer_C", "distractor_chain_endpoint")

    if returned_token is None or not is_endpoint:
        ret_abs_pos = "N/A"
    else:
        tok_pos = _build_token_pos_map(item)
        ret_abs_pos = tok_pos.get(returned_token, "N/A")

    if returned_token is None or not is_endpoint:
        ret_c_rank = "N/A"
    else:
        c_by_pos = c_by_pos_fn(item)
        ret_c_rank = (c_by_pos.index(returned_token) + 1
                      if returned_token in c_by_pos else "N/A")

    if not is_endpoint or ret_abs_pos == "N/A":
        ret_hop1_prox = "N/A"
        ret_hop2_prox = "N/A"
    else:
        h1 = _find_target_chain_fact_pos(item, "hop1_fact")
        h2 = _find_target_chain_fact_pos(item, "hop2_fact")
        ret_hop1_prox = abs(ret_abs_pos - h1) if h1 is not None else "N/A"
        ret_hop2_prox = abs(ret_abs_pos - h2) if h2 is not None else "N/A"

    if query_type == "negative_graph":
        neg_intrusion = (returned_token is not None
                         and returned_token not in ("NULL", "null", "Null"))
    else:
        neg_intrusion = "N/A"

    return {
        "query_type":                   query_type,
        "expected_answer":              expected,
        "returned_token":               returned_token,
        "returned_role":                returned_role,
        "ct_vs_other_C":                ct_vs_other_C,
        "b_vs_c_endpoint":              b_vs_c,
        "returned_abs_position":        ret_abs_pos,
        "returned_c_rank":              ret_c_rank,
        "returned_hop1_proximity":      ret_hop1_prox,
        "returned_hop2_proximity":      ret_hop2_prox,
        "neg_graph_endpoint_intrusion": neg_intrusion,
    }


# ─────────────────────────────────────────────────────────────────────────────
# Per-item record assembly (v1 + v2 substrate)
# ─────────────────────────────────────────────────────────────────────────────

def make_per_item_record(
    item_id: str, query_type: str, prompt_rendered_hash: str, raw_output: str,
    scored: dict, dummy: dict, s8: dict,
    *,
    structural_proxies: Optional[dict] = None,
) -> dict:
    """Per-item record with v1 substrate (self-reference FP16 fields,
    same_error_identity_key) and v2 substrate (structural_proxies slot).

    For FP16 base runs, fp16_raw_output equals raw_output and exact_output_match
    is True — these fields exist for structural compatibility with the stress
    runner comparison workflow.
    """
    return {
        "item_id":                  item_id,
        "query_type":               query_type,
        "prompt_rendered_hash":     prompt_rendered_hash,
        "raw_output":               raw_output,
        "failure_class":            scored["failure_class"],
        "scaffold_class":           scored["scaffold_class"],
        "format_class":             scored["format_class"],
        "returned_token":           scored["returned_token"],
        "returned_role":            scored["returned_role"],
        "is_correct":               scored["is_correct"],
        "dummy_baselines":          dummy,
        "s8_diagnostics":           s8,
        # v1 substrate
        "fp16_raw_output":          raw_output,
        "exact_output_match":       True,
        "same_error_identity_key": (
            f"{scored['failure_class']}|{scored['scaffold_class']}|{scored['format_class']}"
        ),
        # v2 substrate (schema slot only at v2; empty unless candidate threshold sheet declares)
        "structural_proxies":       structural_proxies if structural_proxies is not None else {},
    }


# ─────────────────────────────────────────────────────────────────────────────
# Main entry
# ─────────────────────────────────────────────────────────────────────────────

def _build_arg_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="B1 v2 Harness Runner")
    p.add_argument("--mode", choices=["dry-run", "live"], default="dry-run",
                   help="dry-run: provenance + validation only; live: load model and run inference")
    p.add_argument("--context", choices=["paper2-reproduction", "paper3-certification"],
                   default="paper2-reproduction")
    p.add_argument("--framework-version", default=FRAMEWORK_VERSION_NONE,
                   help="Framework version. For paper3 context, validated against locked sheet.")
    p.add_argument("--threshold-sheet", default=None,
                   help="Path to locked threshold sheet JSON (required for paper3 context)")
    p.add_argument("--expected-threshold-sheet-hash", default=None,
                   help="Expected sha256:... of threshold sheet (required if --threshold-sheet given)")
    p.add_argument("--manifest", default=str(DEFAULT_MANIFEST_PATH))
    p.add_argument("--manifest-subset", type=int, default=None,
                   help="If set, run only the first N items of the manifest (smoke testing). "
                        "Note: subsetting disables gate-decision regression vs Paper 2 baseline.")
    p.add_argument("--output-dir", default=str(EXP_DIR / "results"))
    p.add_argument("--output-prefix", default="RESULTS-B1V2",
                   help="Prefix for output JSON filename")
    return p


def main(argv: Optional[list[str]] = None) -> int:
    parser = _build_arg_parser()
    args = parser.parse_args(argv)

    print(f"B1 v2 Harness Runner — mode={args.mode}, context={args.context}")
    print(f"  framework_version: {args.framework_version}")
    print(f"  manifest:          {args.manifest}")

    # ── Step 1: Locked artifact hash registry verification (D6) ────────────
    print("\nStep 1: Verifying locked artifact hashes...")
    artifact_results = verify_locked_artifacts(strict=True)
    for name, r in artifact_results.items():
        print(f"  {name:18s} {r['status']:10s} {r['actual'][:30]}...")

    # ── Step 2: Threshold sheet (Paper 3 context) ──────────────────────────
    framework_version    = args.framework_version
    threshold_sheet_hash = THRESHOLD_SHEET_HASH_NONE
    threshold_sheet_ts   = None

    if args.context == "paper3-certification":
        if args.threshold_sheet is None or args.expected_threshold_sheet_hash is None:
            print("FATAL: Paper 3 context requires both --threshold-sheet and "
                  "--expected-threshold-sheet-hash", file=sys.stderr)
            return 2
        print("\nStep 2: Verifying threshold-sheet hash BEFORE trust (Manager C3)...")
        try:
            sheet = load_threshold_sheet(Path(args.threshold_sheet),
                                          args.expected_threshold_sheet_hash)
        except ThresholdSheetError as e:
            print(f"FATAL: {e}", file=sys.stderr)
            return 2
        threshold_sheet_hash = args.expected_threshold_sheet_hash
        threshold_sheet_ts   = sheet.get("threshold_sheet_timestamp")
        # Manager C2: framework_version is config-driven and validated against sheet
        try:
            validate_framework_version_agreement(
                framework_version, sheet.get("framework_version", ""))
        except ThresholdSheetError as e:
            print(f"FATAL: {e}", file=sys.stderr)
            return 2
        print(f"  threshold_sheet_hash:  OK ({threshold_sheet_hash[:30]}...)")
        print(f"  framework_version:     config matches sheet ({framework_version})")
        print(f"  threshold_sheet_ts:    {threshold_sheet_ts}")

    # ── Step 3: Capture first_candidate_data_access_timestamp (firewall substrate) ─
    print("\nStep 3: Capturing first_candidate_data_access_timestamp...")
    first_data_access_ts = now_utc_iso()
    print(f"  timestamp: {first_data_access_ts}")

    # ── Step 4: Firewall enforcement (Paper 3 context only) ───────────────
    if args.context == "paper3-certification" and threshold_sheet_ts:
        print("\nStep 4: Enforcing data-access firewall (D6)...")
        try:
            enforce_data_access_firewall(threshold_sheet_ts, first_data_access_ts)
        except FirewallViolation as e:
            print(f"FATAL: {e}", file=sys.stderr)
            return 2
        print("  Firewall: OK (data access postdates sheet lock)")

    # ── Step 5: Manifest load and validation ──────────────────────────────
    print("\nStep 5: Loading and validating manifest...")
    sys.path.insert(0, str(CODE_DIR))
    from tasks_twohop_l1 import validate_manifest
    from scorer_twohop_l1 import (
        classify_output, compute_dummy_baseline_scores,
        _c_objects_by_context_position,
    )
    manifest_path = Path(args.manifest)
    items = json.loads(manifest_path.read_text())
    validation = validate_manifest(items)
    print(f"  validate_manifest(): {validation['pass_count']}/{validation['total']} pass")
    if not validation["all_pass"]:
        print("FATAL: manifest validation failed", file=sys.stderr)
        for iid, errs in validation.get("errors", {}).items():
            for e in errs:
                print(f"  [{iid}] {e}", file=sys.stderr)
        return 2
    manifest_hash = sha256_file(manifest_path)
    print(f"  manifest_hash: {manifest_hash}")

    # Optional subset for smoke testing
    if args.manifest_subset is not None and args.manifest_subset > 0:
        original_count = len(items)
        items = items[:args.manifest_subset]
        print(f"  manifest-subset: using first {len(items)} of {original_count} items "
              f"(smoke mode; gate-decision regression disabled)")

    # ── Provenance assembly (partial; model fields populated below) ───────
    runner_hash = sha256_file(RUNNER_PATH)
    provenance = {
        # v1 carried forward
        "manifest_hash":            manifest_hash,
        "scorer_hash":              artifact_results["scorer"]["actual"],
        "validator_hash":           artifact_results["tasks"]["actual"],
        "runner_hash":              runner_hash,
        "prompt_template_hash":     artifact_results["prompt_template"]["actual"],
        "failure_taxonomy_version": FAILURE_TAXONOMY_VERSION,
        "model_id":                 MODEL_ID,
        "decoding_settings":        DECODING_SETTINGS,
        "run_timestamp":            int(time.time()),
        # v1 additions
        "mlx_lm_version":           None,    # populated in live mode
        "python_version":           sys.version,
        "model_snapshot_hash":      None,    # populated in live mode
        "precision_rung":           "FP16",
        "quant_method":             "none",
        # v2 additions (Paper 3 substrate)
        "analysis_script_hash":     compute_analysis_script_hash(),
        "first_candidate_data_access_timestamp": first_data_access_ts,
        "framework_version":        framework_version,
        "threshold_sheet_hash":     threshold_sheet_hash,
    }

    # ── Dry-run short-circuit ─────────────────────────────────────────────
    if args.mode == "dry-run":
        print("\nDry-run mode: provenance and validation complete. No model loaded.")
        print(f"  runner_hash:  {runner_hash}")
        print(f"  framework_version: {framework_version}")
        print(f"  threshold_sheet_hash: {threshold_sheet_hash}")
        return 0

    # ── Step 6 (live): Load model and tokenizer ───────────────────────────
    print("\nStep 6: Loading FP16 model and tokenizer...")
    try:
        import mlx_lm
        from mlx_lm import load, stream_generate
        from mlx_lm.sample_utils import make_sampler
    except ImportError:
        print("FATAL: mlx_lm not available", file=sys.stderr)
        return 3
    provenance["mlx_lm_version"] = mlx_lm.__version__

    model, tokenizer = load(MODEL_ID)
    print(f"  Model loaded: {MODEL_ID}")
    print(f"  mlx_lm_version: {mlx_lm.__version__}")

    # Locate model snapshot dir (HuggingFace cache)
    hf_cache = Path(os.environ.get("HF_HOME",
                                    Path.home() / ".cache" / "huggingface" / "hub"))
    snap_dir = None
    for candidate in hf_cache.rglob("snapshots/*"):
        if "Qwen2.5-3B-Instruct" in str(candidate) and candidate.is_dir():
            snap_dir = candidate
            break
    if snap_dir is not None:
        provenance["model_snapshot_hash"] = compute_model_snapshot_hash(snap_dir)
        print(f"  model_snapshot_hash: {provenance['model_snapshot_hash'][:38]}...")
    else:
        provenance["model_snapshot_hash"] = "sha256:[model-snapshot-not-located]"
        print("  WARNING: could not locate model snapshot dir", file=sys.stderr)

    # Tokenizer hash check
    tok_file = None
    for cand in hf_cache.rglob("tokenizer.json"):
        if "Qwen2.5-3B-Instruct" in str(cand) and "mlx" not in str(cand):
            tok_file = cand
            break
    if tok_file is not None and tok_file.exists():
        tok_hash = sha256_file(tok_file)
        if tok_hash != EXPECTED_TOKENIZER_HASH:
            print(f"FATAL: tokenizer hash mismatch.\n"
                  f"  expected: {EXPECTED_TOKENIZER_HASH}\n"
                  f"  actual:   {tok_hash}", file=sys.stderr)
            return 2
        provenance["tokenizer_hash"] = tok_hash
        print("  tokenizer_hash: OK")

    sampler = make_sampler(temp=DECODING_SETTINGS["temperature"])

    # ── Step 7 (live): Inference loop ─────────────────────────────────────
    print("\nStep 7: Running inference...")
    template = PROMPT_PATH.read_text()
    all_results = []
    for item in items:
        item_id = item["item_id"]
        for qt in QUERY_TYPES:
            prompt = render_prompt(item, qt, template)
            prompt_hash = sha256_string(prompt)
            chat_prompt = prompt
            if getattr(tokenizer, "chat_template", None) is not None:
                chat_prompt = tokenizer.apply_chat_template(
                    [{"role": "user", "content": prompt}],
                    add_generation_prompt=True, tokenize=False,
                )
            raw_output = ""
            for resp in stream_generate(
                model, tokenizer, prompt=chat_prompt,
                max_tokens=DECODING_SETTINGS["max_tokens"], sampler=sampler,
            ):
                raw_output += resp.text
            raw_output = raw_output.strip()

            scored = classify_output(raw_output, item, qt)
            dummy  = compute_dummy_baseline_scores(item, qt)
            s8     = compute_s8_diagnostics(item, qt, scored,
                                             _c_objects_by_context_position)
            all_results.append(make_per_item_record(
                item_id, qt, prompt_hash, raw_output, scored, dummy, s8,
            ))
            status = "✓" if scored["is_correct"] else "✗"
            print(f"  {item_id}/{qt}: {status} {scored['failure_class']}")

    # ── Step 8: Gate evaluation and stress eligibility ────────────────────
    print("\nStep 8: Evaluating gates...")
    # Evidence artifact hash will be the output file hash; placeholder for now,
    # updated below after the file is written. For in-record use, we use a hash
    # over the result list serialization at evaluation time.
    evidence_pre = sha256_string(json.dumps(all_results, sort_keys=True))
    gate_summary = evaluate_two_hop_l1_gates(
        all_results, evidence_artifact_hash=evidence_pre,
        framework_version=framework_version,
        threshold_sheet_hash=threshold_sheet_hash,
    )
    stress_eligible, elig_reason = determine_stress_eligible(gate_summary)
    print(f"  gate_1: {gate_summary['gate_1']['status']}  "
          f"({gate_summary['gate_1']['reason_code']})")
    print(f"  gate_2: {gate_summary['gate_2']['status']}  "
          f"({gate_summary['gate_2']['reason_code']})")
    print(f"  gate_5: {gate_summary['gate_5']['status']}  "
          f"({gate_summary['gate_5']['reason_code']})")
    print(f"  stress_eligible: {stress_eligible}")

    # Runtime fail-closed
    runtime_fail_closed_block(stress_eligible, elig_reason, gate_summary)

    # ── Step 9: Write output ──────────────────────────────────────────────
    print("\nStep 9: Writing output artifact...")
    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    ts = int(time.time())
    output = {
        "provenance":               provenance,
        "gate_summary":             gate_summary,
        "stress_eligible":          stress_eligible,
        "eligibility_reason_code":  elig_reason,
        "voided_run_log":           [],
        "results":                  all_results,
    }
    out_path = out_dir / f"{args.output_prefix}-cell03-{ts}.json"
    out_path.write_text(json.dumps(output, indent=2))
    output_hash = sha256_file(out_path)
    print(f"  output written: {out_path}")
    print(f"  output_hash:    {output_hash}")
    print(f"  runner_hash:    {runner_hash}")
    return 0 if stress_eligible else 1   # exit code 1 = not stress-eligible (informational, not error)


if __name__ == "__main__":
    sys.exit(main())
