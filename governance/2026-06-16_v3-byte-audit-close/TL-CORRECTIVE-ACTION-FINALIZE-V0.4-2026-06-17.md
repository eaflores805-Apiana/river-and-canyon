# TL Corrective Action — Replace Placeholder v0.4 With Finalized v0.4

**To:** CS Engineer
**Cc:** Senior Engineer
**From:** Team Lead
**Subject:** Correct V3 v0.4 Of-Record Bytes Before Philosophy Record Filing
**Status:** ACTION — clerical correction / no science change

CS,

Hold philosophy decision record filing.

Senior verified that the current repo of-record file:

```text
path-a/of-record/PREREGISTRATION-PATH-A-CONSTRUCTIBILITY-v0.4.md
sha256: bfb4404a…
```

still contains the placeholder:

```text
<v0.3 of-record digest>
```

Senior also verified that the finalized filled version has digest:

```text
c61a3256…
```

and contains the filled v0.3 digest:

```text
d9bd9b219badd25901811ddfbb43b811a04750a77723f6a1f076c7dd641f091c
```

## Required action

Replace the current of-record v0.4 placeholder version with the finalized filled v0.4 bytes.

Target:

```text
path-a/of-record/PREREGISTRATION-PATH-A-CONSTRUCTIBILITY-v0.4.md
expected sha256 after replacement: c61a3256…
```

Update any README / closure note / re-lock reference that currently points to `bfb4404a…` as the of-record v0.4 digest.

Add a short corrective note:

```text
Correction: prior v0.4 elevation landed the pre-fill binding patch containing the <v0.3 of-record digest> placeholder. This commit replaces it with the finalized filled v0.4 bytes. No values, thresholds, rules, categories, controls, or stop-rules changed.
```

## Required return

Return:

```text
PASS — finalized v0.4 landed of-record
```

Include:

```text
- commit
- final remote HEAD
- clean-fetch confirmation
- corrected v0.4 path
- corrected v0.4 sha256
- confirmation placeholder is absent
- confirmation v0.3 digest is present
- list of any README / closure / re-lock references updated
```

## Boundaries

No build.
No item generation.
No prompt generation.
No model run.
No compression.
No Claim C.
No Paper B.
No capability claim.
No mechanism claim.

The Path A FP16 K=5 FAIL remains closed.

Team Lead
