"""Lane 1a' Phase 5 v0.2 corrective validation harness tests.

SYNTHETIC / DIAGNOSTIC -- NON-BINDING -- NOT FOR THRESHOLD DERIVATION
D2 IMPLEMENTATION ARTIFACT
NO MODEL INVOKED -- NO MODEL LOADED -- NO SWEEP EXECUTION
"""
from __future__ import annotations

import hashlib
import sys
from pathlib import Path

import jsonschema
import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from lane1a_prime.lock_packet import (  # noqa: E402
    DriftToleranceDeclaration,
    a6_final_manifest_reverification,
)
from lane1a_prime.oracle_cases import (  # noqa: E402
    ORACLE_CASE_CATALOG,
    PREDICT_FUNCTIONS,
    VALUE_POOL,
    OracleCase,
    predict_ideal_retriever,
    predict_universal_abstainer,
    predict_universal_answerer,
)
from lane1a_prime.analysis import (  # noqa: E402
    ValidationPreFlightConfig,
    ValidationPreFlightRefused,
    verify_pre_flight_config,
)
from lane1a_prime.validation import (  # noqa: E402
    ManifestRecipe,
    OracleVerification,
    T1Report,
    T3Report,
    T4Report,
    apply_policy_battery,
    assemble_instrument_validation_report,
    compute_union_envelope,
    construct_pilot_manifests,
    emit_execution_ledger,
    match_oracle_verdict,
    populate_t1_report,
    populate_t3_report,
    populate_t4_report,
    run_full_instrument_oracle_validation,
    score_policy_outputs,
)

SCHEMAS_DIR = Path(__file__).resolve().parent.parent / "schemas"


def _stratified_small_recipe(rung_id="L01", n=15, n_null=4, seed=0):
    """Build a ManifestRecipe with 5-stratum counts summing to n."""
    base = n // 5
    return ManifestRecipe(
        rung_id=rung_id,
        n_answerable=n,
        n_null=n_null,
        seed=seed,
        n_at_last_position=base,
        n_at_salient_endpoint=base,
        n_in_prefix_neighborhood=base,
        n_recency_adjacent=base,
        n_no_structural_feature=n - 4 * base,
    )


# ---------- manifest construction ----------

def test_construct_pilot_manifests_is_deterministic():
    recipe = _stratified_small_recipe(seed=42)
    r1 = construct_pilot_manifests(recipe)
    r2 = construct_pilot_manifests(recipe)
    assert r1 == r2


def test_construct_pilot_manifests_default_record_count():
    recipe = ManifestRecipe(rung_id="L01", seed=0)
    records = construct_pilot_manifests(recipe)
    assert len(records) == 96


def test_construct_pilot_manifests_stratum_split_default():
    recipe = ManifestRecipe(rung_id="L01", seed=0)
    records = construct_pilot_manifests(recipe)
    answerable = [r for r in records if r["stratum"] == "answerable"]
    null = [r for r in records if r["stratum"] == "null"]
    assert len(answerable) == 80
    assert len(null) == 16


def test_construct_pilot_manifests_schema_conformant():
    with (SCHEMAS_DIR / "manifest_schema.yaml").open() as f:
        schema = yaml.safe_load(f)
    validator = jsonschema.Draft202012Validator(schema)
    recipe = _stratified_small_recipe(seed=7)
    records = construct_pilot_manifests(recipe)
    for record in records:
        validator.validate(record)


def test_construct_pilot_manifests_pilot_final_same_seed_identical():
    """Stratified recipe: same seed -> byte-identical records.

    Under PH5-3, pilot and final with same seed produce identical
    manifests (drift = 0 by construction).
    """
    pilot_recipe = ManifestRecipe(rung_id="L01", seed=0)
    final_recipe = ManifestRecipe(rung_id="L01", seed=0)
    assert construct_pilot_manifests(pilot_recipe) == construct_pilot_manifests(final_recipe)


def test_manifest_recipe_rejects_stratification_sum_mismatch():
    """ManifestRecipe.__post_init__ enforces 5-stratum count sum."""
    with pytest.raises(ValueError, match="must equal n_answerable"):
        ManifestRecipe(
            rung_id="L01",
            n_answerable=80,
            n_at_last_position=12,
            n_at_salient_endpoint=12,
            n_in_prefix_neighborhood=12,
            n_recency_adjacent=12,
            n_no_structural_feature=20,  # Sum = 68 != 80
        )


# ---------- PH5-4 pre-flight refusal ----------

def test_preflight_refuses_on_missing_artifact(tmp_path):
    """Pre-flight raises ValidationPreFlightRefused when an artifact is missing."""
    missing = tmp_path / "does_not_exist.json"
    other = tmp_path / "exists.json"
    other.write_text("{}")
    real_hash = hashlib.sha256(b"{}").hexdigest()
    config = ValidationPreFlightConfig(
        oracle_verdict_table_path=missing,
        oracle_verdict_table_hash=real_hash,
        t3_bounds_path=other,
        t3_bounds_hash=real_hash,
        stratified_recipe_path=other,
        stratified_recipe_hash=real_hash,
    )
    with pytest.raises(ValidationPreFlightRefused, match="missing"):
        verify_pre_flight_config(config)


def test_preflight_refuses_on_hash_mismatch(tmp_path):
    """Pre-flight raises ValidationPreFlightRefused when sha256 mismatches."""
    f = tmp_path / "artifact.json"
    f.write_text('{"k": "v"}')
    wrong_hash = "0" * 64
    config = ValidationPreFlightConfig(
        oracle_verdict_table_path=f,
        oracle_verdict_table_hash=wrong_hash,
        t3_bounds_path=f,
        t3_bounds_hash=wrong_hash,
        stratified_recipe_path=f,
        stratified_recipe_hash=wrong_hash,
    )
    with pytest.raises(ValidationPreFlightRefused, match="hash mismatch"):
        verify_pre_flight_config(config)


def test_preflight_passes_on_matching_hashes(tmp_path):
    """Pre-flight returns silently when all three hashes match."""
    f = tmp_path / "artifact.json"
    payload = b'{"k": "v"}'
    f.write_bytes(payload)
    real_hash = hashlib.sha256(payload).hexdigest()
    config = ValidationPreFlightConfig(
        oracle_verdict_table_path=f,
        oracle_verdict_table_hash=real_hash,
        t3_bounds_path=f,
        t3_bounds_hash=real_hash,
        stratified_recipe_path=f,
        stratified_recipe_hash=real_hash,
    )
    verify_pre_flight_config(config)


def test_manifest_recipe_default_is_locked_5_stratum_schedule():
    """Locked schedule per PH5-1: 12/12/12/12/32 + 16 NULL = 96."""
    recipe = ManifestRecipe(rung_id="L01")
    assert recipe.n_at_last_position == 12
    assert recipe.n_at_salient_endpoint == 12
    assert recipe.n_in_prefix_neighborhood == 12
    assert recipe.n_recency_adjacent == 12
    assert recipe.n_no_structural_feature == 32
    assert recipe.n_answerable == 80
    assert recipe.n_null == 16


# ---------- policy battery ----------

def test_apply_policy_battery_deterministic():
    recipe = _stratified_small_recipe(seed=0)
    records = construct_pilot_manifests(recipe)
    r1 = apply_policy_battery(records)
    r2 = apply_policy_battery(records)
    assert {p: [(o.policy_name, o.predicted_value_token_ids) for o in outs] for p, outs in r1.items()} == \
           {p: [(o.policy_name, o.predicted_value_token_ids) for o in outs] for p, outs in r2.items()}


def test_apply_policy_battery_has_all_five_policies():
    recipe = _stratified_small_recipe(seed=0)
    records = construct_pilot_manifests(recipe)
    out = apply_policy_battery(records)
    assert set(out.keys()) == {
        "pure_last_position",
        "salient_endpoint",
        "recency_excluding_target",
        "prefix_neighbor_confusion",
        "copy_completion",
    }


# ---------- oracle case catalog (v0.2 = 12 cases) ----------

def test_oracle_case_catalog_has_twelve_cases():
    """v0.2 catalog has 12 oracle cases (ORC-01 through ORC-12)."""
    assert len(ORACLE_CASE_CATALOG) == 12


def test_oracle_case_catalog_covers_all_required_types():
    types = {c.oracle_case_type for c in ORACLE_CASE_CATALOG}
    required = {
        "ideal_retriever",
        "pure_last_position_shortcut",
        "salient_endpoint_shortcut",
        "recency_excluding_target_shortcut",
        "prefix_neighbor_confusion_shortcut",
        "token_prior_emitter",
        "universal_answerer",
        "universal_abstainer",
        "perfect_null_on_null_handler",
        "malformed_control_semantic_separation_guard",
        "mixture_shortcut_heavy",
        "mixture_retrieval_heavy",
    }
    assert types == required


def test_oracle_cases_have_label_set_fields():
    """Each OracleCase has the 4 label-set fields (v0.2)."""
    for case in ORACLE_CASE_CATALOG:
        assert hasattr(case, "expected_outcome")
        assert hasattr(case, "required_labels")
        assert hasattr(case, "permitted_co_labels")
        assert hasattr(case, "required_absent_labels")
        assert isinstance(case.required_labels, tuple)
        assert isinstance(case.permitted_co_labels, tuple)
        assert isinstance(case.required_absent_labels, tuple)


def test_orc_01_ideal_retriever_required_absent_all_six():
    """ORC-01 ideal retriever: all 6 elimination labels must be absent."""
    orc01 = [c for c in ORACLE_CASE_CATALOG if c.oracle_case_id == "ORC-01"][0]
    assert orc01.expected_outcome == "not_ruled_out"
    assert len(orc01.required_absent_labels) == 6


def test_orc_10_malformed_control_required_absent_token_prior():
    """ORC-10 v1-mislabeling regression: TP must be absent."""
    orc10 = [c for c in ORACLE_CASE_CATALOG if c.oracle_case_id == "ORC-10"][0]
    assert orc10.expected_outcome == "not_ruled_out"
    assert "accuracy_indistinguishable_from_token_prior" in orc10.required_absent_labels


# ---------- match_oracle_verdict (PH5-2) ----------

def test_match_oracle_verdict_all_clauses_pass():
    case = OracleCase(
        oracle_case_id="TEST",
        oracle_case_type="test",
        expected_outcome="not_ruled_out",
        required_labels=("null_abstention_floor_unmet",),
        permitted_co_labels=("answerable_abstention_ceiling_exceeded",),
        required_absent_labels=("accuracy_indistinguishable_from_token_prior",),
        description="test",
    )
    result = match_oracle_verdict(
        case,
        actual_outcome="not_ruled_out",
        attached_labels=frozenset({"null_abstention_floor_unmet"}),
    )
    assert result.outcome_matched is True
    assert result.required_labels_present is True
    assert result.required_absent_labels_absent is True
    assert result.only_required_or_permitted_attached is True
    assert result.overall_matched is True


def test_match_oracle_verdict_outcome_mismatch():
    case = OracleCase(
        oracle_case_id="TEST",
        oracle_case_type="test",
        expected_outcome="eliminated",
        required_labels=(),
        permitted_co_labels=(),
        required_absent_labels=(),
        description="test",
    )
    result = match_oracle_verdict(
        case,
        actual_outcome="not_ruled_out",
        attached_labels=frozenset(),
    )
    assert result.outcome_matched is False
    assert result.overall_matched is False


def test_match_oracle_verdict_required_label_missing():
    case = OracleCase(
        oracle_case_id="TEST",
        oracle_case_type="test",
        expected_outcome="eliminated",
        required_labels=("null_abstention_floor_unmet",),
        permitted_co_labels=(),
        required_absent_labels=(),
        description="test",
    )
    result = match_oracle_verdict(
        case,
        actual_outcome="eliminated",
        attached_labels=frozenset({"answerable_abstention_ceiling_exceeded"}),
    )
    assert result.required_labels_present is False
    assert result.overall_matched is False


def test_match_oracle_verdict_required_absent_present():
    case = OracleCase(
        oracle_case_id="TEST",
        oracle_case_type="test",
        expected_outcome="not_ruled_out",
        required_labels=(),
        permitted_co_labels=(),
        required_absent_labels=("accuracy_indistinguishable_from_token_prior",),
        description="test",
    )
    result = match_oracle_verdict(
        case,
        actual_outcome="not_ruled_out",
        attached_labels=frozenset({"accuracy_indistinguishable_from_token_prior"}),
    )
    assert result.required_absent_labels_absent is False
    assert result.overall_matched is False


def test_match_oracle_verdict_unexpected_label():
    case = OracleCase(
        oracle_case_id="TEST",
        oracle_case_type="test",
        expected_outcome="eliminated",
        required_labels=("null_abstention_floor_unmet",),
        permitted_co_labels=(),
        required_absent_labels=(),
        description="test",
    )
    # Attached has the required label PLUS an unexpected one
    result = match_oracle_verdict(
        case,
        actual_outcome="eliminated",
        attached_labels=frozenset({
            "null_abstention_floor_unmet",
            "strict_content_gap_instability",
        }),
    )
    assert result.required_labels_present is True
    assert result.only_required_or_permitted_attached is False
    assert result.overall_matched is False


# ---------- full-instrument oracle validation ----------

def test_full_instrument_oracle_validation_returns_12_verifications():
    recipe = ManifestRecipe(rung_id="L01", seed=0)
    records = construct_pilot_manifests(recipe)
    verifications = run_full_instrument_oracle_validation(records)
    assert len(verifications) == 12
    for v in verifications:
        assert isinstance(v, OracleVerification)


def test_full_instrument_ideal_retriever_passes():
    recipe = ManifestRecipe(rung_id="L01", seed=0)
    records = construct_pilot_manifests(recipe)
    verifications = run_full_instrument_oracle_validation(records)
    ideal = [v for v in verifications if v.oracle_case_id == "ORC-01"][0]
    assert ideal.actual_outcome == "not_ruled_out"


def test_full_instrument_universal_answerer_eliminated():
    recipe = ManifestRecipe(rung_id="L01", seed=0)
    records = construct_pilot_manifests(recipe)
    verifications = run_full_instrument_oracle_validation(records)
    v = [x for x in verifications if x.oracle_case_id == "ORC-07"][0]
    assert v.actual_outcome == "eliminated"
    assert "null_abstention_floor_unmet" in v.attached_labels


def test_full_instrument_universal_abstainer_eliminated():
    recipe = ManifestRecipe(rung_id="L01", seed=0)
    records = construct_pilot_manifests(recipe)
    verifications = run_full_instrument_oracle_validation(records)
    v = [x for x in verifications if x.oracle_case_id == "ORC-08"][0]
    assert v.actual_outcome == "eliminated"
    assert "answerable_abstention_ceiling_exceeded" in v.attached_labels


# ---------- T1 / T3 / T4 reports ----------

def test_populate_t1_report_includes_all_policies():
    recipe = ManifestRecipe(rung_id="L01", seed=0)
    records = construct_pilot_manifests(recipe)
    outputs_by_policy = apply_policy_battery(records)
    t1 = populate_t1_report(records, outputs_by_policy)
    assert isinstance(t1, T1Report)
    expected = {"pure_last_position", "salient_endpoint",
                "recency_excluding_target", "prefix_neighbor_confusion",
                "copy_completion"}
    assert set(t1.per_policy_scores.keys()) == expected


def test_populate_t3_report_has_six_criteria_rows():
    """v0.2: T3 has 6 criteria loaded from T3_BOUNDS_DECLARATION.json."""
    t3 = populate_t3_report()
    assert isinstance(t3, T3Report)
    assert len(t3.rows) == 6


def test_populate_t4_report_has_inh_and_ph5_rows():
    t4 = populate_t4_report()
    assert isinstance(t4, T4Report)
    ids = {row["review_item_id"] for row in t4.rows}
    assert {"INH-1", "INH-2", "INH-3"} <= ids
    assert {"PH5-1", "PH5-2", "PH5-3", "PH5-4", "PH5-5"} <= ids


# ---------- report assembly ----------

def test_assemble_validation_report_contains_required_sections():
    recipe = ManifestRecipe(rung_id="L01", seed=0)
    records = construct_pilot_manifests(recipe)
    outputs = apply_policy_battery(records)
    t1 = populate_t1_report(records, outputs)
    t3 = populate_t3_report()
    t4 = populate_t4_report()
    verifications = run_full_instrument_oracle_validation(records)
    report = assemble_instrument_validation_report(t1, t3, t4, verifications, "L01")
    assert "Instrument Validation Report" in report
    assert "SYNTHETIC / DIAGNOSTIC" in report
    assert "T1 — Battery Degeneracy Audit" in report
    assert "T3 — Ideal-Witness" in report
    assert "T4 — Review-to-Lock Disposition Table" in report
    assert "Full-instrument oracle validation" in report
    assert "Report-level non-claim" in report
    assert "LOCK-RECORD remains PENDING" in report


def test_assemble_validation_report_includes_retention_block():
    recipe = ManifestRecipe(rung_id="L01", seed=0)
    records = construct_pilot_manifests(recipe)
    outputs = apply_policy_battery(records)
    t1 = populate_t1_report(records, outputs)
    t3 = populate_t3_report()
    t4 = populate_t4_report()
    verifications = run_full_instrument_oracle_validation(records)
    report = assemble_instrument_validation_report(
        t1, t3, t4, verifications, "L01",
        run_1_retention_pointer="validation/superseded_run-1/",
    )
    assert "Run-1 Retention" in report
    assert "pilot_iteration_count" in report
    assert "validation/superseded_run-1/" in report


# ---------- execution ledger ----------

def test_emit_execution_ledger_carries_four_confirmations(tmp_path: Path):
    sample = tmp_path / "sample.txt"
    sample.write_text("synthetic data")
    ledger = emit_execution_ledger(
        files_created=[sample],
        what_was_generated="x",
        what_was_computed="y",
    )
    assert ledger["no_model_invoked"] == "CONFIRMED"
    assert ledger["no_sweep_id_created"] == "CONFIRMED"
    assert ledger["no_sweep_execution"] == "CONFIRMED"
    assert ledger["no_candidate_or_model_outputs"] == "CONFIRMED"
    assert "SYNTHETIC/DIAGNOSTIC" in ledger["outputs_validation_only"]


# ---------- source-level invariants ----------

def test_validation_source_no_fails_token():
    src = (Path(__file__).resolve().parent.parent / "lane1a_prime" / "validation.py").read_text()
    assert "fails" not in src.lower()


def test_oracle_cases_source_no_fails_token():
    src = (Path(__file__).resolve().parent.parent / "lane1a_prime" / "oracle_cases.py").read_text()
    assert "fails" not in src.lower()


def test_validation_source_no_model_imports():
    src = (Path(__file__).resolve().parent.parent / "lane1a_prime" / "validation.py").read_text()
    for forbidden in ("import mlx_lm", "from mlx_lm", ".from_pretrained(", ".load_model("):
        assert forbidden not in src


def test_oracle_cases_source_no_model_imports():
    src = (Path(__file__).resolve().parent.parent / "lane1a_prime" / "oracle_cases.py").read_text()
    for forbidden in ("import mlx_lm", "from mlx_lm", ".from_pretrained(", ".load_model("):
        assert forbidden not in src
