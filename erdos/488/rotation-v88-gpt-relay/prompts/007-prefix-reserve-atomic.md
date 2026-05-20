EP488 BBDS interface follow-up.

Your PrefixReserve route is promising, but PrefixReserve is false if it is
derived only from local/full-block nonbadness up to the prefix.

Counterexample to the naive/local prefix step:

  q = 31
  C = {16,18,20,24,27,30}
  n = 95

This is primitive and top-window. Also n>=3q, n is uncovered, and n+1=96 is
covered.

Exact values:

  D_C(95;31) = 17
  M(95) = 23
  |C| = 6

Thus

  M(95)+2|C| = 35 > 34 = 2D_C(95;31).

Early complete blocks are nonbad:

  block 1: cov=6, mass=6, slack=6
  block 2: cov=6, mass=9, slack=3
  block 3: cov=5, mass=8, slack=2
  block 4: cov=5, mass=9, slack=1
  block 5: cov=6, mass=8, slack=4
  block 6: cov=5, mass=9, slack=1

But this C has later bad blocks. Its block period is 2160, and the first bad
block is:

  j=16, BlockCov=3, SlotMass=7.

So the repaired target is:

PrefixReserveAtomic:

  TopWindow(C,q),
  n>=3q,
  n uncovered,
  n+1 covered,
  forall j>=3, not BadBlock(C,q,j)
  =>
  M(n)+2|C| <= 2D_C(n;q).

Equivalently, prove the contrapositive:

  If TopWindow(C,q), n>=3q, n uncovered, n+1 covered, and
  M(n)+2|C| > 2D_C(n;q),
  then exists j>=3 with BadBlock(C,q,j).

Task:
Prove PrefixReserveAtomic, or give a concrete counterexample with exact q,C,n
and proof that no BadBlock(j) occurs for all j>=3.

Important:
- Do not use bad-block descent.
- Do not use direct q-shift transport t -> t-q.
- You may use the row growth inequality F_r(m) <= (m/n)(F_r(n)+2), but the
  main missing work is PrefixReserveAtomic.
- Keep the output focused: proof, counterexample, or exact failure point.

