# CS D2 Work-Start Acknowledgement — Lane 1a′

From: CS Engineer
To: Manager
Cc: Team Lead, New Senior Engineer, Senior Engineer, Contributor 5, Contributor 6
Date: 2026-06-11
Re: D2 packet-preparation / validation-packet authorization received; CS work-start acknowledgement
Status: D2 acknowledged; CS scope confirmed; no sweep execution; no sweep_id; no model runs

---

## 1. Acknowledgement

```text
D2 acknowledged.
D2 = packet-preparation / validation-packet authorization (NOT sweep
     execution; NOT model runs; NOT new sweep_id creation).
D3, D4, D5 not granted; CS does not solicit D3 from D2.
The unconditioned_token_prior control remains closed for model
     generation; opens by-name at D4 only or not at all.
```

## 2. CS scope under D2 — what is authorized

Authorized work CS may now perform:

| Class | Activity | Notes |
|---|---|---|
| **Code** | Implement `lane1a_prime_runner.py` and `lane1a_prime_runner_wrapper.py` modules per CS-EP v0.2 §3 | Writing the runner/wrapper source is design work; the modules cannot be invoked against a model under D2. |
| **Code** | Implement manifest schema validator per CS-EP v0.2 §4 | Closed type system; deterministic. |
| **Code** | Implement policy modules (`pure_last_position`, `salient_endpoint`, `recency_excluding_target`, `prefix_neighbor_confusion`, `copy_completion`) per CS-EP v0.2 §6 | Deterministic; no model required. |
| **Code** | Implement control modules (`unconditioned_token_prior`, `scrambled_binding_retrieval`) per CS-EP v0.2 §7 with the **DE-2 typed boundary**, **AL-Q2-schema enum constraints**, and **diagnostic-sidecar emission** | The control modules' code lands at D2; their **invocation** does not (requires model). |
| **Code** | Implement `render_prompt()` + `--dry-run` per CS-EP v0.2 §3.1 (AL-Q1) | Pure-function; no model. |
| **Code** | Implement diagnostic-sidecar pattern per CS-EP v0.2 §5.1 (AL-Q4) | No model required. |
| **Code** | Implement A6 `a6_final_manifest_reverification()` function per CS-EP v0.2 §8 | Deterministic; no model required. Tolerance values come from T1 declared-caps block (IS-7). |
| **Code** | Implement `lock_packet()` IS-8 hard refusal per CS-EP v0.2 §9 | Deterministic; no model required. |
| **Code** | Implement all CS-EP §15 tests | Production-path subprocess smoke; sibling-artifact cross-reference; policy zero-self-match; control no-elimination-reference; drift-tolerance; operation-equivalence lock-time refusal; label-presence; audit-log append-only; assembly dry-run; schema rejection; diagnostic-sidecar disjointness. |
| **Offline validation** | Construct pilot manifests under the locked recipe (per Bundle v0.3 §I.3) | Deterministic seeds; offline; no model. |
| **Offline validation** | Execute the policy battery (A1) against pilot manifests | Deterministic; no model. |
| **Offline validation** | Execute the policy battery against synthetic oracle cases (A5 pre-flight) | Deterministic; no model. **Excludes** the oracle case "token-prior emitter" — that oracle is constructed synthetically (a declared shortcut output) and executed offline against the policies, NOT a model invocation. |
| **Offline validation** | Compute A6 final-manifest re-verification once final manifests exist | Final manifests are constructed under the locked recipe; this is deterministic; no model. |
| **Co-drafting (NS + CS)** | INH-1 disposition (per-diagnostic stratum semantics) | CS implementation footprint: `manifest_record.stratum` field + per-stratum aggregation in analysis script. |
| **Co-drafting (NS + CS)** | INH-2 disposition (outcome-chooser totality + fixed language) | CS implementation footprint: outcome-chooser code; fixed-language emission as typed-string constant. |
| **Co-drafting (NS + CS)** | INH-3 disposition (SE interval method) | Wilson is **proposal, not selection** under D1/D2; CS implements whichever method is selected. |
| **Co-drafting (NS + CS)** | Prompt-shell visibility recommendation for `unconditioned_token_prior` | Drives T2 expected-baseline derivation. Recommendation only; no model invocation under D2. |
| **Refinement** | Update CS-EP and LOCK-RECORD to v0.3 once NS T1/T2/T3 plans concretize | Schema fields, MODEL_ID, PRODUCTION_PYTHON, EXPECTED_MLX_LM_VERSION can be locked once NS plans are stable. |
| **Refinement** | Update Packet-Stage Concern Register as items resolve | Move OPEN-at-D2 items to RESOLVED as dispositions land. |
| **Population** | Populate T4 disposition table with packet-stage review dispositions (governance records, not validation outputs) | Per Bundle v0.3 §V; INH-1/2/3 are CS+NS-owned. |
| **Sealing prep** | LOCK-RECORD `bound_hashes` populated for code artifacts as they reach hash-stable state | No `sweep_id`; no SEALED state; LOCK-RECORD remains PENDING. |

## 3. CS scope under D2 — what is NOT authorized

Specifically prohibited under D2 (per Manager §3 + §4 + §5):

```text
- Sweep execution.
- Model runs (i.e., invoking the runner with the production interpreter against a real model).
- New sweep_id creation (LOCK-RECORD §2 identity.sweep_id remains
  <placeholder; NOT CREATED UNDER D2>).
- unconditioned_token_prior control invocation against any model (requires
  D4 by-name authorization that is not granted here).
- scrambled_binding_retrieval control invocation against any model
  (also requires model; not authorized under D2; in any case the
  output cannot reach an elimination label by DE-2 typed boundary
  + AL-Q2-schema enforcement).
- Candidate selection / ranking / threshold-sheet work / certification
  evaluation (full standing non-authorizations list).
- Any artifact mutation of locked sibling artifacts (B1 v2 source,
  Paper 3 v1.1 release bytes, tier0-run/).
- Anything that would populate sweep outputs labeled
  "RECONNAISSANCE — NON-BINDING — NOT FOR THRESHOLD DERIVATION"
  with real model-generated content.
- Sealing the LOCK-RECORD (requires D3 / D4 preconditions).
```

CS will not invoke a model under D2.
CS will not create a sweep_id under D2.
CS will not seal the LOCK-RECORD under D2.

## 4. CS deliverable plan (proposed order; awaits user direction)

The Manager §6 required-return list has 12 items spanning NS-owned, CS-owned, and joint work. CS proposes the following sequence for CS-owned items, subject to user direction:

| Order | CS deliverable | Status | Depends on |
|---|---|---|---|
| 1 | INH-1, INH-2 disposition co-drafts with NS | NOT STARTED | NS Bundle v0.3 §V + CS analysis-script footprint |
| 2 | INH-3 disposition co-draft with NS (SE interval method recommendation) | NOT STARTED | INH-1/2 dispositions inform statistical framing |
| 3 | Prompt-shell visibility recommendation co-draft with NS | NOT STARTED | NS T2 plan + CS-EP §4 manifest interface |
| 4 | Implement code (runner, wrapper, schema, policy modules, control modules, A6, lock_packet, tests) | NOT STARTED | NS T1/T2/T3 plans + INH dispositions |
| 5 | Construct pilot manifests under locked recipe | NOT STARTED | Code from #4 + locked recipe from NS design packet |
| 6 | Execute policy battery against pilot manifests (A1) | NOT STARTED | #5 |
| 7 | Execute policy battery against synthetic oracle cases (A5 pre-flight) | NOT STARTED | #5 |
| 8 | Compute A6 final-manifest re-verification (once final manifests exist) | NOT STARTED | #5, #6, #7; final-manifest construction |
| 9 | Update CS-EP and LOCK-RECORD to v0.3 with concrete values | NOT STARTED | All above |
| 10 | Update Packet-Stage Concern Register to RESOLVED status for items as they close | ONGOING | Items 1-9 |
| 11 | CS contribution to D2 packet-stage completion bundle return | NOT STARTED | All above |

Items 1-3 (joint co-drafts) are the natural starting point and do not
require code. CS holds for user direction on whether to begin with
the co-drafts or with code, and on coordination cadence with NS.

## 5. Coordination items with New Senior

CS will need from NS in roughly this order:

1. **INH-1/2 disposition framing** (per-stratum semantics; outcome-chooser totality + fixed language) — joint co-draft starting from NS Bundle v0.3 Part V.
2. **INH-3 SE interval method choice** (Wilson proposed; NS confirms or proposes other) — joint co-draft.
3. **Prompt-shell visibility for `unconditioned_token_prior`** — joint co-draft.
4. **T1 declared-cap values + statistical rationale** (per-policy accuracy cap; union-envelope cap; drift tolerance per IS-7) — NS declares; CS verifies pre-pilot timestamp at seal.
5. **T2 control-spec field-level finalization** — NS prepares; CS conforms in code.
6. **T3 ideal-witness record format finalization** — NS prepares; CS reserves test class in §15.
7. **Manifest recipe locked-form** (padding placement; novelty rule; deterministic seeds; per-rung void budget; per-item answer-slot recording) — NS finalizes; CS implements in code.
8. **Final N + answerable/NULL split + void budget** — NS confirms at packet validation; CS implements.

## 6. Standing-governance compliance under D2

CS will continue to operate under all standing rules:

- Pre-Lock Instrument Validation Addendum (`governance/standing/`)
- R6 requirement-inheritance check
- Path Conventions rule (`governance/<date>_<lane>/` + `governance/standing/`)
- G1-open production rule (no production cycle while a condition memo affecting it is G1-open)
- Sibling-artifact cross-reference rule (concrete-value tests against locked siblings)
- Production-path subprocess smoke test rule (production interpreter pin + import smoke before any subprocess invocation)
- "Supersede, don't rewrite" governance rule
- Standing review-discipline rules (failure-mode prompt; protection-layer taxonomy)

## 7. Boundaries preserved

```text
No sweep execution.
No model runs.
No new sweep_id.
No data generation (in the model-output sense).
No execution packet execution.
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
No D3 / D4 / D5 implied or solicited by D2 work.
```

Offline validation work CS performs under D2 (pilot manifest
construction; policy battery execution against pilot manifests and
oracle cases; A6 re-verification on final manifests) **does not
constitute sweep execution and does not require a sweep_id**. These
are pre-lock instrument-validation activities per the addendum, all
offline and deterministic.

All non-Lane-1a′ execution gates remain CLOSED.

## 8. CS posture

```text
Lane 1a' D2 packet-preparation /
  validation-packet authorization:    APPROVED (Manager, 2026-06-11)
CS-owned D2 package artifacts:        landed at commit b55bc85
  - CS-EP v0.2; LOCK-RECORD v0.2; Non-Auth Language v0.2;
    Packet-Stage Concern Register v0.1; CS D2 Package Assembly Summary

CS scope under D2:                    confirmed (§2 above)
CS prohibitions under D2:              confirmed (§3 above)
CS coordination items with NS:         confirmed (§5 above)

CS next action:                       holds for user direction on whether
                                       to begin with:
                                       (a) INH-1/2/3 + prompt-shell joint
                                           co-drafts with NS (no code; pure
                                           governance work), OR
                                       (b) CS-side code implementation
                                           (runner, schema, policies, etc.)
                                           in parallel with NS plan
                                           refinement, OR
                                       (c) some other ordering

Lane 1a close-out v1.2 (parallel):    CLOSED-PENDING-ADOPTION
                                       (Senior owns)

All execution gates:                   CLOSED
```

CS holds for explicit user direction on the first D2 deliverable.

— CS Engineer, 2026-06-11
