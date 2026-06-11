"""Lane 1a runner wrapper — Case B, SIDECAR-ATTESTATION PATTERN (locked).

REMEDIATION 2026-06-10: This wrapper PRESERVES B1 v2 output bytes
unchanged. Lane 1a metadata lives in a sidecar JSON companion file
with its own schema. The wrapper does NOT mutate the runner-attested
output; doing so would create a wrapper-asserted (not runner-attested)
artifact, which is the rejected pattern.

B1 v2 does not expose Lane 1a as a native mode/context, and B1 v2 must
not be edited (B1 v2 locked at merge 3cbfce57; B1 v2.1 unauthorized).
The wrapper:

  1. Reads LOCK-RECORD.md before any invocation. Refuses to proceed
     if the token-prior authorization line is missing or malformed,
     OR if the lock_timestamp is not finalized.
  2. Verifies lock_timestamp < first_data_access_timestamp.
  3. Invokes B1 v2 runner via subprocess with only the locked flags
     B1 v2's argparse accepts:
        --mode live --context paper2-reproduction
        --framework-version none --manifest <path>
  4. Locates the B1 output file produced by the subprocess.
  5. Computes sha256 of the B1 output file (does NOT open + rewrite).
  6. Writes a SIDECAR JSON next to the B1 output file with Lane 1a
     metadata (artifact_class, certification_relevance, the wrapper-
     asserted Lane 1a context, the --context functional statement,
     the B1 output path, and the B1 output sha256).
  7. Enforces the no-re-execution rule by checking the audit log
     for prior runner_started events at the same (rung_id, stratum).
  8. Emits runner_started / runner_completed / runner_anomaly events.

The B1 output file is bit-identical to what B1 v2 produced. Any
auditor can re-hash and verify against the sidecar's recorded
`b1_output_sha256`.
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

CONTEXT_FUNCTIONAL_STATEMENT = (
    "B1 v2 `--context paper2-reproduction` is passed because B1 v2's "
    "locked argparse surface (merge 3cbfce57) does not include "
    "'lane-1a-reconnaissance' as a --context value, and B1 v2 must "
    "not be edited. The `--context` flag selects B1 v2's post-generation "
    "code path; the paper2-reproduction path is used by Lane 1a because "
    "it engages no certification-gate logic and accepts "
    "`framework_version=\"none\"`. Lane 1a semantics are NOT carried by "
    "the B1 `context` field — they are wrapper-asserted via the sidecar "
    "JSON written alongside each B1 output. The B1 output bytes are "
    "preserved unchanged; the sidecar records the B1 output's sha256 "
    "so an auditor can verify byte-for-byte preservation."
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
    b1_output_path: Path,
    b1_output_sha256: str,
    rung_id: str,
    stratum: str,
    attempt_id: int,
) -> Path:
    """Write the Lane 1a sidecar JSON next to the B1 output file.

    The sidecar is the ONLY place Lane 1a metadata is recorded. The B1
    output file itself is not modified.
    """
    sidecar = {
        "schema": "lane-1a-sidecar.schema.json",
        "b1_output_path": str(b1_output_path),
        "b1_output_sha256": b1_output_sha256,
        "b1_context_argument_passed": "paper2-reproduction",
        "b1_framework_version_argument_passed": "none",
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
    sidecar_path = b1_output_path.with_suffix(".lane1a.sidecar.json")
    sidecar_path.write_text(
        json.dumps(sidecar, sort_keys=True, indent=2),
        encoding="utf-8",
    )
    return sidecar_path


def invoke_b1v2(
    rung_id: str,
    stratum: str,
    manifest_path: Path,
    output_dir: Path,
    audit: AuditLogWriter,
    attempt_id: int,
) -> dict[str, Any]:
    """Invoke B1 v2 once for one (rung_id, stratum).

    Returns:
        dict with keys:
          - b1_output_path: the bit-identical B1 v2 output file
          - b1_output_sha256: sha256 of the B1 output (recorded but not mutated)
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
            "b1v2_invocation_args": [
                "--mode", "live",
                "--context", "paper2-reproduction",
                "--framework-version", "none",
                "--manifest", str(manifest_path),
            ],
            "lane_1a_context_attestation": "sidecar",
            "b1_output_will_be_preserved_byte_for_byte": True,
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
            details={"anomaly_kind": "subprocess_failure", "stderr_tail": (e.stderr or "")[-512:]},
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

    b1_output_path = result_files[-1]

    # Compute sha256 of the B1 output WITHOUT opening + rewriting.
    b1_output_sha256 = _sha256_file(b1_output_path)

    # Write the sidecar; do NOT modify b1_output_path.
    sidecar_path = write_sidecar(
        b1_output_path=b1_output_path,
        b1_output_sha256=b1_output_sha256,
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
            "b1_output_path": str(b1_output_path),
            "b1_output_sha256": b1_output_sha256,
            "sidecar_path": str(sidecar_path),
            "b1_output_preserved_unmutated": True,
        },
    )

    return {
        "b1_output_path": b1_output_path,
        "b1_output_sha256": b1_output_sha256,
        "sidecar_path": sidecar_path,
    }


def preflight() -> str:
    """Read LOCK-RECORD; validate token-prior auth + first-data-access
    ordering. Returns 'option_a' or 'option_b'."""
    fields = _read_lock_record()
    path = _validate_lock_record(fields)
    _validate_first_data_access_ordering(fields)
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
