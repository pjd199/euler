"""Functions for finding factors."""

from functools import cache
from math import floor, gcd, prod, sqrt
from random import randint

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


def pollard_rho_with_brent(n: int) -> int:
    if n % 2 == 0:
        return 2
    if n < 2:
        return n

    y = randint(1, n - 1)  # noqa: S311
    c = randint(1, n - 1)  # noqa: S311
    m = randint(1, n - 1)  # noqa: S311
    g = 1
    r = 1
    q = 1
    x = y
    ys = 0

    while g == 1:
        x = y
        for _ in range(r):
            y = (y * y + c) % n

        k = 0
        while k < r and g == 1:
            ys = y
            for _ in range(min(m, r - k)):
                y = (y * y + c) % n
                q = q * abs(x - y) % n
            g = gcd(q, n)
            k += m
        r *= 2

    if g == n:
        while True:
            ys = (ys * ys + c) % n
            g = gcd(abs(x - ys), n)
            if g > 1:
                break
    return g


@cache
def prime_factors_exp(n: int) -> tuple[tuple[int, int], ...]:
    factors: dict[int, int] = {}
    while n > 1:
        factor = pollard_rho_with_brent(n)
        if is_prime(factor):
            while n % factor == 0:
                n = n // factor
                factors[factor] = factors.get(factor, 0) + 1

    return tuple(sorted(factors.items()))


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
