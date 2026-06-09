# Cell02 Preparation Lock Packet — Two-Hop Level 1

**Date:** 2026-06-08
**Prepared by:** CS Engineer
**Status:** FILED — AWAITING TEAM LEAD REVIEW
**Per:** Manager memo — "Cell02 Construction Authorization — Position / Ordering Axis" 2026-06-08
**Requested by:** Team Lead memo — "Cell02 Construction Complete — Preparation Lock Packet Required" 2026-06-08

---

## Purpose

This packet consolidates all offline construction and validation artifacts for Cell02 and confirms that Cell02 changes only the approved axis (position / ordering) from Cell01. It is a pre-authorization packet. No model inference has been performed.

---

## 1. Cell02 item JSON path and SHA-256

```
Path:          tier0-run/items_twohop_l1_cell02.json
SHA-256:       sha256:b81d471616f8830fba76b99b9e1b04e23d3e4af13284c27627481ae89528f4c9
Items:         n = 24
Cell ID:       twohop_l1_cell02
Design:        3 chains per item (target + decoy_1 + decoy_2); 7 facts per context
Ordering:      all-C_target-last — T-hop2 at context position 6 for all 24 items
               (decoy_chain_2 hop2 at position 7 — mechanically required for Gate 5)
RNG seed:      random.Random(20260610)
Generator:     tier0-run/generate_cell02.py
```

**RNG seed note:** Seed 20260609 was discarded after it exposed a broken circuit breaker in `gen_pool` (reset before guard check — `att = 0` before `if att > 300000`), causing an infinite loop. The circuit breaker was fixed (guard moved before reset) and seed 20260610 was selected. The fix does not change the token construction protocol, audit criteria, or any experimental conditions. Seed 20260610 completed successfully with 0 violations.

---

## 2. Manifest hash

```
manifest_hash: sha256:b81d471616f8830fba76b99b9e1b04e23d3e4af13284c27627481ae89528f4c9
```

The manifest hash equals the item JSON hash — the manifest IS the item JSON file.

---

## 3. RNG seed

```
RNG seed: 20260610
```

Different from Cell01 (20260608) as required — new token pool for Cell02.

---

## 4. Validation summary

```
validate_manifest():  24/24 PASS (0 failures)
Confirmed by:         generate_cell02.py Phase 6 output
                      runner_twohop_l1_cell02.py --dry-run Step 2 output
```

---

## 5. Gate 0 / Gate 0.5 token-construction audit summary

### Gate 0 — Manifest schema

```
validate_manifest(): 24/24 PASS
All required fields present; chain structure, query anchors, and
negative_graph_control verified for all 24 items.
Gate 0: PASS
```

### Gate 0.5 — BPE-Jaccard token-construction audit

```
Audit tokenizer:     sha256:c0382117ea329cdf097041132f6d735924b697924d6f6fc3945713e96ce87539
                     (FP16 HuggingFace — confirmed run tokenizer)
Unique tokens audited: 216
Token pairs audited:   23,220
Lev violations (≤2, undeclared):            0
Trig violations (≥0.20, undeclared):        0
BPE-j violations (C-role, ≥0.40, undeclared): 0
Declared near-miss pairs:                   24
All declared pairs j ≥ 0.40:                CONFIRMED (see §6)
Gate 0.5: PASS
```

Token pool composition:

```
C_target / C_neighbor pairs:  24 (declared near-miss pairs)
C_decoy_1:                    rotation C_TARGETS[(i+8)%24]
C_decoy_2:                    rotation C_TARGETS[(i+16)%24]
A_target (prefix ZA):         24
A_decoy_1 (prefix ZD):        24
A_decoy_2 (prefix ZG):        24
B_target (prefix ZB):         24
B_decoy_1 (prefix ZE):        24
B_decoy_2 (prefix ZH):        24
Filler (prefix ZF):           24
Total unique tokens:           216
```

---

## 6. BPE-Jaccard audit under tokenizer sha256:c0382117...

All 24 declared near-miss (C_target / C_neighbor) pairs confirmed j ≥ 0.40 under the FP16 run tokenizer:

```
[01] RRWRO / RRWWT  lev=2  bjac=0.50  tjac=0.20
[02] VHPZM / VHPAS  lev=2  bjac=0.40  tjac=0.20
[03] SKMNK / MDMNK  lev=2  bjac=0.50  tjac=0.20
[04] UDNSZ / HXNSZ  lev=2  bjac=0.50  tjac=0.20
[05] AWILF / SVILF  lev=2  bjac=0.50  tjac=0.20
[06] IXENM / DHENM  lev=2  bjac=0.50  tjac=0.20
[07] NTELO / NTEJE  lev=2  bjac=0.50  tjac=0.20
[08] AJLAC / AJLMA  lev=2  bjac=0.50  tjac=0.20
[09] LVQLN / UDQLN  lev=2  bjac=0.50  tjac=0.20
[10] EQNPV / NYNPV  lev=2  bjac=0.50  tjac=0.20
[11] WJPGX / CDPGX  lev=2  bjac=0.40  tjac=0.20
[12] PPQDD / PPQFD  lev=1  bjac=0.50  tjac=0.20
[13] FJUDM / IOUDM  lev=2  bjac=0.40  tjac=0.20
[14] FLZAC / FBZAC  lev=1  bjac=0.50  tjac=0.20
[15] SGEJJ / SGEVC  lev=2  bjac=0.50  tjac=0.20
[16] DVRRO / DVRDF  lev=2  bjac=0.50  tjac=0.20
[17] VBLTH / VBLAY  lev=2  bjac=0.50  tjac=0.20
[18] EPXRX / EPXSI  lev=2  bjac=0.50  tjac=0.20
[19] PVMEO / PVMRC  lev=2  bjac=0.50  tjac=0.20
[20] MLIMZ / BOIMZ  lev=2  bjac=0.50  tjac=0.20
[21] SYPKQ / HYPKQ  lev=1  bjac=0.60  tjac=0.50
[22] DAAXS / HFAXS  lev=2  bjac=0.50  tjac=0.20
[23] OFWGM / OFWLP  lev=2  bjac=0.50  tjac=0.20
[24] PBKNW / CMKNW  lev=2  bjac=0.50  tjac=0.20

All 24 pairs: bjac ≥ 0.40  ✓
All cross-chain C-role pairs: bjac < 0.40 (0 violations)  ✓
```

---

## 7. Dummy baseline summary — Gate 5

Computed by `scorer_twohop_l1.py:compute_dummy_baseline_scores()` on composite query, all 24 items:

```
always_return_first_C:    0/24 = 0.0000
always_return_last_C:     0/24 = 0.0000
always_return_C_decoy_1:  0/24 = 0.0000
always_return_C_decoy_2:  0/24 = 0.0000
always_return_B_target:   0/24 = 0.0000
always_return_anchor_A:   0/24 = 0.0000
always_return_NULL:       0/24 = 0.0000
uniform_random_expected:  8.0/24 = 0.3333  [theoretical]

Max deterministic strategy (max_det): 0/24 = 0.0000
Gate 5 ceiling:                        9/24
Gate 5 dummy check:                    PASS  (0 ≤ 9)
```

**first_C / last_C functionality confirmed:**

The scorer's `_c_objects_by_context_position` sorts C-role objects by the position_index of their introducing hop2 fact. For all 24 Cell02 items:

```
Context positions of hop2 facts:
  decoy_chain_1 hop2 (cd1): position 2
  target_chain  hop2 (ct):  position 6
  decoy_chain_2 hop2 (cd2): position 7

c_by_pos = [cd1(pos 2), ct(pos 6), cd2(pos 7)]
first_C = cd1  →  NOT ct  →  always_return_first_C = 0/24  ✓
last_C  = cd2  →  NOT ct  →  always_return_last_C  = 0/24  ✓
```

The decoy_chain_2 hop2 placement at position 7 (after ct at position 6) is mechanically required by the all-C_target-last design constraint and the Gate 5 ceiling rule. This is documented in generate_cell02.py module docstring.

---

## 8. Runner path and hash

```
Path:   tier0-run/runner_twohop_l1_cell02.py
Hash:   sha256:d14f6424340699785a8bdc12a8bb6c2b7cb33f96069de49e1fcb945bbc12b0fa
```

**Amendment from Cell01 runner (runner_twohop_l1.py, sha256:f346e4f2...):**

```
Changed:
  ITEMS_PATH:         items_twohop_l1_cell02.json  (was: items_twohop_l1_cell01.json)
  AXIS_CONFIGURATION: "Single axis: position / ordering only. All 24 items C_target-last:
                       T-hop2 at context position 6. decoy_chain_2 hop2 at position 7
                       (Gate 5 forced). Token identities new (RNG seed 20260610);
                       all other variables frozen from Cell01."
  output filename:    RESULTS-TWOHOP-L1-cell02-{ts}.json

Unchanged (frozen):
  EXPECTED_VALIDATOR_HASH:  sha256:bcc26ca0...
  EXPECTED_SCORER_HASH:     sha256:060afad9...
  EXPECTED_TOKENIZER_HASH:  sha256:c0382117...
  MODEL_ID:                 Qwen/Qwen2.5-3B-Instruct
  DECODING_SETTINGS:        temperature=0.0, max_tokens=16
  FROZEN_SETTINGS:          relation_hop1/hop2/hold, context_length, chains_per_item,
                             query_phrasing, instruction_prefix
  QUERY_TEXT:               all 4 query phrasings identical
  render_context():         identical
  get_facts_for_query():    identical (negative_graph hop2 removal logic unchanged)
  render_prompt():          identical
  All inference logic:      identical
```

**One-axis constraint satisfied:** Only ITEMS_PATH and AXIS_CONFIGURATION changed. All locked execution constants are identical to the Cell01 runner.

---

## 9. Prompt template path and hash

```
Path:  tier0-run/prompt_template_twohop_l1.txt
Hash:  sha256:c8a81a299d28c3fd47f4d6fc90c4c57537885d07f01464e68d6fbe2e94a2510e
```

**Status: UNCHANGED from Cell01.** Same hash as recorded in Stage 1 Prep Lock Packet (Cell01): sha256:c8a81a29...

---

## 10. Scorer path and hash

```
Path:  tier0-run/scorer_twohop_l1.py
Hash:  sha256:060afad9db6fc56dc222d8dc1e856fa28fd379811269d899317dbd660c4a91bd
```

**Status: UNCHANGED from Cell01.** Confirmed by runner dry-run hash check (scorer_hash: OK).

---

## 11. Validator / manifest-validator hash

```
Path:  tier0-run/tasks_twohop_l1.py
Hash:  sha256:bcc26ca04b0c5a21db496d08c9307d2e6257315a9376f04473ea68ae36ca349b
```

**Status: UNCHANGED from Cell01.** Confirmed by runner dry-run hash check (validator_hash: OK).

---

## 12. Dry-run prompt-rendering summary

Runner command: `python runner_twohop_l1_cell02.py --dry-run`

```
Step 1 — Provenance hashes:
  runner_hash:           sha256:d14f6424...
  manifest_hash:         sha256:b81d4716...  ✓ matches items_twohop_l1_cell02.json
  validator_hash:        sha256:bcc26ca0...  ✓ OK
  scorer_hash:           sha256:060afad9...  ✓ OK
  prompt_template_hash:  sha256:c8a81a29...

Step 2 — Manifest validation:
  validate_manifest(): 24/24 pass  ✓

Step 3 — Tokenizer hash:
  tokenizer.json: /Users/eliasflores/.cache/huggingface/hub/
    models--Qwen--Qwen2.5-3B-Instruct/snapshots/aa8e72537.../tokenizer.json
  tokenizer_hash: sha256:c0382117...  ✓ OK

Dry-run prompt rendering (item[0] = twohop_l1_c02_i01, all 4 query types):
  [hop1]           chat_template: OK  raw=438chars  formatted=586chars
  [hop2]           chat_template: OK  raw=437chars  formatted=585chars
  [composite]      chat_template: OK  raw=463chars  formatted=611chars
  [negative_graph] chat_template: OK  raw=442chars  formatted=590chars

No model inference performed.
Dry-run exit: clean (exit 0)
```

**Sample rendered prompt — twohop_l1_c02_i01 / hop1:**

```
You are given a set of facts and a question. Answer using only information in
the facts provided. Respond using only this exact format with nothing before or
after: ANSWER: <TOKEN>
If no answer can be determined from the facts, respond: ANSWER: NULL

Facts:
ZDHCU links to ZEAQM.
ZEAQM maps to LVQLN.
ZGLED links to ZHQSU.
ZFNEK holds RRWWT.
ZAJAU links to ZBYQY.
ZBYQY maps to RRWRO.
ZHQSU maps to VBLTH.

Question: ZAJAU links to what?
```

Context ordering confirmed for item 01:
```
pos 1: ZDHCU links to ZEAQM.   [decoy_chain_1 hop1]
pos 2: ZEAQM maps to LVQLN.    [decoy_chain_1 hop2  ← cd1=LVQLN]
pos 3: ZGLED links to ZHQSU.   [decoy_chain_2 hop1]
pos 4: ZFNEK holds RRWWT.      [neighbor fact  ← cn=RRWWT]
pos 5: ZAJAU links to ZBYQY.   [target hop1]
pos 6: ZBYQY maps to RRWRO.    [target hop2  ← ct=RRWRO, T-hop2 at pos 6 ✓]
pos 7: ZHQSU maps to VBLTH.    [decoy_chain_2 hop2  ← cd2=VBLTH, forced pos 7 ✓]
```

Negative_graph confirmed: hop2 fact (pos 6) correctly removed; 6-fact context presented.

---

## 13. Explicit confirmation: only position / ordering changed

```
AXIS CHANGED (one axis):
  Context ordering:  all-C_target-last (T-hop2 at pos 6 for all 24 items)
                     [was: 8+8+8 mixed (C_target-first/middle/last)]
  Token identities:  new token pool (RNG seed 20260610)
                     [required by one-axis constraint: new cell = new tokens]

ALL OTHER VARIABLES UNCHANGED:
  See §14 for full frozen variable list.
```

The token identity change (new pool) is required by the experimental design — using Cell01's tokens in Cell02 would introduce token-identity confounds. New tokens drawn from the same construction protocol under the same BPE-Jaccard audit criteria are required. The construction protocol itself is unchanged.

---

## 14. Frozen variable list

The following are confirmed unchanged from Cell01:

```
Variable                         Cell01 value              Cell02 status
─────────────────────────────────────────────────────────────────────────
model                            Qwen/Qwen2.5-3B-Instruct  FROZEN
precision                        FP16                      FROZEN
n (items)                        24                        FROZEN
prompt template                  sha256:c8a81a29...        FROZEN (confirmed)
prompt template path             prompt_template_twohop_l1.txt  FROZEN
runner (execution logic)         sha256:f346e4f2...        AMENDED — see §8
  (ITEMS_PATH + AXIS_CONFIG      Cell01 items, 8+8+8       → Cell02 items, all-last
   only; all other constants     sha256:f346e4f2...        sha256:d14f6424...)
scorer                           sha256:060afad9...        FROZEN (confirmed)
validator                        sha256:bcc26ca0...        FROZEN (confirmed)
Gate 2 threshold                 ≥ 21/24                   FROZEN
Gate 3 ceilings                  as defined                FROZEN
Gate 5 ceiling                   ≤ 9/24                    FROZEN
relation (hop1)                  'links to'                FROZEN
relation (hop2)                  'maps to'                 FROZEN
relation (hold)                  'holds'                   FROZEN
context length                   7 facts                   FROZEN
chains per item                  3                         FROZEN
query wording (hop1)             '{anchor} links to what?' FROZEN
query wording (hop2)             '{anchor} maps to what?'  FROZEN
query wording (composite)        '{anchor} links to something, which maps to what?'  FROZEN
query wording (neg_graph)        '{anchor} links to something, which maps to what?'  FROZEN
negative_graph construction      remove target_chain/hop2_fact  FROZEN
distractor geometry              2 decoy chains, 1 neighbor     FROZEN
BPE-Jaccard threshold            j ≥ 0.40 (declared near-miss)  FROZEN
token-construction constraints   lev > 2, tjac < 0.20 (non-declared)  FROZEN
dummy baseline rules             first_C, last_C, uniform_random  FROZEN
failure taxonomy version         v1.0                      FROZEN
decoding temperature             0.0                       FROZEN
decoding max_tokens              16                        FROZEN
tokenizer (run)                  sha256:c0382117...        FROZEN
```

---

## 15. Explicit no-model-inference confirmation

```
NO MODEL INFERENCE HAS BEEN PERFORMED FOR CELL02.

All operations in this packet are offline only:
  - token pool generation (generate_cell02.py)
  - manifest construction and validation
  - BPE-Jaccard audit
  - dummy baseline computation
  - runner dry-run (provenance + manifest checks only; no model loaded for scoring)
  - prompt rendering (text output only; no model call)

FP16 inference for Cell02 is NOT authorized by this packet.
Authorization for Cell02 FP16 execution requires a separate Manager authorization
following Team Lead review of this packet.
```

---

## Summary

```
Cell ID:                twohop_l1_cell02
Axis change:            position / ordering only (one-axis rule satisfied)
Manifest hash:          sha256:b81d471616f8830fba76b99b9e1b04e23d3e4af13284c27627481ae89528f4c9
RNG seed:               20260610
validate_manifest():    24/24 PASS
Gate 0:                 PASS
Gate 0.5:               PASS (0 violations, 24/24 near-miss pairs j ≥ 0.40)
Gate 5 dummy ceiling:   PASS (max_det = 0/24 ≤ 9/24)
Dry-run:                PASS (all 4 query types rendered; tokenizer hash confirmed)
Scorer:                 sha256:060afad9... (FROZEN, confirmed)
Validator:              sha256:bcc26ca0... (FROZEN, confirmed)
Prompt template:        sha256:c8a81a29... (FROZEN, confirmed)
Runner (Cell02):        sha256:d14f6424... (amended: ITEMS_PATH + AXIS_CONFIG only)
Tokenizer (run):        sha256:c0382117... (FROZEN, confirmed in dry-run)
Model inference:        NOT PERFORMED — NOT AUTHORIZED
Status:                 AWAITING TEAM LEAD REVIEW
```

---

## 16. Construction proposal path and hash

```
Path:  tier0-run/CELL02-CONSTRUCTION-PROPOSAL-TWOHOP-L1.md
Hash:  sha256:731ddc6ad729121a52fa3b761976246f9a822a858f016964492764214f22229e
```

This document records the pre-registered design specification for Cell02 authorized by Manager memo 2026-06-08, including: selected axis (position/ordering), exact planned manipulation (all-C_target-last, T-hop2 at pos 6), frozen variables, 6 pre-registered diagnostic predictions, gate expectations, artifact requirements, and claim boundaries.

The packet implementation above conforms to the design specified in this proposal. No deviations from the proposal.

---

**Preparation lock packet complete. Cell02 FP16 execution requires separate Manager authorization after Team Lead review.**

— CS Engineer, 2026-06-08
