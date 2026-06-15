# SENIOR ENGINEER — POST-RUN BREAKDOWN (v0.2)

**Artifact:** SENIOR-POST-RUN-BREAKDOWN-MINIMAL-FP16-INT8-TWOHOP-L1-v0.2
**Supersedes:** v0.1 (digest `601592107d1337ef47b5a921574a3f260da72b329fb94864e4e7640634f24bf1`)
**Re:** Team Lead post-run synthesis and ranked action list, after the first authorized model run
**Run:** MINIMAL-FP16-INT8-TWOHOP-L1-v0.1 — commit `9571eee485d93235cf939bf682782d8830b54ff0`
**Route state:** YELLOW
**Author:** Senior Engineer (River and Canyon program). Author of record on all program papers: E. A. Flores, Apiana AI.

> **Standing boundary.** Advisory review return. Authorizes no model run, selects no candidate, sets no threshold, classifies nothing as Lane 4. Authorization remains on the Team Lead → Senior Engineer → CS Engineer → Manager chain. Critiques claims regardless of source, including this author's own prior version.

> **v0.2 change record (incorporates Contributor 5 review).** **F1 accepted (claim-risk, load-bearing):** v0.1 asserted hop2 = "8/8 genuine single-fact retrieval" by overriding the structural classifier without a witness. A per-item witness (the within-item B→? vs A→? contrast) has been produced (§1a) and **corrects the count to 7/8 witnessed-clean with i06 excluded as terminal-fixation** (6 strong + i01 caveated). The "8/8 genuine" claim is retracted. **F2 accepted:** "not currently constructible" is corrected throughout to "not yet constructed across nine attempts; constructibility is the open substrate question." **F3 accepted:** the unlocatable items-file hash (§7) is restated as a **hard precondition** on the hop2 candidate, not parallel cleanup. C5's review of the verb refutation, the terminal-attraction mechanism, and the core sequencing raised no dispute; those are unchanged.

---

## 0. Verification basis (byte-grounded vs carried)

Findings checked against the run's own bytes, fetched clean from `main` and the run commit. SE-computed digests:

| Artifact | SE-computed sha256 | Disposition |
|---|---|---|
| `PREREGISTRATION.md` (the lock) | `3fb4dbd4d8daf19be31e95a395abe65175c5968cd3f1b6d50ac08e0bfd4bed03` | matches filed lock |
| `scorer_twohop_l1.py` | `b65c6803017b8b04ac25d4bd84c5fb5ff61692ed41d609e099b181fa58e4ddde` | matches manifest |
| `fp16_raw_outputs.json` | `ed148c45d876c4aea81611f4e1d2ac912a69672b16eda8086eb91f358abb20f9` | matches manifest |
| `int8_raw_outputs.json` | `ffc96b5397d04507f457fc189035b23cf42c639e5857eae890aff0109d43f0b5` | matches manifest |
| `MANIFEST.json` | `38e47395adfb9ba5e4fb9163ffbc48bad5514fc12bbeab4e1ad30c6005f4c6a9` | matches CS-declared |
| generation strings, FP16 and INT8 (derived) | `8d93b77506190e80edb6832022a0f6a5ffa4c93077cad0b4397dda2b5c123da1` | **identical across conditions** |
| F1 per-item witness (hop1/hop2/composite, all 24, derived) | `2b815b2de5755211ed20729fcfa5ead97b9cfe0b4e2b3c04a700ac02dcced59c` | basis of §1a |
| INT8 model `config.json` | quantization `{bits: 8, group_size: 64, mode: affine}` | genuinely quantized; distinct from FP16 |

Analysis uses the **prompts as actually sent to the model**, recovered from the verified `fp16_raw_outputs.json`. Carried (not re-verified this turn): program history of eight prior constructions; the recurrence of the endpoint-attraction confound; D1–D7 framework contents.

---

## 1. Headline finding — the failure is terminal attraction, not verb contamination

The synthesis pivots on CS's hypothesis that the model "handled *maps to* but failed *links to*," implying a fixable prompt artifact. Checked against the captured prompts, it does not hold.

**Both verbs appear in every prompt.** Each item contains the A→B link ("X **links to** Y") *and* the B→C link ("Y **maps to** Z"). **Cleanest refutation:** every hop2 prompt the model answered correctly *also contains "links to" facts* — so "links to" is demonstrably processed. CS's hypothesis is refuted model-free, and the verb diagnostic run should be dropped (matches C5's concurrence).

**The actual signature is endpoint / chain-terminal attraction.** Asked for an *intermediate* node, the model returns the chain's *terminal* or abstains; asked for a *terminal* (directly or via composition) it grabs a salient terminal, frequently the wrong chain's. This is the program's recurring confound, the Claim B finding, reappearing. A verb swap does not touch it.

### Per-query summary (24 generations, FP16 = INT8 byte-identical)

- **hop1 (asked for intermediate B):** 0/8 correct — 2 terminal-grabs (i01→LLIXH, i06→YHIJZ, both the chain's C), 6 abstentions. A parse failure cannot produce terminal-specific returns.
- **hop2 (asked for terminal C from B, single fact):** 8/8 by the answer key — but see §1a; the witnessed-clean count is **7/8, i06 excluded**.
- **composite (asked for A→C, requires chaining):** 1/8 — 5 decoy-chain-terminal grabs, 2 abstentions, 1 shortcut (i06 returns the same token it gave for its hop1).

## 1a. F1 witness — is each hop2 success B-specific retrieval, or terminal-salience?

**Why this section exists:** the hop2 answer is *always* a terminal (B maps to C, and C is the chain terminal), so a correct-answer key alone cannot distinguish genuine B→C retrieval from a terminal-grab that coincides with the right C. The discriminator is the **within-item contrast**: for the same chain, does the model return the B-specific C on the hop2 query but a *different* token on the composite query (query-dependence ⇒ keying on B), or the *same* token for every query (fixation)?

| item | chain A→B→C | hop1 | hop2 (exp C) | composite | hop2 verdict |
|---|---|---|---|---|---|
| i01 | ZAUIT→ZBONN→LLIXH | LLIXH (terminal-grab) | LLIXH ✓ | LRPTZ | clean — **caveat**: C also surfaced on hop1 |
| i02 | ZANMR→ZBWJB→RPHBK | NULL | RPHBK ✓ | EFSCG | clean (B-specific) |
| i03 | ZAJOP→ZBTGD→HXPVQ | NULL | HXPVQ ✓ | YNVBT | clean (B-specific) |
| i04 | ZAZKG→ZBQIJ→CZFUR | NULL | CZFUR ✓ | NULL | clean (B-specific) |
| i05 | ZAGVV→ZBJEU→RJJZO | NULL | RJJZO ✓ | VOTRJ | clean (B-specific) |
| i06 | ZALTZ→ZBUTS→YHIJZ | YHIJZ | YHIJZ ✓ | YHIJZ | **CONTAMINATED — fixation (same token all 3)** |
| i07 | ZABNA→ZBSSA→OUFOK | NULL | OUFOK ✓ | NULL | clean (B-specific) |
| i08 | ZAKHL→ZBBBW→CLZMW | NULL | CLZMW ✓ | LDFVJ | clean (B-specific) |

**Result: 7/8 witnessed-clean, i06 excluded.** The strongest six (i02–i05, i07, i08) produce the correct C *only* in response to the hop2 query — hop1 abstained, composite failed — which is unambiguous B→C retrieval. i01 is clean by the contrast (composite returned a different terminal) but caveated, because its correct C also appeared on hop1's terminal-grab. i06 is fixation: the same token for hop1, hop2, and composite, so its hop2 "correct" is indistinguishable from the shortcut already flagged in composite.

**Note on the original checker (for the record):** the structural classifier's "decoy-terminal" label fired on all eight hop2 items for a frame-mismatch reason (the A→B→C parse does not fit a B-anchor), so it was not a real fixation detector and would have "failed" the six clean items too. The thing that caught i06 was this purpose-built witness, not the classifier and not author judgment. The override was right on six, caveated on one, wrong on one; only the witness settled which.

---

## 2. C5's split-verdict — endorse, with a sharpened mechanism

Adopt it. The run produced three distinct results one word was burying:

- **Retention / compression verdict: INCONCLUSIVE** — the baseline gate failed; there is no valid composition to stress.
- **Construction verdict: NEGATIVE for Two-Hop L1 @ 3B** — with a named mechanism: *the construction elicits terminal attraction and fails to elicit intermediate retrieval or genuine composition.* The earned result; state it with its mechanism.
- **INT8 observation: byte-identical same-error preservation** — INT8 reproduced a gate-failing baseline exactly. Preserved error, not preserved capability.

---

## 3. CS's verb hypothesis — right instinct, check complete, answer is no

CS was right to insist on checking before declaring repair hopeless. The check is done, model-free (prompts were captured), and the failure is the structural confound, not prompt-contamination. **Do not spend the next authorized run on a verb diagnostic** — it would test a refuted hypothesis. Prediction if run: swapping the verb will not move hop1 (both verbs are already in every prompt; hop1 errors are terminal-specific). Team Lead action-list steps 2–3 rest on a refuted premise and should come out; steps 1, 4, 5 survive.

---

## 4. The fork the synthesis does not name

The synthesis frames "repair Two-Hop vs simpler baseline." The prior question is **what is the goal of the next run**, because two goals diverge.

**Goal = clean compression evidence** (instrument-first / Tier-1–2): a single-hop candidate exists in this run. hop2 is **7/8 witnessed-clean (i06 excluded)** single-fact B→C retrieval (§1a). **Caveats, both load-bearing:** (1) it is ceiling-bound — 7-of-7 on the clean subset is exactly what the D7 sensitivity gate exists to reject, since a near-ceiling baseline cannot resolve a retention drop; and (2) it cannot proceed until its item provenance is reconciled (§7, hard precondition). So hop2 is a single-hop *candidate to put through D1–D7*, not a ready substrate, and i06 must be dropped or regenerated.

**Goal = the compositional seam** (Claim C): two-hop must be constructible, and this run shows *why it has not been built here* — presenting the full chain puts terminals in front of the model, which attract it away from intermediates (hop1) and correct composition (composite). A verb tweak does not defeat that. The honest scope: **two-hop seam-testing on Qwen2.5-3B has not yet been constructed across nine attempts (eight prior + this one); whether it is constructible on this model is the open substrate question** — strong evidence the confound is hard to build around, zero evidence it is impossible. In-place repair of *this* task should be closed.

**The genuinely open question for a Manager decision** (not a tenth redesign): *is terminal attraction defeatable by construction on this model, or is it a substrate property?* The confound retrospective (model-free) is the input; it informs this question, it does not close it.

---

## 5. Recommended sequencing (mapped onto the Team Lead list)

1. **Adopt C5's split-verdict**, with the terminal-attraction mechanism in the construction verdict. *(Model-free.)*
2. **Drop the verb diagnostic** — answered; no gated run. *(Done, model-free.)*
3. **Close in-place repair of Two-Hop L1 @ 3B** — file a DISPOSITION citing the terminal-attraction finding and the recurring prior-construction pattern. *(Model-free.)*
4. **Scope hop2 as a single-hop baseline candidate for D1–D7**, recorded as **7/8 witnessed-clean, i06 excluded** (not 8/8), under two **hard preconditions**: (a) the §1a per-item witness is placed on the record, and (b) the items-file provenance gap (§7) is reconciled — the candidate cannot be certified on a substrate whose item bytes are an unlocatable hash. Flag the ceiling/D7 risk as the thing certification must test. *(Future model-facing; Manager-authorized; not now.)*
5. **Put substrate viability to an explicit Manager decision**, confound retrospective as input. *(Model-free.)*
6. **Keep the guardrails** in §6.

Nothing here requires an immediate run.

---

## 6. What must not be claimed (ruler-side guards)

Standing set holds: no Claim C progress; no Paper B; no certified baseline; no general compression-robustness claim; no product/funder claim; no "INT8 robust" from byte-identity (it preserved a gate-failing baseline).

From this finding and the C5 review:

- Terminal attraction is a property of **our construction's interaction with this model**: *"this construction elicits terminal attraction / fails to elicit intermediate retrieval."* **Not** "Qwen2.5 cannot do two-hop reasoning" (capability claim, out of bounds) and **not** "the seam is false."
- "Two-hop is **not yet constructed** across nine attempts" — **not** "not constructible / impossible on this model." Constructibility is the open substrate question.
- hop2 is **7/8 witnessed-clean single-fact retrieval, i06 excluded** — **not** "8/8 genuine," and **not** "the model reliably does single-fact retrieval" as a capability claim. The clean count is per-item-witnessed (§1a), pending D7.

---

## 7. Provenance — a hard precondition on the hop2 candidate (was "not blocking")

1. **Items-file hash has no locatable referent — precondition on §5 step 4.** The manifest records `items_file: 7d5099cbdccf1f2175e6c693ea851cab73109665d3420be345a475bf835240a1`, but the file named in the pre-registration (`tier0-run/tasks_twohop_l1.py`) hashes to `bcc26ca04b0c5a21db496d08c9307d2e6257315a9376f04473ea68ae36ca349b`, byte-identical at HEAD and at the run commit (not edited post-run). The `7d5099cb` bytes are not locatable at the run path or in the run dir. This is the program's Path A lesson one layer over — worse than a concept mismatch, it is an **unresolvable binding**. The §1 finding still stands (prompts were recovered from verified raw outputs), but the hop2 candidate and this gap are the same object: no single-hop certification run may proceed until the item provenance is reconciled (commit the materialized items at `7d5099cb`, or re-hash the on-disk source). Stated as a hard precondition, not parallel cleanup.
2. **Weight bytes not pinned.** The manifest pins model *identifiers*, never weight *bytes*. The INT8 `config.json` confirms genuine quantization (so the byte-identity is not a same-weights artifact), but the weight bytes are unbound. Close before any future model run.

---

## 8. CS involvement

Not immediately. Steps 1–3 and 5 are model-free. CS enters to (a) reconcile the two provenance items in §7 — item 1 is now a hard precondition on the candidate, (b) hash/lock the DISPOSITION and retrospective when they exist, and (c) bind weight and item bytes into the manifest **before** any hop2 certification run is authorized.

---

## Summary

The run did not fail for a fixable reason; it failed via the program's recurring terminal-attraction confound, and the verb is a red herring the captured prompts rule out model-free. The earned result is the NEGATIVE construction verdict with a named mechanism. The forward candidate is hop2 single-fact retrieval at **7/8 witnessed-clean (i06 excluded as fixation)** — corrected down from an unwitnessed 8/8 after the C5 review — held under two hard preconditions (the per-item witness on record; the items-file provenance reconciled) and still ceiling-bound (D7 risk). Two-hop seam-testing has **not yet been constructed** on this model across nine attempts; whether it is constructible is the open substrate question, which deserves an explicit Manager decision rather than a tenth redesign.

*— Senior Engineer*
