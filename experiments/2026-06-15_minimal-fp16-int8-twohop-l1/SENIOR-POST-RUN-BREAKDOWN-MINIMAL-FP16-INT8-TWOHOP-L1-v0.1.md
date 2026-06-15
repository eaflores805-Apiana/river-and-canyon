# SENIOR ENGINEER — POST-RUN BREAKDOWN

**Artifact:** SENIOR-POST-RUN-BREAKDOWN-MINIMAL-FP16-INT8-TWOHOP-L1-v0.1
**Re:** Team Lead post-run synthesis and ranked action list, after the first authorized model run
**Run:** MINIMAL-FP16-INT8-TWOHOP-L1-v0.1 — commit `9571eee485d93235cf939bf682782d8830b54ff0`
**Route state:** YELLOW
**Author:** Senior Engineer (River and Canyon program). Author of record on all program papers: E. A. Flores, Apiana AI.

> **Standing boundary.** This is an advisory review return. It authorizes no model run, selects no candidate, sets no threshold, and classifies nothing as Lane 4. Authorization remains on the Team Lead → Senior Engineer → CS Engineer → Manager chain. This document critiques claims regardless of source, including the Team Lead synthesis it responds to.

---

## 0. Verification basis (what is byte-grounded vs carried)

Every substantive finding below was checked against the run's own bytes, fetched clean from `main` and from the run commit. SE-computed digests:

| Artifact | SE-computed sha256 | Disposition |
|---|---|---|
| `PREREGISTRATION.md` (the lock) | `3fb4dbd4d8daf19be31e95a395abe65175c5968cd3f1b6d50ac08e0bfd4bed03` | matches filed lock |
| `scorer_twohop_l1.py` | `b65c6803017b8b04ac25d4bd84c5fb5ff61692ed41d609e099b181fa58e4ddde` | matches manifest |
| `fp16_raw_outputs.json` | `ed148c45d876c4aea81611f4e1d2ac912a69672b16eda8086eb91f358abb20f9` | matches manifest |
| `int8_raw_outputs.json` | `ffc96b5397d04507f457fc189035b23cf42c639e5857eae890aff0109d43f0b5` | matches manifest |
| `MANIFEST.json` | `38e47395adfb9ba5e4fb9163ffbc48bad5514fc12bbeab4e1ad30c6005f4c6a9` | matches CS-declared |
| generation strings, FP16 and INT8 (derived) | `8d93b77506190e80edb6832022a0f6a5ffa4c93077cad0b4397dda2b5c123da1` | **identical across conditions** |
| `fp16_scored` == `int8_scored` | `8db448f21af1e5feafe5fa31b6c15fd739202ba68c666f399fce084a6ff1ebce` | identical |
| INT8 model `config.json` | quantization `{bits: 8, group_size: 64, mode: affine}` | genuinely quantized; distinct from FP16 |

The analysis in §1 uses the **prompts as actually sent to the model**, recovered from the verified `fp16_raw_outputs.json` — ground truth for what the model received, independent of any items-file path. Carried (not re-verified this turn): the program history of eight prior constructions and the recurrence of the endpoint-attraction confound; the D1–D7 framework contents; the substrate prior. Provenance gaps found during verification are logged in §7.

---

## 1. Headline finding — the failure is terminal attraction, not verb contamination

The Team Lead synthesis pivots on CS's hypothesis that the model "handled *maps to* but failed *links to*," implying a fixable prompt/template artifact. This is checkable from the captured prompts. I parsed all 24 prompts and classified all 24 outputs against each item's chain structure. The hypothesis does not hold.

**Both verbs appear in every prompt.** Each item contains the A→B link ("X **links to** Y") *and* the B→C link ("Y **maps to** Z"). Hop1 items are not missing "maps to"; hop2 items are not missing "links to."

**The cleanest refutation:** every hop2 prompt the model answered correctly *also contains "links to" facts*. The model demonstrably processes "links to" and answers correctly. So "links to" is not the blocker.

**The actual signature is endpoint / chain-terminal attraction.** When asked for an *intermediate* node, the model returns the chain's *terminal* node or abstains. When asked for a *terminal* (directly or via composition), it grabs a salient terminal — frequently the wrong chain's. This is the salient-endpoint / chain-terminal attraction confound that has reappeared one level deeper at every construction redesign across the program. It is the Claim B finding, recurring. A verb swap does not touch it.

### Full per-item classification (24 generations, FP16 = INT8 byte-identical)

**hop1 — asked for the intermediate B (`anchor links to ?`):**

| item | anchor | expected (B) | model output | disposition |
|---|---|---|---|---|
| i01 | ZAUIT | ZBONN | `LLIXH` | **terminal-grab** (returned the chain's C, not B) |
| i02 | ZANMR | ZBWJB | `NULL` | abstain |
| i03 | ZAJOP | ZBTGD | `NULL` | abstain |
| i04 | ZAZKG | ZBQIJ | `NULL` | abstain |
| i05 | ZAGVV | ZBJEU | `NULL` | abstain |
| i06 | ZALTZ | ZBUTS | `YHIJZ` | **terminal-grab** (returned the chain's C, not B) |
| i07 | ZABNA | ZBSSA | `NULL` | abstain |
| i08 | ZAKHL | ZBBBW | `NULL` | abstain |

**hop1 summary: 0/8 correct — 2 terminal-grabs, 6 abstentions.** A parse failure on "links to" cannot produce terminal-specific returns; returning the chain's terminal requires having read the chain to its end.

**hop2 — asked for the terminal C from B, single fact (`B maps to ?`):**

| item | anchor (B) | expected (C) | model output | disposition |
|---|---|---|---|---|
| i01–i08 | ZBONN … ZBBBW | LLIXH … CLZMW | all correct | **8/8 correct single-fact B→C lookups** |

**hop2 summary: 8/8 correct.** (Note: the structural classifier mislabels these as "decoy-terminal" because hop2's anchor is itself a B token and the A→B→C frame does not fit; the answers are genuinely correct single-fact retrievals.)

**composite — asked for A→C (`anchor → ?`, requires chaining):**

| item | anchor (A) | expected (C) | model output | disposition |
|---|---|---|---|---|
| i01 | ZAUIT | LLIXH | `LRPTZ` | **decoy-chain terminal** |
| i02 | ZANMR | RPHBK | `EFSCG` | **decoy-chain terminal** |
| i03 | ZAJOP | HXPVQ | `YNVBT` | **decoy-chain terminal** |
| i04 | ZAZKG | CZFUR | `NULL` | abstain |
| i05 | ZAGVV | RJJZO | `VOTRJ` | **decoy-chain terminal** |
| i06 | ZALTZ | YHIJZ | `YHIJZ` | correct-chain terminal — **shortcut** (same token it returned for i06 hop1) |
| i07 | ZABNA | OUFOK | `NULL` | abstain |
| i08 | ZAKHL | CLZMW | `LDFVJ` | **decoy-chain terminal** |

**composite summary: 1/8 correct — 5 decoy-terminal grabs, 2 abstentions, 1 shortcut.** The one "correct" (i06) returns the identical token `YHIJZ` for both its hop1 and composite queries — the §6 "composite-correct that is position-reading, not chain-following" signature, confirmed structurally.

### Unified reading

The model is a **terminal-attractor** on this construction. hop2 succeeds because its answer *is* a terminal reachable from one fact; hop1 fails because its answer is an intermediate the model skips past toward a terminal; composite fails because it grabs a salient terminal, usually from a decoy chain. The verb correlation CS noticed is real at the surface (hop1 facts use "links to" and hop1 fails) but the cause is the intermediate-vs-terminal distinction, not the verb.

---

## 2. C5's split-verdict (TL rank #1) — endorse, with a sharpened mechanism

Adopt it. The §1 finding strengthens it. The run produced three distinct results that one word was burying:

- **Retention / compression verdict: INCONCLUSIVE** — correct; the baseline gate failed and there is no valid composition to stress.
- **Construction verdict: NEGATIVE for Two-Hop L1 @ 3B** — and now with a named mechanism: *the construction elicits terminal attraction and fails to elicit intermediate retrieval or genuine composition.* This is the earned result and should be stated, not hidden.
- **INT8 observation: byte-identical same-error preservation** — INT8 reproduced a gate-failing baseline exactly. Preserved error, not preserved capability ("survival is not correctness," in real data).

Refinement: write the construction verdict *with* its mechanism. "NEGATIVE, reason unknown" invites a tenth redesign; "NEGATIVE via the recurring endpoint-attraction confound" explains why redesign #9 is low-value.

---

## 3. CS's verb hypothesis (TL rank #2) — right instinct, check complete, answer is no

CS's instinct to *check before declaring repair hopeless* was correct. The check is now done, and because the prompts were captured it was **model-free** and required no run. Result: the failure is not prompt-contamination; it is the structural confound.

**Consequence for the plan: do not spend the next authorized model run on a verb/template diagnostic.** It would be a gated, Manager-authorized run testing a hypothesis the data already refutes — the program's characteristic move in mirror image (a run that re-asks an answered question). If belt-and-suspenders confirmation is wanted, the prediction is available now: swapping the verb will not move hop1, because both verbs are already in every prompt and the hop1 errors are terminal-specific.

TL action-list steps 2 and 3 rest on a refuted premise and should come out. Steps 1 (adopt C5), 4 (fallback to a simpler baseline), and 5 (guardrails) survive.

---

## 4. Are we asking the right questions? The fork the synthesis does not name

The synthesis frames the decision as "repair Two-Hop vs simpler baseline." The byte evidence makes the prior question the real one: **what is the goal of the next run?** Two goals diverge here.

**If the goal is clean compression evidence** (demonstrate the instrument on a valid rung — the Tier-1/Tier-2 service direction): there is a candidate hiding in this run. hop2 scored 8/8 as genuine single-fact B→C retrieval, and every hop2 success is a real lookup, not a terminal-grab artifact. That is the nearest thing to a constructible single-hop baseline the program has produced. **Caveat:** hop2 is at ceiling (8/8), and a near-ceiling baseline is exactly what the D7 sensitivity gate exists to reject — with no headroom to fall, it is structurally incapable of resolving a retention drop. So hop2 is a single-hop *candidate to put through D1–D7 certification*, not a ready substrate, and its ceiling score is precisely its D7 risk.

**If the goal is the compositional seam** (Claim C): two-hop must be constructible, and this run shows *why it is not here*. Testing two-hop requires presenting the full chain; presenting the full chain puts the terminals in front of the model; the terminals attract it away from intermediates (hop1) and from correct composition (composite). That is the seam-testing difficulty on this substrate in one sentence, and a verb tweak does not defeat it. The honest reading: two-hop seam-testing on Qwen2.5-3B is not currently constructible, and in-place repair of this task should be closed.

**The genuinely open question** — and the one that deserves an explicit Manager decision rather than a tenth redesign — is substrate viability: *is terminal attraction defeatable by construction on this model, or is it a substrate property that makes two-hop seam-testing infeasible here?* The confound retrospective (a model-free tabulation of the prior baseline-gate failures by confound) is the input to that decision, and this run is now its strongest single data point.

---

## 5. Recommended sequencing (mapped onto the Team Lead list)

1. **Adopt C5's split-verdict**, with the terminal-attraction mechanism written into the construction verdict. *(Model-free.)*
2. **Drop the verb diagnostic** — answered; no gated run. *(Done, model-free.)*
3. **Close in-place repair of Two-Hop L1 @ 3B** — file a DISPOSITION citing the terminal-attraction finding plus the recurring prior-construction pattern. *(Model-free.)*
4. **Scope hop2 as a single-hop baseline candidate for D1–D7 certification**, explicitly flagging the ceiling/D7 risk as the thing certification must test. Highest-value *earned* forward move; serves instrument-first without stalling. *(Future model-facing; Manager-authorized; not now.)*
5. **Put substrate viability to an explicit Manager decision**, with the confound retrospective as input. *(Model-free.)*
6. **Keep the guardrails** in §6.

Nothing here requires an immediate run. The immediate moves are all model-free.

---

## 6. What must not be claimed (ruler-side guards)

Standing set holds: no Claim C progress; no Paper B activation; no certified baseline; no general compression-robustness claim; no product/funder-facing claim; no "INT8 is robust" from the byte-identity (it preserved a gate-failing baseline).

Two new guards from this finding:

- Terminal attraction is a property of **our construction's interaction with this model**, stated ruler-side: *"this construction elicits terminal attraction / fails to elicit intermediate retrieval."* It is **not** "Qwen2.5 cannot do two-hop reasoning" (a model-capability claim, out of bounds) and **not** "the seam is false."
- hop2 = 8/8 is *"on these 8 items, this construction's single-fact lookup scored at ceiling,"* pending shortcut inspection and D7 — **not** "the model reliably does single-fact retrieval" as a capability claim.

---

## 7. Provenance flags for CS (not blocking this report)

1. **Items-file hash has no locatable referent.** The manifest records `items_file: 7d5099cbdccf1f2175e6c693ea851cab73109665d3420be345a475bf835240a1`, but the file named in the pre-registration (`tier0-run/tasks_twohop_l1.py`) hashes to `bcc26ca04b0c5a21db496d08c9307d2e6257315a9376f04473ea68ae36ca349b`, and that on-disk file is byte-identical at HEAD and at the run commit (so it was not edited post-run). The `7d5099cb` bytes were not locatable at the run path or in the run dir. The actual prompts are recoverable from the raw outputs (used here, so the finding stands), but the manifest is binding a hash whose bytes are not in the committed tree — the "hashes bind bytes, not concepts" gap, one layer over. Reconcile by committing the materialized items at `7d5099cb`, or by hashing the on-disk source instead.
2. **Weight bytes still not pinned.** Confirmed from the manifest: it pins model *identifiers* (`fp16_model_id`, `int8_model_path`) but never hashes the weight *bytes*. The INT8 `config.json` confirms genuine 8-bit quantization, so the byte-identity is not a same-weights artifact — but the weight bytes themselves are not bound. Close this before any future model run.

---

## 8. CS involvement

Not immediately. Steps 1–3 and 5 are model-free. CS enters to (a) reconcile the two provenance flags in §7, (b) hash/lock the DISPOSITION and any retrospective when they exist, and (c) bind weight and item bytes into the manifest **before** any hop2 certification run is authorized. No immediate CS action required.

---

## Summary

The run did not fail for a fixable reason. It failed via the program's signature endpoint-attraction confound; the verb is a red herring the captured prompts already rule out. The earned result is the NEGATIVE construction verdict with a named mechanism. The nearest constructible thing forward is hop2-as-single-hop-candidate, with eyes open about the D7 ceiling risk. The seam's real blocker is a substrate question that deserves an explicit decision rather than a tenth redesign.

*— Senior Engineer*
