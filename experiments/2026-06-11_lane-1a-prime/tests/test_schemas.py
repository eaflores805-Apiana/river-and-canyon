"""Lane 1a' Phase 1 schema tests.

SYNTHETIC / DIAGNOSTIC -- NON-BINDING -- NOT FOR THRESHOLD DERIVATION
D2 IMPLEMENTATION ARTIFACT
NO MODEL INVOKED -- NO SWEEP_ID CREATED -- NO SWEEP EXECUTION AUTHORIZED

Validates the four Phase 1 schemas:
  - manifest_schema.yaml
  - sidecar_schema.yaml
  - rung_result_schema.yaml
  - lock_record_schema.yaml

Per-schema tests assert valid records pass and invalid records fail.
Cross-schema invariants assert AL-Q2-schema closure, the no-`fails`
token rule, the no-`passes` token rule, and artifact-label vocabulary
consistency.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import pytest
import yaml
from jsonschema import Draft202012Validator, ValidationError

SCHEMAS_DIR = Path(__file__).resolve().parent.parent / "schemas"


def _load_schema(name: str) -> dict[str, Any]:
    with (SCHEMAS_DIR / name).open() as f:
        return yaml.safe_load(f)


@pytest.fixture(scope="module")
def manifest_schema() -> dict[str, Any]:
    return _load_schema("manifest_schema.yaml")


@pytest.fixture(scope="module")
def sidecar_schema() -> dict[str, Any]:
    return _load_schema("sidecar_schema.yaml")


@pytest.fixture(scope="module")
def rung_result_schema() -> dict[str, Any]:
    return _load_schema("rung_result_schema.yaml")


@pytest.fixture(scope="module")
def lock_record_schema() -> dict[str, Any]:
    return _load_schema("lock_record_schema.yaml")


def _validate(schema: dict[str, Any], instance: Any) -> None:
    Draft202012Validator(schema).validate(instance)


def _expect_invalid(schema: dict[str, Any], instance: Any) -> None:
    with pytest.raises(ValidationError):
        _validate(schema, instance)


# ---------- manifest_schema tests ----------

VALID_MANIFEST: dict[str, Any] = {
    "rung_id": "L01",
    "context_block": {
        "padding_prefix": [1, 2, 3],
        "real_pair_block": {
            "start_idx": 3,
            "end_idx": 7,
            "pairs": [
                {"key_token_ids": [10], "value_token_ids": [20]},
                {"key_token_ids": [11], "value_token_ids": [21]},
            ],
        },
    },
    "queried_key": {"key_token_ids": [10]},
    "gold": {"value_token_ids": [20]},
    "stratum": "answerable",
    "metadata": {
        "construction_recipe_hash": "0" * 64,
        "pilot_or_final": "pilot",
        "iteration_index": 0,
    },
}


def test_manifest_valid(manifest_schema):
    _validate(manifest_schema, VALID_MANIFEST)


def test_manifest_rejects_invalid_rung_id(manifest_schema):
    instance = json.loads(json.dumps(VALID_MANIFEST))
    instance["rung_id"] = "L09"
    _expect_invalid(manifest_schema, instance)


def test_manifest_rejects_unknown_stratum(manifest_schema):
    instance = json.loads(json.dumps(VALID_MANIFEST))
    instance["stratum"] = "weird"
    _expect_invalid(manifest_schema, instance)


def test_manifest_rejects_additional_top_level_property(manifest_schema):
    instance = json.loads(json.dumps(VALID_MANIFEST))
    instance["unexpected"] = True
    _expect_invalid(manifest_schema, instance)


def test_manifest_rejects_missing_real_pair_boundary(manifest_schema):
    instance = json.loads(json.dumps(VALID_MANIFEST))
    del instance["context_block"]["real_pair_block"]["start_idx"]
    _expect_invalid(manifest_schema, instance)


def test_manifest_accepts_null_stratum(manifest_schema):
    instance = json.loads(json.dumps(VALID_MANIFEST))
    instance["stratum"] = "null"
    instance["gold"]["value_token_ids"] = []
    _validate(manifest_schema, instance)


# ---------- sidecar_schema tests ----------

VALID_RUNNER_ATTESTED: dict[str, Any] = {
    "sidecar_type": "runner_attested",
    "record_id": "r-001",
    "runner_output_hash": "a" * 64,
    "sweep_id": None,
    "rung_id": "L01",
    "stratum": "answerable",
    "policies_applied": ["pure_last_position", "recency_excluding_target"],
    "controls_applied": [],
    "elimination_label_basis": {
        "basis_policies": ["pure_last_position"]
    },
    "artifact_label": "SYNTHETIC — NON-BINDING — NOT FOR THRESHOLD DERIVATION",
    "audit": {
        "written_at": "2026-06-11T00:00:00Z",
        "written_by_wrapper_hash": "b" * 64,
    },
}

VALID_DIAGNOSTIC_SIDECAR: dict[str, Any] = {
    "sidecar_type": "diagnostic",
    "record_id": "r-002",
    "diagnostic_class": "copy_completion_agreement",
    "artifact_class": "lane-1a-prime-diagnostic",
    "artifact_label": "DIAGNOSTIC — NON-BINDING — NOT FOR THRESHOLD DERIVATION",
    "per_item": [
        {"item_id": "i-001", "diagnostic_value": 1.0, "runner_output_ref": "r-001#0"}
    ],
    "audit": {
        "written_at": "2026-06-11T00:00:00Z",
        "written_by_wrapper_hash": "c" * 64,
    },
}


def test_sidecar_runner_attested_valid(sidecar_schema):
    _validate(sidecar_schema, VALID_RUNNER_ATTESTED)


def test_sidecar_diagnostic_valid(sidecar_schema):
    _validate(sidecar_schema, VALID_DIAGNOSTIC_SIDECAR)


def test_sidecar_rejects_scrambled_binding_in_basis(sidecar_schema):
    """AL-Q2-schema Layer-2 closure: scrambled_binding_retrieval is
    structurally unrepresentable in the elimination basis."""
    instance = json.loads(json.dumps(VALID_RUNNER_ATTESTED))
    instance["elimination_label_basis"]["basis_policies"] = ["scrambled_binding_retrieval"]
    _expect_invalid(sidecar_schema, instance)


def test_sidecar_rejects_unconditioned_token_prior_in_basis(sidecar_schema):
    instance = json.loads(json.dumps(VALID_RUNNER_ATTESTED))
    instance["elimination_label_basis"]["basis_policies"] = ["unconditioned_token_prior"]
    _expect_invalid(sidecar_schema, instance)


def test_sidecar_rejects_copy_completion_in_basis(sidecar_schema):
    """copy_completion is outside the union envelope (Bundle v0.3 §I.4);
    not a valid elimination basis policy."""
    instance = json.loads(json.dumps(VALID_RUNNER_ATTESTED))
    instance["elimination_label_basis"]["basis_policies"] = ["copy_completion"]
    _expect_invalid(sidecar_schema, instance)


def test_sidecar_rejects_invalid_artifact_label(sidecar_schema):
    instance = json.loads(json.dumps(VALID_RUNNER_ATTESTED))
    instance["artifact_label"] = "PROMISING — BINDING — THRESHOLD-RELEVANT"
    _expect_invalid(sidecar_schema, instance)


def test_sidecar_rejects_unknown_sidecar_type(sidecar_schema):
    instance = json.loads(json.dumps(VALID_RUNNER_ATTESTED))
    instance["sidecar_type"] = "something_else"
    _expect_invalid(sidecar_schema, instance)


def test_sidecar_diagnostic_label_must_be_diagnostic(sidecar_schema):
    instance = json.loads(json.dumps(VALID_DIAGNOSTIC_SIDECAR))
    instance["artifact_label"] = "SYNTHETIC — NON-BINDING — NOT FOR THRESHOLD DERIVATION"
    _expect_invalid(sidecar_schema, instance)


def test_sidecar_diagnostic_artifact_class_constant(sidecar_schema):
    instance = json.loads(json.dumps(VALID_DIAGNOSTIC_SIDECAR))
    instance["artifact_class"] = "lane-1a-prime-reconnaissance"
    _expect_invalid(sidecar_schema, instance)


# ---------- rung_result_schema tests ----------

VALID_RUNG_RESULT: dict[str, Any] = {
    "rung_id": "L01",
    "outcome": "not_ruled_out",
    "attached_labels": ["requires_further_investigation"],
    "n_effective": {"answerable": 80, "null_stratum": 16, "pooled": 96},
    "k_contribution": 1,
    "boundary_proximity_flags": {"null_abstention_floor": False},
    "measurements": {
        "null_abstention_floor": {
            "point_estimate": 1.0,
            "ci_lower": 0.806,
            "ci_upper": 1.0,
            "comparison": "ci_lower_bound",
        }
    },
    "audit": {
        "evaluated_at": "2026-06-11T00:00:00Z",
        "analyzer_script_hash": "d" * 64,
    },
}


def test_rung_result_valid_not_ruled_out(rung_result_schema):
    _validate(rung_result_schema, VALID_RUNG_RESULT)


def test_rung_result_valid_eliminated(rung_result_schema):
    instance = json.loads(json.dumps(VALID_RUNG_RESULT))
    instance["outcome"] = "eliminated"
    instance["attached_labels"] = [
        "accuracy_indistinguishable_from_token_prior",
        "insufficient_measurement_headroom",
    ]
    instance["k_contribution"] = 0
    _validate(rung_result_schema, instance)


def test_rung_result_valid_inconclusive(rung_result_schema):
    instance = json.loads(json.dumps(VALID_RUNG_RESULT))
    instance["outcome"] = "inconclusive_not_actionable"
    instance["attached_labels"] = []
    instance["k_contribution"] = 0
    _validate(rung_result_schema, instance)


def test_rung_result_rejects_passes_outcome(rung_result_schema):
    """No `passes_X` value: structural enforcement of the doctrine."""
    instance = json.loads(json.dumps(VALID_RUNG_RESULT))
    instance["outcome"] = "passes_token_prior_separation"
    _expect_invalid(rung_result_schema, instance)


def test_rung_result_rejects_fails_label(rung_result_schema):
    """No `fails` token in any output label."""
    instance = json.loads(json.dumps(VALID_RUNG_RESULT))
    instance["outcome"] = "eliminated"
    instance["attached_labels"] = ["clearly_fails_token_prior_separation"]
    instance["k_contribution"] = 0
    _expect_invalid(rung_result_schema, instance)


def test_rung_result_rejects_invalid_k_contribution(rung_result_schema):
    instance = json.loads(json.dumps(VALID_RUNG_RESULT))
    instance["k_contribution"] = 2
    _expect_invalid(rung_result_schema, instance)


def test_rung_result_rejects_invalid_comparison(rung_result_schema):
    instance = json.loads(json.dumps(VALID_RUNG_RESULT))
    instance["measurements"]["null_abstention_floor"]["comparison"] = "wald_se"
    _expect_invalid(rung_result_schema, instance)


# ---------- lock_record_schema tests ----------

VALID_LOCK_RECORD: dict[str, Any] = {
    "schema_version": "v0.2",
    "state": "PENDING",
    "identity": {
        "lane": "lane-1a-prime",
        "sweep_id": None,
        "created_at": "2026-06-11T00:00:00Z",
    },
    "bound_hashes": {
        "design_packet_hash": None,
        "control_prompt_shell_hash": None,
    },
    "bound_versions": {
        "addendum_path": "governance/standing/PRE-LOCK-INSTRUMENT-VALIDATION-ADDENDUM.md",
        "addendum_sha256": "124f6046d57d365dd47596877fd1eb09088f6990ec3c9a52ac150d0c8ca103b8",
        "addendum_adoption_commit": "e76e7f8",
        "paper3_tag": "paper3-certification-protocol-v1.1",
    },
    "token_prior_authorization": {"state": "NOT_AUTHORIZED"},
    "c2_considered_memos": [],
    "g1_open_check": {"g1_open_count": 0, "pending_memo_ids": []},
    "r6_inheritance_screen": {"screened_prior_lane_requirements": []},
    "audit": {"created_by": "CS Engineer"},
}


def test_lock_record_valid_pending(lock_record_schema):
    _validate(lock_record_schema, VALID_LOCK_RECORD)


def test_lock_record_rejects_invalid_state(lock_record_schema):
    instance = json.loads(json.dumps(VALID_LOCK_RECORD))
    instance["state"] = "PROMISING"
    _expect_invalid(lock_record_schema, instance)


def test_lock_record_rejects_invalid_lane(lock_record_schema):
    instance = json.loads(json.dumps(VALID_LOCK_RECORD))
    instance["identity"]["lane"] = "something-else"
    _expect_invalid(lock_record_schema, instance)


def test_lock_record_rejects_invalid_schema_version(lock_record_schema):
    instance = json.loads(json.dumps(VALID_LOCK_RECORD))
    instance["schema_version"] = "v0.1"
    _expect_invalid(lock_record_schema, instance)


def test_lock_record_rejects_invalid_addendum_path(lock_record_schema):
    """The addendum_path constant is pinned to the adopted standing
    path. Any other path is invalid (closes Path Conventions rule)."""
    instance = json.loads(json.dumps(VALID_LOCK_RECORD))
    instance["bound_versions"]["addendum_path"] = "governance/2026-06-10_lane1a/addendum.md"
    _expect_invalid(lock_record_schema, instance)


def test_lock_record_rejects_invalid_addendum_hash(lock_record_schema):
    instance = json.loads(json.dumps(VALID_LOCK_RECORD))
    instance["bound_versions"]["addendum_sha256"] = "0" * 64
    _expect_invalid(lock_record_schema, instance)


def test_lock_record_rejects_invalid_token_prior_state(lock_record_schema):
    instance = json.loads(json.dumps(VALID_LOCK_RECORD))
    instance["token_prior_authorization"]["state"] = "MAYBE_AUTHORIZED"
    _expect_invalid(lock_record_schema, instance)


def test_lock_record_rejects_invalid_c2_review_state(lock_record_schema):
    instance = json.loads(json.dumps(VALID_LOCK_RECORD))
    instance["c2_considered_memos"] = [{
        "memo_id": "x",
        "memo_path": "x",
        "memo_sha256": "0" * 64,
        "review_state": "PROBABLY_DELIVERED",
        "considered_for_gate": "D2",
    }]
    _expect_invalid(lock_record_schema, instance)


def test_lock_record_accepts_null_sweep_id(lock_record_schema):
    instance = json.loads(json.dumps(VALID_LOCK_RECORD))
    assert instance["identity"]["sweep_id"] is None
    _validate(lock_record_schema, instance)


# ---------- cross-schema invariants ----------

ALL_SCHEMAS = [
    "manifest_schema.yaml",
    "sidecar_schema.yaml",
    "rung_result_schema.yaml",
    "lock_record_schema.yaml",
]


def _all_schema_strings() -> list[str]:
    """Return the raw text of all four schemas concatenated."""
    return [(SCHEMAS_DIR / name).read_text() for name in ALL_SCHEMAS]


def _walk_enums(obj: Any):
    """Yield every string value appearing inside any `enum` or `const`
    keyword in the parsed schema. Comments and descriptions are not
    visited (they were stripped by yaml.safe_load)."""
    if isinstance(obj, dict):
        if "enum" in obj and isinstance(obj["enum"], list):
            for v in obj["enum"]:
                if isinstance(v, str):
                    yield v
        if "const" in obj and isinstance(obj["const"], str):
            yield obj["const"]
        for value in obj.values():
            yield from _walk_enums(value)
    elif isinstance(obj, list):
        for item in obj:
            yield from _walk_enums(item)


def test_no_fails_token_in_any_enum_value(
    manifest_schema, sidecar_schema, rung_result_schema, lock_record_schema
):
    """Cross-schema invariant: no enum or const string value carries
    a `fails` token. Closes the joint disposition rule: descriptive
    serialized labels only; no fails-shaped vocab. Checked against
    the parsed schema values (comments stripped by yaml.safe_load),
    so anti-fails NOTE comments in the source are correctly ignored."""
    for schema in (manifest_schema, sidecar_schema, rung_result_schema, lock_record_schema):
        for value in _walk_enums(schema):
            assert "fails" not in value.lower(), f"`fails` token found in enum/const value: {value}"


def test_no_passes_token_in_any_outcome_or_label(rung_result_schema, sidecar_schema):
    """Cross-schema invariant: no enum value contains `passes_`.
    Closes the no-survivor-ranking doctrine in schema."""
    for schema in (rung_result_schema, sidecar_schema):
        for enum_value in _walk_enums(schema):
            assert "passes_" not in enum_value, f"`passes_` found in enum value: {enum_value}"
            assert not enum_value.startswith("passes"), f"value starts with `passes`: {enum_value}"


def test_artifact_label_vocabulary_consistent_with_e15():
    """Artifact labels in sidecar_schema match the addendum E15 +
    Non-Auth Language v0.2 §6 vocabulary."""
    text = (SCHEMAS_DIR / "sidecar_schema.yaml").read_text()
    expected = [
        "SYNTHETIC — NON-BINDING — NOT FOR THRESHOLD DERIVATION",
        "RECONNAISSANCE — NON-BINDING — NOT FOR THRESHOLD DERIVATION",
        "DIAGNOSTIC — NON-BINDING — NOT FOR THRESHOLD DERIVATION",
    ]
    for label in expected:
        assert label in text, f"E15 label missing from sidecar_schema: {label}"


def test_scrambled_binding_retrieval_never_in_elimination_basis(sidecar_schema):
    """DE-2 + AL-Q2-schema Layer-2 closure: scrambled_binding_retrieval
    is structurally unrepresentable in any elimination basis.

    Walks the parsed sidecar schema; finds the basis_policies enum
    in the elimination_label_basis definition; asserts no control
    name appears. (Comments containing the control name for
    documentation are correctly ignored by yaml.safe_load.)
    """
    defs = sidecar_schema.get("definitions", {})
    basis_def = defs.get("elimination_label_basis")
    assert basis_def is not None, "elimination_label_basis definition missing"
    basis_policies = basis_def["properties"]["basis_policies"]
    enum = basis_policies["items"]["enum"]
    forbidden = {
        "scrambled_binding_retrieval",
        "unconditioned_token_prior",
        "copy_completion",
    }
    illegal = forbidden.intersection(set(enum))
    assert not illegal, f"Forbidden values present in basis_policies enum: {illegal}"


def test_addendum_path_constant_pinned():
    """LOCK-RECORD's addendum_path constant matches the adopted
    standing path."""
    text = (SCHEMAS_DIR / "lock_record_schema.yaml").read_text()
    assert "governance/standing/PRE-LOCK-INSTRUMENT-VALIDATION-ADDENDUM.md" in text


def test_addendum_sha256_pinned():
    """LOCK-RECORD's addendum_sha256 constant matches the adoption
    commit hash."""
    text = (SCHEMAS_DIR / "lock_record_schema.yaml").read_text()
    assert "124f6046d57d365dd47596877fd1eb09088f6990ec3c9a52ac150d0c8ca103b8" in text


def test_paper3_tag_pinned():
    text = (SCHEMAS_DIR / "lock_record_schema.yaml").read_text()
    assert "paper3-certification-protocol-v1.1" in text
