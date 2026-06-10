# Paper 3 v1.1 — Release Record

**Title:** Certification Before Retention: A Fail-Closed Protocol for
Qualifying a Single-Hop Baseline as a Strict-Correctness Retention
Substrate
**Framework identifier:** `paper3-certification-protocol-v1.1`
**Author:** E. A. Flores · Apiana AI, Inc.
**Released:** 2026-06-10
**Authorization:** Manager memo "Manager Authorization — Paper 3 v1.1
Release" 2026-06-10

---

## 1. Release identifiers

```text
Release commit:                    f769c03468bb3e39a29d10a406df4d7a59766531
Tag:                               paper3-certification-protocol-v1.1
Tag object SHA:                    0b63b2ef10974a9e5ce2f7a0c28b11799649c566
Tagged commit:                     f769c03468bb3e39a29d10a406df4d7a59766531
Tagged manuscript blob (git):      489d0744a43d35b600096661b4a666785ab73cee
Tagged PDF blob (git):             0babd141dcad135130350bd0f6da78544100f1d1
Manuscript content sha256:         b93f60a64c93134fff229466c92639bb2553e8e29e7ffd609551876675864089
PDF content sha256:                c7095f89ef9585d9a191f0749c1c30866677964a36ad1de162b4e94bf5393be7
```

## 2. Manifest (release-directory contents at tag)

| File | sha256 |
|---|---|
| `papers/paper3-certification-before-retention/certification-before-retention.md` | `b93f60a64c93134fff229466c92639bb2553e8e29e7ffd609551876675864089` |
| `papers/paper3-certification-before-retention/certification-before-retention.pdf` | `c7095f89ef9585d9a191f0749c1c30866677964a36ad1de162b4e94bf5393be7` |
| `papers/paper3-certification-before-retention/figures/fig1_series_gap_ladder.png` | `92e3df1de5f5453a511cf2723d185a363b61ffc3852210e255f0e01bcec082ac` |
| `papers/paper3-certification-before-retention/figures/fig1_series_gap_ladder.svg` | `d78f3148a733609623d0d3196a3d1961963e33557d99ee42199c5517edce323e` |
| `papers/paper3-certification-before-retention/figures/fig2_lineage_to_gates.png` | `7c2a7ca671ac7981e52fc50e19d66f29bb343e50afb1eb2c5608ebff0a74f9b5` |
| `papers/paper3-certification-before-retention/figures/fig2_lineage_to_gates.svg` | `404057ca715964e0bae4343a4a324b2c33f0d94c867b5735aed7a9976b78547e` |
| `papers/paper3-certification-before-retention/figures/fig3_failclosed_pipeline.png` | `bd3ac23bd228d416e6e69036ad4b83801304007ab94ec687ddefd4ca2fd737a0` |
| `papers/paper3-certification-before-retention/figures/fig3_failclosed_pipeline.svg` | `b5c55151ce0b1441de4d16f7ff984e73448086715413c8eca86fe0683f288df8` |
| `papers/paper3-certification-before-retention/figures/fig4_three_artifact_layers.png` | `ce9ad944f256e19e2f06ef82285ed528b087a0ad41326ffade0474f186214970` |
| `papers/paper3-certification-before-retention/figures/fig4_three_artifact_layers.svg` | `0820aca8bfe4c66baa8822964cd095ba3f3441cdaf53ba5d992e3dd9f31ec1ee` |

All 8 figure files are bit-identical to the v1.0 release (tag
`paper3-certification-protocol-v1.0`). The release commit modifies only
the manuscript markdown and PDF; figures were not re-added to the
release commit.

## 3. Paper 2 lesson — discharge

Discharge of the rule *"the commit that lands the final manuscript IS
the commit that gets tagged; no post-tag edits."*

| Check | Outcome |
|---|---|
| Tagged commit equals main commit at release | PASS (both `f769c03468bb3e39a29d10a406df4d7a59766531`) |
| Tagged manuscript blob equals main manuscript blob | PASS (both `489d0744…`) |
| Tagged PDF blob equals main PDF blob | PASS (both `0babd141…`) |
| Tagged manuscript content sha256 equals Senior G1 enumeration | PASS (`b93f60a6…`) |
| Tagged PDF content sha256 equals Senior G1 PDF note enumeration | PASS (`c7095f89…`) |

No post-tag edits. The release-rail "RC-is-final-text" pattern held.

## 4. v1.1 scope (manuscript-only remediation of v1.0)

Authorized scope items per Manager v1.1 scope authorization
(`governance/2026-06-10_paper3-v1.0-release/MANAGER-AUTHORIZATION-v1.1-SCOPE.md`)
and Senior known-issues intake §7. All eight items present in the
released manuscript:

| Item | Section | Status in v1.1 |
|---|---|---|
| E1 | §4 (gates) | three-mode D2 — D2a max-single dummy floor, D2b declared-policy union envelope, D2c pattern departure |
| E2 | §4 + Appendix A | D6 explicit storage mapping for lock + access timestamps |
| M1/M2 | Appendix B | [SYNTHETIC] illustrative satisfiability note; off-program N values only; six SYNTHETIC labels per value |
| M3 | §9 | certifier operating characteristics and limits (explicit banned-content list: no rates, no ROC, no retroactive gate-firing) |
| Q1 | §5 + Appendix A.2 | `reporting_mode` recording field (renamed from `evaluation_mode` per CS feedback); firewall guards; cross-attempt contamination clause |
| Q2 | Abstract / §6 / §10 | three quote-safe non-claim blocks preserved; functional alignment per Team Lead Option A adjudication |
| H3 | masthead + §A.1 + §8 | framework supersession rule (only latest released identifier lock-eligible) |
| G1 | governance | strengthened transfer rule (SEND-TO-CS = intent; delivery = confirmed commit SHA) — operating governance, not manuscript text |

Additionally, the three CS soft observations from the Draft 2 review
(commit `21e33cc`) were adopted into Draft 3 (the RC manuscript):

| Observation | Section | Status |
|---|---|---|
| A — D2b binding-vs-reported_only justification | §4 D2b | adopted; binding/reported_only choice must be justified in threshold-sheet statistical plan |
| B — cross-attempt `full_profile` contamination | §5 | adopted; full_profile diagnostics may not derive or adjust subsequent attempts' thresholds |
| C — gate provenance table header | §2 | adopted; header reads "Documented motivating record — ancestry, not validation" |

## 5. v1.0 disposition

The v1.0 tag (`paper3-certification-protocol-v1.0`) and its tagged
manuscript blob are **unmodified**. v1.0 is now **superseded-released**:

- Lock-eligibility by default: **NO** (H3 supersession rule applies).
- Use of `paper3-certification-protocol-v1.0` as a `framework_version`
  on a new threshold sheet: refused by default; allowed only under
  explicit written Manager authorization naming the older identifier
  and the specified purpose, recorded in the governance archive.
- Historical reference: the v1.0 manuscript, PDF, and release record
  remain accessible at the v1.0 tag and at
  `governance/2026-06-10_paper3-v1.0-release/RELEASE-RECORD.md`.

The Paper 2 v1.0 lesson on never moving a tag remains in force for
both v1.0 and v1.1 tags.

## 6. Authorization chain

| Step | Actor | Artifact |
|---|---|---|
| v1.1 scope authorized | Manager | `governance/2026-06-10_paper3-v1.0-release/MANAGER-AUTHORIZATION-v1.1-SCOPE.md` |
| v1.1 scope intake | Senior | `governance/2026-06-10_paper3-v1.0-release/PAPER3-KNOWN-ISSUES-AND-DEFERRALS.md` |
| Draft 2 review accepted | Team Lead + CS | commit `21e33cc` (CS review); commit `bcb38c2` (Team Lead hold-posture) |
| Q2 §9/§10 adjudicated | Team Lead | Option A accepted; commit `bcb38c2` |
| Draft 3 G1 SEND-TO-CS | Senior | `Apiana_Papers/.../v1.1/G1-DELIVERY-NOTE-DRAFT3.md` |
| Draft 3 G1 verification | CS | commit `7585afd` |
| PDF G1 SEND-TO-CS (Option A) | Senior | `Apiana_Papers/.../v1.1/G1-DELIVERY-NOTE-RC-PDF.md` |
| v1.1 release authorized | Manager | "Manager Authorization — Paper 3 v1.1 Release" 2026-06-10 |
| Release executed | CS | commit `f769c03` + tag `paper3-certification-protocol-v1.1` (this record) |
| Independent confirmation | Senior | pending Senior post-tag confirmation |

## 7. Non-authorizations carried forward

This release does **not** authorize:

```text
Lane 1a execution
ladder construction
candidate selection
candidate ranking
threshold-sheet population
threshold lock
certification evaluation
new runs
INT8 / INT4 stress
multi-model execution
B1 v2.1 implementation
Claim C activation
Fork A reactivation
Paper 3 application
Paper 6 activation
public benchmark packaging
```

All execution gates remain closed. v1.1 lock-eligibility is a
precondition, not an authorization.

— CS Engineer, 2026-06-10
