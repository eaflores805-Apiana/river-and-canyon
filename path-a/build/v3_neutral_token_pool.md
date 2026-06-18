# V3 Neutral-Token Pool — floor-check tooling artifact (4 of 4)

**Date:** 2026-06-18
**Author:** CS Engineer
**Authority:** Manager + TL ACTION 2026-06-18 ("File V3 Floor-Check Prereg v0.4 and Begin Tooling Build"), Step 2. **Build effort only.**
**Status:** Lockable resource. Lock-at-approval per v0.4 §T.

---

## 0. What this resource is

The explicit, auditable pool of **neutral connective/template material** the prompt realizer (`v3_prompt_realizer.py`) uses to render schema-level item specs into concrete four-context prompts. It is **distinct from** the construction's role-token pool (`v3_token_pool.md`, sha `d5f3594c…`) and **distinct from** the direct-query filler verb templates (`v3_direct_query_filler.md`, sha `7ff83ab8…`). It supplies *fill content* that the realizer drops into structural positions; it does **not** define construction roles, relations, decoy chains, or any V3 schema element.

The realizer is a pure function of `(item_spec, this_pool)`; given the same spec and the same pool, the realizer's output is byte-identical.

## 1. Pool design constraint — character-width parity with per-item role tokens

The V3 item generator (`v3_item_generator.py`, sha `6a2ceee1…`) emits per-item role tokens with a fixed 7-character prefix `i{NNN}_` followed by a role suffix `A` / `B1` / `C1` / `r2` / etc. The full role tokens are therefore **6 or 7 characters** in width: `i007_A` (6), `i007_B1` (7), `i007_C1` (7), `i007_r1` (7), `i007_r2` (7).

To meet the v0.4 §4 / F1 constraint **MAX_DELTA = 8 characters per item-set** across the four-context prompts, the dominant length contribution — the direct-query filler substitution of the bridge fact `(B, r2, C*)` — must produce a triple of **comparable character width** to the original bridge fact. The pool tokens are sized accordingly.

```text
Bridge-fact triple length (example, item 007):
  "(i007_B1, i007_r2, i007_C1)"
  = 1 + 7 + 2 + 7 + 2 + 7 + 1  = 27 characters

Filler triple length (with 7-char neutral W, V):
  "({W}, holds, {V})"
  = 1 + 7 + 2 + 5 + 2 + 7 + 1  = 25 characters

Width delta on the substituted line:  27 - 25 = 2 characters.
Query-text delta across contexts:     ≤ 3 characters (the ".r2" vs single relation).
Total max delta per item-set:         ≤ 5 characters, comfortably under MAX_DELTA = 8.
```

(All 5 filler verbs from `v3_direct_query_filler.md` are exactly 5 characters: `holds`, `marks`, `types`, `pairs`, `links`. Width parity is enforced by the filler-form spec.)

## 2. The neutral-token pool (locked content)

```text
NEUTRAL_W_TOKENS = [
    "neutral",   # 7 chars
    "placebo",   # 7 chars
    "abstain",   # 7 chars
    "padding",   # 7 chars
    "default",   # 7 chars
    "fillerX",   # 7 chars
    "blankXY",   # 7 chars
    "ineutrl",   # 7 chars
]

NEUTRAL_V_TOKENS = [
    "placebo",   # 7 chars
    "abstain",   # 7 chars
    "padding",   # 7 chars
    "default",   # 7 chars
    "fillerX",   # 7 chars
    "blankXY",   # 7 chars
    "ineutrl",   # 7 chars
    "neutral",   # 7 chars
]
```

**All 8 entries are 7 characters wide** by construction. The two arrays are rotations of the same content so that `(W, V)` pairs are never identical-token within a sentence (W != V is enforceable in the realizer if needed).

## 3. Disjointness from construction role-token namespace

Every neutral token in §2 is **disjoint** from the per-item role-token namespace because the role-token namespace is exhaustively the set `{i{NNN}_X | NNN ∈ 001..999, X ∈ {A, B1..B6, C1, T0, Ti1..Ti5, P1..P5, Q1..Q5, S1..S5, X2..X6, r1, r2, rX, rY, s1, s2, t1, t2, u1, u2, v1, v2, w1, w2}}` — every member of which starts with the literal three characters `i`, `0|1|2|3|4|5|6|7|8|9`, `0|1|2|3|4|5|6|7|8|9`, `_`. No entry in §2 starts with `i` followed by a digit followed by a digit followed by `_`, so the disjointness is mechanical.

```text
Disjointness check (mechanical):
  for w in NEUTRAL_W_TOKENS ∪ NEUTRAL_V_TOKENS:
      assert not re.match(r"^i\d\d\d_", w)
  → passes by inspection on the 8 unique entries above.
```

This satisfies the v0.3 §5 / E5 binding admissibility property that the direct-query filler "contains neither B nor C*" — the filler substitution can never coincidentally produce a role-token string.

## 4. Selection rule (realizer reads this)

For item `N`, the realizer selects `(W, V)` deterministically:

```text
W_index = (N - 1) mod len(NEUTRAL_W_TOKENS)
V_index = N mod len(NEUTRAL_V_TOKENS)         # off-by-one rotation so W != V
W = NEUTRAL_W_TOKENS[W_index]
V = NEUTRAL_V_TOKENS[V_index]
```

The rotation guarantees `W != V` for every `N` (proof: when `(N-1) mod 8` would equal `N mod 8`, that requires `(N-1) ≡ N (mod 8)`, which is false). The selection is byte-identical for the same `N`.

## 5. What this pool does NOT do

```text
- Does NOT define construction roles, relations, decoy chains, or any V3 schema element.
- Does NOT enforce per-token semantic neutrality — the strings are character-width-matched
  placeholders; semantic neutrality is an audit property of the chosen lexemes.
- Does NOT authorize execution. The pool is data the realizer reads; it does not
  authorize a run.
- Does NOT pre-materialize prompts. The realizer + this pool together produce prompts
  only when invoked.
```

## 6. Lockability + embedding option (per v0.4 §T)

```text
default mode    separate file (this file).
                Locked digest = sha256(this file's bytes).
                The realizer's behavior depends on (spec, this_pool), so both files'
                digests must be locked at approval.

alternative     if Manager/TL prefer the pool embedded in the realizer as constants:
                the realizer digest then binds the pool, and NO separate file digest
                is locked. This file would then be retained as an audit document only,
                or removed (TL choice). Default here is "separate file" per the v0.4 §T.
```

This file's lockable sha256 is what gets bound at TL approval, alongside the analyzer/realizer/checker shas, into the v0.4 §16-style binding block.

---

— CS Engineer, 2026-06-18
