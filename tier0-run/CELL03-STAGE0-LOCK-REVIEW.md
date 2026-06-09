# Cell03 Stage 0 Construction Packet — Senior Engineer Lock Review

**Date:** 2026-06-08
**Prepared by:** Senior Engineer
**In response to:** Team Lead memo "Review Assignment — Cell03 Stage 0 Construction Packet" 2026-06-08
**Status:** REVIEW COMPLETE — disposition to Team Lead

---

## 1. Review Basis

Files reviewed:

```text
CELL03-CONSTRUCTION-PACKET.md
generate_cell03.py
items_twohop_l1_cell03.json
scorer_twohop_l1.py       (hash verification)
```

All hash and score claims were verified against live files by re-running the
scorer and manifest independently, not solely from the packet narrative.

---

## 2. 12-Item Checklist

```text
1. Scorer hash matches sha256:b65c6803...
   STATUS: PASS
   sha256:b65c6803017b8b04ac25d4bd84c5fb5ff61692ed41d609e099b181fa58e4ddde
   — confirmed by live hashlib.sha256() of scorer_twohop_l1.py

2. Manifest hash consistent across packet and log
   STATUS: PASS
   sha256:7d5099cbdccf1f2175e6c693ea851cab73109665d3420be345a475bf835240a1
   — packet §2: present. EXPERIMENT_LOG Key Files row: present.
   — live re-hash of items_twohop_l1_cell03.json: matches.

3. Validation output present and 24/24 PASS
   STATUS: PASS
   Packet §4: 24/24 PASS recorded.
   Live re-run of validate_manifest(items): Total=24 Pass=24 Fail=0.

4. Token audit output present and clean
   STATUS: PASS
   Packet §5: 0 Lev / 0 Trig / 0 BPE violations. 23,220 pairs audited.
   Tokenizer: sha256:c0382117... (FP16 HuggingFace cache — confirmed run tokenizer match).

5. ct C-rank balance is 8/8/8
   STATUS: PASS
   Live re-score of all 24 items (composite query):
     always_return_first_C:  8/24 — Group A (items 1-8, ct at pos 3)
     always_return_second_C: 8/24 — Group B (items 9-16, ct at pos 5)
     always_return_third_C:  8/24 — Group C (items 17-24, ct at pos 7)
   Balance confirmed 8/8/8.

6. ct absolute-position balance is 8/8/8
   STATUS: PASS
   All 24 manifest cue_balance records verified:
     pos 3: items 1-8 (Group A, first_C)
     pos 5: items 9-16 (Group B, second_C)
     pos 7: items 17-24 (Group C, third_C_last_C)
   Balance confirmed 8/8/8.

7. Adjacency is intentionally broken in all 24 items
   STATUS: PASS
   All 24 cue_balance records: adjacency_broken=True, hop1_hop2_gap=2.
   Spot-check confirmed — representative items from each group:
     i01 (Group A): hop1@pos1, neighbor@pos2, hop2@pos3 — gap=2, neighbor interposed
     i09 (Group B): hop1@pos3, neighbor@pos4, hop2@pos5 — gap=2, neighbor interposed
     i17 (Group C): hop1@pos5, neighbor@pos6, hop2@pos7 — gap=2, neighbor interposed
   Interposed fact is always chain_id=neighbor_context, fact_role=neighbor_decoy_fact.
   No inert filler or decoy-chain fact used as separator.

8. Gate 5 precheck PASS with max_det = 8/24 ≤ 9/24
   STATUS: PASS
   Live re-run of compute_dummy_baseline_scores() over all 24 items (composite):
     always_return_first_C:  8/24
     always_return_second_C: 8/24
     always_return_third_C:  8/24
     always_return_last_C:   8/24
   max_det = 8/24 = 0.3333 ≤ 9/24 = 0.3750 — Gate 5 dummy precheck: PASS

9. always_return_ct and always_return_NULL are reference-only and excluded from max_det
   STATUS: PASS
   Live re-score confirms:
     always_return_ct:   24/24 = 1.0000  (ref only — excluded from max_det)
     always_return_NULL:  0/24 = 0.0000  (ref only — excluded from max_det)
   GATE5_REFERENCE_ONLY = {"always_return_ct", "always_return_NULL"} present in
   generate_cell03.py line 550 and applied in Phase 8 max_det computation.
   Packet §6 dummy baseline table documents both as reference-only.

10. §8 endpoint-intrusion diagnostic readiness explicitly confirmed
    STATUS: PASS — see §4 of this review for detail.

11. Standing caveat present
    STATUS: PASS — see §5 of this review.

12. Explicit no-inference confirmation present
    STATUS: PASS
    Packet §11: "No model inference was performed during Cell03 construction."
    Lists all non-executed inference types. Confirmed present in packet.
```

---

## 3. Cell02 Fixed-Confound Resolution Check

```text
Cell02 confound        Cell03 status
--------------------   -------------------------------------------------
Fixed second_C         RESOLVED — balanced 8+8+8 across first/second/third
exposure

Fixed endpoint-        RESOLVED — ct at pos 3 (8 items), pos 5 (8 items),
position exposure      pos 7 (8 items); no item shares fixed absolute pos

Fixed adjacency/       RESOLVED — neighbor interposed in ALL 24 items,
proximity cue          gap=2 uniformly; not broken in some, intact in others

Unreported endpoint-   RESOLVED — §8 readiness confirmed in packet §8;
intrusion diagnostics  all 10 required fields derivable from manifest
```

All four Cell02 fixed-confound problems are resolved in Cell03.

The fourth item (answer-domain salience — ct is always the correct composite
answer) is noted as UNCONTROLLED in the packet cue-balance table. This is
the correct classification; it cannot be controlled without changing the task
design, and §8 diagnostics are the designated tracking mechanism.

---

## 4. §8 Endpoint-Intrusion Diagnostic Readiness

Ten required fields per Team Lead §5:

```text
Field                              Source                          Status
---------------------------------  ------------------------------  --------
query_type                         item.queries keys               READY
                                   [hop1/hop2/composite/neg_graph]
                                   — present in all 24 items

expected_answer                    item.queries[qt].expected_answer READY
                                   — present in all 24 items,
                                   all 4 query types

returned_token                     scorer classify_output()         READY
                                   — runtime field, not in manifest;
                                   scorer captures for FORMAT_PASS

returned_role                      scorer via object_roles lookup   READY
                                   — object_roles present and
                                   complete for all 24 items;
                                   all chain C_objects confirmed
                                   in object_roles

ct vs other-C endpoint             item.chains[target].C_object     READY
                                   item.chains[decoy_*].C_object
                                   — all C_objects in chains
                                   and object_roles

B endpoint vs C endpoint           returned_role vs ROLE_HOP1_B     READY
                                   vs ROLE_ANSWER_C /
                                   ROLE_DISTRACTOR_CHAIN_ENDPOINT
                                   — object_roles has all roles

returned endpoint absolute pos     position_index via ordered_facts READY
                                   — all 24 items: position_index
                                   present on all 7 ordered_facts

returned endpoint C-rank           _c_objects_by_context_position() READY
                                   — chain_id on all ordered_facts;
                                   C_object in chains; function
                                   available in scorer

returned endpoint adjacency/       |pos(returned) - pos(hop1_fact)| READY
proximity                          |pos(returned) - pos(hop2_fact)|
                                   — fact_role on all ordered_facts;
                                   hop1_fact and hop2_fact identified
                                   by chain_id + fact_role

negative_graph expected NULL,      item.queries[neg_graph]          READY
returned endpoint                  expected_answer == "NULL"
                                   — confirmed 24/24
```

Multiple-position disambiguation rule (earliest position_index) confirmed
as consistent between packet §8 and scorer implementation.

For non-endpoint returns: position / rank / adjacency = N/A — confirmed
in packet §8 and consistent with scorer field behavior.

**§8 diagnostic readiness: CONFIRMED.** All 10 required fields are present
or derivable from the manifest at runner construction time.

---

## 5. Standing Caveat Confirmation

The mandatory standing caveat is present in packet §10:

```text
Gate 5 does not close target-token anchoring as a composite shortcut.
Composite ct-return is correct by construction and cannot be made
ceiling-bearing without turning the correct answer into a dummy failure.
Composite target-token anchoring remains tracked through §8 diagnostics,
especially hop1 failures returning ct.
```

Text confirmed present. No truncation or paraphrase.

---

## 6. Minor Observations (Non-Blocking)

### 6.1 ct_c_rank label format in manifest JSON

The manifest JSON `cue_balance` dict uses `ct_c_rank: "third_C_last_C"`
(underscore-separated) for Group C items. The construction packet narrative
and cue-balance table use `third_C/last_C` (slash-separated). This is a
cosmetic label format discrepancy — the structure is correct and
unambiguous. R = 3 is confirmed; third_C == last_C is correct for all Group C
items. Runner implementation should normalize the label or handle both forms.

### 6.2 C-token rotation design (informational)

C_DECOYS_1 = rotation by +8; C_DECOYS_2 = rotation by +16. This is
identical to the Cell01/Cell02 rotation design. The consequence is that
the C_target token of item N appears as C_decoy of other items. This is
by design, verified clean by the Phase 4 token audit (0 violations), and
consistent with the declared near-miss pair structure. No action required.

### 6.3 Cue-balance table: hop2_abs_position field name

The `cue_balance` dict uses `hop2_abs_position` as the key name, with
value equal to `ct_abs_position`. This is correct (hop2_fact contains ct
as the terminal node; hop2 position = ct position). The name is slightly
redundant with `ct_abs_position` but not incorrect.

---

## 7. Routing Recommendation

```text
Is Cell03 construction clean enough to route for Manager authorization
of one FP16 run only?
```

**YES.**

All 12 checklist items pass. Cell02 fixed-confound problems are fully
resolved. Gate 5 precheck passes at 8/24 — the tightest possible balanced
value (exactly at chance level for uniform_random_expected ≈ 1/3). §8
readiness is confirmed for all 10 required fields. The standing caveat and
no-inference confirmation are present and complete. No substantive issues
were found.

The three minor observations in §6 are clerical/informational and do not
affect construction integrity, gate validity, or run eligibility. None
requires a script re-run or manifest regeneration.

**Cell03 construction packet is clean. Routing to Team Lead for Manager
authorization of one FP16 run only.**

---

## Summary

```text
Checklist items:        12/12 PASS
Cell02 confounds:       4/4 RESOLVED
§8 readiness:           10/10 fields CONFIRMED
Standing caveat:        PRESENT
No-inference:           CONFIRMED
Minor observations:     3 (non-blocking, clerical/informational)

Routing recommendation: YES — route for Manager FP16 authorization
```

The construction packet is accurate. Hashes match. Live re-verification
confirms all packet claims. Cell03 is ready for Stage 0 lock.

**Stage 0 lock review complete. Disposition to Team Lead.**

— Senior Engineer, 2026-06-08
