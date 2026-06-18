# CS FILING MEMO — V3 Floor-Check Preregistration v0.3

**Date:** 2026-06-18
**From:** CS Engineer
**To:** Team Lead; Cc: Senior Engineer, C5, Manager
**Re:** TL ACTION 2026-06-18 — "File V3 Floor-Check Preregistration v0.3 for Review"
**Status:** **PASS — v0.3 filed for CS/C5 review**

---

## Record status

```text
ACTION                  TL, 2026-06-18 ("File V3 Floor-Check Preregistration v0.3 for Review")
verdict                 PASS — v0.3 filed verbatim at the TL-specified path
scope respected         filing-and-review-only ACTION; no scientific edits;
                        no build changes; no N=96 materialization; no run.
substantive re-review   pending — this filing routes to CS feasibility
                        re-review + C5 claim-risk review; verdicts come
                        in a subsequent return.
v0.2 also filed         as the superseded predecessor (inbox workflow
                        requires sweep of every Senior artifact). Marked
                        superseded; retained byte-identical as version trail.
```

---

## 1. Required CS return fields (per TL ACTION)

### commit

```text
to be recorded in §3 once it lands
```

### final remote HEAD

```text
to be recorded in §3 once push completes
```

### filed path

```text
path-a/in-review/PREREGISTRATION-V3-FLOOR-CHECK-v0.3.md
```

(Exactly the path TL specified. The inbox source file was named `PREREGISTRATION-V3-FLOOR-CHECK-PATH-A-v0.3.md` — the `-PATH-A-` infix is dropped at filing per TL's specified destination path. Bytes are byte-identical between source and destination; only the filename differs.)

### sha256 digest

```text
df82b34c4f96e085ea51b8e6e1a735849a39b108b321f79e30b9f20cffa19d5b
```

### clean-fetch confirmation

```text
to be recorded in §3 after `git fetch origin` and per-file verification
```

### confirmation bytes match Senior v0.3 source

```text
YES.

Inbox source (Senior delivery):
  _INBOX/PREREGISTRATION-V3-FLOOR-CHECK-PATH-A-v0.3.md
  sha256 df82b34c4f96e085ea51b8e6e1a735849a39b108b321f79e30b9f20cffa19d5b

Filed destination (after `cp`):
  path-a/in-review/PREREGISTRATION-V3-FLOOR-CHECK-v0.3.md
  sha256 df82b34c4f96e085ea51b8e6e1a735849a39b108b321f79e30b9f20cffa19d5b
                                                          ^ identical

Filing was a byte-identical copy. No scientific content edited. Source
subsequently moved to _INBOX/_PROCESSED/2026-06-18/ for audit trail.
```

### confirmation C5 can access the object

```text
YES — via the standing review-track mechanism documented in
`path-a/in-review/README.md`:

  "Review-track artifacts for the Path A construct-definition and
   candidate-construction design effort. These files are filed here
   so contributors (Senior, Contributors 4/5/6, CS, TL) have byte-
   exact access via clean fetch."

C5's access mechanism is identical to the clean-fetch verification in
§3 below: `git fetch origin && git cat-file -p origin/main:<path>`
or `git clone … && git checkout <SHA>`. A MATCH in the §3 table
demonstrates the bytes are reachable from origin at the named path
and at the named SHA. C5 reading at the same SHA receives the same
bytes (sha256-verified above).
```

---

## 2. Spot-check (filing-routing scope, NOT substantive re-review)

The substantive CS feasibility re-review is a separate deliverable that follows this filing. The TL ACTION explicitly notes this turn is "filing and review only" — the deliverable here is that the bytes are filed correctly. I record below only the **filing-level spot-checks** that confirm v0.3 is the right Senior artifact to file, not an evaluation of its content.

```text
file is a proper Senior v0.3 draft:    YES (header line: "# PREREGISTRATION
                                        — V3 FLOOR CHECK (Path A) v0.3";
                                        sign-off line: "— Senior Engineer
                                        (floor-check prereg draft; routes
                                        for review and approval)")
v0.3 self-identifies as revising v0.2:  YES (header note: "Revises v0.2
                                        (a565e46b...) per TL ACTION after
                                        CS feasibility HOLD")
TL-summarized E1–E5 substance present:
  E1 named analyzer                     YES — `v3_floor_check_analyzer.py`
                                        cited 3× in the bytes
  E2 DQ ceiling exact count rule        YES — `19/96` cited 5× (≤19/96 pass,
                                        ≥20/96 fail per TL summary)
  E3 R6 set-level threshold             YES — `10/96` cited 4× (≥10/96
                                        construct-fail per TL summary)
  E4 hop1 lower-Wilson parallel         YES — "Wilson" cited 14×; "lower"
                                        cited 12×; symmetric treatment
                                        across hop1 + hop2
  E5 prompt length: character + class   PRESENT but still uses "MAX DELTA"
                                        (1 occurrence). TL watchpoint #2
                                        for re-review flags this requires
                                        exact numeric tolerance before
                                        approval. Carried forward to
                                        re-review, not edited at filing.
```

## 3. TL watchpoints for re-review (carried forward, not addressed here)

The TL specified four watchpoints for the upcoming CS feasibility re-review. They are recorded here as the standing review docket for that subsequent return; this filing memo does NOT address them substantively.

```text
1. Analyzer lockability — the analyzer path is named in v0.3 but the
   script does not yet exist in the build. CS re-review will check
   whether v0.3 binds the script's content sufficiently for SE to
   produce it under spec, or whether the prereg needs explicit
   interface/IO definitions before the script can be written.

2. Prompt length matching — v0.3 still uses "predeclared MAX DELTA"
   (this filing's spot-check confirmed). CS re-review will require
   conversion to an exact numeric tolerance (e.g., "MAX DELTA ≤ 8
   characters per context") before TL approval.

3. Analyzer digest — the analyzer digest is not yet locked. CS re-review
   will confirm that the prereg requires the analyzer sha to be locked
   at approval time (and locked into the §16-style byte-binding block)
   before any run authorization.

4. No hidden run — confirmed by the §14 routing language in v0.3 ("This
   preregistration authorizes NO run...") and by this filing being
   review-track only. CS re-review will re-check that no §13-style
   open-slot requirement implicitly authorizes execution.
```

All four watchpoints will be addressed in the next CS deliverable (`CS-FEASIBILITY-RE-REVIEW-V0.3-2026-06-18.md` in this same governance dir, or dated forward as the work lands), with PASS / HOLD / FAIL per the established review verdict format. Today's deliverable is filing only.

## 4. Clean-fetch confirmation

Performed after the filing commit landed; `git fetch origin` immediately preceded the verification. Each file's local sha256 compared against `git cat-file -p origin/main:<path> | sha256sum`.

```text
commit                       2972b8ccf3c1c9ad6a031c9916a9cf3422cb1349
push                         0ddef14..2972b8c  main -> main
origin/main HEAD             2972b8ccf3c1c9ad6a031c9916a9cf3422cb1349
local       HEAD             2972b8ccf3c1c9ad6a031c9916a9cf3422cb1349   (match)

per-file verification (origin/main bytes → local bytes):

MATCH  df82b34c4f96e085ea51b8e6e1a735849a39b108b321f79e30b9f20cffa19d5b
       path-a/in-review/PREREGISTRATION-V3-FLOOR-CHECK-v0.3.md
                   ↑ matches inbox Senior source sha exactly
                   ↑ matches TL-expected sha exactly
MATCH  a565e46b56c182a7aee59a7618ec245245cab110df661cecdba5e105299e0363
       path-a/in-review/PREREGISTRATION-V3-FLOOR-CHECK-v0.2.md
                   ↑ superseded predecessor; retained byte-identical
                     as version trail
MATCH  96be27c3ddfd6ad87f25900bf6b0eadb061ad1f38586b947c47f4670cf99a504
       path-a/in-review/README.md
MATCH  3cb3ad419f4efc81b3d3d3cd7056fc29d90d8bc0f63011882f08a0ea0cf0921e
       governance/2026-06-18_v3-floor-check-prereg-v0.3-filing/TL-ACTION-FILE-V3-FLOOR-CHECK-V0.3-2026-06-18.md
MATCH  f5ded606997b2c7fef3abadbab4bd7d6fb29b8751fc9191dd7e7f736f31686a4
       governance/2026-06-18_v3-floor-check-prereg-v0.3-filing/CS-FILING-MEMO-V3-FLOOR-CHECK-V0.3-2026-06-18.md
                   ↑ this file, immediately PRIOR to the §4 commit
                     (the §4 commit's own sha cross-verified on next sweep)
```

**Streamed-from-origin assertion on v0.3:**

```text
git cat-file -p origin/main:path-a/in-review/PREREGISTRATION-V3-FLOOR-CHECK-v0.3.md | sha256
  → df82b34c4f96e085ea51b8e6e1a735849a39b108b321f79e30b9f20cffa19d5b
  → matches the TL-expected v0.3 source sha exactly.
```

This same fetch mechanism is what C5 will use to read the prereg. The bytes on origin are the bytes Senior delivered, byte-for-byte.

All 5 listed artifacts reproduce byte-exact from the shared repository on a clean fetch. **V3 floor-check prereg v0.3 FILED at the TL-specified path; bytes match Senior source; C5 accessible.**

---

— CS Engineer, 2026-06-18 (clean-fetch appendix)

---

## Non-authorizations (carried forward)

```text
- build changes                        blocked (this ACTION is filing/review only)
- N=96 materialization                 blocked
- prompt generation for execution      blocked
- model run                            blocked
- floor-check run                      blocked
- compression                          blocked program-wide
- Claim C                              blocked
- Paper B                              blocked
- certification claim                  blocked
- capability claim                     blocked
- mechanism claim                      blocked
- candidate selection, threshold values, certification evaluation,
  multi-model, Fork A reactivation, public benchmark packaging,
  artifact mutation                    all carried per standing card

Protected surfaces:
- Paper 2 v1.0 tag (paper2-cells01-03-v1.0, 41c033fc...) +
  tagged manuscript blob (7d6706a3...): never moved.
- tier0-run/ directory: sealed; no new files.

The Path A FP16 K=5 FAIL remains closed.
```

---

— CS Engineer, 2026-06-18
