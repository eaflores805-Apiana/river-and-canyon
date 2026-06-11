"""Lane 1a runner wrapper — Case B (locked; hash-recorded in LOCK-RECORD.md).

B1 v2 does not expose Lane 1a as a native mode/context, and B1 v2 must
not be edited (B1 v2 locked at merge 3cbfce57; B1 v2.1 unauthorized).
This wrapper:

  1. Reads LOCK-RECORD.md before any invocation. Refuses to proceed
     if the token-prior authorization line is missing or malformed.
  2. Verifies lock_timestamp < first_data_access_timestamp.
  3. Invokes B1 v2 runner via subprocess with only the locked flags
     B1 v2's argparse accepts. Specifically:
        --mode live --context paper2-reproduction
        --framework-version none --manifest <path>
  4. Rewrites the `context` field in the B1 v2 output to
     "lane-1a-reconnaissance" (honest override; recorded in audit log).
  5. Injects artifact_class and certification_relevance tags.
  6. Enforces the no-re-execution rule by checking the audit log
     for prior runner_started events at the same (rung_id, stratum).
  7. Emits runner_started / runner_completed / runner_anomaly events.

This wrapper is COMPILABLE-ONLY in this commit: first data access
remains NOT AUTHORIZED. Step-3 production produces the wrapper but
does not invoke it.
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from artifact_tags import tag
from audit_log import AuditLogWriter

SCRIPT_DIR = Path(__file__).resolve().parent
LOCK_RECORD_PATH = SCRIPT_DIR / "LOCK-RECORD.md"
AUDIT_LOG_PATH = SCRIPT_DIR / "AUDIT-LOG.ndjson"

EXPECTED_TOKEN_PRIOR_AUTH = (
    "Manager-authorized Lane 1a token-prior control path"
)

# B1 v2 runner CLI location (in-repo, locked at merge 3cbfce57).
B1V2_RUNNER = (
    SCRIPT_DIR.parents[1]
    / "2026-06-09_b1-harness-v2"
    / "code"
    / "runner_b1_v2.py"
)


class LockRecordError(RuntimeError):
    pass


class FirstDataAccessGateError(RuntimeError):
    pass


class ReExecutionRefused(RuntimeError):
    pass


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
    now_ts = datetime.now(timezone.utc).isoformat(timespec="milliseconds")
    if now_ts <= lock_ts:
        raise FirstDataAccessGateError(
            f"first_data_access_timestamp must postdate lock_timestamp; "
            f"now={now_ts} lock={lock_ts}"
        )


def invoke_b1v2(
    rung_id: str,
    stratum: str,
    manifest_path: Path,
    output_dir: Path,
    audit: AuditLogWriter,
    attempt_id: int,
) -> dict[str, Any]:
    """Invoke B1 v2 once for one (rung_id, stratum). Returns the
    wrapper-tagged output record."""
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
            "b1v2_invocation_args": [
                "--mode", "live",
                "--context", "paper2-reproduction",
                "--framework-version", "none",
                "--manifest", str(manifest_path),
            ],
            "wrapper_context_override": "lane-1a-reconnaissance",
        },
    )

    cmd = [
        sys.executable,
        str(B1V2_RUNNER),
        "--mode", "live",
        "--context", "paper2-reproduction",
        "--framework-version", "none",
        "--manifest", str(manifest_path),
        "--output-dir", str(output_dir),
        "--output-prefix", f"LANE1A-{rung_id}-{stratum}",
    ]

    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, check=True)
    except subprocess.CalledProcessError as e:
        audit.emit(
            "runner_anomaly",
            rung_id=rung_id,
            stratum=stratum,
            attempt_id=attempt_id,
            details={"anomaly_kind": "subprocess_failure", "stderr_tail": e.stderr[-512:] if e.stderr else ""},
        )
        raise

    # Locate the result file produced by B1 v2.
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

    raw = json.loads(result_files[-1].read_text(encoding="utf-8"))

    # Apply Case B wrapper overrides.
    overridden = dict(raw)
    overridden["original_context_from_b1v2"] = raw.get("context")
    overridden["context"] = "lane-1a-reconnaissance"
    overridden = tag(overridden)

    audit.emit(
        "runner_completed",
        rung_id=rung_id,
        stratum=stratum,
        attempt_id=attempt_id,
        details={
            "runner_output_path": str(result_files[-1]),
            "context_override_applied": True,
        },
    )

    return overridden


def preflight() -> str:
    """Read LOCK-RECORD; validate token-prior auth + first-data-access
    ordering. Returns 'option_a' or 'option_b'."""
    fields = _read_lock_record()
    path = _validate_lock_record(fields)
    _validate_first_data_access_ordering(fields)
    return path


if __name__ == "__main__":
    # When invoked as a script, run preflight only. Actual sweep
    # execution is gated by Manager confirmation; this script does NOT
    # auto-execute the sweep.
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
