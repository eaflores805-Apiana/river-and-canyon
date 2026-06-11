"""Lane 1a' synthetic oracle case constructors.

SYNTHETIC / DIAGNOSTIC -- NON-BINDING -- NOT FOR THRESHOLD DERIVATION
D2 IMPLEMENTATION ARTIFACT (PHASE 5)
NO MODEL INVOKED -- NO MODEL LOADED
NO SWEEP_ID CREATED -- NO SWEEP EXECUTION AUTHORIZED

Implements the synthetic oracle cases required for A5 pre-flight and
full-instrument oracle validation (per Team Lead Phase 5 §5):

  - ideal_retriever       : returns gold value on every answerable item
  - last_position_shortcut: returns value at last position
  - salient_endpoint_shortcut: returns value at index 0 (salient endpoint)
  - recency_excluding_shortcut: returns value at last position EXCLUDING queried key
  - prefix_neighbor_shortcut: returns value of nearest shared-prefix neighbor
  - token_prior_emitter  : returns a fixed token from VALUE_POOL (frequency-bias model)
  - universal_answerer   : always answers (never abstains)
  - universal_abstainer  : always abstains (returns None)
  - perfect_null_handler : answers correctly on answerable, abstains on NULL
  - mixture_oracle       : blend of ideal retrieval (default 70%) and a shortcut
  - malformed_control_case: a control case whose declared semantic_target is
                            mismatched with the criterion (screens for ill-formed-class
                            detection)

Each oracle returns a SimulatedPrediction per manifest record. The
oracle does NOT invoke a model; it generates synthetic predictions
deterministically based on the manifest record's structure.

The full-instrument oracle validation pipeline (in validation.py)
takes the simulated predictions, scores them against the manifest's
gold value, aggregates per-stratum, applies T3 criteria via
emit_elimination_label, and computes the rung outcome via
compute_rung_outcome. The actual_full_instrument_outcome is compared
to the oracle's expected_verdict.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Callable, Optional


# Value pool per joint disposition: |VALUE_POOL| = 26
VALUE_POOL = tuple(range(26))


class ExpectedVerdict(Enum):
    """Expected outcome category per the joint disposition."""
    NOT_RULED_OUT = "not_ruled_out"      # the oracle should pass all eliminations
    ELIMINATED = "eliminated"            # the oracle should be eliminated by at least one criterion
    INCONCLUSIVE = "inconclusive_not_actionable"
    FLAG_INDETERMINATE = "flag_indeterminate"  # mixture oracles where outcome is ambiguous


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
    """A synthetic oracle case for full-instrument validation."""
    oracle_case_id: str
    oracle_case_type: str
    expected_verdict: ExpectedVerdict
    description: str
    # The predict function: takes (manifest_records) -> tuple[SimulatedPrediction, ...]
    # The signature is intentionally a Callable[[tuple[dict, ...]], tuple[SimulatedPrediction, ...]]
    # to allow oracle-specific deterministic logic without invoking a model.


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


def predict_last_position_shortcut(records: tuple[dict, ...]) -> tuple[SimulatedPrediction, ...]:
    """Returns the value at the LAST position in the real-pair block."""
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
    """Returns the value at INDEX 0 (the declared salient endpoint
    under our default of position 0)."""
    out = []
    for idx, r in enumerate(records):
        pairs = r["context_block"]["real_pair_block"]["pairs"]
        if not pairs:
            out.append(_make_prediction(r, idx, None))
        else:
            v = tuple(pairs[0]["value_token_ids"])
            out.append(_make_prediction(r, idx, v))
    return tuple(out)


def predict_token_prior_emitter(records: tuple[dict, ...]) -> tuple[SimulatedPrediction, ...]:
    """Returns a fixed value from VALUE_POOL (token-prior bias);
    deterministic per record via record_id hash."""
    out = []
    for idx, r in enumerate(records):
        # Deterministic emission: pick value at index hash(record_id) % len(pool)
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


def predict_perfect_null_handler(records: tuple[dict, ...]) -> tuple[SimulatedPrediction, ...]:
    """Answers correctly (gold) on answerable; abstains on NULL.

    This is the ideal-corner behavior — the criterion's pass region
    must contain this by construction (per joint disposition).
    """
    return predict_ideal_retriever(records)


def predict_mixture_oracle(
    records: tuple[dict, ...],
    blend_fraction: float = 0.7,
) -> tuple[SimulatedPrediction, ...]:
    """Blend of ideal retrieval (blend_fraction) and last-position
    shortcut (1 - blend_fraction). Deterministic split via record index.
    """
    out = []
    for idx, r in enumerate(records):
        # Deterministic: use idx-based mod to allocate
        is_ideal_slot = (idx * 10) % 10 < int(blend_fraction * 10)
        if is_ideal_slot:
            if r["stratum"] == "null":
                out.append(_make_prediction(r, idx, None))
            else:
                gold = tuple(r["gold"]["value_token_ids"])
                out.append(_make_prediction(r, idx, gold))
        else:
            pairs = r["context_block"]["real_pair_block"]["pairs"]
            if pairs:
                v = tuple(pairs[-1]["value_token_ids"])
                out.append(_make_prediction(r, idx, v))
            else:
                out.append(_make_prediction(r, idx, None))
    return tuple(out)


def predict_malformed_control_case(records: tuple[dict, ...]) -> tuple[SimulatedPrediction, ...]:
    """Malformed-control case: simulates a control whose declared
    semantic_target is mismatched with the criterion. The simulated
    behavior here is "always returns the queried key as the predicted
    value" — which is the copy_completion pattern, but routed through
    a control that claims to measure something else.

    The full-instrument validation should detect that this behavior
    is consistent with a copy shortcut, NOT with the declared semantic
    target. The malformed-control screen in B4 (and the T3 dead /
    tautological / malformed screens) should fire.
    """
    out = []
    for idx, r in enumerate(records):
        if r["stratum"] == "null":
            out.append(_make_prediction(r, idx, None))
        else:
            # Returns the queried key as the value (copy shortcut)
            qk = tuple(r["queried_key"]["key_token_ids"])
            out.append(_make_prediction(r, idx, qk))
    return tuple(out)


# ---------- oracle case catalog ----------

ORACLE_CASE_CATALOG: tuple[OracleCase, ...] = (
    OracleCase(
        oracle_case_id="oracle-ideal-retriever",
        oracle_case_type="ideal_retriever",
        expected_verdict=ExpectedVerdict.NOT_RULED_OUT,
        description=(
            "Synthetic ideal retriever: always returns the gold value on "
            "answerable items; abstains on NULL items. Must NOT be "
            "eliminated by any criterion (B4 ideal-witness closure)."
        ),
    ),
    OracleCase(
        oracle_case_id="oracle-last-position-shortcut",
        oracle_case_type="last_position_shortcut",
        expected_verdict=ExpectedVerdict.ELIMINATED,
        description=(
            "Always returns the value at the last position. The "
            "pure_last_position policy detects this shortcut; the "
            "policy-envelope criterion fires."
        ),
    ),
    OracleCase(
        oracle_case_id="oracle-salient-endpoint-shortcut",
        oracle_case_type="salient_endpoint_shortcut",
        expected_verdict=ExpectedVerdict.ELIMINATED,
        description=(
            "Always returns the value at the salient endpoint "
            "(index 0). The salient_endpoint policy detects this; "
            "envelope criterion fires."
        ),
    ),
    OracleCase(
        oracle_case_id="oracle-token-prior-emitter",
        oracle_case_type="token_prior_emitter",
        expected_verdict=ExpectedVerdict.ELIMINATED,
        description=(
            "Emits a fixed value from VALUE_POOL deterministically. "
            "The token_prior_indistinguishable criterion fires."
        ),
    ),
    OracleCase(
        oracle_case_id="oracle-universal-answerer",
        oracle_case_type="universal_answerer",
        expected_verdict=ExpectedVerdict.ELIMINATED,
        description=(
            "Always answers, never abstains. The null_abstention_floor "
            "criterion fires."
        ),
    ),
    OracleCase(
        oracle_case_id="oracle-universal-abstainer",
        oracle_case_type="universal_abstainer",
        expected_verdict=ExpectedVerdict.ELIMINATED,
        description=(
            "Always abstains. The answerable_abstention_ceiling "
            "criterion fires."
        ),
    ),
    OracleCase(
        oracle_case_id="oracle-perfect-null-handler",
        oracle_case_type="perfect_null_handler",
        expected_verdict=ExpectedVerdict.NOT_RULED_OUT,
        description=(
            "Answers gold on answerable; abstains on NULL. The ideal "
            "corner (1.0 NULL abstention, 0.0 answerable abstention) "
            "is inside the pass region by construction (B4 closure)."
        ),
    ),
    OracleCase(
        oracle_case_id="oracle-mixture-70-30",
        oracle_case_type="mixture_oracle",
        expected_verdict=ExpectedVerdict.FLAG_INDETERMINATE,
        description=(
            "70% ideal retrieval + 30% last-position shortcut. The "
            "expected verdict is flag_indeterminate per joint disposition "
            "(the mixture case may fire either way depending on "
            "criterion thresholds; the validation report records the "
            "actual outcome for review)."
        ),
    ),
    OracleCase(
        oracle_case_id="oracle-malformed-control",
        oracle_case_type="malformed_control",
        expected_verdict=ExpectedVerdict.ELIMINATED,
        description=(
            "Simulates a control whose behavior is the copy_completion "
            "shortcut. Should be detected and eliminated (the "
            "malformed-control screen surfaces the mismatch)."
        ),
    ),
)


PREDICT_FUNCTIONS: dict[str, Callable[[tuple[dict, ...]], tuple[SimulatedPrediction, ...]]] = {
    "ideal_retriever": predict_ideal_retriever,
    "last_position_shortcut": predict_last_position_shortcut,
    "salient_endpoint_shortcut": predict_salient_endpoint_shortcut,
    "token_prior_emitter": predict_token_prior_emitter,
    "universal_answerer": predict_universal_answerer,
    "universal_abstainer": predict_universal_abstainer,
    "perfect_null_handler": predict_perfect_null_handler,
    "mixture_oracle": predict_mixture_oracle,
    "malformed_control": predict_malformed_control_case,
}


def get_predict_function(oracle_case_type: str):
    """Return the deterministic predict function for an oracle case type."""
    if oracle_case_type not in PREDICT_FUNCTIONS:
        raise KeyError(f"Unknown oracle_case_type: {oracle_case_type!r}")
    return PREDICT_FUNCTIONS[oracle_case_type]
