# EP-488 Route 2 - Step 2 (open): prove |Q|>=3 is below adjacent pair
## April 12, 2026

### Goal (Route 2 step 2)

Let `Q` be a primitive modulus antichain with `|Q|>=3` and `max(Q)=q`.
Define survivors

`A_Q(x) := #{ 1 <= n <= x : for all d in Q, d does NOT divide n }`

and the two-point operator

`O_Q(n,m) := 2*A_Q(n)/n - A_Q(m)/m`  for `m>n>=q`.

Prove

`max_{m>n>=q} O_Q(n,m) <= O_{ {q-1,q} }^max`

where the RHS is the proved adjacent-pair maximum:

`O_{ {q-1,q} }^max = 1 - (4q-5)/((2q-3)(q-1)^2)` at `(n,m)=(2q-3,(q-1)^2)`.

This would finish EP-488 for all `|Q|>=3` (singleton and pair cases are already proved).

Reference: `route2-adjacent-pair-global-max.md`.

---

### Current best structural candidate (empirical)

Across all "top-window" scans (and the earlier exhaustive `q<=25` scan), the worst `|Q|>=3` set
with fixed `max(Q)=q` is always the consecutive triple

`Q3(q) = {q-2,q-1,q}`.

The maximizing pair returned on large windows is

`(n,m) = (2q-5, (q-2)^2/gcd(q,2))`.

At this pair, the operator value has a closed form (proved by exact counting at that `(n,m)`):

- if `q` odd: `1 - 6/(2q-5) + 3(q-3)/(q-2)^2`,
- if `q` even: `1 - 6/(2q-5) + (3q-10)/(q-2)^2`.

Reference: `route2-consecutive-triple-extremizer.md`.

This value is strictly below the adjacent-pair maximum for every `q>=5`.

---

### Evidence tooling

- `two_point_operator_tools.py` prints the adjacent-pair and consecutive-triple closed forms.
- `route2_step2_check.py` enumerates primitive `Q` in `[q-window,q]` of sizes 3..6 and compares the worst found
  against the adjacent-pair benchmark.

Example:

`python C:\\Users\\z20ma\\OneDrive\\Documents\\!math\\erdos\\488\\route2_step2_check.py --q 200 --window 15 --min-size 3 --max-size 6 --m-mult 300`

returns worst `Q=[198,199,200]` and a positive gap to the adjacent-pair maximum.

---

### What remains (mathematical)

We still need a rigorous "tail compactness / consecutive extremality" theorem of the form:

`max O_Q <= max O_{Q3(q)}`  for all primitive `Q` with `|Q|>=3` and `max(Q)=q`,

or any other argument implying `max O_Q < O_{ {q-1,q} }^max`.

Working proof outline (unproved):

1) Show any near-extremal `Q` must live in a tiny top window near `q` (otherwise extra early multiples force
   `F(n)/n` too large to cancel, and `O_Q` falls to `1 - c/q` scale).
2) Conclude the unique `|Q|>=3` candidate in that top window is `Q3(q)={q-2,q-1,q}`.
3) Prove the global maximizer for `Q3(q)` is the closed-form pair above.
4) Compare its value to the adjacent-pair maximum.

