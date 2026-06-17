# V3 INSTRUMENT BYTE-AUDIT — SE RETURN

**To:** Team Lead **From:** Senior Engineer **Re:** TL ACTION 2026-06-16 (Start V3 Byte-Audit First)
**E. A. Flores**, Apiana AI, Inc. — June 16, 2026 · *Verification only (YELLOW). Certifies nothing, authorizes nothing.*

## VERDICT: **HOLD**

V3 verification needs clarification before the philosophy decision record is drafted. **Not FAIL** — V3's properties are real and byte-grounded, and V3 remains a viable foreclose-all candidate. **Not PASS** — the of-record V3 pre-registration's instrument byte-binding is **stale**: two of the five bytes it pins were modified by the K-sweep patch after the prereg pinned them. The hash-pinning discipline caught a real cross-workstream byte-drift; that is the audit working, and it is fixable with a bounded re-lock.

## 1. Exact files inspected (fetched from repo HEAD `3cfdc3f`)

```text
path-a/of-record/PREREGISTRATION-PATH-A-CONSTRUCTIBILITY-v0.3.md   (the binding source; declared digests read from it)
path-a/of-record/TARGET-CONSTRUCT-DEFINITION-v0.4.md               (READ IN FULL, §0–§9 + outcome branches + feasibility status)
path-a/in-review/TARGET-CONSTRUCT-DEFINITION-v0.4.md               (compared to of-record copy)
path-a/in-review/PATH-A-CANDIDATE-CONSTRUCTION-DESIGN-v0.3.md
path-a/inspector/inspector.py                                      (C1–C9 gate + real-run/sweep structure inspected)
path-a/inspector/constants.py                                      (locked values + mode structure inspected)
tier-1-instrument/modules/g6-standing-rejection-audit/evaluator/g6_evaluator_v0_3.py
```

## 2. Digests recomputed (SE, from repo bytes; compared to the of-record prereg's declared binding)

```text
instrument                   bytes   SE-recompute   prereg-declared   match
definition v0.4 (of-record)  33547   4b616afb       4b616afb          OK
definition v0.4 (in-review)  33547   4b616afb       4b616afb          OK  (of-record == in-review, byte-identical)
design v0.3                  17613   38e05460       38e05460          OK
evaluator g6 v0.3            20277   7adf4eef       7adf4eef          OK
inspector.py                 18567   cb4b0b60       be50c08c          *** MISMATCH ***
constants.py                 12131   1d761c3d       614d185d          *** MISMATCH ***
```

**The mismatch is identified, not mysterious.** `cb4b0b60` (inspector) and `1d761c3d` (constants) are the **K-sweep sweep-mode patch** digests (commit `64a5199`), which I verified earlier this session. The of-record V3 prereg pins the **pre-patch** versions (`be50c08c`, `614d185d`; prereg §4 line 29 and §15 line 108). So the K-sweep work modified the **shared** inspector/constants files *after* the V3 prereg pinned them → the of-record V3 prereg's instrument binding now points at **superseded bytes**. (I have not verified the commit ordering — whether the prereg was elevated before or after the patch — and do not assert it; the current-state inconsistency holds either way.)

## 3. Properties verified (against definition v0.4 read in full + design v0.3 + the patched inspector/constants)

All seven foreclose-all properties are **defined and byte-grounded**:

```text
R1 terminal != answer          definition v0.4 R8.1 + inspector C1 (C* not target/decoy terminal)        VERIFIED
R2 traversal-only selection    same-depth competitors (R8/C5, D=5) + R4b depth-grab scores 1/D + relation
                               -balance (C6/E8) + direct-query/constant-token/interior-position invalidators VERIFIED
R3 derived floor               constants F = max(1/p,1/m,1/D) = 0.20, threshold = F+margin = 0.45 (derived,
                               not free); definition R11/OI-3                                              VERIFIED
R4 genuine two-hop             definition §1 (A-r1->B-r2->C*) + inspector C4 (r1 unique)                   VERIFIED
R5 four-context control        definition R7 + design v0.3 §4 + inspector C8 (composite/hop1/hop2/dq)      VERIFIED
R6 mechanical admissibility    inspector C1–C9 present and intact in the patched file; C9 Manager-lock     VERIFIED
R7 infeasibility-compatible    definition §8.5 pre-committed; "never a license to loosen R8/R6(c)/threshold" VERIFIED
```

And the validity-not-capability discipline is baked into the definition: R1 is recorded as *behavior consistent with traversal under controls*, **never proof the model composed** (definition §2 R1 + §9 boundaries). The R4b depth-competitor split (E7) keeps the depth-selection signal out of the *other* bucket. These are sound and exactly what V3 claims.

## 4. The patch is additive — V3's gate behavior is preserved (this is why HOLD, not FAIL)

I inspected the patched inspector/constants to determine whether the sweep patch altered V3's gate or merely added a branch:

```text
- constants.py declares TWO modes explicitly: REAL-RUN MODE (default; spec lacks _fixture_mode AND
  _sweep_mode -> all of p/D/m/margin/k MUST be declared and MUST match the lock; deviation/absence ->
  fail-closed REJECT) and SWEEP MODE (the ADDED branch; K varies within _sweep_locked_K_list, p/D/m/margin
  still bind to the lock). V3 runs in REAL-RUN mode, which is preserved and still fail-closed.
- The locked values are byte-present and UNCHANGED: K=5, P=5, M_MIN=10, M_FLOOR=5, MARGIN=0.25,
  F=0.20, success threshold=0.45, dominance=0.25. Identical to what the V3 prereg locks.
- inspector.py retains the full C1–C9 gate (C1 terminal!=answer, C2 pairwise-distinct incl {X_i},
  C3 category-separable, C4 r1-unique, C5 same-depth-competitor-count, C6 relation-balance, C7 dq-filler,
  C8 four-context, C9 Manager-lock); the sweep handling is confined to C9's mode branch.
CONCLUSION: the patch ADDED a sweep branch and left the REAL-RUN (V3) path enforcing the same lock,
fail-closed. V3's admissibility behavior is byte-preserved; only the prereg's DECLARED DIGESTS are stale.
```

## 5. Gaps found

```text
G1 (the HOLD cause). The of-record V3 prereg's byte-binding pins inspector be50c08c / constants 614d185d;
   the current shared files are the sweep-patched cb4b0b60 / 1d761c3d. The of-record binding is STALE.
   An of-record prereg cannot govern "these exact bytes" when the bytes it names no longer exist at HEAD.
G2. The additive-patch-preserves-V3 fact (§4) is SE-verified here but NOT yet recorded in the governance
   trail, and is NOT yet confirmed by a real-run fixture. A fixture asserting the V3 REAL-RUN path still
   REJECTS a param-deviation under the PATCHED inspector would close it conclusively (the existing
   fixtures 08/09 test sweep-mode; a real-run-rejection fixture under the patched inspector is the missing one).
G3 (not an audit blocker, noted). The prereg's open slots remain unrealized — item generator + seed, token
   pool, direct-query filler, relation-balancing realization (prereg "open slots"). These are BUILD-time,
   downstream of this audit; flagged so the path is visible, not as part of the HOLD.
```

## 6. Does V3 remain a viable candidate for the foreclose-all direction?

**Yes.** The V3-specific instrument bytes (definition v0.4, design v0.3, evaluator) verify byte-exact; definition v0.4 read in full defines all seven foreclose-all properties soundly; and the shared inspector/constants — though digest-drifted — were verified to *preserve* V3's gate behavior (additive patch, real-run path intact, locked values unchanged). The HOLD is a **binding-staleness bookkeeping** problem created by a different workstream touching shared files, **not** a defect in V3's design or properties.

## 7. Recommendation on next step

**Do NOT draft the philosophy decision record yet** (consistent with the TL ACTION: it waits for a verified V3 row, and the row is verified-in-substance but the of-record binding is stale). First close the HOLD:

```text
REMEDIATION (routes as a prereg re-lock — NOT an SE unilateral edit, since the prereg is of-record):
  1. SE drafts a binding-patch to the V3 prereg: re-pin inspector -> cb4b0b60, constants -> 1d761c3d
     (current HEAD bytes), with the §4-style "SE-verified digest" lines updated and the change-reason
     recorded ("shared inspector/constants patched additively for K-sweep sweep-mode, commit 64a5199;
     REAL-RUN/V3 gate behavior verified preserved per this audit").
  2. CS (optional but recommended, G2): add a real-run-rejection fixture under the patched inspector
     confirming the V3 path still fail-closed REJECTs a param deviation.
  3. TL / Manager re-lock the prereg of-record with the corrected binding.
THEN: V3's row is PASS (verified-in-instrument, binding-current), and the philosophy decision record
  can be drafted on solid ground.
```

This is small, bounded, and squarely the kind of thing the audit existed to surface before the larger decision was ratified. I can draft the binding-patch (step 1) on your word; the re-lock (step 3) is TL/Manager.

## 8. Boundary

```text
- Verification only (YELLOW). This audit certifies nothing, authorizes nothing, builds nothing, runs nothing.
- The Path A FP16 K=5 FAIL remains closed and untouched.
- No Claim C, no Paper B, no capability/mechanism claim, no compression.
- V3 row status: verified-in-substance (properties real, byte-grounded); of-record binding STALE on
  inspector/constants -> HOLD pending the re-lock above.
```

— Senior Engineer (audit return; HOLD)
