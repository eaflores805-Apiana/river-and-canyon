"""Lane 1a plotter (locked; hash-recorded in LOCK-RECORD.md).

Two allowed figure types:
  1. per_rung_diagnostic_points — one panel per diagnostic axis, rungs
     L01..L08 on the x-axis (ladder order, NEVER sorted by statistic),
     markers only (no lines, no smoothing, no shaded regions, no
     reference lines except axis zero), categorical palette.
  2. rung_label_categorical_grid — rows: labels in alphabetical order;
     cols: rungs L01..L08; cells: discrete categorical markers (filled
     if label attached). No gradient colormaps.

Every prohibited figure type raises NotImplementedError keyed to the
design-packet §1.8 enumeration. CS failure-mode 6c upgrades plot
prohibitions from wording-class to code-class protection.

Every saved figure includes the artifact-tag footer + fixed outcome
statement. The figure cannot be saved without these.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

from artifact_tags import get_tag_footer


ALLOWED_FIGURE_TYPES = {
    "per_rung_diagnostic_points",
    "rung_label_categorical_grid",
}

PROHIBITED_FIGURE_TYPES = {
    "heatmap": "Prohibited per design packet v0.3 §1.8 (heat maps)",
    "heat_map": "Prohibited per design packet v0.3 §1.8 (heat maps)",
    "contour": "Prohibited per design packet v0.3 §1.8 (contours)",
    "smoothed_curve": "Prohibited per design packet v0.3 §1.8 (smoothed curves)",
    "smoothing": "Prohibited per design packet v0.3 §1.8 (smoothed curves)",
    "fitted_boundary": "Prohibited per design packet v0.3 §1.8 (fitted boundaries)",
    "regression_line": "Prohibited per design packet v0.3 §1.8 (fitted boundaries)",
    "threshold_line": "Prohibited per design packet v0.3 §1.8 (threshold lines)",
    "certification_band": "Prohibited per design packet v0.3 §1.8 (certification bands)",
    "viability_overlay": "Prohibited per design packet v0.3 §1.8 (viability overlays)",
    "promising_region": "Prohibited per design packet v0.3 §1.8 (promising-region annotations)",
    "ranked_cluster": "Prohibited per design packet v0.3 §1.8 (ranked cluster plots)",
    "ranked_scatter": "Prohibited per design packet v0.3 §1.8 (ranked cluster plots)",
}

RUNG_ORDER = ["L01", "L02", "L03", "L04", "L05", "L06", "L07", "L08"]


class Lane1aPlotter:
    """Code-level enforcement of plot prohibitions."""

    def __init__(self, fixed_outcome_statement: str):
        self.footer = get_tag_footer()
        self.fixed_outcome_statement = fixed_outcome_statement

    def draw(self, figure_type: str, **kwargs: Any) -> Any:
        if figure_type in PROHIBITED_FIGURE_TYPES:
            raise NotImplementedError(
                f"{figure_type}: {PROHIBITED_FIGURE_TYPES[figure_type]}"
            )
        if figure_type not in ALLOWED_FIGURE_TYPES:
            raise NotImplementedError(
                f"{figure_type}: not in ALLOWED_FIGURE_TYPES; Lane 1a "
                f"allows only {sorted(ALLOWED_FIGURE_TYPES)}"
            )
        method = getattr(self, f"_draw_{figure_type}")
        return method(**kwargs)

    def _draw_per_rung_diagnostic_points(
        self, *, axis_name: str, rung_records: list[dict[str, Any]], save_path: Path
    ) -> Path:
        # Defer matplotlib import so plotter can be loaded without it.
        import matplotlib.pyplot as plt  # noqa: PLC0415

        fig, ax = plt.subplots(figsize=(6, 4))
        xs = list(range(len(RUNG_ORDER)))
        # Plot rungs in ladder order (NEVER sorted by statistic).
        rec_by_id = {r["rung_id"]: r for r in rung_records}
        ys = [rec_by_id[rid].get(axis_name) for rid in RUNG_ORDER]
        # Markers only; no lines.
        ax.plot(xs, ys, "o", linewidth=0)
        ax.set_xticks(xs)
        ax.set_xticklabels(RUNG_ORDER)
        ax.set_xlabel("rung")
        ax.set_ylabel(axis_name)
        # Axis-zero reference is allowed by §1.8.
        ax.axhline(0, color="gray", linewidth=0.5)
        # Footer (mandatory).
        fig.text(0.02, 0.02, self.footer, fontsize=7)
        fig.text(0.02, 0.06, self.fixed_outcome_statement[:200] + "…", fontsize=6)
        plt.tight_layout(rect=(0, 0.10, 1, 1))
        plt.savefig(save_path, dpi=150)
        plt.close(fig)
        return save_path

    def _draw_rung_label_categorical_grid(
        self, *, rung_records: list[dict[str, Any]], save_path: Path
    ) -> Path:
        import matplotlib.pyplot as plt  # noqa: PLC0415

        # Rows: labels (alphabetical, locked enum order).
        from analyzer import LABELS_ENUM  # noqa: PLC0415
        labels_sorted = sorted(LABELS_ENUM)
        rec_by_id = {r["rung_id"]: r for r in rung_records}

        fig, ax = plt.subplots(figsize=(8, 5))

        for li, label in enumerate(labels_sorted):
            for ri, rid in enumerate(RUNG_ORDER):
                attached = label in rec_by_id[rid]["labels"]
                marker = "s" if attached else "."
                ax.scatter([ri], [li], marker=marker, s=60, c="black")

        ax.set_yticks(range(len(labels_sorted)))
        ax.set_yticklabels(labels_sorted, fontsize=7)
        ax.set_xticks(range(len(RUNG_ORDER)))
        ax.set_xticklabels(RUNG_ORDER)
        ax.set_xlabel("rung")
        ax.set_ylabel("label")
        fig.text(0.02, 0.02, self.footer, fontsize=7)
        fig.text(0.02, 0.06, self.fixed_outcome_statement[:200] + "…", fontsize=6)
        plt.tight_layout(rect=(0, 0.12, 1, 1))
        plt.savefig(save_path, dpi=150)
        plt.close(fig)
        return save_path
