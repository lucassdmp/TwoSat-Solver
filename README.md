# TwoSat SOLVER

## Logic Solver

Each Number represents an atomic formula.

A minus sign followed by a number represents the negation of that number.

Each line on **elems.txt** represents a formula, theres no need to write any logic OP.

Formulas must be written as followed:

|Formula|Elems.txt|
|:---:|:---:|
|<pre>P|<pre>1|
|<pre>Q|<pre>2|
|<pre>R|<pre>3|
|<pre>-P|<pre>-1|
|<pre>-Q|<pre>-2|
|<pre>-R|<pre>-3|
|<pre>P v Q|<pre>1 2|
| <pre> Q ^ (P v Q) ^ (-P V R)| <pre><code>2 <br>1 2 <br>-1 3 <code> |
# (A single space between elements and a single **ENTER** between formulas)
