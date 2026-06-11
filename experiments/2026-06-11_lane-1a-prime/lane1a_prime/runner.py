"""Lane 1a' standalone generation runner.

SYNTHETIC / DIAGNOSTIC -- NON-BINDING -- NOT FOR THRESHOLD DERIVATION
D2 IMPLEMENTATION ARTIFACT (PHASE 4)
NO MODEL INVOKED -- NO MODEL LOADED
NO SWEEP_ID CREATED -- NO SWEEP EXECUTION AUTHORIZED

Phase 4 implements:
  - MODEL_ID placeholder (locked at packet seal via sibling-artifact rule)
  - render_prompt(): pure function, no subprocess, no model invocation
  - RenderedPrompt / ConformanceResult dataclasses
  - invoke_model() stub (raises NotImplementedError under D2)

The runner is INVOKED by lane1a_prime_runner_wrapper.py at sweep
execution time (D4 by-name authorization). Under D2 Phase 4, the
runner source EXISTS; it is not invoked against a model.

B1-equivalent provenance discipline:
  - The runner self-attests every generation event (Phase 5: when
    model invocation is authorized).
  - The runner output is byte-preserved on disk; the wrapper's
    write_sidecar() writes a byte-disjoint sidecar record (per
    CS-EP v0.2 §5; wrapper.py at Phase 4 implements this).
  - No wrapper-rewrite of runner-attested outputs.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Optional


# Placeholder constants — locked at packet seal under the
# sibling-artifact cross-reference rule. Under D2 Phase 4 these
# remain placeholders; tests verify the placeholder state.

MODEL_ID = "<PLACEHOLDER_LOCKED_AT_PACKET_SEAL>"


@dataclass(frozen=True)
class ConformanceResult:
    """Result of a template-conformance check on a rendered prompt.

    Used by AL-Q1 dry-run for pre-lock interface-contract testing.
    """
    is_conformant: bool
    issues: tuple[str, ...] = ()


@dataclass(frozen=True)
class RenderedPrompt:
    """Output of render_prompt(); a pure-function rendering of a
    manifest record into a prompt string.

    template_id_hash is the sha256 of the locked template; under D2
    Phase 4 the template is the lane's working draft. At packet seal,
    the template_id_hash binds to LOCK-RECORD via control_prompt_shell_hash.
    """
    record_id: str
    text: str
    template_id_hash: str
    conformance_check: ConformanceResult


# The locked prompt template scaffold. The format-preserving rule
# per joint disposition requires the answerable prompt and the
# unconditioned_token_prior shell to be byte-identical except for
# the key-value-pairs block substitution. Phase 4 implements the
# scaffold; Phase 5 binds concrete recipe values.

DEFAULT_TEMPLATE_VERSION = "v0.1-phase4-draft"
DEFAULT_TEMPLATE_ID_HASH = "0" * 64  # placeholder; locked at packet seal


def _compute_template_id_hash(template_text: str) -> str:
    """Compute a deterministic hash of the template text.

    Under D2 Phase 4 this returns the placeholder hash; at packet
    seal, this will compute the real sha256 of the locked template
    bytes and hash-bind into LOCK-RECORD via control_prompt_shell_hash.
    """
    import hashlib
    return hashlib.sha256(template_text.encode("utf-8")).hexdigest()


def _check_conformance(text: str, record: dict) -> ConformanceResult:
    """Template conformance check for a rendered prompt.

    Verifies that the rendered prompt's structure matches the template
    contract. Used by the AL-Q1 dry-run to surface template issues
    pre-lock without any model invocation.
    """
    issues: list[str] = []
    # Sanity checks; these would be expanded at packet seal time
    # with concrete template contract assertions.
    if not text:
        issues.append("rendered text is empty")
    if "record_id" not in record and "queried_key" not in record:
        issues.append("manifest record missing identity fields")
    return ConformanceResult(
        is_conformant=(len(issues) == 0),
        issues=tuple(issues),
    )


def render_prompt(
    record: dict,
    template_text: Optional[str] = None,
    record_id: str = "",
) -> RenderedPrompt:
    """Render a prompt for a single manifest record.

    Pure function (AL-Q1 closure):
      - No subprocess invocation
      - No model load
      - No I/O beyond reading the record and template
      - Deterministic: same inputs -> identical RenderedPrompt
      - No global state mutation

    Under D2 Phase 4 the template_text is a placeholder; at packet
    seal it is locked and hashed into LOCK-RECORD via
    control_prompt_shell_hash.

    Returns a RenderedPrompt with the conformance check result. The
    interface-contract test (Path A.1) calls render_prompt() on
    synthetic ideal-retriever oracle manifests and asserts
    conformance + structural match to the T2 prompt-shell declarations.
    """
    if template_text is None:
        template_text = (
            "# Lane 1a' placeholder prompt template "
            "(locked at packet seal).\n"
            "Available values: <value_pool_listing>\n"
            "Q: <query_scaffold>\n"
            "A: "
        )

    # Pure rendering: no I/O, no subprocess, no model.
    # The rendering is a string substitution against the locked
    # template. At packet seal, this expands to the full
    # format-preserving prompt scaffold byte-identical to the
    # answerable prompt except for the key-value-pairs block
    # substitution (per joint disposition).

    rendered_text = template_text  # placeholder render under D2

    template_id_hash = _compute_template_id_hash(template_text)
    conformance = _check_conformance(rendered_text, record)

    return RenderedPrompt(
        record_id=record_id,
        text=rendered_text,
        template_id_hash=template_id_hash,
        conformance_check=conformance,
    )


def invoke_model(prompt: RenderedPrompt) -> Any:
    """Invoke the model on a rendered prompt.

    UNDER D2: model invocation is NOT authorized. This function body
    is a NotImplementedError stub until D4 sweep execution
    authorization opens model invocation by name.

    The signature is established here so the runner's invocation
    surface is contract-stable. Phase 5 (model-free validation)
    does not call this function. Only authorized D4 sweep execution
    would.
    """
    raise NotImplementedError(
        "Model invocation requires Manager D4 sweep execution "
        "authorization. Not authorized under D2."
    )
