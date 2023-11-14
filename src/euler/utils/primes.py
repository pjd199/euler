from functools import cache
from math import ceil, sqrt

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
    for i in range(0, (ceil(sqrt(n)) - 1) // 2):
        if sieve[i]:
            sieve[2 * i * (i + 1) :: 2 * i + 1] = False

    # return a list of prime numbers
    return [2] + [2 * i + 1 for i, x in enumerate(sieve) if x]


def prime_iterator():
    # yield from the cached primes
    primes = sieve_of_eratosthenes(1000)
    next_index = 0
    while True:
        yield from primes[next_index:]
        next_index = len(primes)
        primes = sieve_of_eratosthenes(primes[-1] * 2)


def is_prime(n: int) -> bool:
    if n <= 1:
        return False  # negative numbers, zero and one are not primes
    if n in (2, 3):
        return True  # two and three are primes
    if n % 2 == 0 or n % 3 == 0:
        return False  # check for simple divisors

    # now search for prime factors, using prime check in form of 6k +- 1
    if any(n % f == 0 or n % (f + 2) == 0 for f in range(5, int(sqrt(n)) + 1, 6)):
        return False

    return True
