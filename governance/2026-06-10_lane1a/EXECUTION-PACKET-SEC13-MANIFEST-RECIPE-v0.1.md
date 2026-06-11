# Execution Packet §13 — Normative Manifest Construction Recipe (v0.1, DRAFT for combined review)

From: CS Engineer · To: Senior Engineer, Team Lead, Manager
Date: 2026-06-10
Status: Normative recipe text; references the design packet §1.2–§1.5 and Senior intent-confirmation §3 eight requirements; pre-registered design surface; freezes on LOCK-RECORD

---

## 0. Status of this document

This is **§13 of the Lane 1a Execution Packet**, written as normative
text rather than implementation detail per Senior intent confirmation
§3. The `manifest_generator.py` docstring refers to this section as
the specification; if there is conflict between code and this text,
the lock review treats this text as authoritative and re-locks the
code.

All variables named here are referenced by `classification_criteria.yaml`
and the per-rung schema; constants here are pre-registered before lock
and not changeable after.

Doctrine restated: **Lane 1a may rule out; Lane 1a may not rule in.**
The recipe is pre-registered before first data access; the no-edit-
after-lock rule applies.

Artifact class for all manifests produced: `lane-1a-reconnaissance`.
Certification relevance: `none`.

---

## 1. Determinism (Senior §3 item 1)

**Seed.** All manifest construction is driven by a single integer
seed pre-registered in `LOCK-RECORD.md` under the key
`manifest_recipe_seed`. The seed value is the canonical sweep ID
hashed to a 64-bit integer:

```text
manifest_recipe_seed = int.from_bytes(
    sha256("lane-1a-2026-06-10".encode("utf-8")).digest()[:8],
    "big"
)
```

This expression itself appears in `LOCK-RECORD.md` and is recomputable;
the seed value is also recorded explicitly for auditor convenience.

**RNG.** All randomness uses `numpy.random.Generator` with the
`PCG64DXSM` bit generator initialized from `manifest_recipe_seed`.
Per-rung sub-seeds are derived deterministically:

```python
def per_rung_seed(rung_id: str) -> int:
    return int.from_bytes(
        sha256(f"{manifest_recipe_seed}:{rung_id}".encode("utf-8")).digest()[:8],
        "big"
    )
```

Producing the manifest for `L01` uses `per_rung_seed("L01")`; same
for `L02`...`L08`. Re-running the manifest generator with the same
LOCK-RECORD yields byte-identical manifests by construction.

**Reproducibility check.** The lock review verifies bit-identity by
running the manifest generator twice on separate machines (or twice
in clean environments on the same machine) and checking the sha256
of every per-rung manifest matches.

## 2. Answer-slot position distribution (Senior §3 item 2)

**Statement.** For each answerable item on each rung, the position of
the answer key (the queried key) within the in-context distractor
list is drawn from the discrete uniform distribution over the available
position indices, *before* the K and X axes apply any structural
constraint.

**Concretely.** For rung with D distractors:
- The context contains D+1 key/value pairs (D distractors + 1 answer).
- The answer-key position `answer_pos` is drawn:
  `answer_pos ~ DiscreteUniform({0, 1, ..., D})`
- The position distribution is pre-declared as uniform; any future
  diagnostic that probes positional bias has a well-defined null.

**Why uniform.** Senior §3 item 2: *"answer-slot position uniformly
distributed over context positions per rung, distribution
pre-declared — so the positional and recency dummy policies have
well-defined, non-degenerate predictions rather than accidental ones."*
Uniform distribution gives the `pure_last_position` policy an exact
expected hit rate of `1/(D+1)`; the `target_recency` policy (predicts
the last key encountered) likewise has a well-defined null. Without
this pre-declaration, dummy-policy predictions become accidental
artifacts of construction.

**Distribution audit field.** Per-rung records carry an `answer_pos_distribution`
field (histogram of the 80 answerable items' `answer_pos` values) so
deviation from uniform is visible in the audit log. The sweep
acceptance check (§8) verifies the empirical distribution does not
deviate from uniform by more than 3 standard deviations on any bin.

## 3. K axis — key confusability (Senior §3 item 3)

The K axis takes values `low` and `high`. Definitions are concrete
and locked in `classification_criteria.yaml`.

### 3.1 K = low (maximize pairwise prefix distance)

**Vocabulary.** Keys drawn from a pool of unique multi-character
identifiers with **declared pairwise prefix-distance constraint**:

```text
For all pairs (k_i, k_j) in the per-rung key set:
    pairwise_prefix_distance(k_i, k_j) >= MIN_PREFIX_DISTANCE_LOW
where pairwise_prefix_distance(a, b) is the number of leading characters
that differ between a and b (first-difference index from the left).
```

Locked constant:

```yaml
MIN_PREFIX_DISTANCE_LOW: 1   # all key pairs differ at the very first character
                             # (i.e., no two keys share a common leading character)
SWEEP_CLASSIFICATION_NOT_A_THRESHOLD_VALUE: true
```

**Construction.** The key pool is a curated alphabet of identifiers
whose first character is unique across the rung's selected D+1 keys.
The recipe picks D+1 distinct first-letters, then completes each key
with a deterministically generated 5-character suffix:

```python
# Pseudocode
rng = numpy.random.Generator(PCG64DXSM(per_rung_seed(rung_id)))
first_letters = rng.choice(BASE_ALPHABET_LOW, size=(D+1), replace=False)
keys = [letter + deterministic_suffix(letter, rng) for letter in first_letters]
```

`BASE_ALPHABET_LOW` is a 26-letter lowercase Latin alphabet (a-z) —
exhaustively recorded in `classification_criteria.yaml`.

### 3.2 K = high (shared-prefix family with declared common-prefix length)

**Vocabulary.** Keys drawn from a single shared-prefix family with a
declared common-prefix length.

Locked constants:

```yaml
COMMON_PREFIX_LENGTH_HIGH: 3   # all keys in the rung share a 3-character leading prefix
                               # disambiguating suffix begins at position 4
KEY_TOTAL_LENGTH: 6            # so D+1 keys = same 3-char prefix + 3-char suffix
                               # gives up to 26^3 = 17,576 disambiguable keys per family
SWEEP_CLASSIFICATION_NOT_A_THRESHOLD_VALUE: true
```

**Construction.** Per rung, a single 3-character prefix is drawn
deterministically; then D+1 distinct 3-character suffixes are drawn
deterministically to complete the keys:

```python
# Pseudocode
rng = numpy.random.Generator(PCG64DXSM(per_rung_seed(rung_id)))
common_prefix = "".join(rng.choice(list("abcdefghijklmnopqrstuvwxyz"), size=3, replace=False))
suffix_set    = sorted({deterministic_3char(rng) for _ in range(2 * (D+1))})[:(D+1)]
keys          = [common_prefix + suffix for suffix in suffix_set]
```

The `homogeneous_prefix_completion` dummy policy now has a
well-defined exact prediction: "predict the next character as the
continuation of the common prefix that maximizes shared-prefix
match in the answer key" — and its expected hit rate is the per-item
probability that the model's homogeneous-prefix continuation matches
the actual queried suffix.

### 3.3 Why this matters

Without these explicit definitions, dummy-policy predictions are
accidental — a key set might happen to be all-distinct-first-chars on
some seeds and all-shared-prefix on others. Senior's failure-mode
question 3 (unordered survivors → implicit ranking) is closed in part
by ensuring the dummy-policy battery has well-defined predictions on
every rung; the K-axis lock is the construction-side guarantor of
that.

## 4. Distractor values type-matched to targets (Senior §3 item 4)

**Statement.** For every item, the answer value and all distractor
values are drawn from the same value-type pool. No item is solvable
by type-elimination alone.

**Value pool.** A single declared value pool is used for all rungs and
all items. The pool contains uniform-format string values
("city-style" entries — short multi-character strings without
embedded numerics that could be eliminated by type-classification).
The value pool is exhaustively listed in
`classification_criteria.yaml` and frozen at lock time.

**Per-item construction.** For each answerable item:

```python
# Pseudocode
target_value = rng.choice(VALUE_POOL, size=1)
# Distractor values: D unique values from the pool, excluding target_value
distractor_values = rng.choice(
    [v for v in VALUE_POOL if v != target_value],
    size=D,
    replace=False,
)
```

**Type-elimination protection.** A future analyzer could probe for
type-elimination by checking whether the model's output is in the
value-pool union. If type-elimination were a free dimension (e.g.,
distractor values were numeric and the answer were a city name), the
model could "answer correctly" without retrieval. The recipe forbids
this by construction.

## 5. NULL items — queried key absent from context (Senior §3 item 5)

**Statement.** Each rung's NULL stratum (16 items per rung) is
constructed identically to the answerable stratum, EXCEPT the queried
key is replaced with a key that does not appear in the in-context
distractor list.

**Construction.** Per NULL item:

```python
# Pseudocode
# Build the in-context key set as in §2 (D+1 keys)
in_context_keys = [...]
# Sample a "decoy queried key" that DOES NOT appear in in_context_keys
decoy_pool = [k for k in vocabulary_for_rung if k not in in_context_keys]
queried_key = rng.choice(decoy_pool, size=1)
# Compose the item: in-context list + the absent queried key
item = {
    "in_context_pairs": list(zip(in_context_keys, distractor_values_for_this_item)),
    "queried_key": queried_key,
    "expected_answer": "NULL",
    "stratum": "null",
}
```

**Why this matters.** The abstention contract D4 depends on the model
correctly identifying that the queried key is absent. A NULL item
must be structurally indistinguishable from an answerable item except
for the absence — otherwise the abstention diagnostic measures
type/format detection rather than actual abstention.

**Mechanical separability.** The `separability_flag` in the per-rung
record is set true iff the locked classifier can mechanically
distinguish a NULL output from an error output (e.g., the model emits
a designated NULL sentinel for NULL items and a value-pool entry for
answerable items). The classifier is locked at lock time and
hash-recorded; it does not have access to the truth label when
classifying.

## 6. Fresh entities only — Fork A bar applies (Senior §3 item 6)

**Statement.** No key, value, prefix, suffix, vocabulary item,
construction template, or manifest configuration may be reused from
any prior program artifact. The Fork A bar applies to **construction
inputs**, not only to artifacts.

**Specifically forbidden as construction inputs.** Manifests,
entities, key vocabularies, value pools, or distractor sets from:

- Paper 2 cells (Cell01, Cell02, Cell03)
- Two-Hop L1 program manifests
- Fork A artifacts (all)
- Any historical paper2-reproduction or paper3-certification artifact
- Any external benchmark dataset (MMLU, HumanEval, etc.)

**Lock-time check.** Before lock, CS computes a "construction-input
inventory hash" — the sha256 of the union of the value pool, the
K=low alphabet, the K=high common-prefix-family alphabet, and the
NULL-decoy alphabet — and compares against a published "novelty
ledger" of prior-program construction inputs. If any non-trivial
overlap is detected (more than `MAX_HISTORICAL_OVERLAP_FRACTION` of
entries), CS regenerates the construction inputs under a new seed
*before* lock. Post-lock, no regeneration.

Locked constant:

```yaml
MAX_HISTORICAL_OVERLAP_FRACTION: 0.05
SWEEP_CLASSIFICATION_NOT_A_THRESHOLD_VALUE: true
```

The novelty ledger lives at
`experiments/2026-06-10_lane-1a-sweep/NOVELTY-LEDGER.md` (a snapshot
of disallowed construction inputs from prior program work; populated
at lock time by CS).

## 7. Tokenization-stable vocabulary (Senior §3 item 7)

**Statement.** All keys, values, and format indicators must
demonstrably preserve BPE tokenization boundaries across the declared
permutation set.

**Declared permutation set.** Five permutations of each item are
evaluated for tokenization stability:

1. Original ordering.
2. Reverse ordering of distractor list.
3. Random permutation of distractor list (deterministic from
   `per_rung_seed`).
4. Swap of two random distractor entries (deterministic from
   `per_rung_seed`).
5. Cyclic shift of distractor list by `D//2` positions.

**Tokenization stability test.** For each candidate vocabulary entry,
CS tokenizes the full item under each of the five permutations using
the Qwen2.5-3B-Instruct tokenizer (locked at lock time;
hash-recorded). The entry passes stability iff the answer-key
tokenization, the queried-key tokenization, and the answer-value
tokenization are bit-identical across all five permutations.

Entries failing stability are excluded from the vocabulary. If the
exclusion drops the available pool below the minimum needed for D=16
+ NULL decoys, CS expands the candidate pool deterministically (next
seed-derived expansion batch) and re-checks until the constructive
constraint is satisfied.

**Per-rung tokenization-stability record.** `tokenization_stability_flag`
in the per-rung record is `true` iff the entire rung's manifest
passes the test on all 80 answerable + 16 NULL items at lock time.
Any rung with a `false` flag at lock time triggers a recipe-failure
event: the manifest is regenerated under a new seed before lock.

## 8. Recipe acceptance check (Senior §3 item 8) — lock-blocking

**Statement.** Before lock, every declared dummy policy must yield a
**well-defined, non-constant** prediction vector on every rung's
generated manifest. A battery that cannot fire on the construction is
uninformative.

**The five declared dummy policies and their prediction surfaces.**

| Policy | Prediction rule | Non-degeneracy check |
|---|---|---|
| `pure_last_position` | Predict the value at the last position in the in-context list | Non-constant if last-position values vary across items |
| `target_recency` | Predict the value of the most recently mentioned key matching the queried key's first character | Non-constant if first-character mentions vary in position across items |
| `salient_endpoint` | Predict the value at either the first or the last position (whichever has higher salience by declared rule) | Non-constant if endpoint values vary across items |
| `copy_completion` | Predict by completing the queried key's tokens (treating the prompt as a copying task) | Non-constant if queried-key completions vary across items |
| `homogeneous_prefix_completion` | Predict the value of the in-context key sharing the longest prefix with the queried key | Non-constant if longest-prefix matches vary across items |

**Lock-blocking acceptance.** For each rung's generated manifest, CS
computes each policy's prediction vector (length 80, one entry per
answerable item) offline and checks two conditions:

1. **Well-defined.** Every entry is either a value from the value
   pool or a designated NULL sentinel. No entry is undefined.
2. **Non-constant.** The prediction vector has at least
   `MIN_NONDEGENERATE_DISTINCT_PREDICTIONS` distinct values across
   the 80 items.

Locked constant:

```yaml
MIN_NONDEGENERATE_DISTINCT_PREDICTIONS: 3
SWEEP_CLASSIFICATION_NOT_A_THRESHOLD_VALUE: true
```

A rung failing on any policy triggers a recipe-failure event: the
rung's manifest is regenerated under a new recorded seed *before*
lock. Post-lock, the no-re-execution rule governs.

**Per-rung acceptance record.** The per-rung record carries a
`recipe_acceptance_check` field (object with five booleans, one per
policy, and the distinct-prediction count). Required to be all-true
for the rung to be admitted to the lock record.

## 9. Lock-blocking summary

A rung's manifest passes recipe review iff **all** of the following
hold at lock time:

```text
1. answer_pos distribution within 3·SE of uniform across 80 items (§2)
2. K-axis prefix-distance constraint satisfied (§3.1 for K=low; §3.2 for K=high)
3. All distractor values drawn from declared value pool; no type elimination (§4)
4. NULL stratum constructed correctly; queried_key absent from in-context list (§5)
5. Construction-input overlap with novelty ledger < MAX_HISTORICAL_OVERLAP_FRACTION (§6)
6. Every item's tokenization is bit-stable across all 5 declared permutations (§7)
7. Every declared dummy policy yields a non-degenerate prediction vector with ≥ MIN_NONDEGENERATE_DISTINCT_PREDICTIONS distinct values (§8)
```

A failure on any check triggers regeneration under a new seed *before
lock*. Post-lock, the no-re-execution rule applies and any anomaly
yields `inconclusive_not_actionable`.

## 10. What `manifest_generator.py` will do

The actual `manifest_generator.py` script is a faithful implementation
of this recipe. Its docstring refers to this document as the
specification:

```python
"""
Lane 1a manifest generator.

Specification: governance/2026-06-10_lane1a/EXECUTION-PACKET-SEC13-MANIFEST-RECIPE-v0.1.md

If this code diverges from the specification, the specification is
authoritative; correct the code and re-lock with a new sha256.

DOCTRINE: Lane 1a may rule out; Lane 1a may not rule in.
ARTIFACT CLASS: lane-1a-reconnaissance
CERTIFICATION RELEVANCE: none

This script is hash-recorded in LOCK-RECORD.md. No edit permitted
after lock; corrections file as a new sweep with a new lock record.
"""
```

The script outputs:

- 8 per-rung manifests at
  `experiments/2026-06-10_lane-1a-sweep/manifests/{L01..L08}.json`
- `manifests/MANIFEST-HASHES.lock` — one-line-per-rung sha256
- `manifests/RECIPE-ACCEPTANCE-CHECK-RESULTS.json` — per-rung
  acceptance record
- `manifests/NOVELTY-LEDGER-CHECK.md` — confirmation that
  construction inputs cleared the novelty ledger check at lock time

All four output groups are hash-recorded in `LOCK-RECORD.md`.

## 11. Open question (none required)

CS has no remaining open question against the recipe. The recipe
adopts all eight of Senior §3's requirements verbatim, with concrete
constants for the items Senior left to CS judgment (D+1 sizing per
rung; explicit alphabet declarations; the tokenization permutation
set; the value-pool entry style).

If Team Lead or Senior identifies a constant that requires
adjustment, CS adjusts before lock per the discipline. After lock,
the constant is frozen.

---

— CS Engineer, 2026-06-10
