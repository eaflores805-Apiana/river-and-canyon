"""
tasks_exp5.py — Experiment 5: Format-Cliff Replication / Prompt-Sensitivity Test

Locked before stability screen begins (2026-06-06). Do not edit after first screen run.

What changed vs. tasks_exp2.py / tasks_exp3.py:
  1. Format instruction: "Reply with exactly: ANSWER:" →
     "Respond using only this exact format with nothing before or after: ANSWER:"
  2. All space-containing intermediate values replaced with no-space ALL-CAPS tokens.
     Eliminates COMPOUND_NOUN_DROP as a possible failure class — every expected value
     is a single token, so any content failure is a genuine CONTENT_LOSS.

What did NOT change:
  - Chain structure, hop count, entity roles
  - Question phrasing (uses token names in place of space-containing names)
  - Terminal status/designation values (already ALL-CAPS single tokens)
  - Scorer (strict_format_score and content_slot_score, unchanged)

Families:
  FA1, FA2, FA3, FA4: 6-hop clean (no distractor)
  FB1, FB4: 6-hop + distractor + negation (same chains as FA1/FA4)
  FC1, FC4: 7-hop role-swap (two parallel chains)
  FD1, FD2, FD4: 5-7 hop, trap + distractor + negation
  AC1, AC2: atomic controls (1-hop)
  NC1: broad-broad negative control
"""

# Format instruction — locked per PREREGISTRATION-EXP5.md §4
_FMT = "Respond using only this exact format with nothing before or after: ANSWER:"


# ---------------------------------------------------------------------------
# FAMILY A — 6-hop clean
# Chain: Person → Token → Token → Token → Container → Item → Status
# No-space tokens throughout. Terminal = ALL-CAPS status.
# ---------------------------------------------------------------------------

_FA1_CTX = (
    "Mira holds CARD7. "
    "CARD7 unlocks GATEC. "
    "GATEC leads to ROOM4. "
    "ROOM4 contains AMBERBOX. "
    "AMBERBOX stores FILEK. "
    "FILEK has status APPROVED."
)

_FA2_CTX = (
    "Dex holds PASS4. "
    "PASS4 opens BAY9. "
    "BAY9 connects to SHELF2. "
    "SHELF2 holds JADEBLK. "
    "JADEBLK contains RECRD5. "
    "RECRD5 has status ACTIVE."
)

_FA3_CTX = (
    "Suki holds TAGA. "
    "TAGA grants access to SECTR7. "
    "SECTR7 contains CABN3. "
    "CABN3 stores SILVTRAY. "
    "SILVTRAY holds FORM6. "
    "FORM6 has status PENDING."
)

_FA4_CTX = (
    "Vance holds FOB12. "
    "FOB12 unlocks TUNNELB. "
    "TUNNELB leads to ALCOVE5. "
    "ALCOVE5 contains OBSDRAW. "
    "OBSDRAW stores LOG3. "
    "LOG3 has status CLEAR."
)

FA1 = {
    "id": "FA1",
    "narrow": {
        "prompt": (
            f"{_FA1_CTX}\n\n"
            f"Question: What status is associated with Mira?\n\n"
            f"{_FMT} <status>"
        ),
        "score_type": "exact",
        "answer": "ANSWER: APPROVED",
    },
    "broad": {
        "prompt": (
            f"{_FA1_CTX}\n\n"
            f"Question: What does AMBERBOX store?\n\n"
            f"{_FMT} <item>"
        ),
        "score_type": "exact",
        "answer": "ANSWER: FILEK",
    },
    "component_checks": [
        {
            "hop": "mira_card",
            "prompt": (
                f"{_FA1_CTX}\n\n"
                f"Question: Which card does Mira hold?\n\n"
                f"{_FMT} <card>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: CARD7",
        },
        {
            "hop": "card_gate",
            "prompt": (
                f"{_FA1_CTX}\n\n"
                f"Question: Which gate does CARD7 unlock?\n\n"
                f"{_FMT} <gate>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: GATEC",
        },
        {
            "hop": "gate_room",
            "prompt": (
                f"{_FA1_CTX}\n\n"
                f"Question: Which room does GATEC lead to?\n\n"
                f"{_FMT} <room>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: ROOM4",
        },
        {
            "hop": "room_box",
            "prompt": (
                f"{_FA1_CTX}\n\n"
                f"Question: What does ROOM4 contain?\n\n"
                f"{_FMT} <container>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: AMBERBOX",
        },
        {
            "hop": "box_file",
            "prompt": (
                f"{_FA1_CTX}\n\n"
                f"Question: What does AMBERBOX store?\n\n"
                f"{_FMT} <item>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: FILEK",
        },
        {
            "hop": "file_status",
            "prompt": (
                f"{_FA1_CTX}\n\n"
                f"Question: What status does FILEK have?\n\n"
                f"{_FMT} <status>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: APPROVED",
        },
    ],
}

FA2 = {
    "id": "FA2",
    "narrow": {
        "prompt": (
            f"{_FA2_CTX}\n\n"
            f"Question: What status is associated with Dex?\n\n"
            f"{_FMT} <status>"
        ),
        "score_type": "exact",
        "answer": "ANSWER: ACTIVE",
    },
    "broad": {
        "prompt": (
            f"{_FA2_CTX}\n\n"
            f"Question: What does JADEBLK contain?\n\n"
            f"{_FMT} <item>"
        ),
        "score_type": "exact",
        "answer": "ANSWER: RECRD5",
    },
    "component_checks": [
        {
            "hop": "dex_pass",
            "prompt": (
                f"{_FA2_CTX}\n\n"
                f"Question: Which pass does Dex hold?\n\n"
                f"{_FMT} <pass>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: PASS4",
        },
        {
            "hop": "pass_bay",
            "prompt": (
                f"{_FA2_CTX}\n\n"
                f"Question: Which bay does PASS4 open?\n\n"
                f"{_FMT} <bay>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: BAY9",
        },
        {
            "hop": "bay_shelf",
            "prompt": (
                f"{_FA2_CTX}\n\n"
                f"Question: Which shelf does BAY9 connect to?\n\n"
                f"{_FMT} <shelf>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: SHELF2",
        },
        {
            "hop": "shelf_block",
            "prompt": (
                f"{_FA2_CTX}\n\n"
                f"Question: What does SHELF2 hold?\n\n"
                f"{_FMT} <container>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: JADEBLK",
        },
        {
            "hop": "block_record",
            "prompt": (
                f"{_FA2_CTX}\n\n"
                f"Question: What does JADEBLK contain?\n\n"
                f"{_FMT} <item>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: RECRD5",
        },
        {
            "hop": "record_status",
            "prompt": (
                f"{_FA2_CTX}\n\n"
                f"Question: What status does RECRD5 have?\n\n"
                f"{_FMT} <status>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: ACTIVE",
        },
    ],
}

FA3 = {
    "id": "FA3",
    "narrow": {
        "prompt": (
            f"{_FA3_CTX}\n\n"
            f"Question: What status is associated with Suki?\n\n"
            f"{_FMT} <status>"
        ),
        "score_type": "exact",
        "answer": "ANSWER: PENDING",
    },
    "broad": {
        "prompt": (
            f"{_FA3_CTX}\n\n"
            f"Question: What does SILVTRAY hold?\n\n"
            f"{_FMT} <item>"
        ),
        "score_type": "exact",
        "answer": "ANSWER: FORM6",
    },
    "component_checks": [
        {
            "hop": "suki_tag",
            "prompt": (
                f"{_FA3_CTX}\n\n"
                f"Question: Which tag does Suki hold?\n\n"
                f"{_FMT} <tag>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: TAGA",
        },
        {
            "hop": "tag_sector",
            "prompt": (
                f"{_FA3_CTX}\n\n"
                f"Question: Which sector does TAGA grant access to?\n\n"
                f"{_FMT} <sector>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: SECTR7",
        },
        {
            "hop": "sector_cabinet",
            "prompt": (
                f"{_FA3_CTX}\n\n"
                f"Question: What does SECTR7 contain?\n\n"
                f"{_FMT} <cabinet>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: CABN3",
        },
        {
            "hop": "cabinet_tray",
            "prompt": (
                f"{_FA3_CTX}\n\n"
                f"Question: What does CABN3 store?\n\n"
                f"{_FMT} <container>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: SILVTRAY",
        },
        {
            "hop": "tray_form",
            "prompt": (
                f"{_FA3_CTX}\n\n"
                f"Question: What does SILVTRAY hold?\n\n"
                f"{_FMT} <item>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: FORM6",
        },
        {
            "hop": "form_status",
            "prompt": (
                f"{_FA3_CTX}\n\n"
                f"Question: What status does FORM6 have?\n\n"
                f"{_FMT} <status>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: PENDING",
        },
    ],
}

FA4 = {
    "id": "FA4",
    "narrow": {
        "prompt": (
            f"{_FA4_CTX}\n\n"
            f"Question: What status is associated with Vance?\n\n"
            f"{_FMT} <status>"
        ),
        "score_type": "exact",
        "answer": "ANSWER: CLEAR",
    },
    "broad": {
        "prompt": (
            f"{_FA4_CTX}\n\n"
            f"Question: What does OBSDRAW store?\n\n"
            f"{_FMT} <item>"
        ),
        "score_type": "exact",
        "answer": "ANSWER: LOG3",
    },
    "component_checks": [
        {
            "hop": "vance_fob",
            "prompt": (
                f"{_FA4_CTX}\n\n"
                f"Question: Which fob does Vance hold?\n\n"
                f"{_FMT} <fob>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: FOB12",
        },
        {
            "hop": "fob_tunnel",
            "prompt": (
                f"{_FA4_CTX}\n\n"
                f"Question: Which tunnel does FOB12 unlock?\n\n"
                f"{_FMT} <tunnel>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: TUNNELB",
        },
        {
            "hop": "tunnel_alcove",
            "prompt": (
                f"{_FA4_CTX}\n\n"
                f"Question: Which alcove does TUNNELB lead to?\n\n"
                f"{_FMT} <alcove>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: ALCOVE5",
        },
        {
            "hop": "alcove_drawer",
            "prompt": (
                f"{_FA4_CTX}\n\n"
                f"Question: What does ALCOVE5 contain?\n\n"
                f"{_FMT} <container>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: OBSDRAW",
        },
        {
            "hop": "drawer_log",
            "prompt": (
                f"{_FA4_CTX}\n\n"
                f"Question: What does OBSDRAW store?\n\n"
                f"{_FMT} <item>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: LOG3",
        },
        {
            "hop": "log_status",
            "prompt": (
                f"{_FA4_CTX}\n\n"
                f"Question: What status does LOG3 have?\n\n"
                f"{_FMT} <status>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: CLEAR",
        },
    ],
}


# ---------------------------------------------------------------------------
# FAMILY B — 6-hop + surface-similar distractor + negation
# Same chains as FA1 / FA4 with one distractor and one negation.
# ---------------------------------------------------------------------------

_FB1_CTX = (
    "Mira holds CARD7. "
    "CARD7 unlocks GATEC. "
    "GATEC leads to ROOM4. "
    "ROOM4 contains AMBERBOX. "
    "AMBERBOX stores FILEK. "
    "FILEK has status APPROVED. "
    "Note: Mira does NOT hold CARD3. "
    "CARD3 unlocks GATEA, which leads to ROOM9 — a separate pathway with no status chain."
)

_FB4_CTX = (
    "Vance holds FOB12. "
    "FOB12 unlocks TUNNELB. "
    "TUNNELB leads to ALCOVE5. "
    "ALCOVE5 contains OBSDRAW. "
    "OBSDRAW stores LOG3. "
    "LOG3 has status CLEAR. "
    "Note: Vance does NOT hold FOB2. "
    "FOB2 unlocks TUNNELF, which leads to ALCOVE1 — a separate pathway with no status chain."
)

FB1 = {
    "id": "FB1",
    "narrow": {
        "prompt": (
            f"{_FB1_CTX}\n\n"
            f"Question: What status is associated with Mira?\n\n"
            f"{_FMT} <status>"
        ),
        "score_type": "exact",
        "answer": "ANSWER: APPROVED",
    },
    "broad": {
        "prompt": (
            f"{_FB1_CTX}\n\n"
            f"Question: What does AMBERBOX store?\n\n"
            f"{_FMT} <item>"
        ),
        "score_type": "exact",
        "answer": "ANSWER: FILEK",
    },
    "component_checks": [
        {
            "hop": "mira_card",
            "prompt": (
                f"{_FB1_CTX}\n\n"
                f"Question: Which card does Mira hold?\n\n"
                f"{_FMT} <card>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: CARD7",
        },
        {
            "hop": "card_gate",
            "prompt": (
                f"{_FB1_CTX}\n\n"
                f"Question: Which gate does CARD7 unlock?\n\n"
                f"{_FMT} <gate>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: GATEC",
        },
        {
            "hop": "gate_room",
            "prompt": (
                f"{_FB1_CTX}\n\n"
                f"Question: Which room does GATEC lead to?\n\n"
                f"{_FMT} <room>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: ROOM4",
        },
        {
            "hop": "room_box",
            "prompt": (
                f"{_FB1_CTX}\n\n"
                f"Question: What does ROOM4 contain?\n\n"
                f"{_FMT} <container>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: AMBERBOX",
        },
        {
            "hop": "box_file",
            "prompt": (
                f"{_FB1_CTX}\n\n"
                f"Question: What does AMBERBOX store?\n\n"
                f"{_FMT} <item>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: FILEK",
        },
        {
            "hop": "file_status",
            "prompt": (
                f"{_FB1_CTX}\n\n"
                f"Question: What status does FILEK have?\n\n"
                f"{_FMT} <status>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: APPROVED",
        },
    ],
}

FB4 = {
    "id": "FB4",
    "narrow": {
        "prompt": (
            f"{_FB4_CTX}\n\n"
            f"Question: What status is associated with Vance?\n\n"
            f"{_FMT} <status>"
        ),
        "score_type": "exact",
        "answer": "ANSWER: CLEAR",
    },
    "broad": {
        "prompt": (
            f"{_FB4_CTX}\n\n"
            f"Question: What does OBSDRAW store?\n\n"
            f"{_FMT} <item>"
        ),
        "score_type": "exact",
        "answer": "ANSWER: LOG3",
    },
    "component_checks": [
        {
            "hop": "vance_fob",
            "prompt": (
                f"{_FB4_CTX}\n\n"
                f"Question: Which fob does Vance hold?\n\n"
                f"{_FMT} <fob>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: FOB12",
        },
        {
            "hop": "fob_tunnel",
            "prompt": (
                f"{_FB4_CTX}\n\n"
                f"Question: Which tunnel does FOB12 unlock?\n\n"
                f"{_FMT} <tunnel>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: TUNNELB",
        },
        {
            "hop": "tunnel_alcove",
            "prompt": (
                f"{_FB4_CTX}\n\n"
                f"Question: Which alcove does TUNNELB lead to?\n\n"
                f"{_FMT} <alcove>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: ALCOVE5",
        },
        {
            "hop": "alcove_drawer",
            "prompt": (
                f"{_FB4_CTX}\n\n"
                f"Question: What does ALCOVE5 contain?\n\n"
                f"{_FMT} <container>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: OBSDRAW",
        },
        {
            "hop": "drawer_log",
            "prompt": (
                f"{_FB4_CTX}\n\n"
                f"Question: What does OBSDRAW store?\n\n"
                f"{_FMT} <item>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: LOG3",
        },
        {
            "hop": "log_status",
            "prompt": (
                f"{_FB4_CTX}\n\n"
                f"Question: What status does LOG3 have?\n\n"
                f"{_FMT} <status>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: CLEAR",
        },
    ],
}


# ---------------------------------------------------------------------------
# FAMILY C — 7-hop role-swap (two parallel chains)
# Both chains fully specified. No compound-noun intermediates.
# vault3_token hop: was "silver token" (COMPOUND_NOUN_DROP in Exp3/4) → now SILVTOK.
# ---------------------------------------------------------------------------

_FC1_CTX = (
    "Nalo holds REDKEY. "
    "REDKEY opens VAULT3. "
    "VAULT3 holds SILVTOK. "
    "SILVTOK activates PANELB. "
    "PANELB controls DOOR6. "
    "DOOR6 leads to LABM. "
    "LABM has designation CYAN. "
    "Kira holds BLUEKEY. "
    "BLUEKEY opens VAULT7. "
    "VAULT7 holds COPPTOK. "
    "COPPTOK activates PANELD. "
    "PANELD controls DOOR2. "
    "DOOR2 leads to LABQ. "
    "LABQ has designation DELTA."
)

_FC4_CTX = (
    "Cael holds CRYSTDISC. "
    "CRYSTDISC fits SLOT6. "
    "SLOT6 opens CHAMBERA. "
    "CHAMBERA contains RUBYGEM. "
    "RUBYGEM sits on PED3. "
    "PED3 is inside UNIT9. "
    "UNIT9 has designation PRIME. "
    "Lyra holds OBSDISC. "
    "OBSDISC fits SLOT11. "
    "SLOT11 opens CHAMBERF. "
    "CHAMBERF contains SAPPHGEM. "
    "SAPPHGEM sits on PED7. "
    "PED7 is inside UNIT4. "
    "UNIT4 has designation FLARE."
)

FC1 = {
    "id": "FC1",
    "narrow": {
        "prompt": (
            f"{_FC1_CTX}\n\n"
            f"Question: What designation is associated with Nalo?\n\n"
            f"{_FMT} <designation>"
        ),
        "score_type": "exact",
        "answer": "ANSWER: CYAN",
    },
    "broad": {
        "prompt": (
            f"{_FC1_CTX}\n\n"
            f"Question: Which panel does SILVTOK activate?\n\n"
            f"{_FMT} <panel>"
        ),
        "score_type": "exact",
        "answer": "ANSWER: PANELB",
    },
    "component_checks": [
        {
            "hop": "nalo_key",
            "prompt": (
                f"{_FC1_CTX}\n\n"
                f"Question: Which key does Nalo hold?\n\n"
                f"{_FMT} <key>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: REDKEY",
        },
        {
            "hop": "red_key_vault",
            "prompt": (
                f"{_FC1_CTX}\n\n"
                f"Question: Which vault does REDKEY open?\n\n"
                f"{_FMT} <vault>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: VAULT3",
        },
        {
            "hop": "vault3_token",
            "prompt": (
                f"{_FC1_CTX}\n\n"
                f"Question: What does VAULT3 hold?\n\n"
                f"{_FMT} <token>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: SILVTOK",
        },
        {
            "hop": "silver_token_panel",
            "prompt": (
                f"{_FC1_CTX}\n\n"
                f"Question: Which panel does SILVTOK activate?\n\n"
                f"{_FMT} <panel>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: PANELB",
        },
        {
            "hop": "panelB_door",
            "prompt": (
                f"{_FC1_CTX}\n\n"
                f"Question: Which door does PANELB control?\n\n"
                f"{_FMT} <door>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: DOOR6",
        },
        {
            "hop": "door6_lab",
            "prompt": (
                f"{_FC1_CTX}\n\n"
                f"Question: Which lab does DOOR6 lead to?\n\n"
                f"{_FMT} <lab>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: LABM",
        },
        {
            "hop": "labM_designation",
            "prompt": (
                f"{_FC1_CTX}\n\n"
                f"Question: What designation does LABM have?\n\n"
                f"{_FMT} <designation>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: CYAN",
        },
        {
            "hop": "kira_key",
            "prompt": (
                f"{_FC1_CTX}\n\n"
                f"Question: Which key does Kira hold?\n\n"
                f"{_FMT} <key>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: BLUEKEY",
        },
        {
            "hop": "labQ_designation",
            "prompt": (
                f"{_FC1_CTX}\n\n"
                f"Question: What designation does LABQ have?\n\n"
                f"{_FMT} <designation>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: DELTA",
        },
    ],
}

FC4 = {
    "id": "FC4",
    "narrow": {
        "prompt": (
            f"{_FC4_CTX}\n\n"
            f"Question: What designation is associated with Cael?\n\n"
            f"{_FMT} <designation>"
        ),
        "score_type": "exact",
        "answer": "ANSWER: PRIME",
    },
    "broad": {
        "prompt": (
            f"{_FC4_CTX}\n\n"
            f"Question: What does CHAMBERA contain?\n\n"
            f"{_FMT} <item>"
        ),
        "score_type": "exact",
        "answer": "ANSWER: RUBYGEM",
    },
    "component_checks": [
        {
            "hop": "cael_disc",
            "prompt": (
                f"{_FC4_CTX}\n\n"
                f"Question: Which disc does Cael hold?\n\n"
                f"{_FMT} <disc>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: CRYSTDISC",
        },
        {
            "hop": "crystal_disc_slot",
            "prompt": (
                f"{_FC4_CTX}\n\n"
                f"Question: Which slot does CRYSTDISC fit?\n\n"
                f"{_FMT} <slot>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: SLOT6",
        },
        {
            "hop": "slot6_chamber",
            "prompt": (
                f"{_FC4_CTX}\n\n"
                f"Question: Which chamber does SLOT6 open?\n\n"
                f"{_FMT} <chamber>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: CHAMBERA",
        },
        {
            "hop": "chamberA_gem",
            "prompt": (
                f"{_FC4_CTX}\n\n"
                f"Question: What does CHAMBERA contain?\n\n"
                f"{_FMT} <gem>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: RUBYGEM",
        },
        {
            "hop": "ruby_gem_pedestal",
            "prompt": (
                f"{_FC4_CTX}\n\n"
                f"Question: Which pedestal does RUBYGEM sit on?\n\n"
                f"{_FMT} <pedestal>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: PED3",
        },
        {
            "hop": "pedestal3_unit",
            "prompt": (
                f"{_FC4_CTX}\n\n"
                f"Question: Which unit is PED3 inside?\n\n"
                f"{_FMT} <unit>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: UNIT9",
        },
        {
            "hop": "unit9_designation",
            "prompt": (
                f"{_FC4_CTX}\n\n"
                f"Question: What designation does UNIT9 have?\n\n"
                f"{_FMT} <designation>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: PRIME",
        },
        {
            "hop": "lyra_disc",
            "prompt": (
                f"{_FC4_CTX}\n\n"
                f"Question: Which disc does Lyra hold?\n\n"
                f"{_FMT} <disc>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: OBSDISC",
        },
        {
            "hop": "unit4_designation",
            "prompt": (
                f"{_FC4_CTX}\n\n"
                f"Question: What designation does UNIT4 have?\n\n"
                f"{_FMT} <designation>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: FLARE",
        },
    ],
}


# ---------------------------------------------------------------------------
# FAMILY D — intermediate-value trap + distractor + negation
# ---------------------------------------------------------------------------

_FD1_CTX = (
    "Hira is assigned to ROUTE12. "
    "ROUTE12 leads to DOCKF. "
    "DOCKF receives VOLCRATE. "
    "VOLCRATE belongs to TOOL9. "
    "TOOL9 is operated by TEAMDELTA. "
    "TEAMDELTA works at STATION3. "
    "STATION3 has priority URGENT. "
    "Note: Hira is NOT assigned to ROUTE21. "
    "ROUTE21 leads to DOCKB, which has priority ROUTINE. "
    "Note: DOCKF does NOT receive VOLCASE — it receives VOLCRATE."
)

_FD2_CTX = (
    "Sable is assigned to PROJ44. "
    "PROJ44 uses MOD7. "
    "MOD7 belongs to LABEPS. "
    "LABEPS is under DIV3. "
    "DIV3 has clearance CLEAN. "
    "Note: Sable is NOT assigned to PROJ11. "
    "PROJ11 uses MOD2, which is under a division with clearance TOXIC."
)

_FD4_CTX = (
    "Maya is assigned to PATH3. "
    "PATH3 connects to JUNCT9. "
    "JUNCT9 feeds SIGTOW1. "
    "SIGTOW1 emits on CHAN4. "
    "CHAN4 has alert level RED. "
    "Note: Maya is NOT assigned to PATH8. "
    "PATH8 connects to JUNCT2, whose channel has alert level BLUE."
)

FD1 = {
    "id": "FD1",
    "narrow": {
        "prompt": (
            f"{_FD1_CTX}\n\n"
            f"Question: What priority is associated with Hira?\n\n"
            f"{_FMT} <priority>"
        ),
        "score_type": "exact",
        "answer": "ANSWER: URGENT",
    },
    "broad": {
        "prompt": (
            f"{_FD1_CTX}\n\n"
            f"Question: Which team operates TOOL9?\n\n"
            f"{_FMT} <team>"
        ),
        "score_type": "exact",
        "answer": "ANSWER: TEAMDELTA",
    },
    "component_checks": [
        {
            "hop": "hira_route",
            "prompt": (
                f"{_FD1_CTX}\n\n"
                f"Question: Which route is Hira assigned to?\n\n"
                f"{_FMT} <route>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: ROUTE12",
        },
        {
            "hop": "route12_dock",
            "prompt": (
                f"{_FD1_CTX}\n\n"
                f"Question: Which dock does ROUTE12 lead to?\n\n"
                f"{_FMT} <dock>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: DOCKF",
        },
        {
            "hop": "dockF_crate",
            "prompt": (
                f"{_FD1_CTX}\n\n"
                f"Question: What does DOCKF receive?\n\n"
                f"{_FMT} <item>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: VOLCRATE",
        },
        {
            "hop": "crate_tool",
            "prompt": (
                f"{_FD1_CTX}\n\n"
                f"Question: Which tool does VOLCRATE belong to?\n\n"
                f"{_FMT} <tool>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: TOOL9",
        },
        {
            "hop": "tool9_team",
            "prompt": (
                f"{_FD1_CTX}\n\n"
                f"Question: Which team operates TOOL9?\n\n"
                f"{_FMT} <team>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: TEAMDELTA",
        },
        {
            "hop": "teamDelta_station",
            "prompt": (
                f"{_FD1_CTX}\n\n"
                f"Question: Where does TEAMDELTA work?\n\n"
                f"{_FMT} <station>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: STATION3",
        },
        {
            "hop": "station3_priority",
            "prompt": (
                f"{_FD1_CTX}\n\n"
                f"Question: What priority does STATION3 have?\n\n"
                f"{_FMT} <priority>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: URGENT",
        },
    ],
}

FD2 = {
    "id": "FD2",
    "narrow": {
        "prompt": (
            f"{_FD2_CTX}\n\n"
            f"Question: What clearance is associated with Sable?\n\n"
            f"{_FMT} <clearance>"
        ),
        "score_type": "exact",
        "answer": "ANSWER: CLEAN",
    },
    "broad": {
        "prompt": (
            f"{_FD2_CTX}\n\n"
            f"Question: Which lab does MOD7 belong to?\n\n"
            f"{_FMT} <lab>"
        ),
        "score_type": "exact",
        "answer": "ANSWER: LABEPS",
    },
    "component_checks": [
        {
            "hop": "sable_project",
            "prompt": (
                f"{_FD2_CTX}\n\n"
                f"Question: Which project is Sable assigned to?\n\n"
                f"{_FMT} <project>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: PROJ44",
        },
        {
            "hop": "project44_module",
            "prompt": (
                f"{_FD2_CTX}\n\n"
                f"Question: Which module does PROJ44 use?\n\n"
                f"{_FMT} <module>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: MOD7",
        },
        {
            "hop": "module7_lab",
            "prompt": (
                f"{_FD2_CTX}\n\n"
                f"Question: Which lab does MOD7 belong to?\n\n"
                f"{_FMT} <lab>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: LABEPS",
        },
        {
            "hop": "labEpsilon_division",
            "prompt": (
                f"{_FD2_CTX}\n\n"
                f"Question: Which division is LABEPS under?\n\n"
                f"{_FMT} <division>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: DIV3",
        },
        {
            "hop": "division3_clearance",
            "prompt": (
                f"{_FD2_CTX}\n\n"
                f"Question: What clearance does DIV3 have?\n\n"
                f"{_FMT} <clearance>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: CLEAN",
        },
    ],
}

FD4 = {
    "id": "FD4",
    "narrow": {
        "prompt": (
            f"{_FD4_CTX}\n\n"
            f"Question: What alert level is associated with Maya?\n\n"
            f"{_FMT} <alert level>"
        ),
        "score_type": "exact",
        "answer": "ANSWER: RED",
    },
    "broad": {
        "prompt": (
            f"{_FD4_CTX}\n\n"
            f"Question: Which junction does PATH3 connect to?\n\n"
            f"{_FMT} <junction>"
        ),
        "score_type": "exact",
        "answer": "ANSWER: JUNCT9",
    },
    "component_checks": [
        {
            "hop": "maya_path",
            "prompt": (
                f"{_FD4_CTX}\n\n"
                f"Question: Which path is Maya assigned to?\n\n"
                f"{_FMT} <path>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: PATH3",
        },
        {
            "hop": "path3_junction",
            "prompt": (
                f"{_FD4_CTX}\n\n"
                f"Question: Which junction does PATH3 connect to?\n\n"
                f"{_FMT} <junction>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: JUNCT9",
        },
        {
            "hop": "junction9_tower",
            "prompt": (
                f"{_FD4_CTX}\n\n"
                f"Question: Which signal tower does JUNCT9 feed?\n\n"
                f"{_FMT} <tower>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: SIGTOW1",
        },
        {
            "hop": "tower1_channel",
            "prompt": (
                f"{_FD4_CTX}\n\n"
                f"Question: Which channel does SIGTOW1 emit on?\n\n"
                f"{_FMT} <channel>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: CHAN4",
        },
        {
            "hop": "channel4_alert",
            "prompt": (
                f"{_FD4_CTX}\n\n"
                f"Question: What alert level does CHAN4 have?\n\n"
                f"{_FMT} <alert level>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: RED",
        },
    ],
}


# ---------------------------------------------------------------------------
# CONTROLS
# AC1: 1-hop atomic. "silver disk" → SILVDISK (was FORMAT_COMPLIANCE_LOSS in Exp4)
# AC2: 1-hop atomic. GOLD is already a clean single token.
# NC1: broad-broad. "current permits" → CURPERM, "old permits" → OLDPERM.
# ---------------------------------------------------------------------------

AC1 = {
    "id": "AC1",
    "narrow": {
        "prompt": (
            "The blue locker contains SILVDISK.\n\n"
            f"Question: What does the blue locker contain?\n\n"
            f"{_FMT} <item>"
        ),
        "score_type": "exact",
        "answer": "ANSWER: SILVDISK",
    },
    "broad": {
        "prompt": (
            "The blue locker contains SILVDISK.\n\n"
            f"Question: What does the blue locker contain?\n\n"
            f"{_FMT} <item>"
        ),
        "score_type": "exact",
        "answer": "ANSWER: SILVDISK",
    },
    "component_checks": [],
}

AC2 = {
    "id": "AC2",
    "narrow": {
        "prompt": (
            "Agent Tova holds clearance level GOLD.\n\n"
            f"Question: What clearance level does Agent Tova hold?\n\n"
            f"{_FMT} <clearance>"
        ),
        "score_type": "exact",
        "answer": "ANSWER: GOLD",
    },
    "broad": {
        "prompt": (
            "Agent Tova holds clearance level GOLD.\n\n"
            f"Question: What clearance level does Agent Tova hold?\n\n"
            f"{_FMT} <clearance>"
        ),
        "score_type": "exact",
        "answer": "ANSWER: GOLD",
    },
    "component_checks": [],
}

NC1 = {
    "id": "NC1",
    "narrow": {
        "prompt": (
            "The archive room holds three cabinets: red, green, and blue. "
            "The red cabinet contains OLDPERM. "
            "The green cabinet contains CURPERM. "
            "The blue cabinet contains EXPPERM.\n\n"
            f"Question: What does the green cabinet contain?\n\n"
            f"{_FMT} <item>"
        ),
        "score_type": "exact",
        "answer": "ANSWER: CURPERM",
    },
    "broad": {
        "prompt": (
            "The archive room holds three cabinets: red, green, and blue. "
            "The red cabinet contains OLDPERM. "
            "The green cabinet contains CURPERM. "
            "The blue cabinet contains EXPPERM.\n\n"
            f"Question: What does the red cabinet contain?\n\n"
            f"{_FMT} <item>"
        ),
        "score_type": "exact",
        "answer": "ANSWER: OLDPERM",
    },
    "component_checks": [],
}


# ---------------------------------------------------------------------------
# PAIRS — full set for stability screen
# ---------------------------------------------------------------------------

PAIRS = [
    FA1, FA2, FA3, FA4,
    FB1, FB4,
    FC1, FC4,
    FD1, FD2, FD4,
    AC1, AC2, NC1,
]
