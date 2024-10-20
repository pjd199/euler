"""
Project Euler Problem 7
=======================

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10001st prime number?
"""

from itertools import islice

from euler.utils.primes import prime_generator


def solution() -> int:
    return next(islice((x for x in prime_generator()), 10000, 10001))


if __name__ == "__main__":
    print(solution())
