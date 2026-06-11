"""Lane 1a' policy modules.

SYNTHETIC / DIAGNOSTIC -- NON-BINDING -- NOT FOR THRESHOLD DERIVATION
D2 IMPLEMENTATION ARTIFACT (PHASE 2)
NO MODEL INVOKED -- NO SWEEP_ID CREATED -- NO SWEEP EXECUTION AUTHORIZED

DE-1 closure (Bundle v0.3 §I.4): policy matching functions are blinded
to exact queried-key identity. The PolicyInputView interface filters
the queried key out at construction time and never exposes it as a
public attribute. Identity-based policies operate on
candidates_excluding_queried_key. Prefix-based policies use the
prefix_distance_to_queried_key method, which returns a numeric
distance without revealing the queried key's value.

The copy_completion diagnostic policy uses DiagnosticInputView, which
does expose the queried key (since copy_completion is a diagnostic
that explicitly echoes it). copy_completion is outside the union
envelope per Bundle v0.3 §I.4 and per the AL-Q4 diagnostic-sidecar
pattern.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class ManifestPair:
    """A single key-value pair from the manifest's real-pair block."""
    key_token_ids: tuple[int, ...]
    value_token_ids: tuple[int, ...]


@dataclass(frozen=True)
class PolicyOutput:
    """Output of a policy invocation.

    A predicted_value_token_ids of None signals the policy emits a
    declared no-match output (per prefix_neighbor_confusion clause 3).
    No-match predictions score incorrect and contribute nothing to the
    union envelope per clause 4.
    """
    policy_name: str
    predicted_value_token_ids: Optional[tuple[int, ...]]

    @property
    def is_no_match(self) -> bool:
        return self.predicted_value_token_ids is None


class PolicyInputView:
    """View of a manifest record exposed to ENVELOPE policy matching
    functions.

    DE-1 INVARIANT (Bundle v0.3 §I.4):
      The queried-key token-id-sequence is filtered into a
      candidates_excluding_queried_key tuple at construction time and
      is NOT exposed as a public attribute. Identity-based policies
      operate on the filtered list. Prefix-based policies use the
      prefix_distance_to_queried_key method, which exposes a numeric
      distance without revealing the queried key.

      The private attribute self._queried_key is name-mangled by
      convention; no policy module in this package may access it
      directly. A source-level grep test enforces this rule.
    """

    def __init__(
        self,
        record_id: str,
        pairs: tuple[ManifestPair, ...],
        queried_key_token_ids: tuple[int, ...],
        real_pair_block_indices: tuple[int, int],
    ) -> None:
        self._record_id = record_id
        self._pairs = pairs
        self._queried_key = queried_key_token_ids  # private; not exposed
        self._real_pair_block_indices = real_pair_block_indices
        # Precompute the queried-key length for prefix-distance use
        # without exposing the queried key itself.
        self._queried_key_length = len(queried_key_token_ids)

    @property
    def record_id(self) -> str:
        return self._record_id

    @property
    def pairs(self) -> tuple[ManifestPair, ...]:
        """All visible pairs in order; used by POSITION-based policies."""
        return self._pairs

    @property
    def candidates_excluding_queried_key(self) -> tuple[ManifestPair, ...]:
        """Pairs with the queried-key pair removed; used by
        IDENTITY-based policies.

        Equality predicate per IS-9: tuple-equality of key_token_ids
        after tokenizer canonicalization. CS reserves the option to
        propose a stricter predicate at packet stage if tokenizer edge
        cases surface (Bundle v0.3 §I.4 "unless CS proposes stricter").
        """
        return tuple(
            p for p in self._pairs if p.key_token_ids != self._queried_key
        )

    @property
    def real_pair_block_indices(self) -> tuple[int, int]:
        return self._real_pair_block_indices

    @property
    def queried_key_length(self) -> int:
        """Length of the queried key, without revealing its tokens.

        Used by prefix_neighbor_confusion to identify the "no
        shared-prefix" boundary (clause 3).
        """
        return self._queried_key_length

    def prefix_distance_to_queried_key(
        self, candidate_key: tuple[int, ...]
    ) -> int:
        """Return prefix-distance from candidate_key to the queried key.

        Distance is defined as queried_key_length - (longest common
        prefix length). A distance of 0 corresponds to a perfect-prefix
        match (which only the queried key itself satisfies; that key
        is excluded from candidates_excluding_queried_key, so this
        method is safe to call from prefix-based policies on the
        filtered list).

        Higher distance = less prefix similarity.
        """
        common = 0
        for a, b in zip(self._queried_key, candidate_key):
            if a == b:
                common += 1
            else:
                break
        return self._queried_key_length - common


class DiagnosticInputView:
    """View of a manifest record exposed to DIAGNOSTIC policies.

    Unlike PolicyInputView, this view DOES expose the queried key,
    because diagnostic policies (such as copy_completion) explicitly
    operate on key identity to produce per-item agreement data for
    the diagnostic sidecar.

    Diagnostic policies are OUTSIDE the union envelope (Bundle v0.3
    §I.4). Their outputs flow to the diagnostic sidecar pattern, not
    the runner-attested sidecar's policies_applied list. The
    consumer-side enforcement (typed boundary between diagnostic
    sidecar and union envelope) lives in the controls module and the
    analysis script.
    """

    def __init__(
        self,
        record_id: str,
        pairs: tuple[ManifestPair, ...],
        queried_key_token_ids: tuple[int, ...],
        real_pair_block_indices: tuple[int, int],
    ) -> None:
        self.record_id = record_id
        self.pairs = pairs
        self.queried_key_token_ids = queried_key_token_ids
        self.real_pair_block_indices = real_pair_block_indices


def build_policy_input_view(record: dict, record_id: str = "") -> PolicyInputView:
    """Construct a PolicyInputView from a manifest record dict.

    The queried key is captured privately at construction time and
    is not exposed thereafter.
    """
    queried_key = tuple(record["queried_key"]["key_token_ids"])
    block = record["context_block"]["real_pair_block"]
    pairs = tuple(
        ManifestPair(
            key_token_ids=tuple(p["key_token_ids"]),
            value_token_ids=tuple(p["value_token_ids"]),
        )
        for p in block["pairs"]
    )
    return PolicyInputView(
        record_id=record_id,
        pairs=pairs,
        queried_key_token_ids=queried_key,
        real_pair_block_indices=(block["start_idx"], block["end_idx"]),
    )


def build_diagnostic_input_view(record: dict, record_id: str = "") -> DiagnosticInputView:
    """Construct a DiagnosticInputView from a manifest record dict."""
    queried_key = tuple(record["queried_key"]["key_token_ids"])
    block = record["context_block"]["real_pair_block"]
    pairs = tuple(
        ManifestPair(
            key_token_ids=tuple(p["key_token_ids"]),
            value_token_ids=tuple(p["value_token_ids"]),
        )
        for p in block["pairs"]
    )
    return DiagnosticInputView(
        record_id=record_id,
        pairs=pairs,
        queried_key_token_ids=queried_key,
        real_pair_block_indices=(block["start_idx"], block["end_idx"]),
    )


# ---------- envelope policies ----------

def pure_last_position(view: PolicyInputView) -> PolicyOutput:
    """Value of the last visible pair.

    Position-based (unchanged from v1). Models the shortcut where a
    model just echoes the most recently seen value. Does not exclude
    the queried key (if it is at the last position, the policy returns
    its value; that is not a self-match shortcut but the natural
    positional behavior).
    """
    if not view.pairs:
        return PolicyOutput(policy_name="pure_last_position", predicted_value_token_ids=None)
    return PolicyOutput(
        policy_name="pure_last_position",
        predicted_value_token_ids=view.pairs[-1].value_token_ids,
    )


def salient_endpoint(
    view: PolicyInputView,
    endpoint_position: int = 0,
) -> PolicyOutput:
    """Value at the declared salient endpoint.

    Position-based (unchanged from v1). The endpoint_position is a
    sweep parameter declared at packet-stage construction recipe; the
    default of 0 (first position) is a Phase 2 placeholder that
    Phase 4 / Phase 5 will replace with the locked configuration
    value.
    """
    if not view.pairs:
        return PolicyOutput(policy_name="salient_endpoint", predicted_value_token_ids=None)
    if endpoint_position < 0 or endpoint_position >= len(view.pairs):
        return PolicyOutput(policy_name="salient_endpoint", predicted_value_token_ids=None)
    return PolicyOutput(
        policy_name="salient_endpoint",
        predicted_value_token_ids=view.pairs[endpoint_position].value_token_ids,
    )


def recency_excluding_target(view: PolicyInputView) -> PolicyOutput:
    """Value of the most recently listed pair EXCLUDING the queried key.

    Identity-based. Replaces v1's target_recency, which was a
    self-match oracle (returned the queried key's value).
    Operates on candidates_excluding_queried_key, where the queried
    key has already been filtered out by the PolicyInputView at
    construction time.
    """
    candidates = view.candidates_excluding_queried_key
    if not candidates:
        return PolicyOutput(
            policy_name="recency_excluding_target",
            predicted_value_token_ids=None,
        )
    return PolicyOutput(
        policy_name="recency_excluding_target",
        predicted_value_token_ids=candidates[-1].value_token_ids,
    )


def prefix_neighbor_confusion(view: PolicyInputView) -> PolicyOutput:
    """Value of the nearest shared-prefix NEIGHBOR, queried key excluded.

    Four-clause total function per Bundle v0.3 §I.4:

      (1) Exact queried-key self-match is excluded. The equality
          predicate is token-id-sequence equality after tokenizer
          canonicalization (IS-9). Enforced structurally by
          operating on view.candidates_excluding_queried_key.

      (2) Ties among shared-prefix neighbors resolve to the most
          recent neighbor in the visible context. Implementation:
          when multiple candidates share the minimum prefix-distance,
          the chosen index is the highest (most recent) of them.

      (3) If no eligible shared-prefix neighbor exists (typical on
          K=low rungs), the policy emits a declared no-match output
          (predicted_value_token_ids=None). "Eligible" means the
          candidate shares at least one prefix token with the queried
          key, i.e., prefix_distance < queried_key_length.

      (4) No-match predictions score incorrect and contribute nothing
          to the union envelope. The envelope aggregator must skip
          PolicyOutput instances whose is_no_match property is True.
          Structural undefinedness on K=low rungs is therefore
          impossible by definition, not by hope.
    """
    candidates = view.candidates_excluding_queried_key  # clause (1)

    if not candidates or view.queried_key_length == 0:
        # Clause (3): no eligible neighbor possible
        return PolicyOutput(
            policy_name="prefix_neighbor_confusion",
            predicted_value_token_ids=None,
        )

    # Compute prefix distance per candidate
    distances = []
    for idx, candidate in enumerate(candidates):
        dist = view.prefix_distance_to_queried_key(candidate.key_token_ids)
        distances.append((dist, idx))

    # Eligible: at least one shared prefix token
    # (prefix_distance < queried_key_length)
    eligible = [(d, idx) for d, idx in distances if d < view.queried_key_length]

    if not eligible:
        # Clause (3): no eligible shared-prefix neighbor
        return PolicyOutput(
            policy_name="prefix_neighbor_confusion",
            predicted_value_token_ids=None,
        )

    # Clause (2): tie-break by most recent (highest index)
    min_dist = min(d for d, _ in eligible)
    nearest = [idx for d, idx in eligible if d == min_dist]
    chosen_idx = max(nearest)

    return PolicyOutput(
        policy_name="prefix_neighbor_confusion",
        predicted_value_token_ids=candidates[chosen_idx].value_token_ids,
    )


# ---------- diagnostic policy (OUTSIDE union envelope) ----------

def copy_completion(view: DiagnosticInputView) -> PolicyOutput:
    """Candidate-output-pattern diagnostic; OUTSIDE the union envelope.

    Per Bundle v0.3 §I.4 and CS-EP v0.2 §5.1 (AL-Q4 closure):
    copy_completion is a per-item agreement-rate diagnostic that
    measures whether the candidate output equals the trivial copy
    of the queried key. It is not an accuracy-eligible envelope
    policy.

    The output flows to the diagnostic_sidecar pattern (sidecar_type:
    "diagnostic"; artifact_class: "lane-1a-prime-diagnostic";
    artifact_label: "DIAGNOSTIC -- NON-BINDING -- NOT FOR THRESHOLD
    DERIVATION"). The union-envelope computation function cannot
    consume DiagnosticInputView output by type construction.

    This function takes DiagnosticInputView (not PolicyInputView)
    because copy_completion needs the queried key's identity (to
    echo it). The type signature is the structural protection: a
    function that takes PolicyInputView cannot accidentally invoke
    copy_completion's identity-revealing semantics.
    """
    return PolicyOutput(
        policy_name="copy_completion",
        predicted_value_token_ids=view.queried_key_token_ids,
    )


# ---------- registries ----------

# Envelope policies: contribute to the union-envelope computation.
ENVELOPE_POLICIES = (
    "pure_last_position",
    "salient_endpoint",
    "recency_excluding_target",
    "prefix_neighbor_confusion",
)

# Diagnostic policies: outside the union envelope; output flows to
# the diagnostic sidecar pattern only.
DIAGNOSTIC_POLICIES = (
    "copy_completion",
)
