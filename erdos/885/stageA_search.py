from __future__ import annotations

import argparse
import json
import math
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Tuple


@dataclass
class Candidate:
    cid: int
    n: int
    factorization: List[Tuple[int, int]]
    tau: int


def tau_of(exps: List[int]) -> int:
    out = 1
    for e in exps:
        out *= e + 1
    return out


def factorization_to_string(fac: List[Tuple[int, int]]) -> str:
    if not fac:
        return "1"
    return "*".join(f"{p}^{e}" for p, e in fac if e > 0)


def parse_int_list(spec: str) -> List[int]:
    parts = [s.strip() for s in spec.split(",") if s.strip()]
    return [int(s) for s in parts]


def generate_smooth(limit: int, primes: List[int]) -> List[Tuple[int, List[Tuple[int, int]]]]:
    out: List[Tuple[int, List[Tuple[int, int]]]] = []

    def dfs(i: int, cur: int, fac: List[Tuple[int, int]]) -> None:
        if i == len(primes):
            out.append((cur, fac.copy()))
            return
        p = primes[i]
        x = cur
        e = 0
        while x <= limit:
            dfs(i + 1, x, fac + ([(p, e)] if e > 0 else []))
            if x > limit // p:
                break
            x *= p
            e += 1

    dfs(0, 1, [])
    out.sort(key=lambda t: t[0])
    dedup: List[Tuple[int, List[Tuple[int, int]]]] = []
    last = None
    for value, fac in out:
        if value != last:
            dedup.append((value, fac))
            last = value
    return dedup


def merge_factorizations(
    fac_a: List[Tuple[int, int]], fac_b: List[Tuple[int, int]]
) -> List[Tuple[int, int]]:
    exps: Dict[int, int] = {}
    for p, e in fac_a:
        exps[p] = exps.get(p, 0) + e
    for p, e in fac_b:
        exps[p] = exps.get(p, 0) + e
    return sorted((p, e) for p, e in exps.items() if e > 0)


def score_candidate(n: int, tau: int, gap: int) -> Tuple[int, int, int]:
    # Prefer lots of divisors and close factor pairs. Smaller n breaks ties.
    return (tau, -gap, -n)


def build_candidates(
    x_bound: int,
    m_max: int,
    primes: List[int],
    multipliers: List[int],
    max_candidates: int,
) -> List[Candidate]:
    smooth = generate_smooth(m_max, primes)
    multiplier_facs: Dict[int, List[Tuple[int, int]]] = {}
    for t in multipliers:
        fac_t: List[Tuple[int, int]] = []
        rem = t
        for p in primes:
            if p * p > rem:
                break
            e = 0
            while rem % p == 0:
                rem //= p
                e += 1
            if e > 0:
                fac_t.append((p, e))
        if rem > 1:
            fac_t.append((rem, 1))
        multiplier_facs[t] = fac_t

    seen = set()
    cands_unsorted: List[Candidate] = []
    generated = 0
    for m, fac in smooth:
        base = m * m
        fac2 = [(p, 2 * e) for p, e in fac if e > 0]
        for t in multipliers:
            n = base * t
            if n > x_bound:
                continue
            if n in seen:
                continue
            seen.add(n)
            fac_n = merge_factorizations(fac2, multiplier_facs[t])
            tau = tau_of([e for _, e in fac_n])
            cands_unsorted.append(Candidate(0, n, fac_n, tau))
            generated += 1

    # Prefer divisor-rich candidates, then smaller n.
    cands_unsorted.sort(key=lambda c: (-c.tau, c.n))
    cands = cands_unsorted[:max_candidates]
    cands.sort(key=lambda c: c.n)
    for i, c in enumerate(cands):
        c.cid = i
    return cands


def build_closepair_candidates(
    x_bound: int,
    smooth_limit: int,
    primes: List[int],
    max_candidates: int,
    pair_ratio: float,
    pair_gap_max: int,
) -> List[Candidate]:
    smooth = generate_smooth(smooth_limit, primes)
    values = [v for v, _ in smooth]
    facs = {v: fac for v, fac in smooth}

    best: Dict[int, Tuple[Tuple[int, int, int], List[Tuple[int, int]], int]] = {}

    for i, u in enumerate(values):
        fac_u = facs[u]
        max_v = min(x_bound // u, int(u * pair_ratio))
        if pair_gap_max > 0:
            max_v = min(max_v, u + pair_gap_max)
        for j in range(i, len(values)):
            v = values[j]
            if v > max_v:
                break
            n = u * v
            if n > x_bound:
                break
            fac_n = merge_factorizations(fac_u, facs[v])
            tau = tau_of([e for _, e in fac_n])
            gap = v - u
            score = score_candidate(n, tau, gap)
            prev = best.get(n)
            if prev is None or score > prev[0]:
                best[n] = (score, fac_n, tau)

    cands_unsorted: List[Candidate] = []
    for n, (_, fac_n, tau) in best.items():
        cands_unsorted.append(Candidate(0, n, fac_n, tau))

    cands_unsorted.sort(key=lambda c: (-c.tau, c.n))
    cands = cands_unsorted[:max_candidates]
    cands.sort(key=lambda c: c.n)
    for i, c in enumerate(cands):
        c.cid = i
    return cands


def enumerate_divisors(fac: List[Tuple[int, int]], max_divisors: int) -> List[int] | None:
    divs = [1]
    for p, e in fac:
        base = list(divs)
        pow_p = 1
        for _ in range(e):
            pow_p *= p
            for d in base:
                divs.append(d * pow_p)
                if len(divs) > max_divisors:
                    return None
    return divs


def deltas_from_divisors(n: int, divisors: List[int], delta_max: int) -> List[int]:
    s = math.isqrt(n)
    out: List[int] = []
    for a in divisors:
        if a > s:
            continue
        b = n // a
        d = b - a
        if d <= delta_max:
            out.append(d)
    return sorted(set(out))


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


def recover_factor_pair(n: int, delta: int) -> Tuple[int, int] | None:
    disc = delta * delta + 4 * n
    s = math.isqrt(disc)
    if s * s != disc:
        return None
    if (s - delta) % 2 != 0:
        return None
    a = (s - delta) // 2
    b = (s + delta) // 2
    if a < 0 or a * b != n:
        return None
    return a, b


def run_search(
    candidates: List[Candidate],
    delta_max: int,
    min_support: int,
    target_k: int,
    log_k4_min_support: int,
    out_dir: Path,
    max_divisors: int,
    log_k4_max_records: int,
    log_biclique_max_records: int,
    progress_interval: int,
    log_pair_min_support: int,
    log_triple_min_support: int,
    log_pair_max_records: int,
    log_triple_max_records: int,
) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)

    with (out_dir / "candidates.tsv").open("w", encoding="utf-8") as f:
        f.write("id\tn\ttau\tfactorization\n")
        for c in candidates:
            f.write(f"{c.cid}\t{c.n}\t{c.tau}\t{factorization_to_string(c.factorization)}\n")

    edges_by_delta: Dict[int, List[int]] = defaultdict(list)
    skipped_divisor_heavy = 0

    print(f"[stageA] candidates={len(candidates)} delta_max={delta_max} min_support={min_support}")
    print("[stageA] building delta index from divisor profiles...")
    for idx, c in enumerate(candidates, start=1):
        divs = enumerate_divisors(c.factorization, max_divisors)
        if divs is None:
            skipped_divisor_heavy += 1
            continue
        deltas = deltas_from_divisors(c.n, divs, delta_max)
        for d in deltas:
            edges_by_delta[d].append(c.cid)
        if progress_interval > 0 and idx % progress_interval == 0:
            print(f"[stageA] processed {idx}/{len(candidates)} candidates")

    for d in list(edges_by_delta.keys()):
        edges_by_delta[d] = sorted(set(edges_by_delta[d]))

    kept_deltas = [d for d, ids in edges_by_delta.items() if len(ids) >= min_support]
    kept_deltas.sort(key=lambda d: (len(edges_by_delta[d]), d))
    print(f"[stageA] kept_deltas={len(kept_deltas)}")

    with (out_dir / "stats.txt").open("w", encoding="utf-8") as f:
        f.write(f"candidates={len(candidates)}\n")
        f.write(f"delta_max={delta_max}\n")
        f.write(f"min_support={min_support}\n")
        f.write(f"target_k={target_k}\n")
        f.write(f"skipped_divisor_heavy={skipped_divisor_heavy}\n")
        f.write(f"kept_deltas={len(kept_deltas)}\n")

    pair_logged = 0
    triple_logged = 0
    k4_logged = 0
    biclique_logged = 0
    best_pair: Tuple[int, List[int], List[int]] = (0, [], [])
    best_triple: Tuple[int, List[int], List[int]] = (0, [], [])
    best_k4: Tuple[int, List[int], List[int]] = (0, [], [])
    best_k5: Tuple[int, List[int], List[int]] = (0, [], [])

    pair_file = (out_dir / "pairs.jsonl").open("w", encoding="utf-8")
    triple_file = (out_dir / "triples.jsonl").open("w", encoding="utf-8")
    k4_file = (out_dir / "k4.jsonl").open("w", encoding="utf-8")
    bic_file = (out_dir / "bicliques.jsonl").open("w", encoding="utf-8")

    def log_pair(prefix: List[int], inter: List[int]) -> None:
        nonlocal pair_logged
        if pair_logged >= log_pair_max_records:
            return
        sample_ids = inter[:20]
        sample_vals = [candidates[i].n for i in sample_ids]
        obj = {
            "type": "pair",
            "support": len(inter),
            "deltas": prefix,
            "sample_n_ids": sample_ids,
            "sample_n_values": sample_vals,
        }
        pair_file.write(json.dumps(obj) + "\n")
        pair_logged += 1

    def log_triple(prefix: List[int], inter: List[int]) -> None:
        nonlocal triple_logged
        if triple_logged >= log_triple_max_records:
            return
        sample_ids = inter[:20]
        sample_vals = [candidates[i].n for i in sample_ids]
        obj = {
            "type": "triple",
            "support": len(inter),
            "deltas": prefix,
            "sample_n_ids": sample_ids,
            "sample_n_values": sample_vals,
        }
        triple_file.write(json.dumps(obj) + "\n")
        triple_logged += 1

    def log_k4(prefix: List[int], inter: List[int]) -> None:
        nonlocal k4_logged
        if k4_logged >= log_k4_max_records:
            return
        sample_ids = inter[:20]
        sample_vals = [candidates[i].n for i in sample_ids]
        sample_relations = []
        for nid in sample_ids[:5]:
            n = candidates[nid].n
            rels = []
            for d in prefix:
                pair = recover_factor_pair(n, d)
                if pair is not None:
                    rels.append({"delta": d, "a": pair[0], "b": pair[1]})
            sample_relations.append({"n_id": nid, "n": n, "relations": rels})
        obj = {
            "type": "k4",
            "support": len(inter),
            "deltas": prefix,
            "sample_n_ids": sample_ids,
            "sample_n_values": sample_vals,
            "sample_relations": sample_relations,
        }
        k4_file.write(json.dumps(obj) + "\n")
        k4_logged += 1

    def log_biclique(prefix: List[int], inter: List[int]) -> None:
        nonlocal biclique_logged
        if biclique_logged >= log_biclique_max_records:
            return
        sample_ids = inter[:min_support]
        sample_vals = [candidates[i].n for i in sample_ids]
        sample_relations = []
        for nid in sample_ids:
            n = candidates[nid].n
            rels = []
            for d in prefix:
                pair = recover_factor_pair(n, d)
                if pair is not None:
                    rels.append({"delta": d, "a": pair[0], "b": pair[1]})
            sample_relations.append({"n_id": nid, "n": n, "relations": rels})
        obj = {
            "type": "biclique",
            "k": target_k,
            "support": len(sample_ids),
            "deltas": prefix,
            "n_ids": sample_ids,
            "n_values": sample_vals,
            "sample_relations": sample_relations,
        }
        bic_file.write(json.dumps(obj) + "\n")
        biclique_logged += 1

    def dfs(prefix: List[int], inter: List[int], start: int) -> None:
        nonlocal best_pair, best_triple, best_k4, best_k5
        if len(inter) < min_support:
            return
        if len(prefix) == target_k:
            if len(inter) > best_k5[0]:
                best_k5 = (len(inter), prefix.copy(), inter[:20].copy())
            log_biclique(prefix, inter)
            return
        if len(prefix) == 2 and len(inter) >= log_pair_min_support:
            log_pair(prefix, inter)
        if len(prefix) == 2 and len(inter) > best_pair[0]:
            best_pair = (len(inter), prefix.copy(), inter[:20].copy())
        if len(prefix) == 3 and len(inter) >= log_triple_min_support:
            log_triple(prefix, inter)
        if len(prefix) == 3 and len(inter) > best_triple[0]:
            best_triple = (len(inter), prefix.copy(), inter[:20].copy())
        if len(prefix) == 4 and len(inter) >= log_k4_min_support:
            log_k4(prefix, inter)
        if len(prefix) == 4 and len(inter) > best_k4[0]:
            best_k4 = (len(inter), prefix.copy(), inter[:20].copy())
        if len(prefix) + (len(kept_deltas) - start) < target_k:
            return

        for i in range(start, len(kept_deltas)):
            d = kept_deltas[i]
            inter2 = intersect_sorted(inter, edges_by_delta[d])
            if len(inter2) >= min_support:
                prefix.append(d)
                dfs(prefix, inter2, i + 1)
                prefix.pop()

    for idx, d0 in enumerate(kept_deltas):
        inter0 = edges_by_delta[d0]
        if len(inter0) >= min_support:
            dfs([d0], inter0, idx + 1)
        if progress_interval > 0 and (idx + 1) % max(1, progress_interval // 10) == 0:
            print(
                f"[stageA] searched {idx + 1}/{len(kept_deltas)} root deltas; "
                f"pairs={pair_logged} triples={triple_logged} k4={k4_logged} bicliques={biclique_logged}"
            )

    pair_file.close()
    triple_file.close()
    k4_file.close()
    bic_file.close()
    with (out_dir / "maxima.json").open("w", encoding="utf-8") as f:
        json.dump(
            {
                "best_pair": {
                    "support": best_pair[0],
                    "deltas": best_pair[1],
                    "sample_n_ids": best_pair[2],
                    "sample_n_values": [candidates[i].n for i in best_pair[2]],
                },
                "best_triple": {
                    "support": best_triple[0],
                    "deltas": best_triple[1],
                    "sample_n_ids": best_triple[2],
                    "sample_n_values": [candidates[i].n for i in best_triple[2]],
                },
                "best_k4": {
                    "support": best_k4[0],
                    "deltas": best_k4[1],
                    "sample_n_ids": best_k4[2],
                    "sample_n_values": [candidates[i].n for i in best_k4[2]],
                },
                "best_k5": {
                    "support": best_k5[0],
                    "deltas": best_k5[1],
                    "sample_n_ids": best_k5[2],
                    "sample_n_values": [candidates[i].n for i in best_k5[2]],
                },
            },
            f,
            indent=2,
        )
    print(
        f"[stageA] done: pairs={pair_logged} triples={triple_logged} "
        f"k4_logged={k4_logged} bicliques={biclique_logged}"
    )
    print(
        "[stageA] maxima: "
        f"pair={best_pair[0]} triple={best_triple[0]} "
        f"k4={best_k4[0]} k5={best_k5[0]}"
    )


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Stage A search for Erdos problem 885")
    p.add_argument("--x", type=int, default=10_000_000_000)
    p.add_argument("--delta-max", type=int, default=20_000)
    p.add_argument("--min-support", type=int, default=5)
    p.add_argument("--target-k", type=int, default=5)
    p.add_argument("--m-max", type=int, default=200_000)
    p.add_argument("--max-candidates", type=int, default=80_000)
    p.add_argument("--max-divisors", type=int, default=200_000)
    p.add_argument("--log-pair-min-support", type=int, default=30)
    p.add_argument("--log-triple-min-support", type=int, default=12)
    p.add_argument("--log-k4-min-support", type=int, default=5)
    p.add_argument("--log-pair-max-records", type=int, default=2000)
    p.add_argument("--log-triple-max-records", type=int, default=2000)
    p.add_argument("--log-k4-max-records", type=int, default=50_000)
    p.add_argument("--log-biclique-max-records", type=int, default=10_000)
    p.add_argument("--primes", type=str, default="2,3,5,7,11,13,17,19")
    p.add_argument("--multipliers", type=str, default="1,2,3,6,10,15")
    p.add_argument("--progress-interval", type=int, default=1000)
    p.add_argument("--candidate-mode", type=str, default="closepair", choices=["square", "closepair", "both"])
    p.add_argument("--smooth-limit", type=int, default=200000)
    p.add_argument("--pair-ratio", type=float, default=1.20)
    p.add_argument("--pair-gap-max", type=int, default=50000)
    p.add_argument("--out-dir", type=str, default="out_stageA_py")
    return p.parse_args()


def main() -> None:
    args = parse_args()
    primes = parse_int_list(args.primes)
    multipliers = parse_int_list(args.multipliers)
    print(f"[stageA] primes={primes}")
    print(f"[stageA] multipliers={multipliers}")
    print(f"[stageA] candidate_mode={args.candidate_mode}")

    candidates_map: Dict[int, Candidate] = {}

    if args.candidate_mode in ("square", "both"):
        sq_candidates = build_candidates(args.x, args.m_max, primes, multipliers, args.max_candidates)
        for c in sq_candidates:
            candidates_map[c.n] = c

    if args.candidate_mode in ("closepair", "both"):
        cp_candidates = build_closepair_candidates(
            args.x,
            args.smooth_limit,
            primes,
            args.max_candidates,
            args.pair_ratio,
            args.pair_gap_max,
        )
        for c in cp_candidates:
            prev = candidates_map.get(c.n)
            if prev is None or c.tau > prev.tau:
                candidates_map[c.n] = c

    candidates = sorted(candidates_map.values(), key=lambda c: c.n)
    if len(candidates) > args.max_candidates:
        candidates = sorted(candidates, key=lambda c: (-c.tau, c.n))[: args.max_candidates]
        candidates.sort(key=lambda c: c.n)
    for i, c in enumerate(candidates):
        c.cid = i

    run_search(
        candidates=candidates,
        delta_max=args.delta_max,
        min_support=args.min_support,
        target_k=args.target_k,
        log_k4_min_support=args.log_k4_min_support,
        out_dir=Path(args.out_dir),
        max_divisors=args.max_divisors,
        log_k4_max_records=args.log_k4_max_records,
        log_biclique_max_records=args.log_biclique_max_records,
        progress_interval=args.progress_interval,
        log_pair_min_support=args.log_pair_min_support,
        log_triple_min_support=args.log_triple_min_support,
        log_pair_max_records=args.log_pair_max_records,
        log_triple_max_records=args.log_triple_max_records,
    )
    print(f"Done. Outputs in: {args.out_dir}")


if __name__ == "__main__":
    main()
