# Standing Non-Authorizations — Quick Card

*Canonical list of lanes that are blocked across the program. Every CS memo, every governance filing, and every implementation decision must respect this list. Items move OFF this list only by explicit Manager authorization filed in `governance/`.*

**Last reviewed:** 2026-06-25
**Status:** All items below remain in force except where explicitly noted.

**Recent partial movement (do NOT generalize):**
- **First compression rung — INT8 (2026-06-21).** Per `governance/2026-06-21_first-compression-rung-direction/MANAGER-DIRECTION-OPEN-FIRST-BOUNDED-COMPRESSION-RUNG-2026-06-21.md`, the blanket compression block is **narrowly LIFTED for INT8 authorization-packet authoring only**, on a single qualified target, framed as *instrument-validation-under-stress*. **The INT8 run itself remains NOT AUTHORIZED** until `FIRST-COMPRESSION-RUNG-AUTHORIZATION-PACKET-v0.1` passes the full chain (Senior draft → C5 claim-risk → CS feasibility → Team Lead synthesis → **Manager by-name run authorization**). **INT4 stays fully blocked.** The bounded interpretation perimeter is *"Can the fail-closed instrument produce a valid FP16-to-INT8 stress-retention readout on the selected qualified target?"* — and nothing else (no seam / Claim C / composition / capability / mechanism). If the FP16 baseline is not qualified, the run must fail closed before any INT8 interpretation. Two prior INT8 touches are distinct and do NOT generalize the lift: INT8-RUNG-1 (2026-06-13, **QUARANTINED**, non-driving) and the minimal FP16↔INT8 run (2026-06-15, **INCONCLUSIVE** per FP16-baseline gate, instrument-side).
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
| **INT8 execution** | Stress runs. Blanket block **narrowly LIFTED 2026-06-21 for authorization-packet authoring only** (see "Recent partial movement" above). The INT8 *run* stays blocked until the packet clears the full review chain and Manager gives by-name run authorization. INT8-RUNG-1 (2026-06-13) is QUARANTINED and non-driving. |
| **INT4 execution** | Stress runs. **Fully blocked** — not covered by the 2026-06-21 INT8 packet-authoring lift. Requires separate Manager authorization. |
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

— CS Engineer, 2026-06-10 (last revised 2026-06-25: INT8 packet-authoring lift recorded; INT8/INT4 split; Paper 2 v1.2 + Paper 3 tags added to protected surfaces; Lane 1a marked closed)
