
# Python Education 2 - PCAP Certification

## Module 1: Modules, Packages, and PIP

- importing and using Python modules;
- using some of the most useful Python standard library modules;
- constructing and using Python packages;
- PIP (Python Installation Package) and how to use it to install and uninstall ready-to-use packages from PyPI.

### Importing Modules

**Decomposition** is the process of dividing the main parts of your program into smaller more manageable piece.

A **Python Module** is a file containing python definitions and statements, which can be later imported and used when necessary.

Modules must be **Imported** using the `import` *keyword*.

    import math
    import sys

    import math, sys

A **Namespace** is a space in which some names exist and the names don't conflict with each other. *Inside a certain namespace, each name must remain unique*.

If a module of a specified name **exists and is accessible**, Python imports its contents and the names defined in the module become known, but they don't enter your code's namespace.

Qualified Import

    import math
    print(math.sin(math.pi/2))
    > 1.0

Selective Import

    from math import sin, pi
    print(sin(pi/2))
    > 1.0

    # ANTI-PATTERN
    from math import *
    print(sin(pi/2))

Importing a module using the `*` keyword is dangerous and should be be avoided to prevent name conflicts.

Importing a module using the `as` keyword imports the module under a variant name, also known as **aliasing**. After importing a module as an alias, **the original module name becomes inaccessible and cannot be used**.

    import math as m
    print(m.sin(m.pi/2))
    > 1.0

    from math import pi as PI, sin as sine
    print(sine(PI/2))
    > 1.0

### Working with Standard Modules

Use the **`dir()`** to show all the names provided through a particular module.

#### The Math Modele

##### Trigonometry

sin(x) → the sine of x;
cos(x) → the cosine of x;
tan(x) → the tangent of x.

asin(x) → the arcsine of x;
acos(x) → the arccosine of x;
atan(x) → the arctangent of x.

pi → a constant with a value that is an approximation of π;
radians(x) → a function that converts x from degrees to radians;
degrees(x) → acting in the other direction (from radians to degrees)

sinh(x) → the hyperbolic sine;
cosh(x) → the hyperbolic cosine;
tanh(x) → the hyperbolic tangent;
asinh(x) → the hyperbolic arcsine;
acosh(x) → the hyperbolic arccosine;
atanh(x) → the hyperbolic arctangent.

##### Exponentiation

e → a constant with a value that is an approximation of Euler's number (e)
exp(x) → finding the value of ex;
log(x) → the natural logarithm of x
log(x, b) → the logarithm of x to base b
log10(x) → the decimal logarithm of x (more precise than log(x, 10))
log2(x) → the binary logarithm of x (more precise than log(x, 2))

pow(x, y) → finding the value of xy (mind the domains), this is *a unique built in function*

##### Math Module Functions

ceil(x) → the ceiling of x (the smallest integer greater than or equal to x)
floor(x) → the floor of x (the largest integer less than or equal to x)
trunc(x) → the value of x truncated to an integer (be careful - it's not an equivalent either of ceil or floor)
factorial(x) → returns x! (x has to be an integral and not a negative)
hypot(x, y) → returns the length of the hypotenuse of a right-angle triangle with the leg lengths equal to x and y (the same as sqrt(pow(x, 2) + pow(y, 2)) but more precise)

#### The Random Module



## Module 2: Strings, Strings and List Methods, and Exceptions

## Module 3: Object-Oriented Programming

## Module 4: Miscellaneous
