"""
B1 v2 Harness Unit Tests
========================

24 tests covering both v1 substrate (B1-T1 through B1-T14) and v2 Paper 3
substrate (B1-T15 through B1-T24).

All tests are offline — no model load, no network. Run with:
    python -m unittest test_b1_harness -v
or:
    python test_b1_harness.py

— CS Engineer, 2026-06-09
"""

from __future__ import annotations

import hashlib
import io
import json
import sys
import tempfile
import unittest
from contextlib import redirect_stderr
from datetime import datetime, timezone, timedelta
from pathlib import Path

# Ensure code/ is importable when running this file directly
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import runner_b1_v2 as r
import structural_proxies as sp


# ─────────────────────────────────────────────────────────────────────────────
# Mock data builders
# ─────────────────────────────────────────────────────────────────────────────

def _mock_item(item_id: str = "MOCK_01") -> dict:
    return {
        "item_id": item_id,
        "chains": [
            {"chain_id": "target_chain",  "role": "target",
             "A_object": "AAAAA", "B_object": "BBBBB", "C_object": "CTCTC"},
            {"chain_id": "decoy_chain_1", "role": "decoy",
             "A_object": "DD1DD", "B_object": "DD1BB", "C_object": "CD1CD"},
            {"chain_id": "decoy_chain_2", "role": "decoy",
             "A_object": "DD2DD", "B_object": "DD2BB", "C_object": "CD2CD"},
        ],
        "object_roles": {
            "AAAAA": "anchor_A",
            "BBBBB": "hop1_B",
            "CTCTC": "answer_C",
            "DD1DD": "other_context",
            "DD1BB": "distractor_chain_intermediate",
            "CD1CD": "distractor_chain_endpoint",
            "DD2DD": "other_context",
            "DD2BB": "distractor_chain_intermediate",
            "CD2CD": "distractor_chain_endpoint",
            "FILLR": "inert_filler",
            "NGHBR": "target_neighbor_decoy",
            "NULL":  "NULL_NO_LINK",
        },
        "queries": {
            "hop1":           {"expected_answer": "BBBBB", "query_anchor": "AAAAA"},
            "hop2":           {"expected_answer": "CTCTC", "query_anchor": "BBBBB"},
            "composite":      {"expected_answer": "CTCTC", "query_anchor": "AAAAA"},
            "negative_graph": {"expected_answer": "NULL",  "query_anchor": "AAAAA"},
        },
        "context": {
            "ordered_facts": [
                {"position_index": 1, "chain_id": "decoy_chain_1",  "fact_role": "decoy_hop1_fact",
                 "text": "DD1DD links to DD1BB."},
                {"position_index": 2, "chain_id": "target_chain",   "fact_role": "hop1_fact",
                 "text": "AAAAA links to BBBBB."},
                {"position_index": 3, "chain_id": "decoy_chain_1",  "fact_role": "decoy_hop2_fact",
                 "text": "DD1BB maps to CD1CD."},
                {"position_index": 4, "chain_id": "target_chain",   "fact_role": "neighbor_decoy_fact",
                 "text": "FILLR holds NGHBR."},
                {"position_index": 5, "chain_id": "target_chain",   "fact_role": "hop2_fact",
                 "text": "BBBBB maps to CTCTC."},
                {"position_index": 6, "chain_id": "decoy_chain_2",  "fact_role": "decoy_hop1_fact",
                 "text": "DD2DD links to DD2BB."},
                {"position_index": 7, "chain_id": "decoy_chain_2",  "fact_role": "decoy_hop2_fact",
                 "text": "DD2BB maps to CD2CD."},
            ],
        },
    }


def _mock_result_records(*, gate2_pass: bool = False, fsf_count: int = 0,
                         max_det_dummy: str = "always_return_first_C",
                         max_det_count: int = 1) -> list:
    """Build a synthetic results list (96 records = 24 items x 4 query types).

    By default produces a Gate 2 FAIL profile (hop1 < 21/24). Set gate2_pass=True
    to produce a passing profile.
    """
    out = []
    hop1_pass = 22 if gate2_pass else 6
    comp_pass = 22 if gate2_pass else 15
    for i in range(24):
        item_id = f"mock_i{i+1:02d}"
        for qt in r.QUERY_TYPES:
            # Determine is_correct and format_class for this record
            if qt == "hop1":
                is_correct = i < hop1_pass
            elif qt == "hop2":
                is_correct = i < 23
            elif qt == "composite":
                is_correct = i < comp_pass
            else:  # negative_graph
                is_correct = False
            fc = "FORMAT_PASS"
            # Make first `fsf_count` hop2 items FSF
            failure_class = "correct" if is_correct else "wrong_chain_selection"
            if qt == "hop2" and i < fsf_count:
                fc = "FORMAT_FAIL"
                is_correct = False
                failure_class = "format_scaffold_failure"
            # Dummy baselines: max_det_dummy gets max_det_count "hits" on composite
            dummy_baselines = {
                "always_return_B_target":  0.0,
                "always_return_anchor_A":  0.0,
                "always_return_first_C":   1.0 if (qt == "composite" and max_det_dummy == "always_return_first_C" and i < max_det_count) else 0.0,
                "always_return_second_C":  1.0 if (qt == "composite" and max_det_dummy == "always_return_second_C" and i < max_det_count) else 0.0,
                "always_return_third_C":   1.0 if (qt == "composite" and max_det_dummy == "always_return_third_C" and i < max_det_count) else 0.0,
                "always_return_last_C":    1.0 if (qt == "composite" and max_det_dummy == "always_return_last_C" and i < max_det_count) else 0.0,
                "always_return_ct":        1.0 if qt == "composite" else 0.0,  # ref-only; excluded from max_det
                "always_return_NULL":      0.0,                                # ref-only
                "uniform_random_expected": 0.04,                               # nondeterministic
            }
            record = {
                "item_id":                 item_id,
                "query_type":              qt,
                "prompt_rendered_hash":    "sha256:test",
                "raw_output":              f"ANSWER: {'X' if not is_correct else 'CTCTC'}",
                "failure_class":           failure_class,
                "scaffold_class":          "SCAFFOLD_PRESENT",
                "format_class":            fc,
                "returned_token":          "CTCTC" if is_correct else "X",
                "returned_role":           "answer_C" if is_correct else "other",
                "is_correct":              is_correct,
                "dummy_baselines":         dummy_baselines,
                "s8_diagnostics":          {},
                "fp16_raw_output":         f"ANSWER: {'X' if not is_correct else 'CTCTC'}",
                "exact_output_match":      True,
                "same_error_identity_key": f"{failure_class}|SCAFFOLD_PRESENT|{fc}",
                "structural_proxies":      {},
            }
            out.append(record)
    return out


# ─────────────────────────────────────────────────────────────────────────────
# v1 tests: B1-T1 through B1-T14
# ─────────────────────────────────────────────────────────────────────────────

class TestV1Substrate(unittest.TestCase):

    def test_B1_T1_mlx_lm_version_slot_in_provenance(self):
        """B1-T1: provenance schema includes mlx_lm_version slot (populated in live mode)."""
        # The runner always sets mlx_lm_version key (None in dry-run, populated in live).
        # Verify the runner's main() flow creates this key. We can do this by
        # inspecting the source-level assignment.
        source = (HERE / "runner_b1_v2.py").read_text()
        self.assertIn('"mlx_lm_version":', source,
                      "mlx_lm_version key must be present in provenance dict")

    def test_B1_T2_python_version_in_provenance(self):
        """B1-T2: python_version is populated from sys.version."""
        source = (HERE / "runner_b1_v2.py").read_text()
        self.assertIn('"python_version":', source)
        self.assertIn("sys.version", source)

    def test_B1_T3_model_snapshot_hash_format(self):
        """B1-T3: model_snapshot_hash returns sha256:... format."""
        with tempfile.TemporaryDirectory() as tmp:
            tmpdir = Path(tmp)
            (tmpdir / "weights.bin").write_bytes(b"abc")
            (tmpdir / "config.json").write_text("{}")
            h = r.compute_model_snapshot_hash(tmpdir)
            self.assertTrue(h.startswith("sha256:"))
            self.assertEqual(len(h), 7 + 64)

    def test_B1_T4_precision_rung_field(self):
        """B1-T4: precision_rung == 'FP16' for FP16 base runner."""
        # Check via the provenance dict construction in main()
        source = (HERE / "runner_b1_v2.py").read_text()
        self.assertIn('"precision_rung":           "FP16"', source)

    def test_B1_T5_gate_summary_schema(self):
        """B1-T5: gate_summary has gate_1, gate_2, gate_5 keys."""
        results = _mock_result_records(gate2_pass=False)
        gs = r.evaluate_two_hop_l1_gates(results, "sha256:test")
        for k in ("gate_1", "gate_2", "gate_5"):
            self.assertIn(k, gs, f"Missing {k}")

    def test_B1_T6_stress_eligible_false_when_gate2_fail(self):
        """B1-T6: stress_eligible False when Gate 2 fails."""
        results = _mock_result_records(gate2_pass=False)
        gs = r.evaluate_two_hop_l1_gates(results, "sha256:test")
        eligible, reason = r.determine_stress_eligible(gs)
        self.assertFalse(eligible)
        self.assertTrue(reason.startswith("GATE2_FAIL"))

    def test_B1_T7_same_error_identity_key_format(self):
        """B1-T7: per-item same_error_identity_key matches f'{failure_class}|{scaffold_class}|{format_class}'."""
        scored = {"failure_class": "wrong_chain_selection",
                  "scaffold_class": "SCAFFOLD_PRESENT", "format_class": "FORMAT_PASS",
                  "returned_token": "X", "returned_role": "other", "is_correct": False}
        record = r.make_per_item_record("i01", "composite", "sha256:test",
                                         "ANSWER: X", scored, {}, {})
        self.assertEqual(record["same_error_identity_key"],
                         "wrong_chain_selection|SCAFFOLD_PRESENT|FORMAT_PASS")

    def test_B1_T8_exact_output_match_true_for_fp16(self):
        """B1-T8: per-item exact_output_match is True for FP16 base run."""
        scored = {"failure_class": "correct", "scaffold_class": "SCAFFOLD_PRESENT",
                  "format_class": "FORMAT_PASS", "returned_token": "CTCTC",
                  "returned_role": "answer_C", "is_correct": True}
        record = r.make_per_item_record("i01", "composite", "sha256:test",
                                         "ANSWER: CTCTC", scored, {}, {})
        self.assertTrue(record["exact_output_match"])
        self.assertEqual(record["fp16_raw_output"], "ANSWER: CTCTC")

    def test_B1_T9_compute_model_snapshot_hash_deterministic(self):
        """B1-T9: compute_model_snapshot_hash is deterministic."""
        with tempfile.TemporaryDirectory() as tmp:
            tmpdir = Path(tmp)
            (tmpdir / "weights.bin").write_bytes(b"deterministic_test_payload")
            (tmpdir / "config.json").write_text("{}")
            h1 = r.compute_model_snapshot_hash(tmpdir)
            h2 = r.compute_model_snapshot_hash(tmpdir)
            self.assertEqual(h1, h2)

    def test_B1_T10_runtime_fail_closed_prints_message(self):
        """B1-T10: runtime fail-closed block prints STRESS-ELIGIBILITY FAIL message."""
        results = _mock_result_records(gate2_pass=False)
        gs = r.evaluate_two_hop_l1_gates(results, "sha256:test")
        _, reason = r.determine_stress_eligible(gs)
        buf = io.StringIO()
        with redirect_stderr(buf):
            r.runtime_fail_closed_block(False, reason, gs)
        out = buf.getvalue()
        self.assertIn("STRESS-ELIGIBILITY FAIL", out)
        self.assertIn("Do not proceed to stress runs", out)

    def test_B1_T11_eligibility_reason_code_fail_format(self):
        """B1-T11: eligibility_reason_code uses GATE_*_FAIL_* pattern on fail."""
        results = _mock_result_records(gate2_pass=False)
        gs = r.evaluate_two_hop_l1_gates(results, "sha256:test")
        eligible, reason = r.determine_stress_eligible(gs)
        self.assertFalse(eligible)
        self.assertTrue(reason.startswith("GATE2_FAIL"))
        # Pattern includes the actual count
        self.assertIn("HOP1_6", reason)

    def test_B1_T12_eligibility_reason_code_pass_format(self):
        """B1-T12: eligibility_reason_code uses STRESS_ELIGIBLE_* pattern on pass."""
        results = _mock_result_records(gate2_pass=True)
        gs = r.evaluate_two_hop_l1_gates(results, "sha256:test")
        eligible, reason = r.determine_stress_eligible(gs)
        self.assertTrue(eligible)
        self.assertTrue(reason.startswith("STRESS_ELIGIBLE_"))

    def test_B1_T13_voided_run_log_empty_for_clean_run(self):
        """B1-T13: voided_run_log present and empty for clean run."""
        # The runner sets voided_run_log = [] in the output dict construction.
        source = (HERE / "runner_b1_v2.py").read_text()
        self.assertIn('"voided_run_log":           [],', source)

    def test_B1_T14_quant_method_none_for_fp16(self):
        """B1-T14: quant_method == 'none' for FP16 base run."""
        source = (HERE / "runner_b1_v2.py").read_text()
        self.assertIn('"quant_method":             "none"', source)


# ─────────────────────────────────────────────────────────────────────────────
# v2 tests: B1-T15 through B1-T24
# ─────────────────────────────────────────────────────────────────────────────

class TestV2Substrate(unittest.TestCase):

    def test_B1_T15_analysis_script_hash_present(self):
        """B1-T15: analysis_script_hash present in provenance and starts with sha256:."""
        h = r.compute_analysis_script_hash()
        self.assertTrue(h.startswith("sha256:"))
        self.assertEqual(h, "sha256:in-runner")

    def test_B1_T16_first_candidate_data_access_timestamp_is_iso8601(self):
        """B1-T16: first_candidate_data_access_timestamp is a valid ISO-8601 UTC string."""
        ts = r.now_utc_iso()
        # Parsing as ISO-8601 should succeed
        parsed = datetime.fromisoformat(ts)
        self.assertIsNotNone(parsed.tzinfo, "Timestamp must be timezone-aware")

    def test_B1_T17_framework_version_config_vs_sheet_agreement(self):
        """B1-T17: framework_version validated against sheet, NOT against hardcoded literal.

        Per Manager C2: test config-vs-sheet agreement. Use an arbitrary, non-hardcoded
        framework_version string. The runner must accept whatever value the sheet declares
        when config matches.
        """
        # Arbitrary string (NOT the Paper 3 v0.4 literal)
        arbitrary_version = "arbitrary-test-framework-v9.9"
        # Same on both sides: passes
        r.validate_framework_version_agreement(arbitrary_version, arbitrary_version)
        # Mismatch: raises
        with self.assertRaises(r.ThresholdSheetError):
            r.validate_framework_version_agreement(arbitrary_version, "different-version")

    def test_B1_T18_threshold_sheet_hash_verification_before_trust(self):
        """B1-T18: load_threshold_sheet verifies hash BEFORE trusting content (Manager C3)."""
        with tempfile.TemporaryDirectory() as tmp:
            sheet_path = Path(tmp) / "sheet.json"
            sheet_content = {"framework_version": "test-v1.0",
                             "threshold_sheet_timestamp": "2026-06-09T00:00:00+00:00"}
            sheet_path.write_text(json.dumps(sheet_content))
            actual_hash = "sha256:" + hashlib.sha256(sheet_path.read_bytes()).hexdigest()
            # Correct hash: loads
            sheet = r.load_threshold_sheet(sheet_path, actual_hash)
            self.assertEqual(sheet["framework_version"], "test-v1.0")
            # Wrong hash: raises BEFORE returning content
            with self.assertRaises(r.ThresholdSheetError):
                r.load_threshold_sheet(sheet_path, "sha256:" + "0" * 64)

    def test_B1_T19_gate_record_a2_schema_complete(self):
        """B1-T19: gate records populate all 13 Paper 3 A.2 schema fields."""
        rec = r.make_gate_record(
            gate_id="test_gate",
            status="pass",
            observed_value=21,
            threshold_value=20,
            reason_code="TEST_PASS",
            evidence_artifact_hash="sha256:test",
            framework_version="test-v1.0",
            threshold_sheet_hash="sha256:sheet",
        )
        required_fields = {
            "gate_id", "status", "observed_value", "threshold_value", "delta",
            "reason_code", "evidence_artifact_hash", "evaluated_by", "evaluated_at",
            "short_circuit", "framework_version", "threshold_sheet_hash",
            "analysis_script_hash",
        }
        self.assertEqual(set(rec.keys()), required_fields)
        self.assertEqual(rec["delta"], 1)  # observed - threshold = 21 - 20 = 1
        self.assertFalse(rec["short_circuit"])

    def test_B1_T20_short_circuit_field_propagates(self):
        """B1-T20: short_circuit field set correctly for skipped gates."""
        rec = r.make_gate_record(
            gate_id="skipped_gate",
            status="not_evaluated",
            observed_value=None,
            threshold_value=None,
            reason_code="SHORT_CIRCUIT_EARLIER_FAIL",
            evidence_artifact_hash="sha256:none",
            short_circuit=True,
        )
        self.assertTrue(rec["short_circuit"])
        self.assertEqual(rec["status"], "not_evaluated")

    def test_B1_T21_firewall_rejects_prelock_access(self):
        """B1-T21: data-access firewall rejects access timestamp predating sheet lock."""
        sheet_ts  = "2026-06-09T12:00:00+00:00"
        access_ts = "2026-06-09T11:59:59+00:00"  # 1 second before lock
        with self.assertRaises(r.FirewallViolation) as ctx:
            r.enforce_data_access_firewall(sheet_ts, access_ts)
        self.assertIn("FIREWALL_VIOLATION_DATA_ACCESS_PRELOCK", str(ctx.exception))

    def test_B1_T22_firewall_passes_when_access_postdates_lock(self):
        """B1-T22: firewall passes when access timestamp postdates sheet lock."""
        sheet_ts  = "2026-06-09T12:00:00+00:00"
        access_ts = "2026-06-09T12:00:01+00:00"  # 1 second after lock
        # Should not raise
        r.enforce_data_access_firewall(sheet_ts, access_ts)

    def test_B1_T23_hash_registry_rejects_mismatched_artifacts(self):
        """B1-T23: hash registry verification rejects mismatched artifacts."""
        with tempfile.TemporaryDirectory() as tmp:
            tmpdir = Path(tmp)
            fake = tmpdir / "fake_artifact.py"
            fake.write_text("# fake content")
            # Wrong expected hash
            artifacts = [("fake", fake, "sha256:" + "0" * 64)]
            # Non-strict + raise_on_mismatch path
            with self.assertRaises(r.HashRegistryMismatch):
                r.verify_locked_artifacts(strict=False, artifacts=artifacts,
                                          raise_on_mismatch=True)
            # Strict path: returns dict but the bad status is recorded
            results = r.verify_locked_artifacts(strict=False, artifacts=artifacts)
            self.assertEqual(results["fake"]["status"], "mismatch")

    def test_B1_T24_structural_proxies_deterministic(self):
        """B1-T24: structural_proxies module functions are deterministic."""
        item = _mock_item()
        # Run every registered proxy twice; outputs must match
        for name, fn in sp.PROXY_REGISTRY.items():
            v1 = fn(item)
            v2 = fn(item)
            self.assertEqual(v1, v2, f"Proxy {name} is non-deterministic")
        # Also verify compute_proxies returns consistent results
        all_names = list(sp.PROXY_REGISTRY.keys())
        p1 = sp.compute_proxies(item, all_names)
        p2 = sp.compute_proxies(item, all_names)
        self.assertEqual(p1, p2)


# ─────────────────────────────────────────────────────────────────────────────
# Additional regression coverage (paper 2 substrate sanity)
# ─────────────────────────────────────────────────────────────────────────────

class TestPaper2Regression(unittest.TestCase):
    """Spot-check that paper-2-shape v1 fields are unchanged by v2 additions."""

    def test_paper2_context_framework_version_is_none(self):
        """Paper 2 reproduction context: framework_version defaults to 'none'."""
        self.assertEqual(r.FRAMEWORK_VERSION_NONE, "none")
        self.assertEqual(r.THRESHOLD_SHEET_HASH_NONE, "none")

    def test_gate_record_in_paper2_context_has_none_framework_version(self):
        """In Paper 2 reproduction, gate records carry framework_version='none'."""
        results = _mock_result_records(gate2_pass=False)
        gs = r.evaluate_two_hop_l1_gates(results, "sha256:test")
        for gate_id, rec in gs.items():
            self.assertEqual(rec["framework_version"], "none",
                             f"{gate_id} framework_version should be 'none' in Paper 2 context")
            self.assertEqual(rec["threshold_sheet_hash"], "none")


if __name__ == "__main__":
    unittest.main(verbosity=2)
