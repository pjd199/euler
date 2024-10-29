"""
Project Euler Problem 60
========================

The primes 3, 7, 109, and 673, are quite remarkable. By taking any two
primes and concatenating them in any order the result will always be
prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The
sum of these four primes, 792, represents the lowest sum for a set of four
primes with this property.

Find the lowest sum for a set of five primes for which any two primes
concatenate to produce another prime.
"""

from itertools import permutations

from euler.utils.primes import is_prime, sieve_of_eratosthenes


def check(primes: list[int]) -> bool:
    return all(is_prime(int(str(a) + str(b))) for a, b in permutations(primes, 2))


def solution60() -> int:
    primes = sieve_of_eratosthenes(10000)
    for a in primes:
        for b in primes:
            if b > a and check([a, b]):
                for c in primes:
                    if c > b and check([a, b, c]):
                        for d in primes:
                            if d > c and check([a, b, c, d]):
                                for e in primes:
                                    if e > d and check([a, b, c, d, e]):
                                        return sum([a, b, c, d, e])

    return -1


if __name__ == "__main__":
    print(solution60())
