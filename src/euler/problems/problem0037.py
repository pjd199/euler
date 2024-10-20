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

from itertools import islice

from euler.utils.digits import join_digits, split_digits
from euler.utils.primes import is_prime, prime_generator


def truncatable_prime(n: int) -> int:
    digits = split_digits(n)
    return all(
        is_prime(join_digits(tuple(digits[:i]))) for i in range(1, len(digits))
    ) and all(is_prime(join_digits(tuple(digits[-i:]))) for i in range(1, len(digits)))


def solution() -> int:
    return sum(
        islice(
            (x for x in islice(prime_generator(), 4, None) if truncatable_prime(x)), 11
        )
    )


if __name__ == "__main__":
    print(solution())
