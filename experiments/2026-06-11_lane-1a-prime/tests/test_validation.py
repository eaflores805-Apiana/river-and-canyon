"""Lane 1a' Phase 5 validation harness tests.

SYNTHETIC / DIAGNOSTIC -- NON-BINDING -- NOT FOR THRESHOLD DERIVATION
D2 IMPLEMENTATION ARTIFACT
NO MODEL INVOKED -- NO MODEL LOADED -- NO SWEEP EXECUTION

Validates the Phase 5 model-free validation harness:
  - Manifest construction deterministic + schema-conformant
  - Policy battery deterministic
  - Oracle cases cover all 9 catalog entries
  - Full-instrument oracle validation classifies the ideal retriever
    as NOT_RULED_OUT (B4 ideal-witness closure)
  - Declared-shortcut oracles get ELIMINATED
  - Perfect NULL handler is in pass region
  - A6 within tolerance for synthetic data
  - T1/T3/T4 populate
  - Execution ledger schema-conformant
"""
from __future__ import annotations

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
    ExpectedVerdict,
    PREDICT_FUNCTIONS,
    VALUE_POOL,
    predict_ideal_retriever,
    predict_universal_abstainer,
    predict_universal_answerer,
)
from lane1a_prime.validation import (  # noqa: E402
    DEFAULT_T3_CRITERIA,
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
    populate_t1_report,
    populate_t3_report,
    populate_t4_report,
    run_full_instrument_oracle_validation,
    score_policy_outputs,
)

SCHEMAS_DIR = Path(__file__).resolve().parent.parent / "schemas"


# ---------- manifest construction ----------

def test_construct_pilot_manifests_is_deterministic():
    """Same recipe -> identical records."""
    recipe = ManifestRecipe(rung_id="L01", n_answerable=10, n_null=2, seed=42)
    r1 = construct_pilot_manifests(recipe)
    r2 = construct_pilot_manifests(recipe)
    assert r1 == r2


def test_construct_pilot_manifests_record_count():
    recipe = ManifestRecipe(rung_id="L01", n_answerable=80, n_null=16, seed=0)
    records = construct_pilot_manifests(recipe)
    assert len(records) == 96


def test_construct_pilot_manifests_stratum_split():
    recipe = ManifestRecipe(rung_id="L01", n_answerable=80, n_null=16, seed=0)
    records = construct_pilot_manifests(recipe)
    answerable = [r for r in records if r["stratum"] == "answerable"]
    null = [r for r in records if r["stratum"] == "null"]
    assert len(answerable) == 80
    assert len(null) == 16


def test_construct_pilot_manifests_schema_conformant():
    """Each constructed manifest record validates against manifest_schema.yaml."""
    with (SCHEMAS_DIR / "manifest_schema.yaml").open() as f:
        schema = yaml.safe_load(f)
    validator = jsonschema.Draft202012Validator(schema)
    recipe = ManifestRecipe(rung_id="L01", n_answerable=10, n_null=2, seed=7)
    records = construct_pilot_manifests(recipe)
    for record in records:
        validator.validate(record)


def test_construct_pilot_manifests_different_seeds_differ():
    recipe1 = ManifestRecipe(rung_id="L01", n_answerable=10, n_null=2, seed=1)
    recipe2 = ManifestRecipe(rung_id="L01", n_answerable=10, n_null=2, seed=2)
    r1 = construct_pilot_manifests(recipe1)
    r2 = construct_pilot_manifests(recipe2)
    assert r1 != r2


# ---------- policy battery ----------

def test_apply_policy_battery_deterministic():
    recipe = ManifestRecipe(rung_id="L01", n_answerable=10, n_null=2, seed=0)
    records = construct_pilot_manifests(recipe)
    r1 = apply_policy_battery(records)
    r2 = apply_policy_battery(records)
    # Convert PolicyOutput dataclasses to tuples for comparison
    assert {p: [(o.policy_name, o.predicted_value_token_ids) for o in outs] for p, outs in r1.items()} == \
           {p: [(o.policy_name, o.predicted_value_token_ids) for o in outs] for p, outs in r2.items()}


def test_apply_policy_battery_has_all_five_policies():
    recipe = ManifestRecipe(rung_id="L01", n_answerable=5, n_null=1, seed=0)
    records = construct_pilot_manifests(recipe)
    out = apply_policy_battery(records)
    assert set(out.keys()) == {
        "pure_last_position",
        "salient_endpoint",
        "recency_excluding_target",
        "prefix_neighbor_confusion",
        "copy_completion",
    }


def test_score_policy_outputs_per_stratum():
    recipe = ManifestRecipe(rung_id="L01", n_answerable=10, n_null=2, seed=0)
    records = construct_pilot_manifests(recipe)
    outputs_by_policy = apply_policy_battery(records)
    score = score_policy_outputs(
        records, outputs_by_policy["pure_last_position"], "answerable"
    )
    assert score.n_effective == 10  # 10 answerable records
    assert 0.0 <= score.accuracy <= 1.0


# ---------- oracle case catalog ----------

def test_oracle_case_catalog_has_nine_cases():
    """Per Team Lead §5: must include ideal retriever, declared
    shortcut oracles, mixture oracle, universal answerer, universal
    abstainer, perfect NULL handler, malformed-control."""
    assert len(ORACLE_CASE_CATALOG) == 9


def test_oracle_case_catalog_covers_all_required_types():
    types = {c.oracle_case_type for c in ORACLE_CASE_CATALOG}
    required = {
        "ideal_retriever",
        "last_position_shortcut",
        "salient_endpoint_shortcut",
        "token_prior_emitter",
        "universal_answerer",
        "universal_abstainer",
        "perfect_null_handler",
        "mixture_oracle",
        "malformed_control",
    }
    assert types == required


def test_predict_ideal_retriever_returns_gold_on_answerable():
    recipe = ManifestRecipe(rung_id="L01", n_answerable=5, n_null=1, seed=0)
    records = construct_pilot_manifests(recipe)
    preds = predict_ideal_retriever(tuple(records))
    for r, p in zip(records, preds):
        if r["stratum"] == "answerable":
            assert p.predicted_value_token_ids == tuple(r["gold"]["value_token_ids"])
        else:  # null
            assert p.abstained


def test_predict_universal_answerer_never_abstains():
    recipe = ManifestRecipe(rung_id="L01", n_answerable=5, n_null=1, seed=0)
    records = construct_pilot_manifests(recipe)
    preds = predict_universal_answerer(tuple(records))
    for p in preds:
        assert not p.abstained


def test_predict_universal_abstainer_always_abstains():
    recipe = ManifestRecipe(rung_id="L01", n_answerable=5, n_null=1, seed=0)
    records = construct_pilot_manifests(recipe)
    preds = predict_universal_abstainer(tuple(records))
    for p in preds:
        assert p.abstained


# ---------- full-instrument oracle validation (Team Lead §5) ----------

def test_full_instrument_oracle_validation_returns_verifications():
    recipe = ManifestRecipe(rung_id="L01", n_answerable=80, n_null=16, seed=0)
    records = construct_pilot_manifests(recipe)
    verifications = run_full_instrument_oracle_validation(records)
    assert len(verifications) == len(ORACLE_CASE_CATALOG)
    # Each verification carries an expected and actual outcome
    for v in verifications:
        assert v.expected_verdict in (
            "not_ruled_out",
            "eliminated",
            "inconclusive_not_actionable",
            "flag_indeterminate",
        )
        assert v.actual_full_instrument_outcome in (
            "not_ruled_out",
            "eliminated",
            "inconclusive_not_actionable",
        )


def test_ideal_retriever_oracle_classified_not_ruled_out():
    """B4 ideal-witness closure: the ideal retriever oracle must NOT
    be eliminated by any criterion. This is the structural anti-v1-
    pathology check."""
    recipe = ManifestRecipe(rung_id="L01", n_answerable=80, n_null=16, seed=0)
    records = construct_pilot_manifests(recipe)
    verifications = run_full_instrument_oracle_validation(records)
    ideal = [v for v in verifications if v.oracle_case_type == "ideal_retriever"][0]
    assert ideal.actual_full_instrument_outcome == "not_ruled_out", (
        f"Ideal retriever was eliminated; pass region does not contain "
        f"the ideal corner. Labels: {ideal.attached_labels}"
    )


def test_perfect_null_handler_classified_not_ruled_out():
    """Perfect NULL handler (1.0 NULL abstention, 0.0 answerable
    abstention) must be in the pass region by construction."""
    recipe = ManifestRecipe(rung_id="L01", n_answerable=80, n_null=16, seed=0)
    records = construct_pilot_manifests(recipe)
    verifications = run_full_instrument_oracle_validation(records)
    perfect_null = [v for v in verifications if v.oracle_case_type == "perfect_null_handler"][0]
    assert perfect_null.actual_full_instrument_outcome == "not_ruled_out"


def test_universal_answerer_classified_eliminated():
    """Universal answerer (never abstains) -> null_abstention_floor
    criterion fires -> ELIMINATED."""
    recipe = ManifestRecipe(rung_id="L01", n_answerable=80, n_null=16, seed=0)
    records = construct_pilot_manifests(recipe)
    verifications = run_full_instrument_oracle_validation(records)
    answ = [v for v in verifications if v.oracle_case_type == "universal_answerer"][0]
    assert answ.actual_full_instrument_outcome == "eliminated"
    assert "null_abstention_floor_unmet" in answ.attached_labels


def test_universal_abstainer_classified_eliminated():
    """Universal abstainer (always abstains) -> answerable_abstention
    ceiling fires -> ELIMINATED."""
    recipe = ManifestRecipe(rung_id="L01", n_answerable=80, n_null=16, seed=0)
    records = construct_pilot_manifests(recipe)
    verifications = run_full_instrument_oracle_validation(records)
    absta = [v for v in verifications if v.oracle_case_type == "universal_abstainer"][0]
    assert absta.actual_full_instrument_outcome == "eliminated"
    assert "answerable_abstention_ceiling_exceeded" in absta.attached_labels


# ---------- A6 ----------

def test_a6_synthetic_drift_within_tolerance():
    recipe_pilot = ManifestRecipe(rung_id="L01", n_answerable=80, n_null=16, seed=0)
    recipe_final = ManifestRecipe(rung_id="L01", n_answerable=80, n_null=16, seed=1)
    pilot_records = construct_pilot_manifests(recipe_pilot)
    final_records = construct_pilot_manifests(recipe_final)
    pilot_outputs = apply_policy_battery(pilot_records)
    final_outputs = apply_policy_battery(final_records)
    pilot_scores = {
        p: score_policy_outputs(pilot_records, outs, "answerable").accuracy
        for p, outs in pilot_outputs.items()
        if p != "copy_completion"
    }
    final_scores = {
        p: score_policy_outputs(final_records, outs, "answerable").accuracy
        for p, outs in final_outputs.items()
        if p != "copy_completion"
    }
    pilot_envelope = compute_union_envelope(pilot_records, pilot_outputs)
    final_envelope = compute_union_envelope(final_records, final_outputs)
    result = a6_final_manifest_reverification(
        pilot_battery_scores=pilot_scores,
        pilot_envelope=pilot_envelope,
        final_battery_scores=final_scores,
        final_envelope=final_envelope,
        declared_drift_tolerance=DriftToleranceDeclaration(per_policy=0.50, envelope=0.50),
    )
    # With a generous tolerance, the drift should be within bounds
    # for two synthetic seeds of the same construction.
    assert result.drift_within_tolerance is True


# ---------- T1 / T3 / T4 reports ----------

def test_populate_t1_report_includes_all_policies():
    recipe = ManifestRecipe(rung_id="L01", n_answerable=20, n_null=4, seed=0)
    records = construct_pilot_manifests(recipe)
    outputs_by_policy = apply_policy_battery(records)
    t1 = populate_t1_report(records, outputs_by_policy)
    assert isinstance(t1, T1Report)
    # All five policies have per-stratum scores
    expected = {"pure_last_position", "salient_endpoint",
                "recency_excluding_target", "prefix_neighbor_confusion",
                "copy_completion"}
    assert set(t1.per_policy_scores.keys()) == expected


def test_populate_t1_report_envelope_in_valid_range():
    recipe = ManifestRecipe(rung_id="L01", n_answerable=20, n_null=4, seed=0)
    records = construct_pilot_manifests(recipe)
    outputs_by_policy = apply_policy_battery(records)
    t1 = populate_t1_report(records, outputs_by_policy)
    assert 0.0 <= t1.union_envelope_score <= 1.0


def test_populate_t3_report_has_criteria_rows():
    t3 = populate_t3_report()
    assert isinstance(t3, T3Report)
    assert len(t3.rows) == len(DEFAULT_T3_CRITERIA)
    for row in t3.rows:
        assert row["disposition"] == "pass"


def test_populate_t4_report_has_three_inh_rows():
    t4 = populate_t4_report()
    assert isinstance(t4, T4Report)
    inh_ids = {row["review_item_id"] for row in t4.rows}
    assert {"INH-1", "INH-2", "INH-3"} <= inh_ids


# ---------- report assembly ----------

def test_assemble_validation_report_contains_required_sections():
    recipe = ManifestRecipe(rung_id="L01", n_answerable=80, n_null=16, seed=0)
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
    assert "T3 — Ideal-Witness / Pass-Region Checklist" in report
    assert "T4 — Review-to-Lock Disposition Table" in report
    assert "Full-instrument oracle validation" in report
    assert "Report-level non-claim" in report
    assert "LOCK-RECORD remains PENDING" in report


# ---------- execution ledger ----------

def test_emit_execution_ledger_carries_four_confirmations(tmp_path: Path):
    sample = tmp_path / "sample.txt"
    sample.write_text("synthetic data")
    ledger = emit_execution_ledger(
        files_created=[sample],
        what_was_generated="pilot manifests by seed",
        what_was_computed="per-policy scores; envelope; oracle verdicts",
    )
    assert ledger["no_model_invoked"] == "CONFIRMED"
    assert ledger["no_sweep_id_created"] == "CONFIRMED"
    assert ledger["no_sweep_execution"] == "CONFIRMED"
    assert ledger["no_candidate_or_model_outputs"] == "CONFIRMED"
    assert "SYNTHETIC/DIAGNOSTIC" in ledger["outputs_validation_only"]


def test_execution_ledger_includes_artifact_hashes(tmp_path: Path):
    sample = tmp_path / "sample.txt"
    sample.write_text("synthetic data")
    ledger = emit_execution_ledger(
        files_created=[sample],
        what_was_generated="test",
        what_was_computed="test",
    )
    assert "sample.txt" in ledger["artifact_hashes"]
    assert len(ledger["artifact_hashes"]["sample.txt"]) == 64


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
