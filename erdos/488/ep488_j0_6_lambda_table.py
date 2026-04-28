"""
Exact lambda-range charging table for EP-488, j0 = 6.

This script records the exact interval-by-interval coefficients used in the
April 10, 2026 closure attempt for the j0 = 6 case.

Notation:
  x = n / a1
  lambda = m / n

On each interval I, the total bad excess is bounded by

    E_bad(I) <= n * (A_I * x + B_I),

while the available budget satisfies

    S1 + S2 > lambda * x * n.

The table below uses exact right-limit coefficients at the left endpoint of
each interval. Since the bad-package coefficient is nonincreasing in lambda
on each interval, and lambda * x is increasing in lambda, the left endpoint
is the worst case.
"""

from __future__ import annotations

from fractions import Fraction


def band_sum_coeff(package_coeff: Fraction, band: int) -> tuple[Fraction, Fraction]:
    """Return (A, B) so package total <= n * (A*x + B) on band `band`."""
    geom = Fraction(2 * band + 1, band * band * (band + 1) * (band + 1))
    alpha = Fraction(5, 2) * package_coeff * geom
    beta = package_coeff * Fraction(5, 4 * band * (band + 1))
    return alpha, beta


INTERVALS = [
    {
        "label": "I1",
        "range": (Fraction(13, 11), Fraction(13, 10)),
        "x_min": Fraction(15, 1),
        "high": {10: Fraction(7, 1)},
        "direct": {},
    },
    {
        "label": "I2",
        "range": (Fraction(13, 10), Fraction(17, 13)),
        "x_min": Fraction(15, 1),
        "high": {9: Fraction(4, 1), 10: Fraction(22, 5)},
        "direct": {},
    },
    {
        "label": "I3",
        "range": (Fraction(17, 13), Fraction(7, 5)),
        "x_min": Fraction(18, 1),
        "high": {9: Fraction(50, 13), 10: Fraction(55, 13), 12: Fraction(5, 1)},
        "direct": {},
    },
    {
        "label": "I4",
        "range": (Fraction(7, 5), Fraction(17, 12)),
        "x_min": Fraction(18, 1),
        "high": {9: Fraction(2, 1), 10: Fraction(11, 5), 12: Fraction(5, 1)},
        "direct": {4: Fraction(1, 1)},
    },
    {
        "label": "I5",
        "range": (Fraction(17, 12), Fraction(13, 9)),
        "x_min": Fraction(18, 1),
        "high": {
            9: Fraction(5, 3),
            10: Fraction(11, 6),
            11: Fraction(2, 1),
            12: Fraction(25, 6),
        },
        "direct": {4: Fraction(5, 6)},
    },
    {
        "label": "I6",
        "range": (Fraction(13, 9), Fraction(3, 2)),
        "x_min": Fraction(18, 1),
        "high": {
            9: Fraction(10, 9),
            10: Fraction(11, 9),
            11: Fraction(8, 3),
            12: Fraction(130, 9),
        },
        "direct": {4: Fraction(5, 9), 8: Fraction(1, 1)},
    },
    {
        "label": "I7",
        "range": (Fraction(3, 2), Fraction(17, 11)),
        "x_min": Fraction(18, 1),
        "high": {12: Fraction(13, 1)},
        "direct": {},
    },
    {
        "label": "I8",
        "range": (Fraction(17, 11), Fraction(19, 12)),
        "x_min": Fraction(18, 1),
        "high": {10: Fraction(10, 1), 12: Fraction(130, 11)},
        "direct": {},
    },
    {
        "label": "I9",
        "range": (Fraction(19, 12), Fraction(17, 10)),
        "x_min": Fraction(18, 1),
        "high": {10: Fraction(55, 6), 11: Fraction(10, 1), 12: Fraction(65, 6)},
        "direct": {},
    },
    {
        "label": "I10",
        "range": (Fraction(17, 10), Fraction(13, 7)),
        "x_min": Fraction(18, 1),
        "high": {
            9: Fraction(6, 1),
            10: Fraction(33, 5),
            11: Fraction(36, 5),
            12: Fraction(39, 5),
        },
        "direct": {},
    },
]


TAIL = {
    "label": "I_tail",
    "range": (Fraction(13, 7), Fraction(11, 1)),
    "x_min": Fraction(18, 1),
    # Universal package/direct coefficients from the v23 note.
    "high": {
        9: Fraction(40, 1),
        10: Fraction(153, 2),
        11: Fraction(89, 1),
        12: Fraction(277, 2),
    },
    "direct": {
        4: Fraction(1, 1),
        6: Fraction(4, 1),
        7: Fraction(2, 1),
        8: Fraction(16, 1),
    },
}


def summarize(interval: dict[str, object]) -> dict[str, object]:
    alpha = Fraction(0, 1)
    beta = Fraction(0, 1)

    for band, coeff in interval["high"].items():
        a, b = band_sum_coeff(coeff, band)
        alpha += a
        beta += b

    for band, coeff in interval["direct"].items():
        a, b = band_sum_coeff(coeff, band)
        alpha += a
        beta += b

    lam_left = interval["range"][0]
    x_min = interval["x_min"]
    margin = lam_left * x_min - (alpha * x_min + beta)

    return {
        "label": interval["label"],
        "lambda_left": lam_left,
        "lambda_right": interval["range"][1],
        "x_min": x_min,
        "alpha": alpha,
        "beta": beta,
        "margin": margin,
    }


def main() -> None:
    print("label  lambda-range          x_min  A                     B                     margin")
    rows = [summarize(item) for item in INTERVALS] + [summarize(TAIL)]
    for row in rows:
        print(
            f"{row['label']:6s} "
            f"({row['lambda_left']}, {row['lambda_right']}) "
            f"{row['x_min']:>5}  "
            f"{row['alpha']!s:>20}  "
            f"{row['beta']!s:>20}  "
            f"{row['margin']!s:>20}"
        )

    worst = min(rows, key=lambda row: row["margin"])
    print()
    print(f"Worst margin: {worst['margin']} on {worst['label']}")


if __name__ == "__main__":
    main()
