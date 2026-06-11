"""Lane 1a runner (locked; hash-recorded in LOCK-RECORD.md).

Lane 1a uses a lane-specific runner that preserves B1 v2-compatible
provenance conventions and locked model-loading dependencies, while
leaving B1 v2 source unedited.

This runner does NOT import any module from `experiments/2026-06-09_b1-harness-v2/`.
It uses `mlx_lm` directly (the same dependency B1 v2 uses) and records
the model snapshot hash in the same format B1 v2 uses
(sha256 over a sorted manifest of model-directory files).

CLI:
    python lane1a_runner.py --manifest <path> --output-dir <dir>
                            --output-prefix <prefix>
                            --stratum {answerable, null, answerable_mirror, null_mirror}
                            --rung-id <L01..L08>

Output: a single JSON file per invocation under <output-dir>, named
<prefix>-<timestamp>.json. The file is BYTE-PRESERVED by the wrapper;
Lane 1a metadata is sidecar-attested.

DOCTRINE: Lane 1a may rule out; Lane 1a may not rule in.
This runner does not authorize anything beyond producing locked-protocol
sweep outputs. The wrapper enforces lock-record + first-data-access
gates before this runner is invoked.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

SCRIPT_DIR = Path(__file__).resolve().parent

# Locked decoding settings (mirror B1 v2 deterministic defaults).
DECODING_SETTINGS = {
    "temperature": 0.0,
    "max_tokens": 64,        # short outputs for single-line key->value
    "greedy": True,
    "seed": 0,
}

MODEL_ID = "mlx-community/Qwen2.5-3B-Instruct-bf16"


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="milliseconds")


def compute_model_snapshot_hash(model_dir: Path) -> str:
    """sha256 over a sorted manifest of (relative path, file size,
    per-file sha256). Mirrors B1 v2's compute_model_snapshot_hash so
    the model-attestation format is comparable across runners."""
    if not model_dir.exists() or not model_dir.is_dir():
        return "sha256:[model-dir-not-found]"
    files = []
    for f in sorted(model_dir.rglob("*")):
        if f.is_file():
            rel = f.relative_to(model_dir)
            size = f.stat().st_size
            file_sha = hashlib.sha256(f.read_bytes()).hexdigest()
            files.append(f"{rel}\t{size}\t{file_sha}")
    manifest_str = "\n".join(files)
    return "sha256:" + hashlib.sha256(manifest_str.encode("utf-8")).hexdigest()


def locate_model_snapshot() -> Path | None:
    """Locate the Qwen2.5-3B-Instruct snapshot directory in the
    HuggingFace cache (same convention B1 v2 uses)."""
    hf_cache = Path(os.environ.get(
        "HF_HOME", Path.home() / ".cache" / "huggingface" / "hub"
    ))
    for candidate in hf_cache.rglob("snapshots/*"):
        if "Qwen2.5-3B-Instruct" in str(candidate) and candidate.is_dir():
            return candidate
    return None


def _sha256_str(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


# Lane 1a manifest schema validator (lightweight; no jsonschema dep).

REQUIRED_MANIFEST_KEYS = {
    "rung_id", "rung_spec", "per_rung_seed",
    "items", "controls",
    "artifact_class", "certification_relevance",
}
REQUIRED_ITEM_KEYS = {
    "item_id", "stratum", "in_context_pairs", "queried_key", "expected_answer",
}
VALID_STRATA = {"answerable", "null", "answerable_mirror", "null_mirror"}


class ManifestValidationError(RuntimeError):
    pass


def validate_lane1a_manifest(manifest: dict[str, Any]) -> None:
    if not isinstance(manifest, dict):
        raise ManifestValidationError("manifest must be a dict")
    missing = REQUIRED_MANIFEST_KEYS - manifest.keys()
    if missing:
        raise ManifestValidationError(f"missing top-level keys: {sorted(missing)}")
    if manifest["artifact_class"] != "lane-1a-reconnaissance":
        raise ManifestValidationError(
            f"artifact_class must be 'lane-1a-reconnaissance', got "
            f"{manifest['artifact_class']!r}"
        )
    if manifest["certification_relevance"] != "none":
        raise ManifestValidationError(
            f"certification_relevance must be 'none', got "
            f"{manifest['certification_relevance']!r}"
        )

    items = manifest["items"]
    controls = manifest["controls"]
    for part_name, part in [
        ("items.answerable", items.get("answerable")),
        ("items.null", items.get("null")),
        ("controls.answerable_mirror", controls.get("answerable_mirror")),
        ("controls.null_mirror", controls.get("null_mirror")),
    ]:
        if part is None or not isinstance(part, list):
            raise ManifestValidationError(f"{part_name} must be a list")
        for i, item in enumerate(part):
            if not isinstance(item, dict):
                raise ManifestValidationError(f"{part_name}[{i}] must be a dict")
            missing_item = REQUIRED_ITEM_KEYS - item.keys()
            if missing_item:
                raise ManifestValidationError(
                    f"{part_name}[{i}] missing item keys: {sorted(missing_item)}"
                )
            if item["stratum"] not in VALID_STRATA:
                raise ManifestValidationError(
                    f"{part_name}[{i}].stratum invalid: {item['stratum']!r}"
                )


# Prompt rendering.

PROMPT_TEMPLATE_PATH = SCRIPT_DIR / "prompt_template.md"


def _read_prompt_template() -> str:
    text = PROMPT_TEMPLATE_PATH.read_text(encoding="utf-8")
    # Extract the fenced template block from prompt_template.md.
    # We accept the first triple-backtick block as the template.
    start = text.find("```")
    if start < 0:
        raise RuntimeError("prompt_template.md has no template block")
    start = text.find("\n", start) + 1
    end = text.find("```", start)
    return text[start:end].strip()


def render_prompt(item: dict[str, Any], template: str) -> str:
    pairs = item["in_context_pairs"]
    in_context_list = "\n".join(f"{k}: {v}" for k, v in pairs)
    return template.replace("{IN_CONTEXT_LIST}", in_context_list).replace(
        "{QUERIED_KEY}", item["queried_key"]
    )


# Main runner.

def _generate_items(
    items: list[dict[str, Any]],
    model: Any,
    tokenizer: Any,
    stream_generate: Any,
    sampler: Any,
    template: str,
) -> list[dict[str, Any]]:
    results = []
    for item in items:
        prompt = render_prompt(item, template)
        prompt_hash = _sha256_str(prompt)
        chat_prompt = prompt
        if getattr(tokenizer, "chat_template", None) is not None:
            chat_prompt = tokenizer.apply_chat_template(
                [{"role": "user", "content": prompt}],
                add_generation_prompt=True, tokenize=False,
            )
        raw_output = ""
        for resp in stream_generate(
            model, tokenizer, prompt=chat_prompt,
            max_tokens=DECODING_SETTINGS["max_tokens"], sampler=sampler,
        ):
            raw_output += resp.text
        results.append({
            "item_id": item["item_id"],
            "stratum": item["stratum"],
            "queried_key": item["queried_key"],
            "expected_answer": item["expected_answer"],
            "prompt_hash": prompt_hash,
            "raw_output": raw_output.strip(),
        })
    return results


def run(
    manifest_path: Path,
    output_path: Path,
    stratum: str,
    rung_id: str,
) -> dict[str, Any]:
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    validate_lane1a_manifest(manifest)

    if rung_id != manifest["rung_id"]:
        raise RuntimeError(
            f"rung_id mismatch: --rung-id={rung_id} but manifest rung_id={manifest['rung_id']}"
        )
    if stratum not in VALID_STRATA:
        raise RuntimeError(f"unknown stratum: {stratum!r}")

    if stratum in ("answerable", "null"):
        items = manifest["items"][stratum]
    else:
        items = manifest["controls"][stratum]

    # Model loading + provenance (B1 v2-compatible conventions).
    try:
        import mlx_lm
        from mlx_lm import load, stream_generate
        from mlx_lm.sample_utils import make_sampler
    except ImportError as e:
        raise RuntimeError(f"mlx_lm not available: {e}")

    provenance: dict[str, Any] = {
        "runner": "lane1a_runner.py",
        "runner_version": "v0.1",
        "doctrine": "Lane 1a may rule out; Lane 1a may not rule in.",
        "framework_version": "none",
        "artifact_class": "lane-1a-reconnaissance",
        "certification_relevance": "none",
        "decoding_settings": DECODING_SETTINGS,
        "model_id": MODEL_ID,
        "mlx_lm_version": mlx_lm.__version__,
        "started_ts": _now_iso(),
    }

    snap_dir = locate_model_snapshot()
    if snap_dir is not None:
        provenance["model_snapshot_hash"] = compute_model_snapshot_hash(snap_dir)
    else:
        provenance["model_snapshot_hash"] = "sha256:[model-snapshot-not-located]"

    model, tokenizer = load(MODEL_ID)
    sampler = make_sampler(temp=DECODING_SETTINGS["temperature"])

    template = _read_prompt_template()
    results = _generate_items(
        items, model, tokenizer, stream_generate, sampler, template,
    )

    provenance["completed_ts"] = _now_iso()

    record = {
        "lane1a_runner_record_schema": "v1",
        "rung_id": rung_id,
        "stratum": stratum,
        "manifest_path": str(manifest_path),
        "manifest_hash": "sha256:" + hashlib.sha256(
            manifest_path.read_bytes()
        ).hexdigest(),
        "provenance": provenance,
        "items": results,
    }

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps(record, sort_keys=True, indent=2),
        encoding="utf-8",
    )
    return record


def _build_arg_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Lane 1a runner (mlx_lm; B1 v2-compatible provenance; B1 v2 unedited)")
    p.add_argument("--manifest", required=True)
    p.add_argument("--output-dir", required=True)
    p.add_argument("--output-prefix", required=True)
    p.add_argument("--stratum", required=True, choices=sorted(VALID_STRATA))
    p.add_argument("--rung-id", required=True,
                   choices=["L01","L02","L03","L04","L05","L06","L07","L08"])
    p.add_argument("--validate-only", action="store_true",
                   help="validate manifest schema only; no model load, no inference")
    return p


def main() -> int:
    args = _build_arg_parser().parse_args()
    manifest_path = Path(args.manifest)

    if args.validate_only:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        validate_lane1a_manifest(manifest)
        print(f"manifest valid: {manifest_path}")
        return 0

    ts = int(time.time())
    output_path = (
        Path(args.output_dir) / f"{args.output_prefix}-{ts}.json"
    )
    record = run(manifest_path, output_path, args.stratum, args.rung_id)
    print(json.dumps({
        "output_path": str(output_path),
        "rung_id": record["rung_id"],
        "stratum": record["stratum"],
        "items_count": len(record["items"]),
        "model_snapshot_hash_prefix": record["provenance"]["model_snapshot_hash"][:46],
    }, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
