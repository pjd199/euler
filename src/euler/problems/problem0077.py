"""
Project Euler Problem 77
========================

It is possible to write ten as the sum of primes in exactly five different
ways:

7 + 3
5 + 5
5 + 3 + 2
3 + 3 + 2 + 2
2 + 2 + 2 + 2 + 2

What is the first value which can be written as the sum of primes in over
five thousand different ways?
"""

from functools import cache
from itertools import count

from euler.utils.primes import prime_generator


@cache
def summation(n: int, limit: int) -> int:
    if n == 0:
        return 1
    if n < 0:
        return 0
    return sum(summation(n - x, x) for x in prime_generator(limit + 1))


def solution0076() -> int:
    return next(i for i in count() if summation(i, i - 1) >= 5000)


if __name__ == "__main__":
    print(solution0076())
