"""Point the website/database at internal ImageGen PNG assets."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
DATABASE = DATA_DIR / "honors_geometry_problem_database.json"
JS_OUTPUT = DATA_DIR / "honors_geometry_problem_database.js"
IMAGEGEN_DIR = DATA_DIR / "imagegen"


def main() -> None:
    data = json.loads(DATABASE.read_text(encoding="utf-8"))
    missing: list[str] = []
    for problem in data["problems"]:
        unit = problem["unit"]
        path = IMAGEGEN_DIR / f"unit_{unit:02d}" / f"{problem['id']}.png"
        if not path.exists():
            missing.append(path.relative_to(ROOT).as_posix())
            continue
        problem["visual_path"] = path.relative_to(DATA_DIR).as_posix()
        problem["visual_mime_type"] = "image/png"

    if missing:
        preview = "\n".join(missing[:20])
        raise SystemExit(f"Missing {len(missing)} ImageGen assets; first missing:\n{preview}")

    data["metadata"]["visual_policy"] = "Every generated problem uses an internal ImageGen PNG bitmap asset and alt text."
    data["metadata"]["image_generation_mode"] = "Internal ImageGen, generated in parallel by unit-level workers."

    DATABASE.write_text(json.dumps(data, indent=2, ensure_ascii=True), encoding="utf-8")
    JS_OUTPUT.write_text(
        "window.HONORS_GEOMETRY_DATABASE = "
        + json.dumps(data, ensure_ascii=True, separators=(",", ":"))
        + ";\n",
        encoding="utf-8",
    )
    print("Updated database and browser JS to use internal ImageGen assets.")


if __name__ == "__main__":
    main()
