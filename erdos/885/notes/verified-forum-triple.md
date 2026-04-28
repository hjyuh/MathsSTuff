# Verified forum triple intersection

Created: 2026-04-26

The EP885 forum post claims

\[
D(79200)\cap D(227205)\cap D(1258560)=\{36,468,692,1028\}.
\]

Thomas Bloom's reply appears to quote \(1029\), but direct verification gives
\(1028\), not \(1029\).

## Verification

For \(D(n)=\{|a-b|:ab=n\}\), direct divisor enumeration gives

\[
D(79200)\cap D(227205)\cap D(1258560)
=\{36,468,692,1028\}.
\]

The factor pairs are:

\[
\begin{array}{c|cccc}
n & d=36 & d=468 & d=692 & d=1028\\
\hline
79200 & 264\cdot 300 & 132\cdot 600 & 100\cdot 792 & 72\cdot 1100\\
227205 & 459\cdot 495 & 297\cdot 765 & 243\cdot 935 & 187\cdot 1215\\
1258560 & 1104\cdot 1140 & 912\cdot 1380 & 828\cdot 1520 & 720\cdot 1748
\end{array}
\]

The check used:

```python
import math

def D(n):
    out=set()
    for a in range(1, math.isqrt(n)+1):
        if n % a == 0:
            out.add(n//a-a)
    return out

nums=[79200,227205,1258560]
print(sorted(set.intersection(*(D(n) for n in nums))))
```

Output:

```text
[36, 468, 692, 1028]
```

This gives a known-good \(K_{4,3}\) object in the incidence graph: four
differences shared by three numbers.
