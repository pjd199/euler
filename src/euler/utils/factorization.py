"""Functions for finding factors."""
from functools import cache
from math import floor, prod, sqrt

from euler.utils.prime_list import primes


@cache
def factors(n: int) -> set[int]:
    found = {1, n}
    for i in range(1, floor(sqrt(n)) + 1):
        if n % i == 0:
            found.add(i)
            found.add(n // i)
    return found


@cache
def prime_factors(n: int) -> list[int]:
    found = []
    prime_iter = iter(primes)
    while n > 1:
        prime = next(prime_iter)
        while n % prime == 0:
            found.append(prime)
            n //= prime
    return found


@cache
def prime_factors_exp(n: int) -> list[int]:
    found = []
    prime_iter = iter(primes)
    while n > 1:
        prime = next(prime_iter)
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
    return prod((f ** (exp + 1) - 1) / (f - 1) for (f, exp) in prime_factors_exp(n))


@cache
def proper_factors(n: int) -> set[int]:
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
