# TwoSat SOLVER

## How to use it:

#### The first line represents the number of atoms followed by the number of formulas



#### Each Number represents an atomic formula.



#### A minus sign followed by a number represents the negation of that formula.


#### Each line on **elems.txt** represents a formula, theres no need to write any logic OP.

## Formulas must be written as followed:

|Formula|Elems.txt|
|:---:|:---:|
|P|1|
|Q|2|
|R|3|
|-P|-1|
|-Q|-2|
|-R|-3|
|P v Q|1 2|
| <pre>(P v Q) ^ (-P V R)| <pre> 1 2 **(ENTER)** -1 3|


## (A single space between elements and a single **ENTER** between formulas)

### File Example
<pre>
 4 4
-1 2
 5 -2
 3 -1
 4 -5