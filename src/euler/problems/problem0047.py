"""
Project Euler Problem 47
========================

The first two consecutive numbers to have two distinct prime factors are:

14 = 2 * 7
15 = 3 * 5

The first three consecutive numbers to have three distinct prime factors
are:

644 = 2^2 * 7 * 23
645 = 3 * 5 * 43
646 = 2 * 17 * 19.

Find the first four consecutive integers to have four distinct primes
factors. What is the first of these numbers?
"""

from itertools import count

from euler.utils.factorization import prime_factors


def solution() -> int:
    return next(
        x
        for x in count(1)
        if len(prime_factors(x)) == 4
        and len(prime_factors(x + 1)) == 4
        and len(prime_factors(x + 2)) == 4
        and len(prime_factors(x + 3)) == 4
    )


if __name__ == "__main__":
    print(solution())
