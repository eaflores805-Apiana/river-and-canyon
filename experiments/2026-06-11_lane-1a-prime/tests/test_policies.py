"""Lane 1a' Phase 2 policy tests.

SYNTHETIC / DIAGNOSTIC -- NON-BINDING -- NOT FOR THRESHOLD DERIVATION
D2 IMPLEMENTATION ARTIFACT
NO MODEL INVOKED -- NO SWEEP_ID CREATED -- NO SWEEP EXECUTION AUTHORIZED

Validates:
  - PolicyInputView DE-1 blinding (queried key not in public attributes)
  - Five policy implementations:
      pure_last_position, salient_endpoint (position-based, no exclusion)
      recency_excluding_target, prefix_neighbor_confusion (identity-based, queried-key excluded)
      copy_completion (diagnostic-only, uses DiagnosticInputView)
  - prefix_neighbor_confusion 4-clause total function
  - Zero-self-match on synthetic ideal-retriever oracle for identity-based policies
  - copy_completion uses DiagnosticInputView, not PolicyInputView
  - No `fails` token in policies.py source
"""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

# Make the lane1a_prime package importable from this test file.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from lane1a_prime.policies import (  # noqa: E402
    DIAGNOSTIC_POLICIES,
    DiagnosticInputView,
    ENVELOPE_POLICIES,
    ManifestPair,
    PolicyInputView,
    PolicyOutput,
    build_diagnostic_input_view,
    build_policy_input_view,
    copy_completion,
    prefix_neighbor_confusion,
    pure_last_position,
    recency_excluding_target,
    salient_endpoint,
)

POLICIES_SOURCE = (Path(__file__).resolve().parent.parent / "lane1a_prime" / "policies.py").read_text()


# ---------- PolicyInputView DE-1 blinding ----------

def _make_view(pairs: list[tuple[tuple[int, ...], tuple[int, ...]]],
               queried_key: tuple[int, ...]) -> PolicyInputView:
    return PolicyInputView(
        record_id="r-001",
        pairs=tuple(ManifestPair(key_token_ids=k, value_token_ids=v) for k, v in pairs),
        queried_key_token_ids=queried_key,
        real_pair_block_indices=(0, len(pairs)),
    )


def _make_diagnostic_view(pairs, queried_key) -> DiagnosticInputView:
    return DiagnosticInputView(
        record_id="r-001",
        pairs=tuple(ManifestPair(key_token_ids=k, value_token_ids=v) for k, v in pairs),
        queried_key_token_ids=queried_key,
        real_pair_block_indices=(0, len(pairs)),
    )


def test_policy_input_view_does_not_expose_queried_key_as_public_attribute():
    """DE-1 closure: queried_key_token_ids is NOT a public attribute
    of PolicyInputView. Public attributes (without leading underscore)
    do not include any name matching queried_key or queried_key_token_ids."""
    view = _make_view([((1,), (10,)), ((2,), (20,))], queried_key=(1,))
    public_attrs = [a for a in dir(view) if not a.startswith("_")]
    assert "queried_key_token_ids" not in public_attrs
    assert "queried_key" not in public_attrs


def test_policy_input_view_exposes_filtered_candidates():
    view = _make_view(
        [((1,), (10,)), ((2,), (20,)), ((3,), (30,))],
        queried_key=(2,),
    )
    candidates = view.candidates_excluding_queried_key
    # Queried key (2,) is filtered out
    candidate_keys = [c.key_token_ids for c in candidates]
    assert (2,) not in candidate_keys
    assert (1,) in candidate_keys
    assert (3,) in candidate_keys


def test_policy_input_view_pairs_unfiltered():
    """The .pairs property exposes the full sequence (for
    position-based policies)."""
    view = _make_view(
        [((1,), (10,)), ((2,), (20,))],
        queried_key=(2,),
    )
    pair_keys = [p.key_token_ids for p in view.pairs]
    # Queried key (2,) is still in .pairs (position-based access)
    assert (2,) in pair_keys


def test_policy_input_view_queried_key_length_without_value():
    view = _make_view([((1,), (10,))], queried_key=(5, 6, 7))
    assert view.queried_key_length == 3


def test_prefix_distance_method_does_not_reveal_queried_key():
    """The prefix_distance_to_queried_key method returns a number;
    callers cannot recover the queried key from it."""
    view = _make_view([((1,), (10,))], queried_key=(7, 8, 9))
    # Distance from a candidate to the queried key
    assert view.prefix_distance_to_queried_key((7, 8, 9)) == 0  # perfect (only the queried key itself)
    assert view.prefix_distance_to_queried_key((7, 8, 0)) == 1  # 2 common
    assert view.prefix_distance_to_queried_key((7,)) == 2       # 1 common
    assert view.prefix_distance_to_queried_key((9,)) == 3       # 0 common


# ---------- pure_last_position ----------

def test_pure_last_position_returns_last_pair_value():
    view = _make_view([((1,), (10,)), ((2,), (20,)), ((3,), (30,))], queried_key=(1,))
    output = pure_last_position(view)
    assert output.policy_name == "pure_last_position"
    assert output.predicted_value_token_ids == (30,)


def test_pure_last_position_no_match_on_empty_pairs():
    view = _make_view([], queried_key=(1,))
    output = pure_last_position(view)
    assert output.is_no_match


# ---------- salient_endpoint ----------

def test_salient_endpoint_default_position_zero():
    view = _make_view([((1,), (10,)), ((2,), (20,))], queried_key=(99,))
    output = salient_endpoint(view)
    assert output.predicted_value_token_ids == (10,)


def test_salient_endpoint_with_specified_position():
    view = _make_view([((1,), (10,)), ((2,), (20,)), ((3,), (30,))], queried_key=(99,))
    output = salient_endpoint(view, endpoint_position=2)
    assert output.predicted_value_token_ids == (30,)


def test_salient_endpoint_out_of_range_is_no_match():
    view = _make_view([((1,), (10,))], queried_key=(99,))
    output = salient_endpoint(view, endpoint_position=5)
    assert output.is_no_match


# ---------- recency_excluding_target ----------

def test_recency_excluding_target_returns_most_recent_non_queried():
    """When queried key (2,) is at the last position, recency_excluding_target
    must NOT return its value. Returns the previous pair's value instead."""
    view = _make_view(
        [((1,), (10,)), ((3,), (30,)), ((2,), (20,))],
        queried_key=(2,),
    )
    output = recency_excluding_target(view)
    # Queried key (2,) excluded; most recent of remainder is (3,) -> (30,)
    assert output.predicted_value_token_ids == (30,)


def test_recency_excluding_target_zero_self_match_on_ideal_retriever_oracle():
    """Synthetic ideal-retriever oracle: queried key at last position
    with gold = queried_key's value. recency_excluding_target must
    return a DIFFERENT value (not the gold) by exclusion."""
    queried_key = (5,)
    gold_value = (50,)
    view = _make_view(
        [((1,), (10,)), ((2,), (20,)), (queried_key, gold_value)],
        queried_key=queried_key,
    )
    output = recency_excluding_target(view)
    assert output.predicted_value_token_ids != gold_value


def test_recency_excluding_target_no_match_when_only_queried_key():
    view = _make_view([((1,), (10,))], queried_key=(1,))
    output = recency_excluding_target(view)
    assert output.is_no_match


# ---------- prefix_neighbor_confusion four-clause total function ----------

def test_prefix_neighbor_confusion_clause1_excludes_self_match():
    """Clause (1): queried-key self-match excluded by tuple-equality."""
    queried_key = (1, 2, 3)
    gold_value = (100,)
    view = _make_view(
        [((1, 2, 3), gold_value), ((1, 2, 9), (200,)), ((4, 5, 6), (300,))],
        queried_key=queried_key,
    )
    output = prefix_neighbor_confusion(view)
    # Queried key (1,2,3) is excluded; nearest neighbor is (1,2,9)
    # -> distance = 3 - 2 = 1
    assert output.predicted_value_token_ids != gold_value
    assert output.predicted_value_token_ids == (200,)


def test_prefix_neighbor_confusion_clause2_tie_break_most_recent():
    """Clause (2): ties resolve to most-recent neighbor (highest index)."""
    queried_key = (1, 2, 3)
    # Two candidates with equal prefix distance (1 from queried key)
    view = _make_view(
        [
            ((1, 2, 7), (100,)),  # idx 0; distance 1
            ((4, 5, 6), (999,)),  # idx 1; distance 3 (no shared prefix)
            ((1, 2, 8), (200,)),  # idx 2; distance 1
        ],
        queried_key=queried_key,
    )
    output = prefix_neighbor_confusion(view)
    # Most recent of the two tied (distance=1) candidates is idx 2 -> (200,)
    assert output.predicted_value_token_ids == (200,)


def test_prefix_neighbor_confusion_clause3_no_match_when_no_eligible_neighbor():
    """Clause (3): no eligible shared-prefix neighbor -> declared
    no-match output."""
    queried_key = (1, 2, 3)
    view = _make_view(
        [((9, 9, 9), (100,)), ((8, 8, 8), (200,))],
        queried_key=queried_key,
    )
    output = prefix_neighbor_confusion(view)
    assert output.is_no_match


def test_prefix_neighbor_confusion_clause4_no_match_outside_envelope():
    """Clause (4): no-match output (None predicted_value_token_ids)
    signals 'contributes nothing to envelope'. The envelope aggregator
    must skip is_no_match outputs."""
    view = _make_view([], queried_key=(1, 2, 3))
    output = prefix_neighbor_confusion(view)
    assert output.is_no_match
    # is_no_match property is the structural signal for the envelope
    # aggregator to skip this output.


def test_prefix_neighbor_confusion_zero_self_match_on_ideal_retriever_oracle():
    """Synthetic ideal-retriever oracle: queried key in candidates
    (excluded by clause 1); prefix_neighbor_confusion never returns
    the queried key's value."""
    queried_key = (5, 6, 7)
    gold_value = (500,)
    view = _make_view(
        [((5, 6, 7), gold_value), ((5, 6, 8), (600,)), ((9, 9, 9), (700,))],
        queried_key=queried_key,
    )
    output = prefix_neighbor_confusion(view)
    assert output.predicted_value_token_ids != gold_value


# ---------- copy_completion (diagnostic; uses DiagnosticInputView) ----------

def test_copy_completion_takes_diagnostic_input_view():
    """copy_completion's type signature is DiagnosticInputView, not
    PolicyInputView. This is the structural protection that prevents
    accidental envelope inclusion."""
    # Resolve string annotations (from __future__ import annotations)
    # to actual types.
    from typing import get_type_hints
    hints = get_type_hints(copy_completion)
    assert hints["view"] is DiagnosticInputView


def test_copy_completion_echoes_queried_key():
    view = _make_diagnostic_view(
        [((1,), (10,))],
        queried_key=(5, 6, 7),
    )
    output = copy_completion(view)
    assert output.predicted_value_token_ids == (5, 6, 7)


def test_copy_completion_in_diagnostic_policies_registry():
    assert "copy_completion" in DIAGNOSTIC_POLICIES


def test_copy_completion_not_in_envelope_policies_registry():
    """AL-Q4 closure: copy_completion is OUTSIDE the union envelope.
    Its name does not appear in the ENVELOPE_POLICIES tuple."""
    assert "copy_completion" not in ENVELOPE_POLICIES


# ---------- envelope-policy registry ----------

def test_envelope_policies_registry_has_four_entries():
    assert len(ENVELOPE_POLICIES) == 4
    assert "pure_last_position" in ENVELOPE_POLICIES
    assert "salient_endpoint" in ENVELOPE_POLICIES
    assert "recency_excluding_target" in ENVELOPE_POLICIES
    assert "prefix_neighbor_confusion" in ENVELOPE_POLICIES


def test_envelope_policies_excludes_control_names():
    """DE-2 schema-side closure: control names never appear in the
    envelope-policy registry."""
    assert "scrambled_binding_retrieval" not in ENVELOPE_POLICIES
    assert "unconditioned_token_prior" not in ENVELOPE_POLICIES


# ---------- build_*_input_view helper ----------

VALID_RECORD = {
    "context_block": {
        "real_pair_block": {
            "start_idx": 0,
            "end_idx": 2,
            "pairs": [
                {"key_token_ids": [1], "value_token_ids": [10]},
                {"key_token_ids": [2], "value_token_ids": [20]},
            ],
        },
    },
    "queried_key": {"key_token_ids": [1]},
}


def test_build_policy_input_view_filters_queried_key_into_candidates():
    view = build_policy_input_view(VALID_RECORD)
    candidate_keys = [c.key_token_ids for c in view.candidates_excluding_queried_key]
    assert (1,) not in candidate_keys
    assert (2,) in candidate_keys


def test_build_diagnostic_input_view_exposes_queried_key():
    view = build_diagnostic_input_view(VALID_RECORD)
    assert view.queried_key_token_ids == (1,)


# ---------- source-level invariants ----------

def test_no_fails_token_in_policies_source():
    """No `fails` token in policies.py source. Closes the joint
    disposition rule (descriptive labels only; no fails-shaped vocab)
    at the source-code level."""
    # Tokenize by simple substring; case-insensitive.
    # We allow only documentation references to v1's "self-match"
    # phenomenon, not "fails" vocab. The source should be clean.
    assert "fails" not in POLICIES_SOURCE.lower(), (
        "`fails` token found in policies.py source"
    )


def test_no_passes_token_in_policies_source():
    """No `passes_` token in policies.py source. Closes the
    no-survivor-ranking doctrine at the source-code level."""
    # Allow regular English words containing `pass` (e.g., "passes" is
    # a normal verb). The strict check is for the prefix `passes_`
    # which would only appear as a label-shaped identifier.
    assert "passes_" not in POLICIES_SOURCE, (
        "`passes_` identifier found in policies.py source"
    )


def test_policies_source_does_not_reference_private_queried_key_outside_view_class():
    """Source-level grep: no policy function accesses view._queried_key.
    Only the PolicyInputView class methods may reference the private
    attribute. Policy functions must use the public interface only.
    """
    # Find the PolicyInputView class definition's span
    class_marker = "class PolicyInputView:"
    end_marker = "\nclass DiagnosticInputView:"
    start = POLICIES_SOURCE.find(class_marker)
    end = POLICIES_SOURCE.find(end_marker)
    assert start != -1 and end != -1
    inside_class = POLICIES_SOURCE[start:end]
    outside_class = POLICIES_SOURCE[:start] + POLICIES_SOURCE[end:]
    # The private attribute name may appear inside the PolicyInputView
    # class (where it is defined) but MUST NOT appear in policy
    # function bodies outside the class.
    assert "self._queried_key" in inside_class
    assert "._queried_key" not in outside_class, (
        "private queried-key attribute referenced outside PolicyInputView class"
    )
