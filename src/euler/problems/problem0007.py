"""
Project Euler Problem 7
=======================

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10001st prime number?
"""
from itertools import islice, count

from euler.utils.primes import prime_iterator, is_prime


def solution1() -> int:
    return next(islice(prime_iterator(), 10000, 10001))

def solution2() -> int:
    found = 0
    for i in count(1, 2):
        if is_prime(i):
            found += 1
        if found == 10000:
            return i

if __name__ == "__main__":
    print(solution1())
