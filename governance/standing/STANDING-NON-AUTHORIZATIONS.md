# Standing Non-Authorizations — Quick Card

*Canonical list of lanes that are blocked across the program. Every CS memo, every governance filing, and every implementation decision must respect this list. Items move OFF this list only by explicit Manager authorization filed in `governance/`.*

**Last reviewed:** 2026-06-25
**Status:** All items below remain in force except where explicitly noted.

**Recent partial movement (do NOT generalize):**
- **First compression rung — INT8: EXECUTED and CLOSED (2026-06-26).** The 2026-06-21 packet-authoring lift was used: the Manager authorized (by name) a light **INT8 control/calibration rung** (`ONE-PAGE-INT8-CONTROL-RUNG-SPEC-v0.1`, superseding the heavier five-gate packet for this rung). CS executed it (`experiments/2026-06-26_first-compression-rung/`, commit `b766f9aa`): FP16=INT8=hop1 0/8, hop2 8/8, composite 1/8; **byte-identity 24/24** → null-stress instrument validation only (no retention / capability / composition / Claim-C claim). **TL disposition: CLOSED, PASS as control/calibration rung** (CS-verified, SE-verified, C5-observed). **The packet-authoring lift is now SPENT.** Per TL 2026-06-26, **all further INT8 work is CLOSED — no rerun, no second control, no packet revival.** **Compression (INT8 and INT4) is BLOCKED again until FP16 constructibility clears.** Forward rule (C5/TL): any non-null future rung — INT4, or any case where INT8 ≠ FP16 — must **restore independent claim-risk review** (full five-gate chain) before any readout is filed; the light path is reserved for null-stress controls only. Distinct prior INT8 touches (do not generalize): INT8-RUNG-1 (2026-06-13, **QUARANTINED**) and the minimal FP16↔INT8 run (2026-06-15, **INCONCLUSIVE**).
- **Lane 1a (pre-candidate occupancy / failure-map sweep)** — *historical: now CLOSED.* Was moved to PACKET PREPARATION AUTHORIZED per `governance/2026-06-10_lane-1a-authorization/MANAGER-AUTHORIZATION.md`; the Lane 1a' / Path A (rung-uniform) execution ran and **CLOSED 2026-06-12** ("breadth untested under the sealed schedule"). Negative-use-only doctrine ("may rule out; may not rule in") stands for any future reconnaissance lane; Lane 1a itself is no longer an open movement.

---

## The list, with reasons

Each item is "what's blocked" and "why it's blocked." A new CS should read this card before doing anything substantive, and re-read it any time scope is unclear.

| Blocked lane | Why it's blocked |
|---|---|
| **candidate selection** | Paper 3 candidate-selection memo has not been issued. No certification attempt can proceed without it. Manager-gated. |
| **threshold values** | Per Paper 3 §7, thresholds must be pre-registered before any candidate evaluation; no post-hoc tuning permitted. Locking values before candidate selection is the wrong order. |
| **certification evaluation** | Requires both candidate selection AND a locked, hash-verified threshold sheet. Neither exists. |
| **new model runs** | All work to date uses one model (`Qwen/Qwen2.5-3B-Instruct`, snapshot `aa8e7253...`). Any new model run requires fresh authorization. |
| **re-runs beyond authorized reproduction validation** | Paper 2 reproduction (`paper2_regression.py`) is the only authorized validity-check rerun. Anything else needs new authorization. |
| **unconditioned token-prior runs** | D1 token-prior control may require a preflight run; that run is **not** pre-authorized by Paper 3 — it requires separate Manager authorization at candidate-selection time. |
| **activation logging** | Activation-outlier telemetry was classified as stress-side validation, not baseline certification. Beyond B1 v2 scope. Requires harness extension and separate authorization. |
| **INT8 execution** | **BLOCKED again (2026-06-26).** The one authorized INT8 control rung executed and CLOSED (commit `b766f9aa`); the 2026-06-21 packet-authoring lift is SPENT. Per TL 2026-06-26: no rerun, no second control, no packet revival. Any new INT8 work requires fresh Manager authorization AND, if non-null (INT8 ≠ FP16 anticipated), the full five-gate claim-risk chain — not the light control path. INT8-RUNG-1 (2026-06-13) remains QUARANTINED. |
| **INT4 execution** | Stress runs. **Fully blocked** — never covered by the 2026-06-21 INT8 lift. Any INT4 rung is non-null by expectation, so it requires the full five-gate claim-risk chain + separate Manager authorization. |
| **compression generally** | **BLOCKED until FP16 constructibility clears** (TL 2026-06-26). The pivot is back to building a composition baseline valid enough to stress; no compression rung proceeds on an unqualified baseline. |
| **multi-model execution** | Single-model is the program's current scope. Multi-model is part of the scaling discussion item (filed 2026-06-09); not authorized. |
| **Fork A reactivation** | Fork A artifacts fail the reactivation bar (provenance below B1 standard; result files have empty `provenance: {}` blocks). Cannot be admitted as live evidence regardless of figures. |
| **Claim C activation** | The seam/linkage claim. Compositional-seam existence is the program's deliberately blocked claim. Stays blocked across all metrology work, including Paper 3 certification. |
| **Paper 3 execution as an experiment** | Paper 3 is a methods/protocol paper. Applying the protocol (selecting a candidate, running certification) is a separate downstream paper requiring separate authorization. |
| **Paper 6 activation** | Paper 6 is not in active scope. Listed as a backstop against premature scope expansion. |
| **public benchmark packaging** | Tooling and distribution posture is an open team-discussion item (`governance/2026-06-09_scaling-discussion-item/`). Not authorized as a deliverable. |
| **artifact mutation** | Locked artifacts (manifests, scorers, runners, result JSONs, tagged manuscripts, locked threshold sheets) must not be edited in place. Any change creates a new artifact with a new hash; corrections file as superseding commits, not history rewrites. |

---

## Two specific protected surfaces

These are not "lanes" but bounded artifacts that must not be touched:

- **Paper 2 v1.0 tag (`paper2-cells01-03-v1.0`, SHA `41c033fc...`) and the tagged manuscript blob (`7d6706a3...`).** Tag is frozen; manuscript blob is preserved in the tag. Verified UNCHANGED at the v1.2 release (2026-06-21). The tag itself never moves. The on-main `papers/paper2-correctness-is-not-constructibility/correctness-is-not-constructibility.md` is now the **v1.2** released body (sha256 `7d6bd7f2…`); post-tag content evolution on main is OK — the v1.0 *tag* never moves.
- **Paper 2 v1.2 tag (`paper2-cells01-03-v1.2`, tag object `82a24b7d...` → target commit `34ef9215...`).** New released version 2026-06-21. Tag frozen; v1.2 PDF lives in follow-on commit `cb977b54` after the tag by design.
- **Paper 3 v1.0 / v1.1 tags (`paper3-certification-protocol-v1.0` `6dbdcc12...`; `…-v1.1` `0b63b2ef...`).** Frozen.
- **`tier0-run/` directory.** Sealed as of Paper 2 v1.0 freeze. Documentation updates to existing files (PROJECT_BRIEFING.md, EXPERIMENT_LOG.md, governance INDEX.md) are permitted; **no new files** may be added.
- **Four sealed-byte files** under `experiments/2026-06-11_lane-1a-prime/validation/` and `experiments/2026-06-10_lane-1a-sweep/LOCK-RECORD.md`. Do not move or modify.

---

## What's required to move an item OFF this list

A Manager memo, filed in `governance/<YYYY-MM-DD>_<lane-name>-authorization/`, containing:
- The specific lane being authorized
- The scope of authorization (what may now be done; what still cannot)
- The required reporting back to Manager
- Any new boundaries that come with the authorization

Until that memo exists in `governance/`, the lane is blocked. CS does not infer authorization from absence; CS infers blockage from absence.

---

## How CS uses this card

- Quote the relevant subset verbatim at the bottom of every governance memo, under a `## Non-authorizations` heading.
- Read this card before starting any work that touches scope.
- If a request would require moving an item off this list, do not start the work — file a clarification or escalation memo first.

---

— CS Engineer, 2026-06-10 (last revised 2026-06-26: INT8 control rung EXECUTED + CLOSED, lift spent, all further INT8 closed, compression re-blocked pending FP16 constructibility, non-null-rung→full-claim-risk rule recorded. Prior 2026-06-25 revision: INT8 packet-authoring lift; INT8/INT4 split; Paper 2 v1.2 + Paper 3 tags protected; Lane 1a closed)
