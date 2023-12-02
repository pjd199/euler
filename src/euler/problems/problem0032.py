"""
Project Euler Problem 32
========================

We shall say that an n-digit number is pandigital if it makes use of all
the digits 1 to n exactly once; for example, the 5-digit number, 15234,
is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 * 186 = 7254, containing
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product
identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to
only include it once in your sum.
"""
from math import floor, log10, sqrt

from euler.utils.digits import pandigital


def solution1() -> int:
    return sum(
        {
            x * y
            for x in range(1, 100)
            for y in range(x, 2000)
            if pandigital(x, y, x * y)
            if floor(log10(x)) + floor(log10(y)) + floor(log10(x * y)) + 3 == 9
        }
    )


def solution2() -> int:
    return sum(
        {
            n
            for n in range(1, 10000)
            for i in range(2, floor(sqrt(n)) + 1)
            if n % i == 0
            if pandigital(n, i, n // i)
            if floor(log10(n)) + floor(log10(i)) + floor(log10(n // i)) + 3 == 9
        }
    )


if __name__ == "__main__":
    print(solution2())
