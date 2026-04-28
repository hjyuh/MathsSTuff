# Border-surface mod-p smoke summary

Date: 2026-04-26.

Script:

```text
scripts/border_surface_modp.py
```

Prime range:

```text
7 <= p <= 101
```

For each Bremner seed, the script counted nontrivial modular solutions to the
simultaneous border equations

\[
X^2+N_i\in\square,\qquad M+x_j^2\in\square,\qquad M+X^2\in\square.
\]

Here "nontrivial" means \(X\not\equiv0\), \(M\not\equiv0\), the new column
square is not congruent to an old column square, and the new row is not
congruent to an old row, all modulo \(p\).

## Results

```text
3Q+T     primes_with_nontrivial= 7/23 total_nontrivial=  40 best=p79:10
4Q       primes_with_nontrivial= 7/23 total_nontrivial=  34 best=p73:16
5Q+T     primes_with_nontrivial=11/23 total_nontrivial=1096 best=p83:760
6Q       primes_with_nontrivial=11/23 total_nontrivial= 798 best=p97:494
7Q+T     primes_with_nontrivial=10/23 total_nontrivial= 134 best=p37:58
8Q+T     primes_with_nontrivial=14/23 total_nontrivial=1000 best=p53:312
```

## Interpretation

This does not prove rational points.  It does say the simultaneous border
surface has plenty of nontrivial local points for the tested seeds and small
primes.  That is materially better than the one-sided fifth-column scan, which
kept returning exactly four common deltas.

The next computational step is to add smoothness/Jacobian-rank filtering and
then attempt \(p\)-adic lifting from high-yield primes such as:

```text
5Q+T at p=83
6Q at p=97
8Q+T at p=53
```
