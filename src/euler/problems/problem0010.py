"""
Project Euler Problem 10
========================

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

from euler.utils.primes import sieve_of_eratosthenes


def solution() -> int:
    return sum(sieve_of_eratosthenes(2000000))


if __name__ == "__main__":
    print(solution())
