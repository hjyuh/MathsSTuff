We audited your previous finite-skeleton theorem for EP488 A2-Induced core
completeness.

Your algebraic identity was correct:

For a connected epsilon-2 core H, with

  d_v = degree(v),
  c_v = number of connected components of H-v,
  t_v = number of triple triangles containing v,
  kappa = sum_v (c_v - 1),
  sigma_v = d_v - c_v - t_v - 1,

we have

  tau + kappa + sum_v sigma_v = 2.

But the claimed sigma_v >= 0 is false for the current v81 notion of
deletion-minimality.

Reason:
v81 deletion-minimality means connected-deletion-minimal:
for every vertex v, either C\{v} is disconnected, or the connected induced
subgraph C\{v} has epsilon <= 1.

It does NOT require total epsilon(H-v) <= 1 when H-v is disconnected.

Local audit:
- old q<=10000 v81 cores: 158.
- new q=10001..15000 sample cores: 31.
- identity failures: 0.
- cores with negative sigma_v: 49.
- nonordinary-bound failures: 32.
- max nonordinary vertices observed: 10.

Also, the q<=10000 list of 29 normalized minimal-core shapes is not global:
a q=10001..15000 frontier sample found 7 additional certified normalized
minimal-core shapes, all epsilon=2.

Example new certified core:
q=10936, n=32400,
C={5760,5832,6000,6075,6144,6400,6480,6750,6912,7680,
   7776,8000,8100,8640,9000,9216,9600,9720,10125,10368}
cyclomatic=2, tau=0, epsilon=2, D_C(n;q)=59,
best/B=16200/32401, delta/B=1806775/3871344.

Another new certified core:
q=10936, n=32400,
C={5760,5832,6000,6075,6144,6400,6480,6750,6912,7200,
   7680,7776,8000,8100,9000,9216,9600,9720,10125,10368,10800}
cyclomatic=4, tau=2, epsilon=2, D_C(n;q)=62,
best/B=16200/32401, delta/B=1872343/4068192.

Task:
Repair the theorem for the actual connected-deletion-minimal setting.

Allowed outputs:

A. A rigorous block-tree skeleton theorem controlling negative sigma at
   articulation/triple vertices and proving a finite or bounded certifiable
   family.
B. A concrete infinite family of connected-deletion-minimal epsilon-2 cores
   with unbounded chain length/diameter, realized by top-window lcm cutoffs.
C. A weaker theorem that strictly advances A2-Induced and covers the new
   q=10936 examples.
D. A precise missing lemma and exact failure point.

Required:
- Do not use total-deletion-minimality unless you explicitly prove how to
  reduce connected-minimal cores to that case.
- Work with the actual top-window lcm-threshold model, not only the pure
  unweighted four-ratio graph.
- Explain how negative sigma vertices are controlled or why they are an
  obstruction.
- Do not discuss A4 or claim EP488 is solved.
- Avoid dead routes: broad triple-stripping, unconditional pseudoforest A2',
  v52 run-count equality, Hunter bridge, undefined x_1/x_3.
