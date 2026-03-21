from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Dict, List, Tuple


def a_max_for_delta(delta: int, x_bound: int) -> int:
    return (math.isqrt(delta * delta + 4 * x_bound) - delta) // 2


def postings_for_delta(delta: int, x_bound: int) -> List[int]:
    amax = a_max_for_delta(delta, x_bound)
    return [a * (a + delta) for a in range(1, amax + 1)]


def intersect_sorted(a: List[int], b: List[int]) -> List[int]:
    i = 0
    j = 0
    out: List[int] = []
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            out.append(a[i])
            i += 1
            j += 1
        elif a[i] < b[j]:
            i += 1
        else:
            j += 1
    return out


def recover_a(n: int, delta: int) -> int | None:
    disc = delta * delta + 4 * n
    s = math.isqrt(disc)
    if s * s != disc:
        return None
    if (s - delta) % 2 != 0:
        return None
    a = (s - delta) // 2
    if a <= 0 or a * (a + delta) != n:
        return None
    return a


def run_search(
    x_bound: int,
    delta_max: int,
    min_support: int,
    target_k: int,
    progress_interval: int,
    out_dir: Path,
    log_pair_max: int,
    log_triple_max: int,
    log_k4_max: int,
    log_k5_max: int,
) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"[delta-first] building postings up to delta={delta_max} with X={x_bound}")
    postings: Dict[int, List[int]] = {}
    kept_deltas: List[int] = []
    for delta in range(delta_max + 1):
        vals = postings_for_delta(delta, x_bound)
        if len(vals) >= min_support:
            postings[delta] = vals
            kept_deltas.append(delta)
        if progress_interval > 0 and delta % progress_interval == 0 and delta > 0:
            print(f"[delta-first] built {delta}/{delta_max} deltas; kept={len(kept_deltas)}")

    kept_deltas.sort(key=lambda d: (len(postings[d]), d))

    best_pair: Tuple[int, List[int], List[int]] = (0, [], [])
    best_triple: Tuple[int, List[int], List[int]] = (0, [], [])
    best_k4: Tuple[int, List[int], List[int]] = (0, [], [])
    best_k5: Tuple[int, List[int], List[int]] = (0, [], [])
    pair_logged = 0
    triple_logged = 0
    k4_logged = 0
    k5_logged = 0

    pair_file = (out_dir / "pairs.jsonl").open("w", encoding="utf-8")
    triple_file = (out_dir / "triples.jsonl").open("w", encoding="utf-8")
    k4_file = (out_dir / "k4.jsonl").open("w", encoding="utf-8")
    k5_file = (out_dir / "bicliques.jsonl").open("w", encoding="utf-8")

    def relation_payload(deltas: List[int], ns: List[int]) -> List[dict]:
        payload = []
        for n in ns[:5]:
            rels = []
            for d in deltas:
                a = recover_a(n, d)
                if a is not None:
                    rels.append({"delta": d, "a": a, "b": a + d})
            payload.append({"n": n, "relations": rels})
        return payload

    def log_json(file, typ: str, deltas: List[int], inter: List[int]) -> None:
        obj = {
            "type": typ,
            "support": len(inter),
            "deltas": deltas,
            "sample_n_values": inter[:20],
            "sample_relations": relation_payload(deltas, inter[:20]),
        }
        file.write(json.dumps(obj) + "\n")

    def dfs(prefix: List[int], inter: List[int], start: int) -> None:
        nonlocal best_pair, best_triple, best_k4, best_k5
        nonlocal pair_logged, triple_logged, k4_logged, k5_logged

        if len(inter) < min_support:
            return
        plen = len(prefix)
        if plen == 2 and len(inter) > best_pair[0]:
            best_pair = (len(inter), prefix.copy(), inter[:20].copy())
        if plen == 3 and len(inter) > best_triple[0]:
            best_triple = (len(inter), prefix.copy(), inter[:20].copy())
        if plen == 4 and len(inter) > best_k4[0]:
            best_k4 = (len(inter), prefix.copy(), inter[:20].copy())
        if plen == target_k and len(inter) > best_k5[0]:
            best_k5 = (len(inter), prefix.copy(), inter[:20].copy())

        if plen == 2 and pair_logged < log_pair_max:
            log_json(pair_file, "pair", prefix, inter)
            pair_logged += 1
        if plen == 3 and triple_logged < log_triple_max:
            log_json(triple_file, "triple", prefix, inter)
            triple_logged += 1
        if plen == 4 and k4_logged < log_k4_max:
            log_json(k4_file, "k4", prefix, inter)
            k4_logged += 1
        if plen == target_k:
            if k5_logged < log_k5_max:
                log_json(k5_file, "biclique", prefix, inter)
                k5_logged += 1
            return

        if plen + (len(kept_deltas) - start) < target_k:
            return

        for i in range(start, len(kept_deltas)):
            d = kept_deltas[i]
            inter2 = intersect_sorted(inter, postings[d])
            if len(inter2) >= min_support:
                prefix.append(d)
                dfs(prefix, inter2, i + 1)
                prefix.pop()

    print(f"[delta-first] kept_deltas={len(kept_deltas)}")
    for idx, d0 in enumerate(kept_deltas):
        dfs([d0], postings[d0], idx + 1)
        if progress_interval > 0 and (idx + 1) % max(1, progress_interval // 10) == 0:
            print(
                f"[delta-first] searched {idx + 1}/{len(kept_deltas)} root deltas; "
                f"best_pair={best_pair[0]} best_triple={best_triple[0]} "
                f"best_k4={best_k4[0]} best_k5={best_k5[0]}"
            )

    pair_file.close()
    triple_file.close()
    k4_file.close()
    k5_file.close()

    with (out_dir / "stats.txt").open("w", encoding="utf-8") as f:
        f.write(f"x_bound={x_bound}\n")
        f.write(f"delta_max={delta_max}\n")
        f.write(f"min_support={min_support}\n")
        f.write(f"target_k={target_k}\n")
        f.write(f"kept_deltas={len(kept_deltas)}\n")

    with (out_dir / "maxima.json").open("w", encoding="utf-8") as f:
        json.dump(
            {
                "best_pair": {
                    "support": best_pair[0],
                    "deltas": best_pair[1],
                    "sample_n_values": best_pair[2],
                },
                "best_triple": {
                    "support": best_triple[0],
                    "deltas": best_triple[1],
                    "sample_n_values": best_triple[2],
                },
                "best_k4": {
                    "support": best_k4[0],
                    "deltas": best_k4[1],
                    "sample_n_values": best_k4[2],
                },
                "best_k5": {
                    "support": best_k5[0],
                    "deltas": best_k5[1],
                    "sample_n_values": best_k5[2],
                },
            },
            f,
            indent=2,
        )

    print(
        "[delta-first] done: "
        f"best_pair={best_pair[0]} best_triple={best_triple[0]} "
        f"best_k4={best_k4[0]} best_k5={best_k5[0]}"
    )


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Direct delta-first search for Erdos problem 885")
    p.add_argument("--x", type=int, default=100_000_000)
    p.add_argument("--delta-max", type=int, default=5000)
    p.add_argument("--min-support", type=int, default=5)
    p.add_argument("--target-k", type=int, default=5)
    p.add_argument("--progress-interval", type=int, default=500)
    p.add_argument("--log-pair-max", type=int, default=1000)
    p.add_argument("--log-triple-max", type=int, default=1000)
    p.add_argument("--log-k4-max", type=int, default=1000)
    p.add_argument("--log-k5-max", type=int, default=1000)
    p.add_argument("--out-dir", type=str, default="out_delta_first")
    return p.parse_args()


def main() -> None:
    args = parse_args()
    run_search(
        x_bound=args.x,
        delta_max=args.delta_max,
        min_support=args.min_support,
        target_k=args.target_k,
        progress_interval=args.progress_interval,
        out_dir=Path(args.out_dir),
        log_pair_max=args.log_pair_max,
        log_triple_max=args.log_triple_max,
        log_k4_max=args.log_k4_max,
        log_k5_max=args.log_k5_max,
    )
    print(f"Done. Outputs in: {args.out_dir}")


if __name__ == "__main__":
    main()
