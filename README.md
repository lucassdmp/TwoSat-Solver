# TwoSat SOLVER

## Logic Solver

Each Number represents an atomic formula.

A minus sign followed by a number represents the negation of that number.

Each line on **elems.txt** represents a formula, theres no need to write any logic OP.

Formulas must be written as followed:

|Formula|Elems.txt|
|:---:|:---:|
|<code>P<code>|<code>1<code>|
|<code>Q<code>|<code>2<code>|
|<code>R<code>|<code>3<code>|
|<code>-P<code>|<code>-1<code>|
|<code>-Q<code>|<code>-2<code>|
|<code>-R<code>|<code>-3<code>|
|<code>P v Q<code>|<code>1 2<code>|
|<code>Q ^ (P v Q) ^ (-P V R)<code>| <code>2 <br>1 2 <br>-1 3 <code> |
# (A single space between elements and a single **ENTER** between formulas)
