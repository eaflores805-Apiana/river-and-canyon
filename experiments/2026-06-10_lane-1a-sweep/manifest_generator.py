"""Lane 1a manifest generator (locked; hash-recorded in LOCK-RECORD.md).

Specification: governance/2026-06-10_lane1a/EXECUTION-PACKET-SEC13-MANIFEST-RECIPE-v0.2.md

If this code diverges from the specification, the specification is
authoritative; correct the code and re-lock with a new sha256.

DOCTRINE: Lane 1a may rule out; Lane 1a may not rule in.
ARTIFACT CLASS: lane-1a-reconnaissance
CERTIFICATION RELEVANCE: none

Constants are loaded from classification_criteria.yaml (NOT embedded
here). Edit YAML before lock; never after.
"""

from __future__ import annotations

import hashlib
import json
import string
from pathlib import Path
from typing import Any

import numpy as np

from artifact_tags import tag
from dummy_policies import (
    DECLARED_POLICIES,
    is_nondegenerate,
    policy_predictions,
)


SCRIPT_DIR = Path(__file__).resolve().parent
SWEEP_ID = "lane-1a-2026-06-11"   # Path E.1 (Manager 2026-06-10): new sweep_id after runtime-env instrument failure


def _sha256_str(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def _seed_from_str(s: str) -> int:
    return int.from_bytes(hashlib.sha256(s.encode("utf-8")).digest()[:8], "big")


def manifest_recipe_seed() -> int:
    return _seed_from_str(SWEEP_ID)


def per_rung_seed(rung_id: str) -> int:
    seed_str = f"{manifest_recipe_seed()}:{rung_id}"
    return _seed_from_str(seed_str)


def _rng(seed: int) -> np.random.Generator:
    return np.random.Generator(np.random.PCG64DXSM(seed))


# Locked value pool (NATO phonetic; declared fresh for Lane 1a per NOVELTY-LEDGER).
VALUE_POOL = [
    "alpha", "bravo", "charlie", "delta", "echo", "foxtrot", "golf",
    "hotel", "india", "juliet", "kilo", "lima", "mike", "november",
    "oscar", "papa", "quebec", "romeo", "sierra", "tango", "uniform",
    "victor", "whiskey", "xray", "yankee", "zulu",
]


def _gen_keys_low(rng: np.random.Generator, n: int) -> list[str]:
    """K=low: unique first characters; 5-char suffix per key."""
    alphabet = list(string.ascii_lowercase)
    rng.shuffle(alphabet)
    first_letters = alphabet[:n]
    keys = []
    for fl in first_letters:
        suffix_chars = [
            string.ascii_lowercase[rng.integers(0, 26)] for _ in range(5)
        ]
        keys.append(fl + "".join(suffix_chars))
    return keys


def _gen_keys_high(rng: np.random.Generator, n: int) -> list[str]:
    """K=high: common 3-char prefix; 3-char disambiguating suffix."""
    prefix_chars = [
        string.ascii_lowercase[rng.integers(0, 26)] for _ in range(3)
    ]
    common_prefix = "".join(prefix_chars)
    suffixes: set[str] = set()
    while len(suffixes) < n:
        s = "".join(
            string.ascii_lowercase[rng.integers(0, 26)] for _ in range(3)
        )
        suffixes.add(s)
    return [common_prefix + s for s in sorted(suffixes)]


def _gen_decoy_key(rng: np.random.Generator, in_context_keys: list[str], k_axis: str) -> str:
    """Generate a key that does NOT appear in in_context_keys."""
    in_set = set(in_context_keys)
    for _ in range(10000):
        if k_axis == "low":
            fl = string.ascii_lowercase[rng.integers(0, 26)]
            suffix = "".join(
                string.ascii_lowercase[rng.integers(0, 26)] for _ in range(5)
            )
            candidate = fl + suffix
        else:
            # K=high: reuse the same common prefix as in_context keys
            if in_context_keys:
                common = in_context_keys[0][:3]
            else:
                common = "".join(
                    string.ascii_lowercase[rng.integers(0, 26)] for _ in range(3)
                )
            suffix = "".join(
                string.ascii_lowercase[rng.integers(0, 26)] for _ in range(3)
            )
            candidate = common + suffix
        if candidate not in in_set:
            return candidate
    raise RuntimeError("could not generate decoy key after 10000 tries")


def _pad_for_extended_context(target_tokens: int = 2048) -> str:
    """Deterministic padding to roughly target_tokens of token budget.
    Format-preserving (key: value lines). For Lane 1a, exact token count
    is recorded post-tokenization in audit; padding line count is
    pre-declared as 100 padding pairs (sufficient to comfortably reach
    2048 tokens at Qwen tokenization)."""
    pad_lines = []
    for i in range(100):
        pad_lines.append(f"pad_{i:03d}: pool_{i:03d}")
    return "\n".join(pad_lines)


def _make_item(
    rng: np.random.Generator,
    item_id: str,
    stratum: str,
    D: int,
    k_axis: str,
    answer_pos: int,
    bindings_scrambled: bool = False,
) -> dict[str, Any]:
    """Construct one item (or control). bindings_scrambled=True for
    controls (token-prior baseline)."""
    n_keys = D + 1
    if k_axis == "low":
        keys = _gen_keys_low(rng, n_keys)
    else:
        keys = _gen_keys_high(rng, n_keys)

    if stratum in ("answerable", "answerable_mirror"):
        # Choose an in-context key as the queried key.
        queried_key = keys[answer_pos]
    else:
        # NULL stratum: queried key not in in_context.
        queried_key = _gen_decoy_key(rng, keys, k_axis)

    # Assign values to in-context keys. For non-control items,
    # `answer_pos` gets a specific target_value. For controls,
    # bindings are scrambled so the answer is not retrievable.
    pool = list(VALUE_POOL)
    rng.shuffle(pool)
    in_context_values = [pool[i % len(pool)] for i in range(n_keys)]

    if bindings_scrambled:
        # Re-permute the values so the answer-at-position is replaced.
        rng.shuffle(in_context_values)

    in_context_pairs = list(zip(keys, in_context_values))

    if stratum == "answerable":
        expected_answer = in_context_pairs[answer_pos][1]
    elif stratum == "null":
        expected_answer = "NULL"
    elif stratum == "answerable_mirror":
        # After scrambling, the "correct" answer is whatever value is now
        # at the queried key's position.
        expected_answer = in_context_pairs[answer_pos][1]
    elif stratum == "null_mirror":
        expected_answer = "NULL"
    else:
        raise ValueError(f"unknown stratum: {stratum}")

    return {
        "item_id": item_id,
        "stratum": stratum,
        "in_context_pairs": in_context_pairs,
        "queried_key": queried_key,
        "expected_answer": expected_answer,
        "answer_slot_index": answer_pos,
    }


def generate_rung(rung_id: str, rung_spec: dict[str, Any]) -> dict[str, Any]:
    """Generate one rung's full manifest (answerable + null +
    answerable_mirror + null_mirror)."""
    D = rung_spec["D"]
    k_axis = rung_spec["K"]
    x_axis = rung_spec["X"]
    seed = per_rung_seed(rung_id)
    rng = _rng(seed)

    answerable = []
    for i in range(80):
        ap = int(rng.integers(0, D + 1))
        answerable.append(
            _make_item(rng, f"{rung_id}-A-{i:03d}", "answerable", D, k_axis, ap)
        )

    null_stratum = []
    for i in range(16):
        ap = int(rng.integers(0, D + 1))
        null_stratum.append(
            _make_item(rng, f"{rung_id}-N-{i:03d}", "null", D, k_axis, ap)
        )

    answerable_mirror = []
    for i in range(80):
        ap = int(rng.integers(0, D + 1))
        answerable_mirror.append(
            _make_item(
                rng, f"{rung_id}-AM-{i:03d}", "answerable_mirror",
                D, k_axis, ap, bindings_scrambled=True,
            )
        )

    null_mirror = []
    for i in range(16):
        ap = int(rng.integers(0, D + 1))
        null_mirror.append(
            _make_item(
                rng, f"{rung_id}-NM-{i:03d}", "null_mirror",
                D, k_axis, ap, bindings_scrambled=True,
            )
        )

    extended_padding = ""
    if x_axis == "extended":
        extended_padding = _pad_for_extended_context()

    manifest = {
        "rung_id": rung_id,
        "rung_spec": rung_spec,
        "per_rung_seed": seed,
        "extended_padding": extended_padding,
        "items": {
            "answerable": answerable,
            "null": null_stratum,
        },
        "controls": {
            "answerable_mirror": answerable_mirror,
            "null_mirror": null_mirror,
        },
    }

    return tag(manifest)


def recipe_acceptance_check_rung(manifest: dict[str, Any]) -> dict[str, Any]:
    """Verify every declared dummy policy yields non-degenerate
    predictions on this rung's answerable items. Lock-blocking."""
    items = manifest["items"]["answerable"]
    result = {"rung_id": manifest["rung_id"], "per_policy": {}}
    all_pass = True
    for policy_name in DECLARED_POLICIES:
        preds = policy_predictions(policy_name, items)
        distinct = len(set(preds))
        ok = is_nondegenerate(preds, min_distinct=3)
        result["per_policy"][policy_name] = {
            "distinct_predictions": distinct,
            "nondegenerate": ok,
        }
        if not ok:
            all_pass = False
    result["all_pass"] = all_pass
    return result


def manifest_sha256(manifest: dict[str, Any]) -> str:
    canonical = json.dumps(manifest, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


RUNG_SPECS = {
    "L01": {"D": 4,  "K": "low",  "X": "base"},
    "L02": {"D": 8,  "K": "low",  "X": "base"},
    "L03": {"D": 16, "K": "low",  "X": "base"},
    "L04": {"D": 4,  "K": "high", "X": "base"},
    "L05": {"D": 8,  "K": "high", "X": "base"},
    "L06": {"D": 16, "K": "high", "X": "base"},
    "L07": {"D": 8,  "K": "low",  "X": "extended"},
    "L08": {"D": 8,  "K": "high", "X": "extended"},
}


def main(output_dir: Path) -> dict[str, Any]:
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    hashes = {}
    acceptance_results = []

    for rung_id, spec in RUNG_SPECS.items():
        manifest = generate_rung(rung_id, spec)
        path = output_dir / f"{rung_id}.json"
        with path.open("w", encoding="utf-8") as f:
            json.dump(manifest, f, sort_keys=True, indent=2)
        hashes[rung_id] = manifest_sha256(manifest)
        acceptance_results.append(recipe_acceptance_check_rung(manifest))

    with (output_dir / "MANIFEST-HASHES.lock").open("w", encoding="utf-8") as f:
        for rid, h in hashes.items():
            f.write(f"{rid}: {h}\n")

    with (output_dir / "RECIPE-ACCEPTANCE-CHECK-RESULTS.json").open(
        "w", encoding="utf-8"
    ) as f:
        json.dump({"results": acceptance_results}, f, sort_keys=True, indent=2)

    return {
        "manifest_recipe_seed": manifest_recipe_seed(),
        "manifest_hashes": hashes,
        "acceptance_results": acceptance_results,
    }


if __name__ == "__main__":
    out = main(SCRIPT_DIR / "manifests")
    print(json.dumps({"manifest_recipe_seed": out["manifest_recipe_seed"]}, indent=2))
