from math import sqrt
from functools import cache
import numpy as np


@cache
def sieve_of_eratosthenes(n: int) -> list[int]:
    # find all the prime number up to n,
    # using the sieve of Eratosthenes
    sieve = np.full(n, True, dtype=np.bool_)
    sieve[0] = False
    sieve[1] = False
    sieve[4::2] = False  # the only even prime is 2

    # perform the sieving action
    for p in range(3, int(sqrt(len(sieve))) + 1, 2):
        if sieve[p]:
            sieve[p**2 :: p] = False
    # return a list of prime numbers
    return [i for i, x in enumerate(sieve) if x]


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