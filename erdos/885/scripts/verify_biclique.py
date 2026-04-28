from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Iterable


def factor_pair_for_difference(n: int, d: int) -> tuple[int, int] | None:
    """Return (a,b) with ab=n and b-a=d, if it exists."""
    if n <= 0 or d < 0:
        return None
    disc = d * d + 4 * n
    s = math.isqrt(disc)
    if s * s != disc:
        return None
    if (s - d) % 2:
        return None
    a = (s - d) // 2
    b = a + d
    if a <= 0 or a * b != n:
        return None
    return a, b


def verify(ns: Iterable[int], deltas: Iterable[int]) -> dict:
    ns = list(ns)
    deltas = list(deltas)
    if len(set(ns)) != len(ns):
        raise ValueError("N values must be distinct")
    if len(set(deltas)) != len(deltas):
        raise ValueError("deltas must be distinct")

    matrix = []
    ok = True
    for n in ns:
        row = []
        for d in deltas:
            pair = factor_pair_for_difference(n, d)
            if pair is None:
                ok = False
                row.append({"delta": d, "ok": False})
            else:
                a, b = pair
                row.append({"delta": d, "ok": True, "a": a, "b": b})
        matrix.append({"n": n, "relations": row})
    return {
        "ok": ok,
        "num_N": len(ns),
        "num_deltas": len(deltas),
        "N_values": ns,
        "deltas": deltas,
        "matrix": matrix,
    }


def parse_ints(spec: str) -> list[int]:
    return [int(x.strip()) for x in spec.replace("\n", ",").split(",") if x.strip()]


def main() -> None:
    parser = argparse.ArgumentParser(description="Verify an EP885 biclique certificate.")
    parser.add_argument("--n", required=True, help="Comma-separated N values.")
    parser.add_argument("--d", required=True, help="Comma-separated differences.")
    parser.add_argument("--out", help="Optional JSON output path.")
    args = parser.parse_args()

    result = verify(parse_ints(args.n), parse_ints(args.d))
    text = json.dumps(result, indent=2)
    if args.out:
        out = Path(args.out)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(text + "\n", encoding="utf-8")
    print(text)
    raise SystemExit(0 if result["ok"] else 1)


if __name__ == "__main__":
    main()
