# Senior Finding (Routed via Manager) — Lane 1a Step-3 Review Blocker: Wrapper Rewrites B1 Output

From: Elias / Manager (routing Senior finding to Team Lead)
To: Team Lead
Cc: CS Engineer, Senior Engineer
Date: 2026-06-10
Status: Combined adversarial review PAUSED pending CS remediation; no first data access; LOCK-RECORD still unsealed

---

## Verbatim memo (Manager-routed Senior finding)

> [Filed verbatim per session message; key dispositions §1–§9 captured
> in CS acknowledgement below; full byte-for-byte content preserved
> in session log.]

---

## CS acknowledgement and remediation plan

CS accepts the finding without dispute. The defect is real:

The wrapper's `invoke_b1v2()` function in `lane1a_runner_wrapper.py`
mutates the B1 v2 output JSON by setting `context = "lane-1a-reconnaissance"`,
saving the original B1 value to `original_context_from_b1v2`. This is
the rejected "honest override" pattern. The runner-attested output is
modified by a wrapper; the provenance chain is no longer cleanly
B1-attested.

The expected sidecar-attestation pattern: B1 output bytes are
preserved unchanged; Lane 1a metadata lives in a sidecar JSON
companion file with its own schema and hash linkage to the B1 output.

CS confirms: this is a G1-instruction-channel failure on the Senior
correction memo (it was SEND-marked but not commit-confirmed at
production time, so CS built from the prior confirmed spec, which
still permitted "honest override"). The G1 rule applies to correction
memos too: intent is not delivery.

## Remediation scope (per memo §5; 9 required items)

| # | Required change | CS plan |
|---|---|---|
| 1 | Replace output-rewrite with sidecar attestation | Rewrite `lane1a_runner_wrapper.py` `invoke_b1v2()` |
| 2 | Preserve original B1 output bytes unchanged | Wrapper reads result file path; does NOT open + rewrite |
| 3 | Record hash of original B1 output | Sidecar carries `b1_output_sha256` |
| 4 | Add sidecar schema | NEW: `schema/lane1a_sidecar.schema.json` |
| 5 | Unit test: original B1 output preserved byte-for-byte | NEW: `test_b1_output_preserved_byte_for_byte` |
| 6 | Unit test: Lane 1a metadata only in sidecar | NEW: `test_lane1a_metadata_only_in_sidecar` |
| 7 | Add `--context` functional statement to LOCK-RECORD + return | LOCK-RECORD gets a "B1 v2 `--context` functional statement" section |
| 8 | Regenerate affected Step-3 artifacts | Re-hash + re-seal |
| 9 | File or close the G1-open Senior correction memo | This file is the formal CS-side close: Senior's correction is now in-repo, hash-recorded, and superseding the prior wrapper semantic |

## New permanent production rule (per memo §6)

CS records the new rule into the standing review-discipline:

```text
No production cycle may begin while any condition memo affecting that
production cycle is G1-open.

Applies to: Senior correction memos, Team Lead conditions, Manager
constraints, CS implementation notes that alter artifact semantics.

A production cycle may proceed only after such condition memos are
either:
  - committed at intended path
  - hash-confirmed
  - explicitly superseded
  - or explicitly ruled out of scope by Team Lead / Manager.
```

CS will append this rule to
`governance/standing/STANDING-REVIEW-DISCIPLINE.md` in this commit.

## Recommended disposition

CS supports Manager's recommended disposition: **A — accept as
review-blocking; direct CS remediation.** CS executes the 9-item
remediation in this commit cycle and produces a fresh LOCK-RECORD
with new hashes for the affected artifacts.

## What CS has NOT done (and continues to NOT do)

- No first data access.
- No model invocation.
- No B1 v2 edit.
- No B1 v2.1 creation.
- No invocation of `lane1a_runner_wrapper.py`.

The locked artifacts at commit `25613d3` remain in place; the
remediation produces a superseding artifact set under the same path,
re-hashed, with the original commit preserved as historical audit
trail (per the "supersede, don't rewrite" rule).

## Standing posture

All execution gates remain CLOSED. Lane 1a remains pre-candidate
reconnaissance only. First data access remains NOT AUTHORIZED.

— CS Engineer, 2026-06-10
