# CAL-Q-FINDING-DIAGNOSTIC-PLAN-v0.1

**Version:** v0.1. River and Canyon program. CAL-Q FINDING TRACK (format-sensitive abstention / difficulty-abstention coupling). Per Manager direction "Open CAL-Q Finding Track, Not a D4 Rescue."
**Status:** MODEL-FREE PLANNING. This artifact designs diagnostics; it authorizes no model execution. It is a finding-track artifact, separate from Paper A and from the closed D4 certification-readiness route. Anchored on origin/main HEAD 3b7491b.
**Owner split:** Senior (drafter — keep mechanisms hypothetical; separate format / difficulty / combined effects) → CS (verify the diagnostics are cleanly separated, do not reopen D4 rescue, imply no execution authorization) → Team Lead (route as a finding-track artifact; keep Paper A and this track separate) → Manager.

---

## 0. What this track is, and is not

```text
IS:  a model-free plan to design how CAL-Q's finding could LATER be tested.
IS:  an attempt to disentangle three candidate drivers of one observed collapse.
NOT: a D4 rescue. D4 is closed as a certification-readiness route and stays closed.
NOT: an execution authorization. No run is approved by this document.
NOT: a mechanism claim. The mechanism is unresolved; this plan is how one would resolve it.
```

This track exists because CAL-Q exposed something worth preserving: a query-side change that successfully created clean-side difficulty *also* collapsed defective abstention to zero. Whether that collapse was driven by the format change, the difficulty increase, or their combination is the open question the diagnostics below are designed to answer — later, under separate execution authorization.

## 1. The finding, stated exactly (byte-anchored)

```text
What was observed in the D4 key-value family (Qwen2.5-3B, FP16):
  - Direct-query content levers (CAL-A/B/C/E) preserved defective abstention:
    abstention on key-absent items stayed high (e.g. CAL-B 0.925), while clean
    accuracy stayed at/near ceiling (0.95-1.00).
  - The code-book query lever (CAL-Q) was the FIRST lever to move clean accuracy
    materially off ceiling: clean strict accuracy 0.65.
  - On that same lever, defective abstention COLLAPSED: abstention 0.00,
    false-emission 1.00 (all 40 key-absent items received a value emission;
    confirmed not a scoring artifact by the form-level positive control).
```

The two changes — query format (direct → code-book alias resolution) and clean-side difficulty (ceiling → 0.65) — were introduced *together* in CAL-Q. That confound is exactly what the diagnostics are built to break.

## 2. The core question

```text
Did defective abstention collapse because of:
  (a) the query FORMAT change (the code-book / indirection itself), or
  (b) the increased lookup DIFFICULTY (independent of how it was induced), or
  (c) the COMBINATION (format and difficulty together, neither alone sufficient)?
```

A clean answer requires varying format and difficulty *independently*, which CAL-Q did not. The three branches below each hold one of these fixed while moving the other, plus one branch that tests a gentler query-side lever.

## 3. Shared measurement definitions (apply to all branches)

So the branches are comparable and pre-declared rather than fit after the fact, every branch uses the same operational definitions:

```text
ABSTENTION PRESERVED:   defective (key-absent) concept-level abstention >= 0.80
                        (the program's preserved-discrimination floor), measured
                        by the same per-item read used in Paper A, with the
                        strict-vs-concept scorer audit applied so a parser artifact
                        cannot be mistaken for a collapse.
ABSTENTION COLLAPSE:    defective concept-level abstention <= 0.20
                        (operationally, near-total value emission on key-absent items).
INTERMEDIATE:           0.20 < abstention < 0.80 — reported as partial, not forced
                        into either bin.
CLEAN-SIDE DIFFICULTY
  MOVEMENT:             clean strict accuracy drops from ceiling (>=0.95) into the
                        off-ceiling band; "meaningful" movement = clean accuracy
                        <= 0.85 (a >= ~0.10 absolute drop from ceiling). Reported
                        as the actual value, not just the bin.
SCORER CONTROL:         every branch runs the four-way report (strict / concept /
                        true-false-emission / format-artifact) so an apparent
                        collapse is confirmed real (as in CAL-Q) or reversed as an
                        artifact (as in CAL-E) before it is interpreted.
HELD-FIXED BASELINE:    each branch is read against the SAME direct-query clean
                        baseline and the SAME content set; only the one declared
                        variable moves.
```

These are decision rules fixed before any run, in the program's pre-declared-rule discipline. No threshold here is a certification target; these are diagnostic bins for reading a future result, not a stress gate.

---

## 4. Diagnostic branch D1 — Format-only change

**Goal.** Change query format away from direct lookup *without* materially increasing lookup difficulty.

**Question.** Does abstention collapse when format changes but difficulty stays low (clean accuracy stays near ceiling)?

```text
1. WHAT CHANGES:        the query FORM — a non-direct phrasing that does NOT add an
                        alias-resolution or multi-step retrieval burden. Candidate:
                        a rephrased-but-equivalent query (e.g. "What value is stored
                        under key K?" vs the direct "K?") that alters surface form
                        while the lookup remains a single-step direct retrieval.
2. WHAT IS HELD FIXED:  the content set; the single-step retrieval difficulty; the
                        abstention target form; the scorer; the clean baseline.
3. ABSTENTION PRESERVED: defective concept-abstention >= 0.80 (per §3).
4. ABSTENTION COLLAPSE:  defective concept-abstention <= 0.20 (per §3).
5. CLEAN-SIDE DIFFICULTY MOVEMENT: EXPECTED MINIMAL — clean accuracy should stay
                        >= 0.95. If clean accuracy drops materially, D1 has FAILED
                        its design (it added difficulty) and is void as a format-only
                        test — re-design the form to be easier before interpreting.
6. SUPPORTS FORMAT SENSITIVITY: abstention collapses (<=0.20) WHILE clean accuracy
                        stays near ceiling (>=0.95). Format alone moved abstention.
7. SUPPORTS DIFFICULTY-COUPLING: abstention PRESERVED (>=0.80) with clean near
                        ceiling — i.e. format change alone did NOT collapse abstention,
                        consistent with difficulty (not format) being the driver.
8. LEAVES MECHANISM UNRESOLVED: intermediate abstention (0.20-0.80), or D1 fails
                        its difficulty-neutral design (item 5), so format and
                        difficulty cannot be separated on this branch.
```

---

## 5. Diagnostic branch D2 — Difficulty-only change

**Goal.** Increase lookup difficulty while preserving the direct-query format as much as possible.

**Question.** Does abstention collapse when difficulty rises but query format stays close to direct lookup?

```text
1. WHAT CHANGES:        clean-side DIFFICULTY, induced WITHOUT a query-format
                        departure — e.g. by content-side load (larger key set,
                        more distractor keys, longer values) that lowers clean
                        accuracy while the query itself remains a direct single-step
                        lookup. (Note: D4 content levers did NOT move clean off
                        ceiling; D2 must push content-side load harder than those
                        did, which is its design challenge — see §7 risk.)
2. WHAT IS HELD FIXED:  the direct-query FORMAT; the abstention target form; the
                        scorer; the clean baseline reference.
3. ABSTENTION PRESERVED: defective concept-abstention >= 0.80 (per §3).
4. ABSTENTION COLLAPSE:  defective concept-abstention <= 0.20 (per §3).
5. CLEAN-SIDE DIFFICULTY MOVEMENT: REQUIRED — clean accuracy must reach <= 0.85 for
                        the branch to be a valid difficulty test. If content-side
                        load cannot move clean off ceiling (the D4 problem), D2 is
                        INCONCLUSIVE-BY-CONSTRUCTION, not evidence either way.
6. SUPPORTS DIFFICULTY-COUPLING: abstention collapses (<=0.20) as clean accuracy
                        falls (<=0.85) under direct-query format. Difficulty alone
                        moved abstention.
7. SUPPORTS FORMAT SENSITIVITY: abstention PRESERVED (>=0.80) even as difficulty
                        rises under direct format — i.e. difficulty alone did NOT
                        collapse abstention, consistent with format (not difficulty)
                        being the driver.
8. LEAVES MECHANISM UNRESOLVED: intermediate abstention (0.20-0.80), or D2 cannot
                        induce the required clean-side movement under direct format
                        (item 5), so difficulty's independent effect is untestable
                        on this branch.
```

---

## 6. Diagnostic branch D3 — Gentle indirect query

**Goal.** Test a milder non-content query lever — a confirm-then-return form — to see whether a gentler query-side departure can add clean difficulty while preserving abstention.

**Example form.**

```text
First confirm whether key K is present.
If present, return its value.
If absent, return NONE.
```

**Question.** Can a gentler query-side lever preserve abstention while adding some clean-side difficulty?

```text
1. WHAT CHANGES:        the query form to a confirm-then-return structure that makes
                        presence/absence an EXPLICIT first step (unlike the code-book
                        lever, which buried indirection in alias resolution). This is
                        a query-side lever, but one designed to CUE the abstention
                        decision rather than obscure it.
2. WHAT IS HELD FIXED:  the content set; the abstention target form (NONE); the
                        scorer; the clean baseline reference.
3. ABSTENTION PRESERVED: defective concept-abstention >= 0.80 (per §3).
4. ABSTENTION COLLAPSE:  defective concept-abstention <= 0.20 (per §3).
5. CLEAN-SIDE DIFFICULTY MOVEMENT: SOME expected (the confirm step adds a hop);
                        report the actual clean accuracy. D3 is most informative if
                        clean accuracy moves off ceiling at all (even modestly).
6. SUPPORTS "CODE-BOOK WAS UNIQUELY HOSTILE": abstention PRESERVED (>=0.80) WITH
                        some clean-side difficulty (clean < 0.95). A gentle query
                        lever both added difficulty and kept abstention — so the
                        code-book form, not query-indirection in general, drove the
                        CAL-Q collapse.
7. SUPPORTS "QUERY DEPARTURE GENERALLY THREATENS ABSTENTION": abstention collapses
                        (<=0.20) under the gentle lever too — so departing from direct
                        lookup tends to threaten abstention in this construct
                        regardless of how gently it is done.
8. LEAVES MECHANISM UNRESOLVED: intermediate abstention (0.20-0.80), or no clean-side
                        movement at all (the confirm step added no difficulty), so the
                        gentle-vs-hostile distinction cannot be drawn.
```

---

## 7. Reading the three branches together

The branches are designed so their *joint* pattern points at one of the three drivers. Indicative readings (each still subject to the per-item scorer control, and none load-bearing on a single branch):

```text
  D1 collapse + D2 preserved   -> FORMAT sensitivity is the likely driver.
  D1 preserved + D2 collapse   -> DIFFICULTY-abstention coupling is the likely driver.
  D1 preserved + D2 preserved  -> neither alone sufficient; COMBINATION (the CAL-Q
   + (CAL-Q still collapsed)       confound) is implicated — abstention survives each
                                   single change but not both together.
  D1 collapse + D2 collapse    -> both channels independently threaten abstention;
                                   the construct is fragile on multiple axes.
  D3 preserved + difficulty     -> the code-book form was uniquely hostile; a gentler
                                   query lever is a candidate path (NOT a D4 reopening
                                   by itself — see boundary).
  D3 collapse                  -> query-side departure broadly threatens abstention here.
```

Each cell is a *hypothesis the pattern would support*, not a proof. Two or three branches agreeing is suggestive; a single branch is not decisive, and any branch that fails its own design constraint (D1 adding difficulty, D2 failing to move clean, D3 adding no difficulty) is void rather than informative.

## 8. Claim boundaries (binding)

**The plan preserves this safe claim (and nothing stronger):**

```text
In the D4 key-value family, direct-query defective abstention was robust across
content-lever variants, but did not transfer to the code-book query format. The
first query-side lever that produced meaningful clean difficulty also collapsed
defective abstention to zero. This suggests abstention behavior in this construct
is format-sensitive and may be coupled to retrieval difficulty.
```

**The plan does NOT claim, and no diagnostic result here may be read as:**

```text
Models cannot abstain.
All absence-defined tasks fail.
D4 can never work.
The seam is false.
Compression fragility has been tested.
The mechanism is already established.
```

The diagnostics are how the mechanism *would be* investigated; running them is a separate, future, authorized step, and even then the result would be scoped to this construct and model, not generalized.

## 9. Relationship to Paper A

```text
Paper A remains first and is not delayed by this track.
Paper A already states the SAFE version of this finding (the code-book lever
  collapsed abstention; §3 worked case) and does not depend on resolving the
  mechanism. This track is FUTURE WORK.
This plan introduces NO claim-safety issue for Paper A: it does not strengthen,
  weaken, or contradict any Paper A claim; it only designs how a question Paper A
  leaves open could later be answered. If a CS or TL review finds any conflict with
  a Paper A claim, that conflict — not the diagnostic design — takes priority.
```

## 10. Boundary (closed gates — unchanged)

```text
No model execution.       No second compression rung.
No D4 rescue.             No full ladder.
No CAL-Q rerun.           No Claim C activation.
No certification run.     No public benchmark packaging.
No compression.           No funder-facing release.
No INT8 / INT4 stress.    No SBIR submission.
```

This is planning only. The route stays closed. The finding stays alive.

## 11. For CS verification (what to check)

```text
- That D1 (format-only) and D2 (difficulty-only) are genuinely separated — D1's
  design forbids material difficulty movement, D2's forbids a format departure — so
  a result cannot be claimed for one driver while secretly moving the other.
- That no branch, as written, constitutes or implies a D4 certification-readiness
  rescue: these are mechanism diagnostics, not an attempt to produce a certifiable
  off-ceiling baseline. (D3 in particular: a gentle lever that preserved abstention
  would be a FINDING about the construct, and a candidate for future design work —
  it is not, by itself, a re-opened D4 route, and must not be packaged as one.)
- That no execution authorization is stated or implied anywhere in the plan.
- That every branch carries the per-item scorer control (so a future apparent
  collapse is confirmed-or-reversed before interpretation, per CAL-E/CAL-Q).
```

— Senior Engineer
