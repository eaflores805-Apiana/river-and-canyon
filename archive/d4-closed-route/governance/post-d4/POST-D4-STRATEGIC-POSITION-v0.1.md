# POST-D4-STRATEGIC-POSITION-v0.1

**Version:** v0.1. River and Canyon program. Strategic position memo (model-free synthesis), requested by the Manager to prevent drift after the D4 pivot.
**Status:** model-free strategy. Synthesizes the current record; recommends a near-term north star and a next-step ordering; authorizes nothing. Anchored on origin/main HEAD 99f8d0b.
**Question to answer:** is the near-term program now best framed as Tier 1 eval-validity instrumentation, with seam work deferred until a valid baseline family exists?
Owner/drafter: Senior Engineer · Team Lead: routing/synthesis · Manager: the strategic decision this memo recommends.

---

## 1. The one-line answer

Yes — with a precise reason. The hybrid (**instrument first, seam deferred**) is not
a diplomatic compromise between two live options; it is what the program's
**dependency structure forces.** The seam experiment is blocked at step zero — it
has no valid baseline family to run against — while the instrument is already
earned and shippable. You cannot run the seam now even if you chose to; you can
ship the instrument now. That asymmetry, not a preference, is the recommendation.

## 2. The current record (the evidence both options are judged against)

```text
EARNED (instrument / Tier-1 eval-validity findings — each an artifact):
  - survival ≠ correctness            (Paper 1, released)
  - correctness ≠ constructibility    (Paper 2, Claim B, released)
  - hash integrity ≠ construct validity (Hash-Integrity note)
  - certification-before-retention gate (Paper 3, D1–D7, released)
  - scorer/parser artifact caught      (CAL-E none/NONE; per-item-read discipline)
  - lever-validity failure identified  (CAL-Q: a difficulty lever can move the
    number by destroying the measured behavior — construct-validity failure of the
    lever itself)
  - a route killed under a pre-declared rule (D4 PIVOT — the discipline produces
    decisions, not just analyses)
  - format-sensitive abstention finding (CAL-Q, scoped)
OPEN (seam track):
  - the seam question is UNANSWERED (no certified compression rung has ever run;
    the program is PRE-STRESS in its official sequence)
  - D4 was the baseline-construction attempt and is CLOSED on PIVOT
  - NO valid baseline FAMILY currently exists → seam stress has nothing to run
    against
```

## 3. Option A — Instrument-as-deliverable

```text
1. EVIDENCE THAT SUPPORTS IT:
   Three released papers + a finding + two caught measurement artifacts (parser
   bug, lever-validity failure) + a route killed under a pre-declared rule. This
   is a body of completed, defensible eval-validity work. It exists NOW.
2. EVIDENCE THAT WEAKENS IT:
   The findings are scoped to a narrow synthetic task family (key-value lookup,
   3B/FP16). "Eval validity broadly" is not yet demonstrated across diverse
   evals; the generality of the instrument is asserted more than shown. Whether
   there is a NAMEABLE external market is not yet checked (the deferred literature
   check is the gate).
3. WORK IT MAKES URGENT:
   Consolidate the methodology into a transferable form; run the literature check
   to position it against published work and test the market claim; draft the
   rejection-audit control (the one structural gap in the control stack).
4. WORK IT DEFERS:
   Alternative baseline-family search and any compression stress — explicitly
   parked until the instrument is consolidated.
5. CLAIM IT CAN SUPPORT NOW:
   "We have a fail-closed eval-validity discipline that catches specific,
   demonstrated failure modes (preserved error, shortcut exploitation, scorer
   artifacts, lever-validity failures) in a constructed task family, and it
   produces decisions, not just analyses."
6. CLAIM IT CANNOT YET SUPPORT:
   "This discipline generalizes to arbitrary evaluations" (scope is one family),
   and "there is a market for it" (unverified — needs the literature/market check).
```

## 4. Option B — Seam-as-deliverable

```text
1. EVIDENCE THAT SUPPORTS IT:
   The seam is a genuine, unanswered research question, and it is the program's
   original motivation. Nothing has shown the seam does NOT exist.
2. EVIDENCE THAT WEAKENS IT:
   Decisive for near-term framing: the seam experiment cannot START. It requires
   a valid baseline family (off-ceiling AND discrimination-preserving), and the
   one family built (D4) is closed on PIVOT with no replacement in hand. Every
   purpose-built construction so far failed its baseline gate. The seam track is
   blocked at step zero, not merely slow.
3. WORK IT MAKES URGENT:
   An alternative-task-family search — find ANY family that can host a calibrated
   baseline — which is open-ended, unbudgeted in time, and has already consumed
   the program's effort once (the entire D4 arc) without yielding one.
4. WORK IT DEFERS:
   The instrument consolidation — i.e. it defers shipping the thing already earned
   in order to chase the thing not yet reachable.
5. CLAIM IT CAN SUPPORT NOW:
   Very little beyond "the seam is an open question we intend to test." It cannot
   claim any seam result, because none exists.
6. CLAIM IT CANNOT YET SUPPORT:
   "Compression causes (or does not cause) a compositional seam" — UNANSWERED.
   "We can measure compression fragility" — the program is pre-stress; it cannot.
```

## 5. The decisive asymmetry

```text
Option A's product EXISTS and is defensible today; its open question is reach
(generality, market), answerable by consolidation + a literature check — cheap,
bounded work.
Option B's product DOES NOT EXIST and cannot be produced until a prerequisite
(valid baseline family) is met that the program has tried and failed to meet
once; its open question is existence, answerable only by open-ended search.
You can ship A now. You cannot run B now. A hybrid that does A first and holds B
open is therefore not splitting the difference — it is sequencing by what is
actually buildable. Choosing B-first would mean deferring a finished product to
chase a blocked one; choosing A-only would mean abandoning the program's
motivating question, which the evidence does not require (the seam is unanswered,
not refuted).
```

## 6. Recommendation

```text
RECOMMENDED NEAR-TERM NORTH STAR: Hybrid — instrument first, seam deferred.
```

```text
This matches the Manager's stated prior, and the memo's contribution is the
REASON it is right rather than merely agreeable: the dependency structure forces
it. Concretely:
  - The near-term CENTER OF GRAVITY is the eval-validity instrument, because that
    is what the evidence has already earned and it is shippable now.
  - The seam remains an OPEN RESEARCH QUESTION, explicitly not abandoned, deferred
    until a valid baseline family exists (which is itself one of the things the
    instrument work may help identify — see §7 item 4).
  - The hybrid is falsifiable and reversible: if the alternative-family search
    (a deferred, lower-priority track) turns up a baseline family that passes the
    gates, the seam track reopens with the instrument now strong enough to certify
    it honestly. Instrument-first makes the eventual seam work BETTER, not just
    later.
```

```text
ONE HONEST CAVEAT on the recommendation: "instrument-as-deliverable" carries an
implicit market claim (someone wants an eval-validity auditing capability) that is
NOT yet verified. The recommendation is sound on the EVIDENCE (the instrument is
what's earned); it is NOT yet sound as a BUSINESS bet until the literature/market
check is run. The memo recommends the instrument as the near-term TECHNICAL center
of gravity; whether it is also a fundable PRODUCT is the first thing item 1 below
must resolve. Do not let "instrument-as-deliverable" silently smuggle in
"instrument-as-confirmed-market."
```

## 7. Recommended next-step ordering

Ordered by what unblocks the most and costs the least:

```text
1. LITERATURE CHECK  (FIRST — it is the gate to everything else)
   It answers two questions both options need: (a) is the methodology record
   institutional memory or a publishable paper? (b) does Tier 1 eval-validity
   auditing have a NAMEABLE market? Until this is run, the strategic recommendation
   rests on an unverified market premise (§6 caveat). It is cheap, model-free, and
   it gates the value of items 2–3. RUN it (actual search of published work on
   shortcut learning, construct validity in eval, pre-registration, eval
   reproducibility), do not assert from pattern-matching.

2. §11 REJECTION-AUDIT CONTROL  (SECOND — unblocked, bounded, and overdue)
   The one structural gap in the control stack (it is asymmetric — nine controls
   distrust good numbers, ~none second-guess a rejection). CAL-Q is the ideal case
   study (a rejection where reading the bytes CONFIRMED the rejection — exactly
   when the audit discipline matters). It is a bounded extraction from the
   methodology record, now fully unblocked by the D4 resolution.

3. TIER 1 METHODOLOGY CONSOLIDATION  (THIRD — but its FORM depends on item 1)
   Consolidate the methodology into a transferable deliverable. Whether this is an
   internal playbook or an external methods paper is DECIDED by the literature
   check (item 1) — so it follows it. Do not consolidate into the wrong form
   before knowing which form is warranted.

4. ALTERNATIVE TASK-FAMILY SEARCH  (FOURTH — the seam track's prerequisite, lower
   priority, explicitly deferred)
   The search for a family that can host a calibrated baseline. This is the only
   item that serves the SEAM track, and it is correctly LAST among the near-term
   options because it is open-ended and the hybrid defers the seam. It is not
   dropped — it is the path by which the seam eventually reopens — but it does not
   precede the instrument work.

5. FUTURE DIAGNOSTICS FOR CAL-Q FORMAT-SENSITIVE ABSTENTION  (FIFTH — gated, needs
   model execution, not near-term)
   The D-1–D-4 diagnostics (separate format from difficulty, gentler lever,
   cross-model, cross-family) that would upgrade the CAL-Q hypothesis toward a
   finding. These require model runs (separate Manager authorization) and are a
   finding-track deepening, not a near-term strategic priority. Park until the
   instrument center of gravity is established.
```

```text
RATIONALE FOR THE ORDERING: items 1–3 are the instrument-first center of gravity,
sequenced so the cheap gate (literature check) precedes the work whose FORM it
determines (consolidation). Items 4–5 are the deferred seam/finding tracks, kept
on the board so nothing is abandoned, but explicitly after the instrument work.
The single most important sequencing point: the literature check is FIRST because
it is the only item that can invalidate the §6 caveat, and every downstream
decision (paper vs playbook, market vs no-market) depends on it.
```

## 8. What this memo does NOT do (guardrails)

```text
- It does NOT abandon the seam. The seam is unanswered, not refuted; the hybrid
  holds it open and names the path back to it (item 4).
- It does NOT claim the instrument generalizes beyond the tested family. That is
  a scope the consolidation must respect and the literature check must position.
- It does NOT confirm a market. It flags that "instrument-as-deliverable" must not
  smuggle in "confirmed market"; item 1 is the test.
- It does NOT authorize anything. It recommends a center of gravity and an
  ordering; the Manager decides.
```

## 9. Closed gates

```text
No new run · No D4 rescue · No CAL-Q rerun · No certification · No compression · No
INT8/INT4 stress · No second compression rung · No full ladder · No Claim C
activation · No public benchmark packaging · No funder-facing release · No SBIR
submission. This memo is model-free strategy.
```

---

## Note

```text
The memo agrees with the Manager's prior (hybrid: instrument first, seam deferred),
but the agreement is load-bearing only because of the reason behind it: the
evidence has EARNED the instrument and the dependency structure BLOCKS the seam.
If those two facts were different — if the seam had a ready baseline family, or if
the instrument findings were not yet banked — the recommendation would differ. The
recommendation follows the evidence, not the prior; it happens to match the prior
because the prior was reading the evidence correctly.
```

— Senior Engineer
