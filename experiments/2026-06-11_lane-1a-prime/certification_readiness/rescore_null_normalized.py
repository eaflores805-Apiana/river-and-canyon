#!/usr/bin/env python3
"""Case-insensitive NULL/none scorer correction + re-score of existing CAL outputs.

Authorized by Manager 2026-06-13 ("Fix NULL Abstention Scorer and Re-Score
Existing CAL Outputs" — model-free scorer correction; NO model execution).

Reads existing raw outputs (CAL-A from constructed-positive-validation/,
CAL-B/C/E from sweep_outputs/) and re-scores under a corrected rule:

    Concept-level abstention if raw.strip().lower() in {"none", "null"}.
    Letter if exactly one a-z (case-insensitive).
    Else OTHER (and reported for inspection).

Keeps 4 categories distinct per Manager:
    1. STRICT scorer correctness (raw == "NONE" exact; preserved for comparison)
    2. CONCEPT-LEVEL abstention (case-insensitive NONE/null match)
    3. TRUE FALSE-ANSWER EMISSION (model returned letter when gold=null)
    4. SCORER/PARSER ARTIFACT (off-grammar; explicitly listed in report)

NO model run. NO new outputs generated. Re-reads existing raw_output strings only.
"""
import json, hashlib
from pathlib import Path
from collections import Counter

REPO_ROOT = Path(__file__).resolve().parents[3]


def sha256_file(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


ABSTENTION_FORMS = {"none", "null"}


def classify(raw_output):
    t = raw_output.strip().split("\n")[0].strip().rstrip(".").rstrip(",").strip()
    if t == "NONE":
        strict_kind = "NONE"
    elif len(t) == 1 and "a" <= t <= "z":
        strict_kind = "letter"
    else:
        strict_kind = "OTHER"
    t_lower = t.lower()
    if t_lower in ABSTENTION_FORMS:
        concept_kind = "abstention"
        abstention_form = t
        letter_value = None
    elif len(t) == 1 and t.isalpha():
        concept_kind = "letter"
        abstention_form = None
        letter_value = t.lower()
    else:
        concept_kind = "OTHER"
        abstention_form = None
        letter_value = None
    return {
        "strict_kind": strict_kind,
        "concept_kind": concept_kind,
        "abstention_form_observed": abstention_form,
        "letter_value": letter_value,
        "raw_normalized": t,
    }


CAL_RAW = {
    "CAL-A": {
        "clean": REPO_ROOT / "governance/2026-06-11_lane-1a-prime/constructed-positive-validation/clean_outputs.json",
        "defective": REPO_ROOT / "governance/2026-06-11_lane-1a-prime/constructed-positive-validation/defective_outputs.json",
    },
    "CAL-B": {
        "clean": REPO_ROOT / "experiments/2026-06-11_lane-1a-prime/certification_readiness/sweep_outputs/cal-b_clean_outputs.json",
        "defective": REPO_ROOT / "experiments/2026-06-11_lane-1a-prime/certification_readiness/sweep_outputs/cal-b_defective_outputs.json",
    },
    "CAL-C": {
        "clean": REPO_ROOT / "experiments/2026-06-11_lane-1a-prime/certification_readiness/sweep_outputs/cal-c_clean_outputs.json",
        "defective": REPO_ROOT / "experiments/2026-06-11_lane-1a-prime/certification_readiness/sweep_outputs/cal-c_defective_outputs.json",
    },
    "CAL-E": {
        "clean": REPO_ROOT / "experiments/2026-06-11_lane-1a-prime/certification_readiness/sweep_outputs/cal-e_clean_outputs.json",
        "defective": REPO_ROOT / "experiments/2026-06-11_lane-1a-prime/certification_readiness/sweep_outputs/cal-e_defective_outputs.json",
    },
}


def rescore_member(items):
    n = len(items)
    strict_correct = 0
    concept_correct = 0
    n_strict_NONE = 0
    n_concept_abstention = 0
    n_letter_strict = 0
    n_letter_concept = 0
    n_OTHER_strict = 0
    n_OTHER_concept = 0
    abstention_forms = Counter()
    other_forms = Counter()
    letter_values = Counter()

    for item in items:
        raw = item.get("raw_output", "")
        gold = item.get("gold_value")
        c = classify(raw)

        if gold is None:
            sc = c["strict_kind"] == "NONE"
        else:
            sc = c["strict_kind"] == "letter" and raw.strip().rstrip(".,") == gold
        if sc:
            strict_correct += 1

        if gold is None:
            cc = c["concept_kind"] == "abstention"
        else:
            cc = c["concept_kind"] == "letter" and c["letter_value"] == gold
        if cc:
            concept_correct += 1

        if c["strict_kind"] == "NONE": n_strict_NONE += 1
        if c["concept_kind"] == "abstention":
            n_concept_abstention += 1
            abstention_forms[c["abstention_form_observed"]] += 1
        if c["strict_kind"] == "letter": n_letter_strict += 1
        if c["concept_kind"] == "letter":
            n_letter_concept += 1
            letter_values[c["letter_value"]] += 1
        if c["strict_kind"] == "OTHER": n_OTHER_strict += 1
        if c["concept_kind"] == "OTHER":
            n_OTHER_concept += 1
            other_forms[c["raw_normalized"][:40]] += 1

    return {
        "n": n,
        "strict_correct": strict_correct,
        "concept_correct": concept_correct,
        "strict_accuracy": strict_correct / n if n else 0.0,
        "concept_accuracy": concept_correct / n if n else 0.0,
        "n_strict_NONE": n_strict_NONE,
        "n_concept_abstention": n_concept_abstention,
        "n_letter_strict": n_letter_strict,
        "n_letter_concept": n_letter_concept,
        "n_OTHER_strict": n_OTHER_strict,
        "n_OTHER_concept": n_OTHER_concept,
        "abstention_forms_observed": dict(abstention_forms),
        "letter_values_observed": dict(letter_values),
        "other_forms_observed": dict(other_forms),
    }


print("=" * 80)
print("Case-insensitive NULL re-score of CAL-A/B/C/E (NO model run)")
print("=" * 80)
print()

results = {}
all_OTHER_forms = Counter()
all_abstention_forms = Counter()

for cid, paths in CAL_RAW.items():
    clean_items = json.load(open(paths["clean"]))
    def_items = json.load(open(paths["defective"]))
    if isinstance(clean_items, dict) and "outputs" in clean_items:
        clean_items = clean_items["outputs"]
    if isinstance(def_items, dict) and "outputs" in def_items:
        def_items = def_items["outputs"]

    clean_r = rescore_member(clean_items)
    def_r = rescore_member(def_items)
    results[cid] = {"clean": clean_r, "defective": def_r}

    for f, c in def_r["other_forms_observed"].items(): all_OTHER_forms[f] += c
    for f, c in clean_r["other_forms_observed"].items(): all_OTHER_forms[f] += c
    for f, c in def_r["abstention_forms_observed"].items(): all_abstention_forms[f] += c
    for f, c in clean_r["abstention_forms_observed"].items(): all_abstention_forms[f] += c

    print(f"--- {cid} ---")
    print(f"  CLEAN     n={clean_r['n']}: strict={clean_r['strict_correct']}/{clean_r['n']}={clean_r['strict_accuracy']:.4f}  concept={clean_r['concept_correct']}/{clean_r['n']}={clean_r['concept_accuracy']:.4f}")
    if clean_r['abstention_forms_observed']:
        print(f"    clean abstention forms (should be 0 for clean): {clean_r['abstention_forms_observed']}")
    print(f"  DEFECTIVE n={def_r['n']}:")
    print(f"    strict NONE accuracy (OLD):           {def_r['strict_accuracy']:.4f}  ({def_r['strict_correct']}/{def_r['n']})")
    print(f"    concept abstention accuracy (NEW):    {def_r['concept_accuracy']:.4f}  ({def_r['concept_correct']}/{def_r['n']})")
    print(f"    true false-emission count (letter):   {def_r['n_letter_concept']}  ({def_r['n_letter_concept']/def_r['n']:.4f})")
    print(f"    OTHER (parser artifact):              {def_r['n_OTHER_concept']}  ({def_r['n_OTHER_concept']/def_r['n']:.4f})")
    print(f"    abstention forms observed: {def_r['abstention_forms_observed']}")
    if def_r['letter_values_observed']:
        print(f"    letter values observed: {def_r['letter_values_observed']}")
    if def_r['other_forms_observed']:
        print(f"    OTHER forms observed: {def_r['other_forms_observed']}")
    print()


print("=" * 80)
print("All abstention forms observed across all members (case-insensitive matched to {none, null}):")
print("=" * 80)
for form, count in all_abstention_forms.most_common():
    print(f"  {count:>3}  {form!r}")

print()
print("=" * 80)
print("All OTHER (off-grammar, non-abstention, non-letter) forms observed:")
print("=" * 80)
if all_OTHER_forms:
    for form, count in all_OTHER_forms.most_common(20):
        print(f"  {count:>3}  {form!r}")
else:
    print("  (none) — all outputs are either letter, NONE/none/Null/NULL, or single letter")


out_path = REPO_ROOT / "governance/2026-06-11_lane-1a-prime/certification-readiness/cal-abce_rescore_summary.json"
summary = {cid: {
    "clean_strict_accuracy": r["clean"]["strict_accuracy"],
    "clean_concept_accuracy": r["clean"]["concept_accuracy"],
    "clean_n": r["clean"]["n"],
    "defective_strict_accuracy_OLD": r["defective"]["strict_accuracy"],
    "defective_concept_abstention_accuracy_NEW": r["defective"]["concept_accuracy"],
    "defective_n_strict_NONE": r["defective"]["n_strict_NONE"],
    "defective_n_concept_abstention": r["defective"]["n_concept_abstention"],
    "defective_n_letter_concept_TRUE_FALSE_EMISSION": r["defective"]["n_letter_concept"],
    "defective_true_false_emission_rate": r["defective"]["n_letter_concept"] / r["defective"]["n"] if r["defective"]["n"] else 0.0,
    "defective_n_OTHER_PARSER_ARTIFACT": r["defective"]["n_OTHER_concept"],
    "defective_abstention_forms_observed": r["defective"]["abstention_forms_observed"],
    "defective_letter_values_observed": r["defective"]["letter_values_observed"],
    "defective_OTHER_forms_observed": r["defective"]["other_forms_observed"],
    "separation_OLD_strict_minus_strict": r["clean"]["strict_accuracy"] - r["defective"]["strict_accuracy"],
    "separation_NEW_clean_minus_concept_abstention": r["clean"]["strict_accuracy"] - r["defective"]["concept_accuracy"],
} for cid, r in results.items()}
out_path.write_text(json.dumps(summary, indent=2))
print()
print(f"Summary JSON: {out_path.relative_to(REPO_ROOT)}")
print(f"sha256:       {sha256_file(out_path)}")
