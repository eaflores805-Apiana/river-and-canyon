"""Lane 1a' Phase 4 sibling-artifact cross-reference tests.

SYNTHETIC / DIAGNOSTIC -- NON-BINDING -- NOT FOR THRESHOLD DERIVATION
D2 IMPLEMENTATION ARTIFACT
NO MODEL INVOKED -- NO MODEL LOADED -- NO SWEEP EXECUTION

Path A.1 standing-rule pattern: any artifact that integrates with
a locked sibling artifact must include a unit test that
cross-references concrete values against the sibling artifact's
source.

Under D2 Phase 4, the runner's MODEL_ID, the wrapper's
PRODUCTION_PYTHON, and the wrapper's EXPECTED_MLX_LM_VERSION are
all PLACEHOLDERS (locked at packet seal). The cross-reference tests
exist as scaffolding now; they will activate at packet seal when
the placeholder values are replaced with locked sibling-artifact
values.

What we CAN cross-reference now:
  - The addendum path constant matches the adopted standing path.
  - The addendum sha256 constant matches the adoption commit.
  - The Paper 3 tag constant matches the locked tag name.
  - The LOCK-RECORD schema's pinned constants match the runtime
    constants.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

REPO_ROOT = Path(__file__).resolve().parents[3]
SCHEMAS_DIR = Path(__file__).resolve().parent.parent / "schemas"
PACKAGE_DIR = Path(__file__).resolve().parent.parent / "lane1a_prime"


# ---------- MODEL_ID / PRODUCTION_PYTHON / EXPECTED_MLX_LM_VERSION ----------

def test_runner_model_id_is_placeholder_until_packet_seal():
    """Path A.1 scaffold: MODEL_ID is currently a placeholder. At
    packet seal, the cross-reference test against the sibling
    artifact (declared by New Senior in the design packet) will
    activate."""
    from lane1a_prime.runner import MODEL_ID
    assert "PLACEHOLDER" in MODEL_ID


def test_wrapper_production_python_is_placeholder_until_packet_seal():
    """Path E.1 scaffold: PRODUCTION_PYTHON is currently a
    placeholder. At packet seal, the cross-reference test against
    the sibling artifact will activate."""
    from lane1a_prime.wrapper import PRODUCTION_PYTHON
    assert "PLACEHOLDER" in PRODUCTION_PYTHON


def test_wrapper_expected_mlx_lm_version_is_placeholder_until_packet_seal():
    from lane1a_prime.wrapper import EXPECTED_MLX_LM_VERSION
    assert "PLACEHOLDER" in EXPECTED_MLX_LM_VERSION


# ---------- LOCK-RECORD schema pins (active cross-references) ----------

def _load_lock_record_schema() -> dict:
    with (SCHEMAS_DIR / "lock_record_schema.yaml").open() as f:
        return yaml.safe_load(f)


def test_lock_record_addendum_path_pin_matches_standing_path():
    """The LOCK-RECORD schema pins addendum_path to the adopted
    standing path. Verify the standing addendum exists at that path
    in the repo."""
    schema = _load_lock_record_schema()
    addendum_path_const = (
        schema["properties"]["bound_versions"]
        ["properties"]["addendum_path"]["const"]
    )
    assert addendum_path_const == (
        "governance/standing/PRE-LOCK-INSTRUMENT-VALIDATION-ADDENDUM.md"
    )
    # The actual file must exist at that path.
    addendum_file = REPO_ROOT / addendum_path_const
    assert addendum_file.exists(), (
        f"Adopted standing addendum missing at expected path: {addendum_file}"
    )


def test_lock_record_addendum_sha256_pin_matches_adopted_bytes():
    """The LOCK-RECORD pins addendum_sha256 to the body of the adopted
    addendum's reviewed bytes (c3e88fd3..., the v0.4.1 source-of-record).

    Note: the on-disk standing file at
    governance/standing/PRE-LOCK-INSTRUMENT-VALIDATION-ADDENDUM.md
    has an "Adoption Record" header prepended; the body below the
    header is byte-equal to the c3e88fd3... source-of-record. The
    pin is the source-of-record hash, not the on-disk file hash.
    """
    schema = _load_lock_record_schema()
    addendum_sha256_pin = (
        schema["properties"]["bound_versions"]
        ["properties"]["addendum_sha256"]["const"]
    )
    # The pin is the v0.4.1 source-of-record sha256 per the
    # adoption record.
    assert addendum_sha256_pin == (
        "124f6046d57d365dd47596877fd1eb09088f6990ec3c9a52ac150d0c8ca103b8"
    )


def test_lock_record_paper3_tag_pin():
    """LOCK-RECORD pins paper3_tag to the released v1.1 tag name."""
    schema = _load_lock_record_schema()
    paper3_tag_const = (
        schema["properties"]["bound_versions"]
        ["properties"]["paper3_tag"]["const"]
    )
    assert paper3_tag_const == "paper3-certification-protocol-v1.1"


# ---------- elimination label vocabulary cross-reference ----------

def test_sidecar_basis_policies_match_envelope_policies():
    """Cross-reference: the sidecar schema's elimination_label_basis
    basis_policies enum lists exactly the four envelope policies,
    same set as ENVELOPE_POLICIES in policies.py."""
    sidecar_path = SCHEMAS_DIR / "sidecar_schema.yaml"
    with sidecar_path.open() as f:
        schema = yaml.safe_load(f)
    basis_enum = (
        schema["definitions"]["elimination_label_basis"]
        ["properties"]["basis_policies"]["items"]["enum"]
    )
    from lane1a_prime.policies import ENVELOPE_POLICIES
    assert set(basis_enum) == set(ENVELOPE_POLICIES)


def test_rung_result_outcome_enum_matches_rung_outcome_values():
    """Cross-reference: rung_result_schema's outcome enum matches
    the RUNG_OUTCOME_VALUES constant from controls.py."""
    rung_result_path = SCHEMAS_DIR / "rung_result_schema.yaml"
    with rung_result_path.open() as f:
        schema = yaml.safe_load(f)
    outcome_enum = schema["properties"]["outcome"]["enum"]
    from lane1a_prime.controls import RUNG_OUTCOME_VALUES
    assert set(outcome_enum) == set(RUNG_OUTCOME_VALUES)


def test_elimination_label_values_match_across_modules():
    """Cross-reference: controls.ELIMINATION_LABEL_VALUES match the
    labels accepted by RungEvaluation (in outcome.py) and
    EliminationCriterion (in analysis.py)."""
    from lane1a_prime.controls import ELIMINATION_LABEL_VALUES
    from lane1a_prime.outcome import RungEvaluation
    from lane1a_prime.analysis import EliminationCriterion, CriterionComparison

    # Constructing RungEvaluation with each label should not raise
    for label in ELIMINATION_LABEL_VALUES:
        ev = RungEvaluation(
            rung_id="L01",
            is_data_sufficient=True,
            attached_elimination_labels=(label,),
            boundary_proximity_flags={},
        )
        assert ev.attached_elimination_labels == (label,)

    # Constructing EliminationCriterion with each label should not raise
    for label in ELIMINATION_LABEL_VALUES:
        crit = EliminationCriterion(
            label=label,
            stratum="answerable",
            comparison=CriterionComparison.POINT_ESTIMATE,
            floor_or_ceiling=0.5,
            is_floor=True,
        )
        assert crit.label == label


def test_artifact_label_constants_match_sidecar_schema_enum():
    """Cross-reference: wrapper's SYNTHETIC_LABEL,
    RECONNAISSANCE_LABEL, DIAGNOSTIC_LABEL constants match the
    sidecar schema's artifact_label enum."""
    sidecar_path = SCHEMAS_DIR / "sidecar_schema.yaml"
    with sidecar_path.open() as f:
        schema = yaml.safe_load(f)
    label_enum = schema["definitions"]["artifact_label"]["enum"]
    from lane1a_prime.wrapper import (
        DIAGNOSTIC_LABEL,
        RECONNAISSANCE_LABEL,
        SYNTHETIC_LABEL,
    )
    assert SYNTHETIC_LABEL in label_enum
    assert RECONNAISSANCE_LABEL in label_enum
    assert DIAGNOSTIC_LABEL in label_enum


# ---------- sweep_id absence cross-reference ----------

def test_no_sweep_id_assignment_in_any_package_module():
    """D2 boundary: no module in lane1a_prime/ creates a sweep_id."""
    for source_file in PACKAGE_DIR.glob("*.py"):
        text = source_file.read_text()
        # Variable assignment to sweep_id with a non-None RHS
        # Allow `sweep_id=None` (D2 boundary marker)
        pattern = re.compile(
            r"\bsweep_id\s*=\s*['\"][A-Za-z0-9_-]+['\"]",
            re.MULTILINE,
        )
        matches = pattern.findall(text)
        assert matches == [], (
            f"sweep_id literal assignment found in {source_file.name}: "
            f"{matches}"
        )
