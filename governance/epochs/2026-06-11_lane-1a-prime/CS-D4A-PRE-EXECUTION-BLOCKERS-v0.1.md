# CS D4-A Pre-Execution Blockers (v0.1)

```text
SYNTHETIC / DIAGNOSTIC — NON-BINDING — NOT FOR THRESHOLD DERIVATION
PRE-EXECUTION GAP MEMO — D4-A NOT YET EXECUTED
BLOCKER — REQUIRES MANAGER DECISION BEFORE D4-A AUTHORING/EXECUTION PROCEEDS
SEALED LOCK-RECORD v1.0 UNCHANGED · D4 TOKEN-PRIOR SLOT: PENDING / UNOPENED
NO MODEL INVOKED · NO MODEL LOADED · NO SWEEP_ID · NO SWEEP EXECUTION
```

To: Manager (decision) · Cc: Team Lead, New Senior Engineer, Senior Engineer
From: CS Engineer
Date: 2026-06-11
Re: Two pre-execution preconditions need disposition before runner authoring + D4-A execution

CS has begun D4-A execution under Manager authorization (`D4-A
minimal operational pilot approved`). On environment audit, two
preconditions need explicit Manager disposition before CS can author
the runner and proceed. Per the standing governance pattern this
memo files them as a BLOCKER rather than CS making unilateral
substitutions to the authorized declaration.

**BLOCKER — requires Manager decision before D4-A authoring/execution.**

---

## §1. BLOCKER 1 — mlx_lm framework version

### State

| field | value |
|---|---|
| Authorized pin (per `LANE1A-PRIME-D4-READINESS-PACKET-v0.2.md` §7 and `CS-D4-READINESS-RUNTIME-SLOTS-v0.2.md` §1) | **`mlx_lm 0.19.3`** |
| Installed on execution host | **`mlx-lm 0.31.3`** (with `mlx 0.31.2`, `mlx-metal 0.31.2`) |
| Verified-null lineage on record (B1 v2 PROVENANCE, 2026-06-10) | `mlx_lm 0.19.3 → 0.31.3 verified-null for the locked Paper 2 reproduction configuration` |

### Why this blocks

Per Manager §6 (verbatim): "abort on runner/model identity mismatch."
Per packet v0.2 §13 hard stop 4: "the D4-A runner stamps the running
`mlx_lm` version at start; if the stamped version is not exactly equal
to the authorized pin (0.19.3), the runner aborts before any model load
or inference."

Authoring the runner with a hardcoded pin of `0.19.3` and invoking it
on this host will produce a deterministic abort at pre-flight. The
runner will not proceed to model load.

CS cannot proceed by:
- silently substituting the pin to `0.31.3` (this would violate the
  authorized declaration);
- installing `mlx_lm 0.19.3` without explicit authorization (this is
  an unauthorized system modification);
- running under `0.31.3` without the version-check abort (this would
  remove a Manager-required safety check from the runner).

### Disposition options (Manager chooses)

```text
Option A — substitute the pin to 0.31.3 by Manager direction:

  [ ] Manager substitutes the authorized pin to mlx_lm 0.31.3
      Rationale: B1 v2 PROVENANCE has 0.31.3 on record as
      verified-null for the Paper 2 reproduction configuration; no
      additional environment setup needed. CS updates the v0.2
      packet/slot memo via a supplemental memo bound to this Manager
      direction; runner is authored with the substituted pin.

Option B — install mlx_lm 0.19.3 in the execution environment:

  [ ] Manager authorizes pip install of mlx_lm==0.19.3
      Rationale: matches the authorized pin exactly. Requires
      installing a specific older mlx_lm release in a venv or the
      system Python on the execution host. CS would attach the
      pip-freeze output of the installation for provenance.

Option C — defer D4-A:

  [ ] Manager defers D4-A pending other work
      D4-A execution stands down; CS does not author the runner
      until the version question is resolved at a later date.
```

CS recommendation: **Option A**. Rationale: the verified-null status
of 0.31.3 is on record from B1 v2 (2026-06-10) and was explicitly
noted as a substitution option in packet v0.2 §7 itself. Substituting
preserves the spirit of the authorized declaration (one exact pin)
with no additional environment work. Manager not bound by this
recommendation.

---

## §2. BLOCKER 2 — model snapshot hash verification routine

### State

| field | value |
|---|---|
| Authorized canonical snapshot hash (per packet v0.2 §4 and slot v0.2 §1; sourced from B1 v2 lock note 2026-06-10) | **`abee745b7dfe399d9254dbcdea5e3e3902aa95d71a31989b7b720b7ac9907b20`** (runner-provenance-backed sha256) |
| Local HF cache snapshot (revision) | `~/.cache/huggingface/hub/models--Qwen--Qwen2.5-3B-Instruct/snapshots/aa8e72537993ba99e69dfaafa59ed015b17504d1/` |
| Local snapshot configuration | `torch_dtype: "bfloat16"` (confirmed bf16); `architectures: ["Qwen2ForCausalLM"]`; `transformers_version: 4.43.1` |

### Why this is a question, not yet a blocker (but it must be resolved before model load)

The authorized `abee745b…` is a **runner-provenance-backed sha256**
computed by the B1 v2 runner over the model weights at a particular
load step. The local HF cache's revision identifier `aa8e7253…` is a
**HuggingFace git revision hash**, computed by HF over the snapshot
manifest. These are different hashing schemes; they cannot be compared
directly.

The local `aa8e7253…` snapshot IS the canonical Paper 2 / B1 v2 model
on the same HF revision — the Paper 2 Freeze Tag Report has
`aa8e7253…` recorded as the asserted snapshot (Paper 2 Appendix B),
and B1 v2 derived the runner-provenance-backed `abee745b…` from the
same files via a runner-side hashing routine.

Two questions follow:

```text
Question 2a:
  Does the runner CS authors compute model_snapshot_hash by replaying
  the B1 v2 runner-provenance routine over the local snapshot's
  weight files?

Question 2b:
  If the runner-derived hash equals abee745b... → match → proceed.
  If it does not equal abee745b... → abort per Manager §6 ("abort on
  runner/model identity mismatch").
```

### CS proposed answer (subject to Manager confirmation)

```text
2a: Yes — replay the B1 v2 runner-provenance routine in the D4-A
    runner's load_model() step. The routine deterministically computes
    sha256 over the canonicalized weight tensor stream (the same
    routine B1 v2 used to derive abee745b...).

2b: If the locally-derived hash equals abee745b..., D4-A proceeds. If
    it does not, the runner aborts and CS files a separate BLOCKER
    memo asking Manager to disposition (re-stage the canonical
    snapshot, or substitute snapshot hash, or defer).
```

CS does not request authorization for Question 2 in this memo because
authoring the runner with the snapshot-verification routine is itself
part of D4-A authoring (Manager already authorized authoring under
"model loading: authorized only as needed for the approved D4-A
pilot"). CS only flags here that the snapshot-verification step is a
**runtime check** that may surface a real mismatch and would then
require its own Manager decision. The local snapshot is highly
unlikely to mismatch (it is the canonical Paper 2 cache, by all
available evidence), but the routine has not been replayed in this
session and CS does not claim a match without running the routine.

---

## §3. Standing confirmations

- Sealed LOCK-RECORD v1.0 sha256 `51e18fa9…` re-verified at this filing — **UNCHANGED**.
- D4 token-prior authorization slot: **PENDING / UNOPENED** (per Manager Q2 decline, the slot remains in its sealed state; TP criterion will be INACTIVE in the D4-A run header and every D4-A report once execution proceeds).
- No model invoked. No model loaded. No sweep_id created. No sweep execution occurred.

## §4. What CS will do upon Manager disposition

```text
If Option A (pin substitution to 0.31.3):
  1. File a supplemental memo binding the substitution to Manager
     direction (preserving the v0.2 packet/slot hashes; the
     substitution lives in a new memo cross-referenced from the D4-A
     runner's preconditions.json).
  2. Author the runner with mlx_lm 0.31.3 as the authorized pin.
  3. Author prompt template, parser, decoding config.
  4. Run pre-flight (lock-event hash check + version check + snapshot
     hash check via the runner-provenance routine).
  5. On all-pass: proceed to 96-record L01 D4-A execution.
  6. On any-refusal: file the abort retention + a follow-up memo.
  7. File LANE1A-PRIME-D4A-PILOT-RETURN-v0.1.md per Manager §8.

If Option B (install 0.19.3):
  1. File a supplemental memo binding the installation to Manager
     authorization (includes pip-freeze output as provenance).
  2. Author the runner with mlx_lm 0.19.3 as the authorized pin.
  3..7. Same as Option A.

If Option C (defer):
  1. CS stands down on D4-A authoring.
  2. The Manager D4-A authorization remains live but unexercised.
  3. No code is authored; no runner is committed.
  4. The sealed LOCK-RECORD v1.0 remains the immutable instrument
     anchor.
```

## §5. Non-claim block (Manager §5 verbatim)

This pre-execution memo does not change the standing constraints.

> D4-A is an instrument-use step, not a capability claim.
>
> It would not establish model capability, model incapability,
> task-family viability, candidate suitability, certification
> readiness, retention-under-compression, Claim C progress, seam
> evidence, or public benchmark status.
>
> The instrument may rule out; it may not rule in.
>
> Passing the declared battery is reportable only as "not explained
> by the declared shortcut battery," never as "not shortcut-driven."
>
> We have improved the ruler; we are only beginning to touch the
> territory.

## §6. Standing carry (non-authorizations, verbatim)

This pre-execution memo does not authorize: D4 sweep execution; D5
close-out; model runs; model loading; new sweep_id; sweep execution;
token-prior model generations; scrambled-binding model generations;
candidate/model outputs; candidate selection; ranking; threshold work;
certification evaluation; stress-retention testing; Claim C activation;
public benchmark packaging.

All model-touching and sweep-execution gates remain CLOSED until
Manager dispositions Blocker 1 above.

**D4 token-prior authorization slot: PENDING / UNOPENED.**

— CS Engineer, 2026-06-11
