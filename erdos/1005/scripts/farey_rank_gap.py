#!/usr/bin/env python3
"""Small exact Farey rank-gap explorer for EP1005.

The script is intentionally simple: it builds the Farey sequence F_n, then
checks increasing index gaps until it finds the first pair whose numerator and
denominator move in opposite directions. If that raw rank gap is l-k, the
EP1005/OEIS convention is f(n) = l-k-1.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction
from math import gcd
from typing import Dict, List, Optional, Sequence, Tuple


Term = Tuple[int, int]


class NoBadPairError(ValueError):
    """Raised when F_n has no non-similarly-ordered pair."""


@dataclass(frozen=True)
class PairRecord:
    left_rank: int
    right_rank: int
    left: Term
    right: Term

    @property
    def raw_gap(self) -> int:
        return self.right_rank - self.left_rank

    @property
    def in_between(self) -> int:
        return self.raw_gap - 1

    @property
    def delta_num(self) -> int:
        return self.right[0] - self.left[0]

    @property
    def delta_den(self) -> int:
        return self.right[1] - self.left[1]


@dataclass(frozen=True)
class SearchResult:
    n: int
    farey_size: int
    raw_gap: int
    in_between: int
    total_pairs_at_gap: int
    shown_pairs: Tuple[PairRecord, ...]


def farey_sequence(n: int) -> List[Term]:
    """Return the Farey sequence of order n from 0/1 through 1/1."""
    if n < 1:
        raise ValueError("n must be at least 1")

    seq: List[Term] = []
    a, b = 0, 1
    c, d = 1, n
    seq.append((a, b))

    while c <= n:
        seq.append((c, d))
        k = (n + b) // d
        a, b, c, d = c, d, k * c - a, k * d - b

    return seq


def similarly_ordered(left: Term, right: Term) -> bool:
    """Return True when (a-c)(b-d) >= 0 for two Farey terms."""
    return (left[0] - right[0]) * (left[1] - right[1]) >= 0


def is_bad_pair(left: Term, right: Term) -> bool:
    return not similarly_ordered(left, right)


def shortest_bad_pairs(n: int, max_pairs: Optional[int] = 8) -> SearchResult:
    """Find the minimum raw rank gap l-k among non-similarly-ordered pairs."""
    if max_pairs is not None and max_pairs < 0:
        raise ValueError("max_pairs must be nonnegative")

    seq = farey_sequence(n)
    size = len(seq)

    for gap in range(1, size):
        shown: List[PairRecord] = []
        total = 0
        for i in range(size - gap):
            left = seq[i]
            right = seq[i + gap]
            if is_bad_pair(left, right):
                total += 1
                if max_pairs is None or len(shown) < max_pairs:
                    shown.append(
                        PairRecord(
                            left_rank=i + 1,
                            right_rank=i + gap + 1,
                            left=left,
                            right=right,
                        )
                    )
        if total:
            return SearchResult(
                n=n,
                farey_size=size,
                raw_gap=gap,
                in_between=gap - 1,
                total_pairs_at_gap=total,
                shown_pairs=tuple(shown),
            )

    raise NoBadPairError(f"F_{n} has no non-similarly-ordered pair")


def parse_fraction_text(text: str) -> Term:
    try:
        value = Fraction(text)
    except (ValueError, ZeroDivisionError) as exc:
        raise argparse.ArgumentTypeError(f"not a fraction: {text!r}") from exc

    if value < 0 or value > 1:
        raise argparse.ArgumentTypeError("Farey fractions here must lie in [0, 1]")
    return (value.numerator, value.denominator)


def rank_gap_report(n: int, left: Term, right: Term) -> PairRecord:
    seq = farey_sequence(n)
    ranks: Dict[Term, int] = {term: i + 1 for i, term in enumerate(seq)}
    missing = [term_text(term) for term in (left, right) if term not in ranks]
    if missing:
        raise ValueError(
            f"not present in F_{n}: {', '.join(missing)} "
            "(check denominators and reduction)"
        )

    left_rank = ranks[left]
    right_rank = ranks[right]
    if left_rank == right_rank:
        raise ValueError("the two endpoint fractions are equal")
    if left_rank > right_rank:
        left, right = right, left
        left_rank, right_rank = right_rank, left_rank

    return PairRecord(
        left_rank=left_rank,
        right_rank=right_rank,
        left=left,
        right=right,
    )


def term_text(term: Term) -> str:
    return f"{term[0]}/{term[1]}"


def pair_text(pair: PairRecord) -> str:
    status = "bad" if is_bad_pair(pair.left, pair.right) else "similarly ordered"
    return (
        f"ranks {pair.left_rank}->{pair.right_rank} "
        f"(raw gap {pair.raw_gap}, f-style gap {pair.in_between}): "
        f"{term_text(pair.left)} < {term_text(pair.right)}; "
        f"delta=({pair.delta_num:+d}, {pair.delta_den:+d}); {status}"
    )


def format_search_result(result: SearchResult) -> str:
    lines = [
        f"Farey order n={result.n}",
        f"|F_n|={result.farey_size}",
        f"shortest raw rank gap l-k={result.raw_gap}",
        f"EP1005/OEIS f(n)=l-k-1={result.in_between}",
        f"bad pairs at this gap={result.total_pairs_at_gap}",
    ]
    if result.shown_pairs:
        lines.append("sample shortest bad pairs:")
        lines.extend(f"  {pair_text(pair)}" for pair in result.shown_pairs)
    return "\n".join(lines)


def print_sequence(n: int) -> None:
    print(f"F_{n}:")
    print(" ".join(term_text(term) for term in farey_sequence(n)))


def totients_up_to(n: int) -> List[int]:
    phi = list(range(n + 1))
    for p in range(2, n + 1):
        if phi[p] == p:
            for multiple in range(p, n + 1, p):
                phi[multiple] -= phi[multiple] // p
    return phi


def assert_farey_invariants(n: int) -> None:
    seq = farey_sequence(n)
    phi = totients_up_to(n)
    expected_size = 1 + sum(phi[1:])
    if len(seq) != expected_size:
        raise AssertionError(f"F_{n} length {len(seq)} != {expected_size}")

    for a, b in seq:
        if not (0 <= a <= b <= n and gcd(a, b) == 1):
            raise AssertionError(f"invalid term in F_{n}: {a}/{b}")

    for (a, b), (c, d) in zip(seq, seq[1:]):
        if a * d >= c * b:
            raise AssertionError(f"not increasing in F_{n}: {a}/{b}, {c}/{d}")
        if b * c - a * d != 1:
            raise AssertionError(f"not Farey adjacent in F_{n}: {a}/{b}, {c}/{d}")


def run_sanity(max_pairs: int) -> None:
    print("Sanity checks: recurrence invariants for n=1..12")
    for n in range(1, 13):
        assert_farey_invariants(n)
    print("ok")
    print()
    print("Shortest bad-pair table:")
    print("n  |F_n|  raw_gap  f(n)  first_sample")
    print("-- -----  -------  ----  ------------")
    for n in range(4, 13):
        result = shortest_bad_pairs(n, max_pairs=max_pairs)
        sample = result.shown_pairs[0] if result.shown_pairs else None
        sample_text = (
            f"{term_text(sample.left)} < {term_text(sample.right)}"
            if sample is not None
            else "(not shown)"
        )
        print(
            f"{n:2d} {result.farey_size:5d} "
            f"{result.raw_gap:8d} {result.in_between:5d}  {sample_text}"
        )


def print_range(start: int, stop: int, max_pairs: int) -> None:
    if start > stop:
        raise ValueError("range start must be <= stop")
    print("n  |F_n|  raw_gap  f(n)  bad_pairs_at_gap  first_sample")
    print("-- -----  -------  ----  ----------------  ------------")
    for n in range(start, stop + 1):
        try:
            result = shortest_bad_pairs(n, max_pairs=max_pairs)
        except NoBadPairError:
            print(f"{n:2d} {len(farey_sequence(n)):5d}  none     none  none              none")
            continue
        sample = result.shown_pairs[0] if result.shown_pairs else None
        sample_text = (
            f"{term_text(sample.left)} < {term_text(sample.right)}"
            if sample is not None
            else "(not shown)"
        )
        print(
            f"{n:2d} {result.farey_size:5d} "
            f"{result.raw_gap:8d} {result.in_between:5d} "
            f"{result.total_pairs_at_gap:18d}  {sample_text}"
        )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Generate Farey sequences and find shortest non-similarly-ordered "
            "pairs for modest EP1005 computations."
        )
    )
    parser.add_argument(
        "n",
        nargs="?",
        type=int,
        help="Farey order to analyze; defaults to 12 unless --sanity exits first.",
    )
    parser.add_argument(
        "--range",
        dest="n_range",
        nargs=2,
        type=int,
        metavar=("START", "STOP"),
        help="Analyze every n in the inclusive range START..STOP.",
    )
    parser.add_argument(
        "--gap",
        nargs=2,
        type=parse_fraction_text,
        metavar=("LEFT", "RIGHT"),
        help="Report the Farey rank gap between two fractions in F_n.",
    )
    parser.add_argument(
        "--sequence",
        action="store_true",
        help="Print the full Farey sequence F_n before the search result.",
    )
    parser.add_argument(
        "--max-pairs",
        type=int,
        default=8,
        help="Maximum shortest bad pairs to show; use 0 for only counts.",
    )
    parser.add_argument(
        "--sanity",
        action="store_true",
        help="Run recurrence checks and print a small n=4..12 sanity table.",
    )
    return parser


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.max_pairs < 0:
        parser.error("--max-pairs must be nonnegative")
    if args.n is not None and args.n < 1:
        parser.error("n must be at least 1")
    if args.n_range is not None and args.gap is not None:
        parser.error("--gap can only be used with a single n")

    if args.sanity:
        run_sanity(args.max_pairs)
        if args.n is None and args.n_range is None and not args.sequence and args.gap is None:
            return 0
        print()

    if args.n_range is not None:
        start, stop = args.n_range
        if start < 1 or stop < 1:
            parser.error("range endpoints must be at least 1")
        print_range(start, stop, args.max_pairs)
        return 0

    n = args.n if args.n is not None else 12
    if args.sequence:
        print_sequence(n)
        print()

    if args.gap is not None:
        try:
            pair = rank_gap_report(n, args.gap[0], args.gap[1])
        except ValueError as exc:
            parser.error(str(exc))
        print(pair_text(pair))
        return 0

    try:
        result = shortest_bad_pairs(n, max_pairs=args.max_pairs)
    except NoBadPairError as exc:
        print(str(exc))
        return 1
    print(format_search_result(result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
