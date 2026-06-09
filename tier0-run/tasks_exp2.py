"""
tasks_exp2.py — Experiment 2: Harder 7B Ladder

Locked before FP16 baseline screen (2026-06-06). Do not edit after first run.

Design principles:
- Terminal values are single ALL-CAPS tokens (avoids compound-noun calibration issue)
- All context is closed-world: every fact needed is in the prompt
- Component checks include the full relevant context (not just one sentence)
- FP16 eligibility screen required before INT8/INT4 sweep

Families:
  FA1-FA4: 6-hop clean (no distractor)
  FB1-FB4: 6-hop + surface-similar distractor + negation
  FC1-FC4: 7-hop role-swap (two parallel chains)
  FD1-FD4: intermediate-value trap + distractor + negation
  FE1-FE3: arithmetic/state dependency
  AC1, AC2: atomic controls (1-hop, broad only)
  NC1: broad-broad negative control
"""

# ---------------------------------------------------------------------------
# FAMILY A — 6-hop clean
# Chain: Person → Object → Location → Sub-location → Container → Item → Status
# No distractor. Terminal value = ALL-CAPS single token.
# ---------------------------------------------------------------------------

_FA1_CTX = (
    "Mira holds Card 7. "
    "Card 7 unlocks Gate C. "
    "Gate C leads to Room 4. "
    "Room 4 contains the amber box. "
    "The amber box stores File K. "
    "File K has status APPROVED."
)

_FA2_CTX = (
    "Dex holds Pass 4. "
    "Pass 4 opens Bay 9. "
    "Bay 9 connects to Shelf 2. "
    "Shelf 2 holds the jade block. "
    "The jade block contains Record 5. "
    "Record 5 has status ACTIVE."
)

_FA3_CTX = (
    "Suki holds Tag A. "
    "Tag A grants access to Sector 7. "
    "Sector 7 contains Cabinet 3. "
    "Cabinet 3 stores the silver tray. "
    "The silver tray holds Form 6. "
    "Form 6 has status PENDING."
)

_FA4_CTX = (
    "Vance holds Fob 12. "
    "Fob 12 unlocks Tunnel B. "
    "Tunnel B leads to Alcove 5. "
    "Alcove 5 contains the obsidian drawer. "
    "The obsidian drawer stores Log 3. "
    "Log 3 has status CLEAR."
)

FA1 = {
    "id": "FA1",
    "narrow": {
        "prompt": (
            f"{_FA1_CTX}\n\n"
            "Question: What status is associated with Mira?\n\n"
            "Reply with exactly: ANSWER: <status>"
        ),
        "score_type": "exact",
        "answer": "ANSWER: APPROVED",
    },
    "broad": {
        "prompt": (
            f"{_FA1_CTX}\n\n"
            "Question: What does the amber box store?\n\n"
            "Reply with exactly: ANSWER: <item>"
        ),
        "score_type": "exact",
        "answer": "ANSWER: File K",
    },
    "component_checks": [
        {
            "hop": "mira_card",
            "prompt": (
                f"{_FA1_CTX}\n\n"
                "Question: Which card does Mira hold?\n\n"
                "Reply with exactly: ANSWER: <card>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: Card 7",
        },
        {
            "hop": "card_gate",
            "prompt": (
                f"{_FA1_CTX}\n\n"
                "Question: Which gate does Card 7 unlock?\n\n"
                "Reply with exactly: ANSWER: <gate>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: Gate C",
        },
        {
            "hop": "gate_room",
            "prompt": (
                f"{_FA1_CTX}\n\n"
                "Question: Which room does Gate C lead to?\n\n"
                "Reply with exactly: ANSWER: <room>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: Room 4",
        },
        {
            "hop": "room_box",
            "prompt": (
                f"{_FA1_CTX}\n\n"
                "Question: What does Room 4 contain?\n\n"
                "Reply with exactly: ANSWER: <container>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: amber box",
        },
        {
            "hop": "box_file",
            "prompt": (
                f"{_FA1_CTX}\n\n"
                "Question: What does the amber box store?\n\n"
                "Reply with exactly: ANSWER: <item>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: File K",
        },
        {
            "hop": "file_status",
            "prompt": (
                f"{_FA1_CTX}\n\n"
                "Question: What status does File K have?\n\n"
                "Reply with exactly: ANSWER: <status>"
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
            "Question: What status is associated with Dex?\n\n"
            "Reply with exactly: ANSWER: <status>"
        ),
        "score_type": "exact",
        "answer": "ANSWER: ACTIVE",
    },
    "broad": {
        "prompt": (
            f"{_FA2_CTX}\n\n"
            "Question: What does the jade block contain?\n\n"
            "Reply with exactly: ANSWER: <item>"
        ),
        "score_type": "exact",
        "answer": "ANSWER: Record 5",
    },
    "component_checks": [
        {
            "hop": "dex_pass",
            "prompt": (
                f"{_FA2_CTX}\n\n"
                "Question: Which pass does Dex hold?\n\n"
                "Reply with exactly: ANSWER: <pass>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: Pass 4",
        },
        {
            "hop": "pass_bay",
            "prompt": (
                f"{_FA2_CTX}\n\n"
                "Question: Which bay does Pass 4 open?\n\n"
                "Reply with exactly: ANSWER: <bay>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: Bay 9",
        },
        {
            "hop": "bay_shelf",
            "prompt": (
                f"{_FA2_CTX}\n\n"
                "Question: Which shelf does Bay 9 connect to?\n\n"
                "Reply with exactly: ANSWER: <shelf>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: Shelf 2",
        },
        {
            "hop": "shelf_block",
            "prompt": (
                f"{_FA2_CTX}\n\n"
                "Question: What does Shelf 2 hold?\n\n"
                "Reply with exactly: ANSWER: <container>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: the jade block",
        },
        {
            "hop": "block_record",
            "prompt": (
                f"{_FA2_CTX}\n\n"
                "Question: What does the jade block contain?\n\n"
                "Reply with exactly: ANSWER: <item>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: Record 5",
        },
        {
            "hop": "record_status",
            "prompt": (
                f"{_FA2_CTX}\n\n"
                "Question: What status does Record 5 have?\n\n"
                "Reply with exactly: ANSWER: <status>"
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
            "Question: What status is associated with Suki?\n\n"
            "Reply with exactly: ANSWER: <status>"
        ),
        "score_type": "exact",
        "answer": "ANSWER: PENDING",
    },
    "broad": {
        "prompt": (
            f"{_FA3_CTX}\n\n"
            "Question: What does the silver tray hold?\n\n"
            "Reply with exactly: ANSWER: <item>"
        ),
        "score_type": "exact",
        "answer": "ANSWER: Form 6",
    },
    "component_checks": [
        {
            "hop": "suki_tag",
            "prompt": (
                f"{_FA3_CTX}\n\n"
                "Question: Which tag does Suki hold?\n\n"
                "Reply with exactly: ANSWER: <tag>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: Tag A",
        },
        {
            "hop": "tag_sector",
            "prompt": (
                f"{_FA3_CTX}\n\n"
                "Question: Which sector does Tag A grant access to?\n\n"
                "Reply with exactly: ANSWER: <sector>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: Sector 7",
        },
        {
            "hop": "sector_cabinet",
            "prompt": (
                f"{_FA3_CTX}\n\n"
                "Question: What does Sector 7 contain?\n\n"
                "Reply with exactly: ANSWER: <cabinet>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: Cabinet 3",
        },
        {
            "hop": "cabinet_tray",
            "prompt": (
                f"{_FA3_CTX}\n\n"
                "Question: What does Cabinet 3 store?\n\n"
                "Reply with exactly: ANSWER: <container>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: silver tray",
        },
        {
            "hop": "tray_form",
            "prompt": (
                f"{_FA3_CTX}\n\n"
                "Question: What does the silver tray hold?\n\n"
                "Reply with exactly: ANSWER: <item>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: Form 6",
        },
        {
            "hop": "form_status",
            "prompt": (
                f"{_FA3_CTX}\n\n"
                "Question: What status does Form 6 have?\n\n"
                "Reply with exactly: ANSWER: <status>"
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
            "Question: What status is associated with Vance?\n\n"
            "Reply with exactly: ANSWER: <status>"
        ),
        "score_type": "exact",
        "answer": "ANSWER: CLEAR",
    },
    "broad": {
        "prompt": (
            f"{_FA4_CTX}\n\n"
            "Question: What does the obsidian drawer store?\n\n"
            "Reply with exactly: ANSWER: <item>"
        ),
        "score_type": "exact",
        "answer": "ANSWER: Log 3",
    },
    "component_checks": [
        {
            "hop": "vance_fob",
            "prompt": (
                f"{_FA4_CTX}\n\n"
                "Question: Which fob does Vance hold?\n\n"
                "Reply with exactly: ANSWER: <fob>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: Fob 12",
        },
        {
            "hop": "fob_tunnel",
            "prompt": (
                f"{_FA4_CTX}\n\n"
                "Question: Which tunnel does Fob 12 unlock?\n\n"
                "Reply with exactly: ANSWER: <tunnel>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: Tunnel B",
        },
        {
            "hop": "tunnel_alcove",
            "prompt": (
                f"{_FA4_CTX}\n\n"
                "Question: Which alcove does Tunnel B lead to?\n\n"
                "Reply with exactly: ANSWER: <alcove>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: Alcove 5",
        },
        {
            "hop": "alcove_drawer",
            "prompt": (
                f"{_FA4_CTX}\n\n"
                "Question: What does Alcove 5 contain?\n\n"
                "Reply with exactly: ANSWER: <container>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: obsidian drawer",
        },
        {
            "hop": "drawer_log",
            "prompt": (
                f"{_FA4_CTX}\n\n"
                "Question: What does the obsidian drawer store?\n\n"
                "Reply with exactly: ANSWER: <item>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: Log 3",
        },
        {
            "hop": "log_status",
            "prompt": (
                f"{_FA4_CTX}\n\n"
                "Question: What status does Log 3 have?\n\n"
                "Reply with exactly: ANSWER: <status>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: CLEAR",
        },
    ],
}


# ---------------------------------------------------------------------------
# FAMILY B — 6-hop + surface-similar distractor + negation
# Same chain as Family A, with one distractor entity and one negation statement.
# ---------------------------------------------------------------------------

_FB1_CTX = (
    "Mira holds Card 7. "
    "Card 7 unlocks Gate C. "
    "Gate C leads to Room 4. "
    "Room 4 contains the amber box. "
    "The amber box stores File K. "
    "File K has status APPROVED. "
    "Note: Mira does NOT hold Card 3. "
    "Card 3 unlocks Gate A, which leads to Room 9 — a separate pathway with no status chain."
)

_FB2_CTX = (
    "Dex holds Pass 4. "
    "Pass 4 opens Bay 9. "
    "Bay 9 connects to Shelf 2. "
    "Shelf 2 holds the jade block. "
    "The jade block contains Record 5. "
    "Record 5 has status ACTIVE. "
    "Note: Dex does NOT hold Pass 14. "
    "Pass 14 opens Bay 6, which connects to Shelf 8 — a separate pathway with no status chain."
)

_FB3_CTX = (
    "Suki holds Tag A. "
    "Tag A grants access to Sector 7. "
    "Sector 7 contains Cabinet 3. "
    "Cabinet 3 stores the silver tray. "
    "The silver tray holds Form 6. "
    "Form 6 has status PENDING. "
    "Note: Suki does NOT hold Tag D. "
    "Tag D grants access to Sector 2, which contains Cabinet 9 — a separate pathway with no status chain."
)

_FB4_CTX = (
    "Vance holds Fob 12. "
    "Fob 12 unlocks Tunnel B. "
    "Tunnel B leads to Alcove 5. "
    "Alcove 5 contains the obsidian drawer. "
    "The obsidian drawer stores Log 3. "
    "Log 3 has status CLEAR. "
    "Note: Vance does NOT hold Fob 2. "
    "Fob 2 unlocks Tunnel F, which leads to Alcove 1 — a separate pathway with no status chain."
)

FB1 = {
    "id": "FB1",
    "narrow": {
        "prompt": (
            f"{_FB1_CTX}\n\n"
            "Question: What status is associated with Mira?\n\n"
            "Reply with exactly: ANSWER: <status>"
        ),
        "score_type": "exact",
        "answer": "ANSWER: APPROVED",
    },
    "broad": {
        "prompt": (
            f"{_FB1_CTX}\n\n"
            "Question: What does the amber box store?\n\n"
            "Reply with exactly: ANSWER: <item>"
        ),
        "score_type": "exact",
        "answer": "ANSWER: File K",
    },
    "component_checks": [
        {
            "hop": "mira_card",
            "prompt": (
                f"{_FB1_CTX}\n\n"
                "Question: Which card does Mira hold?\n\n"
                "Reply with exactly: ANSWER: <card>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: Card 7",
        },
        {
            "hop": "card_gate",
            "prompt": (
                f"{_FB1_CTX}\n\n"
                "Question: Which gate does Card 7 unlock?\n\n"
                "Reply with exactly: ANSWER: <gate>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: Gate C",
        },
        {
            "hop": "gate_room",
            "prompt": (
                f"{_FB1_CTX}\n\n"
                "Question: Which room does Gate C lead to?\n\n"
                "Reply with exactly: ANSWER: <room>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: Room 4",
        },
        {
            "hop": "room_box",
            "prompt": (
                f"{_FB1_CTX}\n\n"
                "Question: What does Room 4 contain?\n\n"
                "Reply with exactly: ANSWER: <container>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: amber box",
        },
        {
            "hop": "box_file",
            "prompt": (
                f"{_FB1_CTX}\n\n"
                "Question: What does the amber box store?\n\n"
                "Reply with exactly: ANSWER: <item>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: File K",
        },
        {
            "hop": "file_status",
            "prompt": (
                f"{_FB1_CTX}\n\n"
                "Question: What status does File K have?\n\n"
                "Reply with exactly: ANSWER: <status>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: APPROVED",
        },
    ],
}

FB2 = {
    "id": "FB2",
    "narrow": {
        "prompt": (
            f"{_FB2_CTX}\n\n"
            "Question: What status is associated with Dex?\n\n"
            "Reply with exactly: ANSWER: <status>"
        ),
        "score_type": "exact",
        "answer": "ANSWER: ACTIVE",
    },
    "broad": {
        "prompt": (
            f"{_FB2_CTX}\n\n"
            "Question: What does the jade block contain?\n\n"
            "Reply with exactly: ANSWER: <item>"
        ),
        "score_type": "exact",
        "answer": "ANSWER: Record 5",
    },
    "component_checks": [
        {
            "hop": "dex_pass",
            "prompt": (
                f"{_FB2_CTX}\n\n"
                "Question: Which pass does Dex hold?\n\n"
                "Reply with exactly: ANSWER: <pass>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: Pass 4",
        },
        {
            "hop": "pass_bay",
            "prompt": (
                f"{_FB2_CTX}\n\n"
                "Question: Which bay does Pass 4 open?\n\n"
                "Reply with exactly: ANSWER: <bay>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: Bay 9",
        },
        {
            "hop": "bay_shelf",
            "prompt": (
                f"{_FB2_CTX}\n\n"
                "Question: Which shelf does Bay 9 connect to?\n\n"
                "Reply with exactly: ANSWER: <shelf>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: Shelf 2",
        },
        {
            "hop": "shelf_block",
            "prompt": (
                f"{_FB2_CTX}\n\n"
                "Question: What does Shelf 2 hold?\n\n"
                "Reply with exactly: ANSWER: <container>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: the jade block",
        },
        {
            "hop": "block_record",
            "prompt": (
                f"{_FB2_CTX}\n\n"
                "Question: What does the jade block contain?\n\n"
                "Reply with exactly: ANSWER: <item>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: Record 5",
        },
        {
            "hop": "record_status",
            "prompt": (
                f"{_FB2_CTX}\n\n"
                "Question: What status does Record 5 have?\n\n"
                "Reply with exactly: ANSWER: <status>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: ACTIVE",
        },
    ],
}

FB3 = {
    "id": "FB3",
    "narrow": {
        "prompt": (
            f"{_FB3_CTX}\n\n"
            "Question: What status is associated with Suki?\n\n"
            "Reply with exactly: ANSWER: <status>"
        ),
        "score_type": "exact",
        "answer": "ANSWER: PENDING",
    },
    "broad": {
        "prompt": (
            f"{_FB3_CTX}\n\n"
            "Question: What does the silver tray hold?\n\n"
            "Reply with exactly: ANSWER: <item>"
        ),
        "score_type": "exact",
        "answer": "ANSWER: Form 6",
    },
    "component_checks": [
        {
            "hop": "suki_tag",
            "prompt": (
                f"{_FB3_CTX}\n\n"
                "Question: Which tag does Suki hold?\n\n"
                "Reply with exactly: ANSWER: <tag>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: Tag A",
        },
        {
            "hop": "tag_sector",
            "prompt": (
                f"{_FB3_CTX}\n\n"
                "Question: Which sector does Tag A grant access to?\n\n"
                "Reply with exactly: ANSWER: <sector>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: Sector 7",
        },
        {
            "hop": "sector_cabinet",
            "prompt": (
                f"{_FB3_CTX}\n\n"
                "Question: What does Sector 7 contain?\n\n"
                "Reply with exactly: ANSWER: <cabinet>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: Cabinet 3",
        },
        {
            "hop": "cabinet_tray",
            "prompt": (
                f"{_FB3_CTX}\n\n"
                "Question: What does Cabinet 3 store?\n\n"
                "Reply with exactly: ANSWER: <container>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: silver tray",
        },
        {
            "hop": "tray_form",
            "prompt": (
                f"{_FB3_CTX}\n\n"
                "Question: What does the silver tray hold?\n\n"
                "Reply with exactly: ANSWER: <item>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: Form 6",
        },
        {
            "hop": "form_status",
            "prompt": (
                f"{_FB3_CTX}\n\n"
                "Question: What status does Form 6 have?\n\n"
                "Reply with exactly: ANSWER: <status>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: PENDING",
        },
    ],
}

FB4 = {
    "id": "FB4",
    "narrow": {
        "prompt": (
            f"{_FB4_CTX}\n\n"
            "Question: What status is associated with Vance?\n\n"
            "Reply with exactly: ANSWER: <status>"
        ),
        "score_type": "exact",
        "answer": "ANSWER: CLEAR",
    },
    "broad": {
        "prompt": (
            f"{_FB4_CTX}\n\n"
            "Question: What does the obsidian drawer store?\n\n"
            "Reply with exactly: ANSWER: <item>"
        ),
        "score_type": "exact",
        "answer": "ANSWER: Log 3",
    },
    "component_checks": [
        {
            "hop": "vance_fob",
            "prompt": (
                f"{_FB4_CTX}\n\n"
                "Question: Which fob does Vance hold?\n\n"
                "Reply with exactly: ANSWER: <fob>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: Fob 12",
        },
        {
            "hop": "fob_tunnel",
            "prompt": (
                f"{_FB4_CTX}\n\n"
                "Question: Which tunnel does Fob 12 unlock?\n\n"
                "Reply with exactly: ANSWER: <tunnel>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: Tunnel B",
        },
        {
            "hop": "tunnel_alcove",
            "prompt": (
                f"{_FB4_CTX}\n\n"
                "Question: Which alcove does Tunnel B lead to?\n\n"
                "Reply with exactly: ANSWER: <alcove>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: Alcove 5",
        },
        {
            "hop": "alcove_drawer",
            "prompt": (
                f"{_FB4_CTX}\n\n"
                "Question: What does Alcove 5 contain?\n\n"
                "Reply with exactly: ANSWER: <container>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: obsidian drawer",
        },
        {
            "hop": "drawer_log",
            "prompt": (
                f"{_FB4_CTX}\n\n"
                "Question: What does the obsidian drawer store?\n\n"
                "Reply with exactly: ANSWER: <item>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: Log 3",
        },
        {
            "hop": "log_status",
            "prompt": (
                f"{_FB4_CTX}\n\n"
                "Question: What status does Log 3 have?\n\n"
                "Reply with exactly: ANSWER: <status>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: CLEAR",
        },
    ],
}


# ---------------------------------------------------------------------------
# FAMILY C — 7-hop role-swap (two parallel chains in the same context)
# Both chains fully specified. Narrow: one person's terminal value.
# Broad: a mid-chain fact from the same person's chain.
# Components verify individual hops from both chains.
# ---------------------------------------------------------------------------

_FC1_CTX = (
    "Nalo holds the red key. "
    "The red key opens Vault 3. "
    "Vault 3 holds the silver token. "
    "The silver token activates Panel B. "
    "Panel B controls Door 6. "
    "Door 6 leads to Lab M. "
    "Lab M has designation CYAN. "
    "Kira holds the blue key. "
    "The blue key opens Vault 7. "
    "Vault 7 holds the copper token. "
    "The copper token activates Panel D. "
    "Panel D controls Door 2. "
    "Door 2 leads to Lab Q. "
    "Lab Q has designation DELTA."
)

_FC2_CTX = (
    "Zara holds the bronze tag. "
    "The bronze tag grants access to Hub 5. "
    "Hub 5 connects to Zone 2. "
    "Zone 2 contains the alpha module. "
    "The alpha module links to Post J. "
    "Post J routes to Bay R. "
    "Bay R has designation NOVA. "
    "Pell holds the iron tag. "
    "The iron tag grants access to Hub 9. "
    "Hub 9 connects to Zone 6. "
    "Zone 6 contains the beta module. "
    "The beta module links to Post V. "
    "Post V routes to Bay W. "
    "Bay W has designation OMEGA."
)

_FC3_CTX = (
    "Tomas holds the amber pass. "
    "The amber pass unlocks Lock 4. "
    "Lock 4 opens Corridor 7. "
    "Corridor 7 leads to Room 9. "
    "Room 9 contains the white chest. "
    "The white chest holds File M. "
    "File M has designation IRON. "
    "Revi holds the jade pass. "
    "The jade pass unlocks Lock 8. "
    "Lock 8 opens Corridor 2. "
    "Corridor 2 leads to Room 3. "
    "Room 3 contains the black chest. "
    "The black chest holds File T. "
    "File T has designation COPPER."
)

_FC4_CTX = (
    "Cael holds the crystal disc. "
    "The crystal disc fits Slot 6. "
    "Slot 6 opens Chamber A. "
    "Chamber A contains the ruby gem. "
    "The ruby gem sits on Pedestal 3. "
    "Pedestal 3 is inside Unit 9. "
    "Unit 9 has designation PRIME. "
    "Lyra holds the obsidian disc. "
    "The obsidian disc fits Slot 11. "
    "Slot 11 opens Chamber F. "
    "Chamber F contains the sapphire gem. "
    "The sapphire gem sits on Pedestal 7. "
    "Pedestal 7 is inside Unit 4. "
    "Unit 4 has designation FLARE."
)

FC1 = {
    "id": "FC1",
    "narrow": {
        "prompt": (
            f"{_FC1_CTX}\n\n"
            "Question: What designation is associated with Nalo?\n\n"
            "Reply with exactly: ANSWER: <designation>"
        ),
        "score_type": "exact",
        "answer": "ANSWER: CYAN",
    },
    "broad": {
        "prompt": (
            f"{_FC1_CTX}\n\n"
            "Question: Which panel does the silver token activate?\n\n"
            "Reply with exactly: ANSWER: <panel>"
        ),
        "score_type": "exact",
        "answer": "ANSWER: Panel B",
    },
    "component_checks": [
        {
            "hop": "nalo_key",
            "prompt": (
                f"{_FC1_CTX}\n\n"
                "Question: Which key does Nalo hold?\n\n"
                "Reply with exactly: ANSWER: <key>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: red",
        },
        {
            "hop": "red_key_vault",
            "prompt": (
                f"{_FC1_CTX}\n\n"
                "Question: Which vault does the red key open?\n\n"
                "Reply with exactly: ANSWER: <vault>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: Vault 3",
        },
        {
            "hop": "vault3_token",
            "prompt": (
                f"{_FC1_CTX}\n\n"
                "Question: What does Vault 3 hold?\n\n"
                "Reply with exactly: ANSWER: <token>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: silver token",
        },
        {
            "hop": "silver_token_panel",
            "prompt": (
                f"{_FC1_CTX}\n\n"
                "Question: Which panel does the silver token activate?\n\n"
                "Reply with exactly: ANSWER: <panel>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: Panel B",
        },
        {
            "hop": "panelB_door",
            "prompt": (
                f"{_FC1_CTX}\n\n"
                "Question: Which door does Panel B control?\n\n"
                "Reply with exactly: ANSWER: <door>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: Door 6",
        },
        {
            "hop": "door6_lab",
            "prompt": (
                f"{_FC1_CTX}\n\n"
                "Question: Which lab does Door 6 lead to?\n\n"
                "Reply with exactly: ANSWER: <lab>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: Lab M",
        },
        {
            "hop": "labM_designation",
            "prompt": (
                f"{_FC1_CTX}\n\n"
                "Question: What designation does Lab M have?\n\n"
                "Reply with exactly: ANSWER: <designation>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: CYAN",
        },
        {
            "hop": "kira_key",
            "prompt": (
                f"{_FC1_CTX}\n\n"
                "Question: Which key does Kira hold?\n\n"
                "Reply with exactly: ANSWER: <key>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: blue",
        },
        {
            "hop": "labQ_designation",
            "prompt": (
                f"{_FC1_CTX}\n\n"
                "Question: What designation does Lab Q have?\n\n"
                "Reply with exactly: ANSWER: <designation>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: DELTA",
        },
    ],
}

FC2 = {
    "id": "FC2",
    "narrow": {
        "prompt": (
            f"{_FC2_CTX}\n\n"
            "Question: What designation is associated with Zara?\n\n"
            "Reply with exactly: ANSWER: <designation>"
        ),
        "score_type": "exact",
        "answer": "ANSWER: NOVA",
    },
    "broad": {
        "prompt": (
            f"{_FC2_CTX}\n\n"
            "Question: Which zone does Hub 5 connect to?\n\n"
            "Reply with exactly: ANSWER: <zone>"
        ),
        "score_type": "exact",
        "answer": "ANSWER: Zone 2",
    },
    "component_checks": [
        {
            "hop": "zara_tag",
            "prompt": (
                f"{_FC2_CTX}\n\n"
                "Question: Which tag does Zara hold?\n\n"
                "Reply with exactly: ANSWER: <tag>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: bronze",
        },
        {
            "hop": "bronze_tag_hub",
            "prompt": (
                f"{_FC2_CTX}\n\n"
                "Question: Which hub does the bronze tag grant access to?\n\n"
                "Reply with exactly: ANSWER: <hub>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: Hub 5",
        },
        {
            "hop": "hub5_zone",
            "prompt": (
                f"{_FC2_CTX}\n\n"
                "Question: Which zone does Hub 5 connect to?\n\n"
                "Reply with exactly: ANSWER: <zone>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: Zone 2",
        },
        {
            "hop": "zone2_module",
            "prompt": (
                f"{_FC2_CTX}\n\n"
                "Question: What does Zone 2 contain?\n\n"
                "Reply with exactly: ANSWER: <module>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: alpha module",
        },
        {
            "hop": "alpha_module_post",
            "prompt": (
                f"{_FC2_CTX}\n\n"
                "Question: Which post does the alpha module link to?\n\n"
                "Reply with exactly: ANSWER: <post>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: Post J",
        },
        {
            "hop": "postJ_bay",
            "prompt": (
                f"{_FC2_CTX}\n\n"
                "Question: Which bay does Post J route to?\n\n"
                "Reply with exactly: ANSWER: <bay>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: Bay R",
        },
        {
            "hop": "bayR_designation",
            "prompt": (
                f"{_FC2_CTX}\n\n"
                "Question: What designation does Bay R have?\n\n"
                "Reply with exactly: ANSWER: <designation>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: NOVA",
        },
        {
            "hop": "pell_tag",
            "prompt": (
                f"{_FC2_CTX}\n\n"
                "Question: Which tag does Pell hold?\n\n"
                "Reply with exactly: ANSWER: <tag>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: iron",
        },
        {
            "hop": "bayW_designation",
            "prompt": (
                f"{_FC2_CTX}\n\n"
                "Question: What designation does Bay W have?\n\n"
                "Reply with exactly: ANSWER: <designation>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: OMEGA",
        },
    ],
}

FC3 = {
    "id": "FC3",
    "narrow": {
        "prompt": (
            f"{_FC3_CTX}\n\n"
            "Question: What designation is associated with Tomas?\n\n"
            "Reply with exactly: ANSWER: <designation>"
        ),
        "score_type": "exact",
        "answer": "ANSWER: IRON",
    },
    "broad": {
        "prompt": (
            f"{_FC3_CTX}\n\n"
            "Question: What does Room 9 contain?\n\n"
            "Reply with exactly: ANSWER: <container>"
        ),
        "score_type": "exact",
        "answer": "ANSWER: white chest",
    },
    "component_checks": [
        {
            "hop": "tomas_pass",
            "prompt": (
                f"{_FC3_CTX}\n\n"
                "Question: Which pass does Tomas hold?\n\n"
                "Reply with exactly: ANSWER: <pass>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: amber pass",
        },
        {
            "hop": "amber_pass_lock",
            "prompt": (
                f"{_FC3_CTX}\n\n"
                "Question: Which lock does the amber pass unlock?\n\n"
                "Reply with exactly: ANSWER: <lock>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: Lock 4",
        },
        {
            "hop": "lock4_corridor",
            "prompt": (
                f"{_FC3_CTX}\n\n"
                "Question: Which corridor does Lock 4 open?\n\n"
                "Reply with exactly: ANSWER: <corridor>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: Corridor 7",
        },
        {
            "hop": "corridor7_room",
            "prompt": (
                f"{_FC3_CTX}\n\n"
                "Question: Which room does Corridor 7 lead to?\n\n"
                "Reply with exactly: ANSWER: <room>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: Room 9",
        },
        {
            "hop": "room9_chest",
            "prompt": (
                f"{_FC3_CTX}\n\n"
                "Question: What does Room 9 contain?\n\n"
                "Reply with exactly: ANSWER: <container>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: white chest",
        },
        {
            "hop": "white_chest_file",
            "prompt": (
                f"{_FC3_CTX}\n\n"
                "Question: What does the white chest hold?\n\n"
                "Reply with exactly: ANSWER: <file>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: File M",
        },
        {
            "hop": "fileM_designation",
            "prompt": (
                f"{_FC3_CTX}\n\n"
                "Question: What designation does File M have?\n\n"
                "Reply with exactly: ANSWER: <designation>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: IRON",
        },
        {
            "hop": "revi_pass",
            "prompt": (
                f"{_FC3_CTX}\n\n"
                "Question: Which pass does Revi hold?\n\n"
                "Reply with exactly: ANSWER: <pass>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: jade pass",
        },
        {
            "hop": "fileT_designation",
            "prompt": (
                f"{_FC3_CTX}\n\n"
                "Question: What designation does File T have?\n\n"
                "Reply with exactly: ANSWER: <designation>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: COPPER",
        },
    ],
}

FC4 = {
    "id": "FC4",
    "narrow": {
        "prompt": (
            f"{_FC4_CTX}\n\n"
            "Question: What designation is associated with Cael?\n\n"
            "Reply with exactly: ANSWER: <designation>"
        ),
        "score_type": "exact",
        "answer": "ANSWER: PRIME",
    },
    "broad": {
        "prompt": (
            f"{_FC4_CTX}\n\n"
            "Question: What does Chamber A contain?\n\n"
            "Reply with exactly: ANSWER: <item>"
        ),
        "score_type": "exact",
        "answer": "ANSWER: ruby gem",
    },
    "component_checks": [
        {
            "hop": "cael_disc",
            "prompt": (
                f"{_FC4_CTX}\n\n"
                "Question: Which disc does Cael hold?\n\n"
                "Reply with exactly: ANSWER: <disc>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: crystal",
        },
        {
            "hop": "crystal_disc_slot",
            "prompt": (
                f"{_FC4_CTX}\n\n"
                "Question: Which slot does the crystal disc fit?\n\n"
                "Reply with exactly: ANSWER: <slot>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: Slot 6",
        },
        {
            "hop": "slot6_chamber",
            "prompt": (
                f"{_FC4_CTX}\n\n"
                "Question: Which chamber does Slot 6 open?\n\n"
                "Reply with exactly: ANSWER: <chamber>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: Chamber A",
        },
        {
            "hop": "chamberA_gem",
            "prompt": (
                f"{_FC4_CTX}\n\n"
                "Question: What does Chamber A contain?\n\n"
                "Reply with exactly: ANSWER: <gem>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: ruby",
        },
        {
            "hop": "ruby_gem_pedestal",
            "prompt": (
                f"{_FC4_CTX}\n\n"
                "Question: Which pedestal does the ruby gem sit on?\n\n"
                "Reply with exactly: ANSWER: <pedestal>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: Pedestal 3",
        },
        {
            "hop": "pedestal3_unit",
            "prompt": (
                f"{_FC4_CTX}\n\n"
                "Question: Pedestal 3 is located inside Unit ___ (fill in the number).\n\n"
                "Reply with exactly: ANSWER: <number>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: 9",
        },
        {
            "hop": "unit9_designation",
            "prompt": (
                f"{_FC4_CTX}\n\n"
                "Question: What designation does Unit 9 have?\n\n"
                "Reply with exactly: ANSWER: <designation>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: PRIME",
        },
        {
            "hop": "lyra_disc",
            "prompt": (
                f"{_FC4_CTX}\n\n"
                "Question: Which disc does Lyra hold?\n\n"
                "Reply with exactly: ANSWER: <disc>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: obsidian",
        },
        {
            "hop": "unit4_designation",
            "prompt": (
                f"{_FC4_CTX}\n\n"
                "Question: What designation does Unit 4 have?\n\n"
                "Reply with exactly: ANSWER: <designation>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: FLARE",
        },
    ],
}


# ---------------------------------------------------------------------------
# FAMILY D — intermediate-value trap + distractor + negation
# Contains a plausible wrong answer reachable from partial traversal.
# Negation rules out the trap. Tests whether trap disrupts composite more
# than component retention.
# ---------------------------------------------------------------------------

_FD1_CTX = (
    "Hira is assigned to Route 12. "
    "Route 12 leads to Dock F. "
    "Dock F receives the violet crate. "
    "The violet crate belongs to Tool 9. "
    "Tool 9 is operated by Team Delta. "
    "Team Delta works at Station 3. "
    "Station 3 has priority URGENT. "
    "Note: Hira is NOT assigned to Route 21. "
    "Route 21 leads to Dock B, which has priority ROUTINE. "
    "Note: Dock F does NOT receive the violet case — it receives the violet crate."
)

_FD2_CTX = (
    "Sable is assigned to Project 44. "
    "Project 44 uses Module 7. "
    "Module 7 belongs to Lab Epsilon. "
    "Lab Epsilon is under Division 3. "
    "Division 3 has clearance CLEAN. "
    "Note: Sable is NOT assigned to Project 11. "
    "Project 11 uses Module 2, which is under a division with clearance TOXIC."
)

_FD3_CTX = (
    "Venn is assigned to Line 5. "
    "Line 5 feeds into Node K. "
    "Node K controls Switch 2. "
    "Switch 2 governs Circuit 8. "
    "Circuit 8 has status ON. "
    "Note: Venn is NOT assigned to Line 6. "
    "Line 6 feeds into Node P, whose circuit has status OFF."
)

_FD4_CTX = (
    "Maya is assigned to Path 3. "
    "Path 3 connects to Junction 9. "
    "Junction 9 feeds Signal Tower 1. "
    "Signal Tower 1 emits on Channel 4. "
    "Channel 4 has alert level RED. "
    "Note: Maya is NOT assigned to Path 8. "
    "Path 8 connects to Junction 2, whose channel has alert level BLUE."
)

FD1 = {
    "id": "FD1",
    "narrow": {
        "prompt": (
            f"{_FD1_CTX}\n\n"
            "Question: What priority is associated with Hira?\n\n"
            "Reply with exactly: ANSWER: <priority>"
        ),
        "score_type": "exact",
        "answer": "ANSWER: URGENT",
    },
    "broad": {
        "prompt": (
            f"{_FD1_CTX}\n\n"
            "Question: Which team operates Tool 9?\n\n"
            "Reply with exactly: ANSWER: <team>"
        ),
        "score_type": "exact",
        "answer": "ANSWER: Team Delta",
    },
    "component_checks": [
        {
            "hop": "hira_route",
            "prompt": (
                f"{_FD1_CTX}\n\n"
                "Question: Which route is Hira assigned to?\n\n"
                "Reply with exactly: ANSWER: <route>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: Route 12",
        },
        {
            "hop": "route12_dock",
            "prompt": (
                f"{_FD1_CTX}\n\n"
                "Question: Which dock does Route 12 lead to?\n\n"
                "Reply with exactly: ANSWER: <dock>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: Dock F",
        },
        {
            "hop": "dockF_crate",
            "prompt": (
                f"{_FD1_CTX}\n\n"
                "Question: What does Dock F receive?\n\n"
                "Reply with exactly: ANSWER: <crate>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: crate",
        },
        {
            "hop": "crate_tool",
            "prompt": (
                f"{_FD1_CTX}\n\n"
                "Question: Which tool does the violet crate belong to?\n\n"
                "Reply with exactly: ANSWER: <tool>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: Tool 9",
        },
        {
            "hop": "tool9_team",
            "prompt": (
                f"{_FD1_CTX}\n\n"
                "Question: Which team operates Tool 9?\n\n"
                "Reply with exactly: ANSWER: <team>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: Team Delta",
        },
        {
            "hop": "teamDelta_station",
            "prompt": (
                f"{_FD1_CTX}\n\n"
                "Question: Where does Team Delta work?\n\n"
                "Reply with exactly: ANSWER: <station>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: Station 3",
        },
        {
            "hop": "station3_priority",
            "prompt": (
                f"{_FD1_CTX}\n\n"
                "Question: What priority does Station 3 have?\n\n"
                "Reply with exactly: ANSWER: <priority>"
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
            "Question: What clearance is associated with Sable?\n\n"
            "Reply with exactly: ANSWER: <clearance>"
        ),
        "score_type": "exact",
        "answer": "ANSWER: CLEAN",
    },
    "broad": {
        "prompt": (
            f"{_FD2_CTX}\n\n"
            "Question: Which lab does Module 7 belong to?\n\n"
            "Reply with exactly: ANSWER: <lab>"
        ),
        "score_type": "exact",
        "answer": "ANSWER: Lab Epsilon",
    },
    "component_checks": [
        {
            "hop": "sable_project",
            "prompt": (
                f"{_FD2_CTX}\n\n"
                "Question: Which project is Sable assigned to?\n\n"
                "Reply with exactly: ANSWER: <project>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: Project 44",
        },
        {
            "hop": "project44_module",
            "prompt": (
                f"{_FD2_CTX}\n\n"
                "Question: Which module does Project 44 use?\n\n"
                "Reply with exactly: ANSWER: <module>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: Module 7",
        },
        {
            "hop": "module7_lab",
            "prompt": (
                f"{_FD2_CTX}\n\n"
                "Question: Which lab does Module 7 belong to?\n\n"
                "Reply with exactly: ANSWER: <lab>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: Lab Epsilon",
        },
        {
            "hop": "labEpsilon_division",
            "prompt": (
                f"{_FD2_CTX}\n\n"
                "Question: Which division is Lab Epsilon under?\n\n"
                "Reply with exactly: ANSWER: <division>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: Division 3",
        },
        {
            "hop": "division3_clearance",
            "prompt": (
                f"{_FD2_CTX}\n\n"
                "Question: What clearance does Division 3 have?\n\n"
                "Reply with exactly: ANSWER: <clearance>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: CLEAN",
        },
    ],
}

FD3 = {
    "id": "FD3",
    "narrow": {
        "prompt": (
            f"{_FD3_CTX}\n\n"
            "Question: What status is associated with Venn?\n\n"
            "Reply with exactly: ANSWER: <status>"
        ),
        "score_type": "exact",
        "answer": "ANSWER: ON",
    },
    "broad": {
        "prompt": (
            f"{_FD3_CTX}\n\n"
            "Question: Which switch does Node K control?\n\n"
            "Reply with exactly: ANSWER: <switch>"
        ),
        "score_type": "exact",
        "answer": "ANSWER: Switch 2",
    },
    "component_checks": [
        {
            "hop": "venn_line",
            "prompt": (
                f"{_FD3_CTX}\n\n"
                "Question: Which line is Venn assigned to?\n\n"
                "Reply with exactly: ANSWER: <line>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: Line 5",
        },
        {
            "hop": "line5_node",
            "prompt": (
                f"{_FD3_CTX}\n\n"
                "Question: Which node does Line 5 feed into?\n\n"
                "Reply with exactly: ANSWER: <node>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: Node K",
        },
        {
            "hop": "nodeK_switch",
            "prompt": (
                f"{_FD3_CTX}\n\n"
                "Question: Which switch does Node K control?\n\n"
                "Reply with exactly: ANSWER: <switch>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: Switch 2",
        },
        {
            "hop": "switch2_circuit",
            "prompt": (
                f"{_FD3_CTX}\n\n"
                "Question: Which circuit does Switch 2 govern?\n\n"
                "Reply with exactly: ANSWER: <circuit>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: Circuit 8",
        },
        {
            "hop": "circuit8_status",
            "prompt": (
                f"{_FD3_CTX}\n\n"
                "Question: What status does Circuit 8 have?\n\n"
                "Reply with exactly: ANSWER: <status>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: ON",
        },
    ],
}

FD4 = {
    "id": "FD4",
    "narrow": {
        "prompt": (
            f"{_FD4_CTX}\n\n"
            "Question: What alert level is associated with Maya?\n\n"
            "Reply with exactly: ANSWER: <alert level>"
        ),
        "score_type": "exact",
        "answer": "ANSWER: RED",
    },
    "broad": {
        "prompt": (
            f"{_FD4_CTX}\n\n"
            "Question: Which junction does Path 3 connect to?\n\n"
            "Reply with exactly: ANSWER: <junction>"
        ),
        "score_type": "exact",
        "answer": "ANSWER: Junction 9",
    },
    "component_checks": [
        {
            "hop": "maya_path",
            "prompt": (
                f"{_FD4_CTX}\n\n"
                "Question: Which path is Maya assigned to?\n\n"
                "Reply with exactly: ANSWER: <path>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: Path 3",
        },
        {
            "hop": "path3_junction",
            "prompt": (
                f"{_FD4_CTX}\n\n"
                "Question: Which junction does Path 3 connect to?\n\n"
                "Reply with exactly: ANSWER: <junction>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: Junction 9",
        },
        {
            "hop": "junction9_tower",
            "prompt": (
                f"{_FD4_CTX}\n\n"
                "Question: Which signal tower does Junction 9 feed?\n\n"
                "Reply with exactly: ANSWER: <tower>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: Signal Tower 1",
        },
        {
            "hop": "tower1_channel",
            "prompt": (
                f"{_FD4_CTX}\n\n"
                "Question: Which channel does Signal Tower 1 emit on?\n\n"
                "Reply with exactly: ANSWER: <channel>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: Channel 4",
        },
        {
            "hop": "channel4_alert",
            "prompt": (
                f"{_FD4_CTX}\n\n"
                "Question: What alert level does Channel 4 have?\n\n"
                "Reply with exactly: ANSWER: <alert level>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: RED",
        },
    ],
}


# ---------------------------------------------------------------------------
# FAMILY E — arithmetic/state dependency
# Intermediate values must be computed and reused. Narrow: final result.
# Broad: an intermediate value. Component checks provide full context,
# ask single-step arithmetic questions.
# ---------------------------------------------------------------------------

_FE1_CTX = (
    "A shipment contains 14 standard parts and 9 bonus parts. "
    "Each part requires 4 screws. "
    "The warehouse already has 12 screws in stock. "
    "Screws are sold in packets of 10."
)

_FE2_CTX = (
    "A rack has 3 rows, each row has 5 slots. "
    "A second rack needs 11 rows with 2 slots each. "
    "The combined slots from both racks must be filled."
)

_FE3_CTX = (
    "A team has 4 sub-groups, each with 6 members. "
    "Each member must carry 3 tools. "
    "The warehouse currently holds 25 tools."
)

FE1 = {
    "id": "FE1",
    "narrow": {
        "prompt": (
            f"{_FE1_CTX}\n\n"
            "Question: How many packets of screws must be ordered "
            "(round up to whole packets)?\n\n"
            "Reply with exactly: ANSWER: <number>"
        ),
        "score_type": "exact",
        "answer": "ANSWER: 8",
    },
    "broad": {
        "prompt": (
            f"{_FE1_CTX}\n\n"
            "Question: How many total parts are in the shipment?\n\n"
            "Reply with exactly: ANSWER: <number>"
        ),
        "score_type": "exact",
        "answer": "ANSWER: 23",
    },
    "component_checks": [
        {
            "hop": "total_parts",
            "prompt": (
                f"{_FE1_CTX}\n\n"
                "Question: What is 14 plus 9?\n\n"
                "Reply with exactly: ANSWER: <number>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: 23",
        },
        {
            "hop": "total_screws_needed",
            "prompt": (
                f"{_FE1_CTX}\n\n"
                "Question: If there are 23 total parts and each requires 4 screws, "
                "how many screws are needed in total?\n\n"
                "Reply with exactly: ANSWER: <number>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: 92",
        },
        {
            "hop": "screws_to_order",
            "prompt": (
                f"{_FE1_CTX}\n\n"
                "Question: If 92 screws are needed and 12 are already in stock, "
                "how many screws must be ordered?\n\n"
                "Reply with exactly: ANSWER: <number>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: 80",
        },
        {
            "hop": "packets_needed",
            "prompt": (
                f"{_FE1_CTX}\n\n"
                "Question: If 80 screws must be ordered and screws come in packets "
                "of 10, how many packets are needed (round up)?\n\n"
                "Reply with exactly: ANSWER: <number>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: 8",
        },
    ],
}

FE2 = {
    "id": "FE2",
    "narrow": {
        "prompt": (
            f"{_FE2_CTX}\n\n"
            "Question: How many additional slots does the second rack need beyond "
            "what the first rack provides?\n\n"
            "Reply with exactly: ANSWER: <number>"
        ),
        "score_type": "exact",
        "answer": "ANSWER: 7",
    },
    "broad": {
        "prompt": (
            f"{_FE2_CTX}\n\n"
            "Question: How many slots does the first rack have?\n\n"
            "Reply with exactly: ANSWER: <number>"
        ),
        "score_type": "exact",
        "answer": "ANSWER: 15",
    },
    "component_checks": [
        {
            "hop": "first_rack_slots",
            "prompt": (
                f"{_FE2_CTX}\n\n"
                "Question: What is 3 times 5?\n\n"
                "Reply with exactly: ANSWER: <number>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: 15",
        },
        {
            "hop": "second_rack_slots",
            "prompt": (
                f"{_FE2_CTX}\n\n"
                "Question: What is 11 times 2?\n\n"
                "Reply with exactly: ANSWER: <number>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: 22",
        },
        {
            "hop": "additional_slots",
            "prompt": (
                f"{_FE2_CTX}\n\n"
                "Question: If the first rack has 15 slots and the second needs 22 slots, "
                "how many additional slots are needed?\n\n"
                "Reply with exactly: ANSWER: <number>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: 7",
        },
    ],
}

FE3 = {
    "id": "FE3",
    "narrow": {
        "prompt": (
            f"{_FE3_CTX}\n\n"
            "Question: How many tools must be ordered from outside the warehouse?\n\n"
            "Reply with exactly: ANSWER: <number>"
        ),
        "score_type": "exact",
        "answer": "ANSWER: 47",
    },
    "broad": {
        "prompt": (
            f"{_FE3_CTX}\n\n"
            "Question: How many members are on the team in total?\n\n"
            "Reply with exactly: ANSWER: <number>"
        ),
        "score_type": "exact",
        "answer": "ANSWER: 24",
    },
    "component_checks": [
        {
            "hop": "total_members",
            "prompt": (
                f"{_FE3_CTX}\n\n"
                "Question: What is 4 times 6?\n\n"
                "Reply with exactly: ANSWER: <number>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: 24",
        },
        {
            "hop": "total_tools_needed",
            "prompt": (
                f"{_FE3_CTX}\n\n"
                "Question: If there are 24 members and each must carry 3 tools, "
                "how many tools are needed in total?\n\n"
                "Reply with exactly: ANSWER: <number>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: 72",
        },
        {
            "hop": "tools_to_order",
            "prompt": (
                f"{_FE3_CTX}\n\n"
                "Question: If 72 tools are needed and 25 are already in the warehouse, "
                "how many must be ordered from outside?\n\n"
                "Reply with exactly: ANSWER: <number>"
            ),
            "score_type": "exact",
            "answer": "ANSWER: 47",
        },
    ],
}


# ---------------------------------------------------------------------------
# CONTROLS
# AC1, AC2: atomic single-step lookup (1 hop, broad only)
# NC1: broad-broad negative control (both arms broad)
# ---------------------------------------------------------------------------

AC1 = {
    "id": "AC1",
    "narrow": {
        "prompt": (
            "The blue locker contains the silver disk.\n\n"
            "Question: What does the blue locker contain?\n\n"
            "Reply with exactly: ANSWER: <item>"
        ),
        "score_type": "exact",
        "answer": "ANSWER: silver disk",
    },
    "broad": {
        "prompt": (
            "The blue locker contains the silver disk.\n\n"
            "Question: What does the blue locker contain?\n\n"
            "Reply with exactly: ANSWER: <item>"
        ),
        "score_type": "exact",
        "answer": "ANSWER: silver disk",
    },
    "component_checks": [],
}

AC2 = {
    "id": "AC2",
    "narrow": {
        "prompt": (
            "Agent Tova holds clearance level GOLD.\n\n"
            "Question: What clearance level does Agent Tova hold?\n\n"
            "Reply with exactly: ANSWER: <clearance>"
        ),
        "score_type": "exact",
        "answer": "ANSWER: GOLD",
    },
    "broad": {
        "prompt": (
            "Agent Tova holds clearance level GOLD.\n\n"
            "Question: What clearance level does Agent Tova hold?\n\n"
            "Reply with exactly: ANSWER: <clearance>"
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
            "The red cabinet contains old permits. "
            "The green cabinet contains current permits. "
            "The blue cabinet contains expired permits.\n\n"
            "Question: What does the green cabinet contain?\n\n"
            "Reply with exactly: ANSWER: <item>"
        ),
        "score_type": "exact",
        "answer": "ANSWER: current permits",
    },
    "broad": {
        "prompt": (
            "The archive room holds three cabinets: red, green, and blue. "
            "The red cabinet contains old permits. "
            "The green cabinet contains current permits. "
            "The blue cabinet contains expired permits.\n\n"
            "Question: What does the red cabinet contain?\n\n"
            "Reply with exactly: ANSWER: <item>"
        ),
        "score_type": "exact",
        "answer": "ANSWER: old permits",
    },
    "component_checks": [],
}


# ---------------------------------------------------------------------------
# PAIRS — exported for run_tier0.py
# ---------------------------------------------------------------------------

PAIRS = [
    FA1, FA2, FA3, FA4,
    FB1, FB2, FB3, FB4,
    FC1, FC2, FC3, FC4,
    FD1, FD2, FD3, FD4,
    FE1, FE2, FE3,
    AC1, AC2, NC1,
]
