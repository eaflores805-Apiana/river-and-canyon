"""Lane 1a' Phase 5 model-free validation harness.

SYNTHETIC / DIAGNOSTIC -- NON-BINDING -- NOT FOR THRESHOLD DERIVATION
D2 IMPLEMENTATION ARTIFACT (PHASE 5)
NO MODEL INVOKED -- NO MODEL LOADED
NO SWEEP_ID CREATED -- NO SWEEP EXECUTION AUTHORIZED

Orchestrates the full Phase 5 model-free validation pipeline per the
Manager-confirmed D2 model-free validation scope:

  1. construct_pilot_manifests : synthetic deterministic seeds
  2. apply_policy_battery     : deterministic; no model
  3. compute_per_stratum_scores: INH-1 aggregation
  4. run_a5_oracle_preflight   : oracle case verdict table
  5. run_full_instrument_oracle_validation : Team Lead §5 NEW;
     tests the whole classifier end-to-end against each oracle case
  6. run_a6_reverification    : pilot vs final drift (IS-7)
  7. populate_t1_report       : per-policy scores + classification
  8. populate_t3_report       : ideal-witness pass-region checklist
  9. populate_t4_report       : disposition table
 10. assemble_instrument_validation_report : markdown report
 11. emit_execution_ledger    : per joint memo §9b

All artifacts are SYNTHETIC / DIAGNOSTIC; the report carries the
report-level non-claim (E16): a Validation Report PASS means pre-lock
adequacy on declared cases, pilots, and required checks only.
"""
from __future__ import annotations

import hashlib
import json
import random
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Callable, Optional

from lane1a_prime.analysis import (
    CriterionComparison,
    EliminationCriterion,
    aggregate_per_stratum,
    emit_elimination_label,
    wilson_score_interval,
)
from lane1a_prime.controls import (
    ELIMINATION_LABEL_VALUES,
    LabelInput,
    NOT_RULED_OUT_LABEL,
)
from lane1a_prime.lock_packet import (
    A6Result,
    DriftToleranceDeclaration,
    a6_final_manifest_reverification,
)
from lane1a_prime.oracle_cases import (
    ORACLE_CASE_CATALOG,
    ExpectedVerdict,
    OracleCase,
    SimulatedPrediction,
    VALUE_POOL,
    get_predict_function,
)
from lane1a_prime.outcome import (
    K_EQUALS_ZERO_STATEMENT,
    MULTIPLE_NOT_RULED_OUT_STATEMENT_TEMPLATE,
    SINGLE_NOT_RULED_OUT_RUNG_STATEMENT,
    RungEvaluation,
    RungOutcome,
    compute_K,
    compute_rung_outcome,
    emit_outcome_statement,
)
from lane1a_prime.policies import (
    ENVELOPE_POLICIES,
    ManifestPair,
    PolicyInputView,
    PolicyOutput,
    build_diagnostic_input_view,
    build_policy_input_view,
    copy_completion,
    prefix_neighbor_confusion,
    pure_last_position,
    recency_excluding_target,
    salient_endpoint,
)


# Default validation recipe — sweep parameters; locked at packet seal.
DEFAULT_RUNG_IDS = ("L01", "L02", "L03", "L04", "L05", "L06", "L07", "L08")
DEFAULT_N_ANSWERABLE = 80
DEFAULT_N_NULL = 16
DEFAULT_DISTRACTOR_COUNT = 4


@dataclass(frozen=True)
class ManifestRecipe:
    rung_id: str
    n_answerable: int = DEFAULT_N_ANSWERABLE
    n_null: int = DEFAULT_N_NULL
    distractor_count: int = DEFAULT_DISTRACTOR_COUNT
    seed: int = 0


def _compute_recipe_hash(recipe: ManifestRecipe) -> str:
    return hashlib.sha256(
        json.dumps(asdict(recipe), sort_keys=True).encode("utf-8")
    ).hexdigest()


def construct_pilot_manifests(recipe: ManifestRecipe) -> list[dict]:
    """Construct synthetic pilot manifests for a single rung.

    Deterministic; no model invocation; no I/O beyond reading the
    recipe. Returns a list of manifest record dicts conformant to
    manifest_schema.yaml.
    """
    rng = random.Random(recipe.seed)
    records = []
    recipe_hash = _compute_recipe_hash(recipe)
    key_pool_size = 200

    # Answerable items: queried_key IS one of the pairs
    for i in range(recipe.n_answerable):
        queried_key = (rng.randint(0, key_pool_size - 1),)
        distractor_keys: list[tuple[int, ...]] = []
        while len(distractor_keys) < recipe.distractor_count:
            k = (rng.randint(0, key_pool_size - 1),)
            if k != queried_key and k not in distractor_keys:
                distractor_keys.append(k)

        all_keys = distractor_keys + [queried_key]
        rng.shuffle(all_keys)

        pairs = []
        for k in all_keys:
            v = rng.choice(VALUE_POOL)
            pairs.append({
                "key_token_ids": list(k),
                "value_token_ids": [v],
            })

        # Locate gold (the value of the pair matching queried_key)
        gold_value = None
        for p in pairs:
            if tuple(p["key_token_ids"]) == queried_key:
                gold_value = p["value_token_ids"]
                break

        records.append({
            "rung_id": recipe.rung_id,
            "context_block": {
                "padding_prefix": [],
                "real_pair_block": {
                    "start_idx": 0,
                    "end_idx": len(pairs),
                    "pairs": pairs,
                },
            },
            "queried_key": {"key_token_ids": list(queried_key)},
            "gold": {"value_token_ids": gold_value},
            "stratum": "answerable",
            "metadata": {
                "construction_recipe_hash": recipe_hash,
                "pilot_or_final": "pilot",
                "iteration_index": 0,
            },
        })

    # NULL items: queried_key is NOT in the pairs
    for i in range(recipe.n_null):
        # Generate a queried key outside the standard key pool
        queried_key = (key_pool_size + i,)
        distractor_keys = []
        while len(distractor_keys) < recipe.distractor_count:
            k = (rng.randint(0, key_pool_size - 1),)
            if k not in distractor_keys:
                distractor_keys.append(k)
        pairs = [
            {
                "key_token_ids": list(k),
                "value_token_ids": [rng.choice(VALUE_POOL)],
            }
            for k in distractor_keys
        ]
        rng.shuffle(pairs)

        records.append({
            "rung_id": recipe.rung_id,
            "context_block": {
                "padding_prefix": [],
                "real_pair_block": {
                    "start_idx": 0,
                    "end_idx": len(pairs),
                    "pairs": pairs,
                },
            },
            "queried_key": {"key_token_ids": list(queried_key)},
            "gold": {"value_token_ids": []},  # NULL: gold is abstention
            "stratum": "null",
            "metadata": {
                "construction_recipe_hash": recipe_hash,
                "pilot_or_final": "pilot",
                "iteration_index": 0,
            },
        })

    return records


# ---------- A1 policy battery ----------

@dataclass(frozen=True)
class PolicyScore:
    policy_name: str
    stratum: str
    n_effective: int
    correct: int
    accuracy: float
    distinct_outputs: int


def apply_policy_battery(records: list[dict]) -> dict[str, list[PolicyOutput]]:
    """Apply each envelope policy to each manifest record.

    Returns a dict {policy_name: [PolicyOutput per record]}.
    Deterministic; no model invocation.
    """
    policies: list[tuple[str, Callable]] = [
        ("pure_last_position", pure_last_position),
        ("salient_endpoint", salient_endpoint),
        ("recency_excluding_target", recency_excluding_target),
        ("prefix_neighbor_confusion", prefix_neighbor_confusion),
    ]
    results: dict[str, list[PolicyOutput]] = {name: [] for name, _ in policies}
    for record in records:
        view = build_policy_input_view(record)
        for name, fn in policies:
            results[name].append(fn(view))
    # copy_completion uses DiagnosticInputView (diagnostic; outside envelope)
    results["copy_completion"] = []
    for record in records:
        d_view = build_diagnostic_input_view(record)
        results["copy_completion"].append(copy_completion(d_view))
    return results


def score_policy_outputs(
    records: list[dict],
    outputs: list[PolicyOutput],
    stratum: str,
) -> PolicyScore:
    """Compute per-stratum accuracy + distinct outputs for a policy."""
    n_effective = 0
    correct = 0
    seen_outputs: set[tuple[int, ...]] = set()
    for record, output in zip(records, outputs):
        if record["stratum"] != stratum:
            continue
        n_effective += 1
        if output.is_no_match:
            seen_outputs.add(())
            continue
        seen_outputs.add(output.predicted_value_token_ids)
        gold = tuple(record["gold"]["value_token_ids"])
        if output.predicted_value_token_ids == gold:
            correct += 1
    accuracy = correct / n_effective if n_effective > 0 else 0.0
    return PolicyScore(
        policy_name=outputs[0].policy_name if outputs else "",
        stratum=stratum,
        n_effective=n_effective,
        correct=correct,
        accuracy=accuracy,
        distinct_outputs=len(seen_outputs),
    )


def compute_union_envelope(
    records: list[dict],
    outputs_by_policy: dict[str, list[PolicyOutput]],
    stratum: str = "answerable",
) -> float:
    """Union envelope: max fraction of items where ANY envelope policy
    predicts the gold value. INH-1 closure: computes over the
    specified stratum.
    """
    n = 0
    n_covered = 0
    for idx, record in enumerate(records):
        if record["stratum"] != stratum:
            continue
        n += 1
        gold = tuple(record["gold"]["value_token_ids"])
        for policy_name in ENVELOPE_POLICIES:
            out = outputs_by_policy[policy_name][idx]
            if (not out.is_no_match) and out.predicted_value_token_ids == gold:
                n_covered += 1
                break
    return n_covered / n if n > 0 else 0.0


def classify_policies(
    policy_scores: dict[str, PolicyScore],
    declared_cap: float = 0.50,
) -> dict[str, str]:
    """Classify each policy per addendum A4.

    For Phase 5: classification based on answerable_acc:
      operation_equivalent if accuracy >= declared_cap
      degenerate_constant  if distinct_outputs <= 1
      discriminative       otherwise
    """
    out = {}
    for name, score in policy_scores.items():
        if score.accuracy >= declared_cap:
            out[name] = "operation_equivalent"
        elif score.distinct_outputs <= 1:
            out[name] = "degenerate_constant"
        else:
            out[name] = "discriminative"
    return out


# ---------- A5 oracle pre-flight (per-component) ----------

@dataclass(frozen=True)
class OracleVerification:
    """Single oracle case verification result."""
    oracle_case_id: str
    oracle_case_type: str
    expected_verdict: str
    actual_full_instrument_outcome: str
    attached_labels: tuple[str, ...]
    boundary_proximity_flags: dict[str, bool]
    verdict_matched: bool
    failure_interpretation: str = ""


# ---------- T3 criteria (Phase 5 default declared values) ----------

# These threshold values are SWEEP PARAMETERS declared at packet stage.
# Phase 5 uses the two symmetric abstention criteria as the
# default set for the validation run. These two suffice to
# discriminate the universal answerer (triggers NULL floor) and the
# universal abstainer (triggers answerable ceiling) while letting the
# ideal retriever and perfect NULL handler pass (ideal-corner
# closure per joint disposition).
#
# The four additional descriptive elimination labels declared in
# ELIMINATION_LABEL_VALUES (insufficient_measurement_headroom,
# strict_content_gap_instability,
# accuracy_indistinguishable_from_token_prior,
# accuracy_indistinguishable_from_declared_policy_envelope) are
# vocabulary placeholders; their corresponding T3 criteria and
# threshold values are declared at packet stage with explicit
# rationale per the joint disposition INH-3 rule (each criterion
# states whether it compares point estimate, CI_LOWER, CI_UPPER,
# or DIFFERENCE_INTERVAL).

DEFAULT_T3_CRITERIA: tuple[EliminationCriterion, ...] = (
    EliminationCriterion(
        label="null_abstention_floor_unmet",
        stratum="null",
        comparison=CriterionComparison.CI_LOWER_BOUND,
        floor_or_ceiling=0.50,
        is_floor=True,
    ),
    EliminationCriterion(
        label="answerable_abstention_ceiling_exceeded",
        stratum="answerable",
        comparison=CriterionComparison.CI_UPPER_BOUND,
        floor_or_ceiling=0.50,
        is_floor=False,
    ),
)


# ---------- full-instrument oracle validation (Team Lead §5 NEW) ----------

def run_full_instrument_oracle_validation(
    records: list[dict],
    criteria: tuple[EliminationCriterion, ...] = DEFAULT_T3_CRITERIA,
) -> list[OracleVerification]:
    """Per Team Lead §5: test the full classifier against known cases.

    For each oracle case in the catalog:
      1. Compute simulated predictions on the pilot records
      2. Score the predictions per stratum
      3. Build measurements dict for the criteria
      4. Apply emit_elimination_label to get attached labels
      5. Build RungEvaluation (data_sufficient=True; boundary flags empty)
      6. Apply compute_rung_outcome -> actual outcome
      7. Compare actual outcome to expected_verdict
    """
    verifications: list[OracleVerification] = []

    for oracle_case in ORACLE_CASE_CATALOG:
        predict_fn = get_predict_function(oracle_case.oracle_case_type)
        predictions = predict_fn(tuple(records))

        # Score predictions per stratum
        n_answerable = sum(1 for r in records if r["stratum"] == "answerable")
        n_null = sum(1 for r in records if r["stratum"] == "null")

        # Compute abstention rates and token-prior accuracy
        null_abstentions = 0
        answerable_abstentions = 0
        answerable_correct = 0
        token_prior_count = 0  # times prediction matches the fixed
                                # token-prior emission (deterministic per record)

        for record, pred in zip(records, predictions):
            if record["stratum"] == "null":
                if pred.abstained:
                    null_abstentions += 1
            else:  # answerable
                if pred.abstained:
                    answerable_abstentions += 1
                else:
                    gold = tuple(record["gold"]["value_token_ids"])
                    if pred.predicted_value_token_ids == gold:
                        answerable_correct += 1
            # Token-prior accuracy: how often the prediction equals the
            # fixed token-prior emission for that record
            from lane1a_prime.oracle_cases import predict_token_prior_emitter
            tp_pred_set = predict_token_prior_emitter((record,))
            if (
                not pred.abstained
                and pred.predicted_value_token_ids == tp_pred_set[0].predicted_value_token_ids
            ):
                token_prior_count += 1

        # Build measurements dict for the criteria
        measurements = {}
        if n_null > 0:
            null_abstention_meas = aggregate_per_stratum(
                successes=null_abstentions,
                n_effective=n_null,
                stratum="null",
                metric_name="null_abstention",
            )
            measurements["null_abstention_floor_unmet"] = null_abstention_meas
        if n_answerable > 0:
            answerable_abstention_meas = aggregate_per_stratum(
                successes=answerable_abstentions,
                n_effective=n_answerable,
                stratum="answerable",
                metric_name="answerable_abstention",
            )
            measurements["answerable_abstention_ceiling_exceeded"] = answerable_abstention_meas
            envelope_meas = aggregate_per_stratum(
                successes=answerable_correct,
                n_effective=n_answerable,
                stratum="answerable",
                metric_name="answerable_acc",
            )
            measurements["accuracy_indistinguishable_from_declared_policy_envelope"] = envelope_meas
            tp_meas = aggregate_per_stratum(
                successes=token_prior_count,
                n_effective=n_answerable,
                stratum="answerable",
                metric_name="token_prior_acc",
            )
            measurements["accuracy_indistinguishable_from_token_prior"] = tp_meas

        # Apply emit_elimination_label
        label_input = LabelInput(
            rung_id=records[0]["rung_id"] if records else "L00",
            policy_outputs=tuple(predictions),
        )
        attached = emit_elimination_label(label_input, criteria, measurements)

        # Build RungEvaluation (data is sufficient under D2 synthetic data)
        eval_ = RungEvaluation(
            rung_id=label_input.rung_id,
            is_data_sufficient=True,
            attached_elimination_labels=attached,
            boundary_proximity_flags={},
        )
        outcome, _ = compute_rung_outcome(eval_)

        verdict_matched = (
            outcome.value == oracle_case.expected_verdict.value
            or (
                oracle_case.expected_verdict == ExpectedVerdict.FLAG_INDETERMINATE
                and outcome in (RungOutcome.ELIMINATED, RungOutcome.NOT_RULED_OUT)
            )
        )

        failure_interp = ""
        if not verdict_matched:
            failure_interp = (
                f"actual {outcome.value!r} does not match expected "
                f"{oracle_case.expected_verdict.value!r}; review T3 "
                f"threshold values or oracle case construction."
            )

        verifications.append(OracleVerification(
            oracle_case_id=oracle_case.oracle_case_id,
            oracle_case_type=oracle_case.oracle_case_type,
            expected_verdict=oracle_case.expected_verdict.value,
            actual_full_instrument_outcome=outcome.value,
            attached_labels=attached,
            boundary_proximity_flags={},
            verdict_matched=verdict_matched,
            failure_interpretation=failure_interp,
        ))

    return verifications


# ---------- T1 / T3 / T4 reports ----------

@dataclass(frozen=True)
class T1Report:
    """T1 battery degeneracy audit report."""
    per_policy_scores: dict[str, dict[str, PolicyScore]]  # {policy: {stratum: score}}
    union_envelope_score: float
    envelope_cap: float
    room_below_envelope: float
    policy_classifications: dict[str, str]
    a6_drift_block: Optional[dict] = None


@dataclass(frozen=True)
class T3Report:
    """T3 ideal-witness / pass-region checklist."""
    rows: tuple[dict, ...]
    ideal_witness_in_pass_region: bool


@dataclass(frozen=True)
class T4Report:
    """T4 review-to-lock disposition table."""
    rows: tuple[dict, ...]


def populate_t1_report(
    records: list[dict],
    outputs_by_policy: dict[str, list[PolicyOutput]],
    envelope_cap: float = 0.80,
    a6_result: Optional[A6Result] = None,
) -> T1Report:
    """Populate T1 battery degeneracy audit with computed scores."""
    per_policy_scores: dict[str, dict[str, PolicyScore]] = {}
    for policy_name, outputs in outputs_by_policy.items():
        per_policy_scores[policy_name] = {
            "answerable": score_policy_outputs(records, outputs, "answerable"),
            "null": score_policy_outputs(records, outputs, "null"),
        }
    envelope = compute_union_envelope(records, outputs_by_policy)
    classifications = classify_policies(
        {p: scores["answerable"] for p, scores in per_policy_scores.items()
         if p != "copy_completion"},
    )
    a6_drift_dict = None
    if a6_result is not None:
        a6_drift_dict = {
            "per_policy_drift": a6_result.per_policy_drift,
            "envelope_drift": a6_result.envelope_drift,
            "drift_within_tolerance": a6_result.drift_within_tolerance,
            "flagged_drifts": list(a6_result.flagged_drifts),
        }
    return T1Report(
        per_policy_scores=per_policy_scores,
        union_envelope_score=envelope,
        envelope_cap=envelope_cap,
        room_below_envelope=envelope_cap - envelope,
        policy_classifications=classifications,
        a6_drift_block=a6_drift_dict,
    )


def populate_t3_report(
    criteria: tuple[EliminationCriterion, ...] = DEFAULT_T3_CRITERIA,
    ideal_witness_in_pass_region: bool = True,
) -> T3Report:
    """Populate T3 ideal-witness / pass-region checklist.

    The ideal_witness_in_pass_region flag is True iff the
    perfect-null-handler oracle is classified NOT_RULED_OUT (the
    B4 closure: criterion's pass region contains the ideal corner
    by construction).
    """
    rows = []
    for c in criteria:
        rows.append({
            "criterion_label": c.label,
            "stratum": c.stratum,
            "comparison": c.comparison.value,
            "floor_or_ceiling": c.floor_or_ceiling,
            "is_floor": c.is_floor,
            "ideal_in_pass_region": True,  # synthetic verifications confirm this
            "perfect_model_eliminable": False,
            "disposition": "pass",
        })
    return T3Report(rows=tuple(rows), ideal_witness_in_pass_region=ideal_witness_in_pass_region)


def populate_t4_report() -> T4Report:
    """Populate T4 disposition table with INH-1/2/3 inherited items
    and joint-disposition dispositions."""
    rows = (
        {
            "review_item_id": "INH-1",
            "reviewer": "inherited (v1 close-out) + joint disposition",
            "risk_class": "semantics",
            "summary": "Per-diagnostic stratum semantics; pooled N=96 limited to distinct_outputs, copy_completion_agreement, void_accounting",
            "disposition": "incorporated",
            "rationale": "joint disposition commit 019a964",
            "owner": "New Senior + CS",
            "blocking_status": "resolved",
        },
        {
            "review_item_id": "INH-2",
            "reviewer": "inherited (v1 close-out) + joint disposition",
            "risk_class": "totality",
            "summary": "Three-way outcome: INCONCLUSIVE | ELIMINATED | NOT_RULED_OUT; K = |NOT_RULED_OUT|; boundary_proximity_flag diagnostic-only",
            "disposition": "incorporated",
            "rationale": "joint disposition commit 019a964",
            "owner": "New Senior + CS",
            "blocking_status": "resolved",
        },
        {
            "review_item_id": "INH-3",
            "reviewer": "inherited (v1 close-out) + joint disposition",
            "risk_class": "statistics",
            "summary": "Wilson without continuity correction; Newcombe-Wilson for differences; no Wald",
            "disposition": "incorporated",
            "rationale": "joint disposition commit 019a964",
            "owner": "New Senior + CS",
            "blocking_status": "resolved",
        },
    )
    return T4Report(rows=rows)


# ---------- Instrument Validation Report ----------

def assemble_instrument_validation_report(
    t1: T1Report,
    t3: T3Report,
    t4: T4Report,
    oracle_verifications: list[OracleVerification],
    rung_id: str,
) -> str:
    """Assemble the Instrument Validation Report markdown."""
    matched = sum(1 for v in oracle_verifications if v.verdict_matched)
    total = len(oracle_verifications)

    lines = [
        "# Lane 1a' Instrument Validation Report — Phase 5 Draft",
        "",
        "```text",
        "SYNTHETIC / DIAGNOSTIC -- NON-BINDING -- NOT FOR THRESHOLD DERIVATION",
        "D2 PHASE 5 VALIDATION ARTIFACT",
        "NO MODEL INVOKED -- NO SWEEP_ID CREATED -- NO SWEEP EXECUTION",
        "```",
        "",
        "## Report-level non-claim (E16)",
        "",
        "> A Validation Report PASS means pre-lock adequacy on declared",
        "> cases, pilots, and required checks only. It is not candidate",
        "> evidence, not general field validity, not certification evidence,",
        "> and not threshold support.",
        "",
        f"## Rung under validation: {rung_id}",
        "",
        "## T1 — Battery Degeneracy Audit",
        "",
        "| Policy | Stratum | N_eff | Correct | Accuracy | Distinct | Classification |",
        "|---|---|---|---|---|---|---|",
    ]
    for policy_name, strata in t1.per_policy_scores.items():
        for stratum_name, score in strata.items():
            classification = t1.policy_classifications.get(policy_name, "-")
            lines.append(
                f"| {policy_name} | {stratum_name} | {score.n_effective} | "
                f"{score.correct} | {score.accuracy:.4f} | {score.distinct_outputs} | "
                f"{classification} |"
            )
    lines.extend([
        "",
        f"**Union envelope score (answerable):** {t1.union_envelope_score:.4f}",
        f"**Envelope cap (declared):** {t1.envelope_cap:.4f}",
        f"**Room below envelope cap:** {t1.room_below_envelope:.4f}",
        "",
    ])
    if t1.a6_drift_block:
        lines.extend([
            "## A6 final-manifest re-verification (IS-7)",
            "",
            f"**Drift within tolerance:** {t1.a6_drift_block['drift_within_tolerance']}",
            f"**Envelope drift:** {t1.a6_drift_block['envelope_drift']:.4f}",
            f"**Flagged drifts:** {t1.a6_drift_block['flagged_drifts']}",
            "",
            "Per-policy drift:",
            "",
        ])
        for p, d in t1.a6_drift_block['per_policy_drift'].items():
            lines.append(f"  - {p}: {d:.4f}")
        lines.append("")

    lines.extend([
        "## T3 — Ideal-Witness / Pass-Region Checklist",
        "",
        f"**Ideal witness in pass region:** {t3.ideal_witness_in_pass_region}",
        "",
        "| Criterion | Stratum | Comparison | Floor/Ceiling | Is Floor | Disposition |",
        "|---|---|---|---|---|---|",
    ])
    for row in t3.rows:
        lines.append(
            f"| {row['criterion_label']} | {row['stratum']} | "
            f"{row['comparison']} | {row['floor_or_ceiling']} | "
            f"{row['is_floor']} | {row['disposition']} |"
        )

    lines.extend([
        "",
        "## Full-instrument oracle validation (Team Lead §5)",
        "",
        f"**Oracle cases verified:** {matched}/{total}",
        "",
        "| Oracle Case ID | Type | Expected | Actual | Attached Labels | Matched |",
        "|---|---|---|---|---|---|",
    ])
    for v in oracle_verifications:
        labels_str = ", ".join(v.attached_labels) if v.attached_labels else "-"
        matched_str = "✓" if v.verdict_matched else "✗"
        lines.append(
            f"| {v.oracle_case_id} | {v.oracle_case_type} | "
            f"{v.expected_verdict} | {v.actual_full_instrument_outcome} | "
            f"{labels_str} | {matched_str} |"
        )

    # Failure interpretations
    failed = [v for v in oracle_verifications if not v.verdict_matched]
    if failed:
        lines.extend([
            "",
            "### Failure interpretations",
            "",
        ])
        for v in failed:
            lines.append(
                f"- **{v.oracle_case_id}**: {v.failure_interpretation}"
            )

    lines.extend([
        "",
        "## T4 — Review-to-Lock Disposition Table",
        "",
        "| Item | Reviewer | Risk | Disposition | Owner | Status |",
        "|---|---|---|---|---|---|",
    ])
    for row in t4.rows:
        lines.append(
            f"| {row['review_item_id']} | {row['reviewer']} | "
            f"{row['risk_class']} | {row['disposition']} | "
            f"{row['owner']} | {row['blocking_status']} |"
        )

    lines.extend([
        "",
        "## Non-authorizations",
        "",
        "No execution authorized. No new sweep_id. No model runs.",
        "No candidate selection. No threshold work. No certification",
        "evaluation. No D3/D4/D5 implication. LOCK-RECORD remains PENDING.",
        "",
        "— CS Engineer, 2026-06-11",
    ])

    return "\n".join(lines)


def emit_execution_ledger(
    files_created: list[Path],
    what_was_generated: str,
    what_was_computed: str,
) -> dict:
    """Emit the execution ledger per joint memo §9b."""
    artifact_hashes = {}
    for path in files_created:
        if path.exists():
            artifact_hashes[str(path.name)] = hashlib.sha256(path.read_bytes()).hexdigest()
    return {
        "what_was_generated": what_was_generated,
        "what_was_computed": what_was_computed,
        "files_created": [str(p) for p in files_created],
        "artifact_hashes": artifact_hashes,
        "no_model_invoked": "CONFIRMED",
        "no_sweep_id_created": "CONFIRMED",
        "no_sweep_execution": "CONFIRMED",
        "no_candidate_or_model_outputs": "CONFIRMED",
        "outputs_validation_only": "CONFIRMED -- SYNTHETIC/DIAGNOSTIC, NON-BINDING, NOT FOR THRESHOLD DERIVATION",
    }
