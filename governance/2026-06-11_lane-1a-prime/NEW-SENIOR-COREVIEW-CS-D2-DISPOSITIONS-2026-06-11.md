# New Senior Co-Review — CS D2 Proposed Dispositions

```text
DRAFT / REVIEW ONLY
D2 SEMANTIC CO-REVIEW ARTIFACT
NO CODE IMPLEMENTATION BEGUN
NO EXECUTION AUTHORIZED
NO SWEEP_ID CREATED
NO MODEL INVOKED
NO VALIDATION OUTPUTS POPULATED
```

To: Team Lead (filter), CS Engineer (co-owner) · Cc: Senior Engineer, Manager
From: New Senior Engineer · 2026-06-11
Reviewed: `CS-PROPOSED-DISPOSITIONS-INH-AND-PROMPT-SHELL-2026-06-11.md` (commit `acf73a3`, all 529
lines read from repo bytes). CS's filing is high quality — the INH-1 table, the Wilson analysis, and
the prompt-shell empirical-validation idea are better than my v0.2 sketches. One item draws a
counter-proposal because it collides with inherited locked vocabulary.

---

## 1. INH-1 — Per-diagnostic stratum semantics: **ENDORSE WITH TARGETED EDITS**

CS's per-metric table is complete and correct, including two rows mine lacked (`distinct_outputs`
over 96; `copy_completion` agreement over 96 — both right, since diversity and copy-resolvability
are properties of the whole rung). Answers to the four review questions: (1) stratum-specific
N_effective as default — endorsed, with CS's type-level enforcement
(`stratum: Literal[...]`, no default argument) as the right mechanism. (2) Pooled N=96 diagnostics:
only `distinct_outputs`, `copy_completion` agreement, and void accounting; I plan no others — the
table is complete at v0.2, answering CS's open question. (3) Mapping complete — confirmed against
Bundle v0.3 Part II/IV row by row. (4) Targeted edit, add one sentence to the T1 plan:

> **Accuracy and abstention metrics are forbidden from cross-stratum aggregation.** No declared
> exception exists at packet stage; any future exception is a must-fix requiring C1 disposition.

Rationale: the type system enforces it in code; the sentence enforces it in governance, so the rule
survives any future reimplementation.

## 2. INH-2 — Outcome-chooser totality: **COUNTER-PROPOSE** (two axes) + one targeted edit

What I endorse first, because most of CS's structure is right: the closed enum concept; **no
`passes_*` value** with the source-level grep test (structural enforcement of the doctrine);
hard-Boolean predicate; INCONCLUSIVE preempting; structural fixed-language emission with the
constants hashed into the LOCK-RECORD. The three fixed statements are substantively correct,
including every non-claim.

**Counter-proposal axis 1 — label naming.** The `CLEARLY_FAILS_*` serialized strings
(`"clearly_fails_token_prior_separation"` etc.) collide with the Manager's original Lane 1a §5
prohibition on fails-shaped, gate-verdict-shaped label vocabulary, and with the inherited
seven-descriptive-label vocabulary carried by R6 into Design Packet I.7. The v1 standing-rule's own
`clearly_fails_D*` phrasing was flagged in review as inconsistent with the controlling §5; we should
not import that inconsistency into code. Exact replacement — the wire/artifact label strings are the
descriptive forms:

```text
accuracy_indistinguishable_from_token_prior
accuracy_indistinguishable_from_declared_policy_envelope
insufficient_measurement_headroom
strict_content_gap_instability
null_abstention_floor_unmet
answerable_abstention_ceiling_exceeded
```

(The last two are the v1 `abstention_contract_instability` label correctly split into the two
re-formed criteria — CS's six-criterion set matches T3 exactly; confirmed complete, answering review
question 5.) Internal enum member names are CS's choice, but serialized values, schema enums,
sidecars, and fixed language carry only descriptive strings: no `fails` token in any output
artifact.

**Counter-proposal axis 2 — RFI is the non-eliminated state, not a fourth tier.** CS proposes RFI
("uncertain zone") as distinct from NON_ELIMINATED, excluded from K. This breaks inherited v1 §1.6
semantics, where `requires_further_investigation` attaches iff no other label attaches and means
exactly "not ruled out under this sweep." Three concrete failures of the four-tier version: (a) it
creates a two-tier gradation inside the survivor set — "cleanly non-eliminated" vs "uncertain" is an
implicit ranking, which is the rule-in smell the doctrine's unordered-set rule exists to prevent;
(b) it makes the fixed language self-contradictory: the K=0 statement ("no rung was non-eliminated…
reconnaissance-negative finding") could emit while rungs sit flagged *requires further
investigation* — the lane would declare the question answered and unanswered simultaneously;
(c) "flagged for re-execution" as an output behavior edges toward road-to-winner; re-execution is a
Manager-authorization question, not a lane output. Exact replacement:

```text
Outcome totality (three-way): INCONCLUSIVE | ELIMINATED | NOT_RULED_OUT.
ELIMINATED carries one or more attached descriptive elimination labels.
NOT_RULED_OUT serializes the inherited label string requires_further_investigation;
  it fires iff the rung is measurable and no elimination label attached.
labels(rung) == {requires_further_investigation}  ⇔  outcome NOT_RULED_OUT.
K = |{rung : outcome == NOT_RULED_OUT}|.
Fixed language binds K to "not ruled out" (substitute that token for
"non-eliminated" in the three constants; all non-claims unchanged).
```

CS's genuine contribution here — boundary-proximity visibility — is preserved without a tier:

```text
boundary_proximity_flag: per-criterion diagnostic field in the per-rung record,
  set when a measurement falls within the criterion's pre-declared proximity zone.
Diagnostic-only and non-eliminating; excluded from outcome determination, from K,
  and from all fixed language; reported in the diagnostics appendix only.
No elimination label, outcome, or statement may reference it.
```

This answers review questions 1–2 in their corrected form: the closed enum is endorsed restructured
to three outcomes plus label attachments; "RFI excluded from K unless it is the sole label" becomes,
under restored semantics, precisely the equality predicate — RFI-as-sole-label *is* K membership.

**Targeted edit — INCONCLUSIVE triggers.** CS's trigger list mixes evaluation-time failures with
lock-blocking conditions. Unresolved pilot-log failures, manifest-validation failure, and A6 drift
exceedance are pre-lock events: under addendum C1/C3 they **block lock** — no rung is ever evaluated
under them, so they cannot be rung outcomes. Keep as evaluation-time INCONCLUSIVE triggers (per
inherited v1 §1.6): void budget exceeded; required policy/control outputs missing from the sidecar;
harness anomaly. Move the other three to the lock-blocking list in the same section.

## 3. INH-3 — SE interval method: **ENDORSE**

(1) Wilson without continuity correction — endorsed. (2) I do not prefer the continuity-corrected
form: CC's extra conservatism widens intervals, and in a negative-use instrument wider intervals
near boundaries can *increase* elimination of good behavior — conservatism is not free here; CS's
method table is correct that standard Wilson's coverage is adequate at our N. (3) Jeffreys remains
fallback only. (4) Newcombe–Wilson for the token-prior separation difference — endorsed (it is the
Wilson-consistent difference interval). (5) Ideal-witness boundary check, computed: at the ideal
NULL corner (p̂ = 16/16), Wilson 95% ≈ [0.806, 1.000] — nonzero width, contains 1.0, no Wald SE=0
zero-width pathology; the v1 corner failure cannot recur in interval form. CS's single-CI-function
invariant with the grep test is exactly right. One declaration to add at packet stage (not a blocker
now): each T3 criterion states whether it compares the **point estimate** or a **CI bound** against
its declared floor/ceiling — the interval method is settled, the comparison rule must be equally
explicit before lock.

## 4. Prompt-shell visibility: **ENDORSE WITH TARGETED EDITS** (convergent with my §1 proposal)

CS and I filed the same recommendation independently — pool-visible — and CS's version is stronger
on two points I adopt: the **ideal-random-emitter oracle** empirically validating the theoretical
baseline in A5 (divergence is itself a finding about pool design), and the
**`control_prompt_shell_hash`** LOCK-RECORD extension, to which I concur at v0.3. Answers: (1)
pool-visible endorsed. (2) The value pool is **global** (single VALUE_POOL, |pool| = 26, constant
across rungs), so rung-determinism holds trivially; stability across pilot and final manifests is
confirmed as an anti-tuning constraint — targeted edit: state the global-pool fact explicitly in the
shell spec so "per-rung" language doesn't imply per-rung pools. (3) Token-id-sequence lexicographic
ordering endorsed, with one requirement: the tokenizer and canonicalization are the **same** ones
declared for the `prefix_neighbor_confusion` equality predicate, identified by name and version in
T1 — one canonicalization for the whole packet. The fixed global order also means no per-item
position leak: the list is identical in every prompt, so "emit the first listed value" is itself a
detectable constant policy, not a shortcut. (4) "Format-preserving" defined: the locked header, the
instruction block, the format contract, and the Q/A scaffold are byte-identical to the answerable
prompt; exactly one substitution — the key-value pairs block is replaced by the `Available values:`
flat list; the queried key is absent from the Q scaffold. (5) Standing taxonomy satisfied:
format-conditioned (full scaffold present) but binding-free (zero task-relevant bindings). (6)
Baseline derivable, not assumed: 1/|pool| from declared semantics, then empirically checked against
the ideal-random-emitter oracle within IS-7 tolerance — derivation plus verification, which is
stronger than either alone.

## 5. Unresolved disagreement with CS

None expected to persist: the INH-2 counter-proposal restores inherited semantics CS did not have in
front of it as a constraint, and CS's design value (boundary visibility, structural enforcement,
fixed constants) survives intact inside the three-way form. If CS holds that the uncertain zone must
be an outcome tier rather than a diagnostic field, that single question goes to Team Lead as the one
genuine disagreement; everything else is convergent.

## 6. Boundary question — preserved

The §9/§9a question stands unchanged: D2 model-free validation scope awaits the Manager's filed
confirmation. Until then this seat continues holding on pilot manifest construction, oracle
pre-flight execution, deterministic policy execution, A6 re-verification, and validation result
population. This co-review is semantic work only.

## 7. Confirmations (required items 7–10)

No code implementation began. No validation execution occurred. No sweep_id was created. No model
was invoked.

— New Senior Engineer (to Team Lead for filter of the joint disposition set)
