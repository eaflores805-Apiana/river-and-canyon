"""Lane 1a' Phase 4 wrapper tests.

SYNTHETIC / DIAGNOSTIC -- NON-BINDING -- NOT FOR THRESHOLD DERIVATION
D2 IMPLEMENTATION ARTIFACT
NO MODEL INVOKED -- NO MODEL LOADED -- NO SWEEP EXECUTION

Validates:
  - run_assembly_dry_run() calls render_prompt() (AL-Q1)
  - PRODUCTION_PYTHON and EXPECTED_MLX_LM_VERSION placeholders
  - verify_production_subprocess_smoke() does NOT load a model
  - write_sidecar() byte-disjoint from runner output; sweep_id null
    under D2
  - assert_no_model_load_in_subprocess_smoke helper
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from lane1a_prime.runner import RenderedPrompt  # noqa: E402
from lane1a_prime.wrapper import (  # noqa: E402
    DIAGNOSTIC_ARTIFACT_CLASS,
    DIAGNOSTIC_LABEL,
    EXPECTED_MLX_LM_VERSION,
    PRODUCTION_PYTHON,
    RECONNAISSANCE_LABEL,
    SYNTHETIC_LABEL,
    SidecarRecord,
    SubprocessSmokeResult,
    assert_no_model_load_in_subprocess_smoke,
    run_assembly_dry_run,
    verify_production_subprocess_smoke,
    write_sidecar,
)

WRAPPER_SOURCE = (Path(__file__).resolve().parent.parent / "lane1a_prime" / "wrapper.py").read_text()


VALID_RECORD = {
    "record_id": "r-001",
    "queried_key": {"key_token_ids": [1]},
    "context_block": {
        "real_pair_block": {
            "start_idx": 0,
            "end_idx": 1,
            "pairs": [{"key_token_ids": [1], "value_token_ids": [10]}],
        },
        "padding_prefix": [],
    },
    "gold": {"value_token_ids": [10]},
    "stratum": "answerable",
    "metadata": {"construction_recipe_hash": "0" * 64, "pilot_or_final": "pilot"},
}


# ---------- run_assembly_dry_run (AL-Q1) ----------

def test_run_assembly_dry_run_returns_rendered_prompt():
    """AL-Q1 closure: run_assembly_dry_run renders a prompt without
    invoking the model."""
    result = run_assembly_dry_run(VALID_RECORD, record_id="r-001")
    assert isinstance(result, RenderedPrompt)


def test_run_assembly_dry_run_no_model_invocation():
    """Dry-run never invokes the model. The wrapper's dry-run path
    calls render_prompt() directly (no subprocess; no model load)."""
    # The result type is RenderedPrompt; if the model had been
    # invoked, the function would have raised NotImplementedError.
    result = run_assembly_dry_run(VALID_RECORD, record_id="r-001")
    # Sanity check: rendered text is present and conformance was checked
    assert result.text != ""
    assert result.conformance_check is not None


# ---------- placeholders ----------

def test_production_python_is_placeholder_under_d2():
    assert "PLACEHOLDER" in PRODUCTION_PYTHON


def test_expected_mlx_lm_version_is_placeholder_under_d2():
    assert "PLACEHOLDER" in EXPECTED_MLX_LM_VERSION


# ---------- subprocess smoke test (Path E.1) ----------

def test_verify_production_subprocess_smoke_succeeds_on_benign_import():
    """The subprocess smoke test runs a benign import (`sys`) and
    succeeds. NO model is loaded."""
    result = verify_production_subprocess_smoke(sys.executable, ("sys",))
    assert result.succeeded is True
    assert result.return_code == 0
    assert result.model_was_loaded is False
    assert "OK" in result.stdout


def test_verify_production_subprocess_smoke_fails_on_nonexistent_module():
    """The subprocess smoke test fails if a required module is
    missing — surfaces dependency-version problems pre-lock."""
    result = verify_production_subprocess_smoke(
        sys.executable,
        ("this_module_does_not_exist_xyz123",),
    )
    assert result.succeeded is False
    assert result.return_code != 0
    assert result.model_was_loaded is False


def test_subprocess_smoke_result_carries_interpreter_path():
    result = verify_production_subprocess_smoke(sys.executable, ("sys",))
    assert result.interpreter_path == sys.executable


def test_subprocess_smoke_never_sets_model_was_loaded_true():
    """Under D2 Phase 4, model_was_loaded is always False. The
    SubprocessSmokeResult dataclass enforces this by default; the
    code path that would set it True does not exist under D2."""
    result = verify_production_subprocess_smoke(sys.executable, ("sys",))
    assert result.model_was_loaded is False


def test_assert_no_model_load_in_subprocess_smoke_accepts_benign():
    assert assert_no_model_load_in_subprocess_smoke(("sys", "math", "json"))


def test_assert_no_model_load_in_subprocess_smoke_rejects_from_pretrained():
    """The helper rejects smoke-import specifications that smuggle
    model-loading calls."""
    assert not assert_no_model_load_in_subprocess_smoke(("torch.load",))
    assert not assert_no_model_load_in_subprocess_smoke(
        ("module.from_pretrained",)
    )
    # Parenthesized calls rejected
    assert not assert_no_model_load_in_subprocess_smoke(
        ("module.load_model()",)
    )


# ---------- write_sidecar (byte-disjoint pattern) ----------

def test_write_sidecar_writes_to_specified_path(tmp_path: Path):
    sidecar = SidecarRecord(
        sidecar_type="runner_attested",
        record_id="r-001",
        runner_output_hash="a" * 64,
        sweep_id=None,
        rung_id="L01",
        stratum="answerable",
        artifact_label=SYNTHETIC_LABEL,
    )
    sidecar_path = tmp_path / "r-001.sidecar.json"
    written_hash = write_sidecar(sidecar_path, sidecar)
    assert sidecar_path.exists()
    assert len(written_hash) == 64


def test_write_sidecar_sweep_id_null_under_d2(tmp_path: Path):
    sidecar = SidecarRecord(
        sidecar_type="runner_attested",
        record_id="r-001",
        runner_output_hash="a" * 64,
        sweep_id=None,  # D2 boundary
        rung_id="L01",
        stratum="answerable",
        artifact_label=SYNTHETIC_LABEL,
    )
    sidecar_path = tmp_path / "r-001.sidecar.json"
    write_sidecar(sidecar_path, sidecar)
    payload = json.loads(sidecar_path.read_text())
    assert payload["sweep_id"] is None


def test_write_sidecar_diagnostic_label_for_diagnostic_sidecar(tmp_path: Path):
    """AL-Q4: diagnostic sidecars carry the DIAGNOSTIC label."""
    sidecar = SidecarRecord(
        sidecar_type="diagnostic",
        record_id="r-002",
        runner_output_hash="b" * 64,
        sweep_id=None,
        rung_id="L02",
        stratum="answerable",
        artifact_label=DIAGNOSTIC_LABEL,
    )
    sidecar_path = tmp_path / "r-002.diagnostic.json"
    write_sidecar(sidecar_path, sidecar)
    payload = json.loads(sidecar_path.read_text())
    assert payload["sidecar_type"] == "diagnostic"
    assert payload["artifact_label"] == DIAGNOSTIC_LABEL


def test_write_sidecar_does_not_modify_runner_output(tmp_path: Path):
    """Architectural invariant: write_sidecar writes a SEPARATE
    file from any hypothetical runner output. Verified by writing
    a stand-in runner output, then writing a sidecar to a different
    path, then asserting the runner output bytes are unchanged."""
    runner_out_path = tmp_path / "r-001.runner_output.txt"
    original_bytes = b"hypothetical runner output\n"
    runner_out_path.write_bytes(original_bytes)
    sidecar = SidecarRecord(
        sidecar_type="runner_attested",
        record_id="r-001",
        runner_output_hash="0" * 64,
        sweep_id=None,
        rung_id="L01",
        stratum="answerable",
        artifact_label=SYNTHETIC_LABEL,
    )
    sidecar_path = tmp_path / "r-001.sidecar.json"
    write_sidecar(sidecar_path, sidecar)
    # Runner output bytes unchanged
    assert runner_out_path.read_bytes() == original_bytes
    # Sidecar at a separate path
    assert sidecar_path.exists()
    assert sidecar_path != runner_out_path


# ---------- E15 label constants ----------

def test_e15_label_constants_match_addendum_vocabulary():
    """The three E15 label constants match the addendum vocabulary
    used elsewhere in the package (sidecar_schema, controls,
    Non-Auth Language)."""
    # Synthetic label
    assert "SYNTHETIC" in SYNTHETIC_LABEL
    assert "NON-BINDING" in SYNTHETIC_LABEL
    assert "NOT FOR THRESHOLD DERIVATION" in SYNTHETIC_LABEL
    # Reconnaissance label
    assert "RECONNAISSANCE" in RECONNAISSANCE_LABEL
    # Diagnostic label
    assert "DIAGNOSTIC" in DIAGNOSTIC_LABEL


def test_diagnostic_artifact_class_constant():
    """AL-Q4 closure: artifact_class for diagnostic sidecars is
    'lane-1a-prime-diagnostic' const."""
    assert DIAGNOSTIC_ARTIFACT_CLASS == "lane-1a-prime-diagnostic"


# ---------- source-level invariants ----------

def test_no_model_loading_imports_in_wrapper_source():
    """Wrapper source contains no model-loading import or call.

    We grep for IMPORT statements (no `import mlx_lm`; no `from mlx_lm`)
    and for CALL patterns (`.from_pretrained(`, `.load_model(`,
    `torch.load(`), NOT for bare substrings. The wrapper's own
    helper function (assert_no_model_load_in_subprocess_smoke) lists
    these substrings as forbidden values inside its body, which would
    trip a naïve substring check.
    """
    forbidden_imports = ["import mlx_lm", "from mlx_lm"]
    for f in forbidden_imports:
        assert f not in WRAPPER_SOURCE, (
            f"Forbidden import {f!r} in wrapper.py"
        )
    forbidden_calls = [
        ".from_pretrained(",
        ".load_model(",
        "torch.load(",
    ]
    for f in forbidden_calls:
        assert f not in WRAPPER_SOURCE, (
            f"Forbidden call pattern {f!r} in wrapper.py"
        )


def test_no_fails_token_in_wrapper_source():
    assert "fails" not in WRAPPER_SOURCE.lower(), (
        "`fails` token found in wrapper.py source"
    )


def test_no_sweep_id_assignment_in_wrapper_source():
    import re
    # Find variable assignments to sweep_id with a non-None value
    pattern = re.compile(
        r"\bsweep_id\s*=\s*['\"]?[A-Za-z0-9_-]",
        re.MULTILINE,
    )
    matches = pattern.findall(WRAPPER_SOURCE)
    assert matches == [], (
        f"sweep_id assignment found in wrapper.py: {matches}"
    )
