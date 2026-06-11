# CS-Side Proposed Dispositions — INH-1 / INH-2 / INH-3 + Prompt-Shell Visibility

```text
DRAFT / REVIEW ONLY
D2 PACKET-PREPARATION ARTIFACT
NO D2 ACCEPTANCE GRANTED
NO EXECUTION AUTHORIZED
NO SWEEP_ID CREATED
NO MODEL RUNS
NO DATA GENERATED
NO VALIDATION OUTPUTS POPULATED
NO CODE IMPLEMENTATION BEGUN
```

From: CS Engineer
To: New Senior Engineer (for co-review); Team Lead (for filter after NS co-review)
Cc: Senior Engineer, Manager
Date: 2026-06-11
Re: CS-side proposed dispositions for INH-1, INH-2, INH-3 + prompt-shell visibility recommendation for `unconditioned_token_prior`
Status: CS proposed — awaiting NS co-review; not yet a joint co-draft

---

## 0. Routing posture

Per Team Lead direction of 2026-06-11: D2 work begins with the four
governance items above; "co-drafted with New Senior before CS begins
code implementation."

CS files **its own proposed positions** in this document. NS picks up,
edits / endorses / counter-proposes. The joint co-draft emerges from
the NS+CS exchange. This document is the CS-side starting point, not
a unilateral disposition.

NS items to consider when co-reviewing:
- Are the proposed N_effective conventions semantically right for
  each diagnostic?
- Is the outcome enum's `NON_ELIMINATED` value correctly named for
  the negative-use doctrine?
- Is Wilson the right CI method, or does the construction's expected
  saturation behavior argue for Jeffreys?
- Is "value pool visible" the right prompt-shell visibility for
  `unconditioned_token_prior`?

---

## 1. INH-1 — Per-diagnostic stratum semantics

### CS proposed disposition

**Default rule:** every metric computes over its **stratum-specific
N_effective**. Cross-stratum aggregation requires explicit
declaration. No metric silently aggregates 80+16.

### Per-metric N_effective table (CS proposed)

| Metric | Stratum | N_effective | Rationale |
|---|---|---|---|
| Per-policy `answerable_acc` | answerable | **80** | accuracy on items where retrieval is the right operation |
| Per-policy `null_acc` | null | **16** | accuracy on items where abstention is the right operation |
| `distinct_outputs` (per policy) | all items | **96** | output-diversity count over the full rung |
| Union envelope score | answerable | **80** | union of per-policy answerable accuracies; envelope is answerable-side by construction |
| `envelope_cap` and `room_below_envelope` | answerable | **80** | the cap is on union envelope; same denominator |
| Operation-equivalence classification (cap check) | answerable | **80** | caps are on answerable_acc per addendum A2/A4 |
| NULL-stratum abstention rate (T3 floor criterion) | null | **16** | abstention measured on NULL items only |
| Answerable-stratum abstention rate (T3 ceiling criterion) | answerable | **80** | abstention measured on answerable items only |
| `unconditioned_token_prior` baseline measurement | answerable (mirrored) | **80** | scoring target is "gold value of mirrored answerable item" per T2 |
| `scrambled_binding_retrieval` correctness | answerable (post-scramble) | **80** | scoring is post-scramble gold on answerable items |
| `copy_completion` agreement rate (diagnostic sidecar) | all items | **96** | per-item agreement applies wherever copying could resolve the item; CS-EP v0.2 §5.1 stores per-item |
| A6 drift on per-policy answerable_acc | answerable | **80** | same denominator as the underlying metric |
| A6 drift on envelope | answerable | **80** | same denominator as the underlying metric |
| A6 drift on null_acc | null | **16** | same denominator as the underlying metric |
| RFI counts / inconclusive counts (rung-level) | n/a (counts) | rung count | metadata about rungs, not items |

### CS schema implications

- T1 table column **`n_effective`** is added per row so the auditor
  can verify the stratum semantics at a glance.
- The analysis script's per-stratum aggregation function takes
  `stratum: Literal["answerable", "null", "all"]` as a required
  argument; no default stratum.
- Per-policy scores returned by the policy battery carry the stratum
  tag they were computed against; mixing strata in a single score
  field is a code-level invariant violation.

### CS implementation footprint (under D2 code authorization)

- `manifest_record.stratum: Literal["answerable", "null"]` (closed enum).
- `compute_per_policy_score(policy, records, stratum)` returns
  `PerPolicyScore(stratum, n_effective, score)`.
- `compute_union_envelope(scores, stratum="answerable")` enforces
  stratum at the type level.
- A6 drift comparison only between scores of the same stratum.

### Open question for NS

Is there any diagnostic NS plans to introduce that aggregates
cross-stratum (i.e., genuinely needs N=96)? `distinct_outputs` is the
only such metric CS identified. If NS plans others, the table above
extends; if not, CS proposes the table is complete at v0.2.

---

## 2. INH-2 — Outcome-chooser totality

### Four sub-questions to answer

1. Non-eliminated predicate
2. RFI-only behavior
3. Inconclusive class
4. Fixed language

### CS proposed disposition

**Outcome enum (closed set; no `passes_*` value):**

```python
class RungOutcome(Enum):
    # Elimination labels (one per pre-registered elimination criterion in T3)
    CLEARLY_FAILS_TOKEN_PRIOR_SEPARATION = "clearly_fails_token_prior_separation"
    CLEARLY_FAILS_ENVELOPE_RULE          = "clearly_fails_envelope_rule"
    CLEARLY_FAILS_MEASUREMENT_HEADROOM   = "clearly_fails_measurement_headroom"
    CLEARLY_FAILS_STRICT_CONTENT_GAP     = "clearly_fails_strict_content_gap"
    CLEARLY_FAILS_NULL_ABSTENTION_FLOOR  = "clearly_fails_null_abstention_floor"
    CLEARLY_FAILS_ANSWERABLE_CEILING     = "clearly_fails_answerable_ceiling"
    # Tertiary states
    REQUIRES_FURTHER_INVESTIGATION       = "requires_further_investigation"
    INCONCLUSIVE                          = "inconclusive"
    NON_ELIMINATED                        = "non_eliminated"
    # NO passes_X value — structural enforcement of "may rule out, may not rule in"
```

(The exact set of `CLEARLY_FAILS_*` values matches the T3 elimination
criteria; the enum above is illustrative.)

### Non-eliminated predicate (equality survivor)

A rung classifies as `NON_ELIMINATED` if and only if:

```python
def is_non_eliminated(rung_evaluation: RungEvaluation) -> bool:
    return (
        not rung_evaluation.is_inconclusive()
        and not any(rung_evaluation.is_eliminated_by(label)
                    for label in ELIMINATION_LABELS)
        and not rung_evaluation.is_rfi()
    )
```

"Equality" means the predicate is hard-Boolean: no soft survivorship,
no threshold proximity counts as survival, no weighted scoring.

### Inconclusive preempts

`INCONCLUSIVE` fires when data is insufficient to evaluate ANY of the
elimination criteria. Specifically, INCONCLUSIVE fires when:

- The pilot iteration log retained ≥1 failed pilot AND the failure
  was unresolved at lock (anti-tuning rule violation; addendum E11);
- Manifest validation failed for the rung's locked manifest;
- ≥1 required policy / control output is missing from the sidecar
  for any item in the rung;
- The A6 final-manifest re-verification flagged drift exceeding the
  declared tolerance (IS-7) for any metric required to evaluate the
  rung's criteria.

INCONCLUSIVE preempts every other outcome: a rung that would have
been NON_ELIMINATED but suffers a data-sufficiency failure is
INCONCLUSIVE, not NON_ELIMINATED.

### RFI-only behavior

`REQUIRES_FURTHER_INVESTIGATION` fires when a criterion's measurement
falls within a pre-declared "uncertain zone" (specific to the
criterion, declared in T3 at packet-stage lock).

RFI is **neither** elimination **nor** non-elimination:

- RFI rungs are NOT counted in K (K counts NON_ELIMINATED only).
- RFI rungs are NOT counted in the eliminated count.
- RFI rungs are flagged for re-execution at a later authorization (if
  any; not authorized by D2 / D4).
- An RFI rung **never** mutates to NON_ELIMINATED in this lane's
  outputs without a separately authorized re-execution + re-evaluation.

### Outcome priority order (when multiple states could apply)

```text
1. INCONCLUSIVE (data sufficiency check; preempts all)
2. CLEARLY_FAILS_* (elimination labels; all-applicable labels are
                     recorded; rung is eliminated)
3. REQUIRES_FURTHER_INVESTIGATION (uncertain-zone fire)
4. NON_ELIMINATED (residual; only if none of 1-3 fire)
```

### K count

```python
K = sum(1 for rung in rungs if rung.outcome == RungOutcome.NON_ELIMINATED)
```

K excludes INCONCLUSIVE, all CLEARLY_FAILS_*, and RFI. K equals the
non-eliminated rung count.

### Fixed language (typed string constants)

```python
# Lane 1a' fixed outcome statements — typed string constants.
# Emission is structural; no other text may be emitted as the
# lane's outcome statement.

K_EQUALS_ZERO_STATEMENT = (
    "Under the sealed Validation Report, the Lane 1a' sweep returned "
    "K=0: no rung was non-eliminated under the pre-registered "
    "negative-use diagnostics. Per the symmetric finality rule "
    "(Lane 1a' Design Proposal v0.2 §10), this is the lane's "
    "substantive reconnaissance-negative finding for this task "
    "family at this scale, for this construction. It is not a "
    "Paper 3 certification verdict and not evidence of model "
    "incapability."
)

SINGLE_NON_ELIMINATED_RUNG_STATEMENT = (
    "The Lane 1a' sweep returned K=1: one rung was non-eliminated "
    "under the pre-registered negative-use diagnostics. Per the "
    "no-positive-use rule (Lane 1a' Design Proposal v0.2 §10), "
    "this outcome is not promising, viable, candidate-ready, "
    "near-certifiable, or suitable for positive selection. It does "
    "not rank, support candidate selection, support threshold work, "
    "or constitute certification evidence."
)

MULTIPLE_NON_ELIMINATED_STATEMENT_TEMPLATE = (
    "The Lane 1a' sweep returned K={k}: {k} rungs were "
    "non-eliminated under the pre-registered negative-use "
    "diagnostics. Per the no-positive-use rule (Lane 1a' Design "
    "Proposal v0.2 §10), this outcome is not promising, viable, "
    "candidate-ready, near-certifiable, or suitable for positive "
    "selection. Non-eliminated rungs are listed in rung-ID order; "
    "no rank fields or computations are emitted; the unordered "
    "non-eliminated set carries no positive evidence weight."
)
```

The outcome-chooser code emits exactly one of these three (or their
RFI/INCONCLUSIVE variants). The strings are hashed into the LOCK-RECORD
via `analysis_script_hash`.

### CS implementation footprint (under D2 code authorization)

- `outcome_chooser.py` exports `compute_rung_outcome(rung_evaluation: RungEvaluation) -> RungOutcome` and `emit_outcome_statement(K: int, non_eliminated_rungs: list[RungID]) -> str`.
- The three fixed-language statements are constants; no f-string interpolation except for the `{k}` and the rung-ID list in the multiple case.
- Test: `test_outcome_enum_has_no_passes_value` — source-level grep asserts no enum value starts with `passes_`.
- Test: `test_emit_outcome_statement_uses_fixed_constants` — source-level grep asserts the emitter references only the named constants.

### Open questions for NS

- Are the elimination labels above (TOKEN_PRIOR_SEPARATION, ENVELOPE_RULE, etc.) the correct set per T3? CS pulled them from Bundle v0.3 §IV's checklist enumeration; NS confirms or adjusts.
- Is the SINGLE_NON_ELIMINATED_RUNG_STATEMENT wording right? CS used the v0.2 §10 no-positive-use language; NS may have specific phrasing.

---

## 3. INH-3 — SE interval method

### CS proposed disposition

**Wilson score interval** (without continuity correction) as the
declared SE interval method for all reported binomial-proportion
diagnostics.

### Rationale

Comparing the candidate methods at our regime (N=80 or N=16; metrics
that may be near boundaries 0 or 1):

| Method | Behavior at boundaries | N=16 coverage | N=80 coverage | Recommended? |
|---|---|---|---|---|
| Wald | catastrophic (interval can extend past [0,1]; coverage collapses near p∈{0,1}) | poor | acceptable far from boundaries | **NO** — never silently Wald per Bundle v0.3 §V INH-3 |
| Wilson (score interval) | excellent (asymmetric near boundaries; bounded in [0,1]) | good | good | **YES — CS recommendation** |
| Wilson with continuity correction | conservative version of Wilson | good (slightly wider) | good (slightly wider) | acceptable alternative if conservatism is preferred |
| Jeffreys (Bayesian) | excellent (smooth; equal-tail credible interval) | good | good | acceptable alternative; requires a prior choice |
| Agresti-Coull | simple approximation of Wilson | acceptable | good | unnecessary when Wilson is available |
| Clopper-Pearson | conservative exact interval | conservative; can be very wide near boundaries | conservative | acceptable for worst-case bounds; overly conservative for reporting |

### Why Wilson

1. Many of our metrics will sit near boundaries:
   - NULL abstention ideally 1.0 (perfect contract abstention)
   - Answerable accuracy potentially near 1.0 (ideal retriever) or near 0.0 (degenerate policy)
   - Token-prior baseline near 1/|value_pool|, which is small
2. N=16 (NULL stratum) is small enough that Wald's catastrophic boundary behavior is unacceptable.
3. Wilson's asymmetric interval near boundaries handles the "100% on 80 items" case without producing a degenerate zero-width interval (which Wald would).
4. Wilson is the standard recommendation in modern statistical literature for binomial proportion confidence intervals at small-to-moderate N.
5. Implementation is well-tested (`scipy.stats.binom_interval(method='wilson')`); CS can implement directly without scipy dependency if dependency surface is a concern.

### Anti-tuning constraint

The SE interval method is declared in T1 at packet lock and hashed
into LOCK-RECORD via `t1_plan_hash` (D1) and
`drift_tolerance_declaration_hash` (D3). Post-pilot change is a
must-fix event requiring C1 disposition per addendum.

### CS implementation footprint (under D2 code authorization)

```python
def wilson_ci(successes: int, n: int, alpha: float = 0.05) -> tuple[float, float]:
    """
    Wilson score interval (no continuity correction).
    Asymmetric; bounded in [0, 1]; well-behaved near p∈{0,1}.
    
    INVARIANT: this function is the ONLY CI emitter in the analysis
    script. test_no_other_ci_method_in_analysis source-level grep
    asserts no call site uses scipy.stats.norm-based Wald formula.
    """
```

Single CI function across the codebase; structurally prevents
silent Wald drift.

### Open question for NS

- Wilson with or without continuity correction? CS proposes without (the standard form). NS may prefer with-continuity-correction for additional conservatism on the NULL stratum (N=16).
- If NS prefers Jeffreys, CS implements Jeffreys instead; the constraint is "never silently Wald".

---

## 4. Prompt-shell visibility recommendation for `unconditioned_token_prior`

### Question (from Bundle v0.3 §VI #1)

"Drives baseline derivation" — should the value pool be visible in
the prompt shell?

### CS proposed recommendation: VALUE POOL VISIBLE in the prompt shell.

### Proposed shell structure (CS-side draft for NS refinement)

```text
<locked_header_text>

Available values: <flat list of the value pool for this rung, in
                   fixed rung-deterministic order to prevent ordering
                   shortcuts>

Q: <query format scaffold with the queried key absent (i.e., the
    "you have just been asked" wrapper but no key tokens)>
A: <model emits one value>
```

Key design choices:

- **Value pool visible.** The flat list of values is rendered. The
  control isolates "emission bias when bindings absent" from
  "vocabulary knowledge". Vocabulary is known to all; bindings are
  what's being tested.
- **Queried key absent.** Per T2 binding-handling rule.
- **Value bindings removed.** No key-value pairs anywhere in the
  shell.
- **Fixed rung-deterministic value-pool ordering.** Prevents an
  ordering shortcut (model emits "the first listed value"). CS
  proposes lexicographic order by token-id sequence (deterministic;
  cannot be tuned post-pilot).
- **Format-preserving.** The shell mirrors the answerable prompt
  format in every other respect.

### Baseline derivation (consequence of value pool visible)

Theoretical baseline: **1 / |value_pool|** (uniform expected emission
under no-bindings condition).

The locked T2 expected-baseline declaration becomes:

```text
expected_baseline = 1 / |value_pool_size|
   = 1 / N_values_per_rung
   (declared at packet lock; pre-pilot)
```

### Empirical validation (A5 pre-flight)

The **"ideal random emitter" oracle** in A5 pre-flight must score
within the locked tolerance of `1 / |value_pool|`. If the empirical
oracle score diverges materially from theoretical, that is itself a
finding about the value-pool design (potentially a frequency-prior
contamination), and the control is re-spec'd before lock.

### Why not "value pool removed"?

Removing the value pool would force the model to rely on real-world
frequency priors over whatever the value vocabulary maps to. The
baseline then becomes hard to specify precisely (depends on tokenizer
+ frequency priors); the control's "above-chance via surface/frequency
bias" detection lose its tractable null. CS rejects this option.

### Caveat noted at the recommendation level

If the model's tokenizer treats certain value tokens differently
(e.g., common English words tokenize differently than rare strings),
the baseline can drift from `1 / |value_pool|` even without bindings.
CS notes this as a packet-stage refinement: the actual baseline used
should be empirically validated against the "ideal random emitter"
oracle in A5 pre-flight, and any deviation from theoretical 1/|pool|
is documented in the T1 sealed table.

### CS implementation footprint (under D2 code authorization)

- The locked prompt-shell template is hashed into LOCK-RECORD via a
  new `control_prompt_shell_hash` field (extension to LOCK-RECORD
  v0.2 §2 `bound_hashes` at v0.3, if NS concurs).
- The expected_baseline field in T2 is populated with
  `1.0 / N_values_per_rung` at packet lock.
- The A5 ideal-random-emitter oracle test asserts the empirical score
  is within IS-7 drift tolerance of `1.0 / N_values_per_rung`.

### Open questions for NS

- Confirm the value pool size is rung-deterministic and stable across
  pilot and final manifests (anti-tuning constraint).
- Confirm the value-pool ordering rule (CS proposes lexicographic by
  token-id sequence). NS may prefer a different deterministic order.
- Confirm whether "format-preserving" includes the full
  answerable-prompt scaffold (including any system message) or only
  the query-and-answer block.

---

## 5. Unresolved disagreement between CS and NS

**NONE on the CS side.** CS files its proposed positions; NS picks up
for co-review. Any disagreement surfaces only after NS co-review,
which has not occurred at the timestamp of this document.

CS lists the open questions for NS at the end of each of §§1–4 above.
NS may endorse, refine, or counter-propose any of these in the
co-review pass.

---

## 6. Explicit confirmation: no code implementation begun

```text
No source file under any execution-side path has been created or
modified. Specifically:
  - No lane1a_prime_runner.py file exists.
  - No lane1a_prime_runner_wrapper.py file exists.
  - No manifest schema validator code exists.
  - No policy module source exists.
  - No control module source exists.
  - No analysis-script code exists.
  - No outcome-chooser code exists.
  - No test file exists.
  - No CI configuration changes.
No code implementation has begun under D2 prior to Team Lead filter
on these dispositions.
```

CS confirms.

---

## 7. Boundaries preserved

```text
No sweep execution.
No model runs.
No new sweep_id.
No data generation (in the model-output sense).
No code implementation begun.
No execution packet execution.
No offline pilot execution.
No oracle pre-flight execution.
No candidate selection.
No candidate ranking.
No threshold-sheet work.
No certification evaluation.
No stress-retention testing.
No B1 v2.1 implementation.
No Paper 3 revision.
No Claim C activation.
No Fork A reactivation.
No Paper 6 activation.
No public benchmark packaging.
No D3 / D4 / D5 implied or solicited.
```

All execution gates remain CLOSED.

---

## 8. CS posture

```text
INH-1 proposed disposition:           filed (§1; per-stratum N_effective
                                      table; CS schema implications;
                                      open question to NS)
INH-2 proposed disposition:           filed (§2; outcome enum; predicate;
                                      RFI behavior; inconclusive
                                      preempts; fixed-language
                                      constants; open questions to NS)
INH-3 proposed disposition:           filed (§3; Wilson score interval
                                      without continuity correction;
                                      single-CI-function invariant;
                                      open question to NS)
Prompt-shell visibility:              filed (§4; value pool visible;
                                      fixed lexicographic ordering;
                                      baseline = 1/|value_pool|;
                                      empirical validation in A5;
                                      open questions to NS)
Unresolved disagreement (CS vs. NS):  NONE on CS side at filing
                                      (NS co-review not yet occurred)
Code implementation:                   NOT STARTED
D2 work ordering:                      governance co-drafts in flight;
                                      code awaits Team Lead filter
                                      after NS co-review

Next:                                 NS co-reviews this document and
                                      either endorses, refines, or
                                      counter-proposes. Joint co-draft
                                      goes to Team Lead filter. On
                                      Team Lead PASS, CS proceeds to
                                      code implementation per the
                                      semantics-first ordering.

Lane 1a close-out v1.2 (parallel):    CLOSED-PENDING-ADOPTION
                                       (Senior owns)
All execution gates:                   CLOSED
```

— CS Engineer, 2026-06-11
