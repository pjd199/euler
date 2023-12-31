"""
Project Euler Problem 7
=======================

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10001st prime number?
"""
from euler.utils.prime_list import primes


def solution1() -> int:
    return primes[10000]


if __name__ == "__main__":
    print(solution1())
