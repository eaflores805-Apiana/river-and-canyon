#!/usr/bin/env python3
"""
v3_composite_gate_item_generator.py — wrapper for fresh-seed materialization.

Generates V3 item specs at an arbitrary contiguous index range by importing
and calling the existing v3_item_generator.generate_item() function directly.

Authority: Manager + TL ACTION 2026-06-18 ("Begin V3 Composite Gate Tooling
Build"). TL preferred this WRAPPER approach over patching v3_item_generator.py
so the underlying generator's bytes (sha 6a2ceee1...) remain unchanged and the
floor-check prereg v0.4's §"REUSED UNCHANGED" claim stays literally true.

The wrapper produces composite-gate-prereg-v0.2 §4 fresh items at the locked
seed range 097..192 (or any index range satisfying the ≤999 constraint that
preserves the 3-digit per-item-prefix scheme + MAX_DELTA = 8 binding).

DOES NOT:
  - alter the underlying generator's bytes
  - import any model
  - execute any prompt
  - authorize a model run
  - introduce any randomness or environment dependency

The wrapper is a pure function of (--start-index, --count): same args →
byte-identical output. Determinism inherited from the underlying generator.

— CS Engineer, 2026-06-18
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

# Make the path-a/build dir importable (we're in it)
_BUILD_DIR = Path(__file__).resolve().parent
if str(_BUILD_DIR) not in sys.path:
    sys.path.insert(0, str(_BUILD_DIR))

# Import the underlying generator's PUBLIC API — bytes unchanged.
import v3_item_generator as _gen


# v0.2 §4 locked invariant: indices ≤ 999 to preserve the 3-digit prefix scheme
# and the MAX_DELTA=8 binding.
MAX_ALLOWED_INDEX = 999


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[1])
    p.add_argument("--out-dir", type=Path, required=True,
                   help="output directory for generated items")
    p.add_argument("--start-index", type=int, required=True,
                   help="first item_index in the range (1-based; ≥1, ≤999)")
    p.add_argument("--count", type=int, required=True,
                   help="number of items to generate (start..start+count-1)")
    p.add_argument("--verbose", action="store_true",
                   help="print each generated item's path + sha256")
    args = p.parse_args(argv)

    end_index = args.start_index + args.count - 1
    if args.start_index < 1:
        print(f"--start-index must be ≥ 1; got {args.start_index}", file=sys.stderr)
        return 2
    if end_index > MAX_ALLOWED_INDEX:
        print(
            f"end-index ({end_index}) exceeds MAX_ALLOWED_INDEX ({MAX_ALLOWED_INDEX}); "
            f"would widen the per-item-prefix beyond 3 digits and break the "
            f"MAX_DELTA=8 token-width binding (v0.2 §4 constraint).",
            file=sys.stderr,
        )
        return 2

    args.out_dir.mkdir(parents=True, exist_ok=True)
    paths_and_hashes = []
    for n in range(args.start_index, end_index + 1):
        position = _gen.slot_for_index(n)
        seed     = _gen.seed_for_index(n)
        item     = _gen.generate_item(n, position, seed)
        body     = json.dumps(item, indent=2, sort_keys=False) + "\n"
        out_path = args.out_dir / f"item_{n:03d}.json"
        out_path.write_text(body)
        sha = hashlib.sha256(body.encode("utf-8")).hexdigest()
        paths_and_hashes.append((out_path, sha))
        if args.verbose:
            print(f"{sha}  {out_path}")

    if not args.verbose:
        print(
            f"wrote {len(paths_and_hashes)} items to {args.out_dir} "
            f"(indices {args.start_index}..{end_index})"
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
