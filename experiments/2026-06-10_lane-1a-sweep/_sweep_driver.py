"""Lane 1a sweep driver — NOT a locked artifact.

This script orchestrates the 32 (rung_id, stratum) invocations of
lane1a_runner.py through the locked wrapper API. It is the execution
tool, not part of the locked packet; the LOCK-RECORD does not include
its hash and its content does not affect the sweep's outputs (the
outputs are determined by the locked artifacts).

The driver uses the wrapper's locked API:
  - preflight() — refuses if LOCK-RECORD timestamp not finalized
  - invoke_runner() — subprocess to lane1a_runner.py + sidecar
  - AuditLogWriter — append-only event log

Each (rung_id, stratum) is a fresh subprocess (the wrapper's design;
the wrapper loads the model fresh each invocation; B1 v2 unedited;
B1 v2.1 not used).
"""

from __future__ import annotations
import json
import sys
import time
import traceback
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from audit_log import AuditLogWriter
from lane1a_runner_wrapper import preflight, invoke_runner

RUNG_IDS = ["L01","L02","L03","L04","L05","L06","L07","L08"]
STRATA = ["answerable","null","answerable_mirror","null_mirror"]

AUDIT_LOG_PATH = SCRIPT_DIR / "AUDIT-LOG.ndjson"
MANIFESTS_DIR = SCRIPT_DIR / "manifests"
RAW_DIR = SCRIPT_DIR / "raw"
RAW_DIR.mkdir(exist_ok=True)

def main():
    audit = AuditLogWriter(AUDIT_LOG_PATH)
    # Preflight (wrapper-side; raises on failure)
    path = preflight()
    audit.emit(
        "first_data_access",
        details={
            "preflight_token_prior_path": path,
            "driver": "_sweep_driver.py",
            "rung_ids": RUNG_IDS,
            "strata": STRATA,
            "planned_attempts": len(RUNG_IDS) * len(STRATA),
        },
    )

    attempt_id = 0
    completed = 0
    anomalies = []
    started_ts = time.time()

    for rung_id in RUNG_IDS:
        manifest_path = MANIFESTS_DIR / f"{rung_id}.json"
        for stratum in STRATA:
            attempt_id += 1
            t0 = time.time()
            try:
                rec = invoke_runner(
                    rung_id=rung_id,
                    stratum=stratum,
                    manifest_path=manifest_path,
                    output_dir=RAW_DIR,
                    audit=audit,
                    attempt_id=attempt_id,
                )
                completed += 1
                dt = time.time() - t0
                print(f"[{attempt_id:02d}/{len(RUNG_IDS)*len(STRATA)}] "
                      f"{rung_id}/{stratum}: OK ({dt:.1f}s) -> {rec['sidecar_path'].name}",
                      flush=True)
            except Exception as e:
                tb = traceback.format_exc()
                anomalies.append({"rung_id": rung_id, "stratum": stratum,
                                  "attempt_id": attempt_id, "err": str(e)})
                print(f"[{attempt_id:02d}] {rung_id}/{stratum}: ANOMALY: {e}",
                      file=sys.stderr, flush=True)
                # Continue; the wrapper will emit runner_anomaly; the rung will
                # be labeled inconclusive_not_actionable at analysis time.

    elapsed = time.time() - started_ts
    audit.emit(
        "sweep_complete",
        details={
            "planned_attempts": len(RUNG_IDS) * len(STRATA),
            "started_attempts": attempt_id,
            "completed_attempts": completed,
            "anomalies": anomalies,
            "wall_clock_seconds": elapsed,
        },
    )
    print(f"\nSweep complete: {completed}/{attempt_id} attempts succeeded "
          f"in {elapsed/60:.1f} min")
    return 0 if completed == len(RUNG_IDS) * len(STRATA) else 1

if __name__ == "__main__":
    sys.exit(main())
