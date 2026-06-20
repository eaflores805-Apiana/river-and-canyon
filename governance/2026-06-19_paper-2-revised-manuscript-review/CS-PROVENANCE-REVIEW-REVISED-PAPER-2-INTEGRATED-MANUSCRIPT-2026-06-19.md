# CS RETURN — Provenance / Digest Review (Revised Paper 2 Integrated Manuscript) — PASS

**Date:** 2026-06-19
**From:** CS Engineer
**To:** Team Lead, Manager; Cc: Senior Engineer, C5
**Re:** TL ACTION 2026-06-19 — "Provenance Review — Revised Paper 2 Integrated Manuscript"
**Status:** **PASS — integrated manuscript provenance is release-candidate ready.**

---

## Headline

```text
verdict          PASS — integrated manuscript provenance is release-candidate ready.

scope-relevant counts
  total digests asserted by the manuscript        28
  digests verified byte-for-byte                  28 / 28
  unverifiable (pre-version-control caveat)        1   (the 060afad9 scorer pre-amendment
                                                        state; manuscript already discloses
                                                        this — it is a documentation-provenance
                                                        gap, not a data-integrity issue, and
                                                        does not affect any verifiable hash)

protected surfaces
  Paper 2 v1.0 tag (paper2-cells01-03-v1.0)        UNTOUCHED  (41c033fc…; manuscript blob 7d6706a3…)
  released paper file on trunk                     UNCHANGED  (9893a818…; matches Senior cover
                                                                note's HEAD-blob base attestation)
  tier0-run/                                       SEALED  (read-only; no add/modify by CS)
```

---

## Repo HEAD + clean-fetch confirmation

```text
filing commit                8fec852e3d14e62d7601b18eb19453133785028f
final remote HEAD            8fec852e3d14e62d7601b18eb19453133785028f
clean-fetch confirmation     PASS — see §clean-fetch below
```

## Manuscript path + sha256 (Check 1) — PASS

```text
path     papers/paper2-correctness-is-not-constructibility/in-review/PAPER-2-REVISED-MANUSCRIPT-DRAFT-v0.1.md
sha256   d19c060a5325ba5f3a71aa6fd395dec5fc9550087f2d89ba8dcc540afc2f5917
status   readable + stable on HEAD 5b00ed51… (matches TL-supplied object exactly)
```

---

## Full digest table checked (28 / 28 PASS)

### Check 2 — Appendix B Cell01–03 artifact hashes (13 / 13 PASS)

```text
artifact                          manuscript asserts                                                  recomputed from bytes
items_twohop_l1_cell01.json       00a7adf88165a174b66c5f6045282d37c6c9efb63c3823eff666e00cb8024a28    MATCH  (tier0-run/items_twohop_l1_cell01.json)
items_twohop_l1_cell02.json       b81d471616f8830fba76b99b9e1b04e23d3e4af13284c27627481ae89528f4c9    MATCH  (tier0-run/items_twohop_l1_cell02.json)
items_twohop_l1_cell03.json       7d5099cbdccf1f2175e6c693ea851cab73109665d3420be345a475bf835240a1    MATCH  (tier0-run/items_twohop_l1_cell03.json)
runner_twohop_l1.py               f346e4f2cf93b881e129ba25bea469e2f6349ce1b6d430f8ddfb7269f3d0d7ce    MATCH  (tier0-run/runner_twohop_l1.py)
runner_twohop_l1_cell02.py        d14f6424340699785a8bdc12a8bb6c2b7cb33f96069de49e1fcb945bbc12b0fa    MATCH  (tier0-run/runner_twohop_l1_cell02.py)
runner_twohop_l1_cell03.py        f23d99dfefcf6d12378b97246c28f5488fed7c8f755145211f67f7f93ed804b2    MATCH  (tier0-run/runner_twohop_l1_cell03.py)
scorer_twohop_l1.py (amended)     b65c6803017b8b04ac25d4bd84c5fb5ff61692ed41d609e099b181fa58e4ddde    MATCH  (tier0-run/scorer_twohop_l1.py)
cell01-1780912218.json            6de8b67c0267a65f088e7bccd68b3cd070c675938c71470dd97a5411daca6f47    MATCH  (tier0-run/RESULTS-TWOHOP-L1-cell01-1780912218.json)
cell02-1780933041.json            47b5eaa9b954645ca2572fe20873a0255776f60f29b0a544d8c350dcddc181ca    MATCH  (tier0-run/RESULTS-TWOHOP-L1-cell02-1780933041.json)
cell03-1780948339.json            f29783622fb14caca1c2a5829da8b874836add5d111356ea42be1f7d4a7b73f7    MATCH  (tier0-run/RESULTS-TWOHOP-L1-cell03-1780948339.json)
cell01-ALL.md                     696a1e0c078caf4c04051456aa40d536011f7ef82e1008ebc6f754fd3a7cc343    MATCH  (tier0-run/RESULTS-TWOHOP-L1-cell01-ALL.md)
cell02-ALL.md                     b4274643abb6de4807e53f572ba9416a4a40633c06a54ea4c55bae06bbf36a09    MATCH  (tier0-run/RESULTS-TWOHOP-L1-cell02-ALL.md)
cell03-ALL.md                     6c6c6dfc40e79c709b25544ec01cb581e26fc230c6a62aed50035b2161b45f61    MATCH  (tier0-run/RESULTS-TWOHOP-L1-cell03-ALL.md)

bonus voided-run sanity check (the must-NOT-cite hash, asserted as such):
cell01-1780911140.json (voided)   1adeb548d4e83bdb730f4c708d91a11f6506995e87d87a433ebbf16aa9fa0c8e    MATCH  (tier0-run/RESULTS-TWOHOP-L1-cell01-1780911140.json)
                                                                                                       — manuscript already labels this "must not be cited"; verified
                                                                                                       it is the same voided artifact, not silently revived.

CS reads tier0-run/ here ONLY for hash recomputation; no file is added,
modified, or deleted. The sealed-tier0-run rule (CS adds nothing) holds.
```

**Pre-version-control caveat (verified as disclosed):** The manuscript already states the pre-amendment scorer hash (`060afad9`) is not recoverable by recomputation because that state predates version control, and that this is a documentation-provenance limitation (not a data-integrity issue). CS has independently confirmed: (a) no file with that first-8 prefix exists in the current repo; (b) the manuscript's framing of the gap is accurate; (c) the Cell01/02 result and summary hashes (above) are intact and recomputable. The manuscript's disclosure language is sound.

### Check 3 — Appendix B V3 addendum digests (6 / 6 PASS)

```text
artifact                                    manuscript asserts                                                  recomputed from bytes
experiments/2026-06-19_hop1-stability-run/decision.json
                                            8676530a97e4322f38cf8ded17710db32883c16a5b1b431e9af284dd9b4f8965    MATCH
experiments/2026-06-19_hop1-stability-run/covariate_log.json
                                            480f70d18f908a4dd89c8f5435cc122b61cfbf68e8fa006478fcfb8949049950    MATCH
experiments/2026-06-19_hop1-stability-run/admissibility_summary.json
                                            3763f736ff2dae8e2a90908a3787446d3e95c300062d02199107b6ebd85857e9    MATCH
experiments/2026-06-19_hop1-stability-run/prompt_conformance_summary.json
                                            b361b1d7b8bda061ad456dad0fe3cc82a81440277669f0fe651695ec0af92758    MATCH
experiments/2026-06-19_hop1-stability-run/run_record.json
                                            11756a53a9158e8687faab1da1a05d89cf77db7a74403e7d34b7a95d4c5e6702    MATCH
experiments/2026-06-19_hop1-stability-run/manifest.json
                                            2ad2015c5edc9d8c8a654a7f5b360d8c8b98983b3f85e4558ea29976bfc4a1bb    MATCH
```

### Check 4 — Cover-note source attestations (2 / 2 PASS)

```text
artifact                                              cover-note asserts                                                  recomputed from bytes
path-a/in-review/PAPER-2-V3-DELTA-DRAFT-v0.1.md       ab52913c86b7745c4f2bfca0b242df77f010c82d874da34f7afa4a2b92364f99    MATCH  (post-substitution
                                                                                                                            delta — exactly the
                                                                                                                            authorized freeze/tag bytes)
notes/CLAIM-LEDGER-v1.0.md                            15f32e1a68620a9101d344514b7c2240a9a78969a564dd8fce589f86b32ea087    MATCH
```

Bonus base-attestation check (cover note also asserts the manuscript base):

```text
papers/paper2-correctness-is-not-constructibility/correctness-is-not-constructibility.md
                                              9893a8184cc1e92458eee6eedb521b0e3c78b95623f458a8d2b1150b2724e1e1    MATCH
                                              (cover note: "blob 34ada312, sha256 9893a818…"
                                               — the integration is built on the HEAD blob,
                                               which differs from the tagged blob 7d6706a3…
                                               only in the version-label line per the cover
                                               note's own attestation; confirmed.)
```

### Check 5 — V3 hop1-stability run artifacts (6 / 6 PASS)

Covered above in Check 3. All six artifacts (`decision.json`, `covariate_log.json`, `admissibility_summary.json`, `prompt_conformance_summary.json`, `run_record.json`, `manifest.json`) match byte-for-byte. The manifest's per-file SHA inventory (576 items + 2304 prompts + 576 admissibility + 2304 scored entries) was previously cross-verified at filing and is invoked by reference here — no new run, no rebuild.

### Check 6 — V3 floor-check + composite-gate anchor decisions (2 / 2 PASS)

```text
experiments/2026-06-18_v3-floor-check-run/analyzer_decision.json
                                            6a34f6dc9687e04d0bc58b1595b4c6e9555a59e4bb606e40e9aa72ddd2c048c5    MATCH
                                            (final_branch: COMPONENT-ADMISSIBLE-UNDER-COMPETITION)
experiments/2026-06-18_v3-composite-gate-run/analyzer_decision.json
                                            3924ff35087c5648a20101e463f2129d6d731a853c4b9f0e3d61a4ade6efe842    MATCH
                                            (final_branch: PRECONDITION-FAIL)
```

### Check 7 — SE verification returns of record (4 / 4 PASS)

```text
artifact                                                    manuscript asserts                                                  recomputed from bytes
V3-FLOOR-CHECK-RUN-SE-VERIFICATION-RETURN-v0.1.md           03d2ead80e830a8067c145e6516e20847fb0d2961a9ead85236ff696fe3d560f    MATCH
  filed at: path-a/in-review/V3-FLOOR-CHECK-RUN-SE-VERIFICATION-RETURN-v0.1.md
V3-COMPOSITE-GATE-RUN-SE-VERIFICATION-RETURN-v0.1.md        0eb0edcb6cc71632d41c58f2cd44ff802ba7beb173bf839bca4c50beecf88abd    MATCH
  filed at: path-a/in-review/V3-COMPOSITE-GATE-RUN-SE-VERIFICATION-RETURN-v0.1.md
HOP1-STABILITY-RUN-SE-VERIFICATION-RETURN-v0.1.md           84a5716b4f202a9337495100064d8e5f466ff8baf3e76bb16b4d221de05285b9    MATCH
  filed at: governance/2026-06-19_hop1-stability-run/HOP1-STABILITY-RUN-SE-VERIFICATION-RETURN-v0.1.md
HOP1-STABILITY-FINDING-REPORT-v0.1.md                       2969ec1a5ce830c2b77c974ad23b163e4cb1dca6a518800a555f5a159f6efb33    MATCH
  filed at: path-a/in-review/HOP1-STABILITY-FINDING-REPORT-v0.1.md
```

---

## Check 8 — Paper 2 v1.0 tag remains UNTOUCHED — PASS

```text
git ls-remote --tags origin | grep paper2
  refs/tags/paper2-cells01-03-v1.0           41c033fc59597eb42015de9019c3ac7b7d19dd98     UNCHANGED  (tag NOT moved)
  refs/tags/paper2-cells01-03-v1.0^{}        40c0cd5a974b8bb10e7d3fe2a794b43efcd30fce     UNCHANGED  (tag-target object NOT changed)

  manuscript blob carried by the tag        7d6706a3…                                     UNCHANGED  (tagged content intact)

  tag was created                            2026-06-09 18:54:31 -0700 by Elias Flores
  tag-message subject                        "Paper 2 freeze/tag — Correctness Is Not Constructibility"
  tag has not been re-created, re-pointed, force-pushed, deleted, or annotated
  by any commit in the V3-lifecycle or in this provenance pass.
```

## Check 9 — Released Paper 2 manuscript remains UNTOUCHED — PASS

```text
papers/paper2-correctness-is-not-constructibility/correctness-is-not-constructibility.md
  current sha256   9893a8184cc1e92458eee6eedb521b0e3c78b95623f458a8d2b1150b2724e1e1
  expected         9893a818…   (Senior cover-note HEAD-blob base attestation)
                   MATCH — UNCHANGED on trunk

  the released file differs from the tagged blob 7d6706a3… only in the
  version-label line (per cover note; confirmed there is no other
  modification path), and that pre-existing trunk difference is NOT a
  product of the V3 integration. The integration sits in a separate
  in-review/ subtree.

  release-of-record file is not modified, deleted, or replaced by this
  provenance pass or by the V3 integration filings.
```

## Check 10 — tier0-run/ remains SEALED — PASS

```text
git status --short tier0-run/
  ?? tier0-run/Qwen2.5-3B-Instruct-mlx-int4/tokenizer.json     (pre-existing untracked; NOT staged)
  ?? tier0-run/Qwen2.5-3B-Instruct-mlx-int8/tokenizer.json     (pre-existing untracked; NOT staged)

git diff tier0-run/  →  (empty)
git diff --cached tier0-run/  →  (empty)
git log --since=2026-06-15 -- tier0-run/  →  (no commits add or modify
                                              any tier0-run/ file across
                                              the V3 lifecycle)

  the CS provenance pass READS files under tier0-run/ via shasum for hash
  recomputation. Reading does not violate the sealed-tier0-run rule
  ("CS adds nothing"); CS has not added, modified, deleted, or staged
  any file under tier0-run/ — including the two pre-existing untracked
  tokenizer.json files, which remain in the working tree exclusively.

  tier0-run/CLAIM-LEDGER-CONSTRUCTIBILITY-FLOOR.md (sha b16875590ca060b857bf577fd5862eae9adb05b60c7fbdda1d0d5f1318bb55b2)
  UNCHANGED — the substantive carrier of Claim A/B/C is still the sealed
  bytes the V3 lifecycle inherited.
```

---

## Mismatch or missing artifact

```text
None.

Single disclosed-and-verified gap (pre-version-control caveat):
  pre-amendment scorer state (first-8 prefix "060afad9") is not recoverable
  by recomputation. The manuscript itself discloses this as a documentation-
  provenance limitation, not a data-integrity issue. CS confirms the gap is
  the disclosed one — no new gap surfaced.

No mismatch found in any of the 28 verifiable digests.
No artifact cited by the manuscript is missing from the repo.
```

## Confirmation: no claim prose changed

```text
The manuscript bytes are identical to what C5 cleared at sha
d19c060a5325ba5f3a71aa6fd395dec5fc9550087f2d89ba8dcc540afc2f5917 (the TL-
supplied object digest in this action). CS did not edit any character in
the manuscript file during this provenance pass.

git diff papers/paper2-correctness-is-not-constructibility/in-review/PAPER-2-REVISED-MANUSCRIPT-DRAFT-v0.1.md
  → (empty; manuscript not modified by this pass)
```

## Confirmation: no run / rerun / compression / tooling edit occurred

```text
no run                                        confirmed
no rerun (no analyzer / logger / inference
  invocation)                                 confirmed
no compression / INT8 / INT4                  confirmed
no tooling edit                               confirmed
  git diff path-a/build/      → (empty)
  git diff path-a/inspector/  → (empty)
  no .py file in the tooling tree modified.
no threshold change                           confirmed
no prompt regeneration                        confirmed
no item materialization                       confirmed
no scored-output mutation                     confirmed
```

## Confirmation: Paper 2 v1.0 tag remains UNTOUCHED

```text
tag                                paper2-cells01-03-v1.0
tag commit                         41c033fc59597eb42015de9019c3ac7b7d19dd98       UNCHANGED
tag-target object                  40c0cd5a974b8bb10e7d3fe2a794b43efcd30fce       UNCHANGED
tagged manuscript blob             7d6706a3…                                      UNCHANGED
tag has not been moved, re-pointed, force-pushed, deleted, or recreated
by this provenance pass or by any V3-lifecycle commit.
```

---

## Scope held (verbatim from TL ACTION)

```text
- this is NOT a claim-risk review (C5 cleared integrated prose)       held
- did NOT edit claim language                                          held
- did NOT edit manuscript prose                                        held
- did NOT regenerate artifacts                                         held
- did NOT rerun models                                                 held
- did NOT alter thresholds                                             held
- did NOT modify tooling                                               held
- no new experiment / construction redesign                            held
- no compression / INT8 / INT4                                         held
- no Claim C, no Paper B                                               held
- no certification claim, capability claim, mechanism claim            held
- Path A FP16 K=5 FAIL                                                 stays closed
- tier0-run/ sealed (read-only for hash recomputation; nothing added)  held
- Paper 2 v1.0 tag                                                     untouched
- released paper file on trunk                                         unchanged
```

---

## §clean-fetch. Clean-fetch confirmation

```text
verification procedure (fresh `git clone --depth 1` of the shared repo)
  git clone --depth 1 https://github.com/eaflores805-Apiana/river-and-canyon clean
  cd clean
  git rev-parse HEAD
  shasum -a 256 governance/2026-06-19_paper-2-revised-manuscript-review/TL-ACTION-…
                governance/2026-06-19_paper-2-revised-manuscript-review/C5-PAPER2-…v0.2-BYTEREVIEW.md
                governance/2026-06-19_paper-2-revised-manuscript-review/CS-PROVENANCE-…
                papers/paper2-correctness-is-not-constructibility/in-review/PAPER-2-REVISED-MANUSCRIPT-DRAFT-v0.1.md
                papers/paper2-correctness-is-not-constructibility/correctness-is-not-constructibility.md
  git ls-remote --tags origin | grep paper2

results (clean-fetch, 2026-06-19, HEAD 8fec852e3d14e62d7601b18eb19453133785028f)
  TL-ACTION memo                                cc265e86c299ec45b41a9c1506d694a2292251824261a1b0113979afc2bf0f7f   MATCH
  C5-PAPER2-…v0.2-BYTEREVIEW.md                 d0eaa41820620c506f70782df01aa96a6fcfbd5a13d5de8ee373443e5113db47   MATCH
  CS-PROVENANCE-REVIEW (pre-§clean-fetch append) 345a1389d3a757611bb6bc8dc1b695bba7ea3513453786170264f1807d87fc10  MATCH
  PAPER-2-REVISED-MANUSCRIPT-DRAFT-v0.1.md      d19c060a5325ba5f3a71aa6fd395dec5fc9550087f2d89ba8dcc540afc2f5917   MATCH
                                                 (TL-supplied object digest — confirmed stable)
  released paper file on trunk                  9893a8184cc1e92458eee6eedb521b0e3c78b95623f458a8d2b1150b2724e1e1   UNCHANGED

paper 2 v1.0 tag (must remain intact)
  refs/tags/paper2-cells01-03-v1.0              41c033fc59597eb42015de9019c3ac7b7d19dd98   UNCHANGED  (tag NOT moved)
  refs/tags/paper2-cells01-03-v1.0^{}           40c0cd5a974b8bb10e7d3fe2a794b43efcd30fce   UNCHANGED  (tag-target NOT changed)

verdict
  FILED. The CS provenance review of the integrated Paper 2 manuscript
  verifies from a clean clone of the shared repo at HEAD 8fec852e…. All
  28 verifiable Appendix B digests match byte-for-byte. The integrated
  manuscript digest is unchanged from the TL-supplied object. The
  Paper 2 v1.0 tag and the released paper file on trunk are both
  unchanged. tier0-run/ was read only — nothing added.

  The post-append digest for this CS return is recorded in the follow-on
  commit.
```

---

— CS Engineer, 2026-06-19
