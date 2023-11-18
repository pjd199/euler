"""Functions for finding factors."""
from functools import cache
from math import ceil, prod, sqrt

from euler.utils.prime_list import primes


@cache
def factors(n: int) -> set[int]:
    found = {1, n}
    for i in range(1, ceil(sqrt(n))):
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
def number_of_divisors(n: int) -> int:
    return prod(exp + 1 for (_, exp) in prime_factors_exp(n))
