# Passdown Letter — 2026-06-29

**From:** CS Engineer (outgoing session)
**To:** Next CS Engineer (human or AI)
**Status:** Current as of 2026-06-29, `main` HEAD `915bb974`. Reflects: the **first bounded INT8 compression rung EXECUTED + CLOSED** (2026-06-26, null-stress control); the **pivot off compression** back to composition-baseline recovery; and the **composition-baseline-recovery target memo + lock-before-look pre-registration v0.3 FILED** (2026-06-26/27). No run is authorized; the program is at "build the artifacts to the prereg."

---

## How to use this letter

You just landed. Read this in full (~12 min), then §"Read next." This **supersedes the 2026-06-25 passdown letter** (preserved in `governance/passdown/` + git history). The 2026-06-25 letter has the deep reconstruction of everything through Paper 2 v1.2; this letter carries the deltas since and the current frontier. If anything here conflicts with `git log` on `main`, **trust git** and ask Manager for a fresh status board.

**Onboarding order (do this first):** `_meta/ONBOARDING-CS.md` → this letter → `governance/standing/STANDING-NON-AUTHORIZATIONS.md`. Then `MAP.md` (rev 6, at-a-glance path view) and `STATUS.md` (prose narrative, current through 2026-06-26).

---

## 1. Project in one paragraph

A behavioral stress-metrology program for LLMs. Released tower: Paper 1 (Final), Paper 2 (**v1.2 public release**, tag `paper2-cells01-03-v1.2`), Paper 3 (cert protocol, v1.0 + v1.1), plus Paper A (instrument) and the parallel Tier-1 instrument architecture. After the June-14 D4 PIVOT the standing direction is **"instrument first, seam deferred."** The first compression rung is now behind us — run once as a null-stress *control*, closed, no decay shown — and the program has **pivoted back to its real blocker: there is no admissible FP16 composition baseline.** The active frontier is recovering one: a redesigned two-step FP16 target, now locked in a pre-registration, awaiting artifact build. Single model throughout: `Qwen/Qwen2.5-3B-Instruct`, rev `aa8e72537993ba99e69dfaafa59ed015b17504d1`, FP16, greedy, mlx_lm 0.31.3, M2 Max.

---

## 2. Current state — by lane

### Compression rung — EXECUTED + CLOSED (the headline since 2026-06-25)
**Status:** **CLOSED.** The first bounded INT8 compression rung ran and closed as a control.
- Governance path: the team adopted the **light control-rung path** (`ONE-PAGE-INT8-CONTROL-RUNG-SPEC-v0.1`; CS feasibility-glance + Manager by-name auth), **superseding** the heavier five-gate `FIRST-COMPRESSION-RUNG-AUTHORIZATION-PACKET` (v0.1→v0.3, which had reached C5 gate-2). All in `governance/2026-06-21_first-compression-rung-direction/`.
- Run: `experiments/2026-06-26_first-compression-rung/` (commit `b766f9aa`). FP16 vs INT8 on the locked n=8 Two-Hop L1 target, greedy. **Result: FP16=INT8=hop1 0/8, hop2 8/8, composite 1/8; byte-identity 24/24 (match_rate 1.0).**
- Readout (the only thing it may say): bounded hop2-only **instrument-validation** readout; **INT8 produced no behavioral perturbation in this setup**; the instrument **preserved fail-closed distinctions** between readout-eligible hop2 and unqualified hop1/composite. hop2 = single-fact retrieval, **not** composition; baseline stays CONTAMINATED→INCONCLUSIVE. **NULL-STRESS instrument validation only — no retention/capability/composition/Claim-C claim.**
- TL disposition: **CLOSED, PASS as control/calibration rung** (CS-verified, SE-verified, C5-observed). CS RETURN + CS closure mirror filed in the direction dir.
- **GOVERNANCE LESSON (now standing):** the light path was appropriate for a **null** control rung; **any non-null future rung — INT4, or any case where INT8 ≠ FP16 — restores the full five-gate claim-risk chain before any readout is filed.** In the standing card.

### Composition-baseline recovery — THE ACTIVE FRONTIER
**Status:** Target memo + pre-registration FILED; **artifact build is the next object (NOT started).** `governance/2026-06-26_composition-baseline-recovery/`.
- **Target memo** `COMPOSITION-BASELINE-RECOVERY-TARGET-MEMO-v0.1` (filed `e40b1c14`): there is no admissible FP16 composition baseline (hop1 inadmissible; composite was position-reading not chain-following), so the construction must be **redesigned** (not retried) — hop1 retrievable, chain-following separable from shortcut, distractors bounded. Framed explicitly as redesign, **not** a V3 retry.
- **Pre-registration** `COMPOSITION-BASELINE-RECOVERY-PREREGISTRATION-v0.3.md` (filed `8fddd493`/`915bb974`; sha256 `8e0e02e0`, matches TL-declared digest). **Lock-before-look, FP16-only, authorizes no run.** Locks: **N=64 / 192 matched same-context triples / D=2**; numeric Wilson-LB floors (**hop1,hop2 ≥0.80; composite ≥0.70; composite-foils ≥0.60**); Wilson rule (z=1.96, lower bound, recomputed in Python); item/foil design; locked distractor set; same-context component controls; position/shortcut foils (`seed=20260626`); pass/fail/**uninterpretable** mapping; **max 3 attempts A1/A2/A3** with floors fixed across attempts; escalation rule; provenance/hash procedure.
- **Next concrete object (per TL):** build the artifacts to the prereg and seal `MANIFEST.json` **before any Manager by-name run authorization** —
  ```
  items file · prompt template · scorer_composition_l1.py · MANIFEST.json
  ```
  **NOT started. CS does not build or run these unless separately directed.** The run, if any, is the Manager's by-name authorization after the manifest is sealed.

### Released papers / standing disciplines (unchanged since 2026-06-25 — see that letter + STATUS for detail)
Paper 1 Final; Paper 2 v1.2 (v1.0 tag `41c033fc` preserved unchanged); Paper 3 v1.0/v1.1; Paper A v1.0; Tier-1 instrument architecture (G6 module; first software returned AUDIT-CIRCULARITY); Hash Integrity Is Not Construct Validity v0.7.2. D4 route CLOSED (PIVOT); CAL-Q + Terminal Attraction parked finding tracks; V3 lifecycle closed (floor-check COMPONENT-ADMISSIBLE → composite-gate PRECONDITION-FAIL; Hop1 Stability HOP1-STABLE-INADMISSIBLE). tier0-run sealed.

---

## 3. What just happened (2026-06-25 → 2026-06-29)

In order on `main`: refreshed the stale 06-10 docs → filed the compression-rung packet v0.1/v0.2 + C5 claim-risk (unblocking C5's gate-2 access HOLD) → filed packet v0.3 → **filed the light control-rung spec + CS feasibility glance** → **executed the INT8 control rung** (`b766f9aa`) → filed CS RETURN + clean-fetch → **closed the rung + pivoted** (STATUS/MAP/standing updated) → **filed the composition-baseline-recovery target memo** (`e40b1c14`) → **filed pre-registration v0.3** (`915bb974`). Every CS filing carried a §clean-fetch verification (post-push remote-HEAD recompute). Working tree clean, in sync with `origin/main`.

---

## 4. What's pending for CS

**The live obligation:** when separately directed, **build the four artifacts to prereg v0.3** (items / prompt template / `scorer_composition_l1.py` / `MANIFEST.json`) and seal hashes. This is a build-to-spec task — every floor, foil rule, n, distractor, and the Wilson recompute is locked in the prereg; build exactly to it, do not adjust floors, seal everything in `MANIFEST.json`. **Do not start until directed.** No run until Manager by-name authorization after the manifest seal.

**Standing event-triggered deliverables:** new paper revision → CS review; new inbox artifact → sweep/classify/file byte-faithful (see Inbox Workflow below); new TL status correction → CS correction report.

**Not pending; user-owned:** root `README.md`, `REVIEW.md`. `STATUS.md` is user-owned but has been refreshed under explicit Manager delegation through 2026-06-26; `MAP.md` is CS-maintained (rev 6).

---

## 5. What's blocked

Read `governance/standing/STANDING-NON-AUTHORIZATIONS.md` in full (revised 2026-06-26). Headlines:
- **INT8** — the one authorized control rung is CLOSED; the 2026-06-21 packet-authoring lift is **spent**; **no rerun, no second control, no packet revival.** New INT8 work needs fresh Manager auth and, if non-null, the full five-gate chain.
- **INT4 / all compression** — **BLOCKED until FP16 constructibility clears PASS.** Non-null rungs require the full five-gate claim-risk chain.
- **Candidate selection / thresholds / certification evaluation** — Manager-gated; not issued.
- **Seam / Claim C / composition / capability / mechanism claims** — blocked.
- **V3 composite-gate retry** — blocked; any V3 reuse must be justified as a *redesigned baseline attempt*, not a retry.
- **Building/running composition-baseline artifacts** — gated: build only when directed; run only by Manager by-name after MANIFEST seal.

Protected surfaces: Paper 2 v1.0 tag (`41c033fc`, blob `7d6706a3`), v1.2 tag (`82a24b7d`→`34ef9215`), Paper 3 v1.0/v1.1 tags, `tier0-run/` (sealed, no new files), the four sealed-byte files under the lane-1a experiment dirs.

---

## 6. Read next

1. `_meta/ONBOARDING-CS.md` — role/scope/conventions (stable).
2. `governance/standing/STANDING-NON-AUTHORIZATIONS.md` — boundary rules (rev 2026-06-26).
3. `governance/2026-06-26_composition-baseline-recovery/` — the active frontier: target memo + prereg v0.3 + CS returns.
4. `governance/2026-06-21_first-compression-rung-direction/` — the closed rung: control-rung spec, run return, closure mirror.
5. `MAP.md` (rev 6) + `STATUS.md` (through 2026-06-26).
6. `governance/passdown/2026-06-25_passdown-letter.md` — deep reconstruction of everything through Paper 2 v1.2 (history; don't treat as current state).

---

## 7. Things that have bitten CS (so you can avoid them)

- **Filing a version that isn't on disk.** 2026-06-27 the TL directed filing prereg **v0.3**, but only v0.1/v0.2 were in the inbox — CS **held** and reported the gap rather than relabel v0.2 as v0.3. *A direction to file is not delivery; delivery is the bytes (ideally with a declared digest). Verify the named object is present + matches before filing.*
- **Treating a null-stress result as a capability/retention claim.** The control rung is *instrument validation only*. "full retention" language is out of bounds; use the allowed-language list. Any non-null rung restores full claim-risk review.
- **Confusing governance weights.** Light path (CS glance + Manager by-name) is for null-stress controls; the five-gate claim-risk chain is for anything that could read as decay. Don't infer one from the other.
- **"Retired" wording on Paper 2 snapshot/mlx_lm; calling a closure "superseded."** Use canonical phrasings (see 2026-06-25 letter §2).
- **Modifying `tier0-run/` / moving a tag / committing model weights.** Sealed / frozen / gitignored. (For the control rung, INT8 weights were symlinked from the working copy then removed — never committed; `git add` scoped to the run dir only.)
- **Inferring authorization from absence.** Infer blockage from absence; escalate.
- **Committing root README/REVIEW without explicit Manager delegation.** User-owned. `MAP.md` is the CS-maintained exception.

---

## 8. Operating notes (how this seat actually runs)

- **Canonical repo:** the GitHub-synced clone at `/Users/eliasflores/Documents/Projects/Apiana_Ai/river-and-canyon`. The older `Apiana_Papers/river_and_the_canyon/river-and-canyon-repo-FINAL/` copy is **not** the push target (but it holds the gitignored model weights — useful for runs).
- **Inbox workflow:** Senior/TL/Manager artifacts arrive in `Apiana_Papers/_INBOX/` (Senior cannot push). CS sweeps each turn → classifies → files byte-faithful into the repo → verifies sha → commits → pushes → reports post-push remote HEAD → moves the source to `_INBOX/_PROCESSED/<date>/`. Redundant tarballs aren't committed; generic `SHA256SUMS.txt` is renamed to an artifact-specific name on filing.
- **FILED discipline:** a filing is FILED only when bytes verify from the shared remote on a **clean fetch** (recompute the content-sha256 from the origin blob) and local == remote == ls-remote. Every CS return appends a §clean-fetch verification.
- **Seat discipline:** CS files, verifies, builds-to-spec, and runs (when authorized). CS does **not** author Senior's manuscripts/packets, does **not** adjudicate C5's claim-risk, and does **not** self-authorize runs. Keep the independent seats independent.
- **Sign-off:** every CS document closes with `— CS Engineer, YYYY-MM-DD`. Co-author line on commits is model-agnostic: `Co-Authored-By: Claude <noreply@anthropic.com>`.

---

## 9. Final state at filing

```
Branch:  main
HEAD:    915bb974  (governance: append clean-fetch verification to prereg v0.3 CS return)
         (this passdown commit lands at HEAD after filing)
Working tree: clean; in sync with origin/main.

Tags:    paper2-cells01-03-v1.0   (41c033fc — frozen, never move)
         paper2-cells01-03-v1.2   (82a24b7d → 34ef9215 — public release)
         paper3-certification-protocol-v1.0  (6dbdcc12)
         paper3-certification-protocol-v1.1  (0b63b2ef)
         synthesis-cells01-03-pass4

Active frontier: composition-baseline recovery. Next object = build items / prompt /
  scorer_composition_l1.py / MANIFEST.json to prereg v0.3 (8e0e02e0) — NOT started; awaiting direction.
Compression: BLOCKED until FP16 constructibility clears PASS. INT8 control rung CLOSED.
```

CS holding for: the artifact-build direction (or the artifacts themselves), and any inbox drops. Building nothing and running nothing until directed.

---

— CS Engineer, 2026-06-29
