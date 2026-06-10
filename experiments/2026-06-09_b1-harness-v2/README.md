# B1 Harness v2 — Implementation

**Filed:** 2026-06-09
**Owner:** CS Engineer
**Status:** Implementation complete; Paper 2 regression infrastructure ready (live execution gated by separate decision)
**Authorization:** Manager / Team Lead memo, "B1 v2 implementation is authorized as bounded validity-harness infrastructure", 2026-06-09

---

## What this is (and isn't)

This directory is the implementation of the B1 v2 harness as bounded validity-harness
infrastructure. It is **not** an experiment in the sense the `experiments/` layout
convention was written for — it has no hypothesis, no run-outcome to disposition, no
PREREGISTRATION.md. It is harness code that future experiments and Paper 3 certification
attempts will use. The standard layout (`code/`, `manifest/`, `results/`, PROVENANCE.md)
is preserved; PREREGISTRATION.md and DISPOSITION.md are intentionally omitted.

## Driving specs

- B1 Implementation Plan v2 — `governance/2026-06-09_b1-harness-plan-revision/B1-IMPLEMENTATION-PLAN-V2.md`
- Paper 3 *Certification Before Retention* v0.4 §8 (B1 dependency)
- Paper 2 reproduction acceptance test plan
- Manager/Team Lead authorization memo (2026-06-09), Senior conditions C1–C3

## Contents

```
code/
  runner_b1_v2.py              # Main B1 v2 runner (configurable: paper2 / paper3 context)
  structural_proxies.py        # D5 substrate — model-free proxies from manifest only
  test_b1_harness.py           # 24 B1 unit tests (B1-T1 through B1-T24)
  paper2_regression.py         # Paper 2 reproduction regression test (Senior C1)
  scorer_twohop_l1.py          # COPY of tier0-run/ scorer; hash-verified at boot
  tasks_twohop_l1.py           # COPY of tier0-run/ tasks; hash-verified at boot
  prompt_template_twohop_l1.txt # COPY of tier0-run/ prompt template; hash-verified at boot
manifest/
  items_twohop_l1_cell03.json  # COPY of tier0-run/ Cell03 manifest; hash-verified at boot
results/
  (populated when runner executes; empty in tracked state)
PROVENANCE.md                  # locked file hashes, environment, version info
README.md                      # this file
```

The four copied foundation files are hash-verified at runtime against their tier0-run/
originals (Paper 2 v1.0 Appendix B). The Paper 2 evidence record in tier0-run/ is
untouched.

## Operational contexts

The runner is a single executable serving two contexts, selected by config flag:

**`--context paper2-reproduction`** (default)
- `framework_version = "none"`, no threshold sheet
- Output: v1-shape fields plus additive B1 v2 substrate
- Used for Paper 2 reproduction and any Two-Hop L1 work

**`--context paper3-certification`**
- `framework_version` set in config; validated against threshold sheet (Manager C2)
- Threshold sheet hash verified before content trust (Manager C3)
- Data-access firewall enforced (Paper 3 v0.4 D6)
- Used for Paper 3 certification attempts (no candidate selected yet)

## Quick start

```
# Run unit tests (all 24 + 2 sanity)
cd code
python3 test_b1_harness.py

# Dry-run smoke (no model load)
python3 runner_b1_v2.py --mode dry-run --context paper2-reproduction

# Live Paper 2 reproduction (loads model, runs 96 inferences on Cell03 manifest)
python3 runner_b1_v2.py --mode live --context paper2-reproduction

# Paper 2 regression vs locked Cell03 results (Senior C1)
python3 paper2_regression.py --mode full
```

## Non-authorizations

Implementing this harness does not authorize:

```
candidate selection · threshold values · new model runs · re-runs
INT8 / INT4 execution · unconditioned token-prior runs · activation logging
multi-model execution · Fork A reactivation · Claim C activation
Paper 3 execution as an experiment · public benchmark packaging
```

— CS Engineer, 2026-06-09
