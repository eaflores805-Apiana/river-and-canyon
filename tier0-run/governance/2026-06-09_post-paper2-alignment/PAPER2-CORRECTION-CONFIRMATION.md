# Paper 2 Correction Confirmation

**Filed:** 2026-06-09  
**Prepared by:** CS Engineer  
**Status:** FINAL — responds to Team Lead memo §3  
**Purpose:** Confirm whether Senior's two clarity corrections resolve the CS-flagged Paper 2 issues.

---

## Correction 1 — Cell02 label

**Senior's correction as reported in Team Lead memo:**
> "The paper now states ct is at pos6, cd2 occupies pos7, and the historical 'ct-last' label is a misnomer."

**CS confirmation: RESOLVED.**

The factual error was: Paper 2 described Cell02 as "all-ct-last" or "all-C_target-last," implying ct is the last C-type object in context. The artifact shows ct at pos6, cd2 at pos7 — ct is second-to-last among C-type objects, not last.

Senior's wording resolves this correctly. The corrected framing:
- States the actual positions (ct at pos6, cd2 at pos7) ✓
- Acknowledges the historical label is a misnomer ✓
- Does not require any change to the numeric results ✓

No remaining issue on this correction.

---

## Correction 2 — §4.5 "(3, 11, 6)" hop1-only scope

**Senior's correction as reported in Team Lead memo:**
> "The paper now states that (3, 11, 6) are hop1-only counts."

**CS confirmation: RESOLVED.**

The ambiguity was: the triple appeared without explicit scope, allowing a reader to interpret it as applying across query types. Adding "hop1-only" removes the ambiguity.

**For completeness, hop1 failure breakdown for Cell03 (from locked artifact):**

| Failure class | Count |
|---|---|
| target_chain_wrong_neighbor | 6 |
| non_context_return | 7 |
| UNCLASSIFIED_OFF_FRAME | 4 |
| wrong_chain_selection | 1 |
| **Total failures** | **18** |
| correct | 6 |
| **Total** | **24** |

CS cannot independently confirm whether "(3, 11, 6)" specifically matches the paper's described breakdown without seeing the final §4.5 text. The triple (3, 11, 6) does not directly correspond to the four failure classes above. If the triple refers to a different grouping (e.g., grouped by item-group A/B/C, or a different sub-classification), Senior should verify the referent against the artifact table above. If the triple refers to a different subset, please route back for CS verification.

**If "(3, 11, 6)" = (wrong_chain_selection + correct_chain_stopped_short in Cell01, or another breakdown):** CS needs the specific grouping to confirm. The addition of "hop1-only" resolves the scope ambiguity; the specific values must be checked against the table above.

---

## Summary

| Correction | Status | Remaining action |
|---|---|---|
| Cell02 "ct-last" label | **RESOLVED** | None |
| §4.5 "(3, 11, 6)" hop1-only | **SCOPE RESOLVED — values to verify** | Senior to confirm triple maps to artifact counts above |

If "(3, 11, 6)" value-checks out against the Cell03 hop1 artifact, both corrections are fully resolved and CS has no remaining hold on Paper 2 framing.

---

— CS Engineer, 2026-06-09
