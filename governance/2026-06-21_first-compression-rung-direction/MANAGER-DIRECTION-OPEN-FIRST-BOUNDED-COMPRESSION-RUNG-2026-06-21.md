# Manager Direction — Open First Bounded Compression Rung

**To:** Team Lead, CS Engineer, Senior Engineer, C5
**From:** Manager
**Subject:** Direction to Open First Bounded Compression Rung
**Status:** DIRECTION — prepare run authorization packet, not execution yet

Paper 2 v1.2 is released in Markdown and independently verified. The program has completed a measurement-validity phase sufficient to justify the first bounded stress measurement.

Manager direction:

```text
Open the first compression rung as instrument-validation-under-stress.
```

## Scope

The next packet should prepare a bounded FP16 → INT8 comparison on the already-prepared, smoke-tested target, subject to the existing pre-registration and baseline qualification gates.

This is not a seam test.

This is not Claim C.

This is not a composition claim.

This is the first attempt to use the fail-closed instrument on a stress rung.

## Required framing

The run, if authorized, may answer only:

```text
Can the fail-closed instrument produce a valid FP16-to-INT8 stress-retention readout on the selected qualified target?
```

It may not answer:

```text
whether compression damages composition
whether the seam exists
whether Claim C is supported
whether V3 is fixed
whether M5 is resolved
```

## Required next artifact

Prepare:

```text
FIRST-COMPRESSION-RUNG-AUTHORIZATION-PACKET-v0.1
```

Include:

```text
- target task / item set
- why the target is qualified enough for this first stress rung
- FP16 baseline gate status
- INT8 stress plan
- exact model / quantization profile
- scorer and validator hashes
- pass / fail / uninterpretable branches
- forbidden interpretations
- artifact and provenance requirements
- stop conditions
```

## Boundaries

No run begins from this direction alone.

No INT4.

No composition / seam / Claim C claim.

No M5 distractor-attractiveness experiment.

No V3 composite-gate retry.

No construction redesign.

If the baseline is not qualified, the run must fail closed before INT8 interpretation.

The Path A FP16 K=5 FAIL remains closed.

— Manager
