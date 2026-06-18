#!/usr/bin/env python3
"""
v3_conformance_runner.py — drive the Path A inspector against every generated
V3 item and emit a single aggregate summary.

Operates as a thin orchestrator:
  - reads every items/*.json in --items-dir
  - invokes the path-a/inspector/inspector.py subprocess for each item,
    pinning each item to its own results JSON
  - reads each per-item inspector result back, aggregates into a summary
  - writes path-a/build/conformance_summary.json
  - exits 0 iff every item disposition == PASS

Why a subprocess invocation: it exercises the inspector exactly the way a
real-run pipeline would (CLI invocation, file I/O), and avoids importing
the inspector module from a path the inspector itself does not declare on
its sys.path. Output bytes (per-item inspection JSON) are identical to
what the inspector's main() writes when called by hand — i.e., the same
artifact a runner pipeline would consume.

Authority: build-realization only (TL/Manager ACTION 2026-06-17). Does NOT
authorize a model run; does NOT exercise model code; produces no model
outputs. The inspector itself is purely schema-level; it reads JSON specs
and emits JSON dispositions.

— CS Engineer, 2026-06-17
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path


def _run_inspector(
    inspector_path: Path,
    spec_path:      Path,
    out_path:       Path,
) -> tuple[int, str]:
    """Invoke inspector.py --spec <spec_path> --output <out_path>.
    Returns (returncode, stdout)."""
    cmd = [
        sys.executable,
        str(inspector_path),
        "--spec",   str(spec_path),
        "--output", str(out_path),
    ]
    cp = subprocess.run(cmd, capture_output=True, text=True, check=False)
    return cp.returncode, cp.stdout + cp.stderr


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--items-dir",      type=Path, required=True,
                   help="directory containing item_*.json specs")
    p.add_argument("--results-dir",    type=Path, required=True,
                   help="directory to write per-item *_inspection.json")
    p.add_argument("--inspector-path", type=Path, required=True,
                   help="path to path-a/inspector/inspector.py")
    p.add_argument("--summary-path",   type=Path, required=True,
                   help="path to write conformance_summary.json")
    args = p.parse_args(argv)

    args.results_dir.mkdir(parents=True, exist_ok=True)

    items = sorted(args.items_dir.glob("item_*.json"))
    if not items:
        print(f"no item_*.json found in {args.items_dir}", file=sys.stderr)
        return 2

    per_item = []
    all_pass = True
    for spec_path in items:
        item_id = spec_path.stem
        out_path = args.results_dir / f"{item_id}_inspection.json"
        rc, log = _run_inspector(args.inspector_path, spec_path, out_path)
        result = json.loads(out_path.read_text())
        disposition = result["disposition"]
        n_passes    = result["n_passes"]
        n_checks    = result["n_checks"]
        n_failures  = result["n_failures"]
        per_item.append({
            "item":               item_id,
            "spec_path":          str(spec_path),
            "result_path":        str(out_path),
            "disposition":        disposition,
            "n_checks":           n_checks,
            "n_passes":           n_passes,
            "n_failures":         n_failures,
            "construction_id":    result.get("construction_id"),
            "inspector_exit":     rc,
        })
        if disposition != "PASS":
            all_pass = False

    summary = {
        "inspector_path":    str(args.inspector_path),
        "items_dir":         str(args.items_dir),
        "results_dir":       str(args.results_dir),
        "n_items":           len(per_item),
        "n_pass":            sum(1 for x in per_item if x["disposition"] == "PASS"),
        "n_reject":          sum(1 for x in per_item if x["disposition"] != "PASS"),
        "all_pass":          all_pass,
        "per_item":          per_item,
        "scope":             "build-realization only; not run-authorized",
        "expected_mode":     "real-run (no _fixture_mode, no _sweep_mode)",
    }
    args.summary_path.write_text(json.dumps(summary, indent=2) + "\n")
    print(f"items: {summary['n_items']}  pass: {summary['n_pass']}  "
          f"reject: {summary['n_reject']}  all_pass: {summary['all_pass']}")
    print(f"summary: {args.summary_path}")
    return 0 if all_pass else 1


if __name__ == "__main__":
    sys.exit(main())
