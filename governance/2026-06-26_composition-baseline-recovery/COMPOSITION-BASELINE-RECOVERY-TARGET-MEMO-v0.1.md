# COMPOSITION-BASELINE-RECOVERY-TARGET-MEMO-v0.1 (DRAFT)

**From:** Senior Engineer (drafted; proposal only; no run performed) → **Route:** Team Lead → CS filing
**Date:** 2026-06-26
**Status:** baseline-recovery target proposal. **Authorizes nothing.** This memo proposes the next FP16 baseline-recovery target and answers one question only: *can an admissible FP16 composition baseline be constructed?* **No INT8 · no INT4 · no compression · no Claim C · no seam · no capability/mechanism claim.**

---

## 1. Why this memo exists

There is no admissible FP16 composition baseline. Until one exists, every compression result is uninterpretable for the compositional question — the 2026-06-26 control rung confirmed the instrument runs and fails closed, but re-confirmed the baseline is **CONTAMINATED → INCONCLUSIVE**. Recovering a readable FP16 composition target is the precondition for all further compression work. This memo proposes that target.

## 2. Current blocker: hop1 inadmissible / composite unreadable

Two-part, and both must be fixed:

- **hop1 inadmissible (`HOP1-STABLE-INADMISSIBLE`).** On the existing Two-Hop L1 construction, the first hop does not clear: 0/8 at FP16 on the 06-15/06-26 target; on Path A it swung 87/96 → 28/96 across the *same* construction (stable, not a seed artifact; max Wilson lower bound **0.4628**, below floor). A model that cannot do single-hop A→B retrieval cannot be doing genuine A→B→C composition — so the composite cannot be admitted as constructible.
- **composite unreadable.** The one composite-"correct" (i06) was **position-reading, not chain-following** — the same tail token emitted for hop1, hop2, and composite alike. So even a passing composite is not evidence of chain composition.

Net: the construction must be **redesigned to make hop1 clear and the composite readable** — not retried as-is.

## 3. Target construct

A redesigned two-step compositional target satisfying three design requirements (specifics — tokens, relations, n, floors — deferred to a future pre-registration; this memo proposes the *type and requirements*, not a built item set):

1. **First hop is retrievable** (addresses hop1 0/8): the A→B fact must be answerable by the FP16 model in-context — candidate levers include clearer relation phrasing, a more salient/learnable first-hop fact, and removing whatever caused the prior NULL-default. If hop1 cannot be made to clear, the family is inadmissible at this scale (see §10).
2. **Chain-following is separable from shortcut** (addresses i06): include control items where emitting the hop2-fact tail (position-reading) yields the *wrong* composite answer, so a composite-correct on those items can only come from traversing the chain.
3. **Distractor attractiveness is bounded** (addresses M5): choose distractors so distractor-attractiveness does not co-vary with hop difficulty.

**V3 note (per Manager caveat):** this is a *redesigned baseline attempt* addressing the named failure modes, **not** a V3 retry. Any element reused from V3 must be justified as redesign, not re-run of foreclose-all.

## 4. FP16-only gates

All at FP16, greedy, on the locked model revision `aa8e7253…`; no compression anywhere:

- **hop1 gate** — first-hop retrieval clears a pre-declared floor (Wilson lower bound > floor).
- **hop2 gate** — second-hop retrieval clears the floor.
- **composite gate** — composite clears the floor.
- **Admissibility (fail-closed):** if hop1 or hop2 does not clear, the composite is **not** admitted as constructible (standing `HOP1-STABLE-INADMISSIBLE` rule). No gate is loosened to manufacture a pass.

## 5. Same-context component controls

The component gates (hop1, hop2) must be measured **in the same context as the composite** — same scaffold, same distractors present — so "component clears" is established under the conditions the composite faces, not only in isolation. (V3 cleared components in isolation yet failed the composite precondition; the redesign must show components clear *with* the composite's context.)

## 6. Distractor / position / shortcut controls

The readability controls — what makes a composite-correct interpretable:

- **Position/shortcut control:** items where tail-emission gives a wrong composite answer (per §3.2); a composite-correct there is chain-following by construction.
- **hop2 shortcut probe:** the paper's §9 precondition — hop2's admission must not *presume* shortcut-freeness; either run the probe or scope the result as not presuming it.
- **Distractor-attractiveness control:** pre-declared distractor set with its co-occurrence properties, so the P-role unanimity (M5) is bounded rather than ambiguous.

## 7. Pass / fail / uninterpretable branches

- **PASS (constructible):** hop1 + hop2 + composite all clear at FP16 in-context, the position/shortcut controls show composite-correct is chain-following, and distractor attractiveness is bounded → an admissible FP16 composition baseline exists; compression work may then be *proposed* on it (separately, later).
- **FAIL (not constructible):** any component or composite gate fails to clear → composite not admitted; not a usable baseline; redesign or escalate.
- **UNINTERPRETABLE:** components clear but the controls cannot separate chain-following from shortcut, or distractor-attractiveness cannot be bounded → composite-correct is unreadable; same disposition as the current baseline (CONTAMINATED → INCONCLUSIVE). **This is not a pass.**

## 8. Forbidden interpretations

A clearing baseline does **not** establish Claim C, the seam, or that composition survives compression (all downstream/out of scope). It is **not** a capability claim ("the model can compose") or a mechanism claim ("the model traverses the chain") — it is a **constructibility** result: the FP16 model produces *readable* composite-correct behavior on this target under these controls. No compression reading of any kind. Constructibility ≠ generality — clears on *this* target, model, and decoding, nothing wider.

## 9. Artifact / provenance requirements

Pre-register the construct, gates, floors, distractor set, and controls **before any FP16 run** (lock-before-look). Pin model revision `aa8e7253…`, scorer, items, prompt template (sha256). Retain raw outputs; score components, composite, and controls. Fresh-clone byte-verification; no weights committed.

## 10. Stop conditions

- If hop1 cannot be made to clear across reasonable redesigns → the Two-Hop L1 family may be inadmissible at 3B; **escalate** (different task family or model — Manager decision), do not keep retrying.
- If the position/shortcut control cannot separate chain-following → the target is unreadable; **do not lower the bar** to force a pass.
- **Hard stop:** no compression work is proposed until an FP16 baseline clears **PASS**.
- Pre-register before each FP16 run; run-once per gate; no iterating a gate to a pass.

---

**Decision framing.** This memo does **not** authorize a run. It proposes the next baseline-recovery target. **Compression remains blocked until FP16 constructibility clears.** Returned to TL for review before CS filing.

— Senior Engineer
