# A residual-cover reduction for Problem 689

I have been looking at Erdos Problem 689 from the following conservative
angle.  I do not have a proof.  The point of this post is to record a
residual-demand calculation and a reduction which seem to isolate the missing
covering lemma.

Problem 689 asks whether, for every sufficiently large \(n\), one can choose
one residue class
\[
  a_p \pmod p \qquad (p\le n,\ p\text{ prime})
\]
so that every \(1\le m\le n\) lies in at least two of the chosen classes.

## 1. Zero residues and residual demand

Fix \(y\le n\), and first choose
\[
  a_p\equiv 0\pmod p \qquad (p\le y).
\]
Write
\[
  \omega_y(m)=\#\{p\le y:p\mid m\},
  \qquad
  d_y(m)=\max(0,2-\omega_y(m)).
\]
Thus the primes \(p>y\) are only asked to supply \(d_y(m)\) further hits at
each \(m\).

Let
\[
  D_y(n)=\sum_{m\le n}d_y(m),
\]
and let
\[
  \Phi(x,y)=\#\{r\le x:\text{ every prime divisor of }r\text{ is }>y\},
\]
with \(1\) included.  Then there is an exact decomposition
\[
  D_y(n)
  =
  2\Phi(n,y)
  +
  \sum_{\substack{p\le y\\ a\ge 1\\ p^a\le n}}
    \Phi(n/p^a,y).
  \tag{1}
\]
Indeed, the first term counts the two residual tokens on integers with no
prime divisor \(\le y\).  If an integer has exactly one distinct small prime
divisor, it is uniquely of the form \(p^a r\), where \(p\le y\), \(a\ge1\),
and \(r\) is \(y\)-rough, and it contributes one residual token.  Integers
with at least two distinct small prime divisors contribute no residual demand.

## 2. The range \(y=n/z\)

The range I find most useful is
\[
  y=\frac nz,\qquad 2\le z\le \sqrt n.
\]
Then \(y\ge\sqrt n\), so every \(y\)-rough integer \(\le n\) is either \(1\)
or a prime \(>y\).  In this range (1) gives the more explicit formula
\[
  D_{n/z}(n)
  =
  2(1+\pi(n)-\pi(n/z))
  +
  \operatorname{PP}(n,n/z)
  +
  \sum_{\substack{p^a\le z\\ a\ge 1}}
    \left(\pi(n/p^a)-\pi(n/z)\right),
  \tag{2}
\]
where
\[
  \operatorname{PP}(n,y)=\#\{p^a\le n:p\le y,\ a\ge1\}.
\]
The main term comes from the \(a=1\) part,
\[
  \sum_{p\le z}\left(\pi(n/p)-\pi(n/z)\right).
\]
Using the prime number theorem and Mertens' theorem, one obtains, for
\(z=z(n)\to\infty\) and \(2\le z\le\sqrt n\),
\[
  D_{n/z}(n)
  \sim
  \frac{n\log\log z}{\log n}.
  \tag{3}
\]
In particular, at \(y=\sqrt n\),
\[
  D_{\sqrt n}(n)\sim \frac{n\log\log n}{\log n}.
  \tag{4}
\]
This is only a count of residual demand; it is not a covering result.

## 3. Token-cover formulation

For each \(m\le n\), introduce residual demand tokens
\[
  T_m=\{(m,j):1\le j\le d_y(m)\},
  \qquad
  V_y=\bigcup_{m\le n}T_m.
\]
For a prime \(p>y\) and residue \(a\pmod p\), the corresponding token shadow is
\[
  \widetilde E(p,a)
  =
  \bigcup_{\substack{m\le n\\ d_y(m)>0\\ m\equiv a\pmod p}}T_m.
\]
There is a small bookkeeping point here.  If \(d_y(m)=2\), one selected
congruence class hitting \(m\) can supply only one hit to \(m\), not both
tokens.  Thus a residual cover should be slot-respecting: after choosing one
residue \(a_p\pmod p\) for each prime in some set \(R\subseteq(y,n]\), each
token \((m,j)\) must be assigned to a selected prime \(p\in R\) with
\[
  m\equiv a_p\pmod p,
\]
and the two tokens of the same \(m\), if present, must be assigned to distinct
primes.

This formulation gives a direct reduction:

**Residual-cover reduction.**  If, after the zero-residue stage at \(y\), the
primes \(p>y\) admit a slot-respecting cover of all residual tokens, then
Problem 689 holds for this \(n\).

The proof is just addition of the hits: the small primes provide
\(\omega_y(m)\) hits, the token cover provides \(d_y(m)\) distinct further
large-prime hits, and
\[
  \omega_y(m)+d_y(m)\ge2.
\]

## 4. What happens at \(y=\sqrt n\)

At the square-root stage the residual set has a simple shape:

- \(1\) has demand \(2\);
- primes \(q>\sqrt n\) have demand \(2\);
- small primes and prime powers have demand \(1\);
- integers \(s^e q\le n\), with \(s\le\sqrt n<q\) prime and \(e\ge1\), have
  demand \(1\).

Some pieces are easy in isolation.  Sparse sets such as \(1\), small primes,
and prime powers can be cleaned individually using distinct primes in
\((n/2,n]\), provided there are fewer tokens than available cleanup primes.
Also, if a large prime \(q>\sqrt n\) keeps the zero residue \(a_q=0\), then it
automatically supplies the remaining hit to every residual target of the form
\(s^e q\).

The tension is that changing \(a_q\) away from \(0\) may help give prime
targets their second hit, but it also destroys the automatic cover of the
whole \(s^e q\)-fiber.  Simple Hall matching, uniform random residues, and a
greedy argument based only on average residue-class sizes do not seem to
resolve this.  For example, uniform random residues on
\((\sqrt n,n]\) give only \((\log 2+o(1))\) expected incidences per large
prime target, below even one full extra cover on average.

## 5. The missing covering lemma

Here is the covering statement I would like to understand.

Let \(y=n/z\), with \(z\to\infty\), and let \(R\) be a reservoir of primes just
above \(y\), say
\[
  R=\{p:y<p\le Ay\}
\]
with \(1<A\le z\).  For the residual token set \(V_y\), can one choose one
residue class modulo each \(p\in R\) so as to cover almost all residual tokens
in a slot-respecting way, leaving only a set small enough to clean one token at
a time with later primes?

Equivalently, is there a Maynard/FGKMT-style random covering or nibble lemma
for the token hypergraph
\[
  \{\widetilde E(p,a):p\in R,\ a\pmod p\},
\]
where the vertices are the residual demand tokens above?  A sufficient version
would produce residue distributions for the reservoir primes with:

- enough one-point degree for most residual tokens;
- small two-point codegrees for distinct tokens;
- controlled edge sizes, roughly at the scale expected for residue classes
  modulo \(p\asymp y\);
- an exceptional set smaller than the number of available cleanup primes.

The exact residual-demand calculation above suggests the amount of work left
after the zero stage is about
\[
  \frac{n\log\log z}{\log n}
\]
when \(y=n/z\) and \(2\le z\le\sqrt n\).  What I do not currently have is the
distributional covering input needed to turn that demand bound into a
slot-respecting cover.

So the question is: is there a known semi-random covering theorem, or a known
variant of the large-prime-gap covering lemmas, that naturally applies to this
mixed residual target set of primes, prime powers, and \(s^e q\)-type
integers?  Or is there a more elementary way to prove the square-root residual
covering lemma directly?
