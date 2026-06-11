"""Lane 1a' Phase 4 runner tests.

SYNTHETIC / DIAGNOSTIC -- NON-BINDING -- NOT FOR THRESHOLD DERIVATION
D2 IMPLEMENTATION ARTIFACT
NO MODEL INVOKED -- NO MODEL LOADED -- NO SWEEP EXECUTION

Validates:
  - render_prompt() is pure (no subprocess; no model invocation;
    deterministic; no I/O)
  - RenderedPrompt + ConformanceResult dataclasses
  - invoke_model() stub blocks under D2 (NotImplementedError)
  - MODEL_ID is placeholder under D2 (sibling-artifact rule)
  - Source-level: runner.py does not import subprocess/mlx_lm
"""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from lane1a_prime.runner import (  # noqa: E402
    MODEL_ID,
    ConformanceResult,
    RenderedPrompt,
    invoke_model,
    render_prompt,
)

RUNNER_SOURCE = (Path(__file__).resolve().parent.parent / "lane1a_prime" / "runner.py").read_text()


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


# ---------- render_prompt purity ----------

def test_render_prompt_returns_rendered_prompt():
    result = render_prompt(VALID_RECORD, record_id="r-001")
    assert isinstance(result, RenderedPrompt)


def test_render_prompt_is_deterministic():
    """Same inputs -> identical RenderedPrompt. Pure function
    invariant."""
    r1 = render_prompt(VALID_RECORD, record_id="r-001")
    r2 = render_prompt(VALID_RECORD, record_id="r-001")
    assert r1 == r2


def test_render_prompt_no_subprocess_in_source():
    """AL-Q1 closure: render_prompt body must not invoke a
    subprocess. The runner module imports nothing from subprocess."""
    # Source-level grep
    assert "import subprocess" not in RUNNER_SOURCE
    assert "from subprocess" not in RUNNER_SOURCE


def test_render_prompt_no_model_import_in_source():
    """No mlx_lm or other model-loading library import in runner."""
    forbidden_imports = [
        "import mlx_lm",
        "from mlx_lm",
        "import torch",
        "from torch",
        "from_pretrained",
        "load_model",
    ]
    for forbidden in forbidden_imports:
        assert forbidden not in RUNNER_SOURCE, (
            f"Forbidden model-loading reference in runner.py: {forbidden}"
        )


def test_render_prompt_returns_conformance_result():
    result = render_prompt(VALID_RECORD, record_id="r-001")
    assert isinstance(result.conformance_check, ConformanceResult)
    assert result.conformance_check.is_conformant is True


def test_render_prompt_template_id_hash_is_sha256():
    """The template_id_hash is the sha256 of the template text;
    binds to LOCK-RECORD via control_prompt_shell_hash at packet seal."""
    result = render_prompt(VALID_RECORD, record_id="r-001")
    assert len(result.template_id_hash) == 64
    # All hex chars
    int(result.template_id_hash, 16)


def test_render_prompt_record_id_passthrough():
    result = render_prompt(VALID_RECORD, record_id="my-record-id")
    assert result.record_id == "my-record-id"


# ---------- invoke_model stub ----------

def test_invoke_model_raises_under_d2():
    """invoke_model is a stub raising NotImplementedError under D2.
    Model invocation requires Manager D4 by-name authorization."""
    prompt = render_prompt(VALID_RECORD, record_id="r-001")
    with pytest.raises(NotImplementedError, match="D4"):
        invoke_model(prompt)


# ---------- sibling-artifact: MODEL_ID is placeholder under D2 ----------

def test_model_id_is_placeholder_under_d2():
    """MODEL_ID is a placeholder under D2; locked at packet seal
    via sibling-artifact rule. The placeholder string is recognizable."""
    assert "PLACEHOLDER" in MODEL_ID


def test_no_sweep_id_assignment_in_runner_source():
    """Phase 4 boundary: no sweep_id is created in runner.py.
    Source-level grep verifies no assignment to sweep_id."""
    # Strip docstrings/comments; check no actual variable assignment
    # to sweep_id. We allow documentation references.
    import re
    # Pattern: word "sweep_id" followed by " = " (assignment)
    # Excluding type annotations like `sweep_id: ...`
    assignment_pattern = re.compile(
        r"\bsweep_id\s*=\s*['\"]?[A-Za-z0-9_-]",
        re.MULTILINE,
    )
    matches = assignment_pattern.findall(RUNNER_SOURCE)
    assert matches == [], (
        f"sweep_id assignment found in runner.py: {matches}"
    )


# ---------- conformance check ----------

def test_conformance_check_flags_empty_text():
    """Conformance check surfaces issues like empty rendered text
    (which would only happen with a malformed template)."""
    # Pass an empty template
    result = render_prompt(VALID_RECORD, template_text="", record_id="r")
    assert result.conformance_check.is_conformant is False
    assert any("empty" in issue for issue in result.conformance_check.issues)


def test_conformance_check_flags_missing_identity():
    """Records missing both record_id and queried_key are flagged."""
    bad_record = {"context_block": {}}
    result = render_prompt(bad_record, record_id="r")
    assert result.conformance_check.is_conformant is False
