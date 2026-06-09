# Experiments — layout convention

*Proposed by Senior Engineer for adoption. Intended to land at `experiments/README.md`.
Applies to ALL experiments going forward.*

## The bright line

`tier0-run/` is **sealed** as of the Paper 1 / Paper 2 freeze/tag. It is the frozen
provenance record for *Survival Is Not Correctness* and *Correctness Is Not
Constructibility*. Its files are referenced by `sha256` at their current paths in the
papers' Appendix B, so moving, renaming, or adding to it would break the locked
provenance and invalidate the freeze.

- **Do not add files to `tier0-run/`.** Ever. Not Cell04, not B1 harness-hardening
  output, not a KV-grid or certification probe, not a compression rung if one unlocks.
- **All new experiments land under `experiments/`**, in the per-experiment layout below.
- The directory is *not* reorganized to this layout — its flatness is the cost of having
  sealed it correctly, and that cost is paid once.

## One directory per experiment

```
experiments/<YYYY-MM-DD>_<slug>/      e.g. 2026-07-01_twohop-l2-cell04
  PREREGISTRATION.md     hypothesis, design, predeclared outcomes, stopping rule,
                         tier + track fields, gate thresholds — written BEFORE the run
  construction/          item / cell construction and stage docs
  manifest/              items_*.json   (locked input)
  code/                  runner_*.py, scorer_*.py, prompt_template_*.txt   (locked)
  results/               RESULTS-*.json + *-ALL.md summaries
  PROVENANCE.md          sha256 of every locked file above; model snapshot WITH its
                         assertion/runner-backing status; run config; environment
  DISPOSITION.md         gate outcomes; what it showed; claim-ledger linkage;
                         and the negative-result reading (Lock 5)
```

Date-prefixed slugs sort chronologically and never collide. `tier` and `track` are
fields inside `PREREGISTRATION.md`, not directory levels — more flexible once stress
and certification work branches.

## Rules carried over from program governance (enforced by the layout)

1. **Pre-registration before run.** `PREREGISTRATION.md` exists and is committed before
   any run; outcomes are not defined post-hoc.
2. **Provenance honesty.** `PROVENANCE.md` states whether the model snapshot is *asserted*
   or *runner-provenance-backed*. Never assert backing that does not exist.
3. **Negative-result form (Lock 5).** `DISPOSITION.md` includes the negative reading; no
   experiment is allowed to carry only a positive interpretation.
4. **Claim-ledger linkage.** `DISPOSITION.md` states the result in claim-ledger terms and
   names which claim (A / B / C …) it touches, and how.

## Governance records

Governance lives with its era. The Paper 1–2 alignment records stay in
`tier0-run/governance/2026-06-09_post-paper2-alignment/` — they are part of the sealed
record. New governance records go in a root-level `governance/`, created when first
needed. (Splitting governance across two locations is intentional: the old set is sealed
with the papers; the new set keeps growing.)
