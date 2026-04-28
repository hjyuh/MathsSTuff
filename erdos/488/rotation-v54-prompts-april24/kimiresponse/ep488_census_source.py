# EP-488 v53 Computational Census
# Source code for independent rerun

import math
from math import gcd
from collections import defaultdict, deque
from itertools import combinations

def lcm_pair(a, b):
    return a * b // gcd(a, b)

def build_lcm_graph(q, n):
    V = list(range(q // 2 + 1, q + 1))
    adj = {v: set() for v in V}
    edges = []
    for i, a in enumerate(V):
        for b in V[i+1:]:
            l = lcm_pair(a, b)
            if l <= n and l % q != 0:
                adj[a].add(b)
                adj[b].add(a)
                edges.append((a, b))
    return V, adj, edges

def find_components(adj, vertices):
    visited = set()
    components = []
    for v in vertices:
        if v not in visited:
            comp = []
            queue = deque([v])
            visited.add(v)
            while queue:
                u = queue.popleft()
                comp.append(u)
                for w in adj[u]:
                    if w not in visited:
                        visited.add(w)
                        queue.append(w)
            components.append(sorted(comp))
    return components

def component_edges(C, adj):
    Cset = set(C)
    edges = []
    for a in C:
        for b in adj[a]:
            if b in Cset and a < b:
                edges.append((a, b))
    return edges

def compute_c_n(a, n, q):
    return n // a - n // lcm_pair(a, q)

def compute_D_C_fast(C, n, q):
    if len(C) <= 10:
        total = 0
        for k in range(1, len(C) + 1):
            for subset in combinations(C, k):
                l = subset[0]
                for a in subset[1:]:
                    l = lcm_pair(l, a)
                mults = n // l - n // lcm_pair(l, q)
                if k % 2 == 1:
                    total += mults
                else:
                    total -= mults
        return total
    else:
        count = 0
        for t in range(1, n + 1):
            if t % q == 0:
                continue
            for a in C:
                if t % a == 0:
                    count += 1
                    break
        return count

def compute_tau(C, n, q):
    Cset = set(C)
    tau = 0
    max_d = n // 60
    for d in range(1, max_d + 1):
        a, b, c = 12*d, 15*d, 20*d
        if a in Cset and b in Cset and c in Cset:
            l = 60 * d
            if l % q == 0:
                continue
            S_l = [v for v in C if l % v == 0]
            if set(S_l) == {a, b, c}:
                tau += 1
    return tau

def strip_triples(C, n, q):
    Cset = set(C)
    removed = set()
    max_d = n // 60
    for d in range(1, max_d + 1):
        a, b, c = 12*d, 15*d, 20*d
        if a in Cset and b in Cset and c in Cset:
            l = 60 * d
            if l % q == 0:
                continue
            S_l = [v for v in C if l % v == 0]
            if set(S_l) == {a, b, c}:
                removed.add(c)
    return sorted([v for v in C if v not in removed]), sorted(removed)

def compute_degrees(C, adj):
    Cset = set(C)
    return {v: len([w for w in adj[v] if w in Cset]) for v in C}

def run_census(q_max=500):
    all_results = []
    for q in range(10, q_max + 1):
        n_start = (5 * q + 1) // 2
        n_end = 3 * q
        if q <= 100:
            n_values = list(range(n_start, n_end))
        else:
            n_values = list(range(n_start, n_end, max(1, (n_end - n_start) // 20)))
            if n_end - 1 not in n_values:
                n_values.append(n_end - 1)

        for n in n_values:
            V, adj, _ = build_lcm_graph(q, n)
            components = find_components(adj, V)
            for C in components:
                if len(C) >= 3:
                    edges = component_edges(C, adj)
                    c = len(edges) - len(C) + 1
                    tau = compute_tau(C, n, q)
                    epsilon = c - tau

                    C_stripped, removed = strip_triples(C, n, q)
                    if len(C_stripped) > 0:
                        Cset_s = set(C_stripped)
                        edges_stripped = [(a, b) for a, b in edges if a in Cset_s and b in Cset_s]
                        is_pseudo = len(edges_stripped) <= len(C_stripped)
                    else:
                        is_pseudo = True

                    degs = compute_degrees(C, adj)
                    x1 = sum(1 for v in C if degs[v] == 1)
                    x3 = sum(1 for v in C if degs[v] == 3)

                    D_C_n = compute_D_C_fast(C, n, q)
                    sum_c = sum(compute_c_n(a, n, q) - 1 for a in C)

                    all_results.append({
                        'q': q, 'n': n, 'C': C,
                        'c': c, 'tau': tau, 'epsilon': epsilon,
                        'x1': x1, 'x3': x3,
                        'D_C_n': D_C_n, 'sum_c_minus_1': sum_c,
                        'A2_target': D_C_n >= sum_c,
                        'is_pseudoforest': is_pseudo,
                    })
    return all_results

if __name__ == '__main__':
    results = run_census(500)
    obstructions = [r for r in results if r['epsilon'] > 1]
    print(f"Total: {len(results)}, Obstructions: {len(obstructions)}")
