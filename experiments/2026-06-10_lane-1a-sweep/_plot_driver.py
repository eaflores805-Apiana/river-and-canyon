"""Lane 1a plot driver — NOT a locked artifact."""
from __future__ import annotations
import json
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

import plotter as plotter_mod
from audit_log import AuditLogWriter

audit = AuditLogWriter(SCRIPT_DIR / "AUDIT-LOG.ndjson")

def main():
    sweep_record = json.loads((SCRIPT_DIR / "sweep_record.json").read_text())
    rung_records = sweep_record["rungs"]
    p = plotter_mod.Lane1aPlotter(sweep_record["fixed_outcome_statement"])
    figures_dir = SCRIPT_DIR / "figures"
    figures_dir.mkdir(exist_ok=True)
    diag_axes = ["strict_acc", "content_acc", "gap", "control_acc",
                 "max_dummy_score", "union_envelope_score", "headroom",
                 "abstention_rate"]
    for axis in diag_axes:
        save_path = figures_dir / f"diag_{axis}.png"
        try:
            p.draw("per_rung_diagnostic_points",
                   axis_name=axis,
                   rung_records=rung_records,
                   save_path=save_path)
            audit.emit("plot_generated",
                       details={"figure_path": str(save_path),
                                "figure_type": "per_rung_diagnostic_points"})
            print(f"  wrote {save_path.name}")
        except Exception as e:
            print(f"  skip {axis}: {e}")
    grid_path = figures_dir / "rung_label_grid.png"
    p.draw("rung_label_categorical_grid",
           rung_records=rung_records,
           save_path=grid_path)
    audit.emit("plot_generated",
               details={"figure_path": str(grid_path),
                        "figure_type": "rung_label_categorical_grid"})
    print(f"  wrote {grid_path.name}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
