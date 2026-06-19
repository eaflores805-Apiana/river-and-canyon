# CONSTRUCTIBILITY-PACKAGING-SCOPE-v0.1

**To:** Team Lead (for Manager/TL review) **Cc:** CS Engineer, C5, Manager **From:** Senior Engineer
**E. A. Flores**, Apiana AI, Inc. — June 19, 2026
*River and Canyon · Path A. Packaging scope only — what claims are now earned, where they belong, what stays forbidden. No run, no construction, no certification. SE drafts; SE locks nothing and authorizes nothing.*

> Grounded in a byte-read of the project record: the claim ledger (`03claimledger.pdf`) and the four target papers' theses/closures (`survivalisnotcorrectness.pdf`, `correctnessisnotconstructibility.pdf`, `certificationbeforeretention.pdf`, `HASHINTEGRITYISNOTCONSTRUCTVALIDITYv0_7_2.pdf`), plus the byte-verified Path A run record. Where I name a paper's current content, I read it; I did not reconstruct it.

## 1. Executive summary

The current V3 composite route is closed as designed: a foreclose-all redesign **cleared the second hop under competition** across every fresh materialization, but its **first-hop admissibility precondition did not hold** — stable-inadmissible across six fresh materializations — so the composite gate was never readable and the composite question is unanswered. This is a **constructibility / measurement-validity finding**, not a model-capability or compression finding (the program remains pre-stress; the model performed the first hop at 0.906 on one materialization). It belongs primarily in **Paper 2 (*Correctness Is Not Constructibility*)** as a second, independent constructibility case — its existing case is a position/rank confound; this is a distinct failure mode (an unstable first-hop precondition surfaced by the very redesign built to remove the first confound). It also supplies a clean **fresh-run / lock-before-look** methods point (Paper 1) and one cautionary sentence for the **certification protocol** (Paper 3), and it is the first **data** trigger for a claim-ledger update — without moving the open compression hypothesis (Claim #5). Recommended route: **package into the existing sequence; do not stand up a new standalone paper; recommend no immediate experiment.**

## 2. Settled findings of record (bounded)

```text
V3 floor check (seeds 001..096):       COMPONENT-ADMISSIBLE-UNDER-COMPETITION
V3 composite gate (fresh 097..192):    PRECONDITION-FAIL  (hop1 failed the floor; gate not read)
Hop1 stability (6 fresh 193..768):     HOP1-STABLE-INADMISSIBLE  (all six hop1 blocks fail; hop2 576/576)
Current V3 composite route:            CLOSED AS DESIGNED
```

Allowed route interpretation (verbatim):

```text
The current V3 composite gate is blocked because hop1 admissibility does not reliably hold across fresh
materializations, while hop2 remains admissible.
```

Anchored across all eight materializations to date, the first hop cleared its floor in **exactly one** (the floor-check, 0.906); the other seven failed (0.24–0.56 on the fresh blocks; 0.292 on the composite-gate set). The single clearing is **anomalous relative to the fresh map**.

## 3. Evidence inventory (paths / digests)

**Repo-verified (recomputed from repository bytes — load-bearing):**
```text
Repository:                 github.com/eaflores805-Apiana/river-and-canyon
Floor-check decision:       6a34f6dc…   (COMPONENT-ADMISSIBLE-UNDER-COMPETITION; hop2 96/96, hop1 87/96)
Composite-gate run:         experiments/2026-06-18_v3-composite-gate-run  HEAD 09030b18
  decision:                 3924ff35…   (PRECONDITION-FAIL; hop1 28/96, hop2 96/96)
Hop1-stability run:         experiments/2026-06-19_hop1-stability-run     HEAD fe677158
  decision.json:            reproduced BYTE-IDENTICAL (HOP1-STABLE-INADMISSIBLE; hop1 224/576, hop2 576/576)
  covariate_log.json:       reproduced BYTE-IDENTICAL (P-role 352/352 P_decoy_head)
  admissibility 576/576 PASS ; conformance 576/576 PASS ; manifest present & complete
Model/profile (locked):     Qwen/Qwen2.5-3B-Instruct rev aa8e7253, FP16, greedy
```

**SE-draft bytes (canonical filing is a CS commit of the same bytes; digest match proves same bytes reviewed):**
```text
HOP1-STABILITY-FINDING-REPORT-v0.1.md            2969ec1a5ce830c2b77c974ad23b163e4cb1dca6a518800a555f5a159f6efb33
HOP1-STABILITY-RUN-SE-VERIFICATION-RETURN-v0.1   84a5716b4f202a9337495100064d8e5f466ff8baf3e76bb16b4d221de05285b9
V3-COMPOSITE-GATE-RUN-SE-VERIFICATION-RETURN     0eb0edcb…
V3-FLOOR-CHECK-RUN-SE-VERIFICATION-RETURN        03d2ead8…
```

**Existing manuscripts / control sheets (project record):**
```text
P1  Survival Is Not Correctness                 survivalisnotcorrectness.pdf            (16 pp)
P2  Correctness Is Not Constructibility         correctnessisnotconstructibility.pdf    (14 pp)
P3  Certification Before Retention              certificationbeforeretention.pdf        (15 pp; file id v1.0 — confirm vs v1.1)
P4  Hash Integrity Is Not Construct Validity    HASHINTEGRITYISNOTCONSTRUCTVALIDITYv0_7_2.pdf (10 pp; standing note)
    Claim Ledger                                03claimledger.pdf
```

## 4. Which paper each finding strengthens

```text
PRIMARY -> Paper 2 (Correctness Is Not Constructibility).
  P2 currently supplies ONE worked demonstration that the baseline gate is binding rather than merely
  conservative: a Two-Hop Level-1 construction whose surface composite accuracy (15/24) dissolves under
  decomposition into a position/rank confound (1/8 at pos3, 6/8 at pos5, 8/8 at pos7). The V3 arc is a
  SECOND, INDEPENDENT case of "surface/component signal is not constructibility": the foreclose-all redesign
  built to remove residual routes cleared the second hop under competition, yet its first-hop precondition was
  stable-inadmissible across fresh materializations — so the composite question could not be posed. Two
  distinct constructibility failures (a position/rank confound; an unstable first-hop precondition) is a real
  strengthening of P2's thesis.

Paper 1 (Survival Is Not Correctness).
  P1's fail-closed staging is reinforced by the fresh-run lesson (§8): a precondition that cleared on one
  (already-seen) materialization did not replicate on fresh disjoint seeds. P1's own closing already states
  the full instrument has not produced a clean seam measurement and incorporates no constructibility-track
  result; this finding is consistent with that and (if P1 is revised) earns a one-line forward pointer.

Paper 3 (Certification Before Retention).
  P3 is a protocol for qualifying a SINGLE-HOP baseline as a retention substrate (no candidate certified). The
  V3 finding is a cautionary data point: single-hop admissibility is not trivially satisfied under competition
  and must itself be shown stable across fresh materializations before certification. One sentence, not a claim
  change.

Paper 4 (Hash Integrity Is Not Construct Validity).
  No claim change. The byte-verification discipline that made this finding trustworthy (independent recompute;
  digests bind bytes; reviewers verified the same SE bytes) is a worked instance of P4's thesis; optionally
  cite the V3 verification returns as an example. P4 stays a standing note (it is explicitly not paper-ready).

Claim Ledger.
  This is the program's FIRST data-trigger update (stop-rule trigger (a): a protocol run). Record the V3
  constructibility result as a new negative finding of record. Do NOT change Claim #5 (precision-demand
  predicts differential retention) — it remains OPEN / Tier-0 / UNRUN. Pre-stress status is unchanged.
```

## 5. New claim candidates (bounded; for review, not yet adopted)

```text
C-new-1  Constructibility can fail at the first hop, not only via a position/rank confound. A foreclose-all
         redesign that cleared the second hop under competition still failed to establish a stable first-hop
         admissibility precondition across fresh materializations.
C-new-2  Component admissibility on a single materialization does not imply cross-materialization
         admissibility. The first hop cleared on one (already-seen) materialization and failed on six fresh,
         disjoint ones; treating the single clearing as a stable baseline would have been an error.
C-new-3  Under V3 at K=5 (FP16, greedy), the second hop was admissible across all fresh materializations while
         the first hop was not — the two components were not equally admissible under the same competition.
C-new-4  Among wrong first-hop predictions in the fresh blocks, outputs landed on the P-role distractor class
         in all logged cases (positional/structural co-occurrence; see §7 — no mechanism).
```

All four are statements about the **V3 construction's behavior under declared controls**, not about model capability or compression.

## 6. Claims still forbidden

```text
Carry the full standing list — none of the following may be written:
  the model cannot do hop1 | the model cannot compose | the model is unstable | binding failure |
  attention failure | reasoning failure | shortcut mechanism | compression readiness | Claim C |
  Paper B | certification | seam evidence.
From the claim ledger, additionally:
  - Do NOT resolve or advance Claim #5 (precision-demand predicts differential retention) — pre-stress / unrun.
  - Do NOT let the carving/imperfection analogy assert an internal defect class; it generates targets, never
    mechanism (No Mountain in the Sentence).
  - Do NOT let a conditional implication (#9: retention profiles / capability-aware serving) borrow the
    field-consensus authority of #1/#2; it holds only if #5 resolves positive, which it has not.
```

## 7. P-role positional observation — boundary

```text
ALLOWED (verbatim): "Among wrong hop1 predictions in the fresh blocks, outputs landed on the P-role distractor
class in all logged cases."
This is positional / structural co-occurrence ONLY. It is the most mechanism-shaped fact in the arc and
therefore carries the tightest leash. In packaging it appears as a logged regularity with an explicit "no
mechanism is claimed." Per the claim ledger's governing rule, for the P-role landing to become anything more
than a co-occurrence it would first require, in a FUTURE pre-registered study (not this packaging): a behavioral
signature, a minimal intervention that should change the landing, and a falsification path. Absent that, it is
recorded as data and nothing else. It is NOT binding/attention/shortcut/identity-resolution and NOT seam
evidence.
```

## 8. Fresh-run / lock-before-look lesson

```text
The floor-check first hop cleared at 0.906 on the already-seen set 001..096. On fresh, disjoint, pre-registered
seeds (097..192, then 193..768) the first-hop rate was 0.24–0.56 and failed the floor in seven of seven fresh
materializations. Requiring fresh, disjoint, pre-registered runs — and barring already-seen data from gate use —
is what prevented an anomalous single clearing from being mistaken for a stable baseline. This is a clean,
citable methods result that strengthens Paper 1's fail-closed staging and instantiates the claim ledger's
stop-rule (a result, not another ranking pass, is what moved the record). Packaging language: bounded, e.g.
"an already-seen materialization must not be treated as a stable baseline; gates require fresh, disjoint runs."
```

## 9. What to cut or revise in existing drafts

```text
Paper 1 (Survival Is Not Correctness):
  - No claim change required; nothing in P1 is contradicted (it reports the seam line blocked at FP16 and makes
    no seam claim). IF revised: add a one-line forward pointer that the constructibility track has since
    produced a banked negative finding (V3 composite blocked at the first-hop precondition). Otherwise leave as
    released. Do not add any seam or capability language.

Paper 2 (Correctness Is Not Constructibility):  [the home of the work]
  - ADD the V3 arc as a second, independent constructibility case after the existing position/rank case.
  - REVISE the abstract from one demonstration to two independent constructions (the position/rank confound;
    the unstable first-hop precondition under foreclose-all controls).
  - Use bounded language throughout the new section: "hop2 admissible across fresh materializations," "hop1
    stable-inadmissible across six fresh materializations," "composite gate not readable," "composite question
    unanswered." AVOID any phrasing that reads as "the model cannot compose" — frame as "the construction could
    not pose the composite question."
  - INCLUDE the P-role co-occurrence with the §7 leash, and the §8 fresh-run lesson as a methods point.
  - Anchor to the banked finding report (2969ec1a…) and the verification returns as evidence of record.

Paper 3 (Certification Before Retention):
  - ADD one cautionary sentence: single-hop admissibility must itself be shown stable across fresh
    materializations before a single-hop baseline is certified as a retention substrate; cite the V3 finding.
  - No other claim change. FIRST confirm the canonical P3 version by byte-check: the project file carries
    identifier v1.0, while the program record refers to a v1.1 (erratum remediated). Edit only the canonical
    bytes; do not edit a stale copy.

Paper 4 (Hash Integrity Is Not Construct Validity):
  - No claim change. OPTIONALLY cite the V3 verification returns as a worked example of byte-binding +
    semantic-read. Keep it a standing governance note (not publication-ready, by its own status line).

Claim Ledger:
  - ADD a status row for the V3 constructibility finding as a negative result of record (first data trigger).
  - Do NOT alter Claim #5's status (open/unrun). Pre-stress is unchanged.
```

## 10. Recommended packaging route

```text
1. Fold the V3/hop1 constructibility finding into Paper 2 as a SECOND independent case (primary home),
   anchored to the banked HOP1-STABILITY-FINDING-REPORT (2969ec1a…) and the three SE verification returns.
2. Add the fresh-run / lock-before-look lesson to Paper 2 (methods) and, if P1 is revised, a forward pointer in
   Paper 1.
3. Add the single cautionary sentence to Paper 3 (after confirming its canonical version).
4. Update the Claim Ledger as the first data-trigger update — without changing Claim #5; record pre-stress.
5. Do NOT stand up a new standalone paper for this finding. A negative constructibility result is strongest as
   a second case inside the paper whose thesis it extends; a separate paper would fragment the series and
   over-elevate a negative result. (The internal finding report already exists as the evidence-of-record
   artifact P2 cites.)
6. Recommend NO immediate experiment.
```

## Manager decision boundary (present; do not decide here)

```text
A. Package and PAUSE Path A.  (Bank the findings; return to the broader paper/program roadmap.)
B. After packaging, consider ONE bounded hop1-safe construction-design attempt — a single pre-registered DESIGN
   question ("can a V3-like construction make hop1 stably admissible across materializations without making
   identity easy or importing a shortcut?"), with a pre-declared stop ("if this construction also fails its
   hop1 precondition, that too is a finding"). NOT a rerun, NOT an open-ended rebuild.

This scope recommends no immediate experiment and does not choose A vs B. That is a TL/Manager decision, best
taken AFTER the packaging artifact exists.
```

## Required return

```text
PASS — constructibility packaging scope drafted for Manager/TL review.
```

## Boundaries

```text
No run. No construction redesign. No prompt edits. No post-hoc slicing. No threshold adjustment. No tooling
edit. No compression. No INT8. No INT4. No Claim C. No Paper B. No certification claim. No capability claim.
No mechanism claim. The program remains PRE-STRESS; the carving analogy stays a target-generator, never a
mechanism. The Path A FP16 K=5 FAIL remains closed. SE drafts this scope; SE locks nothing and authorizes
nothing. The decision among A/B is the Manager's.
```

---

**The one to carry up:** The banked V3/hop1 result is a **constructibility finding**, and its home is **Paper 2** — which today proves the baseline gate is binding with one case (a position/rank confound) and would gain a **second, independent case**: the foreclose-all redesign cleared the second hop under competition but found the **first-hop precondition stable-inadmissible across fresh materializations**, so the composite question could not be posed. It also gives Paper 1 a clean fresh-run/lock-before-look methods point and Paper 3 one cautionary sentence, and it is the claim ledger's **first data-trigger update** — **without** moving the open compression hypothesis (Claim #5); the program stays pre-stress. Recommendation: **fold into the existing sequence, do not create a new paper, recommend no immediate experiment.** P-role stays positional co-occurrence on the tightest leash. SE drafts; SE authorizes nothing; A (pause) vs B (one bounded design attempt, later) is the Manager's call.

— Senior Engineer (constructibility packaging scope; routes for Manager/TL review)
