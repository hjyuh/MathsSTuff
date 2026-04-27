from __future__ import annotations

import argparse
import itertools
import json
import math
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

import numpy as np


def utc_ts() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def pair_index(u: int, v: int, n: int) -> int:
    """Map 0<=u<v<n to [0, nC2). Lex order by u then v."""
    if u > v:
        u, v = v, u
    # offset = sum_{i=0}^{u-1} (n-i-1) = u*(n-1) - u*(u-1)/2
    return u * (n - 1) - (u * (u - 1)) // 2 + (v - u - 1)


def all_pairs(n: int) -> tuple[np.ndarray, np.ndarray]:
    pu = np.empty(n * (n - 1) // 2, dtype=np.int16)
    pv = np.empty(n * (n - 1) // 2, dtype=np.int16)
    idx = 0
    for u in range(n - 1):
        for v in range(u + 1, n):
            pu[idx] = u
            pv[idx] = v
            idx += 1
    return pu, pv


@dataclass
class Instance:
    n: int
    pu: np.ndarray  # [m] u endpoint of pair idx
    pv: np.ndarray  # [m] v endpoint of pair idx
    six_verts: np.ndarray  # [num6,6] uint8
    five_verts: np.ndarray  # [num5,5] uint8
    edge_to_six: list[np.ndarray]  # len=m, each int32 ids
    edge_to_five: list[np.ndarray]


def build_instance(n: int) -> Instance:
    m = n * (n - 1) // 2
    pu, pv = all_pairs(n)

    num6 = math.comb(n, 6)
    six_verts = np.empty((num6, 6), dtype=np.uint8)
    edge_to_six_lists: list[list[int]] = [[] for _ in range(m)]
    sid = 0
    for S in itertools.combinations(range(n), 6):
        six_verts[sid, :] = S
        # 15 pairs
        for i in range(6):
            a = S[i]
            for j in range(i + 1, 6):
                b = S[j]
                edge_to_six_lists[pair_index(a, b, n)].append(sid)
        sid += 1

    num5 = math.comb(n, 5)
    five_verts = np.empty((num5, 5), dtype=np.uint8)
    edge_to_five_lists: list[list[int]] = [[] for _ in range(m)]
    qid = 0
    for Q in itertools.combinations(range(n), 5):
        five_verts[qid, :] = Q
        for i in range(5):
            a = Q[i]
            for j in range(i + 1, 5):
                b = Q[j]
                edge_to_five_lists[pair_index(a, b, n)].append(qid)
        qid += 1

    edge_to_six = [np.array(v, dtype=np.int32) for v in edge_to_six_lists]
    edge_to_five = [np.array(v, dtype=np.int32) for v in edge_to_five_lists]
    return Instance(
        n=n,
        pu=pu,
        pv=pv,
        six_verts=six_verts,
        five_verts=five_verts,
        edge_to_six=edge_to_six,
        edge_to_five=edge_to_five,
    )


def load_edges(path: Path) -> list[tuple[int, int]]:
    raw = json.loads(path.read_text(encoding="utf-8"))
    edges: list[tuple[int, int]] = []
    if not isinstance(raw, list):
        raise ValueError(f"Expected list in {path}")
    for row in raw:
        if not (isinstance(row, list) and len(row) == 2):
            raise ValueError(f"Bad edge row: {row!r}")
        u, v = int(row[0]), int(row[1])
        if u == v:
            raise ValueError(f"Self edge: {u}")
        if u > v:
            u, v = v, u
        edges.append((u, v))
    edges = sorted(set(edges))
    return edges


def write_edges(path: Path, edges: Iterable[tuple[int, int]]) -> None:
    rows = [[int(u), int(v)] for u, v in sorted(edges)]
    path.write_text(json.dumps(rows, indent=2), encoding="utf-8")


def edges_to_adj(n: int, edges: Iterable[tuple[int, int]]) -> list[int]:
    adj = [0] * n
    for u, v in edges:
        adj[u] |= 1 << v
        adj[v] |= 1 << u
    return adj


def induced_edge_count(adj: list[int], vs: Iterable[int]) -> int:
    mask = 0
    vlist = list(vs)
    for v in vlist:
        mask |= 1 << v
    c = 0
    for v in vlist:
        c += (adj[v] & mask).bit_count()
    return c // 2


def verify_graph(
    n: int,
    edges: list[tuple[int, int]],
    e_min: int = 60,
    e_max: int = 65,
    report_examples: int = 5,
) -> dict:
    m = len(edges)
    if not (e_min <= m <= e_max):
        raise ValueError(f"edge_count {m} not in [{e_min},{e_max}]")
    for (u, v) in edges:
        if not (0 <= u < n and 0 <= v < n):
            raise ValueError(f"vertex out of range: {(u, v)}")
        if u >= v:
            raise ValueError(f"edge not ordered: {(u, v)}")
    if len(edges) != len(set(edges)):
        raise ValueError("duplicate edges")

    adj = edges_to_adj(n, edges)

    # K5 check (omega <= 4).
    k5 = 0
    k5_examples: list[tuple[int, ...]] = []
    for Q in itertools.combinations(range(n), 5):
        ok = True
        for a, b in itertools.combinations(Q, 2):
            if (adj[a] >> b) & 1 == 0:
                ok = False
                break
        if ok:
            k5 += 1
            if len(k5_examples) < report_examples:
                k5_examples.append(Q)

    bad0 = 0
    bad12 = 0
    min6 = 99
    max6 = -1
    bad0_examples: list[tuple[int, ...]] = []
    bad12_examples: list[tuple[int, ...]] = []
    for S in itertools.combinations(range(n), 6):
        c = induced_edge_count(adj, S)
        min6 = min(min6, c)
        max6 = max(max6, c)
        if c == 0:
            bad0 += 1
            if len(bad0_examples) < report_examples:
                bad0_examples.append(S)
        elif c >= 12:
            bad12 += 1
            if len(bad12_examples) < report_examples:
                bad12_examples.append(S)

    return {
        "n": n,
        "edge_count": m,
        "k5": k5,
        "k5_examples": k5_examples,
        "six_min": min6,
        "six_max": max6,
        "bad6_zero": bad0,
        "bad6_dense": bad12,
        "bad6_zero_examples": bad0_examples,
        "bad6_dense_examples": bad12_examples,
        "ok": (k5 == 0 and bad0 == 0 and bad12 == 0),
    }


class GraphState:
    def __init__(
        self,
        inst: Instance,
        edges: list[tuple[int, int]],
        w0: int,
        w12: int,
        wk5: int,
    ) -> None:
        self.inst = inst
        self.w0 = int(w0)
        self.w12 = int(w12)
        self.wk5 = int(wk5)

        self.edge_present = np.zeros(inst.pu.shape[0], dtype=np.uint8)
        self.adj = [0] * inst.n

        # O(1) sampling of present/absent edges.
        self.present: list[int] = []
        self.absent: list[int] = list(range(inst.pu.shape[0]))
        self.pos_present = np.full(inst.pu.shape[0], -1, dtype=np.int32)
        self.pos_absent = np.arange(inst.pu.shape[0], dtype=np.int32)

        for (u, v) in edges:
            eid = pair_index(u, v, inst.n)
            self._add_edge_raw(eid)

        # Counts of edges in each 6/5 subset.
        self.six_counts = np.zeros(inst.six_verts.shape[0], dtype=np.int8)
        self.five_counts = np.zeros(inst.five_verts.shape[0], dtype=np.int8)
        for eid in self.present:
            self.six_counts[inst.edge_to_six[eid]] += 1
            self.five_counts[inst.edge_to_five[eid]] += 1

        self.bad0 = int(np.count_nonzero(self.six_counts == 0))
        self.bad12 = int(np.count_nonzero(self.six_counts >= 12))
        self.k5 = int(np.count_nonzero(self.five_counts == 10))

    def score(self) -> int:
        return self.bad0 * self.w0 + self.bad12 * self.w12 + self.k5 * self.wk5

    def edges(self) -> list[tuple[int, int]]:
        out: list[tuple[int, int]] = []
        for eid in self.present:
            u = int(self.inst.pu[eid])
            v = int(self.inst.pv[eid])
            out.append((u, v))
        return sorted(out)

    def _add_edge_raw(self, eid: int) -> None:
        if self.edge_present[eid]:
            return
        self.edge_present[eid] = 1
        u = int(self.inst.pu[eid])
        v = int(self.inst.pv[eid])
        self.adj[u] |= 1 << v
        self.adj[v] |= 1 << u

        # absent -> present
        a_pos = int(self.pos_absent[eid])
        if a_pos != -1:
            last = self.absent[-1]
            self.absent[a_pos] = last
            self.pos_absent[last] = a_pos
            self.absent.pop()
            self.pos_absent[eid] = -1
        p_pos = len(self.present)
        self.present.append(eid)
        self.pos_present[eid] = p_pos

    def _remove_edge_raw(self, eid: int) -> None:
        if not self.edge_present[eid]:
            return
        self.edge_present[eid] = 0
        u = int(self.inst.pu[eid])
        v = int(self.inst.pv[eid])
        self.adj[u] &= ~(1 << v)
        self.adj[v] &= ~(1 << u)

        # present -> absent
        p_pos = int(self.pos_present[eid])
        if p_pos != -1:
            last = self.present[-1]
            self.present[p_pos] = last
            self.pos_present[last] = p_pos
            self.present.pop()
            self.pos_present[eid] = -1
        a_pos = len(self.absent)
        self.absent.append(eid)
        self.pos_absent[eid] = a_pos

    def delta_if_flip(self, eid: int, delta: int) -> tuple[int, int, int, int]:
        """Return (d_bad0, d_bad12, d_k5, d_score) if this edge is flipped by delta."""
        ids6 = self.inst.edge_to_six[eid]
        before6 = self.six_counts[ids6]
        ids5 = self.inst.edge_to_five[eid]
        before5 = self.five_counts[ids5]

        if delta == 1:
            d_bad0 = -int(np.count_nonzero(before6 == 0))
            d_bad12 = int(np.count_nonzero(before6 == 11))
            d_k5 = int(np.count_nonzero(before5 == 9))
        else:
            d_bad0 = int(np.count_nonzero(before6 == 1))
            d_bad12 = -int(np.count_nonzero(before6 == 12))
            d_k5 = -int(np.count_nonzero(before5 == 10))
        d_score = d_bad0 * self.w0 + d_bad12 * self.w12 + d_k5 * self.wk5
        return d_bad0, d_bad12, d_k5, d_score

    def apply_flip(self, eid: int, delta: int) -> None:
        d_bad0, d_bad12, d_k5, _ = self.delta_if_flip(eid, delta)
        self.bad0 += d_bad0
        self.bad12 += d_bad12
        self.k5 += d_k5

        ids6 = self.inst.edge_to_six[eid]
        self.six_counts[ids6] += delta
        ids5 = self.inst.edge_to_five[eid]
        self.five_counts[ids5] += delta

        if delta == 1:
            self._add_edge_raw(eid)
        else:
            self._remove_edge_raw(eid)

    def edge_pairs_in_verts(self, verts: np.ndarray) -> list[int]:
        out: list[int] = []
        k = int(verts.shape[0])
        for i in range(k):
            a = int(verts[i])
            for j in range(i + 1, k):
                b = int(verts[j])
                out.append(pair_index(a, b, self.inst.n))
        return out


def choose_best(
    rng: np.random.Generator,
    candidates: list[int],
    key_fn,
    noise: float,
) -> int:
    if not candidates:
        raise ValueError("empty candidates")
    if rng.random() < noise:
        return int(rng.choice(candidates))
    best = candidates[0]
    best_key = key_fn(best)
    for c in candidates[1:]:
        k = key_fn(c)
        if k < best_key or (k == best_key and rng.random() < 0.5):
            best = c
            best_key = k
    return best


def search(
    inst: Instance,
    start_edges: list[tuple[int, int]],
    seed: int,
    steps: int,
    time_limit_s: float,
    noise: float,
    temp0: float,
    cool: float,
    w0: int,
    w12: int,
    wk5: int,
    remove_sample: int,
    add_sample: int,
    out_jsonl: Path,
    best_model_path: Path,
    best_summary_path: Path,
) -> dict:
    rng = np.random.default_rng(seed)
    state = GraphState(inst, start_edges, w0=w0, w12=w12, wk5=wk5)

    best = {
        "bad6_zero": state.bad0,
        "bad6_dense": state.bad12,
        "k5": state.k5,
        "score": state.score(),
        "step": 0,
        "seed": seed,
        "edge_count": len(state.present),
        "model_path": None,
    }

    out_jsonl.parent.mkdir(parents=True, exist_ok=True)
    with out_jsonl.open("a", encoding="utf-8") as f:
        f.write(
            json.dumps(
                {
                    "ts": utc_ts(),
                    "event": "start",
                    "seed": seed,
                    "steps": steps,
                    "time_limit_s": time_limit_s,
                    "noise": noise,
                    "temp0": temp0,
                    "cool": cool,
                    "w0": w0,
                    "w12": w12,
                    "wk5": wk5,
                    "remove_sample": remove_sample,
                    "add_sample": add_sample,
                    "start": {
                        "bad6_zero": state.bad0,
                        "bad6_dense": state.bad12,
                        "k5": state.k5,
                        "score": state.score(),
                        "edge_count": len(state.present),
                    },
                }
            )
            + "\n"
        )

        def log_best(note: str) -> None:
            best_model_path.parent.mkdir(parents=True, exist_ok=True)
            write_edges(best_model_path, state.edges())
            best.update(
                {
                    "bad6_zero": int(state.bad0),
                    "bad6_dense": int(state.bad12),
                    "k5": int(state.k5),
                    "score": int(state.score()),
                    "edge_count": int(len(state.present)),
                    "model_path": str(best_model_path),
                }
            )
            if state.bad0 == 0 and state.bad12 == 0 and state.k5 == 0:
                v = verify_graph(inst.n, state.edges())
                best["verified_ok"] = bool(v["ok"])
            row = {"ts": utc_ts(), "event": "best", "note": note, **best}
            f.write(json.dumps(row) + "\n")
            f.flush()
            best_summary_path.write_text(json.dumps(best, indent=2), encoding="utf-8")
            print(
                f"[best] step={best['step']} score={best['score']} bad0={best['bad6_zero']} "
                f"bad12={best['bad6_dense']} k5={best['k5']}",
                flush=True,
            )

        start_time = time.time()
        temp = float(temp0)
        refresh_every = 200
        bad0_ids = np.flatnonzero(state.six_counts == 0)
        bad12_ids = np.flatnonzero(state.six_counts >= 12)
        k5_ids = np.flatnonzero(state.five_counts == 10)

        print(
            f"start score={state.score()} bad0={state.bad0} bad12={state.bad12} k5={state.k5}",
            flush=True,
        )

        for step in range(1, steps + 1):
            if time_limit_s and (time.time() - start_time) >= time_limit_s:
                break
            if state.bad0 == 0 and state.bad12 == 0 and state.k5 == 0:
                best["step"] = step - 1
                log_best("solved")
                break

            if step % refresh_every == 0:
                bad0_ids = np.flatnonzero(state.six_counts == 0)
                bad12_ids = np.flatnonzero(state.six_counts >= 12)
                k5_ids = np.flatnonzero(state.five_counts == 10)

            old_score = state.score()
            old_bad0, old_bad12, old_k5 = state.bad0, state.bad12, state.k5

            # Decide which violation family to address.
            mode = "bad0" if state.bad0 > 0 else ("k5" if state.k5 > 0 else "bad12")

            add_eid = None
            rem_eid = None

            if mode == "bad0":
                # Add an edge inside an independent 6-set, then remove a low-impact present edge.
                sid = int(rng.choice(bad0_ids)) if bad0_ids.size else int(rng.integers(0, inst.six_verts.shape[0]))
                verts = inst.six_verts[sid]
                pair_eids = state.edge_pairs_in_verts(verts)
                add_candidates = [e for e in pair_eids if state.edge_present[e] == 0]
                if not add_candidates:
                    continue
                add_eid = choose_best(
                    rng,
                    add_candidates,
                    key_fn=lambda e: state.delta_if_flip(e, +1)[3],
                    noise=noise,
                )
                state.apply_flip(add_eid, +1)

                present_sample = (
                    rng.choice(state.present, size=min(remove_sample, len(state.present)), replace=False).tolist()
                    if state.present
                    else []
                )
                present_candidates = [e for e in present_sample if e != add_eid]
                if not present_candidates:
                    # revert and skip
                    state.apply_flip(add_eid, -1)
                    continue
                rem_eid = choose_best(
                    rng,
                    present_candidates,
                    key_fn=lambda e: state.delta_if_flip(e, -1)[3],
                    noise=noise,
                )
                state.apply_flip(rem_eid, -1)
            elif mode == "k5":
                # Break a K5 by removing an internal edge, then add a low-risk absent edge.
                qid = int(rng.choice(k5_ids)) if k5_ids.size else int(rng.integers(0, inst.five_verts.shape[0]))
                verts5 = inst.five_verts[qid]
                pair_eids = state.edge_pairs_in_verts(verts5)
                rem_candidates = [e for e in pair_eids if state.edge_present[e] == 1]
                if not rem_candidates:
                    continue
                rem_eid = choose_best(
                    rng,
                    rem_candidates,
                    key_fn=lambda e: state.delta_if_flip(e, -1)[3],
                    noise=noise,
                )
                state.apply_flip(rem_eid, -1)

                # If this created any bad0, preferentially fix by adding inside a bad0 6-set.
                if state.bad0 > 0:
                    bad0_ids_now = np.flatnonzero(state.six_counts == 0)
                    sid = int(rng.choice(bad0_ids_now))
                    verts = inst.six_verts[sid]
                    pair_eids = state.edge_pairs_in_verts(verts)
                    add_candidates = [e for e in pair_eids if state.edge_present[e] == 0]
                    if not add_candidates:
                        state.apply_flip(rem_eid, +1)
                        continue
                    add_eid = choose_best(
                        rng,
                        add_candidates,
                        key_fn=lambda e: state.delta_if_flip(e, +1)[3],
                        noise=noise,
                    )
                else:
                    absent_sample = rng.choice(
                        state.absent, size=min(add_sample, len(state.absent)), replace=False
                    ).tolist()
                    add_candidates = absent_sample
                    add_eid = choose_best(
                        rng,
                        add_candidates,
                        key_fn=lambda e: state.delta_if_flip(e, +1)[3],
                        noise=noise,
                    )
                state.apply_flip(add_eid, +1)
            else:
                # Reduce a dense 6-set by removing an internal present edge, then add a low-risk absent edge.
                sid = (
                    int(rng.choice(bad12_ids))
                    if bad12_ids.size
                    else int(rng.integers(0, inst.six_verts.shape[0]))
                )
                verts6 = inst.six_verts[sid]
                pair_eids = state.edge_pairs_in_verts(verts6)
                rem_candidates = [e for e in pair_eids if state.edge_present[e] == 1]
                if not rem_candidates:
                    continue
                rem_eid = choose_best(
                    rng,
                    rem_candidates,
                    key_fn=lambda e: state.delta_if_flip(e, -1)[3],
                    noise=noise,
                )
                state.apply_flip(rem_eid, -1)

                if state.bad0 > 0:
                    bad0_ids_now = np.flatnonzero(state.six_counts == 0)
                    sid2 = int(rng.choice(bad0_ids_now))
                    verts = inst.six_verts[sid2]
                    pair_eids2 = state.edge_pairs_in_verts(verts)
                    add_candidates = [e for e in pair_eids2 if state.edge_present[e] == 0]
                    if not add_candidates:
                        state.apply_flip(rem_eid, +1)
                        continue
                    add_eid = choose_best(
                        rng,
                        add_candidates,
                        key_fn=lambda e: state.delta_if_flip(e, +1)[3],
                        noise=noise,
                    )
                else:
                    absent_sample = rng.choice(
                        state.absent, size=min(add_sample, len(state.absent)), replace=False
                    ).tolist()
                    add_candidates = absent_sample
                    add_eid = choose_best(
                        rng,
                        add_candidates,
                        key_fn=lambda e: state.delta_if_flip(e, +1)[3],
                        noise=noise,
                    )
                state.apply_flip(add_eid, +1)

            new_score = state.score()
            delta = new_score - old_score
            accept = delta <= 0 or (temp > 1e-9 and rng.random() < math.exp(-delta / temp))
            if not accept:
                # revert both flips
                if add_eid is not None:
                    state.apply_flip(add_eid, -1)
                if rem_eid is not None:
                    state.apply_flip(rem_eid, +1)
                state.bad0, state.bad12, state.k5 = old_bad0, old_bad12, old_k5
                # Note: counts and edges already restored by apply_flip; counters restored above.
                new_score = old_score

            temp *= cool

            # Track best (lex on (bad0,bad12,k5,score)).
            cur = (state.bad0, state.k5, state.bad12, state.score())
            best_t = (best["bad6_zero"], best["k5"], best["bad6_dense"], best["score"])
            if cur < best_t:
                best["step"] = step
                log_best("improved")

            if step % 2000 == 0:
                row = {
                    "ts": utc_ts(),
                    "event": "progress",
                    "step": step,
                    "bad6_zero": int(state.bad0),
                    "bad6_dense": int(state.bad12),
                    "k5": int(state.k5),
                    "score": int(state.score()),
                    "temp": float(temp),
                    "edge_count": int(len(state.present)),
                }
                f.write(json.dumps(row) + "\n")
                f.flush()
                print(
                    f"step={step} score={state.score()} bad0={state.bad0} bad12={state.bad12} k5={state.k5}",
                    flush=True,
                )

        # Final write
        best_summary_path.write_text(json.dumps(best, indent=2), encoding="utf-8")
        f.write(json.dumps({"ts": utc_ts(), "event": "done", **best}) + "\n")
        f.flush()

    return best


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, default=26)
    parser.add_argument("--e-min", type=int, default=60)
    parser.add_argument("--e-max", type=int, default=65)
    parser.add_argument("--start-model", type=Path, default=Path("erdos/617/results/ramsey_26_6_max65_model_summary.model.json"))
    parser.add_argument("--verify", type=Path, default=None)
    parser.add_argument("--seed", type=int, default=617)
    parser.add_argument("--steps", type=int, default=200000)
    parser.add_argument("--time-limit-s", type=float, default=120.0)
    parser.add_argument("--noise", type=float, default=0.05)
    parser.add_argument("--temp0", type=float, default=50.0)
    parser.add_argument("--cool", type=float, default=0.9995)
    parser.add_argument("--w0", type=int, default=1000)
    parser.add_argument("--w12", type=int, default=10)
    parser.add_argument("--wk5", type=int, default=200)
    parser.add_argument("--remove-sample", type=int, default=25)
    parser.add_argument("--add-sample", type=int, default=200)
    parser.add_argument("--out-jsonl", type=Path, default=Path("erdos/617/results/phase1_c_local_search_log.jsonl"))
    parser.add_argument("--best-model", type=Path, default=Path("erdos/617/results/phase1_c_best_model.json"))
    parser.add_argument("--best-summary", type=Path, default=Path("erdos/617/results/phase1_c_best_summary.json"))
    args = parser.parse_args()

    if args.verify is not None:
        edges = load_edges(args.verify)
        stats = verify_graph(args.n, edges, e_min=args.e_min, e_max=args.e_max)
        print(json.dumps(stats, indent=2))
        return 0 if stats["ok"] else 1

    start_edges = load_edges(args.start_model)
    inst = build_instance(args.n)
    best = search(
        inst,
        start_edges=start_edges,
        seed=args.seed,
        steps=args.steps,
        time_limit_s=args.time_limit_s,
        noise=args.noise,
        temp0=args.temp0,
        cool=args.cool,
        w0=args.w0,
        w12=args.w12,
        wk5=args.wk5,
        remove_sample=args.remove_sample,
        add_sample=args.add_sample,
        out_jsonl=args.out_jsonl,
        best_model_path=args.best_model,
        best_summary_path=args.best_summary,
    )
    print(json.dumps(best, indent=2))
    return 0 if best.get("verified_ok") else 1


if __name__ == "__main__":
    raise SystemExit(main())
