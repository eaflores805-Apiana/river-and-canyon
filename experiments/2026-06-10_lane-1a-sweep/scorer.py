"""Lane 1a strict + content dual scorer (locked; hash-recorded in LOCK-RECORD.md).

Per Paper 1 dual-scoring discipline:
  strict: model output exactly equals expected_answer (token-strip; case-sensitive)
  content: expected_answer appears as a contiguous substring in model output
            (case-sensitive)
  void: model output is empty or unparseable

For NULL items the expected_answer is the sentinel "NULL".
"""

from __future__ import annotations


NULL_SENTINEL = "NULL"


def _normalize(s: str) -> str:
    """Strip whitespace and surrounding quote marks; preserve case."""
    s = (s or "").strip()
    if s.startswith('"') and s.endswith('"') and len(s) >= 2:
        s = s[1:-1]
    if s.startswith("'") and s.endswith("'") and len(s) >= 2:
        s = s[1:-1]
    return s.strip()


def score_item(
    model_output: str,
    expected_answer: str,
) -> dict:
    """Return a per-item score record.

    Returns:
        dict with keys: strict (bool), content (bool), void (bool),
                        abstained (bool), normalized_output (str)
    """
    out = _normalize(model_output)

    if out == "":
        return {
            "strict": False,
            "content": False,
            "void": True,
            "abstained": False,
            "normalized_output": out,
        }

    abstained = (out == NULL_SENTINEL)
    strict = (out == expected_answer)
    content = (expected_answer in out) if expected_answer else False

    return {
        "strict": strict,
        "content": content,
        "void": False,
        "abstained": abstained,
        "normalized_output": out,
    }
