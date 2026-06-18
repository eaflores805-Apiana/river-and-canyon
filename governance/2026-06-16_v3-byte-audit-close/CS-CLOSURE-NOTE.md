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

To be appended at the foot of this memo after the closure commit lands and `git fetch origin` is run against it.

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
