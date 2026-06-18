#!/usr/bin/env python3
"""
v3_prompt_conformance_checker.py — V3 prompt-level conformance checker (floor-check tooling 3/4).

Verifies that realized four-context prompts PRESERVE the foreclose-all properties
of the underlying schema-level spec AND meet the v0.4 §4/F1 length-matching gate
(character-count delta ≤ MAX_DELTA = 8). Output gates §9(vi) "prompt-realization
conformance PASS" in the analyzer.

Authority: Manager + TL ACTION 2026-06-18 ("File V3 Floor-Check Prereg v0.4
and Begin Tooling Build"), Step 2. **Build effort only.** This tool does NOT
import any model, does NOT execute any prompt, does NOT authorize a run.

Determinism: pure function of (item_spec, realized_prompts); no clock, no RNG,
no environment, no network.

Property checks per item-set:
  P1  composite, hop1, hop2, dq are all present (4 prompt files)
  P2  same-template-class invariant (each prompt starts with "FACTS:\\n"
      and contains exactly one "QUERY: " line)
  P3  composite, hop1, hop2 contain the bridge fact triple "(B, r2, C*)";
      direct_query does NOT (substituted by filler)
  P4  hop1 query does NOT contain C* token (R8.1 / R6c boundary)
  P5  direct_query prompt does NOT contain C* token (R6c direct-recall control;
      C* only appeared at the bridge fact in composite/hop1/hop2, and the
      bridge is substituted in dq, so C* should be absent from the dq prompt)
  P6  the SUBSTITUTED filler line in direct_query does NOT contain B or C*
      (E5 filler binding; B is allowed elsewhere in the dq prompt body — at
      the A-r1-B fact — because the model needs to know what B is to attempt
      the hop2 step; what's forbidden is the filler itself revealing B or C*)
  P7  hop2 query line contains B; expects C* as answer
  P8  no decoy terminal T_i appears in any QUERY line of any context
  P9  per-item char delta across the four contexts ≤ MAX_DELTA = 8
  P10 the filler triple in direct_query uses a verb from the locked verb pool

— CS Engineer, 2026-06-18
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


MAX_DELTA = 8

LOCKED_FILLER_VERBS = {"holds", "marks", "types", "pairs", "links"}


def _read_four(prompts_item_dir: Path) -> dict[str, str]:
    """Return the four prompt strings as a dict keyed by context name."""
    out = {}
    for ctx in ("composite", "hop1", "hop2", "direct_query"):
        p = prompts_item_dir / f"{ctx}.txt"
        if not p.exists():
            raise FileNotFoundError(f"missing prompt file: {p}")
        out[ctx] = p.read_text()
    return out


def _bridge_triple_str(spec: dict) -> str:
    t = spec["target"]
    return f"({t['B']}, {t['r2']}, {t['C_star']})"


def _decoy_terminals(spec: dict) -> set[str]:
    return {d["T_i"] for d in spec.get("decoy_chains", [])}


def check_item(spec: dict, prompts: dict[str, str]) -> dict:
    """Run P1–P10 on a single item; return a per-property result dict."""
    t = spec["target"]
    C_star = t["C_star"]
    B      = t["B"]
    bridge = _bridge_triple_str(spec)
    decoy_terminals = _decoy_terminals(spec)

    checks: dict[str, dict] = {}

    # P1 presence — implicit in _read_four; if we got here, all four exist
    checks["P1_presence"] = {"ok": True}

    # P2 template class
    def _template_ok(text: str) -> bool:
        return text.startswith("FACTS:\n") and text.count("QUERY: ") == 1
    p2_oks = {ctx: _template_ok(text) for ctx, text in prompts.items()}
    checks["P2_template_class"] = {
        "ok":     all(p2_oks.values()),
        "detail": p2_oks,
    }

    # P3 bridge presence
    p3_oks = {
        "composite":    bridge in prompts["composite"],
        "hop1":         bridge in prompts["hop1"],
        "hop2":         bridge in prompts["hop2"],
        "direct_query": bridge not in prompts["direct_query"],
    }
    checks["P3_bridge_presence_or_substitution"] = {
        "ok":     all(p3_oks.values()),
        "detail": p3_oks,
    }

    # P4 hop1 query does not contain C*
    def _query_line(text: str) -> str:
        for line in text.split("\n"):
            if line.startswith("QUERY: "):
                return line
        return ""
    hop1_query = _query_line(prompts["hop1"])
    checks["P4_hop1_query_no_Cstar"] = {
        "ok":     C_star not in hop1_query,
        "detail": {"hop1_query": hop1_query, "C_star": C_star},
    }

    # P5 dq prompt does not contain C*
    checks["P5_dq_no_Cstar"] = {
        "ok":     C_star not in prompts["direct_query"],
        "detail": {"C_star": C_star},
    }

    # P6 SUBSTITUTED FILLER LINE does not contain B or C*
    # (E5 binding: the filler must contain neither B nor C*. B is allowed
    # elsewhere in dq because the model needs to know B to attempt hop2;
    # what's forbidden is the filler line itself revealing B or C*.)
    dq_facts_section_p6 = prompts["direct_query"].split("QUERY: ")[0]
    dq_fact_lines_p6 = [l for l in dq_facts_section_p6.split("\n")
                        if l.startswith("(") and l.endswith(")")]
    filler_line = dq_fact_lines_p6[1] if len(dq_fact_lines_p6) > 1 else ""
    checks["P6_filler_line_no_B_no_Cstar"] = {
        "ok":     (B not in filler_line) and (C_star not in filler_line),
        "detail": {"filler_line": filler_line, "B": B, "C_star": C_star},
    }

    # P7 hop2 query contains B
    hop2_query = _query_line(prompts["hop2"])
    checks["P7_hop2_query_has_B"] = {
        "ok":     B in hop2_query,
        "detail": {"hop2_query": hop2_query, "B": B},
    }

    # P8 no decoy terminal in any query line
    def _no_decoy_terminal_in_query(ctx_text: str) -> bool:
        q = _query_line(ctx_text)
        return not any(t in q for t in decoy_terminals)
    p8_oks = {ctx: _no_decoy_terminal_in_query(text) for ctx, text in prompts.items()}
    checks["P8_no_decoy_terminal_in_queries"] = {
        "ok":     all(p8_oks.values()),
        "detail": p8_oks,
    }

    # P9 char delta
    char_counts = {ctx: len(text) for ctx, text in prompts.items()}
    delta = max(char_counts.values()) - min(char_counts.values())
    checks["P9_char_delta_gate"] = {
        "ok":     delta <= MAX_DELTA,
        "detail": {"char_counts": char_counts, "delta": delta, "max_delta_gate": MAX_DELTA},
    }

    # P10 filler verb is from the locked pool
    # Find the substitute line in direct_query (it replaces the bridge at line index 2 of FACTS body)
    dq_facts_section = prompts["direct_query"].split("QUERY: ")[0]
    dq_fact_lines = [l for l in dq_facts_section.split("\n") if l.startswith("(") and l.endswith(")")]
    # The bridge line was at index 1 of the original facts; same index in the substituted list
    sub_line = dq_fact_lines[1] if len(dq_fact_lines) > 1 else ""
    # Extract verb between commas
    inner = sub_line.strip("()")
    parts = [s.strip() for s in inner.split(",")]
    verb = parts[1] if len(parts) >= 3 else ""
    checks["P10_filler_verb_locked"] = {
        "ok":     verb in LOCKED_FILLER_VERBS,
        "detail": {"sub_line": sub_line, "verb": verb, "locked_pool": sorted(LOCKED_FILLER_VERBS)},
    }

    item_pass = all(c["ok"] for c in checks.values())
    return {
        "item_id":         spec["construction_id"],
        "all_checks_pass": item_pass,
        "checks":          checks,
    }


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--items-dir",     type=Path, required=True,
                   help="directory of item_*.json specs (input)")
    p.add_argument("--prompts-dir",   type=Path, required=True,
                   help="directory of per-item subdirs with {composite,hop1,hop2,direct_query}.txt")
    p.add_argument("--summary-path",  type=Path, required=True,
                   help="path to write prompt_conformance_summary.json")
    args = p.parse_args(argv)

    items = sorted(args.items_dir.glob("item_*.json"))
    if not items:
        print(f"no item_*.json found in {args.items_dir}", file=sys.stderr)
        return 2

    rows = []
    all_pass = True
    for spec_path in items:
        spec = json.loads(spec_path.read_text())
        item_dir = args.prompts_dir / spec_path.stem
        prompts = _read_four(item_dir)
        result = check_item(spec, prompts)
        rows.append(result)
        if not result["all_checks_pass"]:
            all_pass = False

    summary = {
        "checker_version":  "v0.1",
        "max_delta_gate":   MAX_DELTA,
        "items_dir":        str(args.items_dir),
        "prompts_dir":      str(args.prompts_dir),
        "n_items":          len(rows),
        "n_pass":           sum(1 for r in rows if r["all_checks_pass"]),
        "n_fail":           sum(1 for r in rows if not r["all_checks_pass"]),
        "all_pass":         all_pass,
        "section_9_vi_gate": "PASS" if all_pass else "FAIL",
        "per_item":         rows,
        "scope":            "build-realization only; not run-authorized",
    }
    args.summary_path.write_text(json.dumps(summary, indent=2) + "\n")
    print(f"items: {summary['n_items']}  pass: {summary['n_pass']}  fail: {summary['n_fail']}  "
          f"all_pass: {summary['all_pass']}  §9(vi): {summary['section_9_vi_gate']}")
    return 0 if all_pass else 1


if __name__ == "__main__":
    sys.exit(main())
