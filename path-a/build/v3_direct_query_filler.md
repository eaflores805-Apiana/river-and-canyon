# V3 Direct-Query Filler — open-slot realization (3 of 5)

**Date:** 2026-06-17
**Author:** CS Engineer
**Scope:** Build-realization only. Authority: TL/Manager ACTION 2026-06-17 ("Begin V3 Build Open Slots"). Does not authorize a model run.

---

## What this slot realizes

Per `PREREGISTRATION-PATH-A-CONSTRUCTIBILITY-v0.3` §5 (and §"Open slots") and design v0.3 §5 (E5):

> *"The direct-query context withholds the linking fact and asks the composite. The withheld fact is replaced by **neutral, length-matched filler that contains neither B nor C\*** (E5), so the context length/structure matches the composite while providing no traversal path and no exposure of B or C\*."*

The inspector enforces this at C7 by requiring three fields on `spec.direct_query`:

```text
withhold_fact_role            == "B_to_C_star"  (or "A_to_B")
filler_form                   non-empty template string
filler_contains_B_or_C_star   explicitly false
```

## The realization

Five filler templates rotate per item by seed (`seed mod 5`), implemented at `v3_item_generator.py:_FILLER_FORMS` and `_make_direct_query()`:

```text
"{W} holds {V}"
"{W} marks {V}"
"{W} types {V}"
"{W} pairs {V}"
"{W} links {V}"
```

Each template has the same structure: `{W} <5-letter verb> {V}`. The five verbs all have exactly 5 letters; the bracketing whitespace pattern is identical; the only variation across templates is the verb itself. This satisfies the **length-matching** clause: when `{W}` and `{V}` are replaced by neutral tokens (drawn from a pool disjoint from the per-item role namespace), the resulting filler string is character-for-character the same length as the withheld fact `B —r2→ C*` would have been in the same prompt template, modulo identical placeholder substitution.

The **contains-neither-B-nor-C\*** clause is enforced two ways:

```text
1. Schema-level (declared in every item spec):
     direct_query.filler_contains_B_or_C_star == false
   Inspector C7 fail-closes on any other value.

2. Construction-level (the substitution rule, gated downstream):
   The placeholders {W} and {V} are filled at prompt-realization time
   (downstream of this build, gated on Manager by-name authorization)
   with tokens drawn from a pool DISJOINT from the per-item role
   namespace (i.e., disjoint from {"{prefix}B1", "{prefix}C1", ...}).
   Because the per-item prefix is `i{N:03d}_` and the neutral pool is
   prefix-free, set-membership disjointness is mechanical.
```

The schema-level declaration is what the inspector verifies at build time; the construction-level guarantee is what prompt-realization must preserve when this build is actually consumed by a run. Both are necessary; only the first is in this build's scope.

## Rotation logic — why per-seed

Rotating filler form per seed (rather than holding it constant across all items) reduces a potential constant-token-across-queries signal (R6e in scoring; cross-query constant-token invalidator in design v0.3 §7). If every item used the same filler verb, the verb itself becomes a constant token a model could key on across the analysis unit; rotating it across 5 forms × 96 items distributes the verb evenly without changing length or structure.

The rotation is **deterministic** by seed: `filler_form(N) = _FILLER_FORMS[N mod 5]`. So item N = 1 uses "marks", N = 2 uses "types", N = 3 uses "pairs", N = 4 uses "links", N = 5 uses "holds", and the cycle repeats. (Index 0 of the array is "holds", which seed mod 5 == 0 selects; seed = 5 → "holds", seed = 1 → "marks", etc.)

## What this slot does NOT do

```text
- Does NOT fill the {W} / {V} placeholders with concrete neutral tokens.
  Substitution is a prompt-realization concern downstream of Manager by-
  name authorization. This build declares the form; downstream realization
  binds the values under the disjointness guarantee.
- Does NOT enumerate the full neutral token pool. The pool exists in
  prompt-realization code (not in this build); the substitution rule is
  what matters at this layer.
- Does NOT authorize the direct-query context to be presented to a model.
  Presentation requires the full four-context prompt-realization layer
  and Manager by-name run authorization, neither of which is in scope.
```

— CS Engineer, 2026-06-17
