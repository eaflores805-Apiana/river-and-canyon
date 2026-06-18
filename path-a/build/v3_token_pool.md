# V3 Token Pool — open-slot realization (2 of 5)

**Date:** 2026-06-17
**Author:** CS Engineer
**Scope:** Build-realization only. Authority: TL/Manager ACTION 2026-06-17 ("Begin V3 Build Open Slots"). Does not authorize a model run.

---

## Allocation strategy: per-item prefix + role suffix

The token pool is **constructive, not enumerated.** Rather than maintaining a finite list of tokens, the generator allocates per-item:

```text
prefix(N) = "i{N:03d}_"     # e.g. "i007_"

# Within item N, every role takes a role-suffix appended to the prefix:
roles for the target chain:
    A             → "{prefix}A"
    B             → "{prefix}B1"   # B-with-index-1 (target bridge)
    C_star        → "{prefix}C1"   # C-with-index-1 (target answer)
    T             → "{prefix}T0"   # target terminal (index-0 reserved)
    r1            → "{prefix}r1"
    r2            → "{prefix}r2"
    post_C_star_relations → ["{prefix}rX", "{prefix}rY"]

roles for the D=5 same-depth competitors (i = 1..D):
    head_relation_i      → "{prefix}s1"  | "{prefix}t1" | ... (fixed pool, see below)
    B_competitor_i       → "{prefix}B{i+1}"   # B2..B(D+1)
    second_relation_i    → "{prefix}s2"  | "{prefix}t2" | ...
    X_i                  → "{prefix}X{i+1}"   # X2..X(D+1)

roles for the k=5 decoy chains (j = 1..k):
    head_j               → "{prefix}P{j}"
    bridge_j             → "{prefix}Q{j}"
    answer_j             → "{prefix}S{j}"
    T_i_j                → "{prefix}Ti{j}"
```

The competitor relation pool is the fixed list at `v3_item_generator.py:_COMPETITOR_RELATION_PAIRS`:

```text
("s1", "s2"), ("t1", "t2"), ("u1", "u2"), ("v1", "v2"), ("w1", "w2")
```

These 5 pairs cover D = 5 competitors. All 10 strings are disjoint from `r1` and `r2` (C4 requirement).

## Per-item independence

This scheme guarantees the following invariants by construction, for any item count up to and beyond n = 96:

```text
1. C2 pairwise-distinct: every role within an item gets a distinct string
   (target A/B/C*/T are distinct; B_competitors and X_i indices start at 2
   so they cannot collide with target B/C* at index 1; decoy chain entities
   use distinct role letters P/Q/S/Ti). Inspector C2 PASS by construction.

2. Cross-item independence: tokens from item N (prefix "i{N:03d}_") cannot
   alias tokens from item M (prefix "i{M:03d}_") for N ≠ M, regardless of
   role. There is no item-to-item token bleed by construction.

3. C3 categories-separable: C_star ("{prefix}C1") is structurally distinct
   from any X_i ("{prefix}X{i+1}", i+1 ≥ 2); B ("{prefix}B1") is distinct
   from any B_competitor_i ("{prefix}B{i+1}", i+1 ≥ 2); X_i and decoy T_j
   live in disjoint suffix namespaces. Inspector C3 PASS by construction.

4. C4 r1-edge uniqueness: r1 = "{prefix}r1" is fixed; competitor head
   relations are drawn from the {s1, t1, u1, v1, w1} pool — all disjoint
   from "r1" and pairwise distinct. Inspector C4 PASS by construction.
```

The conformance batch (8 items, every check PASS, see `conformance_summary.json`) is the empirical demonstration these construction-time invariants hold under the actual inspector.

## What this pool does NOT do

```text
- Does NOT tokenize against any model's vocabulary. The strings are
  schema-level role symbols, not tokenizer IDs. A downstream prompt-
  realization layer (gated on Manager by-name authorization) would
  embed these into natural-language prompt templates; the actual model
  tokenization happens at run time.
- Does NOT enforce per-item entropy or non-overlap of *meaning* — only
  of *strings*. The strings are deliberately synthetic placeholders
  ("tokA"-style) consistent with the existing inspector fixtures
  (01-09); a model receiving these as raw strings would not infer
  semantic associations between items, which is exactly the property
  the foreclose-all standard relies on.
- Does NOT exhaust a finite pool. The constructive scheme scales with
  item count; no finite token registry needs maintenance.
```

— CS Engineer, 2026-06-17
