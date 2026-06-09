#!/usr/bin/env python3
"""
tasks_exp6.py — Task file for Experiment 6: Test 1 (Seam) with Exp 5 forced-format scaffold.

Pre-registration: PREREGISTRATION-EXP6.md (written before stability screen).

=== TOKEN TAXONOMY ===

PRIMARY_TERMINALS — composite answer tokens for SA1–SA8.
  Each used ONLY as terminal of its designated chain.
  Never intermediates, broad values, or terminals elsewhere.
  No natural antonym. No English word embedded.
  ZUNIP  MAVOQ  KELDA  RIVOK  TANEM  GLAXU  VOPAR  DREXM

NULL_TERMINAL — for NC1 only; absent from NC1's context.
  NIREL

DIAGNOSTIC_TERMINALS — composite answer tokens for DE3/DE4.
  Not from PRIMARY_TERMINALS pool.
  PLABT  WUXEL

BROAD_VALUES — expected answers for broad arm only.
  Never primary terminals or chain intermediates.
  SA1:BRIFQ  SA2:PELRK  SA3:MIXOQ  SA4:KOLVR  SA5:GAVEP
  SA6:ALCRN  SA7:NODEY  SA8:GRUXV
  DE1:SLOTQ  DE2:ZRUVX  DE3:KRIFN  DE4:MUVOX
  NC1:TURVL  AC1a:GOLVX  AC1b:ZOVNX  AC2a:PLORN  AC2b:WAXTR

INTERMEDIATES — chain nodes only; never answer tokens.
  SA1: AXFOB  TUNNB  ALCV5
  SA2: KROMP  VLIXT  DRUFI
  SA3: GORPF  BLIFM  DRAXT
  SA4: WUQEN  PAXYL  GLEBM
  SA5: MUXIV  TORPX  CLAVB
  SA6: ZAROT  FLOBN  KRIMP
  SA7: KLAXP  GLUMT  FRIVB
  SA8: TRIMP  VAXOL  CLUFB

DIAGNOSTIC_NODES — chain nodes in DE items; not SA intermediates.
  DE1: KAXON  CHAMV
  DE2: FRAXB  BLOMP
  DE3: PLOXB  GRIMT
  DE4: XOMBT  GRIVL

DISTRACTOR_ENTITIES — appear only in "X holds Y" distractor facts; not chain nodes.
  GATEP  NEXAL  RUBYX  TUVOX  NEXUL  VOXEL  DRUMN  NEXOV
  GAVEX  KLURF  VLMXT  GROXT  SLOTB
  NODEX (NC1 chain node, not a terminal)

AC_TOKENS — persons and targets for atomic controls only.
  NIRA  FRALP  DEXT  KLUMB

=== RELATION SKELETONS (pre-registered, locked) ===

S1: {A} connects to {B}. {B} leads to {C}. {C} grants {TERMINAL}.
    Q templates: "{A} connects to what?"  "{B} leads to what?"  "{C} grants what?"
    Used by: SA1  SA2  SA3  SA7

S2: {A} routes to {B}. {B} opens into {C}. {C} maps to {TERMINAL}.
    Q templates: "{A} routes to what?"  "{B} opens into what?"  "{C} maps to what?"
    Used by: SA4  SA5  SA6  SA8

=== G COMPUTATION ===

G_content(w) = R_component_content(w) - R_composite_content(w)
G_strict(w)  = R_component_strict(w)  - R_composite_strict(w)

Only items with included_in_G=True contribute to G metrics.
Diagnostic (DE, NC, AC) items are always excluded.
"""

_FMT      = "Respond using only this exact format with nothing before or after: ANSWER:"
_FMT_PARA = "Your entire response must be exactly this and nothing else: ANSWER:"

# ---------------------------------------------------------------------------
# PRIMARY SEAM ITEMS — SA family (8 items)
# 3-hop / 4-node chains. Explicit first-node anchor in composite question.
# Terminal appears ONLY as composite terminal of its designated chain.
# One 1-hop distractor fact per item (stability-screen broad arm only).
# included_in_G: True
# ---------------------------------------------------------------------------

_SA1_CTX = (
    "AXFOB connects to TUNNB. TUNNB leads to ALCV5. ALCV5 grants ZUNIP. "
    "GATEP holds BRIFQ."
)
SA1 = {
    "id": "SA1",
    "family": "S",
    "role": "PRIMARY_SEAM",
    "relation_skeleton": "S1",
    "terminal": "ZUNIP",
    "included_in_G": True,
    "narrow": {
        "prompt": (f"{_SA1_CTX}\n\n"
                   f"Starting from AXFOB, what terminal value does the chain reach?\n\n"
                   f"{_FMT} <value>"),
        "score_type": "exact",
        "answer": "ANSWER: ZUNIP",
    },
    "broad": {
        "prompt": f"{_SA1_CTX}\n\nGATEP holds what?\n\n{_FMT} <value>",
        "score_type": "exact",
        "answer": "ANSWER: BRIFQ",
    },
    "component_checks": [
        {"hop": "axfob_tunnb", "prompt": f"{_SA1_CTX}\n\nAXFOB connects to what?\n\n{_FMT} <value>", "score_type": "exact", "answer": "ANSWER: TUNNB"},
        {"hop": "tunnb_alcv5", "prompt": f"{_SA1_CTX}\n\nTUNNB leads to what?\n\n{_FMT} <value>",   "score_type": "exact", "answer": "ANSWER: ALCV5"},
        {"hop": "alcv5_zunip", "prompt": f"{_SA1_CTX}\n\nALCV5 grants what?\n\n{_FMT} <value>",     "score_type": "exact", "answer": "ANSWER: ZUNIP"},
    ],
}

_SA2_CTX = (
    "KROMP connects to VLIXT. VLIXT leads to DRUFI. DRUFI grants MAVOQ. "
    "NEXAL holds PELRK."
)
SA2 = {
    "id": "SA2",
    "family": "S",
    "role": "PRIMARY_SEAM",
    "relation_skeleton": "S1",
    "terminal": "MAVOQ",
    "included_in_G": True,
    "narrow": {
        "prompt": (f"{_SA2_CTX}\n\n"
                   f"Starting from KROMP, what terminal value does the chain reach?\n\n"
                   f"{_FMT} <value>"),
        "score_type": "exact",
        "answer": "ANSWER: MAVOQ",
    },
    "broad": {
        "prompt": f"{_SA2_CTX}\n\nNEXAL holds what?\n\n{_FMT} <value>",
        "score_type": "exact",
        "answer": "ANSWER: PELRK",
    },
    "component_checks": [
        {"hop": "kromp_vlixt", "prompt": f"{_SA2_CTX}\n\nKROMP connects to what?\n\n{_FMT} <value>", "score_type": "exact", "answer": "ANSWER: VLIXT"},
        {"hop": "vlixt_drufi", "prompt": f"{_SA2_CTX}\n\nVLIXT leads to what?\n\n{_FMT} <value>",   "score_type": "exact", "answer": "ANSWER: DRUFI"},
        {"hop": "drufi_mavoq", "prompt": f"{_SA2_CTX}\n\nDRUFI grants what?\n\n{_FMT} <value>",     "score_type": "exact", "answer": "ANSWER: MAVOQ"},
    ],
}

_SA3_CTX = (
    "GORPF connects to BLIFM. BLIFM leads to DRAXT. DRAXT grants KELDA. "
    "RUBYX holds MIXOQ."
)
SA3 = {
    "id": "SA3",
    "family": "S",
    "role": "PRIMARY_SEAM",
    "relation_skeleton": "S1",
    "terminal": "KELDA",
    "included_in_G": True,
    "narrow": {
        "prompt": (f"{_SA3_CTX}\n\n"
                   f"Starting from GORPF, what terminal value does the chain reach?\n\n"
                   f"{_FMT} <value>"),
        "score_type": "exact",
        "answer": "ANSWER: KELDA",
    },
    "broad": {
        "prompt": f"{_SA3_CTX}\n\nRUBYX holds what?\n\n{_FMT} <value>",
        "score_type": "exact",
        "answer": "ANSWER: MIXOQ",
    },
    "component_checks": [
        {"hop": "gorpf_blifm", "prompt": f"{_SA3_CTX}\n\nGORPF connects to what?\n\n{_FMT} <value>", "score_type": "exact", "answer": "ANSWER: BLIFM"},
        {"hop": "blifm_draxt", "prompt": f"{_SA3_CTX}\n\nBLIFM leads to what?\n\n{_FMT} <value>",   "score_type": "exact", "answer": "ANSWER: DRAXT"},
        {"hop": "draxt_kelda", "prompt": f"{_SA3_CTX}\n\nDRAXT grants what?\n\n{_FMT} <value>",     "score_type": "exact", "answer": "ANSWER: KELDA"},
    ],
}

_SA4_CTX = (
    "WUQEN routes to PAXYL. PAXYL opens into GLEBM. GLEBM maps to RIVOK. "
    "TUVOX holds KOLVR."
)
SA4 = {
    "id": "SA4",
    "family": "S",
    "role": "PRIMARY_SEAM",
    "relation_skeleton": "S2",
    "terminal": "RIVOK",
    "included_in_G": True,
    "narrow": {
        "prompt": (f"{_SA4_CTX}\n\n"
                   f"Starting from WUQEN, what terminal value does the chain reach?\n\n"
                   f"{_FMT} <value>"),
        "score_type": "exact",
        "answer": "ANSWER: RIVOK",
    },
    "broad": {
        "prompt": f"{_SA4_CTX}\n\nTUVOX holds what?\n\n{_FMT} <value>",
        "score_type": "exact",
        "answer": "ANSWER: KOLVR",
    },
    "component_checks": [
        {"hop": "wuqen_paxyl", "prompt": f"{_SA4_CTX}\n\nWUQEN routes to what?\n\n{_FMT} <value>",   "score_type": "exact", "answer": "ANSWER: PAXYL"},
        {"hop": "paxyl_glebm", "prompt": f"{_SA4_CTX}\n\nPAXYL opens into what?\n\n{_FMT} <value>",  "score_type": "exact", "answer": "ANSWER: GLEBM"},
        {"hop": "glebm_rivok", "prompt": f"{_SA4_CTX}\n\nGLEBM maps to what?\n\n{_FMT} <value>",     "score_type": "exact", "answer": "ANSWER: RIVOK"},
    ],
}

_SA5_CTX = (
    "MUXIV routes to TORPX. TORPX opens into CLAVB. CLAVB maps to TANEM. "
    "NEXUL holds GAVEP."
)
SA5 = {
    "id": "SA5",
    "family": "S",
    "role": "PRIMARY_SEAM",
    "relation_skeleton": "S2",
    "terminal": "TANEM",
    "included_in_G": True,
    "narrow": {
        "prompt": (f"{_SA5_CTX}\n\n"
                   f"Starting from MUXIV, what terminal value does the chain reach?\n\n"
                   f"{_FMT} <value>"),
        "score_type": "exact",
        "answer": "ANSWER: TANEM",
    },
    "broad": {
        "prompt": f"{_SA5_CTX}\n\nNEXUL holds what?\n\n{_FMT} <value>",
        "score_type": "exact",
        "answer": "ANSWER: GAVEP",
    },
    "component_checks": [
        {"hop": "muxiv_torpx", "prompt": f"{_SA5_CTX}\n\nMUXIV routes to what?\n\n{_FMT} <value>",  "score_type": "exact", "answer": "ANSWER: TORPX"},
        {"hop": "torpx_clavb", "prompt": f"{_SA5_CTX}\n\nTORPX opens into what?\n\n{_FMT} <value>", "score_type": "exact", "answer": "ANSWER: CLAVB"},
        {"hop": "clavb_tanem", "prompt": f"{_SA5_CTX}\n\nCLAVB maps to what?\n\n{_FMT} <value>",    "score_type": "exact", "answer": "ANSWER: TANEM"},
    ],
}

_SA6_CTX = (
    "ZAROT routes to FLOBN. FLOBN opens into KRIMP. KRIMP maps to GLAXU. "
    "VOXEL holds ALCRN."
)
SA6 = {
    "id": "SA6",
    "family": "S",
    "role": "PRIMARY_SEAM",
    "relation_skeleton": "S2",
    "terminal": "GLAXU",
    "included_in_G": True,
    "narrow": {
        "prompt": (f"{_SA6_CTX}\n\n"
                   f"Starting from ZAROT, what terminal value does the chain reach?\n\n"
                   f"{_FMT} <value>"),
        "score_type": "exact",
        "answer": "ANSWER: GLAXU",
    },
    "broad": {
        "prompt": f"{_SA6_CTX}\n\nVOXEL holds what?\n\n{_FMT} <value>",
        "score_type": "exact",
        "answer": "ANSWER: ALCRN",
    },
    "component_checks": [
        {"hop": "zarot_flobn", "prompt": f"{_SA6_CTX}\n\nZAROT routes to what?\n\n{_FMT} <value>",  "score_type": "exact", "answer": "ANSWER: FLOBN"},
        {"hop": "flobn_krimp", "prompt": f"{_SA6_CTX}\n\nFLOBN opens into what?\n\n{_FMT} <value>", "score_type": "exact", "answer": "ANSWER: KRIMP"},
        {"hop": "krimp_glaxu", "prompt": f"{_SA6_CTX}\n\nKRIMP maps to what?\n\n{_FMT} <value>",    "score_type": "exact", "answer": "ANSWER: GLAXU"},
    ],
}

_SA7_CTX = (
    "KLAXP connects to GLUMT. GLUMT leads to FRIVB. FRIVB grants VOPAR. "
    "DRUMN holds NODEY."
)
SA7 = {
    "id": "SA7",
    "family": "S",
    "role": "PRIMARY_SEAM",
    "relation_skeleton": "S1",
    "terminal": "VOPAR",
    "included_in_G": True,
    "narrow": {
        "prompt": (f"{_SA7_CTX}\n\n"
                   f"Starting from KLAXP, what terminal value does the chain reach?\n\n"
                   f"{_FMT} <value>"),
        "score_type": "exact",
        "answer": "ANSWER: VOPAR",
    },
    "broad": {
        "prompt": f"{_SA7_CTX}\n\nDRUMN holds what?\n\n{_FMT} <value>",
        "score_type": "exact",
        "answer": "ANSWER: NODEY",
    },
    "component_checks": [
        {"hop": "klaxp_glumt", "prompt": f"{_SA7_CTX}\n\nKLAXP connects to what?\n\n{_FMT} <value>", "score_type": "exact", "answer": "ANSWER: GLUMT"},
        {"hop": "glumt_frivb", "prompt": f"{_SA7_CTX}\n\nGLUMT leads to what?\n\n{_FMT} <value>",   "score_type": "exact", "answer": "ANSWER: FRIVB"},
        {"hop": "frivb_vopar", "prompt": f"{_SA7_CTX}\n\nFRIVB grants what?\n\n{_FMT} <value>",     "score_type": "exact", "answer": "ANSWER: VOPAR"},
    ],
}

_SA8_CTX = (
    "TRIMP routes to VAXOL. VAXOL opens into CLUFB. CLUFB maps to DREXM. "
    "NEXOV holds GRUXV."
)
SA8 = {
    "id": "SA8",
    "family": "S",
    "role": "PRIMARY_SEAM",
    "relation_skeleton": "S2",
    "terminal": "DREXM",
    "included_in_G": True,
    "narrow": {
        "prompt": (f"{_SA8_CTX}\n\n"
                   f"Starting from TRIMP, what terminal value does the chain reach?\n\n"
                   f"{_FMT} <value>"),
        "score_type": "exact",
        "answer": "ANSWER: DREXM",
    },
    "broad": {
        "prompt": f"{_SA8_CTX}\n\nNEXOV holds what?\n\n{_FMT} <value>",
        "score_type": "exact",
        "answer": "ANSWER: GRUXV",
    },
    "component_checks": [
        {"hop": "trimp_vaxol", "prompt": f"{_SA8_CTX}\n\nTRIMP routes to what?\n\n{_FMT} <value>",  "score_type": "exact", "answer": "ANSWER: VAXOL"},
        {"hop": "vaxol_clufb", "prompt": f"{_SA8_CTX}\n\nVAXOL opens into what?\n\n{_FMT} <value>", "score_type": "exact", "answer": "ANSWER: CLUFB"},
        {"hop": "clufb_drexm", "prompt": f"{_SA8_CTX}\n\nCLUFB maps to what?\n\n{_FMT} <value>",    "score_type": "exact", "answer": "ANSWER: DREXM"},
    ],
}


# ---------------------------------------------------------------------------
# DIAGNOSTIC ECHO CONTROLS — DE family (4 items)
# Estimate intermediate-token echo rate under the forced-format scaffold.
# Excluded from G_content and G_strict in all cases.
# Only interpretable as echo diagnostic if FP16 content passes (diagnostic_gate).
# If FP16 content=0: classify as FLOOR_DIAGNOSTIC; exclude from echo-rate read.
#
# DE-QE (question-entity echo): 1-hop; echo risk = model outputs question subject.
# DE-PI (penultimate-intermediate echo): 2-hop composite; echo risk = model outputs
#   penultimate node instead of terminal.
# ---------------------------------------------------------------------------

_DE1_CTX = "KAXON leads to CHAMV. GAVEX holds SLOTQ."
DE1 = {
    "id": "DE1",
    "family": "DE",
    "role": "DIAGNOSTIC_ECHO_QE",
    "echo_type": "QE",
    "echo_wrong_value": "KAXON",
    "included_in_G": False,
    "diagnostic_gate": "fp16_content_pass",
    "narrow": {
        "prompt": f"{_DE1_CTX}\n\nKAXON leads to what?\n\n{_FMT} <value>",
        "score_type": "exact",
        "answer": "ANSWER: CHAMV",
    },
    "broad": {
        "prompt": f"{_DE1_CTX}\n\nGAVEX holds what?\n\n{_FMT} <value>",
        "score_type": "exact",
        "answer": "ANSWER: SLOTQ",
    },
    "component_checks": [],
}

_DE2_CTX = "FRAXB leads to BLOMP. KLURF holds ZRUVX."
DE2 = {
    "id": "DE2",
    "family": "DE",
    "role": "DIAGNOSTIC_ECHO_QE",
    "echo_type": "QE",
    "echo_wrong_value": "FRAXB",
    "included_in_G": False,
    "diagnostic_gate": "fp16_content_pass",
    "narrow": {
        "prompt": f"{_DE2_CTX}\n\nFRAXB leads to what?\n\n{_FMT} <value>",
        "score_type": "exact",
        "answer": "ANSWER: BLOMP",
    },
    "broad": {
        "prompt": f"{_DE2_CTX}\n\nKLURF holds what?\n\n{_FMT} <value>",
        "score_type": "exact",
        "answer": "ANSWER: ZRUVX",
    },
    "component_checks": [],
}

# DE-PI: 2-hop composite; penultimate node is the echo risk target.
_DE3_CTX = "PLOXB routes to GRIMT. GRIMT maps to PLABT. VLMXT holds KRIFN."
DE3 = {
    "id": "DE3",
    "family": "DE",
    "role": "DIAGNOSTIC_ECHO_PI",
    "echo_type": "PI",
    "echo_wrong_value": "GRIMT",
    "included_in_G": False,
    "diagnostic_gate": "fp16_content_pass",
    "narrow": {
        "prompt": (f"{_DE3_CTX}\n\n"
                   f"Starting from PLOXB, what terminal value does the chain reach?\n\n"
                   f"{_FMT} <value>"),
        "score_type": "exact",
        "answer": "ANSWER: PLABT",
    },
    "broad": {
        "prompt": f"{_DE3_CTX}\n\nVLMXT holds what?\n\n{_FMT} <value>",
        "score_type": "exact",
        "answer": "ANSWER: KRIFN",
    },
    "component_checks": [
        {"hop": "ploxb_grimt", "prompt": f"{_DE3_CTX}\n\nPLOXB routes to what?\n\n{_FMT} <value>", "score_type": "exact", "answer": "ANSWER: GRIMT"},
        {"hop": "grimt_plabt", "prompt": f"{_DE3_CTX}\n\nGRIMT maps to what?\n\n{_FMT} <value>",   "score_type": "exact", "answer": "ANSWER: PLABT"},
    ],
}

_DE4_CTX = "XOMBT routes to GRIVL. GRIVL maps to WUXEL. GROXT holds MUVOX."
DE4 = {
    "id": "DE4",
    "family": "DE",
    "role": "DIAGNOSTIC_ECHO_PI",
    "echo_type": "PI",
    "echo_wrong_value": "GRIVL",
    "included_in_G": False,
    "diagnostic_gate": "fp16_content_pass",
    "narrow": {
        "prompt": (f"{_DE4_CTX}\n\n"
                   f"Starting from XOMBT, what terminal value does the chain reach?\n\n"
                   f"{_FMT} <value>"),
        "score_type": "exact",
        "answer": "ANSWER: WUXEL",
    },
    "broad": {
        "prompt": f"{_DE4_CTX}\n\nGROXT holds what?\n\n{_FMT} <value>",
        "score_type": "exact",
        "answer": "ANSWER: MUVOX",
    },
    "component_checks": [
        {"hop": "xombt_grivl", "prompt": f"{_DE4_CTX}\n\nXOMBT routes to what?\n\n{_FMT} <value>", "score_type": "exact", "answer": "ANSWER: GRIVL"},
        {"hop": "grivl_wuxel", "prompt": f"{_DE4_CTX}\n\nGRIVL maps to what?\n\n{_FMT} <value>",   "score_type": "exact", "answer": "ANSWER: WUXEL"},
    ],
}


# ---------------------------------------------------------------------------
# NULL CONTROL — NC family (1 item)
# Validates that content_slot_score returns 0 when the expected token is
# absent from context. AXFOB and NIREL both absent from NC1's context.
#
# Expected at every rung: content=0, strict=0.
# Flag condition: if content=1 at any rung, halt — scorer audit required.
# Classification: NULL_CONTROL / EXPECTED_FLOOR (not CONTENT_LOSS).
# Excluded from all G metrics and model-capability claims.
# ---------------------------------------------------------------------------

_NC1_CTX = "CHAMV routes to NODEX. SLOTB contains TURVL."
NC1 = {
    "id": "NC1",
    "family": "NC",
    "role": "NULL_CONTROL",
    "included_in_G": False,
    "expected_fp16_content": 0,
    "flag_if_content_nonzero": True,
    "narrow": {
        "prompt": (f"{_NC1_CTX}\n\n"
                   f"Starting from AXFOB, what terminal value does the chain reach?\n\n"
                   f"{_FMT} <value>"),
        "score_type": "exact",
        "answer": "ANSWER: NIREL",
    },
    "broad": {
        "prompt": f"{_NC1_CTX}\n\nSLOTB contains what?\n\n{_FMT} <value>",
        "score_type": "exact",
        "answer": "ANSWER: TURVL",
    },
    "component_checks": [],
}


# ---------------------------------------------------------------------------
# ATOMIC CONTROLS — AC family (2 items)
# 1-hop person→value sanity checks. Verify basic retrieval is functional at
# each quantization rung. Excluded from G metrics.
# ---------------------------------------------------------------------------

_AC1_CTX = "NIRA holds GOLVX. FRALP holds ZOVNX."
AC1 = {
    "id": "AC1",
    "family": "AC",
    "role": "ATOMIC_CONTROL",
    "included_in_G": False,
    "narrow": {
        "prompt": f"{_AC1_CTX}\n\nNIRA holds what?\n\n{_FMT} <value>",
        "score_type": "exact",
        "answer": "ANSWER: GOLVX",
    },
    "broad": {
        "prompt": f"{_AC1_CTX}\n\nFRALP holds what?\n\n{_FMT} <value>",
        "score_type": "exact",
        "answer": "ANSWER: ZOVNX",
    },
    "component_checks": [],
}

_AC2_CTX = "DEXT holds PLORN. KLUMB holds WAXTR."
AC2 = {
    "id": "AC2",
    "family": "AC",
    "role": "ATOMIC_CONTROL",
    "included_in_G": False,
    "narrow": {
        "prompt": f"{_AC2_CTX}\n\nDEXT holds what?\n\n{_FMT} <value>",
        "score_type": "exact",
        "answer": "ANSWER: PLORN",
    },
    "broad": {
        "prompt": f"{_AC2_CTX}\n\nKLUMB holds what?\n\n{_FMT} <value>",
        "score_type": "exact",
        "answer": "ANSWER: WAXTR",
    },
    "component_checks": [],
}


# ---------------------------------------------------------------------------
# PAIRS — full task list (15 items)
# Stability screen and stress sweep run against this list.
# G_content and G_strict computed only over items with included_in_G=True (SA1–SA8).
# ---------------------------------------------------------------------------
PAIRS = [
    SA1, SA2, SA3, SA4, SA5, SA6, SA7, SA8,   # primary seam items (n=8)
    DE1, DE2, DE3, DE4,                         # diagnostic echo controls
    NC1,                                         # null / scorer validation
    AC1, AC2,                                    # atomic controls
]
