"""Functions for finding factors."""

from functools import cache
from math import floor, prod, sqrt

from euler.utils.primes import is_prime, prime_generator


@cache
def factors(n: int) -> frozenset[int]:
    found = {1, n}
    for i in range(1, floor(sqrt(n)) + 1):
        if n % i == 0:
            found.add(i)
            found.add(n // i)
    return frozenset(found)


@cache
def prime_factors(n: int) -> frozenset[int]:
    if is_prime(n):
        return frozenset({n})
    if n > 1:
        for x in prime_generator(n // 2):
            if n % x == 0:
                return frozenset({x, *prime_factors(n // x)})
    return frozenset()


@cache
def prime_factors_exp(n: int) -> list[tuple[int, int]]:
    found: list[tuple[int, int]] = []
    primes = prime_generator()
    while n > 1:
        prime = next(primes)
        exp = 0
        while n % prime == 0:
            exp += 1
            n //= prime
        if exp > 0:
            found.append((prime, exp))
    return found


@cache
def number_of_factors(n: int) -> int:
    return prod(exp + 1 for (_, exp) in prime_factors_exp(n))


@cache
def sum_of_factors(n: int) -> int:
    return int(
        prod((f ** (exp + 1) - 1) // (f - 1) for (f, exp) in prime_factors_exp(n))
    )


@cache
def proper_factors(n: int) -> frozenset[int]:
    return factors(n) - {n}


@cache
def is_perfect(n: int) -> bool:
    return n == sum(proper_factors(n))


@cache
def is_deficient(n: int) -> bool:
    return sum(proper_factors(n)) < n


@cache
def is_abundant(n: int) -> bool:
    return sum(proper_factors(n)) > n
