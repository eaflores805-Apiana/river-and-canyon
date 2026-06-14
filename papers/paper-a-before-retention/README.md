# Before Retention

**A Fail-Closed Validity Gate for LLM Stress-Retention Evaluation**

E. A. Flores · Apiana AI, Inc. · River and Canyon program

---

## What this is

This repository holds **Paper A** — an *instrument / measurement / experience paper* describing a fail-closed validity gate for stress-retention evaluation of language models, and a worked case in which the gate refused a baseline its own authors were trying to construct.

The paper's argument, in three lines:

> The gate refused a baseline the authors wanted to accept.
> That refusal was justified by per-item construct-validity evidence.
> The same discipline also prevented a false refusal in a separate case.

A retention score (how much of a capability "survives" compression) is a comparison against a baseline. If the baseline rests on a shortcut, saturates at ceiling, or is mis-scored, the retention number inherits the defect and reports it as preserved capability. This paper enforces **construct validity at the baseline** — whether the baseline measured the intended capability at all — as a precondition on any retention claim, and returns a route decision (including *not safe to compare*) rather than a score.

## Scope and status (read before citing)

This is an **instrument paper**, not a methods paper or a product. It is scoped precisely:

- **One** synthetic key-value task family.
- **One** open-weights model (Qwen2.5-3B, FP16).
- **Pre-stress**: no certified baseline has been carried through an executed compression rung.
- The demonstrations are the gate catching defects in **baselines the authors themselves constructed** — which bounds the non-vacuousness claim (see §6.2).

The paper does **not** claim a compression-fragility result, a "compositional seam," a validated general method, or a product. Establishing cross-family generality, demonstrating the gate on an externally constructed evaluation, and carrying a certified baseline through a stress rung are stated as required future work (the planned follow-on, Paper B).

## Repository layout

```text
paper-a/
  paper/
    paper.md            the canonical draft (v0.6, refusal-first)
    paper.pdf           typeset version for review
  figures/
    fig1_certification_box.{png,svg}      the empty certifiable region (keystone)
    fig2_reversal_confirmation.{png,svg}  per-item read reverses one case, confirms another
  sections/             editable section masters (provenance; the paper re-assembles these)
    section-2-background.md
    section-4-instrument.md
    section-5-rejection-audit.md
  supplement/           supporting data manifest (assembly in progress)
  governance/           the decision records that govern the paper's scope and framing
    MANAGER-DECISION-PAPER-A-NOW-v0.1.md      write Paper A now, plan Paper B later
    MANAGER-DECISION-VENUE-OPTION-2-v0.1.md   instrument/measurement/experience, not methods
    VENUE-DECISION-MEMO-PAPER-A-v0.1.md       the memo that surfaced the venue decision
    methodology-record.md                      the failure->control history of the program
```

## The two figures

- **Figure 1 — the certifiable region is empty.** Clean accuracy versus defective discrimination for five calibration candidates. Four content-lever candidates sit at the ceiling wall (no headroom for a retention measurement); the one off-ceiling candidate fell to the discrimination floor (its construct collapsed). No candidate lands in the certifiable region — this is why the program is pre-stress.
- **Figure 2 — the same discipline reverses and confirms.** In one case (CAL-E) the per-item read lifted an aggregate that looked like a failure (a scorer artifact — refusal averted); in another (CAL-Q) it confirmed an aggregate collapse as real (refusal upheld). The identical aggregate signature meant opposite things; only the per-item read distinguished them.

Both figures are generated from the program's run records and report *evidence about the instrument, not about the model*.

## A note on provenance

`paper/paper.md` is the assembled view of the paper. The files in `sections/` are the editable masters for the carried-forward material (§2 background, §4 instrument, §5 rejection audit); edits to that material are made in the masters and the paper is re-assembled. This mirrors the program's own discipline: the artifact and its provenance are kept separate and traceable.

## Status of this draft

Version 1.0 — complete and internally consistent. The contribution is a protocol, one worked refusal case, an honestly-bounded non-vacuousness claim, and a core component (the standing rejection-audit) that is specified but not yet built. The paper states its claims at exactly the strength the evidence supports. The work that would strengthen the contribution — building the rejection audit (model-free), an external demonstration, or a stress rung — is named in the paper and remains the real next increment. Maintained here as the honest instrument-paper record; not yet submitted to a venue.

---

*River and Canyon program · Apiana AI, Inc. · model-free · pre-stress · this repository authorizes no experimental runs.*
