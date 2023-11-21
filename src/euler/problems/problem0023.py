"""
Project Euler Problem 23
========================

A perfect number is a number for which the sum of its proper divisors is
exactly equal to the number. For example, the sum of the proper divisors
of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect
number.

A number whose proper divisors are less than the number is called
deficient and a number whose proper divisors exceed the number is called
abundant.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the
smallest number that can be written as the sum of two abundant numbers is
24. By mathematical analysis, it can be shown that all integers greater
than 28123 can be written as the sum of two abundant numbers. However,
this upper limit cannot be reduced any further by analysis even though it
is known that the greatest number that cannot be expressed as the sum of
two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the
sum of two abundant numbers.
"""
from itertools import combinations_with_replacement
from euler.utils.factorization import is_abundant


def solution1() -> int:
    limit = 28123
    abundant = {n for n in range(12, limit) if is_abundant(n)}
    sums = {a + b for a, b in combinations_with_replacement(abundant, 2)}
    return sum(n for n in range(1, limit) if not n in sums)


def solution2() -> int:
    limit = 28123
    abundant = [n for n in range(12, limit) if is_abundant(n)]

    sums = [False] * (limit * 2)
    for i, a in enumerate(abundant):
        for b in abundant[i:]:
            sums[a + b] = True

    return sum(n for n in range(1, limit) if not sums[n])


if __name__ == "__main__":
    print(solution2())
