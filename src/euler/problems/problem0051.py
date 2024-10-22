"""
Project Euler Problem 51
========================

By replacing the 1st digit of *57, it turns out that six of the possible
values: 157, 257, 457, 557, 757, and 857, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this
5-digit number is the first example having seven primes, yielding the
family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently
56003, being the first member of this family, is the smallest prime with
this property.

Find the smallest prime which, by replacing part of the number (not
necessarily adjacent digits) with the same digit, is part of an eight
prime value family.
"""

from itertools import product
from math import ceil, log10

from euler.utils.primes import sieve_of_eratosthenes


def solution() -> int:
    primes = set(sieve_of_eratosthenes(1000000))
    target_family_length = 8

    for prime in primes:
        length = ceil(log10(prime))
        for mask in product("01", repeat=length):
            family = set()
            for digit in range(10):
                subbed = int(
                    "".join(
                        n if m == "0" else str(digit)
                        for (n, m) in zip(str(prime), mask)
                    )
                )
                if subbed in primes and 10 ** (length - 1) <= subbed <= 10**length:
                    family.add(subbed)

            if len(family) == target_family_length:
                return min(family)
    return -1


if __name__ == "__main__":
    print(solution())
