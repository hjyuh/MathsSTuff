"""Verify internal ImageGen replacement assets."""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

from PIL import Image, ImageStat


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
DATABASE = DATA_DIR / "honors_geometry_problem_database.json"
IMAGEGEN_DIR = DATA_DIR / "imagegen"


def fail(message: str) -> None:
    raise SystemExit(f"VERIFY IMAGEGEN FAILED: {message}")


def main() -> None:
    data = json.loads(DATABASE.read_text(encoding="utf-8"))
    problems = data["problems"]
    if len(problems) != 800:
        fail(f"expected 800 problems, found {len(problems)}")

    missing: list[str] = []
    invalid: list[str] = []
    unit_counts: Counter[int] = Counter()

    for problem in problems:
        unit = problem["unit"]
        path = IMAGEGEN_DIR / f"unit_{unit:02d}" / f"{problem['id']}.png"
        if not path.exists():
            missing.append(path.relative_to(ROOT).as_posix())
            continue
        try:
            with Image.open(path) as image:
                if image.format != "PNG":
                    invalid.append(f"{path}: not PNG")
                    continue
                width, height = image.size
                if width < 512 or height < 512:
                    invalid.append(f"{path}: too small {width}x{height}")
                    continue
                stat = ImageStat.Stat(image.convert("RGB"))
                if max(stat.stddev) < 5:
                    invalid.append(f"{path}: appears blank")
                    continue
        except Exception as exc:  # pragma: no cover - verifier diagnostics
            invalid.append(f"{path}: {exc}")
            continue
        unit_counts[unit] += 1

    if missing:
        preview = "\n".join(missing[:20])
        fail(f"missing {len(missing)} imagegen assets; first missing:\n{preview}")
    if invalid:
        preview = "\n".join(invalid[:20])
        fail(f"invalid {len(invalid)} imagegen assets; first invalid:\n{preview}")

    for unit in range(1, 9):
        if unit_counts[unit] != 100:
            fail(f"unit {unit} expected 100 imagegen assets, found {unit_counts[unit]}")

    print("VERIFY IMAGEGEN PASSED")
    print(f"Images: {sum(unit_counts.values())}")
    print(f"Unit counts: {dict(sorted(unit_counts.items()))}")


if __name__ == "__main__":
    main()
