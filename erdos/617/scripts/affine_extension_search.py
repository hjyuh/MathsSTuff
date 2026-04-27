from __future__ import annotations

import argparse
import itertools
import random
from collections import Counter, defaultdict


def slope_class(p: int, a: tuple[int, int], b: tuple[int, int]) -> int:
    dx = (b[0] - a[0]) % p
    dy = (b[1] - a[1]) % p
    if dx == 0:
        return p
    return (dy * pow(dx, -1, p)) % p


def affine_coloring(p: int, merge: tuple[int, int]) -> tuple[list[tuple[int, int]], dict[tuple[int, int], int]]:
    """Return a p-coloring of K_{p^2} by merging two affine-plane slopes."""
    points = [(x, y) for x in range(p) for y in range(p)]
    slopes = list(range(p + 1))
    a, b = merge
    color_of_slope = {}
    color = 0
    color_of_slope[a] = color
    color_of_slope[b] = color
    color += 1
    for s in slopes:
        if s not in merge:
            color_of_slope[s] = color
            color += 1
    assert color == p
    edge_color = {}
    for i, u in enumerate(points):
        for j in range(i + 1, len(points)):
            v = points[j]
            edge_color[(i, j)] = color_of_slope[slope_class(p, u, v)]
    return points, edge_color


def old_subset_masks(n: int, p: int, edge_color: dict[tuple[int, int], int]) -> list[tuple[tuple[int, ...], int]]:
    """Constraints for a new vertex: for each old p-set S and missing color c, some x_v=c."""
    constraints = []
    all_mask = (1 << p) - 1
    missing_counts = Counter()
    for S in itertools.combinations(range(n), p):
        mask = 0
        for i, j in itertools.combinations(S, 2):
            if i > j:
                i, j = j, i
            mask |= 1 << edge_color[(i, j)]
        missing = all_mask ^ mask
        while missing:
            bit = missing & -missing
            c = bit.bit_length() - 1
            constraints.append((S, c))
            missing_counts[c] += 1
            missing ^= bit
    return constraints, missing_counts


def check_assignment(p: int, constraints: list[tuple[tuple[int, ...], int]], assignment: list[int]) -> bool:
    return all(any(assignment[v] == c for v in S) for S, c in constraints)


def greedy_random_search(
    p: int,
    constraints: list[tuple[tuple[int, ...], int]],
    restarts: int,
    steps: int,
    seed: int,
) -> tuple[list[int] | None, int]:
    rng = random.Random(seed)
    n = p * p
    by_var_color: dict[tuple[int, int], list[int]] = defaultdict(list)
    for idx, (S, c) in enumerate(constraints):
        for v in S:
            by_var_color[(v, c)].append(idx)

    best_unsat = len(constraints)
    for restart in range(restarts):
        assignment = [rng.randrange(p) for _ in range(n)]
        sat_count = [0] * len(constraints)
        unsat = set()
        for idx, (S, c) in enumerate(constraints):
            cnt = sum(assignment[v] == c for v in S)
            sat_count[idx] = cnt
            if cnt == 0:
                unsat.add(idx)
        best_unsat = min(best_unsat, len(unsat))
        if not unsat:
            return assignment, best_unsat

        tabu: dict[tuple[int, int], int] = {}
        for step in range(steps):
            if not unsat:
                return assignment, best_unsat
            target = rng.choice(tuple(unsat))
            S, c_needed = constraints[target]
            candidates = []
            for v in S:
                old = assignment[v]
                if old == c_needed:
                    continue
                key = (v, c_needed)
                if tabu.get(key, -1) > step and rng.random() > 0.02:
                    continue
                gain = 0
                # constraints gaining satisfaction when v changes to c_needed
                for idx in by_var_color[(v, c_needed)]:
                    if sat_count[idx] == 0:
                        gain += 1
                # constraints losing last witness when v leaves old color
                for idx in by_var_color[(v, old)]:
                    if sat_count[idx] == 1:
                        gain -= 1
                candidates.append((gain, rng.random(), v, old))
            if not candidates:
                continue
            _, _, v, old = max(candidates)
            new = c_needed
            assignment[v] = new
            tabu[(v, old)] = step + 3 + rng.randrange(5)
            for idx in by_var_color[(v, old)]:
                sat_count[idx] -= 1
                if sat_count[idx] == 0:
                    unsat.add(idx)
            for idx in by_var_color[(v, new)]:
                if sat_count[idx] == 0:
                    unsat.discard(idx)
                sat_count[idx] += 1
            if len(unsat) < best_unsat:
                best_unsat = len(unsat)
                print(f"restart={restart} step={step} best_unsat={best_unsat}", flush=True)
    return None, best_unsat


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--p", type=int, default=5)
    parser.add_argument("--restarts", type=int, default=200)
    parser.add_argument("--steps", type=int, default=20000)
    parser.add_argument("--seed", type=int, default=617)
    args = parser.parse_args()

    p = args.p
    best = None
    for merge in itertools.combinations(range(p + 1), 2):
        points, colors = affine_coloring(p, merge)
        constraints, counts = old_subset_masks(len(points), p, colors)
        print(f"merge={merge} constraints={len(constraints)} missing_counts={dict(counts)}")
        assignment, best_unsat = greedy_random_search(
            p,
            constraints,
            args.restarts,
            args.steps,
            args.seed + 1000 * merge[0] + merge[1],
        )
        print(f"merge={merge} done best_unsat={best_unsat}")
        if assignment is not None:
            print("FOUND")
            print("merge", merge)
            print("assignment", assignment)
            assert check_assignment(p, constraints, assignment)
            return 0
        if best is None or best_unsat < best[0]:
            best = (best_unsat, merge)
    print(f"NO_EXTENSION_FOUND best={best}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
