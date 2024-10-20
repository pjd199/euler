"""
Project Euler Problem 46
========================

It was proposed by Christian Goldbach that every odd composite number can
be written as the sum of a prime and twice a square.

9 = 7 + 2 * 1^2
15 = 7 + 2 * 2^2
21 = 3 + 2 * 3^2
25 = 7 + 2 * 3^2
27 = 19 + 2 * 2^2
33 = 31 + 2 * 1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a
prime and twice a square?
"""

from itertools import count
from math import sqrt

from euler.utils.primes import is_prime, prime_generator


def is_goldbach(n: int) -> bool:
    return any(
        (n - p >= 0) and sqrt((n - p) / 2).is_integer() for p in prime_generator(n)
    )


def solution() -> int:
    return next(
        x
        for x in filter(lambda n: not is_prime(n), count(3, step=2))
        if not is_goldbach(x)
    )


if __name__ == "__main__":
    print(solution())
