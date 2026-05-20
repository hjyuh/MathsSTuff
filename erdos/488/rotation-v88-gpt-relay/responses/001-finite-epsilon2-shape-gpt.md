Output C: weaker finite skeleton theorem

I cannot prove bounded normalized diameter from the stated hypotheses alone. What does follow rigorously is a finite skeleton reduction: every deletion-minimal ϵ=2 core has at most two units of “topological complexity” outside ordinary degree-2 chains.

This strictly advances the classification but leaves one precise missing lemma: bounding the lengths of the ordinary chains.

Theorem: two-unit skeleton theorem

Let C be a connected induced deletion-minimal high-defect core in the normalized four-ratio graph.

Assume:

ϵ(C)=2,

and for every vertex v∈C,

ϵ(C∖{v})≤1.

Let

H=B
n
	​

(C,q).

For each vertex v, define:

d
v
	​

=deg
H
	​

(v),
c
v
	​

=#connected components of H−v,
t
v
	​

=#triple triangles containing v.

Define the cut excess

κ(C)=
v∈C
∑
	​

(c
v
	​

−1),

and the local surplus

σ
v
	​

=d
v
	​

−c
v
	​

−t
v
	​

−1.

Then

τ(C)+κ(C)+
v∈C
∑
	​

σ
v
	​

=2
	​


with

σ
v
	​

≥0for every v.
	​


Consequently:

τ(C)≤2,
	​

κ(C)≤2−τ(C),
	​


and the number of non-ordinary terminal vertices is at most

2+2τ(C)≤6.
	​


After suppressing all maximal paths whose internal vertices satisfy

t
v
	​

=0,c
v
	​

=1,d
v
	​

=2,

the resulting multigraph skeleton has at most

6 vertices and 9 chain-slots.
	​


Thus the remaining infinite part of the classification, if any, can only come from unbounded lengths of ordinary induced degree-2 chains.

Proof

For a disconnected graph G, write

β(G)=∣E(G)∣−∣V(G)∣+comp(G)

for total cyclomatic number.

Since C is connected and ϵ(C)=2,

ϵ(C)=β(H)−τ(C)=2.

Hence

β(H)=τ(C)+2.

Because H is connected,

β(H)=∣E(H)∣−∣V(H)∣+1.

Therefore

∣E(H)∣=∣V(H)∣+τ(C)+1.

Now delete a vertex v. The edge count drops by d
v
	​

, the vertex count drops by 1, and the number of connected components becomes c
v
	​

. Hence

β(H−v)=(∣E∣−d
v
	​

)−(∣V∣−1)+c
v
	​

=β(H)−d
v
	​

+c
v
	​

.

A triple fiber is exactly a triangle of the form {L/3,L/4,L/5}, and the normalized four-ratio graph has no K
4
	​

. Thus deleting v removes exactly the triple triangles containing v, and creates no new triple triangle. Therefore

τ(C∖{v})=τ(C)−t
v
	​

.

So

ϵ(C∖{v})=β(H−v)−τ(C∖{v})
=(β(H)−d
v
	​

+c
v
	​

)−(τ(C)−t
v
	​

)
=(β(H)−τ(C))−d
v
	​

+c
v
	​

+t
v
	​

=2−d
v
	​

+c
v
	​

+t
v
	​

.

Deletion-minimality gives

ϵ(C∖{v})≤1.

Therefore

2−d
v
	​

+c
v
	​

+t
v
	​

≤1,

so

d
v
	​

−c
v
	​

−t
v
	​

≥1.

Equivalently,

σ
v
	​

=d
v
	​

−c
v
	​

−t
v
	​

−1≥0.
	​


Now sum over all vertices:

v
∑
	​

σ
v
	​

=
v
∑
	​

d
v
	​

−
v
∑
	​

c
v
	​

−
v
∑
	​

t
v
	​

−∣V∣.

We have

v
∑
	​

d
v
	​

=2∣E∣,

and since every triple triangle has exactly three vertices,

v
∑
	​

t
v
	​

=3τ.

Also

v
∑
	​

c
v
	​

=
v
∑
	​

(1+(c
v
	​

−1))=∣V∣+κ.

Thus

v
∑
	​

σ
v
	​

=2∣E∣−(∣V∣+κ)−3τ−∣V∣.

Using

∣E∣=∣V∣+τ+1,

we get

v
∑
	​

σ
v
	​

=2(∣V∣+τ+1)−∣V∣−κ−3τ−∣V∣
=2−τ−κ.

Therefore

τ+κ+
v
∑
	​

σ
v
	​

=2.
	​


This proves the theorem.

Finite skeleton consequence

Call a vertex ordinary if

t
v
	​

=0,c
v
	​

=1,σ
v
	​

=0.

For an ordinary vertex,

σ
v
	​

=d
v
	​

−c
v
	​

−t
v
	​

−1=d
v
	​

−2,

so

d
v
	​

=2.

Thus every ordinary vertex is a non-cut, non-triple, degree-2 vertex.

Let T be the set of non-ordinary vertices. Then T is contained in the union of:

vertices lying in triple triangles;

cut-excess vertices with c
v
	​

>1;

surplus vertices with σ
v
	​

>0.

The number of vertices in triple triangles is at most

3τ.

The number of cut-excess vertices is at most

κ.

The number of surplus vertices is at most

v
∑
	​

σ
v
	​

.

Therefore

∣T∣≤3τ+κ+
v
∑
	​

σ
v
	​

=3τ+(2−τ)=2+2τ.

Since τ≤2,

∣T∣≤6.
	​


Now suppress every maximal path whose internal vertices are ordinary. Suppression preserves cyclomatic number. The skeleton has

V
skel
	​

≤6

and

β
skel
	​

=β(H)=τ+2.

For a connected multigraph,

E
skel
	​

=V
skel
	​

+β
skel
	​

−1.

Thus

E
skel
	​

≤(2+2τ)+(τ+2)−1=3+3τ.

Since τ≤2,

E
skel
	​

≤9.
	​


So there are finitely many possible skeletons. The only unbounded data not controlled by this theorem are the lengths and embeddings of the ordinary degree-2 chains.

Regression consistency
theta13

For the full theta13 core,

∣V∣=13,∣E∣=14,β=14−13+1=2.

There are no triple triangles:

τ=0.

Hence

ϵ=2.

The deletion data are:

κ=0,
v
∑
	​

σ
v
	​

=2.

So

τ+κ+
v
∑
	​

σ
v
	​

=0+0+2=2.

The two surplus vertices are the two degree-3 branch vertices. This is the ordinary theta-type case.

Kimi obstruction

The full Kimi set is not deletion-minimal, but it contains the deletion-minimal induced core

C
0
	​

={216,240,243,256,270,288,320,324,360,384,405}.

For this core,

∣V∣=11,∣E∣=13,

so

β=13−11+1=3.

There is one triple triangle:

{216,270,360},L=1080.

Thus

τ=1,

and

ϵ=β−τ=3−1=2.

Deletion-minimality holds: deleting 216 gives ϵ=0, and deleting any other vertex gives ϵ=1.

The theorem gives

κ=0,
v
∑
	​

σ
v
	​

=1.

Therefore

τ+κ+
v
∑
	​

σ
v
	​

=1+0+1=2.

So Kimi fits the τ=1 skeleton case: one triple triangle plus one surplus unit.

v56 near-miss

The full v56 set contains the deletion-minimal induced core

C
0
	​

={35760,36207,38144,40230,42912,44700,47680,48276,53640,57216,60345,64368,67050}.

For this core,

∣V∣=13,∣E∣=14,

so

β=14−13+1=2.

There are no triple triangles:

τ=0.

Hence

ϵ=2.

Deletion-minimality holds: deleting 35760 or 40230 gives ϵ=0, and deleting any other vertex gives ϵ=1.

The theorem gives

κ=0,
v
∑
	​

σ
v
	​

=2.

Therefore

τ+κ+
v
∑
	​

σ
v
	​

=0+0+2=2.

So v56 has the same theta-type skeleton as theta13.

Exact remaining failure point

The finite shape lemma is now reduced to the following missing lemma.

Missing chain-length lemma

Let P be a maximal induced path in a normalized deletion-minimal ϵ=2 core whose internal vertices are ordinary, i.e.

t
v
	​

=0,c
v
	​

=1,d
v
	​

=2.

One needs to prove that every such P has bounded normalized length, or at least that P must be a shortest admissible path between its terminal endpoints in the normalized four-ratio graph.

The natural replacement proof fails as follows.

Suppose P is not shortest and there is a shorter normalized four-ratio path P
′
 between the same endpoints. Replacing P by P
′
 might produce a smaller ϵ=2 core, but deletion-minimality does not permit replacements. It only says that deleting a vertex from the existing core lowers ϵ to at most 1. It gives no contradiction from the existence of a shorter external path.

Moreover, P
′
 may introduce new chords or new triple triangles, changing both β and τ. Thus the “shortest connecting path” mechanism requires an additional replacement-minimality lemma, not just deletion-minimality.

So the current exact state is:

finite skeletons proved; bounded chain lengths still missing.
	​
