"""
Define a function that can compute a Fibonacci number for any given index, using Binet's Formula.

This file can be run as a script, wherein it prints a statement giving the 50th Fibonacci number.

This file can also be imported as a module, for which the following objects are defined:

    Values
    ------
    phi: (float)
        An approximation of the golden ratio, the largest solution to x^2-x-1.

    Functions
    ---------
    fibonacci:
        Accepts an integer n, and returns an integer equal to the n-th Fibonacci number.

    Modules
    -------
    math:
        The math module of the Python Standard Library.
"""

import math

phi = (1 + math.sqrt(5))/2

def fibonacci(n):
    """Return the n-th Fibonacci number."""
    return round((phi**n - (-phi**(-n))) / math.sqrt(5))

if __name__ == '__main__':
    n = 50
    print('The Fibonacci number at index', n, 'is equal to', fibonacci(n), '.')