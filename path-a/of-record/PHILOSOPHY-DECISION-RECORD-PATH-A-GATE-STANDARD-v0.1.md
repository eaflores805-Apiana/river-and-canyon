# PHILOSOPHY DECISION RECORD — Path A Gate Standard v0.1

**E. A. Flores**, Apiana AI, Inc. — June 16, 2026
*River and Canyon · Path A. Drafted by the Senior Engineer for Manager / Team Lead ratification. A decision artifact only — it authorizes nothing.*

## 0. What this record is

This records a **decision the Manager is making**, not a conclusion an analysis reached. It commits the *standard* the Path A composition gate must meet, records the alternative that was considered and rejected, and names the construction that conforms to the chosen standard. It is a **philosophy choice**, not an empirical finding — the analysis (taxonomy v0.2, `5bdc1ffa…`) informed it but did not prove it, and this record does not claim otherwise. It authorizes no build, run, or downstream action (§5).

## 1. The decision

```text
The Manager commits to FORECLOSE-ALL as the gate standard for Path A.
```

**Rationale (a judgment, stated as such):** *a composition gate is only valid if only traversal can select the answer.* If any non-traversal route — depth, layout position, token salience, relation identity, direct recall, a chain tag, or a topic match — can select the correct answer at a non-trivial rate, then a passing score no longer evidences two-hop composition; it evidences the shortcut. The gate's entire purpose is to measure composition, so the standard it must meet is that **every non-traversal route is foreclosed** (scores at or below a derived floor), leaving traversal as the only path to a passing answer.

This is a commitment about what the gate must *be*, chosen on judgment. It is not an output of the property matrix — the matrix showed which constructions *conform* to this standard *if it is chosen*; it could not, and did not, establish that the standard is correct. That choice is the Manager's, and it is made here.

## 2. The alternative considered and rejected

```text
CONSIDERED:  make-identity-easy  (explicit chain tags / semantically-distinct chains / grouped topology)
REJECTED.
```

**Reason for rejection (philosophy, not data):** the make-identity-easy approach lowers the chain-identity burden by **adding a non-traversal route to answer selection** — the model can separate chains by matching a tag or a topic instead of by traversing. That may make the task easier and the off-map number lower, but it does so by **weakening the very construct the gate is supposed to measure**: a score under that approach is satisfiable by tag/topic-matching, so it no longer isolates composition. Lowering the difficulty by changing what is being measured is not a gate improvement; it is a different, weaker measurement. This is rejected on the standard in §1, not on any experimental result.

(For the record: this rejection is a *standard* judgment. It does not assert that a model *would* use a tag/topic shortcut — only that the approach *offers* one, which the foreclose-all standard forecloses by construction regardless of whether any given model exploits it.)

## 3. V3 status — the candidate vehicle, not a certified result

```text
V3 (the same-depth-competitor construction) is the CURRENT CANDIDATE VEHICLE that CONFORMS
to the foreclose-all standard. V3 is NOT certified.
```

V3 is named here because the byte-audit (SE return `c3f4e667…`) verified that its instrument defines all seven foreclose-all properties and that its admissibility gate enforces them fail-closed, and because its corrected binding is now re-locked of-record (prereg v0.4, `c61a3256…`). That makes V3 the construction that *conforms to the chosen standard* — the vehicle to build toward. It does **not** make V3 a working gate.

**Committing to foreclose-all + V3 does not commit the result:**

```text
- The floor check remains the EMPIRICAL question: does hop2 clear its floor under competition on V3?
- V3 MAY STILL FAIL. Conformance to the standard is not evidence that the substrate can meet it.
- IF V3 FAILS, substrate-infeasibility remains a VALID OUTCOME — a real finding (the gate is honest,
  complete, and unmet on this substrate), never a license to loosen the standard committed in §1.
```

This record commits a standard and a vehicle and a route. It does not predict that the route ends in a certified baseline.

## 4. Route consequence

The commitment establishes this route. Each step gates the next; none is skippable; this record enacts none of them.

```text
foreclose-all commitment          (this record, on ratification)
  -> V3 as candidate vehicle       (conforms to the standard; binding re-locked v0.4)
  -> build open slots              (item generator + seed, token pool, direct-query filler,
                                    relation-balancing realization — CS; Manager/TL approve the effort)
  -> floor-check prereg            (does hop2 clear floor under competition on V3? — SE drafts ->
                                    CS feasibility -> C5 claim-risk -> TL approve)
  -> Manager by-name authorization (the run gate)
  -> CS run                        (execute under lock-before-look)
  -> SE verification               (recompute from bytes; read the verdict; substrate-infeasibility
                                    is a valid verdict)
```

## 5. Boundaries

```text
This decision record does NOT authorize: build · item generation · prompt generation · model run ·
compression · Claim C · Paper B · capability claim · mechanism claim.
It is a decision artifact only; it commits a standard, records a rejected alternative, names a
conforming candidate, and establishes a route. Each route step requires its own gate.
The Path A FP16 K=5 FAIL remains closed and untouched.
SE drafts this record; the Manager / Team Lead ratify it. SE ratifies nothing.
```

---

**The one to carry up:** The Manager commits to **foreclose-all** as the Path A gate standard — *a composition gate is valid only if only traversal can select the answer* — a philosophy choice made on judgment, not a conclusion the property matrix proved (the matrix showed conformance to the standard if chosen, not the standard's correctness). The **make-identity-easy** alternative (tags / distinct topics / grouping) is recorded as **considered-and-rejected**, because it adds a non-traversal route to answer selection and so weakens the construct the gate measures — a standard judgment, not an empirical result. **V3** is framed as the **current candidate vehicle that conforms** to foreclose-all (byte-audit-verified properties, binding re-locked v0.4) — **not certified**: committing to foreclose-all + V3 does **not** commit the result; the floor check remains the empirical question; V3 may still fail; and if it does, substrate-infeasibility is a valid outcome, never a license to loosen the standard. The route is foreclose-all → V3 candidate → build → floor-check prereg → Manager by-name authorization → CS run → SE verification, each step its own gate. This record authorizes no build, run, or downstream action; the FAIL stays closed; SE drafts, Manager/TL ratify.

— Senior Engineer (decision-record draft; routes to Manager / Team Lead for ratification)
