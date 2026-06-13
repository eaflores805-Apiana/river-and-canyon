# SUBMAP-CONVENTION-v1.0

**Version:** v1.0. River and Canyon program. Standing navigation convention.
**Status:** model-free standing pattern. One page on purpose. If this convention is ever longer than the work it governs, it has failed its own test and gets cut.
Owner: Manager · Senior maintains · referenced from Program Map v2.0.

## The idea, in one line

A submap is a function call: it has a return address, a reason, a defined "done," a rough body, and it pops back to the main map when it returns a value.

## When you open a submap, write a CHARTER (fits on one screen)

```text
SUBMAP: <name>
  Parent node:    <which main-map item spawned this — the return address>
  Why:            <one sentence: why this subsection exists>
  Exit condition: <what "done" looks like — 1–3 named outcomes, fixed BEFORE entry>
  Rough plan:     <a few stages, not a schedule>
  Touch / closed: <what it may touch; what stays gated>
```

The one rule that makes this work, not weigh: **fix the exit condition before you enter.** That is the pre-registered-decision discipline you already use for experiments, pointed at navigation. "Done" defined while you can think clearly beats "done" negotiated when you are tired and want to move on.

## When you finish, write a CLOSE-OUT (shorter than the charter)

```text
CLOSE-OUT: <name>
  Outcome:   <which exit condition was hit>
  Returns:   <what the parent map consumes — the return value>
  Traces to: <"this closes parent node X" — pops back to the main map>
```

The `Traces to:` line is the payload. It is the whole reason for the convention: it guarantees you can leave a subsection and return to the main map without having lost your place.

## Three guardrails that keep it light

```text
1. SIZE CAP. Charter ≤ one screen; close-out shorter than the charter. If either
   grows past that, the subsection is too big — split it. The size cap IS the
   anti-bureaucracy mechanism.
2. NOT EVERY JUMP NEEDS A CHARTER. Charters are for MULTI-STAGE subsections. A
   quick verification or a one-artifact task does not get one. Over-chartering
   recreates the bureaucracy you are avoiding.
3. ONE LIVE TRACKER. The "where are we right now" question is answered by a
   single position tracker (PROGRAM-POSITION-v*), not by re-reading the maps.
   Update the tracker when a stage closes; never let it drift from the record.
```

## The test

Before writing any charter, ask: *would this cost more than just doing the thing?* If yes, don't charter it. The convention exists to keep the main thread findable, not to gate work. When in doubt, lighter.

— Senior Engineer
