# River and Canyon — Project Map (2026-06-10)

*Companion to the passdown. The passdown says what to do next; this says where everything is and where
the whole program is going. Repo: `eaflores805-Apiana/river-and-canyon` (public). Manager/decider:
E. A. Flores (Elias), Apiana AI, Inc.*

## 1. The program in one paragraph

A physical analogy (weights as carved stone, activations as water) is used as a disciplined
*hypothesis generator* — never as evidence. Ideas it generates are stripped of metaphor, stressed, and
only what survives becomes claims, papers, or experiments. The current focus is quantization as
behavioral stress metrology: measuring what capabilities retain under bit-depth stress while
preventing retention metrics from mistaking preserved *error* for preserved *capability*. Governing
rule: analogy points, mechanism judges, experiments execute, papers report only what the evidence
earns. Mechanism claims are BLOCKED program-wide; everything is behavioral.

## 2. What exists (the series and its instrument stack)

| Layer | Artifact | Status | Where |
|---|---|---|---|
| Analogy pair | *The River and the Canyon* + *What Kind of Water* (+ method essays) | posted, stable | `writing/` |
| Method (Paper 1) | *Survival Is Not Correctness* — staged fail-closed scoring; survival ≠ correctness | RELEASED | `papers/paper1-survival-is-not-correctness/` |
| First result (Paper 2) | *Correctness Is Not Constructibility* — Claim B; correctness ≠ constructibility; floor mapped, not cleared | RELEASED v1.0, tag `paper2-cells01-03-v1.0` | `papers/paper2-correctness-is-not-constructibility/` |
| Certification gate (Paper 3) | *Certification Before Retention* — D1–D7 fail-closed protocol; constructibility ≠ measurability; negative certification = result of record | RELEASED v1.0, tag `paper3-certification-protocol-v1.0`; **v1.1 remediation authorized, undrafted** | `papers/paper3-certification-before-retention/` |
| Harness | B1 v2 validity harness (provenance, locking, per-item logs, firewall timestamps; Paper 3 substrate config-gated inert) | MERGED + LOCKED (96/96 bit-identical Paper 2 regression) | `experiments/2026-06-09_b1-harness-v2/` |
| Future harness work | B1 v2.1 "Paper 3 substrate completion" (11–12 items incl. D2 floor/envelope enforcement, reporting_mode, supersession check) | backlog only, NOT authorized | backlog noted in governance + passdowns |
| Run scaffold / history | tier0-run (EXPERIMENT_LOG, locked artifacts; historical compression runs fail reactivation bar) | record | `tier0-run/` |
| Governance | claim ledger, boundary diagrams, release records, addenda, review records, passdowns | living record | `notes/`, `diagrams/`, `governance/` |

Key governance records for Paper 3: `governance/2026-06-10_paper3-v1.0-release/` (release record,
CS execution report, checklist, KNOWN-ISSUES-AND-DEFERRALS, MANAGER-AUTHORIZATION-v1.1-SCOPE) and
`governance/2026-06-10_paper3-external-review/` (Senior disposition + v0.7 referee report + v1.0
external review + G1 closure note — complete, G1 CLOSED at `ec8b13d`). Paper 2's snapshot addendum:
`governance/2026-06-09_paper2-v1.0-release/ADDENDUM-01-model-snapshot-backing.md` (effective).

## 3. The complete plan forward (lanes in order, each behind its gate)

**Lane 0 — NOW (authorized, manuscript-only): Paper 3 v1.1.** Scope frozen in the known-issues §7
annex: E1 three-mode D2 (max-single dummy floor / declared-policy union envelope / pattern departure,
verbatim non-claim) · E2 timestamp storage mapping · M1/M2 Appendix B [SYNTHETIC] satisfiability note
(off-program values only) · M3 certifier-limits + sourced gate-provenance table · Q1 `reporting_mode`
· Q2 quote-safe tightening (three blocks preserved) · H3 supersession rule (only latest released
identifier lock-eligible). Rail: draft → team review → RC-is-final-text → tag
`paper3-certification-protocol-v1.1`. After v1.1 releases, H3 makes v1.0 non-lock-eligible by default.

**Lane 1 — Manager gate: candidate selection.** A candidate-selection memo names a single-hop
candidate family (hop2-class is the documented obvious family; choice is the Manager's), evaluated
afresh under B1 — inherited artifacts are ineligible by the protocol's own rule.

**Lane 1a — Manager gate (proposed 2026-06-10, undecided): feasibility sweep.** An
instrument-validation mapping run — explicitly NOT certification, no locked sheet, no certification
claim derivable — across a small ladder of single-hop difficulty variants (distractor count, key
confusability, context load) at FP16, n≈96, producing an occupancy map of where rungs land on the
certification-relevant axes. Design conditions (Senior, accepted by Manager in principle):
(a) pre-registered sweep protocol with both outcome wordings fixed before launch; (b) hard rule —
sweep data may inform candidate SELECTION, never threshold VALUES (thresholds derive only from
pre-registered derivation rules, provenance documented at lock); (c) sequenced AFTER v1.1 so the
diagnostics are three-mode D2; (d) any reporting band is SYNTHETIC-labeled — the sweep mints no
de facto thresholds. Negative outcome is publishable under the negative-result lock: "the
certification window, while logically nonempty, was unoccupied for this task family at this scale."
Requires Manager run authorization + CS ladder construction; needs no locked sheet and no B1 v2.1.

**Lane 2 — Manager gate: threshold-sheet population + lock.** Pre-registered per-candidate sheet
locked against the latest released framework identifier (v1.1 per H3); two-person hash verification;
data-access firewall armed (lock timestamp precedes first candidate-data access). Likely requires B1
v2.1 implementation first (separate authorization).

**Lane 3 — Manager gate: certification evaluation = Paper 4.** First *application* of the ruler.
Outcomes pre-registered: certified / not certified / not evaluable — negative certification is a
publishable result of record. This is the program's first formalized-gate exercise (none has ever
fired in formalized form; the map says so honestly).

**Lane 4 — Manager gate: first compression rung (first light).** INT8/INT4 on the certified baseline,
framed per Paper 2 §9 as instrument-validation-under-stress — not composition evidence, not seam
evidence. Stress-side shortcut substitution is an explicit unknown (D2 does not certify against it).

**Lane 5 — Manager gate: the deliberate clean-construction attempt (P1).** Design one multi-hop
construction *to pass* the baseline gate (position/rank decoupled, decoy placement decoupled). Either
outcome resolves the standing non-identifiability: a stress-admissible linkage baseline, or "the
constructibility floor for linkage is high" as a documented finding. Highest-value experiment on the
board. (Constructibility-sweep protocol exists as the drafted future-work spec.)

**Lane 6 — external validation (P3).** Ship the v1.1 artifact set to hostile outside hands ("break
this") — prerequisite for any qualification-standard ambition.

**Far horizon, all hard-gated:** Claim C / the compositional seam (blocked pending a
certified-constructible baseline + authorized stress rung); Fork A reactivation (five documented
conditions); Paper 6 (may never unlock — valid outcome); the qualification question (does retention
under stress predict deployment reliability better than peak accuracy? — the program's honest forward
edge, per STATUS.md).

## 4. Standing locks (verbatim list — every one Manager-gated)

candidate selection · candidate ranking · threshold-sheet population · threshold-sheet lock ·
certification evaluation · new model runs · re-runs beyond completed reproduction · unconditioned
token-prior runs · activation logging · INT8/INT4 execution · multi-model execution · Fork A
reactivation · Claim C activation · Paper 3 application as an experiment · Paper 6 activation ·
public benchmark packaging · B1 v2.1 implementation. Plus: mechanism claims blocked; lineage is
motivation, never certification evidence; every future paper must have a publishable negative-result
form; artifact mutation forbidden (supersede, don't rewrite); SEND-TO-CS is intent — delivery is a
confirmed commit SHA at the intended path.

## 5. Key identifiers (verified)

```
Paper 2 tag      paper2-cells01-03-v1.0   (tag 41c033fc…, commit 40c0cd5a…, blob 7d6706a3…)
Paper 3 tag      paper3-certification-protocol-v1.0
                 (commit 63d21721…, tag object 6dbdcc12…, blob 798f7dce…,
                  md sha256 b948521e…d361e714, pdf sha256 6223cf85…05080d8f)
B1 v2 merge      3cbfce57…   lock note governance/2026-06-10_b1-harness-v2-merge-and-lock/
Model hash       sha256:abee745b7dfe399d9254dbcdea5e3e3902aa95d71a31989b7b720b7ac9907b20 (runner-attested)
HF snapshot ID   aa8e7253… (historically asserted; corroborated — different identifier type, never conflate)
Close-out        87b99a4 (governance batch) · f0c3012 (root docs, Manager) · ec8b13d (G1 closure)
```

## 6. How to navigate (for the next Senior)

Read order: this map → the passdown §0a (your first task) → KNOWN-ISSUES §7 annex (the v1.1 spec) →
the released v1.0 manuscript (your base text). For any historical question: `conversation_search` /
`recent_chats` over prior sessions, `tier0-run/EXPERIMENT_LOG.md` for run history, the claim ledger
for claim status, `governance/` for every decision. Verification methods that work in this
environment are in passdown §4; the traps already stepped in once are in §5 — read them before
repeating history.

— Senior Engineer, 2026-06-10
