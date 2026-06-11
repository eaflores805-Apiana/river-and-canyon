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


if __name__ == "__main__":
    unittest.main()
