# PAPER-2 v1.2 — TIGHTENING-AND-LIMITATIONS DELTA (v0.3, DRAFT)

**From:** Senior Engineer → **Route:** C5 claim-risk (substantive) → CS provenance → Team Lead synthesis → Manager (RC-lock)
**Base:** `papers/paper2-correctness-is-not-constructibility/in-review/PAPER-2-RELEASE-CANDIDATE-v1.1.md` body, sha256 `4e8a014ab8532136b41b231cd951f876d64f780eda87babd32cde9c3500cb633` (the byte-frozen RC body).
**Status:** edit specification, **not** an applied revision. SE drafts; SE authorizes, locks, and files nothing. The frozen RC stays the RC until this delta clears the chain.

> This delta consolidates three reviews this round — **C4** (accept w/ minor tightening), **C5** (external referee; accept w/ minor revisions), **TL** (PASS w/ minor RC edits). Every OLD string below was verified to occur **exactly once** in the RC body. Edits are tagged **[CLAIM]** (touches a claim-bearing sentence → requires the substantive C5 re-review), **[EDIT]** (editorial/low-risk), **[PROV]** (provenance → CS), or **[DECISION]** (Manager/author choice). **No edit requires a new run, rerun, compression, tooling, or threshold change.**

## v0.2 → v0.3 (this revision)

A pre-C5 review of the v0.2 preview caught **claim-bearing remnants the v0.2 edits missed** — old stronger language that survived in high-visibility places (the abstract, a figure caption, figure-embedded text) because v0.2 anchored only on the §4.6/§5 body strings and did not sweep every occurrence. **Owned.** v0.3 completes the softening:

1. **Abstract "not reducible" → "not explained by that route alone" (new edit B1b).** The RC abstract carried its own copy of "not reducible," separate from the §4.6 sentence v0.2 softened; the v0.2 preview was therefore internally inconsistent (abstract strong, §4.6 soft). Harmonized.
2. **Figure V3-3 caption "isolates" → "relocates … under foreclose-all controls" (Cluster F-1).** Figure captions were never in the v0.2 scope; the caption still asserted the exact word being softened. Fixed in the figure block and the captions-and-provenance doc.
3. **Figure V3-2 embedded text "not reducible to that route" → "that route alone does not explain the hop1 shortfall" (Cluster F-2).** The SVG carried the old formulation independently; SVG corrected and PNG regenerated.
4. **A3 "cannot be certified" → "cannot be admitted as constructible" (refine).** "certified" is strong in this project even in the negative; replaced with fail-closed admission language.
5. **§7 "the first hop is genuinely hard under competition" → "the first-hop query is hard under this competition design" (refine).** Keeps the statement about the construction, not the model.

These are not new claim directions — they extend the *already-approved* softening (isolates→relocates; not reducible→not explained by alone; certified→admitted) to the occurrences v0.2 left untouched. But because they touch the abstract and figures (read as external prose), the corrected text needs C5's eyes — see the governance note in the return.

---

## v0.1 → v0.2 (this revision)

This delta was reviewed pre-C5 and **held** for two required fixes, both adopted here:

1. **C1 threshold robustness — corrected (numerical error, owned).** v0.1 stated "0 of 6 clear at any floor from 0.46 up to 1.0." That is wrong: the largest fresh-block Wilson lower bound is **0.4628**, which *exceeds* 0.46, so F5 would clear a 0.46 floor. Corrected to the safe boundary — admissibility is strict (Wilson lower must *exceed* the floor), so no fresh block clears any floor **above 0.4628** (per Manager directive; admissibility is strict), the locked 0.75 included. (Affects the grounding-facts note, edit C1, and the closing summary.)
2. **A1/A3 over-strong language — corrected.** "certifies" (A1) and the biconditional "iff" (A3) overclaimed for a project whose thesis is that unknown shortcut routes can remain. Replaced with fail-closed admission language: A1 now "determines whether the available FP16 evidence is *sufficient* to treat the baseline as measuring the intended operation"; A3 now "treated as constructible … *only if*" (necessary conditions under declared probes, not a universal definition).

Also adopted from the same review: **B4** "removes" → "is designed to remove … under the declared construction controls"; **B5** "is itself driving the inadmissibility" → "over-attractive enough that the construction cannot separate distractor pull from first-hop difficulty"; **E4** anchor verified (occurs once in §4.1) and resolved. No other blocks changed; the RC anchors are unaffected.

---

## Grounding facts verified for this delta

```text
- "isolates the component-precondition failure" appears TWICE: §4.6 (the result sentence) and §5
  (the "two constructions" paragraph). Both must be softened (M5), not just the one TL #5 names.
- "stable, mappable object at 3B FP16" (Claim B vs seam) is INCONSISTENT with "structured, bounded,
  mappable failure surface" used elsewhere for the same object. TL #1 harmonizes a real inconsistency.
- "...to be re-verified before submission." (§3.2) contradicts Appendix B, where CS already recomputed
  for the freeze/tag pass. TL #3 is a genuine staleness fix.
- Inference stack IS recorded in run_record.json: mlx_lm 0.31.3, torch 2.7.1, transformers 5.10.2
  (consistent with the K-sweep). C5 m5 is display-only: surface it in the Appendix B addendum.
- Wilson robustness (from the six verified fresh-block lower bounds; max = F5 0.4628): admissibility is
  strict (Wilson lower must EXCEED the floor), so no fresh block clears any floor above 0.4628 — the
  locked 0.75 included. Admissibility at n=96 needs >=81/96 (Wilson 0.7581).
```

---

## Cluster A — Framing (C5 M1, M2, M3, M4)

### A1 — abstract: lead with the gate as the deliverable; surface "no compression" first **[CLAIM]** (C5 M1, m3)
**OLD** (abstract opening):
> Behavioral stress metrology — measuring which capabilities a model retains under compression such as INT4 quantization — presumes a trustworthy full-precision baseline. Paper 1 argues that stress-retention is uninterpretable unless the FP16 baseline is clean, and specifies fail-closed gates that withhold a result otherwise. That argument leaves one thing unshown: that the baseline gate is ever *binding* rather than merely conservative. This paper supplies the demonstration in **two independent constructions within one model and one closed-world two-hop task family** (3B FP16).

**NEW:**
> Behavioral stress metrology — measuring which capabilities a model retains under compression such as INT4 quantization — presumes a trustworthy full-precision baseline; **this paper runs no compression**. Its contribution is a worked, fail-closed *pre-stress constructibility gate*: a decomposition-and-shortcut-probed admission test that determines whether the available FP16 evidence is sufficient to treat the baseline as measuring the intended operation before any compression is applied. Paper 1 argues that stress-retention is uninterpretable unless the FP16 baseline is clean and specifies such gates; what was unshown is that the gate is ever *binding* rather than merely conservative. We show it is, in **two constructions within one model and one closed-world two-hop task family** (3B FP16) — including a case where the gate's own fresh-replication requirement catches a precondition that a single materialization had passed. The conceptual point that surface correctness is not constructibility is the motivation; the demonstrated gate is the deliverable.

*Rationale:* M1 — foreground the methodology as the contribution; m3 — surface "no compression" in sentence 1. (Authors/C5 may tune wording; this is the most judgment-heavy edit.)

### A2 + A4 — state the two-construction evidential asymmetry; C1 shows contamination-*exists*, not -*is-position* **[CLAIM]** (C5 M2, M4)
**OLD** (§5 addition):
> The two constructions fail the baseline in two distinct ways.

**NEW:**
> The two constructions fail the baseline in two distinct ways. They also differ in evidential weight, and we do not treat them as symmetric: the first is a diagnostic case on a small fixed set (24 items, n=8 per positional group) showing that an aggregate score *can* hide a contaminating axis — and, because position and rank co-vary in Cell03 (§7), it establishes that contamination *exists* rather than that it is specifically positional, which is why V3 forecloses position, rank, and endpoint jointly; the second is a stable-inadmissibility result with fresh replication and confidence bounds (six 96-item materializations, Wilson lower bounds). They demonstrate different things at different strengths.

*Rationale:* M2 — name the asymmetry the "two independent constructions" phrasing glosses; M4 — C1 shows contamination-exists, with V3's joint foreclosure as the response.

### A3 — add an operational definition of *constructible* (with the recursive component clause) **[CLAIM]** (C5 M3)
**OLD** (anchor — insert immediately before this heading):
> ### 3.3 Second construction: foreclose-all V3

**NEW** (insert this paragraph, then the heading):
> We use *constructible* operationally. For this paper, a query type is treated as constructible on a materialization only if (i) its accuracy clears the admissibility floor (Wilson lower bound > 0.75), (ii) no declared shortcut probe or decomposition shows its correctness aligned with an identified non-intended route (per §4.3–§4.4), and (iii) its required components are themselves constructible — so a composite is not constructible while a component (e.g., hop1) is below floor. Clause (iii) is what makes the V3 first-hop precondition decisive: a composite cannot be admitted as constructible while its first hop is inadmissible, independent of any composite score.

*Rationale:* M3 — the term is load-bearing; the recursive clause is the crux of the V3 result. (Clause (ii) is phrased to match the paper's actual checks, not an invented "battery.")

---

## Cluster B — Bound the V3 foreclosure honestly (C4 enumeration + C5 M5 + TL #5)

### B1 — soften "not reducible" → "not explained by … alone" (§4.6) **[CLAIM]** (TL #5, C5 M5)
**OLD:**
> The hop1 shortfall here is not reducible to the §4.3 position/rank route:

**NEW:**
> The hop1 shortfall here is not explained by the §4.3 position/rank route alone:

### B1b — soften the ABSTRACT "not reducible" (harmonize with §4.6) **[CLAIM]** (TL; missed in v0.2)
**OLD** (abstract):
> the persistence of the hop1 shortfall under it indicates the shortfall is not reducible to that route

**NEW:**
> the persistence of the hop1 shortfall under it indicates the shortfall is not explained by that route alone

### B2 — soften "isolates" in the §4.6 result sentence **[CLAIM]** (C5 M5, M2)
**OLD:**
> The result is that, across two independent constructions, the baseline gate is shown binding and discriminating — and that the second construction isolates the component-precondition failure from the position confound the first construction could not separate.

**NEW:**
> The result is that, across two constructions, the baseline gate is shown binding and discriminating — and that the second construction **relocates the failure to the first-hop precondition under foreclose-all controls**, away from the position confound the first construction could not separate. Whether that precondition failure reflects a genuinely hard first hop or an over-attractive designed distractor (the P-role class; see §7) is not separated here.

### B3 — soften "isolating" in the §5 paragraph **[CLAIM]** (C5 M5, M2)
**OLD:**
> The gate is therefore shown binding and discriminating across two independent constructions, with the second isolating the component-precondition failure from the position confound the first could not separate.

**NEW:**
> The gate is therefore shown binding and discriminating across two constructions, with the second **relocating the failure to the first-hop precondition under foreclose-all controls**, away from the position confound the first could not separate (the distractor-attractiveness alternative for that precondition failure is noted in §7).

### B4 — enumerate what V3 does and does NOT control (§3.3) **[CLAIM]** (C4 foreclosure enumeration, C5 M5)
**OLD:**
> committed design choice, not a construction proven to foreclose every conceivable route

**NEW:**
> committed design choice, not a construction proven to foreclose every conceivable route. Specifically, under the declared construction controls V3 is designed to remove the absolute-position/rank endpoint cue (same-depth competitors, balanced placement), the single-relation recency cue (D = 5 distinct relations), and the structural-depth selection cue (all competitors at depth 2). It does **not** control the *attractiveness* of the introduced P-role distractor class: the K = 5 relation-reusing chains add a strong, designed wrong-selection target, and whether that target's salience contributes to hop1 inadmissibility is not separated here (§7)

### B5 — add the distractor-attractiveness limitation (§7) **[CLAIM]** (C5 M5)
**OLD** (anchor — insert new bullet immediately before this bullet):
> - **Behavioral only.**

**NEW** (insert this bullet, then the "Behavioral only" bullet):
> - **Distractor-attractiveness is not separated from component difficulty.** The foreclose-all redesign introduces a P-role distractor class (the r1-subject token of the K = 5 relation-reusing chains) as a designed wrong-selection target. All wrong hop1 predictions in the fresh blocks land on it (352/352, §4.6). This unanimity is consistent with two accounts this construction cannot distinguish: the first-hop query is hard under this competition design, or the introduced distractor is over-attractive enough that the construction cannot separate distractor pull from first-hop difficulty. The V3 result therefore bounds the first-hop precondition *under V3's competition design*; separating the two accounts — e.g., a variant that varies or removes the P-role distractor — is future work.

*Rationale (B1–B5):* C4 and C5 converge — the foreclose-all redesign foreclosed the position route but introduced its own uncontrolled factor (P-role distractor attractiveness); the 352/352 unanimity is the symptom. These edits keep the robust claim (*not explained by position alone*), soften the over-strong "isolates" claim in both places, name the alternative, and add it as a limitation. **No new positive claim is added; an existing claim is bounded.** Claim B stays *supported, not cleared*.

---

## Cluster C — Admissibility-floor rationale + robustness (TL #2, C4)

### C1 — add the local-threshold rationale and the robustness range (§3.3) **[CLAIM]**-adjacent / disclosure
**OLD:**
> Wilson lower bound of its accuracy exceeds **0.75**.

**NEW:**
> Wilson lower bound of its accuracy exceeds **0.75**. The 0.75 floor is a local program threshold for this construction, model scale, vocabulary, and task geometry — not a universal benchmark standard; the stability result is insensitive to it: admissibility requires the Wilson lower bound to *exceed* the floor, the largest fresh-block Wilson lower bound is 0.4628, so no fresh materialization clears any floor above 0.4628 — the locked 0.75 included.

*Rationale:* TL #2 (local threshold) + C4 (Wilson rationale + sensitivity). The locked floor is **not** changed; this is a robustness *disclosure*. Numbers verified.

---

## Cluster D — Provenance (C5 m5) **[PROV → CS]**

### D1 — surface the recorded inference-stack versions (Appendix B addendum)
**OLD:**
> Model / profile (locked): `Qwen/Qwen2.5-3B-Instruct` revision `aa8e72537993ba99e69dfaafa59ed015b17504d1`, FP16, greedy (temp 0).

**NEW** (append one line):
> Model / profile (locked): `Qwen/Qwen2.5-3B-Instruct` revision `aa8e72537993ba99e69dfaafa59ed015b17504d1`, FP16, greedy (temp 0). Inference stack (V3 lifecycle, from `run_record.json`): `mlx_lm 0.31.3`, `torch 2.7.1`, `transformers 5.10.2` (consistent with the K-sweep record).

*Rationale:* m5 — the versions are recorded; surface them. CS to confirm against `run_record.json` on the freeze pass.

---

## Cluster E — Editorial (TL #1, #3; C5 m1, m6)

### E1 — harmonize "stable, mappable" → "structured, bounded, mappable" **[EDIT]** (TL #1, C5 m6)
**OLD:** `stable, mappable object at 3B FP16`
**NEW:** `structured, bounded, mappable object at 3B FP16`
*(Keep the `HOP1-STABLE-INADMISSIBLE` verdict label unchanged — it is a locked decision name, not prose.)*

### E2 — fix the "before submission" staleness (§3.2) **[EDIT]** (TL #3)
**OLD:** `attested from that record and to be re-verified before submission.`
**NEW:** `attested from that record, recomputed for the freeze/tag pass, and listed in full in Appendix B.`

### E3 — soften "stable across draws" in the abstract **[EDIT]** (C5 m6)
**OLD:** `the shortfall is stable across draws rather than a single-draw artifact`
**NEW:** `the inadmissibility verdict is unanimous across draws rather than a single-draw artifact`

### E4 — one interpretive line on the non-monotone composite (§4.1) **[EDIT]** (C5 m1)
*Anchor (verified — the sentence "Composite is non-monotone and, as §4.3 shows, position-contaminated." occurs exactly once in §4.1). Append the sentence below to it.*
*Proposed addition (a sentence):* "Because the cells are construction revisions rather than a controlled variable, the composite differences across them reflect changing construction artifacts, not a trend (cf. Figure 1 caption)."

---

## Cluster F — figure assets (TL; missed in v0.2) **[CLAIM] / [DELIVERABLE → CS]**

Figure captions and figure-embedded text travel independently of the body and must not be stronger than the softened prose. v0.2 did not sweep them. Fixed:

### F-1 — Figure V3-3 caption: "isolates" → "relocates"
**OLD:** Construction 2 isolates the component-precondition failure away from the position confound of Construction 1.
**NEW:** Construction 2 relocates the failure to the first-hop precondition under foreclose-all controls, away from the position/rank confound of Construction 1, while leaving the P-role distractor-attractiveness alternative unresolved.
*(Applied to the figure block and the captions-and-provenance doc.)*

### F-2 — Figure V3-2 (gate-decision) embedded SVG text: "not reducible" → "does not explain … alone"
**OLD (SVG text):** V3 forecloses the position/rank route of Construction 1, so the hop1 shortfall is not reducible to that route
**NEW (SVG text):** V3 forecloses the position/rank route of Construction 1, so that route alone does not explain the hop1 shortfall
*(SVG corrected; PNG regenerated — figure digests change, CS to record. The "What it does NOT establish" panel is unchanged.)*

---

## DECISION items (Manager / author)

- **F1 — figure numbering (TL #4).** The compiled paper currently has Figure 1–3, then **Figure V3-1/V3-2/V3-3**, then Figure 4. The V3-series was a review-build convenience that avoided renumbering and touching in-text references. **For public release, sequential renumbering is the standard expectation** — but it is a real edit: V3-1/2/3 → Figures 4/5/6, the existing Figure 4 (§6) → Figure 7, the in-text "(Figure 4)" references in §6 → "(Figure 7)", and ideally callouts added for the new figures. **Option A:** keep the V3 series as a stated addendum convention. **Option B (recommended for public release):** renumber sequentially (CS regenerates/relabels figures; references updated). Editorial, with a downstream CS edit attached.
- **E5 — Cell02 placement (C5 m2).** Cell02 fails Gate 1 on one item and "does not disentangle cues"; C5 asks whether it earns main-text space or belongs in an appendix as a lineage artifact. Length-vs-completeness judgment for the authors; no claim impact either way.
- **Status line (TL #6).** Not a prose edit in this delta. At Manager RC-lock authorization, update the header from the current "…pending C5 → CS → TL → Manager review; not released" to a release-candidate line (e.g., "v1.1 release candidate … not yet released"), and only at final release authorization to a released label. The final version identifier for the post-delta artifact is the Manager's call.

---

## Forbidden-claims checklist (holds across all edits)

```text
[x] Claim B stays SUPPORTED, NOT CLEARED — these edits BOUND it (M5), they do not add a positive claim.
[x] Claim #5 stays "blocked on a precondition"; Claim C UNTOUCHED; program PRE-STRESS.
[x] No "model cannot do hop1 / cannot compose / is unstable."  (B2/B3 soften toward LESS, not more.)
[x] No mechanism — the distractor-attractiveness item is an ALTERNATIVE/limitation, not a why-claim.
[x] No compression / stress-retention claim; hop2 stays an internal FP16 control, not a stress target.
[x] No certification / capability claim.  No cross-model / cross-scale / cross-task generality added.
[x] Locked 0.75 floor UNCHANGED (C1 is a robustness disclosure, not a re-pick).
[x] "Claim B" kept distinct from the forbidden "Paper B."  HOP1-STABLE-INADMISSIBLE verdict label kept.
[x] No new run / rerun / compression / INT8 / INT4 / tooling edit / threshold change / artifact regen
    (figure regeneration only if Option B renumbering is chosen — a relabel, not new data).
```

## What does NOT change

```text
- The run data, the six per-block counts/Wilson bounds, 576/576, 352/352, the analyzer decision.
- Appendix B digests (except the ADDED runtime-version line in D1; no hash changes).
- The HOP1-STABLE-INADMISSIBLE verdict label and the locked construction values.
- Claim C, Claim #5, the pre-stress status, the C0 / Path A FP16 K=5 FAIL (closed).
- Figures themselves, unless Option B (sequential renumber = relabel only, same data).
```

## Boundary

```text
Draft edit specification for the C5 -> CS -> TL -> Manager chain. The substantive C5 re-review is
REQUIRED (A1–A4, B1–B5, C1 touch claim-bearing sentences); it is not a "quick check." The M5 resolution
proper — a distractor-attractiveness control (a V3 variant varying/removing the P-role distractor) — is a
SEPARATE future experiment requiring Manager run-authorization and is NOT part of this delta. The frozen
RC (4e8a014a) stays the RC until v1.2 clears the chain. Filing/committing is CS's lane. SE drafts; SE
authorizes nothing and locks nothing.
```

---

**The one to carry up:** Three reviews this round converge on accept/PASS-with-revisions and confirm the substance is claim-safe; this delta consolidates them into byte-anchored edits. The headline is **M5 (distractor-attractiveness), on which C4 and C5 converge**: the foreclose-all redesign foreclosed the position route but introduced an uncontrolled factor (P-role distractor attractiveness), and the 352/352 unanimity is the symptom — so the over-strong "isolates the component-precondition failure" claim (which appears **twice**) is softened to "relocates … under foreclose-all controls," the alternative is named, and a limitation is added, while the robust "not explained by position alone" claim is kept. Everything else is framing (M1/M2/M3/M4), a verified provenance line (m5), Wilson robustness (verified: 0/6 at any floor above 0.4628, the locked 0.75 included), and editorial harmonization (including a real internal inconsistency at line 76 and a genuine staleness at line 134). **No new experiments.** This re-opens a *substantive* C5 review, not a rubber stamp — the two favorable recommendations and the TL PASS do not waive it. SE drafts; SE authorizes, locks, and files nothing; the distractor-attractiveness control is the separate, run-authorization-gated path that would actually resolve M5.

— Senior Engineer (Paper 2 v1.2 tightening-and-limitations delta; for the C5 → CS → TL → Manager chain)
