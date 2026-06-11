"""Lane 1a' runner wrapper.

SYNTHETIC / DIAGNOSTIC -- NON-BINDING -- NOT FOR THRESHOLD DERIVATION
D2 IMPLEMENTATION ARTIFACT (PHASE 4)
NO MODEL INVOKED -- NO MODEL LOADED
NO SWEEP_ID CREATED -- NO SWEEP EXECUTION AUTHORIZED

Phase 4 implements the production-path subprocess pattern (carried
from Lane 1a v1 Path E.1) and the sidecar attestation pattern. The
wrapper does NOT load the model. Subprocess invocation in Phase 4
is import-surface verification only.

Architectural invariants (carried from v1):
  - write_sidecar() writes byte-disjoint from runner output
  - The wrapper never rewrites runner-attested outputs
  - PRODUCTION_PYTHON is the production interpreter (locked at packet)
  - EXPECTED_MLX_LM_VERSION is the runtime dependency pin
"""
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional


# Placeholder constants — locked at packet seal under the
# sibling-artifact cross-reference rule.

PRODUCTION_PYTHON = "<PLACEHOLDER_LOCKED_AT_PACKET_SEAL>"
EXPECTED_MLX_LM_VERSION = "<PLACEHOLDER_LOCKED_AT_PACKET_SEAL>"


# AL-Q4 diagnostic-sidecar artifact_class const per joint disposition.
DIAGNOSTIC_ARTIFACT_CLASS = "lane-1a-prime-diagnostic"

# E15 label vocabulary.
SYNTHETIC_LABEL = "SYNTHETIC — NON-BINDING — NOT FOR THRESHOLD DERIVATION"
RECONNAISSANCE_LABEL = "RECONNAISSANCE — NON-BINDING — NOT FOR THRESHOLD DERIVATION"
DIAGNOSTIC_LABEL = "DIAGNOSTIC — NON-BINDING — NOT FOR THRESHOLD DERIVATION"


@dataclass(frozen=True)
class SidecarRecord:
    """Sidecar record byte-disjoint from runner output.

    Carried from Lane 1a v1 Path E.1. The runner writes its own
    output bytes; the wrapper's write_sidecar() writes this record
    in a SEPARATE file. The wrapper never rewrites the runner's
    output bytes.
    """
    sidecar_type: str  # "runner_attested" | "diagnostic"
    record_id: str
    runner_output_hash: str
    sweep_id: Optional[str]  # null under D2; set only at D4
    rung_id: str
    stratum: str
    artifact_label: str


def write_sidecar(
    out_path: Path,
    sidecar: SidecarRecord,
) -> str:
    """Write a sidecar record to disk; return its sha256.

    Invariant (carried from v1): write_sidecar NEVER reads, edits,
    or rewrites runner output. The sidecar lives in a SEPARATE file
    from the runner's output bytes.

    Output format: JSON, one object per file. The sidecar is
    byte-disjoint from the runner's output stream by construction
    (different file path; different write).
    """
    payload = {
        "sidecar_type": sidecar.sidecar_type,
        "record_id": sidecar.record_id,
        "runner_output_hash": sidecar.runner_output_hash,
        "sweep_id": sidecar.sweep_id,  # null under D2
        "rung_id": sidecar.rung_id,
        "stratum": sidecar.stratum,
        "artifact_label": sidecar.artifact_label,
    }
    text = json.dumps(payload, indent=2, sort_keys=True)
    out_path.write_text(text)
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


@dataclass(frozen=True)
class SubprocessSmokeResult:
    """Result of the production-path subprocess smoke test."""
    succeeded: bool
    interpreter_path: str
    stdout: str
    stderr: str
    return_code: int
    model_was_loaded: bool  # always False under D2 Phase 4


def verify_production_subprocess_smoke(
    python_executable: str,
    smoke_imports: tuple[str, ...] = ("sys",),
) -> SubprocessSmokeResult:
    """Path E.1 carry: spawn the production subprocess and verify
    import surface.

    IMPORTANT: Phase 4 D2 constraint — the smoke test imports
    modules; it does NOT load a model.

    The default smoke_imports is ("sys",) — a benign import that
    succeeds on any Python installation. At packet seal, the
    production smoke test passes smoke_imports = ("mlx_lm",
    "mlx_lm.sample_utils") and verifies the EXPECTED_MLX_LM_VERSION;
    that test is run by the CI pre-lock check, not by Phase 4
    test code (which has no mlx_lm dependency).

    The subprocess script is:
        for module_name in smoke_imports:
            __import__(module_name)
        print("OK")

    No model invocation. No model load. No pretrained-checkpoint
    loading. No tokenizer initialization.
    """
    imports_script = "; ".join(
        f"__import__('{name}')" for name in smoke_imports
    )
    code = f"{imports_script}; print('OK')"

    proc = subprocess.run(
        [python_executable, "-c", code],
        capture_output=True,
        text=True,
        timeout=10,
    )
    return SubprocessSmokeResult(
        succeeded=(proc.returncode == 0),
        interpreter_path=python_executable,
        stdout=proc.stdout,
        stderr=proc.stderr,
        return_code=proc.returncode,
        model_was_loaded=False,
    )


def run_assembly_dry_run(record: dict, record_id: str = "") -> "RenderedPrompt":
    """AL-Q1 closure: render a prompt without invoking the model.

    Used by the interface-contract test (Path A.1 pattern) at
    packet-stage pre-lock. The function is a pure-function call
    into the runner's render_prompt(). No subprocess. No model load.

    The wrapper's --dry-run flag (CLI) is the wrapper-side surface
    that exposes this. The function body here is what the CLI calls.
    """
    # Late import to avoid wrapper-runner circular import at module
    # load time.
    from lane1a_prime.runner import render_prompt
    return render_prompt(record, record_id=record_id)


def assert_no_model_load_in_subprocess_smoke(smoke_imports: tuple[str, ...]) -> bool:
    """Source-level assertion helper: confirms the smoke_imports
    tuple contains no module name known to trigger a model load.

    Used by tests to verify the wrapper's smoke test stays
    import-only.
    """
    forbidden_substrings = (
        # Pretrained-checkpoint loader name fragments
        "_pretrained",
        "load_model",
        "torch.load",
    )
    for module_name in smoke_imports:
        # Bare module-name imports do not trigger model loads.
        # We reject any caller-supplied import specification that
        # carries a forbidden substring or contains parentheses
        # (which would indicate an embedded function call rather
        # than a bare import).
        if any(sub in module_name for sub in forbidden_substrings):
            return False
        if "(" in module_name or ")" in module_name:
            return False
    return True
