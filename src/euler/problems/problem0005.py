"""
Project Euler Problem 5
=======================

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest number that is evenly divisible by all of the numbers
from 1 to 20?
"""

from itertools import count

from euler.utils.primes import prime_generator


def check(n: int) -> bool:
    return all(n % i == 0 for i in range(2, 21))


def solution1() -> int:
    return next(i for i in count(2) if check(i))


def solution2() -> int:
    result = 1
    upper = 21
    for prime in prime_generator(upper):
        for i in count(1):
            if prime ** (i + 1) > upper:
                result *= prime**i
                break

    return result


if __name__ == "__main__":
    print(solution2())
