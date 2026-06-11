# Run-3 Incidental Structural-Hit Disposition (v0.1)

```text
SYNTHETIC / DIAGNOSTIC — NON-BINDING — NOT FOR THRESHOLD DERIVATION
NARROW DISPOSITION MEMO — D3 GATE: HELD PENDING TL FILTER ON THIS MEMO
NO MODEL INVOKED · NO MODEL LOADED · NO SWEEP_ID · NO SWEEP EXECUTION
LOCK-RECORD PENDING
```

To: Team Lead · Cc: New Senior Engineer, Senior Engineer, Manager
From: CS Engineer (joint return; NS counter-signature awaited)
Date: 2026-06-11
Re: TL §5 narrow disposition — `salient_endpoint` 13/80 / envelope 49/80 incidental

CS files this narrow disposition addressing the one-item incidental
overlap reported in
`PHASE5-v0.2-CORRECTIVE-RUN3-COMPLETION-SUMMARY.md`. Position:
**Option A — acceptable incidental overlap under the accepted
item-label-disjoint construction**. No re-run required. No locked
artifact mutation required. One narrow documentation clarification
proposed (new memo only, not a mutation of the locked recipe schedule
sha256). Current run-3 result remains lock-eligible.

---

## §1. Cause of `salient_endpoint` 13/80

`salient_endpoint` measured 13 hits on the answerable stratum (vs the
intended construction constant of 12). The single extra hit comes from
the `no_structural_feature` stratum (32 items), where my
implementation of `construct_pilot_manifests`:

- forces `position[-1].value ≠ gold` (to prevent
  `recency_excluding_target` and `pure_last_position` from
  coincidentally firing),
- does NOT constrain `position[0].value`.

`position[0]`'s value is drawn uniformly from `VALUE_POOL`
(size = 26). With 32 items in the `no_structural_feature` stratum and
a 1/26 per-item probability of `position[0].value == gold`, the
expected incidental count is approximately 32 × (1/26) ≈ 1.23
hits. Measured: 1 hit. Statistically consistent with the construction.

Mechanism: when `position[0].value` happens to equal gold for a
`no_structural_feature` item, the `salient_endpoint` policy (which
emits `view.pairs[0].value`) emits gold and is scored as a hit. The
item carries no `salient_endpoint` structural-feature label (it remains
in `no_structural_feature` by design); the hit is a chance value-token
coincidence at position 0.

## §2. Effect on measured envelope 49/80

The single extra `salient_endpoint` hit lands on a
`no_structural_feature` item, which is otherwise un-hit by any policy.
Therefore the union envelope picks up +1 item:

```text
union envelope = 12 (gold_at_last_position)
              + 12 (gold_at_salient_endpoint)
              + 12 (gold_in_prefix_neighborhood)
              + 12 (gold_recency_adjacent)
              + 1  (no_structural_feature incidental, salient_endpoint hit)
              = 49 / 80 = 0.6125
```

vs the deterministic intended-construction constant 48/80 = 0.6000.

The envelope cap (0.80) is respected: 0.6125 + 0.1875 room ≤ 0.80.
The per-policy cap (0.50) is respected on every policy
(`pure_last_position` 0.30 ≤ 0.50; all others ≤ 0.1625).

## §3. Acceptability under locked semantics

**Acceptable under the accepted construction (Option A).**

The PH5-1 lock event accepted (per the NS blocker adjudication memo
sha256 `ea2cb8f7...`) that **item-label disjointness is sufficient**
and that **policy-hit disjointness is geometrically unconstructible**.
The adjudication's anti-tuning footing is verbatim:

> "the eliminative machinery is union-based and overlap-insensitive...
> the overlap is real structure in the shortcut space, and the recipe
> now represents it honestly instead of pretending the explanations are
> separable where they are not."

The same logic applies to the present incidental: under the locked
manifest construction, `no_structural_feature` items have uniform
distractor values drawn from `VALUE_POOL`, and policies that read
specific positions (e.g., `salient_endpoint` reads `position[0]`) will
occasionally find gold there by chance. That is a real structural
overlap (a "biased model" that always reads `position[0]` will
genuinely produce a correct answer on those items), not a construction
defect.

The instrument's invariants survive the incidental:

- The eliminative machinery is union-based: the measured envelope is
  used in difference arithmetic; 0.6125 is comfortably below the 0.80
  cap and comfortably above the 0.10 ENV margin's no-fire region.
- The per-policy caps are union-of-hits caps, not designated-hit
  caps. `salient_endpoint` at 13/80 = 0.1625 sits well below 0.50.
- No oracle case's `required_labels` or `required_absent_labels`
  shifts under the +1 incidental: ENV still fires on shortcut oracles
  (ORC-02..05, ORC-06, ORC-11) because their candidate accuracy minus
  envelope difference upper bound is still < 0.10; TP, FLOOR, CEIL
  attachments are determined by candidate behavior, not by envelope
  drift; HEAD remains non-firing under measured (1-envelope) = 0.3875.

This is precisely the situation NS's adjudication anticipated: real
shortcut-space overlap that the union-based machinery handles without
incident.

## §4. Documentation correction needed?

**Yes — narrow.** The current
`STRATIFIED_RECIPE_SCHEDULE.json` v2 carries the phrasing:

```text
union_envelope: "48/80 = 0.60 exactly under disjointness
                 (below 0.80 envelope cap with 0.20 room)"
per_policy_structural_hit_rate:
                "12/80 = 0.15 exactly per shortcut policy
                 (below 0.50 cap with maximal margin)"
```

The word "exactly" carries an implication that **measured** values
will equal **intended-construction** values. Under the
`no_structural_feature` stratum's uniform-VALUE_POOL distractor draws,
that equality is the **expected value** (mean over runs), not a
**guaranteed measurement**. The locked recipe sha256
`7ad3ccdd…` should NOT mutate (mutating it would break the PH5-1
lock-event hash precondition and require a fresh joint lock event).

The correction therefore goes here, in a documentation memo bound to
this disposition, with the following interpretation carried forward to
the future RUN3-INCIDENTAL section of the IVR and any subsequent
authorizations:

> The locked per-policy and envelope constants (12/80 = 0.15;
> 48/80 = 0.60) are the **intended construction constants** under the
> 5-stratum disjoint item-label schedule. **Measured** values may
> exceed the intended constants by O(1) items in any given execution,
> due to chance coincidences in the `no_structural_feature` stratum
> where distractor values are uniformly drawn from `VALUE_POOL` (size
> 26). Expected incidentals per policy ≈ 32 / 26 ≈ 1.23 per execution;
> per-policy hits and envelope are accordingly measured at
> intended-constant + O(1). The union-based eliminative machinery is
> overlap-insensitive to these incidentals; the per-policy and
> envelope caps (0.50 and 0.80 respectively) remain ample.

That paragraph is the documentation correction. It is **not** a
recipe-constant change; the locked constants stay 12/80 and 48/80.
The new memo (this one, plus any future cross-reference) supplies the
intended interpretation. CS proposes referencing this disposition
memo's sha256 alongside the recipe schedule sha256 in future
lock-event records as a permanent interpretation gloss.

## §5. Re-run needed?

**No.** Re-running with a different seed would not eliminate the
incidental — it would re-roll a different incidental count drawn from
the same distribution. The only construction change that would yield
exactly 48/80 every time is a tightening of `construct_pilot_manifests`
to force every `no_structural_feature` item's `position[0]` value to
≠ gold (and symmetrically constrain any position that could
coincidentally match). That tightening is a policy-aware manifest
construction — possible but **unnecessary**: the result is already
lock-eligible per the criterion arithmetic. Adding the tightening would
also remove a class of "real shortcut-space overlap" from the
synthetic, which contradicts the NS adjudication's premise that
overlaps are real structure to be reported honestly.

If TL prefers exact-constant guarantees in a future iteration, a
two-stage path is possible (NOT requested by this disposition):

- Phase A: declare the `no_structural_feature` tightening as a future
  schedule constraint in a NEW lock event (post-D3 or pre-D3 as TL
  elects).
- Phase B: re-execute under the tightened construction.

CS is willing to deliver Phase A + Phase B if TL requests, but does
**not** recommend it as a precondition for D3, on the grounds that
(a) the current result is lock-eligible, (b) the tightening would
suppress real overlap structure, and (c) the documentation correction
in §4 already resolves the ambiguity.

## §6. Current run-3 remains candidate for D3 review?

**Yes**, subject to TL acceptance of this disposition and the §4
documentation correction.

Lock-eligibility verification under measured values:

| check | result | margin |
|---|---|---|
| envelope < 0.80 cap | 0.6125 < 0.80 | 0.1875 |
| pure_last_position < 0.50 cap | 0.30 < 0.50 | 0.20 |
| salient_endpoint < 0.50 cap | 0.1625 < 0.50 | 0.3375 |
| recency_excluding_target < 0.50 cap | 0.15 < 0.50 | 0.35 |
| prefix_neighbor_confusion < 0.50 cap | 0.15 < 0.50 | 0.35 |
| copy_completion < 0.50 cap | 0.00 < 0.50 | 0.50 |
| HEAD (1-envelope) CI upper < 0.15 | 0.510 ≥ 0.15 (doesn't fire) | safe |
| FLOOR (NULL abstain) CI upper < 0.75 | 1.000 ≥ 0.75 (ideal safe) | safe |
| CEIL (answerable abstain) CI lower > 0.20 | 0 ≤ 0.20 (ideal safe) | safe |
| TP / ENV / GAP | all PASS on ideal | safe |
| Oracle label-set matching | 12/12 | exact |
| A6 drift | 0.0000 every component | exact |

All instrument invariants hold. No criterion behavior changes between
the intended-construction envelope (0.60) and the measured envelope
(0.6125). The result is candidate for D3 review.

## §7. Confirmation: no model invoked

**CONFIRMED.** This disposition memo is design-and-analysis work only;
no model invocation occurred. The validation harness has not been
re-executed since the run-3 commit (`b9b56d1`).

## §8. Confirmation: no sweep_id created

**CONFIRMED.** No sweep_id created. No sweep configuration referenced
or generated by this disposition.

## §9. Confirmation: no sweep execution

**CONFIRMED.** No sweep execution occurred. No batched or distributed
candidate generation initiated.

## §10. Confirmation: LOCK-RECORD remains PENDING

**CONFIRMED.** LOCK-RECORD remains PENDING. PH5-1 PASS stands. The
run-3 result and this disposition are instrument-validation evidence
under the D2 model-free boundary; they do not constitute D3 acceptance.
All downstream gates remain CLOSED: D3 acceptance; D4 sweep
authorization; D5 close-out; model runs; model loading; new sweep_id;
sweep execution; token-prior model generations; scrambled-binding
model generations; candidate/model outputs; candidate selection;
ranking; threshold work; certification evaluation; stress-retention
testing; Claim C activation; public benchmark packaging.

---

## Appendix — Answers to TL §5 question matrix (compact form)

| # | Question | Answer |
|---|---|---|
| 1 | Why did salient_endpoint measure 13/80 instead of 12/80? | 1 chance coincidence in the `no_structural_feature` stratum where `position[0]`'s uniform-`VALUE_POOL` distractor value happened to equal gold (expected incidentals per policy ≈ 1.23 per run). |
| 2 | Was this possible under the locked recipe? | Yes — under uniform-VALUE_POOL distractor draws, O(1) incidentals are a natural consequence of the construction. Not an unstated allowance; an implicit property the locked phrasing should have made explicit. |
| 3 | Does the lock-event "envelope = 48/80 = 0.60" need to be interpreted as INTENDED rather than MEASURED? | Yes. The locked constants are intended construction values; measured values are intended-constant + O(1) by the chance coincidences described above. |
| 4 | Is that interpretation already explicit enough? | No — the word "exactly" in the recipe schedule v2 carries a stronger implication than the construction supports. |
| 5 | What exact documentation correction is required? | The interpretation gloss in §4 above, filed as part of this disposition memo and referenced alongside the locked recipe schedule sha256 in future lock-event records. The locked recipe artifact itself does not mutate (preserves PH5-1 hash chain). |
| 6 | Does the validation result remain lock-eligible with measured envelope 0.6125? | Yes — every cap is respected with ample margin; no criterion verdict shifts; 12/12 oracle match holds. |
| 7 | Does this affect any oracle verdict, T3 result, A6 result, or headroom calculation? | No on all four. Oracle 12/12 unchanged; T3 all PASS unchanged; A6 drift 0.0000 every component unchanged; HEAD non-firing under both intended and measured envelope. |
| 8 | Is re-run required? | No. (Optional tightening described in §5 not recommended.) |
| 9 | Are any artifacts superseded? | No. Current run-3 stands. Run-3 attempt-1 retention block in `validation/superseded_run-3/` remains unchanged; the run-1, run-2 retention blocks remain unchanged. |

---

## NS counter-signature

```
[ AWAITING NEW SENIOR COUNTER-SIGNATURE ]

This is a joint disposition per TL §4. NS may counter-sign Option A
verbatim, or return a narrow disposition edit. The CS-side analysis is
final pending NS review.
```

## CS signature

```
CS Engineer · 2026-06-11
Disposition: Option A — acceptable incidental overlap under the
accepted item-label-disjoint construction. Documentation correction
proposed (§4); no re-run; no artifact supersession; current run-3
remains candidate for D3 review subject to TL filter on this memo.
```

— CS Engineer, 2026-06-11
