# What Kind of Smoothing? — Quantization Methods as Structural Probes

**Version:** v0.2. River and Canyon program. Research-question framing (model-free). C5 claim-risk review integrated.
**Status:** A question, not a result. It claims no finding, authorizes no run, and changes no gate.
**What this is:** the full, readable framing of a detail that also lives — compressed — in NORTH-STAR §2 ("the stressor is a basis, not a dial"). The North Star is the canonical frame; this companion note is the long-form of that one paragraph, retained (per Manager direction) because the §2 compression cannot carry the full reasoning. It is **not** a new direction, **not** a peer to the North Star, and **not** a separate research goal — it elaborates §2 and nothing more. Anchor: origin/main 7bc15f0. For Manager / Team Lead / CS consideration alongside NORTH-STAR v1.2.

---

## The question, stated plainly

The point is not that we know which quantization methods damage which behaviors. We do not. The point is that **this is the right question to ask** — and that the program is built to ask it honestly rather than to assume its answer.

The weak question, which the field can already answer, is: *does quantization reduce accuracy?* Broadly, at low enough bit-depth, yes. That tells us almost nothing about the structure of what a model learned.

The question worth asking is:

> **Which quantization method damages which behavior — and does the *pattern* of that damage reveal anything about the structure of the behavior?**

We are trying to grab a glimpse of that structure. Not a map — a glimpse. If method-resolved stress lets us see more than a single accuracy test can, that is the result we are reaching for. If it does not — if the damage is uninformative, or cannot be separated from artifacts of measurement — that is a valid outcome too, and the discipline below is precisely what lets us tell the two apart. The aim is to ask whether we can probe structure at all, while refusing to claim we have seen more than the probe can earn.

## What changed in the framing: a dial became a basis

It is easy — and we have done it — to picture quantization as a single dial: full precision at one end, INT4 at the other; turn it down, watch behavior degrade. On that picture the stressor is *scalar*, and a failure can say only one thing: *this behavior is fragile.*

That picture is impoverished, because quantization is not one operation. It is a family of different ways to coarsen a model, and the methods are not interchangeable: weight-only versus weight-plus-activation; INT8, INT4, FP8; AWQ (activation-aware, protects a small fraction of salient weight channels); GPTQ (layer-wise error-minimizing reconstruction); SmoothQuant (shifts quantization difficulty from activation outliers onto weights, enabling W8A8); rotation-based methods, codebook / adaptive methods, and quantization-aware training. Each makes a different choice about *what to preserve and what to discard*. Strip the analogy and the mechanical statement is the same: different methods perturb different parts of the computation, so they can damage different learned structure.

The moment the stressor is a **basis** rather than a **dial**, a failure stops being a verdict and becomes a coordinate.

## Why a basis beats a dial: verdict versus structural hypothesis

A single stressor yields a verdict — fragile or robust. A family of stressors, each perturbing the model differently, yields a *profile*: which methods a behavior survives and which it fails.

A profile is **not, by itself, structural evidence.** It is a structural *hypothesis* — a candidate statement about what kind of representation a behavior lives in — that becomes evidence only after the measurement confounds in the next section are ruled out, per rung. This is the same discipline the program applies at every prior layer: an alarm is sufficient to trigger interpretation, not to establish it; "not explained by the declared confounds" is not "therefore structural."

Two cautions bind the inference from *which method* to *what representation*, and they must travel with any reading of a profile:

- **Methods are entangled bundles, not clean scalpels.** It is tempting to say "survives AWQ, dies under GPTQ, therefore depends on what AWQ protects." But AWQ and GPTQ differ in several ways at once — calibration sensitivity, outlier handling, layer-wise error distribution — not only in "what they preserve." A survives-AWQ / dies-GPTQ profile is equally consistent with a calibration-sensitivity difference that has nothing to do with representation. A profile localizes structure *only to the extent the methods' other differences are controlled or matched.* Otherwise "the method is the resolving instrument" promises a resolution the instruments do not cleanly deliver.
- **Same-error identity must be checked per rung** (a note for the protocol that operationalizes this frame). Two methods producing the *same wrong answer* is the cross-method analog of survival-without-correctness; a profile built on retention counts that never check same-error identity per method would reproduce Paper 1's exact failure one dimension up. Every rung in a profile carries its own correctness and same-error-identity check before any cross-method comparison is permitted.

With those guards in place, *which* methods break a behavior can begin to say something about *what kind of representation* it depends on — as a hypothesis to be tested, not a verdict to be read off.

## The seam, correctly understood, is a profile — not a cliff

The deeper target was never "where does compositional behavior break." It is sharper:

> Does **linked** (compositional, multi-hop) behavior have a **different fragility profile** than its **component** operations?

If the single hops survive a method that breaks the composition, the *interesting* reading is that the composition is computed or stored in a structurally distinct place from its parts. But that reading has a mundane rival that must be ruled out first: **the composite task may simply be harder** — nearer a saturation or floor boundary — so it degrades earlier under *any* perturbation, with no structural separateness at all. "Different fragility profile" must be guarded against "the harder task degrades first." The differential is a structural *candidate* only after difficulty and headroom are matched across the component and composite items — exactly the load-matching the program already builds into its Tier-0 instruments. With that match in place, the seam is reframed from a single cliff one falls off at some bit-depth to a **difference between profiles** — a more specific, more falsifiable object than any scalar bit-depth test can support, but only as a candidate, never self-certifying.

## Why this makes the instrument more necessary — not less

The richer readout is more seductive, and that is exactly the danger. A cross-method difference has many candidate explanations, only one of which is the interesting one: real capability fragility; activation-outlier sensitivity; calibration mismatch; a scorer artifact; a baseline shortcut surviving (or not surviving) the smoothing; format instability; output-contract issues; a task saturated at ceiling or collapsed at floor. The more dimensions the probe has, the more ways it can *manufacture apparent structure from measurement artifacts.* So the certification discipline does not relax as the readout grows richer — it becomes *more* essential. The order is unchanged, and the method-richness reinforces every step of it:

1. Certify the baseline — it measures the intended construct.
2. Declare the quantization method as the *full* stress profile — format, weights-only versus weights+activations, bit-depth ladder, calibration-file hash, calibration distribution.
3. Run the *same items* under that profile.
4. Log correctness, same-error identity, scorer artifacts, and failure class — *per rung.*
5. Compare across methods *only after each rung is independently interpretable.*

A retention number without a complete stress specification is not a result. A fragility profile read off an uncertified baseline is not a finding. The probe is only as trustworthy as the least-certified point in it.

## The posture: a glimpse, not a map

This is the part to hold onto, because it is the easiest to lose once the framing gets exciting. We are **not** claiming that methods *do* damage different behaviors — that is the hypothesis, not a result. We are not claiming a seam exists, or that we have measured one. We are reaching to learn whether method-resolved stress *can* expose structure at all, and we are prepared for the answer to be "not legibly, not yet, not here." The aspiration is to glimpse how a capability is built; the discipline is to refuse to draw a map from a glimpse. The whole program is the machinery that keeps those two honest about each other.

## What this is not

- **A warrant.** This frame is a *question, not an authorization.* No future sweep may cite it as a reason to run, and no per-method result may cite it to upgrade itself from a coordinate to a structural claim. A ratified research frame defines what would be *worth* asking; it never licenses an experiment or inflates a finding. (This carries the claim ledger's negative-use discipline into the research frame.)
- Not a claim that quantization methods damage different behaviors (that is the question).
- Not a claim that any seam exists or has been measured.
- Not a claim the program can run this now: it is **pre-stress** — no certified, stressable baseline family exists yet (the synthetic key-value family at 3B/FP16 produced none across the candidates tried).
- Not an authorization for any run, method sweep, compression, or stress rung.
- Not a change to any gate. Certification still comes first; this framing makes that more true, not less.

## Where the program is, and the next real step

The instrument is **earned as an internal contribution** (Paper A); external promotion to "publishable" or "published" requires blinded review and is not asserted here. The seam is unearned, because there is nothing valid to stress yet. The next real step — when separately authorized — is *not* "run a method sweep." It is the precondition that makes a sweep meaningful: find or construct a baseline family that can both **clear the gate** and **be stressed** — one where a genuine operation is being performed, so that different methods can differentially damage it in a way that means something. Only against such a baseline does the method-basis become a probe rather than a noise generator.

The clean long-game frame, scoped honestly:

> Quantization methods are not merely deployment optimizations; they are candidate behavioral stress probes. Different recipes coarsen the learned surface differently. Within the task structure the program can actually instantiate and certify, comparing certified baselines under multiple declared stress profiles *may* let us begin to map which behaviors depend on which kinds of numerical precision — as a hypothesis to be earned per family, with cross-family generality explicitly unclaimed. We trust no fragility profile until the baseline and the measurement are certified.

The method-basis idea is general. The *evidence* any sweep could produce is scoped to whatever family clears the gate. The seam is the scientific question; the instrument is the condition for asking it honestly; the methods are how the question could be resolved finely enough to be worth asking at all — if the discipline above is held at every rung.
