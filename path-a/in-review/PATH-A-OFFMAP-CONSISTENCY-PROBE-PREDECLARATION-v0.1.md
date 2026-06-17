# PATH-A OFF-MAP CONSISTENCY PROBE — PRE-DECLARATION (lock-before-look) v0.1

**E. A. Flores**, Apiana AI, Inc. — June 16, 2026
*River and Canyon · Path A. Prepared by the Senior Engineer. A lock-before-look pre-declaration for a NEW analytical cut on the EXISTING scout data. Binds before any slice is computed.*

## 0. Why this needs to exist before the slice

The scout (HEAD `3cfdc3f`) was bound to its pre-declared metrics. The questions below — *is the off-map concentrated on a subset of items, and do off-map items share a position or structure* — are **new cuts on the same committed data, formulated after seeing the cliff.** Re-slicing committed data along new axes until a pattern appears is analytical fishing — the program's signature failure recurring at the analysis layer — **unless the cut is pre-committed.** This document locks the questions, the decision rule, and the null **before any computation**; the slice is then run **once** against them. No result here certifies or authorizes anything.

## 1. Scope split — what is a slice vs. what needs a new run

```text
SLICE OF EXISTING DATA (this pre-declaration governs; no new model run):
  - per-item concentration of the off-map (subset vs spread)
  - positional / structural sharing among off-map items

ALREADY A LOCKED SCOUT METRIC (computed + verified; available, NOT re-fished):
  - cross-query chain-identity PATTERN (anchor-tracking / fixed / switching), gated on the
    component load-floor. Already reported from the scout: anchor-tracking share falls 77%->50%
    as K rises; ZERO fixed-wrong-chain keys at any cell. This is cited, not recomputed for novelty.

NEEDS A NEW RUN (NOT obtainable by slicing this data; deferred):
  - run-to-run variability ("same input, same wrong chain every time?"). The scout was SINGLE
    GREEDY generation per item -> deterministic -> same input gives same output, so a single-run
    slice CANNOT test run-to-run stability. Testing it requires a NEW multi-sample run (temperature
    or multi-seed) under its OWN pre-registration and Manager by-name authorization. Out of scope here.
```

## 2. Pre-declared questions (fixed before any computation)

```text
Q1 — CONCENTRATION. Across the off-map items (composite lands at decoy answer-depth), is the off-map
     SPREAD across most items, or CONCENTRATED on a subset?
     Operationalization (declared now): rank items by whether they go off-map; per cell and pooled
     across K>=2 (the plateau), report what fraction of items account for the off-map mass.
     Pre-declared cut: "CONCENTRATED" = a minority of items (<= 1/3 of the n that ever go off-map)
     accounts for the majority (>= 2/3) of off-map instances on the plateau; "SPREAD" = off-map
     instances are distributed across the majority of items with no such minority carrying them.

Q2 — POSITIONAL / STRUCTURAL SHARING. Among off-map items, do they share an identifiable structural
     feature — a layout position of the target chain, a specific decoy slot the answer lands in, or
     an item-construction feature recorded in the materialized ground truth?
     Operationalization: for off-map items, tabulate (a) target-chain layout position, (b) which
     decoy slot the landed token belongs to, (c) any recorded item feature. Pre-declared cut:
     "STRUCTURED" = off-map concentrates on a position/slot/feature beyond its base proportion (a
     declared margin, e.g. >= 2x base share); "UNSTRUCTURED" = off-map matches base proportions.
```

## 3. The null (forces "file diffuse and stop")

```text
NULL: the off-map is SPREAD (Q1) AND UNSTRUCTURED (Q2) — distributed across most items, matching
base proportions on position/slot/feature, with no concentrated subset and no positional structure.
If the null holds, the finding is "the off-map is diffuse across items and positions" — that is the
result; it is FILED, and the probe STOPS. A diffuse null is a real outcome, not a failed probe, and
it is NOT a license to keep slicing for some other axis until structure appears.
```

## 4. Decision rule — and its containment (read this; it is the claim-risk core)

```text
IF CONCENTRATED and/or STRUCTURED (Q1/Q2 fire):
  -> LEANS toward a STABLE shortcut or a saturation localized to a subset/position at this load.
IF DIFFUSE and UNSTRUCTURED (the null):
  -> LEANS toward diffuse instability rather than a localized stable route.

CONTAINMENT (mandatory):
  - BOTH outcomes are POSITIONAL DISTRIBUTION facts about WHERE the off-map lands across items and
    positions. NEITHER establishes a mechanism. A concentrated/structured result does NOT prove a
    "stable shortcut"; a diffuse result does NOT prove "instability." Each is a LEAN on plausibility,
    not a determination.
  - This probe STILL does not separate (a) traversal / (b) relation-keyed grab / (c) chain-anchor
    inconsistency. It describes the off-map's distribution; it does not adjudicate process. The
    instrument cannot see footsteps.
  - The lean wording is fixed now so that, after the slice, a concentrated result cannot be written
    up as "we found the shortcut" and a diffuse result cannot be written up as "we found it's
    unstable." Both get the "consistent-with / leans" form, never the "establishes" form.
```

## 5. Run discipline

```text
- ONE COMPUTATION PER QUESTION. Q1 and Q2 are each computed ONCE against the cuts declared in §2,
  on the existing scout artifacts. No re-slicing, no new axes added after look, no cut threshold
  moved after seeing the distribution.
- A different axis (e.g., per-relation, per-token-length) is a FRESH pre-declaration, not an
  extension of this one.
- Reported against the §3 null and §4 rule verbatim. SE computes from repo bytes and echoes the
  per-item counts so the result is reviewer-assertable.
```

## 6. Status / routing

```text
- Lock-before-look pre-declaration. Binds the slice. The slice does NOT run until this is locked.
- Routes Senior-draft -> TL / Manager acknowledge the lock -> SE computes ONCE -> reports against
  the pre-declared null and decision rule.
- Run-to-run variability is explicitly deferred to a separate run + prereg + Manager authorization.
- Certifies nothing, authorizes nothing; the closed K=5 FAIL stands; the cliff finding (separate
  note) is the standing positional result regardless of this probe's outcome.
```

— Senior Engineer (pre-declaration; locks before the slice)
