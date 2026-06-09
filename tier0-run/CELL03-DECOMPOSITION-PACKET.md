# Cell03 FP16 Decomposition Packet

**Date:** 2026-06-08
**Prepared by:** CS Engineer
**Per:** Team Lead memo "Cell03 FP16 Feedback Synthesis — Decomposition Before Claim-B Map Entry"
**Status:** FILED — for Team Lead synthesis preparation

---

## A. Hop1 Failure Decomposition

### A.1 Raw tokens — 4 UNCLASSIFIED cases

```text
item_id               group   returned_token   role                    token_type
twohop_l1_c03_i10     B       ZGUPE            other_context           A_decoy_2 (ad2 for i10)
twohop_l1_c03_i17     C       ZFWWT            inert_filler            filler (fl for i17)
twohop_l1_c03_i21     C       ZFXFK            inert_filler            filler (fl for i21)
twohop_l1_c03_i22     C       ZFAHA            inert_filler            filler (fl for i22)
```

None of the 4 UNCLASSIFIED tokens is a neighbor (cn) return. The filler tokens
(ZFWWT, ZFXFK, ZFAHA) are the left-side subjects of the neighbor_decoy_fact line
(`fl holds cn`) at pos6 in Group C. The model returned the filler (fl) rather than
any chain token. ZGUPE for i10 is the A_object of decoy_chain_2 (ad2, ROLE_OTHER_CONTEXT).

### A.2 Group split — all 18 hop1 failures

```text
Group   correct   NULL(non_ctx)   ct-anchored(wrong_nbr)   UNCLASSIFIED   wrong_chain   total_fail
A       0/8       6               2                         0              0             8
B       4/8       0               2                         1              1             4
C       2/8       1               2                         3              0             6

total   6/24      7               6                         4              1             18
```

**Group A: 0/8 correct on hop1 — complete failure.**
Every Group A item failed hop1: 6 NULL returns plus 2 ct-anchored returns. No Group A item
returned bt correctly.

**Group B: 4/8 correct.** The 4 failures split across ct-anchored (2), UNCLASSIFIED (1),
wrong_chain (1).

**Group C: 2/8 correct.** The 6 failures split across UNCLASSIFIED (3), ct-anchored (2),
NULL (1).

### A.3 NULL group split

```text
All 7 NULL returns:
  twohop_l1_c03_i02   Group A
  twohop_l1_c03_i03   Group A
  twohop_l1_c03_i04   Group A
  twohop_l1_c03_i05   Group A
  twohop_l1_c03_i07   Group A
  twohop_l1_c03_i08   Group A
  twohop_l1_c03_i18   Group C

6/7 NULL returns are from Group A. 1/7 from Group C. 0 from Group B.
```

### A.4 Does NULL / UNCLASSIFIED correlate with the interposed-neighbor design?

**NULL and Group A layout:**

In Group A, the context opens with:
```text
pos 1: target_chain  hop1_fact      (at links to bt)      ← hop1 anchor and expected answer
pos 2: neighbor_ctx  neighbor_fact  (fl holds cn)         ← interposed immediately after
pos 3: target_chain  hop2_fact      (bt maps to ct)       ← ct here
pos 4-7: decoy chains
```

The model sees: query anchor, immediately followed by the neighbor interruption, then
ct at pos3. With no prior context to ground the query, Group A items have the neighbor
fact interposed between the anchor and the only other target-chain token visible
before the decoy chains begin. 6/8 Group A items returned NULL rather than following
hop1 to bt.

**UNCLASSIFIED and Group C layout:**

In Group C, the hop1 query context is:
```text
pos 1-4: decoy chains (fully represented)
pos 5: target_chain  hop1_fact      (at links to bt)
pos 6: neighbor_ctx  neighbor_fact  (fl holds cn)         ← interposed after hop1
pos 7: target_chain  hop2_fact      (bt maps to ct)
```

3/4 UNCLASSIFIED items are from Group C and returned the filler token (fl), the
left-side subject of the neighbor_decoy_fact line at pos6. With hop1 at pos5 and
the neighbor at pos6 immediately following, the model may be treating the neighbor
fact as a continuation of the chain and returning the first token of that line (fl).

This is a neighbor-proximity artifact. The filler token appears immediately after hop1,
in the same position slot that bt would occupy if the chain continued normally.

**UNCLASSIFIED in Group B:**

i10 returned ZGUPE = ad2 (ROLE_OTHER_CONTEXT, A_object of decoy_chain_2). This is
the anchor token for decoy_chain_2 at pos6. The Group B context has the target chain
at pos3-5 and decoy_chain_2 at pos6-7. The model may have followed from hop1 anchor
into decoy_chain_2's A-object rather than following the target chain. An isolated case.

### A.5 Did any hop1 failure return the interposed neighbor cn?

**No.** Zero hop1 failures returned the neighbor (cn) token.

The neighbor token is on the right side of the neighbor_decoy_fact (`fl holds cn`).
The 3 Group C UNCLASSIFIED returns retrieved the filler (fl, the left side), not cn.
No item mistook the neighbor for the hop1 answer.

### A.6 Summary

```text
Group A hop1 is catastrophically disrupted by the interposed-neighbor design.
  The neighbor appears immediately after hop1 in Group A (pos1: hop1, pos2: neighbor).
  6/8 Group A items returned NULL — the model cannot navigate to bt with this layout.
  The 2 ct-anchored Group A items still skipped to pos3 (hop2 endpoint).
  0/8 correct.

Group C produces neighbor-proximity artifacts.
  3/8 Group C items returned the filler token (left side of the neighbor line at pos6).
  The neighbor line immediately follows hop1 in Group C (pos5: hop1, pos6: neighbor).
  Model treats the neighbor fact as a chain continuation and returns fl.

ct-anchoring is layout-independent: 2/8 per group regardless of where the neighbor falls.

No item returned cn (the neighbor token itself).
```

---

## B. Composite Wrong_Chain Decomposition

### B.1 Full wrong_chain record

```text
item_id               group   ct_rank      returned   chain   ret_pos   ct_pos   cd2_pos
twohop_l1_c03_i01     A       first_C      LRPTZ      cd2     7         3        7
twohop_l1_c03_i02     A       first_C      EFSCG      cd2     7         3        7
twohop_l1_c03_i03     A       first_C      YNVBT      cd2     7         3        7
twohop_l1_c03_i05     A       first_C      VOTRJ      cd2     7         3        7
twohop_l1_c03_i08     A       first_C      LDFVJ      cd2     7         3        7
twohop_l1_c03_i09     B       second_C     LLIXH      cd2     7         5        7
twohop_l1_c03_i11     B       second_C     HXPVQ      cd2     7         5        7
```

**All 7 wrong_chain returns: decoy_chain_2 C-endpoint (cd2), all at context position 7.**

cd2 is at context position 7 in Groups A and B (decoy_chain_2 hop2_fact is the last
fact in the context for both groups). In Group C, cd2 is at position 4 — not last.

### B.2 Group split

```text
Group   correct   wrong_chain   non_context   wrong_chain token
A       1/8       5/8           2/8           all cd2 (pos 7)
B       6/8       2/8           0/8           all cd2 (pos 7)
C       8/8       0/8           0/8           — no failures
```

### B.3 Composite wrong_chain is a last-position bias, not a chain-identity bias

**All 7 wrong_chain returns retrieved cd2 at context position 7.**

In Groups A and B, cd2 is the last C-endpoint in the context (pos7 = last fact).
In Group C, cd2 is at pos4 and ct is at pos7 (last) — the model returns ct, which
is correct. When the model returns the last C-endpoint, it is correct in Group C
and wrong in Groups A and B.

The composite gradient is direct:

```text
Group A (ct at pos 3, first_C):   composite correct 1/8   ← ct is far from last; cd2 at last
Group B (ct at pos 5, second_C):  composite correct 6/8   ← ct is closer to last; cd2 at last
Group C (ct at pos 7, third_C):   composite correct 8/8   ← ct IS last; cd2 not last
```

This is a last-position / last-C preference on composite. When ct is last, this preference
is correct. When ct is not last, it fires wrong (cd2 is last and is returned instead).

### B.4 Relation to Cell02 composite

Cell02: wrong_chain = 4/24 (all items had ct at pos6, cd2 at pos7).
Cell03: wrong_chain = 7/24 (Groups A/B have ct not at last; Group C has ct at last).

The Cell02 wrong_chain cases were also last-position misfires: the model preferred cd2
(pos7) over ct (pos6). In Cell03 Groups A and B, the gap between ct and last position is
larger, producing more misfires. In Group C, the same preference fires correctly.

The increase in wrong_chain (4 → 7) is explained entirely by the Cell03 balanced design
putting ct at non-last positions for 16 items (Groups A and B), where the last-position
preference fires wrong. It is not new chain-selection fragility — it is the same last-C
bias operating against a more adversarial position layout.

### B.5 Summary

```text
ALL composite wrong_chain returns: cd2 at position 7 (last context position).
Composite accuracy follows a last-position gradient:
  ct at pos 7 (Group C): 8/8 correct
  ct at pos 5 (Group B): 6/8 correct
  ct at pos 3 (Group A): 1/8 correct

wrong_chain increase (4 → 7) is explained by last-position bias operating against
non-last ct positions in Groups A and B.

No wrong_chain from Group C. No B-endpoint wrong_chain. No anchor_echo.
Composite wrong_chain is a single-mechanism failure: last-C preference.
```

---

## C. Negative_Graph Endpoint-Intrusion Decomposition

### C.1 Is the intrusion ct-specific?

**No. Zero intrusions returned ct.**

On negative_graph, the hop2_fact is removed from context. For all groups, ct is
contained in the hop2_fact (the fact `bt maps to ct`). When that fact is removed,
ct is no longer present in the rendered context. No item returned ct on neg_graph
because ct was not visible.

The neg_graph intrusion pattern is NOT answer-domain salience (ct-specific).
It is a general endpoint-emission tendency: the model returns whatever endpoint
is available in the truncated context.

### C.2 Full intrusion breakdown

```text
item_id               group   returned   intr_type           tok_pos   last_vis_C_pos   is_last_vis_C
twohop_l1_c03_i02     A       EFSCG      cd2_C_ep            7         7                True
twohop_l1_c03_i05     A       ZTPUT      cd1_C_ep            5         7                False
twohop_l1_c03_i08     A       LDFVJ      cd2_C_ep            7         7                True
twohop_l1_c03_i09     B       LLIXH      cd2_C_ep            7         7                True
twohop_l1_c03_i10     B       RPHBK      cd2_C_ep            7         7                True
twohop_l1_c03_i11     B       HXPVQ      cd2_C_ep            7         7                True
twohop_l1_c03_i12     B       CZFUR      cd2_C_ep            7         7                True
twohop_l1_c03_i13     B       ZBMXF      target_B_ep (bt)    3         7                —
twohop_l1_c03_i14     B       ZHAEI      B_decoy_interm      6         7                —
twohop_l1_c03_i15     B       ZHQBK      B_decoy_interm      6         7                —
twohop_l1_c03_i16     B       CLZMW      cd2_C_ep            7         7                True
twohop_l1_c03_i17     C       YJKBM      cd2_C_ep            4         4                True
twohop_l1_c03_i19     C       ZBZCI      target_B_ep (bt)    5         4                —
twohop_l1_c03_i20     C       ZBPQV      target_B_ep (bt)    5         4                —
twohop_l1_c03_i21     C       ZBCOG      target_B_ep (bt)    5         4                —
twohop_l1_c03_i22     C       MDUJI      cd2_C_ep            4         4                True
twohop_l1_c03_i23     C       ZBFYY      target_B_ep (bt)    5         4                —
twohop_l1_c03_i24     C       ZBXRT      target_B_ep (bt)    5         4                —
```

### C.3 Intrusion type summary

```text
decoy_C_endpoint (cd1 or cd2):   10/18
target_B_endpoint (bt, hop1_B):   6/18
B_decoy_intermediate:             2/18

ct returns:                       0/18
```

Of the 10 decoy_C_endpoint intrusions: **9/10 returned the last visible C-endpoint
in the neg_graph context.** The exception (i05) returned cd1 at pos5 rather than
cd2 at pos7 — one item deviating from the last-visible-C pattern.

### C.4 Group breakdown

```text
Group   correct_NULL   intrusion   C_endpoint   target_B   B_decoy_interm
A       5/8            3/8         3            0          0
B       0/8            8/8         5            1          2
C       1/8            7/8         2            5          0
```

### C.5 What drives the group asymmetry?

**Group A (best: 5/8 correct NULL)**

After removing hop2(pos3), Group A context is: pos1(target_hop1), pos2(neighbor),
pos4(d1h1), pos5(d1h2/cd1), pos6(d2h1), pos7(d2h2/cd2).

The target chain has one visible fact (hop1 at pos1), appearing early before the
decoy chains. 5/8 items returned NULL — the model recognized no valid A→C path.
3/8 items returned decoy C endpoints (2 at cd2/pos7, 1 at cd1/pos5).

**Group B (worst: 0/8 correct NULL)**

After removing hop2(pos5), Group B context is: pos1(d1h1), pos2(d1h2/cd1),
pos3(target_hop1), pos4(neighbor), pos6(d2h1), pos7(d2h2/cd2).

Both decoy chains are fully represented with visible C-endpoints. The model returns
an endpoint every time: 5 cd2(pos7), 1 bt(pos3 target B), 2 B_decoy_interm(pos6).
No NULL returns.

**Group C (7/8 intrusion: 5 B_target + 2 C_decoy)**

After removing hop2(pos7), Group C context is: pos1(d1h1), pos2(d1h2/cd1),
pos3(d2h1), pos4(d2h2/cd2), pos5(target_hop1), pos6(neighbor).

The target chain's last visible token is bt (at pos5) — the hop2 fact containing ct
is removed, so the target chain terminates at bt. 5/8 Group C items returned bt
(target_B_endpoint). The model followed the target hop1 link and stopped at bt.

In Group C, the last visible C-endpoint is cd2 at pos4. 2/8 items returned cd2(pos4)
instead of the B_target pattern.

The shift from C-endpoint intrusion (Groups A/B) to B-endpoint intrusion (Group C)
is explained by the context structure after hop2 removal:
- Groups A/B: decoy C-endpoints remain visible and are returned
- Group C: decoy C-endpoints are earlier in context (pos4); target bt is at pos5,
  immediately after decoy chain material — model follows hop1 to bt rather than
  looking back to pos4

### C.6 Separator: ct-specific vs chain-terminal vs endpoint-emission

```text
ct-specific (answer-domain salience):
  0/18 intrusions returned ct — ct is absent from context.
  RULED OUT as the mechanism for neg_graph intrusion.

chain-terminal / endpoint-emission:
  10/18 returned a decoy C-endpoint, 9/10 of which was the last visible C-endpoint.
  6/18 returned the target chain's B-terminal (bt) when hop2 was removed.
  SUPPORTED: the model fills in a terminal token regardless of which chain owns it.

Ct-anchoring on hop1 (from Section A) is a SEPARATE phenomenon:
  On hop1 (where ct IS in context), 6/24 returned ct.
  On neg_graph (where ct is ABSENT from context), 0/18 returned ct.
  This confirms hop1 ct-anchoring requires ct to be present and visible.
  It is not driven by abstract answer-domain salience decoupled from token visibility.
```

---

## D. Top-Level Taxonomy Check

### D.1 Do all Cell03 failures fit existing top-level classes?

**Yes.**

```text
Failure class             Cell03 count   Coverage
correct                   50/96          —
format_scaffold_failure   0/96           —
non_context_return        9/96           all NULL returns on hop1; 2 NULL on composite
correct_chain_stopped_short 0/96         —
wrong_chain_selection     21/96          hop1(1), hop2(1), composite(7), neg_graph(12)
target_chain_wrong_neighbor 12/96        hop1(6), neg_graph(6)
anchor_echo               0/96           —
UNCLASSIFIED_OFF_FRAME    4/96           hop1 only: 3 filler returns + 1 A_decoy_2 return
total                     96/96
```

All 96 outputs are classified. No output falls outside the taxonomy.

### D.2 Is a new top-level failure class needed?

**No.**

The 4 UNCLASSIFIED cases (hop1 only) are correctly classified under the existing
UNCLASSIFIED_OFF_FRAME class. They represent in-context tokens with roles
(ROLE_INERT_FILLER, ROLE_OTHER_CONTEXT) that are not addressed by the 8
classification rules by design — these roles are not chain endpoints, anchors, or
NULL tokens. The UNCLASSIFIED class is the correct home.

The filler-return behavior (model returns fl from the neighbor_decoy_fact line on hop1)
is a neighbor-proximity artifact. It is a noteworthy interaction effect but does not
require a new class. The returned tokens are in-context and classifiable structurally.

3/4 UNCLASSIFIED cases are from Group C (where the neighbor is immediately adjacent
to hop1 at pos5/pos6). If Group C neighbor-proximity artifacts recur in future cells,
a sub-category annotation may be warranted as a §8 diagnostic extension — but the
top-level taxonomy is adequate.

### D.3 Taxonomy adequacy assessment for Claim B

```text
All three cells (01–03) produce outputs classifiable by the existing 8-class taxonomy.
UNCLASSIFIED rate across cells:
  Cell01: 0/96
  Cell02: 0/96
  Cell03: 4/96 (4.2%, all hop1)

Cell03 UNCLASSIFIED rate is within the Gate 4a watch trigger (> 2% = 2/96).
All 4 cases are attributable to a single structural cause (neighbor-adjacent filler return).

Conclusion: the failure taxonomy is not expanding. The Claim B constructibility floor
is mapping onto a stable, classifiable failure landscape.
```

---

## Summary

```text
A. Hop1 failure:
   Group A total failure (0/8 correct): interposed neighbor after hop1 at pos1
   causes abstention (6 NULL) + ct-anchoring (2); filler-return artifacts in Group C (3)
   linked to neighbor immediately after hop1 at pos5; no item returned the cn token itself

B. Composite wrong_chain:
   All 7 returns: cd2 at position 7 (last context position)
   Last-position / last-C bias drives composite; gradient matches ct_abs_position:
   Group C (ct=last): 8/8; Group B (ct=middle): 6/8; Group A (ct=first): 1/8
   wrong_chain increase (4→7) fully explained by balanced design — not new fragility

C. Negative_graph intrusion:
   0/18 intrusions returned ct (ct is absent from neg_graph context)
   10/18 returned last-visible decoy C-endpoint (chain-terminal emission)
   6/18 returned target B-endpoint (bt) when hop2 removed and B was terminal
   Not ct-specific; not answer-domain-salience driven;
   pure endpoint-emission / last-visible-terminal behavior

D. Taxonomy:
   All 96 outputs classified by existing taxonomy; no new class needed
   UNCLASSIFIED_OFF_FRAME (4) is architecturally correct, neighbor-proximity attributable
   Failure landscape is stable and mappable for Claim B
```

**Decomposition packet filed. No model inference was performed.**

— CS Engineer, 2026-06-08
