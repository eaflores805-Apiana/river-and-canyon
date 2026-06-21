# Manager Decision — Paper 2 v1.2 RC Status-Line Cleanup

**To:** CS Engineer
**Cc:** Senior Engineer, C5, Team Lead
**From:** Manager
**Subject:** Narrow status-line cleanup on Paper 2 v1.2 RC
**Status:** AUTHORIZED — status-line edit only

CS,

Manager accepts the TL recommendation.

Proceed with the narrow Paper 2 v1.2 RC status-line cleanup only.

Decisions:

```text
1. Keep V3 figure numbering for this RC.
2. Keep Cell02 placement in main text.
3. Accept CS's new-file policy preserving v1.1 unchanged.
4. Update only the manuscript status/version line to v1.2 release candidate.
```

Use the status line proposed by TL:

```text
v1.2 release candidate. River and Canyon program. Companion to Survival Is Not Correctness: A Staged, Fail-Closed Metrology Protocol for Stress-Retention Evaluation (Paper 1). Experimental values and artifact hashes are attested from the locked run records and listed in Appendix B; CS independently recomputed them for the freeze/tag pass. This release candidate adds a second, independent construction (foreclose-all V3; §3.3, §4.6), integrates the V3/hop1 constructibility finding, and supersedes v1.1 pending final release authorization.
```

No other prose changes.

Return:

```text
CS RETURN — PAPER 2 v1.2 RC STATUS-LINE CLEANUP COMPLETE
```

Include:

```text
- commit SHA
- final remote HEAD
- clean-fetch confirmation
- final v1.2 RC path and sha256
- confirmation only status line changed
- confirmation all claim-bearing v0.3 strings remain unchanged
- confirmation figures unchanged
- confirmation no release/tag occurred
- confirmation no run/rerun/compression/tooling/threshold change occurred
```

Boundaries: no release, no tag, no new experiment, no construction redesign, no compression, no INT8/INT4, no Claim C, no Paper B, no certification/capability/mechanism claim. Path A FP16 K=5 FAIL remains closed.
