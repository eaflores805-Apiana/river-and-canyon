"""
Matched task pairs for Tier 0. THIS IS THE REAL WORK — and it's yours.

The scaffold runs whatever is here. The quality of the result depends entirely
on whether these pairs are genuinely matched. Two worked examples are provided
to show the discipline; replace and expand to ~20-40 pairs.

THE MATCHING RULES (from the protocol — every pair must satisfy all):
  1. Split by PRECISION DEMAND, not apparent difficulty. The "narrow" arm is the
     one where a small deviation flips correctness (exact ordering, binding,
     arithmetic, strict format). The "broad" arm tolerates many valid outputs.
  2. Comparable SCORING STRICTNESS. Don't score broad with a tolerant judge and
     narrow with exact-match — that manufactures the gap. Both use structured,
     checkable scoring (exact or strict checklist).
  3. Matched CONTEXT-DEPTH. Evidence sits at comparable positions in both prompts.
  4. Matched GENERATION LENGTH and STATE-LOAD. The broad arm must place comparable
     load on the residual stream — otherwise activation-outlier blowout on the
     longer/heavier arm masquerades as a precision effect.

COUNTEREXAMPLE (optional per pair, but it's what catches robust-wrong):
  An item where the obvious shortcut gives the WRONG answer. If the model gives
  the shortcut answer and keeps giving it under quantization, that's robust-wrong.
"""

PAIRS = [

    # ---- Worked example 1: temporal ordering (same source text both arms) ----
    {
        "id": "P01",
        "source_note": "both arms use the same short event passage; only precision demand differs",
        "narrow": {
            # precision-demanding: exact ordering + state binding, one slip flips it
            "prompt": (
                "Passage: At 9am Maria opened the shop. At 10am she received a delivery. "
                "At 11am, before lunch, she restocked the shelves using the delivery. "
                "After lunch at 1pm she did inventory.\n\n"
                "Question: Did the restocking happen before or after the delivery arrived, "
                "and what did she use to restock? Answer in the form: '<before/after>, <item>'."
            ),
            "score_type": "exact",
            "answer": "after, delivery",
        },
        "broad": {
            # robustness-tolerant: many valid phrasings, graceful, SAME passage length
            "prompt": (
                "Passage: At 9am Maria opened the shop. At 10am she received a delivery. "
                "At 11am, before lunch, she restocked the shelves using the delivery. "
                "After lunch at 1pm she did inventory.\n\n"
                "Question: List the three main things Maria did during the day "
                "(any reasonable wording)."
            ),
            "score_type": "checklist",
            "required_facts": ["open", "deliver", "restock"],  # 'inventory' optional 4th
        },
        "counterexample": {
            # shortcut = assume chronological mention order = causal order; here the
            # 'before lunch' clause makes naive order-reading give the wrong answer
            "prompt": (
                "Passage: At 9am Maria opened the shop. At 10am she received a delivery. "
                "At 11am, before lunch, she restocked the shelves using the delivery. "
                "After lunch at 1pm she did inventory.\n\n"
                "Question: Did she do inventory before or after restocking? "
                "Answer 'before' or 'after'."
            ),
            "score_type": "exact",
            "answer": "after",  # inventory at 1pm is AFTER restock at 11am
        },
    },

    # ---- Worked example 2: multi-step arithmetic vs. explanation (matched length) ----
    {
        "id": "P02",
        "source_note": "narrow = exact carry chain; broad = explain the concept; lengths matched",
        "narrow": {
            "prompt": (
                "Compute step by step and give only the final number: "
                "(47 * 8) + (136 - 89) - (12 * 3). End with 'ANSWER: <number>'."
            ),
            "score_type": "exact",
            "answer": "ANSWER: 387",  # 376 + 47 - 36 = 387
        },
        "broad": {
            "prompt": (
                "Explain, in a few sentences, the order of operations you would use to "
                "evaluate an expression like (a*b)+(c-d)-(e*f). Mention which operations "
                "come first and why."
            ),
            "score_type": "checklist",
            "required_facts": ["multipl", "before", "left"],  # multiplication before +/-, left-to-right
        },
        "counterexample": {
            # shortcut = left-to-right without precedence; gives wrong answer
            "prompt": (
                "Evaluate giving only the final number: 2 + 3 * 4. "
                "End with 'ANSWER: <number>'."
            ),
            "score_type": "exact",
            "answer": "ANSWER: 14",  # shortcut (2+3)*4=20 is the robust-wrong trap
        },
    },

    # ---- ADD ~18-38 MORE PAIRS HERE ----
    # Domains the protocol suggests: code with edge cases, multi-hop lookup,
    # state-tracking, tool/permission boundaries, logic with surface-similarity traps.
    # For each: matched length + state-load, symmetric scoring, one counterexample.

]
