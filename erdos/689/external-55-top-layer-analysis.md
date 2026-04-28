# Analysis of 5.5 top-layer argument

Created: 2026-04-25

This note records the useful split found by the external 5.5 run:

1. the literal top-layer theorem with arbitrary high-prime residues is true;
2. the genuinely directed version, where every residue is represented by a
   switched prime, remains much harder;
3. the tempting extension from top layer to all parity residuals runs into an
   asymptotic cancellation.

## 1. The arbitrary-residue top-layer theorem checks out

Let
\[
  H_{\rm top}(n)=\{h(q)=2^kq:n/2<h(q)\le n,\ q\le n/2\text{ odd prime}\}.
\]
Then
\[
  |H_{\rm top}(n)|=\pi(n/2)-1\sim \frac{n}{2\log n}.
\]

Switch \(3\) and \(5\) to nonzero residues \(c_3,c_5\). Choose \(c_3\) to cover
at least half of the nonzero classes of \(H_{\rm top}\) modulo \(3\), then
choose \(c_5\) to cover at least a quarter of what remains modulo \(5\). The
uncovered top-layer set has size at most
\[
  \left(\frac38+o(1)\right)\frac{n}{2\log n}.
\]

The high primes \(P\in(n/2,n]\) satisfying
\[
  P\equiv c_3\pmod 3
  \quad\text{or}\quad
  P\equiv c_5\pmod 5
\]
occupy \(5\) of the \(8\) reduced residue classes modulo \(15\), so by the
prime number theorem in arithmetic progressions their count is
\[
  \left(\frac58+o(1)\right)\frac{n}{2\log n}.
\]

Thus there are enough repairable high primes to assign one high prime to every
top target left uncovered by \(3,5\), plus \(O(1)\) extra high primes to repair
the switched small primes and handle \(h(3),h(5)\). The high primes are
repairable because each lies in one of the two selected small residue classes.

This proves the literal top-layer theorem with arbitrary residues.

## 2. Why this is not the directed theorem

The proof uses high primes \(P_t>n/2\) with residues
\[
  b_{P_t}\equiv t\pmod {P_t}
\]
for arbitrary top targets \(t\in H_{\rm top}\). Usually \(t\bmod P_t\) is not
a switched prime. So this is not a proof in the directed/permutation model
where each residue must be of the form \(r(p)\in R\).

If \(P>n/2\) is forced to hit \(t\in(n/2,n]\) through a directed residue
represented by a switched prime \(r\), then
\[
  t\equiv r\pmod P
\]
implies \(r=t-P\), since \(t\) is even and \(r=t\) is impossible. Thus the
directed high-prime mop-up requires Goldbach-type representations
\[
  t=P+r,\qquad P>n/2,\quad r\le n/2\text{ prime}.
\]
That is the harder packing problem studied in `directed-switching-packing.md`
and `goldbach-prime-inputs.md`.

## 3. Tempting full-solution extension and the cancellation

The top-layer proof suggests a tempting full parity-first strategy:

1. switch a fixed small set \(S\) of odd primes to nonzero residues \(c_s\);
2. use high primes \(P>n/2\), chosen from the union of the repair classes
   \(P\equiv c_s\pmod s\), to mop up all residual demand one token at a time.

This does not immediately prove Problem 689. The reason is that switching the
small primes creates new demand on their multiples, and the asymptotic gain
from the small sieve cancels against this new debt.

Let \(S\) be any fixed finite set of odd primes, and write
\[
  \alpha_s=1-\frac1{s-1}.
\]
The high repair reservoir has asymptotic density
\[
  1-\prod_{s\in S}\alpha_s
\]
inside the primes in \((n/2,n]\). Hence it has size
\[
  \left(\frac{1-\prod_{s\in S}\alpha_s}{2}+o(1)\right)\frac n{\log n}.
\]

Now count the main residual demand after switching \(S\). The main terms are
even numbers
\[
  m=2^k d q\le n,
\]
where \(d\) is \(S\)-smooth and \(q\) is a prime outside \(S\). Such an \(m\)
has exactly one remaining zero-prime hit, from \(q\), so it needs a selected
small residue unless one of the congruences \(m\equiv c_s\pmod s\) holds.

For fixed \(d\), the avoidance density among \(q\) is
\[
  \prod_{\substack{s\in S\\s\nmid d}}\alpha_s.
\]
The main-term coefficient for residual demand is therefore
\[
  \sum_{\substack{d\ge1\\d\;S\text{-smooth}}}
    \frac1d
    \prod_{\substack{s\in S\\s\nmid d}}\alpha_s.
\]
This Euler product factors as
\[
  \prod_{s\in S}
  \left(\alpha_s+\sum_{e\ge1}\frac1{s^e}\right)
  =
  \prod_{s\in S}
  \left(\frac{s-2}{s-1}+\frac1{s-1}\right)
  =
  1.
\]

So a fixed small-prime sieve leaves
\[
  (1+o(1))\frac n{\log n}
\]
main residual tokens once the debt on \(S\)-smooth multiples is included.
But even the entire high-prime interval \((n/2,n]\) contains only
\[
  \left(\frac12+o(1)\right)\frac n{\log n}
\]
primes. Thus a one-high-prime-per-token mop-up cannot handle the full residual
set.

This cancellation is why the arbitrary-residue top-layer proof is real but
does not directly solve #689.

## 4. Updated interpretation

The top-layer result is still important:

- it proves the literal top-layer theorem without directed residues;
- it shows that our directed model is an intentionally stronger sufficient
  framework, not a necessity for #689;
- it suggests that high-prime arbitrary residues are powerful for sparse layers.

But a full solution still needs a mechanism where many residue classes cover
multiple residual targets, especially below the top layer. A pure high-prime
singleton cleanup has too little capacity once the full parity residual set is
counted correctly.
