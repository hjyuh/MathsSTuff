# EP1005 unit-step reduction and obstruction

Date: 2026-05-11

This note records a near-global reduction that almost proves EP1005 but has
one important obstruction.

## Every bad interval contains a real unit-step subinterval

Let

```tex
\alpha=\frac ab<\frac cd=\beta
```

be a bad ordered pair, so

```tex
u=c-a\ge1,\qquad v=b-d\ge1.
```

Define the real unit-step point

```tex
\gamma=\frac{a+1}{b-1}.
```

Then

```tex
\alpha<\gamma\le\beta.
```

The first inequality is immediate:

```tex
a(b-1)<b(a+1).
```

For the second, compute

```tex
c(b-1)-d(a+1)
=bc-ad-c-d
=b(u-1)+a(v-1)+v-u.
```

This is nonnegative for all `u,v>=1`; it is zero only in the diagonal
case `u=v=1`.

Thus every bad interval contains

```tex
\frac ab<\frac{a+1}{b-1}.
```

## Why this does not immediately solve the problem

If `(a+1,b-1)=1`, then the unit-step point is a Farey fraction and the
subinterval is a genuine diagonal bad interval. A full lower bound for all
diagonal bad intervals would then imply the desired lower bound for the
original bad pair.

If `(a+1,b-1)>1`, however, the unit-step point reduces:

```tex
\frac{a+1}{b-1}=\frac{a'}{b'}.
```

The reduced numerator `a'` can be much smaller than `a`, so

```tex
\frac ab<\frac{a'}{b'}
```

is not a bad pair. This subinterval can have fewer than the conjectural number
of Farey fractions.

Example:

```tex
n=95,\qquad
\frac{47}{95}<\frac{48}{94}=\frac{24}{47}.
```

The unit-step subinterval has only `25` interior Farey fractions, below the
conjectural value `27`. But any actual bad right endpoint with numerator
larger than `47` is much farther away; the best extension is

```tex
\frac{47}{95}<\frac{49}{94},
```

which has `58` interior Farey fractions.

## Remaining lemma suggested by this reduction

The full conjecture would follow from the following two statements:

1. Every diagonal bad interval

   ```tex
   \frac aq<\frac{a+1}{q-1}
   ```

   has at least the van Doorn conjectural number of interior Farey fractions
   for `n>=92`.

2. If the real unit-step point reduces, i.e.

   ```tex
   g=(a+1,b-1)>1,
   ```

   then every bad endpoint

   ```tex
   \frac cd\ge\frac{a+1}{b-1},\qquad c>a,\ d<b,
   ```

   gives an interval

   ```tex
   \frac ab<\frac cd
   ```

   with strictly more than the conjectural number of interior Farey fractions,
   for `n>=92`.

The second statement is the exact place where the simple unit-step reduction
currently fails. It should be attacked by counting the additional interval
from the reduced unit-step point to the first possible bad endpoint.

## Offset structure when the unit-step point reduces

Let

```tex
g=(a+1,b-1)>1,\qquad
\frac{a+1}{b-1}=\frac xy
```

with `(x,y)=1`. Then

```tex
a=gx-1,\qquad b=gy+1.
```

The lower offset of `a/b` from `x/y` is large and explicit:

```tex
by-ax=(gy+1)x-(gx-1)y=x+y.
```

Now let `c/d` be any reduced bad endpoint above `x/y`, so

```tex
c>a=gx-1,\qquad d<b=gy+1,\qquad \frac cd>\frac xy.
```

Since `c>=gx` and `d<=gy`, its upper offset from `x/y` is

```tex
cy-dx=(c-gx)y+(gy-d)x.
```

This is a positive integer, and therefore

```tex
cy-dx\ge \min(x,y).
```

Thus the reduced unit-step obstruction is not arbitrary. It produces an
interval around `x/y` with offsets at least

```tex
A=x+y,\qquad C\ge \min(x,y).
```

The fan-count function

```tex
G(m)=\sum_{h=1}^{m-1}\frac{\phi(h)}{h}\left(1-\frac hm\right)
```

appears naturally here. Computation strongly suggests, and standard totient
sum estimates imply for large `m`, that

```tex
G(m)\ge \frac m4.
```

If this inequality is combined with a uniform fan-count lower bound whose
error is controlled when `A` and `C` grow with `y`, then the reduced unit-step
case would be eliminated:

```tex
\frac n y \left(G(x+y)+G(\min(x,y))\right)
\ge \frac n4 + \text{surplus}.
```

The difficulty is not the main term. The difficulty is proving a sharp enough
error term in the primitive fan count uniformly when the offset parameters are
of size comparable to `y`.
