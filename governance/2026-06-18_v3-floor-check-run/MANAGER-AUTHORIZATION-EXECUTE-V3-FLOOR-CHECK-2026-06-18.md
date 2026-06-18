# Manager By-Name Authorization — Execute V3 Floor Check

**To:** CS Engineer
**Cc:** Senior Engineer, C5, Team Lead
**From:** Manager
**Subject:** Authorization to Execute V3 Floor Check
**Status:** AUTHORIZED — V3 FLOOR CHECK ONLY

I authorize CS to execute the locked V3 Floor Check by name:

```text
PREREGISTRATION — V3 FLOOR CHECK (Path A) v0.4
```

This authorization is limited to the V3 floor-check run described in the approved package.

## Locked purpose

Execute the empirical floor check:

```text
Does hop2 clear its reliability floor under V3 same-depth-competitor competition?
```

The primary metric is hop2-isolated retrieval, reported alone against the locked floor. This is not a composite certification run.

## Locked tooling

Use the approved and verified tooling:

```text
v3_floor_check_analyzer.py
sha256: 0f5a3f7438a6936fe449ea3558321a734b999b2ac2e8384032c2890e155f3585

v3_prompt_realizer.py
sha256: fb561fdc526115da94c6137b739e8bb3b6adf30825d83f864cda713bc0750909

v3_prompt_conformance_checker.py
sha256: b8afa3f89dd7f375058500820bdf2bf58a46384d2283c8f2a31f1b8c92ad2b82

v3_neutral_token_pool.md
sha256: bc2020c2c4e1293f62c9f83a9b24a61f98c1ede35d5a071ee8cfd72a316ab0d9
```

## Required execution sequence

CS may now perform the following, in order:

```text
1. Materialize the full N=96 V3 item set.
2. Confirm each item passes C1–C9 in real-run mode.
3. Realize four-context prompts for each item:
   composite / hop1 / hop2 / direct_query.
4. Run prompt-conformance checks.
5. Confirm MAX_DELTA = 8 character-count gate under the current token-width / relation-naming / K=5 scheme.
6. Execute the V3 Floor Check under the locked run profile.
7. Analyze outputs using the locked analyzer.
8. Return all artifacts, hashes, clean-fetch verification, and the §9 / §10 branch.
```

## MAX_DELTA binding caveat

`MAX_DELTA = 8` is approved only for the current scheme:

```text
- current per-item token-width scheme
- current locked Manager values: K=5, D=5, P=5, M=10
- current four-context relation-naming scheme
```

Any change to token width, construction shape, relation naming, or locked values reopens prompt-length conformance and is not authorized by this memo.

## Required return

Return:

```text
CS RETURN — V3 FLOOR CHECK EXECUTED
```

Include:

```text
- commit
- final remote HEAD
- all artifact paths
- sha256 hashes
- clean-fetch confirmation
- N=96 materialization summary
- C1–C9 admissibility result
- prompt-realization conformance result
- MAX_DELTA result
- model/run profile
- raw output path and hash
- analyzer output path and hash
- hop2 rate and Wilson 95% CI
- hop1 rate and Wilson 95% CI
- direct-query C* count
- invalidated item count
- final §9 / §10 branch
```

## Boundaries

This authorization does **not** authorize:

```text
compression
INT8
INT4
Claim C
Paper B
certification claim
capability claim
mechanism claim
rerun
post-hoc slicing
floor adjustment
tooling edit after data
```

The Path A FP16 K=5 FAIL remains closed.

Manager authorizes this run by name.

— Manager
