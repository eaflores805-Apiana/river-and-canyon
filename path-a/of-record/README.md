# Path A — Of-Record

Definition-of-record + locked preregistration for **Path A constructibility**.
Artifacts here are **of-record**: elevated by Manager + Team Lead authorization;
the in-review iterations are retained in `path-a/in-review/` as the version trail.

## Of-record artifacts

| File | sha256 | Status |
|---|---|---|
| `TARGET-CONSTRUCT-DEFINITION-v0.4.md` | `4b616afb919114ee6e0b524e030172cc6f9a96ea8e206fc65bcbd0571eb23c29` | **definition-of-record** for Path A. Gate-before-construction rule surface. v0.4 narrow patches over v0.3: (1) dominance threshold 0.25 promoted from scorer code into the definition (R11, §8.3, checklist #7); (2) real-run fixture-mode guard added (checklist #11). No do-not-alter invariant changed. |
| `PREREGISTRATION-PATH-A-CONSTRUCTIBILITY-v0.3.md` | `d9bd9b219badd25901811ddfbb43b811a04750a77723f6a1f076c7dd641f091c` | **preregistration-of-record** — locked FP16-only constructibility test at Manager-approved parameter point. Binds by digest to v0.4 (of-record above), design v0.3 (in-review, see §16 for SHAs), inspector + evaluator + constants. **Locking this shell does not authorize a run.** A run requires separate Manager by-name authorization with lock-before-look discipline. |

## Authority + sequencing

- TL ACTION 2026-06-15 ("Elevate v0.4 and Lock Prereg v0.3") relayed Manager approval.
- Atomic of-record commit: this filing + the `path-a/inspector/constants.py` `DOMINANT_RATE_THRESHOLD_PROVENANCE.status` update from `"FLAGGED FOR PROMOTION"` to `"PROMOTED"` (per the CS prior recommendation to bundle atomically).
- In-review trail preserved at `path-a/in-review/`; README there now marks the elevated bytes with pointers to `path-a/of-record/`.

## What this changes

- The dominance threshold (0.25) is now declared in the definition, not buried in scorer code. The provenance flag in `constants.py` reads `"PROMOTED"` referencing v0.4 by digest.
- The real-run fixture-mode guard (`_fixture_mode: true` is inadmissible for real-run pre-registration) is now a definition-level admissibility requirement, complementing the software-level enforcement (inspector C9 + evaluator LOCK_VIOLATION).
- The preregistration shell v0.3 is now the locked declaration; per its §17 stop-rule, no post-hoc change to construction / gate / scoring / invalidators / floor / threshold / dominance threshold / analysis unit after results are seen. Re-runs require a new locked pre-registration.

## What this does NOT change / authorize

- **NOT a certified baseline** — definition v0.4 defines the bar a run must clear; locking the prereg does not meet it.
- **NOT a run authorization** — model execution requires separate Manager by-name authorization.
- **NOT Claim C / Paper B / compression / capability / mechanism claim** of any kind.
- The substrate-infeasibility branch (definition §8.5) remains pre-committed but does NOT fire from a single run.

## Boundaries (carried)

```text
no items ; no concrete token lists ; no prompt templates ; no model run ;
no compression rung ; no certified baseline ; no Claim C ; no Paper B ;
no model-capability claim ; no mechanism / architecture / training-distribution claim.
```

— CS Engineer, 2026-06-15 (filed under TL ACTION + Manager approval for of-record elevation)
