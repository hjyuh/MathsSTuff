from __future__ import annotations

import argparse
import itertools
import json
import math
import random
import time
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_TEMPLATE = ROOT / "results" / "ramsey_26_6_max65_model_summary.model.json"
DEFAULT_OUT = ROOT / "results" / "codex_ramsey_template_pack.json"


def edge_list(n: int) -> tuple[list[tuple[int, int]], dict[tuple[int, int], int]]:
    edges = [(i, j) for i in range(n) for j in range(i + 1, n)]
    return edges, {edge: idx for idx, edge in enumerate(edges)}


def iter_bits(mask: int) -> Iterable[int]:
    while mask:
        bit = mask & -mask
        yield bit.bit_length() - 1
        mask ^= bit


def load_template(path: Path) -> list[tuple[int, int]]:
    rows = json.loads(path.read_text(encoding="utf-8"))
    edges = []
    for row in rows:
        a, b = row
        if a == b:
            raise ValueError(f"loop in template edge {row}")
        if a > b:
            a, b = b, a
        edges.append((int(a), int(b)))
    if len(edges) != len(set(edges)):
        raise ValueError("template has duplicate edges")
    return edges


def template_alpha_check(n: int, template: set[tuple[int, int]], clique: int) -> dict[str, object]:
    independent_witness = None
    clique_witness = None
    for subset in itertools.combinations(range(n), clique):
        present = 0
        for a, b in itertools.combinations(subset, 2):
            if (a, b) in template:
                present += 1
        if present == 0 and independent_witness is None:
            independent_witness = subset
        if present == math.comb(clique, 2) and clique_witness is None:
            clique_witness = subset
        if independent_witness is not None and clique_witness is not None:
            break
    return {
        "no_independent_6": independent_witness is None,
        "independent_6_witness": list(independent_witness) if independent_witness else None,
        "no_clique_6": clique_witness is None,
        "clique_6_witness": list(clique_witness) if clique_witness else None,
    }


def mask_for_perm(
    template_edges: list[tuple[int, int]],
    permutation: list[int],
    edge_id: dict[tuple[int, int], int],
) -> int:
    mask = 0
    for a, b in template_edges:
        x = permutation[a]
        y = permutation[b]
        if x > y:
            x, y = y, x
        mask |= 1 << edge_id[(x, y)]
    return mask


def packing_objective(counts: list[int]) -> int:
    return sum((count - 1) * (count - 1) for count in counts)


def coverage_summary(counts: list[int], edges: list[tuple[int, int]]) -> dict[str, object]:
    uncovered = [edges[i] for i, count in enumerate(counts) if count == 0]
    overlapped = [
        {"edge": list(edges[i]), "multiplicity": count}
        for i, count in enumerate(counts)
        if count > 1
    ]
    return {
        "objective": packing_objective(counts),
        "uncovered_edges": len(uncovered),
        "overlapped_edges": len(overlapped),
        "max_multiplicity": max(counts),
        "uncovered_edge_list": [list(edge) for edge in uncovered],
        "overlapped_edge_list": overlapped,
    }


def induced_coloring_stats(
    n: int,
    r: int,
    edges: list[tuple[int, int]],
    masks: list[int],
) -> dict[str, object]:
    colors = [-1] * len(edges)
    color_sizes = [0] * r
    for color, mask in enumerate(masks):
        for eid in iter_bits(mask):
            if colors[eid] == -1:
                colors[eid] = color
                color_sizes[color] += 1
    for eid, color in enumerate(colors):
        if color == -1:
            # Assign uncovered edges to the currently smallest color class.
            chosen = min(range(r), key=color_sizes.__getitem__)
            colors[eid] = chosen
            color_sizes[chosen] += 1

    edge_id = {edge: idx for idx, edge in enumerate(edges)}
    missing_total = 0
    bad_subsets = 0
    first_bad = None
    for subset in itertools.combinations(range(n), r + 1):
        seen = set()
        for a, b in itertools.combinations(subset, 2):
            seen.add(colors[edge_id[(a, b)]])
        missing = sorted(set(range(r)) - seen)
        if missing:
            missing_total += len(missing)
            bad_subsets += 1
            if first_bad is None:
                first_bad = {"subset": list(subset), "missing": missing}
    return {
        "derived_missing_total": missing_total,
        "derived_bad_subsets": bad_subsets,
        "derived_color_sizes": color_sizes,
        "derived_first_bad": first_bad,
    }


def search_pack(
    n: int,
    r: int,
    template_edges: list[tuple[int, int]],
    seconds_per_seed: float,
    seeds: list[int],
    log_interval: int,
) -> dict[str, object]:
    edges, edge_id = edge_list(n)
    best: dict[str, object] | None = None

    for seed in seeds:
        rng = random.Random(seed)
        permutations = []
        masks = []
        counts = [0] * len(edges)
        for _ in range(r):
            permutation = list(range(n))
            rng.shuffle(permutation)
            mask = mask_for_perm(template_edges, permutation, edge_id)
            permutations.append(permutation)
            masks.append(mask)
            for eid in iter_bits(mask):
                counts[eid] += 1

        current = packing_objective(counts)
        seed_best_obj = current
        started = time.perf_counter()
        step = 0
        print(
            f"seed={seed} start objective={current} uncovered={sum(c == 0 for c in counts)} "
            f"overlapped={sum(c > 1 for c in counts)}",
            flush=True,
        )

        while time.perf_counter() - started < seconds_per_seed:
            step += 1
            color = rng.randrange(r)
            a = rng.randrange(n)
            b = rng.randrange(n - 1)
            if b >= a:
                b += 1

            permutation = permutations[color]
            permutation[a], permutation[b] = permutation[b], permutation[a]
            new_mask = mask_for_perm(template_edges, permutation, edge_id)
            old_mask = masks[color]
            if new_mask == old_mask:
                permutation[a], permutation[b] = permutation[b], permutation[a]
                continue

            removed = old_mask & ~new_mask
            added = new_mask & ~old_mask
            delta = 0
            for eid in iter_bits(removed):
                count = counts[eid]
                delta += (count - 2) * (count - 2) - (count - 1) * (count - 1)
            for eid in iter_bits(added):
                count = counts[eid]
                delta += count * count - (count - 1) * (count - 1)

            elapsed_fraction = min(1.0, (time.perf_counter() - started) / seconds_per_seed)
            temperature = max(0.05, 2.0 * (1.0 - elapsed_fraction))
            accept = delta <= 0 or rng.random() < math.exp(-delta / temperature)
            if accept:
                for eid in iter_bits(removed):
                    counts[eid] -= 1
                for eid in iter_bits(added):
                    counts[eid] += 1
                masks[color] = new_mask
                current += delta
            else:
                permutation[a], permutation[b] = permutation[b], permutation[a]

            if current < seed_best_obj:
                seed_best_obj = current
                elapsed = time.perf_counter() - started
                summary = coverage_summary(counts, edges)
                candidate = {
                    "seed": seed,
                    "step": step,
                    "elapsed_seconds": round(elapsed, 3),
                    "permutations": [p[:] for p in permutations],
                    "masks": masks[:],
                    "counts": counts[:],
                    **summary,
                }
                if best is None or candidate["objective"] < best["objective"]:  # type: ignore[index]
                    best = candidate
                print(
                    f"seed={seed} step={step} best_objective={current} "
                    f"uncovered={summary['uncovered_edges']} overlapped={summary['overlapped_edges']} "
                    f"elapsed={elapsed:.1f}",
                    flush=True,
                )
                if current == 0:
                    return best

            if log_interval > 0 and step % log_interval == 0:
                print(
                    f"seed={seed} step={step} current={current} seed_best={seed_best_obj} "
                    f"global_best={best['objective'] if best else 'n/a'}",
                    flush=True,
                )

    if best is None:
        raise RuntimeError("search did not initialize a best state")
    return best


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Pack five permuted 65-edge alpha<=5 templates as a structured EP617 search."
    )
    parser.add_argument("--template", type=Path, default=DEFAULT_TEMPLATE)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--n", type=int, default=26)
    parser.add_argument("--r", type=int, default=5)
    parser.add_argument("--seconds-per-seed", type=float, default=60.0)
    parser.add_argument("--seeds", type=int, nargs="+", default=[1, 2, 3])
    parser.add_argument("--log-interval", type=int, default=200000)
    args = parser.parse_args()

    if args.n != args.r * args.r + 1:
        raise SystemExit("this script is specialized to n = r^2 + 1")

    template_edges = load_template(args.template)
    template_set = set(template_edges)
    template_check = template_alpha_check(args.n, template_set, args.r + 1)
    if not template_check["no_independent_6"]:
        raise SystemExit(f"template is not alpha<=5: {template_check}")

    best = search_pack(
        n=args.n,
        r=args.r,
        template_edges=template_edges,
        seconds_per_seed=args.seconds_per_seed,
        seeds=args.seeds,
        log_interval=args.log_interval,
    )
    edges, _ = edge_list(args.n)
    masks = [int(mask) for mask in best.pop("masks")]  # type: ignore[arg-type]
    counts = [int(count) for count in best.pop("counts")]  # type: ignore[arg-type]
    result = {
        "status": "exact_pack_found" if best["objective"] == 0 else "partial_pack",
        "n": args.n,
        "r": args.r,
        "template_path": str(args.template),
        "template_edges": len(template_edges),
        "template_check": template_check,
        **best,
        "coverage": coverage_summary(counts, edges),
        "derived_coloring": induced_coloring_stats(args.n, args.r, edges, masks),
    }

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps({k: result[k] for k in ("status", "objective", "coverage", "derived_coloring")}, indent=2))
    return 0 if result["status"] == "exact_pack_found" else 1


if __name__ == "__main__":
    raise SystemExit(main())
