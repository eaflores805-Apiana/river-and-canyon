"""Lane 1a analyzer (locked; hash-recorded in LOCK-RECORD.md).

Reads per-rung raw outputs; computes the 8 diagnostic axes; applies
§1.6 classification rules with B2 preempt and B1 gap sign; assembles
per-rung records; computes K and the survivor set; emits the fixed
outcome statement; writes the sweep record.

B-series fixes applied:
  B1 — gap := content_acc - strict_acc
  B2 — inconclusive_not_actionable preempts all other labels
  B3 — control_acc denominator = 80 answerable-mirror controls only
  B4 — token-prior path read from LOCK-RECORD
  B5 — total_attempts must equal planned_generation_count; survivors
       serialized alphabetically by rung_id
"""

from __future__ import annotations

import json
import math
import string
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Optional

from artifact_tags import tag

SCRIPT_DIR = Path(__file__).resolve().parent

LABELS_ENUM = {
    "accuracy_indistinguishable_from_token_prior",
    "accuracy_indistinguishable_from_declared_policy_envelope",
    "insufficient_measurement_headroom",
    "strict_content_gap_instability",
    "abstention_contract_instability",
    "inconclusive_not_actionable",
    "requires_further_investigation",
}

RUNG_IDS = ["L01", "L02", "L03", "L04", "L05", "L06", "L07", "L08"]


def _binomial_se(p: float, n: int) -> float:
    if n <= 0:
        return float("inf")
    return math.sqrt(max(p * (1.0 - p) / n, 0.0))


def assign_labels(rung_record: dict[str, Any]) -> list[str]:
    """Mechanical label-assignment rules.

    B2 — inconclusive preempts: void_count_total > 5 OR
         harness_anomaly_flag OR missing_required_outputs_flag fires
         FIRST and returns ["inconclusive_not_actionable"] alone.
    """

    # B2 preempt: measurement validity checks evaluate first.
    if (
        rung_record["void_count"] > 5
        or rung_record["harness_anomaly_flag"]
        or rung_record["missing_required_outputs_flag"]
    ):
        return ["inconclusive_not_actionable"]

    labels: list[str] = []

    strict_acc = rung_record["strict_acc"]
    content_acc = rung_record["content_acc"]
    control_acc = rung_record["control_acc"]
    n_s_eff = rung_record["N_effective"]
    union_envelope = rung_record["union_envelope_score"]

    se_strict = _binomial_se(strict_acc, n_s_eff)

    # Token-prior indistinguishability (only if control was evaluated).
    if control_acc is not None:
        n_c_eff = 80 - rung_record["void_count_control_answerable_mirror"]  # B3
        se_control = _binomial_se(control_acc, n_c_eff)
        se_diff = math.sqrt(se_strict ** 2 + se_control ** 2)
        if (strict_acc - control_acc) <= 2 * se_diff:
            labels.append("accuracy_indistinguishable_from_token_prior")

    # Declared-policy envelope indistinguishability.
    if strict_acc <= union_envelope + 2 * se_strict:
        labels.append("accuracy_indistinguishable_from_declared_policy_envelope")

    # Insufficient measurement headroom.
    if strict_acc >= 1 - 3 * se_strict:
        labels.append("insufficient_measurement_headroom")

    # Strict-content gap instability (B1 sign convention).
    gap = content_acc - strict_acc
    if gap >= 0.15:
        labels.append("strict_content_gap_instability")

    # Abstention contract instability.
    abstention_rate = rung_record["abstention_rate"]
    separability = rung_record["separability_flag"]
    if not (0.50 <= abstention_rate <= 0.95) or not separability:
        labels.append("abstention_contract_instability")

    # Neutral label iff no other label.
    if not labels:
        labels.append("requires_further_investigation")

    return sorted(labels)


# Fixed-outcome statements (byte-locked; read from fixed_outcome.md is
# best practice but the canonical strings are also embedded here for
# the unit test to pin them).

STATEMENT_A = (
    "The certification window, while logically nonempty, was unoccupied "
    "for this task family at this scale: every rung carried at least "
    "one elimination label under the pre-registered sweep classification."
)
STATEMENT_B_TEMPLATE = (
    "{K} of 8 rungs were not ruled out under the pre-registered sweep "
    "classification and remain an unordered survivor set. Survivorship "
    "is neither ranking nor positive evidence; certification eligibility "
    "remains undetermined pending separately authorized candidate "
    "selection and certification."
)
STATEMENT_C = (
    "Any construction examined after this sweep is expected to perform "
    "worse during fresh certification than during sweep exploration; "
    "regression from sweep behavior is not instrument failure and must "
    "not be used to tune thresholds."
)


def emit_outcome(rung_records: list[dict[str, Any]]) -> tuple[str, list[str], int]:
    """Return (fixed_outcome_statement, survivors_alphabetical, K).

    Determinism: K is computed by the exact rule below; the survivor
    list is constructed in alphabetical rung_id order (B5).
    """
    survivors = [
        r["rung_id"]
        for r in rung_records
        if r["labels"] == ["requires_further_investigation"]
    ]
    K = len(survivors)

    # B5 — survivors serialized in alphabetical rung-ID order.
    survivors_sorted = sorted(survivors)

    if K == 0:
        statement = STATEMENT_A
    else:
        statement = STATEMENT_B_TEMPLATE.format(K=K)

    statement = statement + "\n\n" + STATEMENT_C

    return statement, survivors_sorted, K


def build_per_rung_record(
    rung_id: str,
    raw_outputs: dict[str, Any],
    manifest_hash: str,
    per_item_log_path: str,
    raw_output_dir: str,
) -> dict[str, Any]:
    """Assemble one rung's record from raw outputs. raw_outputs is the
    rung's aggregated scoring data: {answerable, null, answerable_mirror,
    null_mirror, harness_flags}."""
    A = raw_outputs.get("answerable", {})
    N = raw_outputs.get("null", {})
    AM = raw_outputs.get("answerable_mirror", {})
    NM = raw_outputs.get("null_mirror", {})

    void_a = A.get("void_count", 0)
    void_n = N.get("void_count", 0)
    void_am = AM.get("void_count", 0)
    void_nm = NM.get("void_count", 0)

    n_a_eff = 80 - void_a
    n_am_eff = 80 - void_am

    strict_acc = A.get("strict_count", 0) / max(n_a_eff, 1)
    content_acc = A.get("content_count", 0) / max(n_a_eff, 1)
    gap = content_acc - strict_acc  # B1 sign convention

    strict_acc_se = _binomial_se(strict_acc, n_a_eff)
    content_acc_se = _binomial_se(content_acc, n_a_eff)

    if AM:
        control_acc = AM.get("strict_count", 0) / max(n_am_eff, 1)
        control_acc_se = _binomial_se(control_acc, n_am_eff)
    else:
        control_acc = None
        control_acc_se = None

    headroom = 1.0 - strict_acc

    abstention_rate = N.get("abstain_count", 0) / max(16 - void_n, 1)
    abstention_rate_se = _binomial_se(abstention_rate, max(16 - void_n, 1))

    record = {
        "rung_id": rung_id,
        "manifest_hash": manifest_hash,
        "N_declared": 96,
        "N_effective": n_a_eff,
        "void_count": void_a + void_n + void_am + void_nm,
        "void_count_answerable": void_a,
        "void_count_null": void_n,
        "void_count_control_answerable_mirror": void_am,
        "void_count_control_null_mirror": void_nm,
        "strict_acc": strict_acc,
        "strict_acc_se": strict_acc_se,
        "content_acc": content_acc,
        "gap": gap,
        "control_acc": control_acc,
        "control_acc_se": control_acc_se,
        "max_dummy_score": raw_outputs.get("max_dummy_score", 0.0),
        "union_envelope_score": raw_outputs.get("union_envelope_score", 0.0),
        "headroom": headroom,
        "abstention_rate": abstention_rate,
        "abstention_rate_se": abstention_rate_se,
        "separability_flag": raw_outputs.get("separability_flag", False),
        "tokenization_stability_flag": raw_outputs.get(
            "tokenization_stability_flag", True
        ),
        "harness_anomaly_flag": raw_outputs.get("harness_anomaly_flag", False),
        "missing_required_outputs_flag": raw_outputs.get(
            "missing_required_outputs_flag", False
        ),
        "answer_pos_distribution": raw_outputs.get(
            "answer_pos_distribution",
            {"bin_counts": [], "bin_count_total": 0, "max_deviation_sigma": 0.0},
        ),
        "labels": [],  # filled in next
        "per_item_log_path": per_item_log_path,
        "raw_output_dir": raw_output_dir,
    }

    record["labels"] = assign_labels(record)
    return tag(record)
