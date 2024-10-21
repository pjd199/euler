from collections import deque
from collections.abc import Iterator
from functools import cache
from itertools import takewhile
from math import ceil, sqrt

_sieve_cache = deque([2])
_sieve_data = {}
_sieve_location = 3


def _caching_prime_generator() -> Iterator[int]:
    # from https://eli.thegreenplace.net/2023/my-favorite-prime-number-generator/
    global _sieve_cache, _sieve_data, _sieve_location
    yield from _sieve_cache

    while True:
        p = _sieve_data.pop(_sieve_location, None)
        if not p:
            _sieve_data[_sieve_location**2] = _sieve_location
            _sieve_cache.append(_sieve_location)
            yield _sieve_location
        else:
            x = _sieve_location + p + p  # get odd multiples
            while x in _sieve_data:
                x += p + p
            _sieve_data[x] = p
        _sieve_location += 2


def prime_generator(n: int | None = None) -> Iterator[int]:
    if n is None:
        return _caching_prime_generator()
    return takewhile(lambda x: x <= n, _caching_prime_generator())


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
    for i in range((ceil(sqrt(n))) // 2):
        if sieve[i]:
            sieve[2 * i * (i + 1) :: 2 * i + 1] = False

    # return a list of prime numbers
    return [2] + [2 * i + 1 for i, x in enumerate(sieve) if x]


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
