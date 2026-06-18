# V3 Relation Balance — open-slot realization (4 of 5)

**Date:** 2026-06-17
**Author:** CS Engineer
**Scope:** Build-realization only. Authority: TL/Manager ACTION 2026-06-17 ("Begin V3 Build Open Slots"). Does not authorize a model run.

---

## What this slot realizes

Design v0.3 §2 (E8 — binding admissibility property):

> *"Relation **frequency, order, and position** must be balanced across the target and competitor paths, so that **r1/r2 cannot be selected by salience alone**. No relation on the queried path may be made more frequent, earlier-ordered, or more positionally prominent than the competitor relations. This is what bounds the relation-identity route (route 4, §8) at the structural-depth floor 1/D rather than letting a relation-salience signal break the floor."*

Inspector C6 enforces this at the schema level (`inspector.py:check_C6_relation_balance`):

```text
1. frequency balance: every queried + competitor relation appears the same
   number of times in spec.relation_balance.frequency.
2. role-grouped order: every "head" relation (r1 + competitor head_relation_i)
   appears at the same set of path-positions; same for "tail" relations
   (r2 + competitor second_relation_i). Heads vs tails may differ — heads
   at slot 0 of their path, tails at slot 1.
```

## The realization

Implemented at `v3_item_generator.py:_make_relation_balance()`:

```text
head_relations = [prefix + "r1", prefix + "s1", prefix + "t1", prefix + "u1",
                  prefix + "v1", prefix + "w1"]      # 1 + D = 6 head relations

tail_relations = [prefix + "r2", prefix + "s2", prefix + "t2", prefix + "u2",
                  prefix + "v2", prefix + "w2"]      # 1 + D = 6 tail relations

frequency       = { r: 1 for r in head_relations ∪ tail_relations }
order_positions = { r: [0] for r in head_relations }
                | { r: [1] for r in tail_relations }
```

Every relation has frequency exactly **1**. The target relation r1 has the same frequency as each competitor head_relation; r2 has the same frequency as each competitor second_relation; head class is held at the same frequency as tail class. C6's frequency clause is satisfied by uniform-1 frequencies across all 12 relations.

Every head relation appears at position `[0]` and every tail relation appears at position `[1]`. The set of distinct position-tuples for heads is `{[0]}` (one element); same for tails (`{[1]}`). C6's role-grouped order clause is satisfied because all heads share their position-set and all tails share theirs.

## Why frequency 1 (not higher)

The schema records "presentation frequency" — how many distinct edge facts of each relation appear in the constructed layout. Each fact appears once (because the construction is a single chain plus D = 5 competitor branches plus k = 5 decoy chains, with one edge per role per path). The salience signal the standard worries about is "is r1 more frequent than s1/t1/u1/v1/w1 across the item layout?" — and the answer is no: each appears exactly once.

If a downstream prompt-realization layer were to re-introduce frequency imbalance (e.g., by repeating r1 in instructions), C6 would no longer be the protection layer; that imbalance would have to be controlled at the prompt-template level. The schema-level balance C6 enforces is necessary but not sufficient for total presentation balance, and the build artifacts here record only the schema-level guarantee.

## Why position-0 vs position-1 (and why that's still balanced)

A relation's path-position is "first edge of a path" (head, position 0) or "second edge" (tail, position 1). r1 is structurally a head relation (A → B); r2 is structurally a tail relation (B → C\*). Competitor head_relation_i is the first edge of competitor path i (A → B_competitor_i); competitor second_relation_i is the second edge (B_competitor_i → X_i).

The role-grouped position check is *not* "every relation at the same position" — heads and tails would then have to merge. It is "every head at the same position-set; every tail at the same position-set." That permits the schema's natural position assignment (heads at 0, tails at 1) while still forbidding the salience signal: a model cannot key on "r1 is earlier than s1" because they are both at position 0, nor on "r2 is later than s2" because they are both at position 1.

## How this prevents the relation-identity route from breaking the floor

The floor F = max(1/p, 1/m, 1/D) = max(0.20, 0.10, 0.20) = 0.20 prices the strongest *single* non-traversal route. The relation-identity route — "key on which relation token names r1/r2 vs s1/s2 etc." — is bounded by 1/D = 0.20 *only* if there is no salience signal that lets the model tell r1/r2 apart from competitor relations without following them. C6 forecloses three salience sources at the schema level:

```text
- frequency salience: same count for r1 as for s1/t1/u1/v1/w1.
- order salience: r1 and competitor head_relations all at position 0.
- position salience: r2 and competitor second_relations all at position 1.
```

With those three salience sources zeroed at the schema layer, the strongest single relation-identity heuristic still scores at 1/D (random pick among the D competitor heads, plus the target head, conditioned on "head position"). That keeps the route at the floor, not above it.

If C6 reported PASS but the prompt-realization layer reintroduced salience (e.g., by mentioning r1 in instructions), that would be a downstream realization defect, not a schema defect. The build artifacts here record the schema-level guarantee.

## What this slot does NOT do

```text
- Does NOT enforce salience balance at the prompt-template layer.
  That is downstream of this build and gated on Manager by-name
  authorization.
- Does NOT extend balance to anything outside the queried + competitor
  relation set (e.g., decoy chain relations are not balanced against r1/r2,
  because they are not on the queried path and so cannot select C* via
  relation-identity at the queried position).
- Does NOT pre-register the floor 1/D = 0.20 — that is locked in
  constants.py / prereg v0.4 / definition v0.4 §"derived heuristic floor";
  this slot only realizes the protection that *makes* 1/D the binding
  term for the relation-identity route.
```

— CS Engineer, 2026-06-17
