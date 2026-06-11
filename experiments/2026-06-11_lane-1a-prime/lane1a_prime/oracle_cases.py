"""Lane 1a' synthetic oracle case constructors (v0.2 — corrective re-run).

SYNTHETIC / DIAGNOSTIC -- NON-BINDING -- NOT FOR THRESHOLD DERIVATION
D2 IMPLEMENTATION ARTIFACT (PHASE 5 CORRECTIVE)
NO MODEL INVOKED -- NO MODEL LOADED
NO SWEEP_ID CREATED -- NO SWEEP EXECUTION AUTHORIZED

v0.2 changes from v0.1:
  - OracleCase expanded with required_labels / permitted_co_labels /
    required_absent_labels per joint disposition (commit 019a964 +
    NS oracle table v0.2 sha256 a5d95065...)
  - 12 oracle cases per NS v0.2 (ORC-01 through ORC-12)
  - ORC-10 redefined: post-scramble-gold (rebinding-following) with
    expected_outcome = not_ruled_out and required_absent = {TP}
  - New ORCs added: ORC-04 (recency_excluding_target shortcut),
    ORC-05 (prefix_neighbor_confusion shortcut),
    ORC-11 (mixture shortcut-heavy 0.75),
    ORC-12 (mixture retrieval-heavy 0.25; boundary case)
  - Oracle cases loaded from ORACLE_VERDICT_TABLE.json (locked at
    PH5-1 lock event; sha256 add5f707...)

Each oracle returns a SimulatedPrediction per manifest record. The
oracle does NOT invoke a model.
"""
from __future__ import annotations

import json
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import Callable, Optional


# Value pool per joint disposition: |VALUE_POOL| = 26
VALUE_POOL = tuple(range(26))


# Lock event artifact paths
LOCK_EVENT_DIR = Path(__file__).resolve().parent.parent / "validation"
ORACLE_VERDICT_TABLE_PATH = LOCK_EVENT_DIR / "ORACLE_VERDICT_TABLE.json"


@dataclass(frozen=True)
class SimulatedPrediction:
    """A synthetic prediction for a single manifest record.

    predicted_value_token_ids = None means abstention.
    """
    record_id: str
    predicted_value_token_ids: Optional[tuple[int, ...]]

    @property
    def abstained(self) -> bool:
        return self.predicted_value_token_ids is None


@dataclass(frozen=True)
class OracleCase:
    """A synthetic oracle case for full-instrument validation (v0.2).

    Per joint disposition (NS oracle table v0.2):

      expected_outcome:        one of RUNG_OUTCOME_VALUES
      required_labels:         MUST attach (each label must be in
                                attached_labels)
      permitted_co_labels:     MAY also attach (no constraint either way)
      required_absent_labels:  MUST NOT attach (none may be in
                                attached_labels)

    A case passes iff all four label-set conditions hold:
      1. actual_outcome == expected_outcome
      2. required_labels subset attached_labels
      3. required_absent_labels intersection attached_labels = empty
      4. attached_labels subset (required_labels union permitted_co_labels)
    """
    oracle_case_id: str
    oracle_case_type: str
    expected_outcome: str
    required_labels: tuple[str, ...]
    permitted_co_labels: tuple[str, ...]
    required_absent_labels: tuple[str, ...]
    description: str
    blend_fraction_sweep_parameter: Optional[float] = None


def _record_id(record: dict, idx: int) -> str:
    """Compute a stable record id from the record dict + index."""
    rung = record.get("rung_id", "L00")
    return f"{rung}-{idx:03d}"


def _make_prediction(
    record: dict,
    idx: int,
    predicted: Optional[tuple[int, ...]],
) -> SimulatedPrediction:
    return SimulatedPrediction(
        record_id=_record_id(record, idx),
        predicted_value_token_ids=predicted,
    )


# ---------- oracle predict functions ----------

def predict_ideal_retriever(records: tuple[dict, ...]) -> tuple[SimulatedPrediction, ...]:
    """Always returns the gold value on answerable items; abstains on NULL."""
    out = []
    for idx, r in enumerate(records):
        if r["stratum"] == "null":
            out.append(_make_prediction(r, idx, None))
        else:
            gold = r["gold"]["value_token_ids"]
            out.append(_make_prediction(r, idx, tuple(gold)))
    return tuple(out)


def predict_pure_last_position_shortcut(records: tuple[dict, ...]) -> tuple[SimulatedPrediction, ...]:
    """Returns the value at the LAST position in the real-pair block.

    Under the stratified recipe, ~25% of answerable items have the
    queried_key at the last position. The policy hits gold for those
    items.
    """
    out = []
    for idx, r in enumerate(records):
        pairs = r["context_block"]["real_pair_block"]["pairs"]
        if not pairs:
            out.append(_make_prediction(r, idx, None))
        else:
            v = tuple(pairs[-1]["value_token_ids"])
            out.append(_make_prediction(r, idx, v))
    return tuple(out)


def predict_salient_endpoint_shortcut(records: tuple[dict, ...]) -> tuple[SimulatedPrediction, ...]:
    """Returns the value at index 0 (the declared salient endpoint)."""
    out = []
    for idx, r in enumerate(records):
        pairs = r["context_block"]["real_pair_block"]["pairs"]
        if not pairs:
            out.append(_make_prediction(r, idx, None))
        else:
            v = tuple(pairs[0]["value_token_ids"])
            out.append(_make_prediction(r, idx, v))
    return tuple(out)


def predict_recency_excluding_target_shortcut(records: tuple[dict, ...]) -> tuple[SimulatedPrediction, ...]:
    """Returns the value of the most recent pair EXCLUDING the queried key.

    For pilot data this is just the second-to-last pair if the queried
    key happens to be at the last position; otherwise the last pair.
    """
    out = []
    for idx, r in enumerate(records):
        pairs = r["context_block"]["real_pair_block"]["pairs"]
        queried_key = tuple(r["queried_key"]["key_token_ids"])
        candidates = [
            p for p in pairs
            if tuple(p["key_token_ids"]) != queried_key
        ]
        if not candidates:
            out.append(_make_prediction(r, idx, None))
        else:
            v = tuple(candidates[-1]["value_token_ids"])
            out.append(_make_prediction(r, idx, v))
    return tuple(out)


def predict_prefix_neighbor_confusion_shortcut(records: tuple[dict, ...]) -> tuple[SimulatedPrediction, ...]:
    """Returns the value of the nearest shared-prefix neighbor.

    Total-function rules per NS v0.2: excludes the queried key; ties
    resolve to most-recent; when no eligible shared-prefix neighbor
    exists, emits the declared no-match value (VALUE_POOL[0]) which
    scores incorrect but does NOT abstain (total function — never None).
    """
    no_match_fallback = (VALUE_POOL[0],)
    out = []
    for idx, r in enumerate(records):
        pairs = r["context_block"]["real_pair_block"]["pairs"]
        queried_key = tuple(r["queried_key"]["key_token_ids"])
        candidates = [
            (i, tuple(p["key_token_ids"]), tuple(p["value_token_ids"]))
            for i, p in enumerate(pairs)
            if tuple(p["key_token_ids"]) != queried_key
        ]
        if not candidates or not queried_key:
            out.append(_make_prediction(r, idx, no_match_fallback))
            continue
        # Compute prefix distance per candidate
        scored = []
        for i, k, v in candidates:
            common = 0
            for a, b in zip(queried_key, k):
                if a == b:
                    common += 1
                else:
                    break
            distance = len(queried_key) - common
            if distance < len(queried_key):  # has shared prefix
                scored.append((distance, i, v))
        if not scored:
            out.append(_make_prediction(r, idx, no_match_fallback))
            continue
        min_dist = min(d for d, _, _ in scored)
        nearest = [(i, v) for d, i, v in scored if d == min_dist]
        # Tie-break by most recent (highest index)
        chosen_idx, chosen_value = max(nearest, key=lambda iv: iv[0])
        out.append(_make_prediction(r, idx, chosen_value))
    return tuple(out)


def predict_token_prior_emitter(records: tuple[dict, ...]) -> tuple[SimulatedPrediction, ...]:
    """Emits a uniform sample from VALUE_POOL on every item.

    Per joint disposition: token-prior emitter samples uniformly from
    the value pool. Deterministic per record via record_id hash for
    reproducibility.
    """
    out = []
    for idx, r in enumerate(records):
        rid = _record_id(r, idx)
        emit = VALUE_POOL[hash(rid) % len(VALUE_POOL)]
        out.append(_make_prediction(r, idx, (emit,)))
    return tuple(out)


def predict_universal_answerer(records: tuple[dict, ...]) -> tuple[SimulatedPrediction, ...]:
    """Always answers (never abstains). Returns the first value from VALUE_POOL."""
    out = []
    for idx, r in enumerate(records):
        out.append(_make_prediction(r, idx, (VALUE_POOL[0],)))
    return tuple(out)


def predict_universal_abstainer(records: tuple[dict, ...]) -> tuple[SimulatedPrediction, ...]:
    """Always abstains (returns None)."""
    out = []
    for idx, r in enumerate(records):
        out.append(_make_prediction(r, idx, None))
    return tuple(out)


def predict_perfect_null_on_null_handler(records: tuple[dict, ...]) -> tuple[SimulatedPrediction, ...]:
    """Answers correctly on answerable; abstains on NULL.

    Equivalent to the ideal_retriever; retained as a separate ORC
    (v1 abstention-band regression guard).
    """
    return predict_ideal_retriever(records)


def predict_malformed_control_semantic_separation_guard(
    records: tuple[dict, ...],
) -> tuple[SimulatedPrediction, ...]:
    """Perfect rebinding-follower presented as candidate.

    Under the synthetic construction (no actual scramble step),
    rebinding-following is indistinguishable from ideal retrieval.
    The point of ORC-10 is to verify that this behavior does NOT
    fire accuracy_indistinguishable_from_token_prior — the v1
    mislabeling regression check.

    Identical predictions to predict_ideal_retriever; the case
    differs only in the expected label-set (required_absent={TP}).
    """
    return predict_ideal_retriever(records)


def predict_mixture_shortcut_heavy(
    records: tuple[dict, ...],
    blend_fraction: float = 0.75,
) -> tuple[SimulatedPrediction, ...]:
    """Mixture: blend_fraction shortcut + (1 - blend_fraction) gold; NULL per contract.

    Default blend_fraction = 0.75 (shortcut-heavy). The mixture is
    deterministic by item index for reproducibility.
    """
    out = []
    last_position_preds = predict_pure_last_position_shortcut(records)
    ideal_preds = predict_ideal_retriever(records)
    answerable_ordinal = 0
    for idx, r in enumerate(records):
        if r["stratum"] == "null":
            # NULL items always per contract (abstain)
            out.append(_make_prediction(r, idx, None))
        else:
            # Deterministic allocation across the answerable stratum:
            # first floor(blend_fraction * n_answerable) ordinals are
            # shortcut slots; the rest are ideal slots. Pre-declared
            # by blend_fraction; not data-dependent.
            is_shortcut_slot = (answerable_ordinal % 100) < int(blend_fraction * 100)
            if is_shortcut_slot:
                out.append(last_position_preds[idx])
            else:
                out.append(ideal_preds[idx])
            answerable_ordinal += 1
    return tuple(out)


def predict_mixture_retrieval_heavy(
    records: tuple[dict, ...],
    blend_fraction: float = 0.25,
) -> tuple[SimulatedPrediction, ...]:
    """Mixture: blend_fraction shortcut + (1 - blend_fraction) gold; NULL per contract.

    Default blend_fraction = 0.25 (retrieval-heavy). Boundary case.
    """
    return predict_mixture_shortcut_heavy(records, blend_fraction=blend_fraction)


PREDICT_FUNCTIONS: dict[str, Callable[[tuple[dict, ...]], tuple[SimulatedPrediction, ...]]] = {
    "ideal_retriever": predict_ideal_retriever,
    "pure_last_position_shortcut": predict_pure_last_position_shortcut,
    "salient_endpoint_shortcut": predict_salient_endpoint_shortcut,
    "recency_excluding_target_shortcut": predict_recency_excluding_target_shortcut,
    "prefix_neighbor_confusion_shortcut": predict_prefix_neighbor_confusion_shortcut,
    "token_prior_emitter": predict_token_prior_emitter,
    "universal_answerer": predict_universal_answerer,
    "universal_abstainer": predict_universal_abstainer,
    "perfect_null_on_null_handler": predict_perfect_null_on_null_handler,
    "malformed_control_semantic_separation_guard": predict_malformed_control_semantic_separation_guard,
    "mixture_shortcut_heavy": predict_mixture_shortcut_heavy,
    "mixture_retrieval_heavy": predict_mixture_retrieval_heavy,
}


def get_predict_function(oracle_case_type: str):
    """Return the deterministic predict function for an oracle case type."""
    if oracle_case_type not in PREDICT_FUNCTIONS:
        raise KeyError(f"Unknown oracle_case_type: {oracle_case_type!r}")
    return PREDICT_FUNCTIONS[oracle_case_type]


def load_oracle_verdict_table(
    path: Path = ORACLE_VERDICT_TABLE_PATH,
) -> tuple[OracleCase, ...]:
    """Load the locked oracle verdict table from disk.

    The path defaults to the lock-event artifact at
    `validation/ORACLE_VERDICT_TABLE.json` (sha256 add5f707... at
    PH5-1 lock event). The pre-flight check
    (`validation.verify_pre_flight_config`) verifies the hash before
    this function's results are used.
    """
    with path.open() as f:
        data = json.load(f)
    cases = []
    for case_data in data["oracle_cases"]:
        cases.append(OracleCase(
            oracle_case_id=case_data["oracle_case_id"],
            oracle_case_type=case_data["oracle_case_type"],
            expected_outcome=case_data["expected_outcome"],
            required_labels=tuple(case_data["required_labels"]),
            permitted_co_labels=tuple(case_data["permitted_co_labels"]),
            required_absent_labels=tuple(case_data["required_absent_labels"]),
            description=case_data["description"],
            blend_fraction_sweep_parameter=case_data.get("blend_fraction_sweep_parameter"),
        ))
    return tuple(cases)


# For backward compatibility with v0.1 callers (test_validation.py legacy):
# ORACLE_CASE_CATALOG holds the locked v0.2 cases loaded from the table.
ORACLE_CASE_CATALOG: tuple[OracleCase, ...] = load_oracle_verdict_table()
