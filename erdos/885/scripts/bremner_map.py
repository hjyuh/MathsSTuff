#!/usr/bin/env python3
"""Exact Bremner-family generator for EP885 K4,4 seeds.

This implements the rational map described in Bremner's 2019 paper.

The final curve is

    E: y^2 = x^3 + x^2 - 120x + 400,

with generator Q=(0,20) and 2-torsion T=(4,0).  A point nQ, or nQ+T,
maps to rational half-differences and four columns.  Clearing denominators
gives a K4,4 certificate in the EP885 incidence language.

The output signs and row order need not match Bremner's printed table; factor
differences are absolute values, so signs do not affect the certificate.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from fractions import Fraction
from math import gcd
from pathlib import Path
from typing import Iterable


Point = tuple[Fraction, Fraction] | None


CURVE_A2 = Fraction(1)
CURVE_A4 = Fraction(-120)
CURVE_A6 = Fraction(400)
GENERATOR_Q: Point = (Fraction(0), Fraction(20))
TORSION_T: Point = (Fraction(4), Fraction(0))


def curve_add(p: Point, q: Point) -> Point:
    """Add points on y^2 = x^3 + A2*x^2 + A4*x + A6."""
    if p is None:
        return q
    if q is None:
        return p
    x1, y1 = p
    x2, y2 = q
    if x1 == x2 and y1 == -y2:
        return None
    if p == q:
        if y1 == 0:
            return None
        slope = (3 * x1 * x1 + 2 * CURVE_A2 * x1 + CURVE_A4) / (2 * y1)
    else:
        slope = (y2 - y1) / (x2 - x1)
    x3 = slope * slope - CURVE_A2 - x1 - x2
    y3 = -(y1 + slope * (x3 - x1))
    return x3, y3


def curve_mul(n: int, p: Point) -> Point:
    if n < 0:
        r = curve_mul(-n, p)
        if r is None:
            return None
        return r[0], -r[1]
    result: Point = None
    addend = p
    while n:
        if n & 1:
            result = curve_add(result, addend)
        addend = curve_add(addend, addend)
        n >>= 1
    return result


def lcm(a: int, b: int) -> int:
    return abs(a * b) // gcd(a, b)


def primitive_integer_scale(values: Iterable[Fraction]) -> tuple[list[int], Fraction]:
    vals = list(values)
    den = 1
    for v in vals:
        den = lcm(den, v.denominator)
    ints = [int(v * den) for v in vals]
    common = 0
    for z in ints:
        common = gcd(common, abs(z))
    if common == 0:
        return ints, Fraction(den)
    return [z // common for z in ints], Fraction(den, common)


@dataclass(frozen=True)
class BremnerOutput:
    point: tuple[str, str]
    scale: str
    half_difference_table: list[list[int]]
    deltas: list[int]
    N_values: list[int]
    positive_N_count: int
    all_N_positive: bool

    def to_jsonable(self) -> dict:
        return {
            "point": {"x": self.point[0], "y": self.point[1]},
            "scale": self.scale,
            "half_difference_table": self.half_difference_table,
            "deltas": self.deltas,
            "N_values": self.N_values,
            "positive_N_count": self.positive_N_count,
            "all_N_positive": self.all_N_positive,
        }


def bcd_from_final_curve_point(point: Point) -> tuple[Fraction, Fraction, Fraction]:
    if point is None:
        raise ValueError("point at infinity is not admissible")
    x, y = point
    b = 2 * (80 - 40 * x + x * x) * (40 - 10 * x + 2 * y + x * y)
    c = (80 + 32 * x - 5 * x * x - 12 * y + x * y) * (
        40 - 10 * x + 2 * y + x * y
    )
    d = 8 * (x - 4) * (x + 5) * (80 - 40 * x + x * x)
    return b, c, d


def bremner_rational_rows(point: Point) -> list[tuple[Fraction, Fraction, Fraction, Fraction]]:
    b, c, d = bcd_from_final_curve_point(point)

    q = b * (b - d) * d * (c + d)
    r = d * (b**3 - c * d**2)
    s = b**3 * c - d**4

    delta = (
        b * c * (q * q - r * r) * s
        + c * d * (r * r - s * s) * q
        + d * b * (s * s - q * q) * r
    )

    x0 = (
        -(d * d - b * b) * c * (q * q - r * r) * s
        + (b * b - c * c) * d * (s * s - q * q) * r
    ) / (2 * delta)
    y0 = (
        (b * b + d * d) * c * (q * q - r * r) * s
        + 2 * b * c * d * (r * r - s * s) * q
        + (b * b + c * c) * d * (s * s - q * q) * r
    ) / (2 * delta)
    z0 = (
        -(d * d - b * b) * c * (q * q + r * r) * s
        - (b * b - c * c) * d * (s * s + q * q) * r
        - 2 * (c * c - d * d) * b * q * r * s
    ) / (2 * delta)

    x1 = (
        (c * c - d * d) * b * (q * q - r * r) * s
        - (b * b - c * c) * d * (r * r - s * s) * q
    ) / (2 * delta)
    y1 = (
        (c * c + d * d) * b * (q * q - r * r) * s
        + (b * b + c * c) * d * (r * r - s * s) * q
        + 2 * b * c * d * r * (s * s - q * q)
    ) / (2 * delta)
    z1 = (
        -(c * c - d * d) * b * (q * q + r * r) * s
        - (b * b - c * c) * d * (r * r + s * s) * q
        - 2 * c * q * r * s * (d * d - b * b)
    ) / (2 * delta)

    x2 = (
        (d * d - b * b) * c * (r * r - s * s) * q
        - (c * c - d * d) * b * (s * s - q * q) * r
    ) / (2 * delta)
    y2 = (
        2 * b * c * d * (q * q - r * r) * s
        + (b * b + d * d) * c * (r * r - s * s) * q
        + (c * c + d * d) * b * (s * s - q * q) * r
    ) / (2 * delta)
    z2 = (
        -(c * c - d * d) * b * (s * s + q * q) * r
        - (d * d - b * b) * c * (r * r + s * s) * q
        - 2 * (b * b - c * c) * d * q * r * s
    ) / (2 * delta)

    x3 = (x1 * y2 * z2 - x2 * y1 * z1) / (x1 * x1 - x2 * x2)
    y3 = (y1 * x2 * z2 - y2 * x1 * z1) / (y1 * y1 - y2 * y2)
    z3 = (z1 * y2 * x2 - z2 * y1 * x1) / (z1 * z1 - z2 * z2)

    x4 = (x0 * y1 * z1 - x1 * y0 * z0) / (x0 * x0 - x1 * x1)
    y4 = (y0 * x1 * z1 - y1 * x0 * z0) / (y0 * y0 - y1 * y1)
    z4 = (z0 * y1 * x1 - z1 * y0 * x0) / (z0 * z0 - z1 * z1)

    t0 = (x1 * x2 * z0 + x0 * z1 * z2) / (x0 * x0 - z0 * z0)
    t1 = (x2 * x0 * z1 + x1 * z2 * z0) / (x1 * x1 - z1 * z1)
    t2 = (x0 * x1 * z2 + x2 * z0 * z1) / (x2 * x2 - z2 * z2)
    t3 = (x3 * y0 * y2 - x0 * x2 * y3) / (x3 * x3 - y3 * y3)
    t4 = (y0 * y2 * z4 + y4 * z0 * z2) / (y4 * y4 - z4 * z4)

    return [
        (x0, y0, z0, t0),
        (x1, y1, z1, t1),
        (x2, y2, z2, t2),
        (x3, y3, z3, t3),
        (x4, y4, z4, t4),
    ]


def generate(n: int, add_torsion: bool) -> BremnerOutput:
    point = curve_mul(n, GENERATOR_Q)
    if add_torsion:
        point = curve_add(point, TORSION_T)
    if point is None:
        raise ValueError("selected point is infinity")

    rational_rows = bremner_rational_rows(point)
    flat = [v for row in rational_rows for v in row]
    ints, scale = primitive_integer_scale(flat)
    rows = [ints[i : i + 4] for i in range(0, len(ints), 4)]

    base = rows[0]
    deltas = sorted(2 * abs(v) for v in base)
    base_x = base[0]
    n_values = sorted(row[0] * row[0] - base_x * base_x for row in rows[1:])
    positive_count = sum(1 for z in n_values if z > 0)

    return BremnerOutput(
        point=(str(point[0]), str(point[1])),
        scale=str(scale),
        half_difference_table=rows,
        deltas=deltas,
        N_values=n_values,
        positive_N_count=positive_count,
        all_N_positive=positive_count == len(n_values),
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, required=True, help="Use nQ on Bremner's final elliptic curve.")
    parser.add_argument("--torsion", action="store_true", help="Use nQ + T instead of nQ.")
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()

    output = generate(args.n, args.torsion)
    payload = output.to_jsonable()
    text = json.dumps(payload, indent=2, sort_keys=True)
    print(text)
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
