# Cell03 Construction Packet — Two-Hop Level 1

**Date:** 2026-06-08
**Prepared by:** CS Engineer
**Authorization:** Manager / Team Lead memo "Authorized — Construct Cell03 Manifest Only" 2026-06-08
**Status:** FILED — awaiting Team Lead review before Stage 0 lock

---

## 1. Cell03 Item Manifest

```text
File:             items_twohop_l1_cell03.json
Cell ID:          twohop_l1_cell03
n_items:          24
Chains per item:  3 (target_chain + decoy_chain_1 + decoy_chain_2)
Context facts:    7 per item
Relations:        hop1 = "links to" / hop2 = "maps to" / neighbor = "holds"
RNG seed:         20260615
Generation script: generate_cell03.py
```

---

## 2. Manifest Hash

```text
sha256:7d5099cbdccf1f2175e6c693ea851cab73109665d3420be345a475bf835240a1
```

---

## 3. Scorer Hash Used

```text
sha256:b65c6803017b8b04ac25d4bd84c5fb5ff61692ed41d609e099b181fa58e4ddde
```

This is the re-locked amended scorer (Cell03 scorer amendment, Manager-authorized 2026-06-08).

---

## 4. Validation Output

```text
$ python generate_cell03.py

Phase 6: validate_manifest()...
  Total=24  Pass=24  Fail=0
  validate_manifest(): ALL PASS
```

**24/24 PASS.** No validation errors.

---

## 5. Token Audit Output

```text
Tokenizer used:  sha256:c0382117ea329cdf097041132f6d735924b697924d6f6fc3945713e96ce87539
Tokenizer path:  models--Qwen--Qwen2.5-3B-Instruct (FP16 HuggingFace cache)

Token pool:      216 unique tokens (24 C_target + 24 C_neighbor + 24*7 role pools)
Pair count:      23,220 pairs audited

Phase 4 results:
  Lev violations  (<=2, undeclared):           0
  Trig violations (>=0.20, undeclared):        0
  BPE violations  (C-role, >=0.40, undeclared): 0

Token pool audit: PASS
```

All 24 declared near-miss pairs satisfy k ≤ 2, j_bpe ≥ 0.40, j_trig ≥ 0.20.

### Declared near-miss pairs (C_target / C_neighbor):

```text
[01] LLIXH / NFIXH   lev=2  bjac=0.50  tjac=0.20
[02] RPHBK / RPHDJ   lev=2  bjac=0.50  tjac=0.20
[03] HXPVQ / CPPVQ   lev=2  bjac=0.40  tjac=0.20
[04] CZFUR / CZFNF   lev=2  bjac=0.50  tjac=0.20
[05] RJJZO / RJJNK   lev=2  bjac=0.50  tjac=0.20
[06] YHIJZ / YHIYD   lev=2  bjac=0.40  tjac=0.20
[07] OUFOK / XEFOK   lev=2  bjac=0.50  tjac=0.20
[08] CLZMW / MHZMW   lev=2  bjac=0.50  tjac=0.20
[09] YJKBM / YJKCV   lev=2  bjac=0.50  tjac=0.20
[10] GCGMX / GCGGG   lev=2  bjac=0.50  tjac=0.20
[11] RIMFB / RIMAR   lev=2  bjac=0.50  tjac=0.20
[12] KRNJK / YRNJK   lev=1  bjac=0.50  tjac=0.50
[13] ZTPUT / ZTPGC   lev=2  bjac=0.50  tjac=0.20
[14] MDUJI / MDURU   lev=2  bjac=0.50  tjac=0.20
[15] AYKRS / XYKRS   lev=1  bjac=0.50  tjac=0.50
[16] AARQW / AARLN   lev=2  bjac=0.40  tjac=0.20
[17] LRPTZ / NZPTZ   lev=2  bjac=0.50  tjac=0.20
[18] EFSCG / RWSCG   lev=2  bjac=0.50  tjac=0.20
[19] YNVBT / YNVQG   lev=2  bjac=0.40  tjac=0.20
[20] DYLYG / GHLYG   lev=2  bjac=0.50  tjac=0.20
[21] VOTRJ / VOTPN   lev=2  bjac=0.40  tjac=0.20
[22] GYKXD / GYKUO   lev=2  bjac=0.40  tjac=0.20
[23] AQRJC / AQRVF   lev=2  bjac=0.50  tjac=0.20
[24] LDFVJ / LDFJN   lev=2  bjac=0.60  tjac=0.20
```

All pairs satisfy: lev ≤ 2, bjac ≥ 0.40, tjac ≥ 0.20. Gate 0.5 PASS.

---

## 6. Dummy Baseline Table (composite query, all 24 items)

```text
Dummy                        Count / Rate      Status
--------------------------   ---------------   -------
always_return_first_C        8/24  = 0.3333    ceiling-bearing
always_return_second_C       8/24  = 0.3333    ceiling-bearing
always_return_third_C        8/24  = 0.3333    ceiling-bearing
always_return_last_C         8/24  = 0.3333    ceiling-bearing
always_return_ct             24/24 = 1.0000    reference-only (excluded from max_det)
always_return_NULL           0/24  = 0.0000    reference-only (excluded from max_det)
always_return_B_target       0/24  = 0.0000    diagnostic
always_return_anchor_A       0/24  = 0.0000    diagnostic
always_return_C_decoy_1      0/24  = 0.0000    diagnostic
always_return_C_decoy_2      0/24  = 0.0000    diagnostic
uniform_random_expected      ≈0.3333           theoretical reference
```

Per-group breakdown:

```text
Group A (items 1-8, ct first_C at pos 3):
  always_return_first_C:  8/8   <- ct IS first_C
  always_return_second_C: 0/8
  always_return_third_C:  0/8
  always_return_last_C:   0/8
  always_return_ct:       8/8   (ref)

Group B (items 9-16, ct second_C at pos 5):
  always_return_first_C:  0/8
  always_return_second_C: 8/8   <- ct IS second_C
  always_return_third_C:  0/8
  always_return_last_C:   0/8
  always_return_ct:       8/8   (ref)

Group C (items 17-24, ct third_C = last_C at pos 7):
  always_return_first_C:  0/8
  always_return_second_C: 0/8
  always_return_third_C:  8/8   <- ct IS third_C
  always_return_last_C:   8/8   <- ct IS last_C (third_C == last_C for R=3)
  always_return_ct:       8/8   (ref)
```

Note: `always_return_ct` = 24/24 on composite is expected by construction (ct IS the
correct composite answer). This is the reference-only upper bound; it is excluded from
the max_det ceiling check per GATE5_REFERENCE_ONLY policy.

---

## 7. Gate 5 Precheck Result

```text
Max deterministic (ceiling-bearing): 8/24 = 0.3333
Gate 5 ceiling:                      9/24 = 0.3750
Margin:                              1/24

Gate 5 dummy precheck: PASS
```

The 8/24 balanced design ensures each rank dummy scores exactly at chance level
(8/24 ≈ 1/3 = uniform_random_expected). No rank dummy is inflated by ct being
fixed at a single rank across all items (the Cell02 confound is resolved).

The `always_return_ct` and `always_return_NULL` reference-only dummies are
excluded from the max_det calculation per GATE5_REFERENCE_ONLY policy.

---

## 8. §8 Diagnostic Readiness Confirmation

The Cell03 runner (`runner_twohop_l1_cell03.py`, to be constructed) must emit
item-level §8 endpoint-intrusion diagnostics for all scored items. This section
confirms the manifest supports all required diagnostic fields.

### Required §8 fields — manifest readiness:

```text
query_type
  Source: query key (hop1 / hop2 / composite / negative_graph)
  Status: present in manifest queries dict — READY

expected_answer
  Source: item.queries[query_type].expected_answer
  Status: present — READY

returned_token
  Source: scorer classify_output() returned_token field
  Status: scorer captures this field for all FORMAT_PASS outputs — READY

returned_role
  Source: scorer classify_output() returned_role field
  Status: scorer captures this field via object_roles lookup — READY

ct vs other-C endpoint
  Source: compare returned_token to item.chains[target].C_object (ct)
          and item.chains[decoy_*].C_object (cd1, cd2)
  Status: all C_objects present in chains and object_roles — READY

B endpoint vs C endpoint
  Source: compare returned_role to ROLE_HOP1_B vs ROLE_ANSWER_C /
          ROLE_DISTRACTOR_CHAIN_ENDPOINT
  Status: object_roles has all role assignments — READY

returned endpoint absolute position
  Source: map returned_token to position_index via ordered_facts
  Status: all tokens appear in ordered_facts; position_index present — READY
  Disambiguation: earliest position_index if token appears at multiple positions
                  (same rule as _c_objects_by_context_position)

returned endpoint C-rank
  Source: compute _c_objects_by_context_position(item), find index of returned_token
  Status: scorer function available; c_by_pos derivable from manifest — READY

returned endpoint adjacency/proximity
  Source: |position(returned_token) - position(target_hop2_fact)| 
          and |position(returned_token) - position(target_hop1_fact)|
  Status: all position_index values present in ordered_facts;
          target_chain hop1_fact and hop2_fact identified by chain_id + fact_role — READY

negative_graph expected NULL, returned endpoint
  Source: query_type == negative_graph, returned_token != NULL
  Status: negative_graph queries with expected_answer=NULL present — READY
```

For non-endpoint returns (returned_role not in ROLE_ANSWER_C / ROLE_DISTRACTOR_CHAIN_ENDPOINT):
```text
  position / rank / adjacency = N/A
```

Multiple-position objects: use earliest position_index (same rule as scorer).

**§8 diagnostic readiness: CONFIRMED.** All required fields derivable from
the manifest and scorer output. Runner implementation responsibility is noted.

---

## 9. Cue-Balance Table

The three confounded Cell02 cues that are controlled in Cell03:

```text
Cue                   Cell02                 Cell03
--------------------- ---------------------- ------------------------------
Adjacency/proximity   hop1 at pos 5,         neighbor interposed between
                      hop2 at pos 6,         hop1 and hop2 in ALL 24 items;
                      ADJACENT (gap=1)       gap = 2 (one fact between)
                                             [PRIMARY AXIS MANIPULATION]

ct C-rank             ct = second_C for      8 items: ct = first_C  (Group A)
                      ALL 24 items           8 items: ct = second_C (Group B)
                                             8 items: ct = third_C/last_C (Group C)
                                             [CONTROL REPAIR — balanced]

ct absolute position  ct at pos 6 for        8 items: ct at pos 3 (Group A)
                      ALL 24 items           8 items: ct at pos 5 (Group B)
                                             8 items: ct at pos 7 (Group C)
                                             [CONTROL REPAIR — balanced]

Answer-domain         ct is always the       ct is always the correct composite
salience              correct composite      answer (cannot be controlled without
                      answer                 changing task design) — unchanged
                                             [UNCONTROLLED — §8 diagnostic only]
```

### Per-item cue-balance summary:

```text
Group   Items    ct_C_rank      ct_abs_pos   hop1_pos   hop2_pos   neighbor_pos   adjacency
------  -------  -------------- ----------   --------   --------   ------------   ---------
A       1-8      first_C        3            1          3          2              broken (gap=2)
B       9-16     second_C       5            3          5          4              broken (gap=2)
C       17-24    third_C/last_C 7            5          7          6              broken (gap=2)
```

The neighbor fact (`fl holds cn`) is positioned immediately between target hop1 and
target hop2 in all three groups. The interposed fact is always the neighbor_decoy_fact;
no inert or decoy-chain fact is used as the separator.

---

## 10. Standing Caveat

**This caveat is mandatory in all Cell03 documents.**

```text
Gate 5 does not close target-token anchoring as a composite shortcut.
Composite ct-return is correct by construction and cannot be made ceiling-bearing
without turning the correct answer into a dummy failure.
Composite target-token anchoring remains tracked through §8 diagnostics,
especially hop1 failures returning ct.
```

---

## 11. Explicit No-Inference Confirmation

```text
No model inference was performed during Cell03 construction.

The following were not executed:
  FP16 run
  INT8 run
  INT4 run
  confirmation pass
  prompt repair
  7B evaluation

The generate_cell03.py script performs:
  token generation and BPE-Jaccard audit (tokenizer only, no model)
  manifest schema validation (offline, no model)
  dummy baseline computation (deterministic scorer, no model)

items_twohop_l1_cell03.json is a manifest only. No model outputs are included.
```

---

## Summary

```text
Cell ID:                    twohop_l1_cell03
Manifest hash:              sha256:7d5099cbdccf1f2175e6c693ea851cab73109665d3420be345a475bf835240a1
Scorer hash:                sha256:b65c6803...
Tokenizer hash:             sha256:c0382117...  (FP16 run tokenizer — confirmed match)
validate_manifest():        24/24 PASS
Token audit:                PASS (0 Lev / 0 Trig / 0 BPE violations)
Gate 5 precheck:            PASS (max_det = 8/24 ≤ 9/24)
§8 readiness:               CONFIRMED
Adjacency broken:           ALL 24 items (gap = 2)
ct C-rank balance:          8 first_C / 8 second_C / 8 third_C-last_C
ct position balance:        8 at pos 3 / 8 at pos 5 / 8 at pos 7
No inference:               CONFIRMED

Cell03 construction:        COMPLETE — awaiting Team Lead Stage 0 lock review
```

**Construction packet filed. No model inference authorized or performed.**

— CS Engineer, 2026-06-08
