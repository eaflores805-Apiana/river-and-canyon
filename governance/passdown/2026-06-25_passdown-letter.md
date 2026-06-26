# Passdown Letter — 2026-06-25

**From:** CS Engineer (outgoing session)
**To:** Next CS Engineer (human or AI)
**Status:** Current as of 2026-06-25. Reflects: Paper 2 **v1.2 PUBLIC RELEASE** (tag `paper2-cells01-03-v1.2`, 2026-06-21); the full **V3 program lifecycle** run and closed (2026-06-15 → 2026-06-19); **Hop1 Stability Investigation** executed (HOP1-STABLE-INADMISSIBLE, 2026-06-19); and the **first bounded compression rung direction** issued by Manager (2026-06-21) — packet preparation authorized, run NOT authorized.

---

## How to use this letter

You have just landed in the project. Read this in full (~15 minutes), then go to §"Read next" for your first-day documents.

**This letter supersedes the 2026-06-10 passdown letter**, which is now ~15 days and several hundred commits stale and should NOT be used for current state. The 2026-06-10 letter predates the entire D4 calibration lifecycle, the repo reorganization, Paper A, the Tier-1 instrument architecture, the V3 lifecycle, Paper 2 v1.1/v1.2, and the compression-rung direction. It is preserved in `governance/passdown/` and in git history as an audit record only.

If anything here conflicts with what `git log` shows on `main`, **trust git** and ask Manager for a fresh status board. The repo is the source of truth; this letter is a point-in-time index into it.

---

## 1. Project in one paragraph

A behavioral stress-metrology program for LLMs. The metrology tower is released — Paper 1 (method, Final), Paper 2 (first result; **v1.2 public release 2026-06-21**), Paper 3 (certification protocol; v1.0 + v1.1 released 2026-06-10) — plus a lettered instrument paper, **Paper A — *Before Retention*** (released v1.0), and a parallel **Tier-1 instrument architecture** (`tier-1-instrument/`, spec + G6 module work). After the June-14 D4 PIVOT the program adopted **"instrument first, seam deferred"** (NORTH-STAR v1.2, method-as-basis reframe). The most recent active surface was the **V3 (same-depth-competitor) construction** under Path A, which ran a full floor-check → composite-gate lifecycle and closed at **PRECONDITION-FAIL**. As of 2026-06-21 Manager has directed opening the **first bounded compression rung** (FP16→INT8 as *instrument-validation-under-stress*) — **packet preparation only; no run authorized.** The single model throughout remains `Qwen/Qwen2.5-3B-Instruct`, revision `aa8e72537993ba99e69dfaafa59ed015b17504d1`, FP16, greedy, mlx_lm 0.31.3, M2 Max.

---

## 2. Current state — by lane

### Paper 1 — Survival Is Not Correctness
**Status:** Final. No active work. `papers/paper1-survival-is-not-correctness/`.

### Paper 2 — Correctness Is Not Constructibility
**Status:** **v1.2 PUBLIC RELEASE 2026-06-21.** Supersedes v1.0 as the released version; v1.0 tag preserved unchanged.
- Release commit: `34ef9215e8706f5a18288274be27678593dd2c01`
- New annotated tag: `paper2-cells01-03-v1.2` (tag object `82a24b7dbff12b2ca501a093182bf35858f22caf`; target commit `34ef9215…`)
- Released Markdown sha256: `7d6bd7f265ed908ed658279bb0dc090a096f981e8d7aa732ca1c93d43cb586c3` (git blob OID `21f10620d7445dfadcff5bc2fbf36f8f662e651e`)
- Released path: `papers/paper2-correctness-is-not-constructibility/correctness-is-not-constructibility.md`
- **v1.2 PDF** filed as a follow-on commit `cb977b54` (on `main` after the v1.2 tag, by design — PDF lives after the tag, not inside it).
- **Paper 2 v1.0 tag `paper2-cells01-03-v1.0` (`41c033fc…`; target `40c0cd5a…`; manuscript blob `7d6706a3…`) UNCHANGED** — not moved, re-pointed, or force-pushed. Verified at v1.2 release. **Never move it.**
- v1.2 content delta from v1.0: V3 integration + tightening/limitations (the §6/§9 hop2 single-lookup qualification language now lives here — see compression-rung lane below). Release records: `governance/2026-06-21_paper-2-v1.2-public-release/`.
- **Canonical snapshot + mlx_lm wording (do NOT flatten — carried from prior passdowns):**
  - snapshot: *"historically asserted in v1.0; subsequently corroborated by B1 runner-provenance-backed bit-identity reproduction; release-record addendum committed; Paper 2 tag/manuscript unchanged."*
  - mlx_lm: *"mlx_lm 0.19.3 → 0.31.3 was verified-null for the locked Paper 2 reproduction configuration … Version drift remains a provenance variable for any changed configuration."*

### Paper 3 — Certification Before Retention
**Status:** v1.0 + v1.1 both **RELEASED 2026-06-10**. No active manuscript work this period.
- v1.0 tag `paper3-certification-protocol-v1.0` (`6dbdcc12…`); v1.1 tag `paper3-certification-protocol-v1.1` (`0b63b2ef…`).
- Paper 3 is the certification *protocol*. Applying it (candidate selection, certification run) is still a separate downstream lane and remains **blocked** on a candidate-selection memo (not issued).

### Paper A — Before Retention (instrument paper)
**Status:** **RELEASED v1.0.** `papers/paper-a-before-retention/`. Lettered A/B dyad — NOT a 4th metrology paper. Packages the fail-closed validity gate that refused the D4/CAL-Q baseline and prevented a false refusal on CAL-E. Positioning section taken through external peer review (v0.7). Binding scope: one synthetic family, one model, pre-stress, no compression rung run; non-vacuousness claim *suggested* by two worked episodes, not *established* by a standing mechanism. **Paper B (stress paper) is a DEFERRED placeholder** (`paper-b/planning/`, empty by design) — requires separate authorization.

### Tier-1 instrument architecture
**Status:** Active parallel discipline. `tier-1-instrument/`. Eval-Validity Gate Tool Spec v0.1 (nine-gate architecture; G1–G5 implemented in Paper A, G6–G9 specified) + G6 Standing Rejection-Audit Spec v0.1, both CS-PASS. G6 module work has progressed to a first software evaluator (Case 1 missing-channel) which returned **AUDIT-CIRCULARITY**; Option B opened design-only by Manager. G6 build remains the standing model-free target. No certification claim attaches to any of it.

### Path A / V3 construction — the recent focal surface
**Status:** Full lifecycle run and **CLOSED at PRECONDITION-FAIL** (2026-06-18/19). Sequence:
1. **K-Sweep scout + FP16 constructibility run (2026-06-15):** Path A FP16 constructibility = **FAIL** (dominant-signature branch; FP16-only, Manager-authorized, no compression, no retry). K-sweep K=1..5 outcome **BOUNDARY** (best at K=1 edge; K=5 reproduces FAIL byte-exact). Cliff finding: admissible-load set = {K=1}; hop2-in-isolation INADMISSIBLE under competition on the existing construction; the ~40% off-map is the substrate ceiling for this construction. **K=5 FAIL stays closed.**
2. **V3 named** (Construction Property Taxonomy) as the conforming foreclose-all candidate. **Philosophy Decision Record v0.1 RATIFIED 2026-06-17:** FORECLOSE-ALL is the Path A gate standard; MAKE-IDENTITY-EASY rejected; V3 is the conforming *candidate vehicle*, **NOT certified**. Substrate-infeasibility is a valid outcome and never a license to loosen the standard.
3. **V3 floor-check run (2026-06-18):** §10 = **COMPONENT-ADMISSIBLE-UNDER-COMPETITION** (hop2 96/96, hop1 87/96 Wilson-lower 0.8313 > 0.75 floor, dq 0/96). Bounded as component-admissibility ONLY — NOT certification, capability, or mechanism.
4. **V3 composite-gate run (2026-06-18):** fresh disjoint seeds 097..192; §8 = **PRECONDITION-FAIL** (cond_c fails; gate not read). **hop1 swung 87/96 → 28/96** (Wilson-lower 0.2102 << 0.75) across the *same construction* at different per-item index ranges, with every other measured property identical. Mechanism NOT decidable from this run. Missing manifest filed 2026-06-19; lifecycle closed as a valid PRECONDITION-FAIL with full sha256 inventory. `experiments/2026-06-18_v3-composite-gate-run/`.

### Hop1 Stability Investigation
**Status:** **EXECUTED 2026-06-19 — HOP1-STABLE-INADMISSIBLE.** Authorized as its own pre-registered investigation (not licensed by the PRECONDITION-FAIL outcome alone) to probe *why* hop1 differed at 097..192 vs 001..096. Outcome on 6 fresh blocks: the P-role distractor reproduces 100% on fresh items → hop1 is stably **inadmissible** on this construction, not a seed artifact. `experiments/2026-06-19_hop1-stability-run/`. Finding report v0.1 in `path-a/in-review/HOP1-STABILITY-FINDING-REPORT-v0.1.md`. This fed the Paper 2 V3-delta / v1.2 integration.

### First bounded compression rung — THE LIVE EVENT
**Status:** **Manager DIRECTION issued 2026-06-21; CS ACKNOWLEDGED; standing by for Senior packet draft.** `governance/2026-06-21_first-compression-rung-direction/`.
- Manager directed: *open the first compression rung as instrument-validation-under-stress* — prepare `FIRST-COMPRESSION-RUNG-AUTHORIZATION-PACKET-v0.1`. **No run begins from this direction alone.**
- **This narrowly lifts the blanket compression block** for INT8 *packet-authoring scope only.* The INT8 run remains gated on the full chain: Senior draft → C5 claim-risk → CS feasibility → TL synthesis → **Manager by-name run authorization.** **INT4 stays blocked.** Seam/Claim C/composition/capability/mechanism, M5, V3 composite-gate retry, construction redesign — all stay blocked. Path A FP16 K=5 FAIL stays closed.
- Bounded interpretation perimeter (the ONLY question a run may answer): *"Can the fail-closed instrument produce a valid FP16-to-INT8 stress-retention readout on the selected qualified target?"*
- **Qualifying-target context (Senior to decide, CS does not pre-adjudicate):** Paper 2 v1.2 §6/§9 name single-hop retrieval (hop2) as the natural first candidate but bound it carefully — certifying hop2's own shortcut-freeness is a precondition for any stress rung on it. Senior's packet must either (a) argue hop2 is qualified enough for *instrument*-validation (vs capability) via the §6/§9 distinction, (b) specify a hop2-specific shortcut/position probe first, or (c) pick another already-prepared smoke-tested target.
- **Heads-up — this is NOT the first INT8 bytes ever touched.** Two prior INT8 touches exist and must not be confused with this rung: (1) **INT8-RUNG-1** ran 2026-06-13 in the D4 route ("RETENTION-PASS") and was **QUARANTINED** (Manager INT8-RUNG-1 classification, non-driving; `archive`/quarantine governance suite); (2) the **minimal FP16↔INT8 run** 2026-06-15 (`experiments/2026-06-15_minimal-fp16-int8-twohop-l1/`) was byte-identical 24/24 and **INCONCLUSIVE** per the pre-registered FP16-baseline gate, classified instrument-side. The June-21 direction is the first *properly-gated bounded* rung framed as instrument-validation-under-stress.

### D4 certification route
**Status:** **CLOSED by Manager PIVOT (2026-06-13).** Valuable negative result, not a rescue track. No candidate cleared full certification off-ceiling. CAL-Q converted to a **finding track** (`finding-tracks/cal-q-format-sensitive-abstention/`), explicitly not a D4 rescue. `archive/d4-closed-route/`. Safe-claim wording and six forbidden over-readings travel with it (see STATUS.md June-14 update; do not re-derive).

### Finding tracks (parked)
- **CAL-Q format-sensitive abstention** — `finding-tracks/cal-q-format-sensitive-abstention/`.
- **Terminal Attraction** — `finding-tracks/terminal-attraction/` (Senior finding report v0.4 + figures + PDF; from the 2026-06-15 bounds sweep). Parked, not abandoned.

### Standing governance discipline
- **Hash Integrity Is Not Construct Validity v0.7.2** — third project discipline (artifact/concept layer), released; `papers/standing-notes/`. Shown-semantic-read gate now required on every model-facing readiness packet. *Hashes bind bytes; they do not bind concepts.*
- NORTH-STAR v1.2, PROGRAM-MAP-v2.0, PROGRAM-CONTROL-LEDGER-v0.3, PROGRAM-POSITION — Senior/Manager-maintained authoritative trackers in `governance/standing/`. (`MAP.md` at root is the CS-maintained at-a-glance path view; this passdown updated it to rev 5.)

### Two-Hop L1 cells / tier0-run
**Status:** Sealed (Stage 0). Cells 01–03 complete, all NOT stress-eligible. **No new files in `tier0-run/`.**

---

## 3. What just happened (this period, 2026-06-11 → 2026-06-25)

In rough order: Lane 1a' D4 synthesis → **D4 calibration sweep (CAL-A..Q) → Manager PIVOT** closing D4 → **INT8-RUNG-1 run + quarantine** → **repo reorganization** (13-phase A–M move, all hash checks PASS, sealed bytes unchanged) → **Paper A released** + **Tier-1 instrument architecture + G6 module work** → **first authorized model runs** (minimal FP16↔INT8 INCONCLUSIVE; Terminal Attraction bounds sweep) → **Path A K-sweep + FP16 constructibility FAIL** → **Philosophy Decision (FORECLOSE-ALL)** → **V3 build → floor-check COMPONENT-ADMISSIBLE → composite-gate PRECONDITION-FAIL** → **Hop1 Stability HOP1-STABLE-INADMISSIBLE** → **Paper 2 V3-delta → v1.1-rc → v1.2 public release + PDF** → **Manager direction: open first bounded compression rung.**

Every CS filing in this period carried a §clean-fetch verification appendix (post-push remote-HEAD recompute from a clean fetch) per the filing-discipline standard. Working tree is clean and in sync with `origin/main` at filing.

---

## 4. What's pending for CS

**Active obligation (the live one):**
- **First-compression-rung packet.** Stand by for Senior to drop `FIRST-COMPRESSION-RUNG-AUTHORIZATION-PACKET-v0.1`. CS does **NOT** draft it (Senior's lane). When it lands: inbox-sweep → file byte-faithful (to `path-a/in-review/` or wherever the cover note directs) → run the standard CS feasibility/provenance review. Anticipated checks are enumerated verbatim in `governance/2026-06-21_first-compression-rung-direction/CS-ACK-FIRST-COMPRESSION-RUNG-DIRECTION-2026-06-21.md` §"Tooling/provenance posture" (target identity+path+sha256; FP16 baseline-gate status vs locked hashes; INT8 quantization library/version + deterministic step hash; scorer+validator hash recompute; mechanically-decidable pass/fail/**uninterpretable** branches; forbidden-interpretations completeness; pre-stated stop conditions; recompute path for every asserted hash). **No PASS without all items; return HOLD with a specific gap list otherwise.** CS does **not** execute the run, materialize/render items for execution, or load any quantization tooling until a separate Manager by-name run-authorization memo lands.

**Standing CS deliverables (event-triggered):**
- New paper revision → CS review (substantive: full review per `governance/standing/STANDING-REVIEW-DISCIPLINE.md`; editorial: short ack).
- New Team Lead status correction → CS correction report.
- Manager authorization for candidate selection → opens the Paper 3 application lane (currently blocked).

**Not pending; user-owned:**
- Root docs `STATUS.md`, `README.md`, `REVIEW.md`. Per standing instruction these are user-owned; **CS does not commit them without explicit Manager delegation.** (`MAP.md` is CS-maintained — see rev 5.) As of this passdown, STATUS.md is current through its 2026-06-14 update and is behind the V3 lifecycle / Paper 2 v1.2 / compression-rung events; flag to Manager if a refresh is wanted.

---

## 5. What's blocked

Read `governance/standing/STANDING-NON-AUTHORIZATIONS.md` in full (updated this session to reflect the compression-rung lift). Headlines:

- **INT8 execution** — *narrowly lifted for packet-authoring only* (2026-06-21 Manager direction). The run itself stays blocked pending Manager by-name authorization at the end of the full review chain.
- **INT4 execution** — blocked.
- **Candidate selection / threshold values / certification evaluation** — blocked; Manager-gated; no candidate-selection memo issued.
- **Seam / Claim C / composition / capability / mechanism claims** — blocked across all metrology work.
- **M5 distractor-attractiveness experiment** — blocked.
- **V3 composite-gate retry** — blocked.
- **Construction redesign** — blocked.
- **Path A FP16 K=5 FAIL** — stays closed.
- **D4 route** — closed (Manager-only to reopen).
- **New model runs / multi-model** — blocked beyond authorized instrument-side work; single-model scope.
- **Public benchmark packaging** — open team-discussion item; not authorized.

Protected surfaces: Paper 2 v1.0 tag (`41c033fc…`, blob `7d6706a3…`), Paper 2 v1.2 tag (`82a24b7d…` → `34ef9215…`), Paper 3 v1.0/v1.1 tags, `tier0-run/` (sealed, no new files), and the four sealed-byte files under `experiments/2026-06-11_lane-1a-prime/validation/` + `experiments/2026-06-10_lane-1a-sweep/LOCK-RECORD.md`.

---

## 6. Open questions / decisions awaiting actors

| Question | Owner | Status |
|---|---|---|
| First-compression-rung authorization packet (v0.1 draft) | Senior | **Open** — directed 2026-06-21; not yet delivered as of 2026-06-25 |
| First-compression-rung **run** by-name authorization | Manager | Open; gated on packet → C5 → CS → TL chain |
| hop1 097..192-vs-001..096 mechanism | (recorded, not licensed) | Hop1 Stability returned HOP1-STABLE-INADMISSIBLE; mechanism not claimed; further probing would need its own authorization |
| Paper 3 candidate-selection memo | Manager | Open; no deadline |
| Whether to refresh user-owned root docs (STATUS/README/REVIEW) | Manager/User | Open; CS holds unless delegated |
| Scaling / tooling posture (tool vs instrument) | Team discussion | Filed 2026-06-09; not yet held |

---

## 7. Read next (first-day documents)

1. **`_meta/ONBOARDING-CS.md`** — role/scope/conventions. (Stable; still accurate.)
2. **`governance/standing/STANDING-NON-AUTHORIZATIONS.md`** — boundary rules (updated this session for the INT8 lift).
3. **`governance/standing/STANDING-REVIEW-DISCIPLINE.md`** — failure-mode review prompt + protection-layer taxonomy.
4. **`governance/2026-06-21_first-compression-rung-direction/`** — both files: Manager direction + CS ack (the live lane).
5. **`MAP.md`** (root, rev 5) — at-a-glance path view of the whole program.
6. **`governance/2026-06-21_paper-2-v1.2-public-release/`** — what just released.

Then browse: `STATUS.md` (project narrative through 2026-06-14; behind on the V3/v1.2/rung events but the best prose overview); `governance/standing/PROGRAM-CONTROL-LEDGER-v0.3.md` (per-route detail); the V3 run dirs under `experiments/2026-06-18_*` and `experiments/2026-06-19_*`.

---

## 8. Things that have bitten CS (so you can avoid them)

- **Trusting a stale passdown.** This very letter exists because the 2026-06-10 one was trusted-as-current 15 days too long. Cross-check the passdown date against `git log` before relying on it.
- **"Retired" wording on Paper 2 snapshot or mlx_lm.** Use the canonical phrasings in §2 verbatim.
- **Confusing the June-21 rung with INT8-RUNG-1 or the June-15 minimal run.** Three distinct INT8 touches; only the June-21 one is the gated instrument-validation rung, and even it is packet-authoring-only until by-name run authorization.
- **Treating the compression-block lift as general.** It is INT8, packet-authoring, single-target, fail-closed only. INT4 and everything else stay blocked.
- **Modifying `tier0-run/` or moving any tag.** Sealed / frozen. Documentation updates to existing tier0 files only; no new files; no tag moves.
- **Inferring authorization from absence.** Infer blockage from absence; escalate.
- **Filing what isn't on disk.** Delivery is a confirmed commit SHA at the intended path, not a SEND-TO-CS marker. Every CS return reports post-push remote HEAD from a clean fetch before claiming FILED.
- **Committing root docs (STATUS/README/REVIEW) without explicit Manager delegation.** User-owned. `MAP.md` is the exception (CS-maintained).
- **Rewriting git history.** Don't. File superseding commits.

---

## 9. Final state at filing

```
Branch:  main
HEAD:    3b336c69  governance: file Manager direction to open first bounded compression rung + CS acknowledgment
         (this passdown + standing-card + MAP rev-5 commit will land at HEAD after filing)
Working tree: clean; in sync with origin/main at clone.

Tags:    paper2-cells01-03-v1.0              (41c033fc; Paper 2 v1.0 frozen — never move)
         paper2-cells01-03-v1.2              (82a24b7d → 34ef9215; Paper 2 v1.2 public release)
         paper3-certification-protocol-v1.0  (6dbdcc12)
         paper3-certification-protocol-v1.1  (0b63b2ef)
         synthesis-cells01-03-pass4          (c6e8d1c6; Cells01-03 evidence)

Branches: main; origin/b1-harness-v2 (ff8466b2, B1 v2 harness — merged/locked to main history)
```

CS holding for: Senior first-compression-rung packet (no deadline stated). All recent CS deliverables filed and pushed; clean-fetch verified.

---

— CS Engineer, 2026-06-25
