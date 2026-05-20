# EP1005 progress addendum

Date: 2026-05-12

This addendum records corrections and new proof-search artifacts from the
latest pass.  The full conjecture remains open.

## Unit-step `H>=2` buffered drift

The local constant-floor target was corrected.  In the signature

```tex
\alpha_t=\cdots=\alpha_{t+4}=m,\qquad
\beta_t=\cdots=\beta_{t+3}=m+2,\qquad \beta_{t+4}=m+3,
```

with

```tex
p=K+t,\qquad r=A+m,
```

the four-band target is

```tex
D(p+r+7)-D(p+r+2)
=
\begin{cases}
3,&p+r\equiv0\pmod4,\\
-1,&p+r\equiv1\pmod4,\\
2,&p+r\equiv2\pmod4,\\
1,&p+r\equiv3\pmod4.
\end{cases}
```

So `p+r==1 mod 4` is automatically harmless; the observed negative blocks
all have target `3` and `p+r==0 mod 4`.

A new checker summarizes negative floor signatures:

```text
python scripts\unit_step_hge2_negative_floor_summary.py 9000 --target3-mod --t-max 240 --alpha-window 180 --max-pure-records 120 --max-negative-records 400
```

Output summary:

```text
pure_records=65
negative_records=260
target_counts: 3 -> 260
residue_counts: 0 -> 260
```

The dominant signature remains length `(3,3,3,3)` with minimum pre-block
buffer `1579`, but negative blocks also occur with near-constant signatures
such as `(3,3,3,4)` and `(3,3,4,3)`.  Therefore the proof target is not
"negative implies constant length three"; it is a finite near-constant
floor-signature theorem plus a buffer lemma for every negative CRT template.

Files updated:

```text
scripts/unit_step_hge2_negative_floor_summary.py
notes/unit-step-Hge2-buffered-drift-draft.md
```

## Diagonal non-reciprocal `c>=2`

The exact-tail quotient transform was made executable in

```text
scripts/diagonal_nonreciprocal_tail_quotient_check.py
```

It verifies equality between the divisor tail

```tex
\sum_{d>T}N_u(d)N_j(d)
```

and the quotient sum obtained from `a+u=de`, `j=dy`, with the forced ratio
window

```tex
{a\over r}< {e\over y}< {a+1\over c}.
```

Verification:

```text
python scripts\diagonal_nonreciprocal_tail_quotient_check.py 300 --s-max 40 --cutoff 1
checked=442226
mismatches=0

python scripts\diagonal_nonreciprocal_tail_quotient_check.py 300 --s-max 80 --h-min 1 --h-max 1 --cutoff 10
checked=510867
mismatches=0

python scripts\diagonal_nonreciprocal_tail_quotient_check.py 220 --s-max 80 --h-min 2 --cutoff 1
checked=167346
mismatches=0

python scripts\diagonal_nonreciprocal_tail_quotient_check.py 500 --s-max 20 --h-min 2 --cutoff 1
checked=304290
mismatches=0
```

The existing exact-tail Mobius gate remains certified in the checked
`h>=2` box:

```text
python scripts\diagonal_nonreciprocal_band_check.py 500 --s-max 40 --h-min 2 --mobius-cutoff 1 --exact-tail
checked=594090
bad=0
mobius_bad=0
mobius_best=(3, 104, 4, 23, 12, 1, 44, 41)
```

Files updated:

```text
scripts/diagonal_nonreciprocal_tail_quotient_check.py
notes/diagonal-nonreciprocal-cge2-exact-tail-draft.md
```

## Diagonal non-reciprocal `c=1`

The first large-slack gate was rerun through `h<=500`:

```text
python scripts\diagonal_nonreciprocal_c1_first_gap.py 500 --max-a-extra 800
h_checked=500
bad=398
nonpositive_step=0
last_bad=(44, 47, Fraction(-83805514698775, 10593329013498))
```

This strengthens confidence that the existing large-`h` estimate and exact
finite box are aligned.  The later shifted-block increment still has the
same real gap: the exact rational checker covers `h<=300`, `k<=100`, but a
larger `h<=500`, `k<=150` run timed out and should not be used as evidence.
The branch still needs an all-`h`, all-`k` analytic increment bound or an
optimized finite-reduction checker.

An optimized exact checker was added after that timeout:

```text
scripts/diagonal_nonreciprocal_c1_increment_fast.py
```

It avoids evaluating the dual `p`-wise bound unless the `j`-wise bound is
negative, and reports whether each `(h,k)` row is closed for all larger `A`
by four-step drift.

New exact slices:

```text
python scripts\diagonal_nonreciprocal_c1_increment_fast.py 300 --k-max 100 --max-a-extra 1000 --max-records 5
bad=0
closed_pairs=30000
unclosed_pairs=0

python scripts\diagonal_nonreciprocal_c1_increment_fast.py 400 --h-min 301 --k-max 100 --max-a-extra 500
bad=0
closed_pairs=10000
unclosed_pairs=0

python scripts\diagonal_nonreciprocal_c1_increment_fast.py 300 --k-min 101 --k-max 160 --max-a-extra 500 --max-records 5
bad=0
closed_pairs=18000
unclosed_pairs=0
```

The wider diagnostics also close:

```text
python scripts\diagonal_nonreciprocal_c1_increment_fast.py 800 --h-min 401 --k-max 100 --max-a-extra 300
bad=0
closed_pairs=40000
unclosed_pairs=0

python scripts\diagonal_nonreciprocal_c1_increment_fast.py 300 --k-min 161 --k-max 260 --max-a-extra 300 --max-records 5
bad=0
closed_pairs=30000
unclosed_pairs=0
p_pair_ranges
100: h=8 A=12 k_min=161 k_max=260
99: h=9 A=13 k_min=162 k_max=260
```

Thus the exact finite-reduction evidence now reaches `h<=800,k<=100` and
`h<=300,k<=260`, with all larger `A` closed in those slices.  This is still
not an all-parameter proof, but it sharply identifies the dual-bound
families that the large-`k`, small-`h` argument must handle.
