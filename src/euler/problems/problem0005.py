"""
Project Euler Problem 5
=======================

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest number that is evenly divisible by all of the numbers
from 1 to 20?
"""

from itertools import count

from euler.utils.primes import sieve_of_eratosthenes


def check(n: int) -> bool:
    for i in range(1, 21):
        if n % i != 0:
            return False
    return True


def solution1() -> int:
    for i in count(2):
        if check(i):
            return i


def solution2() -> int:
    result = 1
    upper = 20
    for prime in sieve_of_eratosthenes(upper):
        for i in count(1):
            if prime ** (i + 1) > upper:
                result *= prime**i
                break

    return result


if __name__ == "__main__":
    print(solution2())
