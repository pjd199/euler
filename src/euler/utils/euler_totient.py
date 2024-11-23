from functools import cache
from math import prod

from euler.utils.factorization import prime_factors_exp
from euler.utils.primes import is_prime


@cache
def totient(n: int) -> int:
    if is_prime(n):
        return n - 1
    return int(prod(p ** (e - 1) * (p - 1) for p, e in prime_factors_exp(n)))


@cache
def totients_sieve(limit: int) -> list[int]:
    # numpy has an import overhead, so only import when needed
    import numpy as np

    phi = np.arange(limit + 1)
    phi[0] = 1
    phi[1] = 1
    for i in range(2, limit + 1):
        if phi[i] == i:  # i is a prime number
            phi[i::i] = phi[i::i] * (i - 1) // i
    return list(phi)
