# Phase 1 Agent E Degree-Sequence Probe

Degree-only necessary constraints used for the no-K5 minimum-colour branch on `K_26`:

1. `alpha(G) <= 5` from the lower 6-set bound (`every 6-set has >= 1 edge`).
2. `omega(G) <= 4` by hypothesis.
3. For a vertex `v` with degree `d`, writing `N(v)` and `M(v)` for neighbors/nonneighbors:
   - `e(M(v)) >= min_edges_alpha_le_4(|M(v)|)`.
   - `e(N(v)) <= ex(|N(v)|, K4)`.
   - `e(N(v)) <= floor(6 * C(d,5) / C(d-2,3))` from every 5-subset of `N(v)` inducing at most 6 edges.
   - Mixed `a`-neighbor / `(5-a)`-nonneighbor upper-6 inequalities for `a = 1..5`.
4. Caro-Wei on `G`: `sum 1/(d_i+1) <= 5`.
5. Caro-Wei on the complement: `sum 1/(26-d_i) <= 4`.
6. Erdos-Gallai graphicality, plus a weak neighbor-degree-sum interval consistency check.

Probe cap per k: 100 sample sequences.

| k | local allowed degrees | sample sequences found | hit cap | search seconds | first sample |
| - | - | - | - | - | - |
| 60 | [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25] | 100 | True | 0.074 | `[5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]` |
| 61 | [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25] | 100 | True | 0.077 | `[5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4]` |
| 62 | [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25] | 100 | True | 0.069 | `[5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4]` |
| 63 | [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25] | 100 | True | 0.076 | `[5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4]` |
| 64 | [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25] | 100 | True | 0.067 | `[5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4]` |
| 65 | [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25] | 100 | True | 0.086 | `[5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]` |

## Conclusion

- Pruned k-values: [].
- Surviving k-values: [60, 61, 62, 63, 64, 65].
- Degree-only constraints do not prune any k in `60..65`.
- Exact degree-sequence branching is easy to generate but not selective: the probe hit the sample cap quickly for every k.
