# Claim Ledger — v0.1

*A control sheet, not an essay. It separates what this project can currently infer from what would follow if the protocol works. Companion to the full record (`inference-ranking.md`); this is the one-page front door. Offered as a reusable claim-control pattern for framework-driven work — not a method for all of AI research.*

**Method — a collected multi-pass convergence audit.** The rankings in this ledger were not assigned from a single authorial pass. They were collected from multiple feedback passes using different evaluation criteria (evidence × centrality, impact × certainty, evidence × practical-importance, and others), then reconciled by *convergence* rather than by raw score. The author's role was to gather, compare, and audit the outputs — not to assign the final hierarchy from scratch. Claims that remained stable across harder and softer axes were treated as more durable than claims that scored highly only under flattering or weakly falsifiable criteria. So the ledger records what survived collected ranking pressure, not what the author wished were strongest.

*Three caveats keep this honest. (1) The prompts still shaped the passes — the author chose what to ask, so "collected" is not "independent of the author." (2) The sources were not blind to the work or to prior passes, so convergence among them is weaker than convergence among blinded reviewers; a shared prior may pull toward agreement. (3) Reconciliation was after-the-fact and author-run — selecting which convergence to record and which overclaims to flag is itself a judgment layer, less biased than assigning scores but not zero. This is therefore an informal-but-structured convergence audit, not blind peer review. And convergence shows a claim is robust to how it is evaluated — not that it is true. That still requires data.)

---

## 1. Purpose

Keep the project honest about what it has and hasn't earned. The ledger sits between the protocol and the roadmap like a circuit breaker: before talking about what this would change, state what is actually known.

## 2. The five-layer stack

| Layer | Job |
|---|---|
| Analogy paper (*River and Canyon*) | Generates the question |
| Synthesis paper (*What Kind of Water*) | Organizes it into two axes |
| Protocol (*Fragility Probe*) | Tests one slice |
| **Inference ledger (this)** | **Governs what can be claimed before data** |
| Implications roadmap | Maps what follows *if* the test works |

## 3. Claim-status table (the heart)

| # | Claim | Status |
|---|---|---|
| 1 | Peak accuracy is an incomplete qualification metric | **Field consensus** (multi-source; not ours) |
| 2 | Quantization damage is non-uniform; salient weights matter | **Field consensus** (AWQ/SmoothQuant) |
| 3 | Quantization is the *inverse problem* to training — a stress instrument | **Original framing** (ours; evidence underneath is the field's) |
| 4 | Fragility localizes to early method/execution steps | **Empirical anchor** — concentrated risk: one author cluster, unreplicated |
| 5 | Precision-demanding tasks retain less under declared quantization stress than matched broad tasks | **Open hypothesis** — Tier 0 target; unrun |
| 5b | Stress-retention predicts deployment reliability better than peak accuracy | **Open qualification hypothesis** — requires a later validation study; not tested by Tier 0 |
| 6 | Provenance shapes the mix, not the fate (axes separable) | **Open hypothesis** (untested as a claim) |
| 7 | Wide basins / narrow ridges / carved structure | **Interpretation** (language, not measured mechanism) |
| 8 | "Small dose of sharp water" (LoRA / recovery / grounding rhyme) | **Speculative extension** (loose pattern) |
| 9 | Evaluation becomes a retention profile; capability-aware serving; train-for-retention | **Conditional implication** (holds only if #5 resolves positive) |

Durable center to defend: **#3 + #5** — quantization as stress instrument, and the Tier 0 test of whether precision demand predicts differential retention. **#5b is the forward qualification hinge, not yet tested by Tier 0.** All survive even if #4, #6, #7, #8 are refuted; none depends on #4 replicating.

## 4. Three inversions (portable hygiene rules)

1. Beautiful prose can carry weak evidence.
2. Strong evidence can have concentrated replication risk ("has citations" ≠ "is robust").
3. Flattering summaries are often least falsifiable.

## 5. Governing rule

**Implications are conditional. They are not evidence.** Inference first, implication second, roadmap only under condition.

**The carving/imperfection analogy is retained only as a heuristic for generating measurement targets. It is not evidence for internal defect classes.** Any proposed failure mode it suggests must be translated into a behavioral signature, a minimal intervention that should change the behavior, and a falsification path *before* it enters serious work. Phrases like "unevenly supported learned structure" are interpretive at most — useful as a sentence, never as a thesis, and never a claim about internal mechanism. This guardrail exists because the analogy is generative and therefore tempting to over-read; the discipline is to let it ask *where to look* and never let it answer *what is internally wrong*. A corollary, recorded after an audit of the analogy's wider output: the analogy can be mapped post-hoc onto a long list of known failure families, but this is a sign of its **flexibility, not its validity** — a frame loose enough to fit almost any known error after the fact has little discriminating power. That exploratory output may be parked as an open question (see `notes/open-question-uneven-support.md`), but it does not upgrade the analogy's claim status: it remains a question generator, not evidence, taxonomy, or mechanism.

## 6. Stop-rule

**The next update to this ledger requires data, not another ranking pass.** Five passes have not moved the substance ordering; ranking is not measurement. The next real input is a result.

This ledger updates only when new evidence arrives — specifically: (a) a protocol run, (b) independent replication of a cited result, (c) external critique that changes a claim's status, or (d) new literature affecting a claim category. Another ranking pass over the same material is not a trigger.

## 7. Open risks

| Risk | Statement |
|---|---|
| **Hinge validation** | Stress-retention is not yet shown to predict deployment reliability better than peak accuracy. The instrument measures retention cleanly; that is not proof retention *matters*. If retention is clean but irrelevant, the result is a precise ruler for something nobody needs. Tier 0 can show differential retention; it cannot by itself show deployment reliability. |
| **Stress generality** | Quantization is the *first clean probe*, not the whole family. Pruning, distillation, LoRA merges, long-context pressure, tool-use, distribution shift, decoding and calibration drift are separate stresses requiring separate tests. Do not generalize a quantization result to "fragility" in general. |
| **Profile gaming** | Any metric that becomes a gate becomes a target. If retention profiles become adoption gates, task pairs must be partly held out, scorers versioned, calibration artifacts hashed, and benchmarks periodically refreshed — or the profile will be optimized rather than measured. |

---

## Worked example — one claim through the ledger

**Claim:** "Models silently lose exact-reasoning steps under low-bit quantization while staying fluent."

- As **field consensus** (#1): "peak accuracy is incomplete / robustness ≠ accuracy" — *supported, multi-source.* ✓ may state plainly.
- As **empirical anchor** (#4): "...and it localizes to early execution steps" — *one research line, unreplicated.* ✓ may cite, must label concentrated-risk.
- As **original framing** (#3): "...which is why quantization works as a *measurement instrument* for load-bearing structure" — *ours; the reframe, not a finding.* ✓ may claim as framing.
- As **conditional implication** (#9): "...so model cards should report retention profiles" — *only if #5 holds.* ✗ may NOT state as present-tense recommendation; must stay "if the test works, then."

The same sentence spans four categories. Mixing them — letting the conditional implication borrow the field consensus's authority — is the failure the ledger exists to block.

---

**The symmetry that makes this legitimate:** the protocol asks whether a *capability* retains performance under different stress conditions; the ledger asks whether a *claim* retains credibility under different evaluative pressures. The project did not only argue for stress-testing — it applied stress-testing to its own claims. That is the difference between a claim ledger and a diary: a diary says "here is what I think"; the ledger says "here is what survived repeated pressure."

*This ledger makes the project's claim-status inspectable. It does not solve overclaiming; a ledger can be ignored or cherry-picked. It makes status visible; it does not make readers honest. Offered as how this project kept its claims separated — not as a new constitution of epistemology.*
