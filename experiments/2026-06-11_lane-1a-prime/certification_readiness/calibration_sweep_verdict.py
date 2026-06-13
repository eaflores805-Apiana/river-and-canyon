#!/usr/bin/env python3
"""
calibration_sweep_verdict.py — PRE-REGISTERED interpretation harness.

River and Canyon program. Certification-readiness submap, stage 3 interpretation.
Model-free. This script does NOT run the model. It consumes the run-output JSON
that CS produces (one per candidate) and emits the band verdict against the
PRE-DECLARED decision rule from OFF-CEILING-CALIBRATION-SWEEP-SPEC-v0.1.

The point of pre-registering this BEFORE the run: when the real bytes come back,
the verdict is computed mechanically and cannot be reinterpreted to fit a hope.

USAGE (run by CS or Senior AFTER CS produces the run outputs):
    python3 calibration_sweep_verdict.py \
        --floor 0.6125 --margin <m> --delta <d> \
        --ceiling 1.0 \
        --run CAL-A:path/to/cal_a_run.json \
        --run CAL-B:path/to/cal_b_run.json \
        --run CAL-C:path/to/cal_c_run.json \
       [--run CAL-D:path/to/cal_d_run.json]

Each run JSON must contain (CS's runner emits this):
    {
      "candidate_id": "CAL-B",
      "clean_member":     {"summary": {"strict_accuracy": <float>, "n": <int>}},
      "defective_member": {"summary": {"strict_accuracy": <float>, "n": <int>}},
      "single_difference_ok": <bool>,
      "manifest_sha256": "...", "scorer_sha256": "...",
      "prompt_template_sha256": "...", "raw_output_path": "..."
    }

margin (m) and delta (d) are pre-declared band parameters; they are inputs, not
chosen after seeing results. If unset, the harness HOLDS and reports that the
band parameters must be fixed before a verdict is valid.
"""
import argparse, json, sys


def classify_candidate(clean_acc, floor, margin, ceiling, delta):
    """Where does this candidate's clean accuracy sit relative to the band?"""
    lower = floor + margin          # must be strictly above this
    upper = ceiling - delta         # must be strictly below this
    if clean_acc >= upper:          # at/above the saturation-room boundary
        return "CEILING", lower, upper
    if clean_acc <= lower:          # at/below the shortcut-floor+margin boundary
        return "FLOOR_COLLAPSE", lower, upper
    return "IN_BAND", lower, upper   # strictly inside


def verdict(candidates, floor, margin, ceiling, delta):
    """Apply the PRE-DECLARED decision rule. Returns (verdict, reasoning)."""
    # INSUFFICIENT gate first: any authorized candidate failing single-difference
    bad = [c["candidate_id"] for c in candidates if not c.get("single_difference_ok", False)]
    if bad:
        return ("INSUFFICIENT / NEEDS REPAIR",
                f"single-difference check failed for {bad}; matching invalid → cannot judge band")

    placed = []
    for c in candidates:
        ca = c["clean_member"]["summary"]["strict_accuracy"]
        where, lo, hi = classify_candidate(ca, floor, margin, ceiling, delta)
        placed.append((c["candidate_id"], ca, where))

    in_band = [p for p in placed if p[2] == "IN_BAND"]
    escaped_ceiling = [p for p in placed if p[2] in ("IN_BAND", "FLOOR_COLLAPSE")]
    collapsed = [p for p in placed if p[2] == "FLOOR_COLLAPSE"]

    # Rule, verbatim from the spec:
    if in_band:
        return ("BAND PLAUSIBLE",
                f"in-band candidate(s): {[(p[0], round(p[1],4)) for p in in_band]} "
                f"land in ({floor}+{margin}, {ceiling}-{delta}) = ({floor+margin}, {ceiling-delta})")
    if escaped_ceiling and len(collapsed) == len(escaped_ceiling):
        return ("BAND TOO NARROW",
                f"every ceiling-escaping candidate collapsed to/below floor+margin "
                f"({[(p[0], round(p[1],4)) for p in collapsed]}); "
                f"levers cannot separate ceiling escape from floor collapse")
    # nothing escaped the ceiling at all → not narrow, not plausible: needs harder settings
    return ("INSUFFICIENT / NEEDS REPAIR",
            f"no candidate escaped the ceiling (all CEILING: "
            f"{[(p[0], round(p[1],4)) for p in placed]}); "
            f"levers did not move accuracy off ceiling → specify harder settings, do not pivot")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--floor", type=float, default=0.6125)
    ap.add_argument("--ceiling", type=float, default=1.0)
    ap.add_argument("--margin", type=float, default=None)
    ap.add_argument("--delta", type=float, default=None)
    ap.add_argument("--run", action="append", default=[],
                    help="CAND_ID:path/to/run.json")
    args = ap.parse_args()

    if args.margin is None or args.delta is None:
        print("HOLD: margin (m) and delta (δ) must be PRE-DECLARED before a verdict "
              "is valid. Re-run with --margin and --delta fixed in advance.",
              file=sys.stderr)
        sys.exit(2)

    candidates = []
    for spec in args.run:
        cid, path = spec.split(":", 1)
        with open(path) as f:
            d = json.load(f)
        d["candidate_id"] = d.get("candidate_id", cid)
        candidates.append(d)

    if not candidates:
        print("HOLD: no run outputs provided. This harness interprets a completed "
              "run; it does not produce one.", file=sys.stderr)
        sys.exit(2)

    v, why = verdict(candidates, args.floor, args.margin, args.ceiling, args.delta)

    print("=== OFF-CEILING CALIBRATION SWEEP — PRE-REGISTERED VERDICT ===")
    print(f"band: {args.floor} + {args.margin} < clean_acc < {args.ceiling} - {args.delta}")
    print(f"      = ({args.floor + args.margin}, {args.ceiling - args.delta})\n")
    for c in candidates:
        ca = c["clean_member"]["summary"]["strict_accuracy"]
        da = c.get("defective_member", {}).get("summary", {}).get("strict_accuracy")
        where, lo, hi = classify_candidate(ca, args.floor, args.margin, args.ceiling, args.delta)
        print(f"  {c['candidate_id']}: clean={ca}  defective={da}  → {where}")
        print(f"      floor+margin={lo}  ceiling-δ={hi}  single_diff_ok={c.get('single_difference_ok')}")
    print(f"\nVERDICT: {v}")
    print(f"REASON:  {why}")
    print("\nNOTE: calibration only. NOT certification, NOT compression, NOT Claim C evidence.")


if __name__ == "__main__":
    main()
