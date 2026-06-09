# Instrument Standardization Scoping Memo

**Filed:** 2026-06-09  
**Prepared by:** CS Engineer  
**Audience:** Manager, Team Lead  
**Status:** DRAFT — for management review and authorization decisions  
**Purpose:** Scope the path from current fragmented per-cell runner architecture to a general, reusable test tool capable of running any cell, model, and precision level under a single standardized instrument.

---

## §1 The Problem

The current runner architecture grew incrementally: each cell produced a new runner file by amending the previous one. The result is three runner files (`runner_twohop_l1.py`, `runner_twohop_l1_cell02.py`, `runner_twohop_l1_cell03.py`) that share roughly 90% of their code but are maintained independently. Each amendment introduced provenance drift: the Cell03 runner has §8 diagnostics and an updated mlx_lm API that the Cell01 runner does not, and none of the three runners write the full provenance fields that B1 requires.

This is manageable at three cells. It becomes a material liability at ten cells across three precision levels, because:

- A fix or improvement must be applied separately to every runner file
- Each runner file requires its own hash constant and amendment lock note
- Cross-cell comparison requires verifying that all runners behaved equivalently, which is harder when they are structurally different
- Onboarding a new team member requires reading three files instead of one

The end goal — a test tool that can sweep any cell, model, and precision level under a single provenance-locked instrument — requires resolving this now, while the architecture is still small enough to change cleanly.

---

## §2 The End Goal

A single parameterized test tool with the following properties:

- Accepts a **cell config** (manifest path, axis description, gate thresholds, expected hashes) as input
- Accepts a **model config** (model ID, precision level, model directory, optional FP16 reference file for stress comparison) as input
- Writes a **fully provenance-locked result JSON** conforming to a single schema regardless of cell or model
- Evaluates all gates at runtime and writes `gate_summary` and `stress_eligible` to the output
- Blocks stress runs at runtime if the cell has not cleared Gate 2 at FP16
- Supports both FP16 baseline runs and INT8/INT4 stress runs under the same code path
- Produces per-item same-error identity fields for every run (FP16 self-reference for base runs; FP16-vs-stressed comparison for stress runs)
- Passes a standard acceptance test suite (AT-1 through AT-8, see `PAPER2-REPRODUCTION-ACCEPTANCE-TEST-PLAN.md`) after any change

This is not a novel research instrument. It is engineering infrastructure that makes the existing instrument reliable and scalable.

---

## §3 Build Order

The five stages below are sequenced so that each stage delivers usable value on its own and unblocks the next. No stage requires science decisions — all gate thresholds, scoring axes, and cell designs remain controlled by the normal authorization process.

---

### Stage 1 — B1 Runner (foundation)

**What it is:** Amend `runner_twohop_l1_cell03.py` to add the missing provenance fields and output structure identified in `B1-IMPLEMENTATION-PLAN.md`.

**New fields added:**
- Provenance: `mlx_lm_version`, `python_version`, `model_snapshot_hash`, `precision_rung`
- Output: `gate_summary`, `stress_eligible`
- Per-item: `same_error_identity_key`, `fp16_raw_output`, `exact_output_match`
- Runtime fail-closed Gate 2 block

**What it does not change:** Scorer, manifests, failure taxonomy, gate thresholds, existing result JSONs.

**Unblocks:** Paper 2 reproduction acceptance test; future cell runs on a consistent output schema.

**Authorization needed:** Manager confirmation that "bounded validity-hardening" (Team Update 2026-06-09) covers runner code changes.

**Effort:** ~1–2 days. 10 unit tests. Dry-run required before any live run.

---

### Stage 2 — Cell Config Abstraction

**What it is:** Refactor the B1 runner so that all cell-specific constants (ITEMS_PATH, AXIS_CONFIGURATION, EXPECTED_SCORER_HASH, EXPECTED_MANIFEST_HASH, gate thresholds) are passed in as a config dict or config file rather than hardcoded. The runner code itself becomes cell-agnostic.

**Result:** One runner file handles Cell01, Cell02, Cell03, and all future cells. Per-cell configs are small, auditable, version-controlled files. A fix to the runner propagates to all cells automatically.

**What it does not change:** Scorer, manifests, cell designs, gate thresholds (they move from runner constants to config files, not changed in value).

**Cell01/02/03 runner disposition:** The three existing runner files are frozen as-is — their hashes remain embedded in the original result JSONs as the provenance record of what produced those outputs. The B1/Stage 2 runner is used for reproduction runs and all future cells. No re-run of Cell01/02/03 is required by this stage; re-runs are covered by the reproduction acceptance test process.

**Unblocks:** Multi-cell execution without new runner files; cleaner onboarding; Stage 3.

**Effort:** ~2–3 days. Requires regression test: Stage 2 runner on Cell03 manifest must reproduce Cell03 Stage 1 output exactly (all AT tests pass).

**Authorization needed:** Manager approval to proceed with Stage 2 after Stage 1 acceptance test passes.

---

### Stage 3 — Automated Acceptance Test Script

**What it is:** Implement AT-1 through AT-8 (from `PAPER2-REPRODUCTION-ACCEPTANCE-TEST-PLAN.md`) as a runnable Python script. Takes a result JSON as input, checks all acceptance criteria, outputs a pass/fail report.

**Result:** Acceptance testing goes from a manual checklist to a one-command verification. Any new run or runner change can be validated in seconds.

**Unblocks:** Reliable regression testing for all future runner changes; Stage 4 batch execution (automated routing requires automated evaluation).

**Effort:** ~1 day. No new authorization required — this is a test utility, not a run.

---

### Stage 4 — Multi-Model Parameterization

**What it is:** Extend the Stage 2 runner to accept MODEL_ID and precision level as runtime arguments. Add model manifest hash gating for any model directory passed in. Add FP16-reference comparison logic (currently only in Fork A stress runner) to the standard runner, so that any stress run can compare against a declared FP16 reference.

**Result:** Running Cell03 at INT8 requires passing `--model Qwen2.5-3B-Instruct --bits 8 --fp16-ref cell03_fp16_result.json` rather than a separate runner file. All provenance, gate evaluation, and same-error identity logic is identical to the FP16 path.

**Critical prerequisite:** This stage is only useful once a cell has cleared Gate 2 at FP16 and been declared stress-eligible. Building Stage 4 before Track A produces a stress-eligible cell is building infrastructure with no workload to drive it.

**Unblocks:** Track B (synthetic two-step linkage under compression); any multi-precision sweep.

**Effort:** ~2–3 days after Stage 2 is stable. Requires Manager authorization per the stress-eligibility gate process — Stage 4 existing does not itself authorize stress runs.

---

### Stage 5 — Batch Execution and Routing

**What it is:** A sweep controller that takes a list of (cell config, model config, precision) combinations, runs them in sequence, evaluates gates after each run, and produces a routing summary: which cells are stress-eligible, which are Branch 3, which hit unexpected failure modes.

**Result:** A full constructibility boundary sweep across cells and model sizes can be run as a single authorized job. The routing summary feeds directly into the Claim B map update process.

**Critical prerequisite:** At least one stress-eligible cell from Track A. Without a stress-eligible cell, a batch executor has no meaningful workload.

**Unblocks:** Track A at scale; systematic Claim B boundary mapping.

**Effort:** ~3–5 days. Requires careful design of the authorization check — the controller must not initiate stress runs on cells that have not been explicitly declared stress-eligible by the gate process.

---

## §4 Summary Table

| Stage | Description | Effort | Prerequisite | Unblocks |
|---|---|---|---|---|
| 1 — B1 Runner | Add provenance fields, gate_summary, fail-closed block | 1–2 days | Manager authorization | Paper 2 reproduction; consistent output schema |
| 2 — Cell Config Abstraction | Single runner, cell-specific config files | 2–3 days | Stage 1 accepted | Multi-cell without new runner files |
| 3 — Acceptance Test Script | AT-1–AT-8 as runnable script | 1 day | Stage 1 complete | Automated regression for all future changes |
| 4 — Multi-Model Parameterization | MODEL_ID + precision as runtime args | 2–3 days | Stage 2 + stress-eligible cell | Track B; multi-precision sweeps |
| 5 — Batch Execution | Sweep controller + routing summary | 3–5 days | Stage 4 + stress-eligible cell | Track A at scale; Claim B mapping |

**Total effort (Stages 1–3, foundation):** ~4–6 days  
**Total effort (Stages 4–5, full tool):** +5–8 days, gated on Track A outcome

---

## §5 Key Decision Points for Management

**Decision 1 (immediate):** Authorize Stages 1–3 as a bounded backfill project. This is pure infrastructure hardening with no science decisions. Recommended: YES — needed for Paper 2 reproduction regardless.

**Decision 2 (after Track A produces a result):** Authorize Stages 4–5 based on whether the constructibility boundary map requires multi-model and multi-precision sweeps. If Track A produces a stress-eligible cell, Stage 4 becomes the priority. If Track A produces more Branch 3 cells, the priority shifts to cell design iteration and Stages 4–5 wait.

**Decision 3 (not yet actionable):** Whether the general test tool eventually needs to support task families beyond the current two-hop L1 construction (e.g., three-hop, different relation types, different context lengths). This would require scorer extension and is a research decision, not an engineering decision. Not in scope for Stages 1–5.

---

## §6 What This Does Not Change

- Gate thresholds and authorization process — unchanged
- Scorer — not amended under this plan
- Cell designs, manifests — not amended
- Existing result JSONs — not rewritten
- Science decisions (what to test, what claims to make) — remain with Manager and Team Lead

The standardization plan is exclusively an engineering infrastructure decision.

---

— CS Engineer, 2026-06-09
