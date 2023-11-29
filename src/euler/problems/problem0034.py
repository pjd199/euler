"""
Project Euler Problem 34
========================

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of
their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""
from math import factorial

from euler.utils.digits import split_digits


def solution1() -> int:
    return sum(
        n
        for n in range(3, 50000)
        if sum(factorial(digit) for digit in split_digits(n)) == n
    )


if __name__ == "__main__":
    print(solution1())
