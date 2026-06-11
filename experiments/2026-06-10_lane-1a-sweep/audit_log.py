"""Lane 1a audit-log writer (locked; hash-recorded in LOCK-RECORD.md).

NDJSON; append-only. One event per line. See AUDIT-LOG-FORMAT.md for
event schema and the B5 total_attempts semantics.
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

from artifact_tags import tag

VALID_EVENTS = {
    "lock_record_sealed",
    "manifest_generated",
    "recipe_acceptance_check",
    "novelty_ledger_check",
    "first_data_access",
    "runner_started",
    "runner_completed",
    "runner_anomaly",
    "re_execution_refused",
    "analysis_started",
    "analysis_completed",
    "plot_generated",
    "sweep_complete",
}

VALID_STRATA = {"answerable", "null", "answerable_mirror", "null_mirror", None}


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="milliseconds")


class AuditLogWriter:
    def __init__(self, log_path: Path):
        self.log_path = Path(log_path)
        self.log_path.parent.mkdir(parents=True, exist_ok=True)

    def emit(
        self,
        event: str,
        *,
        rung_id: Optional[str] = None,
        attempt_id: Optional[int] = None,
        stratum: Optional[str] = None,
        details: Optional[dict[str, Any]] = None,
    ) -> None:
        if event not in VALID_EVENTS:
            raise ValueError(f"unknown event: {event!r}")
        if stratum not in VALID_STRATA:
            raise ValueError(f"unknown stratum: {stratum!r}")
        record = {
            "ts": _now_iso(),
            "event": event,
            "rung_id": rung_id,
            "attempt_id": attempt_id,
            "stratum": stratum,
            "details": tag(details or {}),
        }
        line = json.dumps(record, separators=(",", ":"), sort_keys=True)
        with self.log_path.open("a", encoding="utf-8") as f:
            f.write(line + "\n")

    def read_all(self) -> list[dict[str, Any]]:
        if not self.log_path.exists():
            return []
        out: list[dict[str, Any]] = []
        with self.log_path.open("r", encoding="utf-8") as f:
            for ln in f:
                ln = ln.strip()
                if not ln:
                    continue
                out.append(json.loads(ln))
        return out

    def count(self, event: str) -> int:
        return sum(1 for e in self.read_all() if e["event"] == event)

    def has_prior(self, event: str, rung_id: str, stratum: str) -> bool:
        for e in self.read_all():
            if (
                e["event"] == event
                and e.get("rung_id") == rung_id
                and e.get("stratum") == stratum
            ):
                return True
        return False
