# The River and the Canyon

A pair of essays that build a physical analogy for how large language models work — then stress-test it, propose a way to measure it, and reflect on the method itself.

## The work, in order

**1. The River and the Canyon**
A physical analogy for a transformer: weights as a frozen mountain, activations as water moving over fixed stone, training as the slow carving of the rock, inference as water running over stone that no longer moves. The second half deliberately tries to break the analogy to find exactly where it stops being the territory.
→ [`writing/the-river-and-the-canyon/`](writing/the-river-and-the-canyon/) — **new here? start with the lean edition** (`-lean`), the whole picture in one fast read; the full paper develops each step and stress-tests every claim. Both come in Markdown (reads in-browser), PDF (typeset), and Word. Figures are in `assets/`.

**2. What Kind of Water Carves the Mountain?** *(companion)*
The first paper followed only one river: human language. This one asks what changes when the water changes — code, video, simulation, action — and finds a second axis underneath the obvious one. Not just *where* a capability's structure came from (provenance), but *how much precision it needs to survive* (fragility), with quantization as the instrument that exposes the second. The compact claim, and the guard against over-reading it: **provenance shapes the mix, not the fate.** It is framed as a perspective worth testing, not a finished framework.
→ [`writing/what-kind-of-water/`](writing/what-kind-of-water/)

Read the two in order; the second assumes the first.

## The metrology papers

Running the baseline tier of the program above produced four evidence-bound papers that stand on their own, without the analogy — the method, its first result, the certification protocol that gates any future stress reading, and an instrument paper distilled from the first time that protocol was exercised on a baseline its own authors were trying to construct.

**Survival Is Not Correctness** — the metrology *method*. A staged, fail-closed protocol for stress-retention evaluation. It makes operational the one blind spot the speculative work left standing: a capability that *survives* stress is not thereby *correct*, so a retention number that does not log baseline-correctness, stressed-correctness, and same-error identity together can score stable wrong behavior as robustness.
→ [`papers/paper1-survival-is-not-correctness/`](papers/paper1-survival-is-not-correctness/) — Markdown and PDF; figures in `assets/`.

**Correctness Is Not Constructibility** — the first *result* built on that method (released, v1.0). Pre-stress baseline mapping of a two-hop construction on one 3B model at full precision: surface correctness is not constructibility, and the tested construction's constructibility floor is structured, bounded, and mappable but **not cleared**. That floor is the precondition any compression-stress reading depends on, so the result sits *upstream* of the seam, not on it. The compression seam itself remains unrun and unclaimed.
→ [`papers/paper2-correctness-is-not-constructibility/`](papers/paper2-correctness-is-not-constructibility/) — Markdown and PDF; figures in `figures/`.

**Certification Before Retention** — the certification *protocol* (released, v1.0). Papers 1 and 2 leave a gap: even a correct, constructible single-hop baseline is not automatically a valid *substrate* for retention measurement. This paper closes it with a fail-closed conjunction of seven pre-registered gates (D1–D7) — correctness above emission bias, shortcut resistance, strict-scoring stability, abstention calibration, load matching, runner-backed provenance, and a sensitivity/power floor — with a locked per-candidate threshold sheet, a data-access firewall, and negative certification as a result of record. It ships the ruler; applying it to any candidate remains separately unauthorized, and no candidate has been certified.
→ [`papers/paper3-certification-before-retention/`](papers/paper3-certification-before-retention/) — Markdown and PDF; figures in `figures/`.

**Before Retention: A Fail-Closed Validity Gate for LLM Stress-Retention Evaluation** — the instrument *paper* (released, v1.0). When the certification protocol from Paper 3 was first exercised against a candidate single-hop baseline (a synthetic key-value family on Qwen2.5-3B at FP16), the gate refused a baseline its own authors were trying to construct: surface accuracy looked usable, but a per-item construct-validity read showed the abstention signal had collapsed under a query-side lever — the baseline no longer measured the intended capability. A separate per-item read, on a different candidate, also *prevented* a false refusal that a scorer artifact would have caused (a CAL-E reversal). Paper A turns those two worked episodes into a fail-closed validity gate whose output is a *route decision* (`pass`, `needs-repair`, `quarantine`, `refuse`), never a bare retention number, with construct-validity enforced at the baseline before any retention claim. Scope is binding: one synthetic family, one model, pre-stress, no compression rung run; the non-vacuousness claim is suggested by two worked episodes, not established by a standing mechanism (the standing rejection-audit module — the same component external reviewers named as the highest-value next build — is specified, not built). It ships the gate; certifies no candidate; authorizes no run.
→ [`papers/paper-a-before-retention/`](papers/paper-a-before-retention/) — Markdown and PDF; figures, sections, supplement, and bundled governance inside.

These four are the *metrology* set (method ↔ first result ↔ certification gate ↔ instrument distilled from exercising the gate); the two essays above are the *analogy* pair (the picture ↔ what the water carves). The analogy pair points; the metrology set reports only what the evidence earns.

## Tier 1 instrument

Paper A's gate has also been converted into a reusable architecture under [`tier-1-instrument/`](tier-1-instrument/): the **Eval-Validity Gate Tool Spec** (the nine-gate architecture; G1–G5 implemented in Paper A, G6–G9 specified) and the **G6 Standing Rejection-Audit Spec** (the first missing module — how the instrument audits its own "no" without circularity, via at least one of three mechanized-independent channels: blind second reader, pre-registered output-classification schema applied without route knowledge, or external ground-truth labels). The architecture inherits Paper A's scope exactly — one family, one model, pre-stress — and is held under the same boundary as the paper: human semantic judgement (construct-validity, scorer-divergence adjudication, independent rejection-audit read) stays human; only independence and bookkeeping mechanize. The next model-free build target is the G6 standing audit; no software is built yet. Specs live in `tier-1-instrument/specs/`; the structure-of-the-organization, inventory, and move record live in `tier-1-instrument/organization/`. A secondary finding track, [`finding-tracks/cal-q-format-sensitive-abstention/`](finding-tracks/cal-q-format-sensitive-abstention/), preserves the CAL-Q finding (the format-sensitive abstention collapse that prompted Paper A's worked refusal) as a model-free diagnostic plan — explicitly future research, not a rerun of the closed certification route. The closed D4 route lives at [`archive/d4-closed-route/`](archive/d4-closed-route/) for provenance.

## Standing governance note

**Hash Integrity Is Not Construct Validity** — a methodological companion to Papers 1–2, released as a standing governance note (v0.7.2). It names a third project discipline at the artifact/concept layer: an artifact's bytes can be perfectly hash-bound — pinned, provenance-tracked, mutation-proof — and still fail to instantiate the experimental concept it is named for. The note adopts a *shown semantic-read* gate for every load-bearing artifact before any model-facing execution, with a worked example, a mechanical-rendering floor that prevents the gate from becoming prose ritual, a detection signature (improbable identity across nominally distinct conditions is a semantic-validity alarm, sufficient to trigger review but not necessary for mismatch), and a designator mechanism (put the qualifier inside the result name). The case study is Path A (rung-uniform), closed by Manager disposition as a schedule-layer finding: a faithful run whose sealed schedule mapped eight rung labels to one structure, so the run measured one surface eight times rather than eight distinct surfaces. Standing record only — not Paper 4, not a publication-ready paper, not a model-behavior claim. *Hashes bind bytes; they do not bind concepts.*
→ [`governance/standing/HASH-INTEGRITY-IS-NOT-CONSTRUCT-VALIDITY-v0.7.2.md`](governance/standing/HASH-INTEGRITY-IS-NOT-CONSTRUCT-VALIDITY-v0.7.2.md) — Markdown and PDF; figures in `governance/standing/figures/`.

## Notes and proposals

**No Mountain in the Sentence** — a short companion essay on the *method* behind the papers: the discipline for trusting an analogy exactly as far as it earns. It states one rule (say the claim with no mountain in the sentence) and three questions, then applies them to the mountain analogy itself.
→ in [`writing/the-river-and-the-canyon/`](writing/the-river-and-the-canyon/)

**A Fragility Probe for Carved Structure** — a *proposed* experiment (not a completed result) for testing one prediction of the second paper: whether precision-demanding capabilities retain less of their full-precision performance under quantization than matched broad ones. A small, runnable, falsifiable pilot, with a pre-declared decision rule that allows a flat result.
→ [`notes/fragility-probe-protocol.md`](notes/fragility-probe-protocol.md)

**Analogy as Scaffold** — a method note on using a physical analogy without letting the picture smuggle claims into the mechanism: three registers kept separate (analogy for questions, mechanism for claims, measurement for results), and the three risks the image imports (reification, false continuity, imported agency).
→ [`notes/analogy-as-scaffold.md`](notes/analogy-as-scaffold.md)

**Capability Under Load** — a seed note (explicitly speculative, not a result) on a downstream implication: that capacity and *usable structure* may be different things — a model can have representational room for a capability without having carved a structure that bears load under stress.
→ [`notes/capability-under-load.md`](notes/capability-under-load.md)

**Where things stand** — current status of each piece and the one open question (does provenance predict fragility beyond task-type?) is in [`STATUS.md`](STATUS.md); what the post-publication literature search found — the fragility axis is established, the provenance question is open — is in [`notes/literature-notes.md`](notes/literature-notes.md).

**Parked open question — the uneven-support pattern** — a side note, explicitly *not* a finding: the carving analogy can be used to generate a long list of failure patterns, but the high match-rate to real LLM errors is a sign of the frame's flexibility, not its validity (it is post-hoc, and reduces to field-established families). The note keeps the intuition while stripping its authority, and reframes the durable residue as *behavioral parameters* rather than defects. Its raw object-to-think-against is a companion list. The guardrail for the whole branch: *reach is not validity.*
→ [`notes/open-question-uneven-support.md`](notes/open-question-uneven-support.md) and [`notes/carved-path-pattern-list.md`](notes/carved-path-pattern-list.md)

**Claim Ledger** — for claim status and epistemic boundaries: a one-page control sheet that sorts every major claim into field consensus, original framing, empirical anchor, open hypothesis, interpretation, or conditional implication — and states what would change each. It exists to stop the project from being misread, not to impress. The governing rule: implications are conditional; they are not evidence.
→ [`notes/claim-ledger-practice-note.md`](notes/claim-ledger-practice-note.md)

## Governance diagrams

Six diagrams make the project's discipline legible at a glance — what it is, what it isn't, what's left to do, and what each result would mean. Each owns one failure mode: the **lineage** (what the analogy generated and what unequally survived), the **boundary** and the **Venn** (what the method can and cannot decide, in table and spatial form), the **gap map** (unexplored areas by field), the **decision matrix** (what each Tier 0 outcome means, pre-registered), and the **status ladder** (what promotes a claim, so one run is not mistaken for a framework). The set, with a gallery and the governance finding behind the Venn, is in [`diagrams/`](diagrams/).

## On method

The papers share one discipline: the analogy is allowed to be vivid only as long as the mechanism underneath it stays in view. Claims are sorted by how well the evidence actually supports them, limits are stated plainly, and where the work reaches past what is established it says so. The picture is a way of asking sharper questions, not a machine for predicting what will work. Where the work proposes rather than demonstrates — the provenance-by-fragility interaction, the fragility probe, the capability-under-load idea — it is marked as a proposal, not a result.

*Written by E. A. Flores, Apiana AI, Inc. Licensed CC BY-NC 4.0.*
