# Lane 1a' Prime — Path A Run Return (v0.1)

```text
SYNTHETIC / DIAGNOSTIC — NON-BINDING — NOT FOR THRESHOLD DERIVATION
PATH A L01–L08 OPERATIONAL PILOT — EXECUTED 2026-06-12
PER-RUNG ADJUDICATION; NO CROSS-RUNG AGGREGATION; NO COMPOSITE SCORE; NO SURVIVAL COUNT
SEALED LOCK-RECORD v1.0 UNCHANGED · D4-A AND D4-B RUN-OF-RECORD UNMUTATED
TP CRITERION ACTIVE BY MANAGER DECISION · ALL EMITTED REPORTS CARRY TP FIELDS
```

To: Manager (decision) · Cc: Team Lead, New Senior Engineer, Senior Engineer, Contributor 5
From: CS Engineer
Date: 2026-06-12
Re: Manager §8 31-item return — Path A L01–L08 token-prior-active pilot

Path A executed under Manager Path A authorization (2026-06-12; all
four boxes approved). All Manager-required preconditions PASSED at
runtime. 1,536 inferences completed (8 rungs × 96 candidates × 2
sweeps). Each of the eight rungs adjudicated **separately** under the
full six-criterion set; eight rung-local bounded results, none
aggregating into anything.

**Critical language constraint (per Manager §5, NS OC3 guard, and
Synthesis v0.3 §5 repetition guard):** the eight per-rung outcomes
**do not aggregate**. They are not "8/8 survived." They are not
"robust." They are eight rung-local bounded sentences, each saying
only what is locally true on that rung's narrow surface.

---

## §1. Candidate sweep_id

```text
lane1a-prime-pathA-cand-20260612-003538-v4uva6
```

## §2. TP control sweep_id

```text
lane1a-prime-pathA-tp-20260612-003538-hdo9fu
```

Both stamped into every Path A artifact (pre_flight_log,
execution_ledger, per-record outputs).

## §3. Commit SHA

Recorded after this commit lands; reported in CS delivery message.

(Prior HEAD: `055c61b52464572d44a023e9fadcc1b0da627ea6` — the commit
containing the STANDARD-RETURN-TEMPLATE-v1.0 + delivery.)

## §4. Model identity

```text
Family:    Qwen2.5
Variant:   Qwen2.5-3B-Instruct
Precision: bf16 (unquantized; mlx native)
```

(Same model as D4-A / D4-B.)

## §5. Model snapshot / revision hash

| field | value |
|---|---|
| Authorized canonical | `sha256:abee745b7dfe399d9254dbcdea5e3e3902aa95d71a31989b7b720b7ac9907b20` |
| Computed at runtime (B1 v2 routine) | `sha256:abee745b7dfe399d9254dbcdea5e3e3902aa95d71a31989b7b720b7ac9907b20` |
| Match | **YES — exact** |

## §6. Local model hash / provenance

```text
HF snapshot dir: ~/.cache/huggingface/hub/models--Qwen--Qwen2.5-3B-Instruct/
                  snapshots/aa8e72537993ba99e69dfaafa59ed015b17504d1/
Same canonical Paper 2 / B1 v2 / D4-A / D4-B snapshot. No re-staging.
```

## §7. Runner path and sha256

| field | value |
|---|---|
| Runner path | `experiments/2026-06-11_lane-1a-prime/d4_runner/lane1a_runner_path_a.py` |
| sha256 | `9ce0f9bdd903cfb19a52ea3f30a738f85de13511a476af9393a68d47d652717a` |

Supporting files:

| file | sha256 |
|---|---|
| `d4_runner/preconditions_path_a.json` | `59f61465fc915ecd0c9a412eeb183ce6f5e70c04aae7d3bc5aa875136c069fa2` |
| `d4_runner/prompt_template_v1.json` (candidate retrieval-shell) | `f1956e7dd43f165c8707fe88bc11757888f108e7e9766aa186ac9fc04f8b368a` |
| `d4_runner/prompt_template_v1_tp.json` (TP no-bindings shell) | `af55f9757005c6cd7c1baa1c77852d4a4bb596f185ceaccfb875ad29f3108615` |
| `d4_runner/decoding_config.json` | `a20391d89972d47c0b231f5c6da9f8a9f4c7be8c975ab98bd95a32327196f803` |
| `d4_runner/parse_model_output.py` | `fbdf989cdb8f258b7b2e18000835aafd9814a195b3eae0d73f540c08d35a1180` |

## §8. Generator path and sha256

| field | value |
|---|---|
| Generator path | `experiments/2026-06-11_lane-1a-prime/lane1a_prime/validation.py` |
| sha256 | `db69519fe84396e7854f80460b41b60c7aeb1ef06948171b7fd91b4c1860bcac` |

Matches the Manager-authorized generator pin verbatim. Generator hash
mismatch abort armed; did not fire.

## §9. Framework version

```text
Authorization pin: mlx_lm 0.31.3 (Option A carryforward from D4-A)
Actual installed:  mlx_lm 0.31.3
Match:             YES
```

## §10. Decoding config

```json
{
  "temperature": 0.0,
  "top_p": 1.0,
  "top_k": -1,
  "repetition_penalty": 1.0,
  "max_new_tokens": 32,
  "seed": 0,
  "greedy": true
}
```

Single greedy pass per record per sweep. No retries.

## §11. Output directory

```text
experiments/2026-06-11_lane-1a-prime/path_a_run/
```

Sealed `validation/` directory **NOT touched** — verified by
before/after snapshot inventory of sealed directory file hashes
(ledger field `no_sealed_byte_change: CONFIRMED`). `d4_a_pilot/` and
`d4_b_pilot/` also untouched.

## §12. L01 sealed manifest path and hash

```text
path:   experiments/2026-06-11_lane-1a-prime/validation/pilot_manifests_L01.json
        experiments/2026-06-11_lane-1a-prime/validation/final_manifests_L01.json
sha256: afe0e545c318132a5821e6d02ba3f41093c05ce7a2623a120d0088e03b29b09f (both)
```

Sealed L01 manifests consumed read-only. Hash re-verified at runtime
against the sealed-time value; no regeneration occurred.

## §13. L02–L08 materialized manifest paths and hashes

Each rung materialized under `path_a_run/manifests/<rung>/` using the
approved generator (`db69519f…`) and locked seed (`0`). Per Manager
§4, pilot and final must match byte-for-byte (PH5-3 identical-seed
property). **All seven matched.**

| Rung | pilot sha256 | final sha256 | pilot == final |
|---|---|---|---|
| L01 (sealed; not regenerated) | `afe0e545c318132a5821e6d02ba3f41093c05ce7a2623a120d0088e03b29b09f` | `afe0e545c318132a5821e6d02ba3f41093c05ce7a2623a120d0088e03b29b09f` | ✓ |
| L02 | `068f0a9ac9e005cf…` | `068f0a9ac9e005cf…` | ✓ |
| L03 | `b4110a2851d2ad5c…` | `b4110a2851d2ad5c…` | ✓ |
| L04 | `02e528e65d7dd492…` | `02e528e65d7dd492…` | ✓ |
| L05 | `bb8c60979112741a…` | `bb8c60979112741a…` | ✓ |
| L06 | `2dc44b6072015539…` | `2dc44b6072015539…` | ✓ |
| L07 | `94b70ce3b880e13a…` | `94b70ce3b880e13a…` | ✓ |
| L08 | `3aa32862f1cf8a69…` | `3aa32862f1cf8a69…` | ✓ |

Full sha256s recorded in
`path_a_run/manifest_hash_record.json` (sha256 `5b000c969a8da5a4…`).
Per-rung recipe-conformance check (80 answerable + 16 NULL per rung)
passed on all seven materialized rungs; conformance abort did not fire.

## §14. Pilot/final manifest comparison results

```text
All eight rungs: pilot manifest byte-identical to final manifest.
PH5-3 identical-seed property verified for L01 (sealed) and for
L02-L08 (newly materialized).
No pilot/final mismatch abort fired.
No A6 drift (drift = 0 by construction on every rung).
```

## §15. Raw candidate output paths and hashes

96 per-record JSON files per rung × 8 rungs = 768 raw candidate
outputs, organized under
`experiments/2026-06-11_lane-1a-prime/path_a_run/<rung>/candidate_outputs/`.

Consolidated per-rung candidate predictions:

| Rung | candidate_predictions.json sha256 |
|---|---|
| L01 | `ba276b0539a4e7eed6662ea586c94aa0adc6a54ecaa92a0fd5c6540b3d170b76` |
| L02 | `6d3e090bc47f16a93b2a398056122427…` |
| L03 | `1c87227851e99373b61a1067030c2fe4…` |
| L04 | `3c7e7991317227c625cefd68c4cc5996…` |
| L05 | `6dfaf2ce1f9f1eaf7dd5feab452bfaa2…` |
| L06 | `23efca0d800166489c29411e78f4dd07…` |
| L07 | `3298de5bb983a17b5e7b62c454ec2f16…` |
| L08 | `baff792238295d20a7daeb1de2add26b…` |

(L01's candidate_predictions.json sha matches D4-B's L01 candidate
predictions sha256 — the model is deterministic at temperature 0 on
the same prompts and same sealed manifests.)

## §16. TP control output paths and hashes

96 per-record JSON files per rung × 8 rungs = 768 TP control outputs,
organized under
`experiments/2026-06-11_lane-1a-prime/path_a_run/<rung>/tp_control_outputs/`.

Consolidated per-rung TP control predictions:

| Rung | tp_control_predictions.json sha256 |
|---|---|
| L01 | `3bc7621c7b0bddf142f74b122e5f01259393e1bbb74850e2d741630cac110ee6` |
| L02 | `c5a048b1acaa02e7ef146ba520c3a9a4…` |
| L03 | `c4452cf82bc3e5ed276de5ac3487fcfe…` |
| L04 | `1051f297446b4b7f064765a98b6ae698…` |
| L05 | `455f5176d8913e2ceb3f983433f91001…` |
| L06 | `5f6485a01713b7048f0ad471c495e336…` |
| L07 | `91f1b6e4c86461a789918bc452a98cd8…` |
| L08 | `efc10230b00c76eabf4c1cc7d6e2f928…` |

(L01's TP predictions sha matches D4-B's L01 TP predictions —
deterministic at temperature 0 on same no-bindings prompts. Note: per
the readiness packet, the L01 TP control here is **measured fresh in
Path A** as a control artifact for Path A's per-rung adjudication; it
is not "reused" from D4-B in any evidentiary sense, even though the
bytes happen to be identical.)

## §17. Execution ledger path and hash

| field | value |
|---|---|
| Path | `experiments/2026-06-11_lane-1a-prime/path_a_run/execution_ledger.json` |
| sha256 | `af64ab10e6e97d338f4d97c61345169ff8333f73fe53adce5a4a829628135b8a` |

The ledger carries the ACTIVE TP banner at top, both sweep_ids, the
generator path + hash, all eight per-rung manifest hashes (pilot +
final), per-rung outcomes, runner hash, full provenance chain, and
the `no_sealed_byte_change: CONFIRMED` field.

## §18. Per-rung result artifacts and hashes

Per-rung T3 reports (each carries the ACTIVE TP banner, per-rung
six-criterion evaluation, per-rung outcome, per-rung
candidate_vs_tp_comparison block):

| Rung | t3_report.json sha256 |
|---|---|
| L01 | `af0d79be39ab23210f3e578f0dd148d9…` |
| L02 | `da60e8f9c51483abec6ad8dcd1e7bfbc…` |
| L03 | `62c9a8f5f9ec250165f212bca9556f34…` |
| L04 | `ed013bb390c69bc775d5499fe24b6d14…` |
| L05 | `87b638cf8822890fe42826d50bcae983…` |
| L06 | `3045805eae9d6960c9cd732f82461142…` |
| L07 | `9c5a88802fcb08c8fee8f538a16ba990…` |
| L08 | `dd06ca7bf94d46d7ac2ecd40397626c5…` |

Per-rung A6 re-verifications:

| Rung | a6_re_verification.json sha256 |
|---|---|
| L01 | `b539c2089a7dfb3bfc4351c5b91e3f3b…` |
| L02 | `2a08911b80b0bbb291c480fe78ae6d84…` |
| L03 | `b7823d336c80839fd159c4f7dd95a23c…` |
| L04 | `afbc1b64508c548d38562662bf365c02…` |
| L05 | `bdd30c67abc664a30c86fef0569ef884…` |
| L06 | `f972142e26d3acf84031ac6b92b816dc…` |
| L07 | `785fdec11f378c250617feb23ccde79b…` |
| L08 | `3ed67a05b1f78b05b89066ca56bc403b…` |

Run-level IVR:

| file | sha256 |
|---|---|
| `instrument_validation_report.md` | `72b9216d8475d14b334a9782eefef16498ff0c42e4bb6b89ca9be283d686d6cb` |

## §19. Per-rung candidate-vs-token-prior comparison artifacts and hashes

| Rung | candidate_vs_tp_comparison.json sha256 |
|---|---|
| L01 | `fff8b48b85c6890138556d2ca987a001…` |
| L02 | `fff8b48b85c6890138556d2ca987a001…` |
| L03 | `fff8b48b85c6890138556d2ca987a001…` |
| L04 | `fff8b48b85c6890138556d2ca987a001…` |
| L05 | `fff8b48b85c6890138556d2ca987a001…` |
| L06 | `fff8b48b85c6890138556d2ca987a001…` |
| L07 | `fff8b48b85c6890138556d2ca987a001…` |
| L08 | `fff8b48b85c6890138556d2ca987a001…` |

(All identical sha256: the per-rung comparison block is computed from
candidate/TP counts that happened to be identical across all rungs;
deterministic JSON output → identical bytes. This is an artifact of
this specific candidate × this specific surface, not a property of
the comparison machinery. Per the per-rung adjudication rule, these
remain eight independent rung-local computations that happened to
produce the same numbers.)

## §20. Per-rung criterion outcomes (rung-local; no aggregation)

Each rung adjudicated **separately** under the full six-criterion set.
Eight rung-local results:

| Rung | candidate accuracy | TP control accuracy | NW diff CI [lower, upper] | TP fires? | Other criteria | Attached labels | **Rung-local outcome** |
|---|---|---|---|---|---|---|---|
| L01 | 1.0000 (80/80) | 0.0125 (1/80) | [0.9159, 0.9978] | NO (0.998 > 0.10) | All PASS | (none) | **NOT_RULED_OUT** |
| L02 | 1.0000 (80/80) | 0.0125 (1/80) | [0.9159, 0.9978] | NO | All PASS | (none) | **NOT_RULED_OUT** |
| L03 | 1.0000 (80/80) | 0.0125 (1/80) | [0.9159, 0.9978] | NO | All PASS | (none) | **NOT_RULED_OUT** |
| L04 | 1.0000 (80/80) | 0.0125 (1/80) | [0.9159, 0.9978] | NO | All PASS | (none) | **NOT_RULED_OUT** |
| L05 | 1.0000 (80/80) | 0.0125 (1/80) | [0.9159, 0.9978] | NO | All PASS | (none) | **NOT_RULED_OUT** |
| L06 | 1.0000 (80/80) | 0.0125 (1/80) | [0.9159, 0.9978] | NO | All PASS | (none) | **NOT_RULED_OUT** |
| L07 | 1.0000 (80/80) | 0.0125 (1/80) | [0.9159, 0.9978] | NO | All PASS | (none) | **NOT_RULED_OUT** |
| L08 | 1.0000 (80/80) | 0.0125 (1/80) | [0.9159, 0.9978] | NO | All PASS | (none) | **NOT_RULED_OUT** |

**Per Manager §5 + Synthesis v0.3 §5 + NS OC3 guard:** these are eight
rung-local bounded sentences. They **do not aggregate** into
certification, robustness, task-family viability, model capability, or
Claim C progress. No "8/8 survived" phrasing. No composite score. No
survival count. Each rung's NOT_RULED_OUT is the same bounded
sentence said eight times about a single narrow surface (the
construction the sealed recipe generates per rung).

### Per-criterion outcome at each rung (all rungs identical)

| Criterion | Outcome at every rung (L01-L08) |
|---|---|
| null_abstention_floor_unmet | PASSED |
| answerable_abstention_ceiling_exceeded | PASSED |
| **accuracy_indistinguishable_from_token_prior** | **PASSED** (CI upper 0.998 >> 0.10 locked margin; criterion does not fire; TP active and measured fresh per rung) |
| accuracy_indistinguishable_from_declared_policy_envelope | PASSED |
| insufficient_measurement_headroom | PASSED |
| strict_content_gap_instability | PASSED |

## §21. Abort status

```text
abort_triggered:  NO
abort_reason:     n/a
elapsed_seconds:  404.7
```

All twelve Manager §7 abort triggers were armed; none fired.

## §22. INCONCLUSIVE status

```text
rung-level INCONCLUSIVE:  0 / 8 rungs
record-level INCONCLUSIVE: 0 candidate parse failures across all 8 rungs;
                          0 TP control parse failures across all 8 rungs
per-rung void rate:       0.0 / 0.05 (well below budget on every rung)
```

## §23. Confirmation: TP was active by Manager decision

**CONFIRMED.** TP banner ACTIVE form propagated into every emitted
report (per-rung pre_flight, t3, a6, candidate_vs_tp, run-level
ledger, run-level IVR). Verified at this filing by direct read of
each `tp_banner` block. The Manager Q4 authorization
(`AUTHORIZED — Manager Path A 2026-06-12 (unconditioned_token_prior
method; control artifacts only; not candidate evidence …)`) appears
in the `tp_inactivity_authority` field of every banner instance.

Per-rung TP control was measured fresh (per Manager + readiness
packet directive — D4-B's L01 TP prior was NOT reused, even though
the bytes for L01 happened to be identical due to determinism).

## §24. Confirmation: all reports carried TP fields

**CONFIRMED.** All four required TP fields present in every Path A
emitted report:

| field | value at every rung |
|---|---|
| `tp_criterion_status` | `"ACTIVE"` |
| `tp_inactivity_authority` | `"n/a (Manager authorized TP generations for this run)"` |
| `tp_generation_status` | `"RUN (authorized)"` |
| `tp_elimination_labels_enabled` | `true` |

Verified across pre_flight, all 8 per-rung t3 reports, all 8 per-rung
a6_re_verifications, all 8 per-rung candidate_vs_tp comparisons, and
run-level execution ledger. **Eight rungs × four fields × five
artifact types = 160 banner field presences, all confirmed.**

## §25. Confirmation: no sealed byte changed

**CONFIRMED.** The runner snapshotted the sealed `validation/`
directory inventory (file paths + sha256s) **before** any
materialization or inference and re-snapshotted at run end. The two
inventories were compared at the end of the run; they matched
byte-for-byte. The ledger records `no_sealed_byte_change: CONFIRMED`.

Additionally re-verified at this return filing: the three lock-event
artifacts and the L01 sealed manifests all hash to their sealed-time
values:

| sealed artifact | sha256 | match |
|---|---|---|
| `validation/ORACLE_VERDICT_TABLE.json` | `9c6cbda9eb5b6e850b88451529bb989dee6355ce145c31d1fca5d7b0f3a7fba5` | ✓ |
| `validation/T3_BOUNDS_DECLARATION.json` | `45565d0b46c05da4f7d5c13956ac3a6331cc0748dfba4546f8f1d6cc46addd39` | ✓ |
| `validation/STRATIFIED_RECIPE_SCHEDULE.json` | `7ad3ccddecd070074e666ffaf2178aa0afd3cfda78fc08ef375fe68a907130c5` | ✓ |
| `validation/pilot_manifests_L01.json` | `afe0e545c318132a5821e6d02ba3f41093c05ce7a2623a120d0088e03b29b09f` | ✓ |
| `validation/final_manifests_L01.json` | `afe0e545c318132a5821e6d02ba3f41093c05ce7a2623a120d0088e03b29b09f` | ✓ |
| `governance/.../LANE1A-PRIME-SEALED-LOCK-RECORD-v1.0.md` | `51e18fa9f45379a37aaac6f33b2bcef442e3dff6eeb0268ad073ac04423d1935` | ✓ |

Sealed LOCK-RECORD: ≈20th survival check.

D4-A and D4-B run-of-record artifacts also re-verified unmutated.

## §26. Confirmation: no quantization occurred

**CONFIRMED.** bf16 unquantized throughout. Execution ledger:
`no_quantization: "CONFIRMED"`.

## §27. Confirmation: no INT8 / INT4 occurred

**CONFIRMED.** No INT8 / INT4 weights loaded. Execution ledger:
`no_int8_or_int4: "CONFIRMED"`. No path under
`tier0-run/Qwen2.5-3B-Instruct-mlx-int{4,8}/` was accessed.

## §28. Confirmation: no threshold work occurred

**CONFIRMED.** No threshold values were derived, populated, locked,
or referenced beyond the already-sealed T3 bounds. Execution ledger:
`no_threshold_work: "CONFIRMED"`.

## §29. Confirmation: no certification evaluation occurred

**CONFIRMED.** No candidate was certified, no certification window
was applied, no certification scope was declared. Execution ledger:
`no_certification_evaluation: "CONFIRMED"`.

## §30. Confirmation: Claim C remains inactive

**CONFIRMED.** Claim C is INACTIVE. No activation event filed.
Execution ledger: `no_claim_c_activation: "CONFIRMED"`.

## §31. Non-claim block (Manager §10 verbatim)

> Path A, even if all rungs return NOT_RULED_OUT, does not establish:
> model capability, model incapability, candidate certification,
> task-family viability, certification readiness,
> retention-under-compression, Claim C progress, seam evidence, or
> public benchmark status.
>
> Standing framing remains:
>
> The instrument may rule out; it may not rule in.
>
> Reportable only as "not explained by the declared shortcut battery"
> (and — TP being active and measured — "not explained by the
> candidate's own measured token prior") **per rung**.
>
> Never reportable as "not shortcut-driven."

### Carried interpretation guards (verbatim from D4 Synthesis v0.3 + Constructibility-Risk Note)

> **Repetition guard (OC3):** D4-A, D4-B, and Path A's eight rungs are
> non-eliminations on narrow surfaces. They do not aggregate into
> certification, robustness, or general viability.

> **Token-prior over-read guard (OC1):** "Not explained by the
> measured token prior" must never decay into "not shortcut-driven."
> The accepted interpretation is exactly two clauses — *not explained
> by the declared shortcut battery; not explained by the candidate's
> own measured token prior* — and nothing else.

> **Three-branch interpretation of any future non-certification:**
> threshold miscalibration · gate-design defect · genuine
> constructibility barrier at model/task/scale. The third branch
> remains a first-class possible result, not presumed, not a failure.

> Forbidden phrasings remain prohibited: `model passed` ·
> `capability established` · `not shortcut-driven` · `candidate
> certified` · `task family viable` · `Claim C progressed` ·
> `seam evidence` · `public benchmark result` · `certification
> achieved`.

---

## Appendix A — Reading the result honestly

Per the synthesis v0.3 §5 progression discipline, Path A is one more
event in the **instrument-operation history**, not a step up a
capability ladder. The eight rung-local NOT_RULED_OUT outcomes share
identical per-rung structure (candidate 1.0; TP control 0.0125; NW
diff `[0.916, 0.998]`); this **describes a candidate that performs the
declared retrieval task deterministically across rungs constructed by
the same recipe**, with a token-prior control comfortably separated
from the candidate's behavior on each rung. It does not describe
capability beyond the task family, viability beyond L01-L08, or any
certification-relevant readiness.

The natural per-rung sentence (template; substitute "L0k" as needed):

> On rung L0k, the instrument did not attach any elimination label
> under the active six-criterion set. The result is reportable only
> as not explained by the declared shortcut battery or by the
> candidate's own measured token prior, on rung L0k.

Eight of these. None aggregates with any other.

## Appendix B — Required Manager verification path (Manager §9)

```text
1. New Senior performs full G1 byte verification.
2. New Senior recomputes all artifact hashes.
3. New Senior confirms sealed LOCK-RECORD v1.0 unchanged.
4. New Senior audits generator and materialization chain.
5. New Senior independently recomputes all per-rung Newcombe-Wilson intervals.
6. New Senior audits per-rung adjudication.
7. New Senior confirms TP active by Manager decision.
8. New Senior confirms all reports carried TP fields.
9. New Senior confirms no unauthorized work occurred.
10. Team Lead filters the result.
11. Manager reviews the result.
```

CS does not claim citability for this result. It is filed for the
above verification chain.

## Appendix C — Standing carry (non-authorizations, verbatim)

This Path A run return does not authorize: quantization stress;
INT8 / INT4; stress-retention testing; candidate selection; ranking;
threshold work; certification evaluation; Claim C activation; public
benchmark packaging; funder-facing release; SBIR submission.

All gates outside Path A's narrow authorized scope remain CLOSED.

**D4 token-prior authorization slot:** was authorized for Path A
under Manager 2026-06-12 with the explicit guard "control artifacts
only · not candidate evidence · not threshold material · not reusable
outside this lane's locked comparison." That guard binds the Path A
TP control outputs in perpetuity. The slot is not generally open;
any future TP authorization is a separate Manager decision.

— CS Engineer, 2026-06-12
