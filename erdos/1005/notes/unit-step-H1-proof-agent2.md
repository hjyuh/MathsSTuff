# EP1005 H=1 unit-step edge proof

Date: 2026-05-11

This note proves the primitive lattice inequality left open in
`notes/unit-step-edge-H1-reduction.md`.

Let

```tex
X=g-1,\qquad Y=B,\qquad (X,Y+1)=1,\qquad n=(X+1)Y+1.
```

Put

```tex
S(X,Y)=
\#\{(p,h):1\le p\le X,\ 1\le h\le Y,\ (p,h)=1,\
(Y+1)p>Xh\}.
```

The edge count is `E=2+S(X,Y)`.  We prove, for `n>=92`,

```tex
E>M(n)=\left\lfloor {n\over4}\right\rfloor+d_{n\bmod 4},
\qquad (d_0,d_1,d_2,d_3)=(1,2,2,4).
```

Equivalently, since all quantities are integral, it is enough to prove

```tex
S(X,Y)\ge M(n)-1.
```

## Residue discrepancy lemma

For an integer `m>=1`, a real interval `I`, and `|I|` its length,

```tex
\#\{z\in I\cap\mathbb Z:(z,m)=1\}
\ge {\varphi(m)\over m}|I|-\tau(m).
```

Indeed,

```tex
1_{(z,m)=1}=\sum_{d\mid (z,m)}\mu(d).
```

The number of multiples of each `d|m` in `I` differs from `|I|/d` by at
most `1`, so the total error is at most `\sum_{d|m}1=\tau(m)`.

Write

```tex
\Phi(t)=\sum_{m\le t}\varphi(m),\qquad
T(t)=\sum_{m\le t}\tau(m),
```

and

```tex
G(t)=\sum_{m=1}^t {\varphi(m)\over m}\left(1-{m\over t+1}\right).
```

Applying the discrepancy lemma by vertical columns gives

```tex
S(X,Y)\ge {Y+1\over X}\Phi(X)-T(X).       \tag{1}
```

For fixed `p`, the admissible `h` are exactly the integers in
`0<h<(Y+1)p/X`.

Applying the same lemma by horizontal rows gives

```tex
S(X,Y)\ge XG(Y)-T(Y).                    \tag{2}
```

For fixed `h`, the admissible `p` lie in
`Xh/(Y+1)<p\le X`.

## Weak explicit arithmetic estimates

We use only the following weak estimates:

```tex
T(t)\le t(1+\log t),                                      \tag{3}
```

and, for all `t>=1`,

```tex
{\Phi(t)\over t}-{t+1\over4}\ge {t\over50},\qquad
G(t)-{t\over4}\ge {t\over50}.                              \tag{4}
```

Here (3) follows from

```tex
T(t)=\sum_{d\le t}\left\lfloor {t\over d}\right\rfloor
\le t\sum_{d\le t}{1\over d}\le t(1+\log t).
```

For (4), it is enough to use the standard explicit summatory-totient
bound

```tex
\Phi(t)\ge {3\over\pi^2}t^2-t\log t-t,
```

for `t>=1000`, and direct exact verification for `t<1000`.  This gives
`\Phi(t)\ge 0.29t^2` for every `t>=1`.

The first inequality in (4) follows immediately for `t>=13`, and the
remaining `t<13` are checked directly.

For the second inequality, summation by parts gives

```tex
G(t)=
{\Phi(t)\over t(t+1)}
+\sum_{m=1}^{t-1}{\Phi(m)\over m(m+1)}.
```

Thus

```tex
G(t)\ge 0.29\sum_{m=1}^{t-1}{m\over m+1}
=0.29(t-H_t),
```

where `H_t` is the `t`-th harmonic number.  Since
`H_t<=1+\log t`, this is at least `0.27t` for `t>=200`; the remaining
`t<200` are checked directly.

## Reduction to a finite rectangle

Since `d_r<=4`,

```tex
M(n)-1\le {n\over4}+3
={XY+Y\over4}+{13\over4}.                  \tag{5}
```

Let

```tex
A_X={\Phi(X)\over X}-{X+1\over4},
\qquad
B_Y=G(Y)-{Y\over4}.
```

By (4), `A_X>=X/50` and `B_Y>=Y/50`.

From (1), (3), and (5), the desired inequality follows whenever

```tex
Y A_X\ge T(X)+{13\over4}.
```

In particular, it follows whenever

```tex
Y\ge 50(1+\log X)+163.                    \tag{6}
```

From (2), (3), and (5), the desired inequality follows whenever

```tex
X B_Y\ge T(Y)+{Y\over4}+{13\over4}.
```

In particular, it follows whenever

```tex
X\ge 50\log Y+225.                        \tag{7}
```

Therefore any possible exception must satisfy both

```tex
Y<50(1+\log X)+163,\qquad X<50\log Y+225.
```

Substituting the first inequality into the second gives

```tex
X<50\log(50(1+\log X)+163)+225.
```

The right side minus `X` is decreasing for `X>=539`, and at `X=539` it is
negative.  Hence every possible exception has

```tex
X\le 538,\qquad Y\le 527.
```

## Exact finite check

The remaining rectangle is checked exactly by the defining formula.

```python
from math import gcd

D = [1, 2, 2, 4]

def M(n):
    return n // 4 + D[n % 4]

XMAX = 580
YMAX = 570

pref = [[0] * (YMAX + 1) for _ in range(XMAX + 1)]
for p in range(1, XMAX + 1):
    s = 0
    for h in range(1, YMAX + 1):
        if gcd(p, h) == 1:
            s += 1
        pref[p][h] = s

def S(X, Y):
    return sum(
        pref[p][min(Y, ((Y + 1) * p - 1) // X)]
        for p in range(1, X + 1)
    )

mins = []
minsur = 10**9
bad = []
checked = 0

for X in range(1, XMAX + 1):
    for Y in range(1, YMAX + 1):
        if gcd(X, Y + 1) != 1:
            continue
        n = (X + 1) * Y + 1
        if n < 92:
            continue
        checked += 1
        E = 2 + S(X, Y)
        sur = E - M(n)
        if sur < minsur:
            minsur = sur
            mins = [(X, Y, n, E, M(n), sur)]
        elif sur == minsur:
            mins.append((X, Y, n, E, M(n), sur))
        if sur <= 0:
            bad.append((X, Y, n, E, M(n), sur))

print("checked", checked)
print("minsur", minsur)
print("mins", mins)
print("bad", len(bad))
```

Output:

```text
checked 200940
minsur 3
mins [(6, 18, 127, 38, 35, 3), (10, 10, 111, 34, 31, 3)]
bad 0
```

Thus `E-M(n)>=3` throughout the finite rectangle.  Together with the
analytic reduction above, this proves the `H=1` non-reduced unit-step edge
inequality for all `n>=92`.
