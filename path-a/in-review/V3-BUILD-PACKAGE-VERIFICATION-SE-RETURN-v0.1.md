# V3 BUILD-PACKAGE VERIFICATION — SE RETURN

**To:** Team Lead **Cc:** CS Engineer **From:** Senior Engineer **Re:** TL ACTION 2026-06-17 (Verify V3 Build Open Slots)
**E. A. Flores**, Apiana AI, Inc. — June 17, 2026 · *Verification only (YELLOW). No run. Certifies nothing.*

## VERDICT: **PASS**

V3 build verified from bytes — the generator realizes the V3 construction, all four open slots are realized in code and artifacts, the demonstration batch is genuinely conformance-checkable, the conformance run reproduces 8/8 PASS independently, and the generator is deterministic. No model run, prompt-for-model generation, or hidden authorization occurred. **Ready for the V3 floor-check prereg draft** (which is itself separately gated, §recommendation).

## Method note

Verified against a fresh `git clone` at HEAD `703b3a3` (GitHub API was rate-limited; clone + raw unaffected). Reproductions were **executed**, not read: the conformance runner and the generator were run in the cloned tree.

## 1. Exact files inspected (HEAD `703b3a3`)

```text
path-a/build/v3_item_generator.py         path-a/build/v3_token_pool.md
path-a/build/v3_conformance_runner.py     path-a/build/v3_direct_query_filler.md
path-a/build/README.md                    path-a/build/v3_relation_balance.md
path-a/build/conformance_summary.json     path-a/build/v3_seed_plan.md
path-a/build/items/item_001..008.json (8)
path-a/build/conformance/item_001..008_inspection.json (8)
path-a/inspector/inspector.py  +  path-a/inspector/constants.py   (the instrument under test)
path-a/in-review/PATH-A-CANDIDATE-CONSTRUCTION-DESIGN-v0.3.md     (design realized against)
```

## 2. Hashes recomputed (SE, from clone at HEAD `703b3a3`)

```text
v3_item_generator.py       6a2ceee15442ebbd…
v3_conformance_runner.py   2a4408353e3713e3…
v3_token_pool.md           d5f3594ce42a9e55…
v3_direct_query_filler.md  7ff83ab82de13c7d…
v3_relation_balance.md     de45d2a9bb640177…
v3_seed_plan.md            f501f741f47faafd…
conformance_summary.json   9280986a937aa378…
inspector.py (under test)  cb4b0b60bd6dc2b5…   ← matches the v0.4 re-pin
constants.py (under test)  1d761c3d1c56e7ac…   ← matches the v0.4 re-pin
```

The build was conformance-checked against the **re-pinned (v0.4) instrument** — the inspector/constants digests under test equal the values Manager/TL re-locked of-record. Correct instrument.

## 3. Commands run

```text
git clone … && git checkout 703b3a3
python3 path-a/build/v3_conformance_runner.py --items-dir path-a/build/items \
   --results-dir /tmp/repro_conf --inspector-path path-a/inspector/inspector.py \
   --summary-path /tmp/repro_summary.json
python3 path-a/build/v3_item_generator.py --out-dir /tmp/gen_a --count 8     (twice: gen_a, gen_b)
sha256sum / diff / field-level JSON compare
```

## 4. Task-by-task findings

**(1) Generator realizes V3 per design v0.3 — VERIFIED.** The construction logic is in code, not merely described:

```text
_make_depth_2_competitors(prefix, D):  D=5 same-depth competitors at the head, each a DISTINCT
                                        relation (the V3 same-depth-competitor topology — depth/
                                        position/salience all score 1/D, only relation-following selects C*)
_make_relation_balance(prefix, D):      head relations at order-position 0, tail at 1, balanced
                                        frequency + role-grouped order (the E8 relation-balancing the
                                        inspector's C6 checks)
_make_direct_query(seed):               neutral, length-matched filler containing neither B nor C*
                                        (the E5 direct-query control)
_make_decoy_chains:                     k=5 chain-level decoy clutter
```

**(2) Four open slots realized in code + artifacts — VERIFIED.**

```text
slot 1  item generator + seed   v3_item_generator.py + seed=item-index, position=((N-1) mod p)+1, v3_seed_plan.md
slot 2  token pool              per-item prefix `i{NNN}_` + role-letter convention in code; v3_token_pool.md (4061B)
slot 3  direct-query filler     _make_direct_query + _FILLER_FORMS rotation; v3_direct_query_filler.md (4285B)
slot 4  relation balancing      _make_relation_balance; v3_relation_balance.md (6318B)
```

**(3) Demonstration batch genuinely conformance-checkable — VERIFIED.** The 8 items are JSON construction specs (schema-level, the form the inspector consumes). The inspector ran against all 8 and produced per-item dispositions — i.e., they are real inputs to the gate, not decorative.

**(4) Conformance runner reproduces 8/8 PASS, 9/9 checks, real-run — VERIFIED BY EXECUTION.** I ran the runner into a temp dir: **8 items, 8 PASS, 0 reject, all_pass=True, 9/9 checks per item, real-run mode on every item** (all 8 committed inspections also carry real-run mode). Construction IDs encode seed+position (`item_001_pos1_seed001` … `item_008_pos8_seed008`).

**(5) Generator deterministic — VERIFIED.** Two independent runs with identical args (`--count 8`) are **byte-identical (8/8)**; and the regenerated items are **byte-identical to the committed items (8/8)** — so the committed batch is exactly what the generator produces. *(Self-correction logged: my first determinism attempt used `--n` (the generator takes `--count`); it errored into empty dirs and would have produced a vacuous "identical" of two empty sets — caught and redone with the correct arg, real counts printed.)*

**(6) Build honors v0.4 locked values — VERIFIED.** In code: `LOCKED_K=5, LOCKED_D=5, LOCKED_P=5, LOCKED_M=10, LOCKED_MARGIN=0.25`, with an import-time assertion that the competitor-relation pool ≥ D. In a generated item (`item_001`): `params {k:5, D:5, p:5, m:10, margin:0.25}`, with exactly 5 depth_2_competitors and no `_fixture_mode`/`_sweep_mode` (→ real-run). F=0.20 and success threshold=0.45 are enforced by the inspector (constants under test `1d761c3d…`), which all 8 items pass.

**(7) No hidden run / prompt-for-model / model execution — VERIFIED.** No `torch`/`mlx`/`transformers`/`openai`/`anthropic`/network imports anywhere in the generator or runner. The **only** subprocess use is the runner invoking `inspector.py` as a CLI — a schema-level admissibility check, not a model. The generator produces construction specs only and writes no prompt strings (its docstring states this and the code bears it out).

## 5. Mismatch / blocker

```text
ONE field differs between committed and SE-reproduced inspections, and it is fully explained:
  - timestamp_utc: committed 2026-06-18T06:38:23Z vs SE-repro 2026-06-18T06:50:16Z
  - This is 1 of 52 leaf fields. ALL other fields — every disposition, all 9 checks, params,
    construction_id, mode (real-run) — are BYTE-IDENTICAL. The diff is wall-clock only and does
    not touch the conformance verdict.
NO substantive mismatch. NO blocker.
```

## 6. What this PASS does and does NOT mean (containment)

```text
- "Conformance PASS" = the 8 generated items pass the inspector's C1–C9 ADMISSIBILITY gate in
  real-run mode — i.e., they are well-formed V3 construction specs satisfying the foreclose-all
  structural requirements. It is a property of the CONSTRUCTION ARTIFACTS, not of any model.
- It does NOT mean V3 has been tested against a model; does NOT mean hop2 clears its floor under
  competition; does NOT certify V3; makes NO capability or mechanism claim. The floor check remains
  the open empirical question, and substrate-infeasibility remains a valid future outcome.
- The items are SCHEMA-LEVEL SPECS, not prompts. A prompt-realization layer (specs -> concrete
  prompts for the four contexts) would be separately gated by Manager by-name authorization; it is
  NOT part of this build and was NOT performed.
- The batch is 8 DEMONSTRATION items, not the full N=96. The generator's prefix scheme generalizes
  to N=96 without schema change, but only 8 are built/checked; full materialization is gated.
```

## 7. Recommendation

**Yes — recommend drafting the V3 floor-check prereg next.** The build clears the "build open slots" gate: the construction is realized, deterministic, conformance-checkable, and conformant under the re-pinned instrument. The floor check (does hop2 clear its floor under competition on V3?) is the correct next step — and it remains fully gated:

```text
SE drafts V3 floor-check prereg  ->  CS feasibility  ->  C5 claim-risk  ->  TL approve
   ->  Manager by-name authorization  ->  CS run  ->  SE verification
```

I can draft the floor-check prereg (lock-before-look: pre-declared floor question, metric, null, decision rule, and the substrate-infeasibility branch) on your word. Drafting it authorizes no run.

## 8. Boundary

```text
- Verification only (YELLOW). No model run, no floor-check run, no compression, no certification,
  no Claim C, no Paper B, no capability claim, no mechanism claim.
- The Path A FP16 K=5 FAIL remains closed and untouched.
- SE verifies; SE authorizes nothing. The floor-check prereg, if drafted, routes for approval and
  Manager by-name authorization before any run.
```

— Senior Engineer (build verification; PASS)
