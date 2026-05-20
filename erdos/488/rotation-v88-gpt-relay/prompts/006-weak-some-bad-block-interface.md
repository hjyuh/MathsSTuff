EP488 BBDS interface, narrowed target.

Previous prompt asking for current-height BadBlock(h) stalled. Do not try to
localize to the current height unless it falls out for free.

Definitions:
- TopWindow(C,q): q/2 < r < q for every r in C.
- D_C(x;q) counts t<=x with q not divide t and some r in C divides t.
- Block(q,j)=((j-1)q,jq].
- BlockCov(j)=covered points in Block(q,j).
- Slot(r,j)=q-free multiples of r in Block(q,j).
- SlotMass(j)=sum_r |Slot(r,j)|.
- BadBlock(j): 2*BlockCov(j) < SlotMass(j).
- RunEndExtremal: n uncovered, n+1 covered, m covered, m+1 uncovered,
  m>n, and D_C(m;q)/m > 2D_C(n;q)/n.

Known facts:
- slot_card_le_two: every top-window Slot(r,j) has size <= 2.
- dfun_eq_sum_blockCov at block boundaries.
- Bad-block descent is false; do not use it.
- Strong current-height lemma may be overlocalized.
- It is enough for the global reduction to prove:

  If TopWindow(C,q), RunEndExtremal(C,q,n,m), and 3q <= n,
  then exists j >= 3 with BadBlock(C,q,j).

Task:
Prove or disprove this weaker interface:

  no BadBlock(j) for every j>=3
  => D_C(m;q)/m <= 2D_C(n;q)/n

under the RunEndExtremal hypotheses.

Allowed outputs:
A. Rigorous proof with exact inequalities.
B. Concrete counterexample with exact q,C,n,m,D(n),D(m), bad blocks.
C. Exact missing inequality, stated formally, with why the proof stops.

Keep the answer short and mathematical. Do not re-explain EP488 background.

