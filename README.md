# TwoSat SOLVER

## Logic Solver

Each Number represents an atomic formula.

A minus sign followed by a number represents the negation of that number.

Each line on **elems.txt** represents a formula, theres no need to write any logic OP.

Formulas must be written as followed:

|Formula|Elems.txt|
|:---:|:---:|
|P|1|
|Q|2|
|R|3|
|-P|-1|
|-Q|-2|
|-R|-3|
|P v Q|1 2|
| <pre> Q ^ (P v Q) ^ (-P V R)|<pre> 2 (\n) 1 2 (\n) -1 3|
# (A single space between elements and a single **ENTER** between formulas)
