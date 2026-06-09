#!/usr/bin/env python3
"""
tasks_exp7.py — Task file for Experiment 7: Primary Seam Test (Construction Repair).

Pre-registration: PREREGISTRATION-EXP7.md (locked 2026-06-06).

Repairs two Exp6 construction artifacts (see RESULTS-EXP6.md §6):
  1. Distractor fact moved to context FRONT (was at end → caused last-value anchoring).
  2. Decoy fact added to context END: DECOY_ENTITY marks DECOY_VALUE.
  3. S1 skeleton only (connects / leads / grants) for all SA items.
  4. Terminal is neither the first nor last ALL-CAPS token in any SA context.

SA context pattern (locked):
  DISTRACTOR_ENTITY holds BROAD_VALUE.
  A connects to B. B leads to C. C grants TERMINAL.
  DECOY_ENTITY marks DECOY_VALUE.

Run static validation before FP16 stability screen:
  python3 tasks_exp7.py

=== TOKEN TAXONOMY ===

PRIMARY_TERMINALS — composite answer tokens for SA1–SA8.
  Each used ONLY as terminal of its designated chain.
  Never intermediates, broad values, decoy values, or terminals elsewhere.
  FAVOX  PLONX  WEXBI  ZULPA  DRIXM  NORVA  KRAXI  VEFLM

NULL_TERMINAL — for NC1 only; absent from NC1's context.
  BAXNU

DIAGNOSTIC_TERMINALS — composite answer tokens for DE3/DE4.
  Not from PRIMARY_TERMINALS pool.
  WOXUR  BLIXT

SA_DECOY_VALUES — last ALL-CAPS token in each SA context.
  Never terminals, broad values, or intermediates.
  SA1:SLOMX  SA2:VARGN  SA3:DUPLX  SA4:YOMBL  SA5:RAXLV
  SA6:BROXN  SA7:ZEPHI  SA8:WULFT

BROAD_VALUES — expected answers for broad arm only.
  Never primary terminals, intermediates, or decoy values.
  SA1:GROXL  SA2:FLIPN  SA3:BUVAX  SA4:KRAZM  SA5:WOVLU
  SA6:QUAFT  SA7:NIXBL  SA8:LORVX
  DE1:VIMPL  DE2:WIXPL  DE3:KLINP  DE4:TAXGR
  NC1:ZULNX  AC1:WUMFT  AC2:WUNFA

AC_NARROW_ANSWERS — narrow arm expected answers for AC items.
  AC1:GRUVL  AC2:DRIXP

AC_DECOY_VALUES — last ALL-CAPS token in AC contexts.
  AC1:BLIVX  AC2:KLONB

DE_PI_DECOY_VALUES — last ALL-CAPS token in DE-PI contexts.
  DE3:DRUVF  DE4:VAXLM

INTERMEDIATES — chain nodes only; never answer tokens.
  SA1: GRIXP  VUNLB  MEXOT
  SA2: DRALX  KLOMF  ZAPVI
  SA3: BLUXN  WIVOT  FROPK
  SA4: SKRON  PAMVL  XOTBI
  SA5: VOMPL  JAXOL  GLIVN
  SA6: MAXBI  GRULP  WOXEN
  SA7: DRIZP  ZARVP  KARVO
  SA8: TROXB  FLUMB  NAKVI

DIAGNOSTIC_NODES — chain nodes in DE items; not SA intermediates.
  DE1: ZIXPA(anchor)  ORBUX(target)
  DE2: FLOXB(anchor)  GRUMV(target)
  DE3: PLOXN(anchor)  GRIVT(penultimate)
  DE4: ZOMPL(anchor)  VRAXI(penultimate)

DISTRACTOR_ENTITIES — subjects of "X holds Y" distractor facts; first in SA context.
  BILMO  TRAXK  VLUMB  ZROXN  GLIFP  BLIXO  DROFL  GRAFI

DECOY_ENTITIES — subjects of "X marks Y" decoy facts; last in SA context.
  SORMB  PROXK  WULNI  GLOXI  VUNFT  KARBX  TREXN  PLOMV

DE_CONTEXT_ENTITIES — subjects and holders in DE contexts; not SA entities.
  DE1: KRONB     DE2: TRAXO
  DE3: VRAXB(distractor)  XOMBI(decoy)
  DE4: FLONB(distractor)  KORNU(decoy)

NC_CONTEXT — entities in NC1 context; chain is not traversable from absent anchor VIXOM.
  PIXNV  NAXBI  GRAXB(chain value, not scored)
  VIXOM — absent anchor; must not appear in any context.
  BAXNU — absent expected answer; must not appear in any context.

AC_ENTITIES — subjects and decoy entities for atomic controls.
  NOXBA  PRAXE  SORNI     (AC1)
  KLOMR  BIXTV  ZARPL     (AC2)

=== RELATION SKELETONS (locked for SA items) ===

S1 (all SA items): {A} connects to {B}. {B} leads to {C}. {C} grants {TERMINAL}.
    Component Q templates:
      "{A} connects to what?"
      "{B} leads to what?"
      "{C} grants what?"

=== G COMPUTATION ===

G_content(w) = R_component_content(w) - R_composite_content(w)
G_strict(w)  = R_component_strict(w)  - R_composite_strict(w)

Only items with included_in_G=True (SA1–SA8) contribute to G metrics.
"""

import hashlib
import re
import sys
from pathlib import Path

_FMT      = "Respond using only this exact format with nothing before or after: ANSWER:"
_FMT_PARA = "Your entire response must be exactly this and nothing else: ANSWER:"


# =============================================================================
# PRIMARY SEAM ITEMS — SA family (8 items)
# Context: DISTRACTOR holds BROAD. A connects to B. B leads to C. C grants TERMINAL. DECOY marks DECOY_VALUE.
# included_in_G: True
# =============================================================================

_SA1_CTX = (
    "BILMO holds GROXL. "
    "GRIXP connects to VUNLB. VUNLB leads to MEXOT. MEXOT grants FAVOX. "
    "SORMB marks SLOMX."
)
SA1 = {
    "id": "SA1", "family": "S", "role": "PRIMARY_SEAM",
    "relation_skeleton": "S1", "terminal": "FAVOX", "decoy_value": "SLOMX",
    "included_in_G": True,
    "narrow": {
        "prompt": (f"{_SA1_CTX}\n\n"
                   f"Starting from GRIXP, what terminal value does the chain reach?\n\n"
                   f"{_FMT} <value>"),
        "score_type": "exact", "answer": "ANSWER: FAVOX",
    },
    "broad": {
        "prompt": f"{_SA1_CTX}\n\nBILMO holds what?\n\n{_FMT} <value>",
        "score_type": "exact", "answer": "ANSWER: GROXL",
    },
    "component_checks": [
        {"hop": "grixp_vunlb", "prompt": f"{_SA1_CTX}\n\nGRIXP connects to what?\n\n{_FMT} <value>", "score_type": "exact", "answer": "ANSWER: VUNLB"},
        {"hop": "vunlb_mexot", "prompt": f"{_SA1_CTX}\n\nVUNLB leads to what?\n\n{_FMT} <value>",   "score_type": "exact", "answer": "ANSWER: MEXOT"},
        {"hop": "mexot_favox", "prompt": f"{_SA1_CTX}\n\nMEXOT grants what?\n\n{_FMT} <value>",     "score_type": "exact", "answer": "ANSWER: FAVOX"},
    ],
}

_SA2_CTX = (
    "TRAXK holds FLIPN. "
    "DRALX connects to KLOMF. KLOMF leads to ZAPVI. ZAPVI grants PLONX. "
    "PROXK marks VARGN."
)
SA2 = {
    "id": "SA2", "family": "S", "role": "PRIMARY_SEAM",
    "relation_skeleton": "S1", "terminal": "PLONX", "decoy_value": "VARGN",
    "included_in_G": True,
    "narrow": {
        "prompt": (f"{_SA2_CTX}\n\n"
                   f"Starting from DRALX, what terminal value does the chain reach?\n\n"
                   f"{_FMT} <value>"),
        "score_type": "exact", "answer": "ANSWER: PLONX",
    },
    "broad": {
        "prompt": f"{_SA2_CTX}\n\nTRAXK holds what?\n\n{_FMT} <value>",
        "score_type": "exact", "answer": "ANSWER: FLIPN",
    },
    "component_checks": [
        {"hop": "dralx_klomf", "prompt": f"{_SA2_CTX}\n\nDRALX connects to what?\n\n{_FMT} <value>", "score_type": "exact", "answer": "ANSWER: KLOMF"},
        {"hop": "klomf_zapvi", "prompt": f"{_SA2_CTX}\n\nKLOMF leads to what?\n\n{_FMT} <value>",   "score_type": "exact", "answer": "ANSWER: ZAPVI"},
        {"hop": "zapvi_plonx", "prompt": f"{_SA2_CTX}\n\nZAPVI grants what?\n\n{_FMT} <value>",     "score_type": "exact", "answer": "ANSWER: PLONX"},
    ],
}

_SA3_CTX = (
    "VLUMB holds BUVAX. "
    "BLUXN connects to WIVOT. WIVOT leads to FROPK. FROPK grants WEXBI. "
    "WULNI marks DUPLX."
)
SA3 = {
    "id": "SA3", "family": "S", "role": "PRIMARY_SEAM",
    "relation_skeleton": "S1", "terminal": "WEXBI", "decoy_value": "DUPLX",
    "included_in_G": True,
    "narrow": {
        "prompt": (f"{_SA3_CTX}\n\n"
                   f"Starting from BLUXN, what terminal value does the chain reach?\n\n"
                   f"{_FMT} <value>"),
        "score_type": "exact", "answer": "ANSWER: WEXBI",
    },
    "broad": {
        "prompt": f"{_SA3_CTX}\n\nVLUMB holds what?\n\n{_FMT} <value>",
        "score_type": "exact", "answer": "ANSWER: BUVAX",
    },
    "component_checks": [
        {"hop": "bluxn_wivot", "prompt": f"{_SA3_CTX}\n\nBLUXN connects to what?\n\n{_FMT} <value>", "score_type": "exact", "answer": "ANSWER: WIVOT"},
        {"hop": "wivot_fropk", "prompt": f"{_SA3_CTX}\n\nWIVOT leads to what?\n\n{_FMT} <value>",   "score_type": "exact", "answer": "ANSWER: FROPK"},
        {"hop": "fropk_wexbi", "prompt": f"{_SA3_CTX}\n\nFROPK grants what?\n\n{_FMT} <value>",     "score_type": "exact", "answer": "ANSWER: WEXBI"},
    ],
}

_SA4_CTX = (
    "ZROXN holds KRAZM. "
    "SKRON connects to PAMVL. PAMVL leads to XOTBI. XOTBI grants ZULPA. "
    "GLOXI marks YOMBL."
)
SA4 = {
    "id": "SA4", "family": "S", "role": "PRIMARY_SEAM",
    "relation_skeleton": "S1", "terminal": "ZULPA", "decoy_value": "YOMBL",
    "included_in_G": True,
    "narrow": {
        "prompt": (f"{_SA4_CTX}\n\n"
                   f"Starting from SKRON, what terminal value does the chain reach?\n\n"
                   f"{_FMT} <value>"),
        "score_type": "exact", "answer": "ANSWER: ZULPA",
    },
    "broad": {
        "prompt": f"{_SA4_CTX}\n\nZROXN holds what?\n\n{_FMT} <value>",
        "score_type": "exact", "answer": "ANSWER: KRAZM",
    },
    "component_checks": [
        {"hop": "skron_pamvl", "prompt": f"{_SA4_CTX}\n\nSKRON connects to what?\n\n{_FMT} <value>", "score_type": "exact", "answer": "ANSWER: PAMVL"},
        {"hop": "pamvl_xotbi", "prompt": f"{_SA4_CTX}\n\nPAMVL leads to what?\n\n{_FMT} <value>",   "score_type": "exact", "answer": "ANSWER: XOTBI"},
        {"hop": "xotbi_zulpa", "prompt": f"{_SA4_CTX}\n\nXOTBI grants what?\n\n{_FMT} <value>",     "score_type": "exact", "answer": "ANSWER: ZULPA"},
    ],
}

_SA5_CTX = (
    "GLIFP holds WOVLU. "
    "VOMPL connects to JAXOL. JAXOL leads to GLIVN. GLIVN grants DRIXM. "
    "VUNFT marks RAXLV."
)
SA5 = {
    "id": "SA5", "family": "S", "role": "PRIMARY_SEAM",
    "relation_skeleton": "S1", "terminal": "DRIXM", "decoy_value": "RAXLV",
    "included_in_G": True,
    "narrow": {
        "prompt": (f"{_SA5_CTX}\n\n"
                   f"Starting from VOMPL, what terminal value does the chain reach?\n\n"
                   f"{_FMT} <value>"),
        "score_type": "exact", "answer": "ANSWER: DRIXM",
    },
    "broad": {
        "prompt": f"{_SA5_CTX}\n\nGLIFP holds what?\n\n{_FMT} <value>",
        "score_type": "exact", "answer": "ANSWER: WOVLU",
    },
    "component_checks": [
        {"hop": "vompl_jaxol", "prompt": f"{_SA5_CTX}\n\nVOMPL connects to what?\n\n{_FMT} <value>", "score_type": "exact", "answer": "ANSWER: JAXOL"},
        {"hop": "jaxol_glivn", "prompt": f"{_SA5_CTX}\n\nJAXOL leads to what?\n\n{_FMT} <value>",   "score_type": "exact", "answer": "ANSWER: GLIVN"},
        {"hop": "glivn_drixm", "prompt": f"{_SA5_CTX}\n\nGLIVN grants what?\n\n{_FMT} <value>",     "score_type": "exact", "answer": "ANSWER: DRIXM"},
    ],
}

_SA6_CTX = (
    "BLIXO holds QUAFT. "
    "MAXBI connects to GRULP. GRULP leads to WOXEN. WOXEN grants NORVA. "
    "KARBX marks BROXN."
)
SA6 = {
    "id": "SA6", "family": "S", "role": "PRIMARY_SEAM",
    "relation_skeleton": "S1", "terminal": "NORVA", "decoy_value": "BROXN",
    "included_in_G": True,
    "narrow": {
        "prompt": (f"{_SA6_CTX}\n\n"
                   f"Starting from MAXBI, what terminal value does the chain reach?\n\n"
                   f"{_FMT} <value>"),
        "score_type": "exact", "answer": "ANSWER: NORVA",
    },
    "broad": {
        "prompt": f"{_SA6_CTX}\n\nBLIXO holds what?\n\n{_FMT} <value>",
        "score_type": "exact", "answer": "ANSWER: QUAFT",
    },
    "component_checks": [
        {"hop": "maxbi_grulp", "prompt": f"{_SA6_CTX}\n\nMAXBI connects to what?\n\n{_FMT} <value>", "score_type": "exact", "answer": "ANSWER: GRULP"},
        {"hop": "grulp_woxen", "prompt": f"{_SA6_CTX}\n\nGRULP leads to what?\n\n{_FMT} <value>",   "score_type": "exact", "answer": "ANSWER: WOXEN"},
        {"hop": "woxen_norva", "prompt": f"{_SA6_CTX}\n\nWOXEN grants what?\n\n{_FMT} <value>",     "score_type": "exact", "answer": "ANSWER: NORVA"},
    ],
}

_SA7_CTX = (
    "DROFL holds NIXBL. "
    "DRIZP connects to ZARVP. ZARVP leads to KARVO. KARVO grants KRAXI. "
    "TREXN marks ZEPHI."
)
SA7 = {
    "id": "SA7", "family": "S", "role": "PRIMARY_SEAM",
    "relation_skeleton": "S1", "terminal": "KRAXI", "decoy_value": "ZEPHI",
    "included_in_G": True,
    "narrow": {
        "prompt": (f"{_SA7_CTX}\n\n"
                   f"Starting from DRIZP, what terminal value does the chain reach?\n\n"
                   f"{_FMT} <value>"),
        "score_type": "exact", "answer": "ANSWER: KRAXI",
    },
    "broad": {
        "prompt": f"{_SA7_CTX}\n\nDROFL holds what?\n\n{_FMT} <value>",
        "score_type": "exact", "answer": "ANSWER: NIXBL",
    },
    "component_checks": [
        {"hop": "drizp_zarvp", "prompt": f"{_SA7_CTX}\n\nDRIZP connects to what?\n\n{_FMT} <value>", "score_type": "exact", "answer": "ANSWER: ZARVP"},
        {"hop": "zarvp_karvo", "prompt": f"{_SA7_CTX}\n\nZARVP leads to what?\n\n{_FMT} <value>",   "score_type": "exact", "answer": "ANSWER: KARVO"},
        {"hop": "karvo_kraxi", "prompt": f"{_SA7_CTX}\n\nKARVO grants what?\n\n{_FMT} <value>",     "score_type": "exact", "answer": "ANSWER: KRAXI"},
    ],
}

_SA8_CTX = (
    "GRAFI holds LORVX. "
    "TROXB connects to FLUMB. FLUMB leads to NAKVI. NAKVI grants VEFLM. "
    "PLOMV marks WULFT."
)
SA8 = {
    "id": "SA8", "family": "S", "role": "PRIMARY_SEAM",
    "relation_skeleton": "S1", "terminal": "VEFLM", "decoy_value": "WULFT",
    "included_in_G": True,
    "narrow": {
        "prompt": (f"{_SA8_CTX}\n\n"
                   f"Starting from TROXB, what terminal value does the chain reach?\n\n"
                   f"{_FMT} <value>"),
        "score_type": "exact", "answer": "ANSWER: VEFLM",
    },
    "broad": {
        "prompt": f"{_SA8_CTX}\n\nGRAFI holds what?\n\n{_FMT} <value>",
        "score_type": "exact", "answer": "ANSWER: LORVX",
    },
    "component_checks": [
        {"hop": "troxb_flumb", "prompt": f"{_SA8_CTX}\n\nTROXB connects to what?\n\n{_FMT} <value>", "score_type": "exact", "answer": "ANSWER: FLUMB"},
        {"hop": "flumb_nakvi", "prompt": f"{_SA8_CTX}\n\nFLUMB leads to what?\n\n{_FMT} <value>",   "score_type": "exact", "answer": "ANSWER: NAKVI"},
        {"hop": "nakvi_veflm", "prompt": f"{_SA8_CTX}\n\nNAKVI grants what?\n\n{_FMT} <value>",     "score_type": "exact", "answer": "ANSWER: VEFLM"},
    ],
}


# =============================================================================
# DIAGNOSTIC ECHO CONTROLS — DE family (4 items)
# Estimate intermediate-token echo rate under the forced-format scaffold.
# Excluded from G in all cases. Only interpretable if FP16 content passes.
# DE-QE: 1-hop; echo risk = model returns the question anchor entity.
# DE-PI: 2-hop composite; echo risk = model returns penultimate node.
# DE-PI items apply distractor-first/decoy-last to eliminate same context artifact.
# =============================================================================

_DE1_CTX = "ZIXPA leads to ORBUX. KRONB holds VIMPL."
DE1 = {
    "id": "DE1", "family": "DE", "role": "DIAGNOSTIC_ECHO_QE",
    "echo_type": "QE", "echo_wrong_value": "ZIXPA",
    "included_in_G": False, "diagnostic_gate": "fp16_content_pass",
    "narrow": {
        "prompt": f"{_DE1_CTX}\n\nZIXPA leads to what?\n\n{_FMT} <value>",
        "score_type": "exact", "answer": "ANSWER: ORBUX",
    },
    "broad": {
        "prompt": f"{_DE1_CTX}\n\nKRONB holds what?\n\n{_FMT} <value>",
        "score_type": "exact", "answer": "ANSWER: VIMPL",
    },
    "component_checks": [],
}

_DE2_CTX = "FLOXB leads to GRUMV. TRAXO holds WIXPL."
DE2 = {
    "id": "DE2", "family": "DE", "role": "DIAGNOSTIC_ECHO_QE",
    "echo_type": "QE", "echo_wrong_value": "FLOXB",
    "included_in_G": False, "diagnostic_gate": "fp16_content_pass",
    "narrow": {
        "prompt": f"{_DE2_CTX}\n\nFLOXB leads to what?\n\n{_FMT} <value>",
        "score_type": "exact", "answer": "ANSWER: GRUMV",
    },
    "broad": {
        "prompt": f"{_DE2_CTX}\n\nTRAXO holds what?\n\n{_FMT} <value>",
        "score_type": "exact", "answer": "ANSWER: WIXPL",
    },
    "component_checks": [],
}

# DE-PI: distractor first, decoy last — same position-artifact repair as SA items.
_DE3_CTX = (
    "VRAXB holds KLINP. "
    "PLOXN leads to GRIVT. GRIVT grants WOXUR. "
    "XOMBI marks DRUVF."
)
DE3 = {
    "id": "DE3", "family": "DE", "role": "DIAGNOSTIC_ECHO_PI",
    "echo_type": "PI", "echo_wrong_value": "GRIVT",
    "decoy_value": "DRUVF",
    "included_in_G": False, "diagnostic_gate": "fp16_content_pass",
    "narrow": {
        "prompt": (f"{_DE3_CTX}\n\n"
                   f"Starting from PLOXN, what terminal value does the chain reach?\n\n"
                   f"{_FMT} <value>"),
        "score_type": "exact", "answer": "ANSWER: WOXUR",
    },
    "broad": {
        "prompt": f"{_DE3_CTX}\n\nVRAXB holds what?\n\n{_FMT} <value>",
        "score_type": "exact", "answer": "ANSWER: KLINP",
    },
    "component_checks": [
        {"hop": "ploxn_grivt", "prompt": f"{_DE3_CTX}\n\nPLOXN leads to what?\n\n{_FMT} <value>",  "score_type": "exact", "answer": "ANSWER: GRIVT"},
        {"hop": "grivt_woxur", "prompt": f"{_DE3_CTX}\n\nGRIVT grants what?\n\n{_FMT} <value>",    "score_type": "exact", "answer": "ANSWER: WOXUR"},
    ],
}

_DE4_CTX = (
    "FLONB holds TAXGR. "
    "ZOMPL leads to VRAXI. VRAXI grants BLIXT. "
    "KORNU marks VAXLM."
)
DE4 = {
    "id": "DE4", "family": "DE", "role": "DIAGNOSTIC_ECHO_PI",
    "echo_type": "PI", "echo_wrong_value": "VRAXI",
    "decoy_value": "VAXLM",
    "included_in_G": False, "diagnostic_gate": "fp16_content_pass",
    "narrow": {
        "prompt": (f"{_DE4_CTX}\n\n"
                   f"Starting from ZOMPL, what terminal value does the chain reach?\n\n"
                   f"{_FMT} <value>"),
        "score_type": "exact", "answer": "ANSWER: BLIXT",
    },
    "broad": {
        "prompt": f"{_DE4_CTX}\n\nFLONB holds what?\n\n{_FMT} <value>",
        "score_type": "exact", "answer": "ANSWER: TAXGR",
    },
    "component_checks": [
        {"hop": "zompl_vraxi", "prompt": f"{_DE4_CTX}\n\nZOMPL leads to what?\n\n{_FMT} <value>",  "score_type": "exact", "answer": "ANSWER: VRAXI"},
        {"hop": "vraxi_blixt", "prompt": f"{_DE4_CTX}\n\nVRAXI grants what?\n\n{_FMT} <value>",    "score_type": "exact", "answer": "ANSWER: BLIXT"},
    ],
}


# =============================================================================
# NULL CONTROL — NC family (1 item)
# Absent anchor (VIXOM) and expected answer (BAXNU) are not in NC1's context.
# Validates content_slot_score returns 0 when expected token is absent.
# Flag condition: if content=1 at any rung, halt — scorer audit required.
# =============================================================================

_NC1_CTX = "PIXNV leads to GRAXB. NAXBI holds ZULNX."
NC1 = {
    "id": "NC1", "family": "NC", "role": "NULL_CONTROL",
    "included_in_G": False,
    "expected_fp16_content": 0, "flag_if_content_nonzero": True,
    "narrow": {
        "prompt": (f"{_NC1_CTX}\n\n"
                   f"Starting from VIXOM, what terminal value does the chain reach?\n\n"
                   f"{_FMT} <value>"),
        "score_type": "exact", "answer": "ANSWER: BAXNU",
    },
    "broad": {
        "prompt": f"{_NC1_CTX}\n\nNAXBI holds what?\n\n{_FMT} <value>",
        "score_type": "exact", "answer": "ANSWER: ZULNX",
    },
    "component_checks": [],
}


# =============================================================================
# ATOMIC CONTROLS — AC family (2 items)
# 1-hop sanity checks. Decoy fact last to eliminate AC-level last-value anchoring.
# Narrow and broad ask about different entities in the same context.
# Excluded from G metrics.
# =============================================================================

_AC1_CTX = "NOXBA holds GRUVL. PRAXE holds WUMFT. SORNI marks BLIVX."
AC1 = {
    "id": "AC1", "family": "AC", "role": "ATOMIC_CONTROL",
    "decoy_value": "BLIVX",
    "included_in_G": False,
    "narrow": {
        "prompt": f"{_AC1_CTX}\n\nNOXBA holds what?\n\n{_FMT} <value>",
        "score_type": "exact", "answer": "ANSWER: GRUVL",
    },
    "broad": {
        "prompt": f"{_AC1_CTX}\n\nPRAXE holds what?\n\n{_FMT} <value>",
        "score_type": "exact", "answer": "ANSWER: WUMFT",
    },
    "component_checks": [],
}

_AC2_CTX = "KLOMR holds DRIXP. BIXTV holds WUNFA. ZARPL marks KLONB."
AC2 = {
    "id": "AC2", "family": "AC", "role": "ATOMIC_CONTROL",
    "decoy_value": "KLONB",
    "included_in_G": False,
    "narrow": {
        "prompt": f"{_AC2_CTX}\n\nKLOMR holds what?\n\n{_FMT} <value>",
        "score_type": "exact", "answer": "ANSWER: DRIXP",
    },
    "broad": {
        "prompt": f"{_AC2_CTX}\n\nBIXTV holds what?\n\n{_FMT} <value>",
        "score_type": "exact", "answer": "ANSWER: WUNFA",
    },
    "component_checks": [],
}


# =============================================================================
# PAIRS — full task list (15 items)
# G computed over SA1–SA8 only (included_in_G=True).
# =============================================================================
PAIRS = [
    SA1, SA2, SA3, SA4, SA5, SA6, SA7, SA8,  # primary seam items (n=8)
    DE1, DE2, DE3, DE4,                        # diagnostic echo controls (n=4)
    NC1,                                        # null / scorer validation (n=1)
    AC1, AC2,                                   # atomic controls (n=2)
]


# =============================================================================
# STATIC VALIDATION
# Run before FP16 stability screen: python3 tasks_exp7.py
# All checks must pass. Manifest hash emitted with report.
# =============================================================================

def _all_caps_tokens(text: str):
    """Return list of all 4+-char ALL-CAPS tokens in order of appearance."""
    return re.findall(r'\b[A-Z]{4,}\b', text)


def validate_tasks():
    errors = []

    def fail(check, msg):
        errors.append((check, msg))

    # ------------------------------------------------------------------
    # Token pool definitions (registered pools for disjointness checks)
    # ------------------------------------------------------------------
    PRIMARY_TERMINALS  = {"FAVOX", "PLONX", "WEXBI", "ZULPA", "DRIXM", "NORVA", "KRAXI", "VEFLM"}
    NULL_TERMINAL      = {"BAXNU"}
    DIAG_TERMINALS     = {"WOXUR", "BLIXT"}
    SA_DECOY_VALUES    = {"SLOMX", "VARGN", "DUPLX", "YOMBL", "RAXLV", "BROXN", "ZEPHI", "WULFT"}
    SA_BROAD_VALUES    = {"GROXL", "FLIPN", "BUVAX", "KRAZM", "WOVLU", "QUAFT", "NIXBL", "LORVX"}
    DE_BROAD_VALUES    = {"VIMPL", "WIXPL", "KLINP", "TAXGR"}
    NC_BROAD_VALUE     = {"ZULNX"}
    AC_NARROW_ANSWERS  = {"GRUVL", "DRIXP"}
    AC_BROAD_ANSWERS   = {"WUMFT", "WUNFA"}
    AC_DECOY_VALUES    = {"BLIVX", "KLONB"}
    DE_PI_DECOY_VALUES = {"DRUVF", "VAXLM"}
    SA_INTERMEDIATES   = {
        "GRIXP", "VUNLB", "MEXOT",
        "DRALX", "KLOMF", "ZAPVI",
        "BLUXN", "WIVOT", "FROPK",
        "SKRON", "PAMVL", "XOTBI",
        "VOMPL", "JAXOL", "GLIVN",
        "MAXBI", "GRULP", "WOXEN",
        "DRIZP", "ZARVP", "KARVO",
        "TROXB", "FLUMB", "NAKVI",
    }
    DE_NODES = {"ZIXPA", "ORBUX", "FLOXB", "GRUMV", "PLOXN", "GRIVT", "ZOMPL", "VRAXI"}

    ALL_POOLS = [
        ("PRIMARY_TERMINALS",  PRIMARY_TERMINALS),
        ("NULL_TERMINAL",      NULL_TERMINAL),
        ("DIAG_TERMINALS",     DIAG_TERMINALS),
        ("SA_DECOY_VALUES",    SA_DECOY_VALUES),
        ("SA_BROAD_VALUES",    SA_BROAD_VALUES),
        ("DE_BROAD_VALUES",    DE_BROAD_VALUES),
        ("NC_BROAD_VALUE",     NC_BROAD_VALUE),
        ("AC_NARROW_ANSWERS",  AC_NARROW_ANSWERS),
        ("AC_BROAD_ANSWERS",   AC_BROAD_ANSWERS),
        ("AC_DECOY_VALUES",    AC_DECOY_VALUES),
        ("DE_PI_DECOY_VALUES", DE_PI_DECOY_VALUES),
        ("SA_INTERMEDIATES",   SA_INTERMEDIATES),
        ("DE_NODES",           DE_NODES),
    ]

    # ------------------------------------------------------------------
    # Check: decoy_pool_disjoint_from_all_answer_value_pools
    # ------------------------------------------------------------------
    for i, (name_a, pool_a) in enumerate(ALL_POOLS):
        for name_b, pool_b in ALL_POOLS[i + 1:]:
            overlap = pool_a & pool_b
            if overlap:
                fail("decoy_pool_disjoint_from_all_answer_value_pools",
                     f"{name_a} ∩ {name_b} = {overlap}")

    # ------------------------------------------------------------------
    # Bucket integrity: SA items included_in_G=True; DE/NC/AC=False
    # ------------------------------------------------------------------
    for p in PAIRS:
        fam = p.get("family")
        ing = p.get("included_in_G", True)
        if fam == "S" and not ing:
            fail("bucket_integrity", f"{p['id']}: SA item has included_in_G=False")
        if fam in ("DE", "NC", "AC") and ing:
            fail("bucket_integrity", f"{p['id']}: {fam} item has included_in_G=True")
        if fam not in ("S", "DE", "NC", "AC"):
            fail("bucket_integrity", f"{p['id']}: unrecognized family={fam!r}")

    # ------------------------------------------------------------------
    # SA-item checks
    # ------------------------------------------------------------------
    sa_items = [p for p in PAIRS if p.get("family") == "S"]
    s1_verbs = ("connects to", "leads to", "grants")
    s2_markers = ("routes to", "opens into", "maps to")

    for p in sa_items:
        pid = p["id"]
        ctx = p["narrow"]["prompt"].split("\n\n")[0]
        terminal  = p.get("terminal", "")
        decoy_val = p.get("decoy_value", "")
        caps = _all_caps_tokens(ctx)

        # terminal_not_first_all_caps
        if caps and caps[0] == terminal:
            fail("terminal_not_first_all_caps",
                 f"{pid}: terminal {terminal!r} is first ALL-CAPS token in context")

        # terminal_not_last_all_caps
        if caps and caps[-1] == terminal:
            fail("terminal_not_last_all_caps",
                 f"{pid}: terminal {terminal!r} is last ALL-CAPS token in context")

        # last_all_caps_is_registered_decoy
        if not decoy_val:
            fail("last_all_caps_is_registered_decoy",
                 f"{pid}: no decoy_value field registered")
        elif caps and caps[-1] != decoy_val:
            fail("last_all_caps_is_registered_decoy",
                 f"{pid}: last ALL-CAPS={caps[-1]!r}, registered decoy={decoy_val!r}")

        # distractor_fact_first: context starts with "WORD holds WORD."
        if not re.match(r'^[A-Z]{4,} holds [A-Z]{4,}\.', ctx):
            fail("distractor_fact_first",
                 f"{pid}: context does not start with 'ENTITY holds VALUE.'")

        # decoy_fact_last: context ends with "WORD marks WORD."
        if not re.search(r'[A-Z]{4,} marks [A-Z]{4,}\.$', ctx):
            fail("decoy_fact_last",
                 f"{pid}: context does not end with 'ENTITY marks VALUE.'")

        # S1_skeleton_uniformity: all three S1 verbs present; no S2 verbs
        for verb in s1_verbs:
            if verb not in ctx:
                fail("S1_skeleton_uniformity",
                     f"{pid}: S1 verb '{verb}' not found in context")
        for verb in s2_markers:
            if verb in ctx:
                fail("S1_skeleton_uniformity",
                     f"{pid}: S2 verb '{verb}' found in context")

        # anchor_matches_hop1_subject
        narrow_q = p["narrow"]["prompt"].split("\n\n")[1]
        m_anchor = re.search(r"Starting from ([A-Z]{4,})", narrow_q)
        if not m_anchor:
            fail("anchor_matches_hop1_subject",
                 f"{pid}: could not parse anchor from composite prompt")
        elif p.get("component_checks"):
            comp0_q = p["component_checks"][0]["prompt"].split("\n\n")[1]
            m_hop1 = re.search(r"([A-Z]{4,}) connects to what\?", comp0_q)
            if not m_hop1:
                fail("anchor_matches_hop1_subject",
                     f"{pid}: could not parse hop1 subject from component[0] prompt")
            elif m_anchor.group(1) != m_hop1.group(1):
                fail("anchor_matches_hop1_subject",
                     f"{pid}: composite anchor={m_anchor.group(1)!r}, "
                     f"hop1 subject={m_hop1.group(1)!r}")

        # SA_has_exactly_3_components
        n_comps = len(p.get("component_checks", []))
        if n_comps != 3:
            fail("SA_has_exactly_3_components",
                 f"{pid}: has {n_comps} component check(s), expected 3")

    # ------------------------------------------------------------------
    # NC_expected_answer_absent_from_all_contexts
    # BAXNU (expected answer) and VIXOM (absent anchor) must not appear
    # in any item's context string.
    # ------------------------------------------------------------------
    nc_absent = {"BAXNU", "VIXOM"}
    for p in PAIRS:
        ctx = p["narrow"]["prompt"].split("\n\n")[0]
        for tok in nc_absent:
            if tok in ctx:
                fail("NC_expected_answer_absent_from_all_contexts",
                     f"{p['id']}: NC-absent token {tok!r} found in context")

    # ------------------------------------------------------------------
    # Manifest hash
    # ------------------------------------------------------------------
    src = Path(__file__).read_text(encoding="utf-8")
    manifest_hash = hashlib.sha256(src.encode("utf-8")).hexdigest()

    # ------------------------------------------------------------------
    # Report
    # ------------------------------------------------------------------
    all_checks = [
        "terminal_not_first_all_caps",
        "terminal_not_last_all_caps",
        "last_all_caps_is_registered_decoy",
        "decoy_pool_disjoint_from_all_answer_value_pools",
        "distractor_fact_first",
        "decoy_fact_last",
        "S1_skeleton_uniformity",
        "anchor_matches_hop1_subject",
        "SA_has_exactly_3_components",
        "NC_expected_answer_absent_from_all_contexts",
        "bucket_integrity",
    ]
    failed_checks = {check for check, _ in errors}

    print("=== tasks_exp7.py static validation ===\n")
    for check in all_checks:
        status = "FAIL" if check in failed_checks else "PASS"
        print(f"  [{status}] {check}")

    print(f"\n  manifest_hash: sha256:{manifest_hash}")

    if errors:
        print(f"\n{len(errors)} validation error(s):\n")
        for check, msg in errors:
            print(f"  FAIL [{check}]: {msg}")
        sys.exit(1)
    else:
        print(f"\nAll {len(all_checks)} checks passed.")
        print("Hash this line before running the stability screen:")
        print(f"  sha256:{manifest_hash}")


if __name__ == "__main__":
    validate_tasks()
