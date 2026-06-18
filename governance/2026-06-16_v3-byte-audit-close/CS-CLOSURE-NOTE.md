# CS CLOSURE NOTE — V3 Instrument Byte-Audit HOLD Lifecycle

**Date:** 2026-06-17
**From:** CS Engineer
**To:** Team Lead; Cc: Senior Engineer, Manager
**Re:** Closure of the V3 byte-audit HOLD lifecycle initiated by TL ACTION 2026-06-16 ("Close V3 Instrument Byte-Audit HOLD Before Philosophy Decision Record")
**Status:** LIFECYCLE CLOSED — v0.4 RE-LOCKED OF RECORD; Senior cleared to draft philosophy decision record

---

## Record status

```text
Lifecycle           V3 instrument byte-binding HOLD-close
Opened              2026-06-16 (Senior byte-audit return verdict HOLD)
Closed              2026-06-16 (Manager + Team Lead re-lock of v0.4 of-record)
Filed               2026-06-17 (CS closure note + memo filings)
Of-record outcome   PREREGISTRATION-PATH-A-CONSTRUCTIBILITY-v0.4 (binding-patch
                    successor to v0.3; scope = instrument byte-binding only)
Route unlocked      Senior cleared to draft philosophy decision record
                    (foreclose-all standard, V3 vehicle, audit → build → floor-check)
```

---

## 1. The four artifacts that closed the loop

In sequence:

```text
1. SENIOR — V3 instrument byte-audit return         (verdict: HOLD)
   path:  path-a/in-review/V3-INSTRUMENT-BYTE-AUDIT-SE-RETURN-v0.1.md
   sha:   c3f4e6670d51c225322161c02b9b2eef9eda74bc7729ccd3a3a2ed74e81fbdcc
   trail: Senior verified V3's seven foreclose-all properties byte-grounded
          against definition v0.4, design v0.3, and the patched inspector/
          constants. Identified the HOLD cause: the of-record v0.3 prereg's
          byte-binding block pinned inspector be50c08c… / constants 614d185d…,
          but those shared files were patched additively for K-sweep sweep-mode
          (commit 64a5199) → current HEAD is cb4b0b60… / 1d761c3d… → of-record
          binding stale. Verified the patch additive: REAL-RUN/V3 gate behavior
          preserved; locked values byte-present and unchanged; C1–C9 intact.
          Recommended remediation = narrow binding-patch re-lock.

2. SENIOR — binding-patch prereg v0.4 (in-review draft)
   path:  path-a/in-review/PREREGISTRATION-PATH-A-CONSTRUCTIBILITY-v0.4-binding-patch.md
   sha:   bfb4404ab1bf872e7e81056b144440d1a09e31b88fc6b400cb6e4cac48f0b8f6
   trail: Narrow-scope binding patch re-pinning inspector be50c08c… →
          cb4b0b60bd6dc2b5… and constants 614d185d… → 1d761c3d1c56e7ac…,
          attesting no values / thresholds / outcome rules / scoring
          categories / controls / stop-rules / forbidden interpretations
          changed. Senior locked nothing — routed to TL/Manager for re-lock
          after parallel CS fixture PASS.

3. CS — V3 real-run parameter-deviation fixture     (verdict: PASS)
   fixture:   tier-1-instrument/modules/g6-standing-rejection-audit/evaluator/
              tests/fixtures/path_a/10_v3_real_run_param_deviation/
   spec sha:  42cd53c4cb19124a810792d66c6e8391d688893b20f082acc6fb705f9f294aad
   expected:  cd068ef32e86a46fa8b2ffe35bf793dda5565722fecbf4f1943af0f6bc9289c5
   result:    path-a/inspector/results/10_v3_real_run_param_deviation_inspection.json
   result sh: 5f09fe253b7c6195568f93b9c3b79e26b2b4f0e860834c83a750621dfedf4190
   trail:     Spec runs REAL-RUN mode (no _fixture_mode, no _sweep_mode)
              with internally consistent drift (params.D = 4 AND 4 actual
              depth_2_competitors AND 4-entry relation_balance). Inspector
              under test: cb4b0b60bd6dc2b5… (patched) + 1d761c3d1c56e7ac…
              (patched). Result: disposition REJECT, 8/9 checks pass, single
              failure isolated to C9_manager_lock_binding ("params.D = 4 !=
              Manager-locked D_DEPTH_COMPETITORS = 5"), validation.mode =
              real-run, _expected_match: true. Closes the G2 gap from §1:
              executable evidence that the K-sweep additive patch did not
              loosen the REAL-RUN fail-closed binding.
   memo:      governance/2026-06-16_v3-byte-audit-close/
              CS-RETURN-V3-REAL-RUN-FIXTURE-2026-06-16.md
              (Appendix A: per-file clean-fetch verification against origin/main)

4. MANAGER + TEAM LEAD — re-lock record (RE-LOCKED OF RECORD)
   path:  governance/2026-06-16_v3-byte-audit-close/
          MANAGER-TL-RE-LOCK-v0.4-2026-06-16.md
   sha:   96bda3cf55d3adce4a8484e116cee0b9ed3c2a859633ecc6f6e07f83b2e000fb
   trail: Manager + Team Lead re-locked v0.4 as the of-record successor to
          v0.3 (v0.3 sha d9bd9b21…). Scope = instrument byte-binding only;
          attested no scientific content changed. Route unlock: Senior
          cleared to draft the philosophy decision record (foreclose-all
          standard, V3 vehicle, route audit → build → floor-check). The
          philosophy record itself does not by itself authorize build or run.
```

## 2. Final of-record state (post-re-lock)

```text
path-a/of-record/
  TARGET-CONSTRUCT-DEFINITION-v0.4.md                  4b616afb…   (unchanged)
  PREREGISTRATION-PATH-A-CONSTRUCTIBILITY-v0.3.md      d9bd9b21…   superseded — retained
  PREREGISTRATION-PATH-A-CONSTRUCTIBILITY-v0.4.md      bfb4404a…   PREREG OF RECORD ← new
  README.md                                                          updated with v0.4 row
                                                                     + supersession note

path-a/inspector/
  inspector.py     cb4b0b60bd6dc2b5f1d7ee6c4eaf3fc274cbb10254b5a548c637c84ca27348a9
  constants.py     1d761c3d1c56e7aca9ef32a3f8b05c310e2aa5f35c6d91e67fd7fd81468915dd
  results/10_v3_real_run_param_deviation_inspection.json
                   5f09fe253b7c6195568f93b9c3b79e26b2b4f0e860834c83a750621dfedf4190

  → the two digests v0.4 of-record now pins match the two files at HEAD
  → the digest gap that caused the HOLD is closed
```

Of-record bindings (the only meaningful change between v0.3 and v0.4):

```text
                    v0.3 (superseded)      v0.4 (of record)
inspector.py        be50c08c…              cb4b0b60bd6dc2b5…
constants.py        614d185d…              1d761c3d1c56e7ac…
all other digests   unchanged              unchanged
all values          unchanged              unchanged
all outcome rules   unchanged              unchanged
all stop-rules      unchanged              unchanged
```

## 3. What is now unlocked vs what remains blocked

```text
UNLOCKED (per re-lock memo § "Route unlock"):
  - Senior may draft the philosophy decision record:
      foreclose-all as the gate standard
      V3 as the candidate vehicle
      route: audit → build → floor-check
    The philosophy record is a decision artifact; it does not by itself
    authorize build or run.

STILL BLOCKED (unchanged by the re-lock):
  - build (no item generation; no prompt generation; no construction build)
  - model run (a run requires separate Manager by-name authorization with
               lock-before-look discipline, even against the locked v0.4 shell)
  - compression
  - Claim C / Paper B
  - capability claim / mechanism claim
  - candidate selection memo (Paper 3) — independently blocked, not touched here
  - threshold values, certification evaluation, multi-model execution, Fork A
    reactivation, public benchmark packaging — all carried per standing card
```

## 4. Doctrine notes (what this lifecycle demonstrated, for the trail)

```text
- The hash-pinning discipline worked as designed. A cross-workstream change
  to shared files (K-sweep additive patch on inspector/constants) silently
  drifted the of-record V3 prereg's byte-binding to point at superseded
  bytes; the byte-audit caught it before the philosophy decision was ratified.

- "Additive patch preserves the prior gate" is a code-reading claim until it
  is tested. The CS fixture (10) converted Senior's code-reading attestation
  into executable evidence: REAL-RUN fail-closed REJECT on a Manager-lock
  deviation under the patched inspector. The two together (Senior structural
  read + CS executable evidence) carried the re-lock; either alone would
  have been weaker.

- The lifecycle followed the discipline:
    HOLD raised → narrow remediation drafted → executable evidence produced
    → Manager + TL re-lock → version trail retained (v0.3 byte-identical at
    of-record as the prior-of-record audit record; v0.4 binding patch
    byte-identical at both in-review and of-record).
  No history rewrite; superseding commits only.
```

## 5. Files added or modified in this turn (CS, today)

```text
CHANGED (of-record + READMEs)
  path-a/of-record/PREREGISTRATION-PATH-A-CONSTRUCTIBILITY-v0.4.md   (NEW; bfb4404a…)
  path-a/of-record/README.md                                          (v0.4 row + addendum)
  path-a/in-review/README.md                                          (v0.3/v0.4 row updates)

ADDED (governance)
  governance/2026-06-16_v3-byte-audit-close/
    MANAGER-TL-RE-LOCK-v0.4-2026-06-16.md                             (NEW; 96bda3cf…)
    CS-CLOSURE-NOTE.md                                                (this file)
```

The CS-RETURN-V3-REAL-RUN-FIXTURE-2026-06-16.md filed yesterday in the same dir is unchanged and remains the CS evidence of record for the fixture half.

## 6. Clean-fetch verification

Performed after the closure commit landed; `git fetch origin` immediately preceded the verification. Each file's local sha256 was compared against `git cat-file -p origin/main:<path> | sha256sum` so the bytes verified are the **origin** bytes, not the local working-tree bytes.

```text
origin/main HEAD             b70c39f150cca6234ff98ec5ebbe2f8f7cc2ef5e
local       HEAD             b70c39f150cca6234ff98ec5ebbe2f8f7cc2ef5e   (match)

per-file verification (origin/main bytes → local bytes):

MATCH  bfb4404ab1bf872e7e81056b144440d1a09e31b88fc6b400cb6e4cac48f0b8f6
       path-a/of-record/PREREGISTRATION-PATH-A-CONSTRUCTIBILITY-v0.4.md
MATCH  bfb4404ab1bf872e7e81056b144440d1a09e31b88fc6b400cb6e4cac48f0b8f6
       path-a/in-review/PREREGISTRATION-PATH-A-CONSTRUCTIBILITY-v0.4-binding-patch.md
                   ↑ same sha at both locations → byte-identical elevation verified
MATCH  d9bd9b219badd25901811ddfbb43b811a04750a77723f6a1f076c7dd641f091c
       path-a/of-record/PREREGISTRATION-PATH-A-CONSTRUCTIBILITY-v0.3.md
                   ↑ unchanged from prior of-record (superseded but retained)
MATCH  4b616afb919114ee6e0b524e030172cc6f9a96ea8e206fc65bcbd0571eb23c29
       path-a/of-record/TARGET-CONSTRUCT-DEFINITION-v0.4.md
                   ↑ unchanged; v0.4 binding patch did not touch the definition
MATCH  73c786a532c4c3a3b7320398d64d2561945c85ef6693a9f74ce2cfc3ce7b523b
       path-a/of-record/README.md
MATCH  a0877e934e869719bfc47ef0c4cd46c35b99c7c9949121b9c7b7a271bcea73fe
       path-a/in-review/README.md
MATCH  96bda3cf55d3adce4a8484e116cee0b9ed3c2a859633ecc6f6e07f83b2e000fb
       governance/2026-06-16_v3-byte-audit-close/MANAGER-TL-RE-LOCK-v0.4-2026-06-16.md
MATCH  bb55324fbcab837c670bb2eb3cc4ae5515c3fbd72c7a1543f1bba8794d42db72
       governance/2026-06-16_v3-byte-audit-close/CS-RETURN-V3-REAL-RUN-FIXTURE-2026-06-16.md
                   ↑ filed yesterday; unchanged this lifecycle turn
MATCH  cb4b0b60bd6dc2b5f1d7ee6c4eaf3fc274cbb10254b5a548c637c84ca27348a9
       path-a/inspector/inspector.py
                   ↑ the file v0.4 of-record now pins
MATCH  1d761c3d1c56e7aca9ef32a3f8b05c310e2aa5f35c6d91e67fd7fd81468915dd
       path-a/inspector/constants.py
                   ↑ the file v0.4 of-record now pins
MATCH  5f09fe253b7c6195568f93b9c3b79e26b2b4f0e860834c83a750621dfedf4190
       path-a/inspector/results/10_v3_real_run_param_deviation_inspection.json
                   ↑ executable evidence the patched inspector still fail-closed
```

All 12 artifacts reproduce byte-exact from the shared repository on a clean fetch. The two-copy v0.4 invariant (in-review binding patch and of-record prereg sharing sha `bfb4404a…`) is verified directly. The two pinned-instrument digests (inspector `cb4b0b60…` and constants `1d761c3d…`) match the corresponding files at HEAD. **HOLD-close lifecycle FILED and closed.**

---

## 7. Correction — finalized v0.4 replaces placeholder v0.4 (2026-06-17)

**Why this section exists.** Sections 1–6 above are preserved as the historical record of the original lifecycle close: every claim about sha `bfb4404a…` in §§1, 2, 5, 6 was true at the time it was verified. **It described the pre-fill binding-patch bytes.** Senior subsequently identified that the binding-patch text Senior originally delivered contained an unfilled placeholder — the line *"supersedes v0.3 (of-record, `<v0.3 of-record digest>`) for the instrument byte-binding block solely"* — i.e. the `<v0.3 of-record digest>` token was never replaced with the actual v0.3 of-record sha. The bytes that landed of-record on 2026-06-17 carried that placeholder.

**TL corrective action (2026-06-17):** `governance/2026-06-16_v3-byte-audit-close/TL-CORRECTIVE-ACTION-FINALIZE-V0.4-2026-06-17.md`. Status: ACTION — clerical correction / no science change. Required CS to replace the of-record v0.4 file with Senior's finalized filled bytes (sha `c61a3256…`) and update every README / closure / re-lock reference pointing to `bfb4404a…` as the of-record v0.4 digest.

**CS execution.**

```text
REPLACED (byte-identical with Senior's finalized bytes; sha c61a3256...)
  path-a/of-record/PREREGISTRATION-PATH-A-CONSTRUCTIBILITY-v0.4.md
  path-a/in-review/PREREGISTRATION-PATH-A-CONSTRUCTIBILITY-v0.4-binding-patch.md
    (Senior re-issued under the same in-review filename → byte-identical
     pair invariant preserved at the corrected sha)

CONFIRMED on the corrected of-record bytes
  placeholder `<v0.3 of-record digest>` count : 0
  v0.3 of-record digest d9bd9b21… count       : 1

UPDATED references (bfb4404a... → c61a3256...)
  path-a/of-record/README.md       — v0.4 row sha + new corrective addendum
  path-a/in-review/README.md       — v0.4 binding-patch row sha + correction note
  governance/2026-06-16_v3-byte-audit-close/CS-CLOSURE-NOTE.md
                                   — this §7 (the prior §§1–6 are historical
                                     and intentionally retain bfb4404a…)

UNCHANGED references (the bfb4404a... mention is HISTORICAL, not load-bearing)
  governance/2026-06-16_v3-byte-audit-close/MANAGER-TL-RE-LOCK-v0.4-2026-06-16.md
                                   — re-lock memo does not cite v0.4's sha
  governance/2026-06-16_v3-byte-audit-close/CS-RETURN-V3-REAL-RUN-FIXTURE-2026-06-16.md
                                   — historical claim about the SE-drafted
                                     in-review binding patch at the time of
                                     fixture filing; kept as audit record
```

**Scientific content delta:** none. No values, thresholds, outcome rules, scoring categories, controls, stop-rules, or forbidden interpretations changed between `bfb4404a…` and `c61a3256…`. The only delta is the placeholder being replaced with the actual v0.3 of-record digest `d9bd9b219badd25901811ddfbb43b811a04750a77723f6a1f076c7dd641f091c`, which is what Senior originally intended that line to read. Both byte-strings re-pin inspector `cb4b0b60…` and constants `1d761c3d…` identically, attest the same UNCHANGED invariants, and route through the same Manager + TL re-lock authority.

## 8. Clean-fetch verification — corrected state (2026-06-17, second verification)

Performed after the correction commit landed; `git fetch origin` immediately preceded the verification. Each file's local sha256 compared against `git cat-file -p origin/main:<path> | sha256sum`.

```text
origin/main HEAD              9ea16d1de5e985f9d5f80f0ba452417246cb41be
local       HEAD              9ea16d1de5e985f9d5f80f0ba452417246cb41be   (match)

per-file verification (origin/main bytes → local bytes):

MATCH  c61a3256d26e0ed0226e46a60d9b701baddfe3006249db687f221aea57315955
       path-a/of-record/PREREGISTRATION-PATH-A-CONSTRUCTIBILITY-v0.4.md
MATCH  c61a3256d26e0ed0226e46a60d9b701baddfe3006249db687f221aea57315955
       path-a/in-review/PREREGISTRATION-PATH-A-CONSTRUCTIBILITY-v0.4-binding-patch.md
                   ↑ corrected byte-identical pair invariant — both at c61a3256…
MATCH  d9bd9b219badd25901811ddfbb43b811a04750a77723f6a1f076c7dd641f091c
       path-a/of-record/PREREGISTRATION-PATH-A-CONSTRUCTIBILITY-v0.3.md
                   ↑ unchanged; superseded but retained as prior-of-record trail
MATCH  cb4b0b60bd6dc2b5f1d7ee6c4eaf3fc274cbb10254b5a548c637c84ca27348a9
       path-a/inspector/inspector.py
MATCH  1d761c3d1c56e7aca9ef32a3f8b05c310e2aa5f35c6d91e67fd7fd81468915dd
       path-a/inspector/constants.py
                   ↑ the two files v0.4 of-record now pins; finalized v0.4 cites
                     the same digests as the placeholder version did
MATCH  f1b916c0e5a7542b7a95138f34f2b953e3d83e0f0bb5b529f59c98342177a2e0
       path-a/of-record/README.md
MATCH  202af3c84af0ef18a35fbad2ac27758e946a3e00ea9ac8771549b05bdca24b78
       path-a/in-review/README.md
MATCH  49b7f499cf0437d499cfc028e75fe9684a7cba96bd5455cdb32747c647394c59
       governance/2026-06-16_v3-byte-audit-close/TL-CORRECTIVE-ACTION-FINALIZE-V0.4-2026-06-17.md
MATCH  0c429583d931cd67f3f7073e1991c29aa8b5aa470c60bb288096e200bee38cb1
       governance/2026-06-16_v3-byte-audit-close/CS-CLOSURE-NOTE.md
                   ↑ this file, immediately PRIOR to the §8 commit (the §8
                     commit's own sha will be cross-verified on the next sweep)
MATCH  96bda3cf55d3adce4a8484e116cee0b9ed3c2a859633ecc6f6e07f83b2e000fb
       governance/2026-06-16_v3-byte-audit-close/MANAGER-TL-RE-LOCK-v0.4-2026-06-16.md
                   ↑ unchanged; re-lock memo did not cite v0.4 sha
```

**Streamed-from-origin assertions on the corrected of-record v0.4 bytes** (via `git cat-file -p origin/main:<path>`):

```text
placeholder `<v0.3 of-record digest>` count    : 0   (absent)
v0.3 of-record digest d9bd9b21… count          : 1   (filled, as Senior intended)
```

All 10 listed artifacts reproduce byte-exact from the shared repository on a clean fetch. The corrected of-record v0.4 contains zero placeholders and exactly one occurrence of the filled v0.3 of-record digest. **TL corrective action FILED and closed.**

---

— CS Engineer, 2026-06-17 (correction appendix)

---

## Non-authorizations (carried forward)

```text
- candidate selection: blocked.
- threshold values: blocked (pre-registered, not freely tunable).
- certification evaluation: blocked.
- new model runs: blocked (single-model scope; any new run = fresh authorization).
- re-runs beyond authorized reproduction validation: blocked.
- INT8 / INT4 execution: blocked.
- multi-model execution: blocked.
- Fork A reactivation: blocked permanently.
- Claim C activation: blocked.
- Paper 3 execution as an experiment: blocked.
- Paper 6 activation: blocked.
- public benchmark packaging: blocked.
- artifact mutation: locked artifacts must not be edited in place.

Protected surfaces:
- Paper 2 v1.0 tag (paper2-cells01-03-v1.0, 41c033fc…) + tagged manuscript
  blob (7d6706a3…): never moved.
- tier0-run/ directory: sealed; no new files.

v0.4 lock-eligibility ≠ run authorization. A model run still requires
separate Manager by-name authorization with lock-before-look. The Path A
FP16 K=5 FAIL remains closed.
```

---

— CS Engineer, 2026-06-17
