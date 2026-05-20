"""Build prompt manifests for replacing generated diagrams with internal ImageGen PNGs."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
DATABASE = DATA_DIR / "honors_geometry_problem_database.json"
MANIFEST_DIR = DATA_DIR / "imagegen_manifest"
IMAGEGEN_DIR = DATA_DIR / "imagegen"


def prompt_for(problem: dict) -> str:
    proof_note = "This is a proof-oriented visual; emphasize the givens and geometric relationships." if problem["proof_required"] else "This is a practice-problem visual; emphasize the diagram needed to solve it."
    return "\n".join(
        [
            "Use case: scientific-educational",
            "Asset type: honors geometry problem visual",
            f"Primary request: Create a clean, readable bitmap diagram for problem {problem['id']}.",
            "Scene/backdrop: plain white worksheet-style background.",
            f"Subject: {problem['visual_alt_text']}",
            f"Problem context: {problem['question']}",
            f"Topic: {problem['topic']}",
            f"Standard: {problem['standard']}",
            f"Style/medium: crisp educational classroom diagram, high contrast, large readable labels, raster PNG.",
            "Composition/framing: centered diagram with generous margins; no decorative page chrome.",
            proof_note,
            "Text constraints: include only the labels, numbers, point names, or measurements that are needed for the diagram; keep any included text large and legible.",
            "Avoid: tiny text, blurry text, extra explanatory paragraphs, answer text, watermark, logo, decorative background, clutter.",
        ]
    )


def main() -> None:
    data = json.loads(DATABASE.read_text(encoding="utf-8"))
    MANIFEST_DIR.mkdir(parents=True, exist_ok=True)
    all_records: list[dict] = []
    for unit in range(1, 9):
        unit_records = []
        unit_dir = IMAGEGEN_DIR / f"unit_{unit:02d}"
        unit_dir.mkdir(parents=True, exist_ok=True)
        for problem in data["problems"]:
            if problem["unit"] != unit:
                continue
            record = {
                "id": problem["id"],
                "unit": problem["unit"],
                "unit_problem_number": problem["unit_problem_number"],
                "topic": problem["topic"],
                "difficulty": problem["difficulty"],
                "problem_type": problem["problem_type"],
                "proof_required": problem["proof_required"],
                "question": problem["question"],
                "visual_alt_text": problem["visual_alt_text"],
                "destination": (unit_dir / f"{problem['id']}.png").relative_to(ROOT).as_posix(),
                "prompt": prompt_for(problem),
            }
            unit_records.append(record)
            all_records.append(record)

        (MANIFEST_DIR / f"unit_{unit:02d}.json").write_text(json.dumps(unit_records, indent=2), encoding="utf-8")

    (MANIFEST_DIR / "all.json").write_text(json.dumps(all_records, indent=2), encoding="utf-8")
    print(f"Wrote {len(all_records)} prompt records to {MANIFEST_DIR}")


if __name__ == "__main__":
    main()
