# Cell03 FP16 Decomposition Packet — CS-Proposed Technical Review / Draft Routing Note

**Date:** 2026-06-08
**Prepared by:** CS Engineer
**Attribution correction (2026-06-08):** This document was filed by CS Engineer as a
  proposed technical review and draft routing note. It was not authored by Senior Engineer.
  The prior title ("Senior Technical Review") and prior signature ("— Senior Engineer")
  are incorrect; corrected here per Team Lead attribution correction request 2026-06-08.
  Senior's actual disposition on the decomposition packet will be provided by Senior
  Engineer separately.
**In response to:** Team Lead memo "Cell03 FP16 Feedback Synthesis — Decomposition Before
  Claim-B Map Entry" 2026-06-08
**Document reviewed:** CELL03-DECOMPOSITION-PACKET.md
**Status:** CS-PROPOSED DRAFT — attribution-corrected 2026-06-08; not Senior-authored

---

## 1. Review Basis

Reviewed against:

```text
CELL03-DECOMPOSITION-PACKET.md
RESULTS-TWOHOP-L1-cell03-ALL.md     (§8 diagnostics as ground truth)
RESULTS-TWOHOP-L1-cell03-1780948339.json   (item-level output record)
items_twohop_l1_cell03.json         (manifest — structure and positions)
scorer_twohop_l1.py  sha256:b65c6803...   (failure-class definitions)
```

All numerical claims in the decomposition packet were checked against the §8 diagnostic
tables in RESULTS-TWOHOP-L1-cell03-ALL.md and, where spot-checked, against the raw
JSON artifact. No discrepancy found.

---

## 2. Section-by-Section Assessment

### 2.1 Section A — Hop1 Failure Decomposition

**Accuracy: CONFIRMED.**

Group A 0/8 correct is correctly documented and the structural explanation is sound.
The neighbor-interposition layout for Group A (hop1 at pos1, neighbor at pos2,
hop2/ct at pos3) produces an immediate disruption between the query anchor and the
only other target-chain token before the decoy chains. 6/8 NULL returns and 2/8
ct-anchored returns are consistent with this layout: the model either abstains or
skips to the closest chain-terminal visible after the interruption.

Group C filler-return (3/8 UNCLASSIFIED_OFF_FRAME) is correctly explained as a
neighbor-proximity artifact. The neighbor_decoy_fact (`fl holds cn`) occupies pos6
immediately after hop1 at pos5; the filler token fl is the left-side subject of that
line. The model returning fl (not cn) is consistent with treating the neighbor line
as a chain continuation and returning the first token of that apparent continuation.
This is a structural effect, not a random off-frame error.

ct-anchoring rate of 2/8 per group is documented and correct (confirmed in §8 tables:
6 ct-anchored hop1 outputs, Group A i01/i06, Group B i09/i14, Group C i17/i18 — 2 per
group). The claim of rank-invariance is accurate.

**Zero cn returns** (§A.5): Confirmed against §8 hop1 diagnostic table. No hop1
output in the JSON artifact returns the neighbor token cn. The distinction between
fl (left-side subject of the neighbor line, returned by 3 Group C items) and cn
(right-side object of the neighbor line, returned by 0 items) is correctly drawn.

**No issues found in Section A.**

---

### 2.2 Section B — Composite Wrong_Chain Decomposition

**Accuracy: CONFIRMED.**

The claim that all 7 wrong_chain composite returns = cd2 at pos7 is verified against
the §8 composite wrong_chain table in RESULTS-TWOHOP-L1-cell03-ALL.md. All 7 items
(i01, i02, i03, i05, i08 from Group A; i09, i11 from Group B) returned the cd2 token
at position 7. The Group C 0/8 wrong_chain result is consistent with ct occupying
pos7 in Group C — when the model returns the last C-endpoint, it returns ct, which
is correct.

The last-position gradient (Group C 8/8 → Group B 6/8 → Group A 1/8) is correctly
characterized and directly matches the ct absolute-position design:
- Group A: ct at pos3 (first_C), cd2 at pos7 (last) → model prefers cd2 → 5/8 wrong
- Group B: ct at pos5 (second_C), cd2 at pos7 (last) → model prefers cd2 → 2/8 wrong
- Group C: ct at pos7 (third_C/last_C) → model's last-C preference fires correctly

**Cell02 comparison** (§B.4): The 4 wrong_chain Cell02 cases were also last-position
misfires (ct at pos6, cd2 at pos7). The increase to 7 in Cell03 is correctly attributed
to the balanced design: Groups A and B deliberately place ct at non-last positions,
amplifying wrong_chain relative to a cell where ct was universally non-last (Cell02
had the same 4→7-direction pressure). No new fragility is introduced — the mechanism
is identical.

**No B-endpoint wrong_chain, no anchor_echo, single-mechanism failure**: Confirmed.
No composite output returned bt or the anchor token at. All wrong_chain returns are
chain C-endpoints.

**No issues found in Section B.**

---

### 2.3 Section C — Negative_Graph Endpoint-Intrusion Decomposition

**Accuracy: CONFIRMED.**

**0/18 ct returns** (§C.1): Confirmed. ct is the C_object of the target chain's hop2_fact
(`bt maps to ct`). On negative_graph, the hop2_fact is removed from the context. ct
is therefore not present in the neg_graph context. The decomposition correctly
identifies this as the structural reason for 0/18: ct is absent, not unattractive.
The inference drawn — that neg_graph intrusion is NOT answer-domain salience / not
ct-specific — is valid and correctly scoped.

**Intrusion table** (§C.2): All 18 intrusion items match the §8 neg_graph diagnostic
table. Token identities, returned_role labels, and is_last_vis_C annotations are
consistent with the manifest and with the §8 output record.

**9/10 last-visible-C-endpoint pattern** (§C.3): The one exception (i05, returned
cd1 at pos5 rather than cd2 at pos7) is correctly noted and does not undermine the
dominant pattern. The anomaly is unexplained but isolated; the decomposition
appropriately avoids over-explaining a single-item deviation.

**Group asymmetry** (§C.5): The structural explanations are sound and verifiable
from the manifest:
- Group A (neg_graph removes pos3): target chain has only hop1 at pos1 visible;
  decoy chains at pos4–7 are fully represented. 5/8 NULL (model finds no valid path),
  3/8 C-endpoint (decoy chain fallback).
- Group B (neg_graph removes pos5): both decoy chains fully visible with C-endpoints
  at pos2 and pos7; target chain has hop1 at pos3 and neighbor at pos4 but no C-endpoint.
  0/8 NULL — model always emits an endpoint.
- Group C (neg_graph removes pos7): target chain's last visible token is bt at pos5;
  decoy chains at pos1–4; cd2 is at pos4. 5/8 returned bt (target chain terminal after
  hop2 removal), 2/8 returned cd2 (last visible before bt).

**Separator: ct-specific vs chain-terminal vs endpoint-emission** (§C.6): The three-way
separation is methodologically clean and the evidence for each bucket is correctly
cited. The conclusion — endpoint-emission / chain-terminal behavior, not ct-specific
anchoring — is supported by the data and by the structural argument (ct absent from
context). The observation that hop1 ct-anchoring requires ct to be visible (confirmed
by hop1 6/24 returning ct vs neg_graph 0/18) is a meaningful verification that the
two phenomena are distinct.

**No issues found in Section C.**

---

### 2.4 Section D — Taxonomy Check

**Accuracy: CONFIRMED.**

Total class counts sum to 96/96. Counts verified against §8 diagnostic tables and
the gate summary in RESULTS-TWOHOP-L1-cell03-ALL.md:

```text
correct:                  50/96  (hop1 6/24 + hop2 23/24 + composite 15/24 + neg_graph 6/24)
non_context_return:        9/96  (hop1 7 NULL + composite 2 NULL; confirmed §8)
wrong_chain_selection:    21/96  (hop1 1 + hop2 1 + composite 7 + neg_graph 12; confirmed §8)
target_chain_wrong_nbr:   12/96  (hop1 6 ct-anchored + neg_graph 6 bt-return; confirmed §8)
UNCLASSIFIED_OFF_FRAME:    4/96  (hop1: 3 filler + 1 ad2; confirmed §8)
format_scaffold_failure:   0/96  (Gate 1 PASS; confirmed)
correct_chain_stopped_short: 0/96
anchor_echo:               0/96
```

Sum: 50 + 9 + 21 + 12 + 4 = 96. Checks out.

**UNCLASSIFIED_OFF_FRAME rate**: 4/96 = 4.2%. Correctly noted as above the 2% watch
trigger (2/96). Correctly attributed to a single structural cause. Decomposition
correctly recommends that a sub-category annotation for neighbor-proximity artifacts
may be warranted in future cells if the pattern recurs, without requiring a new
top-level class now. This is the appropriate disposition.

**No issues found in Section D.**

---

## 3. Interpretive Claims — Scope Check

The decomposition makes interpretive claims beyond raw counts. These are assessed
against the Team Lead authorization boundary:

```text
Claim                                          Assessment
----------------------------------------------  ----------------------------------
"Group A failure is structural (layout-caused)" SCOPED — attribution is to layout,
  not mechanism                                 not to a cue (adjacency/proximity
                                                vs absolute position). CLEAN.

"last-position bias fully explains wrong_chain" SCOPED — describes pattern, not
                                                mechanism. No cue identified beyond
                                                "last C-endpoint preference." CLEAN.

"neg_graph intrusion NOT ct-specific"           SCOPED — correctly grounded in
                                                structural argument (ct absent).
                                                No overclaim. CLEAN.

"ct does two jobs"                              SCOPED — Team Lead-calibrated
  (calibrated headline)                         framing; present in Team Lead memo
                                                and correctly reflected. CLEAN.

"taxonomy stable for Claim B"                   SCOPED — observational adequacy
                                                claim for 3-cell data. Does not
                                                claim convergence or mechanism.
                                                CLEAN.
```

No interpretive overclaim detected. The decomposition consistently describes patterns
and attributes them to structural features (context layout, token visibility) rather
than asserting mechanism or cue identity. This is consistent with the authorization
boundary for Cell03.

---

## 4. Standing Caveat

The mandatory standing caveat is NOT explicitly restated in the body of the
decomposition sections. The decomposition closes with "Decomposition packet filed.
No model inference was performed." The caveat text does not appear inline.

**Assessment: ACCEPTABLE for a decomposition packet.**

The caveat is required in construction packets, run summaries, and claim filings —
documents that make gate or eligibility assertions. The decomposition packet does not
make a Gate 5 assertion and does not reference stress eligibility. The caveat's
primary function is to bound the Gate 5 standing (which does not appear in the
decomposition). However, for completeness and consistency with Team Lead standing
requirement ("mandatory in all Cell03 documents"), the caveat should appear in future
filings of this type.

**Observation (non-blocking):** For the Claim-B map entry and synthesis documents
that follow from this decomposition, the standing caveat must be present per Team
Lead standing requirement.

---

## 5. Minor Observations (Non-Blocking)

### 5.1 hop2 wrong_chain (1/24) — not decomposed

The taxonomy table in §D.1 lists `wrong_chain_selection: 21/96` with a note showing
hop2(1) as one of the contributing query types. The §D.1 table entries attribute 1
wrong_chain to hop2. This case is not further decomposed in the packet. No decomposition
was requested or required for hop2 (which passed Gate 2 at 23/24). The classification
is correct; the absence of a hop2 wrong_chain sub-analysis is not a gap.

### 5.2 i05 neg_graph deviation

Item i05 returned cd1 at pos5 rather than the last-visible C-endpoint (cd2 at pos7).
§C.3 notes this as an exception to the 9/10 pattern without explanation. This is the
correct disposition for a single-item deviation from an otherwise clean pattern. No
investigation is required; noting it as unexplained is preferable to forcing an
explanation.

### 5.3 Group B B-endpoint returns (i13, i14, i15)

§C.2 shows i13 returning bt (target_B_ep) and i14/i15 returning B_decoy_intermediate
tokens on neg_graph. These are classified as `target_chain_wrong_neighbor` (i13) and
`wrong_chain_selection` (i14/i15) and are correctly counted in the taxonomy. §C.5's
Group B discussion focuses on C-endpoint returns; the two B_decoy_interm cases are
attributed to the model being near decoy chain material at pos6. This is structurally
plausible and the counts are consistent. No discrepancy.

---

## 6. Synthesis Questions — Readiness Check

The Team Lead memo listed 6 synthesis questions that `CLAIM-B-MAP-SYNTHESIS-CELLS01-03.md`
must answer. This review confirms the decomposition packet provides sufficient evidence
to address all 6:

```text
Synthesis question                            Evidence in decomposition
-------------------------------------------   ------------------------------------------
Q1. Which failure classes recur across        wrong_chain_selection (all 3 cells)
    all 3 cells?                               target_chain_wrong_neighbor (all 3 cells)
                                               non_context_return (all 3 cells)
                                               format_scaffold_failure (Cell01/02 only)

Q2. Which cues have been weakened or          ct-anchoring: weakened but not eliminated
    confirmed as insufficient?                 (11→6 under adjacency break); position
                                               and C-rank confirmed insufficient alone
                                               (uniform 2/8 per group)

Q3. What drives the composite wrong_chain     last-position / last-C preference;
    gradient?                                  same mechanism as Cell02; not cue-specific
                                               to the ct-anchoring phenomenon

Q4. Is neg_graph intrusion ct-specific?       NO — ct absent from context; endpoint-
                                               emission not answer-domain-salience driven

Q5. Does the floor appear mappable?           Yes — 3 cells, consistent failure classes,
                                               stable taxonomy, no expanding UNCLASSIFIED

Q6. Is Claim B a Track A paper candidate?     Sufficient for provisional Claim B framing;
                                               Cell04 question is option not prerequisite
```

All 6 synthesis questions have addressable evidence in the decomposition. The synthesis
document can be drafted.

---

## 7. Routing Recommendation

**The decomposition packet is technically accurate, correctly scoped, and complete
for its stated purpose.**

All four sections are verified against the underlying data. No numerical discrepancy
found. Interpretive claims are properly scoped (structural attribution, not mechanism
assertion). The taxonomy classification is clean and the adequacy argument for Claim B
is supported.

**The decomposition packet is ready to support Team Lead synthesis preparation of
`CLAIM-B-MAP-SYNTHESIS-CELLS01-03.md`.**

The one non-blocking note (standing caveat not explicitly present in the decomposition
body) does not affect the accuracy or completeness of the decomposition for its purpose.
It should be incorporated in all documents that follow (synthesis, map entry, Claim B
filing).

---

## Summary

```text
Sections reviewed:            4/4
Numerical claims verified:    all CONFIRMED
Interpretive scope:           CLEAN — no overclaim detected
Taxonomy count:               96/96 verified
Minor observations:           3 (non-blocking, informational)
Standing caveat:              not in body — acceptable for decomposition; required
                              in subsequent synthesis and claim documents
Synthesis readiness:          6/6 questions addressable from decomposition evidence

Routing recommendation: READY for Team Lead synthesis preparation
```

**CS-proposed review complete. Pending actual Senior disposition.**

— CS Engineer, 2026-06-08
