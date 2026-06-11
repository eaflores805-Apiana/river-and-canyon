"""Lane 1a runner wrapper — Path A, SIDECAR-ATTESTATION PATTERN (locked).

PATH A REMEDIATION 2026-06-10: B1 v2's --manifest interface requires a
Two-Hop L1-specific schema; Lane 1a manifests are single-hop key->value
nested dicts and do not match that schema. Per Manager direction,
Lane 1a uses a lane-specific runner that preserves B1 v2-compatible
provenance conventions and locked model-loading dependencies, while
leaving B1 v2 source unedited.

The wrapper subprocesses `lane1a_runner.py` (not B1 v2 CLI) and
preserves the runner output bytes byte-for-byte. Lane 1a metadata
lives in a sidecar JSON companion file with its own schema.

B1 v2 source remains unedited; B1 v2.1 is not created. The shared
dependency is `mlx_lm` (the locked model-loading library both B1 v2
and `lane1a_runner.py` use); the runner records the model snapshot
hash in the same format B1 v2 uses.

The wrapper:

  1. Reads LOCK-RECORD.md before any invocation. Refuses to proceed
     if the token-prior authorization line is missing or malformed,
     OR if the lock_timestamp is not finalized.
  2. Verifies lock_timestamp < first_data_access_timestamp.
  3. Invokes `lane1a_runner.py` via subprocess.
  4. Locates the runner output file produced by the subprocess.
  5. Computes sha256 of the runner output file (does NOT open + rewrite).
  6. Writes a SIDECAR JSON next to the runner output file with Lane 1a
     metadata (artifact_class, certification_relevance, the wrapper-
     asserted Lane 1a context, the runner-functional statement,
     the runner output path, and the runner output sha256).
  7. Enforces the no-re-execution rule by checking the audit log
     for prior runner_started events at the same (rung_id, stratum).
  8. Emits runner_started / runner_completed / runner_anomaly events.

The runner output file is bit-identical to what lane1a_runner.py
produced. Any auditor can re-hash and verify against the sidecar's
recorded `runner_output_sha256`.
"""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from artifact_tags import ARTIFACT_CLASS, CERTIFICATION_RELEVANCE
from audit_log import AuditLogWriter

SCRIPT_DIR = Path(__file__).resolve().parent
LOCK_RECORD_PATH = SCRIPT_DIR / "LOCK-RECORD.md"
AUDIT_LOG_PATH = SCRIPT_DIR / "AUDIT-LOG.ndjson"

EXPECTED_TOKEN_PRIOR_AUTH = (
    "Manager-authorized Lane 1a token-prior control path"
)
PENDING_TIMESTAMP_SENTINEL = "PENDING_TEAM_LEAD_REVIEW"

# Path E.1 (Manager 2026-06-10) — Production subprocess interpreter pin.
# The wrapper uses this EXPLICIT path, not sys.executable, because sys.executable
# in the production environment previously resolved to /opt/anaconda3/bin/python
# (mlx_lm 0.19.3, no make_sampler), causing an instrument failure before any
# model load. The explicit path below pins Python 3.13 with mlx_lm 0.31.3.
# Cross-referenced against runner_config.yaml production.python_interpreter by
# unit test test_interpreter_path_matches_config.
PRODUCTION_PYTHON = "/Library/Frameworks/Python.framework/Versions/3.13/bin/python3"
EXPECTED_MLX_LM_VERSION = "0.31.3"

CONTEXT_FUNCTIONAL_STATEMENT = (
    "Lane 1a uses a lane-specific runner (lane1a_runner.py) that "
    "preserves B1 v2-compatible provenance conventions and locked "
    "model-loading dependencies, while leaving B1 v2 source unedited. "
    "B1 v2's `--manifest` interface requires a Two-Hop L1-specific "
    "schema and cannot consume Lane 1a's single-hop key->value "
    "nested-dict manifests; per Manager direction (Path A, 2026-06-10), "
    "the wrapper subprocesses lane1a_runner.py instead. Lane 1a "
    "semantics are wrapper-asserted via the sidecar JSON written "
    "alongside each runner output. The runner output bytes are "
    "preserved unchanged; the sidecar records the runner output's "
    "sha256 so an auditor can verify byte-for-byte preservation. "
    "This is not native B1 v2 execution and is not B1 v2.1."
)

# Lane 1a runner (in-repo, locked alongside the wrapper).
LANE1A_RUNNER = SCRIPT_DIR / "lane1a_runner.py"


class LockRecordError(RuntimeError):
    pass


class FirstDataAccessGateError(RuntimeError):
    pass


class ReExecutionRefused(RuntimeError):
    pass


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="milliseconds")


def _sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def _read_lock_record() -> dict[str, str]:
    if not LOCK_RECORD_PATH.exists():
        raise LockRecordError(
            f"LOCK-RECORD.md not found at {LOCK_RECORD_PATH}; refusing to invoke"
        )
    text = LOCK_RECORD_PATH.read_text(encoding="utf-8")
    fields: dict[str, str] = {}
    for line in text.splitlines():
        m = re.match(r"^([A-Za-z_][A-Za-z0-9_ \-]+):\s+(.*)$", line)
        if m:
            fields[m.group(1).strip()] = m.group(2).strip()
    return fields


def _validate_lock_record(fields: dict[str, str]) -> str:
    auth = fields.get("Token-prior control authorization", "")
    if auth == EXPECTED_TOKEN_PRIOR_AUTH:
        return "option_a"
    if auth == "offline_fallback":
        return "option_b"
    raise LockRecordError(
        f"Token-prior control authorization line missing or unrecognized: {auth!r}"
    )


def _validate_first_data_access_ordering(fields: dict[str, str]) -> None:
    lock_ts = fields.get("Lock timestamp", "")
    if not lock_ts:
        raise FirstDataAccessGateError("Lock timestamp missing from LOCK-RECORD")
    if lock_ts == PENDING_TIMESTAMP_SENTINEL:
        raise FirstDataAccessGateError(
            f"Lock timestamp is {PENDING_TIMESTAMP_SENTINEL}; "
            f"Team Lead must append a finalized RFC 3339 UTC value before invocation"
        )
    now_ts = _now_iso()
    if now_ts <= lock_ts:
        raise FirstDataAccessGateError(
            f"first_data_access_timestamp must postdate lock_timestamp; "
            f"now={now_ts} lock={lock_ts}"
        )


def write_sidecar(
    *,
    runner_output_path: Path,
    runner_output_sha256: str,
    rung_id: str,
    stratum: str,
    attempt_id: int,
    # Back-compat alias for prior unit-test signature; the legacy
    # parameter name b1_output_path is accepted but the canonical name
    # going forward is runner_output_path.
    b1_output_path: Path | None = None,
    b1_output_sha256: str | None = None,
) -> Path:
    """Write the Lane 1a sidecar JSON next to the runner output file.

    The sidecar is the ONLY place Lane 1a metadata is recorded. The
    runner output file itself is not modified.
    """
    if runner_output_path is None and b1_output_path is not None:
        runner_output_path = b1_output_path
    if runner_output_sha256 is None and b1_output_sha256 is not None:
        runner_output_sha256 = b1_output_sha256

    sidecar = {
        "schema": "lane-1a-sidecar.schema.json",
        "runner_output_path": str(runner_output_path),
        "runner_output_sha256": runner_output_sha256,
        "runner_name": "lane1a_runner.py",
        "wrapper_attestation": {
            "artifact_class": ARTIFACT_CLASS,
            "certification_relevance": CERTIFICATION_RELEVANCE,
            "lane_1a_context": "lane-1a-reconnaissance",
            "context_is_wrapper_asserted_not_runner_attested": True,
            "context_functional_statement": CONTEXT_FUNCTIONAL_STATEMENT,
        },
        "rung_id": rung_id,
        "stratum": stratum,
        "attempt_id": attempt_id,
        "wrapper_invocation_ts": _now_iso(),
    }
    sidecar_path = runner_output_path.with_suffix(".lane1a.sidecar.json")
    sidecar_path.write_text(
        json.dumps(sidecar, sort_keys=True, indent=2),
        encoding="utf-8",
    )
    return sidecar_path


def invoke_runner(
    rung_id: str,
    stratum: str,
    manifest_path: Path,
    output_dir: Path,
    audit: AuditLogWriter,
    attempt_id: int,
) -> dict[str, Any]:
    """Invoke lane1a_runner.py once for one (rung_id, stratum).

    Returns:
        dict with keys:
          - runner_output_path: the bit-identical lane1a_runner.py output file
          - runner_output_sha256: sha256 of the runner output (recorded but not mutated)
          - sidecar_path: the Lane 1a sidecar JSON file path
    """
    if audit.has_prior("runner_started", rung_id, stratum):
        audit.emit(
            "re_execution_refused",
            rung_id=rung_id,
            stratum=stratum,
            attempt_id=attempt_id,
            details={"reason": "prior runner_started for (rung_id, stratum) in audit log"},
        )
        raise ReExecutionRefused(
            f"Re-execution refused for rung={rung_id} stratum={stratum}"
        )

    audit.emit(
        "runner_started",
        rung_id=rung_id,
        stratum=stratum,
        attempt_id=attempt_id,
        details={
            "runner_invocation_args": [
                "--manifest", str(manifest_path),
                "--output-dir", str(output_dir),
                "--output-prefix", f"LANE1A-{rung_id}-{stratum}",
                "--stratum", stratum,
                "--rung-id", rung_id,
            ],
            "runner_name": "lane1a_runner.py",
            "lane_1a_context_attestation": "sidecar",
            "runner_output_will_be_preserved_byte_for_byte": True,
            "b1_v2_unedited": True,
            "b1_v2_1_unused": True,
        },
    )

    cmd = [
        PRODUCTION_PYTHON,
        str(LANE1A_RUNNER),
        "--manifest", str(manifest_path),
        "--output-dir", str(output_dir),
        "--output-prefix", f"LANE1A-{rung_id}-{stratum}",
        "--stratum", stratum,
        "--rung-id", rung_id,
    ]

    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, check=True)
    except subprocess.CalledProcessError as e:
        audit.emit(
            "runner_anomaly",
            rung_id=rung_id,
            stratum=stratum,
            attempt_id=attempt_id,
            details={"anomaly_kind": "subprocess_failure", "stderr_tail": (e.stderr or "")[-512:]},
        )
        raise

    # Locate the result file produced by lane1a_runner.py.
    result_files = sorted(
        output_dir.glob(f"LANE1A-{rung_id}-{stratum}*.json")
    )
    if not result_files:
        audit.emit(
            "runner_anomaly",
            rung_id=rung_id,
            stratum=stratum,
            attempt_id=attempt_id,
            details={"anomaly_kind": "no_output_file"},
        )
        raise RuntimeError(f"no result file produced for {rung_id} {stratum}")

    runner_output_path = result_files[-1]

    # Compute sha256 of the runner output WITHOUT opening + rewriting.
    runner_output_sha256 = _sha256_file(runner_output_path)

    # Write the sidecar; do NOT modify runner_output_path.
    sidecar_path = write_sidecar(
        runner_output_path=runner_output_path,
        runner_output_sha256=runner_output_sha256,
        rung_id=rung_id,
        stratum=stratum,
        attempt_id=attempt_id,
    )

    audit.emit(
        "runner_completed",
        rung_id=rung_id,
        stratum=stratum,
        attempt_id=attempt_id,
        details={
            "runner_output_path": str(runner_output_path),
            "runner_output_sha256": runner_output_sha256,
            "sidecar_path": str(sidecar_path),
            "runner_output_preserved_unmutated": True,
        },
    )

    return {
        "runner_output_path": runner_output_path,
        "runner_output_sha256": runner_output_sha256,
        "sidecar_path": sidecar_path,
    }


# Back-compat alias (deprecated name; kept to minimize ripple on prior tests).
invoke_b1v2 = invoke_runner


def production_subprocess_smoke_test() -> dict[str, Any]:
    """Path E.1: spawn the production subprocess and verify its import
    surface succeeds AND its mlx_lm version matches the locked
    expected value.

    This is the test that would have caught the prior instrument
    failure. It runs at preflight time before any model load.

    Returns dict with: interpreter, mlx_lm_version, import_ok.
    Raises RuntimeError on failure.
    """
    if not Path(PRODUCTION_PYTHON).exists():
        raise RuntimeError(
            f"production python interpreter not found: {PRODUCTION_PYTHON}"
        )
    probe = (
        "import sys, mlx_lm; "
        "from mlx_lm.sample_utils import make_sampler; "
        "print(mlx_lm.__version__)"
    )
    proc = subprocess.run(
        [PRODUCTION_PYTHON, "-c", probe],
        capture_output=True, text=True,
    )
    if proc.returncode != 0:
        raise RuntimeError(
            f"production subprocess smoke test FAILED:\n"
            f"  interpreter: {PRODUCTION_PYTHON}\n"
            f"  stderr: {proc.stderr.strip()}"
        )
    observed_version = proc.stdout.strip()
    if observed_version != EXPECTED_MLX_LM_VERSION:
        raise RuntimeError(
            f"production subprocess mlx_lm version mismatch:\n"
            f"  expected: {EXPECTED_MLX_LM_VERSION}\n"
            f"  observed: {observed_version}"
        )
    return {
        "interpreter": PRODUCTION_PYTHON,
        "mlx_lm_version": observed_version,
        "import_ok": True,
    }


def preflight() -> str:
    """Read LOCK-RECORD; validate token-prior auth + first-data-access
    ordering; run production subprocess smoke test (Path E.1).
    Returns 'option_a' or 'option_b'."""
    fields = _read_lock_record()
    path = _validate_lock_record(fields)
    _validate_first_data_access_ordering(fields)
    production_subprocess_smoke_test()
    return path


if __name__ == "__main__":
    audit = AuditLogWriter(AUDIT_LOG_PATH)
    try:
        path = preflight()
        audit.emit(
            "first_data_access",
            details={
                "preflight_path": path,
                "note": "preflight passed; sweep execution requires Manager confirmation outside this script",
            },
        )
    except (LockRecordError, FirstDataAccessGateError) as e:
        print(f"Preflight FAILED: {e}", file=sys.stderr)
        sys.exit(1)
