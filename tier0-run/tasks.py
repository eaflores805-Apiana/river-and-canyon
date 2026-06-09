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

    # ==========================================================================
    # SMOKE SWEEP PAIRS (Tier 0A / Tier 0B calibration)
    # All passed 7B at FP16/INT8/INT4. Too easy for 7B fragility signal.
    # Kept for instrument health checks and negative controls.
    # ==========================================================================

    # ---- P01R: temporal ordering (simplified baseline) ----
    # Cell: compositional_low_support | chain_len: 2
    # NOTE: 7B fails narrow at FP16 (baseline seam failure, not compression).
    #       1.5B passes. Kept as diagnostic; excluded from ΔR (NaN).
    {
        "id": "P01R",
        "source_note": "simplified temporal comparison; baseline seam failure on 7B (capability floor, not compression)",
        "narrow": {
            "prompt": (
                "Use only the schedule below.\n\n"
                "Schedule:\n"
                "* Delivery happened at 10:00 AM.\n"
                "* Restocking happened at 11:00 AM.\n\n"
                "Question: Did restocking happen BEFORE or AFTER delivery? "
                "Also name the event it is compared against.\n\n"
                "Answer using exactly this format:\n"
                "ANSWER: <BEFORE or AFTER>, <event>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: AFTER, delivery",
        },
        "broad": {
            "prompt": (
                "Use only the schedule below.\n\n"
                "Schedule:\n"
                "* Delivery happened at 10:00 AM.\n"
                "* Restocking happened at 11:00 AM.\n\n"
                "Question: List the two events and their times.\n\n"
                "Answer using exactly this format:\n"
                "ANSWER: delivery = <time>; restocking = <time>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: delivery = 10:00 AM; restocking = 11:00 AM",
        },
        "component_checks": [
            {
                "hop": "delivery_time",
                "prompt": (
                    "Use only the schedule below.\n\n"
                    "Schedule:\n"
                    "* Delivery happened at 10:00 AM.\n"
                    "* Restocking happened at 11:00 AM.\n\n"
                    "Question: What time did delivery happen?\n\n"
                    "Answer using exactly this format:\n"
                    "ANSWER: <time>"
                ),
                "score_type": "exact",
                "answer": "ANSWER: 10:00 AM",
            },
            {
                "hop": "restocking_time",
                "prompt": (
                    "Use only the schedule below.\n\n"
                    "Schedule:\n"
                    "* Delivery happened at 10:00 AM.\n"
                    "* Restocking happened at 11:00 AM.\n\n"
                    "Question: What time did restocking happen?\n\n"
                    "Answer using exactly this format:\n"
                    "ANSWER: <time>"
                ),
                "score_type": "exact",
                "answer": "ANSWER: 11:00 AM",
            },
        ],
    },

    # ---- P02R: two-step arithmetic (small numbers, easier baseline) ----
    # Cell: compositional_low_support | chain_len: 2
    # NOTE: 7B passes all rungs. 1.5B shows seam failure at FP16 (components pass,
    #       composite fails). Too easy for 7B fragility signal.
    {
        "id": "P02R",
        "source_note": "two-step arithmetic; 7B stable; 1.5B shows FP16 seam failure (capability floor)",
        "narrow": {
            "prompt": (
                "Use only the numbers below.\n\n"
                "A box has 12 red parts.\n"
                "A second box has 8 blue parts.\n"
                "Each part needs 3 screws.\n\n"
                "Question: How many screws are needed for all parts?\n\n"
                "Answer using exactly this format:\n"
                "ANSWER: <number>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: 60",
        },
        "broad": {
            "prompt": (
                "Use only the numbers below.\n\n"
                "A box has 12 red parts.\n"
                "A second box has 8 blue parts.\n"
                "Each part needs 3 screws.\n\n"
                "Question: List the two part counts.\n\n"
                "Answer using exactly this format:\n"
                "ANSWER: red parts = <number>; blue parts = <number>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: red parts = 12; blue parts = 8",
        },
        "component_checks": [
            {
                "hop": "total_parts",
                "prompt": (
                    "Use only the numbers below.\n\n"
                    "A box has 12 red parts.\n"
                    "A second box has 8 blue parts.\n\n"
                    "Question: How many total parts are there?\n\n"
                    "Answer using exactly this format:\n"
                    "ANSWER: <number>"
                ),
                "score_type": "exact",
                "answer": "ANSWER: 20",
            },
            {
                "hop": "screws_per_part",
                "prompt": (
                    "Use only the numbers below.\n\n"
                    "Each part needs 3 screws.\n\n"
                    "Question: How many screws does each part need?\n\n"
                    "Answer using exactly this format:\n"
                    "ANSWER: <number>"
                ),
                "score_type": "exact",
                "answer": "ANSWER: 3",
            },
            {
                "hop": "multiply_20x3",
                "prompt": (
                    "Question: What is 20 × 3?\n\n"
                    "Answer using exactly this format:\n"
                    "ANSWER: <number>"
                ),
                "score_type": "exact",
                "answer": "ANSWER: 60",
            },
        ],
    },

    # ---- P03: key/vault/token 2-hop (synthetic closed-world) ----
    # Cell: compositional_low_support | chain_len: 2
    # NOTE: Both 7B and 1.5B stable at all rungs. Kept as negative control.
    {
        "id": "P03",
        "source_note": "key/vault/token 2-hop; both 7B and 1.5B stable — negative control",
        "narrow": {
            "prompt": (
                "Use only the facts below.\n\n"
                "Facts:\n"
                "* Nalo owns the red key.\n"
                "* The red key opens Vault 3.\n"
                "* Vault 3 contains the silver token.\n\n"
                "Question: Which token can Nalo access?\n\n"
                "Answer using exactly this format:\n"
                "ANSWER: <token>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: silver token",
        },
        "broad": {
            "prompt": (
                "Use only the facts below.\n\n"
                "Facts:\n"
                "* Nalo owns the red key.\n"
                "* The red key opens Vault 3.\n"
                "* Vault 3 contains the silver token.\n\n"
                "Question: List exactly two facts from the passage.\n\n"
                "Answer using exactly this format:\n"
                "ANSWER: 1) <fact>; 2) <fact>"
            ),
            "score_type": "checklist",
            "required_facts": ["nalo", "red key", "vault 3"],
        },
        "component_checks": [
            {
                "hop": "nalo_key",
                "prompt": (
                    "Use only the facts below.\n\n"
                    "Facts:\n"
                    "* Nalo owns the red key.\n"
                    "* The red key opens Vault 3.\n"
                    "* Vault 3 contains the silver token.\n\n"
                    "Question: Which key does Nalo own?\n\n"
                    "Answer using exactly this format:\n"
                    "ANSWER: <key>"
                ),
                "score_type": "exact",
                "answer": "ANSWER: red key",
            },
            {
                "hop": "key_vault",
                "prompt": (
                    "Use only the facts below.\n\n"
                    "Facts:\n"
                    "* Nalo owns the red key.\n"
                    "* The red key opens Vault 3.\n"
                    "* Vault 3 contains the silver token.\n\n"
                    "Question: Which vault does the red key open?\n\n"
                    "Answer using exactly this format:\n"
                    "ANSWER: <vault>"
                ),
                "score_type": "exact",
                "answer": "ANSWER: Vault 3",
            },
            {
                "hop": "vault_token",
                "prompt": (
                    "Use only the facts below.\n\n"
                    "Facts:\n"
                    "* Nalo owns the red key.\n"
                    "* The red key opens Vault 3.\n"
                    "* Vault 3 contains the silver token.\n\n"
                    "Question: What token does Vault 3 contain?\n\n"
                    "Answer using exactly this format:\n"
                    "ANSWER: <token>"
                ),
                "score_type": "exact",
                "answer": "ANSWER: silver token",
            },
        ],
    },

    # ---- P04: person/team/station/file 2-hop ----
    # Cell: compositional_low_support | chain_len: 2
    # NOTE: 7B stable. 1.5B fails station_file component at FP16 (component floor).
    {
        "id": "P04",
        "source_note": "person/team/station/file 2-hop; 7B stable; 1.5B shows component failure at station_file hop",
        "narrow": {
            "prompt": (
                "Use only the facts below.\n\n"
                "Facts:\n"
                "* Riven is assigned to Team Delta.\n"
                "* Team Delta reports to Station 8.\n"
                "* Station 8 stores the amber file.\n\n"
                "Question: Which file is associated with Riven?\n\n"
                "Answer using exactly this format:\n"
                "ANSWER: <file>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: amber file",
        },
        "broad": {
            "prompt": (
                "Use only the facts below.\n\n"
                "Facts:\n"
                "* Riven is assigned to Team Delta.\n"
                "* Team Delta reports to Station 8.\n"
                "* Station 8 stores the amber file.\n\n"
                "Question: List exactly two facts from the passage.\n\n"
                "Answer using exactly this format:\n"
                "ANSWER: 1) <fact>; 2) <fact>"
            ),
            "score_type": "checklist",
            "required_facts": ["riven", "team delta", "station 8"],
        },
        "component_checks": [
            {
                "hop": "person_team",
                "prompt": (
                    "Use only the facts below.\n\n"
                    "Facts:\n"
                    "* Riven is assigned to Team Delta.\n"
                    "* Team Delta reports to Station 8.\n"
                    "* Station 8 stores the amber file.\n\n"
                    "Question: Which team is Riven assigned to?\n\n"
                    "Answer using exactly this format:\n"
                    "ANSWER: <team>"
                ),
                "score_type": "exact",
                "answer": "ANSWER: Team Delta",
            },
            {
                "hop": "team_station",
                "prompt": (
                    "Use only the facts below.\n\n"
                    "Facts:\n"
                    "* Riven is assigned to Team Delta.\n"
                    "* Team Delta reports to Station 8.\n"
                    "* Station 8 stores the amber file.\n\n"
                    "Question: Which station does Team Delta report to?\n\n"
                    "Answer using exactly this format:\n"
                    "ANSWER: <station>"
                ),
                "score_type": "exact",
                "answer": "ANSWER: Station 8",
            },
            {
                "hop": "station_file",
                "prompt": (
                    "Use only the facts below.\n\n"
                    "Facts:\n"
                    "* Riven is assigned to Team Delta.\n"
                    "* Team Delta reports to Station 8.\n"
                    "* Station 8 stores the amber file.\n\n"
                    "Question: Which file does Station 8 store?\n\n"
                    "Answer using exactly this format:\n"
                    "ANSWER: <file>"
                ),
                "score_type": "exact",
                "answer": "ANSWER: amber file",
            },
        ],
    },

    # ---- P05: atomic clean control (negative control) ----
    # Cell: atomic_low_shortcut | chain_len: 1
    # NOTE: Stable at all rungs on both 7B and 1.5B. Instrument health check.
    {
        "id": "P05",
        "source_note": "atomic single-step lookup; negative control; stable on both 7B and 1.5B",
        "narrow": {
            "prompt": (
                "Closed-world facts:\n"
                "* Toma = blue.\n"
                "* Rika = green.\n"
                "* Lemu = orange.\n\n"
                "Question: What color is Rika?\n\n"
                "Answer using exactly this format:\n"
                "ANSWER: <color>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: green",
        },
        "broad": {
            "prompt": (
                "Closed-world facts:\n"
                "* Toma = blue.\n"
                "* Rika = green.\n"
                "* Lemu = orange.\n\n"
                "Question: What color is Toma?\n\n"
                "Answer using exactly this format:\n"
                "ANSWER: <color>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: blue",
        },
    },

    # ---- P06: atomic high-shortcut robust-wrong probe ----
    # Cell: atomic_high_shortcut | chain_len: 1
    # NOTE: 7B passes (resists label at all rungs).
    #       1.5B: stable-wrong on narrow, broad flips 0→1 at INT4.
    #       Shortcut causality NOT fully established (broad fails at FP16 on 1.5B).
    {
        "id": "P06",
        "source_note": "label-content mismatch; 7B passes; 1.5B stable-wrong; shortcut causality not confirmed",
        "narrow": {
            "prompt": (
                "Use only the facts below.\n\n"
                "Facts:\n"
                "* The box labeled SAFE contains the dangerous powder.\n"
                "* The box labeled DANGER contains the safe powder.\n\n"
                "Question: Which box contains the dangerous powder?\n\n"
                "Answer using exactly this format:\n"
                "ANSWER: <SAFE or DANGER>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: SAFE",
        },
        "broad": {
            "prompt": (
                "Use only the facts below.\n\n"
                "Facts:\n"
                "* The box labeled BLUE contains the dangerous powder.\n"
                "* The box labeled RED contains the safe powder.\n\n"
                "Question: Which box contains the dangerous powder?\n\n"
                "Answer using exactly this format:\n"
                "ANSWER: <BLUE or RED>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: BLUE",
        },
        "counterexample": {
            "prompt": (
                "Use only the facts below.\n\n"
                "Facts:\n"
                "* The box labeled SAFE contains the dangerous powder.\n"
                "* The box labeled DANGER contains the safe powder.\n\n"
                "Question: Which box contains the dangerous powder?\n\n"
                "Answer using exactly this format:\n"
                "ANSWER: <SAFE or DANGER>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: SAFE",
        },
    },


    # ==========================================================================
    # CALIBRATION LADDER — 7B target pairs
    # Design goal: 7B passes at FP16, degrades at INT4.
    # Run --bits 16 first to confirm baseline before full sweep.
    #
    # LB1-LB4: 4-hop chains, no distractors
    # LC1-LC4: 4-hop chains, one distractor chain
    # LD1-LD4: 5-hop chains, distractor + added complexity
    # ==========================================================================

    # ---- LB1: 4-hop, no distractor ----
    # person → key → vault → token → gate
    {
        "id": "LB1",
        "source_note": "4-hop chain, no distractor; extends P03 by one step",
        "narrow": {
            "prompt": (
                "Use only the facts below.\n\n"
                "Facts:\n"
                "* Nalo owns the red key.\n"
                "* The red key opens Vault 3.\n"
                "* Vault 3 contains the silver token.\n"
                "* The silver token activates Gate B.\n\n"
                "Question: Which gate can Nalo activate?\n\n"
                "Answer using exactly this format:\n"
                "ANSWER: <gate>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: Gate B",
        },
        "broad": {
            "prompt": (
                "Use only the facts below.\n\n"
                "Facts:\n"
                "* Nalo owns the red key.\n"
                "* The red key opens Vault 3.\n"
                "* Vault 3 contains the silver token.\n"
                "* The silver token activates Gate B.\n\n"
                "Question: List exactly two facts from the passage.\n\n"
                "Answer using exactly this format:\n"
                "ANSWER: 1) <fact>; 2) <fact>"
            ),
            "score_type": "checklist",
            "required_facts": ["nalo", "red key", "gate b"],
        },
        "component_checks": [
            {
                "hop": "nalo_key",
                "prompt": (
                    "Use only the facts below.\n\n"
                    "Facts:\n"
                    "* Nalo owns the red key.\n"
                    "* The red key opens Vault 3.\n"
                    "* Vault 3 contains the silver token.\n"
                    "* The silver token activates Gate B.\n\n"
                    "Question: Which key does Nalo own?\n\n"
                    "Answer using exactly this format:\n"
                    "ANSWER: <key>"
                ),
                "score_type": "exact",
                "answer": "ANSWER: red key",
            },
            {
                "hop": "key_vault",
                "prompt": (
                    "Use only the facts below.\n\n"
                    "Facts:\n"
                    "* Nalo owns the red key.\n"
                    "* The red key opens Vault 3.\n"
                    "* Vault 3 contains the silver token.\n"
                    "* The silver token activates Gate B.\n\n"
                    "Question: Which vault does the red key open?\n\n"
                    "Answer using exactly this format:\n"
                    "ANSWER: <vault>"
                ),
                "score_type": "exact",
                "answer": "ANSWER: Vault 3",
            },
            {
                "hop": "vault_token",
                "prompt": (
                    "Use only the facts below.\n\n"
                    "Facts:\n"
                    "* Nalo owns the red key.\n"
                    "* The red key opens Vault 3.\n"
                    "* Vault 3 contains the silver token.\n"
                    "* The silver token activates Gate B.\n\n"
                    "Question: What does Vault 3 contain?\n\n"
                    "Answer using exactly this format:\n"
                    "ANSWER: <token>"
                ),
                "score_type": "exact",
                "answer": "ANSWER: silver token",
            },
            {
                "hop": "token_gate",
                "prompt": (
                    "Use only the facts below.\n\n"
                    "Facts:\n"
                    "* Nalo owns the red key.\n"
                    "* The red key opens Vault 3.\n"
                    "* Vault 3 contains the silver token.\n"
                    "* The silver token activates Gate B.\n\n"
                    "Question: Which gate does the silver token activate?\n\n"
                    "Answer using exactly this format:\n"
                    "ANSWER: <gate>"
                ),
                "score_type": "exact",
                "answer": "ANSWER: Gate B",
            },
        ],
    },

    # ---- LB2: 4-hop, no distractor ----
    # person → badge → sector → file → code
    {
        "id": "LB2",
        "source_note": "4-hop chain, no distractor; different domain from LB1",
        "narrow": {
            "prompt": (
                "Use only the facts below.\n\n"
                "Facts:\n"
                "* Soren holds the green badge.\n"
                "* The green badge grants entry to Sector 4.\n"
                "* Sector 4 archives the delta file.\n"
                "* The delta file contains code 7.\n\n"
                "Question: Which code can Soren retrieve?\n\n"
                "Answer using exactly this format:\n"
                "ANSWER: <code>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: 7",
        },
        "broad": {
            "prompt": (
                "Use only the facts below.\n\n"
                "Facts:\n"
                "* Soren holds the green badge.\n"
                "* The green badge grants entry to Sector 4.\n"
                "* Sector 4 archives the delta file.\n"
                "* The delta file contains code 7.\n\n"
                "Question: List exactly two facts from the passage.\n\n"
                "Answer using exactly this format:\n"
                "ANSWER: 1) <fact>; 2) <fact>"
            ),
            "score_type": "checklist",
            "required_facts": ["soren", "green badge", "sector 4"],
        },
        "component_checks": [
            {
                "hop": "soren_badge",
                "prompt": (
                    "Use only the facts below.\n\n"
                    "Facts:\n"
                    "* Soren holds the green badge.\n"
                    "* The green badge grants entry to Sector 4.\n"
                    "* Sector 4 archives the delta file.\n"
                    "* The delta file contains code 7.\n\n"
                    "Question: Which badge does Soren hold?\n\n"
                    "Answer using exactly this format:\n"
                    "ANSWER: <badge>"
                ),
                "score_type": "exact",
                "answer": "ANSWER: green",
            },
            {
                "hop": "badge_sector",
                "prompt": (
                    "Use only the facts below.\n\n"
                    "Facts:\n"
                    "* Soren holds the green badge.\n"
                    "* The green badge grants entry to Sector 4.\n"
                    "* Sector 4 archives the delta file.\n"
                    "* The delta file contains code 7.\n\n"
                    "Question: Which sector does the green badge grant entry to?\n\n"
                    "Answer using exactly this format:\n"
                    "ANSWER: <sector>"
                ),
                "score_type": "exact",
                "answer": "ANSWER: Sector 4",
            },
            {
                "hop": "sector_file",
                "prompt": (
                    "Use only the facts below.\n\n"
                    "Facts:\n"
                    "* Soren holds the green badge.\n"
                    "* The green badge grants entry to Sector 4.\n"
                    "* Sector 4 archives the delta file.\n"
                    "* The delta file contains code 7.\n\n"
                    "Question: Which file does Sector 4 archive?\n\n"
                    "Answer using exactly this format:\n"
                    "ANSWER: <file>"
                ),
                "score_type": "exact",
                "answer": "ANSWER: delta file",
            },
            {
                "hop": "file_code",
                "prompt": (
                    "Use only the facts below.\n\n"
                    "Facts:\n"
                    "* Soren holds the green badge.\n"
                    "* The green badge grants entry to Sector 4.\n"
                    "* Sector 4 archives the delta file.\n"
                    "* The delta file contains code 7.\n\n"
                    "Question: What does the delta file contain?\n\n"
                    "Answer using exactly this format:\n"
                    "ANSWER: <code>"
                ),
                "score_type": "exact",
                "answer": "ANSWER: code 7",
            },
        ],
    },

    # ---- LB3: 4-hop, no distractor ----
    # person → card → locker → disk → sequence
    {
        "id": "LB3",
        "source_note": "4-hop chain, no distractor; person/card/locker/disk domain",
        "narrow": {
            "prompt": (
                "Use only the facts below.\n\n"
                "Facts:\n"
                "* Taya carries the amber card.\n"
                "* The amber card unlocks Locker 12.\n"
                "* Locker 12 stores the indigo disk.\n"
                "* The indigo disk encodes sequence 44.\n\n"
                "Question: Which sequence can Taya access?\n\n"
                "Answer using exactly this format:\n"
                "ANSWER: <sequence>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: 44",
        },
        "broad": {
            "prompt": (
                "Use only the facts below.\n\n"
                "Facts:\n"
                "* Taya carries the amber card.\n"
                "* The amber card unlocks Locker 12.\n"
                "* Locker 12 stores the indigo disk.\n"
                "* The indigo disk encodes sequence 44.\n\n"
                "Question: List exactly two facts from the passage.\n\n"
                "Answer using exactly this format:\n"
                "ANSWER: 1) <fact>; 2) <fact>"
            ),
            "score_type": "checklist",
            "required_facts": ["taya", "amber card", "locker 12"],
        },
        "component_checks": [
            {
                "hop": "taya_card",
                "prompt": (
                    "Use only the facts below.\n\n"
                    "Facts:\n"
                    "* Taya carries the amber card.\n"
                    "* The amber card unlocks Locker 12.\n"
                    "* Locker 12 stores the indigo disk.\n"
                    "* The indigo disk encodes sequence 44.\n\n"
                    "Question: Which card does Taya carry?\n\n"
                    "Answer using exactly this format:\n"
                    "ANSWER: <card>"
                ),
                "score_type": "exact",
                "answer": "ANSWER: amber card",
            },
            {
                "hop": "card_locker",
                "prompt": (
                    "Use only the facts below.\n\n"
                    "Facts:\n"
                    "* Taya carries the amber card.\n"
                    "* The amber card unlocks Locker 12.\n"
                    "* Locker 12 stores the indigo disk.\n"
                    "* The indigo disk encodes sequence 44.\n\n"
                    "Question: Which locker does the amber card unlock?\n\n"
                    "Answer using exactly this format:\n"
                    "ANSWER: <locker>"
                ),
                "score_type": "exact",
                "answer": "ANSWER: Locker 12",
            },
            {
                "hop": "locker_disk",
                "prompt": (
                    "Use only the facts below.\n\n"
                    "Facts:\n"
                    "* Taya carries the amber card.\n"
                    "* The amber card unlocks Locker 12.\n"
                    "* Locker 12 stores the indigo disk.\n"
                    "* The indigo disk encodes sequence 44.\n\n"
                    "Question: Which disk does Locker 12 store?\n\n"
                    "Answer using exactly this format:\n"
                    "ANSWER: <disk>"
                ),
                "score_type": "exact",
                "answer": "ANSWER: indigo disk",
            },
            {
                "hop": "disk_sequence",
                "prompt": (
                    "Use only the facts below.\n\n"
                    "Facts:\n"
                    "* Taya carries the amber card.\n"
                    "* The amber card unlocks Locker 12.\n"
                    "* Locker 12 stores the indigo disk.\n"
                    "* The indigo disk encodes sequence 44.\n\n"
                    "Question: Which sequence does the indigo disk encode?\n\n"
                    "Answer using exactly this format:\n"
                    "ANSWER: <sequence>"
                ),
                "score_type": "exact",
                "answer": "ANSWER: 44",
            },
        ],
    },

    # ---- LB4: 4-hop, no distractor ----
    # person → permit → chamber → crystal → signal
    {
        "id": "LB4",
        "source_note": "4-hop chain, no distractor; person/permit/chamber/crystal domain",
        "narrow": {
            "prompt": (
                "Use only the facts below.\n\n"
                "Facts:\n"
                "* Kael holds the bronze permit.\n"
                "* The bronze permit opens Chamber 9.\n"
                "* Chamber 9 houses the opal crystal.\n"
                "* The opal crystal emits signal X7.\n\n"
                "Question: Which signal can Kael trigger?\n\n"
                "Answer using exactly this format:\n"
                "ANSWER: <signal>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: X7",
        },
        "broad": {
            "prompt": (
                "Use only the facts below.\n\n"
                "Facts:\n"
                "* Kael holds the bronze permit.\n"
                "* The bronze permit opens Chamber 9.\n"
                "* Chamber 9 houses the opal crystal.\n"
                "* The opal crystal emits signal X7.\n\n"
                "Question: List exactly two facts from the passage.\n\n"
                "Answer using exactly this format:\n"
                "ANSWER: 1) <fact>; 2) <fact>"
            ),
            "score_type": "checklist",
            "required_facts": ["kael", "bronze permit", "chamber 9"],
        },
        "component_checks": [
            {
                "hop": "kael_permit",
                "prompt": (
                    "Use only the facts below.\n\n"
                    "Facts:\n"
                    "* Kael holds the bronze permit.\n"
                    "* The bronze permit opens Chamber 9.\n"
                    "* Chamber 9 houses the opal crystal.\n"
                    "* The opal crystal emits signal X7.\n\n"
                    "Question: Which permit does Kael hold?\n\n"
                    "Answer using exactly this format:\n"
                    "ANSWER: <permit>"
                ),
                "score_type": "exact",
                "answer": "ANSWER: bronze permit",
            },
            {
                "hop": "permit_chamber",
                "prompt": (
                    "Use only the facts below.\n\n"
                    "Facts:\n"
                    "* Kael holds the bronze permit.\n"
                    "* The bronze permit opens Chamber 9.\n"
                    "* Chamber 9 houses the opal crystal.\n"
                    "* The opal crystal emits signal X7.\n\n"
                    "Question: Which chamber does the bronze permit open?\n\n"
                    "Answer using exactly this format:\n"
                    "ANSWER: <chamber>"
                ),
                "score_type": "exact",
                "answer": "ANSWER: Chamber 9",
            },
            {
                "hop": "chamber_crystal",
                "prompt": (
                    "Use only the facts below.\n\n"
                    "Facts:\n"
                    "* Kael holds the bronze permit.\n"
                    "* The bronze permit opens Chamber 9.\n"
                    "* Chamber 9 houses the opal crystal.\n"
                    "* The opal crystal emits signal X7.\n\n"
                    "Question: Which crystal does Chamber 9 house?\n\n"
                    "Answer using exactly this format:\n"
                    "ANSWER: <crystal>"
                ),
                "score_type": "exact",
                "answer": "ANSWER: opal crystal",
            },
            {
                "hop": "crystal_signal",
                "prompt": (
                    "Use only the facts below.\n\n"
                    "Facts:\n"
                    "* Kael holds the bronze permit.\n"
                    "* The bronze permit opens Chamber 9.\n"
                    "* Chamber 9 houses the opal crystal.\n"
                    "* The opal crystal emits signal X7.\n\n"
                    "Question: Which signal does the opal crystal emit?\n\n"
                    "Answer using exactly this format:\n"
                    "ANSWER: <signal>"
                ),
                "score_type": "exact",
                "answer": "ANSWER: X7",
            },
        ],
    },

    # ---- LC1: 4-hop + distractor chain (same domain as LB1) ----
    # Main: Nalo → red key → Vault 3 → silver token → Gate B
    # Distractor: Lyra → blue key → Vault 1 → bronze token → Gate D
    {
        "id": "LC1",
        "source_note": "4-hop + distractor; must select Nalo's chain and ignore Lyra's chain",
        "narrow": {
            "prompt": (
                "Use only the facts below.\n\n"
                "Facts:\n"
                "* Nalo owns the red key.\n"
                "* The red key opens Vault 3.\n"
                "* Vault 3 contains the silver token.\n"
                "* The silver token activates Gate B.\n"
                "* Lyra owns the blue key.\n"
                "* The blue key opens Vault 1.\n"
                "* Vault 1 contains the bronze token.\n"
                "* The bronze token activates Gate D.\n\n"
                "Question: Which gate can Nalo activate?\n\n"
                "Answer using exactly this format:\n"
                "ANSWER: <gate>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: Gate B",
        },
        "broad": {
            "prompt": (
                "Use only the facts below.\n\n"
                "Facts:\n"
                "* Nalo owns the red key.\n"
                "* The red key opens Vault 3.\n"
                "* Vault 3 contains the silver token.\n"
                "* The silver token activates Gate B.\n"
                "* Lyra owns the blue key.\n"
                "* The blue key opens Vault 1.\n"
                "* Vault 1 contains the bronze token.\n"
                "* The bronze token activates Gate D.\n\n"
                "Question: List exactly two facts from the passage.\n\n"
                "Answer using exactly this format:\n"
                "ANSWER: 1) <fact>; 2) <fact>"
            ),
            "score_type": "checklist",
            "required_facts": ["nalo", "red key", "gate b"],
        },
        "component_checks": [
            {
                "hop": "nalo_key",
                "prompt": (
                    "Use only the facts below.\n\n"
                    "Facts:\n"
                    "* Nalo owns the red key.\n"
                    "* The red key opens Vault 3.\n"
                    "* Vault 3 contains the silver token.\n"
                    "* The silver token activates Gate B.\n"
                    "* Lyra owns the blue key.\n"
                    "* The blue key opens Vault 1.\n"
                    "* Vault 1 contains the bronze token.\n"
                    "* The bronze token activates Gate D.\n\n"
                    "Question: Which key does Nalo own?\n\n"
                    "Answer using exactly this format:\n"
                    "ANSWER: <key>"
                ),
                "score_type": "exact",
                "answer": "ANSWER: red key",
            },
            {
                "hop": "key_vault",
                "prompt": (
                    "Use only the facts below.\n\n"
                    "Facts:\n"
                    "* Nalo owns the red key.\n"
                    "* The red key opens Vault 3.\n"
                    "* Vault 3 contains the silver token.\n"
                    "* The silver token activates Gate B.\n"
                    "* Lyra owns the blue key.\n"
                    "* The blue key opens Vault 1.\n"
                    "* Vault 1 contains the bronze token.\n"
                    "* The bronze token activates Gate D.\n\n"
                    "Question: Which vault does the red key open?\n\n"
                    "Answer using exactly this format:\n"
                    "ANSWER: <vault>"
                ),
                "score_type": "exact",
                "answer": "ANSWER: Vault 3",
            },
            {
                "hop": "vault_token",
                "prompt": (
                    "Use only the facts below.\n\n"
                    "Facts:\n"
                    "* Nalo owns the red key.\n"
                    "* The red key opens Vault 3.\n"
                    "* Vault 3 contains the silver token.\n"
                    "* The silver token activates Gate B.\n"
                    "* Lyra owns the blue key.\n"
                    "* The blue key opens Vault 1.\n"
                    "* Vault 1 contains the bronze token.\n"
                    "* The bronze token activates Gate D.\n\n"
                    "Question: What does Vault 3 contain?\n\n"
                    "Answer using exactly this format:\n"
                    "ANSWER: <token>"
                ),
                "score_type": "exact",
                "answer": "ANSWER: silver token",
            },
            {
                "hop": "token_gate",
                "prompt": (
                    "Use only the facts below.\n\n"
                    "Facts:\n"
                    "* Nalo owns the red key.\n"
                    "* The red key opens Vault 3.\n"
                    "* Vault 3 contains the silver token.\n"
                    "* The silver token activates Gate B.\n"
                    "* Lyra owns the blue key.\n"
                    "* The blue key opens Vault 1.\n"
                    "* Vault 1 contains the bronze token.\n"
                    "* The bronze token activates Gate D.\n\n"
                    "Question: Which gate does the silver token activate?\n\n"
                    "Answer using exactly this format:\n"
                    "ANSWER: <gate>"
                ),
                "score_type": "exact",
                "answer": "ANSWER: Gate B",
            },
        ],
    },

    # ---- LC2: 4-hop + distractor chain (badge/sector domain) ----
    # Main: Soren → green badge → Sector 4 → delta file → code 7
    # Distractor: Mira → orange badge → Sector 2 → epsilon file → code 3
    {
        "id": "LC2",
        "source_note": "4-hop + distractor; badge/sector domain; must select Soren's chain",
        "narrow": {
            "prompt": (
                "Use only the facts below.\n\n"
                "Facts:\n"
                "* Soren holds the green badge.\n"
                "* The green badge grants entry to Sector 4.\n"
                "* Sector 4 archives the delta file.\n"
                "* The delta file contains code 7.\n"
                "* Mira holds the orange badge.\n"
                "* The orange badge grants entry to Sector 2.\n"
                "* Sector 2 archives the epsilon file.\n"
                "* The epsilon file contains code 3.\n\n"
                "Question: Which code can Soren retrieve?\n\n"
                "Answer using exactly this format:\n"
                "ANSWER: <code>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: 7",
        },
        "broad": {
            "prompt": (
                "Use only the facts below.\n\n"
                "Facts:\n"
                "* Soren holds the green badge.\n"
                "* The green badge grants entry to Sector 4.\n"
                "* Sector 4 archives the delta file.\n"
                "* The delta file contains code 7.\n"
                "* Mira holds the orange badge.\n"
                "* The orange badge grants entry to Sector 2.\n"
                "* Sector 2 archives the epsilon file.\n"
                "* The epsilon file contains code 3.\n\n"
                "Question: List exactly two facts from the passage.\n\n"
                "Answer using exactly this format:\n"
                "ANSWER: 1) <fact>; 2) <fact>"
            ),
            "score_type": "checklist",
            "required_facts": ["soren", "green badge", "sector 4"],
        },
        "component_checks": [
            {
                "hop": "soren_badge",
                "prompt": (
                    "Use only the facts below.\n\n"
                    "Facts:\n"
                    "* Soren holds the green badge.\n"
                    "* The green badge grants entry to Sector 4.\n"
                    "* Sector 4 archives the delta file.\n"
                    "* The delta file contains code 7.\n"
                    "* Mira holds the orange badge.\n"
                    "* The orange badge grants entry to Sector 2.\n"
                    "* Sector 2 archives the epsilon file.\n"
                    "* The epsilon file contains code 3.\n\n"
                    "Question: Which badge does Soren hold?\n\n"
                    "Answer using exactly this format:\n"
                    "ANSWER: <badge>"
                ),
                "score_type": "exact",
                "answer": "ANSWER: green",
            },
            {
                "hop": "badge_sector",
                "prompt": (
                    "Use only the facts below.\n\n"
                    "Facts:\n"
                    "* Soren holds the green badge.\n"
                    "* The green badge grants entry to Sector 4.\n"
                    "* Sector 4 archives the delta file.\n"
                    "* The delta file contains code 7.\n"
                    "* Mira holds the orange badge.\n"
                    "* The orange badge grants entry to Sector 2.\n"
                    "* Sector 2 archives the epsilon file.\n"
                    "* The epsilon file contains code 3.\n\n"
                    "Question: Which sector does the green badge grant entry to?\n\n"
                    "Answer using exactly this format:\n"
                    "ANSWER: <sector>"
                ),
                "score_type": "exact",
                "answer": "ANSWER: Sector 4",
            },
            {
                "hop": "sector_file",
                "prompt": (
                    "Use only the facts below.\n\n"
                    "Facts:\n"
                    "* Soren holds the green badge.\n"
                    "* The green badge grants entry to Sector 4.\n"
                    "* Sector 4 archives the delta file.\n"
                    "* The delta file contains code 7.\n"
                    "* Mira holds the orange badge.\n"
                    "* The orange badge grants entry to Sector 2.\n"
                    "* Sector 2 archives the epsilon file.\n"
                    "* The epsilon file contains code 3.\n\n"
                    "Question: Which file does Sector 4 archive?\n\n"
                    "Answer using exactly this format:\n"
                    "ANSWER: <file>"
                ),
                "score_type": "exact",
                "answer": "ANSWER: delta file",
            },
            {
                "hop": "file_code",
                "prompt": (
                    "Use only the facts below.\n\n"
                    "Facts:\n"
                    "* Soren holds the green badge.\n"
                    "* The green badge grants entry to Sector 4.\n"
                    "* Sector 4 archives the delta file.\n"
                    "* The delta file contains code 7.\n"
                    "* Mira holds the orange badge.\n"
                    "* The orange badge grants entry to Sector 2.\n"
                    "* Sector 2 archives the epsilon file.\n"
                    "* The epsilon file contains code 3.\n\n"
                    "Question: What does the delta file contain?\n\n"
                    "Answer using exactly this format:\n"
                    "ANSWER: <code>"
                ),
                "score_type": "exact",
                "answer": "ANSWER: 7",
            },
        ],
    },

    # ---- LC3: 4-hop + distractor chain (card/locker domain) ----
    # Main: Taya → amber card → Locker 12 → indigo disk → sequence 44
    # Distractor: Remy → silver card → Locker 5 → crimson disk → sequence 19
    {
        "id": "LC3",
        "source_note": "4-hop + distractor; card/locker domain; must select Taya's chain",
        "narrow": {
            "prompt": (
                "Use only the facts below.\n\n"
                "Facts:\n"
                "* Taya carries the amber card.\n"
                "* The amber card unlocks Locker 12.\n"
                "* Locker 12 stores the indigo disk.\n"
                "* The indigo disk encodes sequence 44.\n"
                "* Remy carries the silver card.\n"
                "* The silver card unlocks Locker 5.\n"
                "* Locker 5 stores the crimson disk.\n"
                "* The crimson disk encodes sequence 19.\n\n"
                "Question: Which sequence can Taya access?\n\n"
                "Answer using exactly this format:\n"
                "ANSWER: <sequence>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: 44",
        },
        "broad": {
            "prompt": (
                "Use only the facts below.\n\n"
                "Facts:\n"
                "* Taya carries the amber card.\n"
                "* The amber card unlocks Locker 12.\n"
                "* Locker 12 stores the indigo disk.\n"
                "* The indigo disk encodes sequence 44.\n"
                "* Remy carries the silver card.\n"
                "* The silver card unlocks Locker 5.\n"
                "* Locker 5 stores the crimson disk.\n"
                "* The crimson disk encodes sequence 19.\n\n"
                "Question: List exactly two facts from the passage.\n\n"
                "Answer using exactly this format:\n"
                "ANSWER: 1) <fact>; 2) <fact>"
            ),
            "score_type": "checklist",
            "required_facts": ["taya", "amber card", "locker 12"],
        },
        "component_checks": [
            {
                "hop": "taya_card",
                "prompt": (
                    "Use only the facts below.\n\n"
                    "Facts:\n"
                    "* Taya carries the amber card.\n"
                    "* The amber card unlocks Locker 12.\n"
                    "* Locker 12 stores the indigo disk.\n"
                    "* The indigo disk encodes sequence 44.\n"
                    "* Remy carries the silver card.\n"
                    "* The silver card unlocks Locker 5.\n"
                    "* Locker 5 stores the crimson disk.\n"
                    "* The crimson disk encodes sequence 19.\n\n"
                    "Question: Which card does Taya carry?\n\n"
                    "Answer using exactly this format:\n"
                    "ANSWER: <card>"
                ),
                "score_type": "exact",
                "answer": "ANSWER: amber card",
            },
            {
                "hop": "card_locker",
                "prompt": (
                    "Use only the facts below.\n\n"
                    "Facts:\n"
                    "* Taya carries the amber card.\n"
                    "* The amber card unlocks Locker 12.\n"
                    "* Locker 12 stores the indigo disk.\n"
                    "* The indigo disk encodes sequence 44.\n"
                    "* Remy carries the silver card.\n"
                    "* The silver card unlocks Locker 5.\n"
                    "* Locker 5 stores the crimson disk.\n"
                    "* The crimson disk encodes sequence 19.\n\n"
                    "Question: Which locker does the amber card unlock?\n\n"
                    "Answer using exactly this format:\n"
                    "ANSWER: <locker>"
                ),
                "score_type": "exact",
                "answer": "ANSWER: Locker 12",
            },
            {
                "hop": "locker_disk",
                "prompt": (
                    "Use only the facts below.\n\n"
                    "Facts:\n"
                    "* Taya carries the amber card.\n"
                    "* The amber card unlocks Locker 12.\n"
                    "* Locker 12 stores the indigo disk.\n"
                    "* The indigo disk encodes sequence 44.\n"
                    "* Remy carries the silver card.\n"
                    "* The silver card unlocks Locker 5.\n"
                    "* Locker 5 stores the crimson disk.\n"
                    "* The crimson disk encodes sequence 19.\n\n"
                    "Question: Which disk does Locker 12 store?\n\n"
                    "Answer using exactly this format:\n"
                    "ANSWER: <disk>"
                ),
                "score_type": "exact",
                "answer": "ANSWER: indigo disk",
            },
            {
                "hop": "disk_sequence",
                "prompt": (
                    "Use only the facts below.\n\n"
                    "Facts:\n"
                    "* Taya carries the amber card.\n"
                    "* The amber card unlocks Locker 12.\n"
                    "* Locker 12 stores the indigo disk.\n"
                    "* The indigo disk encodes sequence 44.\n"
                    "* Remy carries the silver card.\n"
                    "* The silver card unlocks Locker 5.\n"
                    "* Locker 5 stores the crimson disk.\n"
                    "* The crimson disk encodes sequence 19.\n\n"
                    "Question: Which sequence does the indigo disk encode?\n\n"
                    "Answer using exactly this format:\n"
                    "ANSWER: <sequence>"
                ),
                "score_type": "exact",
                "answer": "ANSWER: 44",
            },
        ],
    },

    # ---- LC4: 4-hop + distractor chain (permit/chamber domain) ----
    # Main: Kael → bronze permit → Chamber 9 → opal crystal → signal X7
    # Distractor: Voss → copper permit → Chamber 2 → jade crystal → signal K3
    {
        "id": "LC4",
        "source_note": "4-hop + distractor; permit/chamber domain; must select Kael's chain",
        "narrow": {
            "prompt": (
                "Use only the facts below.\n\n"
                "Facts:\n"
                "* Kael holds the bronze permit.\n"
                "* The bronze permit opens Chamber 9.\n"
                "* Chamber 9 houses the opal crystal.\n"
                "* The opal crystal emits signal X7.\n"
                "* Voss holds the copper permit.\n"
                "* The copper permit opens Chamber 2.\n"
                "* Chamber 2 houses the jade crystal.\n"
                "* The jade crystal emits signal K3.\n\n"
                "Question: Which signal can Kael trigger?\n\n"
                "Answer using exactly this format:\n"
                "ANSWER: <signal>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: X7",
        },
        "broad": {
            "prompt": (
                "Use only the facts below.\n\n"
                "Facts:\n"
                "* Kael holds the bronze permit.\n"
                "* The bronze permit opens Chamber 9.\n"
                "* Chamber 9 houses the opal crystal.\n"
                "* The opal crystal emits signal X7.\n"
                "* Voss holds the copper permit.\n"
                "* The copper permit opens Chamber 2.\n"
                "* Chamber 2 houses the jade crystal.\n"
                "* The jade crystal emits signal K3.\n\n"
                "Question: List exactly two facts from the passage.\n\n"
                "Answer using exactly this format:\n"
                "ANSWER: 1) <fact>; 2) <fact>"
            ),
            "score_type": "checklist",
            "required_facts": ["kael", "bronze permit", "chamber 9"],
        },
        "component_checks": [
            {
                "hop": "kael_permit",
                "prompt": (
                    "Use only the facts below.\n\n"
                    "Facts:\n"
                    "* Kael holds the bronze permit.\n"
                    "* The bronze permit opens Chamber 9.\n"
                    "* Chamber 9 houses the opal crystal.\n"
                    "* The opal crystal emits signal X7.\n"
                    "* Voss holds the copper permit.\n"
                    "* The copper permit opens Chamber 2.\n"
                    "* Chamber 2 houses the jade crystal.\n"
                    "* The jade crystal emits signal K3.\n\n"
                    "Question: Which permit does Kael hold?\n\n"
                    "Answer using exactly this format:\n"
                    "ANSWER: <permit>"
                ),
                "score_type": "exact",
                "answer": "ANSWER: bronze permit",
            },
            {
                "hop": "permit_chamber",
                "prompt": (
                    "Use only the facts below.\n\n"
                    "Facts:\n"
                    "* Kael holds the bronze permit.\n"
                    "* The bronze permit opens Chamber 9.\n"
                    "* Chamber 9 houses the opal crystal.\n"
                    "* The opal crystal emits signal X7.\n"
                    "* Voss holds the copper permit.\n"
                    "* The copper permit opens Chamber 2.\n"
                    "* Chamber 2 houses the jade crystal.\n"
                    "* The jade crystal emits signal K3.\n\n"
                    "Question: Which chamber does the bronze permit open?\n\n"
                    "Answer using exactly this format:\n"
                    "ANSWER: <chamber>"
                ),
                "score_type": "exact",
                "answer": "ANSWER: Chamber 9",
            },
            {
                "hop": "chamber_crystal",
                "prompt": (
                    "Use only the facts below.\n\n"
                    "Facts:\n"
                    "* Kael holds the bronze permit.\n"
                    "* The bronze permit opens Chamber 9.\n"
                    "* Chamber 9 houses the opal crystal.\n"
                    "* The opal crystal emits signal X7.\n"
                    "* Voss holds the copper permit.\n"
                    "* The copper permit opens Chamber 2.\n"
                    "* Chamber 2 houses the jade crystal.\n"
                    "* The jade crystal emits signal K3.\n\n"
                    "Question: Which crystal does Chamber 9 house?\n\n"
                    "Answer using exactly this format:\n"
                    "ANSWER: <crystal>"
                ),
                "score_type": "exact",
                "answer": "ANSWER: opal",
            },
            {
                "hop": "crystal_signal",
                "prompt": (
                    "Use only the facts below.\n\n"
                    "Facts:\n"
                    "* Kael holds the bronze permit.\n"
                    "* The bronze permit opens Chamber 9.\n"
                    "* Chamber 9 houses the opal crystal.\n"
                    "* The opal crystal emits signal X7.\n"
                    "* Voss holds the copper permit.\n"
                    "* The copper permit opens Chamber 2.\n"
                    "* Chamber 2 houses the jade crystal.\n"
                    "* The jade crystal emits signal K3.\n\n"
                    "Question: Which signal does the opal crystal emit?\n\n"
                    "Answer using exactly this format:\n"
                    "ANSWER: <signal>"
                ),
                "score_type": "exact",
                "answer": "ANSWER: X7",
            },
        ],
    },

    # ---- LD1: 5-hop + distractor ----
    # Main: Ziri → gold key → Vault 7 → emerald token → Terminal C → passcode 91
    # Distractor: Lyra → silver key → Vault 4 → ruby token → Terminal A → passcode 55
    {
        "id": "LD1",
        "source_note": "5-hop + distractor; key/vault/token/terminal/passcode domain",
        "narrow": {
            "prompt": (
                "Use only the facts below.\n\n"
                "Facts:\n"
                "* Ziri owns the gold key.\n"
                "* The gold key opens Vault 7.\n"
                "* Vault 7 contains the emerald token.\n"
                "* The emerald token activates Terminal C.\n"
                "* Terminal C holds passcode 91.\n"
                "* Lyra owns the silver key.\n"
                "* The silver key opens Vault 4.\n"
                "* Vault 4 contains the ruby token.\n"
                "* The ruby token activates Terminal A.\n"
                "* Terminal A holds passcode 55.\n\n"
                "Question: Which passcode is accessible to Ziri?\n\n"
                "Answer using exactly this format:\n"
                "ANSWER: <passcode>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: 91",
        },
        "broad": {
            "prompt": (
                "Use only the facts below.\n\n"
                "Facts:\n"
                "* Ziri owns the gold key.\n"
                "* The gold key opens Vault 7.\n"
                "* Vault 7 contains the emerald token.\n"
                "* The emerald token activates Terminal C.\n"
                "* Terminal C holds passcode 91.\n"
                "* Lyra owns the silver key.\n"
                "* The silver key opens Vault 4.\n"
                "* Vault 4 contains the ruby token.\n"
                "* The ruby token activates Terminal A.\n"
                "* Terminal A holds passcode 55.\n\n"
                "Question: List exactly two facts from the passage.\n\n"
                "Answer using exactly this format:\n"
                "ANSWER: 1) <fact>; 2) <fact>"
            ),
            "score_type": "checklist",
            "required_facts": ["ziri", "gold key", "vault 7"],
        },
        "component_checks": [
            {
                "hop": "ziri_key",
                "prompt": (
                    "Use only the facts below.\n\n"
                    "Facts:\n"
                    "* Ziri owns the gold key.\n"
                    "* The gold key opens Vault 7.\n"
                    "* Vault 7 contains the emerald token.\n"
                    "* The emerald token activates Terminal C.\n"
                    "* Terminal C holds passcode 91.\n"
                    "* Lyra owns the silver key.\n"
                    "* The silver key opens Vault 4.\n"
                    "* Vault 4 contains the ruby token.\n"
                    "* The ruby token activates Terminal A.\n"
                    "* Terminal A holds passcode 55.\n\n"
                    "Question: Which key does Ziri own?\n\n"
                    "Answer using exactly this format:\n"
                    "ANSWER: <key>"
                ),
                "score_type": "exact",
                "answer": "ANSWER: gold key",
            },
            {
                "hop": "key_vault",
                "prompt": (
                    "Use only the facts below.\n\n"
                    "Facts:\n"
                    "* Ziri owns the gold key.\n"
                    "* The gold key opens Vault 7.\n"
                    "* Vault 7 contains the emerald token.\n"
                    "* The emerald token activates Terminal C.\n"
                    "* Terminal C holds passcode 91.\n"
                    "* Lyra owns the silver key.\n"
                    "* The silver key opens Vault 4.\n"
                    "* Vault 4 contains the ruby token.\n"
                    "* The ruby token activates Terminal A.\n"
                    "* Terminal A holds passcode 55.\n\n"
                    "Question: Which vault does the gold key open?\n\n"
                    "Answer using exactly this format:\n"
                    "ANSWER: <vault>"
                ),
                "score_type": "exact",
                "answer": "ANSWER: Vault 7",
            },
            {
                "hop": "vault_token",
                "prompt": (
                    "Use only the facts below.\n\n"
                    "Facts:\n"
                    "* Ziri owns the gold key.\n"
                    "* The gold key opens Vault 7.\n"
                    "* Vault 7 contains the emerald token.\n"
                    "* The emerald token activates Terminal C.\n"
                    "* Terminal C holds passcode 91.\n"
                    "* Lyra owns the silver key.\n"
                    "* The silver key opens Vault 4.\n"
                    "* Vault 4 contains the ruby token.\n"
                    "* The ruby token activates Terminal A.\n"
                    "* Terminal A holds passcode 55.\n\n"
                    "Question: What does Vault 7 contain?\n\n"
                    "Answer using exactly this format:\n"
                    "ANSWER: <token>"
                ),
                "score_type": "exact",
                "answer": "ANSWER: emerald token",
            },
            {
                "hop": "token_terminal",
                "prompt": (
                    "Use only the facts below.\n\n"
                    "Facts:\n"
                    "* Ziri owns the gold key.\n"
                    "* The gold key opens Vault 7.\n"
                    "* Vault 7 contains the emerald token.\n"
                    "* The emerald token activates Terminal C.\n"
                    "* Terminal C holds passcode 91.\n"
                    "* Lyra owns the silver key.\n"
                    "* The silver key opens Vault 4.\n"
                    "* Vault 4 contains the ruby token.\n"
                    "* The ruby token activates Terminal A.\n"
                    "* Terminal A holds passcode 55.\n\n"
                    "Question: Which terminal does the emerald token activate?\n\n"
                    "Answer using exactly this format:\n"
                    "ANSWER: <terminal>"
                ),
                "score_type": "exact",
                "answer": "ANSWER: Terminal C",
            },
            {
                "hop": "terminal_passcode",
                "prompt": (
                    "Use only the facts below.\n\n"
                    "Facts:\n"
                    "* Ziri owns the gold key.\n"
                    "* The gold key opens Vault 7.\n"
                    "* Vault 7 contains the emerald token.\n"
                    "* The emerald token activates Terminal C.\n"
                    "* Terminal C holds passcode 91.\n"
                    "* Lyra owns the silver key.\n"
                    "* The silver key opens Vault 4.\n"
                    "* Vault 4 contains the ruby token.\n"
                    "* The ruby token activates Terminal A.\n"
                    "* Terminal A holds passcode 55.\n\n"
                    "Question: Which passcode does Terminal C hold?\n\n"
                    "Answer using exactly this format:\n"
                    "ANSWER: <passcode>"
                ),
                "score_type": "exact",
                "answer": "ANSWER: 91",
            },
        ],
    },

    # ---- LD2: 5-hop + distractor ----
    # Main: Bren → blue chip → Zone 6 → quartz shard → Station R → frequency 330
    # Distractor: Cass → red chip → Zone 2 → iron shard → Station P → frequency 120
    {
        "id": "LD2",
        "source_note": "5-hop + distractor; chip/zone/shard/station/frequency domain",
        "narrow": {
            "prompt": (
                "Use only the facts below.\n\n"
                "Facts:\n"
                "* Bren holds the blue chip.\n"
                "* The blue chip grants access to Zone 6.\n"
                "* Zone 6 contains the quartz shard.\n"
                "* The quartz shard tunes Station R.\n"
                "* Station R broadcasts frequency 330.\n"
                "* Cass holds the red chip.\n"
                "* The red chip grants access to Zone 2.\n"
                "* Zone 2 contains the iron shard.\n"
                "* The iron shard tunes Station P.\n"
                "* Station P broadcasts frequency 120.\n\n"
                "Question: Which frequency can Bren access?\n\n"
                "Answer using exactly this format:\n"
                "ANSWER: <frequency>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: 330",
        },
        "broad": {
            "prompt": (
                "Use only the facts below.\n\n"
                "Facts:\n"
                "* Bren holds the blue chip.\n"
                "* The blue chip grants access to Zone 6.\n"
                "* Zone 6 contains the quartz shard.\n"
                "* The quartz shard tunes Station R.\n"
                "* Station R broadcasts frequency 330.\n"
                "* Cass holds the red chip.\n"
                "* The red chip grants access to Zone 2.\n"
                "* Zone 2 contains the iron shard.\n"
                "* The iron shard tunes Station P.\n"
                "* Station P broadcasts frequency 120.\n\n"
                "Question: List exactly two facts from the passage.\n\n"
                "Answer using exactly this format:\n"
                "ANSWER: 1) <fact>; 2) <fact>"
            ),
            "score_type": "checklist",
            "required_facts": ["bren", "blue chip", "zone 6"],
        },
        "component_checks": [
            {
                "hop": "bren_chip",
                "prompt": (
                    "Use only the facts below.\n\n"
                    "Facts:\n"
                    "* Bren holds the blue chip.\n"
                    "* The blue chip grants access to Zone 6.\n"
                    "* Zone 6 contains the quartz shard.\n"
                    "* The quartz shard tunes Station R.\n"
                    "* Station R broadcasts frequency 330.\n"
                    "* Cass holds the red chip.\n"
                    "* The red chip grants access to Zone 2.\n"
                    "* Zone 2 contains the iron shard.\n"
                    "* The iron shard tunes Station P.\n"
                    "* Station P broadcasts frequency 120.\n\n"
                    "Question: Which chip does Bren hold?\n\n"
                    "Answer using exactly this format:\n"
                    "ANSWER: <chip>"
                ),
                "score_type": "exact",
                "answer": "ANSWER: blue chip",
            },
            {
                "hop": "chip_zone",
                "prompt": (
                    "Use only the facts below.\n\n"
                    "Facts:\n"
                    "* Bren holds the blue chip.\n"
                    "* The blue chip grants access to Zone 6.\n"
                    "* Zone 6 contains the quartz shard.\n"
                    "* The quartz shard tunes Station R.\n"
                    "* Station R broadcasts frequency 330.\n"
                    "* Cass holds the red chip.\n"
                    "* The red chip grants access to Zone 2.\n"
                    "* Zone 2 contains the iron shard.\n"
                    "* The iron shard tunes Station P.\n"
                    "* Station P broadcasts frequency 120.\n\n"
                    "Question: Which zone does the blue chip grant access to?\n\n"
                    "Answer using exactly this format:\n"
                    "ANSWER: <zone>"
                ),
                "score_type": "exact",
                "answer": "ANSWER: Zone 6",
            },
            {
                "hop": "zone_shard",
                "prompt": (
                    "Use only the facts below.\n\n"
                    "Facts:\n"
                    "* Bren holds the blue chip.\n"
                    "* The blue chip grants access to Zone 6.\n"
                    "* Zone 6 contains the quartz shard.\n"
                    "* The quartz shard tunes Station R.\n"
                    "* Station R broadcasts frequency 330.\n"
                    "* Cass holds the red chip.\n"
                    "* The red chip grants access to Zone 2.\n"
                    "* Zone 2 contains the iron shard.\n"
                    "* The iron shard tunes Station P.\n"
                    "* Station P broadcasts frequency 120.\n\n"
                    "Question: Which shard does Zone 6 contain?\n\n"
                    "Answer using exactly this format:\n"
                    "ANSWER: <shard>"
                ),
                "score_type": "exact",
                "answer": "ANSWER: quartz shard",
            },
            {
                "hop": "shard_station",
                "prompt": (
                    "Use only the facts below.\n\n"
                    "Facts:\n"
                    "* Bren holds the blue chip.\n"
                    "* The blue chip grants access to Zone 6.\n"
                    "* Zone 6 contains the quartz shard.\n"
                    "* The quartz shard tunes Station R.\n"
                    "* Station R broadcasts frequency 330.\n"
                    "* Cass holds the red chip.\n"
                    "* The red chip grants access to Zone 2.\n"
                    "* Zone 2 contains the iron shard.\n"
                    "* The iron shard tunes Station P.\n"
                    "* Station P broadcasts frequency 120.\n\n"
                    "Question: Which station does the quartz shard tune?\n\n"
                    "Answer using exactly this format:\n"
                    "ANSWER: <station>"
                ),
                "score_type": "exact",
                "answer": "ANSWER: Station R",
            },
            {
                "hop": "station_frequency",
                "prompt": (
                    "Use only the facts below.\n\n"
                    "Facts:\n"
                    "* Bren holds the blue chip.\n"
                    "* The blue chip grants access to Zone 6.\n"
                    "* Zone 6 contains the quartz shard.\n"
                    "* The quartz shard tunes Station R.\n"
                    "* Station R broadcasts frequency 330.\n"
                    "* Cass holds the red chip.\n"
                    "* The red chip grants access to Zone 2.\n"
                    "* Zone 2 contains the iron shard.\n"
                    "* The iron shard tunes Station P.\n"
                    "* Station P broadcasts frequency 120.\n\n"
                    "Question: Which frequency does Station R broadcast?\n\n"
                    "Answer using exactly this format:\n"
                    "ANSWER: <frequency>"
                ),
                "score_type": "exact",
                "answer": "ANSWER: 330",
            },
        ],
    },

    # ---- LD3: 5-hop + distractor + negation ----
    # Main: Finn → platinum pass → Wing 3 → topaz cube → Panel 8 → cipher 77
    # Negation: "Finn does not hold an iron pass."
    # Distractor: Gale → iron pass → Wing 1 → onyx cube → Panel 2 → cipher 33
    {
        "id": "LD3",
        "source_type": "5-hop + distractor + negation; negation targets the distractor entity's access item",
        "narrow": {
            "prompt": (
                "Use only the facts below.\n\n"
                "Facts:\n"
                "* Finn holds the platinum pass.\n"
                "* Finn does not hold an iron pass.\n"
                "* The platinum pass grants entry to Wing 3.\n"
                "* Wing 3 contains the topaz cube.\n"
                "* The topaz cube activates Panel 8.\n"
                "* Panel 8 holds cipher 77.\n"
                "* Gale holds the iron pass.\n"
                "* The iron pass grants entry to Wing 1.\n"
                "* Wing 1 contains the onyx cube.\n"
                "* The onyx cube activates Panel 2.\n"
                "* Panel 2 holds cipher 33.\n\n"
                "Question: Which cipher can Finn access?\n\n"
                "Answer using exactly this format:\n"
                "ANSWER: <cipher>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: 77",
        },
        "broad": {
            "prompt": (
                "Use only the facts below.\n\n"
                "Facts:\n"
                "* Finn holds the platinum pass.\n"
                "* Finn does not hold an iron pass.\n"
                "* The platinum pass grants entry to Wing 3.\n"
                "* Wing 3 contains the topaz cube.\n"
                "* The topaz cube activates Panel 8.\n"
                "* Panel 8 holds cipher 77.\n"
                "* Gale holds the iron pass.\n"
                "* The iron pass grants entry to Wing 1.\n"
                "* Wing 1 contains the onyx cube.\n"
                "* The onyx cube activates Panel 2.\n"
                "* Panel 2 holds cipher 33.\n\n"
                "Question: List exactly two facts from the passage.\n\n"
                "Answer using exactly this format:\n"
                "ANSWER: 1) <fact>; 2) <fact>"
            ),
            "score_type": "checklist",
            "required_facts": ["finn", "platinum pass", "wing 3"],
        },
        "component_checks": [
            {
                "hop": "finn_pass",
                "prompt": (
                    "Use only the facts below.\n\n"
                    "Facts:\n"
                    "* Finn holds the platinum pass.\n"
                    "* Finn does not hold an iron pass.\n"
                    "* The platinum pass grants entry to Wing 3.\n"
                    "* Wing 3 contains the topaz cube.\n"
                    "* The topaz cube activates Panel 8.\n"
                    "* Panel 8 holds cipher 77.\n"
                    "* Gale holds the iron pass.\n"
                    "* The iron pass grants entry to Wing 1.\n"
                    "* Wing 1 contains the onyx cube.\n"
                    "* The onyx cube activates Panel 2.\n"
                    "* Panel 2 holds cipher 33.\n\n"
                    "Question: Which pass does Finn hold?\n\n"
                    "Answer using exactly this format:\n"
                    "ANSWER: <pass>"
                ),
                "score_type": "exact",
                "answer": "ANSWER: platinum",
            },
            {
                "hop": "pass_wing",
                "prompt": (
                    "Use only the facts below.\n\n"
                    "Facts:\n"
                    "* Finn holds the platinum pass.\n"
                    "* Finn does not hold an iron pass.\n"
                    "* The platinum pass grants entry to Wing 3.\n"
                    "* Wing 3 contains the topaz cube.\n"
                    "* The topaz cube activates Panel 8.\n"
                    "* Panel 8 holds cipher 77.\n"
                    "* Gale holds the iron pass.\n"
                    "* The iron pass grants entry to Wing 1.\n"
                    "* Wing 1 contains the onyx cube.\n"
                    "* The onyx cube activates Panel 2.\n"
                    "* Panel 2 holds cipher 33.\n\n"
                    "Question: Which wing does the platinum pass grant entry to?\n\n"
                    "Answer using exactly this format:\n"
                    "ANSWER: <wing>"
                ),
                "score_type": "exact",
                "answer": "ANSWER: Wing 3",
            },
            {
                "hop": "wing_cube",
                "prompt": (
                    "Use only the facts below.\n\n"
                    "Facts:\n"
                    "* Finn holds the platinum pass.\n"
                    "* Finn does not hold an iron pass.\n"
                    "* The platinum pass grants entry to Wing 3.\n"
                    "* Wing 3 contains the topaz cube.\n"
                    "* The topaz cube activates Panel 8.\n"
                    "* Panel 8 holds cipher 77.\n"
                    "* Gale holds the iron pass.\n"
                    "* The iron pass grants entry to Wing 1.\n"
                    "* Wing 1 contains the onyx cube.\n"
                    "* The onyx cube activates Panel 2.\n"
                    "* Panel 2 holds cipher 33.\n\n"
                    "Question: Which cube does Wing 3 contain?\n\n"
                    "Answer using exactly this format:\n"
                    "ANSWER: <cube>"
                ),
                "score_type": "exact",
                "answer": "ANSWER: topaz cube",
            },
            {
                "hop": "cube_panel",
                "prompt": (
                    "Use only the facts below.\n\n"
                    "Facts:\n"
                    "* Finn holds the platinum pass.\n"
                    "* Finn does not hold an iron pass.\n"
                    "* The platinum pass grants entry to Wing 3.\n"
                    "* Wing 3 contains the topaz cube.\n"
                    "* The topaz cube activates Panel 8.\n"
                    "* Panel 8 holds cipher 77.\n"
                    "* Gale holds the iron pass.\n"
                    "* The iron pass grants entry to Wing 1.\n"
                    "* Wing 1 contains the onyx cube.\n"
                    "* The onyx cube activates Panel 2.\n"
                    "* Panel 2 holds cipher 33.\n\n"
                    "Question: Which panel does the topaz cube activate?\n\n"
                    "Answer using exactly this format:\n"
                    "ANSWER: <panel>"
                ),
                "score_type": "exact",
                "answer": "ANSWER: Panel 8",
            },
            {
                "hop": "panel_cipher",
                "prompt": (
                    "Use only the facts below.\n\n"
                    "Facts:\n"
                    "* Finn holds the platinum pass.\n"
                    "* Finn does not hold an iron pass.\n"
                    "* The platinum pass grants entry to Wing 3.\n"
                    "* Wing 3 contains the topaz cube.\n"
                    "* The topaz cube activates Panel 8.\n"
                    "* Panel 8 holds cipher 77.\n"
                    "* Gale holds the iron pass.\n"
                    "* The iron pass grants entry to Wing 1.\n"
                    "* Wing 1 contains the onyx cube.\n"
                    "* The onyx cube activates Panel 2.\n"
                    "* Panel 2 holds cipher 33.\n\n"
                    "Question: Which cipher does Panel 8 hold?\n\n"
                    "Answer using exactly this format:\n"
                    "ANSWER: <cipher>"
                ),
                "score_type": "exact",
                "answer": "ANSWER: cipher 77",
            },
        ],
    },

    # ---- LD4: 5-hop + two distractors ----
    # Main: Hira → jade tag → Block 5 → copper capsule → Bay 9 → code 248
    # Distractor 1: Wren → pearl tag → Block 3 → silver capsule → Bay 1 → code 119
    # Distractor 2: Oda → obsidian tag → Block 7 → glass capsule → Bay 4 → code 562
    {
        "id": "LD4",
        "source_note": "5-hop + two distractors; maximum state-load in this set",
        "narrow": {
            "prompt": (
                "Use only the facts below.\n\n"
                "Facts:\n"
                "* Hira carries the jade tag.\n"
                "* The jade tag unlocks Block 5.\n"
                "* Block 5 stores the copper capsule.\n"
                "* The copper capsule opens Bay 9.\n"
                "* Bay 9 holds code 248.\n"
                "* Wren carries the pearl tag.\n"
                "* The pearl tag unlocks Block 3.\n"
                "* Block 3 stores the silver capsule.\n"
                "* The silver capsule opens Bay 1.\n"
                "* Bay 1 holds code 119.\n"
                "* Oda carries the obsidian tag.\n"
                "* The obsidian tag unlocks Block 7.\n"
                "* Block 7 stores the glass capsule.\n"
                "* The glass capsule opens Bay 4.\n"
                "* Bay 4 holds code 562.\n\n"
                "Question: Which code does Hira's path lead to?\n\n"
                "Answer using exactly this format:\n"
                "ANSWER: <code>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: 248",
        },
        "broad": {
            "prompt": (
                "Use only the facts below.\n\n"
                "Facts:\n"
                "* Hira carries the jade tag.\n"
                "* The jade tag unlocks Block 5.\n"
                "* Block 5 stores the copper capsule.\n"
                "* The copper capsule opens Bay 9.\n"
                "* Bay 9 holds code 248.\n"
                "* Wren carries the pearl tag.\n"
                "* The pearl tag unlocks Block 3.\n"
                "* Block 3 stores the silver capsule.\n"
                "* The silver capsule opens Bay 1.\n"
                "* Bay 1 holds code 119.\n"
                "* Oda carries the obsidian tag.\n"
                "* The obsidian tag unlocks Block 7.\n"
                "* Block 7 stores the glass capsule.\n"
                "* The glass capsule opens Bay 4.\n"
                "* Bay 4 holds code 562.\n\n"
                "Question: List exactly two facts from the passage.\n\n"
                "Answer using exactly this format:\n"
                "ANSWER: 1) <fact>; 2) <fact>"
            ),
            "score_type": "checklist",
            "required_facts": ["hira", "jade tag", "block 5"],
        },
        "component_checks": [
            {
                "hop": "hira_tag",
                "prompt": (
                    "Use only the facts below.\n\n"
                    "Facts:\n"
                    "* Hira carries the jade tag.\n"
                    "* The jade tag unlocks Block 5.\n"
                    "* Block 5 stores the copper capsule.\n"
                    "* The copper capsule opens Bay 9.\n"
                    "* Bay 9 holds code 248.\n"
                    "* Wren carries the pearl tag.\n"
                    "* The pearl tag unlocks Block 3.\n"
                    "* Block 3 stores the silver capsule.\n"
                    "* The silver capsule opens Bay 1.\n"
                    "* Bay 1 holds code 119.\n"
                    "* Oda carries the obsidian tag.\n"
                    "* The obsidian tag unlocks Block 7.\n"
                    "* Block 7 stores the glass capsule.\n"
                    "* The glass capsule opens Bay 4.\n"
                    "* Bay 4 holds code 562.\n\n"
                    "Question: Which tag does Hira carry?\n\n"
                    "Answer using exactly this format:\n"
                    "ANSWER: <tag>"
                ),
                "score_type": "exact",
                "answer": "ANSWER: jade tag",
            },
            {
                "hop": "tag_block",
                "prompt": (
                    "Use only the facts below.\n\n"
                    "Facts:\n"
                    "* Hira carries the jade tag.\n"
                    "* The jade tag unlocks Block 5.\n"
                    "* Block 5 stores the copper capsule.\n"
                    "* The copper capsule opens Bay 9.\n"
                    "* Bay 9 holds code 248.\n"
                    "* Wren carries the pearl tag.\n"
                    "* The pearl tag unlocks Block 3.\n"
                    "* Block 3 stores the silver capsule.\n"
                    "* The silver capsule opens Bay 1.\n"
                    "* Bay 1 holds code 119.\n"
                    "* Oda carries the obsidian tag.\n"
                    "* The obsidian tag unlocks Block 7.\n"
                    "* Block 7 stores the glass capsule.\n"
                    "* The glass capsule opens Bay 4.\n"
                    "* Bay 4 holds code 562.\n\n"
                    "Question: Which block does the jade tag unlock?\n\n"
                    "Answer using exactly this format:\n"
                    "ANSWER: <block>"
                ),
                "score_type": "exact",
                "answer": "ANSWER: Block 5",
            },
            {
                "hop": "block_capsule",
                "prompt": (
                    "Use only the facts below.\n\n"
                    "Facts:\n"
                    "* Hira carries the jade tag.\n"
                    "* The jade tag unlocks Block 5.\n"
                    "* Block 5 stores the copper capsule.\n"
                    "* The copper capsule opens Bay 9.\n"
                    "* Bay 9 holds code 248.\n"
                    "* Wren carries the pearl tag.\n"
                    "* The pearl tag unlocks Block 3.\n"
                    "* Block 3 stores the silver capsule.\n"
                    "* The silver capsule opens Bay 1.\n"
                    "* Bay 1 holds code 119.\n"
                    "* Oda carries the obsidian tag.\n"
                    "* The obsidian tag unlocks Block 7.\n"
                    "* Block 7 stores the glass capsule.\n"
                    "* The glass capsule opens Bay 4.\n"
                    "* Bay 4 holds code 562.\n\n"
                    "Question: Which capsule does Block 5 store?\n\n"
                    "Answer using exactly this format:\n"
                    "ANSWER: <capsule>"
                ),
                "score_type": "exact",
                "answer": "ANSWER: copper capsule",
            },
            {
                "hop": "capsule_bay",
                "prompt": (
                    "Use only the facts below.\n\n"
                    "Facts:\n"
                    "* Hira carries the jade tag.\n"
                    "* The jade tag unlocks Block 5.\n"
                    "* Block 5 stores the copper capsule.\n"
                    "* The copper capsule opens Bay 9.\n"
                    "* Bay 9 holds code 248.\n"
                    "* Wren carries the pearl tag.\n"
                    "* The pearl tag unlocks Block 3.\n"
                    "* Block 3 stores the silver capsule.\n"
                    "* The silver capsule opens Bay 1.\n"
                    "* Bay 1 holds code 119.\n"
                    "* Oda carries the obsidian tag.\n"
                    "* The obsidian tag unlocks Block 7.\n"
                    "* Block 7 stores the glass capsule.\n"
                    "* The glass capsule opens Bay 4.\n"
                    "* Bay 4 holds code 562.\n\n"
                    "Question: Which bay does the copper capsule open?\n\n"
                    "Answer using exactly this format:\n"
                    "ANSWER: <bay>"
                ),
                "score_type": "exact",
                "answer": "ANSWER: Bay 9",
            },
            {
                "hop": "bay_code",
                "prompt": (
                    "Use only the facts below.\n\n"
                    "Facts:\n"
                    "* Hira carries the jade tag.\n"
                    "* The jade tag unlocks Block 5.\n"
                    "* Block 5 stores the copper capsule.\n"
                    "* The copper capsule opens Bay 9.\n"
                    "* Bay 9 holds code 248.\n"
                    "* Wren carries the pearl tag.\n"
                    "* The pearl tag unlocks Block 3.\n"
                    "* Block 3 stores the silver capsule.\n"
                    "* The silver capsule opens Bay 1.\n"
                    "* Bay 1 holds code 119.\n"
                    "* Oda carries the obsidian tag.\n"
                    "* The obsidian tag unlocks Block 7.\n"
                    "* Block 7 stores the glass capsule.\n"
                    "* The glass capsule opens Bay 4.\n"
                    "* Bay 4 holds code 562.\n\n"
                    "Question: Which code does Bay 9 hold?\n\n"
                    "Answer using exactly this format:\n"
                    "ANSWER: <code>"
                ),
                "score_type": "exact",
                "answer": "ANSWER: 248",
            },
        ],
    },

]
