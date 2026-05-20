# EP1005 fixed rational fan lemma

Date: 2026-05-11

This note generalizes the `1/2` fan count. It does not solve EP1005 by
itself, but it proves that any bad interval containing a fixed rational
`r/s != 1/2` has a linear lower bound strictly larger than `n/4`.

## Setup

Let

```tex
\alpha=\frac ab<\frac rs<\frac cd=\beta
```

where `(r,s)=1`, `0<r<s`, and `s>=3`. Assume the endpoint pair is bad:

```tex
u=c-a\ge1,\qquad v=b-d\ge1.
```

Define the offsets from `r/s` by

```tex
A=br-as>0,\qquad C=cs-dr>0.
```

Then

```tex
A+C=su+rv.
```

In particular

```tex
A+C\ge s+r\ge s+1.
```

## Fan count around `r/s`

For every `h>=1`, the fractions below `r/s` with determinant `h` are the
solutions of

```tex
rq-sp=h.
```

They lie in `(a/b,r/s)` exactly when

```tex
Aq>bh.
```

For fixed `h`, the solutions form one arithmetic progression modulo `s`.
Among them, the primitive ones have natural density `phi(h)/h`, because any
common divisor of `p` and `q` must divide `h`.

Similarly, the fractions above `r/s` with determinant `h` are the solutions
of

```tex
sp-rq=h,
```

and they lie in `(r/s,c/d)` exactly when

```tex
Cq>dh.
```

Consequently, for fixed `A,C,r,s`,

```tex
B_n(a/b,c/d)\ge
\frac ns
\left(
\sum_{1\le h<A}\frac{\phi(h)}{h}\left(1-\frac hA\right)
+
\sum_{1\le h<C}\frac{\phi(h)}{h}\left(1-\frac hC\right)
\right)
-O_{A,C,r,s}(1).
```

Define

```tex
G(m)=\sum_{h=1}^{m-1}\frac{\phi(h)}{h}\left(1-\frac hm\right).
```

The lower bound is

```tex
B_n(a/b,c/d)\ge \frac n s (G(A)+G(C))-O_{A,C,r,s}(1).
```

## Consequence for fixed cells

Since `G` is increasing and `A+C>=s+r`, the worst case is when one offset is
`1`. Thus

```tex
G(A)+G(C)\ge G(s+r-1)\ge G(s).
```

For `s>=3`,

```tex
\frac{G(s)}{s}>\frac14.
```

The first values are:

```text
s=3: 5/18
s=4: 7/24
s=5: 22/75
s=6: 3/10
```

and the values tend to `3/pi^2`.

Therefore every fixed rational cell `r/s` with `s>=3` has a constant
`eta_{r,s}>0` such that

```tex
B_n(a/b,c/d)\ge \left(\frac14+\eta_{r,s}\right)n-O_{r,s,A,C}(1)
```

for endpoint offsets `A,C` fixed.

For the first off-center cell `1/3`, this can be made completely elementary.
If `A,C>=2`, the determinant-one fans alone give at least `n/3-O(1)`.
If one offset is `1`, then the other is at least `3`, and determinant-one plus
determinant-two fans on the larger side give

```tex
B_n(a/b,c/d)\ge \frac{5n}{18}-O(1).
```

Since `5/18>1/4`, no fixed-offset `1/3` cell can be extremal for all large
`n`.

## Remaining gap

This note handles fixed rational cells and fixed offsets. The full EP1005
conjecture still needs a uniform argument when the least-denominator rational
inside the bad interval has denominator growing with `n`, or when the offsets
`A,C` grow with `n` in a way that makes the `O_{A,C,r,s}(1)` term too large.

