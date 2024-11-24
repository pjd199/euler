"""
Project Euler Problem 71
========================

Consider the fraction, n/d, where n and d are positive integers. If n < d
and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d 8 in ascending order
of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3,
                       5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that 2/5 is the fraction immediately to the left of 3/7.

By listing the set of reduced proper fractions for d 1,000,000 in
ascending order of size, find the numerator of the fraction immediately to
the left of 3/7.
"""

from fractions import Fraction
from itertools import pairwise

from euler.utils.sequences import farey


def solution0071() -> int:
    limit = 1000000
    start = 8

    right = Fraction(3, 7)
    left = next(a for a, b in pairwise(farey(start)) if b == right)

    limit = 1000000
    for _ in range(start + 1, limit):
        mediant = Fraction(
            left.numerator + right.numerator,
            left.denominator + right.denominator,
        )
        if mediant.denominator <= limit:
            left = mediant
    return left.numerator


if __name__ == "__main__":
    print(solution0071())
