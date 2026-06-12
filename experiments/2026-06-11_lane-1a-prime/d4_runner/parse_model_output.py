"""Lane 1a' Prime D4-A model output parser.

Maps model response strings → SimulatedPrediction-shaped predictions.

Value pool: VALUE_POOL = range(26); mapped to letters 'a'..'z'.
Abstention marker: exact word 'NONE' (case-insensitive recognized).
"""
from __future__ import annotations

import re
import string
from typing import Optional


# Inverse mapping: letter -> value-pool token id
LETTER_TO_VALUE_ID = {ch: i for i, ch in enumerate(string.ascii_lowercase)}


def parse_model_output(text: str) -> dict:
    """Parse a model response string into the prediction shape.

    Returns a dict with:
      - predicted_value_token_ids: tuple[int, ...] | None
        (None = abstained per the contract)
      - parse_status: 'parsed_value' | 'parsed_abstention' | 'parse_failure'
      - raw_text: the original response (truncated)
      - extracted_token: the letter or 'NONE' or '' extracted
    """
    raw = text or ""
    # Strip whitespace, leading/trailing markers
    cleaned = raw.strip()

    # Truncate at first newline (the assistant's first line is the answer)
    if "\n" in cleaned:
        cleaned = cleaned.split("\n", 1)[0].strip()

    # Strip surrounding punctuation that some models may add
    cleaned = cleaned.strip(string.punctuation + string.whitespace)

    # Empty response -> abstention by default (model produced no content)
    if not cleaned:
        return {
            "predicted_value_token_ids": None,
            "parse_status": "parse_failure",
            "raw_text": raw[:200],
            "extracted_token": "",
        }

    # Check for the abstention marker
    if cleaned.upper() == "NONE":
        return {
            "predicted_value_token_ids": None,
            "parse_status": "parsed_abstention",
            "raw_text": raw[:200],
            "extracted_token": "NONE",
        }

    # Check for a single lowercase letter (the canonical answer form)
    if len(cleaned) == 1 and cleaned in LETTER_TO_VALUE_ID:
        return {
            "predicted_value_token_ids": (LETTER_TO_VALUE_ID[cleaned],),
            "parse_status": "parsed_value",
            "raw_text": raw[:200],
            "extracted_token": cleaned,
        }

    # Permissive: extract the first single-letter token
    # (handles "The value is q." or "q\nNote: ..." patterns)
    m = re.match(r"^\s*([a-z])\b", cleaned.lower())
    if m:
        letter = m.group(1)
        return {
            "predicted_value_token_ids": (LETTER_TO_VALUE_ID[letter],),
            "parse_status": "parsed_value",
            "raw_text": raw[:200],
            "extracted_token": letter,
        }

    # Permissive abstention: any text containing "NONE" as a standalone token
    if re.search(r"\bNONE\b", cleaned, re.IGNORECASE):
        return {
            "predicted_value_token_ids": None,
            "parse_status": "parsed_abstention",
            "raw_text": raw[:200],
            "extracted_token": "NONE",
        }

    # Parse failure: model produced text that doesn't match the contract.
    # Per D4-A INCONCLUSIVE handling, this is a per-record void.
    return {
        "predicted_value_token_ids": None,
        "parse_status": "parse_failure",
        "raw_text": raw[:200],
        "extracted_token": cleaned[:32],
    }


def render_pair_lines(pairs: list[dict]) -> str:
    """Render the pair list portion of the prompt."""
    lines = []
    for p in pairs:
        key_ids = p["key_token_ids"]
        value_ids = p["value_token_ids"]
        # Multi-token keys space-separated; single-token values mapped to letters
        key_str = " ".join(str(k) for k in key_ids)
        if len(value_ids) == 1 and 0 <= value_ids[0] <= 25:
            value_str = string.ascii_lowercase[value_ids[0]]
        else:
            # Defensive: shouldn't happen on Lane 1a' manifests
            value_str = " ".join(str(v) for v in value_ids)
        lines.append(f"{key_str} -> {value_str}")
    return "\n".join(lines)


def render_query_key(queried_key: dict) -> str:
    """Render the query key portion of the prompt."""
    key_ids = queried_key["key_token_ids"]
    return " ".join(str(k) for k in key_ids)
