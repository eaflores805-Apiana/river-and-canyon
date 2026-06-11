"""Lane 1a artifact-tagging logic (locked; hash-recorded in LOCK-RECORD.md).

Doctrine: Lane 1a may rule out; Lane 1a may not rule in.

Every Lane 1a write point (analyzer records, sweep record, figures,
audit log entries) passes through this module to ensure the artifact
class and certification-relevance tag pair is present.
"""

from __future__ import annotations

from typing import Any

# Locked constants. Do not edit after LOCK-RECORD seal.
ARTIFACT_CLASS = "lane-1a-reconnaissance"
CERTIFICATION_RELEVANCE = "none"


def tag(payload: dict[str, Any]) -> dict[str, Any]:
    """Inject artifact_class and certification_relevance into a payload.

    Returns a NEW dict (does not mutate input). If the keys already
    exist with non-canonical values, raises ValueError — callers must
    not override the tags.
    """
    if "artifact_class" in payload and payload["artifact_class"] != ARTIFACT_CLASS:
        raise ValueError(
            f"artifact_class override rejected: {payload['artifact_class']!r} "
            f"(must be {ARTIFACT_CLASS!r})"
        )
    if (
        "certification_relevance" in payload
        and payload["certification_relevance"] != CERTIFICATION_RELEVANCE
    ):
        raise ValueError(
            f"certification_relevance override rejected: "
            f"{payload['certification_relevance']!r} "
            f"(must be {CERTIFICATION_RELEVANCE!r})"
        )
    out = dict(payload)
    out["artifact_class"] = ARTIFACT_CLASS
    out["certification_relevance"] = CERTIFICATION_RELEVANCE
    return out


def get_tag_footer() -> str:
    """Plot figure footer (mandatory on every figure)."""
    return (
        f"artifact_class: {ARTIFACT_CLASS} | "
        f"certification_relevance: {CERTIFICATION_RELEVANCE}"
    )
