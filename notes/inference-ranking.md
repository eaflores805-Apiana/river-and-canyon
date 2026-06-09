# Inference Ranking — What Kind of Water Carves the Mountain?

*A running record of inferences drawn from this work, ranked by impact. "Impact" here = durability × centrality × whether it is ours to contribute — not prose quality, not how established, not how exciting. The recurring finding across every ranking pass on this project: those axes do not coincide, and they often invert.*

*Method: each inference is verified against the literature where verification is possible before it is ranked. A ranking with a check under it beats a ranking that trusts the claim.*

---

## Set 1 — logged June 2026

Ranked most-impactful to least. Each entry notes the source document's own rating (load-bearing strength, 1–10) where given, and where this ranking departs from it and why.

### 1. Quantization reframed as the inverse problem to training
**Impact: highest. (Source rated 7.5 on strength.)**
The most durable original move in the work, and the one that is genuinely *ours* — the evidence underneath is the field's; this framing is the contribution. Rated for survivability, not evidence: it holds even if the geometry account, the provenance axis, and every speculative claim are refuted. Seeing a deployment afterthought (quantization) as a *measurement instrument* for which carvings are load-bearing is the spine that makes the rest coherent. Ranked first for impact because it is the only top item that does not depend on any single research line holding up.

### 2. The stress-retention qualification question
**Impact: high. (Source rated 7.)**
The most novel forward direction, least encumbered by prior art, and it inherits none of the framework's explanatory burden — it only needs the measurement to track field behavior. Does retention-under-stress predict deployment reliability better than peak accuracy? Insulated from the anchor's single-source risk because it is a *new* measurement, not a reliance on the existing one. Ceiling capped because it is a proposal — an empirical bet that could simply lose. This is where the work can still add something nobody has. (Same item as A8 in the protocol.)

### 3. Within-chain step-localization of fragility
**Impact: high but contingent. (Source rated 8 — highest on evidence; downgraded here for impact.)**
Within-study, apples-to-apples: same reasoning chains, method/execution errors elevated over conceptual ones, failure entering at an identifiable early step. Mechanism-suggestive in a way accuracy curves are not — the strongest *evidence* in the work.
**VERIFIED (June 2026):** the step-localization result traces to one author cluster — 2505.11574 extending 2501.03035, building on Feng et al. 2024 and Liu et al. 2025 for the underlying phenomenon. No *independent* group reproducing the step-localization finding was found. The "it's one group" attack is therefore **live and confirmed**, not hypothetical. This is the reason it ranks third for *impact* despite ranking first for *evidence quality*: its weight is concentrated in a single line and contingent on replication that is not in our hands. Strong spine, concentrated risk.

### 4. The two-mechanism distinction (fine spacing vs. salient/outlier channels)
**Impact: medium. (Source rated 6.5.)**
Well-grounded on the mechanism side (AWQ, SmoothQuant — confirmed standard methods). The "outlier channels are architectural plumbing, not conceptual difficulty" correction is a genuine guard against over-reading — the same behavioral-vs-ontological discipline enforced throughout the project. Capped because the load-bearing verb — that the two failure modes *come apart* for real capabilities — is asserted, not shown. A useful guard, not a contribution.

### 5. Cross-domain selectivity (math/reasoning fragile, broad language robust)
**Impact: medium-low. (Source rated 6.)**
Real and field-converging, but the weaker *form* of a signal whose strong form is item 3. The 69.81% comes from one research line (2505.11574); the "fluency survives" support leans partly on a *different* paper measuring a *different* thing (~4.4% decline in self-explanation). Stitching those into "selective" is an inference across non-comparable measurements. The within-study selectivity (item 3) is the strong version; this cross-domain version is the stitched one. Verification confirms the caution.

### 6. Provenance ⊥ fragility — the actual two-axis claim
**Impact: low as a claim; high as a test. (Source rated 4.)**
The title thesis, and explicitly the weakest *claim* because it is the unproven part — correctly labeled speculative. Its value is as a well-posed, falsifiable test (the within-modality predictions, especially "proof-text reasoning should break like code, not like chat"), not as a signal. Rate the question high; rate the assertion low. Its impact is entirely deferred to whether the probe runs.

### 7. The "small dose of sharp water" convergence (LoRA / quant recovery / action grounding)
**Impact: lowest. (Source rated 3.)**
The most evocative passage and the thinnest inference. Three mechanistically unrelated phenomena — low intrinsic rank of updates, margin restoration, symbol grounding — bundled under a pattern ("broad cheap base + small sharp dose") loose enough to describe most of transfer learning. Reads as insight; may be a selection effect. Correctly hedged in the paper ("if that pattern is real"). A critique of inferential weight, not of honesty.

**Excluded from ranking:** model collapse (Shumailov, *Nature*) — in absolute terms the most Established citation, but orthogonal: imported support, not a signal of *this* framework's value.

---

## Two inversions that govern this set

**Inversion 1 — prose quality is inverse to evidential weight.** The two most beautifully written moves (item 7, the convergence pattern; item 6, the provenance-as-second-axis frame) are the two weakest signals. Beautiful writing reads as confidence, and these are the places least entitled to it. The status note partly inoculates; the body still occasionally lets cadence carry a claim the evidence won't.

**Inversion 2 — highest evidence is highest concentrated risk.** The strongest-evidence item (3, step-localization) is also the most fragile to a single attack, because it rests on one author cluster (verified). The two items that survive scrutiny best — the framing (1) and the forward question (2) — are precisely the two that depend on *neither* prose carrying a claim *nor* one paper replicating.

**Standing conclusion:** defend the framing and the forward question; brace for the anchor and the prose. What feels strongest (clean anchor, beautiful passages) is exactly the seam a sharp reader pulls. What is actually strongest (the unglamorous inverse-problem framing, the insulated qualification question) is the part that does not depend on luck — replication luck or rhetorical momentum.

*The one verification that would move this ranking: independent replication of the step-localization result. If it lands, item 3 rises and the anchor's concentrated-risk caveat lifts. Until then, the ranking above holds.*

---

## Set 2 — logged June 2026 (impact × certainty framing)

A third independent pass arrived (a second was a duplicate of the field-signals doc and was not logged). This one ranks by **Impact × Certainty Status** — the best axis of the set, because it pairs each signal's importance with whether it is *true now* or *still a hypothesis awaiting compute*. That pairing is the secure-vs-contingent distinction this project runs on, applied per-signal. Logged not as a fresh list of scores but as the **cross-pass reconciliation**, because three passes now exist and the convergence between them is worth more than any single ranking.

### The convergent core (what survives all three passes)

Three independent rankings on three different axes — evidence × centrality (Set 1), question-generation, and impact × certainty (this set) — converge on the same substance while disagreeing on the numbers:

- **The inverse-problem framing / metaphor-decoupling is the durable center.** Set 1 ranked it #1 for impact; the question-generation pass ranked it #2; this pass names it "the absolute biggest signal." Crowned by all three. This is the most-replicated finding across every pass — and it is the part that is *ours* (the evidence underneath is the field's; the framing is the contribution).
- **The qualification question (retention > peak accuracy) is high-impact and explicitly a hypothesis.** All three rank it high; the honest ones flag it unproven. This pass marks it "Empirical Hypothesis" outright — the most honest of the three on this point. Same item as A8.
- **Provenance ⊥ fragility is high as a question, unproven as a claim.** All three place it there.
- **The speculative readings** (the "precious water" cross-domain pattern; precision-as-a-learned-resource) rank lower or are flagged not-yet-law by all three.

### Certainty split this pass makes explicit (its real contribution)

- **True Now** (methodological / cross-domain supported): hard ≠ fragile (the decoupling of complexity); the precious-water grounding pattern; telemetric evaluation (the four-outcome self-diagnosing instrument).
- **Empirical Hypothesis** (awaiting the protocol): retention-over-accuracy qualification; modality-as-pressure (provenance ⊥ fragility).

This reproduces, per-signal, the secure/contingent split established for the implications: the methodological signals hold now; the exciting capability claims are bets.

### Two flags — things in this doc NOT to absorb

- **545 vs. 332 examples (quantization recovery).** This pass cites ~545; Set 1's source cited ~332. Both are real but from *different studies in the same line* (2501.03035 reports 545; 2505.11574 reports 332). Not an inconsistency to reconcile — two separate results. The record uses 332 as primary (the later, step-localization paper) and notes 545 as the earlier figure.
- **The geometric overclaim in "modality as pressure."** This pass states provenance ⊥ fragility as mechanistic fact: proof-text reasoning "*will* share an *identical* low-bit geometric fragility profile... *because* both require the exact same fine-grained vector spacing." That "identical / because" asserts the geometric mechanism the paper explicitly holds as *unproven interpretation*. This is the one place the doc breaches the paper's own guard (geometry as interpretation, not measured fact). Logged as a **misread to not absorb**, not a finding — the paper's hedged version ("*may* share") is the correct form.

### The interpretive rule (the thing none of the three docs says about itself)

**Trust what survives all three rankings; discount the absolute numbers, which inflate as the rating axis softens.** Set 1 (hardest axis, evidence × centrality) gave the two-axis claim a 4/10. This pass (impact axis) rates its components 9/10. *Same claim, same evidence, different number — because different scale.* The escalation tracks the softness of the axis, not the strength of the evidence. The convergent core (framing + qualification-question-as-hypothesis) is the real signal; the 9s and 10s are coordinate-system artifacts. A conclusion that survives being measured three ways is more trustworthy than one that scores 10/10 on one way.

### Inversion 3 (this set adds it)

**The most flattering ranking is the least falsifiable.** The question-generation pass's headline ("analogy as question-generator," 10/10) and this pass's "flawless execution / completely outlives" are nearly impossible to be *wrong* — which means they carry the least information. The highest scores cluster on the softest, least-falsifiable axis. Discount accordingly: a signal is not strong because it scored 10 on the axis least able to fail it.

---

## Set 3 — logged June 2026 (evidence × practical-importance, Strong/Moderate/Weak scale)

A fourth pass, and the **most epistemically disciplined of all of them** — it grades Strong / Moderate / Weak-Open / Interpretive rather than inflated /10s, which resists the axis-softness inflation flagged above. It largely *confirms* the record, which is itself the finding (a fourth independent pass on a fourth axis converging on the same core). Two things it added, one of which moves a rating.

### Verification upgrade — the #1 signal is firmer than the anchor (this is the important one)

This pass ranks **"peak accuracy is an incomplete qualification metric"** at #1, Strong. Searched for independent support beyond the single step-localization line — and unlike the anchor, **this claim has broad, multi-source, independent backing**:
- Paraphrasing benchmark questions significantly lowers absolute scores across 34 LLMs — high benchmark scores do not capture robustness to real-world input variation (arXiv 2509.04013).
- A robustness survey states accuracy alone is insufficient for real-world reliability (arXiv 2505.18658).
- Production-evaluation work: static benchmark scores do not predict production reliability under distribution shift — concrete example, 96.6% on MATH-500 vs 13.59% on Humanity's Last Exam (LayerLens, 2026).
- Agent-evaluation survey: binary outcome metrics are insufficient; fine-grained evaluation is needed (arXiv 2503.16416).

**This is the first verification in the record that *strengthened* a signal rather than confining it.** The #1 claim does NOT depend on the unreplicated step-localization paper — it stands on independent ground.

### The split the #1 signal must be recorded with (it cuts both ways)

The headline divides into two claims with very different support, and this pass slightly conflates them:
- **"Peak accuracy is incomplete / robustness != accuracy"** -> **broadly, independently supported.** Strong is correct. *Well-replicated, and the field's, not ours.*
- **"...and precision-demand under quantization specifically predicts it, via step-localization"** -> **one research line, unreplicated** (verified, Set 1). The narrower *mechanism* is suggestive, not Strong.

So: the general signal is Strong and crowded; the specific mechanism that would make it *ours* is single-source. They must not be merged in the record.

### What this sharpens — the protocol's true position

The contribution sits in the gap. The field broadly knows "accuracy is incomplete" (Strong, established, not ours). What it lacks is a *clean, isolated way to measure precision-demand fragility* — which is the protocol. So the searches improve the positioning: the protocol is **not** claiming to discover the blind spot (the field knows it); it offers the **controlled instrument the established consensus lacks**. "The blind spot is established; here is a clean way to measure one slice of it" is a stronger, more honest position than "we found the blind spot."

### Convergence holds across all four passes

This pass's tiers map onto the record with no strain: Strongest (#1 accuracy-incomplete, #2 silent-failure, #3 stress-retention-informative) = the secure methodological + qualification core; Actionable-narrower (#4 implementation/CoT, #5 targeted-recovery) = the moderate middle; Open (#6 precision-demand-as-predictor, #7 provenance, #8 geometry) = the contingent/interpretive tail. Same shape as Sets 1-2. Four independent passes, four axes, **stable substance ordering** — the convergence is now strong enough to treat as the record's most reliable output. Its disciplined Strong/Moderate/Weak grading also confirms the inversion: when the axis is rigorous, the speculative items (geometry, provenance) self-report as Weak/Interpretive rather than scoring 9/10.

---

## Set 4 — logged June 2026 (analogy-predicted-it framing, /10 scale)

A fifth pass (fourth distinct). It **converges with all prior passes on substance ordering** — fifth independent pass, same shape: precision-demand / framing / step-localization at top, provenance / geometry lower. But it adds **no new verified signal**, and it is the **most inflated pass in the record** — every signal 6-10/10, "decisive," "the backbone," "this axis is real." It is the clearest single instance of the pattern Inversion 3 names. Logged briefly, with two overclaims flagged as misreads-not-findings, because a record disciplined for four sets must not relax on the fifth.

### Overclaim 1 — "multiple independent studies" for a single-source mechanism (the important catch)

This pass rates precision-demand fragility **10/10, "confirmed by multiple independent studies."** The record has verified **twice** (Sets 1 and 3) that the step-localization mechanism rests on **one author cluster, unreplicated**. This pass transfers the broad claim's genuine multi-source support onto the narrow mechanism, then rates the merged thing decisive. This is the conflation Set 3 flagged, now hardened into a "10/10." The disentangling stands:
- **"Peak accuracy incomplete / robustness != accuracy"** -> multiple independent studies (verified, Set 3). Strong.
- **"Precision-demand via step-localization is the confirmed axis"** -> one line, unreplicated (verified, Sets 1 + 3). NOT "multiple independent studies."

Do not absorb "multiple studies confirmed precision-demand-via-step-localization." We checked; they did not. The general signal is strong and the field's; the specific mechanism that would make it ours is single-source.

### Overclaim 2 — "the analogy encodes a latent mechanistic model" (the seductive one)

This pass's #8 claims the analogy "predicted the right axes, mechanisms, failure modes, and instrument before the literature confirmed them... it encodes a latent mechanistic model of transformers." This is the **exact claim the whole project was built to avoid** — "the analogy is true." The honest, record-held version: the analogy was a good *question-generator* (Set 2), and is explicitly *not* a validated mechanism — the papers themselves hold the geometry as unproven interpretation. "Encodes a latent mechanistic model" promotes the scaffolding back into a theory. Flagged as a misread. The correct framing remains: the analogy pointed true and then made itself optional; it did not turn out to be a secret mechanistic model.

### Net of Set 4

Convergence confirmed (fifth pass, stable ordering). No new signal. Two overclaims that the record's own rules predict and reject. Set 4's value is almost entirely as **confirmation that the convergence is robust and that the inflation tracks axis-softness exactly as Inversion 3 says** — its 10/10s, its "multiple studies," and its "latent mechanistic model" are the three inflations the record was built to catch, all in one pass.

---

## Standing summary across all five passes

Five independent rankings, five axes (evidence x centrality; field-establishedness; question-generation; impact x certainty; evidence x practical-importance; analogy-predicted-it). The convergence is now the record's most reliable output:

- **Durable center, crowned by every pass:** the inverse-problem framing (quantization as measurement instrument) and the stress-retention qualification question. These are *ours* (framing) and *insulated* (question needs no anchor). Defend these.
- **Strong but the field's, not ours:** "peak accuracy is incomplete" (multi-source verified). Build on it; do not claim it.
- **Strong evidence, concentrated risk:** step-localization (single author cluster, verified twice). The spine that needs replication we do not control.
- **High as a question, unproven as a claim:** provenance ⊥ fragility. The probe's target, not a finding.
- **Speculative tail, self-labeled weak on rigorous axes:** geometry mechanism, precision-as-resource, the small-sharp-water pattern.

The three inversions hold across all five passes: (1) prose quality is inverse to evidential weight; (2) highest evidence is highest concentrated risk; (3) the most flattering ranking is the least falsifiable, and numbers inflate as the axis softens.

**The one move that changes any of this is data** — running the protocol. Five rankings have not moved the substance ordering one inch, because ranking is not measurement. The next real input is a result, not a sixth pass.

---

## Meta-note — the ledger turned on itself (logged June 2026)

A sixth pass proposed that the claim-ledger *itself* is the project's transferable practice-level contribution — "a way to keep speculative AI frameworks honest before data arrives." Recorded here, but filed honestly:

- **What is real (anchor):** a claim-ledger was kept on this project and it functioned — it caught overclaims, separated evidential registers, and let verification move ratings both ways (up in Set 3, rejecting overclaims in Set 4).
- **What is a bet (open test):** that this is a *transferable method* useful to other projects or other authors. n = 1, run by someone already disposed to the discipline. Whether it helps someone not so disposed is untested. Filed as **open test, not finding.**
- **The slip caught:** the proposing documents stated "the practice-level contribution is already real / valuable / the most transferable thing" — which promotes a transfer-hope into a demonstrated contribution. That is *implication masquerading as inference* — committed in the documents praising the project for avoiding it. The same gravity as Set 4's "latent mechanistic model": each retelling promotes the thing one rung up the evidential ladder.

The leashed version, which is defensible: **a claim ledger makes the epistemic status of framework-driven work *inspectable*** — not "solves overclaiming," not "already valuable as a method." Distilled into the one-page `claim-ledger-practice-note.md`, framed as offered-not-proven.

This entry exists because a record that did not note its own most-flattering moment being declined would be incomplete. The ledger stayed honest about itself: offered the crown, it filed the crown under *open test*.
