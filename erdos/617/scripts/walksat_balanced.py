from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path

import numpy as np


def build_instance(r: int) -> tuple[list[tuple[int, int]], np.ndarray, list[np.ndarray]]:
    n = r * r + 1
    edges = [(i, j) for i in range(n) for j in range(i + 1, n)]
    edge_id = {e: idx for idx, e in enumerate(edges)}
    subsets = []
    edge_to_subsets = [[] for _ in edges]
    for sid, S in enumerate(itertools.combinations(range(n), r + 1)):
        eids = []
        for a, b in itertools.combinations(S, 2):
            eid = edge_id[(a, b)]
            eids.append(eid)
            edge_to_subsets[eid].append(sid)
        subsets.append(eids)
    subset_edges = np.array(subsets, dtype=np.int32)
    edge_to_subsets_np = [np.array(v, dtype=np.int32) for v in edge_to_subsets]
    return edges, subset_edges, edge_to_subsets_np


def counts_from_coloring(colors: np.ndarray, subset_edges: np.ndarray, r: int) -> np.ndarray:
    counts = np.zeros((subset_edges.shape[0], r), dtype=np.int8)
    for c in range(r):
        counts[:, c] = (colors[subset_edges] == c).sum(axis=1)
    return counts


def violation_stats(counts: np.ndarray) -> tuple[int, int, np.ndarray]:
    missing_per_subset = (counts == 0).sum(axis=1)
    bad_subset_ids = np.flatnonzero(missing_per_subset)
    return int(missing_per_subset.sum()), int(bad_subset_ids.size), bad_subset_ids


def greedy_flip_gain(
    edge_to_subsets: list[np.ndarray],
    counts: np.ndarray,
    edge: int,
    old: int,
    new: int,
) -> int:
    if old == new:
        return -10**9
    ids = edge_to_subsets[edge]
    # old color loses one count: if it was 1, that creates one missing color.
    # new color gains one count: if it was 0, that repairs one missing color.
    return int((counts[ids, new] == 0).sum() - (counts[ids, old] == 1).sum())


def apply_flip(
    edge_to_subsets: list[np.ndarray],
    counts: np.ndarray,
    colors: np.ndarray,
    edge: int,
    new: int,
) -> int:
    old = int(colors[edge])
    if old == new:
        return 0
    ids = edge_to_subsets[edge]
    delta = int((counts[ids, old] == 1).sum() - (counts[ids, new] == 0).sum())
    counts[ids, old] -= 1
    counts[ids, new] += 1
    colors[edge] = new
    return delta


def search(
    r: int,
    restarts: int,
    steps: int,
    seed: int,
    out_dir: Path,
    noise: float,
) -> dict:
    rng = np.random.default_rng(seed)
    edges, subset_edges, edge_to_subsets = build_instance(r)
    m = len(edges)
    best = {
        "missing_total": 10**18,
        "bad_subsets": 10**18,
        "restart": None,
        "step": None,
        "colors": None,
    }

    for restart in range(restarts):
        colors = rng.integers(0, r, size=m, dtype=np.int8)
        counts = counts_from_coloring(colors, subset_edges, r)
        missing_total, bad_count, bad_ids = violation_stats(counts)
        if (missing_total, bad_count) < (best["missing_total"], best["bad_subsets"]):
            best.update(
                {
                    "missing_total": missing_total,
                    "bad_subsets": bad_count,
                    "restart": restart,
                    "step": 0,
                    "colors": colors.copy(),
                }
            )
            print(f"restart={restart} step=0 missing={missing_total} bad={bad_count}", flush=True)
        if missing_total == 0:
            break

        for step in range(1, steps + 1):
            if step % 200 == 0:
                missing_total, bad_count, bad_ids = violation_stats(counts)
                if missing_total == 0:
                    best.update(
                        {
                            "missing_total": 0,
                            "bad_subsets": 0,
                            "restart": restart,
                            "step": step,
                            "colors": colors.copy(),
                        }
                    )
                    break
            if len(bad_ids) == 0:
                break
            sid = int(rng.choice(bad_ids))
            missing_colors = np.flatnonzero(counts[sid] == 0)
            if missing_colors.size == 0:
                _, _, bad_ids = violation_stats(counts)
                continue
            target_color = int(rng.choice(missing_colors))
            candidate_edges = subset_edges[sid]
            if rng.random() < noise:
                edge = int(rng.choice(candidate_edges))
            else:
                gains = [
                    (
                        greedy_flip_gain(edge_to_subsets, counts, int(e), int(colors[e]), target_color),
                        float(rng.random()),
                        int(e),
                    )
                    for e in candidate_edges
                    if int(colors[e]) != target_color
                ]
                if not gains:
                    edge = int(rng.choice(candidate_edges))
                else:
                    edge = max(gains)[2]
            missing_total += apply_flip(edge_to_subsets, counts, colors, edge, target_color)

            if missing_total < best["missing_total"] or (
                missing_total == best["missing_total"] and step % 1000 == 0
            ):
                _, bad_count_now, bad_ids_now = violation_stats(counts)
                if (missing_total, bad_count_now) < (best["missing_total"], best["bad_subsets"]):
                    best.update(
                        {
                            "missing_total": int(missing_total),
                            "bad_subsets": int(bad_count_now),
                            "restart": restart,
                            "step": step,
                            "colors": colors.copy(),
                        }
                    )
                    if step <= 200 or step % 1000 == 0 or missing_total < 100:
                        print(
                            f"restart={restart} step={step} missing={missing_total} bad={bad_count_now}",
                            flush=True,
                        )
                    bad_ids = bad_ids_now
                if missing_total == 0:
                    break
        if best["missing_total"] == 0:
            break

    out_dir.mkdir(parents=True, exist_ok=True)
    summary = {k: v for k, v in best.items() if k != "colors"}
    summary.update({"r": r, "n": r * r + 1, "edges": m, "subsets": int(subset_edges.shape[0])})
    (out_dir / f"walksat_r{r}_summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    if best["colors"] is not None:
        color_rows = [
            {"edge": list(edges[i]), "color": int(c)}
            for i, c in enumerate(best["colors"].tolist())
        ]
        (out_dir / f"walksat_r{r}_best_coloring.json").write_text(
            json.dumps(color_rows, indent=2),
            encoding="utf-8",
        )
    return summary


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--r", type=int, default=5)
    parser.add_argument("--restarts", type=int, default=20)
    parser.add_argument("--steps", type=int, default=50000)
    parser.add_argument("--seed", type=int, default=617)
    parser.add_argument("--noise", type=float, default=0.02)
    parser.add_argument("--out-dir", type=Path, default=Path("erdos/617/results"))
    args = parser.parse_args()
    summary = search(args.r, args.restarts, args.steps, args.seed, args.out_dir, args.noise)
    print(json.dumps(summary, indent=2))
    return 0 if summary["missing_total"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
