"""
Project Euler Problem 41
========================

We shall say that an n-digit number is pandigital if it makes use of all
the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital
and is also prime.

What is the largest n-digit pandigital prime that exists?
"""

from itertools import permutations

from euler.utils.primes import is_prime


def solution() -> int:
    pandigitals = [
        int("".join(x)) for r in range(1, 10) for x in permutations("7654321", r)
    ]
    return max(x for x in pandigitals if is_prime(x))


if __name__ == "__main__":
    print(solution())
