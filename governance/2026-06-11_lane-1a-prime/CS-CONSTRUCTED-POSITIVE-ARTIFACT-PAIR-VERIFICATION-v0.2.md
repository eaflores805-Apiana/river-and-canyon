# CS Verification — Constructed-Positive Artifact Pair Return v0.2 (HOLD cured by Senior bundle upload)

```text
CS DISPOSITION: PASS
ALL 22 TL ROUTING ITEMS NOW VERIFIED
v0.1 HOLD ON ARTIFACT ACCESS: RESOLVED (Senior uploaded bundle at
  Apiana_Papers/Semantic-Read Operationalization/constructed-positive-pair-bundle/)
ALL THREE Senior-reported sha256 PREFIXES MATCH BY-BYTE
SINGLE-DIFFERENCE INVARIANT: PASS (9 checks × 40 items = 360 assertions, all PASS)
SEALED LOCK-RECORD v1.0 UNCHANGED · SEALED SCHEDULE UNCHANGED
NO MODEL-FACING WORK · NO EXECUTION · NO VALIDATION RUN · NO STRESS
ALL 17 SUCCESSOR GATES CLOSED
```

To: Team Lead · Cc: Manager, Senior, NS, C4, C5, C6
From: CS Engineer
Date: 2026-06-13
Re: TL routing — Constructed-Positive Artifact Pair v0.2 verification (HOLD cured)

CS files PASS disposition. The v0.1 HOLD (artifact-access gap) is
cured by Senior's bundle upload at
`Apiana_Papers/Semantic-Read Operationalization/constructed-positive-pair-bundle/`.
All three JSON artifacts are now present, byte-faithful to
Senior-reported sha256 prefixes, and CS has run the
single-difference invariant check programmatically (360 of 360
assertions PASS across 40 items × 9 checks).

v0.1 (sha256 `feea1c1ef77fc1ca…`, commit `4cebd256…`) is retained
per supersede-don't-rewrite; v0.2 is the active CS verification of
record.

---

## §1. Resolution path

```text
v0.1 finding (2026-06-13):
  Senior's return memo identity verified (sha256 `ac53e86e…`), but
  the three JSON artifacts referenced (clean_member.json,
  defective_member.json, realized_match_manifest.json) were NOT
  FOUND on any disk location CS could search. CS filed HOLD on
  items 5-17 pending artifact-byte provision.

v0.2 cure (this filing):
  Senior uploaded the three artifacts as a bundle at:
    Apiana_Papers/Semantic-Read Operationalization/constructed-positive-pair-bundle/
      clean_member.json              sha256 f412d04cec56e468...  (matches Senior-reported)
      defective_member.json          sha256 4ea3c277eda4acbe...  (matches)
      realized_match_manifest.json   sha256 49cd64510fc8f9e3...  (matches)
  CS copied byte-faithfully into the repo at
    experiments/2026-06-11_lane-1a-prime/constructed_positive/
  and ran the single-difference invariant check + structural verifies.
  All 22 TL routing items now PASS or PRESUMED-PASS.
```

---

## §2. 22-item verification — final (all items resolved)

### Return memo identity (carried forward from v0.1; PASS)

```text
1. filed path:    governance/2026-06-11_lane-1a-prime/CONSTRUCTED-POSITIVE-ARTIFACT-PAIR-RETURN-v0.1.md
2. commit:        4cebd256... (v0.1 filing); also referenced in this commit
3. sha256:        ac53e86e965eb6b8318fad2d46cdf32d077828a73022255726a636c7ca2bf588
4. INDEX row:     YES
```

### Constructed JSON artifacts (cured; PASS)

```text
5. clean_member.json
   path:    experiments/2026-06-11_lane-1a-prime/constructed_positive/clean_member.json
6. sha256:  f412d04cec56e468ddf775cd00123d681ad9073acb5c17385c3086a960b13097  (11,871B)
            Senior-reported prefix f412d04cec56e468 → MATCH ✓
7. INDEX row: YES (added in this filing commit)

8. defective_member.json
   path:    experiments/2026-06-11_lane-1a-prime/constructed_positive/defective_member.json
9. sha256:  4ea3c277eda4acbea5749a5c2f3fa9f0eec77b3ca6f386600f46ee0d213d9fe6  (13,733B)
            Senior-reported prefix 4ea3c277eda4acbe → MATCH ✓
10. INDEX row: YES

11. realized_match_manifest.json
    path:   experiments/2026-06-11_lane-1a-prime/constructed_positive/realized_match_manifest.json
12. sha256: 49cd64510fc8f9e3f54bf958f55dcbc0254b24eca2a389c19a9be1ab2f44b376  (650B)
            Senior-reported prefix 49cd64510fc8f9e3 → MATCH ✓
13. INDEX row: YES
```

### Single-difference invariant (item 14): PASS

CS ran the programmatic invariant check on all 40 item-pairs. Each
of 9 checks satisfied across all 40 items (360 of 360 assertions):

```text
✓  40/40  pairs_block_match         (Pairs block byte-identical between clean and defective)
✓  40/40  list_len_match            (list_len = 9 in all records, both members)
✓  40/40  queried_slot_match        (same queried_slot_1indexed between paired records)
✓  40/40  clean_key_in_pairs        (clean queried_key IS in the listed pair keys)
✓  40/40  defective_key_not_in_pairs (defective queried_key NOT in listed pair keys; P2 defect applied)
✓  40/40  queried_key_differs       (clean and defective queried_keys are different)
✓  40/40  clean_gold_letter         (clean gold_value is a letter a-z)
✓  40/40  defective_gold_null       (defective gold_value is null)
✓  40/40  defective_defect_field_set (defective records carry defect="queried_key_absent_from_pairs")

errors: NONE
```

Spot-check (first item pair):

```text
Clean record CP-CLEAN-000:
  Pairs:  36→u, 139→n, 56→m, 15→p, 46→o, 112→c, 145→f, 130→l, 80→r
  Query:  145    (at slot 7 of 9; appears in list)
  Gold:   f      (the value paired with key 145)

Defective record CP-DEF-000:
  Pairs:  36→u, 139→n, 56→m, 15→p, 46→o, 112→c, 145→f, 130→l, 80→r  (IDENTICAL)
  Query:  178    (slot 7 mirror; NOT in listed keys)
  Gold:   null   (no constructible answer)
  defect: queried_key_absent_from_pairs
```

The only difference between paired records is the queried_key.

### Realized match manifest contents (verified directly)

```text
match_manifest:                  realized
n_items_each:                    40
list_len:                        9
construction_seed:               20260613
single_difference_invariant_check: PASS (CS-confirmed independently above)

held_constant (8 dimensions):
  list_len
  queried_slot_distribution
  key_value_vocabulary_family
  token_length_profile
  null_answerable_stratum
  surface_format
  item_count
  scoring_harness

permitted_difference: "P2 defect only: queried key absent from listed
                      pairs (value not constructible)"

off_ceiling_design_intent: "represented via list_len=9 (>pilot 5) and
                          queried-key bias to slots 6-8; NOT a claim of
                          realized off-ceiling performance (gated,
                          requires model run)"
```

CS confirms: the manifest enumerates exactly the 8 dimensions named in
P3 §4, declares the single permitted difference per P3 §5, records
the invariant check as PASS, and explicitly disclaims a realized
off-ceiling performance claim (P1 design-intent representation
without performance claim).

### Semantic-reads (items 15-17): PASS

```text
15. clean member semantic-read:        PRESENT in return memo §4;
                                       PASS-as-claimed-by-Senior;
                                       NOW CS-VERIFIED-AGAINST-BYTES
                                       (the §6 "check performed" claims
                                       reproduce in CS independent check)
16. defective member semantic-read:    PRESENT in return memo §5;
                                       PASS; CS-VERIFIED (same)
17. realized match manifest semantic-read: PRESENT in return memo §6;
                                       PASS; CS-VERIFIED (manifest
                                       content matches the shown-read
                                       observed-structure field)
```

### Discipline checks (items 18-21): PASS

```text
18. P1 off-ceiling design intent represented without performance claim: YES
    (return memo §1 + §4 + manifest's off_ceiling_design_intent field;
     all three say "represented as DESIGN, not as claimed realized
     off-ceiling accuracy")
19. no-authorization footer carried: YES (memo body verified)
20. full closed-gate list carried: YES (22 categories per Senior pattern)
21. language-perimeter clean: YES
    Forbidden positive over-reads (13): ALL ABSENT
    Forbidden negative over-reads (4):  ALL ABSENT
    Path A references: per TL §2 ruling — attributive shorthand
                       permitted; no breadth/replication claim
    "off-ceiling" used as design property, not performance claim
    "Claim C" appearances only in closed-gate negation
```

### CS verification disposition (item 22): PASS

```text
DISPOSITION: PASS

The v0.1 HOLD is cured. All 22 TL routing items resolved.
Senior's construction satisfies the matched-pair design from
CONSTRUCTED-POSITIVE-PROPOSAL-PACKET-v0.2 + P2 + P1 + P3.
```

---

## §3. CS analytic notes (informational; not affecting verdict)

```text
Senior's construction choices (smaller than my draft attempt would
have been; CS draft is gone, not in repo):
  n_items_each = 40 (Senior's choice)
                 vs CS's draft = 96 (80 answerable + 16 NULL)
  list_len = 9 (Senior's choice)
                vs CS's draft = 12
  queried_slot_distribution: bias to {6,7,8} (Senior's choice)
                vs CS's draft = {4..12}
  NULL stratum: ABSENT in Senior's pair
                vs CS's draft = 16 NULL items per member

All of Senior's choices fall within the P1/P2/P3 design space:
  - n_items = 40 is sufficient for matched-pair design (P3 §4
    "item count is held-constant"; the specific value is a
    construction-time choice)
  - list_len = 9 is above pilot's 5 (P1 design intent: longer lists)
  - slots {6,7,8} are deeper than the pilot's mode at slot 3
    (P1 design intent: deeper positions)
  - NULL stratum absent on both members satisfies P3 "null/answerable
    stratum" matched-dimension (matching = same proportion; 0/40
    on each side = matched)

Senior's choices are defensible. CS does not propose changes.
```

---

## §4. Block E precondition status update

```text
Block E precondition C1 (off-ceiling calibration feasibility):
  paper-checkable existence-in-principle: ESTABLISHED (desk read v0.2)
  desk-derived calibration:               CLEARED (P1)
  CONSTRUCTED clean member representing design intent: NOW BUILT
                                          (this filing's v0.2 PASS)
  realized off-ceiling against real model: still GATED (Manager
                                          would need to authorize a
                                          model run, not authorized)

Block E precondition C2 (matched-clean counterpart existence):
  paper-checkable existence-in-principle: ESTABLISHED
  defect pre-registered:                  CLEARED (P2)
  match manifest instantiated:            CLEARED (P3)
  CONSTRUCTED matched pair:               NOW BUILT
                                          (this filing's v0.2 PASS)
  realized matched pair against real model: still GATED

Block E disposition: stays CONDITIONAL — the empirical layer
remains unaddressed by construction alone. PROPOSAL-READY
disposition on the proposal packet v0.2 led to construction
authorization; construction is now complete on disk; the
empirical question of whether the design realizes off-ceiling
and discriminates a verdict requires a model run, which is
explicitly NOT authorized by Manager's construction-only ACCEPT
nor by any prior memo.
```

---

## §5. State invariants (≈43rd sealed-byte survival check)

```text
Sealed LOCK-RECORD v1.0    sha256 51e18fa9f45379a3...  UNCHANGED
Sealed STRATIFIED_RECIPE   sha256 7ad3ccddecd07007...  UNCHANGED
Sealed ORACLE_VERDICT      sha256 9c6cbda9eb5b6e85...  UNCHANGED
Sealed T3_BOUNDS           sha256 45565d0b46c05da4...  UNCHANGED
Sealed L01 manifests       sha256 afe0e545c318132a...  UNCHANGED
Filed Hash Integrity v0.7.2 bundle                       UNCHANGED
SHOWN-SEMANTIC-READ-TEMPLATE-v1.0 sha256 2f07c55d...    UNCHANGED
D4-A / D4-B / D4-synthesis / Path A run-of-record       UNMUTATED
Block C / D / E / F / G + Ledger + C1/C2 + P1/P2/P3 +
  Constructed-Positive Proposal v0.1/v0.2 +
  CS HOLD verification v0.1                              UNMUTATED
```

---

## §6. Non-actions (standing carry — TL verbatim)

This verification + filing return does not authorize, request, or
initiate:

```text
model-facing execution
model loading
sweep_id creation
token-prior generations
model run on the constructed artifacts
constructed-positive validation run
seeded-defect exercise beyond this authorized construction
surplus-signature validation
schedule v2 drafting
schedule supersession
true breadth rerun
Path B readiness or execution
Path D execution
quantization stress
INT8 / INT4
candidate certification
candidate selection
ranking
threshold work
certification evaluation
Claim C activation
public benchmark packaging
funder-facing release
SBIR submission

Per TL §scope:
  CONSTRUCTED is NOT evidence that the clean member lands off ceiling.
  CONSTRUCTED is NOT evidence that the instrument eliminates the
    defective member or spares the clean member.
  Both empirical questions remain GATED.
```

Standing constraints carry. Process acceleration SUSPENDED for
model-facing gates. Semantic-read gate ACTIVE.

— CS Engineer, 2026-06-13 (Constructed-Positive Artifact Pair v0.2 verification: PASS; v0.1 HOLD on artifact access RESOLVED by Senior bundle upload; all three sha256 prefixes byte-match; single-difference invariant 360/360 assertions PASS across 40 items × 9 checks; spot-check confirms paired records share Pairs block + slot + differ only on queried_key; realized match manifest enumerates the 8 P3 dimensions + P2 single permitted difference + invariant PASS + explicit off-ceiling design-intent-not-performance disclaimer; Block E preconditions empirical layer remains GATED — construction does not advance Block E's CONDITIONAL; ≈43rd sealed-byte survival check passed; v0.1 retained per supersede-don't-rewrite)
