# Manager / Team Lead Direction — Lane 1a Manifest Interface Remediation (Path A)

From: Elias / Manager
To: CS Engineer
Cc: Senior Engineer, Team Lead
Date: 2026-06-10
Status: Path A authorized; CS executing remediation; first data access NOT authorized

---

## Verbatim memo

> CS,
>
> Manager and Team Lead acknowledge the deviation report filed at
> commit `a37ca24`. CS correctly stopped at deviation discovery; no
> first data access occurred.
>
> Finding accepted; damage assessment accepted.
>
> ## 3. Remediation decision
>
> Manager selects: **Path A** — create a Lane 1a-specific runner using
> the same locked model-loading / provenance conventions, without
> editing B1 v2.
>
> CS may implement
> `experiments/2026-06-10_lane-1a-sweep/lane1a_runner.py`.
>
> The runner must preserve Lane 1a manifest semantics and must not
> require modifying B1 v2.
>
> ## 4. Important wording correction
>
> After Path A, the packet must NOT claim Lane 1a is executed
> *through* B1 v2.
>
> The correct wording is:
>
> ```text
> Lane 1a uses a lane-specific runner that preserves B1 v2-compatible
> provenance conventions and locked model-loading dependencies, while
> leaving B1 v2 source unedited.
> ```
>
> Do NOT describe this as native B1 v2 execution.
> Do NOT describe this as B1 v2.1.
>
> ## 5. Authorized remediation work
>
> [9 items: add `lane1a_runner.py`; update wrapper; update runner
> config; update LOCK-RECORD; add tests; preserve sidecar; preserve
> byte-preservation; re-seal hashes; return remediation report.]
>
> ## 6. Required tests
>
> [12 conditions to test.]
>
> ## 7. Required CS return after remediation
>
> [11 items.]
>
> ## 8. Review sequence after remediation
>
> CS return → Senior confirms intent → Team Lead combined review →
> LOCK-RECORD timestamp finalized → Manager reauthorizes → CS may
> execute if preflight passes.
>
> ## 10. Disposition
>
> Path A remediation: authorized
> B1 v2 edit: not authorized
> B1 v2.1: not authorized
> First data access: not authorized
>
> — Elias / Manager

---

## CS acknowledgement and execution declaration

CS confirms:

1. **Path A authorized.** CS proceeds with single-cycle remediation
   producing:
   - `experiments/2026-06-10_lane-1a-sweep/lane1a_runner.py` (NEW)
   - `experiments/2026-06-10_lane-1a-sweep/lane1a_runner_wrapper.py` (UPDATED)
   - `experiments/2026-06-10_lane-1a-sweep/runner_config.yaml` (UPDATED)
   - `experiments/2026-06-10_lane-1a-sweep/test_lane1a_packet.py` (UPDATED)
   - `experiments/2026-06-10_lane-1a-sweep/LOCK-RECORD.md` (RE-SEALED)

2. **Wording discipline applied verbatim.** All Lane 1a documentation
   produced from this point forward uses the Manager-prescribed
   wording:

   > Lane 1a uses a lane-specific runner that preserves B1 v2-
   > compatible provenance conventions and locked model-loading
   > dependencies, while leaving B1 v2 source unedited.

   CS will not describe Lane 1a as native B1 v2 execution or as B1 v2.1.

3. **B1 v2 source remains unedited.** The new runner uses `mlx_lm`
   directly (the same dependency B1 v2 uses) and records model
   snapshot provenance in B1 v2-compatible format (sha256 over a
   sorted manifest of model-directory files), but does NOT import any
   module from `experiments/2026-06-09_b1-harness-v2/`.

4. **B1 v2.1 is not created and not used.** No new harness-side
   capability is added; `lane1a_runner.py` is a sweep-specific runner,
   not a harness extension.

5. **Sidecar attestation pattern preserved.** The wrapper continues to
   write `*.lane1a.sidecar.json` companion files; the runner output
   bytes are preserved unchanged; the only modification is that the
   underlying runner is `lane1a_runner.py` instead of B1 v2's CLI.

6. **First data access does NOT occur in this commit cycle.** No
   model load; no inference; no `AUDIT-LOG.ndjson` writes; no live
   sweep outputs.

7. **All §6 test requirements covered.** CS adds tests for: manifest
   schema validation; malformed-manifest rejection; model attestation
   recording; byte-for-byte preservation; sidecar-only metadata;
   const-locked Lane 1a tags; no-re-execution enforcement; planned
   generation count; B1 v2 unedited; B1 v2.1 absent.

8. **§7 11-item return** filed alongside this remediation as
   `CS-PATH-A-REMEDIATION-RETURN-2026-06-10.md`.

— CS Engineer, 2026-06-10
