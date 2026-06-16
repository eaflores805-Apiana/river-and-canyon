# PATH-A-FP16-R6CAT-DIAGNOSTIC-NOTE-v0.1

**E. A. Flores**, Apiana AI, Inc. — June 16, 2026
*River and Canyon · Path A. Prepared by the Senior Engineer. Descriptive post-hoc diagnostic.*

> **What this is.** A read-only, descriptive partition of the **R6cat ("other") bucket** from the locked Path A FP16 constructibility run (commit `265114b`), produced to inform the next construction. It answers one question: *where, in each item's layout, did the 38 off-map composite responses come from?*
>
> **What this is NOT.** Not a re-score. Not a new result of record. It changes **no** verdict, **no** category definition, **no** threshold. The run outcome remains **FAIL** exactly as locked. It is not a capability claim, not Claim C, not Paper B, and it authorizes nothing — in particular, no re-run (a re-run requires a new locked pre-registration; §17).
>
> **The one discipline this note holds above all (per C5 claim-risk).** The finding is **positional** — *where the tokens sit* — never **mechanistic** — *what computation produced them*. The decoy-traversal reading is labeled throughout as a **next-hypothesis, not a finding**.

## 0. Bytes analyzed (all SE-fetched and digest-verified)

- Run commit `265114b92a38656534d7e630ad84130a535f67dc`.
- `scored.json` (`b46725bf…`) — per-item composite tokens + categories (binding scorer output).
- `items_materialized.json` (`bfcda897…`) — per-item ground-truth entity sets (target, decoy_chains, depth_2_competitors, holds_facts, direct_query_filler), generator seed, conformance.
- `fp16_raw_outputs.json` (`10fc1732…`) — raw generations.
- Governed by pre-registration v0.3 (`d9bd9b21…`) under definition v0.4 (`4b616afb…`).

*Provenance correction (credit CS).* An earlier statement that the per-item entity sets were unavailable was wrong: they are in `items_materialized.json`, on the same commit. That file also records the **item-generator seed `20260615`** and **per-item conformance 96/96** — closing the seed open-slot and confirming all 96 items were admissible.

## 1. The question

The run's predicted-failure (on-map) categories were near-empty — R2 (target-terminal-grab) 4.2%, R4 (decoy-terminal-grab) 2.1%, R4b (depth-competitor-grab) 0/96, R3 (stopped-short) 11.5%, R5 (abstain) 8.3%. The mass was **R6cat = 39.6% (38/96)**: the model committed to entities outside every named-failure category. Per definition v0.4, a high *other* rate signals the construction/scorer is mis-specified — so the question for the next construction is **which** layout slots those 38 tokens occupy.

## 2. Method and validation

Two independent classifications, plus C5's format check:

1. **Token-prefix** — each token's role/chain is encoded in its name (`tC`=target C\*, `dC`=decoy answer, `dB`=decoy bridge, `cX`=depth-2 competitor, etc.).
2. **Ground-truth exact set-membership** — each R6cat token matched against *that item's* actual entity sets in `items_materialized.json`.
3. **Format-variant check (C5)** — each R6cat token tested for case-variant / suffix-match / substring overlap with the item's target tokens, to detect a correct answer mis-scored on a formatting difference.

**Validation:** both classifications reproduce the binding scorer's category counts **exactly** (R1=33 candidates, R2=4, R3=11, R4=2, R5=8, R6cat=38), and methods (1) and (2) agree on the R6cat partition to the item. The partition is therefore the scorer's own logic extended to the *other* bucket, not a heuristic overlay.

## 3. Result (positional)

| Where the 38 R6cat tokens sit | count | share |
|---|---:|---:|
| Decoy-chain **answer** node (`dC`, depth-2, wrong chain) | 33 | 87% |
| Decoy-chain **bridge** node (`dB`, depth-1, wrong chain) | 5 | 13% |
| Novel token (in **no** item set) | 0 | 0% |
| Format-variant of a target token (C5 check) | 0 | 0% |

- **38/38 are on-page entities.** None are hallucinated-from-nowhere; none are noise.
- **0 format-variants.** The "maybe these were right answers in a different shape" alternative is **empirically ruled out** — not argued away. None of the 38 are disguised correct answers.
- **Spread across all five decoy chains** (7 / 15 / 2 / 13 / 1). Concentration in one chain would indicate a position/ordering artifact; the spread is consistent with a genuine chain-level effect, not a single sticky slot.

**Claim-safe statement (the only one the tokens license):** *33 of 96 composite responses sat at decoy-chain depth-2 answer positions, and 5 at decoy-chain bridge positions; all 38 off-map tokens are on-page entities, none format-variants of the target.* The diagnosis sharpens from the pre-registration's generic "missing-fact" to **"the off-map mass is structured, sitting at decoy depth-2 answer positions, on the chain-anchor axis."**

## 4. What this does NOT establish (load-bearing, per C5-F1)

A response token equal to a decoy chain's answer-C node is consistent with **two mechanisms the token alone cannot separate**:

- (a) the model **traversed** decoy-r1 → decoy-r2 from the decoy head (genuine wrong-chain composition), **or**
- (b) the model **grabbed** that node by terminal / depth / recency — the routes we excluded **for the target C\*, and never for the decoy-C nodes.**

The control battery (hop1, hop2, direct-query) was applied **only to the target chain**; verified from the bytes — every query anchor is a target token (`tA`/`tB`), and **no decoy chain was ever independently queried.** So a decoy-C token match carries **none** of the per-item validation that gates target R1 — it is a raw token match, exactly the un-controlled inference the construct exists to prevent, pointed at a decoy instead of the target. Moreover, because the decoys were never queried, **this run structurally cannot separate (a) from (b)** — there is no decoy-chain hop signal to test against.

Therefore: **"the model composed / traversed two hops on a wrong chain" is hypothesis, not measurement**, and is not asserted here. What is measured is *where the tokens sit* (decoy depth-2 positions), not *what computation produced them*. The decoy-traversal reading is a strong **next-hypothesis**, testable only by applying the same control battery to the decoy chains in a future pre-registration.

No selectivity ratio (e.g., "right-chain vs wrong-chain %") is stated, per C5-F2: any such ratio would treat the 33 decoy-C tokens as confirmed traversals, inheriting the unvalidated premise. If ever stated, it is conditional on the 33 being traversals, which is not established.

## 5. What the built controls do establish (sound, positional)

The construction's engineered exclusions **held** under live test: **R4b = 0/96** (the same-depth / disjoint-relation competitor design working as designed — depth-selection did not draw), **direct-query 100% pass** (the A→C\* recall route empirically closed), **no constant-token** (no flat-heuristic answering). So whatever the 33 decoy-C tokens are, they are **not** the four confound routes controlled for on the target. That genuinely narrows the space. The leak is on the **one axis the decoys deliberately left structurally identical to the target** — they share r1/r2 and are distinguishable only by head (chain-anchor). The diagnosis "the failure is on chain-anchor disambiguation, not on the controlled confounds" is sound at the positional level.

## 6. Corroborating load context

Single-fact retrieval was already unreliable under the same clutter: hop1 control pass-rate **0.740**, hop2 **0.677** — about a third of "B maps to ?" lookups missed under 30 facts of clutter, *before composition is attempted*. This is complementary to §3–§5: at this load the model's responses are structured (decoy depth-2 positions) yet component retrieval is degraded. Both are **per-construction-at-this-load** observations, not capability claims; whether the driver is the clutter count (k=5), the relation labeling, or the prompt format is what a load-varying follow-up would isolate.

Layout-position diagnostic (secondary): the position-4 quintile showed R1-validated 0/17 against ~0.30 for positions 1–2. Underpowered (n=17) and confounded with whatever co-varies with that quintile; a hypothesis for a *controlled* position design, not a finding here.

## 7. What this informs (next-design inputs — not actions, not authorized)

- A **chain-anchor-disambiguation control**: apply the hop1/hop2/direct-query battery to the **decoy** chains so decoy-C grabs receive the same validation target-C does — the only way to separate §4's (a) from (b). New pre-registration; Senior + Manager call.
- A candidate **named category** for a future definition v0.5: "decoy-chain answer-grab (right depth, wrong chain)," so this mode is scored rather than absorbed into *other*. Definition change for a future run, never a retrofit to this one.
- **Load-varying** (vary k, or chain distinguishability) to find where chain-anchor binding holds.
- A **controlled** C\*-position design (position as a locked factor with adequate per-cell n) to test the position-4 signal.

## 8. Scope and boundaries

- **The FAIL stands.** This note re-scores nothing and moves no R1, threshold, or outcome.
- **Not a capability claim.** "Qwen2.5-3B can/can't do two-hop" is out of bounds and unsupported; all observations are per-construction-at-this-load instrument diagnostics.
- **Mechanism out of bounds.** Where the tokens sit is verified; why the model bound to a decoy chain is not claimed.
- **n=1.** Nothing here touches substrate-infeasibility (§14 / def v0.4 §8.5 require repeated admissible failure).
- **Authorizes nothing.** No re-run, no new pre-registration, no compression, no Claim C, no Paper B follows from this note. A re-run requires a new locked pre-registration and may never loosen R8 / R6(c) / threshold.
- **Not of-record.** Post-hoc description, not a locked result; descriptive diagnostic only.

*Credits: CS Engineer (identified `items_materialized.json` as the ground-truth source; independent recomputation of all outcome quantities). Contributor 5 (F1 positional-vs-traversal containment; F2 selectivity-ratio containment; format-variant check). Both corrections are built into the claims above.*

*Status: descriptive diagnostic note v0.1, read-only, non-verdict-changing. Positional claims only; decoy-traversal labeled next-hypothesis. Certifies nothing; authorizes nothing.*
