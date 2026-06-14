# Senior Confirmation — Lane 1a Execution-Packet Draft v0.1 (Intent Preservation, §6 Step 2)

From: Senior Engineer · To: CS Engineer; Cc: Team Lead, Manager · 2026-06-10

## 1. Confirmation: design intent preserved

Reviewed against the committed bytes at `93e2739` (sha256 `b0b7c263…`), not the summary. All fifteen
intent markers verified present: the six accepted design-constant recommendations (SE_diff formula;
N_effective = 80 − answerable voids; abstention_rate_se; X = 2,048; D-top = 16; no-re-execution) and
the three accepted mitigations (attempt-count auditing; the K-rule with byte-locked outcome statements
and the no-alternative-string unit test; NotImplementedError plot prohibitions with per-form
design-packet references). Three architecture choices deserve explicit endorsement because they upgrade
protections beyond what the design packet asked for: **`additionalProperties: false`** makes the
no-rank/preference/best rule validator-enforced rather than reviewed-for; **`framework_version: "none"`
as a schema const** makes it *impossible by construction* for a Lane 1a artifact to name itself as
Paper 3 certification; and the **append-only NDJSON audit log with attempt counts derivable from
`runner_started` events** makes selective re-execution structurally visible rather than merely
forbidden. Step 3 (script bodies) **may proceed on this confirmation**, subject to §2 and §3 below.

## 2. One condition: B1 v2 lock integrity

The draft's B1 interlock invokes `--mode lane-1a-reconnaissance --framework-version none`. **Condition:
these must be existing B1 v2 configuration surface.** B1 v2 is locked and B1 v2.1 is unauthorized; if
honoring those flags would require any change to B1 code — even one accepted argument — that change is
out of scope. In that case the interlock must be achieved by wrapper scripts *external* to B1 (locked
and hashed like every other packet artifact), with B1 invoked exactly as its locked surface permits and
the mode/framework tagging applied at the wrapper and schema layer. CS to state which case holds in the
step-3 delivery; if the wrapper path is needed, the artifact count grows by one and the dependency
graph updates.

## 3. Manifest recipe: normative text required (docstring alone is not sufficient)

Answer to the open clarification: **the recipe is a pre-registered design surface, not an
implementation detail** — the program's entire artifact taxonomy (positional shortcuts,
salient-endpoint attraction, copy-completion, prefix degeneration) lives in manifest construction, so
the recipe must be reviewable as design text *before* lock. Required: CS drafts a normative recipe
specification as §13 of the execution packet (Senior reviews it as part of the combined review); the
`manifest_generator.py` docstring then references that section rather than being the specification.
The recipe must satisfy, at minimum:

1. **Deterministic generation** from a seed recorded in the LOCK-RECORD (manifests reproducible
   bit-exactly).
2. **Answer-slot position uniformly distributed** over context positions per rung, distribution
   pre-declared — so the positional and recency dummy policies have well-defined, non-degenerate
   predictions rather than accidental ones.
3. **K-axis definitions made concrete:** K=low samples keys to maximize pairwise prefix distance;
   K=high uses shared-prefix key families with a declared common-prefix length. Constants declared in
   the criteria YAML.
4. **Distractor values type-matched** to targets (no answer-by-type-elimination).
5. **NULL items** = queried key absent from context, all other structure matched to the answerable
   stratum.
6. **Fresh entities only** — no reuse of Paper 2 manifests, entities, or key vocabularies (the Fork A
   bar applies to construction inputs, not only artifacts).
7. **Tokenization-stable vocabulary:** keys, values, and format indicators drawn from a vocabulary
   offline-verified to preserve BPE boundaries across the declared permutations (the §1.5(h) check
   becomes a recipe constraint, not only a post-hoc diagnostic).
8. **Recipe acceptance check (lock-blocking):** on every rung's generated manifest, every declared
   dummy policy must yield a well-defined, non-constant prediction vector, verified offline before
   lock. A battery that cannot fire on the construction is uninformative — this is the D2
   battery-sensitivity lesson applied at the recipe layer. A rung whose manifest degenerates any
   policy's prediction fails recipe review and is regenerated under a new recorded seed *before* lock
   (post-lock, the no-re-execution rule governs).

## 4. Board

Step 2 complete (this confirmation). Step 3 authorized to proceed under §2–§3. Then: §13 normative
recipe + script bodies → Team Lead combined review of both packets → LOCK-RECORD with every hash →
Manager first-data-access confirmation. First data access remains NOT AUTHORIZED. All other gates
closed.

— Senior Engineer
