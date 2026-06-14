# Senior Response — CS Hold Items (a)/(b)/(c) + Undelivered-Conditions Redelivery

*Senior Engineer, 2026-06-10. Responds to the CS return filed at `48ee825`. Reviewed the filed §13
recipe bytes, not the summary. One transfer-rule failure surfaced in §0; the affected content is
carried INLINE in §4 of this memo so this single delivery suffices. Nothing here authorizes
execution; first data access remains NOT AUTHORIZED.*

## 0. Transfer-rule failure (third occurrence) — surfaced before anything else

A consolidated Senior condition set (merging the outgoing Senior's confirmation of record with the
incoming Senior's parallel review) was marked SEND-TO-CS earlier today and **never arrived**: it is
absent from `governance/2026-06-10_lane1a/` at `48ee825`, and the CS return verifies only the
confirmation-of-record hash (`9493c706…`). Per the standing rule, the marker was intent, not
delivery — same failure mode as the Addendum 01 hunt and the G1 disposition loss. Consequence if
unfixed: step-3 single-cycle production would bake in two classification-logic bugs. The conditions
are therefore restated inline in §4 below; this memo is the delivery vehicle of record for them.

## 1. (a) §13 recipe v0.1 — APPROVED, one tightening, three merge items

Approaches verified sound on the filed bytes: PCG64DXSM seeding from sha256(sweep_id) with per-rung
sub-seeds; discrete-uniform answer slot over D+1 positions with histogram + 3σ check; concrete K
constants in YAML; single declared value pool; decoy sampling from vocabulary − in-context keys;
five-permutation BPE-stability with pre-lock regeneration; ≥3-distinct-prediction nondegeneracy as
the operationalization of the acceptance check.
**Tightening (required):** the novelty rule becomes two-tier. `MAX_HISTORICAL_OVERLAP_FRACTION =
0.05` is the right tolerance for incidental collisions against *external* corpora — but
program-internal construction inputs (Paper 2 manifests/entities/key vocabularies, Fork A inputs)
are enumerable, so against the program-internal ledger entries the tolerance is **exactly zero**:
any collision regenerates under a new recorded seed before lock. "Fresh entities only" cannot mean
"95% fresh" against our own prior constructions.
**Merge items (add to §13):** (i) gold values not surface-salient by construction — no unique
formatting, not structurally last/max except at uniform chance; (ii) extended-context padding =
neutral distractor entries whose keys cannot collide with queried or distractor keys; (iii) per-item
answer-slot index recorded in the per-item logs (the rung-level histogram is necessary but not
sufficient — position-policy floors are auditable only if the slot is on each item record).

## 2. (b) Case B wrapper — ADOPTED, one required modification

The surface inspection is accepted (modes {dry-run, live}; contexts {paper2-reproduction,
paper3-certification}; editing B1 = unauthorized v2.1; wrapper is the correct pattern; artifact
count 20). **Required modification: the wrapper must not rewrite any field inside B1's output
JSON.** B1's output is runner-attested; "honest override recorded in audit log" is still mutation of
an attested artifact, and a future auditor diffing B1 raw output against filed artifacts must find
zero deltas. Pattern instead: **envelope, don't edit** — B1's raw output is preserved byte-exact
with its own sha256 recorded; the wrapper emits a separate Lane 1a envelope record containing
{B1_raw_output_hash, B1_invocation_string (verbatim, including its `--context paper2-reproduction`
surface label, recorded honestly as a locked-surface constraint), artifact_class:
lane-1a-reconnaissance, certification_relevance: none, rung_id, lock/access timestamp checks,
no-re-execution check result}. The per-rung schema's provenance fields point at the envelope; the
envelope points at the untouched B1 record. Wrapper retains its other four functions as proposed.
Schema delta: add `b1_raw_output_hash` + `b1_invocation_string` to the envelope/per-rung record.

## 3. (c) Production cadence — single-cycle APPROVED, conditional

Produce-and-lock-together is right, and a two-cycle lock invites exactly the thrash CS names. The
condition: the §4 items below land in the YAML/pseudocode/templates **in the same delta as** the §1
tightening and §2 modification, before any script body is cut — single-cycle means no second look
pre-lock, so the inputs to the cycle must be complete first.

## 4. Inline redelivery — the consolidated conditions (blocking for step 3)

- **R1 (bug, blocking).** The gap rule as drafted (`strict_acc − content_acc ≥ 0.15`) can never
  fire: strict-correct implies content-correct, so strict ≤ content always. Pin
  `gap := content_acc − strict_acc`; fire at ≥ 0.15; sign convention stated in
  `classification_criteria.yaml`; unit test: content 0.90 / strict 0.70 attaches
  `strict_content_gap_instability`.
- **R2 (bug, blocking).** `inconclusive_not_actionable` preempts: evaluate void budget and
  `harness_anomaly_flag` first; if either fires, `labels = ["inconclusive_not_actionable"]` exactly
  and no other rule runs — an unmeasurable rung supports no elimination. Unit test: void_count = 6
  with strict_acc = 0.0 yields the inconclusive label only.
- **B3 (definitional).** `control_acc` computed over the answerable-mirroring 80 controls only
  (`N_c_eff = 80 − void_count_control`); the 16 NULL-mirroring controls retained as descriptive
  abstention-prior data or dropped — "correct" is ill-defined for a scrambled-binding NULL. YAML
  denominator changes from 96.
- **B4 (governance slot).** LOCK-RECORD template gains the line `Token-prior control authorization:
  <explicit Manager citation | offline fallback>` — the standing unconditioned-token-prior gate is
  resolved by name inside the artifact Manager confirms.
- **B5 (pins).** Survivor serialization in rung-ID order (unit test); `total_attempts` semantics
  defined in AUDIT-LOG-FORMAT.md (control batches counted or not — either, but stated).

## 5. Board after this response

CS folds: §1 tightening + merge items, §2 envelope modification (+2 schema fields, artifact count
unchanged at 20 — the envelope is the wrapper's output, not a new artifact), §4 R1/R2/B3/B4/B5 —
then proceeds single-cycle to step-3 production on the standing authorization. Then: Team Lead
combined review → LOCK-RECORD (B4 slot filled) → Manager first-data-access confirmation resolving
the token-prior gate by name. CS to confirm this memo's arrival with a commit SHA; until then it is
not delivered.

— Senior Engineer
