EP488 A2-Induced focused barrier. Do not discuss A4 except where explicitly
needed as a dependency. Do not claim EP488 is solved.

Current verified progress:

1. v86 pointwise extension theorem:
   If a reduced top-window core S is pointwise EP-safe, every admissible
   top-window extension S union {a} remains pointwise EP-safe.

2. v87 minimal-core theorem:
   Every connected induced deletion-minimal high-defect core has epsilon=2.

3. v88 audit:
   The old claim "29 normalized minimal-core shapes" is not global.
   In q=10001..15000 smooth representatives, 99 additional certified
   deletion-minimal epsilon-2 cores were found, with 11 new normalized shapes.

4. v88 block decomposition audit:
   For 158 old q<=10000 cores plus 99 q=10001..15000 sample cores,
   every connected-minimal epsilon-2 core decomposes into biconnected blocks
   with positive block-epsilon partition exactly one of:

     [2]      : 177 cores
     [1, 1]   : 80 cores

   No audited core has positive block partition [1,1,1], [2,1], [3], etc.

Definitions:

For a connected induced core H=B_n(C,q):
- beta(G)=|E(G)|-|V(G)|+comp(G), total cyclomatic number.
- tau(G)=number of top-window triple fibers contained in G.
- epsilon(G)=beta(G)-tau(G).
- A biconnected edge block B has block-epsilon epsilon(B)=beta(B)-tau(B),
  where tau(B) counts triple fibers whose three vertices lie in B.
- Connected-deletion-minimal means epsilon(H)=2 and for every vertex v,
  if H-v is connected, then epsilon(H-v)<=1. It does NOT require
  total epsilon(H-v)<=1 when H-v is disconnected.

Known algebra:
For connected epsilon=2 core H, with

  d_v = degree(v),
  c_v = number of connected components of H-v,
  t_v = number of triple triangles containing v,
  kappa = sum_v (c_v-1),
  sigma_v = d_v-c_v-t_v-1,

we have

  tau + kappa + sum_v sigma_v = 2.

But sigma_v can be negative at articulation/triple vertices under connected
minimality. That invalidates the previous finite-skeleton proof.

Task:
Prove or disprove the Block Partition Theorem:

Every connected-deletion-minimal reduced top-window epsilon=2 core has
positive biconnected block-epsilon partition either [2] or [1,1].

Equivalently:
- no positive block has epsilon>=3;
- no core contains one epsilon=2 block plus another positive block;
- no core contains three or more positive epsilon=1 blocks.

Allowed outputs:
A. Rigorous proof of the Block Partition Theorem.
B. Concrete counterexample q,n,C with exact block list, block epsilons,
   tau, beta, epsilon=2, and connected-minimality verified.
C. Weaker theorem that strictly advances A2-Induced and covers all audited
   examples, including the q=10936 new cores.
D. Precise missing lemma and exact failure point.

Required:
- Work in the actual top-window lcm-threshold model, not just the pure
  unweighted four-ratio graph.
- Treat articulation vertices and negative sigma correctly.
- State every hypothesis.
- Avoid dead routes: broad triple-stripping, unconditional A2' pseudoforest,
  v52 run-count equality, Hunter density bridge, undefined x_1/x_3.
