#!/usr/bin/env python3
"""build_manifest.py — assemble manifest.json for the Hop1 Stability run.

Inventories every artifact under experiments/2026-06-19_hop1-stability-run/
with sha256 digests, alongside locked tooling + prereg digests.
Pure read-only inventory; does not mutate any artifact.
"""
from __future__ import annotations
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RUN  = Path(__file__).resolve().parent
RUN_REL = RUN.relative_to(ROOT)


def sha(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def entry(p: Path) -> dict:
    return {"path": str(p.relative_to(ROOT)), "sha256": sha(p)}


def inv(d: Path, glob: str = "*") -> list[dict]:
    return [entry(p) for p in sorted(d.rglob(glob)) if p.is_file()]


def main() -> int:
    manifest = {
        "run_id": "v3-hop1-stability-2026-06-19",
        "run_directory": str(RUN_REL),
        "authority": "Manager by-name authorization 2026-06-19 "
                     "(Execute Hop1 Stability Investigation)",
        "prereg": entry(ROOT / "path-a/in-review/PREREGISTRATION-HOP1-STABILITY-PATH-A-v0.1.md"),
        "instrument": {
            "inspector": entry(ROOT / "path-a/inspector/inspector.py"),
            "constants": entry(ROOT / "path-a/inspector/constants.py"),
        },
        "hop1_stability_tooling": {
            "analyzer":         entry(ROOT / "path-a/build/v3_hop1_stability_analyzer.py"),
            "covariate_logger": entry(ROOT / "path-a/build/v3_hop1_covariate_logger.py"),
        },
        "reused_tooling_unchanged": {
            "item_generator_wrapper": entry(ROOT / "path-a/build/v3_composite_gate_item_generator.py"),
            "item_generator":         entry(ROOT / "path-a/build/v3_item_generator.py"),
            "prompt_realizer":        entry(ROOT / "path-a/build/v3_prompt_realizer.py"),
            "conformance_checker":    entry(ROOT / "path-a/build/v3_prompt_conformance_checker.py"),
            "conformance_runner":     entry(ROOT / "path-a/build/v3_conformance_runner.py"),
            "neutral_token_pool":     entry(ROOT / "path-a/build/v3_neutral_token_pool.md"),
        },
        "auxiliary_scripts": {
            "inference_runner": entry(RUN / "run_step_5.py"),
            "manifest_builder": entry(RUN / "build_manifest.py"),
        },
        "items":           inv(RUN / "items_193_768"),
        "prompts":         inv(RUN / "prompts"),
        "admissibility":   inv(RUN / "admissibility"),
        "scored":          inv(RUN / "scored"),
        "summaries": {
            "realization_summary":           entry(RUN / "realization_summary.json"),
            "admissibility_summary":         entry(RUN / "admissibility_summary.json"),
            "prompt_conformance_summary":    entry(RUN / "prompt_conformance_summary.json"),
        },
        "run_record":      entry(RUN / "run_record.json"),
        "covariate_log":   entry(RUN / "covariate_log.json"),
        "decision":        entry(RUN / "decision.json"),
        "inference_log":   entry(RUN / "run_step_5.log"),
    }

    dec = json.loads((RUN / "decision.json").read_text())
    manifest["final_branch"]            = dec["final_branch"]
    manifest["branch_priority_order"]   = dec["branch_priority_order"]
    manifest["n1A_enforcement"]         = dec["n1A_enforcement"]

    manifest["boundaries_held_at_filing"] = [
        "no composite-gate retry",
        "no compression / INT8 / INT4",
        "no Claim C, Paper B, certification, capability, mechanism claims",
        "no rerun until preferred branch appeared",
        "no post-hoc covariate fishing (only the predeclared §6 set logged)",
        "no prompt edits after execution (prompts consumed as committed)",
        "no tooling edits after data (all 8 tooling digests UNCHANGED)",
        "N1.A enforced: composite + dq rendered but NEVER executed",
        "anchors 001..096 / 097..192 NOT entered into branch decision",
        "tier0-run/ remained sealed (no files added)",
        "Path A FP16 K=5 FAIL stays closed",
    ]
    manifest["counts"] = {
        "n_items":             576,
        "n_admissibility":     576,
        "n_prompts_rendered":  2304,
        "n_prompts_executed":  1152,
        "n_scored_contract":   1152,
        "n_blocks":            6,
        "n_per_block":         96,
    }
    manifest["scope"] = ("run-record inventory only; no bytes mutated by this manifest filing")

    (RUN / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    print(f"manifest written: {RUN / 'manifest.json'}")
    print(f"final_branch:    {manifest['final_branch']}")
    print(f"items inventoried:  items={len(manifest['items'])} prompts={len(manifest['prompts'])} "
          f"admissibility={len(manifest['admissibility'])} scored={len(manifest['scored'])}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
