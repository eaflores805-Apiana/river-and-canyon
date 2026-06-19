# C5 RETURN — Hop1 Stability Investigation Preregistration v0.1 Claim-Risk

**Prepared by:** Contributor 5 (adversarial-foresight / claim-risk)
**To:** Team Lead · **Cc:** CS, Senior, New Senior, Manager
**Date:** 2026-06-18
**Object requested:** `PREREGISTRATION — HOP1 STABILITY INVESTIGATION (Path A) v0.1`
**Status:** review return. Authorizes nothing; locks nothing.

---

## Verdict

```text
HOLD — ARTIFACT ACCESS (filing-not-yet-propagated). The named object is not at a readable
HEAD, and a pre-registration is lock-before-look — not cleared unread.

Checked this turn:
  - Fresh clone at HEAD 9744e0ee5ea377b86fc24211511deb330bb39a1a.
  - find . for *HOP1*STABILITY* → no file.
  - grep -rIl "HOP1 STABILITY" → only MAP.md + an unrelated composite-gate-run memo, NOT the prereg.
  - search for the declared digest 71f00482… across all .md → no match.
  - in-review holds the full prior lineage (constructibility v0.1–v0.4, floor-check v0.1–v0.4,
    composite-gate v0.2, my prior C5 returns) but NOT the hop1-stability prereg.
  - /mnt/user-data/uploads/ → only the Hash-Integrity files.
This is the same routing-order situation as the composite-gate v0.2 first pass: the TL notice
asks CS to FILE and asks C5 to REVIEW in one notice; the filing is upstream and has not reached
the remote I can fetch.
```

The HOLD lifts the instant CS's filing lands at the readable path with the digest the TL notice
already requires (I verify against it — the declared `71f00482…`). The seven focus items, four
watchpoints, and TL questions A–D are answered below as standing rulings, so the verdict
converts on sight IF the bytes match. Two of these I can rule on with high confidence now,
because they are recurring traps this seat has named repeatedly and the TITLE alone raises them.

## 0. Scope note — confirming a routing description, not bytes

```text
I have the TL notice's framing, not the prereg. Every ruling below is "resolved IF the bytes
match"; the PASS waits on the filed object. A changelog is not the artifact (the discipline
that caught my wrong "80/96 = hop2 failure" inference two turns ago).
```

## The two highest-confidence rulings (raised by the title + TL framing, before the bytes)

```text
RULING — "STABILITY" IS A MODEL-PROPERTY WORD AND MUST BE BOUNDED TO MATERIALIZATION-LEVEL
  ADMISSIBILITY (focus item 4, watchpoint B). This is the load-bearing claim-risk surface of
  the whole object, and it's in the TITLE. "Hop1 stability" reads naturally as "the model
  STABLY does hop1" — a capability/disposition claim about the model. The only claim-safe
  meaning is about the CONSTRUCTION's MATERIALIZATIONS: "does hop1 clear its admissibility floor
  CONSISTENTLY ACROSS FRESH BLOCKS of the construction" — a property of the construction-under-
  this-load measured across independent materializations, NOT a property the model possesses.
  REQUIRED: every branch label (STABLE-ADMISSIBLE / STABLE-INADMISSIBLE / UNSTABLE) must be
  explicitly defined as "the floor verdict is/ isn't unanimous across the fresh blocks" — a
  statement about cross-block verdict agreement, never "the model is stable/unstable at hop1."
  Watchpoint B answer: "stability = unanimous floor verdict across fresh blocks" IS claim-safe
  AND mechanically clear PROVIDED the unanimity is over the per-block floor VERDICTS (each block
  clears or doesn't, by the locked Wilson rule) and "stable" is never detached from "across
  these blocks, at this load." It is the right definition; the risk is purely that "stable"
  travels as a model word — so the bytes must bind it to cross-block verdict agreement at every
  use, including the branch names and the carry-up.

RULING — THE P-ROLE HYPOTHESIS IS THE IMPORTED-FROM-SEEN-DATA TRAP, AND MUST BE A FRESH-TESTED
  CONFIRMATORY HYPOTHESIS WITH A PRE-COMMITTED RULE (focus item 2, watchpoint C). A pattern
  noticed in the already-seen floor-check/composite data (a P-role distractor effect) cannot be
  asserted as a finding — it can only be RE-TESTED on fresh disjoint data under a rule fixed
  before that data is seen. This is the exact shape of the lock-before-look discipline: the
  seen data GENERATED the hypothesis; only fresh data can TEST it; and the test rule (what P-role
  pattern, at what threshold, counts as confirmation vs null) must be declared before the fresh
  blocks are scored, or it is post-hoc fishing dressed as confirmation. REQUIRED: the prereg
  must (a) state the P-role pattern as a HYPOTHESIS derived from seen data, explicitly NOT a
  finding; (b) pre-declare the exact fresh-data test and its decision rule; (c) pre-declare the
  NULL (what fresh result would DISCONFIRM the P-role hypothesis), so confirmation is falsifiable;
  (d) bar the seen data from the confirmatory test (anchors only, focus item 1). Watchpoint C
  answer: it is stated narrowly enough ONLY IF all four hold; the narrowing that matters most is
  (c) — a confirmatory hypothesis with no pre-stated disconfirming outcome is not confirmatory,
  it is a search for support.
```

## The seven focus items (rulings; byte-confirm on filing)

```text
1. ANCHORS (001..096, 097..192 as anchors only, not fresh evidence) — RULING: required, and it
   is the same bar applied to the composite gate (seen data is informational/barred from being
   evidence). BYTE-CHECK: the prereg must state the floor-check (001..096) and composite-gate
   (097..192) materializations are ANCHORS/context only — used to locate the hypothesis, NEVER
   counted as stability evidence — and that stability is evaluated ONLY on the fresh blocks
   (193..768 per the TL seed note). Confirm no seen-block verdict enters the unanimity count.
2. P-ROLE HYPOTHESIS — see the high-confidence ruling above. Fresh-tested, pre-committed rule,
   pre-stated null, seen data barred.
3. EXPLORATORY COVARIATES descriptive-only — RULING: required, and this is a fishing surface. A
   stability investigation logging multiple covariates can mine them post-hoc for a "finding."
   BYTE-CHECK: secondary covariates must be labeled DESCRIPTIVE/EXPLORATORY, explicitly NOT
   hypothesis tests, with NO decision rule attached to them and NO claim permitted from them
   without a fresh pre-registered test — the same "a descriptive byproduct is not a result"
   discipline from the K-sweep. Any covariate that gets a threshold becomes a hidden hypothesis
   and must be declared as one or stripped.
4. BRANCH LANGUAGE bounded to materialization-admissibility — see the high-confidence ruling.
   STABLE-ADMISSIBLE / STABLE-INADMISSIBLE / UNSTABLE = cross-block floor-verdict agreement at
   this load, never model capability.
5. MECHANISM BOUNDARY (no attention/binding/reasoning/shortcut/mechanism labels) — RULING:
   required, and "stability" investigations are especially prone to mechanism leak ("the model's
   hop1 binding is unstable"). BYTE-CHECK: zero mechanism vocabulary; the covariate logger
   (v3_hop1_covariate_logger.py) must log POSITIONAL/STRUCTURAL covariates (where tokens sit,
   item properties), never named mechanisms — the positional-not-mechanistic discipline from the
   off-map arc, carried to this object. Confirm covariate NAMES are positional in surface form.
6. COMPOSITE BOUNDARY (not a composite-gate rerun; does not reopen certification) — RULING:
   required and structurally important. This is a HOP1 (single-component) investigation; it must
   not touch the composite gate or its certification question. BYTE-CHECK: explicit statement
   that this investigates hop1 floor-verdict stability across blocks, is NOT the composite gate,
   does NOT produce or bear on composite certification, and the composite-gate prereg is
   untouched. (Watchpoint D ties in: hop2-control-fail must not expand this into a composite or
   full-component study — see below.)
7. DOWNSTREAM BOUNDARY (no compression/Claim C/Paper B/capability/mechanism/certification leak)
   — RULING: required; the forbidden block must carry the full perimeter, same as the floor-check
   and composite-gate prereg. BYTE-CHECK: confirm all named leaks are explicitly forbidden.
```

## TL watchpoints A and D (B and C answered above)

```text
A. IS 6 FRESH BLOCKS THE RIGHT FIXED SIZE? — This is primarily a power/feasibility call
   (CS + TL/Manager), not a claim-risk call, and I defer the number. The CLAIM-RISK constraint
   on it: whatever block count is chosen must be FIXED BEFORE the run and the unanimity rule
   defined over exactly that count — 6 blocks must not become "5 if the 6th is inconvenient" or
   "7 to break a tie" after look (the K-sweep one-computation-per-cell stop-rule, applied to
   blocks). And the cost (6 × 96 × 2 = 1,152 prompts) is a Manager resourcing decision. Whether
   6 is right for power is CS/TL/Manager; whether it is LOCKED is the claim-risk requirement.
   One claim-risk note: if 6 blocks is chosen to make "unanimous across blocks" a meaningful
   bar (more blocks = stricter unanimity), that logic should be stated, so the block count is
   principled, not arbitrary.

D. IS HOP2-CONTROL-FAILURE HANDLED SAFELY, WITHOUT BECOMING A BROADER COMPONENT-STABILITY STUDY?
   — RULING: this is a real scope-creep risk and the watchpoint is well-placed. The investigation
   is about HOP1 stability; hop2 enters only as a CONTROL (is the second component still
   admissible on these fresh blocks, so a hop1 reading is interpretable). A HOP2-CONTROL-FAIL
   branch must do ONE thing: declare the block's hop1 reading uninterpretable (hop2 not
   admissible → can't isolate hop1) and route to examine/re-pre-register — it must NOT silently
   expand the investigation into "hop2 stability" or "component stability" generally, which would
   be scope the prereg didn't lock. BYTE-CHECK: the HOP2-CONTROL-FAIL branch is bounded to "this
   block's hop1 result is uninterpretable," NOT a finding about hop2, and does not convert the
   study into a two-component stability investigation. Keep it a control, not a second subject.
```

## The standing critical guard for this object

```text
"STABILITY" IS THE OVER-READ ENGINE HERE, exactly as "certification" was for the composite gate.
The pull is to read "hop1 is stable across blocks" as "the model reliably does hop1" — a
capability claim. Every ruling above is a guard on that pull. Even a clean STABLE-ADMISSIBLE
result yields ONLY "hop1 cleared its admissibility floor unanimously across the fresh blocks of
this construction at this load" — a cross-block materialization-admissibility statement, never
"the model is stable at hop1," never capability, never mechanism. If the bytes' branch language
or carry-up says more, that is the validity→capability step, and it is a HOLD regardless of the
other rulings.
```

## Recommendation

```text
1. CS files v0.1 at the readable path with the declared digest (the TL notice requires it). On
   filing, this HOLD lifts and I review the actual bytes.
2. On review, priorities: the "stability"-bounding at every branch label and the carry-up (the
   over-read engine); the P-role hypothesis as fresh-tested with a pre-stated NULL (not just a
   pre-stated confirmation); the exploratory-covariate fishing guard (no thresholds on secondary
   covariates); and the hop2-control-fail scope bound (control, not a second subject).
3. Do not lock until claim-risk clears the actual bytes. CS feasibility (seed realizability
   193..768, the two new tools, scale, covariate extractability) is independent and must also clear.
Requires CS verification: the filing + digest; seed-range realizability; the two new tools;
covariate mechanical-extractability. Authorization implication: none.
SEPARATE FLAG (not this object): the search surfaced a 2026-06-18_v3-composite-gate-run governance
dir with a "FILE MISSING MANIFEST" TL action — i.e. the composite-gate RAN since my last review
and has a manifest issue. That is not the hop1 object and I make no ruling on it, but if a
composite-gate run occurred, its result routes to claim-risk review under the v0.2 prereg's
result-time guard (a clean PASS is gate-cleared-this-run, never upgraded). Flagging so it is not
lost; it is a separate review when routed.
```

## Boundaries checked

```text
- No verdict on unread bytes: object confirmed not-at-readable-HEAD (clone at 9744e0e, exhaustive
  find/grep/digest-search, uploads) and HELD; rulings are description-level with every line marked
  byte-check-required.
- No run, materialization, prompt generation, tooling creation, composite-gate retry, compression,
  INT8/INT4, Claim C, or Paper B authorized or proposed. Sets no threshold; recommends no path.
- "Stability" treated as cross-block materialization-admissibility, never model capability; P-role
  as fresh-tested hypothesis not seen-data finding; mechanism vocabulary forbidden; composite gate
  not reopened; the K=5 FAIL stays closed.
```

---

**The one to carry up:** I cannot verdict the hop1 stability prereg v0.1 because its bytes are not at a readable HEAD — same routing-order situation as the composite-gate v0.2 first pass (the TL notice asks CS to file and C5 to review in one notice; the filing hasn't propagated; clone at `9744e0e` shows the full prior lineage in-review but not this object, and no file matches the declared digest `71f00482…`). The access HOLD lifts the instant CS's filing lands with that digest. Two rulings I can make with high confidence from the title and TL framing now: first, "STABILITY" is a model-property word and the load-bearing claim-risk surface — it must be bounded at every branch label and the carry-up to CROSS-BLOCK MATERIALIZATION-ADMISSIBILITY ("hop1 clears its floor unanimously across the fresh blocks of this construction at this load"), never "the model is stable at hop1"; watchpoint B's "stability = unanimous floor verdict across fresh blocks" is the right, mechanically-clear definition provided "stable" is never detached from "across these blocks, at this load." Second, the P-ROLE HYPOTHESIS is the imported-from-seen-data trap and must be a fresh-tested confirmatory hypothesis with a PRE-STATED NULL (not just a pre-stated confirmation — a confirmatory hypothesis with no disconfirming outcome is a search for support), the seen 001..096/097..192 blocks barred to anchors-only. The other focus items map cleanly: exploratory covariates descriptive-only with no thresholds (the fishing guard), mechanism vocabulary forbidden and covariate names positional in surface form, the composite gate not reopened, hop2-control-fail bounded to "this block's hop1 reading is uninterpretable" and NOT expanded into a component-stability study (watchpoint D), and the full downstream-leak perimeter. The standing guard: "stability" is the over-read engine here exactly as "certification" was for the composite gate — even a clean result yields only a cross-block admissibility statement, never capability or mechanism. File v0.1 with its digest and the verdict converts on sight; do not lock until claim-risk clears the actual bytes. Separately flagged, not this object: the search shows the composite gate appears to have RUN (a 2026-06-18 composite-gate-run governance dir with a missing-manifest TL action), which when routed gets its own claim-risk review under the v0.2 result-time guard — flagging so it is not lost.

— Contributor 5
