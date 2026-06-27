# CS RETURN — COMPOSITION BASELINE RECOVERY PREREGISTRATION v0.3 FILED

**Date:** 2026-06-27
**From:** CS Engineer
**To:** Team Lead, Manager; Cc: Senior Engineer, C5
**Re:** Byte-faithful filing of Senior's `COMPOSITION-BASELINE-RECOVERY-PREREGISTRATION-v0.3` per TL "PASS TO FILING"
**Status:** **FILED.** Filing action only — lock-before-look FP16-only pre-registration; authorizes nothing; no run.

---

## Required return fields

```text
filed path .............. governance/2026-06-26_composition-baseline-recovery/COMPOSITION-BASELINE-RECOVERY-PREREGISTRATION-v0.3.md
sha256 at filed path .... 8e0e02e0f9b40924efe3c6f976c302a0696ee4ad06118e8ba73cb461d80f62fe
matches declared digest . YES — == TL-declared 8e0e02e0f9b40924efe3c6f976c302a0696ee4ad06118e8ba73cb461d80f62fe ✓
                          (and == inbox SHA256SUMS.txt; archived as
                           COMPOSITION-BASELINE-RECOVERY-PREREGISTRATION-v0.3-SHA256SUMS.txt)
commit SHA .............. 8fddd493348a2feafc015cf3372ca58494b66415
final remote HEAD ....... 8fddd493348a2feafc015cf3372ca58494b66415  (this HEAD-fill commit follows)
clean-fetch confirm ..... PASS — see §clean-fetch below
```

## Confirmations (the required set)

```text
- filed sha256 matches 8e0e02e0… ......... CONFIRMED
- no run occurred ........................ CONFIRMED (filing only)
- no model query occurred ................ CONFIRMED (no model loaded; no inference)
- no compression work occurred ........... CONFIRMED (no FP16/INT8/INT4 execution)
- no INT8 / INT4 work occurred ........... CONFIRMED
- no canonical paper files were touched .. CONFIRMED (git status papers/ empty)
- INT8 control rung remains closed ....... CONFIRMED (2026-06-26 control rung CLOSED, commit b766f9aa)
```

## Delivery-gap note (resolved)

The prior turn's HOLD is cleared: v0.3 had not been delivered (only v0.1 + v0.2 were in the inbox), so CS held rather than relabel v0.2. v0.3 has now been delivered with a declared digest and is filed. The byte-identical re-drop of `…TARGET-MEMO-v0.1.md` (already filed `e40b1c14`) was swept to `_PROCESSED`, not re-filed. Superseded prereg drafts v0.1 (`4ad606dc`) and v0.2 (`e261fd19`) were not directed for filing; preserved in `_PROCESSED/2026-06-27`, not committed (their deltas are documented in v0.3's own §"v0.1→v0.2" / §"v0.2→v0.3" changelog). Available to file as a supersession trail if TL directs.

## Shown-semantic-read (filing diligence — TL already PASSED TO FILING)

The artifact instantiates its name: a **lock-before-look FP16-only pre-registration** that "authorizes nothing," locking the design the target memo deferred — exact n (**N=64; 192 matched same-context triples; D=2**), numeric **floors** (hop1/hop2 Wilson-LB ≥0.80, composite ≥0.70, composite-foils ≥0.60), the **Wilson rule** (z=1.96, lower bound, recomputed in Python), item/foil design, locked distractor set, same-context component controls, position/shortcut foils (`seed=20260626`), pass/fail/uninterpretable mapping, **max 3 attempts (A1/A2/A3)** with floors fixed across attempts, escalation rule, and provenance/hash procedure. v0.2→v0.3 is the narrow TL-HOLD fix only (separate document-revision from attempt-ID; "Document revision numbers are not attempt numbers"); no substantive change. No run authorization or compression language is present (FP16-only; forbidden interpretations restated).

## Next step (per TL — not a run, not CS-initiated)

The next object is **not** a run. Concrete artifacts must be built to this pre-registration and sealed in `MANIFEST.json` before any Manager by-name run authorization:

```text
- items file
- prompt template
- scorer_composition_l1.py
- MANIFEST.json
```

**CS does not build or run these unless separately directed.** Holding.

---

## §clean-fetch verification (post-push)

```text
Pre-reg committed at 8fddd493 (this CS-RETURN HEAD-fill commit lands immediately after).
Fetched origin/main fresh and recomputed the filed pre-reg content-sha256 from the origin blob:
  governance/2026-06-26_composition-baseline-recovery/COMPOSITION-BASELINE-RECOVERY-PREREGISTRATION-v0.3.md
  → 8e0e02e0f9b40924efe3c6f976c302a0696ee4ad06118e8ba73cb461d80f62fe  ✓ == TL-declared digest
final remote HEAD verified == local == ls-remote at push time (8fddd493).
Bytes verify from the shared remote on clean fetch → FILED.
```

---

## Non-authorizations (carried forward)

```text
- No run · no model query · no INT8 · no INT4 · no compression. Compression BLOCKED until FP16
  constructibility clears PASS.
- No Claim C · no seam · no capability · no mechanism claim.
- INT8 control rung remains CLOSED. Path A FP16 K=5 FAIL stays closed. tier0-run sealed.
  Paper 2 v1.0/v1.2 + Paper 3 tags preserved; canonical paper files untouched.
- This pre-registration locks a design; it authorizes no run. Building artifacts / running requires
  separate direction; the run, if any, is the Manager's by-name authorization after MANIFEST seal.
```

---

— CS Engineer, 2026-06-27
