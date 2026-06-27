# COMPOSITION-BASELINE-RECOVERY-PREREGISTRATION-v0.3 (DRAFT)

**From:** Senior Engineer (drafted; lock-before-look pre-registration; no run performed) → **Route:** Team Lead → CS filing
**Date:** 2026-06-26
**Implements:** `COMPOSITION-BASELINE-RECOVERY-TARGET-MEMO-v0.1` (filed). **Authorizes nothing.** Locks the design the memo deferred so a result is readable. **FP16-only · no INT8 · no INT4 · no compression.**

> Lock-before-look: everything below is declared *before* any model is run. Floors are fixed here and are **not** adjustable post-hoc. A run, if later authorized by the Manager by name, may only report PASS / FAIL / UNINTERPRETABLE against these locked criteria.

---

## v0.2 → v0.3 (this revision)

One narrow TL-HOLD fix: **separate document revision from experimental attempt ID.** v0.2's §10 reused `v0.2` / `v0.3` as *attempt* labels, colliding with the *document* revision numbers — impermissible for a lock-before-look pre-registration. Fixed by relabeling attempts **A1 / A2 / A3** (distinct from document versions) in §10 and §11, and adding "**Document revision numbers are not attempt numbers.**" **No substantive change:** n, floors, Wilson rule, item design, foil structure, query forms, and forbidden interpretations are byte-unchanged from v0.2.

---

## v0.1 → v0.2 (this revision)

Two narrow TL-HOLD fixes; **core design unchanged** (N=64, 192 matched same-context triples, D=2, greedy FP16-only, Wilson floors, foil readability gate, pass/fail/uninterpretable mapping; no compression / INT8 / INT4 / Claim C / seam / capability / mechanism claim).

1. **Attempt budget made strict (§10–§11).** "Up to R=3 redesign iterations" was ambiguous (3 total vs 3 after v0.1) and internally inconsistent with its own examples. Now: **maximum total attempts = 3** (attempt labels A1/A2/A3 defined in §10). **No fourth attempt, no silent re-rolls;** each attempt needs its own pre-registered change set before any run; floors fixed across all attempts. Escalation (§11) triggers after the final attempt.
2. **Foil / position-randomization reconciled (§1, §5, §6).** "Target-tail position uniform across contexts" conflicted with the foil constraint. Now explicit: for the **32 foil contexts**, target C is **never** positionally-last (a distractor tail is last); for the **32 non-foil contexts**, target-tail position is **randomized/balanced under the pre-declared seed**; **position distributions are reported separately** for foil vs non-foil so position effects are auditable.

---

## 0. Question (locked)

Can an admissible FP16 composition baseline be constructed on the redesigned two-step target below, such that **hop1, hop2, the same-context component controls, and the composite all clear their pre-declared FP16 floors**, and the composite-correct is **readable as chain-following (not position-reading)** with distractor/position/shortcut artifacts bounded?

## 1. Design overview + exact n

- **Item = one context** (the target chain + D distractor chains, order randomized) **+ one query.**
- **N = 64 target contexts**, each queried as **hop1, hop2, and composite against the identical context block** → **192 matched queries** (64 per type). Matched triples give the same-context component controls (§4).
- **32 of the 64** contexts are **anti-shortcut foils** (§6): the composite answer C is **never** the positionally-last value tail (a distractor tail is last). The other **32 non-foil** contexts have target-tail position **randomized/balanced under the pre-declared seed**.
- **D = 2 distractor chains** per context (§5).
- Total model generations per run: **192**. Seed for context/order generation **pre-declared** (`seed = 20260626`).

## 2. Item design (actual)

Disjoint nonce token pools so there is no pretraining association to lean on; relations are clear English so the *relation* is parsed but the *association* must be retrieved from context. Each chain is `A —rel1→ B —rel2→ C`.

Worked example context (target chain `WUGEX→JBORP→VANKO`; one distractor shown):

```text
Facts:
- The holder of WUGEX is JBORP.
- The signal of JBORP is VANKO.
- The holder of QILMA is ZDRUW.
- The signal of ZDRUW is PFEXT.

Question: What is the signal of the holder of WUGEX?
Answer:
```

Expected composite = **VANKO** (`WUGEX → holder → JBORP → signal → VANKO`). A position-reader emitting the last tail (PFEXT) is **wrong** → this is how foils separate chain-following from shortcut.

- **Entities / values:** distinct CVCVC nonce tokens, disjoint pools, one use each per context.
- **Relations:** drawn from a fixed clear-English set `{holder, signal, color, city, owner}`; `rel1 ≠ rel2` within a chain.
- **hop1 and hop2 are symmetric forward lookups** of equal form and difficulty (this is the fix for the prior hop1 0/8 vs hop2 8/8 asymmetry).

## 3. Query forms (locked, verbatim)

```text
hop1      : What is the {rel1} of {A}?              -> expect B
hop2      : What is the {rel2} of {B}?              -> expect C
composite : What is the {rel2} of the {rel1} of {A}? -> expect C  (requires A->B->C)
```

Decode: **greedy, temperature 0.0, max_tokens 8.** Scorer extracts the first token-run matching the value pool; exact-match against the expected token (case-sensitive).

## 4. Same-context component controls

hop1, hop2, and composite are asked against the **identical context block** (same facts, same distractors, same order) within a matched triple. A component gate clears **only if it clears in-context** — not in an isolated minimal prompt. (V3 cleared components in isolation but failed the composite precondition; this forces components to clear under the composite's actual conditions.)

## 5. Distractor set (locked)

- **D = 2** distractor chains per context, same schema, disjoint tokens.
- **Distractor tails are drawn from the same nonce pool as correct tails** (surface-matched), so distractor attractiveness is controlled, not confounded with hop difficulty (the M5 bound).
- Chain order randomized per context under the pre-declared seed, **subject to the §6 foil constraint** (foil contexts place a distractor tail last).
- **Distractor-tail classification** is scored: for each composite generation, record whether the output is {correct C · a distractor tail · the positionally-last tail · NULL/other}.

## 6. Position / shortcut controls

- **(a) Foil contexts (n=32):** the target C is **never the positionally-last tail; the positionally-last tail must be a distractor tail.** A composite-correct on a foil is therefore **chain-following by construction**.
- **(b) Non-foil contexts (n=32):** target-tail position is **randomized/balanced under the pre-declared seed** (`seed = 20260626`).
- **(c) Position distributions are reported separately for foil and non-foil contexts** — so position effects are auditable.
- **(d) Shortcut probe:** report the composite distractor-tail / positionally-last-tail / NULL rates. A position-reader shows a high positionally-last-tail rate; a chain-follower shows high correct-C **including on foils**.
- **Readability rule:** the composite counts as "readable as chain-following" **only if composite accuracy on the 32 foils clears its floor** (§7), not merely the overall composite.

## 7. Floors (pre-declared, numeric — locked)

```text
hop1            : Wilson 95% lower bound >= 0.80   (in-context, n=64)
hop2            : Wilson 95% lower bound >= 0.80   (in-context, n=64)
composite (all) : Wilson 95% lower bound >= 0.70   (n=64)
composite-foils : Wilson 95% lower bound >= 0.60   (readability, n=32)
```

Rationale (locked): components must be *strong* (≥0.80 LB) for composition to be a meaningful question; the foil floor is the readability gate that the prior baseline had no analogue for. **No floor is adjusted after look.**

## 8. Wilson rule (locked)

Wilson score interval, 95% (z = 1.96), **lower bound**, with p̂ = k/n:

```text
LB = ( p̂ + z²/2n − z·sqrt[ p̂(1−p̂)/n + z²/4n² ] ) / ( 1 + z²/n )
```

A gate clears **iff** its Wilson lower bound ≥ the pre-declared floor. The bound is **recomputed independently in Python from this formula** (not credited from a library call alone).

## 9. Pass / fail / uninterpretable (locked mapping)

- **PASS (constructible + readable):** hop1-LB ≥ 0.80 **and** hop2-LB ≥ 0.80 **and** composite(all)-LB ≥ 0.70 **and** composite-foils-LB ≥ 0.60, all in-context → **an admissible FP16 composition baseline exists.** Compression work may then be *proposed* on it (separately, later).
- **FAIL (not constructible):** any of hop1 / hop2 / composite(all) below floor → composite **not admitted**; not a usable baseline.
- **UNINTERPRETABLE (not readable):** components and overall composite clear **but** composite-foils below floor, or the shortcut probe indicates position-reading → composite-correct is unreadable → **CONTAMINATED → INCONCLUSIVE. This is not a pass.**

## 10. Maximum total experimental attempts (locked)

**Maximum total experimental attempts = 3.**

```text
A1 = initial baseline-recovery attempt governed by this preregistration once artifacts are built and sealed.
A2 = first redesign attempt, if A1 fails or is uninterpretable.
A3 = final redesign attempt, if A2 fails or is uninterpretable.
```

**No A4. No fourth attempt. No silent re-rolls.** Each attempt requires its **own preregistered change set before any run.** **Document revision numbers are not attempt numbers.** A redesign is a bounded change to make a gate clear — it is **never** a floor change. **Floors (§7) remain fixed across A1–A3.**

## 11. Escalation rule (locked)

If after **A3** hop1 (or the composite-foils readability gate) still cannot clear → the Two-Hop L1 family is **provisionally inadmissible at 3B**. **Stop and escalate to the Manager** with three options — different task family, larger model, or different decoding — and do **not** attempt a fourth. "Family inadmissible at this scale" is a **result of record**, not a failure to hide.

## 12. Artifact / provenance + hashes (locked procedure)

Lock-before-look requires the concrete artifacts to be **built to this spec and sha256-sealed in `MANIFEST.json`, committed BEFORE any model is run.**

```text
Pinned now:
  model revision   aa8e7253...                    (locked Qwen2.5-3B-Instruct FP16)
  prereg           = sha256 of THIS file (sealed on filing)
  seed             20260626

Built to spec, hashes SEALED in MANIFEST.json before look (cannot be hashed until built):
  items_file        (64 contexts x {hop1,hop2,composite} + 32 foils, generated under seed)
  prompt_template   (the §2/§3 scaffold)
  scorer_composition_l1.py   (scores hop1/hop2/composite + foil + distractor-tail class;
                              extends Cell03 scorer b65c6803 but NEW -> own hash at build)
```

Raw outputs retained for all 192 generations; components, composite, foils, and distractor-tail classes scored. Fresh-clone byte-verification. **No weights committed.** (This §12 is the one place hashes are not yet in the text — they are committed in the sealed manifest pre-run; the *procedure* is what is locked here.)

## Forbidden interpretations (restated)

A PASS is a **constructibility** result only: the FP16 model produces *readable* composite-correct behavior on **this** target, model, and decoding. It is **not** a capability claim, **not** a mechanism claim, **not** Claim C, **not** a seam result, and carries **no compression reading**. Constructibility ≠ generality.

---

**Decision framing.** This pre-registration does **not** authorize a run. It locks the first FP16 baseline-recovery attempt. **Compression remains blocked until FP16 constructibility clears PASS.** Returned to TL for review before CS filing; the run, if any, is the Manager's by-name authorization after the artifacts are built and the manifest sealed.

— Senior Engineer
