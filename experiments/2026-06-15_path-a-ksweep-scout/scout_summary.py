#!/usr/bin/env python3
"""
scout_summary.py -- Path A K-Sweep Scout cross-cell aggregation + disposition.

Per locked prereg v1.0 (sha 248581f6...) §4 + §5. Reads scored_K1.json ..
scored_K5.json + closed K=5 run's scored.json (for the K=5 reproduction check).
Emits SCOUT_SUMMARY.json + DISPOSITION text.

LOCKED RULES applied verbatim from prereg:
  SHAPE PATTERNS (named pre-look): ramp / cliff / plateau / interior-peak / reverse-K / flat
  BAND-HINT (Q3 = yes worth certifying later) -- ALL of:
    (i)   validated-R1 markedly higher at some interior K than at K=1 AND K=5 ends
    (ii)  at that K, control margins STABLE OR STRONGER (not weakest there)
    (iii) Dial A steady-or-up while Dial B beats per-K base rate
  THE NULL: validated-R1 flat or monotone across K with no interior lift meeting band-hint
  BOUNDARY (F2): best cell at range edge -> descriptive caveat; separate one-off if pursued
  STOP-RULE: no added K, no re-slice, no new pattern post-hoc.

K=5 REPRODUCTION CHECK (§5):
  K=5 cell must reproduce validated-R1 ≈ 18/96 from closed run. Failure voids scout.
"""
from __future__ import annotations

import json
import math
import sys
from pathlib import Path

RUN_DIR = Path(__file__).resolve().parent
CLOSED_K5_DIR = RUN_DIR.parent / "2026-06-15_path-a-fp16-constructibility"
K_LIST = [1, 2, 3, 4, 5]


def load_scored(K: int) -> dict:
    return json.loads((RUN_DIR / f"scored_K{K}.json").read_text())


def main() -> int:
    cells = {}
    for K in K_LIST:
        d = load_scored(K)
        s = d["summary"]
        cells[K] = {
            "n":                     s["n_items"],
            "R1_validated":          s["primary"]["R1_validated"],
            "R1_rate":               s["primary"]["R1_validated_rate"],
            "ci_lo":                 s["primary"]["wilson_95_ci"]["lower"],
            "ci_hi":                 s["primary"]["wilson_95_ci"]["upper"],
            "ci_half_width":         s["primary"]["wilson_95_ci"]["half_width"],
            "off_map_positional":    s["secondary"]["off_map_positional"]["rate"],
            "off_map_dC":            s["secondary"]["off_map_positional"]["decoy_answer_depth_dC"]["rate"],
            "off_map_dB":            s["secondary"]["off_map_positional"]["decoy_bridge_depth_dB"]["rate"],
            "dial_A":                s["secondary"]["dial_A_answer_depth_landing"]["rate"],
            "dial_B_share":          s["secondary"]["dial_B_right_chain_share"]["share"],
            "dial_B_base":           s["secondary"]["dial_B_right_chain_share"]["base_rate"],
            "dial_B_gain_over_base": s["secondary"]["dial_B_right_chain_share"]["gain_over_base"],
            "chain_membership_pattern": s["secondary"]["chain_membership_pattern"]["pattern_summary"],
            "hop1_pass":             s["secondary"]["control_margins"]["hop1_pass_rate"],
            "hop2_pass":             s["secondary"]["control_margins"]["hop2_pass_rate"],
            "dq_pass":               s["secondary"]["control_margins"]["dq_pass_rate"],
            "terminal_grab_R2":      s["secondary"]["control_margins"]["terminal_grab_R2_rate"],
            "decoy_terminal_R4":     s["secondary"]["control_margins"]["decoy_terminal_R4_rate"],
            "depth_competitor_R4b":  s["secondary"]["control_margins"]["depth_competitor_R4b_rate"],
            "R6cat_rate":            s["composite_rates"].get("R6cat", 0.0),
            "R5_abstain_rate":       s["composite_rates"].get("R5", 0.0),
            "R3_stopped_short_rate": s["composite_rates"].get("R3", 0.0),
        }

    # ── K=5 REPRODUCTION CHECK ─────────────────────────────────────────────
    closed_scored = json.loads((CLOSED_K5_DIR / "scored.json").read_text())
    closed_R1 = closed_scored["summary"]["invalidation_counts"]["R1_validated"]
    new_K5_R1 = cells[5]["R1_validated"]
    repro_ok = (new_K5_R1 == closed_R1)

    # ── Shape classification ────────────────────────────────────────────────
    R1_curve = [cells[K]["R1_rate"] for K in K_LIST]
    def is_monotone(seq):
        ups = sum(1 for i in range(len(seq)-1) if seq[i+1] > seq[i])
        dns = sum(1 for i in range(len(seq)-1) if seq[i+1] < seq[i])
        return ("up" if dns == 0 and ups > 0 else
                "down" if ups == 0 and dns > 0 else
                "non_monotone")
    def is_flat(seq, eps=0.05):
        return (max(seq) - min(seq)) <= eps

    # Argmax K
    best_K = max(K_LIST, key=lambda k: cells[k]["R1_rate"])
    best_R1 = cells[best_K]["R1_rate"]
    end_K1 = cells[1]["R1_rate"]
    end_K5 = cells[5]["R1_rate"]

    if is_flat(R1_curve, eps=0.05):
        shape = "flat"
    else:
        mono = is_monotone(R1_curve)
        if mono == "up":
            shape = "ramp"            # increases with K
        elif mono == "down":
            shape = "reverse-K"       # decreases with K (like terminal-attraction sweep)
        else:
            # Non-monotone. Could be interior-peak, cliff, plateau, or other.
            # Interior-peak: best_K in {2,3,4} AND best_R1 > both ends
            if best_K in (2, 3, 4) and best_R1 > end_K1 and best_R1 > end_K5:
                shape = "interior-peak"
            else:
                # Cliff: sharp drop between adjacent cells
                drops = [R1_curve[i] - R1_curve[i+1] for i in range(len(R1_curve)-1)]
                rises = [R1_curve[i+1] - R1_curve[i] for i in range(len(R1_curve)-1)]
                if max(drops + [0]) > 0.2 or max(rises + [0]) > 0.2:
                    shape = "cliff"
                else:
                    shape = "plateau"

    # ── Band-hint evaluation (descriptive Q3) ──────────────────────────────
    band_hint_per_K = {}
    for K in K_LIST:
        if K == 1 or K == 5:
            band_hint_per_K[K] = {
                "is_interior": False,
                "qualifies":   False,
                "reason":      "edge cell; band-hint must be INTERIOR (K in 2,3,4) per prereg",
            }
            continue
        c = cells[K]
        # (i) markedly higher than both ends -- use Wilson lower > end CI upper as 'markedly'
        end1 = cells[1]; end5 = cells[5]
        cond_i = (c["ci_lo"] > end1["ci_hi"] and c["ci_lo"] > end5["ci_hi"])
        # (ii) control margins stable-or-stronger here -- compare to the better of the two ends
        ends_hop1 = max(end1["hop1_pass"], end5["hop1_pass"])
        ends_hop2 = max(end1["hop2_pass"], end5["hop2_pass"])
        ends_dq   = max(end1["dq_pass"],   end5["dq_pass"])
        cond_ii = (c["hop1_pass"] >= ends_hop1 - 0.02 and  # 2-pt tolerance
                   c["hop2_pass"] >= ends_hop2 - 0.02 and
                   c["dq_pass"]   >= ends_dq   - 0.02)
        # (iii) Dial A steady-or-up AND Dial B beats per-K base rate (gain > 0)
        ends_dial_A = max(end1["dial_A"], end5["dial_A"])
        cond_iii_A = (c["dial_A"] >= ends_dial_A - 0.05)
        cond_iii_B = (c["dial_B_gain_over_base"] is not None and c["dial_B_gain_over_base"] > 0.0)
        cond_iii = cond_iii_A and cond_iii_B
        qualifies = cond_i and cond_ii and cond_iii
        band_hint_per_K[K] = {
            "is_interior":   True,
            "qualifies":     qualifies,
            "cond_i_markedly_higher_than_ends":         cond_i,
            "cond_ii_control_margins_stable_or_better": cond_ii,
            "cond_iii_A_dial_A_steady_or_up":           cond_iii_A,
            "cond_iii_B_dial_B_beats_per_K_base_rate":  cond_iii_B,
            "cond_iii":                                 cond_iii,
        }

    any_band_hint = any(v["qualifies"] for v in band_hint_per_K.values())
    band_hint_K = next((k for k, v in band_hint_per_K.items() if v["qualifies"]), None)

    # ── Boundary case (F2) ─────────────────────────────────────────────────
    is_boundary = best_K in (1, 5)
    boundary_note = (f"best cell at K={best_K} (range edge); structure may extend "
                     f"beyond {{1..5}}; pursuing is a SEPARATE one-off per prereg F2"
                     if is_boundary else None)

    # ── Q3 disposition ─────────────────────────────────────────────────────
    if any_band_hint:
        Q3 = "BAND-HINT"
        Q3_K = band_hint_K
        Q3_reason = (f"interior K={band_hint_K} meets ALL band-hint conditions: validated-R1 "
                     f"markedly higher than both ends AND control margins stable-or-stronger AND "
                     f"Dial A steady-or-up AND Dial B beats per-K base rate")
    elif is_boundary:
        Q3 = "BOUNDARY"
        Q3_K = best_K
        Q3_reason = boundary_note
    else:
        Q3 = "NO-BAND"
        Q3_K = None
        Q3_reason = "validated-R1 flat or monotone across K with no interior lift meeting the band-hint conditions"

    summary = {
        "run_name":              "PATH-A-KSWEEP-SCOUT-2026-06-15",
        "stage":                 "scout_summary",
        "preregistration_sha":   "248581f673df2300ddf8567bd7fb826f1c3536dd459ff20576b689a07ea5ab90",
        "K_list":                K_LIST,
        "cells":                 cells,
        # K=5 reproduction harness check (§5)
        "K5_reproduction_check": {
            "closed_R1_validated":      closed_R1,
            "new_K5_R1_validated":      new_K5_R1,
            "match":                    repro_ok,
            "verdict":                  "PASS" if repro_ok else "FAIL",
            "note":                     "Per prereg §5: if K=5 cell does not reproduce the closed FAIL (~18/96), harness is suspect and scout is void pending diagnosis.",
            "closed_run_scored_path":   str(CLOSED_K5_DIR / "scored.json"),
        },
        # Shape + Q3
        "shape":                 shape,
        "shape_curve_R1_validated": dict(zip(K_LIST, R1_curve)),
        "best_K":                best_K,
        "best_R1_rate":          best_R1,
        "is_boundary":           is_boundary,
        "boundary_note":         boundary_note,
        "band_hint_per_K":       band_hint_per_K,
        "any_band_hint":         any_band_hint,
        "Q3_disposition":        Q3,
        "Q3_K":                  Q3_K,
        "Q3_reason":             Q3_reason,
        # Stop-rule reminder
        "stop_rule": "No added K, no re-slice, no new pattern post-hoc. Per prereg §4. Any extension is a fresh one-off.",
    }

    out_path = RUN_DIR / "SCOUT_SUMMARY.json"
    out_path.write_text(json.dumps(summary, indent=2) + "\n")
    print(f"wrote {out_path}")

    print("\n=== K-Sweep Scout Summary ===")
    print("K  | n  | R1   | rate  | Wilson 95% CI    | off-map+  | dC    | dB    | Dial A | Dial B  | base  | gain   | hop1 | hop2 | dq   ")
    print("-- | -- | ---- | ----- | ---------------- | --------- | ----- | ----- | ------ | ------- | ----- | ------ | ---- | ---- | ----")
    for K in K_LIST:
        c = cells[K]
        gain = c["dial_B_gain_over_base"]
        gain_s = f"{gain:+.4f}" if gain is not None else "  n/a "
        dB_s   = f"{c['dial_B_share']:.4f}" if c["dial_B_share"] is not None else " n/a  "
        print(f"K={K} | {c['n']:>2d} | {c['R1_validated']:>4d} | {c['R1_rate']:.3f} | [{c['ci_lo']:.4f},{c['ci_hi']:.4f}] | {c['off_map_positional']:.4f}    | {c['off_map_dC']:.3f} | {c['off_map_dB']:.3f} | {c['dial_A']:.4f} | {dB_s} | {c['dial_B_base']:.3f} | {gain_s} | {c['hop1_pass']:.2f} | {c['hop2_pass']:.2f} | {c['dq_pass']:.2f}")
    print(f"\nShape: {shape}")
    print(f"Best K: {best_K} (R1 rate {best_R1:.4f})")
    print(f"K=5 reproduction: {'PASS' if repro_ok else 'FAIL'}  (closed={closed_R1}  new={new_K5_R1})")
    print(f"Q3 disposition: {Q3}  (K={Q3_K})")
    print(f"  reason: {Q3_reason}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
