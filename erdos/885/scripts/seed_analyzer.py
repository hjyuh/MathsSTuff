from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Iterable


def parse_ints(spec: str | None) -> list[int]:
    if not spec:
        return []
    return [int(x.strip()) for x in spec.replace("\n", ",").split(",") if x.strip()]


def d_set(n: int, delta_max: int | None = None) -> set[int]:
    out: set[int] = set()
    r = math.isqrt(n)
    for a in range(1, r + 1):
        if n % a == 0:
            d = n // a - a
            if delta_max is None or d <= delta_max:
                out.add(d)
    return out


def postings_for_delta(delta: int, x_bound: int) -> list[int]:
    amax = (math.isqrt(delta * delta + 4 * x_bound) - delta) // 2
    return [a * (a + delta) for a in range(1, amax + 1)]


def intersect_sorted_lists(lists: list[list[int]]) -> list[int]:
    if not lists:
        return []
    sets = [set(xs) for xs in sorted(lists, key=len)]
    inter = sets[0]
    for s in sets[1:]:
        inter = inter.intersection(s)
        if not inter:
            break
    return sorted(inter)


def analyze_n_seed(ns: list[int], delta_max: int | None) -> dict:
    ds = [d_set(n, delta_max) for n in ns]
    common = sorted(set.intersection(*ds)) if ds else []
    return {
        "mode": "n-seed",
        "N_values": ns,
        "delta_max": delta_max,
        "common_delta_count": len(common),
        "common_deltas": common,
    }


def analyze_delta_seed(deltas: list[int], x_bound: int, extension_delta_max: int | None) -> dict:
    postings = [postings_for_delta(d, x_bound) for d in deltas]
    common_ns = intersect_sorted_lists(postings)
    result = {
        "mode": "delta-seed",
        "deltas": deltas,
        "x_bound": x_bound,
        "support": len(common_ns),
        "sample_N_values": common_ns[:50],
    }
    if common_ns and extension_delta_max is not None:
        common_deltas = sorted(set.intersection(*(d_set(n, extension_delta_max) for n in common_ns)))
        result["common_delta_count_up_to_bound"] = len(common_deltas)
        result["common_deltas_up_to_bound"] = common_deltas
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description="Analyze EP885 seed bicliques.")
    parser.add_argument("--n", help="Comma-separated N seed values.")
    parser.add_argument("--d", help="Comma-separated delta seed values.")
    parser.add_argument("--x-bound", type=int, default=10**9)
    parser.add_argument("--delta-max", type=int)
    parser.add_argument("--out")
    args = parser.parse_args()

    ns = parse_ints(args.n)
    deltas = parse_ints(args.d)
    if ns and deltas:
        # First verify all given incidences are present by intersecting D(N).
        n_report = analyze_n_seed(ns, args.delta_max)
        delta_report = analyze_delta_seed(deltas, args.x_bound, args.delta_max)
        result = {"n_seed": n_report, "delta_seed": delta_report}
    elif ns:
        result = analyze_n_seed(ns, args.delta_max)
    elif deltas:
        result = analyze_delta_seed(deltas, args.x_bound, args.delta_max)
    else:
        raise SystemExit("provide --n and/or --d")

    text = json.dumps(result, indent=2)
    if args.out:
        out = Path(args.out)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(text + "\n", encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
