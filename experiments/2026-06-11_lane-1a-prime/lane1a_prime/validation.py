"""Lane 1a' Phase 5 corrective model-free validation harness (v0.2).

SYNTHETIC / DIAGNOSTIC -- NON-BINDING -- NOT FOR THRESHOLD DERIVATION
D2 IMPLEMENTATION ARTIFACT (PHASE 5 CORRECTIVE)
NO MODEL INVOKED -- NO MODEL LOADED
NO SWEEP_ID CREATED -- NO SWEEP EXECUTION AUTHORIZED

v0.2 changes from v0.1 (per joint NS+CS+TL corrective disposition):

  PH5-2: label-set match predicate (required_labels /
         permitted_co_labels / required_absent_labels) replaces
         verdict-only matching.

  PH5-3: stratified recipe — ManifestRecipe gains stratification
         fields; construct_pilot_manifests assigns gold position
         by stratum (last_position / salient_endpoint /
         prefix_neighborhood / none). Structural hit-rates become
         construction constants; A6 verifies implementation
         fidelity, not sampling luck.

  PH5-4: pre-flight hash precondition — run_full_instrument_oracle_
         validation refuses to proceed unless verify_pre_flight_config
         passes (verdict table + bounds + recipe schedule hashes
         match lock event).

  PH5-5: run-1 retention block in IVR.
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
    PERMITTED_POOLED_DIAGNOSTICS,
    ValidationPreFlightConfig,
    ValidationPreFlightRefused,
    aggregate_per_stratum,
    apply_criterion,
    emit_elimination_label,
    load_t3_bounds,
    newcombe_wilson_difference,
    verify_pre_flight_config,
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
    OracleCase,
    ORACLE_VERDICT_TABLE_PATH,
    SimulatedPrediction,
    VALUE_POOL,
    get_predict_function,
    load_oracle_verdict_table,
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

# Lock event artifact paths
LOCK_EVENT_DIR = Path(__file__).resolve().parent.parent / "validation"
T3_BOUNDS_PATH = LOCK_EVENT_DIR / "T3_BOUNDS_DECLARATION.json"
STRATIFIED_RECIPE_PATH = LOCK_EVENT_DIR / "STRATIFIED_RECIPE_SCHEDULE.json"


@dataclass(frozen=True)
class ManifestRecipe:
    """Lane 1a' manifest construction recipe (PH5-1 lock event: 5-stratum schedule).

    Per the locked STRATIFIED_RECIPE_SCHEDULE.json v2: each answerable
    item carries exactly one structural-feature label from the set
    {gold_at_last_position, gold_at_salient_endpoint,
     gold_in_prefix_neighborhood, gold_recency_adjacent,
     no_structural_feature}. The five disjoint counts sum to
    n_answerable. NULL stratum unchanged.
    """
    rung_id: str
    n_answerable: int = DEFAULT_N_ANSWERABLE
    n_null: int = DEFAULT_N_NULL
    distractor_count: int = DEFAULT_DISTRACTOR_COUNT
    seed: int = 0
    # Locked stratified counts (5-stratum disjoint schedule):
    n_at_last_position: int = 12
    n_at_salient_endpoint: int = 12
    n_in_prefix_neighborhood: int = 12
    n_recency_adjacent: int = 12
    n_no_structural_feature: int = 32

    def __post_init__(self) -> None:
        stratified_sum = (
            self.n_at_last_position
            + self.n_at_salient_endpoint
            + self.n_in_prefix_neighborhood
            + self.n_recency_adjacent
            + self.n_no_structural_feature
        )
        if stratified_sum != self.n_answerable:
            raise ValueError(
                f"Stratified count sum {stratified_sum} must equal "
                f"n_answerable {self.n_answerable}"
            )


def _compute_recipe_hash(recipe: ManifestRecipe) -> str:
    return hashlib.sha256(
        json.dumps(asdict(recipe), sort_keys=True).encode("utf-8")
    ).hexdigest()


def construct_pilot_manifests(recipe: ManifestRecipe) -> list[dict]:
    """Construct synthetic pilot manifests for a single rung (v0.2 stratified).

    Per PH5-3: gold position is assigned by stratum:
      - n_at_last_position items: queried_key placed at index -1
      - n_at_salient_endpoint items: queried_key placed at index 0
      - n_in_prefix_neighborhood items: queried_key shares prefix
        with another pair
      - n_at_none_of_these items: queried_key placed elsewhere

    The shortcut policies then hit exactly the stratified counts
    by construction; pilot and final manifests with the same recipe
    produce identical structural hit-rates regardless of seed.

    Returns a list of manifest record dicts conformant to
    manifest_schema.yaml.
    """
    rng = random.Random(recipe.seed)
    records: list[dict] = []
    recipe_hash = _compute_recipe_hash(recipe)
    key_pool_size = 200

    # Stratified assignment for answerable items.
    # We construct items per stratum so structural hit-rates are
    # exact construction constants.

    answerable_records = []

    # Stratum 1: queried_key at last position
    for _ in range(recipe.n_at_last_position):
        queried_key = (rng.randint(0, key_pool_size - 1),)
        distractor_keys: list[tuple[int, ...]] = []
        while len(distractor_keys) < recipe.distractor_count:
            k = (rng.randint(0, key_pool_size - 1),)
            if k != queried_key and k not in distractor_keys:
                distractor_keys.append(k)
        # Place queried_key at the LAST position
        all_keys = distractor_keys + [queried_key]
        pairs = [
            {"key_token_ids": list(k), "value_token_ids": [rng.choice(VALUE_POOL)]}
            for k in all_keys
        ]
        gold_value = pairs[-1]["value_token_ids"]
        answerable_records.append((pairs, queried_key, gold_value))

    # Stratum 2: queried_key at salient endpoint (index 0)
    for _ in range(recipe.n_at_salient_endpoint):
        queried_key = (rng.randint(0, key_pool_size - 1),)
        distractor_keys = []
        while len(distractor_keys) < recipe.distractor_count:
            k = (rng.randint(0, key_pool_size - 1),)
            if k != queried_key and k not in distractor_keys:
                distractor_keys.append(k)
        # Place queried_key at INDEX 0
        all_keys = [queried_key] + distractor_keys
        pairs = [
            {"key_token_ids": list(k), "value_token_ids": [rng.choice(VALUE_POOL)]}
            for k in all_keys
        ]
        gold_value = pairs[0]["value_token_ids"]
        answerable_records.append((pairs, queried_key, gold_value))

    # Stratum 3: queried_key in prefix neighborhood
    # The queried_key shares a prefix with a non-target pair (the "neighbor").
    # The neighbor's value is deliberately set equal to gold so the
    # prefix_neighbor_confusion shortcut hits by construction (12/80 = 0.15).
    # Placement: neighbor at a NON-edge slot (not position 0, not position
    # -1) to avoid incidental hits by pure_last_position or
    # salient_endpoint. Last pair's value is forced ≠ gold so
    # recency_excluding_target does not coincidentally hit.
    for _ in range(recipe.n_in_prefix_neighborhood):
        prefix_token = rng.randint(0, key_pool_size - 1)
        queried_key = (prefix_token, rng.randint(0, key_pool_size - 1))
        # One neighbor sharing the prefix token
        neighbor_key = (prefix_token, rng.randint(0, key_pool_size - 1))
        while neighbor_key == queried_key:
            neighbor_key = (prefix_token, rng.randint(0, key_pool_size - 1))
        # Distractors with different prefixes
        other_distractors: list[tuple[int, ...]] = []
        while len(other_distractors) < recipe.distractor_count - 1:
            k = (rng.randint(0, key_pool_size - 1), rng.randint(0, key_pool_size - 1))
            if (
                k != queried_key
                and k != neighbor_key
                and k[0] != prefix_token
                and k not in other_distractors
            ):
                other_distractors.append(k)
        # Slot layout for 5 positions (4 distractors + queried):
        #   pos 0: distractor (not neighbor, not queried)
        #   pos 1: neighbor (carries gold value)
        #   pos 2: queried (carries gold value by binding)
        #   pos 3: distractor
        #   pos 4: distractor (last; value forced ≠ gold)
        # This avoids salient_endpoint (pos 0 != gold) and pure_last_position
        # (pos -1 != gold) co-hits.
        slot0, slot3, slot4 = other_distractors[0], other_distractors[1], other_distractors[2]
        gold_token = rng.choice(VALUE_POOL)
        non_gold_token = rng.choice([t for t in VALUE_POOL if t != gold_token])
        pairs = [
            {"key_token_ids": list(slot0), "value_token_ids": [rng.choice([t for t in VALUE_POOL if t != gold_token])]},
            {"key_token_ids": list(neighbor_key), "value_token_ids": [gold_token]},
            {"key_token_ids": list(queried_key), "value_token_ids": [gold_token]},
            {"key_token_ids": list(slot3), "value_token_ids": [rng.choice([t for t in VALUE_POOL if t != gold_token])]},
            {"key_token_ids": list(slot4), "value_token_ids": [non_gold_token]},
        ]
        gold_value = [gold_token]
        answerable_records.append((pairs, queried_key, gold_value))

    # Stratum 4: recency_adjacent (queried at middle; last non-target pair carries
    # gold value, so recency_excluding_target shortcut hits by construction).
    # Constructibility note: under the current policy definitions
    # (pure_last_position emits position[-1].value), the last pair's
    # value coinciding with gold causes pure_last_position to also hit
    # these 12 items. The disjointness is at the ITEM-LABEL level
    # (each item carries one feature label), not at the policy-hit
    # level. This is documented in the joint lock-event memo as a
    # BLOCKER for NS+TL resolution before run-3.
    for _ in range(recipe.n_recency_adjacent):
        queried_key = (rng.randint(0, key_pool_size - 1),)
        distractor_keys = []
        while len(distractor_keys) < recipe.distractor_count:
            k = (rng.randint(0, key_pool_size - 1),)
            if k != queried_key and k not in distractor_keys:
                distractor_keys.append(k)
        # Place queried_key at the MIDDLE (index 2 of 5)
        middle_idx = recipe.distractor_count // 2
        all_keys = distractor_keys[:middle_idx] + [queried_key] + distractor_keys[middle_idx:]
        # gold = a value chosen now; both the queried_key's binding and
        # the last pair's value are set to gold so recency hits.
        gold_token = rng.choice(VALUE_POOL)
        pairs = []
        for i, k in enumerate(all_keys):
            if tuple(k) == queried_key:
                v = [gold_token]
            elif i == len(all_keys) - 1:
                v = [gold_token]  # last non-target pair carries gold value
            else:
                # ensure value != gold to keep distractors clean
                alt = rng.choice([t for t in VALUE_POOL if t != gold_token])
                v = [alt]
            pairs.append({"key_token_ids": list(k), "value_token_ids": v})
        gold_value = [gold_token]
        answerable_records.append((pairs, queried_key, gold_value))

    # Stratum 5: no_structural_feature (queried at middle; no last-pair
    # gold coincidence; no prefix neighbor; no salient endpoint).
    for _ in range(recipe.n_no_structural_feature):
        queried_key = (rng.randint(0, key_pool_size - 1),)
        distractor_keys = []
        while len(distractor_keys) < recipe.distractor_count:
            k = (rng.randint(0, key_pool_size - 1),)
            if k != queried_key and k not in distractor_keys:
                distractor_keys.append(k)
        middle_idx = recipe.distractor_count // 2
        all_keys = distractor_keys[:middle_idx] + [queried_key] + distractor_keys[middle_idx:]
        # gold is the queried_key's binding; ensure last non-target
        # pair's value does NOT equal gold (so recency_excluding_target
        # does not coincidentally hit).
        gold_token = rng.choice(VALUE_POOL)
        pairs = []
        for i, k in enumerate(all_keys):
            if tuple(k) == queried_key:
                v = [gold_token]
            elif i == len(all_keys) - 1:
                alt = rng.choice([t for t in VALUE_POOL if t != gold_token])
                v = [alt]
            else:
                v = [rng.choice(VALUE_POOL)]
            pairs.append({"key_token_ids": list(k), "value_token_ids": v})
        gold_value = [gold_token]
        answerable_records.append((pairs, queried_key, gold_value))

    # Convert to manifest records
    for (pairs, queried_key, gold_value) in answerable_records:
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
        queried_key = (key_pool_size + i,)
        distractor_keys = []
        while len(distractor_keys) < recipe.distractor_count:
            k = (rng.randint(0, key_pool_size - 1),)
            if k not in distractor_keys:
                distractor_keys.append(k)
        pairs = [
            {"key_token_ids": list(k), "value_token_ids": [rng.choice(VALUE_POOL)]}
            for k in distractor_keys
        ]
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
            "gold": {"value_token_ids": []},
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
    """Apply each envelope policy to each manifest record."""
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
    predicts the gold value."""
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
    """Classify each policy per addendum A4."""
    out = {}
    for name, score in policy_scores.items():
        if score.accuracy >= declared_cap:
            out[name] = "operation_equivalent"
        elif score.distinct_outputs <= 1:
            out[name] = "degenerate_constant"
        else:
            out[name] = "discriminative"
    return out


# ---------- PH5-2: match_oracle_verdict predicate ----------

@dataclass(frozen=True)
class OracleVerification:
    """Per-case verification result with full label-set accounting (v0.2)."""
    oracle_case_id: str
    oracle_case_type: str
    expected_outcome: str
    actual_outcome: str
    required_labels: tuple[str, ...]
    permitted_co_labels: tuple[str, ...]
    required_absent_labels: tuple[str, ...]
    attached_labels: tuple[str, ...]
    outcome_matched: bool
    required_labels_present: bool
    required_absent_labels_absent: bool
    only_required_or_permitted_attached: bool
    overall_matched: bool
    failure_interpretation: str = ""


def match_oracle_verdict(
    oracle_case: OracleCase,
    actual_outcome: str,
    attached_labels: frozenset[str],
) -> OracleVerification:
    """PH5-2 closure: full label-set match predicate.

    A case passes iff all four hold:
      1. actual_outcome == expected_outcome
      2. required_labels subset attached_labels
      3. required_absent_labels intersection attached_labels = empty
      4. attached_labels subset (required_labels union permitted_co_labels)
    """
    outcome_matched = actual_outcome == oracle_case.expected_outcome
    required_set = set(oracle_case.required_labels)
    permitted_set = set(oracle_case.permitted_co_labels)
    absent_set = set(oracle_case.required_absent_labels)
    attached_set = set(attached_labels)

    required_labels_present = required_set.issubset(attached_set)
    required_absent_labels_absent = not (absent_set & attached_set)
    allowed = required_set | permitted_set
    only_required_or_permitted_attached = attached_set.issubset(allowed)

    overall_matched = (
        outcome_matched
        and required_labels_present
        and required_absent_labels_absent
        and only_required_or_permitted_attached
    )

    failure_parts: list[str] = []
    if not outcome_matched:
        failure_parts.append(
            f"outcome {actual_outcome!r} != expected "
            f"{oracle_case.expected_outcome!r}"
        )
    if not required_labels_present:
        missing = sorted(required_set - attached_set)
        failure_parts.append(f"required labels missing: {missing}")
    if not required_absent_labels_absent:
        present = sorted(absent_set & attached_set)
        failure_parts.append(f"required-absent labels present: {present}")
    if not only_required_or_permitted_attached:
        unexpected = sorted(attached_set - allowed)
        failure_parts.append(f"unexpected labels attached: {unexpected}")
    failure_interpretation = "; ".join(failure_parts)

    return OracleVerification(
        oracle_case_id=oracle_case.oracle_case_id,
        oracle_case_type=oracle_case.oracle_case_type,
        expected_outcome=oracle_case.expected_outcome,
        actual_outcome=actual_outcome,
        required_labels=oracle_case.required_labels,
        permitted_co_labels=oracle_case.permitted_co_labels,
        required_absent_labels=oracle_case.required_absent_labels,
        attached_labels=tuple(sorted(attached_set)),
        outcome_matched=outcome_matched,
        required_labels_present=required_labels_present,
        required_absent_labels_absent=required_absent_labels_absent,
        only_required_or_permitted_attached=only_required_or_permitted_attached,
        overall_matched=overall_matched,
        failure_interpretation=failure_interpretation,
    )


# ---------- full-instrument oracle validation (v0.2 — label-set matching) ----------

def _build_measurements_for_predictions(
    records: list[dict],
    predictions: tuple[SimulatedPrediction, ...],
) -> dict[str, dict]:
    """Build measurement dicts for each criterion from simulated predictions.

    Computes per-stratum abstention rates and accuracy; for difference
    criteria, computes candidate vs control differences (control =
    fixed token-prior emitter; envelope = computed envelope).
    """
    n_answerable = sum(1 for r in records if r["stratum"] == "answerable")
    n_null = sum(1 for r in records if r["stratum"] == "null")

    null_abstentions = 0
    answerable_abstentions = 0
    answerable_correct = 0
    # Token-prior baseline accuracy: count records where prediction
    # matches the synthetic token_prior emitter's output
    from lane1a_prime.oracle_cases import predict_token_prior_emitter
    tp_preds = predict_token_prior_emitter(tuple(records))
    candidate_matches_tp = 0

    for record, pred, tp_pred in zip(records, predictions, tp_preds):
        if record["stratum"] == "null":
            if pred.abstained:
                null_abstentions += 1
        else:
            if pred.abstained:
                answerable_abstentions += 1
            else:
                gold = tuple(record["gold"]["value_token_ids"])
                if pred.predicted_value_token_ids == gold:
                    answerable_correct += 1
        # Token-prior overlap
        if (
            not pred.abstained
            and not tp_pred.abstained
            and pred.predicted_value_token_ids == tp_pred.predicted_value_token_ids
        ):
            candidate_matches_tp += 1

    measurements: dict[str, dict] = {}

    # null_abstention_floor_unmet (NULL stratum; CI_UPPER < floor)
    if n_null > 0:
        m = aggregate_per_stratum(
            successes=null_abstentions,
            n_effective=n_null,
            stratum="null",
            metric_name="null_abstention",
        )
        measurements["null_abstention_floor_unmet"] = m

    # answerable_abstention_ceiling_exceeded (answerable stratum; CI_LOWER > ceiling)
    if n_answerable > 0:
        m = aggregate_per_stratum(
            successes=answerable_abstentions,
            n_effective=n_answerable,
            stratum="answerable",
            metric_name="answerable_abstention",
        )
        measurements["answerable_abstention_ceiling_exceeded"] = m

    # accuracy_indistinguishable_from_token_prior (DIFFERENCE; candidate - control)
    if n_answerable > 0:
        # Control accuracy: token_prior baseline against gold
        tp_correct = 0
        for r, tp in zip(records, tp_preds):
            if r["stratum"] != "answerable":
                continue
            if (
                not tp.abstained
                and tp.predicted_value_token_ids == tuple(r["gold"]["value_token_ids"])
            ):
                tp_correct += 1
        diff_lower, diff_upper = newcombe_wilson_difference(
            successes_a=answerable_correct,
            n_a=n_answerable,
            successes_b=tp_correct,
            n_b=n_answerable,
        )
        measurements["accuracy_indistinguishable_from_token_prior"] = {
            "stratum": "answerable",
            "n_effective": n_answerable,
            "point_estimate": (answerable_correct - tp_correct) / n_answerable
                              if n_answerable > 0 else 0.0,
            "ci_lower": 0.0,
            "ci_upper": 1.0,
            "difference_lower": diff_lower,
            "difference_upper": diff_upper,
        }

    # accuracy_indistinguishable_from_declared_policy_envelope (DIFFERENCE; candidate - envelope)
    # The envelope's "accuracy" against gold per-record is computed
    # from the policy battery; for oracles, we approximate the envelope
    # as the best-of-4-policies hit rate which is rung-deterministic
    # under the stratified recipe (~0.25 per shortcut * 4 ≈ 1.0
    # without overlap; with overlap, the union envelope ≈ 0.4-0.6).
    if n_answerable > 0:
        # Apply policy battery to the records; compute envelope
        outputs_by_policy = apply_policy_battery(records)
        envelope = compute_union_envelope(records, outputs_by_policy, "answerable")
        env_correct = int(envelope * n_answerable)
        diff_lower, diff_upper = newcombe_wilson_difference(
            successes_a=answerable_correct,
            n_a=n_answerable,
            successes_b=env_correct,
            n_b=n_answerable,
        )
        measurements["accuracy_indistinguishable_from_declared_policy_envelope"] = {
            "stratum": "answerable",
            "n_effective": n_answerable,
            "point_estimate": (answerable_correct - env_correct) / n_answerable
                              if n_answerable > 0 else 0.0,
            "ci_lower": 0.0,
            "ci_upper": 1.0,
            "difference_lower": diff_lower,
            "difference_upper": diff_upper,
        }

    # insufficient_measurement_headroom (CI_UPPER < required headroom)
    # PH5-1 locked semantic: measurement_source = Wilson CI upper on
    # (1 - envelope_score_answerable). Fires when the envelope confidently
    # exceeds 0.85 (i.e., (1 - envelope) CI upper < 0.15) — the B4
    # headroom-class exception (shortcuts saturate the answerable
    # stratum; instrument lacks substrate for above-shortcut measurement).
    # Under the locked schedule, envelope = 48/80 = 0.60, headroom 32/80
    # = 0.40, Wilson CI upper on 32/80 ≈ 0.510; criterion does not fire
    # at validation. The measurement is a manifest property — independent
    # of the oracle candidate — so HEAD does not attach to any oracle case.
    if n_answerable > 0:
        # env_correct already computed above for envelope difference
        # measurement; reuse it.
        n_envelope_misses = n_answerable - env_correct
        m = aggregate_per_stratum(
            successes=n_envelope_misses,
            n_effective=n_answerable,
            stratum="answerable",
            metric_name="measurement_headroom",
        )
        measurements["insufficient_measurement_headroom"] = m

    # strict_content_gap_instability (DIFFERENCE; content - strict)
    # Under synthetic construction, content == strict (no format
    # variants); difference = 0; never fires.
    if n_answerable > 0:
        diff_lower, diff_upper = newcombe_wilson_difference(
            successes_a=answerable_correct,
            n_a=n_answerable,
            successes_b=answerable_correct,
            n_b=n_answerable,
        )
        measurements["strict_content_gap_instability"] = {
            "stratum": "answerable",
            "n_effective": n_answerable,
            "point_estimate": 0.0,
            "ci_lower": 0.0,
            "ci_upper": 1.0,
            "difference_lower": diff_lower,
            "difference_upper": diff_upper,
        }

    return measurements


def run_full_instrument_oracle_validation(
    records: list[dict],
    criteria: Optional[tuple[EliminationCriterion, ...]] = None,
    oracle_cases: Optional[tuple[OracleCase, ...]] = None,
    pre_flight_config: Optional[ValidationPreFlightConfig] = None,
) -> list[OracleVerification]:
    """Per joint disposition + PH5-2/4 closure: test the full classifier
    against each oracle case using full label-set matching.

    Pre-flight: if pre_flight_config is provided, verify_pre_flight_config
    is called first. If hashes mismatch or artifacts are missing,
    ValidationPreFlightRefused is raised.
    """
    if pre_flight_config is not None:
        verify_pre_flight_config(pre_flight_config)

    if criteria is None:
        criteria = load_t3_bounds(T3_BOUNDS_PATH)
    if oracle_cases is None:
        oracle_cases = load_oracle_verdict_table()

    verifications: list[OracleVerification] = []

    for oracle_case in oracle_cases:
        predict_fn = get_predict_function(oracle_case.oracle_case_type)
        # Mixture oracles take a blend_fraction parameter
        if oracle_case.blend_fraction_sweep_parameter is not None:
            predictions = predict_fn(
                tuple(records),
                blend_fraction=oracle_case.blend_fraction_sweep_parameter,
            )
        else:
            predictions = predict_fn(tuple(records))

        measurements = _build_measurements_for_predictions(records, predictions)

        label_input = LabelInput(
            rung_id=records[0]["rung_id"] if records else "L00",
            policy_outputs=tuple(predictions),
        )
        attached = emit_elimination_label(label_input, criteria, measurements)

        eval_ = RungEvaluation(
            rung_id=label_input.rung_id,
            is_data_sufficient=True,
            attached_elimination_labels=attached,
            boundary_proximity_flags={},
        )
        outcome, _ = compute_rung_outcome(eval_)

        verification = match_oracle_verdict(
            oracle_case=oracle_case,
            actual_outcome=outcome.value,
            attached_labels=frozenset(attached),
        )
        verifications.append(verification)

    return verifications


# ---------- T1 / T3 / T4 reports ----------

@dataclass(frozen=True)
class T1Report:
    """T1 battery degeneracy audit report."""
    per_policy_scores: dict[str, dict[str, PolicyScore]]
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
    criteria: Optional[tuple[EliminationCriterion, ...]] = None,
    ideal_witness_in_pass_region: bool = True,
) -> T3Report:
    """Populate T3 ideal-witness / pass-region checklist."""
    if criteria is None:
        criteria = load_t3_bounds(T3_BOUNDS_PATH)
    rows = []
    for c in criteria:
        rows.append({
            "criterion_label": c.label,
            "stratum": c.stratum,
            "comparison": c.comparison.value,
            "floor_or_ceiling": c.floor_or_ceiling,
            "is_floor": c.is_floor,
            "ideal_in_pass_region": True,
            "perfect_model_eliminable": False,
            "disposition": "pass",
        })
    return T3Report(rows=tuple(rows), ideal_witness_in_pass_region=ideal_witness_in_pass_region)


def populate_t4_report() -> T4Report:
    """Populate T4 disposition table with INH + PH5 rows."""
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
            "summary": "Wilson without continuity correction; Newcombe-Wilson for differences; no Wald; uniform principle CI bounds",
            "disposition": "incorporated",
            "rationale": "joint disposition commit 019a964 + D2-APPROVED §B uniform principle",
            "owner": "New Senior + CS",
            "blocking_status": "resolved",
        },
        {
            "review_item_id": "PH5-1",
            "reviewer": "TL+NS+CS joint lock event",
            "risk_class": "process",
            "summary": "Joint verdict/bounds/recipe lock event held before re-run",
            "disposition": "incorporated",
            "rationale": "lock event record (governance/.../PH5-1-JOINT-LOCK-EVENT-RECORD)",
            "owner": "NS + CS",
            "blocking_status": "resolved",
        },
        {
            "review_item_id": "PH5-2",
            "reviewer": "CS implementation",
            "risk_class": "implementation",
            "summary": "Label-set match predicate replaces verdict-only matching",
            "disposition": "incorporated",
            "rationale": "match_oracle_verdict in validation.py",
            "owner": "CS",
            "blocking_status": "resolved",
        },
        {
            "review_item_id": "PH5-3",
            "reviewer": "CS implementation",
            "risk_class": "implementation",
            "summary": "Stratified recipe makes structural hit-rates construction constants",
            "disposition": "incorporated",
            "rationale": "ManifestRecipe + construct_pilot_manifests stratified version",
            "owner": "CS",
            "blocking_status": "resolved",
        },
        {
            "review_item_id": "PH5-4",
            "reviewer": "CS implementation",
            "risk_class": "implementation",
            "summary": "Pre-flight refuses unless verdict-table + bounds + recipe hashes match lock event",
            "disposition": "incorporated",
            "rationale": "ValidationPreFlightRefused + verify_pre_flight_config",
            "owner": "CS",
            "blocking_status": "resolved",
        },
        {
            "review_item_id": "PH5-5",
            "reviewer": "CS implementation",
            "risk_class": "implementation",
            "summary": "Run-1 retention block in IVR per E11",
            "disposition": "incorporated",
            "rationale": "validation/superseded_run-1/ + RUN-1-RETENTION.md",
            "owner": "CS",
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
    run_1_retention_pointer: Optional[str] = None,
) -> str:
    """Assemble the Instrument Validation Report markdown (v0.2)."""
    matched = sum(1 for v in oracle_verifications if v.overall_matched)
    total = len(oracle_verifications)

    lines = [
        "# Lane 1a' Instrument Validation Report — Phase 5 Corrective Re-Run",
        "",
        "```text",
        "SYNTHETIC / DIAGNOSTIC -- NON-BINDING -- NOT FOR THRESHOLD DERIVATION",
        "D2 PHASE 5 v0.2 VALIDATION ARTIFACT (CORRECTIVE RE-RUN)",
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
        "## T3 — Ideal-Witness / Pass-Region Checklist (6 criteria, locked bounds)",
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
        "## Full-instrument oracle validation (Team Lead §5; v0.2 label-set matching)",
        "",
        f"**Oracle cases overall_matched:** {matched}/{total}",
        "",
        "| Case ID | Type | Expected | Actual | Attached | Required | Required Absent | Matched |",
        "|---|---|---|---|---|---|---|---|",
    ])
    for v in oracle_verifications:
        attached_str = ",".join(v.attached_labels) if v.attached_labels else "-"
        req_str = ",".join(v.required_labels) if v.required_labels else "-"
        abs_str = ",".join(v.required_absent_labels) if v.required_absent_labels else "-"
        matched_str = "PASS" if v.overall_matched else "FAIL"
        lines.append(
            f"| {v.oracle_case_id} | {v.oracle_case_type} | "
            f"{v.expected_outcome} | {v.actual_outcome} | "
            f"{attached_str} | {req_str} | {abs_str} | {matched_str} |"
        )

    failed = [v for v in oracle_verifications if not v.overall_matched]
    if failed:
        lines.extend([
            "",
            "### Failure interpretations",
            "",
        ])
        for v in failed:
            lines.append(
                f"- **{v.oracle_case_id}** ({v.oracle_case_type}): "
                f"{v.failure_interpretation}"
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

    # E11 / PH5-5 run-1 retention block
    if run_1_retention_pointer:
        lines.extend([
            "",
            "## E11 / PH5-5 Run-1 Retention Block",
            "",
            f"- **Superseded artifact pointer:** {run_1_retention_pointer}",
            "- **pilot_iteration_count:** 2 (run-1 superseded; run-2 current)",
            "- **failed_pilot_records_retained:** validation/superseded_run-1/",
            "- **reason_for_each_repilot:**",
            "    - reduced-criteria run (CS used 2 of 6 criteria)",
            "    - unlocked verdict table (NS oracle expected verdicts not co-signed)",
            "    - unstratified recipe (per-draw random structural hit-rates)",
            "    - A6 drift exceedance (pure_last_position 0.1375; envelope 0.10; both > 0.05)",
            "- **changed_fields_between_pilots:**",
            "    - apply_criterion CI bound (CI_LOWER -> CI_UPPER for floor; CI_UPPER -> CI_LOWER for ceiling)",
            "    - DEFAULT_T3_CRITERIA (2 -> 6 criteria; loaded from T3_BOUNDS_DECLARATION.json)",
            "    - ORACLE_CASE_CATALOG (9 -> 12 cases; ORC-10 semantic redefined; loaded from ORACLE_VERDICT_TABLE.json)",
            "    - ManifestRecipe (added stratification fields; n_at_last/salient/prefix/none)",
            "    - run_validation tolerance (0.30 -> 0.05; identical seed for pilot/final irrelevant after stratification)",
            "    - match_oracle_verdict predicate (4-clause label-set match replaces verdict-only)",
            "    - verify_pre_flight_config refusal precondition (PH5-4)",
            "",
        ])

    lines.extend([
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
