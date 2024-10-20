"""
Project Euler Problem 35
========================

The number, 197, is called a circular prime because all rotations of the
digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37,
71, 73, 79, and 97.

How many circular primes are there below one million?
"""

from collections import deque

from euler.utils.digits import join_digits, split_digits
from euler.utils.primes import is_prime, sieve_of_eratosthenes


def circular_prime(n: int) -> bool:
    digits = deque(split_digits(n))
    if n != 2 and any(x % 2 == 0 for x in digits):
        return False
    for _ in range(len(digits)):
        if not is_prime(join_digits(tuple(digits))):
            return False
        digits.rotate(1)
    return True


def solution() -> int:
    return sum(1 for n in sieve_of_eratosthenes(1000000) if circular_prime(n))


if __name__ == "__main__":
    print(solution())
