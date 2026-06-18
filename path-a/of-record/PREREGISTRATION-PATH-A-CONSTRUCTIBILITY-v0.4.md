# PREREGISTRATION-PATH-A-CONSTRUCTIBILITY-v0.4 (binding patch)

**E. A. Flores**, Apiana AI, Inc. — June 16, 2026
*River and Canyon · Path A. Prepared by the Senior Engineer. **Binding patch only** — supersedes v0.3 (of-record, `<v0.3 of-record digest>`) for the instrument byte-binding block solely. Drafted for TL/Manager re-lock; SE locks nothing.*

> **Why v0.4 exists (narrow scope).** The V3 instrument byte-audit (SE return, `c3f4e667…`) returned HOLD for one reason: the of-record v0.3 prereg's byte-binding pinned `inspector.py = be50c08c…` and `constants.py = 614d185d…`, but the K-sweep sweep-mode patch (commit `64a5199`) modified those **shared** files after v0.3 pinned them, so the of-record binding pointed at superseded bytes. The patch was verified **additive** — it added a sweep-mode branch and left the **REAL-RUN** path (which V3 uses) enforcing the same Manager lock fail-closed, with every locked value byte-present and unchanged. v0.4 **re-pins the two stale digests to current HEAD and records the reason. It changes nothing else.** This is the minimal correction that makes the of-record binding accurate; it is not a content revision.

## What v0.4 changes (the only changes)

```text
1. RE-PIN inspector.py:   be50c08c…  ->  cb4b0b60bd6dc2b5…   (current HEAD 3cfdc3f; SE-recomputed)
2. RE-PIN constants.py:   614d185d…  ->  1d761c3d1c56e7ac…   (current HEAD 3cfdc3f; SE-recomputed)
3. REASON RECORDED: the shared inspector.py / constants.py were patched additively for K-sweep
   sweep-mode (commit 64a5199). The V3 REAL-RUN gate behavior was verified PRESERVED by the SE
   byte-audit (return c3f4e667…): REAL-RUN mode still requires p/D/m/margin/k to match the Manager
   lock and fail-closed REJECTs deviation; the full C1–C9 inspector gate is intact; the sweep
   handling is confined to C9's mode branch and does not touch the real-run path.
```

## Corrected byte-binding block (supersedes v0.3 §15 byte-binding)

The run is governed by these exact bytes (SE-recomputed from repo bytes at HEAD `3cfdc3f`, declared digests echoed adjacently for reviewer assertion):

```text
definition v0.4   4b616afb…   (unchanged; verified byte-exact, of-record == in-review)
design v0.3       38e05460…   (unchanged; verified byte-exact)
inspector.py      cb4b0b60bd6dc2b5…   (RE-PINNED from be50c08c…; additive sweep-mode patch, real-run preserved)
constants.py      1d761c3d1c56e7ac…   (RE-PINNED from 614d185d…; additive sweep-mode patch, locked values unchanged)
evaluator g6 v0.3 7adf4eef…   (unchanged; verified byte-exact)
```

## Attestation — no values, thresholds, rules, categories, or stop-rules changed

SE re-confirmed (this turn) that every locked quantity is byte-present and unchanged in the re-pinned `constants.py` and that the gate structure is intact in the re-pinned `inspector.py`:

```text
UNCHANGED and byte-present (verified):
  - foreclose-all standard ........................ intact (definition v0.4, design v0.3 — not touched)
  - F = max(1/p,1/m,1/D) = 0.20 ................... present in constants.py derivation
  - success threshold = F + margin = 0.45 ......... present
  - margin = 0.25 ................................. MARGIN = 0.25 present
  - dominance threshold = 0.25 .................... DOMINANT_RATE_THRESHOLD = 0.25 present
  - K = 5, P = 5, M_MIN = 10, M_FLOOR = 5 ......... all present
  - D_DEPTH_COMPETITORS ........................... present
  - R4b depth-competitor split (E7) ............... unchanged (definition v0.4 §2, evaluator — not touched)
  - fixture-mode guard ............................ _fixture_mode guard present (constants + inspector)
  - REAL-RUN mode enforcement ..................... present and fail-closed
  - CI decision rule (Wilson 95%, MECE partition).. unchanged (definition v0.4 §8, prereg §14 — not touched)
  - §17 stop-rule / substrate-infeasibility ....... unchanged (definition v0.4 §8.5 — not touched)
  - forbidden interpretations ..................... unchanged (definition v0.4 §9 — not touched)
```

Only the two instrument **digests** in the binding block moved, to match the bytes already at HEAD. No value, threshold, outcome rule, scoring category, control, or stop-rule was altered.

## Scope and boundaries (unchanged from v0.3)

```text
- This remains a SHELL: it declares and binds; it contains no items, tokens, prompts, model-execution
  command, or compression rung. Locking it does NOT authorize a run (a run needs separate Manager
  by-name authorization with lock-before-look and the §13 fixture-mode assertion).
- This binding patch is SE-DRAFTED and locks nothing. TL/Manager re-lock the corrected binding of-record.
- It does not authorize a build, item generation, prompt generation, a model run, or compression.
- Not a certified baseline, not Claim C, not Paper B, not a capability or mechanism claim.
- The Path A FP16 K=5 FAIL remains closed and untouched.
```

## Dependency note (the gate this patch sits behind)

```text
This binding patch is one of two parallel HOLD-closure actions:
  - SE (this artifact): re-pin the binding + attest no-other-change.
  - CS (parallel): add a V3 REAL-RUN parameter-deviation fixture under the patched inspector/constants,
    confirming the real-run path still fail-closed REJECTs a deviation (PASS return with fixture/result
    paths, commit, sha256s, clean-fetch). The existing fixtures 08/09 test sweep-mode; this is the
    missing real-run-rejection case.
After BOTH return: TL/Manager re-lock this corrected binding of-record. ONLY THEN may SE draft the
philosophy decision record.
```

---

## Changelog v0.3 → v0.4 (binding patch — no values changed)

```text
RE-PINNED  inspector.py  be50c08c… -> cb4b0b60bd6dc2b5…  (current HEAD; additive K-sweep sweep-mode patch)
RE-PINNED  constants.py  614d185d… -> 1d761c3d1c56e7ac…  (current HEAD; locked values byte-present, unchanged)
RECORDED   reason: shared inspector/constants patched additively for K-sweep sweep-mode (commit 64a5199);
           V3 real-run gate behavior verified preserved by SE byte-audit (return c3f4e667…).
ATTESTED   no values / thresholds / outcome rules / scoring categories / controls / stop-rules / forbidden
           interpretations changed; only the two binding-block digests moved to match HEAD bytes.
UNCHANGED  the entire v0.3 content otherwise: scope, research question, locked Manager values, construction
           schema, admissibility gate (C1–C9), scoring (R1–R6cat incl. R4b), floor/threshold/dominance,
           outcome branches (MECE), fixture-mode guard, §17 stop-rule, forbidden interpretations, and the
           no-items/prompts/run shell scope. v0.4 is a binding-currency correction, not a content revision.
```

— Senior Engineer (binding patch draft; SE locks nothing — routes to TL/Manager for re-lock, after CS fixture PASS)
