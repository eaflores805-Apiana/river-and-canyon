# CS D4-A TP-Banner Deviation Acknowledgement + Fix Plan (v0.1)

```text
SYNTHETIC / DIAGNOSTIC — NON-BINDING — NOT FOR THRESHOLD DERIVATION
NAMED-DEVIATION ACK + FUTURE-RUN FIX PLAN — NO POST-HOC MUTATION
D4-A RESULT STANDS AS EMITTED · SEALED LOCK-RECORD v1.0 UNCHANGED
NO MODEL INVOKED · NO MODEL LOADED · NO SWEEP_ID · NO SWEEP EXECUTION
D4 TOKEN-PRIOR SLOT: PENDING / UNOPENED
```

To: Manager (decision) · Cc: Team Lead, New Senior Engineer, Senior Engineer
From: CS Engineer
Date: 2026-06-11
Re: Manager §5 10-item return — TP-banner deviation ack + fix plan

CS acknowledges the named deviation Manager dispositioned on the D4-A
pilot. CS confirms no D4-A output will be mutated. CS files the
future-run fix as a code patch (runner + tests) prepared now but
applicable only to successor runs, per Manager §4. No model execution,
sweep_id, or sweep is requested by this memo.

---

## §1. Acknowledgement of named deviation

**ACKNOWLEDGED.** CS accepts Manager's disposition verbatim:

> D4-A result accepted with named deviation.
> Deviation class: report-emitter completeness defect.
> No post-hoc mutation of run outputs authorized.
> Future-run blocker: report emitter must be fixed before any successor
> D4 run.

The substantive protections of the D4-A run were preserved: TP was
inactive by Manager decision; no token-prior generations occurred;
TP elimination labels did not fire; authoritative carriers (execution
ledger, IVR, T3 report) recorded the inactive state; no unauthorized
work occurred. The deviation is that three subsidiary emitted reports
(T1 JSON, T4 JSON, A6 JSON) did not include the TP inactive-by-decision
banner. CS owns this and treats it as a runner / report-emitter
completeness defect, not as a substantive instrument failure.

## §2. Confirmation: no D4-A outputs will be mutated

**CONFIRMED.** Re-verified at this filing that all six D4-A artifact
sha256s reported in `LANE1A-PRIME-D4A-PILOT-RETURN-v0.1.md` §13 are
byte-identical to their committed values at HEAD:

| artifact | committed sha256 | actual sha256 at this filing | match |
|---|---|---|---|
| `t1_report.json` | `ebe0a952…` | `ebe0a952…` | ✓ |
| `t3_report.json` | `a4e0236b…` | `a4e0236b…` | ✓ |
| `t4_report.json` | `6d265d25…` | `6d265d25…` | ✓ |
| `a6_re_verification.json` | `3c2e09b1…` | `3c2e09b1…` | ✓ |
| `execution_ledger.json` | `f75db02c…` | `f75db02c…` | ✓ |
| `instrument_validation_report.md` | `7510c06a…` | `7510c06a…` | ✓ |

These artifacts and all 96 per-record `candidate_outputs/<id>.json`
files remain unmodified as part of the D4-A run record.

The sealed LOCK-RECORD v1.0 (sha256 `51e18fa9…`) is also re-verified
UNCHANGED.

## §3. Affected emitted reports from D4-A

Per Manager §1 (TL/NS finding), the following D4-A artifacts did NOT
carry the TP inactive-by-decision banner at emit time:

| artifact | banner present? | what it had |
|---|---|---|
| `t1_report.json` | **NO** | per-policy scores, envelope, A6 drift block, candidate summary (no TP fields) |
| `t4_report.json` | **NO** | INH-1..3 + PH5-1..5 + D4A-runner/D4A-tp-inactive/D4A-pin-substitution rows; D4A-tp-inactive row references Manager Q2 by free text, but no structured TP banner block |
| `a6_re_verification.json` | **NO** | drift block only (no TP fields) |

For completeness, the following D4-A artifacts DID carry the banner
or banner-equivalent fields at emit time:

| artifact | banner-equivalent fields present |
|---|---|
| `execution_ledger.json` | `tp_criterion_status: "INACTIVE BY MANAGER DECISION"`, `no_token_prior_generations: "CONFIRMED — Q2 declined by Manager"` |
| `t3_report.json` | `tp_inactive_by_manager_decision: true`, `tp_inactivity_authority: "MANAGER-AUTHORIZATION-LANE-1A-PRIME-D4A 2026-06-11 §4 (Q2 decline)"`, plus per-row `disposition_d4a: "INACTIVE_BY_MANAGER_DECISION"` on the TP criterion |
| `instrument_validation_report.md` | "Inactive criteria (by Manager decision)" section with full Manager Q2 authority citation |

The fix below brings the three NO-banner reports up to parity with
the three banner-carrying reports.

## §4. Proposed runner / report-emitter patch location

**Single patch surface, single source of truth:**

| file | location | change |
|---|---|---|
| `experiments/2026-06-11_lane-1a-prime/d4_runner/lane1a_runner.py` | new helper `tp_banner_block(token_prior_authorized, authority_ref)` near the other module-level helpers | returns a canonical 4-field banner dict; one function call constructs the banner once per run |
| same file | new `main()` step 1a immediately after `preconditions` are loaded | reads `token_prior_decision` and `tp_authority_ref` from preconditions; constructs `tp_banner` ONCE per run |
| same file | each emission envelope (`pre_flight_log`, `t1_report`, `t3_report`, `t4_report`, `a6_re_verification`, `execution_ledger`) | adds `"tp_banner": tp_banner` as a TOP-LEVEL field; for `pre_flight_log` also embeds the banner under `run_header` |

Patch already applied (sha256 of patched runner:
`1d6f7085c8ed6b5d4ebb023a008ccb1c8e1cf2d156bf32f0705870c9d11a31dc`).

Important: the patch is to the RUNNER, which produces NEW artifacts on
successor runs. The patch does NOT modify any D4-A artifact. Per
Manager §3, the existing D4-A `t1_report.json`, `t4_report.json`, and
`a6_re_verification.json` remain unmodified and carry the named
deviation as part of the historical record.

## §5. Proposed fields to add (verbatim, per Manager §4)

The `tp_banner_block(token_prior_authorized=False, authority_ref=...)`
helper returns:

```json
{
  "tp_criterion_status": "INACTIVE BY MANAGER DECISION",
  "tp_inactivity_authority": "<authority_ref carried verbatim>",
  "tp_generation_status": "NOT RUN — DECLINED BY MANAGER",
  "tp_elimination_labels_enabled": false
}
```

When `token_prior_authorized=True`, the helper returns the symmetric
active form:

```json
{
  "tp_criterion_status": "ACTIVE",
  "tp_inactivity_authority": "n/a (Manager authorized TP generations for this run)",
  "tp_generation_status": "RUN (authorized)",
  "tp_elimination_labels_enabled": true
}
```

This block is embedded at the TOP LEVEL of every emission envelope
(`pre_flight_log`, `t1_report`, `t3_report`, `t4_report`,
`a6_re_verification`, `execution_ledger`) and additionally inside
`pre_flight_log.run_header` for run-header parity.

## §6. Tests / dry-run checks to confirm banner propagation

Five unit tests added at
`experiments/2026-06-11_lane-1a-prime/tests/test_d4_runner_tp_banner.py`
(sha256 `d4ac402427a14e6c6eac3a9cec1d0c1451978b4437b245c45135412f74095c7e`):

1. `test_tp_banner_block_q2_declined_has_required_fields` — verifies the four
   required fields are present and have the expected inactive-form values.
2. `test_tp_banner_block_q2_authorized_has_required_fields` — symmetric
   coverage for the future-authorized path.
3. `test_tp_banner_block_authority_ref_carried_verbatim_when_declined` —
   verifies the authority reference is preserved byte-for-byte.
4. `test_tp_banner_propagates_into_simulated_emission_envelopes` —
   simulates the embedded-in-every-emission contract across all six
   envelopes (`pre_flight_log`, `t1_report`, `t3_report`, `t4_report`,
   `a6_re_verification`, `execution_ledger`).
5. `test_runner_module_exposes_banner_function` — verifies the patched
   runner module exports `tp_banner_block` for future-run wiring; also
   reads the committed `preconditions.json` and verifies the banner it
   would produce matches the inactive form.

Test suite status at this filing:

```text
pytest experiments/2026-06-11_lane-1a-prime/tests/
  252 passed (5 new banner tests + 247 pre-existing tests, all green)
```

No model invocation, no sweep_id, no sweep execution during tests; all
tests are dictionary-shape and function-export checks.

## §7. Confirmation: the fix applies only to future authorized runs

**CONFIRMED.** Per Manager §3 (no post-hoc mutation), the patch applies
exclusively to artifacts emitted by FUTURE authorized D4 runs. The
existing D4-A artifacts at `experiments/2026-06-11_lane-1a-prime/d4_a_pilot/`
remain UNMODIFIED. CS will not re-emit, re-write, normalize, or
backfill any D4-A artifact under this fix plan.

Concrete carriers of this constraint:

- The patch is in the runner code only. The runner only WRITES under
  `experiments/2026-06-11_lane-1a-prime/d4_a_pilot/`; it does not
  retroactively load or modify previously-written D4-A artifacts.
- No `os.utime`, no file overwrite, no in-place edit of D4-A JSONs
  exists in the patch.
- Any future authorized D4 run is gated behind a separate Manager
  authorization which would (presumably) specify its own
  `sweep_id`/output directory; the D4-A directory remains the
  immutable D4-A pilot record.

## §8. Confirmation: no model execution is requested

**CONFIRMED.** This memo and the patch authoring do not request, and
do not perform, any model execution.

## §9. Confirmation: no sweep_id creation is requested

**CONFIRMED.** No sweep_id is created by this memo or the patch
authoring. The D4-A sweep_id `lane1a-prime-d4a-20260611-201722-ymbngp`
remains the single D4-A identifier.

## §10. Confirmation: no sweep execution is requested

**CONFIRMED.** No sweep execution is requested or initiated. The
patched runner stands idle until a separately-authorized successor
D4 run.

---

## §11. Accepted result language (Manager §6 verbatim carry)

Going forward, the D4-A result is carried only as:

> The instrument did not attach any elimination label under the active
> five-criterion set.

And:

> The result is reportable only as **"not explained by the declared
> shortcut battery."**

CS will NOT write any of: `model passed`, `capability established`,
`not shortcut-driven`, `candidate certified`, `task family viable`,
`Claim C progressed`, `seam evidence`, `public benchmark result`.

This language constraint binds the D4-A result, the D4-A return memo
(`LANE1A-PRIME-D4A-PILOT-RETURN-v0.1.md`), the IVR, and any future
governance reference.

## §12. Standing carry (non-authorizations, verbatim)

This memo does not authorize: D5 close-out; L02–L08 execution;
token-prior model generations; scrambled-binding model generations;
quantization stress; INT8 / INT4; candidate selection; ranking;
threshold work; certification evaluation; stress-retention testing;
Claim C activation; public benchmark packaging.

No further model-facing work is authorized by this memo. All
successor-execution gates remain CLOSED.

**D4 token-prior authorization slot: PENDING / UNOPENED.**

— CS Engineer, 2026-06-11
