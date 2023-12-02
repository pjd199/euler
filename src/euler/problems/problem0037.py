"""
Project Euler Problem 37
========================

The number 3797 has an interesting property. Being prime itself, it is
possible to continuously remove digits from left to right, and remain
prime at each stage: 3797, 797, 97, and 7. Similarly we can work from
right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left
to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""
from functools import cache
from euler.utils.digits import split_digits, join_digits
from euler.utils.prime_list import primes


@cache
def is_prime(*args: int) -> bool:
    return join_digits(args) in primes


def solution1() -> int:
    total = 0
    for prime in primes[4:]:
        digits = split_digits(prime)
        if all(is_prime(*digits[:i]) for i in range(1, len(digits))) and all(
            is_prime(*digits[-i:]) for i in range(1, len(digits))
        ):
            total += prime
    return total


if __name__ == "__main__":
    print(solution1())
