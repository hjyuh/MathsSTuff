#!/usr/bin/env python3
"""Search rational fifth columns for a Bremner K4,4 seed.

For fixed rows N_i, a rational fifth column is X such that

    X^2 + N_i is a rational square for all i=1..4.

Parameterize the first conic X^2 + N_anchor = U^2 by

    X = (s^2 - N_anchor t^2) / (2 s t).

Then test the other three rows exactly.  This is a bounded-height search in the
parameter (s:t), not a proof of nonexistence.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import bremner_map


def is_square(n: int) -> bool:
    if n < 0:
        return False
    r = math.isqrt(n)
    return r * r == n


def search(seed: bremner_map.BremnerOutput, bound: int, anchor: int, max_hits: int) -> dict:
    n_values = seed.N_values
    n0 = n_values[anchor]
    old_t = {(d // 2) ** 2 for d in seed.deltas}
    hits = []
    tested = 0
    passed_two = 0
    passed_three = 0
    for s in range(1, bound + 1):
        for t in range(1, bound + 1):
            if math.gcd(s, t) != 1:
                continue
            tested += 1
            a = s * s - n0 * t * t
            den = 2 * s * t
            x_square_num = a * a
            x_square_den = den * den
            if x_square_den and x_square_num % x_square_den == 0:
                x2_int = x_square_num // x_square_den
                if x2_int in old_t:
                    continue
            passed = 1
            roots = []
            for idx, n_i in enumerate(n_values):
                if idx == anchor:
                    continue
                numerator = x_square_num + n_i * x_square_den
                if not is_square(numerator):
                    break
                roots.append(math.isqrt(numerator))
                passed += 1
                if passed == 2:
                    passed_two += 1
                if passed == 3:
                    passed_three += 1
            else:
                hit = {
                    "s": s,
                    "t": t,
                    "X_num": a,
                    "X_den": den,
                    "X2_num": x_square_num,
                    "X2_den": x_square_den,
                    "old_column_square": (
                        x_square_num % x_square_den == 0
                        and x_square_num // x_square_den in old_t
                    ),
                }
                hits.append(hit)
                if len(hits) >= max_hits:
                    return {
                        "tested_parameters": tested,
                        "passed_two_counter": passed_two,
                        "passed_three_counter": passed_three,
                        "hits": hits,
                        "stopped_early": True,
                    }
    return {
        "tested_parameters": tested,
        "passed_two_counter": passed_two,
        "passed_three_counter": passed_three,
        "hits": hits,
        "stopped_early": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, required=True)
    parser.add_argument("--torsion", action="store_true")
    parser.add_argument("--bound", type=int, default=500)
    parser.add_argument("--anchor", type=int, default=0)
    parser.add_argument("--max-hits", type=int, default=20)
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()

    seed = bremner_map.generate(args.n, args.torsion)
    payload = {
        "seed": f"{args.n}Q+T" if args.torsion else f"{args.n}Q",
        "bound": args.bound,
        "anchor": args.anchor,
        "N_values": seed.N_values,
        "deltas": seed.deltas,
    }
    payload.update(search(seed, args.bound, args.anchor, args.max_hits))
    text = json.dumps(payload, indent=2)
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(text + "\n", encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
