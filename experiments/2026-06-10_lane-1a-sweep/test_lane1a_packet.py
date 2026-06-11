"""Lane 1a packet unit tests (locked; hash-recorded in LOCK-RECORD.md).

Locks the B-series corrections (B1 gap sign, B2 inconclusive preempt,
B5 survivor rung-ID order, audit-log append-only, plot prohibitions,
schema rejection of order fields, outcome-statement determinism,
recipe acceptance check non-degeneracy).

Run from this directory:
    python -m unittest test_lane1a_packet
"""

from __future__ import annotations

import json
import os
import re
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

import analyzer  # noqa: E402
import artifact_tags  # noqa: E402
import audit_log  # noqa: E402
import dummy_policies  # noqa: E402
import manifest_generator  # noqa: E402
import plotter  # noqa: E402
import scorer  # noqa: E402


def _make_rung_record(
    *,
    rung_id="L01",
    strict_acc=0.5,
    content_acc=0.5,
    control_acc=0.5,
    union_envelope_score=0.5,
    void_count=0,
    void_a=0, void_n=0, void_am=0, void_nm=0,
    harness_anomaly_flag=False,
    missing_required_outputs_flag=False,
    abstention_rate=0.75,
    separability_flag=True,
):
    return {
        "rung_id": rung_id,
        "manifest_hash": "0" * 64,
        "N_declared": 96,
        "N_effective": 80 - void_a,
        "void_count": void_count,
        "void_count_answerable": void_a,
        "void_count_null": void_n,
        "void_count_control_answerable_mirror": void_am,
        "void_count_control_null_mirror": void_nm,
        "strict_acc": strict_acc,
        "strict_acc_se": 0.05,
        "content_acc": content_acc,
        "gap": content_acc - strict_acc,
        "control_acc": control_acc,
        "control_acc_se": 0.05,
        "max_dummy_score": 0.2,
        "union_envelope_score": union_envelope_score,
        "headroom": 1.0 - strict_acc,
        "abstention_rate": abstention_rate,
        "abstention_rate_se": 0.125,
        "separability_flag": separability_flag,
        "tokenization_stability_flag": True,
        "harness_anomaly_flag": harness_anomaly_flag,
        "missing_required_outputs_flag": missing_required_outputs_flag,
        "answer_pos_distribution": {
            "bin_counts": [10] * 8,
            "bin_count_total": 80,
            "max_deviation_sigma": 0.5,
        },
        "labels": [],
        "per_item_log_path": "raw/L01.json",
        "raw_output_dir": "raw/L01/",
        "artifact_class": "lane-1a-reconnaissance",
        "certification_relevance": "none",
    }


class TestB1GapSign(unittest.TestCase):
    """Senior v0.3 §1.6 unit test: content 0.90 / strict 0.70 -> label
    attaches."""

    def test_gap_sign_content_minus_strict(self):
        r = _make_rung_record(strict_acc=0.70, content_acc=0.90)
        labels = analyzer.assign_labels(r)
        self.assertIn("strict_content_gap_instability", labels,
                      f"B1 gap sign fix: expected label; got {labels}")

    def test_gap_below_threshold_no_label(self):
        r = _make_rung_record(strict_acc=0.80, content_acc=0.85)
        labels = analyzer.assign_labels(r)
        self.assertNotIn("strict_content_gap_instability", labels)


class TestB2InconclusivePreempts(unittest.TestCase):
    """Inconclusive preempt: if void_count>5 fires, no other label
    attaches."""

    def test_void_count_exceeded_preempts_other_labels(self):
        # Set strict_acc and content_acc such that the gap rule would
        # normally fire; void_count_total = 6 should preempt.
        r = _make_rung_record(
            strict_acc=0.70, content_acc=0.90, void_count=6, void_a=6
        )
        labels = analyzer.assign_labels(r)
        self.assertEqual(labels, ["inconclusive_not_actionable"])

    def test_harness_anomaly_preempts(self):
        r = _make_rung_record(strict_acc=0.50, content_acc=0.50, harness_anomaly_flag=True)
        labels = analyzer.assign_labels(r)
        self.assertEqual(labels, ["inconclusive_not_actionable"])

    def test_missing_outputs_preempts(self):
        r = _make_rung_record(strict_acc=0.50, content_acc=0.50, missing_required_outputs_flag=True)
        labels = analyzer.assign_labels(r)
        self.assertEqual(labels, ["inconclusive_not_actionable"])


class TestB5SurvivorOrdering(unittest.TestCase):
    """Survivors serialized in alphabetical rung-ID order."""

    def test_survivors_alphabetical(self):
        rs = [
            _make_rung_record(rung_id=rid, strict_acc=0.80, content_acc=0.81,
                              control_acc=0.30, union_envelope_score=0.30,
                              abstention_rate=0.75, separability_flag=True)
            for rid in ["L08", "L02", "L05", "L01", "L07"]
        ]
        # Force each record to attach only requires_further_investigation by
        # using strict_acc well above envelope+2*SE and headroom OK.
        for r in rs:
            r["labels"] = ["requires_further_investigation"]
        statement, survivors, K = analyzer.emit_outcome(rs)
        self.assertEqual(survivors, sorted(survivors))
        self.assertEqual(survivors, ["L01", "L02", "L05", "L07", "L08"])
        self.assertEqual(K, 5)


class TestOutcomeStatementDeterminism(unittest.TestCase):
    """No alternative string can be produced by emit_outcome."""

    def test_k_zero_emits_statement_a(self):
        rs = [
            _make_rung_record(rung_id=rid)
            for rid in ["L01", "L02"]
        ]
        for r in rs:
            r["labels"] = ["insufficient_measurement_headroom"]
        statement, survivors, K = analyzer.emit_outcome(rs)
        self.assertEqual(K, 0)
        self.assertIn(analyzer.STATEMENT_A, statement)
        self.assertIn(analyzer.STATEMENT_C, statement)

    def test_k_positive_emits_statement_b(self):
        rs = [
            _make_rung_record(rung_id="L01"),
            _make_rung_record(rung_id="L02"),
        ]
        rs[0]["labels"] = ["requires_further_investigation"]
        rs[1]["labels"] = ["insufficient_measurement_headroom"]
        statement, survivors, K = analyzer.emit_outcome(rs)
        self.assertEqual(K, 1)
        self.assertIn("1 of 8 rungs were not ruled out", statement)
        self.assertIn(analyzer.STATEMENT_C, statement)

    def test_always_appends_statement_c(self):
        rs = [_make_rung_record(rung_id="L01")]
        rs[0]["labels"] = ["requires_further_investigation"]
        statement, _, _ = analyzer.emit_outcome(rs)
        self.assertTrue(statement.endswith(analyzer.STATEMENT_C))


class TestPlotProhibitions(unittest.TestCase):
    """Every prohibited form raises NotImplementedError."""

    def test_each_prohibited_form_raises(self):
        p = plotter.Lane1aPlotter("dummy outcome")
        for prohibited in plotter.PROHIBITED_FIGURE_TYPES:
            with self.assertRaises(NotImplementedError) as cm:
                p.draw(prohibited)
            self.assertIn("§1.8", str(cm.exception))

    def test_unknown_form_raises(self):
        p = plotter.Lane1aPlotter("dummy outcome")
        with self.assertRaises(NotImplementedError):
            p.draw("scatter_3d")


class TestSchemaRejectionOfOrderFields(unittest.TestCase):
    """Per-rung schema and sweep schema reject rank/preference/best
    fields via additionalProperties:false."""

    def test_per_rung_schema_rejects_rank_field(self):
        try:
            import jsonschema
        except ImportError:
            self.skipTest("jsonschema not installed")
        schema = json.loads(
            (SCRIPT_DIR / "schema" / "per_rung_record.schema.json").read_text()
        )
        # Build a minimum-valid record then add a 'rank' field.
        base = _make_rung_record(rung_id="L01")
        base["labels"] = ["requires_further_investigation"]
        # Sanity: base is valid.
        jsonschema.validate(base, schema)
        # Inject a forbidden field.
        bad = dict(base)
        bad["rank"] = 1
        with self.assertRaises(jsonschema.ValidationError):
            jsonschema.validate(bad, schema)
        bad2 = dict(base)
        bad2["preference"] = "L01"
        with self.assertRaises(jsonschema.ValidationError):
            jsonschema.validate(bad2, schema)

    def test_sweep_schema_blocks_paper3_framework_version(self):
        try:
            import jsonschema
        except ImportError:
            self.skipTest("jsonschema not installed")
        schema = json.loads(
            (SCRIPT_DIR / "schema" / "sweep_record.schema.json").read_text()
        )
        bad = {
            "sweep_id": "lane-1a-2026-06-10",
            "framework_version": "paper3-certification-protocol-v1.1",
            # ... other fields omitted; schema requires framework_version=='none'
        }
        with self.assertRaises(jsonschema.ValidationError):
            jsonschema.validate(bad, schema)


class TestRecipeAcceptanceCheck(unittest.TestCase):
    """Every declared dummy policy must yield a non-degenerate prediction
    vector on every rung's generated manifest."""

    def test_recipe_acceptance_check_passes_on_all_rungs(self):
        with tempfile.TemporaryDirectory() as td:
            out = manifest_generator.main(Path(td))
            for r in out["acceptance_results"]:
                self.assertTrue(
                    r["all_pass"],
                    f"recipe acceptance check failed on {r['rung_id']}: "
                    f"{r['per_policy']}",
                )


class TestAuditLogAppendOnly(unittest.TestCase):
    """Writer opens file with mode 'a' only; events accumulate."""

    def test_appends(self):
        with tempfile.TemporaryDirectory() as td:
            log_path = Path(td) / "AUDIT-LOG.ndjson"
            w = audit_log.AuditLogWriter(log_path)
            w.emit("lock_record_sealed", details={"lock_record_hash": "0" * 64})
            w.emit("first_data_access", details={})
            events = w.read_all()
            self.assertEqual(len(events), 2)
            self.assertEqual(events[0]["event"], "lock_record_sealed")
            self.assertEqual(events[1]["event"], "first_data_access")

    def test_count_runner_started_gives_total_attempts(self):
        with tempfile.TemporaryDirectory() as td:
            log_path = Path(td) / "AUDIT-LOG.ndjson"
            w = audit_log.AuditLogWriter(log_path)
            for i in range(5):
                w.emit(
                    "runner_started",
                    rung_id="L01",
                    attempt_id=i,
                    stratum="answerable",
                )
            # Note: in real use no_re_execution_rule blocks repeats; this
            # tests writer behavior only.
            self.assertEqual(w.count("runner_started"), 5)


class TestArtifactTagsRejectOverride(unittest.TestCase):
    def test_override_rejected(self):
        with self.assertRaises(ValueError):
            artifact_tags.tag({"artifact_class": "paper3-certification"})
        with self.assertRaises(ValueError):
            artifact_tags.tag({"certification_relevance": "high"})

    def test_tags_injected_cleanly(self):
        out = artifact_tags.tag({"foo": "bar"})
        self.assertEqual(out["artifact_class"], "lane-1a-reconnaissance")
        self.assertEqual(out["certification_relevance"], "none")


class TestScorer(unittest.TestCase):
    def test_strict_implies_content(self):
        # If strict matches, content must also match (substring is exact).
        s = scorer.score_item("alpha", "alpha")
        self.assertTrue(s["strict"])
        self.assertTrue(s["content"])
        self.assertFalse(s["void"])

    def test_void_on_empty(self):
        s = scorer.score_item("", "alpha")
        self.assertTrue(s["void"])

    def test_abstain_detected(self):
        s = scorer.score_item("NULL", "NULL")
        self.assertTrue(s["strict"])
        self.assertTrue(s["abstained"])


class TestDummyPoliciesNondegenerate(unittest.TestCase):
    def test_each_policy_nondegenerate_on_synthetic_manifest(self):
        # Build a tiny synthetic manifest with 10 items where the LAST
        # value, the recency-match value, etc. all vary across items.
        import string
        items = []
        alphabet = list(string.ascii_lowercase)
        for i in range(10):
            keys = [f"k{i}{j}" for j in range(5)]
            # Rotate the values per item so last-position varies.
            values = [alphabet[(i + j) % 26] for j in range(5)]
            items.append({
                "item_id": f"X-{i}",
                "stratum": "answerable",
                "in_context_pairs": list(zip(keys, values)),
                "queried_key": keys[i % 5],
                "expected_answer": values[i % 5],
                "answer_slot_index": i % 5,
            })
        for name in dummy_policies.DECLARED_POLICIES:
            preds = dummy_policies.policy_predictions(name, items)
            self.assertTrue(
                dummy_policies.is_nondegenerate(preds),
                f"policy {name} degenerate: {preds}",
            )


class TestWrapperSidecarPattern(unittest.TestCase):
    """Wrapper must preserve runner output bytes byte-for-byte and record
    Lane 1a metadata in a sidecar JSON only."""

    def _stage_fake_runner_output(self, tmp: Path, rung_id: str, stratum: str) -> Path:
        out_dir = tmp / "raw"
        out_dir.mkdir()
        # Simulate a lane1a_runner.py output JSON (Path A schema).
        runner_output = {
            "lane1a_runner_record_schema": "v1",
            "rung_id": rung_id,
            "stratum": stratum,
            "manifest_path": "manifests/L01.json",
            "manifest_hash": "sha256:" + "0" * 64,
            "provenance": {
                "runner": "lane1a_runner.py",
                "framework_version": "none",
                "model_snapshot_hash": "sha256:abee745b...",
            },
            "items": [{"item_id": "x", "raw_output": "alpha"}],
        }
        path = out_dir / f"LANE1A-{rung_id}-{stratum}-1234.json"
        path.write_text(json.dumps(runner_output, sort_keys=True, indent=2), encoding="utf-8")
        return path

    def test_runner_output_preserved_byte_for_byte(self):
        """Wrapper does not modify the runner output file."""
        import lane1a_runner_wrapper as wrapper  # noqa: PLC0415
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td)
            runner_path = self._stage_fake_runner_output(tmp, "L01", "answerable")
            original_bytes = runner_path.read_bytes()
            original_sha = wrapper._sha256_file(runner_path)

            sidecar = wrapper.write_sidecar(
                runner_output_path=runner_path,
                runner_output_sha256=original_sha,
                rung_id="L01",
                stratum="answerable",
                attempt_id=1,
            )

            self.assertEqual(runner_path.read_bytes(), original_bytes)
            self.assertEqual(wrapper._sha256_file(runner_path), original_sha)
            self.assertTrue(sidecar.exists())
            self.assertNotEqual(sidecar, runner_path)

    def test_lane1a_metadata_only_in_sidecar(self):
        """Lane 1a metadata never injected into runner output."""
        import lane1a_runner_wrapper as wrapper  # noqa: PLC0415
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td)
            runner_path = self._stage_fake_runner_output(tmp, "L02", "answerable_mirror")
            sidecar_path = wrapper.write_sidecar(
                runner_output_path=runner_path,
                runner_output_sha256=wrapper._sha256_file(runner_path),
                rung_id="L02",
                stratum="answerable_mirror",
                attempt_id=1,
            )

            runner_payload = json.loads(runner_path.read_text(encoding="utf-8"))
            self.assertNotIn("artifact_class", runner_payload)
            self.assertNotIn("certification_relevance", runner_payload)
            self.assertNotIn("lane_1a_context", runner_payload)
            self.assertNotIn("original_context_from_b1v2", runner_payload)

            sidecar = json.loads(sidecar_path.read_text(encoding="utf-8"))
            self.assertEqual(sidecar["wrapper_attestation"]["artifact_class"],
                             "lane-1a-reconnaissance")
            self.assertEqual(sidecar["wrapper_attestation"]["lane_1a_context"],
                             "lane-1a-reconnaissance")
            self.assertEqual(sidecar["runner_name"], "lane1a_runner.py")
            self.assertTrue(
                sidecar["wrapper_attestation"]
                ["context_is_wrapper_asserted_not_runner_attested"]
            )
            self.assertGreater(
                len(sidecar["wrapper_attestation"]["context_functional_statement"]),
                200,
            )

    def test_sidecar_validates_against_schema(self):
        try:
            import jsonschema
        except ImportError:
            self.skipTest("jsonschema not installed")
        import lane1a_runner_wrapper as wrapper  # noqa: PLC0415
        schema = json.loads(
            (SCRIPT_DIR / "schema" / "lane1a_sidecar.schema.json").read_text()
        )
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td)
            runner_path = self._stage_fake_runner_output(tmp, "L03", "null")
            sidecar_path = wrapper.write_sidecar(
                runner_output_path=runner_path,
                runner_output_sha256=wrapper._sha256_file(runner_path),
                rung_id="L03",
                stratum="null",
                attempt_id=2,
            )
            sidecar = json.loads(sidecar_path.read_text(encoding="utf-8"))
            jsonschema.validate(sidecar, schema)


class TestLane1aRunnerManifestValidation(unittest.TestCase):
    """Path A: lane1a_runner.py validates the Lane 1a manifest schema."""

    def setUp(self):
        import lane1a_runner  # noqa: PLC0415
        self.runner = lane1a_runner

    def _good_manifest(self):
        return {
            "rung_id": "L01",
            "rung_spec": {"D": 4, "K": "low", "X": "base"},
            "per_rung_seed": 123,
            "items": {
                "answerable": [
                    {"item_id": "L01-A-000", "stratum": "answerable",
                     "in_context_pairs": [["a", "alpha"]],
                     "queried_key": "a", "expected_answer": "alpha"}
                ],
                "null": [
                    {"item_id": "L01-N-000", "stratum": "null",
                     "in_context_pairs": [["a", "alpha"]],
                     "queried_key": "z", "expected_answer": "NULL"}
                ],
            },
            "controls": {
                "answerable_mirror": [
                    {"item_id": "L01-AM-000", "stratum": "answerable_mirror",
                     "in_context_pairs": [["a", "alpha"]],
                     "queried_key": "a", "expected_answer": "bravo"}
                ],
                "null_mirror": [
                    {"item_id": "L01-NM-000", "stratum": "null_mirror",
                     "in_context_pairs": [["a", "alpha"]],
                     "queried_key": "z", "expected_answer": "NULL"}
                ],
            },
            "artifact_class": "lane-1a-reconnaissance",
            "certification_relevance": "none",
        }

    def test_valid_manifest_accepted(self):
        self.runner.validate_lane1a_manifest(self._good_manifest())

    def test_missing_top_level_keys_rejected(self):
        m = self._good_manifest()
        del m["items"]
        with self.assertRaises(self.runner.ManifestValidationError):
            self.runner.validate_lane1a_manifest(m)

    def test_wrong_artifact_class_rejected(self):
        m = self._good_manifest()
        m["artifact_class"] = "paper3-certification"
        with self.assertRaises(self.runner.ManifestValidationError):
            self.runner.validate_lane1a_manifest(m)

    def test_wrong_certification_relevance_rejected(self):
        m = self._good_manifest()
        m["certification_relevance"] = "high"
        with self.assertRaises(self.runner.ManifestValidationError):
            self.runner.validate_lane1a_manifest(m)

    def test_invalid_stratum_rejected(self):
        m = self._good_manifest()
        m["items"]["answerable"][0]["stratum"] = "not-a-stratum"
        with self.assertRaises(self.runner.ManifestValidationError):
            self.runner.validate_lane1a_manifest(m)

    def test_missing_item_field_rejected(self):
        m = self._good_manifest()
        del m["items"]["answerable"][0]["queried_key"]
        with self.assertRaises(self.runner.ManifestValidationError):
            self.runner.validate_lane1a_manifest(m)

    def test_actual_generated_manifests_validate(self):
        """All 8 generated Lane 1a manifests pass lane1a_runner validation."""
        for rid in ["L01","L02","L03","L04","L05","L06","L07","L08"]:
            p = SCRIPT_DIR / "manifests" / f"{rid}.json"
            if not p.exists():
                self.skipTest(f"manifest {rid} not generated yet")
            m = json.loads(p.read_text(encoding="utf-8"))
            self.runner.validate_lane1a_manifest(m)


class TestLane1aRunnerProvenance(unittest.TestCase):
    """Path A: lane1a_runner.py uses B1 v2-compatible model attestation
    convention without importing B1 v2 source."""

    def test_no_b1v2_imports(self):
        # Strict check: lane1a_runner.py must not reference B1 v2 modules.
        src = (SCRIPT_DIR / "lane1a_runner.py").read_text(encoding="utf-8")
        self.assertNotIn("import runner_b1_v2", src)
        self.assertNotIn("from runner_b1_v2", src)
        self.assertNotIn("from experiments.2026-06-09_b1-harness-v2", src)
        self.assertNotIn("b1_harness", src)

    def test_compute_model_snapshot_hash_signature(self):
        import lane1a_runner  # noqa: PLC0415
        # B1 v2 compatibility: same algorithm signature.
        self.assertTrue(hasattr(lane1a_runner, "compute_model_snapshot_hash"))
        # Verify on a tiny synthetic directory.
        with tempfile.TemporaryDirectory() as td:
            (Path(td) / "config.json").write_text("{}")
            (Path(td) / "weights.bin").write_text("x")
            h = lane1a_runner.compute_model_snapshot_hash(Path(td))
            self.assertTrue(h.startswith("sha256:"))
            self.assertEqual(len(h), len("sha256:") + 64)

    def test_decoding_settings_locked(self):
        import lane1a_runner  # noqa: PLC0415
        self.assertEqual(lane1a_runner.DECODING_SETTINGS["temperature"], 0.0)
        self.assertEqual(lane1a_runner.DECODING_SETTINGS["greedy"], True)
        self.assertEqual(lane1a_runner.DECODING_SETTINGS["seed"], 0)

    def test_model_id_matches_b1v2(self):
        """Path A.1 (Manager 2026-06-10): lane1a_runner.MODEL_ID must
        match B1 v2's MODEL_ID byte-for-byte. Cross-references the
        B1 v2 source directly so future drift trips CI."""
        import lane1a_runner  # noqa: PLC0415
        # SCRIPT_DIR = experiments/2026-06-10_lane-1a-sweep/
        # parents[0] = experiments/
        b1v2_src_path = (
            SCRIPT_DIR.parents[0]
            / "2026-06-09_b1-harness-v2" / "code" / "runner_b1_v2.py"
        )
        self.assertTrue(b1v2_src_path.exists(),
                        f"B1 v2 source not found at {b1v2_src_path}")
        b1v2_src = b1v2_src_path.read_text(encoding="utf-8")
        # Find B1 v2's MODEL_ID assignment.
        m = re.search(r'^MODEL_ID\s*=\s*"([^"]+)"', b1v2_src, re.MULTILINE)
        self.assertIsNotNone(m, "could not locate MODEL_ID in B1 v2 source")
        b1v2_model_id = m.group(1)
        self.assertEqual(
            lane1a_runner.MODEL_ID, b1v2_model_id,
            f"lane1a_runner.MODEL_ID ({lane1a_runner.MODEL_ID!r}) must "
            f"match B1 v2 MODEL_ID ({b1v2_model_id!r}) byte-for-byte",
        )


class TestPathE1ProductionSubprocess(unittest.TestCase):
    """Path E.1 (Manager 2026-06-10): production subprocess interpreter
    pin + cross-reference + smoke test. The instrument failure occurred
    because sys.executable resolved to a Python whose mlx_lm did not
    have the expected import surface; these tests prevent recurrence."""

    def test_interpreter_path_matches_config(self):
        import lane1a_runner_wrapper as wrapper  # noqa: PLC0415
        cfg_text = (SCRIPT_DIR / "runner_config.yaml").read_text()
        m = re.search(r'python_interpreter:\s*"([^"]+)"', cfg_text)
        self.assertIsNotNone(m, "could not locate python_interpreter in runner_config.yaml")
        cfg_path = m.group(1)
        self.assertEqual(
            wrapper.PRODUCTION_PYTHON, cfg_path,
            f"wrapper PRODUCTION_PYTHON ({wrapper.PRODUCTION_PYTHON!r}) must "
            f"match runner_config.yaml production.python_interpreter ({cfg_path!r})",
        )

    def test_expected_mlx_lm_version_matches_config(self):
        import lane1a_runner_wrapper as wrapper  # noqa: PLC0415
        cfg_text = (SCRIPT_DIR / "runner_config.yaml").read_text()
        m = re.search(r'expected_mlx_lm_version:\s*"([^"]+)"', cfg_text)
        self.assertIsNotNone(m, "could not locate expected_mlx_lm_version")
        cfg_version = m.group(1)
        self.assertEqual(wrapper.EXPECTED_MLX_LM_VERSION, cfg_version)

    def test_production_subprocess_smoke(self):
        """Spawn the production subprocess; verify the runner's import
        surface succeeds; verify mlx_lm version. This is the test that
        would have caught the prior instrument failure."""
        import lane1a_runner_wrapper as wrapper  # noqa: PLC0415
        result = wrapper.production_subprocess_smoke_test()
        self.assertTrue(result["import_ok"])
        self.assertEqual(result["mlx_lm_version"], wrapper.EXPECTED_MLX_LM_VERSION)
        self.assertEqual(result["interpreter"], wrapper.PRODUCTION_PYTHON)

    def test_wrapper_does_not_use_sys_executable_for_subprocess(self):
        """Subprocess argv[0] must be PRODUCTION_PYTHON, not sys.executable."""
        wrapper_src = (SCRIPT_DIR / "lane1a_runner_wrapper.py").read_text()
        m = re.search(r'cmd\s*=\s*\[\s*([A-Za-z_\.]+),', wrapper_src)
        self.assertIsNotNone(m, "could not locate cmd = [...] in wrapper")
        argv0 = m.group(1)
        self.assertEqual(argv0, "PRODUCTION_PYTHON",
                         f"wrapper subprocess argv[0] should be PRODUCTION_PYTHON, got {argv0!r}")


if __name__ == "__main__":
    unittest.main()
