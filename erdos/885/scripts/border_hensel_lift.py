#!/usr/bin/env python3
"""Hensel lift a smooth EP885 border point with fixed (X,M).

This utility takes one mod-p border point from `border_surface_modp.py` and
lifts the square roots in

    U_i^2 = X^2 + N_i,
    V_j^2 = M + x_j^2,
    W^2   = M + X^2

to modulus p^e, keeping X and M fixed as their integer representatives.  This
does not find a rational point.  It certifies that a chosen smooth modular
border point gives a compatible p-adic local point to the requested precision.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import bremner_map
from border_surface_modp import sqrt_table_mod_p


def hensel_sqrt_fixed_a(a: int, p: int, exponent: int) -> int:
    """Lift a simple square root of a modulo p to modulo p**exponent."""
    roots = sqrt_table_mod_p(p)
    residue = a % p
    if residue not in roots:
        raise ValueError(f"{a} is not a square modulo {p}")
    root = roots[residue]
    if root % p == 0:
        raise ValueError("root is not simple modulo p; fixed-(X,M) lift not automatic")

    modulus = p
    for _ in range(1, exponent):
        # root^2 - a is divisible by modulus.  Choose t modulo p such that
        # (root + t*modulus)^2 == a mod modulus*p.
        error = (root * root - a) // modulus
        t = (-error * pow(2 * root, -1, p)) % p
        root = root + t * modulus
        modulus *= p
    return root % modulus


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, required=True)
    parser.add_argument("--torsion", action="store_true")
    parser.add_argument("--p", type=int, required=True)
    parser.add_argument("--X", type=int, required=True)
    parser.add_argument("--M", type=int, required=True)
    parser.add_argument("--exponent", type=int, default=8)
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()

    seed = bremner_map.generate(args.n, args.torsion)
    cols = [(d // 2) ** 2 for d in seed.deltas]
    x2 = args.X * args.X

    u_roots = [hensel_sqrt_fixed_a(x2 + row, args.p, args.exponent) for row in seed.N_values]
    v_roots = [hensel_sqrt_fixed_a(args.M + col, args.p, args.exponent) for col in cols]
    w_root = hensel_sqrt_fixed_a(args.M + x2, args.p, args.exponent)
    modulus = args.p**args.exponent

    checks = {
        "U": [((u * u - (x2 + row)) % modulus) for u, row in zip(u_roots, seed.N_values)],
        "V": [((v * v - (args.M + col)) % modulus) for v, col in zip(v_roots, cols)],
        "W": (w_root * w_root - (args.M + x2)) % modulus,
    }
    payload = {
        "seed": f"{args.n}Q+T" if args.torsion else f"{args.n}Q",
        "p": args.p,
        "exponent": args.exponent,
        "modulus": modulus,
        "X": args.X,
        "M": args.M,
        "U_roots_mod_p_power": u_roots,
        "V_roots_mod_p_power": v_roots,
        "W_root_mod_p_power": w_root,
        "checks_mod_p_power": checks,
    }
    text = json.dumps(payload, indent=2)
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(text + "\n", encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
