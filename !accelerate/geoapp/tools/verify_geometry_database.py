"""Verify the generated honors geometry problem database."""

from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
DATABASE = DATA_DIR / "honors_geometry_problem_database.json"


REQUIRED_FIELDS = [
    "id",
    "unit",
    "unit_title",
    "unit_problem_number",
    "standard",
    "topic",
    "difficulty",
    "problem_type",
    "question",
    "answer",
    "explanation",
    "proof_required",
    "visual_required",
    "visual_alt_text",
    "visual_path",
    "visual_mime_type",
    "source_alignment",
]

EXPECTED_DIFFICULTIES = {
    "easy": 25,
    "moderate": 30,
    "challenging": 25,
    "honors": 20,
}


def fail(message: str) -> None:
    raise SystemExit(f"VERIFY FAILED: {message}")


def main() -> None:
    if not DATABASE.exists():
        fail(f"missing database: {DATABASE}")

    data = json.loads(DATABASE.read_text(encoding="utf-8"))
    problems = data.get("problems")
    if not isinstance(problems, list):
        fail("top-level problems field is not a list")
    if len(problems) != 800:
        fail(f"expected 800 problems, found {len(problems)}")
    svg_files = list(DATA_DIR.rglob("*.svg"))
    if svg_files:
        fail(f"expected no SVG assets under data, found {len(svg_files)}")

    ids: set[str] = set()
    unit_counts: Counter[int] = Counter()
    difficulty_by_unit: dict[int, Counter[str]] = defaultdict(Counter)
    proof_counts: Counter[int] = Counter()
    visual_count = 0
    type_by_unit: dict[int, Counter[str]] = defaultdict(Counter)

    for problem in problems:
        for field in REQUIRED_FIELDS:
            if field not in problem:
                fail(f"{problem.get('id', '<missing id>')} missing field {field}")
            if field not in {"proof_required", "visual_required"} and problem[field] in ("", None, []):
                fail(f"{problem.get('id', '<missing id>')} has empty field {field}")

        pid = problem["id"]
        if pid in ids:
            fail(f"duplicate id {pid}")
        ids.add(pid)

        unit = problem["unit"]
        if unit not in range(1, 9):
            fail(f"{pid} has invalid unit {unit}")
        expected_prefix = f"HG-U{unit:02d}-"
        if not pid.startswith(expected_prefix):
            fail(f"{pid} does not match unit prefix {expected_prefix}")

        number = problem["unit_problem_number"]
        if not isinstance(number, int) or number < 1 or number > 100:
            fail(f"{pid} has invalid unit_problem_number {number}")

        if problem["difficulty"] not in EXPECTED_DIFFICULTIES:
            fail(f"{pid} has invalid difficulty {problem['difficulty']}")
        if len(problem["question"]) < 40:
            fail(f"{pid} question is too short")
        if len(problem["answer"]) < 8:
            fail(f"{pid} answer is too short")
        if len(problem["explanation"]) < 180:
            fail(f"{pid} explanation is too short")
        if len(problem["visual_alt_text"]) < 20:
            fail(f"{pid} visual alt text is too short")

        if not problem["visual_required"]:
            fail(f"{pid} is missing required visual flag")
        visual_path = DATA_DIR / problem["visual_path"]
        if not visual_path.exists():
            fail(f"{pid} visual file missing: {visual_path}")
        if visual_path.suffix.lower() != ".png":
            fail(f"{pid} visual is not a PNG path: {visual_path}")
        if problem["visual_mime_type"] != "image/png":
            fail(f"{pid} visual_mime_type is not image/png")
        with Image.open(visual_path) as image:
            if image.format != "PNG":
                fail(f"{pid} visual file is not PNG format")
            width, height = image.size
            if width < 300 or height < 220:
                fail(f"{pid} visual dimensions are too small: {width}x{height}")
        visual_count += 1

        if problem["proof_required"]:
            proof = problem.get("proof")
            if not proof or len(proof) < 150:
                fail(f"{pid} proof is missing or too short")
            proof_counts[unit] += 1

        unit_counts[unit] += 1
        difficulty_by_unit[unit][problem["difficulty"]] += 1
        type_by_unit[unit][problem["problem_type"]] += 1

    for unit in range(1, 9):
        if unit_counts[unit] != 100:
            fail(f"unit {unit} expected 100 problems, found {unit_counts[unit]}")
        if difficulty_by_unit[unit] != EXPECTED_DIFFICULTIES:
            fail(f"unit {unit} difficulty distribution mismatch: {dict(difficulty_by_unit[unit])}")
        if proof_counts[unit] < 20:
            fail(f"unit {unit} expected at least 20 proof-required problems, found {proof_counts[unit]}")
        if len(type_by_unit[unit]) < 4:
            fail(f"unit {unit} expected at least 4 problem types, found {dict(type_by_unit[unit])}")

    metadata = data.get("metadata", {})
    if metadata.get("problem_count") != 800:
        fail("metadata problem_count is not 800")
    if metadata.get("problems_per_unit") != 100:
        fail("metadata problems_per_unit is not 100")
    if len(metadata.get("units", [])) != 8:
        fail("metadata does not describe 8 units")

    print("VERIFY PASSED")
    print(f"Problems: {len(problems)}")
    print(f"Images: {visual_count}")
    print(f"Unit counts: {dict(sorted(unit_counts.items()))}")
    print(f"Proof counts: {dict(sorted(proof_counts.items()))}")
    print("Difficulty per unit:")
    for unit in range(1, 9):
        print(f"  Unit {unit}: {dict(difficulty_by_unit[unit])}")


if __name__ == "__main__":
    main()
