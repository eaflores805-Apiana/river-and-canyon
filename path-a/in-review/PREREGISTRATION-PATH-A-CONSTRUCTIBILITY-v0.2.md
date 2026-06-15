# PREREGISTRATION-PATH-A-CONSTRUCTIBILITY-v0.2

**E. A. Flores**, Apiana AI, Inc. — June 15, 2026
*River and Canyon · Path A. Prepared by the Senior Engineer. FP16-only constructibility pre-registration **shell**.*

> **v0.2 revision note.** Folds CS feasibility edits and C5's preloaded claim-risk rulings into v0.1 (`eb3dee05…`): CERTIFY-as-validity-verdict at point of use, per-item-validated global R1, the CI-based decision rule, threshold-vs-dominance provenance separation, dominance-threshold rationale, other-rate-ceiling scoping, the locking-≠-authorization restatement, and the substrate-infeasibility carry. C5's HOLD on v0.1 was **artifact-access** (the bytes were not readable), not content; v0.2 is to be filed byte-exact for C5 to re-review the actual object.

## 1. Scope / negative-use

A lock-before-look declaration of the construction, admissibility gate, scoring, floor, outcome rules, and forbidden interpretations for a **single FP16 constructibility test at the Manager-locked parameter point**. It exists so the analysis cannot be tuned to results after they are seen.

**This is a shell.** It locks rules, values, and the exact instrument bytes; it leaves item realization to declared open slots (§ open slots). It contains no task items, concrete tokens, prompt templates, model-execution command, or compression rung.

**This does not authorize a run.** Locking this shell is not execution and not authorization. A run requires the Manager's by-name authorization with lock-before-look, the §13 fixture-mode assertion, and the open slots realized. The Senior Engineer drafts this artifact and authorizes nothing.

**Negative-use.** Not a certified baseline (it defines the bar a run must clear; it does not meet it), not Claim C progress, not Paper B, not a capability or mechanism claim, not a compression result. The strongest statement a cleared run supports is a **validity** statement about elicited behavior under declared FP16 conditions.

## 2. Research question

At the locked parameter point, does an admissible construction elicit behavior **consistent with two-hop composition** — R1 rate ≥ the derived success threshold over the pre-declared analysis unit, with every non-traversal route excluded (terminal-grab, direct A→C\* recall, structural-depth selection, relation-identity, cross-query constant-token) — under **FP16, no compression**? Equivalently: is a **certified-constructible FP16 baseline** achievable on this substrate? The question is **constructibility, not capability**; a CERTIFY outcome is a validity statement about elicited behavior, never a claim that the model composes internally. Three substantive outcomes are possible (certify / inconclusive / fail), plus the pre-committed substrate-infeasibility possibility on repeated admissible failure (§14, §17).

## 3. Model / rung: FP16 only

- **Rung:** FP16 only. **Zero compression rungs** in this pre-registration. Stress/quantization is deferred by design — this is the baseline-constructibility step that must clear *before* any stress rung (program direction: instrument first, seam deferred). Claim C remains blocked behind this step.
- **Model (to be pinned at lock):** the FP16 model and its exact revision hash are a locked input; program precedent is Qwen2.5-3B-Instruct at a pinned HF revision. The concrete model load and execution are downstream and require authorization (§1); naming the model here locks the design input, it does not run it.

## 4. Locked Manager values

Bound to `constants.py` (SE-verified digest `614d185d…1c`):

| value | symbol | locked |
|---|---|---|
| clutter chains | k | 5 |
| same-depth competitors | D | 5 |
| C\* position slots | p | 5 |
| equal-salience candidates (min) | m_min | 10 |
| items (run) | n | 96 |
| margin | — | 0.25 |
| derived floor | F | 0.20 |
| success threshold | F + margin | 0.45 |

Derivation (locked): **F = max(1/p, 1/m, 1/D) = max(0.20, 0.10, 0.20) = 0.20**; **success threshold = F + margin = 0.45**. m policy: m ≥ 10 required; m > 10 permitted (drives 1/m lower); m < 5 inadmissible. These values are locked before look; the inspector C9 and evaluator enforce them fail-closed (§7, §13).

## 5. Construction schema

Per `PATH-A-CANDIDATE-CONSTRUCTION-DESIGN-v0.3` (SE digest `38e05460…`), at property level:

- **Interior-target:** `A —r1→ B —r2→ C* —(further edges)→ … → T`. C\* is the two-hop target and an interior node; T is the chain sink and a wrong answer (terminal ≠ answer).
- **Same-depth competitors (D=5):** A fans out via **distinct** relations so D nodes sit at depth 2; only following r1→r2 selects C\*. A depth-only heuristic scores 1/D.
- **Decoy chains (k=5):** competing chains; sinks are decoy terminals (wrong).
- **C\* position varied across p=5 slots** (defeats fixed-position grab).
- **Relation-balancing (E8, binding):** relation frequency, order, and position balanced across competitors so r1/r2 cannot be selected by salience alone.

Concrete tokens are an **open slot** (item generation).

## 6. Four-context design

Per design v0.3 §4: **composite / hop1 / hop2 / direct-query**, each in a **separate clutter-matched (k=5) context**, composite uncontaminated by prior controls (isolation). **4× generation cost** accepted. Per-item, per-query **token + category logging** for G6 scoring and future same-error-identity. The direct-query context withholds the bridge and replaces it with **neutral, length-matched filler containing neither B nor C\*** (E5; realization is an open slot).

## 7. Inspector gate (admissibility before scoring)

Every construction passes the Path A inspector (SE digest `be50c08c…`) **before** any scoring; a failing construction is **rejected at construction level**, logged, and dispositioned (not item cleanup). Checks: C1 terminal ≠ answer · C2 pairwise-distinct incl {X_i} · C3 seven-category separable · C4 r1 unique · C5 competitor-count structural consistency · C6 relation-balance (E8) · C7 direct-query filler (E5) · C8 four-context (E4) · **C9 Manager-lock binding (p/D/m/margin == locked; missing/deviating → fail-closed REJECT)**. The §13 fixture-mode guard is part of admissibility.

## 8. Scoring categories

Scored by **G6 evaluator v0.3** (SE digest `7adf4eef…`), multiclass **primary**, binary accuracy **non-gating**: **R1** correct-composition · **R2** target-terminal-grab · **R3** stopped-short (error, not partial credit) · **R4** decoy-terminal-grab · **R4b** depth-competitor-grab (depth-selection / wrong-depth-2 competitor) · **R5** abstain (failure-to-elicit on an answerable composite) · **R6cat** other. Per definition v0.4 §2.

## 9. Invalidators

A composite-correct response is **not** R1 if any holds (definition v0.4 §3): R6(a) terminal coincidence (→ construction rejection); R6(b) controls not available; R6(c) direct A→C\* shortcut (direct-query control); R6(d) interior-position salience; R6(e) cross-query constant-token; R6(f) below the derived floor. Mechanically-computable invalidators are applied by the scorer; the residual judgment call (R6cat adjudication of ambiguous tokens) is flagged and adjudicated under role-separation.

## 10. Derived heuristic floor

**F = max(1/p, 1/m, 1/D) = 0.20.** Components: terminal-grab → 0 (R8.1); direct-query → ≈0 on the retained subset (measured by control); position → 1/p = 0.20; token-pick → 1/m = 0.10; structural-depth → 1/D = 0.20. **Binding terms: position and depth (0.20).** A passing R1 rate must exceed **F + margin = 0.45**. (Relation-identity, once balanced per E8, is bounded by 1/D and adds no term.)

## 11. Dominance threshold

**Value: 0.25 over the pre-declared analysis unit** (definition v0.4; bound to `constants.DOMINANT_RATE_THRESHOLD`). **What it governs:** the **failure-signature dominance** test only — a rate-based failure category (R2/R4/R4b/R3/R5; constant-token; direct-query-shortcut) is "dominant" when its rate ≥ 0.25 over the analysis unit (§12). **Why 0.25:** a failure mode must account for at least a quarter of the analysis unit to be called a *dominant regime*, which separates a genuine failure regime from scattered noise; it is a pre-declared scorer threshold, **promoted from scorer code into definition v0.4** so it is not a free hidden number. **Distinct from the floor and the success threshold** — three different numbers with three different roles: **F = 0.20** (derived heuristic floor, §10), **success threshold = F + margin = 0.45** (the bar R1 must clear to CERTIFY, §10/§14), **dominance threshold = 0.25** (failure-signature dominance only, here). Control-floor failure and other-rate-ceiling breach use their own declared criteria, not 0.25 (§15).

## 12. Analysis unit declaration

**Declared (pre-registration):** because this pre-registration tests a **single parameter point** (one locked regime, not a sweep), per-cell and global coincide, so the **primary analysis unit is the global run** — the n=96 composite-query items at the locked point. **Secondary diagnostic:** a per-C\*-position breakdown (p=5) reported as a **layout diagnostic only**, not a dominance cell.

**Global R1 is computed over per-item validated items.** Validation is per item and gates numerator inclusion **before** aggregation: an item contributes to the R1 numerator only if (a) its R7 controls pass (hop1, hop2, and the direct-query control showing C\* is *not* producible with the bridge withheld) **and** (b) none of the R6 invalidators fire for that item (terminal coincidence, components-unavailable, direct-recall, interior-position, constant-token). The global R1 rate is then (count of items classified R1 after per-item validation) ÷ (count of admissible items), and dominance (§11) and the outcome branches (§14) are evaluated on that validated aggregate over the global run. *This declaration is the pre-registration's to make under definition v0.4; it is recorded here for Manager/TL confirmation at lock.*

## 13. Real-run fixture-mode guard

The run construction spec **must assert `_fixture_mode` is absent or false** (definition v0.4 checklist #11). A spec with `_fixture_mode: true` is **inadmissible for this real-run pre-registration** and is only a software fixture. Enforced fail-closed by inspector C9 and evaluator LOCK_VIOLATION; bound here as a pre-registration admissibility requirement so a real run cannot bypass Manager-lock enforcement by self-declaring fixture mode. **Locking this shell does not authorize model execution; a model run requires separate Manager by-name authorization** (§1).

## 14. Outcome branches

**Decision procedure (CI-based).** The test statistic is the **per-item-validated R1 proportion** (§12) over n=96, with a **two-sided 95% Wilson score confidence interval**. n=96 powers the separation: at p≈0.45 the Wilson half-width is ≈0.10, so the interval can resolve the 0.45 success threshold from the 0.20 floor (a 0.25 gap). *(Wilson 95% is the declared method; if CS's realization adopts a different CI, it must be stated explicitly and re-locked.)* The decision rule maps the result to exactly one of five pre-committed outcomes (definition v0.4 §8):

- **CERTIFY** — R1 **lower CI bound > 0.45**, controls pass, all invalidators clear, and **no** failure signature dominant. **CERTIFY is an instrument / validity verdict only:** it states the run cleared the gate (elicited behavior consistent with two-hop composition under the declared exclusions). It is **not** certification-of-record and **not** downstream authorization — not for a stress rung, Claim C, or Paper B (§18).
- **INCONCLUSIVE** — the **R1 CI crosses the [0.20, 0.45] boundary** (the interval is neither entirely above 0.45 nor entirely below 0.20) with **no** dominant failure signature. Neither certifies nor refutes.
- **FAIL** — the **R1 upper CI bound < 0.20**, **or** a failure signature is dominant (§15). The dominant signature (or sub-floor R1) is the diagnosis.
- **REJECTED-CONSTRUCTION** — an admissibility breach at inspection or scoring (§7); rejected as a whole, logged, dispositioned.
- **SUBSTRATE-INFEASIBILITY CANDIDATE** — pre-committed (definition v0.4 §8.5): on **repeated admissible constructions failing to certify**, the conjunction of exclusions may be unsatisfiable on this substrate. **It does not fire from a single run**, and a failing construction is **never** a license to loosen R8 / R6(c) / the success threshold to manufacture a pass (§17).

## 15. Failure signatures

Each mapped to a diagnosis (definition v0.4 R11): R2 dominant (target-terminal attraction); R4 dominant (cross-chain salience); R4b dominant (depth-selection regime; R4b-dominant with R1 ≈ 1/D confirms depth-selection); R3 dominant (hop2-in-composition failure); R5 dominant (abstention regime → failure-to-elicit); cross-query constant-token prevalent (flat heuristic); direct-query shortcut prevalent (direct-recall route active). **Rate-based signatures use the 0.25 dominance threshold.** Plus, with **their own declared criteria**: control-floor failure (controls not met); **other-rate-ceiling breach** — ceiling **0.10, applying ONLY to residual R6cat / *other*** (off-distribution/malformed); **R4b depth-competitor-grabs are excluded from *other* and diagnosed separately** via the R4b-dominant signature, so the 0.10 ceiling never absorbs the depth-selection signal (E7). And R1 indistinguishable from the derived floor.

## 16. Provenance requirements

- **Byte-binding:** the run is governed by these exact bytes — definition v0.4 (`4b616afb…`), design v0.3 (`38e05460…`), inspector (`be50c08c…`), evaluator (`7adf4eef…`), constants (`614d185d…`). Hash verification on fetched bytes, declared digests echoed adjacently.
- **Per-result provenance:** every evaluator output carries `manager_lock_summary` + `fixture_mode`; the dominance-threshold provenance flag must read **promoted to definition v0.4** (open slot: `constants.DOMINANT_RATE_THRESHOLD_PROVENANCE` status updated from "FLAGGED FOR PROMOTION" to "promoted to TARGET-CONSTRUCT-DEFINITION-v0.4" once v0.4 is of-record).
- **Lock-before-look:** this pre-registration is locked and committed **before** any run; the analysis plan, threshold, and analysis unit are fixed before results exist. Sealed-tree boundary preserved (no tokenizer/model artifacts staged into the gate tree).
- **Definition-of-record:** definition v0.4 must be elevated to of-record (Manager/TL) before this pre-registration is itself locked of-record; it is currently `in-review/`.

## 17. Stop rule

The pre-registration is locked: **no post-hoc change** to the construction, gate, scoring categories, invalidators, floor, threshold, dominance threshold, or analysis unit after results are seen. A failed admissible construction is a **FAIL** (or, on repetition, a substrate-infeasibility candidate) — **never** a license to loosen R8 / R6(c) / the threshold to manufacture a pass. Certification requires **R1 to rise** (R12.2), not R2 to fall. One run per locked spec; re-runs require a new locked pre-registration. **Next update requires data, not another ranking pass and not a loosened gate.**

## 18. Forbidden interpretations

- A **CERTIFY emission is not a certified baseline of-record** — it is the instrument identifying that the run cleared the gate; certification of-record is a separate governance act.
- **"A depth-2 heuristic approximates traversal"** (E6) may **not** be used as justification; depth-selection is excluded and priced in, never excused as proto-composition.
- **NOT_RULED_OUT discipline:** the absence of a failure signature is not the presence of composition. R1 is the **best-supported interpretation, not proof**; a **capability** claim would require mechanistic intervention **and** cross-construction generalization, which this run does not and cannot provide.
- No **Claim C**, **Paper B**, **capability**, **mechanism / architecture / training-distribution**, **compression-robustness**, or **task-family-viability** claims follow from any outcome here.

---

## Open slots still requiring CS realization

- **Item generator + seed** — downstream; the inspector validates a generator's output, the generator itself is not in this shell.
- **Concrete token pool** — synthetic tokenized strings per Path A precedent; item-generation territory.
- **Direct-query filler realization** — neutral, length-matched, no B or C\* (E5).
- **Relation-balancing realization** — frequency/order/position balanced across competitors (E8).
- **Power / CI confirmation** — the decision procedure is now specified (Wilson 95% on per-item-validated R1; edge mapping in §14) and the INCONCLUSIVE band edges are fixed at [0.20, 0.45); CS confirms the Wilson half-width arithmetic at n=96 and may re-lock if a different CI is adopted.
- **Other-rate ceiling value** — proposed 0.10; Manager/TL confirmation.
- **Analysis-unit confirmation** — proposed global-primary (§12); Manager/TL confirmation.
- **Provenance-flag update** — `constants.DOMINANT_RATE_THRESHOLD_PROVENANCE` → "promoted to v0.4" (CS code follow-through).
- **Definition-of-record elevation** of v0.4 (Manager/TL) before this shell is locked of-record.
- **The run itself** — model load + execution — requires Manager by-name authorization with lock-before-look (not in this shell).

## Changelog v0.1 → v0.2 (CS feasibility + C5 preloaded claim-risk)

1. **CERTIFY language (§14)** — defined at point of use as an instrument/validity verdict only; not certification-of-record, not downstream authorization.
2. **Global-primary analysis unit (§12)** — global R1 is computed over per-item validated items; R7 controls and R6 invalidators gate numerator inclusion before aggregation.
3. **Decision rule (§14)** — added the power/CI procedure (Wilson 95% on validated R1, n=96) with exact edge mapping: lower CI > 0.45 → CERTIFY; CI crosses [0.20, 0.45] → INCONCLUSIVE; upper CI < 0.20 or dominant signature → FAIL.
4. **Band/threshold provenance (§10, §11)** — F = max(1/p,1/m,1/D) = 0.20, success threshold = F + margin = 0.45, shown distinct from the dominance threshold = 0.25.
5. **Dominance-threshold rationale (§11)** — stated what 0.25 governs (failure-signature dominance only) and why, so it is not a free hidden scorer number.
6. **Other-rate ceiling (§15)** — 0.10 confirmed to apply only to residual R6cat/*other*; R4b depth-competitor-grabs excluded and diagnosed separately.
7. **Fixture-mode guard (§13)** — restated that real-run specs assert `_fixture_mode` absent/false, and that locking the shell does not authorize execution (a run needs separate Manager by-name authorization).
8. **Substrate-infeasibility (§14, §17)** — carried definition v0.4 §8.5 language: one run does not fire it, and failure is never a license to loosen R8/R6(c)/threshold.

**Unchanged:** all controlling-byte bindings, the locked Manager values, the construction schema, the inspector gate, the scoring categories, and the no-items/prompts/run scope. This remains a shell that declares and binds and does not authorize a run.

---

*Status: pre-registration shell v0.2, FP16-only, lock-before-look. Folds CS feasibility + C5 preloaded claim-risk edits. No items, prompts, tokens, model-execution command, or compression rung. Declares and binds; does not authorize a run. For CS byte-exact filing, then C5 re-review of the actual object.*
