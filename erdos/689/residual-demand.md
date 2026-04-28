# Residual demand after the zero-residue stage

Let
\[
  \omega_y(m)=\#\{p\le y:p\mid m\},
  \qquad
  d_y(m)=\max(0,2-\omega_y(m)),
\]
and
\[
  D_y(n)=\sum_{m\le n} d_y(m).
\]
Thus \(d_y(m)=2\) if \(m\) has no prime divisor \(\le y\), \(d_y(m)=1\) if it has exactly one distinct prime divisor \(\le y\), and \(d_y(m)=0\) otherwise.

Write
\[
  \Phi(x,y)=\#\{r\le x: p\mid r \Rightarrow p>y\}
\]
for the count of \(y\)-rough integers up to \(x\), with \(1\) included.

## Exact decomposition

The basic identity is
\[
  D_y(n)
  =
  2\Phi(n,y)
  +
  \sum_{\substack{p\le y\\ a\ge 1\\ p^a\le n}}
    \Phi(n/p^a,y).
  \tag{1}
\]

Proof: the first term counts the two tokens attached to integers with no small prime divisor. If \(m\) has exactly one distinct small prime divisor, say \(p\le y\), write \(m=p^a r\), where \(a\ge 1\) and \(r\) has no prime divisor \(\le y\). This representation is unique, and contributes one token. Integers with at least two distinct small prime divisors contribute no tokens.

This identity is often the cleanest starting point because it separates the problem into a rough-number term and a one-small-prime term.

## A general upper bound

For all \(3\le y\le n\),
\[
  D_y(n)
  \ll
  \frac{n\log\log y}{\log y}
  +
  \frac{y}{\log y}
  +
  \frac{\sqrt n}{\log n}
  \tag{2}
\]
with an absolute implied constant.

In particular, unless \(y\) is very close to \(n\), the useful summary is
\[
  D_y(n)\ll \frac{n\log\log y}{\log y}.
\]

Proof: use the standard upper-bound sieve estimate
\[
  \Phi(x,y)\ll \frac{x}{\log y}\qquad (x\ge y\ge 3),
\]
and the trivial estimate \(\Phi(x,y)=1\) for \(x<y\). Applying these to (1),
\[
  D_y(n)
  \ll
  \frac{n}{\log y}
  +
  \frac{n}{\log y}
    \sum_{\substack{p\le y\\ a\ge 1\\ p^a\le n}} \frac1{p^a}
  +
  \#\{p^a\le n:p\le y,\ a\ge 1\}.
\]
Mertens' estimate gives
\[
  \sum_{p\le y}\sum_{a\ge 1}\frac1{p^a}
  =
  \sum_{p\le y}\frac1{p-1}
  =
  \log\log y+O(1).
\]
Also
\[
  \#\{p^a\le n:p\le y,\ a\ge 1\}
  \le \pi(y)+O(\pi(\sqrt n)+n^{1/3})
  \ll \frac{y}{\log y}+\frac{\sqrt n}{\log n}.
\]
This proves (2).

This bound is deliberately crude but robust. It uses only the linear sieve/Brun upper bound for rough numbers, Mertens' theorem, and the prime number theorem in the weak form \(\pi(x)\ll x/\log x\).

## The range \(y=n/z\) with \(2\le z\le \sqrt n\)

This is the most useful range for the staged covering plan because \(y\ge \sqrt n\). In this range every \(y\)-rough integer \(\le n\) is either \(1\) or a prime \(>y\). Hence
\[
  \Phi(n,y)=1+\pi(n)-\pi(y).
\]

Similarly, if \(m=p^a r\) has exactly one small prime divisor \(p\le y\), then the rough factor \(r\) is either \(1\) or a prime \(q>y\). The prime case occurs only when
\[
  p^a q\le n,\qquad q>y,
\]
equivalently \(p^a\le n/y=z\). Therefore
\[
  D_{n/z}(n)
  =
  2(1+\pi(n)-\pi(n/z))
  +
  \operatorname{PP}(n,n/z)
  +
  \sum_{\substack{p^a\le z\\ a\ge 1}}
    \left(\pi(n/p^a)-\pi(n/z)\right),
  \tag{3}
\]
where
\[
  \operatorname{PP}(n,y)=\#\{p^a\le n:p\le y,\ a\ge 1\}
\]
counts the pure prime powers carrying one residual token.

The \(a=1\) part of the last sum is the main term:
\[
  S_1(n,z)=\sum_{p\le z}\left(\pi(n/p)-\pi(n/z)\right).
\]
The higher-power part is smaller:
\[
  \sum_{\substack{p^a\le z\\ a\ge 2}}
    \pi(n/p^a)
  \ll
  \frac{n}{\log n}
  \sum_{a\ge 2}\sum_p\frac1{p^a}
  \ll
  \frac{n}{\log n}.
  \tag{4}
\]
Also
\[
  2(\pi(n)-\pi(n/z))+\operatorname{PP}(n,n/z)
  \ll
  \frac{n}{\log n}+\frac{n/z}{\log(n/z)}+\frac{\sqrt n}{\log n}.
  \tag{5}
\]

Combining (3)--(5), for \(2\le z\le \sqrt n\),
\[
  D_{n/z}(n)
  \ll
  \frac{n(1+\log\log(3z))}{\log n}.
  \tag{6}
\]

This improves the general bound in this range: the relevant logarithm is \(\log\log z\), not \(\log\log y\), because a residual one-small-prime integer with a large prime cofactor must have its small-prime power \(p^a\le z=n/y\).

## Asymptotic for \(y=n/z\), \(z\to\infty\), \(z\le\sqrt n\)

If \(z=z(n)\to\infty\) and \(2\le z\le\sqrt n\), then
\[
  D_{n/z}(n)
  \sim
  \frac{n\log\log z}{\log n}.
  \tag{7}
\]

Proof sketch: by the prime number theorem, uniformly for \(p\le z\le\sqrt n\),
\[
  \pi(n/p)=\frac{n/p}{\log(n/p)}(1+o(1)).
\]
Thus
\[
  \sum_{p\le z}\pi(n/p)
  =
  n(1+o(1))\sum_{p\le z}\frac1{p\log(n/p)}.
\]
By partial summation and Mertens' theorem,
\[
  \sum_{p\le z}\frac1{p\log(n/p)}
  =
  \frac{\log\log z+O(1)}{\log n},
  \qquad 2\le z\le\sqrt n.
\]
The subtraction term satisfies
\[
  \pi(n/z)\pi(z)
  \ll
  \frac{n}{\log(n/z)\log z}
  =
  o\!\left(\frac{n\log\log z}{\log n}\right),
\]
since \(z\to\infty\). The higher prime powers, pure prime powers, and no-small-prime tokens are all
\[
  O(n/\log n)+O((n/z)/\log(n/z))+O(\sqrt n/\log n),
\]
which is \(o(n\log\log z/\log n)\). Therefore (7) follows from (3).

## Special case \(y=\sqrt n\)

Taking \(z=\sqrt n\) in (3) gives the exact formula
\[
  D_{\sqrt n}(n)
  =
  2(1+\pi(n)-\pi(\sqrt n))
  +
  \operatorname{PP}(n,\sqrt n)
  +
  \sum_{\substack{p^a\le \sqrt n\\ a\ge 1}}
    \left(\pi(n/p^a)-\pi(\sqrt n)\right).
  \tag{8}
\]
Consequently,
\[
  D_{\sqrt n}(n)
  \sim
  \frac{n\log\log n}{\log n}.
  \tag{9}
\]

The main contribution is from integers \(pq\le n\) with \(p\le\sqrt n<q\); these are exactly the residual one-token semiprimes with one small prime factor and one large prime factor. The two-token integers \(1\) and primes \(>\sqrt n\) contribute only \(O(n/\log n)\), and prime powers contribute only \(O(\sqrt n/\log n)\) to the count of pure prime-power tokens, plus \(O(n/\log n)\) through higher powers in the semiprime sum.

## Covering relevance and caveats

For later covering work, the bound to use is
\[
  D_{n/z}(n)
  \ll
  \frac{n(1+\log\log(3z))}{\log n}
  \qquad (2\le z\le\sqrt n).
\]
In particular,
\[
  D_{\sqrt n}(n)\asymp \frac{n\log\log n}{\log n}.
\]

These estimates control only total residual demand. They do not by themselves imply that the remaining primes can cover the residual tokens. The obstruction is distributional: a residue class modulo \(p\asymp n/z\) hits about \(z\) integers in \([1,n]\), and only a fraction of those are residual targets. A later covering lemma must use the arithmetic structure of the target set, not merely the total mass \(D_y(n)\).

For \(y<\sqrt n\), formula (1) remains exact and the general sieve bound (2) remains valid, but the sharper elementary classification used in (3) fails because a \(y\)-rough cofactor can have two or more prime factors. In that range one should either keep (1) with Buchstab estimates for \(\Phi(x,y)\), or use the robust upper bound (2) if an upper bound is sufficient.

Standard estimates invoked here are the prime number theorem, Mertens' theorem for \(\sum_{p\le x}1/p\), and the elementary upper-bound sieve estimate \(\Phi(x,y)\ll x/\log y\).
