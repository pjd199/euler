from collections.abc import Iterator
from functools import cache
from itertools import count
from math import ceil, sqrt


@cache
def is_prime(n: int) -> bool:
    if n <= 1:
        return False  # negative numbers, zero and one are not primes
    if n in (2, 3):
        return True  # two and three are primes
    if n % 2 == 0 or n % 3 == 0:
        return False  # check for simple divisors

    # now search for prime factors, using prime check in form of 6k +- 1
    return not any(
        n % f == 0 or n % (f + 2) == 0 for f in range(5, int(sqrt(n)) + 1, 6)
    )


def prime_generator(limit: int | None = None) -> Iterator[int]:
    # from https://eli.thegreenplace.net/2023/my-favorite-prime-number-generator/
    yield 2
    d = {}
    for q in count(3, step=2):
        p = d.pop(q, None)
        if not p:
            d[q * q] = q
            if limit is None or q <= limit:
                yield q
            else:
                return
        else:
            x = q + p + p  # get odd multiples
            while x in d:
                x += p + p
            d[x] = p


@cache
def sieve_of_eratosthenes(n: int) -> list[int]:
    # numpy has an import overhead, so only import when needed
    import numpy as np

    # n must be higher than the smallest prime number
    if n < 2:
        return []

    # find all the prime number up to n,
    # using the sieve of Eratosthenes. The sieve
    # will only look at odd numbers as 2 is the only
    # even prime number
    sieve = np.full((n - 1) // 2, True, dtype=np.bool_)
    sieve[0] = False

    # perform the sieving action
    for i in range((ceil(sqrt(n)) - 1) // 2):
        if sieve[i]:
            sieve[2 * i * (i + 1) :: 2 * i + 1] = False

    # return a list of prime numbers
    return [2] + [2 * i + 1 for i, x in enumerate(sieve) if x]
