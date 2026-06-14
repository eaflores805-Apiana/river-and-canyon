# Project Review — The River and the Canyon

*A one-document overview of the whole body of work: what it is, what holds weight, what the literature did to it, and what remains. For review and orientation. The papers and notes are the record; this is the map of the map.*

---

## What this project is

A pair of physics-analogy papers about transformer models — **The River and the Canyon** (weights as a frozen mountain, activations as water moving over it, training as the slow carving of stone) and a companion, **What Kind of Water Carves the Mountain?** (what different training media carve, and which structure survives when precision is removed) — plus two evidence-bound metrology papers (a stress-retention protocol and its first pre-stress result), a method essay, a literature audit, a scored index of implications, and a proposed experiment.

The mature one-line statement of what it became:

> The analogy is not the product. It was a **discovery tool** — it generated testable distinctions, those distinctions turned out to be real questions, and the durable contribution is a disciplined way to *ask* whether model capabilities are stable under stress, a clean way to *measure* it, and an honest account of what the picture does *not* let you claim.

The analogy is logically **unnecessary to defend** the conclusions, though it was necessary to **find** them. The scaffold came down once the building stood.

---

## The arc, honestly told

1. **Both papers were written, revised, and posted** (LinkedIn + GitHub). They do not overclaim: the geometric account is presented as interpretation, not validated mechanism.
2. **The literature was searched, four times, on the project's own claims** — and the claims correctly *shrank* each time:
   - **Fragility** (precision-demanding capabilities degrade more under quantization) — **established by the field**, not original here.
   - **Provenance** (training origin shapes capability and robustness) — **established with controls** (arXiv 2409.04556 holds data volume constant; 2509.21499 runs 3,331 parallel NL-vs-code fine-tunes). Not original here either.
   - **Format-sensitivity** (FP8 ≠ INT8 ≠ INT4) — established (arXiv 2411.02355, ~500K evaluations).
   - The honest result: the framework's value is **synthesis and anticipation**, not discovery. It independently converged on phenomena serious groups were already measuring — which is directional success for a *discovery tool*, not redundancy.
3. **The implications were collected** (seven sources, saturating at 2/0/0 new in the last three rounds), **scored for evidence not excitement**, and **stress-tested against several rounds of feedback**. The center of gravity never moved.
4. **The probe was hardened** through real corrections — a metric-symmetry fix (the protocol had been endorsing a confound), format/calibration specification, a precision-demand task rule, three predeclared outcomes, and a parallel-diagnostic-tracks restructure.

Throughout, the discipline held: claims were never allowed to outrun evidence, and the framework was *attacked* (force, routing, prior art, confounds, rivals) rather than defended — surviving by shedding non-load-bearing claims, which is what a robust structure does under stress.

---

## What holds real weight

By the project's own test — *does it survive even if the river-and-canyon account is wrong?* (mechanism-independence) — the durable core is small and unglamorous, and that is the honest signature of a framework that was filtered hard:

- **A8 — the live question.** *Does retention under stress predict deployment reliability better than peak benchmark accuracy?* Mechanism-independent, open (the clean head-to-head appears undone), useful regardless of originality, and squarely in qualification-engineering territory. This is the load-bearing contribution.
- **The rescue test (B13) and cross-stress validation (B28)** — the cheapest, most direct follow-ons; mechanism-independent; they would distinguish a real fragility signature from a quantization-format artifact.
- **The boundary markers** — what the framework says you *don't* need to worry about (FlashAttention is safe; weights are immutable at inference; claims scoped to post-training quantization only). A framework that only sounds alarms is a smoke detector with anxiety; clean negatives are what earn trust.
- **The method itself** — find the variable underneath, render it as physical structure, read off the testable question, then **de-image** (strip the metaphor, keep only what survives as bare mechanism), and score for evidence rather than excitement. At this stage the methodology is the contribution as much as any single claim.
- **The metrology protocol, now written.** The survival-≠-correctness blind spot — the one durable residue of the speculative work — is now a staged, fail-closed stress-retention method (*Survival Is Not Correctness*), with a first pre-stress result on it (*Correctness Is Not Constructibility*): a two-hop construction's constructibility floor, mapped at full precision and found not cleared. Mechanism-independent; this is where the discovery tool's output became an evidence-bound deliverable.

Everything vivid and exciting — silent alignment decay, split-domain silicon, dynamic-precision hardware, the causal ladder — is **mechanism-dependent and clusters in the speculative tier.** Excitement and evidence came out *inversely correlated*, which is exactly why the index scores for evidence.

---

## The honest status

| Component | Status |
| --- | --- |
| Both papers | Written, posted, calibrated (no mechanism overclaims) |
| Literature positioning | Done; claims shrank to synthesis-not-discovery |
| Implications index | Converged (~52 rows), scored, saturated, feedback-stress-tested |
| Fragility probe | Hardened, format-aware, artifact-guarded, adoption-ready |
| **Empirical result** | **Baseline-constructibility data only.** One 3B model run at full precision (the two-hop cells behind *Correctness Is Not Constructibility*); the construction's floor is mappable but not cleared. **No compression-stress retention data** — the seam is unrun. |
| Standing governance note (Hash Integrity Is Not Construct Validity, v0.7.2, released) | Methodological discipline at the artifact/concept layer, distilled from the Path A (rung-uniform) episode — a faithful run whose sealed schedule mapped eight rung labels to one structure. Adopts a shown-semantic-read gate now required for every model-facing readiness packet. *Hashes bind bytes; they do not bind concepts.* Not Paper 4; no model-behavior claim. |

The experimental program is now complete *as a design*: a baseline (Tier 0) plus a fan of parallel diagnostic tracks (rescue, uncertainty, cross-stress, prompting-recovery), then provenance and targeted-intervention tiers — **every tier contingent on a clean baseline signal — the baseline-constructibility cells have now run (the floor is mappable but not cleared), and the compression sweep at the center has not.**

This is the project's defining honesty and the reason the rest is trustworthy: it stops exactly where the evidence stops. The strongest claim is not "I proved how transformers work." It is "a disciplined analogy led to a clean, testable question that stands on its own."

---

## What remains

> **Update — June 9, 2026.** Part of this has now happened. The baseline-constructibility tier was run and written up as two papers (*Survival Is Not Correctness*, the protocol; *Correctness Is Not Constructibility*, its first pre-stress result). They moved the frontier rather than retiring it: the tested two-hop construction's constructibility floor is mappable but **not cleared**, so the next genuine event is no longer "run the baseline" but "certify a constructible baseline a stress reading could trust." The bit-depth sweep described below is still the goal; the metrology work showed it has a precondition not yet met. The prose below remains accurate for that *compression sweep*, which is still unrun.

> **Update — June 10, 2026.** The precondition now has its instrument. *Certification Before Retention* (Paper 3, released v1.0) defines the fail-closed D1–D7 certification gate a baseline must pass before any stress reading on it is interpretable, and the B1 v2 validity harness — merged and locked, with a bit-identical Paper 2 regression behind it — supplies the provenance substrate the protocol requires. Paper 2 itself moved from release candidate to released v1.0. The next genuine event is unchanged in kind but sharper in form: select a candidate, lock a threshold sheet against the released protocol, and run the certification — each under separate authorization — and only a certified baseline unlocks the sweep.

> **Update — June 12, 2026.** The first model-facing run under the Paper 3 framework — *Path A (rung-uniform)* — executed faithfully and surfaced a different failure mode from the ones the framework was built to catch. The sealed instrument did its job (pinned generator, two-pass materialization, pre-inference hash recording, zero aborts, byte-perfect post-run verification); the sealed schedule, however, mapped all eight rung labels `L01..L08` to one default structure, so the run measured one L01-equivalent surface eight times rather than eight distinct ones. Verification held the run before citation; Manager disposition closed it as a *schedule-layer finding*, not a breadth result. The case is now citable only under its binding characterization, and the scope sentence travels with it: **Breadth is untested under the current sealed schedule.** The episode produced a third methodological discipline alongside the project's two existing ones (*survival is not correctness*; *correctness is not constructibility*) — **hash integrity is not construct validity**: a path/hash-valid artifact can fail to instantiate the concept it is named for, so concept-fit needs its own gate, separate from byte-fit. The discipline is now a standing governance note ([`governance/standing/HASH-INTEGRITY-IS-NOT-CONSTRUCT-VALIDITY-v0.7.2.md`](governance/standing/HASH-INTEGRITY-IS-NOT-CONSTRUCT-VALIDITY-v0.7.2.md), v0.7.2, Manager-accepted) plus a shown-semantic-read gate that is now required before any model-facing readiness packet routes to Manager. The framework's pattern held: a load-bearing claim ("L01–L08 breadth") was shed when the artifact didn't instantiate it, and the downstream verification layer caught what the upstream authorization layer had not asked. Standing governance rule; not Paper 4; no model-behavior claim. The compression sweep remains blocked — and the bound has tightened from "needs a certified baseline" to "needs a certified baseline *and* a schedule that defines the concept its labels imply." That is the load-bearing methodological gain made standing.

Not more design. The design converged several rounds ago; the implications, the insights, and the protocol-refinements have each saturated. The single remaining move that changes the project's *state* rather than its *prose* is empirical:

> **Run the Tier 0 pilot — one open-weights model, a bit-depth sweep, matched broad/narrow pairs under comparable scoring strictness, the three predeclared outcomes — or hand the protocol to someone who will.**

The probe is runnable by one person without a cluster. It is built to be able to come back *no*. That is the next genuine event. Everything upstream of it — the papers, the index, the hardened protocol — is complete and waiting on it.

The river pointed true; the field was standing where it pointed; and the one place the field is thinnest — *how capability should be qualified* — is the place the framework's forward edge now honestly lies, and the place its author is most equipped to stand.

---

*Repository: the two papers (`writing/the-river-and-the-canyon/`, `writing/what-kind-of-water/`), method and audit notes plus the scored implications index and the fragility-probe protocol (`notes/`). Status and start-here in `STATUS.md` and the root `README.md`. Compiled for review, E. A. Flores / Apiana AI, Inc.*
