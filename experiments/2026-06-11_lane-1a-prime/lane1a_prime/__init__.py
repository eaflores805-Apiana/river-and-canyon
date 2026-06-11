"""Lane 1a' deterministic core.

SYNTHETIC / DIAGNOSTIC -- NON-BINDING -- NOT FOR THRESHOLD DERIVATION
D2 IMPLEMENTATION ARTIFACT (PHASE 2)
NO MODEL INVOKED -- NO SWEEP_ID CREATED -- NO SWEEP EXECUTION AUTHORIZED

Modules:
  - policies: PolicyInputView (DE-1 blinding), DiagnosticInputView,
              ManifestPair, PolicyOutput; five policies
              (pure_last_position, salient_endpoint,
              recency_excluding_target, prefix_neighbor_confusion,
              copy_completion).
  - controls: ControlSpec dataclass; UNCONDITIONED_TOKEN_PRIOR_SPEC;
              SCRAMBLED_BINDING_RETRIEVAL_SPEC; ControlOutput;
              LabelInput; DiagnosticInterpretation; emit_elimination_label
              signature (Phase 3 implements body).
"""
